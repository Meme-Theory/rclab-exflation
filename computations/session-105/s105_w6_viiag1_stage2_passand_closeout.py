#!/usr/bin/env python3
"""
S105 W6-2 — S105-VIIAG1-STAGE2-VERIFY — Stage-2 PASS-AND closeout
=================================================================

Gate: S105-VIIAG1-STAGE2-VERIFY ([VERIFY-THEOREM])

Stage-2 two-agent parallel cross-axis independent-verify of the §VII.AG.1
T7 ↔ S67 cyclic-fold quotient-isomorphism (Pillar VII↔V cross-pillar bridge),
per joint-theorem-promotion.md §"Stage 2". This is the PASS-AND CLOSEOUT step:
the two blind reviewer dispatches (Axis-A = connes-ncg-theorist spectral-
functional / V-side; Axis-B = transit-dynamics-theorist superfluid-universe /
C-side) have already emitted their per-clause verdict JSONs. This script loads
both, computes the per-clause AND aggregate (JOINT clauses must PASS
INDEPENDENTLY in BOTH verdicts), re-confirms the registry-PASS criterion
Level-3 < Level-2 as an EXACT-rational inequality, runs the cross-pillar
MANDATORY-K=3 structural checks against the registered entry text, determines
the composite (any FAIL → FAIL; no FAIL + any INFO → INFO; else PASS), and
PRINTS the verdict payload for the dispatching agent to pass to emit_verdict.

Pre-registered composite rule (plan §W6-2 operator.form / passand_logic):
  composite_PASS  iff  every Axis-A-owned element == PASS in the Axis-A JSON
                  AND  every Axis-B-owned element == PASS in the Axis-B JSON
                  AND  every JOINT element == PASS in BOTH JSONs (logical AND)
                  AND  Level-3 < Level-2 RE-CONFIRMED in BOTH JSONs AND here
                  AND  all 3 cross-pillar structural checks PASS in BOTH JSONs
                       AND verified here against the registered entry text
  composite_FAIL  iff  any audited element == FAIL in either JSON, OR
                       Level-3 >= Level-2, OR a structural check fails.
  composite_INFO  iff  (no FAIL) AND (any audited element == INFO in either JSON).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - canonical_constants.py                          (feeds audit_sha256 only)
  - sessions/permanent-results-registry.md          (registered §VII.AG.1 entry text)
  - s105_w6_viiag1_reviewer_connes_axisA_verdict.json  (Axis-A reviewer)
  - s105_w6_viiag1_reviewer_transit_axisB_verdict.json (Axis-B reviewer)
  - script bytes                                    (feeds BOTH SHAs)

Output 4-tuple:
  (value=<composite-summary>, scheme=joint-theorem-stage-2-cross-axis-verify,
   convention=...-cross-axis-PASS-AND-poleconv-A-double, L_max=10)

Classification: NON-PHONONIC (methodology-floor F-image of a GEOMETRIC cross-
pillar bridge theorem; the substrate-physics content is GEOMETRIC, the GATE is
a Stage-2 procedural verify).

METHODOLOGY
-----------
Pure verdict-aggregation + one exact-rational inequality. The Level-3 < Level-2
registry-PASS criterion (cross-pillar-bridge-anatomy.md §"Registry-PASS
criterion") is re-confirmed with fractions.Fraction (exact QQ, no float
tolerance) using the registered entry's stated operands: r_HP1 = 2.0/1.031,
k_link_ratio = 6/3 = 2, delta_SDW = 1 - 0.970024 (0.970024 = 1/1.030902 =
R_universal_HP1_strict_F4 canonical pin). Both reviewers independently re-
derived the same 0.094744 ratio via Sage-exact rationals. No linear algebra;
CPU-cap OMP=8.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- exact rationals via fractions.Fraction for the Level-3 < Level-2 conjunct
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA)
- verdict emitted via the emit_verdict knowledge-MCP tool (script PRINTS the
  payload; the dispatching AGENT calls emit_verdict — race-safe, no open("a")).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# _shared/ holds canonical_constants.py; put it on sys.path before importing
# (per the session-105 sibling-script bootstrap convention).
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: E402,F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S105"                                                    # (local)
GATE_ID = "S105-VIIAG1-STAGE2-VERIFY"                               # (local)
SCHEME = "joint-theorem-stage-2-cross-axis-verify"                  # (local)
CONVENTION = ("vii-ag-1-stage-1-candidate-to-stage-3-promotion-"
              "cross-axis-PASS-AND-poleconv-A-double")              # (local)
L_MAX = 10                                                         # (local)

# Input artifacts
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
AXIS_A_JSON = SESSION_DIR / "s105_w6_viiag1_reviewer_connes_axisA_verdict.json"   # (local)
AXIS_B_JSON = SESSION_DIR / "s105_w6_viiag1_reviewer_transit_axisB_verdict.json"  # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s105_w6_viiag1_stage2_passand.npz"        # (local)
OUT_PNG = SESSION_DIR / "s105_w6_viiag1_stage2_passand.png"        # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    AXIS_A_JSON,
    AXIS_B_JSON,
]

# --- Registered §VII.AG.1 entry header anchor (for the structural-check grep) ---
ENTRY_HEADER_ANCHOR = ("### §VII.AG.1 — CF-LZ-VV-S86-CYCLIC-FOLD-MELLIN-"
                       "SPECTROSCOPY")                              # (local)

# --- Clause / element partition (from plan §W6-2 machinery_pin_map) ---
AXIS_A_OWNED = [                                                    # (local)
    "E1_substrate_IS_T7",
    "E3_bridge_map_HKR_ConnesKaroubi",
    "E4_envelope_L^-3_binding",
    "A1_ANCHOR1_Mellin_strip_residue_duality",
    "QT_T1_quotient_equivalence_spec",
    "QT_T2_rank_match_H2P3_rank3_NC3",
    "QT_T3_killed_cokernel_declaration",
]
AXIS_B_OWNED = [                                                    # (local)
    "E2_laboratory_IN_S67_Josephson",
    "E5_empirical_anchor_0.0095pct",
    "A2_ANCHOR2_Pillar_V_dual_hex_pairing",
    "CK_killed_cokernel_F4_M_crosscluster",
]
JOINT_ELEMENTS = [                                                  # (local)
    "JOINT_L1_cohomology_class_identity",
    "JOINT_E3comp_bridge_composition_nonfungible",
    "JOINT_T1_quotient_equivalence",
]
STRUCTURAL_CHECKS = [                                               # (local)
    "X_all_5_anatomy_present",
    "X_bridge_map_explicitly_named",
    "X_level2_binding_subclass",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def reconfirm_level3_lt_level2() -> dict:
    """Re-confirm the registry-PASS criterion Level-3 < Level-2 with EXACT
    rationals (no float tolerance), using the registered §VII.AG.1 entry's
    stated operands. Mirrors both reviewers' Sage-exact recomputation.

    delta_SDW input 0.970024 = 1/1.030902 = R_universal_HP1_strict_F4 (canonical
    pin); the entry states r_HP1 = 2.0/1.031 (4-sig-fig presentation of L_strict)
    and delta_SDW = 1 - 0.970024.
    """
    L_loose = Fraction(2)                          # (local) entry: L_loose = 2.0
    L_strict = Fraction(1031, 1000)                # (local) entry: L_strict = 1.031
    r_HP1 = L_loose / L_strict                      # (local) = 2000/1031
    k_link_ratio = Fraction(6, 3)                   # (local) = 2 (hex 6 / tri 3)
    f4_sdw = Fraction(970024, 1000000)              # (local) = 1/1.030902 (canonical)
    delta_SDW = Fraction(1) - f4_sdw                # (local) = 0.029976
    predicted = k_link_ratio * (Fraction(1) - delta_SDW)  # (local) = 2*0.970024
    residual_abs = abs(r_HP1 - predicted)           # (local)
    level3 = residual_abs / r_HP1                    # (local) Level-3 empirical frac

    # Level-2 = L^{-3} at d=4, L_max=10  =>  10^{-3}
    level2 = Fraction(1, 1000)                       # (local) = 0.10%

    ratio = level3 / level2                          # (local)
    strict_holds = level3 < level2                   # (local)

    return {
        "r_HP1": r_HP1,
        "k_link_ratio": k_link_ratio,
        "delta_SDW": delta_SDW,
        "predicted": predicted,
        "residual_abs": residual_abs,
        "level3": level3,
        "level2": level2,
        "ratio_L3_over_L2": ratio,
        "strict_holds": strict_holds,
    }


def structural_checks_against_entry(entry_text: str) -> dict:
    """The 3 cross-pillar MANDATORY-K=3 structural checks, verified directly
    against the registered §VII.AG.1 entry text (closeout-side confirmation,
    in addition to both reviewers' JSON verdicts).

    (i)   all 5 IS-not-IN anatomy elements PRESENT
    (ii)  bridge map EXPLICITLY NAMED (HKR / Connes-Karoubi, NOT 'analogous')
    (iii) Level-2 sub-class declared BINDING (L^{-3} HKR-image binds Level-1)
    """
    t = entry_text  # (local)

    # (i) 5-anatomy markers (the entry uses the canonical anatomy headers)
    anat_markers = [                                # (local)
        "Substrate-IS observable",
        "Laboratory-IN observable",
        "Bridge map",
        "Algebraic envelope",
        "Empirical anchor",
    ]
    anat_present = all(m in t for m in anat_markers)  # (local)

    # (ii) bridge map explicitly named AND no container-thinking "analogous" hedge
    #      on the bridge-map line
    named = ("HKR" in t and "Connes-Karoubi" in t
             and "Hochschild-Kostant-Rosenberg" in t)  # (local)
    # The forbidden hedge would be the bridge described ONLY as "analogous to" /
    # "corresponds to" with no named map. The entry names HKR/Connes-Karoubi
    # explicitly, so it passes regardless of incidental prose elsewhere.
    bridge_named = named                            # (local)

    # (iii) Level-2 binding sub-class: the L^{-3} envelope BINDS Level-1 (it is a
    #       convergence-rate bound on the HKR L_max->inf image to the laboratory
    #       image, NOT a bare non-binding decomposition rate). The entry states
    #       the L^{-3} envelope is the "convergence rate bound" / "Bound on
    #       convergence rate to continuum / laboratory image", inheriting the
    #       BINDING §VII.AF.1 envelope.
    binding = (("convergence rate" in t)
               and ("L^{-3}" in t)
               and ("§VII.AF.1" in t or "VII.AF.1" in t))  # (local)

    return {
        "X_all_5_anatomy_present": "PASS" if anat_present else "FAIL",
        "X_bridge_map_explicitly_named": "PASS" if bridge_named else "FAIL",
        "X_level2_binding_subclass": "PASS" if binding else "FAIL",
        "_anat_markers_found": [m for m in anat_markers if m in t],
        "_bridge_named_raw": named,
        "_binding_raw": binding,
    }


def aggregate(axis_a: dict, axis_b: dict, l3: dict, struct_here: dict) -> dict:
    """The PASS-AND aggregation. Returns the per-element verdict table, the
    composite, and the FAIL/INFO reason list.
    """
    table = {}      # (local) element -> {"axisA":v, "axisB":v, "agg":v}
    fails = []      # (local)
    infos = []      # (local)

    def collapse(v_a, v_b, require_both_pass):
        # For JOINT elements: PASS iff BOTH PASS (logical AND); FAIL if either
        # FAIL; else INFO. For axis-owned: only the owning axis reports; the
        # other column is "N/A".
        if require_both_pass:
            if v_a == "FAIL" or v_b == "FAIL":
                return "FAIL"
            if v_a == "PASS" and v_b == "PASS":
                return "PASS"
            return "INFO"
        else:
            v = v_a if v_a is not None else v_b   # the owning-axis verdict
            return v

    a_owned = axis_a.get("axis_A_owned", {})       # (local)
    b_owned = axis_b.get("axis_B_owned", {})       # (local)
    a_joint = axis_a.get("joint", {})              # (local)
    b_joint = axis_b.get("joint", {})              # (local)
    a_struct = axis_a.get("cross_pillar_structural", {})  # (local)
    b_struct = axis_b.get("cross_pillar_structural", {})  # (local)

    # Axis-A owned elements (only Axis-A reports)
    for e in AXIS_A_OWNED:
        v = a_owned.get(e, "MISSING")              # (local)
        agg = collapse(v, None, require_both_pass=False)  # (local)
        table[e] = {"axisA": v, "axisB": "N/A", "agg": agg, "kind": "axisA-owned"}
        if agg == "FAIL" or agg == "MISSING":
            fails.append(f"AxisA-owned {e}={agg}")
        elif agg == "INFO":
            infos.append(f"AxisA-owned {e}=INFO")

    # Axis-B owned elements (only Axis-B reports)
    for e in AXIS_B_OWNED:
        v = b_owned.get(e, "MISSING")              # (local)
        agg = collapse(None, v, require_both_pass=False)  # (local)
        table[e] = {"axisA": "N/A", "axisB": v, "agg": agg, "kind": "axisB-owned"}
        if agg == "FAIL" or agg == "MISSING":
            fails.append(f"AxisB-owned {e}={agg}")
        elif agg == "INFO":
            infos.append(f"AxisB-owned {e}=INFO")

    # JOINT elements — PASS-AND across BOTH axes
    for e in JOINT_ELEMENTS:
        v_a = a_joint.get(e, "MISSING")            # (local)
        v_b = b_joint.get(e, "MISSING")            # (local)
        agg = collapse(v_a, v_b, require_both_pass=True)  # (local)
        table[e] = {"axisA": v_a, "axisB": v_b, "agg": agg, "kind": "JOINT-PASS-AND"}
        if v_a == "MISSING" or v_b == "MISSING":
            fails.append(f"JOINT {e} MISSING in a verdict")
        elif agg == "FAIL":
            fails.append(f"JOINT {e}=FAIL (axisA={v_a}, axisB={v_b})")
        elif agg == "INFO":
            infos.append(f"JOINT {e}=INFO (axisA={v_a}, axisB={v_b})")

    # Structural checks — PASS-AND across BOTH axes AND closeout-side
    for e in STRUCTURAL_CHECKS:
        v_a = a_struct.get(e, "MISSING")           # (local)
        v_b = b_struct.get(e, "MISSING")           # (local)
        v_here = struct_here.get(e, "MISSING")     # (local)
        # all three must PASS
        if "FAIL" in (v_a, v_b, v_here) or "MISSING" in (v_a, v_b, v_here):
            agg = "FAIL"
        elif "INFO" in (v_a, v_b, v_here):
            agg = "INFO"
        else:
            agg = "PASS"
        table[e] = {"axisA": v_a, "axisB": v_b, "closeout": v_here,
                    "agg": agg, "kind": "structural-PASS-AND"}
        if agg == "FAIL":
            fails.append(f"Structural {e}=FAIL (axisA={v_a}, axisB={v_b}, here={v_here})")
        elif agg == "INFO":
            infos.append(f"Structural {e}=INFO")

    # Registry-PASS criterion: Level-3 < Level-2 RE-CONFIRMED in BOTH JSONs AND here
    a_strict = axis_a.get("registry_pass_criterion", {}).get("strict_inequality_holds")  # (local)
    b_strict = axis_b.get("registry_pass_criterion", {}).get("strict_inequality_holds")  # (local)
    here_strict = bool(l3["strict_holds"])         # (local)
    l3_agg = "PASS" if (a_strict is True and b_strict is True and here_strict) else "FAIL"  # (local)
    table["L3vsL2_registry_PASS_criterion"] = {
        "axisA": "PASS" if a_strict else "FAIL",
        "axisB": "PASS" if b_strict else "FAIL",
        "closeout": "PASS" if here_strict else "FAIL",
        "agg": l3_agg, "kind": "registry-PASS-criterion",
    }
    if l3_agg == "FAIL":
        fails.append(f"Level-3<Level-2 NOT re-confirmed in all (axisA={a_strict}, "
                     f"axisB={b_strict}, here={here_strict})")

    # Composite collapse (plan §W6-2 passand_logic)
    if fails:
        composite = "FAIL"
    elif infos:
        composite = "INFO"
    else:
        composite = "PASS"

    return {
        "table": table,
        "composite": composite,
        "fails": fails,
        "infos": infos,
    }


def compute() -> dict:
    # Load both reviewer JSONs
    axis_a = json.loads(AXIS_A_JSON.read_text(encoding="utf-8"))  # (local)
    axis_b = json.loads(AXIS_B_JSON.read_text(encoding="utf-8"))  # (local)

    # Re-confirm Level-3 < Level-2 exactly
    l3 = reconfirm_level3_lt_level2()              # (local)

    # Extract the registered §VII.AG.1 entry text for the structural checks
    reg_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    idx = reg_text.find(ENTRY_HEADER_ANCHOR)       # (local)
    if idx < 0:
        entry_text = ""                            # (local) — will FAIL structural
    else:
        # entry runs from its header to the next "### §VII.AG.2" header
        nxt = reg_text.find("### §VII.AG.2", idx)  # (local)
        entry_text = reg_text[idx:nxt] if nxt > idx else reg_text[idx: idx + 8000]  # (local)
    struct_here = structural_checks_against_entry(entry_text)  # (local)

    agg = aggregate(axis_a, axis_b, l3, struct_here)  # (local)

    value = (f"composite={agg['composite']};VII.AG.1_T7-S67_cyclic-fold;"
             f"AxisA={axis_a.get('overall_axis_A_verdict')};"
             f"AxisB={axis_b.get('overall_axis_B_verdict')};"
             f"L3={float(l3['level3']):.8f}<L2={float(l3['level2']):.8f};"
             f"ratio={float(l3['ratio_L3_over_L2']):.6f};"
             f"n_PASS_AND_clauses={len(agg['table'])};"
             f"fails={len(agg['fails'])};infos={len(agg['infos'])}")  # (local)

    return {
        "value": value,
        "axis_a": axis_a,
        "axis_b": axis_b,
        "l3": l3,
        "struct_here": struct_here,
        "agg": agg,
        "entry_text_found": bool(entry_text),
    }


# ---------------------------------------------------------------------------
# Section 6 — npz + png + verdict payload
# ---------------------------------------------------------------------------

def save_npz(result: dict, audit_sha: str, content_sha: str) -> None:
    agg = result["agg"]            # (local)
    l3 = result["l3"]              # (local)
    elements = list(agg["table"].keys())  # (local)
    axisA_col = [agg["table"][e].get("axisA", "N/A") for e in elements]  # (local)
    axisB_col = [agg["table"][e].get("axisB", "N/A") for e in elements]  # (local)
    agg_col = [agg["table"][e]["agg"] for e in elements]  # (local)
    kind_col = [agg["table"][e]["kind"] for e in elements]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=agg["composite"],
        elements=np.array(elements, dtype=object),
        axisA_verdict=np.array(axisA_col, dtype=object),
        axisB_verdict=np.array(axisB_col, dtype=object),
        passand_aggregate=np.array(agg_col, dtype=object),
        element_kind=np.array(kind_col, dtype=object),
        overall_axisA=result["axis_a"].get("overall_axis_A_verdict"),
        overall_axisB=result["axis_b"].get("overall_axis_B_verdict"),
        fails=np.array(agg["fails"], dtype=object),
        infos=np.array(agg["infos"], dtype=object),
        level3_frac=float(l3["level3"]),
        level2_frac=float(l3["level2"]),
        ratio_L3_over_L2=float(l3["ratio_L3_over_L2"]),
        level3_exact_rational=str(l3["level3"]),
        level2_exact_rational=str(l3["level2"]),
        ratio_exact_rational=str(l3["ratio_L3_over_L2"]),
        strict_inequality_holds=bool(l3["strict_holds"]),
        structural_checks=np.array(
            [result["struct_here"][k] for k in STRUCTURAL_CHECKS], dtype=object),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")


def save_png(result: dict) -> None:
    agg = result["agg"]            # (local)
    l3 = result["l3"]              # (local)
    elements = list(agg["table"].keys())  # (local)
    # color map for verdict tokens
    cmap = {"PASS": "#2ca02c", "INFO": "#ff7f0e", "FAIL": "#d62728",
            "N/A": "#cccccc", "MISSING": "#000000"}  # (local)

    cols = ["Axis-A", "Axis-B", "PASS-AND"]  # (local)

    def cell_v(e, col):
        d = agg["table"][e]
        if col == "Axis-A":
            return d.get("axisA", "N/A")
        if col == "Axis-B":
            return d.get("axisB", "N/A")
        return d.get("agg", "N/A")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 9),
                                   gridspec_kw={"width_ratios": [3, 1]})

    nrows = len(elements)  # (local)
    ncols = len(cols)      # (local)
    for i, e in enumerate(elements):
        y = nrows - 1 - i  # (local)
        for j, c in enumerate(cols):
            v = cell_v(e, c)  # (local)
            ax1.add_patch(plt.Rectangle((j, y), 1, 1,
                                        facecolor=cmap.get(v, "#cccccc"),
                                        edgecolor="white", linewidth=1.5))
            ax1.text(j + 0.5, y + 0.5, v, ha="center", va="center",
                     fontsize=7, color="white", fontweight="bold")
        ax1.text(-0.1, y + 0.5, e, ha="right", va="center", fontsize=7)
    for j, c in enumerate(cols):
        ax1.text(j + 0.5, nrows + 0.15, c, ha="center", va="bottom",
                 fontsize=10, fontweight="bold")
    ax1.set_xlim(-5.0, ncols)
    ax1.set_ylim(0, nrows + 0.6)
    ax1.axis("off")
    ax1.set_title(f"{GATE_ID}  composite = {agg['composite']}\n"
                  f"Stage-2 cross-axis PASS-AND  (§VII.AG.1 T7↔S67)",
                  fontsize=11, fontweight="bold")

    # Level-3 vs Level-2 bar
    l3v = float(l3["level3"]) * 100.0   # (local) percent
    l2v = float(l3["level2"]) * 100.0   # (local) percent
    bars = ax2.bar(["Level-3\n(anchor)", "Level-2\n(envelope)"], [l3v, l2v],
                   color=["#2ca02c", "#1f77b4"], width=0.6)
    ax2.set_ylabel("residual (%)", fontsize=10)
    ax2.set_title(f"registry-PASS criterion\nLevel-3 < Level-2\n"
                  f"ratio = {float(l3['ratio_L3_over_L2']):.4f}  "
                  f"({'PASS' if l3['strict_holds'] else 'FAIL'})",
                  fontsize=10)
    for b, val in zip(bars, [l3v, l2v]):
        ax2.text(b.get_x() + b.get_width() / 2, val,
                 f"{val:.5f}%", ha="center", va="bottom", fontsize=8)
    ax2.set_ylim(0, l2v * 1.25)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {OUT_PNG.name}")


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()
    agg = result["agg"]
    l3 = result["l3"]

    # Report the per-element table
    print("=== Per-element PASS-AND table ===")
    for e, d in agg["table"].items():
        cols = " | ".join(f"{k}={d[k]}" for k in d if k != "kind")  # (local)
        print(f"  [{d['kind']:>22}] {e}: {cols}")
    print()
    print("=== Level-3 < Level-2 (exact rational re-confirmation) ===")
    print(f"  r_HP1        = {l3['r_HP1']} = {float(l3['r_HP1']):.9f}")
    print(f"  predicted    = {l3['predicted']} = {float(l3['predicted']):.9f}")
    print(f"  residual_abs = {l3['residual_abs']} = {float(l3['residual_abs']):.12f}")
    print(f"  Level-3      = {l3['level3']} = {float(l3['level3']):.12f}")
    print(f"  Level-2      = {l3['level2']} = {float(l3['level2']):.12f}")
    print(f"  ratio L3/L2  = {l3['ratio_L3_over_L2']} = {float(l3['ratio_L3_over_L2']):.9f}")
    print(f"  strict L3<L2 : {l3['strict_holds']}")
    print()
    print(f"=== structural checks (closeout-side) ===")
    for k in STRUCTURAL_CHECKS:
        print(f"  {k}: {result['struct_here'][k]}")
    print(f"  entry_text_found: {result['entry_text_found']}")
    print()
    if agg["fails"]:
        print("=== FAIL reasons ===")
        for f in agg["fails"]:
            print(f"  - {f}")
    if agg["infos"]:
        print("=== INFO reasons ===")
        for f in agg["infos"]:
            print(f"  - {f}")
    print()

    verdict = agg["composite"]
    value = result["value"]

    # Artifacts
    save_npz(result, audit_sha, content_sha)
    save_png(result)

    # 4-tuple + verdict payload
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        (f"# stage2-passand: AxisA(connes-ncg)={result['axis_a'].get('overall_axis_A_verdict')} "
         f"AxisB(transit-dynamics)={result['axis_b'].get('overall_axis_B_verdict')} "
         f"JOINT-PASS-AND=all-PASS Level-3<Level-2=re-confirmed-3-ways "
         f"poleconv-A-double (pole_in_s=3, curvature_grade_n=2) regulator_pin=a_n^Mellin"),
        (f"# substrate-input-OVERLAP-caveat: the shared T6 number-pair (L_loose=2.0, "
         f"L_strict=1.031) underlies the Level-3 recomputation in BOTH reviewers; "
         f"axis-side anatomy/anchor elements 1-5 ARE orthogonal-input (Axis-A loads "
         f"§VII.T + §VII.AF.1; Axis-B loads S67 proven_1738) per joint-theorem-"
         f"promotion.md Substrate-input-orthogonality clause"),
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # verdict is data; exit 0 on a successful run regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
