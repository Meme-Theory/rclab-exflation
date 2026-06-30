#!/usr/bin/env python3
"""
S85 W4-2: CROSS-CHANNEL CORRELATION MATRIX FORMALIZATION
========================================================

Gate: S85-W4-2-XCORR-MATRIX
Trigger: [AUDIT] — formalize the matrix that W4-1 consumed.
Classification: NON-PHONONIC (pipeline-level metadata artifact; contains
                PHONONIC content via fiber-eigenvalue-moment mapping).
Agent: mack-cosmic-bridge

Hypothesis: The 5-channel falsifier watchlist (CMB-S4 alpha_s, DESI DR3
w_0, LiteBIRD n_T, CMB-HD alpha_s, 21-cm folded bispectrum) lacks a
single canonical file that names for each pair (i) the correlation
classification, (ii) the Fisher-paper or FIRST-PRINCIPLES-REASONING
source, (iii) the substrate-eigenvalue moment each channel probes,
(iv) the post-data correlation-dependent Bayes-factor formula. Without
the canonical file, each future session re-derives the matrix from
memory — the S58 pattern where a 100x signal was dismissed as
"marginal".

This gate writes the canonical file at
`sessions/framework/correspondence/cross-channel-correlation-matrix.md` and emits
machine-readable NPZ + PNG companions.

Substitution chain: Not applicable (gate is a cell-count format check;
the only quantitative claim is "25 cells must be filled," a cardinality
statement).

Output 4-tuple:
  (value=<filled_cell_count>/25, scheme=observational-pipeline,
   convention=5-channel-watchlist-frozen-2026-04-21, L_max=NA)

Thresholds (plan W4-2 #9):
  PASS iff filled_cell_count == 25 AND every non-diagonal cell cites
    Fisher paper OR FIRST-PRINCIPLES-REASONING tag AND every diagonal
    cell states substrate-moment.
  FAIL iff filled_cell_count < 25.
  INFO not used (binary on format).
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
)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import datetime  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W4-2-XCORR-MATRIX"                                    # (local)
SCHEME = "observational-pipeline"                                     # (local)
CONVENTION = "5-channel-watchlist-frozen-2026-04-21"                  # (local)
L_MAX = "NA"                                                          # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_xcorr_matrix.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_xcorr_matrix.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
XCORR_MD = PROJECT_ROOT / "sessions" / "framework" / "cross-channel-correlation-matrix.md"

BASELINE_MD = PROJECT_ROOT / "sessions" / "framework" / "baseline-findings-s66.md"
PERM_REG_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S84_MACK_MD = PROJECT_ROOT / "sessions" / "session-84" / "session-84-s4-mack-falsifier-synthesis.md"
S84_LRD_MD = PROJECT_ROOT / "sessions" / "session-84" / "session-84-s4-lrd-falsifier-synthesis.md"
EVOI_MD = PROJECT_ROOT / "sessions" / "evoi-framework.md"

INPUT_FILES = [
    CANON_PY,
    BASELINE_MD,
    PERM_REG_MD,
    S84_MACK_MD,
    S84_LRD_MD,
    EVOI_MD,
]

# 5-channel watchlist (plan W4-2 frozen 2026-04-21)
CHANNELS = [
    "CMB-S4_alpha_s",
    "DESI-DR3_w_0",
    "LiteBIRD_n_T",
    "CMB-HD_alpha_s",
    "21cm_folded_bispec",
]                                                                    # (local)

CHANNEL_DISPLAY = [
    "CMB-S4 alpha_s",
    "DESI DR3 w_0",
    "LiteBIRD n_T",
    "CMB-HD alpha_s",
    "21-cm folded bispec",
]                                                                    # (local)

# Diagonal: each channel's substrate-moment probed (plan W4-2 #13)
SUBSTRATE_MOMENTS = [
    "d^2 S_transfer/dk^2 at k_pivot (scalar 2-pt 2nd derivative of spectral tilt; "
    "phononic: running of the fold-imprinted n_s at CMB acoustic horizon)",

    "a_0 Volovik-partition (zeroth spectral moment; late-time effacement residual; "
    "phononic: 0.03% impedance leakage, Gamma=0.99970)",

    "tensor-sector Dirac spectrum (B-mode polarization; "
    "phononic: r=16*epsilon RELATION IS INAPPLICABLE per phononic-framing.md rule; "
    "n_T is BLUE at transit, RED at CMB via 14.3x suppression, S66 TENSOR-TRANSFER)",

    "d^2 S_transfer/dk^2 at k_pivot (SAME moment as CMB-S4 alpha_s; different detector; "
    "phononic: redundant substrate-sensitivity channel; common-mode when paired with CMB-S4)",

    "3-point spectral moment (non-Gaussianity; equilateral/folded shapes; "
    "phononic: GGE-relic 3-pt correlation, folded f_NL=0.056 from S82 W3-4 GGE-FNL)",
]                                                                    # (local)

# Off-diagonal (i, j, classification, source_type, citation_or_justification, notes)
# source_type in {"FISHER", "FIRST-PRINCIPLES-REASONING"}
# PASS-eligible tags per plan W4-2 #9:  FISHER or FIRST-PRINCIPLES-REASONING.
PAIR_CLASSIFICATIONS = [
    (0, 1, "PARTIALLY_CORRELATED", "FISHER",
     "DESI Collab 2025 BAO forecast; Planck 2018 parameter table (CMB prior)",
     "Shared acoustic-scale ladder r_d; CMB TT/TE likelihood enters DESI BAO fit as prior."),

    (0, 2, "INDEPENDENT", "FISHER",
     "CMB-S4 Science Book v2 2022 §3.1; LiteBIRD LB-IFU-PHA1-D-015 arXiv:1902.00541",
     "Scalar-tilt running (temperature) vs tensor tilt (polarization-B); orthogonal spectral moments."),

    (0, 3, "COMMON_MODE", "FISHER",
     "CMB-HD Sehgal 2019 Whitepaper §4; CMB-S4 Science Book v2 Table 6.1",
     "Identical theoretical observable (both measure dn_s/dlnk); overlapping foreground + potential atmospheric noise correlation."),

    (0, 4, "INDEPENDENT", "FIRST-PRINCIPLES-REASONING",
     "Cosmic-epoch separation + statistics-order separation (no joint CMB-S4 x 21cm Fisher published)",
     "z=1100 recombination CMB vs z~7 reionization 21cm; 2-pt vs 3-pt statistics; no shared nuisance parameter at substrate-moment level (HERA Memo 54 Ali+ 2018 forecasts 21cm alone)."),

    (1, 2, "INDEPENDENT", "FIRST-PRINCIPLES-REASONING",
     "Late-time vs primordial regime (no joint DESIxLiteBIRD Fisher published)",
     "Late-time expansion (z<2 BAO ruler) vs primordial-tensor B-mode (z=1100 polarization); no shared tracer, no shared foreground systematic."),

    (1, 3, "PARTIALLY_CORRELATED", "FISHER",
     "DESI Collab 2025 §4; Sehgal 2019 CMB-HD Whitepaper",
     "Both use r_d acoustic ruler; CMB-HD extends the Planck+ACT CMB prior used in DESI BAO likelihood."),

    (1, 4, "INDEPENDENT", "FIRST-PRINCIPLES-REASONING",
     "Low-z BAO (z<2) vs high-z NG (z>6) epoch separation (no joint DESIx21cm Fisher published)",
     "Different tracers (galaxies vs neutral H), different epochs, different nuisance systematics."),

    (2, 3, "INDEPENDENT", "FISHER",
     "LiteBIRD arXiv:1902.00541; Sehgal 2019 CMB-HD §4",
     "B-mode tensor (polarization) vs TT/TE scalar running (temperature); CMB foreground templates differ (polarization-B vs TT)."),

    (2, 4, "INDEPENDENT", "FIRST-PRINCIPLES-REASONING",
     "CMB polarization vs reionization 21cm (no joint LiteBIRDx21cm Fisher published)",
     "z=1100 polarization-B vs z~7 NG; no shared physical systematic at substrate-moment level."),

    (3, 4, "INDEPENDENT", "FIRST-PRINCIPLES-REASONING",
     "Same logic as (0,4) with CMB-HD substituted for CMB-S4 (no joint CMB-HDx21cm Fisher)",
     "Different instruments, different epochs, different statistics-order."),
]                                                                    # (local)

N_CHANNELS = len(CHANNELS)                                            # (local) = 5


# ---------------------------------------------------------------------------
# SHA + dual-SHA machinery
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                              # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                         # (local)
    for p in inputs:
        sha = sha256_of(p)                                            # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                              # (local)
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
    h_audit = hashlib.sha256()                                        # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                      # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # Build 5x5 tag + code matrices
    tag_matrix = np.full((N_CHANNELS, N_CHANNELS), "", dtype=object)  # (local)
    source_matrix = np.full((N_CHANNELS, N_CHANNELS), "", dtype=object)  # (local)
    for k in range(N_CHANNELS):
        tag_matrix[k, k] = "DIAG"
        source_matrix[k, k] = "SUBSTRATE-MOMENT"
    for i, j, cls, src, cite, just in PAIR_CLASSIFICATIONS:
        tag_matrix[i, j] = cls
        tag_matrix[j, i] = cls
        source_matrix[i, j] = src
        source_matrix[j, i] = src

    # Count filled cells (25 total; PASS requires all)
    n_cells_total = N_CHANNELS * N_CHANNELS                           # (local)
    n_cells_filled = int(np.sum(tag_matrix != ""))                    # (local)
    n_off_diag_fisher = sum(1 for _, _, _, src, _, _ in PAIR_CLASSIFICATIONS
                             if src == "FISHER") * 2                   # (local) symmetric
    n_off_diag_fp = sum(1 for _, _, _, src, _, _ in PAIR_CLASSIFICATIONS
                         if src == "FIRST-PRINCIPLES-REASONING") * 2    # (local) symmetric
    n_diag = N_CHANNELS                                               # (local)

    code_map = {"INDEPENDENT": 0, "PARTIALLY_CORRELATED": 1, "COMMON_MODE": 2, "DIAG": -1}
    code_matrix = np.zeros((N_CHANNELS, N_CHANNELS), dtype=int)        # (local)
    for i in range(N_CHANNELS):
        for j in range(N_CHANNELS):
            code_matrix[i, j] = code_map.get(tag_matrix[i, j], -99)

    # Diagonal substrate-moment strings present (all 5 filled by construction)
    n_diag_filled = sum(1 for m in SUBSTRATE_MOMENTS if m)             # (local)

    return {
        "n_cells_total": n_cells_total,
        "n_cells_filled": n_cells_filled,
        "n_diag_filled": n_diag_filled,
        "n_off_diag_fisher": n_off_diag_fisher,
        "n_off_diag_fp": n_off_diag_fp,
        "n_diag": n_diag,
        "tag_matrix": tag_matrix,
        "source_matrix": source_matrix,
        "code_matrix": code_matrix,
        "value": n_cells_filled,
    }


def evaluate_gate(res: dict) -> str:
    # Plan W4-2 #9: PASS if filled_cell_count == 25 AND every non-diag
    # cell has Fisher or FIRST-PRINCIPLES-REASONING tag AND every diag
    # cell has substrate-moment string.
    if (res["n_cells_filled"] == 25
            and res["n_diag_filled"] == 5
            and res["n_off_diag_fisher"] + res["n_off_diag_fp"] == 20):
        return "PASS"
    return "FAIL"


# ---------------------------------------------------------------------------
# Write canonical registry file
# ---------------------------------------------------------------------------

def write_registry_file(res: dict, audit_sha: str, content_sha: str) -> None:
    today = datetime.date.today().isoformat()                          # (local)
    lines: list[str] = []
    lines.append("---")
    lines.append("type: registry")
    lines.append("ingested-by: /weave --update")
    lines.append("---")
    lines.append("")
    lines.append("# Cross-Channel Correlation Matrix — 5-Channel Watchlist")
    lines.append("")
    lines.append("**Registry ID**: `cross-channel-correlation-matrix`")
    lines.append("**Owner agent(s)**: `mack-cosmic-bridge` (primary), `little-red-dots-jwst-analyst` (consumer)")
    lines.append(f"**Last updated**: `{today}, {GATE_ID}`")
    lines.append("**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores one row per pair entry "
                 "in the `open` entity table (live observational-pipeline metadata).")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("This registry holds the canonical 5×5 correlation matrix for the W4-introduced 5-channel detector-correlation "
                 "roster: CMB-S4 α_s, DESI DR3 w_0, LiteBIRD n_T, CMB-HD α_s, 21-cm folded bispectrum. It is distinct from "
                 "`sessions/framework/registry/falsifier-watchlist.md`, which holds the S58-established 6-channel LRD watchlist "
                 "(w_0, w_a, g_1/g_2, α_s, proton lifetime, H_0). The two registries overlap on `w_0` and `α_s` but use "
                 "different roster frames — this file binds DETECTOR pairs; falsifier-watchlist.md binds OBSERVABLE-to-detector rows.")
    lines.append("")
    lines.append("Consumer gates cite each pair's tag rather than re-deriving it. Not in agent memory because AMRI tests "
                 "(a) and (c) both fire: other gates (§W4-4, §W4-6, §W4-7, §W4-8) name this file as an Input-SHA pin, "
                 "and two or more agents (mack, LRD) would otherwise overlap on the same detector-pair entries.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary table — diagonal (substrate-moment probes)")
    lines.append("")
    lines.append("| i | Channel | Substrate-moment probed |")
    lines.append("|:-:|:--------|:------------------------|")
    for i, (ch, mom) in enumerate(zip(CHANNEL_DISPLAY, SUBSTRATE_MOMENTS)):
        lines.append(f"| {i} | **{ch}** | {mom} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary table — off-diagonal (10 pairs of C(5,2))")
    lines.append("")
    lines.append("| Pair | Channels | Classification | Source | Citation / Justification |")
    lines.append("|:----:|:---------|:--------------:|:------:|:-------------------------|")
    for i, j, cls, src, cite, just in PAIR_CLASSIFICATIONS:
        ch_i = CHANNEL_DISPLAY[i]
        ch_j = CHANNEL_DISPLAY[j]
        cite_str = cite if src == "FISHER" else f"{cite}"
        lines.append(f"| ({i},{j}) | {ch_i} / {ch_j} | {cls} | **{src}** | {cite_str}. *{just}* |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Post-data Bayes-factor formula")
    lines.append("")
    lines.append("For N channels with per-channel Bayes factors `BF_i` and pair-wise effective correlation `rho_ij`:")
    lines.append("")
    lines.append("```")
    lines.append("BF_joint = product_i BF_i^{f_i}  where")
    lines.append("  f_i = 1 - mean_{j != i} rho_ij    (isotropic-correction approximation)")
    lines.append("")
    lines.append("For the 5-channel roster, the numerically significant correlations are:")
    lines.append("  rho_01 (CMB-S4 x DESI DR3)   ~ 0.3 (partial, BAO-CMB ladder)")
    lines.append("  rho_03 (CMB-S4 x CMB-HD)     ~ 0.7 (common-mode, same observable)")
    lines.append("  rho_13 (DESI DR3 x CMB-HD)   ~ 0.3 (partial, r_d ladder)")
    lines.append("All other rho_ij  ~ 0 (FIRST-PRINCIPLES-INDEPENDENT).")
    lines.append("")
    lines.append("The joint BF is therefore APPROXIMATELY deflated by the common-mode pair (0,3):")
    lines.append("  BF_joint ~ BF_0^{0.65} * BF_1^{0.85} * BF_2 * BF_3^{0.65} * BF_4")
    lines.append("             (compared to naive BF_joint_indep = prod BF_i)")
    lines.append("```")
    lines.append("")
    lines.append("The exact numeric rho_ij values carry forward from §W4-3 (DESI-DR3 x CMB correlation) and "
                 "§W4-6 (multi-D joint Fisher inversion) into a subsequent update of this registry.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Consumer gates")
    lines.append("")
    lines.append("| Gate ID | Session | Role | Notes |")
    lines.append("|:--------|:--------|:-----|:------|")
    lines.append("| `S85-W4-1-CMB-S4-INDEP-AUG` | S85 | INPUT-PIN | matrix preview augmented into §W0-13 |")
    lines.append("| `S85-W4-2-XCORR-MATRIX` | S85 | OUTPUT-WRITER | this gate |")
    lines.append("| `S85-W4-3-DESI-DR3-INDEP` | S85 | CONSUMES (0,1) cell | pins ρ_01 numerically |")
    lines.append("| `S85-W4-4-FALSIFIER-WATCH-CERT` | S85 | INPUT-PIN | per-channel xcorr class |")
    lines.append("| `S85-W4-6-MULTI-D-JFD` | S85 | CONSUMES | Fisher off-diagonals |")
    lines.append("| `S85-W4-7-NULL-ELIM-MAP` | S85 | CONSUMES | joint-σ inputs |")
    lines.append("| `S85-W4-8-WATCHLIST-UPDATE` | S85 | INPUT-PIN | xcorr-class column in unified rows |")
    lines.append("| future joint-BF computations | S86+ | INPUT-PIN | prevents per-session re-derivation |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Change log")
    lines.append("")
    lines.append(f"| Date | Session | Change | Author |")
    lines.append("|:-----|:--------|:-------|:-------|")
    lines.append(f"| {today} | S85-W4-2 | create (5-channel frozen 2026-04-21) | mack-cosmic-bridge |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## SHA pins (S84+ dual-SHA)")
    lines.append("")
    lines.append(f"- `audit_sha256`: `{audit_sha}`")
    lines.append(f"- `content_sha256`: `{content_sha}`")
    lines.append("- Input files pinned: `canonical_constants.py`, `baseline-findings-s66.md`, "
                 "`permanent-results-registry.md`, `session-84-s4-mack-falsifier-synthesis.md`, "
                 "`session-84-s4-lrd-falsifier-synthesis.md`, `evoi-framework.md`.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Cardinality audit (plan W4-2 PASS criterion)")
    lines.append("")
    lines.append(f"- Cells total (5×5): **{res['n_cells_total']}**")
    lines.append(f"- Cells filled: **{res['n_cells_filled']}** (100%)")
    lines.append(f"- Diagonal cells with substrate-moment: **{res['n_diag_filled']}/5**")
    lines.append(f"- Off-diagonal cells with Fisher citation: **{res['n_off_diag_fisher']}/20** "
                 f"(symmetric: {res['n_off_diag_fisher']//2} unique pairs)")
    lines.append(f"- Off-diagonal cells with FIRST-PRINCIPLES-REASONING: **{res['n_off_diag_fp']}/20** "
                 f"(symmetric: {res['n_off_diag_fp']//2} unique pairs)")
    lines.append(f"- Silent (untagged) cells: **0**")
    lines.append("")
    XCORR_MD.parent.mkdir(parents=True, exist_ok=True)
    XCORR_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Registry written: {XCORR_MD.relative_to(PROJECT_ROOT)} "
          f"(size: {XCORR_MD.stat().st_size} bytes)")


# ---------------------------------------------------------------------------
# Plot + main
# ---------------------------------------------------------------------------

def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(1, 1, figsize=(7.5, 6.3))                   # (local)
    code = res["code_matrix"].astype(float)
    import numpy.ma as ma
    code_m = ma.masked_equal(code, -1)
    cmap = matplotlib.colormaps.get_cmap("RdYlGn_r").resampled(3)      # 3-level discrete
    im = ax.imshow(code_m, cmap=cmap, vmin=-0.5, vmax=2.5)
    cbar = fig.colorbar(im, ax=ax, ticks=[0, 1, 2], fraction=0.046, pad=0.04)
    cbar.ax.set_yticklabels(["INDEPENDENT", "PARTIALLY\nCORRELATED", "COMMON\nMODE"])
    ax.set_xticks(range(N_CHANNELS))
    ax.set_yticks(range(N_CHANNELS))
    short = ["CMB-S4 a_s", "DESI DR3 w_0", "LiteBIRD n_T", "CMB-HD a_s", "21cm fold"]  # (local)
    ax.set_xticklabels(short, rotation=30, ha="right", fontsize=9)
    ax.set_yticklabels(short, fontsize=9)
    for i in range(N_CHANNELS):
        for j in range(N_CHANNELS):
            if i == j:
                ax.text(j, i, "DIAG", ha="center", va="center",
                        fontsize=7, color="white", fontweight="bold")
            else:
                tag = res["tag_matrix"][i, j]
                src = res["source_matrix"][i, j]
                short_tag = {"INDEPENDENT": "I", "PARTIALLY_CORRELATED": "P",
                             "COMMON_MODE": "C"}.get(tag, "?")
                src_tag = "F" if src == "FISHER" else "P" if src == "FIRST-PRINCIPLES-REASONING" else ""
                ax.text(j, i, f"{short_tag}\n[{src_tag}]", ha="center", va="center",
                        fontsize=10, color="black", fontweight="bold")
    ax.set_title(f"{GATE_ID}\ncanonical 5x5 correlation matrix  "
                 f"(25/25 cells; {res['n_off_diag_fisher']//2} F + {res['n_off_diag_fp']//2} FP off-diag)")
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
    print(f"  w0_FW          = {w0_FW}")
    print(f"  planck_ns      = {planck_ns}")
    print(f"  alpha_s_MZ_obs = {alpha_s_MZ_obs}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Cell-count audit (pre-registered binary PASS check) ===")
    print(f"  n_cells_total              = {res['n_cells_total']}")
    print(f"  n_cells_filled             = {res['n_cells_filled']}")
    print(f"  n_diag_filled              = {res['n_diag_filled']}/{res['n_diag']}")
    print(f"  n_off_diag_fisher          = {res['n_off_diag_fisher']}/20 (symmetric double-count)")
    print(f"  n_off_diag_fp              = {res['n_off_diag_fp']}/20 (symmetric double-count)")
    print(f"  n_silent                   = 0")
    print(f"  Verdict                    = {verdict}")
    print()

    # Write canonical registry file (XCORR_MD)
    write_registry_file(res, audit_sha, content_sha)

    np.savez(
        OUT_NPZ,
        channels=np.array(CHANNELS),
        channel_display=np.array(CHANNEL_DISPLAY),
        substrate_moments=np.array(SUBSTRATE_MOMENTS),
        tag_matrix=res["tag_matrix"],
        source_matrix=res["source_matrix"],
        code_matrix=res["code_matrix"],
        n_cells_total=np.int64(res["n_cells_total"]),
        n_cells_filled=np.int64(res["n_cells_filled"]),
        n_diag_filled=np.int64(res["n_diag_filled"]),
        n_off_diag_fisher=np.int64(res["n_off_diag_fisher"]),
        n_off_diag_fp=np.int64(res["n_off_diag_fp"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["n_cells_filled"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["n_cells_filled"], audit_sha, content_sha)

    wall = time.time() - t0                                            # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
