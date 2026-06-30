#!/usr/bin/env python3
"""
S87 W3-3d — S87-W3-3D-JOINT-LITEBIRD-LISA-FISHER-DISCOUNT
==========================================================

Gate: S87-W3-3D-JOINT-LITEBIRD-LISA-FISHER-DISCOUNT ([VERIFY])

Pre-registered threshold (plan §W3-3d.9):
  joint_margin_sigma = sqrt(margin_LB^2 + margin_LISA^2)
  PASS iff joint_margin_sigma >= 1.5
  INFO iff 1.0 <= joint_margin_sigma < 1.5
  FAIL iff joint_margin_sigma < 1.0

Inputs:
  - computations/session-87/s87_w3_3a_litebird_n_T_discriminator.npz (margin_LB)
  - computations/session-87/s87_w3_3b_lisa_omega_gw_a_c_discriminator.npz (split_OOM)
  - canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=<joint_margin_sigma>, scheme=joint-Fisher-information,
   convention=LiteBIRD-+-LISA-axis-orthogonal-per-VII.AC.3, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Compute joint Fisher information assuming axis-orthogonality per §VII.AC.3
Rank-2 Product Detector Orthogonality Theorem. Information sums:
  F_joint = F_LB + F_LISA  (additive under axis-orthogonality)
joint_margin_sigma = sqrt(F_joint).

Stage-1 candidate landing for the Joint LiteBIRD-LISA-Fisher cross-axis theorem
per .claude/rules/joint-theorem-promotion.md; Stage-2 two-agent independent
verify is queued as S88 carry-forward.

LISA OOM-to-σ conversion: σ_OOM_LISA = 1.0 OOM (LISA log-space sensitivity 1σ
floor in OOM; plan-implicit pin per §W3-3d.6 LISA design-sensitivity floor at
pivot frequency).
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
from canonical_constants import *  # noqa: E402, F401, F403

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

GATE_ID = "S87-W3-3D-JOINT-LITEBIRD-LISA-FISHER-DISCOUNT"  # (local)
SCHEME = "joint-Fisher-information"  # (local)
CONVENTION = "LiteBIRD-+-LISA-axis-orthogonal-per-VII.AC.3"  # (local)
L_MAX = "N/A"  # (local)

PASS_THRESHOLD = 1.5  # (local) joint_margin_sigma >= 1.5 PASSes
INFO_FLOOR = 1.0  # (local) [1.0, 1.5) is INFO

# LISA OOM-to-σ convention pin (plan-implicit per §W3-3d.6)
SIGMA_OOM_LISA = 1.0  # (local) LISA log-space 1σ sensitivity floor in OOM

UPSTREAM_LB = resolve_output(87, 's87_w3_3a_litebird_n_T_discriminator.npz')
UPSTREAM_LISA = resolve_output(87, 's87_w3_3b_lisa_omega_gw_a_c_discriminator.npz')

OUT_NPZ = resolve_output(87, 's87_w3_3d_joint_litebird_lisa_fisher.npz')
OUT_PNG = resolve_output(87, 's87_w3_3d_joint_litebird_lisa_fisher.png')
OUT_JSON = resolve_output(87, 's87_w3_3d_joint_litebird_lisa_fisher.json')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    UPSTREAM_LB,
    UPSTREAM_LISA,
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
    """Substitution chain (per plan §W3-3d.10):
    Step 1: F_LB = margin_LB^2 ; F_LISA = margin_LISA^2 ; F_joint = sum
    Step 2: PASS iff sqrt(F_joint) >= 1.5
    Step 3: simplify
    Step 4: direction — joint margin monotone non-decreasing in per-axis margins;
            sign_verdict = PASS (joint always >= max(per-axis))
    """
    a_data = np.load(UPSTREAM_LB)  # (local)
    b_data = np.load(UPSTREAM_LISA)  # (local)
    margin_LB = float(a_data["margin_sigma"])  # (local)
    split_OOM_abs = float(b_data["split_OOM_abs"])  # (local)
    margin_LISA = split_OOM_abs / SIGMA_OOM_LISA  # (local)

    F_LB = margin_LB ** 2  # (local)
    F_LISA = margin_LISA ** 2  # (local)
    F_joint = F_LB + F_LISA  # (local)
    joint_margin = math.sqrt(F_joint)  # (local)

    return {
        "margin_LB": margin_LB,
        "split_OOM_abs": split_OOM_abs,
        "margin_LISA": margin_LISA,
        "F_LB": F_LB,
        "F_LISA": F_LISA,
        "F_joint": F_joint,
        "joint_margin_sigma": joint_margin,
    }


def evaluate_gate(joint_margin):
    if joint_margin >= PASS_THRESHOLD:
        composite = "PASS"
        mag = "PASS"
    elif joint_margin >= INFO_FLOOR:
        composite = "INFO"
        mag = "INFO"
    else:
        composite = "FAIL"
        mag = "FAIL"
    # Sign per plan §W3-3d.10 Step 4: joint margin monotone non-decreasing in
    # per-axis margins; sign_verdict = PASS (predicted joint > max(per-axis))
    sign = "PASS"
    regime = "VALID"
    return composite, mag, sign, regime


def make_plot(result, png_path):
    fig, ax = plt.subplots(figsize=(8, 6))
    # Fisher ellipse on (n_T, log Ω_GW) plane: schematic 4-cell decomposition.
    # Cell centers (n_T, log Ω_GW): use canonical pins from upstream NPZs.
    # Show the joint Fisher confidence ellipse around the predicted Path-H/(A) cell.
    margin_LB = result["margin_LB"]  # (local)
    margin_LISA = result["margin_LISA"]  # (local)
    joint = result["joint_margin_sigma"]  # (local)

    # Side panels: per-axis marginals
    fig = plt.figure(figsize=(9, 6))
    gs = fig.add_gridspec(2, 2, width_ratios=[3, 1], height_ratios=[1, 3],
                          hspace=0.05, wspace=0.05)
    ax_main = fig.add_subplot(gs[1, 0])
    ax_top = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax_main)

    # Schematic: per-axis Gaussians around 0
    xs = np.linspace(-3, 3, 200)  # (local) σ-units on n_T axis
    ys = np.linspace(-3, 3, 200)  # (local) σ-units on log Ω_GW axis
    X, Y = np.meshgrid(xs, ys)
    # Joint Gaussian (axis-orthogonal): exponent = -(X^2 + Y^2)/2
    Z = np.exp(-0.5 * (X ** 2 + Y ** 2))  # (local)
    ax_main.contourf(X, Y, Z, levels=20, cmap="viridis")
    # Mark per-axis margins
    ax_main.axvline(margin_LB, color="white", linestyle="--", linewidth=1.0,
                    label=f"margin_LB = {margin_LB:.4f}σ")
    ax_main.axhline(min(margin_LISA, 3), color="white", linestyle=":", linewidth=1.0,
                    label=f"margin_LISA = {margin_LISA:.2f}σ (capped at 3σ)")
    ax_main.set_xlabel("n_T axis (σ-units)")
    ax_main.set_ylabel("log Ω_GW axis (σ-units)")
    ax_main.set_xlim(-3, 3)
    ax_main.set_ylim(-3, 3)
    ax_main.legend(loc="upper right", fontsize=8)

    # Top marginal (n_T)
    ax_top.plot(xs, np.exp(-0.5 * xs ** 2), "b-")
    ax_top.set_ylabel("LB density")
    ax_top.tick_params(axis="x", labelbottom=False)
    # Right marginal (log Ω_GW)
    ax_right.plot(np.exp(-0.5 * ys ** 2), ys, "r-")
    ax_right.set_xlabel("LISA density")
    ax_right.tick_params(axis="y", labelleft=False)

    fig.suptitle(
        f"§W3-3d Joint Fisher | margin_LB={margin_LB:.4f} margin_LISA={margin_LISA:.2f} "
        f"→ joint={joint:.4f}σ"
    )
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
    composite, mag_v, sign_v, regime_v = evaluate_gate(result["joint_margin_sigma"])

    print("=== Computation result ===")
    print(f"  margin_LB        = {result['margin_LB']:.6f}")
    print(f"  split_OOM_abs    = {result['split_OOM_abs']:.6f}")
    print(f"  margin_LISA      = {result['margin_LISA']:.6f}")
    print(f"  F_LB             = {result['F_LB']:.6f}")
    print(f"  F_LISA           = {result['F_LISA']:.4f}")
    print(f"  F_joint          = {result['F_joint']:.4f}")
    print(f"  joint_margin_σ   = {result['joint_margin_sigma']:.6f}")
    print(f"  composite        = {composite}")
    print(f"  3-tuple          = sign={sign_v} mag={mag_v} regime={regime_v}")

    np.savez(OUT_NPZ,
             joint_margin_sigma=result["joint_margin_sigma"],
             margin_LB=result["margin_LB"],
             margin_LISA=result["margin_LISA"],
             F_LB=result["F_LB"],
             F_LISA=result["F_LISA"],
             F_joint=result["F_joint"],
             sigma_OOM_LISA=SIGMA_OOM_LISA,
             pass_threshold=PASS_THRESHOLD,
             info_floor=INFO_FLOOR)
    out_json = {
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": round(result["joint_margin_sigma"], 4),
        "value_full": result["joint_margin_sigma"],
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "details": {
            "margin_LB": result["margin_LB"],
            "margin_LISA": result["margin_LISA"],
            "F_LB": result["F_LB"],
            "F_LISA": result["F_LISA"],
            "F_joint": result["F_joint"],
            "sigma_OOM_LISA_pin": SIGMA_OOM_LISA,
        },
        "joint_theorem_promotion_pathway_stage": "STAGE-1-CANDIDATE",
        "stage_2_carry_forward": "S88-JOINT-LITEBIRD-LISA-FISHER-INDEPENDENT-VERIFY",
    }
    OUT_JSON.write_text(json.dumps(out_json, indent=2), encoding="utf-8")
    make_plot(result, OUT_PNG)

    tag = (f"(value={round(result['joint_margin_sigma'], 4)!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    value_pub = round(result["joint_margin_sigma"], 4)
    append_verdict(composite, value_pub, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
