#!/usr/bin/env python3
"""
S85 W1a-7: LISA-FLAGSHIP-FIX-TIGHTENING (W6 D.2)
================================================

Gate: S85-W1a-LISA-FLAGSHIP-FIX-TIGHTENING
Trigger: [VERIFY]
Classification: META (tightens pre-registration boundaries)
Agent: mack-cosmic-bridge

Hypothesis: The S84 LISA pre-registration falsification window
[h_c^(A)/10, 10*h_c^(A)] is tightenable to approximately
[h_c^(A)/1.19, 1.19*h_c^(A)] using the W1a-6 fix-k/fix-f consistency
as internal error budget. A tighter window makes LISA DECISIVE rather
than merely consistent (SNR >= 5 at 3-sigma band).

Substitution chain (Python-verified):
  Step 1: Error budget components (plan §W1a-7 §7):
            sigma_fix_kf = 1e-3   (from W1a-6 PASS)
            sigma_cS     = 5e-2   (canonical-constants provenance for c_S)
            sigma_transit = 2e-2  (S65 NT-BLUE-65)
  Step 2: Quadrature: sigma_total = sqrt(sum sigma_i^2)
          = sqrt(1e-6 + 2.5e-3 + 4e-4)
          = sqrt(2.901e-3)
          = 0.05386 (5.39%)
  Step 3: 3-sigma tightening factors:
          factor_up = 1 + 3*sigma_total = 1.1616
          factor_dn = 1 - 3*sigma_total = 0.8384
          (Plan §W1a-7 computes ~1.19 either way -- within 2% of our
           full-quadrature 1.16.)
  Step 4: h_c^(A) / h_n_LISA at f_pivot = 3 mHz = 10^11 (S84 W6-50).
          Downshifted by factor_up: h_c_tight / h_n = 10^11 / 1.1616
                                                    = 8.61e10.
  Step 5: SNR^2 integrated over LISA band:
          band: 10% of f_pivot, i.e., df = 3e-4 Hz
          T_mission = 4 years = 1.2623e8 s
          N_bins = df * T_mission = 3.79e4 (log-spaced bins)
          SNR^2 = (h_c/h_n)^2 * N_bins = (8.61e10)^2 * 3.79e4
                = 2.81e26
          SNR  = sqrt(2.81e26) = 1.68e13
  Step 6: Compare to PASS threshold (SNR >= 5):
          1.68e13 >> 5   ==> PASS
  Direction: Even 3-sigma downshift cannot erode the 11-OOM amplitude
             margin provided by S84 W6-50. LISA becomes DECISIVE, not
             merely consistent, for the framework CGWB-PT prediction.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-85/s85_w1a_cf_m4_lisa_flagship.npz (W1a-6 output)
  - computations/session-84/s84_w6_50_cgwb_pt.py (if present)
  - script bytes

Output 4-tuple:
  (value=<SNR_at_3sigma_band>, scheme=fix-k-dominant, convention=LISA-SRD-v3, L_max=10)

Thresholds (pre-registered, plan §W1a-7):
  - PASS iff SNR_LISA_at_3sigma >= 5.
  - FAIL iff SNR < 1.
  - INFO iff 1 <= SNR < 5.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import c_Gold  # noqa: E402 (documented in W1a-6 as substrate sound speed)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1a-LISA-FLAGSHIP-FIX-TIGHTENING"                    # (local)
SCHEME = "fix-k-dominant"                                           # (local)
CONVENTION = "LISA-SRD-v3"                                          # (local)
L_MAX = 10                                                          # (local)

# Error-budget components (plan §W1a-7 §7, FROZEN)
SIGMA_FIX_KF = 1e-3                                                 # (local) from W1a-6 PASS
SIGMA_CS = 5e-2                                                     # (local) c_S canonical-constants provenance
SIGMA_TRANSIT = 2e-2                                                # (local) S65 NT-BLUE-65

# Amplitude margin from S84 W6-50 (h_c^(A) / h_n_LISA at f_pivot)
H_C_OVER_HN_S84 = 1e11                                              # (local) S84 W6-50 canonical margin

# LISA pivot + mission
F_PIVOT = 3e-3                                                      # (local) Hz, LISA SRD-v3
T_MISSION_YEARS = 4.0                                               # (local) LISA nominal mission
BANDWIDTH_FRAC = 0.1                                                # (local) 10% of pivot

# Pre-registered thresholds (plan §W1a-7 §9)
PASS_SNR = 5.0                                                      # (local) DECISIVE threshold
FAIL_SNR = 1.0                                                      # (local) below => not useful

OUT_NPZ = SCRIPT_DIR / "s85_w1a_lisa_flagship_tightening.npz"
OUT_PNG = SCRIPT_DIR / "s85_w1a_lisa_flagship_tightening.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
W1A_6_NPZ = SCRIPT_DIR / "s85_w1a_cf_m4_lisa_flagship.npz"
W6_50_PY = SCRIPT_DIR / "s84_w6_50_cgwb_pt.py"

INPUT_FILES = [CANON_PY]
for extra in (W1A_6_NPZ, W6_50_PY):
    if extra.exists():
        INPUT_FILES.append(extra)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def compute() -> dict:
    # Quadrature sum
    sig_total = float(np.sqrt(SIGMA_FIX_KF ** 2
                              + SIGMA_CS ** 2
                              + SIGMA_TRANSIT ** 2))                # (local)
    factor_up = 1.0 + 3.0 * sig_total                               # (local)
    factor_dn = 1.0 - 3.0 * sig_total                               # (local)

    # Downshifted strain ratio at LISA pivot
    h_c_over_hn_tight = H_C_OVER_HN_S84 / factor_up                 # (local)

    # Integrated SNR across LISA band
    T_mission_s = T_MISSION_YEARS * 365.25 * 24.0 * 3600.0          # (local)
    df_band = BANDWIDTH_FRAC * F_PIVOT                              # (local)
    N_bins = df_band * T_mission_s                                  # (local)
    SNR_squared = (h_c_over_hn_tight ** 2) * N_bins                 # (local)
    SNR = float(np.sqrt(SNR_squared))                               # (local)

    return {
        "value": SNR,
        "sigma_total": sig_total,
        "factor_up": factor_up,
        "factor_dn": factor_dn,
        "h_c_over_hn_tight": h_c_over_hn_tight,
        "h_c_over_hn_S84": H_C_OVER_HN_S84,
        "T_mission_s": T_mission_s,
        "df_band": df_band,
        "N_bins": N_bins,
        "SNR": SNR,
        "SNR_squared": SNR_squared,
        "sigma_components": {
            "fix_kf": SIGMA_FIX_KF,
            "cS": SIGMA_CS,
            "transit": SIGMA_TRANSIT,
        },
    }


def evaluate_gate(res: dict) -> str:
    snr = res["SNR"]                                                # (local)
    if snr >= PASS_SNR:
        return "PASS"
    if snr < FAIL_SNR:
        return "FAIL"
    return "INFO"


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


def make_plot(res: dict, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.6))             # (local)

    # Panel A: error-budget decomposition
    ax = axes[0]
    labels = ["fix-k/f\n(W1a-6)", "c_S\n(canonical)", "transit\n(NT-BLUE-65)", "TOTAL\n(quad sum)"]
    vals = [res["sigma_components"]["fix_kf"], res["sigma_components"]["cS"],
            res["sigma_components"]["transit"], res["sigma_total"]]
    colors = ["#1a5fb4", "#b06530", "#b03030", "#333333"]
    ax.bar(labels, vals, color=colors, alpha=0.85)
    for i, v in enumerate(vals):
        ax.text(i, v * 1.08, f"{v:.4f}", ha="center", fontsize=9)
    ax.set_ylabel(r"1-$\sigma$ component")
    ax.set_title(rf"Quadrature: $\sigma$_total = {res['sigma_total']:.4f}")
    ax.grid(True, alpha=0.25, axis="y")

    # Panel B: tightened window vs LISA noise
    ax = axes[1]
    # Conceptual: h_c band [h_c/factor_up, factor_up*h_c] relative to h_n=1
    h_c_center = res["h_c_over_hn_S84"]
    h_c_up = h_c_center * res["factor_up"]
    h_c_dn = h_c_center * res["factor_dn"]
    ax.axhspan(h_c_dn, h_c_up, color="#2a7a2a", alpha=0.35,
               label=f"3σ tightened band: [{h_c_dn:.3e}, {h_c_up:.3e}] h_n")
    ax.axhline(h_c_center, color="#1a5fb4", lw=2.0,
               label=rf"$h_c^{{(A)}}/h_n$ = {h_c_center:.3e} (S84)")
    ax.axhline(1.0, color="#b03030", lw=1.5, ls=":",
               label="LISA noise (h_n = 1)")
    ax.axhline(5.0, color="#773300", lw=1.0, ls="--",
               label=f"SNR_bin PASS floor (5)")
    ax.set_yscale("log")
    ax.set_ylabel(r"$h_c / h_n$ at $f_{pivot}$")
    ax.set_xticks([])
    ax.set_title(rf"Integrated SNR = {res['SNR']:.2e} (PASS >= {PASS_SNR})")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.25, which="both")

    fig.suptitle(f"{GATE_ID}: LISA becomes DECISIVE via 3-sigma tightening")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: sigma components = (fix_kf={SIGMA_FIX_KF}, cS={SIGMA_CS}, transit={SIGMA_TRANSIT})")
    print(f"  Step 2: sigma_total = sqrt(sum^2) = {res['sigma_total']:.6f}")
    print(f"  Step 3: 3-sigma factors: up={res['factor_up']:.4f}, down={res['factor_dn']:.4f}")
    print(f"  Step 4: h_c/h_n (S84 W6-50) = {H_C_OVER_HN_S84:.0e}")
    print(f"          Downshifted by factor_up: h_c_tight/h_n = {res['h_c_over_hn_tight']:.3e}")
    print(f"  Step 5: T_mission = {res['T_mission_s']:.3e} s, df_band = {res['df_band']:.3e} Hz")
    print(f"          N_bins = df * T = {res['N_bins']:.3e}")
    print(f"          SNR^2 = (h_c_tight/h_n)^2 * N_bins = {res['SNR_squared']:.3e}")
    print(f"          SNR = {res['SNR']:.3e}")
    print(f"  Step 6: Thresholds: PASS >= {PASS_SNR}, FAIL < {FAIL_SNR}")
    print(f"          {res['SNR']:.3e} >= {PASS_SNR} ==> {verdict}")
    print()

    np.savez(
        OUT_NPZ,
        SNR=np.float64(res["SNR"]),
        SNR_squared=np.float64(res["SNR_squared"]),
        sigma_total=np.float64(res["sigma_total"]),
        factor_up=np.float64(res["factor_up"]),
        factor_dn=np.float64(res["factor_dn"]),
        h_c_over_hn_S84=np.float64(res["h_c_over_hn_S84"]),
        h_c_over_hn_tight=np.float64(res["h_c_over_hn_tight"]),
        T_mission_s=np.float64(res["T_mission_s"]),
        df_band=np.float64(res["df_band"]),
        N_bins=np.float64(res["N_bins"]),
        sigma_fix_kf=np.float64(SIGMA_FIX_KF),
        sigma_cS=np.float64(SIGMA_CS),
        sigma_transit=np.float64(SIGMA_TRANSIT),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["SNR"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["SNR"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
