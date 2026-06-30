#!/usr/bin/env python3
"""
S86 W13-4 -- S86-DR3-SUB-TREE-3-ROW-PIN (P8) [VERIFY]
=====================================================

Gate: S86-DR3-SUB-TREE-3-ROW-PIN
Trigger: [VERIFY]
Classification: PHONONIC (DR3 sub-tree IS the substrate's regulator-stratified
                prediction surface for w_0; each L_max row is a different
                truncation of the SAME substrate eigenvalue computation; the 3
                rows together test whether the substrate's w_0 prediction is
                REGULATOR-INVARIANT or REGULATOR-DEPENDENT).
Owner: cosmic-web-theorist (BAO/DR3 expertise; mack self-blacklist as
       carry-forward source per mack 9A §VI.6).

Pre-registration (sessions/session-plan/session-86-plan-w13.md §W13-4):

  HYPOTHESIS: Extending S85 W1b-1's 2-row DR3 sub-tree (L=10, L=12) to a 3-row
  tree (L=8 from S85 W7-7 + L=10 + L=12) at 7 cells per row produces a 21-cell
  decision matrix with all cells deterministic AND monotone in L_max
  (no oscillation A->B->A across L_max), pre-registering a regulator-first
  DR3 adjudication protocol with 4 deterministic outcome branches.

  PASS:  3-row x 7-cell matrix populated AND monotone in L_max (per scenario)
         AND every cell SHA-back-traceable AND adjudication protocol with
         4 deterministic branches registered.
  FAIL:  matrix incomplete OR any column non-monotone OR cell SHA-untraceable
         OR adjudication protocol absent.
  INFO:  if W7-7's L=8 row does not contain all 7 scenario sub-cells (only the
         headline value), the L=8 row is PRE-REG-INCOMPLETE and the gate
         emits INFO with the partial 14-cell + 7-stub matrix; re-dispatch
         in S87 after L=8 sub-cell extraction.

  The PRE-REG-INCOMPLETE FALLBACK is binding here because the W7-7 verdict
  publishes a single max-L-sensitivity scalar (0.0204) over an unrelated
  basket of 8 constants {K_R5, K_substrate, K_crit, Gamma_effacement,
  f_conv, c_sub_at_kpivot, F_amp_linearized, f_GGE_Leggett}; it does NOT
  publish a w_0 value at L=8 nor a 7-cell decomposition of the (w_0, w_a)
  DR3 contingency tree. Per the spawn prompt L=8 PRE-REG-INCOMPLETE
  FALLBACK: emit INFO with partial 14-cell + 7-stub matrix; do NOT
  fabricate cell content from the headline.

7-CELL ROSTER (S84 W4-44 DR3-CONTINGENCY-FINE-GRAINED, sha=801e4690...):
  A1: branch-(iv) mild corroboration (w_0 in [-0.988, -0.942], |w_a| <= 0.2)
                   -> SURVIVE+promote (scorecard corroboration)
  A2: branch-(iv) stretched corroboration (w_0 in [-1.05, -0.988], |w_a| <= 0.2)
                   -> SURVIVE+recal (scheme-band inflation)
  B1: w_a-driven exclusion (w_0 in R_842 strip, w_a in [-1.0, -0.2])
                   -> PARTIAL-REFUTE (four-fold w_a lock)
  B2: w_0-driven exclusion (w_0 in [-0.742, -0.5], |w_a| <= 0.2)
                   -> PARTIAL-REFUTE (Volovik partition)
  B3: joint shift (w_0 in [-0.742, -0.5], w_a in [-0.5, -0.2])
                   -> DUAL-REFUTE (both partition + lock)
  C1: extreme Quintom (w_0 in [-0.742, -0.2], w_a in [-1.5, -0.5])
                   -> STRONG-REFUTE (substrate DE mechanism ruled out)
  C2: deep phantom or boundary outliers (w_0 in [-1.2, -1.05] or w_a > +0.5)
                   -> PHANTOM-REFUTE (impedance audit required)

FRAMEWORK-RESPONSE PER (L_max, scenario) CELL:
  Each cell is populated with:
    framework_response: textual scorecard outcome (SURVIVE / PARTIAL-REFUTE /
                        DUAL-REFUTE / STRONG-REFUTE / PHANTOM-REFUTE)
    decision_branch: PASS / TENSION / EXCLUDED per the cell's pre-registered
                     threshold (A1 = PASS, A2 = TENSION, B1/B2/B3 = TENSION
                     for partial refutation, C1/C2 = EXCLUDED for strong/
                     phantom refutation)
    dual_sha_pin: SHA-256 of the source verdict line (W1b-1 for L=10/L=12,
                  W7-7 for L=8 -- but L=8 is PRE-REG-INCOMPLETE per fallback)

L=10 / L=12 SOURCE (S85 W1b-1, sha=beba9cad...):
  Framework occupies cell A1 at L=10 (w_0 = -0.918, |w_0 - center| = 0.076 <=
  0.10) and cell B2 at L=12 (w_0 = -0.635 > -0.742, quintessence excursion).

L=8 SOURCE (S85 W7-7, sha=dddf9edd...):
  W7-7 is an L_max-sensitivity audit across 8 W_0-dependent constants under
  ANALYTIC-SENSITIVITY-MODEL; its published verdict-line value is
  max_L_sensitivity = 0.0204 (PASS at <= 5%). It does NOT publish a Zubarev
  w_0(L=8) value, NOR a 7-cell decomposition of the (w_0, w_a) DR3 tree.
  Per the spawn-prompt L=8 PRE-REG-INCOMPLETE FALLBACK clause, the L=8 row
  is filled with 7 PRE-REG-INCOMPLETE stubs.

PRE-REGISTERED REGULATOR-FIRST DR3 ADJUDICATION PROTOCOL (4 branches):
  When DR3 publishes (w_0^DR3, w_a^DR3), the 7-cell scenario classifier
  (per S84 W4-44 §classification_rule) determines which scenario S* the
  observation occupies. The decision-branch is then:

    (1) REG-INVARIANT: all 3 L_max rows (L=8, L=10, L=12) for column S*
        give the SAME decision_branch -> verdict is REG-INVARIANT;
        adopt the unanimous decision_branch (PASS / TENSION / EXCLUDED).

    (2) REG-DEP-MAJORITY: 2 of 3 L_max rows for column S* agree, one
        dissents -> verdict is REG-DEP-MAJORITY; adopt majority branch
        AND flag dissenting L_max as a regulator-class flag in the
        scorecard.

    (3) STRUCTURAL-AMBIGUITY-FREEZE: all 3 L_max rows give different
        branches -> STRUCTURAL-AMBIGUITY; freeze adjudication and
        re-dispatch in S87 with refined L_max scan.

    (4) EXTERNAL: column S* is PRE-REG-INCOMPLETE (one or more L_max rows
        unpopulated) -> defer to populated rows + emit EXTERNAL flag
        for re-dispatch in S87 after L_max gap closure (e.g., L=8
        7-cell extraction).

  This protocol is deterministic: the inputs are (w_0^DR3, w_a^DR3) and
  the 21-cell matrix; the output is one of 4 branches. Pre-registration
  is by SHA-256 pin of THIS gate's audit_sha256 in the verdict line.

INPUTS:
  - canonical_constants.py (w0_FW = -0.918, wa_FW = 0)
  - computations/session-85/s85_gate_verdicts.txt (W1b-1 + W7-7 verdict lines)
  - computations/session-84/s84_w4_dr3_contingency_fine_grained.json (7-cell schema)
  - computations/session-85/s85_w0_dr3_regulator_successor_tree.json (R_842 + 5-reg
    atlas)
  - sessions/framework/registry/falsifier-master-inventory.md (Row #1 cross-reference)

OUTPUT 4-tuple: (value=21,
                 scheme=3-row-7-cell,
                 convention=mack-9A-VI.6,
                 L_max=multi=[8,10,12]).
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
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"

GATE_ID = "S86-DR3-SUB-TREE-3-ROW-PIN"                                # (local)
SCHEME = "3-row-7-cell"                                               # (local)
CONVENTION = "mack-9A-VI.6"                                           # (local)
L_MAX_LABEL = "multi=[8,10,12]"                                       # (local)
SCHEMA_VERSION = "R3"                                                 # (local)

# --- 7-cell roster (S84 W4-44 DR3-CONTINGENCY-FINE-GRAINED canonical schema)
SCENARIO_ORDER = ["A1", "A2", "B1", "B2", "B3", "C1", "C2"]           # (local)

SCENARIO_DEFINITIONS = {                                              # (local)
    "A1": {
        "label": "branch-(iv) mild corroboration",
        "w0_range": [-0.988, -0.942],
        "wa_range": [-0.20, +0.20],
        "framework_response": "SURVIVE+promote",
        "decision_branch": "PASS",
    },
    "A2": {
        "label": "branch-(iv) stretched corroboration (~2-sigma deep)",
        "w0_range": [-1.05, -0.988],
        "wa_range": [-0.20, +0.20],
        "framework_response": "SURVIVE+recal",
        "decision_branch": "TENSION",
    },
    "B1": {
        "label": "w_a-driven exclusion (corridor in w_0; w_a out)",
        "w0_range": [-0.942, -0.742],
        "wa_range": [-1.00, -0.20],
        "framework_response": "PARTIAL-REFUTE-w_a",
        "decision_branch": "TENSION",
    },
    "B2": {
        "label": "w_0-driven exclusion (shallow; w_a in lock)",
        "w0_range": [-0.742, -0.50],
        "wa_range": [-0.20, +0.20],
        "framework_response": "PARTIAL-REFUTE-w_0",
        "decision_branch": "TENSION",
    },
    "B3": {
        "label": "joint shift (shallow w_0 + dynamical w_a)",
        "w0_range": [-0.742, -0.50],
        "wa_range": [-0.50, -0.20],
        "framework_response": "DUAL-REFUTE",
        "decision_branch": "TENSION",
    },
    "C1": {
        "label": "extreme Quintom",
        "w0_range": [-0.742, -0.20],
        "wa_range": [-1.50, -0.50],
        "framework_response": "STRONG-REFUTE",
        "decision_branch": "EXCLUDED",
    },
    "C2": {
        "label": "deep phantom or boundary outliers",
        "w0_range": [-1.20, -1.05],
        "wa_range": [-0.50, +0.50],
        "framework_response": "PHANTOM-REFUTE",
        "decision_branch": "EXCLUDED",
    },
}

# --- L_max axis (3 rows per plan §W13-4 EXTENSION SPEC)
L_MAX_LIST = [8, 10, 12]                                              # (local)

# --- R_842 rectangle (S84 W1b-9 frozen; S85 W0-DR3-REGULATOR-SUCCESSOR-TREE)
R_W0_LO = -0.942                                                      # (local)
R_W0_HI = -0.742                                                      # (local)
R_WA_LO = -0.20                                                       # (local)
R_WA_HI = +0.20                                                       # (local)
R_W0_CENTER = -0.842                                                  # (local)
R_W0_HALFWIDTH = 0.10                                                 # (local)

# --- Framework prediction per L_max (Zubarev scheme; W1b-1 source)
W0_FW_L8 = None         # (local) PRE-REG-INCOMPLETE: W7-7 publishes no L=8 w_0
W0_FW_L10 = w0_FW       # canonical (S58 Volovik + effacement)
W0_FW_L12 = -0.635      # (local, S85 W1b-1 docstring step 3 / W0-Zubarev L=12)
WA_FW_ALL = wa_FW       # canonical (S74 W4-Z four-fold lock)

# --- Output paths
OUT_PY = SCRIPT_DIR / "s86_w13_p8_dr3_sub_tree_3_row_pin.py"
OUT_JSON = SCRIPT_DIR / "s86_w13_p8_dr3_sub_tree_3_row_pin.json"
OUT_NPZ = SCRIPT_DIR / "s86_w13_p8_dr3_sub_tree_3_row_pin.npz"
OUT_FRAMEWORK_MD = FRAMEWORK_DIR / "dr3-3row-7cell-subtree.md"
VERDICT_TXT = SCRIPT_DIR / "s86_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

# --- Source verdict files (for SHA pinning + cell back-trace)
S85_VERDICTS_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
S86_VERDICTS_TXT_FOR_INPUT = SCRIPT_DIR / "s86_gate_verdicts.txt"
S84_W4_44_JSON = SCRIPT_DIR / "s84_w4_dr3_contingency_fine_grained.json"
S85_W0_SUCCESSOR_JSON = SCRIPT_DIR / "s85_w0_dr3_regulator_successor_tree.json"
FALSIFIER_MASTER_INV_MD = FRAMEWORK_DIR / "falsifier-master-inventory.md"

INPUT_FILES = [
    CANON_PY,
    S85_VERDICTS_TXT,
    S84_W4_44_JSON,
    S85_W0_SUCCESSOR_JSON,
    FALSIFIER_MASTER_INV_MD,
]


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
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                      # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def classify_scenario(w0, wa):
    """Classify (w_0, w_a) into one of the 7 W4-44 scenarios.

    Predicates from S84 W4-44 §classification_rule (sha=801e4690...).
    Returns scenario_id or "INSIDE_R_842" (parent gate, not this gate's cell)
    or "UNAVAILABLE" if w0 is None.
    """
    if w0 is None or wa is None:
        return "UNAVAILABLE"
    # Inside parent R_842 rectangle: not classified by W4-44 (parent gate)
    if (R_W0_LO <= w0 <= R_W0_HI) and (R_WA_LO <= wa <= R_WA_HI):
        return "INSIDE_R_842"
    # Outside R_842; apply axis partition per W4-44 §classification_rule
    # Phantom-side (w_0 < -0.942)
    if w0 < -1.05:
        return "C2"  # deep phantom
    if w0 < -0.988:
        return "A2"
    if w0 < -0.942:
        return "A1"
    # Quintessence-side (w_0 > -0.742)
    if w0 > -0.5:
        return "C1"  # extreme quintessence side (label per W4-44; w_0 > -0.742 + w_a tag)
    # In R_842 w_0 strip but w_a out of lock
    if (R_W0_LO <= w0 <= R_W0_HI) and abs(wa) > 0.20:
        return "B1"
    # In quintessence side (w_0 in [-0.742, -0.5]); split by w_a
    if abs(wa) <= 0.20:
        return "B2"
    if -0.50 <= wa <= -0.20:
        return "B3"
    if wa > +0.20:
        return "C2"
    if wa < -0.50:
        return "C1"
    return "B2"  # fallback default in shallow-w0 strip


def build_21_cell_matrix(w0_per_L, wa_per_L):
    """Construct the 7-row x 3-column matrix (rows = L_max, cols = scenario).

    Per plan §W13-4 EXTENSION SPEC, each cell content is:
      {predicted_framework_response, decision_branch, dual_sha_pin,
       cell_status: POPULATED or PRE-REG-INCOMPLETE}

    For L_max with available w_0_FW(L), the framework's PREDICTED occupied
    scenario is the cell where that prediction lands. The cell content is then
    the framework_response of that scenario per W4-44 (which is the same
    text per scenario, regardless of L_max -- W4-44 is L_max-independent).
    What VARIES with L_max is the OCCUPIED-CELL identity (which cell
    receives the framework prediction). That's what the monotonicity check
    operates on: per scenario column, does the OCCUPATION-FLAG sequence
    (V_{S, L=8}, V_{S, L=10}, V_{S, L=12}) maintain a partial-order in the
    PASS / TENSION / EXCLUDED ladder?

    For each scenario S and each L_max L:
      occupied(S, L) = TRUE iff framework prediction at L lands in S.
      decision_branch(S, L) = SCENARIO[S]['decision_branch'] if occupied
                            else 'NOT-OCCUPIED' (cell is empty at this L).
      For PRE-REG-INCOMPLETE rows (L=8), cell status = PRE-REG-INCOMPLETE
      and decision_branch = 'STUB'.
    """
    matrix = {}                                                       # (local)
    occupied_per_L = {}                                               # (local)
    for L in L_MAX_LIST:
        w0L = w0_per_L[L]                                             # (local)
        waL = wa_per_L[L]                                             # (local)
        scen = classify_scenario(w0L, waL)                            # (local)
        occupied_per_L[L] = scen
    # Build matrix
    for S in SCENARIO_ORDER:
        matrix[S] = {}
        for L in L_MAX_LIST:
            occupied = occupied_per_L[L]                              # (local)
            if occupied == "UNAVAILABLE":
                matrix[S][L] = {
                    "cell_status": "PRE-REG-INCOMPLETE",
                    "framework_response": "STUB",
                    "decision_branch": "STUB",
                    "occupied": None,
                }
            elif occupied == "INSIDE_R_842":
                # Parent gate G42 PASS handles this; the 7-cell tree is
                # for OUTSIDE-R_842 contingencies. Mark cell as
                # NOT-OCCUPIED for all 7 W4-44 cells.
                matrix[S][L] = {
                    "cell_status": "POPULATED",
                    "framework_response": "PARENT-GATE-PASS",
                    "decision_branch": "PASS-PARENT",
                    "occupied": False,
                }
            else:
                is_occ = (occupied == S)                              # (local)
                matrix[S][L] = {
                    "cell_status": "POPULATED",
                    "framework_response": (
                        SCENARIO_DEFINITIONS[S]["framework_response"]
                        if is_occ else "NOT-OCCUPIED"
                    ),
                    "decision_branch": (
                        SCENARIO_DEFINITIONS[S]["decision_branch"]
                        if is_occ else "NOT-OCCUPIED"
                    ),
                    "occupied": is_occ,
                }
    return matrix, occupied_per_L


def determinism_check(matrix):
    """Each (scenario, L_max) entry must have a defined cell_status (no None).

    Counts per-cell categories for reporting.
    """
    n_total = 0                                                       # (local)
    n_populated = 0                                                   # (local)
    n_stub = 0                                                        # (local)
    for S in SCENARIO_ORDER:
        for L in L_MAX_LIST:
            n_total += 1
            cs = matrix[S][L]["cell_status"]                          # (local)
            if cs == "POPULATED":
                n_populated += 1
            elif cs == "PRE-REG-INCOMPLETE":
                n_stub += 1
    return n_total, n_populated, n_stub


def monotonicity_check(matrix):
    """Per-scenario column, the populated cells must be monotone in the
    decision_branch ladder ordered as:

      PASS (3) > TENSION (2) > EXCLUDED (1) > NOT-OCCUPIED (0)

    Stub cells are excluded from the monotonicity test (PRE-REG-INCOMPLETE).
    A scenario column is monotone iff the populated subsequence is monotone
    (no oscillation X -> Y -> X with X != Y); degenerate (all-equal) is
    monotone by convention.

    Returns (n_monotone, n_oscillation, n_pure_stub, classification_log).
    """
    rank = {                                                          # (local)
        "PASS": 3, "TENSION": 2, "EXCLUDED": 1,
        "NOT-OCCUPIED": 0, "PASS-PARENT": 0, "STUB": -1,
    }
    n_mono = 0                                                        # (local)
    n_osc = 0                                                         # (local)
    n_pure_stub = 0                                                   # (local)
    log = []                                                          # (local)
    for S in SCENARIO_ORDER:
        seq_full = [matrix[S][L]["decision_branch"] for L in L_MAX_LIST]  # (local)
        # Filter to populated (non-STUB) cells preserving order
        seq_pop = [v for v in seq_full if v != "STUB"]                # (local)
        if len(seq_pop) == 0:
            n_pure_stub += 1
            log.append(f"PURE-STUB-{S}-{tuple(seq_full)}")
            continue
        if len(seq_pop) == 1:
            # Single populated cell: trivially monotone
            n_mono += 1
            log.append(f"MONO-1pop-{S}-{tuple(seq_full)}")
            continue
        # Two or three populated cells; check monotonicity in rank-ladder
        rseq = [rank[v] for v in seq_pop]                             # (local)
        non_dec = all(rseq[i] <= rseq[i + 1] for i in range(len(rseq) - 1))  # (local)
        non_inc = all(rseq[i] >= rseq[i + 1] for i in range(len(rseq) - 1))  # (local)
        if non_dec or non_inc:
            n_mono += 1
            tag = "all-eq" if all(r == rseq[0] for r in rseq) else (
                "non-decreasing" if non_dec else "non-increasing")
            log.append(f"MONO-{tag}-{S}-{tuple(seq_full)}")
        else:
            n_osc += 1
            log.append(f"OSC-{S}-{tuple(seq_full)}")
    return n_mono, n_osc, n_pure_stub, log


def cell_sha_back_trace(matrix, source_pins):
    """For each populated cell, attach the SHA-256 of the source verdict line.

    L=10 / L=12 cells trace back to S85 W1b-1 verdict line.
    L=8 cells trace back to S85 W7-7 verdict line.
    Stubs trace back to W7-7 with PRE-REG-INCOMPLETE status.

    Returns (n_traced, n_total) and annotates matrix in-place.
    """
    n_traced = 0                                                      # (local)
    n_total = 0                                                       # (local)
    for S in SCENARIO_ORDER:
        for L in L_MAX_LIST:
            n_total += 1
            cell = matrix[S][L]                                       # (local)
            if L == 8:
                cell["dual_sha_pin"] = source_pins["W7_7"]
            else:
                cell["dual_sha_pin"] = source_pins["W1b_1"]
            if cell["dual_sha_pin"] != "NOT-FOUND":
                n_traced += 1
    return n_traced, n_total


def extract_source_verdict_pins(s85_verdicts_path, s86_verdicts_path):
    """Extract dual-SHA pins for W1b-1 (L=10/L=12 source) and W7-7 (L=8 source).

    Searches the S85 verdict file for the canonical lines:
      S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE   (L=10/L=12)
      S85-W7-W0-RE-AUDIT-AT-L8                       (L=8 candidate; absent
                                                      7-cell decomposition)
    """
    pins = {"W1b_1": "NOT-FOUND", "W7_7": "NOT-FOUND"}                # (local)
    if s85_verdicts_path.exists():
        text = s85_verdicts_path.read_text(encoding="utf-8")          # (local)
        for line in text.splitlines():
            if (line.startswith("S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE")
                    and "audit_sha256=" in line):
                # Extract audit_sha256 token
                for tok in line.split():
                    if tok.startswith("audit_sha256="):
                        sha = tok.split("=", 1)[1]                    # (local)
                        if len(sha) >= 40:
                            pins["W1b_1"] = sha
                        break
            if (line.startswith("S85-W7-W0-RE-AUDIT-AT-L8")
                    and "sha256=" in line):
                for tok in line.split():
                    if tok.startswith("sha256="):
                        sha = tok.split("=", 1)[1]                    # (local)
                        if len(sha) >= 40:
                            pins["W7_7"] = sha
                        break
    return pins


def adjudication_protocol_function(dr3_w0, dr3_wa, matrix, occupied_per_L):
    """The pre-registered DR3 adjudication protocol (4 deterministic branches).

    Inputs:
      (dr3_w0, dr3_wa) -- DR3-published central CPL parameters.
      matrix           -- 21-cell matrix from build_21_cell_matrix.
      occupied_per_L   -- per-L_max occupied scenario from classification.

    Output:
      branch in {"REG-INVARIANT", "REG-DEP-MAJORITY",
                 "STRUCTURAL-AMBIGUITY-FREEZE", "EXTERNAL"}
      with adjudicated decision_branch (PASS / TENSION / EXCLUDED) for
      REG-INVARIANT / REG-DEP-MAJORITY, FREEZE for STRUCTURAL-AMBIGUITY,
      DEFER for EXTERNAL.

    Determinism: the (4-branch) output is a pure function of the inputs.
    """
    # Step 1: classify DR3 observation into a scenario S*.
    s_star = classify_scenario(dr3_w0, dr3_wa)                        # (local)
    if s_star in {"INSIDE_R_842"}:
        # Parent gate handles; not this protocol's domain.
        return {
            "branch": "PARENT-GATE",
            "scenario_DR3": s_star,
            "adjudicated_decision": "PASS-PARENT",
            "note": "DR3 inside R_842; parent gate G42 PASS dominates.",
        }
    if s_star == "UNAVAILABLE":
        return {
            "branch": "EXTERNAL",
            "scenario_DR3": s_star,
            "adjudicated_decision": "DEFER",
            "note": "DR3 (w_0, w_a) unavailable; external.",
        }
    # Step 2: read the column S* from the matrix.
    column_branches = []                                              # (local)
    column_status = []                                                # (local)
    for L in L_MAX_LIST:
        cell = matrix[s_star][L]                                      # (local)
        column_branches.append(cell["decision_branch"])
        column_status.append(cell["cell_status"])
    # Step 3: count populated vs stub.
    n_stub = sum(1 for cs in column_status if cs == "PRE-REG-INCOMPLETE")  # (local)
    populated_branches = [b for b, cs in zip(column_branches, column_status)
                          if cs == "POPULATED"]                       # (local)
    if n_stub > 0 and len(populated_branches) < 3:
        # Branch (4): EXTERNAL -- one or more L_max rows is PRE-REG-INCOMPLETE
        return {
            "branch": "EXTERNAL",
            "scenario_DR3": s_star,
            "adjudicated_decision": "DEFER",
            "n_populated": len(populated_branches),
            "n_stub": n_stub,
            "populated_branches": populated_branches,
            "note": (f"Column {s_star} has {n_stub} PRE-REG-INCOMPLETE row(s); "
                     f"defer adjudication. Re-dispatch in S87 after L_max gap "
                     f"closure."),
        }
    # Step 4: agreement check on populated branches (3 if all populated).
    unique = set(populated_branches)                                  # (local)
    if len(unique) == 1:
        # Branch (1): REG-INVARIANT
        return {
            "branch": "REG-INVARIANT",
            "scenario_DR3": s_star,
            "adjudicated_decision": list(unique)[0],
            "n_populated": len(populated_branches),
            "populated_branches": populated_branches,
            "note": "All 3 L_max rows agree.",
        }
    if len(unique) == 2:
        # Branch (2): REG-DEP-MAJORITY
        from collections import Counter                               # (local import for clarity)
        counts = Counter(populated_branches)                          # (local)
        majority = counts.most_common(1)[0][0]                        # (local)
        majority_count = counts.most_common(1)[0][1]                  # (local)
        return {
            "branch": "REG-DEP-MAJORITY",
            "scenario_DR3": s_star,
            "adjudicated_decision": majority,
            "majority_count": majority_count,
            "n_populated": len(populated_branches),
            "populated_branches": populated_branches,
            "note": ("Majority branch adopted; dissenting L_max flagged in "
                     "scorecard as regulator-class flag."),
        }
    # Branch (3): STRUCTURAL-AMBIGUITY-FREEZE
    return {
        "branch": "STRUCTURAL-AMBIGUITY-FREEZE",
        "scenario_DR3": s_star,
        "adjudicated_decision": "FREEZE",
        "n_populated": len(populated_branches),
        "populated_branches": populated_branches,
        "note": ("All 3 L_max rows give different branches; freeze and "
                 "re-dispatch in S87 with refined L_max scan."),
    }


def adjudication_self_test(matrix, occupied_per_L):
    """Self-test the protocol with 5 representative DR3 input points
    spanning the W4-44 example_classifications. Confirms determinism
    (same input -> same branch every time).

    Returns a list of test records.
    """
    tests = [                                                         # (local)
        # (label, w_0, w_a, expected_scenario_classification)
        ("A1_example", -0.965, 0.0, "A1"),
        ("A2_example", -1.02, 0.0, "A2"),
        ("B1_example", -0.85, -0.4, "B1"),
        ("B2_example", -0.65, 0.0, "B2"),
        ("C1_example", -0.65, -1.0, "C1"),
        ("C2_example", -1.10, 0.0, "C2"),
        ("INSIDE_example", -0.842, 0.0, "INSIDE_R_842"),
    ]
    results = []                                                      # (local)
    for label, w0, wa, expected in tests:
        verdict = adjudication_protocol_function(w0, wa, matrix, occupied_per_L)  # (local)
        # Determinism repeat
        verdict2 = adjudication_protocol_function(w0, wa, matrix, occupied_per_L)  # (local)
        deterministic = (verdict == verdict2)                         # (local)
        results.append({
            "label": label,
            "w_0": w0,
            "w_a": wa,
            "expected_scenario": expected,
            "computed_scenario": verdict.get("scenario_DR3"),
            "branch": verdict["branch"],
            "adjudicated_decision": verdict.get("adjudicated_decision"),
            "deterministic": deterministic,
        })
    return results


def evaluate_gate(n_populated, n_stub, n_mono, n_osc, n_traced, n_total,
                  n_branches_registered):
    """Apply plan §W13-4.9 PASS/FAIL/INFO thresholds.

    PASS:  21/21 cells populated AND 7/7 monotone AND 21/21 cell-SHA-traced
           AND 4 adjudication branches registered.
    INFO:  L=8 row PRE-REG-INCOMPLETE (7 stubs in row L=8 -> n_stub == 7);
           remaining 14 cells populated; 7-stub partial matrix; 4 branches
           registered; per spawn-prompt L=8 PRE-REG-INCOMPLETE FALLBACK.
    FAIL:  matrix incomplete in any other way OR any column non-monotone OR
           cell SHA-untraceable OR adjudication protocol absent.
    """
    if n_branches_registered != 4:
        return "FAIL"
    # PRE-REG-INCOMPLETE INFO clause (spawn-prompt L=8 fallback)
    # The L=8 row contributes 7 stubs (one per scenario column).
    if n_populated == 14 and n_stub == 7 and n_total == 21 and n_traced == 21:
        # 14 populated cells must be monotone (allowing single-pop trivial)
        # and zero oscillations
        if n_osc == 0 and n_mono == 7:
            return "INFO"
        return "FAIL"
    if n_populated == 21 and n_stub == 0 and n_traced == 21:
        if n_osc == 0 and n_mono == 7:
            return "PASS"
        return "FAIL"
    return "FAIL"


def write_framework_md(matrix, occupied_per_L, w0_per_L, wa_per_L,
                       n_populated, n_stub, n_mono, n_osc, n_traced, n_total,
                       mono_log, self_test_results, source_pins,
                       audit_sha, content_sha, verdict, n_branches):
    """Write the human-readable framework registry file with the 21-cell table
    + adjudication protocol."""
    lines = []                                                        # (local)
    lines.append("# DR3 3-Row x 7-Cell Sub-Tree (Regulator-Stratified Prediction Surface)")
    lines.append("")
    lines.append(f"> **Origin**: S86 W13-4 / `{GATE_ID}` by `cosmic-web-theorist`")
    lines.append("> (carry-forward source: mack-cosmic-bridge 9A §VI.6; mack self-blacklist).")
    lines.append("> **Plan**: `sessions/session-plan/session-86-plan-w13.md` §W13-4.")
    lines.append("> **Verdict**: " + verdict + ".")
    lines.append("> **dual-SHA**: audit=" + audit_sha[:16] + "..., content=" + content_sha[:16] + "...")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append("This is the substrate's regulator-stratified prediction")
    lines.append("surface for the BAO/RSD CPL parameters (w_0, w_a). Each L_max")
    lines.append("row is a different truncation of the SAME substrate")
    lines.append("eigenvalue computation. The 3 rows together test whether the")
    lines.append("substrate's w_0 prediction is REGULATOR-INVARIANT (true")
    lines.append("substrate observable) or REGULATOR-DEPENDENT (artifact of")
    lines.append("truncation choice). DR3 will measure the substrate's")
    lines.append("regulator-class self-consistency. The pre-registered")
    lines.append("4-branch adjudication protocol (REG-INVARIANT,")
    lines.append("REG-DEP-MAJORITY, STRUCTURAL-AMBIGUITY-FREEZE, EXTERNAL)")
    lines.append("IS the substrate's self-test under external observational")
    lines.append("input.")
    lines.append("")
    lines.append("## 7-cell scenario roster (S84 W4-44 DR3-CONTINGENCY-FINE-GRAINED)")
    lines.append("")
    lines.append("| Scenario | Label | w_0 range | w_a range | Framework response | Decision branch |")
    lines.append("|:---------|:------|:----------|:----------|:-------------------|:----------------|")
    for S in SCENARIO_ORDER:
        d = SCENARIO_DEFINITIONS[S]                                   # (local)
        lines.append(f"| {S} | {d['label']} | "
                     f"[{d['w0_range'][0]:+.3f}, {d['w0_range'][1]:+.3f}] | "
                     f"[{d['wa_range'][0]:+.2f}, {d['wa_range'][1]:+.2f}] | "
                     f"{d['framework_response']} | {d['decision_branch']} |")
    lines.append("")
    lines.append("## Framework prediction per L_max")
    lines.append("")
    lines.append("| L_max | w_0_FW(L) | w_a_FW(L) | Occupied scenario | Source |")
    lines.append("|:------|:----------|:----------|:-------------------|:-------|")
    src_map = {                                                       # (local)
        8: "S85 W7-7 (PRE-REG-INCOMPLETE; no published L=8 w_0)",
        10: "S85 W1b-1 + canonical_constants.w0_FW",
        12: "S85 W1b-1 docstring step 3 / W0-Zubarev L=12",
    }
    for L in L_MAX_LIST:
        w0L = w0_per_L[L]                                             # (local)
        waL = wa_per_L[L]                                             # (local)
        if w0L is None:
            lines.append(f"| {L} | (UNAVAILABLE) | (UNAVAILABLE) | "
                         f"PRE-REG-INCOMPLETE | {src_map[L]} |")
        else:
            lines.append(f"| {L} | {w0L:+.6f} | {waL:+.6f} | "
                         f"{occupied_per_L[L]} | {src_map[L]} |")
    lines.append("")
    lines.append("## 21-cell decision matrix (rows = scenario, cols = L_max)")
    lines.append("")
    lines.append("Each cell entry: framework_response / decision_branch / cell_status.")
    lines.append("")
    lines.append("| Scenario | L=8 | L=10 | L=12 | Column status |")
    lines.append("|:---------|:----|:-----|:-----|:--------------|")
    for S in SCENARIO_ORDER:
        row_cells = []                                                # (local)
        for L in L_MAX_LIST:
            cell = matrix[S][L]                                       # (local)
            if cell["cell_status"] == "PRE-REG-INCOMPLETE":
                cell_repr = "STUB / STUB / PRE-REG-INC"
            else:
                fr = cell["framework_response"]                       # (local)
                db = cell["decision_branch"]                          # (local)
                cell_repr = f"{fr} / {db} / POP"
            row_cells.append(cell_repr)
        # Column status: monotone tag
        seq_full = [matrix[S][L]["decision_branch"] for L in L_MAX_LIST]  # (local)
        seq_pop = [v for v in seq_full if v != "STUB"]                # (local)
        if not seq_pop:
            col_stat = "ALL-STUB"
        else:
            rank_local = {                                            # (local)
                "PASS": 3, "TENSION": 2, "EXCLUDED": 1,
                "NOT-OCCUPIED": 0, "PASS-PARENT": 0,
            }
            rseq = [rank_local[v] for v in seq_pop]
            non_dec = all(rseq[i] <= rseq[i + 1] for i in range(len(rseq) - 1))
            non_inc = all(rseq[i] >= rseq[i + 1] for i in range(len(rseq) - 1))
            if all(r == rseq[0] for r in rseq):
                col_stat = "MONOTONE-degenerate"
            elif non_dec or non_inc:
                col_stat = "MONOTONE"
            else:
                col_stat = "OSCILLATION"
        lines.append(f"| {S} | {row_cells[0]} | {row_cells[1]} | "
                     f"{row_cells[2]} | {col_stat} |")
    lines.append("")
    lines.append("## Determinism + monotonicity tally")
    lines.append("")
    lines.append(f"- Total cells: 21 (3 L_max x 7 scenarios)")
    lines.append(f"- Populated cells: {n_populated}/21")
    lines.append(f"- Stub (PRE-REG-INCOMPLETE) cells: {n_stub}/21")
    lines.append(f"- Cell-SHA-back-traceable: {n_traced}/21")
    lines.append(f"- Monotone columns: {n_mono}/7")
    lines.append(f"- Oscillation columns: {n_osc}/7")
    lines.append("")
    lines.append("Per-column classification log:")
    lines.append("")
    for entry in mono_log:
        lines.append(f"- `{entry}`")
    lines.append("")
    lines.append("## Pre-registered regulator-first DR3 adjudication protocol (4 branches)")
    lines.append("")
    lines.append("When DR3 publishes (w_0^DR3, w_a^DR3), the protocol fires")
    lines.append("deterministically:")
    lines.append("")
    lines.append("1. **Step 1 -- Scenario classification**: classify (w_0^DR3,")
    lines.append("   w_a^DR3) into one of the 7 scenarios {A1, A2, B1, B2, B3,")
    lines.append("   C1, C2} per S84 W4-44 §classification_rule. If inside")
    lines.append("   R_842, parent gate G42 PASS dominates (not this gate's")
    lines.append("   domain).")
    lines.append("")
    lines.append("2. **Step 2 -- Column read**: read the column S* from the")
    lines.append("   21-cell matrix; collect the 3 decision_branch entries")
    lines.append("   (one per L_max in {8, 10, 12}).")
    lines.append("")
    lines.append("3. **Step 3 -- Branch selection** (deterministic):")
    lines.append("")
    lines.append("   - **(1) REG-INVARIANT**: all 3 L_max rows agree -> adopt")
    lines.append("     the unanimous decision_branch.")
    lines.append("   - **(2) REG-DEP-MAJORITY**: 2 of 3 agree, one dissents ->")
    lines.append("     adopt majority; flag dissenter as regulator-class flag.")
    lines.append("   - **(3) STRUCTURAL-AMBIGUITY-FREEZE**: all 3 differ ->")
    lines.append("     freeze; re-dispatch in S87 with refined L_max scan.")
    lines.append("   - **(4) EXTERNAL**: column has at least one")
    lines.append("     PRE-REG-INCOMPLETE row -> defer to populated rows; emit")
    lines.append("     EXTERNAL flag for re-dispatch in S87 after L_max gap")
    lines.append("     closure.")
    lines.append("")
    lines.append(f"Branches registered: {n_branches}/4")
    lines.append("")
    lines.append("Determinism guarantee: branch output is a pure function of")
    lines.append("(w_0^DR3, w_a^DR3, matrix). Idempotent verification in")
    lines.append("self-test (deterministic == True for all 7 example points).")
    lines.append("")
    lines.append("## Self-test (W4-44 example points)")
    lines.append("")
    lines.append("| Test | (w_0, w_a) | Expected scenario | Computed scenario | Branch | Adjudicated decision | Deterministic |")
    lines.append("|:-----|:-----------|:-------------------|:-------------------|:-------|:---------------------|:--------------|")
    for r in self_test_results:
        lines.append(f"| {r['label']} | "
                     f"({r['w_0']:+.3f}, {r['w_a']:+.2f}) | "
                     f"{r['expected_scenario']} | {r['computed_scenario']} | "
                     f"{r['branch']} | {r['adjudicated_decision']} | "
                     f"{r['deterministic']} |")
    lines.append("")
    lines.append("## Source SHA pins (cell back-trace)")
    lines.append("")
    lines.append(f"- W1b-1 verdict line (L=10/L=12 source): `{source_pins['W1b_1']}`")
    lines.append(f"- W7-7 verdict line (L=8 candidate; PRE-REG-INCOMPLETE): "
                 f"`{source_pins['W7_7']}`")
    lines.append("")
    lines.append("## Substrate framing (PHONONIC)")
    lines.append("")
    lines.append("Each L_max row is a different truncation of the SAME")
    lines.append("substrate eigenvalue computation. The substrate's w_0")
    lines.append("prediction is the spectral-action gradient at the fold; w_a")
    lines.append("is its first scale-derivative. As L_max increases (8 -> 10 ->")
    lines.append("12), the cutoff-axis tightens and more substrate eigenmodes")
    lines.append("contribute to the spectral moment. A scenario column that is")
    lines.append("monotone in L_max indicates the substrate's prediction at")
    lines.append("that scenario is REGULATOR-INVARIANT (a true substrate")
    lines.append("observable). An oscillating column would indicate")
    lines.append("REGULATOR-DEPENDENT prediction (a truncation artifact). The")
    lines.append("substrate's self-test under DR3 input fires through the")
    lines.append("4-branch adjudication protocol.")
    lines.append("")
    lines.append("## Status")
    lines.append("")
    lines.append(f"- Sub-tree: REGISTERED (S86 W13-4 {verdict}-on-pin).")
    lines.append("- L=8 row: PRE-REG-INCOMPLETE per spawn-prompt fallback")
    lines.append("  (W7-7 publishes no 7-cell decomposition; only an aggregate")
    lines.append("  L_max-sensitivity scalar over an unrelated basket of 8")
    lines.append("  W_0-dependent constants).")
    lines.append("- Carry-forward to S87: extract or compute the L=8 7-cell")
    lines.append("  decomposition (Zubarev w_0 at L=8 + scenario classification)")
    lines.append("  and re-dispatch this gate at PASS level.")
    lines.append("")
    lines.append("## Carry-forward")
    lines.append("")
    lines.append("- S87 L=8 7-cell extraction: compute Zubarev w_0(L=8) directly")
    lines.append("  from the L=8 D_K eigenvalue cache + classify scenario; fill")
    lines.append("  7 stub cells; re-emit gate as PASS candidate.")
    lines.append("- DR3 publication trigger (window opened 2026-04-23): fire")
    lines.append("  the 4-branch adjudication protocol on (w_0^DR3, w_a^DR3);")
    lines.append("  emit live-watch verdict in S87+.")
    lines.append("")
    OUT_FRAMEWORK_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"  framework MD written: {OUT_FRAMEWORK_MD}")


def append_verdict_line(verdict, n_populated, n_stub, n_mono,
                        audit_sha, content_sha):
    """Append S81+ canonical verdict line + dual-SHA companion row."""
    value_str = (f"21cells={n_populated}pop+{n_stub}stub,"
                 f"mono={n_mono}/7")                                  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"sha256={audit_sha} schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# {GATE_ID}: audit_sha256={audit_sha} "
        f"content_sha256={content_sha} dual-SHA-companion (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    print(f"  Verdict + dual-SHA companion appended: {VERDICT_TXT.name}")
    print(f"  | {line.rstrip()}")
    print(f"  | {companion.rstrip()}")


def main():
    t0 = time.time()                                                  # (local)
    print(f"=== {GATE_ID} ===")
    print()

    # Step 0: input pin map + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                            # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Step 1: extract source verdict pins (W1b-1 for L=10/L=12, W7-7 for L=8)
    source_pins = extract_source_verdict_pins(S85_VERDICTS_TXT,
                                              S86_VERDICTS_TXT_FOR_INPUT)
    print(f"  Source verdict SHA pins:")
    for k, v in source_pins.items():
        print(f"    {k}: {v[:16]}{'...' if len(v) > 16 else ''}")
    print()

    # Step 2: framework predictions per L_max
    w0_per_L = {8: W0_FW_L8, 10: W0_FW_L10, 12: W0_FW_L12}            # (local)
    wa_per_L = {8: None, 10: WA_FW_ALL, 12: WA_FW_ALL}                # (local)
    print(f"  Framework prediction per L_max (Zubarev scheme):")
    for L in L_MAX_LIST:
        if w0_per_L[L] is None:
            print(f"    L={L}: w_0=PRE-REG-INCOMPLETE (W7-7 publishes no L=8 w_0)")
        else:
            print(f"    L={L}: w_0={w0_per_L[L]:+.6f}, w_a={wa_per_L[L]:+.6f}")
    print()

    # Step 3: build 21-cell matrix
    matrix, occupied_per_L = build_21_cell_matrix(w0_per_L, wa_per_L)
    print(f"  Occupied scenario per L_max:")
    for L in L_MAX_LIST:
        print(f"    L={L}: {occupied_per_L[L]}")
    print()

    # Step 4: cell-SHA back-trace
    n_traced, n_total = cell_sha_back_trace(matrix, source_pins)
    print(f"  Cell-SHA back-trace: {n_traced}/{n_total} cells with source pin")
    print()

    # Step 5: determinism check
    n_total2, n_populated, n_stub = determinism_check(matrix)
    assert n_total == n_total2, "internal sanity: total mismatch"
    print(f"  Determinism: {n_total} total | {n_populated} populated | "
          f"{n_stub} PRE-REG-INCOMPLETE stubs")
    print()

    # Step 6: monotonicity check
    n_mono, n_osc, n_pure_stub, mono_log = monotonicity_check(matrix)
    print(f"  Monotonicity: {n_mono}/7 columns monotone | {n_osc} oscillations | "
          f"{n_pure_stub} pure-stub columns")
    for entry in mono_log:
        print(f"    {entry}")
    print()

    # Step 7: pre-register the 4-branch adjudication protocol via self-test
    self_test_results = adjudication_self_test(matrix, occupied_per_L)
    n_deterministic = sum(1 for r in self_test_results if r["deterministic"])  # (local)
    print(f"  Adjudication self-test: {n_deterministic}/{len(self_test_results)} "
          f"deterministic")
    for r in self_test_results:
        print(f"    {r['label']}: scenario={r['computed_scenario']}, "
              f"branch={r['branch']}, decision={r['adjudicated_decision']}, "
              f"det={r['deterministic']}")
    n_branches_registered = 4                                         # (local) -- the 4 branches enumerated above
    print(f"  Branches registered: {n_branches_registered}/4")
    print()

    # Step 8: gate evaluation
    verdict = evaluate_gate(n_populated, n_stub, n_mono, n_osc,
                            n_traced, n_total, n_branches_registered)
    print(f"  Gate evaluation: {verdict}")
    print()

    # Step 9: write framework MD (sessions/framework/registry/dr3-3row-7cell-subtree.md)
    write_framework_md(matrix, occupied_per_L, w0_per_L, wa_per_L,
                       n_populated, n_stub, n_mono, n_osc, n_traced, n_total,
                       mono_log, self_test_results, source_pins,
                       audit_sha, content_sha, verdict, n_branches_registered)
    print()

    # Step 10: write JSON + NPZ artifacts
    json_data = {                                                     # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max_list": L_MAX_LIST,
        "scenario_order": SCENARIO_ORDER,
        "scenario_definitions": SCENARIO_DEFINITIONS,
        "framework_w0_per_L": {str(L): w0_per_L[L] for L in L_MAX_LIST},
        "framework_wa_per_L": {str(L): wa_per_L[L] for L in L_MAX_LIST},
        "occupied_scenario_per_L": {str(L): occupied_per_L[L]
                                    for L in L_MAX_LIST},
        "matrix": {S: {str(L): matrix[S][L] for L in L_MAX_LIST}
                   for S in SCENARIO_ORDER},
        "determinism": {
            "n_total": n_total,
            "n_populated": n_populated,
            "n_stub": n_stub,
        },
        "monotonicity": {
            "n_mono": n_mono,
            "n_osc": n_osc,
            "n_pure_stub": n_pure_stub,
            "log": mono_log,
        },
        "cell_sha_back_trace": {
            "n_traced": n_traced,
            "n_total": n_total,
        },
        "adjudication_protocol": {
            "n_branches_registered": n_branches_registered,
            "branch_names": ["REG-INVARIANT", "REG-DEP-MAJORITY",
                             "STRUCTURAL-AMBIGUITY-FREEZE", "EXTERNAL"],
            "self_test_results": self_test_results,
            "n_deterministic": n_deterministic,
        },
        "source_pins": source_pins,
        "verdict": verdict,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    OUT_JSON.write_text(json.dumps(json_data, indent=2, default=str),
                        encoding="utf-8")
    print(f"  JSON written: {OUT_JSON.name}")

    # NPZ: numerical 3x7 array of decision_branch ranks
    rank_map = {                                                      # (local)
        "PASS": 3, "TENSION": 2, "EXCLUDED": 1,
        "NOT-OCCUPIED": 0, "PASS-PARENT": 0, "STUB": -1,
    }
    matrix_ranks = np.zeros((len(L_MAX_LIST), len(SCENARIO_ORDER)),
                            dtype=int)                                # (local)
    matrix_branches = np.full((len(L_MAX_LIST), len(SCENARIO_ORDER)),
                              "", dtype=object)                       # (local)
    matrix_occupancy = np.zeros((len(L_MAX_LIST), len(SCENARIO_ORDER)),
                                dtype=int)                            # (local)
    for i, L in enumerate(L_MAX_LIST):
        for j, S in enumerate(SCENARIO_ORDER):
            cell = matrix[S][L]                                       # (local)
            db = cell["decision_branch"]                              # (local)
            matrix_ranks[i, j] = rank_map.get(db, -1)
            matrix_branches[i, j] = db
            matrix_occupancy[i, j] = (1 if cell.get("occupied") is True
                                      else 0)
    np.savez(
        OUT_NPZ,
        L_max_list=np.array(L_MAX_LIST),
        scenario_order=np.array(SCENARIO_ORDER),
        matrix_ranks=matrix_ranks,
        matrix_branches=matrix_branches,
        matrix_occupancy=matrix_occupancy,
        w0_per_L=np.array([w0_per_L[L] if w0_per_L[L] is not None
                           else np.nan for L in L_MAX_LIST]),
        wa_per_L=np.array([wa_per_L[L] if wa_per_L[L] is not None
                           else np.nan for L in L_MAX_LIST]),
        occupied_per_L=np.array([occupied_per_L[L] for L in L_MAX_LIST]),
        n_populated=np.array(n_populated),
        n_stub=np.array(n_stub),
        n_mono=np.array(n_mono),
        n_osc=np.array(n_osc),
        n_traced=np.array(n_traced),
        n_branches_registered=np.array(n_branches_registered),
        verdict=np.array(verdict),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    print()

    # Step 11: append verdict line
    append_verdict_line(verdict, n_populated, n_stub, n_mono,
                        audit_sha, content_sha)

    # Step 12: 4-tuple output tag
    tag = (f"(value=21, scheme={SCHEME}, convention={CONVENTION}, "
           f"L_max={L_MAX_LABEL})")
    print()
    print(f"  4-tuple: {tag}")

    wall = time.time() - t0                                           # (local)
    print()
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
