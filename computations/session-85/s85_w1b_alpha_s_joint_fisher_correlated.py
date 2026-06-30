#!/usr/bin/env python3
"""
S85 W1b-2: ALPHA-S-JOINT-FISHER-CORRELATED
==========================================

Gate: S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED
Trigger: [VERIFY]
Classification: META (Fisher formalism; detector-level)
Agent: mack-cosmic-bridge

Hypothesis: The W1a-9 MULTID-FISHER assumes diagonal detector correlation
across {CMB-S4, CMB-HD, LiteBIRD, DESI-DR3, LISA}. Realistic correlation
is BLOCK-diagonal: CMB-S4/LiteBIRD share foreground (rho=0.15 at low-l),
CMB-S4/CMB-HD share sky overlap (rho=0.30 for alpha_s modes), DESI/LISA
independent. Propagating off-diagonals widens joint sigma(alpha_s);
gate tests whether the widening stays below the 25% tolerance.

Substitution chain (Python-verified):
  Step 1: sigma(alpha_s) per detector:
            sigma_S4   = 2.1e-3   (CMB-S4 CDR Table)
            sigma_HD   = 1.5e-3   (CMB-HD projection, MacInnis anchor)
            sigma_LB   = 1.05e-2  (LiteBIRD, 5x CMB-S4; Hazumi anchor)
            sigma_DR3  = 1.0e-2   (DESI-DR3 alpha_s weak)
            sigma_LISA = 1.0e-1   (LISA does not probe alpha_s directly)
          (all alpha_s-as-probed-quantity; other spectral observables
           are block-diagonally separate)
  Step 2: 5x5 correlation matrix C (plan §W1b-2 pre-registered):
            C_{S4,HD}  = 0.30 (partial sky overlap for alpha_s modes)
            C_{S4,LB}  = 0.15 (atmospheric + galactic foreground low-l)
            C_{DR3,*}  = 0     (DESI independent of CMB detectors)
            C_{LISA,*} = 0     (LISA independent)
          symmetric; unit diagonal.
  Step 3: Cov := Sigma . C . Sigma, with Sigma = diag(sigma_i).
  Step 4: combined inverse-variance (diagonal case):
            var_diag = 1 / sum_i 1/sigma_i^2
            sigma_diag = 1.2035e-3
          combined variance under correlated case (Cauchy-Schwarz):
            var_corr = 1 / (1^T . Cov^{-1} . 1)
            sigma_corr = 1.3597e-3
  Step 5: ratio = sigma_corr / sigma_diag = 1.1297
  Step 6: Compare to thresholds (plan §W1b-2):
            PASS iff ratio <= 1.25 ==> 1.1297 <= 1.25 => PASS
            FAIL iff ratio > 1.50
            INFO iff 1.25 < ratio <= 1.50
  Direction: correlation widens posterior; ratio >= 1 always (Cauchy-
             Schwarz on Fisher). Magnitude is output; gate tests
             whether it falls inside the 25% band.

Cross-check:
  - det(C) = 0.8875 (drops from 1 as off-diagonals turn on)
  - Diagonal limit (all C_ij = 0 off-diag): ratio = 1 exactly (sanity)

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - sessions/session-plan/session-85-plan-w1b.md (this plan)

Output 4-tuple:
  (value=<sigma_corr/sigma_diag>, scheme=Fisher-marg-Gauss, convention=block-diag-C, L_max=n/a)

Thresholds (plan §W1b-2):
  - PASS iff ratio <= 1.25 (W1a-9 claim survives within 25% widening)
  - FAIL iff ratio > 1.50
  - INFO iff 1.25 < ratio <= 1.50
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: E402, F401, F403 (for SHA pin + possible future ref)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED"                 # (local)
SCHEME = "Fisher-marg-Gauss"                                        # (local)
CONVENTION = "block-diag-C"                                         # (local)
L_MAX_LABEL = "n/a"                                                 # (local)

# Detector sigma(alpha_s) vector (per-detector 1-sigma)
DET_LABELS = ["CMB-S4", "CMB-HD", "LiteBIRD", "DESI-DR3", "LISA"]   # (local)
SIGMA_S4   = 2.1e-3                                                 # (local, CMB-S4 CDR Planck-like)
SIGMA_HD   = 1.5e-3                                                 # (local, CMB-HD projected; MacInnis anchor)
SIGMA_LB   = 1.05e-2                                                # (local, LiteBIRD 5x S4; Hazumi anchor)
SIGMA_DR3  = 1.0e-2                                                 # (local, DESI DR3 alpha_s weak)
SIGMA_LISA = 1.0e-1                                                 # (local, LISA insensitive to alpha_s)

# 5x5 correlation matrix (plan §W1b-2 pre-registered off-diagonals)
RHO_S4_HD  = 0.30                                                   # (local, partial sky overlap alpha_s modes)
RHO_S4_LB  = 0.15                                                   # (local, atmospheric+galactic foreground low-l)
# All other cross-pairs = 0

# Thresholds (plan §W1b-2)
PASS_RATIO = 1.25                                                   # (local)
FAIL_RATIO = 1.50                                                   # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w1b_alpha_s_joint_fisher_correlated.npz"
OUT_PNG = SCRIPT_DIR / "s85_w1b_alpha_s_joint_fisher_correlated.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
PLAN_MD = PROJECT_ROOT / "sessions" / "session-plan" / "session-85-plan-w1b.md"

INPUT_FILES = [CANON_PY]
if PLAN_MD.exists():
    INPUT_FILES.append(PLAN_MD)


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
    sigmas = np.array([SIGMA_S4, SIGMA_HD, SIGMA_LB, SIGMA_DR3, SIGMA_LISA],
                      dtype=np.float64)                              # (local)
    C = np.array([
        [1.0,        RHO_S4_HD, RHO_S4_LB, 0.0, 0.0],
        [RHO_S4_HD,  1.0,       0.0,       0.0, 0.0],
        [RHO_S4_LB,  0.0,       1.0,       0.0, 0.0],
        [0.0,        0.0,       0.0,       1.0, 0.0],
        [0.0,        0.0,       0.0,       0.0, 1.0],
    ], dtype=np.float64)                                            # (local)

    Sigma = np.diag(sigmas)                                         # (local)
    Cov = Sigma @ C @ Sigma                                         # (local)

    # Inverse-variance combine
    ones = np.ones(5, dtype=np.float64)                             # (local)
    Cov_inv = np.linalg.inv(Cov)                                    # (local)
    var_combined_corr = 1.0 / float(ones @ Cov_inv @ ones)          # (local)
    sigma_combined_corr = float(np.sqrt(var_combined_corr))         # (local)

    var_combined_diag = 1.0 / float(np.sum(1.0 / sigmas ** 2))      # (local)
    sigma_combined_diag = float(np.sqrt(var_combined_diag))         # (local)

    ratio = sigma_combined_corr / sigma_combined_diag               # (local)
    det_C = float(np.linalg.det(C))                                 # (local)

    # Sanity check: C = I -> ratio = 1 exactly
    C_id = np.eye(5)                                                # (local)
    Cov_id = Sigma @ C_id @ Sigma
    sigma_check = float(np.sqrt(1.0 / (ones @ np.linalg.inv(Cov_id) @ ones)))
    ratio_id = sigma_check / sigma_combined_diag
    sanity_ok = abs(ratio_id - 1.0) < 1e-12                         # (local)

    return {
        "value": ratio,
        "ratio": ratio,
        "sigma_corr": sigma_combined_corr,
        "sigma_diag": sigma_combined_diag,
        "sigmas": sigmas,
        "correlation_matrix": C,
        "Cov": Cov,
        "det_C": det_C,
        "sanity_identity_ratio": ratio_id,
        "sanity_ok": sanity_ok,
    }


def evaluate_gate(res: dict) -> str:
    r = res["ratio"]                                                # (local)
    if r <= PASS_RATIO:
        return "PASS"
    if r > FAIL_RATIO:
        return "FAIL"
    return "INFO"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def make_plot(res: dict, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.6))             # (local)

    # Panel A: 5x5 correlation heatmap
    ax = axes[0]
    im = ax.imshow(res["correlation_matrix"], cmap="RdBu_r", vmin=-0.5, vmax=1.0)
    ax.set_xticks(range(5)); ax.set_xticklabels(DET_LABELS, rotation=30, ha="right")
    ax.set_yticks(range(5)); ax.set_yticklabels(DET_LABELS)
    for i in range(5):
        for j in range(5):
            ax.text(j, i, f"{res['correlation_matrix'][i,j]:.2f}",
                    ha="center", va="center", fontsize=8, color="#111111")
    ax.set_title(rf"Correlation matrix (det C={res['det_C']:.4f})")
    fig.colorbar(im, ax=ax, fraction=0.046)

    # Panel B: sigma comparison
    ax = axes[1]
    labels = [rf"$\sigma_{{diag}}$", rf"$\sigma_{{corr}}$",
              "ratio", "PASS band", "FAIL line"]
    vals = [res["sigma_diag"], res["sigma_corr"],
            res["ratio"] * res["sigma_diag"],  # scale for plot
            PASS_RATIO * res["sigma_diag"],
            FAIL_RATIO * res["sigma_diag"]]
    colors = ["#1a5fb4", "#b03030", "#b06530", "#2a7a2a", "#553300"]
    ax.bar(range(len(vals)), vals, color=colors, alpha=0.85)
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labels, fontsize=9, rotation=20, ha="right")
    for i, v in enumerate(vals):
        ax.text(i, v * 1.02, f"{v:.3e}", ha="center", fontsize=8)
    ax.set_ylabel(r"$\sigma(\alpha_s)$ (combined)")
    ax.set_title(rf"ratio = {res['ratio']:.4f}  (PASS $\leq$ {PASS_RATIO})")
    ax.grid(True, alpha=0.25, axis="y")

    fig.suptitle(f"{GATE_ID}: 5x5 block-diagonal correlation widens sigma by "
                 f"{100*(res['ratio']-1):.1f}%")
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
    print(f"  Step 1: sigma(alpha_s) per detector:")
    for l, s in zip(DET_LABELS, res["sigmas"]):
        print(f"          {l:10s}: {s:.3e}")
    print(f"  Step 2: 5x5 correlation matrix off-diagonals:")
    print(f"          C(CMB-S4, CMB-HD)  = {RHO_S4_HD}")
    print(f"          C(CMB-S4, LiteBIRD)= {RHO_S4_LB}")
    print(f"          det(C) = {res['det_C']:.6f}")
    print(f"  Step 3: Cov = Sigma . C . Sigma assembled.")
    print(f"  Step 4: combined sigma:")
    print(f"          sigma_diag = {res['sigma_diag']:.4e}")
    print(f"          sigma_corr = {res['sigma_corr']:.4e}")
    print(f"  Step 5: ratio = {res['ratio']:.6f}")
    print(f"  Step 6: Thresholds PASS<={PASS_RATIO}, FAIL>{FAIL_RATIO}")
    print(f"          {res['ratio']:.4f} <= {PASS_RATIO} ==> {verdict}")
    print(f"  Sanity (C=I): ratio_id = {res['sanity_identity_ratio']:.12f} "
          f"(expect 1 exactly; ok={res['sanity_ok']})")
    print()

    np.savez(
        OUT_NPZ,
        ratio=np.float64(res["ratio"]),
        sigma_corr=np.float64(res["sigma_corr"]),
        sigma_diag=np.float64(res["sigma_diag"]),
        sigmas=res["sigmas"],
        correlation_matrix=res["correlation_matrix"],
        Cov=res["Cov"],
        det_C=np.float64(res["det_C"]),
        sanity_ok=np.array(res["sanity_ok"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["ratio"], SCHEME, CONVENTION, L_MAX_LABEL)
    print(tag)
    append_verdict(verdict, res["ratio"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
