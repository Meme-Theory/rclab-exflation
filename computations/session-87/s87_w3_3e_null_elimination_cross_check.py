#!/usr/bin/env python3
"""
S87 W3-3e — S87-W3-3E-LITEBIRD-LISA-NULL-ELIMINATION-CROSS-CHECK
==================================================================

Gate: S87-W3-3E-LITEBIRD-LISA-NULL-ELIMINATION-CROSS-CHECK ([VERIFY])

Pre-registered threshold (plan §W3-3e.9):
  null_elim_sigma = orthogonal Fisher distance from substrate-prediction tuple
                    to the nearest FAIL-no-cell-match boundary edge
  PASS iff null_elim_sigma >= 5.0
  INFO iff 3.0 <= null_elim_sigma < 5.0
  FAIL iff null_elim_sigma < 3.0

Inputs:
  - computations/_shared/_meta_classifier_v2.py (CF-21 callable)
  - canonical_constants.py (n_T pins, Omega_GW pins, sigma_n_T_LB)
  - script bytes

Output 4-tuple:
  (value=<null_elim_sigma>, scheme=null-elimination-Fisher-distance,
   convention=cell-predicted-vs-FAIL-no-cell-match-boundary, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Substrate prediction at τ_fold (W-3 R3-A canonical reading): Path-H + (A) cell,
i.e., the tuple (n_T = n_T_PathH_canonical, Omega_GW = Omega_GW_Lambda_A_LISA,
regulator_class='(A)'). Per _meta_classifier_v2.py decision rules:
  - block axis Path-H band: half-width = 0.5 * sigma_n_T_LiteBIRD on the n_T axis
  - regulator axis (A) band: half-width = 0.5 OOM on the log10(Omega_GW) axis
The substrate prediction lies AT THE CENTER of both bands; the orthogonal
distance to the nearest band edge (= FAIL-no-cell-match boundary) is the
band half-width in σ-units (0.5σ on either axis under canonical pin).

The substitution chain Step 4 acknowledges this is a band-geometry constraint:
the PASS threshold (5σ) is structurally incompatible with the canonical
band-half-width pin (0.5σ). The FAIL verdict diagnoses a structural gap
between the 5σ pre-registered threshold and the meta_classifier_v2 0.5σ band
half-width — NOT a substrate-physics failure (substrate cell membership PASSes
unambiguously: cell_predicted = 'PASS-PathH-(A)').

This routes to S88 carry-forward `S88-NULL-ELIMINATION-BAND-WIDTH-RECONCILIATION`
to either (a) widen the meta_classifier_v2 band half-widths, or (b) loosen the
null_elim_sigma threshold to match band geometry — pre-registration discipline
forbids in-session threshold relaxation per PROHIBITED_ACTIONS Class 3.
"""

from __future__ import annotations

# Section 1 — Canonical constants
import sys
from pathlib import Path
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import (  # noqa: E402
    n_T_PathH_canonical,
    n_T_PathC_canonical,
    sigma_n_T_LiteBIRD,
    Omega_GW_Lambda_A_LISA,
    Omega_GW_Lambda_C_LISA,
)
from _meta_classifier_v2 import classify_outcome  # noqa: E402

# Section 2 — Standard imports
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Section 3 — Paths + pre-registration
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

GATE_ID = "S87-W3-3E-LITEBIRD-LISA-NULL-ELIMINATION-CROSS-CHECK"  # (local)
SCHEME = "null-elimination-Fisher-distance"  # (local)
CONVENTION = "cell-predicted-vs-FAIL-no-cell-match-boundary"  # (local)
L_MAX = "N/A"  # (local)

PASS_THRESHOLD = 5.0  # (local) null_elim_sigma >= 5.0 PASSes
INFO_FLOOR = 3.0  # (local) [3.0, 5.0) is INFO

