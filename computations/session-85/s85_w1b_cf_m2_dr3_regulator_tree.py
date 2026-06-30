#!/usr/bin/env python3
"""
S85 W1b-1: CF-M2 DR3 REGULATOR-CONDITIONAL TREE
===============================================

Gate: S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE
Trigger: [AUDIT]
Classification: META (pre-registration extension; observational binding)
Agent: mack-cosmic-bridge

Hypothesis: The S84 W4-44 fine-grained DR3 contingency matrix (7 cells
A1/A2/B1/B2/B3/C1/C2, sha=801e4690) is regulator-agnostic — it assumes
the framework prediction is the single canonical value w_0 = -0.918.
Amending the 7-cell matrix with a layered regulator-branch condition
(each cell carries 3 sub-verdicts: {L_max=8, L_max=10, L_max=12})
tests whether rectangle R_842 containment is preserved across all
regulator layers, or reveals a regulator-layer-specific exclusion in
at least one DR3 cell.

Method summary:
  The 7 cells partition (w_0, w_a) space (from plan §W1b-1; echoed in
  S85 W0-DR3-REGULATOR-SUCCESSOR-TREE JSON). For each L_max level
  {8, 10, 12}, the framework prediction (w_0(L), w_a(L)) falls into
  exactly one cell; the 21-cell matrix records that cell assignment.
  If the framework prediction flips between cells as L_max varies,
  the DR3 tree is regulator-layer-conditional (FAIL).

Input data (from filesystem; no new compute):
  - canonical_constants.py: w0_FW = -0.918 (L_max=10 Zubarev canonical)
  - s85_w0_dr3_regulator_successor_tree.json: R2 Zubarev L=5 w_0 = -0.918
  - s85_w0_zubarev_lmax_convergence_to_minus_one.* : L_max=12 extrapolated
    Zubarev value = -0.635 (FAIL gate against convergence-to-minus-one)
  - L_max=8: NO PUBLISHED Zubarev value in S85 artifacts;
    this row is marked DATA-UNAVAILABLE.

Substitution chain (Python-verified):
  Step 1: R_842 rectangle (from W0-DR3-REGULATOR-SUCCESSOR-TREE.json):
          w_0 in [-0.942, -0.742], w_a in [-0.2, 0.2];
          center (-0.842, 0), half-widths (0.1, 0.2).
  Step 2: 7-cell partition of (w_0, w_a) space:
          A1: contained AND |w_0 - center| <= 1*half_width_w_0 (1-sigma box)
          A2: contained AND 1*hw < |w_0 - center| <= 2*half_width  (2-sigma box)
          B1: w_0 < R_w0_lo = -0.942 (phantom excursion, still inside CPL)
          B2: w_0 > R_w0_hi = -0.742 (quintessence excursion)
          B3: |w_a| > 0.2 (CPL evolution)
          C1: w_0 < -1.5 (exotic phantom)
          C2: w_0 > -0.5 (exotic quintessence)
          (mutually exclusive; cover full plane)
  Step 3: Framework prediction per L_max (Zubarev scheme, canonical):
          L_max = 5:  w_0 = -0.918, w_a = 0  (W0-successor R2_Zubarev)
          L_max = 8:  DATA-UNAVAILABLE (no S85 Zubarev L=8 computation)
          L_max = 10: w_0 = -0.918, w_a = 0  (canonical w0_FW, S58)
          L_max = 12: w_0 = -0.635, w_a = 0  (S85 W0 Zubarev convergence
                      extrapolation FAIL value)
  Step 4: Cell assignment:
          L=5:  -0.918 in [-0.942, -0.742] AND |w_0 - (-0.842)| = 0.076 <= 0.1
                 => A1 (contained, 1-sigma)
          L=10: same -> A1
          L=12: -0.635 > -0.742 => B2 (quintessence excursion)
  Step 5: Framework-prediction-cell flip test across L_max in {10, 12}:
          cell(L=10) = A1; cell(L=12) = B2; A1 != B2 => FLIP occurs.
  Step 6: Plan §W1b-1 threshold:
          PASS iff all 21 cells preserve S84 W4-44 verdicts across
                   L_max layers -> NOT the case, cell A1 "loses" the
                   framework prediction and B2 "gains" it between
                   L=10 and L=12.
          FAIL iff at least one cell flips IN->OUT (or OUT->IN) when
                   L_max changes by 2 -> YES, this is exactly what
                   happens. VERDICT = FAIL.
  Direction: DR3 tree is regulator-layer-conditional. S86 must
             maintain 3 sub-trees (one per L_max) and DR3-event
             adjudication becomes regulator-first, NOT box-first.

Note: L_max=8 data unavailable. The FAIL verdict is reached by
L_max=10 vs L_max=12 alone. If a subsequent S86 run produces a
Zubarev w_0 at L_max=8 and it falls in a NEW cell (e.g., B1 or
elsewhere), the FAIL is confirmed in MORE detail; it cannot be
overturned.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - s85_w0_dr3_regulator_successor_tree.json
  - s85_w0_zubarev_lmax_convergence_to_minus_one.npz (if present)

Output 4-tuple:
  (value='FLIP-A1-to-B2-at-L12', scheme=Zubarev, convention=R_842-successor, L_max=enumerated{5,10,12})

Thresholds (pre-registered, plan §W1b-1):
  - PASS: all 21 cells preserve verdict across L_max
  - FAIL: at least one cell flips IN->OUT when L_max changes by 2
  - INFO: mixed (some regulator-robust, some not)

Output files:
  - s85_w1b_cf_m2_dr3_regulator_tree.py
  - s85_w1b_cf_m2_dr3_regulator_tree.npz (21-cell matrix)
  - s85_w1b_cf_m2_dr3_regulator_tree.png (heatmap)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import w0_FW  # noqa: E402

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE"            # (local)
SCHEME = "Zubarev"                                                  # (local)
CONVENTION = "R_842-successor"                                      # (local)
L_MAX_LABEL = "enumerated{5,10,12}"                                 # (local)

# R_842 rectangle from W0-DR3-REGULATOR-SUCCESSOR-TREE.json (canonical)
R_W0_LO = -0.942                                                    # (local, W0-successor)
R_W0_HI = -0.742                                                    # (local, W0-successor)
R_WA_LO = -0.20                                                     # (local)
R_WA_HI = +0.20                                                     # (local)
R_W0_CENTER = -0.842                                                # (local) W0-successor center
R_W0_HALFWIDTH = 0.1                                                # (local)

# Framework w_0 predictions per L_max (all Zubarev scheme)
W0_FW_L5 = -0.918                                                   # (local, W0-successor R2 Zubarev)
W0_FW_L10 = w0_FW                                                   # canonical (S58 Volovik + effacement)
W0_FW_L12 = -0.635                                                  # (local, S85 W0 Zubarev convergence extrapolation)
WA_FW_ALL = 0.0                                                     # (local, S74 W4-Z frozen)

OUT_NPZ = SCRIPT_DIR / "s85_w1b_cf_m2_dr3_regulator_tree.npz"
OUT_PNG = SCRIPT_DIR / "s85_w1b_cf_m2_dr3_regulator_tree.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
W0_SUCCESSOR_JSON = SCRIPT_DIR / "s85_w0_dr3_regulator_successor_tree.json"
W0_ZUBAREV_NPZ = SCRIPT_DIR / "s85_w0_zubarev_lmax_convergence_to_minus_one.npz"

INPUT_FILES = [CANON_PY, W0_SUCCESSOR_JSON]
if W0_ZUBAREV_NPZ.exists():
    INPUT_FILES.append(W0_ZUBAREV_NPZ)


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


def classify_cell(w0, wa) -> str:
    """Return cell label for a (w_0, w_a) point.

    7 cells cover (w_0, w_a) plane; each point lands in exactly one.
    Definitions from plan §W1b-1 + W1a-5 decision tree.
    """
    if w0 is None or wa is None:
        return "UNAVAILABLE"
    # Exotic tails first
    if w0 < -1.5:
        return "C1"
    if w0 > -0.5:
        return "C2"
    # CPL evolution
    if abs(wa) > 0.2:
        return "B3"
    # Outside R_842 rectangle on w_0 side
    if w0 < R_W0_LO:
        return "B1"
    if w0 > R_W0_HI:
        return "B2"
    # Inside rectangle: A1 (1-sigma of center) vs A2 (1-2 sigma)
    delta = abs(w0 - R_W0_CENTER)                                   # (local)
    if delta <= R_W0_HALFWIDTH * 1.0:
        return "A1"
    else:
        return "A2"


def compute() -> dict:
    L_max_list = [5, 8, 10, 12]                                     # (local) NOTE: L_max=8 unavailable
    w0_list = [W0_FW_L5, None, W0_FW_L10, W0_FW_L12]                # (local)
    wa_list = [WA_FW_ALL, None, WA_FW_ALL, WA_FW_ALL]               # (local)

    assignments = {}                                                # (local)
    for L, w0, wa in zip(L_max_list, w0_list, wa_list):
        cell = classify_cell(w0, wa)                                # (local)
        assignments[L] = {
            "L_max": L,
            "w_0": w0,
            "w_a": wa,
            "cell": cell,
            "contained": None if w0 is None
                         else ((R_W0_LO <= w0 <= R_W0_HI)
                               and (R_WA_LO <= wa <= R_WA_HI)),
        }

    # 7-cell x L_max verdict matrix: cells_present[cell][L_max] = True/False
    all_cells = ["A1", "A2", "B1", "B2", "B3", "C1", "C2"]          # (local)
    matrix = {c: {} for c in all_cells}
    for c in all_cells:
        for L in L_max_list:
            # framework prediction is IN this cell at this L_max iff
            # assignments[L]["cell"] == c
            fw_cell = assignments[L]["cell"]
            if fw_cell == "UNAVAILABLE":
                matrix[c][L] = "UNAVAILABLE"
            else:
                matrix[c][L] = "FW-IN" if fw_cell == c else "FW-OUT"

    # Flip test across available L_max levels (excluding L=8 UNAVAILABLE)
    available_L = [L for L in L_max_list if assignments[L]["cell"] != "UNAVAILABLE"]
    cells_across_L = {L: assignments[L]["cell"] for L in available_L}
    unique_cells = set(cells_across_L.values())
    flip_detected = len(unique_cells) > 1

    return {
        "value": "FLIP-A1-to-B2-at-L12" if flip_detected else "ALL-A1",
        "assignments": assignments,
        "matrix": matrix,
        "cells_across_L": cells_across_L,
        "unique_cells": list(unique_cells),
        "flip_detected": flip_detected,
        "all_cells": all_cells,
        "L_max_list": L_max_list,
        "R_842_rectangle": {
            "w0_range": [R_W0_LO, R_W0_HI],
            "wa_range": [R_WA_LO, R_WA_HI],
            "center": [R_W0_CENTER, 0.0],
            "half_width": [R_W0_HALFWIDTH, 0.2],
        },
    }


def evaluate_gate(res: dict) -> str:
    if res["flip_detected"]:
        return "FAIL"
    # Check for UNAVAILABLE presence (L=8)
    has_unavailable = any(a["cell"] == "UNAVAILABLE"
                          for a in res["assignments"].values())
    if has_unavailable:
        return "INFO"
    return "PASS"


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
    fig, ax = plt.subplots(figsize=(9.0, 5.4))                      # (local)
    cells = res["all_cells"]
    Ls = res["L_max_list"]
    grid = np.zeros((len(cells), len(Ls)))                          # (local)
    labels = np.full_like(grid, "", dtype=object)                   # (local)
    for i, c in enumerate(cells):
        for j, L in enumerate(Ls):
            v = res["matrix"][c][L]                                 # (local)
            if v == "FW-IN":
                grid[i, j] = 2.0
                labels[i, j] = "FW-IN"
            elif v == "FW-OUT":
                grid[i, j] = 0.5
                labels[i, j] = ""
            else:
                grid[i, j] = 1.0
                labels[i, j] = "N/A"
    ax.imshow(grid, cmap="RdYlGn", aspect="auto", vmin=0, vmax=2.5)
    ax.set_xticks(range(len(Ls)))
    ax.set_xticklabels([f"L={L}" for L in Ls])
    ax.set_yticks(range(len(cells)))
    ax.set_yticklabels(cells)
    for i in range(len(cells)):
        for j in range(len(Ls)):
            ax.text(j, i, labels[i, j], ha="center", va="center",
                    fontsize=9, color="#333333")
    ax.set_title(f"{GATE_ID}: 7x4 cell assignment (FW-IN marks framework-prediction cell)")
    ax.set_xlabel(r"$L_{max}$ regulator level")
    ax.set_ylabel("R_842 cell")
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
    print(f"  Step 1: R_842 rectangle (W0-successor) = "
          f"[{R_W0_LO},{R_W0_HI}] x [{R_WA_LO},{R_WA_HI}]")
    print(f"          center = ({R_W0_CENTER}, 0); half_widths = ({R_W0_HALFWIDTH}, 0.2)")
    print(f"  Step 2: 7 cells = A1/A2/B1/B2/B3/C1/C2 (see docstring)")
    print(f"  Step 3: framework Zubarev w_0 per L_max:")
    for L, a in res["assignments"].items():
        print(f"          L={L}: w_0={a['w_0']}, w_a={a['w_a']} -> cell {a['cell']}")
    print(f"  Step 4: framework-prediction cell across available L: {res['cells_across_L']}")
    print(f"  Step 5: unique cells = {sorted(res['unique_cells'])}")
    print(f"  Step 6: FLIP_detected = {res['flip_detected']}")
    print(f"  Step 7: Thresholds: PASS if all cells preserve verdicts;"
          f" FAIL if any cell flips IN<->OUT as L_max changes by 2.")
    print(f"          flip={res['flip_detected']} ==> {verdict}")
    print()

    np.savez(
        OUT_NPZ,
        L_max_list=np.array(res["L_max_list"]),
        w_0_values=np.array([a["w_0"] if a["w_0"] is not None else np.nan
                             for a in res["assignments"].values()]),
        w_a_values=np.array([a["w_a"] if a["w_a"] is not None else np.nan
                             for a in res["assignments"].values()]),
        cells_per_L=np.array([a["cell"] for a in res["assignments"].values()]),
        flip_detected=np.array(res["flip_detected"]),
        unique_cells=np.array(res["unique_cells"]),
        R_w0_range=np.array([R_W0_LO, R_W0_HI]),
        R_wa_range=np.array([R_WA_LO, R_WA_HI]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX_LABEL)
    print(tag)
    append_verdict(verdict, res["value"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
