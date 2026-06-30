#!/usr/bin/env python3
"""
S87 W3-3b — S87-W3-3B-LISA-OMEGA-GW-A-C-REGULATOR-CLASS-DISCRIMINATOR
======================================================================

Gate: S87-W3-3B-LISA-OMEGA-GW-A-C-REGULATOR-CLASS-DISCRIMINATOR ([VERIFY])

Pre-registered threshold (plan §W3-3b.9):
  split_OOM = log10(Omega_GW_FW_(A) / Omega_GW_FW_(C))
  PASS iff |split_OOM| >= 1.0
  INFO iff 0.5 <= |split_OOM| < 1.0
  FAIL iff |split_OOM| < 0.5

Sage-exact regulator-class values per .claude/rules/regulator-pin-discipline.md
extension: round-figure 1e-57 FORBIDDEN; canonical Omega_GW_Lambda_C_LISA = 8.299e-58.

Inputs:
  - canonical_constants.py (Omega_GW_Lambda_A_LISA, Omega_GW_Lambda_C_LISA)
  - script bytes

Output 4-tuple:
  (value=<|split_OOM|>, scheme=LISA-Ω_GW,
   convention=(A)-vs-(C)-regulator-class-split, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Ω_GW is a substrate-emergent observable; the (A)/(C) regulator-class split is
structural geometry of the regulator-class atlas's two sub-cone partition.
Substrate IS the spectrum; LISA measures its lab-image; the split is structural.
"""

from __future__ import annotations

# Section 1 — Canonical constants (MANDATORY first import)
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
    Omega_GW_Lambda_A_LISA,
    Omega_GW_Lambda_C_LISA,
)

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

GATE_ID = "S87-W3-3B-LISA-OMEGA-GW-A-C-REGULATOR-CLASS-DISCRIMINATOR"  # (local)
SCHEME = "LISA-Ω_GW"  # (local)
CONVENTION = "(A)-vs-(C)-regulator-class-split"  # (local)
L_MAX = "N/A"  # (local)

PASS_THRESHOLD = 1.0  # (local) |split_OOM| >= 1.0 PASSes
INFO_FLOOR = 0.5  # (local) [0.5, 1.0) is INFO

OUT_NPZ = resolve_output(87, 's87_w3_3b_lisa_omega_gw_a_c_discriminator.npz')
OUT_PNG = resolve_output(87, 's87_w3_3b_lisa_omega_gw_a_c_discriminator.png')
OUT_JSON = resolve_output(87, 's87_w3_3b_lisa_omega_gw_a_c_discriminator.json')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

INPUT_FILES = [resolve_script(None, 'canonical_constants.py')]


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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
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
    """Substitution chain (per plan §W3-3b.10):
    Step 1: definitions (Sage-exact rationals).
    Step 2: |log10(A/C)| >= 1.0
    Step 3: simplify
    Step 4: direction — Sage check yields ratio ~1.205e+47 → split_OOM ≈ +47.08
            sign_verdict PASS (predicted positive matches computed positive)
    """
    omega_A = float(Omega_GW_Lambda_A_LISA)  # (local)
    omega_C = float(Omega_GW_Lambda_C_LISA)  # (local)
    ratio = omega_A / omega_C  # (local)
    split_OOM = math.log10(ratio)  # (local)
    return {
        "split_OOM": split_OOM,
        "split_OOM_abs": abs(split_OOM),
        "ratio": ratio,
        "Omega_A": omega_A,
        "Omega_C": omega_C,
    }


def evaluate_gate(split_OOM):
    abs_split = abs(split_OOM)  # (local)
    if abs_split >= PASS_THRESHOLD:
        composite = "PASS"
        mag = "PASS"
    elif abs_split >= INFO_FLOOR:
        composite = "INFO"
        mag = "INFO"
    else:
        composite = "FAIL"
        mag = "FAIL"
    # Sign verdict per plan §W3-3b.10 Step 4:
    # Predicted direction split_OOM > 0; computed sign matches → PASS
    sign = "PASS" if split_OOM > 0 else "FAIL"
    regime = "VALID"  # exact arithmetic; no regime breakdown
    return composite, mag, sign, regime


def make_plot(result, png_path):
    fig, ax = plt.subplots(figsize=(8, 5))
    log_A = math.log10(result["Omega_A"])  # (local)
    log_C = math.log10(result["Omega_C"])  # (local)

    # Show the two regulator-class predictions on log-y
    labels = ["Ω_GW^(A)", "Ω_GW^(C)"]  # (local)
    vals = [log_A, log_C]  # (local)
    colors = ["tab:blue", "tab:red"]  # (local)
    xs = np.arange(2)  # (local)
    ax.bar(xs, vals, color=colors, alpha=0.6, edgecolor="black")
    # LISA strain-sensitivity floor at 3 mHz: nominal log10 Ω_floor ≈ -12 (informational)
    ax.axhline(-12, linestyle="--", color="black", linewidth=0.8,
               label="LISA design-sensitivity floor (~10^{-12} OOM)")
    ax.set_xticks(xs)
    ax.set_xticklabels(labels)
    ax.set_ylabel("log10 Ω_GW")
    ax.set_title(
        f"§W3-3b LISA Ω_GW (A)/(C) split | split_OOM = {result['split_OOM']:.4f}"
    )
    ax.legend()
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
    composite, mag_v, sign_v, regime_v = evaluate_gate(result["split_OOM"])

    print("=== Computation result ===")
    print(f"  Omega_A          = {result['Omega_A']:.6e}")
    print(f"  Omega_C          = {result['Omega_C']:.6e}")
    print(f"  ratio (A)/(C)    = {result['ratio']:.6e}")
    print(f"  split_OOM        = {result['split_OOM']:.6f}")
    print(f"  |split_OOM|      = {result['split_OOM_abs']:.6f}")
    print(f"  composite        = {composite}")
    print(f"  3-tuple          = sign={sign_v} mag={mag_v} regime={regime_v}")

    np.savez(OUT_NPZ,
             split_OOM=result["split_OOM"],
             split_OOM_abs=result["split_OOM_abs"],
             ratio=result["ratio"],
             Omega_A=result["Omega_A"],
             Omega_C=result["Omega_C"],
             pass_threshold=PASS_THRESHOLD,
             info_floor=INFO_FLOOR)
    out_json = {
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": round(result["split_OOM_abs"], 4),
        "value_full": result["split_OOM_abs"],
        "split_OOM_signed": result["split_OOM"],
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "details": {
            "Omega_A": result["Omega_A"],
            "Omega_C": result["Omega_C"],
            "ratio": result["ratio"],
        },
    }
    OUT_JSON.write_text(json.dumps(out_json, indent=2), encoding="utf-8")
    make_plot(result, OUT_PNG)

    tag = (f"(value={round(result['split_OOM_abs'], 4)!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    value_pub = round(result["split_OOM_abs"], 4)
    append_verdict(composite, value_pub, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