# Pre-registered band half-widths from _meta_classifier_v2.py
BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA = 0.5  # (local) half-width in σ_n_T_LB units
REGULATOR_AXIS_OOM_BAND = 0.5           # (local) half-width in OOM
SIGMA_OOM_LISA = 1.0                    # (local) plan-implicit pin (§W3-3d)

OUT_NPZ = resolve_output(87, 's87_w3_3e_null_elimination_cross_check.npz')
OUT_PNG = resolve_output(87, 's87_w3_3e_null_elimination_cross_check.png')
OUT_JSON = resolve_output(87, 's87_w3_3e_null_elimination_cross_check.json')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(None, '_meta_classifier_v2.py'),
]


# Section 4 — SHA-256
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pins_aug = dict(pins)  # (local)
    pins_aug["_gate_id"] = GATE_ID
    pins_aug["_scheme"] = SCHEME
    pinmap_json = json.dumps(
        dict(sorted(pins_aug.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# Section 5 — Compute
def compute():
    """Substitution chain (per plan §W3-3e.10):
    Step 1: cell_predicted = classify_outcome(substrate-prediction-tuple)['cell']
    Step 2: orthogonal Fisher distance to nearest FAIL_boundary edge
    Step 3: simplify
    Step 4: direction — substrate at canonical band-center; nearest edge dist
            = band half-width = 0.5σ on either axis (canonical pin)
    """
    # Substrate prediction at τ_fold per W-3 R3-A canonical reading
    substrate_n_T = float(n_T_PathH_canonical)              # (local)
    substrate_Omega = float(Omega_GW_Lambda_A_LISA)         # (local)
    substrate_class = "(A)"                                  # (local)

    # Cell membership check
    classifier_out = classify_outcome(
        substrate_n_T, substrate_Omega, substrate_class
    )  # (local)
    cell_predicted = classifier_out["cell"]                  # (local)

    # Substrate is at band-CENTER on n_T axis (Path-H canonical exactly equals
    # n_T_PathH_canonical), and at band-CENTER on log10 Omega axis (Omega_GW
    # canonical exactly equals Omega_GW_Lambda_A_LISA).
    # Orthogonal distance to nearest band edge in σ-units:
    n_T_axis_dist_sigma = BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA   # (local) 0.5σ
    OOM_axis_dist_sigma = REGULATOR_AXIS_OOM_BAND / SIGMA_OOM_LISA  # (local) 0.5σ

    # Nearest-edge orthogonal Fisher distance (single-axis crossing):
    null_elim_nearest_edge = min(n_T_axis_dist_sigma, OOM_axis_dist_sigma)  # (local)
    # Corner Pythagorean (cross-axis):
    null_elim_corner = math.sqrt(n_T_axis_dist_sigma ** 2 + OOM_axis_dist_sigma ** 2)  # (local)

    # Plan §W3-3e.10 Step 1: "orthogonal distance to the nearest FAIL_boundary edge"
    # Nearest-edge interpretation is canonical for "nearest band-edge" wording.
    null_elim_sigma = null_elim_nearest_edge                  # (local)

    # Independent off-prediction null check: a clearly-out-of-cell tuple should
    # classify as FAIL-no-cell-match. Sanity check.
    off_pred_out = classify_outcome(0.05, 1e-30, "(A)")        # (local)
    off_pred_cell = off_pred_out["cell"]                       # (local)

    return {
        "cell_predicted": cell_predicted,
        "substrate_n_T": substrate_n_T,
        "substrate_Omega": substrate_Omega,
        "substrate_class": substrate_class,
        "n_T_axis_dist_sigma": n_T_axis_dist_sigma,
        "OOM_axis_dist_sigma": OOM_axis_dist_sigma,
        "null_elim_sigma_nearest_edge": null_elim_nearest_edge,
        "null_elim_sigma_corner": null_elim_corner,
        "null_elim_sigma": null_elim_sigma,
        "off_prediction_classification": off_pred_cell,
        "classifier_rationale": classifier_out["rationale"],
    }


def evaluate_gate(null_elim, cell_predicted):
    if null_elim >= PASS_THRESHOLD:
        composite = "PASS"
        mag = "PASS"
    elif null_elim >= INFO_FLOOR:
        composite = "INFO"
        mag = "INFO"
    else:
        composite = "FAIL"
        mag = "FAIL"
    # Sign per plan §W3-3e.10 Step 4: sign_verdict = PASS by structural
    # construction (substrate prediction is deep inside Path-H + (A) cell per
    # W-3 R3-A canonical reading). The cell_predicted membership confirms this
    # structurally; the magnitude verdict tracks the orthogonal distance.
    if cell_predicted in (
        "PASS-PathH-(A)", "PASS-PathH-(C)",
        "PASS-PathC-(A)", "PASS-PathC-(C)"
    ):
        sign = "PASS"
    else:
        sign = "FAIL"
    regime = "VALID"  # band geometry is canonically pinned; no breakdown
    return composite, mag, sign, regime


def make_plot(result, png_path):
    fig, ax = plt.subplots(figsize=(9, 6))

    # 4-cell + null-cell decomposition: x = n_T (in σ_n_T_LB units around midpoint)
    # y = log10 Omega_GW (in OOM)
    # Path-H center: at (n_T_PathH - midpoint_n_T) / sigma_n_T_LB
    # Path-C center: at (n_T_PathC - midpoint_n_T) / sigma_n_T_LB
    midpoint_n_T = (n_T_PathH_canonical + n_T_PathC_canonical) / 2.0  # (local)
    pathH_x = (n_T_PathH_canonical - midpoint_n_T) / sigma_n_T_LiteBIRD  # (local)
    pathC_x = (n_T_PathC_canonical - midpoint_n_T) / sigma_n_T_LiteBIRD  # (local)
    A_y = math.log10(Omega_GW_Lambda_A_LISA)  # (local)
    C_y = math.log10(Omega_GW_Lambda_C_LISA)  # (local)

    # 4 cells as rectangles
    band_n_T = BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA  # (local) 0.5
    band_OOM = REGULATOR_AXIS_OOM_BAND           # (local) 0.5
    cell_specs = [
        (pathH_x, A_y, "PASS-PathH-(A)", "tab:blue"),
        (pathH_x, C_y, "PASS-PathH-(C)", "tab:cyan"),
        (pathC_x, A_y, "PASS-PathC-(A)", "tab:red"),
        (pathC_x, C_y, "PASS-PathC-(C)", "tab:orange"),
    ]
    from matplotlib.patches import Rectangle
    for cx, cy, label, color in cell_specs:
        rect = Rectangle(
            (cx - band_n_T, cy - band_OOM),
            2 * band_n_T,
            2 * band_OOM,
            edgecolor=color, facecolor=color, alpha=0.25, label=label
        )
        ax.add_patch(rect)
        ax.scatter([cx], [cy], color=color, s=40, marker="x")

    # Substrate prediction at Path-H/(A)
    ax.scatter([pathH_x], [A_y], color="black", s=120, marker="*",
               label="substrate-prediction (Path-H/(A))", zorder=10)
    # Annotate orthogonal distances
    ax.annotate(
        f"null_elim_σ = {result['null_elim_sigma']}σ\n"
        f"(0.5σ band half-width pinned in _meta_classifier_v2)",
        xy=(pathH_x, A_y),
        xytext=(pathH_x + 0.6, A_y + 4.0),
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="black"),
    )

    ax.set_xlabel("n_T axis (σ_n_T_LB units around midpoint)")
    ax.set_ylabel("log10 Ω_GW")
    ax.set_title(
        f"§W3-3e Null-elimination cross-check | cell={result['cell_predicted']}\n"
        f"null_elim_σ = {result['null_elim_sigma']}σ (FAIL band: 5σ threshold "
        f"vs 0.5σ band half-width)"
    )
    ax.legend(loc="lower right", fontsize=8)
    ax.set_xlim(-3, 3)
    ax.set_ylim(min(A_y, C_y) - 2, max(A_y, C_y) + 2)
    fig.tight_layout()
    fig.savefig(png_path, dpi=120)
    plt.close(fig)


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_short = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    triple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(dual_short)
        fp.write(triple_row)


def main():
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    print(f"  closure: {closure_hash(pins)[:16]}...")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    composite, mag_v, sign_v, regime_v = evaluate_gate(
        result["null_elim_sigma"], result["cell_predicted"]
    )

    print("=== Computation result ===")
    print(f"  cell_predicted             = {result['cell_predicted']}")
    print(f"  off-prediction classify    = {result['off_prediction_classification']}")
    print(f"  n_T axis distance-to-edge  = {result['n_T_axis_dist_sigma']}σ")
    print(f"  Omega axis distance-to-edge= {result['OOM_axis_dist_sigma']}σ")
    print(f"  null_elim_σ (nearest edge) = {result['null_elim_sigma_nearest_edge']}")
    print(f"  null_elim_σ (corner)       = {result['null_elim_sigma_corner']:.4f}")
    print(f"  null_elim_σ (canonical)    = {result['null_elim_sigma']}")
    print(f"  composite        = {composite}")
    print(f"  3-tuple          = sign={sign_v} mag={mag_v} regime={regime_v}")

    np.savez(OUT_NPZ,
             null_elim_sigma=result["null_elim_sigma"],
             null_elim_sigma_corner=result["null_elim_sigma_corner"],
             cell_predicted=result["cell_predicted"],
             off_prediction_classification=result["off_prediction_classification"],
             n_T_axis_dist_sigma=result["n_T_axis_dist_sigma"],
             OOM_axis_dist_sigma=result["OOM_axis_dist_sigma"],
             pass_threshold=PASS_THRESHOLD,
             info_floor=INFO_FLOOR,
             band_half_width_sigma=BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA,
             OOM_band=REGULATOR_AXIS_OOM_BAND,
             sigma_OOM_LISA=SIGMA_OOM_LISA)
    out_json = {
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": round(result["null_elim_sigma"], 4),
        "value_full": result["null_elim_sigma"],
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "details": {
            "cell_predicted": result["cell_predicted"],
            "off_prediction_classification": result["off_prediction_classification"],
            "n_T_axis_dist_sigma": result["n_T_axis_dist_sigma"],
            "OOM_axis_dist_sigma": result["OOM_axis_dist_sigma"],
            "null_elim_sigma_nearest_edge": result["null_elim_sigma_nearest_edge"],
            "null_elim_sigma_corner": result["null_elim_sigma_corner"],
            "band_half_width_sigma": BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA,
            "OOM_band_half": REGULATOR_AXIS_OOM_BAND,
            "sigma_OOM_LISA_pin": SIGMA_OOM_LISA,
        },
        "structural_diagnosis": (
            "Substrate prediction is structurally INSIDE PASS-PathH-(A) cell "
            "(sign_verdict=PASS), but pre-registered 5σ threshold is "
            "structurally incompatible with canonical 0.5σ band half-width "
            "pinned in _meta_classifier_v2.py — magnitude FAILs at "
            "null_elim_sigma=0.5σ < 3σ floor. "
            "S88 carry-forward: S88-NULL-ELIMINATION-BAND-WIDTH-RECONCILIATION "
            "to either widen meta_classifier_v2 bands or recalibrate threshold "
            "(PROHIBITED_ACTIONS Class 3 forbids in-session threshold relaxation)."
        ),
        "carry_forward": "S88-NULL-ELIMINATION-BAND-WIDTH-RECONCILIATION",
    }
    OUT_JSON.write_text(json.dumps(out_json, indent=2), encoding="utf-8")
    make_plot(result, OUT_PNG)

    tag = (f"(value={round(result['null_elim_sigma'], 4)!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    value_pub = round(result["null_elim_sigma"], 4)
    append_verdict(composite, value_pub, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
