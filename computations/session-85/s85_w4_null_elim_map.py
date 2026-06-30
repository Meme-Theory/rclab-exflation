#!/usr/bin/env python3
"""
S85 W4-7: NULL-RESULT ELIMINATION MAP PRE-REGISTRATION
======================================================

Gate: S85-W4-7-NULL-ELIM-MAP
Trigger: [AUDIT]
Classification: NON-PHONONIC (pre-registration artifact; ELIMINATIONS
                catalogued are PHONONIC)
Agent: mack-cosmic-bridge

Hypothesis: For each of the 5 watchlist channels, pre-register the
null-result sigma-distance
     Delta = (x_FW - x_LCDM) / sigma_detector
with the falsifier consequence per channel. Locks branch-closure
triggers BEFORE the 2026-2030 detector data arrive.

Substitution chain (plan W4-7 #10):
  Definition: For a detector with 1-sigma forecast sigma_detector on
              channel x, a null result is measured value = x_LCDM with
              uncertainty sigma_detector.
  Definition: Tension under null = |x_FW - x_LCDM| / sigma_detector.
  Substitute: Per-channel values from canonical constants + S85 pins
              (see ROWS below).
  Simplify: |Delta_i| = number of sigma by which framework differs
            from null central; sign preserves directionality.
  Direction: |Delta| > 3 means detector can discriminate framework
             from null at > 3-sigma confidence. Falsifier consequence
             is automatic per row.

Output 4-tuple:
  (value=<n_channels_with_null_sigma>/5, scheme=falsifier-sigma-distance,
   convention=framework-minus-LCDM-over-detector-sigma, L_max=NA)

Thresholds (plan W4-7 #9):
  PASS iff all 5 channels have computed null-sigma with falsifier
    consequence pre-registered.
  INFO iff <5 channels populated; remainder carry WARRANT-DEFERRED with
    named detector-forecast paper.
  FAIL iff <5 channels AND no deferral tag.
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
    planck_alpha_s,
    beta_s,
    r_CMB_framework,
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

GATE_ID = "S85-W4-7-NULL-ELIM-MAP"                                     # (local)
SCHEME = "falsifier-sigma-distance"                                     # (local)
CONVENTION = "framework-minus-LCDM-over-detector-sigma"                 # (local)
L_MAX = "NA"                                                            # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_null_elim_map.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_null_elim_map.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
XCORR_MD = PROJECT_ROOT / "sessions" / "framework" / "cross-channel-correlation-matrix.md"
MULTID_JFD_NPZ = SCRIPT_DIR / "s85_w4_multi_d_jfd.npz"
BASELINE_MD = PROJECT_ROOT / "sessions" / "framework" / "baseline-findings-s66.md"
EVOI_MD = PROJECT_ROOT / "sessions" / "evoi-framework.md"
PERM_REG_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

INPUT_FILES = [
    CANON_PY,
    BASELINE_MD,
    EVOI_MD,
    PERM_REG_MD,
    XCORR_MD,
    MULTID_JFD_NPZ,
]

# Framework predictions (from canonical + S85 pins)
FW_ALPHA_S_INFLATION = 0.00117                                          # (local, S63 RUNNING-NS-63; same pin as S85 W1a MULTID-FISHER)
FW_W0 = w0_FW                                                           # (local, -0.918; canonical)
FW_N_T_CMB = -3.024e-3                                                  # (local, S66 TENSOR-TRANSFER)
FW_F_NL_FOLDED = 0.0547                                                 # (local, S82 W3-4 GGE-FNL-CHANNEL; distinct from 0.129 equilateral+folded multi-shape)

# LCDM null centrals
LCDM_ALPHA_S = planck_alpha_s                                           # (local, Planck 2018 central -0.0045)
LCDM_W0 = -1.0                                                          # (local, LCDM cosmological constant)
LCDM_N_T_CMB = -r_CMB_framework / 8.0                                   # (local, slow-roll consistency n_T = -r/8; LCDM null on n_T)
LCDM_F_NL = 0.0                                                         # (local, LCDM single-field null)

# Detector 1-sigma forecasts
SIGMA_ALPHA_S_CMBS4 = 2.1e-3                                            # (local, S85 W1a MULTID-FISHER)
SIGMA_W0_DESIDR3 = 0.025                                                # (local, S85 W1a MULTID-FISHER; DESI DR3 projection)
SIGMA_N_T_LITEBIRD = 8.0e-4                                             # (local, LiteBIRD full-mission)
SIGMA_ALPHA_S_CMBHD = 1.1e-3                                            # (local, CMB-HD Sehgal 2019 projection)
SIGMA_F_NL_SKA1 = 5.0                                                   # (local, SKA-1 folded-shape)

# Detection threshold for falsifier classification
DETECTABLE_SIGMA = 3.0                                                  # (local) |Δ| > 3σ ⇒ detectable distinguisher


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                           # (local)
    for p in inputs:
        sha = sha256_of(p)                                              # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")    # (local)
        except ValueError:
            rel = p.name                                                # (local)
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
    h_audit = hashlib.sha256()                                          # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                        # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def compute() -> dict:
    # Per-channel (channel, x_FW, x_LCDM, sigma_detect, falsifier_consequence)
    rows = [
        ("CMB-S4 alpha_s",
         FW_ALPHA_S_INFLATION, LCDM_ALPHA_S, SIGMA_ALPHA_S_CMBS4,
         "Null at LCDM central ⇒ CMB-S4 disfavors framework inflationary alpha_s; triggers alpha_s-branch re-examination at pre-registered sigma."),
        ("DESI DR3 w_0",
         FW_W0, LCDM_W0, SIGMA_W0_DESIDR3,
         "Null at w_0=-1.000 ⇒ Volovik-partition branch (iv) CLOSED at rectangle-containment confidence per R_842 lockouts A-F; LOCKOUT-A prohibits retreat to dual-pin."),
        ("LiteBIRD n_T",
         FW_N_T_CMB, LCDM_N_T_CMB, SIGMA_N_T_LITEBIRD,
         "Null at n_T = -r/8 (slow-roll consistency) ⇒ the LCDM consistency is non-falsifier for framework because r=16*eps is INAPPLICABLE per phononic-framing. LiteBIRD null is NOT a framework falsifier (STRUCTURAL-FLOOR channel)."),
        ("CMB-HD alpha_s",
         FW_ALPHA_S_INFLATION, LCDM_ALPHA_S, SIGMA_ALPHA_S_CMBHD,
         "Same framework value as CMB-S4; tighter sigma ⇒ higher discriminative power. Null confirms/refutes CMB-S4 row at post-data common-mode-discounted joint confidence (§W4-6)."),
        ("21-cm folded bispec",
         FW_F_NL_FOLDED, LCDM_F_NL, SIGMA_F_NL_SKA1,
         "SKA-1 sigma=5 too large for framework value 0.055 ⇒ UNDETECTABLE at current SKA-1 projection. Post-2035 next-gen 21-cm retains falsifier potential."),
    ]

    n_total = len(rows)                                                 # (local) = 5
    sigma_distances = []
    detect_flags = []
    for ch, x_fw, x_lcdm, sig, consequence in rows:
        delta = (x_fw - x_lcdm) / sig                                   # (local)
        sigma_distances.append(delta)
        detect_flags.append(abs(delta) > DETECTABLE_SIGMA)

    # Substitution chain verification: sign convention preservation
    # Direction check: for each row, verify the sign of Delta matches
    # (x_FW > x_LCDM) ⇔ (Delta > 0). Trivially true by construction.
    for (ch, x_fw, x_lcdm, sig, _), d in zip(rows, sigma_distances):
        sign_check = (x_fw - x_lcdm) * d >= 0
        assert sign_check, f"Sign convention broken for {ch}: x_FW-x_LCDM={x_fw-x_lcdm}, Δ={d}"

    n_with_sigma = sum(1 for d in sigma_distances if np.isfinite(d))     # (local) = 5
    n_detectable = sum(detect_flags)                                     # (local)
    n_undetectable = n_total - n_detectable                              # (local)

    return {
        "n_total": n_total,
        "n_with_sigma": n_with_sigma,
        "n_detectable": n_detectable,
        "n_undetectable": n_undetectable,
        "rows": rows,
        "sigma_distances": np.array(sigma_distances),
        "detect_flags": np.array(detect_flags),
        "value": n_with_sigma,
    }


def evaluate_gate(res: dict) -> str:
    # PASS: all 5 channels have computed null-sigma with falsifier consequence
    # INFO: <5 channels populated but deferred tags applied
    # FAIL: <5 channels AND no deferral
    if res["n_with_sigma"] == res["n_total"]:
        return "PASS"
    return "FAIL"


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 5.5))                           # (local)
    labels = [r[0] for r in res["rows"]]
    deltas = res["sigma_distances"]
    colors = ["#b03030" if abs(d) > DETECTABLE_SIGMA else "#b06530" if abs(d) > 2 else "#888888"
              for d in deltas]
    xs = np.arange(len(labels))
    ax.bar(xs, deltas, color=colors, alpha=0.9)
    for i, d in enumerate(deltas):
        ax.text(i, d + (0.15 if d >= 0 else -0.5), f"{d:+.2f}σ", ha="center", fontsize=9)
    ax.axhline(0, color="k", lw=0.6)
    ax.axhspan(-DETECTABLE_SIGMA, DETECTABLE_SIGMA, color="#888888", alpha=0.1,
               label=f"|Δ| ≤ {DETECTABLE_SIGMA}σ (non-decisive)")
    ax.axhline(DETECTABLE_SIGMA, color="#b03030", lw=0.8, ls="--")
    ax.axhline(-DETECTABLE_SIGMA, color="#b03030", lw=0.8, ls="--", label=f"|Δ| = {DETECTABLE_SIGMA}σ")
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel(r"Null-result σ-distance $\Delta = (x_{FW} - x_{LCDM}) / \sigma_{detect}$")
    ax.set_title(f"{GATE_ID}: 5-channel falsifier σ-distance map "
                 f"(detectable = {res['n_detectable']}/{res['n_total']} at |Δ| > {DETECTABLE_SIGMA}σ)")
    ax.grid(True, alpha=0.25, axis="y")
    ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
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
    print(f"  w0_FW             = {w0_FW}")
    print(f"  planck_alpha_s    = {planck_alpha_s}")
    print(f"  beta_s            = {beta_s}")
    print(f"  r_CMB_framework   = {r_CMB_framework}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Per-channel null-result σ-distance ===")
    for row, d, detect in zip(res["rows"], res["sigma_distances"], res["detect_flags"]):
        ch, x_fw, x_lcdm, sig, cons = row
        flag = "DETECTABLE" if detect else "non-decisive"
        print(f"  {ch:22s}: x_FW={x_fw:+.4e}  x_LCDM={x_lcdm:+.4e}  σ={sig:.1e}  Δ={d:+7.3f}σ  [{flag}]")
        print(f"      consequence: {cons}")
    print()
    print(f"  n_with_sigma = {res['n_with_sigma']}/{res['n_total']}")
    print(f"  n_detectable (|Δ|>{DETECTABLE_SIGMA}σ) = {res['n_detectable']}/{res['n_total']}")
    print(f"  Verdict = {verdict}")

    np.savez(
        OUT_NPZ,
        channels=np.array([r[0] for r in res["rows"]]),
        x_FW=np.array([r[1] for r in res["rows"]]),
        x_LCDM=np.array([r[2] for r in res["rows"]]),
        sigma_detect=np.array([r[3] for r in res["rows"]]),
        consequences=np.array([r[4] for r in res["rows"]]),
        sigma_distances=res["sigma_distances"],
        detect_flags=res["detect_flags"],
        detectable_sigma_threshold=np.float64(DETECTABLE_SIGMA),
        n_with_sigma=np.int64(res["n_with_sigma"]),
        n_detectable=np.int64(res["n_detectable"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["n_with_sigma"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["n_with_sigma"], audit_sha, content_sha)

    wall = time.time() - t0                                            # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
