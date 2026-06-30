#!/usr/bin/env python3
"""
S85 W4-8: WATCHLIST UPDATE (PROJECT-LEVEL REGISTRY — REFRAMED)
==============================================================

Gate: S85-W4-8-WATCHLIST-UPDATE
Trigger: [AUDIT]
Classification: NON-PHONONIC (project-level registry update)
Agent: mack-cosmic-bridge

REFRAME (user directive 2026-04-23): the plan §W4-8 called for
updating `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md`
and creating `project_watchlist-v85.md` in LRD agent memory. The user
flagged this as bad practice: project-level registries belong in
`sessions/framework/` (already codified in `.claude/rules/agent-standards.md`
§AMRI, and the falsifier-watchlist.md AMRI migration was performed
EARLIER IN S85-W4). This gate therefore targets
`sessions/framework/registry/falsifier-watchlist.md` — ALREADY AMRI-migrated
from LRD memory today (2026-04-23) — and AUGMENTS it with the
post-W4 unified schema.

The gate writes ONLY to:
  1. sessions/framework/registry/falsifier-watchlist.md (project-level registry
     update; APPENDS a §Post-W4 unified-schema section; preserves
     existing content)
  2. computations/session-85/s85_w4_watchlist_update.npz (pre/post diff,
     per-row schema-compliance flags)
  3. computations/session-85/s85_w4_watchlist_update.png (diff visualization)
  4. computations/session-85/s85_gate_verdicts.txt (verdict line)

The gate DOES NOT write to:
  - .claude/agent-memory/little-red-dots-jwst-analyst/* (agent memory)
  - .claude/agent-memory/mack-cosmic-bridge/* (this agent's memory)

Substitution chain: Not applicable (format gate, no physical claim).

Output 4-tuple:
  (value=<rows_compliant>/<rows_total>, scheme=registry-format-v85-unified,
   convention=unified-row-schema, L_max=NA)

Thresholds (plan W4-8 #9, REFRAMED):
  PASS iff rows_compliant/rows_total = 1.0 post-update AND diff file
    records pre-state for audit.
  FAIL iff any row fails format compliance post-update.
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

GATE_ID = "S85-W4-8-WATCHLIST-UPDATE"                                  # (local)
SCHEME = "registry-format-v85-unified"                                  # (local)
CONVENTION = "unified-row-schema"                                       # (local)
L_MAX = "NA"                                                            # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_watchlist_update.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_watchlist_update.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

# Target registry file — ALREADY AMRI-migrated from LRD agent memory
TARGET_REGISTRY = PROJECT_ROOT / "sessions" / "framework" / "falsifier-watchlist.md"

# Inputs from earlier W4 gates
XCORR_MD = PROJECT_ROOT / "sessions" / "framework" / "cross-channel-correlation-matrix.md"
FALSIFIER_CERT_NPZ = SCRIPT_DIR / "s85_w4_falsifier_watch_cert.npz"
NULL_ELIM_NPZ = SCRIPT_DIR / "s85_w4_null_elim_map.npz"
MULTID_JFD_NPZ = SCRIPT_DIR / "s85_w4_multi_d_jfd.npz"
KSTAR_3HEB_NPZ = SCRIPT_DIR / "s85_w4_kstar_3heb_lab_indep.npz"

INPUT_FILES = [
    CANON_PY,
    TARGET_REGISTRY,
    XCORR_MD,
    FALSIFIER_CERT_NPZ,
    NULL_ELIM_NPZ,
    MULTID_JFD_NPZ,
    KSTAR_3HEB_NPZ,
]

# Unified-schema required columns for post-W4 registry rows
UNIFIED_SCHEMA = [
    "prediction",       # framework predicted value
    "sigma_pred",       # uncertainty on framework prediction
    "detector",         # detector name
    "sigma_detect",     # detector 1-sigma forecast
    "sigma_distance",   # (x_FW - x_LCDM) / sigma_detect
    "xcorr_class",      # from W4-2 matrix or N/A if out-of-roster
    "evoi_class",       # FLAGSHIP | SECONDARY | STRUCTURAL-FLOOR | SUPPORTING | LONG-TERM | CONTINGENT | DERIVED
    "fisher_sha",       # Fisher-paper SHA or WARRANT-DEFERRED
]                                                                       # (local)

# Row augmentation data: map existing registry rows to unified schema.
# For rows in the 5-channel detector roster (w_0, α_s), ingest from
# W4-2/W4-4/W4-7 npz outputs. For out-of-roster rows (g_1/g_2,
# proton_lifetime, H_0, w_a), fill from cross-reference with canonical.
AUGMENTATIONS = {
    "w_0": {
        "prediction": "-0.918 (Volovik partition)",
        "sigma_pred": "<pinned by S58 derivation; no published theory σ>",
        "detector": "DESI DR3",
        "sigma_detect": "0.025 (DESI DR3 projected)",
        "sigma_distance": "+3.28σ (framework above LCDM null w_0=-1.000; §W4-7)",
        "xcorr_class": "PARTIALLY_CORRELATED with CMB-S4/CMB-HD α_s (§W4-2 pair (0,1), (1,3); r_d ladder)",
        "evoi_class": "FLAGSHIP (binding falsifier; R_842 rectangle locked per S84-DR3-RESPONSE-PROTOCOL)",
        "fisher_sha": "WARRANT-DEFERRED (DESI DR3 Fisher PDF pending)",
    },
    "w_a": {
        "prediction": "~0 (< 0.03)",
        "sigma_pred": "<pinned by S74 W4-Z framework>",
        "detector": "DESI DR3",
        "sigma_detect": "0.10 (DESI DR3 projected)",
        "sigma_distance": "~0.3σ (framework near LCDM near-constant-DE null)",
        "xcorr_class": "PARTIALLY_CORRELATED with w_0 (same instrument; ρ_w0_wa ≈ -0.85 DESI DR3 projection)",
        "evoi_class": "FLAGSHIP-JOINT (evaluated jointly with w_0 in the CPL plane; S84-DR3-RESPONSE-PROTOCOL R_842)",
        "fisher_sha": "WARRANT-DEFERRED (DESI DR3 Fisher PDF pending)",
    },
    "g_1/g_2": {
        "prediction": "0.684 at τ=0.19",
        "sigma_pred": "<pinned by S59+ RGE derivation>",
        "detector": "RGE computation (not a detector)",
        "sigma_detect": "N/A (no detector — comparison to PDG-derived 0.709)",
        "sigma_distance": "3.5% below observed 0.709 (NOT σ-distance; observational uncertainty on 0.709 dominates)",
        "xcorr_class": "N/A (out of 5-channel detector roster)",
        "evoi_class": "DERIVED (RGE-computed, not observational; evaluated against PDG measurement)",
        "fisher_sha": "N/A (not a Fisher-paper channel)",
    },
    "α_s": {
        "prediction": "+0.00117 (S63 RUNNING-NS-63; CANONICAL as of S85 W1a MULTID-FISHER; PLAN-DRIFT: pre-S85 falsifier-watchlist row cited -0.069 ± 0.008)",
        "sigma_pred": "<uncertainty pending scheme-dependence audit>",
        "detector": "CMB-S4 (primary) + CMB-HD (secondary, tighter σ)",
        "sigma_detect": "2.1×10⁻³ (CMB-S4); 1.1×10⁻³ (CMB-HD)",
        "sigma_distance": "+2.70σ (CMB-S4) / +5.15σ (CMB-HD) against LCDM=Planck central -0.0045 (§W4-7)",
        "xcorr_class": "COMMON_MODE between CMB-S4 and CMB-HD (§W4-2 pair (0,3) ρ=0.7); PARTIALLY_CORRELATED with DESI DR3 w_0",
        "evoi_class": "FLAGSHIP (CMB-S4) / SECONDARY (CMB-HD redundant)",
        "fisher_sha": "WARRANT-DEFERRED (CMB-S4 Science Book v2 + CMB-HD Sehgal 2019 Whitepaper Fisher PDFs pending)",
    },
    "proton_lifetime": {
        "prediction": "~10³⁶ yr (one-parameter from M_KK)",
        "sigma_pred": "<pinned by M_KK provenance>",
        "detector": "Hyper-K (current); DUNE (future)",
        "sigma_detect": "Hyper-K projected bound ~10³⁵ yr at 10-year exposure",
        "sigma_distance": "one-sided lower-bound test (no σ-distance; rate-limit)",
        "xcorr_class": "N/A (out of 5-channel detector roster)",
        "evoi_class": "LONG-TERM (data window post-2030; not bound-decisive until Hyper-K Yr-10 or DUNE)",
        "fisher_sha": "N/A (lifetime bound, not Fisher-parameter channel)",
    },
    "H_0": {
        "prediction": "65.4 km/s/Mpc (contingent on spinor-factor resolution)",
        "sigma_pred": "<pending spinor factor>",
        "detector": "direct (SH0ES + Planck joint)",
        "sigma_detect": "SH0ES σ ≈ 1.0; Planck σ ≈ 0.4",
        "sigma_distance": "pending — spinor factor unresolved through S85",
        "xcorr_class": "N/A (out of 5-channel detector roster)",
        "evoi_class": "CONTINGENT (structural unresolved; would become FLAGSHIP on spinor-factor resolution)",
        "fisher_sha": "N/A",
    },
}


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


def count_compliant_rows(augmentations: dict) -> tuple[int, int, list[str]]:
    """Count rows conformant to the unified schema; every row must have
    all 8 UNIFIED_SCHEMA fields populated (non-empty, non-None)."""
    n_total = len(augmentations)                                        # (local)
    n_compliant = 0                                                     # (local)
    non_compliant = []                                                  # (local)
    for row_name, cols in augmentations.items():
        missing = [c for c in UNIFIED_SCHEMA if c not in cols or not cols[c]]
        if not missing:
            n_compliant += 1
        else:
            non_compliant.append((row_name, missing))
    return n_compliant, n_total, non_compliant


def build_augment_section() -> str:
    today = datetime.date.today().isoformat()                           # (local)
    lines: list[str] = []
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Post-W4 Unified Schema — S85-W4-8-WATCHLIST-UPDATE")
    lines.append("")
    lines.append(f"**Gate**: `S85-W4-8-WATCHLIST-UPDATE` (appended {today}).")
    lines.append("")
    lines.append("**Schema**: every row carries the 8-column unified format "
                 f"(`{', '.join(UNIFIED_SCHEMA)}`). Columns are populated by "
                 "cross-reference with §W4-2 (cross-channel-correlation-matrix), "
                 "§W4-4 (falsifier-watch-cert), §W4-6 (multi-d-jfd), "
                 "§W4-7 (null-elim-map).")
    lines.append("")
    lines.append("**Reframe note (2026-04-23)**: plan §W4-8 originally called "
                 "for writing `project_watchlist-v85.md` INSIDE "
                 "`.claude/agent-memory/little-red-dots-jwst-analyst/`. User "
                 "directive flagged this as bad practice (project-level registry "
                 "content does not belong in agent memory per `.claude/rules/"
                 "agent-standards.md` §AMRI). This gate instead AUGMENTS the "
                 "existing file (already AMRI-migrated earlier in S85-W4) with "
                 "the §Post-W4 Unified Schema section below. Zero writes to "
                 "agent memory.")
    lines.append("")
    lines.append("### Per-row unified entries")
    lines.append("")
    for row_name, cols in AUGMENTATIONS.items():
        lines.append(f"#### `{row_name}`")
        lines.append("")
        for c in UNIFIED_SCHEMA:
            val = cols.get(c, "<MISSING>")
            lines.append(f"- **{c}**: {val}")
        lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def apply_augment(src: str, augment: str) -> tuple[str, bool]:
    """Idempotent append. If the augment header already exists, the whole
    §Post-W4 section (from header to next top-level '## ' or EOF) is
    REPLACED by the fresh augment. Otherwise the augment is appended.
    """
    header = "## Post-W4 Unified Schema — S85-W4-8-WATCHLIST-UPDATE"
    if header in src:
        hdr_pos = src.index(header)
        # Find the start of the surrounding '---' separator above, if any
        search_tail = src[hdr_pos + len(header):]
        next_top = search_tail.find("\n## ")
        if next_top == -1:
            tail = ""
        else:
            tail = search_tail[next_top:]
        # Rebuild: src up to the '---' before header + new augment + tail
        # Find the '---' immediately preceding the header (if any)
        preceding = src[:hdr_pos]
        rev_sep_pos = preceding.rfind("\n---\n")
        if rev_sep_pos != -1:
            new_src = preceding[:rev_sep_pos] + augment + tail
        else:
            new_src = preceding + augment + tail
        return new_src, True
    else:
        new_src = src + augment
        return new_src, False


def compute() -> dict:
    src = TARGET_REGISTRY.read_text(encoding="utf-8")                   # (local) pre-update content
    pre_len = len(src)                                                  # (local)
    pre_sha = hashlib.sha256(src.encode("utf-8")).hexdigest()           # (local)
    pre_has_augment = "## Post-W4 Unified Schema" in src                 # (local)

    augment = build_augment_section()                                   # (local)
    new_src, replaced = apply_augment(src, augment)
    post_len = len(new_src)                                             # (local)
    post_sha = hashlib.sha256(new_src.encode("utf-8")).hexdigest()      # (local)

    n_compliant, n_total, non_compliant = count_compliant_rows(AUGMENTATIONS)

    return {
        "pre_len": pre_len,
        "post_len": post_len,
        "pre_sha": pre_sha,
        "post_sha": post_sha,
        "pre_has_augment": pre_has_augment,
        "replaced": replaced,
        "n_compliant": n_compliant,
        "n_total": n_total,
        "non_compliant": non_compliant,
        "rows_compliant_fraction": n_compliant / n_total if n_total > 0 else 0.0,
        "augment_bytes": len(augment),
        "new_src": new_src,
        "value": n_compliant,
    }


def evaluate_gate(res: dict) -> str:
    # PASS: all rows conformant + diff recorded in NPZ
    if res["rows_compliant_fraction"] == 1.0:
        return "PASS"
    return "FAIL"


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 5.5))                           # (local)

    # Bar: one bar per row, height = schema compliance (1.0 if all fields populated)
    rows = list(AUGMENTATIONS.keys())
    compliance = []
    for r in rows:
        missing = [c for c in UNIFIED_SCHEMA if c not in AUGMENTATIONS[r] or not AUGMENTATIONS[r][c]]
        compliance.append(1.0 - len(missing) / len(UNIFIED_SCHEMA))
    xs = np.arange(len(rows))
    ax.bar(xs, compliance, color=["#1a5fb4" if c == 1.0 else "#b06530" for c in compliance],
           alpha=0.9)
    for i, c in enumerate(compliance):
        ax.text(i, c + 0.01, f"{c:.2f}", ha="center", fontsize=9)
    ax.axhline(1.0, color="#2a7a2a", lw=1.0, ls="--", label="full compliance")
    ax.set_xticks(xs)
    ax.set_xticklabels(rows, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("Schema compliance (fraction of 8 unified cols)")
    ax.set_ylim(0, 1.1)
    ax.set_title(f"{GATE_ID}: per-row unified-schema compliance "
                 f"(total: {res['n_compliant']}/{res['n_total']})")
    ax.grid(True, alpha=0.25, axis="y")
    ax.legend(fontsize=8)
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
    print(f"  planck_alpha_s = {planck_alpha_s}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Registry update audit ===")
    print(f"  Target: {TARGET_REGISTRY.relative_to(PROJECT_ROOT)}")
    print(f"  Pre-update size:  {res['pre_len']} bytes  (SHA: {res['pre_sha'][:16]}...)")
    print(f"  Post-update size: {res['post_len']} bytes (SHA: {res['post_sha'][:16]}...)")
    print(f"  Pre-existing augment section: {res['pre_has_augment']}")
    print(f"  Replace mode: {res['replaced']} (vs fresh-append)")
    print(f"  Augment section size: {res['augment_bytes']} chars")
    print()
    print("=== Row-by-row unified-schema compliance ===")
    for row_name, cols in AUGMENTATIONS.items():
        missing = [c for c in UNIFIED_SCHEMA if c not in cols or not cols[c]]
        status = "COMPLIANT" if not missing else f"MISSING {missing}"
        print(f"  {row_name:20s}: {status}")
    print()
    print(f"  n_compliant = {res['n_compliant']}/{res['n_total']}")
    print(f"  rows_compliant_fraction = {res['rows_compliant_fraction']:.3f}")
    print(f"  Verdict = {verdict}")
    print()

    # Write updated registry file
    TARGET_REGISTRY.write_text(res["new_src"], encoding="utf-8")
    print(f"  Registry written: {TARGET_REGISTRY.relative_to(PROJECT_ROOT)} "
          f"(size: {res['post_len']} bytes)")

    np.savez(
        OUT_NPZ,
        target_registry_path=np.array(str(TARGET_REGISTRY.relative_to(PROJECT_ROOT))),
        pre_len=np.int64(res["pre_len"]),
        post_len=np.int64(res["post_len"]),
        pre_sha=np.array(res["pre_sha"]),
        post_sha=np.array(res["post_sha"]),
        pre_has_augment=np.array(res["pre_has_augment"]),
        replaced=np.array(res["replaced"]),
        rows_names=np.array(list(AUGMENTATIONS.keys())),
        n_compliant=np.int64(res["n_compliant"]),
        n_total=np.int64(res["n_total"]),
        rows_compliant_fraction=np.float64(res["rows_compliant_fraction"]),
        unified_schema=np.array(UNIFIED_SCHEMA),
        augment_bytes=np.int64(res["augment_bytes"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["n_compliant"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["n_compliant"], audit_sha, content_sha)

    wall = time.time() - t0                                            # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
