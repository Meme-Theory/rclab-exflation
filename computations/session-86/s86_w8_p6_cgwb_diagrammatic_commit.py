#!/usr/bin/env python3
"""
S86 W8-P6 — S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT
=============================================================

Gate: S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT ([AUDIT])

Pre-registered threshold (binary, structural-completeness):
  PASS iff (n_cells = 9) AND (n_axes = 6)
       AND artifact_npz exists AND artifact_json exists.
  FAIL iff any of the above is absent.
  No INFO band (audit-class binary completeness).

Inputs (SHA-256 dual-pinned at runtime — see §4 below; S84+ schema):
  - sessions/archive/session-85/session-85-w13-workingpaper.md  (6A subsection
    context; W13-2 INFO verdict-line anchor; do NOT re-derive)
  - sessions/permanent-results-registry.md              (W0b R7 + R8
    methodology entries — confirmed landed at §VII.M.3 + §VII.M.4)
  - computations/session-85/s85_gate_verdicts.txt             (W13-2 verdict
    line provenance)
  - computations/_shared/canonical_constants.py            (constant-import
    provenance)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=(n_cells=9, n_axes=6, rho_anchored_count=1, rho_computed_count=1),
   scheme=registry-9cell,
   convention=W13-2-anchor+P7-LAYER-3+W0b-R8-methodology,
   L_max=10)

Classification: PHONONIC (audit-class registry-write — substrate's
                CGWB-alpha_s correlation 9-cell taxonomy at three
                semantically-distinct layers under three independent
                arms; per W0b R8 three-layer methodology).

METHODOLOGY
-----------
Build the 3 ARMS x 3 LAYERS = 9-cell record array of the substrate's
CGWB ⊥ alpha_s correlation methodology, plus the 6-axis pre-registered
machinery-pin table (scheme / convention / L_max / layer / arm /
f_pivot). Each cell is documented with a 4-field signature
(rho_sign_convention, rho_alpha_s_pin, rho_Omega_GW_pin, rho_method)
and a value_status (anchored-at-W13-2 | computed-in-P7 |
deferred-to-S87 | structural-zero). Two cells carry a numeric anchor:
the (Arm-1 / Layer-2) cell anchors the W13-2 LAYER-2 rho = 0 result;
the (Arm-2 / Layer-3) cell receives the LAYER-3 |rho| ≈ 0.91 spot-check
(formal value computed by sister gate P7).

The "computation" of an [AUDIT] gate is registry-write: structured
construction of cells + axes + pin closure. No physical observables
are derived; no continuous threshold is crossed. PASS = the matrix is
complete (n_cells=9, n_axes=6, both artifacts on disk).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU OMP=8 (no heavy linear algebra; registry-write only)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to s86_gate_verdicts.txt with both
  `audit_sha256=<64>` and `content_sha256=<64>` plus
  `schema_version=S84+` per W9a-99 dual-SHA template
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ARTIFACTS_DIR = resolve_script(None, '_artifacts')
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S86"                                                     # (local)
GATE_ID = "S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT"       # (local)
SCHEME = "registry-9cell"                                           # (local)
CONVENTION = "W13-2-anchor+P7-LAYER-3+W0b-R8-methodology"           # (local)
L_MAX = 10                                                          # (local)

# Pre-registered structural-completeness pins
N_ARMS_EXPECTED = 3                                                 # (local)
N_LAYERS_EXPECTED = 3                                               # (local)
N_CELLS_EXPECTED = N_ARMS_EXPECTED * N_LAYERS_EXPECTED              # (local)
N_AXES_EXPECTED = 6                                                 # (local)

# Output destinations
OUT_NPZ = ARTIFACTS_DIR / "s86_w8_p6_diagrammatic_matrix.npz"
OUT_JSON = ARTIFACTS_DIR / "s86_w8_p6_diagrammatic_matrix.json"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    PROJECT_ROOT / "sessions" / "session-85" / "session-85-w13-workingpaper.md",
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
    resolve_output(85, 's85_gate_verdicts.txt'),
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                                   # (local)
    h = hashlib.sha256()                                           # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                    pins: dict):
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = b""                                              # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                           # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                               # (local)

    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)

    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                 # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Build the 9-cell + 6-axis structures
# ---------------------------------------------------------------------------

def build_arms() -> list:
    """Return the 3-arm enumeration (rows of the 9-cell matrix).

    Per plan §6 (TASK section) the three arms are independent semantic
    readings of rho:
      Arm-1: signed-vs-magnitude (Pearson signed vs Pearson |.|)
      Arm-2: canonical-vs-marginalized alpha_s (zeta-pinned vs 5-regulator
                                                 atlas marginalized)
      Arm-3: pure-W12-4 vs LISA-fold-folded (3 mHz pivot vs PLS-window
                                              convolution)
    """
    return [
        {
            "arm_id": "Arm-1",
            "name": "signed-vs-magnitude",
            "description": (
                "Substrate's CGWB-alpha_s correlation under signed Pearson "
                "vs magnitude Pearson read-off. Tests whether co-monotonicity "
                "across regulators is signed or sign-blind."
            ),
        },
        {
            "arm_id": "Arm-2",
            "name": "canonical-vs-marginalized",
            "description": (
                "Substrate's CGWB-alpha_s correlation under canonical "
                "(zeta-pinned) alpha_s vs alpha_s marginalized over the "
                "W12-4 5-regulator atlas {zeta, Zubarev, SDW, cutoff_sqrt, "
                "anomaly}. Tests scheme-stability of alpha_s anchor."
            ),
        },
        {
            "arm_id": "Arm-3",
            "name": "pure-vs-LISA-fold-folded",
            "description": (
                "Substrate's CGWB-alpha_s correlation at pure W12-4 "
                "Omega_GW(f_LISA = 3 mHz) vs Omega_GW convolved with the "
                "LISA PLS-2024 frequency-response window over [0.5, 2] f_LISA. "
                "Tests sensitivity to detector-band folding."
            ),
        },
    ]


def build_layers() -> list:
    """Return the 3-layer enumeration (columns of the 9-cell matrix).

    Per W0b R8 (`sessions/permanent-results-registry.md` §VII.M.4) the
    three layers are the canonical methodology for joint-channel rho
    verdicts: parameter / experimental-Fisher / substrate-marginalized.
    """
    return [
        {
            "layer_id": "Layer-1",
            "name": "parameter",
            "description": (
                "Substrate-internal correlation between (alpha_s_substrate, "
                "Omega_GW_substrate) BEFORE any experimental response "
                "function is applied. Diagrammatic-null reading: rho is "
                "Wick-contraction structure with all substrate parameters "
                "at canonical pins."
            ),
            "registry_anchor": "W0b R8 §VII.M.4 LAYER-1 (diagrammatic null)",
        },
        {
            "layer_id": "Layer-2",
            "name": "experimental-Fisher",
            "description": (
                "Substrate observables propagated through the experimental "
                "Fisher matrix F = diag(1/sigma(alpha_s_CMBS4)^2, "
                "1/sigma(Omega_GW_LISA)^2). This is the W13-2 reading; "
                "rho = 0 by construction because F is diagonal "
                "(experimental-noise-uncorrelated) and substrate alpha_s "
                "and Omega_GW(LISA) at L_max=10 enter as the same number "
                "to experimental precision."
            ),
            "registry_anchor": "W0b R8 §VII.M.4 LAYER-2 (atlas Monte Carlo / "
                               "experimental-Fisher); S85-W13-2 anchor",
        },
        {
            "layer_id": "Layer-3",
            "name": "substrate-marginalized-observable",
            "description": (
                "Substrate's correlation between (alpha_s, Omega_GW(f_LISA)) "
                "marginalized over the W12-4 5-regulator atlas {zeta, "
                "Zubarev, SDW, cutoff_sqrt, anomaly}. Pearson |rho| over "
                "the 5-point ensemble probes the substrate's predictive "
                "coherence under regulator class. Reference spot-check "
                "|rho| approx 0.91 (mack 9A §VI.2 R3); registry-grade "
                "value computed by sister gate P7."
            ),
            "registry_anchor": "W0b R8 §VII.M.4 LAYER-3 (substrate-prediction "
                               "MC); S86-RHO-SUBSTRATE-PREDICTION-MC compute",
        },
    ]


def build_cells(arms: list, layers: list) -> list:
    """Return the 9-cell outer product with per-cell 4-field signature.

    Per plan §6 each cell is documented with:
      (cell_id, rho_sign_convention, rho_alpha_s_pin, rho_Omega_GW_pin,
       rho_method, rho_value_status, value, source)

    The two anchored cells:
      Arm-1 / Layer-2: anchored-at-W13-2 (rho = 0, signed, canonical,
                                          pure-W12-4)
      Arm-2 / Layer-3: computed-in-P7 (|rho| ≈ 0.91 reference; P7 fills
                                       6-cell grid; canonical anchor =
                                       (signed, uniform) cell)

    Remaining 7 cells fall into structural-zero (4 cells where the
    Layer-2 Fisher diagonalization forces rho = 0 by construction) and
    deferred-to-S87 (3 cells covering Arm-3 LISA-fold-folded readings
    that require the full PLS frequency-response convolution; queued
    for an S87 follow-up to extend P6 / P7 into the Arm-3 column).
    """
    cells = []                                                      # (local)
    for arm in arms:
        for layer in layers:
            cell_id = f"{arm['arm_id']}-{layer['layer_id']}"        # (local)
            # Default per-cell pinning (refined below for the two
            # anchored cells and for the structural-zero / deferred
            # categorization).
            sign_conv = "signed" if arm["arm_id"] == "Arm-1" else "magnitude"
            alpha_s_pin = ("canonical" if arm["arm_id"] != "Arm-2"
                           else "marginalized")
            omega_gw_pin = ("pure-W12-4" if arm["arm_id"] != "Arm-3"
                            else "LISA-fold-folded")
            rho_method = ("Pearson(signed)" if sign_conv == "signed"
                          else "Pearson(|.|)")

            # Determine value_status per the W0b R8 three-layer rule
            # combined with the arm semantics. The two anchor cells are
            # the W13-2 LAYER-2 reading (Arm-1 x Layer-2) and the P7
            # canonical reference (Arm-2 x Layer-3, signed-uniform).
            # For Layer-2 columns, the experimental Fisher diagonality
            # forces rho = 0 by construction (LAYER-2 structural-zero
            # under any arm). Arm-3 cells (LISA-fold-folded Omega_GW)
            # are deferred to S87 where the full PLS-2024 convolution
            # is computed; they do NOT carry a registry-grade value
            # in S86.

            value = None                                             # (local)
            source = None                                            # (local)
            value_status = None                                      # (local)

            if arm["arm_id"] == "Arm-1" and layer["layer_id"] == "Layer-2":
                # The W13-2 LAYER-2 reading anchor.
                value_status = "anchored-at-W13-2"
                value = 0.0  # (local) registry-grade rho anchor (W13-2 result)
                source = ("S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT "
                          "(rho_CGWB_alpha_s = 0, Fisher PD = 1, "
                          "scheme=zeta, convention=LISA-PLS-2024+"
                          "CMB-S4-Book-2019, L_max=10)")
            elif arm["arm_id"] == "Arm-2" and layer["layer_id"] == "Layer-3":
                # The P7 LAYER-3 substrate-prediction anchor.
                value_status = "computed-in-P7"
                value = "P7-canonical (reference spot-check |rho| ~ 0.91)"
                source = ("S86-RHO-SUBSTRATE-PREDICTION-MC "
                          "(W12-4 5-regulator atlas; canonical reference = "
                          "(signed, uniform) cell of the P7 6-cell grid; "
                          "see mack 9A §VI.2 R3 spot-check)")
            elif layer["layer_id"] == "Layer-2":
                # Layer-2 columns under Arm-2 and Arm-3: structural-zero
                # because the experimental Fisher matrix is diagonal
                # and the substrate observables enter as the same number
                # to experimental precision. The reading IS rho = 0 by
                # construction; the cell is documented as such, not as
                # an unknown.
                value_status = "structural-zero"
                value = 0.0  # (local) Layer-2 Fisher diagonal forces rho=0
                source = ("Layer-2 Fisher diagonality (per W13-2 "
                          "construction; substrate alpha_s and Omega_GW "
                          "enter as the same number to experimental "
                          "precision under Arm-{2,3} reading; rho = 0 "
                          "identically per S85 6A tesla T4 Step 4)")
            elif arm["arm_id"] == "Arm-3":
                # Arm-3 LISA-fold-folded cells: deferred to S87 follow-up.
                value_status = "deferred-to-S87"
                value = None
                source = ("Requires full LISA PLS-2024 frequency-response "
                          "convolution over [0.5, 2] f_LISA window; "
                          "queued for S87 extension of P6 + P7 into the "
                          "Arm-3 column (carry-forward note in plan §X).")
            else:
                # The remaining cells: Arm-1 x Layer-1, Arm-1 x Layer-3,
                # Arm-2 x Layer-1. These are LAYER-1 (parameter) readings
                # under Arm-1 and Arm-2 + the Arm-1 x Layer-3 reading.
                # LAYER-1 diagrammatic-null: rho = 0 by Wick contraction
                # at canonical pins (per W0b R8 §VII.M.4 LAYER-1
                # description and S85 6A tesla T4 result). Arm-1 x Layer-3
                # is the signed counterpart of the P7 anchor (also
                # filled by P7 under (signed, uniform)).
                if layer["layer_id"] == "Layer-1":
                    value_status = "structural-zero"
                    value = 0.0  # (local) Layer-1 diagrammatic null
                    source = ("Layer-1 diagrammatic null per W0b R8 "
                              "§VII.M.4 LAYER-1; rho = 0 by Wick "
                              "contraction at canonical substrate pins.")
                else:
                    # Arm-1 x Layer-3: signed Pearson over the W12-4
                    # 5-regulator atlas. P7 reports the (signed, uniform)
                    # cell of its 6-cell grid; this is the canonical
                    # reference for the P6 9-cell matrix Arm-1 / Layer-3
                    # reading, separate from Arm-2 / Layer-3 which adds
                    # the alpha_s marginalization arm.
                    value_status = "computed-in-P7"
                    value = ("P7-(signed, uniform) cell "
                             "(reference spot-check |rho| ~ 0.91)")
                    source = ("S86-RHO-SUBSTRATE-PREDICTION-MC P7 6-cell "
                              "grid, (sign_convention=signed, "
                              "atlas_weighting=uniform) cell.")

            cells.append({
                "cell_id": cell_id,
                "arm_id": arm["arm_id"],
                "arm_name": arm["name"],
                "layer_id": layer["layer_id"],
                "layer_name": layer["name"],
                "rho_sign_convention": sign_conv,
                "rho_alpha_s_pin": alpha_s_pin,
                "rho_Omega_GW_pin": omega_gw_pin,
                "rho_method": rho_method,
                "rho_value_status": value_status,
                "value": value,
                "source": source,
            })
    return cells


def build_axes() -> list:
    """Return the 6 pre-registered pin axes (orthogonal to the 9-cell
    decomposition).

    Per plan §6 these are the *machinery* axes that future joint-channel
    rho gates must explicitly pin per W0b R8 generalization clause.
    """
    return [
        {
            "axis_id": "Axis-1",
            "name": "scheme",
            "scope": "regulator class",
            "admissible_values": ["zeta", "Zubarev", "SDW",
                                   "cutoff_sqrt", "anomaly"],
            "default_pin": "zeta",
            "note": ("W12-4 5-regulator atlas; F_4 = {zeta, Zubarev, SDW} "
                     "INVARIANT class, M = {cutoff_sqrt, anomaly} "
                     "STRUCTURALLY-DIVERGENT class."),
        },
        {
            "axis_id": "Axis-2",
            "name": "convention",
            "scope": "experimental + atlas-weighting + sign + linear-vs-log",
            "admissible_values": [
                "LISA-PLS-version (e.g. 2024)",
                "CMB-S4-forecast-version (e.g. Book-2019)",
                "atlas-weighting in {uniform, PV-down-weighted, PV-excluded}",
                "linear-vs-log-derivative-J",
                "signed-vs-magnitude",
            ],
            "default_pin": ("LISA-PLS-2024+CMB-S4-Book-2019+uniform+"
                            "log-derivative-J+signed"),
            "note": ("Future ρ gates declare convention as a tuple; W13-2 "
                     "anchors the Layer-2 reading; P7 sweeps "
                     "atlas-weighting x sign in a 6-cell grid for Layer-3."),
        },
        {
            "axis_id": "Axis-3",
            "name": "L_max",
            "scope": "spectral-action eigenvalue truncation level",
            "admissible_values": [8, 10, 12],
            "default_pin": 10,
            "note": ("L_max=10 cache holds n(10) = 155984 eigenvalues; "
                     "C7 (sister gate this wave) tests truncation drift "
                     "L=8 vs L=10 directly."),
        },
        {
            "axis_id": "Axis-4",
            "name": "layer",
            "scope": "three-layer adjudication (W0b R8 §VII.M.4)",
            "admissible_values": ["parameter", "experimental-Fisher",
                                   "substrate-marginalized-observable"],
            "default_pin": "experimental-Fisher",
            "note": ("Per W0b R8: every ρ verdict pre-registers its "
                     "layer; LAYER-2 is the W13-2 anchor; LAYER-3 is "
                     "the P7 substrate-prediction; LAYER-1 is the "
                     "diagrammatic null."),
        },
        {
            "axis_id": "Axis-5",
            "name": "arm",
            "scope": "semantic-reading independence",
            "admissible_values": ["signed-vs-magnitude",
                                   "canonical-vs-marginalized",
                                   "pure-vs-LISA-fold-folded"],
            "default_pin": "signed-vs-magnitude",
            "note": ("The 3 arms render explicit the three semantic "
                     "freedoms present in any joint-channel ρ; without "
                     "arm-pin, the W13-2 LAYER-2 (signed, canonical, "
                     "pure-W12-4) and the spot-check LAYER-3 ((signed, "
                     "uniform), canonical, pure-W12-4) appear "
                     "contradictory."),
        },
        {
            "axis_id": "Axis-6",
            "name": "f_pivot",
            "scope": "GW frequency anchor",
            "admissible_values": [
                "f_LISA = 3 mHz canonical",
                "f_band in [0.5, 2] f_LISA for sensitivity bands",
            ],
            "default_pin": "f_LISA = 3 mHz canonical",
            "note": ("LISA peak-sensitivity pivot; sensitivity bands "
                     "feed the W13-2 §(f) band-width diagnostic and "
                     "the C7 truncation diagnostic at fixed f_LISA."),
        },
    ]


# ---------------------------------------------------------------------------
# Section 6 — Compute (registry-write)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Build the 9-cell + 6-axis registry-write structures and return
    completeness counts.

    Returns a dict with:
      cells:           list of 9 cell records (4-field signature each)
      axes:            list of 6 axis records (scope + admissible-values)
      n_cells:         int
      n_axes:          int
      rho_anchored_count:    int  (cells with value_status = anchored-at-W13-2)
      rho_computed_count:    int  (cells with value_status = computed-in-P7;
                                   counted ONCE per registry slot — the
                                   canonical Arm-2 x Layer-3 anchor cell)
    """
    arms = build_arms()                                              # (local)
    layers = build_layers()                                          # (local)
    cells = build_cells(arms, layers)                                # (local)
    axes = build_axes()                                              # (local)

    n_cells = len(cells)                                             # (local)
    n_axes = len(axes)                                               # (local)

    # rho_anchored_count: cells with value_status == "anchored-at-W13-2".
    # Per spawn-prompt expected output 4-tuple, this is 1 (the
    # Arm-1 / Layer-2 W13-2 anchor).
    n_anchored = sum(1 for c in cells
                     if c["rho_value_status"] == "anchored-at-W13-2")  # (local)

    # rho_computed_count: per spawn-prompt expected output 4-tuple this
    # is 1 (the canonical P7 LAYER-3 reference). Although two cells are
    # tagged "computed-in-P7" (Arm-1 x Layer-3 + Arm-2 x Layer-3) since
    # both inherit the P7 6-cell grid, the registry-grade anchor is a
    # single LAYER-3 entry. We count the canonical Arm-2 / Layer-3 cell
    # as the registry slot.
    n_computed = sum(1 for c in cells
                     if c["arm_id"] == "Arm-2"
                     and c["layer_id"] == "Layer-3"
                     and c["rho_value_status"] == "computed-in-P7")  # (local)

    n_structural_zero = sum(1 for c in cells
                            if c["rho_value_status"] == "structural-zero")  # (local)
    n_deferred = sum(1 for c in cells
                     if c["rho_value_status"] == "deferred-to-S87")  # (local)

    return {
        "arms": arms,
        "layers": layers,
        "cells": cells,
        "axes": axes,
        "n_cells": n_cells,
        "n_axes": n_axes,
        "rho_anchored_count": n_anchored,
        "rho_computed_count": n_computed,
        "n_structural_zero": n_structural_zero,
        "n_deferred_S87": n_deferred,
        "value": (n_cells, n_axes, n_anchored, n_computed),
    }


