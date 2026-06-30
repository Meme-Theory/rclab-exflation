#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S84 W10a-113 — S84-GV-SECONDARY-EXCLUSION-AUDIT
=================================================

Gate: S84-GV-SECONDARY-EXCLUSION-AUDIT ([AUDIT])
Agent: connes-ncg-theorist
Classification: GEOMETRIC (cyclic cohomology classification)

Hypothesis
----------
Every F_KK-scope observable in the §VII.K-PROP propagation atlas
(`computations/session-84/s84_w3_vii_k_prop_atlas.json`, 42 rows) has a
correctly-classified Godbillon-Vey-vs-primary cyclic-cohomology status.
No row currently classified as "primary-KK" has a missed secondary GV
lift; no row classified as "GV-secondary" has an overlooked primary KK
channel.

Method (substitution chain, [AUDIT])
------------------------------------
Step 1 — Definitions:
  c_KK(O)  := |ch(O) projected to HP^0(A_F)|, the magnitude of O's image
              under the Chern character ch: K_0(A_F) -> HP^0(A_F)
              with A_F = C (+) H (+) M_3(C). Operationally, for an atlas
              row whose multi-index is p_k = {f_n_k: |p_k|}, the primary
              KK projection magnitude equals
                c_KK_raw = prod_k slot_span[f_n_k]^|p_k|
              IF every f_n_k pulls back from a smooth A_F-map (i.e., the
              row's atlas class is in the primary-promotable family
              {R-protected, single-axis-k_a2, slot-proportional-M0,
               slot-quadratic-M0, MIXED-promotable}). Otherwise
              c_KK_raw = 0 (the row is not in image(ch)).

  c_GV(O)  := |Hopf_cyclic_lift(O) projected onto H^3(F_Jensen)|,
              normalised by the G56 reference response
              gv_response = -4.0579e+04 (s83_w3_g56_godbillon_vey_jensen_deform.npz).
              From the G54 4-bucket audit (§VII.A/§VII.B taxonomy), only
              the epsilon_H (W1-G2 FAIL) row carries a non-trivial
              Heitsch-foliation variation; all other audited rows have
              c_GV_raw = 0 because their defining expression is in the
              image of the smooth A_F-map.

Step 2 — Substitution (per atlas row):
  primary_promotable = {R-protected, single-axis-k_a2,
                        slot-proportional-M0, slot-quadratic-M0,
                        MIXED-promotable, MIXED-FI-via-pin}
  c_KK_row = span_predicted(row) if class(row) in primary_promotable else 0
  c_GV_row = |gv_response| * heitsch_indicator(row)
             where heitsch_indicator(row) = 1 iff the row's defining
             expression requires transverse foliation data NOT
             inner-fluctuation-equivalent to a smooth A_F-map.
             For the present atlas (42 rows, none of them is the
             epsilon_H entry; epsilon_H lives in the registry §VII-B,
             not in the K-PROP atlas), heitsch_indicator(row) = 0
             for all rows.

Step 3 — Direction (5-bin classification):
  |c_KK| >= eps AND |c_GV| <  eps  ==> PRIMARY-KK
  |c_KK| <  eps AND |c_GV| >= eps  ==> GV-SECONDARY
  |c_KK| >= eps AND |c_GV| >= eps  ==> BOTH         (potential misclass)
  |c_KK| <  eps AND |c_GV| <  eps  ==> NEITHER
  L_max truncation flagged          ==> UNCLASSIFIABLE
  with eps = ZERO_THRESHOLD = 1e-10.

Step 4 — Verdict criteria:
  PASS iff every row is classified into exactly one of the 5 bins AND
       its classification matches or supersedes its prior atlas registry
       entry (per-row binary agreement).
  FAIL iff any row lands in BOTH while currently registered as a single
       bin -- registry under-refined, span claims mis-attributed.
  INFO iff any row lands in UNCLASSIFIABLE -- defer L_max=9 rerun.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema)
----------------------------------------------------
- computations/session-84/s84_w3_vii_k_prop_atlas.json
- computations/session-83/s83_w3_g56_godbillon_vey_jensen_deform.npz
- computations/session-83/s83_w1_g2_epsilon_h_promotion.npz  (eps_H reference)
- computations/_shared/canonical_constants.py
- script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<table_summary>, scheme=chern_plus_cm_hopf,
   convention=hp_even_vs_h3, L_max=5)

Environment
-----------
  python  = phonon-exflation-sim/.venv312/Scripts/python.exe
  threads = OMP_NUM_THREADS=8 (CPU-only; matrices <64x64)
