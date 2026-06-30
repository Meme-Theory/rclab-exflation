#!/usr/bin/env python3
"""
S87 W3-3a — S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR
================================================================

Gate: S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR ([VERIFY])

Pre-registered threshold (plan §W3-3a.9):
  margin_sigma = |n_T_PathH - n_T_PathC| / sigma_n_T_LiteBIRD
  PASS iff margin_sigma >= 1.0
  INFO iff 0.5 <= margin_sigma < 1.0
  FAIL iff margin_sigma < 0.5

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py (n_T_PathH_canonical, n_T_PathC_canonical, sigma_n_T_LiteBIRD)
  - script bytes

Output 4-tuple:
  (value=<margin_sigma>, scheme=LiteBIRD-n_T,
   convention=Path-H-vs-Path-C-block-axis, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
n_T is a substrate-emergent observable derived from spectral moments at tau_fold.
Path-H and Path-C are the two regulator-class projections of the substrate's
two-cell decomposition; their predicted n_T values are derived from r values via
the single-field consistency relation n_T = -r/8 (S84 W4-39 EXACT). The
discriminator margin in σ_LiteBIRD units measures how decisively LiteBIRD's
projected sensitivity can resolve the two-cell decomposition.

Direction of explanation: substrate (regulator-class lattice) → bridge map
(spectral moment → n_T projection) → laboratory (LiteBIRD measurement).

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediate variables tagged `# (local)`
- GPU NOT NEEDED (scalar arithmetic)
- Atomic single-line append to s87_gate_verdicts.txt + dual-SHA companion row
- 3-tuple companion row: sign_verdict=N/A (no signed delta) + magnitude_verdict + regime_verdict
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
    n_T_PathH_canonical,
    n_T_PathC_canonical,
    sigma_n_T_LiteBIRD,
)

# Section 2 — Standard imports
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Section 3 — Paths + pre-registration
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"  # (local)
GATE_ID = "S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR"  # (local)
SCHEME = "LiteBIRD-n_T"  # (local)
CONVENTION = "Path-H-vs-Path-C-block-axis"  # (local)
L_MAX = "N/A"  # (local)

PASS_THRESHOLD = 1.0  # (local) margin_sigma >= 1.0 PASSes
INFO_FLOOR = 0.5  # (local) margin_sigma in [0.5, 1.0) is INFO

OUT_NPZ = resolve_output(87, 's87_w3_3a_litebird_n_T_discriminator.npz')
OUT_PNG = resolve_output(87, 's87_w3_3a_litebird_n_T_discriminator.png')
OUT_JSON = resolve_output(87, 's87_w3_3a_litebird_n_T_discriminator.json')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

INPUT_FILES = [resolve_script(None, 'canonical_constants.py')]


# Section 4 — SHA-256 input-pin block
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
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
    """Substitution chain implementation:
    Step 1: definitions (canonical pins)
    Step 2: |n_T_PathH - n_T_PathC| / sigma
    Step 3: simplify
    Step 4: direction (no signed delta — magnitude only)
    """
    abs_diff = abs(float(n_T_PathH_canonical) - float(n_T_PathC_canonical))  # (local)
    margin_sigma = abs_diff / float(sigma_n_T_LiteBIRD)  # (local)
    return {
        "margin_sigma": margin_sigma,
        "abs_diff_n_T": abs_diff,
        "n_T_PathH": float(n_T_PathH_canonical),
        "n_T_PathC": float(n_T_PathC_canonical),
        "sigma_n_T_LiteBIRD": float(sigma_n_T_LiteBIRD),
    }


def evaluate_gate(margin_sigma):
    if margin_sigma >= PASS_THRESHOLD:
        return ("PASS", "PASS", "VALID")
    if margin_sigma >= INFO_FLOOR:
        return ("INFO", "INFO", "VALID")
    return ("FAIL", "FAIL", "VALID")


def make_plot(result, png_path):
    fig, ax = plt.subplots(figsize=(8, 5))
    n_TH = result["n_T_PathH"]  # (local)
    n_TC = result["n_T_PathC"]  # (local)
    sig = result["sigma_n_T_LiteBIRD"]  # (local)

    # Plot Path-H and Path-C as bars with sigma error bars
    labels = ["Path-H", "Path-C"]  # (local)
    vals = [n_TH, n_TC]  # (local)
    errs = [sig, sig]  # (local)
    colors = ["tab:blue", "tab:red"]  # (local)
    xs = np.arange(2)  # (local)
    ax.bar(xs, vals, yerr=errs, color=colors, capsize=10,
           alpha=0.6, edgecolor="black", label="±σ_LB")
    # Shade LiteBIRD sensitivity band
    ymid = (n_TH + n_TC) / 2  # (local)
    ax.axhspan(ymid - sig / 2, ymid + sig / 2, color="gray", alpha=0.2,
               label="LiteBIRD ±σ band (centered at midpoint)")
    ax.set_xticks(xs)
    ax.set_xticklabels(labels)
    ax.set_ylabel("n_T")
    ax.set_title(f"§W3-3a n_T discriminator | margin_σ = {result['margin_sigma']:.4f}")
    ax.axhline(0, linestyle=":", color="black", linewidth=0.5)
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
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    margin = result["margin_sigma"]
    composite, mag_v, regime_v = evaluate_gate(margin)
    sign_v = "N/A"  # plan §W3-3a.10: |·| only — no signed delta

    print(f"=== Computation result ===")
    print(f"  n_T_PathH        = {result['n_T_PathH']}")
    print(f"  n_T_PathC        = {result['n_T_PathC']}")
    print(f"  sigma_n_T_LB     = {result['sigma_n_T_LiteBIRD']}")
    print(f"  |Δn_T|           = {result['abs_diff_n_T']:.6e}")
    print(f"  margin_sigma     = {margin:.6f}")
    print(f"  composite        = {composite}")
    print(f"  3-tuple          = sign={sign_v} mag={mag_v} regime={regime_v}")

    # Save .npz, .json, .png
    np.savez(OUT_NPZ,
             margin_sigma=margin,
             n_T_PathH=result["n_T_PathH"],
             n_T_PathC=result["n_T_PathC"],
             sigma_n_T_LiteBIRD=result["sigma_n_T_LiteBIRD"],
             abs_diff_n_T=result["abs_diff_n_T"],
             pass_threshold=PASS_THRESHOLD,
             info_floor=INFO_FLOOR)
    out_json = {
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": round(margin, 4),
        "value_full": margin,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "details": {
            "n_T_PathH": result["n_T_PathH"],
            "n_T_PathC": result["n_T_PathC"],
            "sigma_n_T_LiteBIRD": result["sigma_n_T_LiteBIRD"],
            "abs_diff_n_T": result["abs_diff_n_T"],
        },
    }
    OUT_JSON.write_text(json.dumps(out_json, indent=2), encoding="utf-8")
    make_plot(result, OUT_PNG)

    tag = (f"(value={round(margin, 4)!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    # Round to 4 sig figs per plan §W3-3a.7 publication_precision_pin
    value_pub = round(margin, 4)
    append_verdict(composite, value_pub, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