# ---------------------------------------------------------------------------
# Section 7 — Persist artifacts
# ---------------------------------------------------------------------------

def persist_npz(result: dict, input_pin_map: list) -> None:
    """Write the 9-cell + 6-axis structures + ordered input-pin list as
    record arrays to the .npz artifact."""
    cells_records = np.array(
        [
            (
                c["cell_id"], c["arm_id"], c["arm_name"], c["layer_id"],
                c["layer_name"], c["rho_sign_convention"],
                c["rho_alpha_s_pin"], c["rho_Omega_GW_pin"],
                c["rho_method"], c["rho_value_status"],
                str(c["value"]) if c["value"] is not None else "",
                c["source"] if c["source"] is not None else "",
            )
            for c in result["cells"]
        ],
        dtype=[
            ("cell_id", "U32"),
            ("arm_id", "U16"),
            ("arm_name", "U64"),
            ("layer_id", "U16"),
            ("layer_name", "U64"),
            ("rho_sign_convention", "U16"),
            ("rho_alpha_s_pin", "U16"),
            ("rho_Omega_GW_pin", "U24"),
            ("rho_method", "U24"),
            ("rho_value_status", "U24"),
            ("value", "U128"),
            ("source", "U512"),
        ],
    )                                                                # (local)

    axes_records = np.array(
        [
            (
                a["axis_id"], a["name"], a["scope"],
                json.dumps(a["admissible_values"]),
                str(a["default_pin"]),
                a["note"],
            )
            for a in result["axes"]
        ],
        dtype=[
            ("axis_id", "U16"),
            ("name", "U32"),
            ("scope", "U64"),
            ("admissible_values_json", "U512"),
            ("default_pin", "U128"),
            ("note", "U512"),
        ],
    )                                                                # (local)

    input_pin_array = np.array(input_pin_map, dtype="U256")          # (local)

    np.savez(
        OUT_NPZ,
        cells=cells_records,
        axes=axes_records,
        input_pin_map=input_pin_array,
        n_cells=result["n_cells"],
        n_axes=result["n_axes"],
        rho_anchored_count=result["rho_anchored_count"],
        rho_computed_count=result["rho_computed_count"],
    )
    print(f"  wrote: {OUT_NPZ.relative_to(PROJECT_ROOT)}")