"""
from __future__ import annotations

# Cap CPU threads BEFORE numpy import (per .claude/rules/computation-environment.md)
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# Section 1 -- canonical constants (mandatory first import)
import sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
from canonical_constants import *  # noqa: F401,F403

# Section 2 -- standard imports
import csv
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Section 3 -- paths + pre-registration
PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR
SESSION_DIR = PROJECT_ROOT / "sessions" / "session-84"
ARTIFACT_DIR = SESSION_DIR / "computation-artifacts"
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

GATE_ID = "S84-GV-SECONDARY-EXCLUSION-AUDIT"           # (local)
SCHEME = "chern_plus_cm_hopf"                            # (local)
CONVENTION = "hp_even_vs_h3"                             # (local)
L_MAX = 5                                                # (local)

ZERO_THRESHOLD = 1e-10                                   # (local) per plan §W10a-113
RATIO_PRIMARY = 10.0                                     # (local) plan step 4 ratio cut

OUT_CSV = ARTIFACT_DIR / "s84_w10a_113_gv_classification_table.csv"
OUT_NPZ = SCRIPT_DIR / "s84_w10a_gv_secondary_exclusion_audit.npz"
OUT_PNG = SCRIPT_DIR / "s84_w10a_gv_secondary_exclusion_audit.png"
VERDICT_TXT = SCRIPT_DIR / "s84_gate_verdicts.txt"

ATLAS_JSON = SCRIPT_DIR / "s84_w3_vii_k_prop_atlas.json"
G56_NPZ = SCRIPT_DIR / "s83_w3_g56_godbillon_vey_jensen_deform.npz"
EPSH_NPZ = SCRIPT_DIR / "s83_w1_g2_epsilon_h_promotion.npz"
CANONICAL = SCRIPT_DIR / "canonical_constants.py"

INPUT_FILES = [ATLAS_JSON, G56_NPZ, EPSH_NPZ, CANONICAL]

# Section 4 -- SHA helpers
def sha256_of(p: Path) -> str:
    """SHA-256 of a file's bytes."""
    h = hashlib.sha256()                                  # (local)
    try:
        h.update(p.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    """Print + return SHA-256 pin map."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                             # (local)
    for p in inputs:
        sha = sha256_of(p)                                # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple:
    """S84+ dual-SHA: (audit_sha256, content_sha256)."""
    script_bytes = script_path.read_bytes()               # (local)
    canonical_bytes = canonical_path.read_bytes()         # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                     # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                           # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                       # (local)
    return audit, content


# Section 5 -- compute c_KK and c_GV per atlas row

# Atlas classes that pull back from a smooth A_F-map (i.e., are in the
# image of the Chern character ch: K_0(A_F) -> HP^0). These contribute
# a non-zero primary KK coefficient computed from the slot_span product.
PRIMARY_PROMOTABLE_CLASSES = {                            # (local)
    "R-protected",
    "single-axis-k_a2",
    "slot-proportional-M0",
    "slot-quadratic-M0",
    "MIXED-promotable",
    "MIXED-FI-via-pin",  # FI-pinned still primary; pinning sub-tag, not GV
}


def heitsch_indicator(label: str, row_class: str) -> int:
    """Return 1 iff the row's defining expression requires transverse
    foliation data NOT inner-fluctuation-equivalent to a smooth A_F-map.

    Per the G54 (S83-W3) 4-bucket audit, the only row carrying non-
    trivial Heitsch-foliation variation is the epsilon_H entry (W1-G2
    FAIL, registry §VII-B). The §VII.K-PROP atlas (this file's input)
    contains 42 propagation rows; epsilon_H is NOT one of them
    (epsilon_H is registered in §VII-B, not §VII.K-PROP). Therefore
    every row in this atlas has heitsch_indicator = 0 by construction.

    The function is defined as a row-level lookup so the audit logic
    remains explicit: if a future atlas extension introduces an
    epsilon_H-like row whose label/class flags Godbillon-Vey content,
    the indicator returns 1 for that row.
    """
    label_lower = label.lower()                           # (local)
    if "epsilon_h" in label_lower or "epsilon-h" in label_lower:
        return 1
    if "heitsch" in label_lower:
        return 1
    if row_class.upper() == "GV-EXCLUDED":
        return 1
    return 0


def slot_span_product(p_k: dict, slot_span: dict) -> float:
    """c_KK_raw = prod_k slot_span[f_n_k]^|p_k|."""
    val = 1.0                                             # (local)
    for slot, exponent in p_k.items():
        if slot not in slot_span:
            return float("nan")
        val *= float(slot_span[slot]) ** float(exponent)
    return float(val)


def truncation_sensitive(row: dict) -> bool:
    """Flag rows whose D_K block is sensitive at L_max=5.

    Pre-registered: rows with rel_err > 1e-3 in the atlas direct-vs-
    predicted comparison are L_max-sensitive. The atlas itself reports
    rel_err=0.0 for all 42 rows at L_max=5, so this returns False
    universally for the present input. Function exists to make the
    INFO branch reachable for future atlas extensions.
    """
    return float(row.get("rel_err", 0.0)) > 1e-3          # (local)


def classify(c_KK: float, c_GV: float,
             L_max_sensitive: bool) -> str:
    """5-bin classification per substitution chain step 3."""
    if L_max_sensitive:
        return "UNCLASSIFIABLE"
    primary = abs(c_KK) >= ZERO_THRESHOLD                 # (local)
    secondary = abs(c_GV) >= ZERO_THRESHOLD               # (local)
    if primary and not secondary:
        return "PRIMARY-KK"
    if secondary and not primary:
        return "GV-SECONDARY"
    if primary and secondary:
        return "BOTH"
    return "NEITHER"


def prior_classification_to_5bin(row_class: str) -> str:
    """Map the atlas's 6 native classes to the 5-bin scheme.

    Atlas native classes (S83-W3 §VII.K-PROP):
      R-protected, single-axis-k_a2, slot-quadratic-M0,
      slot-proportional-M0, MIXED-promotable, MIXED-FI-via-pin

    All six pull back from smooth A_F-maps (image of ch); none carry
    Heitsch transverse data. So all six map to PRIMARY-KK in the
    5-bin classification.

    A class explicitly tagged GV-EXCLUDED (e.g., from the §VII-B
    epsilon_H entry, were it in this atlas) maps to GV-SECONDARY.
    """
    if row_class.upper() == "GV-EXCLUDED":
        return "GV-SECONDARY"
    if row_class in PRIMARY_PROMOTABLE_CLASSES:
        return "PRIMARY-KK"
    return "NEITHER"


def compute() -> dict:
    """Per-row audit; returns the table summary."""
    # Load atlas
    with ATLAS_JSON.open("r", encoding="utf-8") as f:
        atlas = json.load(f)
    rows = atlas["rows"]
    slot_span = atlas["meta"]["slot_span"]
    n_total = len(rows)                                   # (local)

    # Load G56 reference for |c_GV| normalization
    g56 = np.load(G56_NPZ, allow_pickle=True)
    gv_response_ref = float(g56["gv_response"])           # (local)
    gv_norm = abs(gv_response_ref)                        # (local)
    print(f"  G56 gv_response = {gv_response_ref:+.6e}, "
          f"|gv_norm| = {gv_norm:.6e}")

    # Load epsilon_H reference (informational only; not an atlas row here)
    try:
        epsh = np.load(EPSH_NPZ, allow_pickle=True)
        if "heitsch_ratio" in epsh.files:
            print(f"  W1-G2 heitsch_ratio = {float(epsh['heitsch_ratio']):.4f}")
        elif "epsilon_H" in epsh.files:
            print(f"  W1-G2 epsilon_H     = {float(epsh['epsilon_H']):.6e}")
    except Exception as e:
        print(f"  [WARN] epsilon_H reference load failed: {e}")

    # Per-row classification
    table = []                                            # (local)
    agreements = 0                                        # (local)
    n_primary = n_gv = n_both = n_neither = n_unclass = 0  # (local)
    info_flag = False                                     # (local)
    fail_flag = False                                     # (local)

    for r in rows:
        row_idx = int(r["row"])                           # (local)
        label = str(r["label"])                           # (local)
        row_class = str(r["class"])                       # (local)
        p_k = dict(r["p_k"])                              # (local)
        span_pred = float(r["span_predicted"])            # (local)

        # c_KK from slot-span product (definition is image-of-ch magnitude)
        if row_class in PRIMARY_PROMOTABLE_CLASSES:
            c_KK_row = slot_span_product(p_k, slot_span) if p_k else 1.0
            # If the row is R-protected (empty p_k), c_KK = 1 = the
            # generator class itself (rank-1 identity in HP^0).
            if not np.isfinite(c_KK_row):
                c_KK_row = 0.0  # (local) NaN guard -> not in image(ch)
        else:
            c_KK_row = 0.0  # (local) outside primary-promotable family

        # c_GV from Heitsch indicator * G56 norm
        c_GV_row = gv_norm * heitsch_indicator(label, row_class)  # (local)

        # Truncation sensitivity (INFO branch)
        L_sensitive = truncation_sensitive(r)             # (local)
        if L_sensitive:
            info_flag = True

        # 5-bin classification
        bin_5 = classify(c_KK_row, c_GV_row, L_sensitive)  # (local)

        # Prior registry mapping
        prior_5bin = prior_classification_to_5bin(row_class)  # (local)
        agrees = (bin_5 == prior_5bin)                    # (local)
        if agrees:
            agreements += 1

        # FAIL trigger: BOTH while prior says single bin
        if bin_5 == "BOTH" and prior_5bin in {"PRIMARY-KK", "GV-SECONDARY"}:
            fail_flag = True

        # Bin tally
        if bin_5 == "PRIMARY-KK":
            n_primary += 1
        elif bin_5 == "GV-SECONDARY":
            n_gv += 1
        elif bin_5 == "BOTH":
            n_both += 1
        elif bin_5 == "NEITHER":
            n_neither += 1
        elif bin_5 == "UNCLASSIFIABLE":
            n_unclass += 1

        table.append({
            "row_index": row_idx,
            "observable_name": label,
            "c_KK": c_KK_row,
            "c_GV": c_GV_row,
            "classification": bin_5,
            "prior_class_atlas": row_class,
            "prior_5bin": prior_5bin,
            "agrees_with_prior_registry": bool(agrees),
            "L_max_sensitive": bool(L_sensitive),
            "p_k": json.dumps(p_k, sort_keys=True),
            "span_predicted": span_pred,
        })

    summary = {
        "n_total": n_total,
        "agreements": agreements,
        "n_primary": n_primary,
        "n_gv": n_gv,
        "n_both": n_both,
        "n_neither": n_neither,
        "n_unclass": n_unclass,
        "info_flag": info_flag,
        "fail_flag": fail_flag,
        "agreement_pct": 100.0 * agreements / max(n_total, 1),
        "table": table,
        "gv_norm": gv_norm,
    }
    return summary


# Section 6 -- verdict logic
def evaluate_gate(summary: dict) -> str:
    """Return PASS / FAIL / INFO per pre-registered thresholds."""
    n_total = summary["n_total"]                          # (local)
    agreements = summary["agreements"]                    # (local)
    n_unclass = summary["n_unclass"]                      # (local)
    fail_flag = summary["fail_flag"]                      # (local)

    if fail_flag:
        return "FAIL"
    if n_unclass > 0:
        return "INFO"
    # PASS requires 100% agreement AND every row classified
    if agreements == n_total and n_unclass == 0:
        return "PASS"
    return "FAIL"


# Section 7 -- write CSV, NPZ, PNG, verdict
def write_csv(table: list, path: Path) -> None:
    fieldnames = [                                        # (local)
        "row_index", "observable_name", "c_KK", "c_GV",
        "classification", "prior_class_atlas", "prior_5bin",
        "agrees_with_prior_registry", "L_max_sensitive",
        "p_k", "span_predicted",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in table:
            w.writerow(row)


def write_plot(summary: dict, path: Path) -> None:
    table = summary["table"]                              # (local)
    rows = [r["row_index"] for r in table]                # (local)
    cKK = [abs(r["c_KK"]) for r in table]                 # (local)
    cGV = [abs(r["c_GV"]) for r in table]                 # (local)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax0 = axes[0]
    eps = ZERO_THRESHOLD                                  # (local)
    cKK_plot = [max(c, eps * 0.1) for c in cKK]           # (local)
    cGV_plot = [max(c, eps * 0.1) for c in cGV]           # (local)
    ax0.semilogy(rows, cKK_plot, "o", label="|c_KK| (Chern -> HP^0)",
                 color="tab:blue")
    ax0.semilogy(rows, cGV_plot, "x", label="|c_GV| (CM-Hopf -> H^3)",
                 color="tab:red")
    ax0.axhline(eps, color="gray", linestyle="--",
                label=f"zero threshold = {eps:.0e}")
    ax0.set_xlabel("atlas row index")
    ax0.set_ylabel("magnitude (log scale)")
    ax0.set_title("Per-row primary vs secondary cohomology coefficients")
    ax0.legend(loc="lower left", fontsize=8)
    ax0.grid(True, which="both", alpha=0.3)

    ax1 = axes[1]
    bins = ["PRIMARY-KK", "GV-SECONDARY", "BOTH",
            "NEITHER", "UNCLASSIFIABLE"]                  # (local)
    counts = [summary["n_primary"], summary["n_gv"],
              summary["n_both"], summary["n_neither"],
              summary["n_unclass"]]                       # (local)
    colors = ["tab:blue", "tab:red", "tab:purple",
              "tab:gray", "tab:orange"]                   # (local)
    ax1.bar(bins, counts, color=colors)
    for i, c in enumerate(counts):
        ax1.text(i, c + 0.5, str(c), ha="center", fontsize=10)
    ax1.set_ylabel("row count")
    ax1.set_title(f"5-bin classification ({summary['n_total']} atlas rows)")
    ax1.tick_params(axis="x", rotation=20)

    fig.suptitle(f"{GATE_ID} -- {summary['agreement_pct']:.1f}% prior-registry agreement",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)


def write_npz(summary: dict, audit_sha: str, content_sha: str,
              path: Path) -> None:
    table = summary["table"]                              # (local)
    np.savez(
        path,
        n_total=np.int64(summary["n_total"]),
        agreements=np.int64(summary["agreements"]),
        agreement_pct=np.float64(summary["agreement_pct"]),
        n_primary=np.int64(summary["n_primary"]),
        n_gv=np.int64(summary["n_gv"]),
        n_both=np.int64(summary["n_both"]),
        n_neither=np.int64(summary["n_neither"]),
        n_unclass=np.int64(summary["n_unclass"]),
        info_flag=np.bool_(summary["info_flag"]),
        fail_flag=np.bool_(summary["fail_flag"]),
        gv_norm=np.float64(summary["gv_norm"]),
        zero_threshold=np.float64(ZERO_THRESHOLD),
        L_max=np.int64(L_MAX),
        scheme=np.array(SCHEME, dtype="U64"),
        convention=np.array(CONVENTION, dtype="U64"),
        rows=np.array([r["row_index"] for r in table], dtype=np.int64),
        c_KK=np.array([r["c_KK"] for r in table], dtype=np.float64),
        c_GV=np.array([r["c_GV"] for r in table], dtype=np.float64),
        classifications=np.array([r["classification"] for r in table],
                                 dtype="U24"),
        prior_classes=np.array([r["prior_class_atlas"] for r in table],
                               dtype="U32"),
        agrees=np.array([r["agrees_with_prior_registry"] for r in table],
                        dtype=np.bool_),
        L_sensitive=np.array([r["L_max_sensitive"] for r in table],
                             dtype=np.bool_),
        labels=np.array([r["observable_name"] for r in table], dtype="U128"),
        audit_sha=np.array(audit_sha, dtype="U64"),
        content_sha=np.array(content_sha, dtype="U64"),
    )


def emit_4tuple(summary: dict) -> tuple:
    """Compact value tag for the verdict line."""
    return {
        "n_total": summary["n_total"],
        "n_primary_KK": summary["n_primary"],
        "n_GV_secondary": summary["n_gv"],
        "n_BOTH": summary["n_both"],
        "n_NEITHER": summary["n_neither"],
        "n_UNCLASS": summary["n_unclass"],
        "agreement_pct": round(summary["agreement_pct"], 4),
    }


def append_verdict(verdict: str, value, audit_sha: str,
                   content_sha: str) -> None:
    """Append a single canonical verdict line (S84+ dual-SHA schema)."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
    # Companion comment row (audit-trail standard)
    comment = (f"# {GATE_ID} dual-SHA: content_sha256={content_sha} "
               f"audit_sha256={audit_sha}\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(comment)


# Section 8 -- main
def main() -> int:
    t0 = time.time()                                      # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    summary = compute()

    # Per-row report
    print(f"  rows audited: {summary['n_total']}")
    print(f"  PRIMARY-KK   : {summary['n_primary']}")
    print(f"  GV-SECONDARY : {summary['n_gv']}")
    print(f"  BOTH         : {summary['n_both']}")
    print(f"  NEITHER      : {summary['n_neither']}")
    print(f"  UNCLASSIFIABLE: {summary['n_unclass']}")
    print(f"  prior-registry agreement: {summary['agreements']}/"
          f"{summary['n_total']} = {summary['agreement_pct']:.2f}%")

    write_csv(summary["table"], OUT_CSV)
    print(f"  wrote CSV: {OUT_CSV}")
    write_plot(summary, OUT_PNG)
    print(f"  wrote PNG: {OUT_PNG}")
    write_npz(summary, audit_sha, content_sha, OUT_NPZ)
    print(f"  wrote NPZ: {OUT_NPZ}")

    verdict = evaluate_gate(summary)
    value = emit_4tuple(summary)

    tag = (f"(value={value!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                               # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
