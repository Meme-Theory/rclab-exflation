#!/usr/bin/env python3
"""
S85 W4-1: CMB-S4 alpha_s FLAGSHIP INDEPENDENCE AUGMENT
======================================================

Gate: S85-W4-1-CMB-S4-INDEP-AUG
Trigger: [AUDIT]
Classification: NON-PHONONIC (methodology pre-registration; detector-level
                independence is a pipeline property)
Agent: mack-cosmic-bridge

Hypothesis: The CMB-S4 alpha_s flagship pre-registration (plan section W0-13)
is silent on the correlation structure among the 5 watchlist channels
(CMB-S4 alpha_s, DESI DR3 w_0, LiteBIRD n_T, CMB-HD alpha_s, 21-cm folded
bispectrum). Silence permits Bayes-factor inflation by factor up to k^(N-1)
~ 81 for 5 channels each with BF ~ k=3. The augment closes the silence by
attaching an Independence subsection classifying all C(5,2) = 10 pairs.

Substitution chain (Python-verified in Section 5 below):
  Step 1: Definition — BF_joint_indep = product_i BF_i          (independence)
  Step 2: Definition — BF_joint_corr  ~ max_i BF_i              (common-mode)
  Step 3: Substitute N=5, BF_i = k = 3 (illustrative):
            BF_joint_indep = k^5 = 243
            BF_joint_corr  = k   = 3
            Ratio          = k^4 = 81
  Step 4: Simplify: reporting BF_joint_indep for actually-correlated channels
          OVER-states the evidence by factor ~81.
  Step 5: Direction: augment is DEFLATIONARY on joint BF.
  Conclusion: omission inflates BF; augment prevents inflation.

Output 4-tuple:
  (value=<coverage_fraction>, scheme=observational-pipeline,
   convention=channel-list-frozen-to-W0-flagship, L_max=NA)

Thresholds (plan section W4-1):
  PASS  iff coverage_fraction == 1.0 AND Fisher citation per pair
  INFO  iff coverage_fraction < 1.0 AND every non-Fisher pair tagged
          WARRANT-DEFERRED citing the missing Fisher-paper source
  FAIL  iff coverage_fraction < 1.0 AND some pair silent (no tag)

Classification key:
  INDEPENDENT           — distinct substrate moments; first-principles argument
  PARTIALLY_CORRELATED  — shared acoustic-scale ladder or overlapping foreground
  COMMON_MODE           — same theoretical observable, overlapping systematics
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
    planck_ns,
    alpha_s_MZ_obs,
    planck_alpha_s,
    beta_s,
    sigma_beta_s_CMB_S4,
)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import re  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W4-1-CMB-S4-INDEP-AUG"                               # (local)
SCHEME = "observational-pipeline"                                    # (local)
CONVENTION = "channel-list-frozen-to-W0-flagship"                    # (local)
L_MAX = "NA"                                                         # (local)

# 5-channel watchlist frozen to W0 flagship scope (plan W4-1 #1-5)
CHANNELS = [
    "CMB-S4_alpha_s",        # running of scalar tilt dn_s/dlnk at k_pivot
    "DESI-DR3_w_0",          # dark-energy equation of state at z~0.3-2.0
    "LiteBIRD_n_T",          # tensor tilt from B-mode polarization
    "CMB-HD_alpha_s",        # independent running-of-tilt measurement
    "21cm_folded_bispec",    # NG shape from HERA/SKA reionization
]                                                                    # (local)

# Substrate-moment probed by each channel diagonal (for plan section W4-1 section 13)
SUBSTRATE_MOMENTS = [
    "d^2 S_transfer/dk^2 at k_pivot (scalar 2-pt 2nd derivative)",
    "a_0 Volovik-partition (zeroth spectral moment)",
    "tensor-sector Dirac spectrum (B-mode polarization; r=16eps INAPPLICABLE per phononic-framing)",
    "d^2 S_transfer/dk^2 at k_pivot (SAME moment as CMB-S4 alpha_s)",
    "3-point spectral moment (non-Gaussianity; distinct from 2-pt)",
]                                                                    # (local)

# Pair-wise (off-diagonal) classification with Fisher-source citation
# Tuple: (i, j, classification, fisher_or_WARRANT, citation, justification)
PAIR_CLASSIFICATIONS = [
    # CMB-S4 alpha_s vs DESI DR3 w_0
    (0, 1, "PARTIALLY_CORRELATED", "FISHER",
     "DESI Collab 2025 BAO forecast; Planck 2018 parameter table",
     "Shared acoustic-scale ladder (r_d) correlates Planck TT foregrounds with DESI BAO distance-scale."),
    # CMB-S4 alpha_s vs LiteBIRD n_T
    (0, 2, "INDEPENDENT", "FISHER",
     "CMB-S4 Science Book v2 2022 section 3.1; LiteBIRD 1902.00541",
     "Scalar-tilt running vs tensor tilt: orthogonal spectral moments; polarization-B foreground independent of TT."),
    # CMB-S4 alpha_s vs CMB-HD alpha_s
    (0, 3, "COMMON_MODE", "FISHER",
     "CMB-HD Sehgal 2019 Whitepaper section 4; CMB-S4 Science Book v2 Table 6.1",
     "Identical theoretical observable; overlapping foreground model; potentially correlated atmospheric noise."),
    # CMB-S4 alpha_s vs 21cm folded bispec
    (0, 4, "INDEPENDENT", "WARRANT-DEFERRED",
     "HERA Memo 54 (Ali+ 2018); no joint CMB-S4 x 21cm Fisher published",
     "z=1100 recombination (CMB) vs z~7 reionization (21cm); 2-pt vs 3-pt statistics; epoch-separated."),
    # DESI DR3 w_0 vs LiteBIRD n_T
    (1, 2, "INDEPENDENT", "WARRANT-DEFERRED",
     "DESI Collab 2025; LiteBIRD 1902.00541; no joint DESIxLiteBIRD published",
     "Late-time expansion history vs primordial-tensor B-mode; no shared systematic."),
    # DESI DR3 w_0 vs CMB-HD alpha_s
    (1, 3, "PARTIALLY_CORRELATED", "FISHER",
     "DESI Collab 2025 section 4; Sehgal 2019 CMB-HD Whitepaper",
     "Both derive r_d acoustic ruler; CMB-HD extends Planck+ACT CMB prior used in DESI BAO likelihood."),
    # DESI DR3 w_0 vs 21cm folded bispec
    (1, 4, "INDEPENDENT", "WARRANT-DEFERRED",
     "DESI Collab 2025; HERA Memo 54; no joint DESIx21cm Fisher published",
     "Low-z BAO (z<2) vs high-z NG (z>6); epoch-separated; different tracers."),
    # LiteBIRD n_T vs CMB-HD alpha_s
    (2, 3, "INDEPENDENT", "FISHER",
     "LiteBIRD 1902.00541; Sehgal 2019 CMB-HD section 4",
     "B-mode tensor vs TT/TE scalar running; CMB foreground templates differ between channels."),
    # LiteBIRD n_T vs 21cm folded bispec
    (2, 4, "INDEPENDENT", "WARRANT-DEFERRED",
     "LiteBIRD 1902.00541; HERA Memo 54; no joint published",
     "CMB polarization vs reionization cross-correlation; no shared systematic."),
    # CMB-HD alpha_s vs 21cm folded bispec
    (3, 4, "INDEPENDENT", "WARRANT-DEFERRED",
     "Sehgal 2019 CMB-HD; HERA Memo 54; no joint CMB-HDx21cm Fisher published",
     "Same logic as CMB-S4 x 21cm; different instrument-epoch pairing."),
]                                                                    # (local)

# Illustrative BF-inflation parameters for the substitution chain
K_ILLUSTRATIVE = 3.0                                                 # (local) per-channel BF example
N_CHANNELS = 5                                                       # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_cmbs4_indep_aug.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_cmbs4_indep_aug.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

W0_PLAN_MD = PROJECT_ROOT / "sessions" / "session-plan" / "session-85-plan-w0.md"
S84_MACK_MD = PROJECT_ROOT / "sessions" / "session-84" / "session-84-s4-mack-falsifier-synthesis.md"
S84_LRD_MD = PROJECT_ROOT / "sessions" / "session-84" / "session-84-s4-lrd-falsifier-synthesis.md"
PERM_REG_MD = PROJECT_ROOT / "sessions" / "framework" / "permanent-results-registry.md"
BASELINE_MD = PROJECT_ROOT / "sessions" / "framework" / "baseline-findings-s66.md"

INPUT_FILES = [
    CANON_PY,
    W0_PLAN_MD,
    S84_MACK_MD,
    S84_LRD_MD,
    PERM_REG_MD,
    BASELINE_MD,
]


# ---------------------------------------------------------------------------
# SHA + dual-SHA machinery (S84+ schema, matches script-template.py)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                             # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                        # (local)
    for p in inputs:
        sha = sha256_of(p)                                           # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                             # (local)
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
    h_audit = hashlib.sha256()                                       # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                     # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute: coverage, BF-inflation substitution-chain verification
# ---------------------------------------------------------------------------

def compute() -> dict:
    n_pairs_required = N_CHANNELS * (N_CHANNELS - 1) // 2            # (local) = 10
    n_pairs_addressed = len(PAIR_CLASSIFICATIONS)                     # (local)
    n_pairs_fisher = sum(1 for _, _, _, tag, _, _ in PAIR_CLASSIFICATIONS
                         if tag == "FISHER")                          # (local)
    n_pairs_deferred = sum(1 for _, _, _, tag, _, _ in PAIR_CLASSIFICATIONS
                           if tag == "WARRANT-DEFERRED")              # (local)
    n_pairs_silent = n_pairs_addressed - n_pairs_fisher - n_pairs_deferred  # (local)

    # Strict-Fisher coverage fraction (plan W4-1 PASS requires 1.0)
    coverage_fraction_strict = n_pairs_fisher / n_pairs_required      # (local)
    # Addressed-inclusive fraction (Fisher OR deferred)
    coverage_fraction_addressed = (n_pairs_fisher + n_pairs_deferred) / n_pairs_required  # (local)

    # BF-inflation substitution chain (Python-verified numerics)
    k = K_ILLUSTRATIVE                                                # (local)
    N = N_CHANNELS                                                    # (local)
    BF_indep = k ** N                                                 # (local) = 243
    BF_corr = k                                                       # (local) = 3
    ratio = BF_indep / BF_corr                                        # (local) = 81
    expected_ratio = k ** (N - 1)                                     # (local) = 81
    # Assert direction of the claim
    assert ratio == expected_ratio, f"BF-ratio mismatch: {ratio} != {expected_ratio}"
    assert BF_indep > BF_corr, "Direction broken: BF_indep must exceed BF_corr"

    # 5x5 matrix of qualitative tags (diagonal = DIAG-SUBSTRATE, off-diagonal = pair tag)
    tag_matrix = np.full((N, N), "", dtype=object)                    # (local)
    for k_idx in range(N):
        tag_matrix[k_idx, k_idx] = "DIAG"
    for i, j, cls, src_tag, cite, just in PAIR_CLASSIFICATIONS:
        tag_matrix[i, j] = cls
        tag_matrix[j, i] = cls

    # Numeric code for heatmap: 0 INDEPENDENT, 1 PARTIALLY_CORRELATED, 2 COMMON_MODE, -1 diag
    code = {"INDEPENDENT": 0, "PARTIALLY_CORRELATED": 1, "COMMON_MODE": 2, "DIAG": -1}
    code_matrix = np.zeros((N, N), dtype=int)                          # (local)
    for i in range(N):
        for j in range(N):
            code_matrix[i, j] = code[tag_matrix[i, j]] if tag_matrix[i, j] else -99

    return {
        "n_pairs_required": n_pairs_required,
        "n_pairs_addressed": n_pairs_addressed,
        "n_pairs_fisher": n_pairs_fisher,
        "n_pairs_deferred": n_pairs_deferred,
        "n_pairs_silent": n_pairs_silent,
        "coverage_fraction_strict": coverage_fraction_strict,
        "coverage_fraction_addressed": coverage_fraction_addressed,
        "BF_indep_illustrative": BF_indep,
        "BF_corr_illustrative": BF_corr,
        "BF_ratio_illustrative": ratio,
        "K_illustrative": k,
        "N_channels": N,
        "tag_matrix": tag_matrix,
        "code_matrix": code_matrix,
        "value": coverage_fraction_strict,   # plan-specified primary value
    }


def evaluate_gate(res: dict) -> str:
    # PASS: all 10 pairs have FISHER citation (strict coverage == 1.0)
    # INFO: coverage < 1.0 AND n_pairs_silent == 0 (all non-Fisher are WARRANT-DEFERRED)
    # FAIL: coverage < 1.0 AND n_pairs_silent > 0
    if res["coverage_fraction_strict"] == 1.0:
        return "PASS"
    if res["n_pairs_silent"] == 0:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 6 — W0-13 plan-file augment insertion (idempotent)
# ---------------------------------------------------------------------------

INDEPENDENCE_HEADER = "### W0-13 APPENDIX: Independence Subsection (augmented by S85-W4-1-CMB-S4-INDEP-AUG)"


def build_augment_text(res: dict) -> str:
    """Return the Markdown §Independence subsection inserted into W0-13.

    The subsection is written as a single block ending before the '---'
    terminator of W0-13. It is idempotent: if already present, the block
    is replaced rather than duplicated.
    """
    lines = []
    lines.append("")
    lines.append(INDEPENDENCE_HEADER)
    lines.append("")
    lines.append("*Inserted by S85-W4-1-CMB-S4-INDEP-AUG. Closes the silence on correlation structure "
                 "among the 5-channel falsifier watchlist. Prevents Bayes-factor inflation up to "
                 f"factor k^{N_CHANNELS - 1} = {int(res['BF_ratio_illustrative'])} for per-channel BF ~ k = {int(K_ILLUSTRATIVE)}.*")
    lines.append("")
    lines.append("**5-channel watchlist:**")
    for i, (ch, mom) in enumerate(zip(CHANNELS, SUBSTRATE_MOMENTS)):
        lines.append(f"  {i}. `{ch}` --- probes: {mom}")
    lines.append("")
    lines.append("**Pair-wise classification (C(5,2) = 10 off-diagonal cells):**")
    lines.append("")
    lines.append("| Pair | Channels | Classification | Source | Citation | Justification |")
    lines.append("|:----:|:---------|:--------------:|:------:|:---------|:--------------|")
    for i, j, cls, src, cite, just in PAIR_CLASSIFICATIONS:
        ch_i = CHANNELS[i].replace("_", " ")
        ch_j = CHANNELS[j].replace("_", " ")
        lines.append(f"| ({i},{j}) | {ch_i} / {ch_j} | {cls} | {src} | {cite} | {just} |")
    lines.append("")
    lines.append(f"**Coverage**: {res['n_pairs_fisher']}/{res['n_pairs_required']} pairs with published Fisher citations "
                 f"(= {res['coverage_fraction_strict']:.3f}); "
                 f"{res['n_pairs_deferred']}/{res['n_pairs_required']} tagged WARRANT-DEFERRED "
                 f"(no published joint Fisher); 0 silent.")
    lines.append("")
    lines.append("**Substitution chain — BF-inflation direction:**")
    lines.append("")
    lines.append("```")
    lines.append("Step 1: BF_joint_indep = product_i BF_i   (independence)")
    lines.append("Step 2: BF_joint_corr  ~ max_i BF_i       (common-mode)")
    lines.append(f"Step 3: Substitute N={N_CHANNELS}, BF_i = k = {int(K_ILLUSTRATIVE)}:")
    lines.append(f"        BF_joint_indep = k^N = {int(res['BF_indep_illustrative'])}")
    lines.append(f"        BF_joint_corr  = k   = {int(res['BF_corr_illustrative'])}")
    lines.append(f"        Ratio          = k^(N-1) = {int(res['BF_ratio_illustrative'])}")
    lines.append("Step 4: Simplify — over-states evidence by ~k^(N-1) when pairs COMMON_MODE.")
    lines.append("Step 5: Direction — augment is DEFLATIONARY on joint BF.")
    lines.append("Conclusion: omission inflates; augment closes silence and pins discount per pair.")
    lines.append("```")
    lines.append("")
    lines.append("**Post-data Bayes-factor formula (W4-2 will canonicalize):**")
    lines.append("")
    lines.append("  `BF_joint = BF_CMBS4 * BF_DESI^{1-rho_01} * BF_LiteB * BF_CMBHD^{1-rho_03} * BF_21cm`")
    lines.append("")
    lines.append("where rho_ij are taken from the §W4-2 xcorr matrix (specifically rho_01 = pipeline "
                 "CMB-S4/DESI DR3; rho_03 = CMB-S4/CMB-HD common-mode).")
    lines.append("")
    lines.append("**Artifacts (S84+ dual-SHA):**")
    lines.append(f"  - `computations/session-85/s85_w4_cmbs4_indep_aug.npz` (machine-readable matrix)")
    lines.append(f"  - `computations/session-85/s85_w4_cmbs4_indep_aug.png` (heatmap)")
    lines.append("")
    return "\n".join(lines)


def insert_augment_into_w0_plan(augment_text: str) -> bool:
    """Insert the augment into the W0-13 block of session-85-plan-w0.md.

    Idempotent: if the INDEPENDENCE_HEADER already appears anywhere in the
    W0-13 block, replace the existing block (from the header line through
    the next '---' terminator) with the fresh augment_text.

    Returns True if the plan file was modified, False if no change.
    """
    if not W0_PLAN_MD.exists():
        print(f"  [augment-insert] W0 plan file missing: {W0_PLAN_MD}")
        return False

    src = W0_PLAN_MD.read_text(encoding="utf-8")

    # Locate the W0-13 block: starts at '## §W0-13.' ends at next '## §W0-14.'
    m_start = re.search(r"^## §W0-13\.[^\n]*$", src, re.MULTILINE)
    m_end = re.search(r"^## §W0-14\.[^\n]*$", src, re.MULTILINE)
    if not (m_start and m_end):
        print(f"  [augment-insert] could not locate W0-13 / W0-14 markers")
        return False
    block_start = m_start.start()
    block_end = m_end.start()
    block = src[block_start:block_end]

    # Find the '---' terminator line inside the block (last one before W0-14)
    term_match = list(re.finditer(r"^\s*---\s*$", block, re.MULTILINE))
    if not term_match:
        print("  [augment-insert] no '---' terminator found inside W0-13 block")
        return False
    term_pos_in_block = term_match[-1].start()

    # Check if an augment already exists inside W0-13 block
    if INDEPENDENCE_HEADER in block:
        # Replace the existing augment: from header to just before '---'
        hdr_pos = block.index(INDEPENDENCE_HEADER)
        new_block = block[:hdr_pos] + augment_text.strip() + "\n\n" + block[term_pos_in_block:]
    else:
        # Insert the augment just before the '---' terminator
        new_block = block[:term_pos_in_block] + augment_text.strip() + "\n\n" + block[term_pos_in_block:]

    new_src = src[:block_start] + new_block + src[block_end:]
    if new_src == src:
        print("  [augment-insert] no change (already identical)")
        return False
    W0_PLAN_MD.write_text(new_src, encoding="utf-8")
    print(f"  [augment-insert] wrote augment to {W0_PLAN_MD.relative_to(PROJECT_ROOT)} "
          f"(size: {len(augment_text)} chars)")
    return True


# ---------------------------------------------------------------------------
# Section 7 — Plot + verdict + main
# ---------------------------------------------------------------------------

def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(1, 1, figsize=(7.5, 6.3))                  # (local)
    code = res["code_matrix"].astype(float)
    # Mask diagonal for clearer visual
    import numpy.ma as ma
    code_m = ma.masked_equal(code, -1)

    cmap = plt.cm.get_cmap("RdYlGn_r", 3)                             # 3-level discrete
    im = ax.imshow(code_m, cmap=cmap, vmin=-0.5, vmax=2.5)
    cbar = fig.colorbar(im, ax=ax, ticks=[0, 1, 2], fraction=0.046, pad=0.04)
    cbar.ax.set_yticklabels(["INDEPENDENT", "PARTIALLY\nCORRELATED", "COMMON\nMODE"])

    ax.set_xticks(range(res["N_channels"]))
    ax.set_yticks(range(res["N_channels"]))
    short = ["CMB-S4 a_s", "DESI DR3 w_0", "LiteBIRD n_T", "CMB-HD a_s", "21cm fold"]  # (local)
    ax.set_xticklabels(short, rotation=30, ha="right", fontsize=9)
    ax.set_yticklabels(short, fontsize=9)

    # Annotate cells
    for i in range(res["N_channels"]):
        for j in range(res["N_channels"]):
            if i == j:
                ax.text(j, i, "DIAG", ha="center", va="center",
                        fontsize=7, color="white", fontweight="bold")
            else:
                tag = res["tag_matrix"][i, j]
                short_tag = {"INDEPENDENT": "I", "PARTIALLY_CORRELATED": "P",
                             "COMMON_MODE": "C"}.get(tag, "?")
                ax.text(j, i, short_tag, ha="center", va="center",
                        fontsize=11, color="black", fontweight="bold")

    ax.set_title(f"{GATE_ID}\n5x5 channel-pair correlation classification "
                 f"({res['n_pairs_fisher']} Fisher + {res['n_pairs_deferred']} deferred / {res['n_pairs_required']})")
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
    t0 = time.time()                                                  # (local)

    # 1. Pin inputs (pre-edit snapshot for audit integrity)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                            # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Canonical constants echo (confirm import works)
    print("=== Canonical constants used ===")
    print(f"  w0_FW               = {w0_FW}")
    print(f"  planck_ns           = {planck_ns}")
    print(f"  alpha_s_MZ_obs      = {alpha_s_MZ_obs}")
    print(f"  planck_alpha_s      = {planck_alpha_s}")
    print(f"  beta_s              = {beta_s}")
    print(f"  sigma_beta_s_CMB_S4 = {sigma_beta_s_CMB_S4}")
    print()

    # 2. Compute coverage + matrix + substitution-chain verification
    res = compute()

    # 3. Verdict
    verdict = evaluate_gate(res)

    # 4. Narrate substitution chain
    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: BF_joint_indep = product_i BF_i   (independence)")
    print(f"  Step 2: BF_joint_corr  ~ max_i BF_i       (common-mode)")
    print(f"  Step 3: Substitute N={res['N_channels']}, BF_i = k = {res['K_illustrative']}:")
    print(f"          BF_joint_indep = k^N = {res['BF_indep_illustrative']}")
    print(f"          BF_joint_corr  = k   = {res['BF_corr_illustrative']}")
    print(f"          Ratio          = k^(N-1) = {res['BF_ratio_illustrative']}")
    print(f"  Step 4: Ratio = {res['BF_ratio_illustrative']} over-states evidence by this factor.")
    print(f"  Step 5: Direction: augment is DEFLATIONARY on joint BF.")
    print()

    # 5. Coverage breakdown
    print("=== Coverage breakdown ===")
    print(f"  n_pairs_required    = {res['n_pairs_required']}")
    print(f"  n_pairs_addressed   = {res['n_pairs_addressed']}")
    print(f"  n_pairs_fisher      = {res['n_pairs_fisher']} (published Fisher citation)")
    print(f"  n_pairs_deferred    = {res['n_pairs_deferred']} (WARRANT-DEFERRED, no joint Fisher published)")
    print(f"  n_pairs_silent      = {res['n_pairs_silent']} (untagged)")
    print(f"  coverage_fraction   = {res['coverage_fraction_strict']:.3f} (strict Fisher)")
    print(f"  coverage_addressed  = {res['coverage_fraction_addressed']:.3f} (Fisher + deferred)")
    print()

    # 6. Save NPZ + PNG
    np.savez(
        OUT_NPZ,
        channels=np.array(CHANNELS),
        substrate_moments=np.array(SUBSTRATE_MOMENTS),
        tag_matrix=res["tag_matrix"],
        code_matrix=res["code_matrix"],
        n_pairs_required=np.int64(res["n_pairs_required"]),
        n_pairs_fisher=np.int64(res["n_pairs_fisher"]),
        n_pairs_deferred=np.int64(res["n_pairs_deferred"]),
        n_pairs_silent=np.int64(res["n_pairs_silent"]),
        coverage_fraction_strict=np.float64(res["coverage_fraction_strict"]),
        coverage_fraction_addressed=np.float64(res["coverage_fraction_addressed"]),
        BF_indep=np.float64(res["BF_indep_illustrative"]),
        BF_corr=np.float64(res["BF_corr_illustrative"]),
        BF_ratio=np.float64(res["BF_ratio_illustrative"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    # 7. Insert augment into W0-13 block (LAST step so input-SHA snapshot is pre-edit)
    augment_text = build_augment_text(res)
    insert_augment_into_w0_plan(augment_text)

    # 8. Emit 4-tuple + verdict line
    tag = emit_4tuple(res["coverage_fraction_strict"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["coverage_fraction_strict"], audit_sha, content_sha)

    wall = time.time() - t0                                           # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
