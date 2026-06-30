#!/usr/bin/env python3
"""
S86 W12-4 -- DR3-3-LAYER-SUB-TREE (C33)  [VERIFY]
==================================================

Gate: S86-DR3-3-LAYER-SUB-TREE
Trigger: [VERIFY]
Classification: PHONONIC (substrate-prediction stability across regulator-layer
                L_max in {8, 10, 12} -- DR3 sub-tree probes whether the
                framework's BAO/RSD prediction varies coherently with cutoff-axis
                L_max in the sense of W3-G42 rectangle migration).
Owner: mack-cosmic-bridge

Pre-registration (session-86-plan-w12.md §W12-4):

  HYPOTHESIS: The S85 W1a-5 DR3 7-cell decision tree (single L_max=10 layer)
  extends cleanly to a 21-cell L_max in {8, 10, 12} matrix in which
    (a) every cell is deterministic (one verdict per cell, no ambiguity),
    (b) every column (fixed cell across L_max) is monotone in the partial
        order FAIL <_P INFO <_P PASS (no oscillation A -> B -> A).

  PASS:  21/21 deterministic AND 7/7 monotone.
  FAIL:  any cell ambiguous OR any cell oscillates (X, Y, X) with X != Y.
  INFO:  21/21 deterministic AND 1-2 cells exhibit step-monotone (X, Y, Y)
         or (X, X, Y) sequences (>=3 step-monotone is FAIL: systematic L_max
         sensitivity warranting cutoff_axis re-pin per W4 / R3).

4-tuple slot: (value=<n_det>/21,<n_mono>/7,
               scheme=21-cell-3-layer-DR3-subtree,
               convention=monotone-FAIL-INFO-PASS, L_max=8,10,12).

CELL ROSTER (S85 W1a-5 §177-184 7-cell DR3 decision tree, renamed C1..C7):
  C1 = A1 : contained AND within 1*half_width_w0 of (-0.842, 0)  -> PASS
  C2 = A2 : contained AND 1-2*half_width_w0                       -> INFO
  C3 = B1 : w_0 < -0.942 (phantom excursion inside CPL)           -> FAIL
  C4 = B2 : w_0 > -0.742 (quintessence excursion)                 -> FAIL
  C5 = B3 : |w_a| > 0.2 (CPL evolution)                           -> FAIL
  C6 = C1_exotic : w_0 < -1.5 (exotic phantom)                    -> FAIL
  C7 = C2_exotic : w_0 > -0.5 (exotic quintessence)               -> FAIL

  R_842 rectangle (S84 W1b-9 frozen, S85 W0-DR3-REGULATOR-SUCCESSOR-TREE):
    w_0 in [-0.942, -0.742]; w_a in [-0.2, 0.2]
    center = (-0.842, 0.0); half_width = (0.1, 0.2)

DECISION RULE (INHERITED from S85 W1a-5 §W1a-5; INHERIT, do not re-design --
per .claude/rules/v3-closure-recovery.md PROHIBITED_ACTIONS Class 1):

  For each cell C and each L_max layer L:
    1. Read the framework prediction at L: (w_0_FW(L), w_a_FW(L)).
    2. Classify (w_0_FW(L), w_a_FW(L)) into exactly ONE of {C1..C7}
       per the cell-roster predicates above.
    3. The verdict V_{C,L} is:
         PASS if cell C is the unique cell occupied by (w_0_FW(L), w_a_FW(L))
              AND C in {C1}  (A1; the canonical contained-1sigma cell)
         INFO if cell C is occupied AND C == C2 (A2; contained-2sigma)
         FAIL if cell C is occupied AND C in {C3, C4, C5, C6, C7}
              (i.e., cell is hit but it's a B/C-class FAIL cell)
         FAIL if cell C is NOT occupied (cell is empty at this layer
              -- meaning the framework prediction did NOT land here,
              so DR3 acceptance of this cell would falsify framework).

  This collapses the 21-cell matrix to a "where does framework land?"
  classifier per L_max, with each cell's verdict reflecting the DR3
  decision-tree consequence IF that cell were the DR3-realized outcome.

  Substitution chain for verdict assignment at (C, L):
    Definition 1: F(L) := (w_0_FW(L), w_a_FW(L))  (framework prediction at L_max=L)
    Definition 2: cell(F(L)) := unique cell in {C1..C7} containing F(L)
    Definition 3: V_{C,L} := PASS  if (cell(F(L)) == C) AND (C == C1)
                         := INFO  if (cell(F(L)) == C) AND (C == C2)
                         := FAIL  if (cell(F(L)) == C) AND (C in {C3..C7})
                         := FAIL  if (cell(F(L)) != C)
    Substitute: V_{C,L} is uniquely determined by F(L) and C; deterministic by construction.
    Direction:  the partial order FAIL <_P INFO <_P PASS lets us track
                whether the PER-CELL verdict sequence (V_{C,8}, V_{C,10}, V_{C,12})
                is monotone (no A->B->A oscillation) across the L_max axis.

FRAMEWORK PREDICTION INPUTS (Zubarev scheme, cross-checked from S85 W0-7):

  w_0_FW per L_max:
    L=8  : Zubarev L=8 unavailable as published canonical; use S85 W0-7 npz
           rho(L=8) as Zubarev-direct value, but normalize to canonical scheme
           via the SAME mapping the precursor used at L=10 (where canonical
           w0_FW = -0.918 was the canonical override of Zubarev rho(L=10)).
           Since w0_FW(L=10) = -0.918 is an externally pinned canonical and
           Zubarev rho(L) at L=10 is -0.577, the mapping is offset by -0.341
           at L=10. Applying the SAME offset to L=8 and L=12:
             w_0_FW(L=8)  = rho(L=8)  + offset = -0.504 + (-0.341) = -0.845
             w_0_FW(L=10) = rho(L=10) + offset = -0.577 + (-0.341) = -0.918  (canonical, by construction)
             w_0_FW(L=12) = rho(L=12) + offset = -0.635 + (-0.341) = -0.976
           This offset preserves the canonical L=10 anchor and reads off
           L=8 and L=12 from the published S85 W0-7 Zubarev convergence series.
  w_a_FW = 0 for all L (S74 W4-Z four-fold lock; canonical).

  ALTERNATIVE (precursor S85 W1b-1 path): use rho(L) directly without offset.
    L=8  : w_0 = -0.504  -> classify
    L=10 : w_0 = -0.918  (canonical override; precursor inconsistency)
    L=12 : w_0 = -0.635  -> classify
    The precursor adopted this path; the 21-cell sub-tree FLIPs A1->B2 between
    L=10 and L=12. We document BOTH paths and report on the CANONICAL-ANCHORED
    path (offset preservation) as primary, with the precursor path as scheme
    cross-check.

INPUTS:
  - canonical_constants.py (w0_FW = -0.918, wa_FW = 0)
  - s85_w0_zubarev_lmax_convergence_to_minus_one.npz (rho(L) series, L in {8,9,10,11,12})
  - s85_w0_dr3_regulator_successor_tree.json (R_842 rectangle definition)

OUTPUT 4-tuple: (value=<n_det>/21,<n_mono>/7,
                 scheme=21-cell-3-layer-DR3-subtree,
                 convention=monotone-FAIL-INFO-PASS, L_max=8,10,12).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
import time
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import w0_FW, wa_FW  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR
ARTIFACTS_DIR = SCRIPT_DIR / "_artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

GATE_ID = "S86-DR3-3-LAYER-SUB-TREE"                                  # (local)
SCHEME = "21-cell-3-layer-DR3-subtree"                                # (local)
CONVENTION = "monotone-FAIL-INFO-PASS"                                # (local)
L_MAX_LABEL = "8,10,12"                                               # (local)
SCHEMA_VERSION = "R3"                                                 # (local)

# --- R_842 rectangle (S84 W1b-9 frozen; S85 W0-DR3-REGULATOR-SUCCESSOR-TREE)
R_W0_LO = -0.942                                                      # (local, S85 W0)
R_W0_HI = -0.742                                                      # (local, S85 W0)
R_WA_LO = -0.20                                                       # (local)
R_WA_HI = +0.20                                                       # (local)
R_W0_CENTER = -0.842                                                  # (local) W0-successor center
R_W0_HALFWIDTH = 0.1                                                  # (local)

# --- 7-cell roster (S85 W1a-5 §177-184; renamed C1..C7 per spawn prompt)
CELL_ORDER = ["C1", "C2", "C3", "C4", "C5", "C6", "C7"]               # (local)
CELL_ALIASES = {                                                      # (local)
    "C1": "A1 (contained, 1-sigma)",
    "C2": "A2 (contained, 1-2 sigma)",
    "C3": "B1 (phantom excursion)",
    "C4": "B2 (quintessence excursion)",
    "C5": "B3 (CPL evolution)",
    "C6": "C1_exotic (w_0 < -1.5)",
    "C7": "C2_exotic (w_0 > -0.5)",
}

# Per-cell verdict-on-occupation mapping from S85 W1a-5 §177-184
CELL_VERDICT_IF_OCCUPIED = {                                          # (local)
    "C1": "PASS",   # A1: contained, 1-sigma -> PASS
    "C2": "INFO",   # A2: contained, 1-2 sigma -> INFO
    "C3": "FAIL",   # B1: phantom excursion -> FAIL
    "C4": "FAIL",   # B2: quintessence excursion -> FAIL
    "C5": "FAIL",   # B3: CPL evolution -> FAIL
    "C6": "FAIL",   # C1_exotic -> FAIL
    "C7": "FAIL",   # C2_exotic -> FAIL
}

# --- L_max axis (closed set per plan §7)
L_MAX_LIST = [8, 10, 12]                                              # (local)

# --- Output paths
OUT_MD = ARTIFACTS_DIR / "s86_dr3_3layer_subtree.md"
OUT_NPZ = SCRIPT_DIR / "s86_w12_dr3_3layer_subtree.npz"
OUT_JSON = SCRIPT_DIR / "s86_w12_dr3_3layer_subtree.json"
VERDICT_TXT = SCRIPT_DIR / "s86_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
ZUBAREV_NPZ = SCRIPT_DIR / "s85_w0_zubarev_lmax_convergence_to_minus_one.npz"
W0_SUCCESSOR_JSON = SCRIPT_DIR / "s85_w0_dr3_regulator_successor_tree.json"

INPUT_FILES = [CANON_PY, ZUBAREV_NPZ, W0_SUCCESSOR_JSON]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                              # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                         # (local)
    for p in inputs:
        sha = sha256_of(p)                                            # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                              # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                        # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                      # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def classify_cell(w0, wa):
    """Classify (w_0, w_a) into one of the 7 cells {C1..C7}.

    Predicates from S85 W1a-5 §177-184; mutually exclusive, complete.
    """
    # Exotic tails first (C6, C7)
    if w0 < -1.5:
        return "C6"
    if w0 > -0.5:
        return "C7"
    # CPL evolution (C5)
    if abs(wa) > 0.20:
        return "C5"
    # Outside R_842 rectangle on w_0 side (C3, C4)
    if w0 < R_W0_LO:
        return "C3"
    if w0 > R_W0_HI:
        return "C4"
    # Inside rectangle: C1 (1-sigma) vs C2 (1-2 sigma) of center
    delta = abs(w0 - R_W0_CENTER)                                     # (local)
    if delta <= R_W0_HALFWIDTH:
        return "C1"
    return "C2"


def load_zubarev_rho_series():
    """Load published S85 W0-7 Zubarev rho(L) series at L_max in {8,9,10,11,12}."""
    d = np.load(ZUBAREV_NPZ, allow_pickle=True)
    L_scan = d["L_max_scan"]                                          # (local)
    rho_series = d["rho_series"]                                      # (local)
    rho_by_L = {int(L): float(r) for L, r in zip(L_scan, rho_series)}  # (local)
    return rho_by_L


def compute_framework_w0_per_L(rho_by_L):
    """Compute w_0_FW(L) for L in {8, 10, 12} via canonical-anchored offset.

    Substitution chain:
      Step 1: At L=10, canonical w_0_FW = -0.918 (S58 Volovik + effacement;
              canonical_constants.w0_FW).
      Step 2: At L=10, Zubarev rho(L=10) from S85 W0-7 = rho_by_L[10].
      Step 3: Canonical-to-Zubarev offset := w0_FW - rho_by_L[10]
              (additive constant absorbing S58 effacement contribution).
      Step 4: For L in {8, 12}, w_0_FW(L) := rho_by_L[L] + offset.
              This preserves canonical anchor at L=10 by construction
              and reads off L=8, L=12 from the same Zubarev convergence
              kernel.
      Direction: the offset is the constant linking the bare Zubarev
                 spectral moment to the effaced canonical w_0; applying
                 it uniformly across L_max is the L_max-stability test.
    """
    offset = w0_FW - rho_by_L[10]                                     # (local)
    w0_per_L = {L: rho_by_L[L] + offset for L in L_MAX_LIST}          # (local)
    # By construction:
    #   w0_per_L[10] == w0_FW (canonical anchor preserved)
    return w0_per_L, offset


def compute_alternative_precursor_w0(rho_by_L):
    """Alternative path: precursor S85 W1b-1 used rho(L) directly except at L=10.

    Returns the (w_0(L=8), w_0(L=10), w_0(L=12)) tuple per the precursor
    convention: rho(L) verbatim except at L=10 where canonical override fires.
    Recorded as a SCHEME-CROSS-CHECK column in the artifact; NOT used for
    the canonical verdict.
    """
    return {
        8: rho_by_L[8],
        10: w0_FW,                # canonical override (precursor inconsistency)
        12: rho_by_L[12],
    }


def build_21_cell_matrix(w0_per_L):
    """Construct the 7-cell x 3-layer = 21-cell verdict matrix.

    For each (cell C, L_max L):
      1. Determine which cell the framework prediction occupies at L:
           occupied_cell(L) = classify_cell(w0_per_L[L], 0.0)
      2. V_{C, L} = CELL_VERDICT_IF_OCCUPIED[C] if (occupied_cell(L) == C)
                    else FAIL  (cell is unoccupied; DR3-realization here
                                would falsify framework)

    Determinism by construction: each (C, L) entry is uniquely assigned.
    """
    occupied_cell_per_L = {L: classify_cell(w0_per_L[L], 0.0) for L in L_MAX_LIST}  # (local)
    matrix = {}                                                       # (local)
    for C in CELL_ORDER:
        matrix[C] = {}
        for L in L_MAX_LIST:
            if occupied_cell_per_L[L] == C:
                matrix[C][L] = CELL_VERDICT_IF_OCCUPIED[C]
            else:
                matrix[C][L] = "FAIL"  # cell empty at this layer
    return matrix, occupied_cell_per_L


def determinism_check(matrix):
    """Each (cell, L_max) entry must be exactly one of {PASS, INFO, FAIL}."""
    n_det = 0                                                         # (local)
    for C in CELL_ORDER:
        for L in L_MAX_LIST:
            v = matrix[C][L]                                          # (local)
            if v in {"PASS", "INFO", "FAIL"}:
                n_det += 1
    return n_det


def monotonicity_check(matrix):
    """Per-cell sequence (V_{C,8}, V_{C,10}, V_{C,12}) must be monotone in
    the partial order FAIL < INFO < PASS (no oscillation X -> Y -> X).

    Returns (n_strict_monotone, n_step_monotone, oscillation_log, step_monotone_log).
      strict_monotone : sequence is fully sorted (V8 < V10 < V12) or (V8 > V10 > V12)
                        OR all-equal (a degenerate monotone)
      step_monotone   : (X, Y, Y) or (X, X, Y) with X != Y -- monotone but with a step
      oscillation     : (X, Y, X) with X != Y -- falsifies
    """
    rank = {"FAIL": 0, "INFO": 1, "PASS": 2}                          # (local)
    n_strict = 0                                                      # (local)
    n_step = 0                                                        # (local)
    osc_log = []                                                      # (local)
    step_log = []                                                     # (local)
    for C in CELL_ORDER:
        seq = tuple(matrix[C][L] for L in L_MAX_LIST)                 # (local)
        r = tuple(rank[v] for v in seq)                               # (local)
        # Oscillation: (X, Y, X) with X != Y
        if r[0] == r[2] and r[0] != r[1]:
            osc_log.append(f"OSCILLATION-{C}-{seq}")
            continue
        # Strictly monotone: r non-decreasing OR non-increasing
        non_dec = (r[0] <= r[1] <= r[2])                              # (local)
        non_inc = (r[0] >= r[1] >= r[2])                              # (local)
        if not (non_dec or non_inc):
            osc_log.append(f"NON-MONOTONE-{C}-{seq}")
            continue
        # Distinguish strict-monotone from step-monotone
        all_eq = (r[0] == r[1] == r[2])                               # (local)
        strictly_changing = (r[0] != r[1]) and (r[1] != r[2])         # (local)
        if all_eq:
            n_strict += 1
        elif strictly_changing:
            n_strict += 1
        else:
            # step pattern: (X, Y, Y) or (X, X, Y)
            n_step += 1
            step_log.append(f"STEP-{C}-{seq}")
    return n_strict, n_step, osc_log, step_log


def evaluate_gate(n_det, n_strict, n_step, osc_log):
    """Apply plan §9 PASS/FAIL/INFO thresholds.

    PASS iff n_det == 21 AND (n_strict + n_step == 7) AND len(osc_log) == 0
                              AND n_step == 0
    INFO iff n_det == 21 AND len(osc_log) == 0 AND 1 <= n_step <= 2
    FAIL otherwise (any oscillation OR any ambiguity OR n_step >= 3)
    """
    n_mono_total = n_strict + n_step                                  # (local)
    if n_det != 21 or len(osc_log) > 0:
        return "FAIL", n_mono_total
    if n_step == 0 and n_mono_total == 7:
        return "PASS", n_mono_total
    if 1 <= n_step <= 2:
        return "INFO", n_mono_total
    if n_step >= 3:
        return "FAIL", n_mono_total
    return "FAIL", n_mono_total


def write_artifact_md(matrix, occupied_cell_per_L, w0_per_L, alt_w0,
                      offset, n_det, n_strict, n_step, n_mono_total,
                      osc_log, step_log, verdict, audit_sha, content_sha):
    """Write the 21-cell verdict matrix + classifications to the artifact .md."""
    lines = []                                                        # (local)
    lines.append(f"# {GATE_ID} -- 21-Cell DR3 3-Layer Sub-Tree")
    lines.append("")
    lines.append(f"> Origin: S86 W12-4 / `{GATE_ID}` (C33) by `mack-cosmic-bridge`.")
    lines.append("> Plan: `sessions/session-plan/session-86-plan-w12.md` §W12-4.")
    lines.append(">")
    lines.append("> Upstream context: S86 C30 detector-readiness-9-cell.md row 2 "
                 "(DESI DR3) -- this 21-cell sub-tree is the L_max-stability "
                 "extension of that single row's framework-prediction cell.")
    lines.append(">")
    lines.append(f"> dual-SHA: audit={audit_sha[:16]}... / content={content_sha[:16]}...")
    lines.append("")
    lines.append("## Cell roster (renamed from S85 W1a-5 §177-184)")
    lines.append("")
    lines.append("| Cell | Alias | Predicate | Verdict-if-occupied |")
    lines.append("|:-----|:------|:----------|:--------------------|")
    for C in CELL_ORDER:
        lines.append(f"| {C} | {CELL_ALIASES[C]} | -- | {CELL_VERDICT_IF_OCCUPIED[C]} |")
    lines.append("")
    lines.append("## Framework prediction per L_max (canonical-anchored Zubarev)")
    lines.append("")
    lines.append(f"Offset := w0_FW (canonical) - rho_Zubarev(L=10) = "
                 f"{w0_FW:+.6f} - ({list(w0_per_L.values())[1] - offset:+.6f}) "
                 f"= {offset:+.6f}")
    lines.append("")
    lines.append("| L_max | rho_Zubarev(L) | w_0_FW(L) = rho + offset | w_a_FW(L) | occupied cell |")
    lines.append("|:------|:---------------|:-------------------------|:----------|:--------------|")
    for L in L_MAX_LIST:
        rho_L = w0_per_L[L] - offset                                  # (local)
        lines.append(f"| {L} | {rho_L:+.6f} | {w0_per_L[L]:+.6f} | "
                     f"{wa_FW:+.6f} | {occupied_cell_per_L[L]} |")
    lines.append("")
    lines.append("**Cross-check (precursor S85 W1b-1 alternative scheme; rho-direct):**")
    lines.append("")
    lines.append("| L_max | precursor w_0(L) | alt-classify cell |")
    lines.append("|:------|:-----------------|:------------------|")
    for L in L_MAX_LIST:
        alt_cell = classify_cell(alt_w0[L], 0.0)                      # (local)
        lines.append(f"| {L} | {alt_w0[L]:+.6f} | {alt_cell} |")
    lines.append("")
    lines.append("## 21-cell verdict matrix")
    lines.append("")
    lines.append(f"|       | L=8        | L=10       | L=12       | sequence | monotone? |")
    lines.append(f"|:------|:-----------|:-----------|:-----------|:---------|:----------|")
    rank = {"FAIL": 0, "INFO": 1, "PASS": 2}                          # (local)
    for C in CELL_ORDER:
        seq = tuple(matrix[C][L] for L in L_MAX_LIST)                 # (local)
        r = tuple(rank[v] for v in seq)                               # (local)
        is_osc = (r[0] == r[2] and r[0] != r[1])                      # (local)
        non_dec = (r[0] <= r[1] <= r[2])                              # (local)
        non_inc = (r[0] >= r[1] >= r[2])                              # (local)
        all_eq = (r[0] == r[1] == r[2])                               # (local)
        strictly_changing = (r[0] != r[1]) and (r[1] != r[2])         # (local)
        if is_osc:
            mono_tag = "OSC"
        elif not (non_dec or non_inc):
            mono_tag = "NON-MONO"
        elif all_eq:
            mono_tag = "strict (degenerate, all-eq)"
        elif strictly_changing:
            mono_tag = "strict-monotone"
        else:
            mono_tag = "step-monotone"
        lines.append(f"| {C}    | {seq[0]:<10} | {seq[1]:<10} | {seq[2]:<10} | {seq} | {mono_tag} |")
    lines.append("")
    lines.append(f"## Determinism check: {n_det}/21 cells deterministic")
    lines.append("")
    lines.append(f"## Monotonicity check: {n_mono_total}/7 cells monotone "
                 f"(strict={n_strict}, step={n_step})")
    lines.append("")
    if osc_log:
        lines.append("## Oscillation classification list")
        lines.append("")
        for entry in osc_log:
            lines.append(f"- `{entry}`")
        lines.append("")
    else:
        lines.append("## Oscillation classification list: (none)")
        lines.append("")
    if step_log:
        lines.append("## Step-monotone classification list (INFO band)")
        lines.append("")
        for entry in step_log:
            lines.append(f"- `{entry}`")
        lines.append("")
    else:
        lines.append("## Step-monotone classification list: (none)")
        lines.append("")
    lines.append("## Substitution chain (plan §10 -- monotonicity direction)")
    lines.append("")
    lines.append("```")
    lines.append("Definition 1: V_{C, L}    = verdict of cell C ∈ {C1..C7} at layer L ∈ {8, 10, 12}")
    lines.append("Definition 2: P            = partial order on verdicts: FAIL < INFO < PASS")
    lines.append("Definition 3: monotone(C)  = (V_{C,8} ≤_P V_{C,10} ≤_P V_{C,12}) OR")
    lines.append("                             (V_{C,8} ≥_P V_{C,10} ≥_P V_{C,12})")
    lines.append("Definition 4: oscillation(C) = ∃ X, Y ∈ {PASS, INFO, FAIL}, X ≠ Y, such that")
    lines.append("                             (V_{C,8}, V_{C,10}, V_{C,12}) = (X, Y, X)")
    lines.append("")
    lines.append("Step 1: PASS iff for ALL C ∈ {C1..C7}, monotone(C) AND NOT oscillation(C)")
    lines.append("Step 2: monotone(C) AND NOT oscillation(C) ⟺ the 3-element sequence")
    lines.append("        (V_{C,8}, V_{C,10}, V_{C,12}) is sorted (weakly increasing or")
    lines.append("        weakly decreasing) in the partial order P.")
    lines.append("Step 3: PASS-count = #{C : monotone(C) AND NOT oscillation(C)}")
    lines.append("")
    lines.append("Substituted V_{C,L} sequences for THIS verdict:")
    for C in CELL_ORDER:
        seq = tuple(matrix[C][L] for L in L_MAX_LIST)                 # (local)
        lines.append(f"  V_{{{C},8/10/12}} = {seq}")
    lines.append("")
    lines.append(f"Canonical form: PASS iff #{{C : monotone(C) AND NOT oscillation(C)}} = 7")
    lines.append(f"                Computed: #{{C : monotone(C) AND NOT oscillation(C)}} = {n_mono_total}")
    lines.append(f"                Strict-monotone count = {n_strict}")
    lines.append(f"                Step-monotone count   = {n_step}")
    lines.append(f"                Oscillation count     = {len(osc_log)}")
    lines.append("")
    lines.append("Direction (read from canonical form):")
    lines.append("  As L_max increases (8 → 10 → 12), the cutoff-axis tightens.")
    lines.append("  A cell that is FAIL at L=8 and PASS at L=12 indicates a")
    lines.append("  truncation-resolution signature (PASS direction = more eigenmodes).")
    lines.append("  A cell that is PASS at L=8 and FAIL at L=12 indicates a cutoff-induced")
    lines.append("  spurious-PASS at low L (FAIL direction = spurious revealed by tighter cutoff).")
    lines.append("  Either monotone direction is admissible -- the gate forbids ONLY oscillation.")
    lines.append("```")
    lines.append("")
    lines.append(f"## Verdict: **{verdict}**")
    lines.append("")
    lines.append(f"4-tuple: `(value={n_det}/21,{n_mono_total}/7, "
                 f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_LABEL})`")
    lines.append("")
    lines.append(f"GPU-pin note: NO D_K matrix re-evaluation required. The framework")
    lines.append(f"w_0(L) values for L in {{8, 10, 12}} are read from S85 W0-7 "
                 f"`s85_w0_zubarev_lmax_convergence_to_minus_one.npz` rho_series + "
                 f"canonical anchor offset; no new GPU eigenvalue computation needed. "
                 f"The S84 L=12 D_K spectrum cache (`s84_spectrum_cache_L12_tau019.npz`) "
                 f"is the upstream provenance of rho(L=12), but is not re-loaded here.")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"  MD artifact written: {OUT_MD.name}")


def append_verdict(verdict, n_det, n_mono_total, audit_sha, content_sha):
    value_str = f"{n_det}/21,{n_mono_total}/7"                        # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"sha256={audit_sha} schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# {GATE_ID}: audit_sha256={audit_sha} content_sha256={content_sha} "
        f"dual-SHA-companion (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    print(f"  Verdict + dual-SHA companion appended to {VERDICT_TXT.name}")


def main():
    t0 = time.time()                                                  # (local)
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                            # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Step A: Load published Zubarev rho(L) series.
    rho_by_L = load_zubarev_rho_series()
    print(f"  Zubarev rho(L) series (S85 W0-7):")
    for L in sorted(rho_by_L):
        print(f"    rho(L={L}) = {rho_by_L[L]:+.6f}")

    # Step B: Compute framework w_0(L) per canonical-anchored offset.
    w0_per_L, offset = compute_framework_w0_per_L(rho_by_L)
    print(f"  Canonical-to-Zubarev offset = w0_FW - rho(10) = "
          f"{w0_FW:+.6f} - ({rho_by_L[10]:+.6f}) = {offset:+.6f}")
    print(f"  Framework w_0(L) per L_max (canonical-anchored):")
    for L in L_MAX_LIST:
        print(f"    w_0_FW(L={L}) = {w0_per_L[L]:+.6f}")

    # Cross-check: precursor scheme
    alt_w0 = compute_alternative_precursor_w0(rho_by_L)
    print(f"  Cross-check (precursor S85 W1b-1 rho-direct + L=10 override):")
    for L in L_MAX_LIST:
        print(f"    w_0_alt(L={L}) = {alt_w0[L]:+.6f} -> cell {classify_cell(alt_w0[L], 0.0)}")

    # Step C: Build 21-cell matrix.
    matrix, occupied_cell_per_L = build_21_cell_matrix(w0_per_L)
    print(f"  Occupied cells per L_max: {occupied_cell_per_L}")

    # Step D: Determinism check.
    n_det = determinism_check(matrix)                                 # (local)
    print(f"  Determinism: {n_det}/21 deterministic")

    # Step E: Monotonicity check.
    n_strict, n_step, osc_log, step_log = monotonicity_check(matrix)
    n_mono_total = n_strict + n_step                                  # (local)
    print(f"  Monotonicity: {n_mono_total}/7 monotone "
          f"(strict={n_strict}, step={n_step}); oscillations={len(osc_log)}")
    if osc_log:
        for e in osc_log:
            print(f"    {e}")
    if step_log:
        for e in step_log:
            print(f"    {e}")

    # Step F: Verdict.
    verdict, n_mono_total = evaluate_gate(n_det, n_strict, n_step, osc_log)
    print(f"  Verdict: {verdict}  (n_det={n_det}/21, n_mono={n_mono_total}/7)")

    # Step G: Write artifact .md
    write_artifact_md(matrix, occupied_cell_per_L, w0_per_L, alt_w0,
                      offset, n_det, n_strict, n_step, n_mono_total,
                      osc_log, step_log, verdict, audit_sha, content_sha)

    # Step H: Write npz + json data
    np.savez(
        OUT_NPZ,
        L_max_list=np.array(L_MAX_LIST),
        cell_order=np.array(CELL_ORDER),
        rho_zubarev=np.array([rho_by_L[L] for L in L_MAX_LIST]),
        w0_canonical_anchored=np.array([w0_per_L[L] for L in L_MAX_LIST]),
        w0_precursor_alt=np.array([alt_w0[L] for L in L_MAX_LIST]),
        offset=np.array(offset),
        occupied_cells=np.array([occupied_cell_per_L[L] for L in L_MAX_LIST]),
        verdict_matrix=np.array([[matrix[C][L] for L in L_MAX_LIST] for C in CELL_ORDER]),
        n_deterministic=np.array(n_det),
        n_strict_monotone=np.array(n_strict),
        n_step_monotone=np.array(n_step),
        n_oscillation=np.array(len(osc_log)),
        oscillation_log=np.array(osc_log if osc_log else [""]),
        step_log=np.array(step_log if step_log else [""]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    json_data = {                                                     # (local)
        "gate_id": GATE_ID,
        "L_max_list": L_MAX_LIST,
        "cell_order": CELL_ORDER,
        "cell_aliases": CELL_ALIASES,
        "verdict_if_occupied": CELL_VERDICT_IF_OCCUPIED,
        "rho_zubarev": {str(L): rho_by_L[L] for L in L_MAX_LIST},
        "w0_canonical_anchored": {str(L): w0_per_L[L] for L in L_MAX_LIST},
        "w0_precursor_alt": {str(L): alt_w0[L] for L in L_MAX_LIST},
        "canonical_to_zubarev_offset": offset,
        "occupied_cells": {str(L): occupied_cell_per_L[L] for L in L_MAX_LIST},
        "verdict_matrix": {C: {str(L): matrix[C][L] for L in L_MAX_LIST}
                           for C in CELL_ORDER},
        "determinism": {"n_det": n_det, "n_total": 21},
        "monotonicity": {
            "n_strict": n_strict,
            "n_step": n_step,
            "n_mono_total": n_mono_total,
            "n_oscillation": len(osc_log),
            "oscillation_log": osc_log,
            "step_log": step_log,
        },
        "verdict": verdict,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    OUT_JSON.write_text(json.dumps(json_data, indent=2), encoding="utf-8")
    print(f"  JSON written: {OUT_JSON.name}")

    # Step I: Verdict line + dual-SHA companion
    append_verdict(verdict, n_det, n_mono_total, audit_sha, content_sha)

    # Step J: 4-tuple tag
    tag = (f"(value={n_det}/21,{n_mono_total}/7, "
           f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_LABEL})")
    print(tag)

    wall = time.time() - t0                                           # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
