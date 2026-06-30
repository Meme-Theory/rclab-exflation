#!/usr/bin/env python3
"""
S85 W4-6: MULTI-D JOINT FISHER INDEPENDENCE DISCOUNT
====================================================

Gate: S85-W4-6-MULTI-D-JFD
Trigger: [VERIFY]
Classification: NON-PHONONIC (Fisher-matrix arithmetic)
Agent: mack-cosmic-bridge

Hypothesis: N-channel joint Fisher matrix (N=5 channels on the W4-2
watchlist) with positive-definite off-diagonals gives sigma_joint
<= sigma_single for each parameter direction theta_j. The geometric-
mean discount factor vector calibrates future joint-Bayes evidence.

Substitution chain (plan W4-6 #10, Python-verified):
  Step 1: Definition — F_full = sum_i F_single_i over N channels;
          each F_single_i is positive-semi-definite (real detector).
  Step 2: Definition — sigma_joint(theta_j) = [F_full^{-1}]_{jj}^{1/2};
          sigma_single_i(theta_j) = [F_single_i^{-1}]_{jj}^{1/2}.
  Step 3: Substitute — F_full - F_single_i = sum_{k != i} F_single_k
          is PSD (sum of PSD matrices is PSD).
  Step 4: Simplify — PSD ordering ⇒ [F_full^{-1}]_jj <= [F_single_i^{-1}]_jj,
          so sigma_joint <= sigma_single_i on the diagonal.
  Step 5: Direction — discount factor = sigma_joint / sigma_single_i <= 1.
          Equality only when F_full - F_single_i = 0 (degenerate).
  Python verification: script asserts np.all(sigma_joint <= sigma_single + 1e-12).

Output 4-tuple:
  (value=<geometric_mean_discount_factor>, scheme=observational-pipeline,
   convention=Fisher-matrix-joint-GAUSSIAN-marginal, L_max=NA)

Thresholds (plan W4-6 #9):
  PASS iff F @ F_inv identity below 1e-6 AND 5 Fisher papers available
  INFO iff >= 1 Fisher paper unavailable (PRE-REG-INCOMPLETE)
  FAIL iff numerical singular Fisher
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

GATE_ID = "S85-W4-6-MULTI-D-JFD"                                       # (local)
SCHEME = "observational-pipeline"                                       # (local)
CONVENTION = "Fisher-matrix-joint-GAUSSIAN-marginal"                    # (local)
L_MAX = "NA"                                                            # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_multi_d_jfd.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_multi_d_jfd.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
XCORR_MD = PROJECT_ROOT / "sessions" / "framework" / "cross-channel-correlation-matrix.md"

# Fisher PDFs (expected at runtime; INFO fires if absent)
CMBS4_FISHER = PROJECT_ROOT / "researchers" / "CMB-S4" / "science_book_v2.pdf"
DESI_FISHER = PROJECT_ROOT / "researchers" / "DESI" / "desi_dr3_bao_forecast.pdf"
LITEBIRD_FISHER = PROJECT_ROOT / "researchers" / "LiteBIRD" / "litebird_forecast.pdf"
CMBHD_FISHER = PROJECT_ROOT / "researchers" / "CMB-HD" / "sehgal_2019_whitepaper.pdf"
HERA_FISHER = PROJECT_ROOT / "researchers" / "HERA" / "hera_memo_54.pdf"
FISHER_FILES = [CMBS4_FISHER, DESI_FISHER, LITEBIRD_FISHER, CMBHD_FISHER, HERA_FISHER]

INPUT_FILES = [CANON_PY, XCORR_MD]

# 5 channels, 4 substrate parameters (with CMB-S4 + CMB-HD SHARING α_s)
CHANNELS = ["CMB-S4_alpha_s", "DESI-DR3_w_0", "LiteBIRD_n_T", "CMB-HD_alpha_s", "21cm_folded"]  # (local)
PARAMS = ["alpha_s_scalar", "w_0", "n_T_tensor", "f_NL_folded"]                                  # (local)
# Which parameter each channel primarily probes:
PARAM_IDX_PER_CHANNEL = [0, 1, 2, 0, 3]                                                          # (local) CMB-S4, CMB-HD both -> param 0 (α_s)
SIGMAS = np.array([2.1e-3, 0.025, 8.0e-4, 1.1e-3, 5.0], dtype=np.float64)                        # (local)

# Common-mode correlation ρ_ij between channel pairs (from §W4-2).
# For channels that share a parameter (e.g., 0 & 3 both on α_s),
# ρ_ij is the DATA-LEVEL correlation that DISCOUNTS the naive Fisher sum.
# For channels on different parameters, ρ_ij is irrelevant for the
# single-parameter Fisher addition (the discount appears only when two
# channels measure the SAME parameter).
RHO_COMMON_MODE = 0.7                                                                            # (local) CMB-S4 × CMB-HD α_s pair (COMMON_MODE in §W4-2)

IDENTITY_TOL = 1e-6                                                                              # (local)


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


def build_channel_fishers(include_channels: list[int] | None = None) -> list[np.ndarray]:
    """Per-channel Fisher matrix in the 4-dim parameter space. Each
    channel i contributes a DIAGONAL Fisher with non-zero entry only at
    the parameter it primarily probes (PARAM_IDX_PER_CHANNEL[i]).

    When two channels share a parameter (CMB-S4 & CMB-HD both on α_s),
    their Fisher entries ADD at that diagonal position — this is the
    information-summation PSD structure the plan §W4-6 #10 invokes.
    """
    channel_list = range(len(CHANNELS)) if include_channels is None else include_channels
    N_p = len(PARAMS)                                                   # (local) = 4
    per_channel = []
    for i in channel_list:
        F = np.zeros((N_p, N_p), dtype=np.float64)                       # (local)
        j = PARAM_IDX_PER_CHANNEL[i]                                     # (local)
        F[j, j] = 1.0 / (SIGMAS[i] ** 2)
        per_channel.append(F)
    return per_channel


def apply_common_mode_discount(F_block: np.ndarray,
                               shared_channels: list[tuple[int, int, float]]) -> np.ndarray:
    """Apply data-level common-mode discount to channels that share a
    parameter.

    For each (i, j, rho) in shared_channels: channels i and j probe the
    SAME parameter theta_k = PARAM_IDX_PER_CHANNEL[i] = PARAM_IDX_PER_CHANNEL[j]
    with sigma_i, sigma_j, and data-level correlation rho.

    The correctly-discounted Fisher contribution to theta_k is
    1^T C^{-1} 1 for the 2x2 data covariance
    C = [[sigma_i^2, rho*sigma_i*sigma_j], [rho*sigma_i*sigma_j, sigma_j^2]].

    This REPLACES the naive sum (1/sigma_i^2 + 1/sigma_j^2) for that
    diagonal entry.
    """
    F_adj = F_block.copy()                                              # (local)
    for (ci, cj, rho) in shared_channels:
        k = PARAM_IDX_PER_CHANNEL[ci]                                    # (local)
        assert PARAM_IDX_PER_CHANNEL[cj] == k, \
            f"common-mode discount requires shared param; channels {ci},{cj} on params " \
            f"{PARAM_IDX_PER_CHANNEL[ci]},{PARAM_IDX_PER_CHANNEL[cj]}"
        sig_i = SIGMAS[ci]                                               # (local)
        sig_j = SIGMAS[cj]                                               # (local)
        C = np.array([[sig_i * sig_i, rho * sig_i * sig_j],
                      [rho * sig_i * sig_j, sig_j * sig_j]], dtype=np.float64)
        ones = np.ones(2, dtype=np.float64)                              # (local)
        F_kk_discounted = float(ones @ np.linalg.inv(C) @ ones)          # (local)
        # Replace the naive sum at diagonal k with the discounted value
        F_adj[k, k] = F_kk_discounted
    return F_adj


def compute() -> dict:
    N_p = len(PARAMS)                                                   # (local) = 4
    # Per-channel Fisher (diagonal, 4x4)
    per_channel = build_channel_fishers()                                # (local) list of 5 matrices

    # Naive independent sum (no common-mode discount)
    F_full_indep = sum(per_channel)                                      # (local) 4x4 diagonal

    # Apply common-mode discount on channel pair (0, 3) both on param α_s
    shared = [(0, 3, RHO_COMMON_MODE)]                                   # (local)
    F_full = apply_common_mode_discount(F_full_indep, shared)            # (local) 4x4 diagonal

    # Identity check
    F_inv = np.linalg.inv(F_full)                                        # (local)
    id_resid = np.linalg.norm(F_full @ F_inv - np.eye(F_full.shape[0]))   # (local)
    identity_ok = bool(id_resid < IDENTITY_TOL)

    # Per-parameter sigma_joint
    sigma_joint = np.sqrt(np.diag(F_inv))                                # (local) 4-vector

    # Per-parameter sigma_single_best: min over channels that probe this param
    sigma_single_best = np.full(N_p, np.inf)                             # (local)
    for i in range(len(CHANNELS)):
        k = PARAM_IDX_PER_CHANNEL[i]
        if SIGMAS[i] < sigma_single_best[k]:
            sigma_single_best[k] = SIGMAS[i]

    # Discount vector per parameter
    discount = sigma_joint / sigma_single_best                           # (local) 4-vector

    # Geometric-mean discount across parameters
    geom_mean_discount = float(np.exp(np.mean(np.log(discount))))        # (local)

    # Direction assertion (plan §W4-6 #10 step 5)
    direction_ok = bool(np.all(sigma_joint <= sigma_single_best + 1e-12))
    assert direction_ok, (
        f"PSD ordering broken: sigma_joint={sigma_joint} > sigma_single_best={sigma_single_best}"
    )

    # Independent-sum reference (for contrast with common-mode discount)
    F_inv_indep = np.linalg.inv(F_full_indep)                            # (local)
    sigma_joint_indep = np.sqrt(np.diag(F_inv_indep))                    # (local)
    # Common-mode inflation: how much does σ_joint grow when correlation is applied?
    cm_inflation = sigma_joint / sigma_joint_indep                       # (local) >=1

    # Progressive inclusion N_channels ∈ {3, 4, 5}
    progressive = {}
    for N_incl in [3, 4, 5]:
        pc_subset = build_channel_fishers(include_channels=list(range(N_incl)))
        F_sub_indep = sum(pc_subset)
        # apply common-mode only if both channels 0 and 3 are in the subset
        shared_sub = [(0, 3, RHO_COMMON_MODE)] if 0 in range(N_incl) and 3 in range(N_incl) else []
        F_sub = apply_common_mode_discount(F_sub_indep, shared_sub)
        try:
            F_sub_inv = np.linalg.inv(F_sub)
            sigma_joint_sub = np.sqrt(np.diag(F_sub_inv))
        except np.linalg.LinAlgError:
            sigma_joint_sub = np.full(N_p, np.nan)
        progressive[f"N_{N_incl}_sigma_joint"] = sigma_joint_sub

    return {
        "N_channels": len(CHANNELS),
        "N_params": N_p,
        "channels": CHANNELS,
        "params": PARAMS,
        "param_idx_per_channel": np.array(PARAM_IDX_PER_CHANNEL),
        "sigmas": SIGMAS,
        "rho_common_mode": RHO_COMMON_MODE,
        "F_full": F_full,
        "F_full_indep": F_full_indep,
        "F_inv": F_inv,
        "identity_residual": float(id_resid),
        "identity_ok": identity_ok,
        "sigma_joint": sigma_joint,
        "sigma_joint_indep": sigma_joint_indep,
        "sigma_single_best": sigma_single_best,
        "discount_vector": discount,
        "cm_inflation": cm_inflation,
        "geom_mean_discount": geom_mean_discount,
        "direction_ok": direction_ok,
        "progressive": progressive,
        "value": geom_mean_discount,
    }


def evaluate_gate(res: dict) -> str:
    n_fisher_present = sum(1 for p in FISHER_FILES if p.exists())      # (local)
    if not res["identity_ok"]:
        return "FAIL"
    if n_fisher_present < 5:
        return "INFO"
    if not res["direction_ok"]:
        return "FAIL"
    return "PASS"


def make_plot(res: dict, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))                  # (local)

    # Panel A: discount vector (sigma_joint / sigma_single_best per PARAMETER)
    ax = axes[0]
    N_p = res["N_params"]
    xs = np.arange(N_p)
    ax.bar(xs, res["discount_vector"], color="#1a5fb4", alpha=0.85)
    for i, d in enumerate(res["discount_vector"]):
        ax.text(i, d + 0.005, f"{d:.3f}", ha="center", fontsize=8)
    ax.axhline(1.0, color="#b03030", lw=1.0, ls="--", label="no-discount (=1)")
    ax.axhline(res["geom_mean_discount"], color="#2a7a2a", lw=1.0, ls=":",
               label=f"geom-mean = {res['geom_mean_discount']:.4f}")
    ax.set_xticks(xs)
    ax.set_xticklabels(res["params"], rotation=30, ha="right", fontsize=9)
    ax.set_ylabel(r"$\sigma_{\mathrm{joint}} / \sigma_{\mathrm{single,best}}$")
    ax.set_ylim(0, 1.1)
    ax.set_title("Per-parameter discount (≤ 1 always)")
    ax.grid(True, alpha=0.25, axis="y")
    ax.legend(fontsize=8, loc="lower right")

    # Panel B: Fisher heatmap (4x4 diagonal)
    ax = axes[1]
    with np.errstate(divide="ignore"):
        heat = np.log10(np.abs(res["F_full"]) + 1e-30)
    im = ax.imshow(heat, cmap="viridis")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label=r"$\log_{10} |F_{ij}|$")
    ax.set_xticks(range(N_p))
    ax.set_yticks(range(N_p))
    ax.set_xticklabels(res["params"], rotation=30, ha="right", fontsize=9)
    ax.set_yticklabels(res["params"], fontsize=9)
    for i in range(N_p):
        for j in range(N_p):
            val = res["F_full"][i, j]
            if abs(val) > 1e-10:
                ax.text(j, i, f"{val:.1e}", ha="center", va="center",
                        fontsize=7, color="white" if val < res["F_full"].max() * 0.3 else "black")
    ax.set_title("F_full (4×4) -- param-space Fisher sum (α_s channels 0+3 common-mode discounted)")

    fig.suptitle(f"{GATE_ID}: geom-mean discount = {res['geom_mean_discount']:.4f}; "
                 f"identity residual = {res['identity_residual']:.2e}; direction = {'PASS' if res['direction_ok'] else 'FAIL'}")
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

    # Pin Fisher PDFs (if present)
    print(f"\n  Fisher PDF presence check:")
    n_fisher_present = 0                                                # (local)
    for p in FISHER_FILES:
        present = p.exists()
        if present:
            n_fisher_present += 1
            print(f"    PRESENT : {p.relative_to(PROJECT_ROOT)}")
            pins[str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")] = sha256_of(p)
        else:
            print(f"    absent  : {p.relative_to(PROJECT_ROOT)}")
    print(f"  Fisher papers available: {n_fisher_present}/5")
    print()

    script_path = Path(__file__).resolve()                             # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("=== Canonical constants used (read-only) ===")
    print(f"  tau_fold = {tau_fold}")
    print(f"  M_KK     = {M_KK}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    N_p = res["N_params"]
    print(f"=== Fisher matrix ({N_p}×{N_p}, param-space) ===")
    for i in range(N_p):
        row = " ".join(f"{res['F_full'][i, j]:+.2e}" for j in range(N_p))
        print(f"  {res['params'][i]:22s} [{i}]  {row}")
    print(f"\n  F_full @ F_inv identity residual = {res['identity_residual']:.2e} "
          f"(<= {IDENTITY_TOL}? {res['identity_ok']})")
    print()

    print("=== Per-parameter σ_joint vs σ_single_best (common-mode discounted) ===")
    for j, param in enumerate(res["params"]):
        print(f"  {param:22s}: σ_single_best={res['sigma_single_best'][j]:.3e} "
              f"σ_joint={res['sigma_joint'][j]:.3e} "
              f"σ_joint_indep={res['sigma_joint_indep'][j]:.3e} "
              f"discount={res['discount_vector'][j]:.4f} "
              f"CM-inflation={res['cm_inflation'][j]:.4f}")
    print(f"\n  Geometric-mean discount = {res['geom_mean_discount']:.6f}")
    print(f"  Direction assertion (σ_joint ≤ σ_single_best): {res['direction_ok']}")
    print()

    print("=== Progressive inclusion N ∈ {3, 4, 5} ===")
    for N_incl in [3, 4, 5]:
        sj = res["progressive"][f"N_{N_incl}_sigma_joint"]
        print(f"  N_incl={N_incl}: σ_joint = [{', '.join(f'{x:.3e}' for x in sj)}]")
    print()

    info_reason = ""
    if verdict == "INFO":
        info_reason = f"PRE-REG-INCOMPLETE-{n_fisher_present}of5-Fisher-PDFs"

    np.savez(
        OUT_NPZ,
        channels=np.array(res["channels"]),
        params=np.array(res["params"]),
        param_idx_per_channel=res["param_idx_per_channel"],
        sigmas=res["sigmas"],
        rho_common_mode=np.float64(res["rho_common_mode"]),
        F_full=res["F_full"],
        F_full_indep=res["F_full_indep"],
        F_inv=res["F_inv"],
        identity_residual=np.float64(res["identity_residual"]),
        identity_ok=np.array(res["identity_ok"]),
        sigma_joint=res["sigma_joint"],
        sigma_joint_indep=res["sigma_joint_indep"],
        sigma_single_best=res["sigma_single_best"],
        discount_vector=res["discount_vector"],
        cm_inflation=res["cm_inflation"],
        geom_mean_discount=np.float64(res["geom_mean_discount"]),
        direction_ok=np.array(res["direction_ok"]),
        N_3_sigma_joint=res["progressive"]["N_3_sigma_joint"],
        N_4_sigma_joint=res["progressive"]["N_4_sigma_joint"],
        N_5_sigma_joint=res["progressive"]["N_5_sigma_joint"],
        n_fisher_pdfs_present=np.int64(n_fisher_present),
        info_reason=np.array(info_reason),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["geom_mean_discount"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["geom_mean_discount"], audit_sha, content_sha, info_reason)

    wall = time.time() - t0                                            # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