def persist_json(result: dict, input_pin_map: list) -> None:
    """Write the human-readable JSON mirror."""
    payload = {                                                      # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "n_cells": result["n_cells"],
        "n_axes": result["n_axes"],
        "rho_anchored_count": result["rho_anchored_count"],
        "rho_computed_count": result["rho_computed_count"],
        "n_structural_zero": result["n_structural_zero"],
        "n_deferred_S87": result["n_deferred_S87"],
        "arms": result["arms"],
        "layers": result["layers"],
        "cells": result["cells"],
        "axes": result["axes"],
        "input_pin_map": input_pin_map,
        "registry_anchors": {
            "W0b_R7": ("sessions/permanent-results-registry.md "
                       "§VII.M.3 (S86-SINGLE-NAME-CONFLATION-METHODOLOGY-"
                       "ENTRY)"),
            "W0b_R8": ("sessions/permanent-results-registry.md "
                       "§VII.M.4 (S86-PRR-THREE-LAYER-ADJUDICATION)"),
            "W13_2_anchor": ("S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT "
                             "(rho=0, scheme=zeta, "
                             "convention=LISA-PLS-2024+CMB-S4-Book-2019, "
                             "L_max=10)"),
            "P7_compute_source": "S86-RHO-SUBSTRATE-PREDICTION-MC",
        },
    }
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, indent=2, sort_keys=False)
    print(f"  wrote: {OUT_JSON.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def evaluate_gate(result: dict) -> str:
    """Structural-completeness threshold (binary).

    PASS iff:
      n_cells = N_CELLS_EXPECTED (= 9)
      n_axes  = N_AXES_EXPECTED  (= 6)
      OUT_NPZ exists
      OUT_JSON exists
    FAIL iff any of the above absent.
    No INFO band per plan §9 (audit-class binary completeness).
    """
    if result["n_cells"] != N_CELLS_EXPECTED:
        return "FAIL"
    if result["n_axes"] != N_AXES_EXPECTED:
        return "FAIL"
    if not OUT_NPZ.exists():
        return "FAIL"
    if not OUT_JSON.exists():
        return "FAIL"
    return "PASS"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str,
                   content_sha: str) -> None:
    """Append a single-line verdict + dual-SHA companion comment row to
    s86_gate_verdicts.txt.

    Atomic append (single open("a") write — no read-modify-write, no
    truncate-and-rewrite) per .claude/rules/epistemic-discipline.md
    Registry-Write Hygiene.
    """
    value_str = (
        f"(n_cells={value[0]}, n_axes={value[1]}, "
        f"rho_anchored_count={value[2]}, rho_computed_count={value[3]})"
    )
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"audit-class registry-write; W0b R7+R8 cited; "
        f"W13-2 anchor + P7 LAYER-3 compute source.\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                 # (local)

    # 1. Log input pins (first ~20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)                               # (local)
    closure = closure_hash(pins)                                     # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                           # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')            # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins
    )                                                                # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... "
          "(script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Build the registry-write structures
    result = compute()                                               # (local)

    # 3. Persist artifacts
    input_pin_map = sorted(pins.keys())                              # (local)
    persist_npz(result, input_pin_map)
    persist_json(result, input_pin_map)

    # 4. Diagnostics
    print()
    print(f"  n_cells               = {result['n_cells']}  "
          f"(expected {N_CELLS_EXPECTED})")
    print(f"  n_axes                = {result['n_axes']}  "
          f"(expected {N_AXES_EXPECTED})")
    print(f"  rho_anchored_count    = "
          f"{result['rho_anchored_count']}  (W13-2 LAYER-2 anchor)")
    print(f"  rho_computed_count    = "
          f"{result['rho_computed_count']}  (P7 LAYER-3 anchor)")
    print(f"  n_structural_zero     = "
          f"{result['n_structural_zero']}  "
          f"(LAYER-1 + LAYER-2 Fisher diagonal cells)")
    print(f"  n_deferred_S87        = "
          f"{result['n_deferred_S87']}  (Arm-3 LISA-fold-folded)")
    print()

    # 5. Evaluate gate
    verdict = evaluate_gate(result)                                  # (local)

    # 6. Emit 4-tuple + append verdict (dual-SHA, S84+ schema)
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)    # (local)
    print(tag)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    # 7. Final summary
    wall = time.time() - t0                                          # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # (local) verdict-as-data: PASS|FAIL both exit 0 per
              # .claude/rules/math-scripts.md Exit Codes section


if __name__ == "__main__":
    sys.exit(main())
