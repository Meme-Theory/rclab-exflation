#!/usr/bin/env python3
"""
S87 W3-3c — S87-DELTA-SPEED-MELLIN-WINDOW (CF-23, [SIGN] trigger)
==================================================================

Gate: S87-DELTA-SPEED-MELLIN-WINDOW ([SIGN])

Pre-registered threshold (plan §W3-3c.9):
  - PASS:  sign_PASS AND mag_PASS AND regime=VALID
  - INFO:  margin in [3σ, 5σ) OR regime=MARGINAL
  - FAIL:  sign_verdict=FAIL OR regime=BREAKDOWN OR mag_PASS=False with regime=VALID
  - PRE-REG-INCOMPLETE: any canonical pin missing per Class-(f) remediation

Class-(f) protocol (per .claude/rules/substrate-first-canonical-sourcing.md):
  Required pins:
    - delta_speed_PathH (Mellin-window substrate prediction at τ_fold, Path-H)
    - delta_speed_PathC (Mellin-window substrate prediction at τ_fold, Path-C)
    - sigma_delta_speed_mellin_noise (numerical noise floor at L_max=10)
  If ANY missing, emit PRE-REG-INCOMPLETE; D_max ≥ 3.0 HARD-HALT band per
  Class-(f) — placeholder O(10⁻ⁿ) FORBIDDEN.

MCP audit performed before compute:
  mcp__knowledge__.list_constants("delta_speed|sigma_delta_speed") → 0 hits
  mcp__knowledge__.search_knowledge("delta_speed asymmetric inheritance Volovik
                                    R3-A Mellin-cone Path-H Path-C") → 10 hits;
                                    none provide a substrate-first canonical
                                    value for delta_speed_PathH/PathC.
  mcp__knowledge__.search_knowledge("phonon mode speed deviation flat reference
                                    c_S asymmetric inheritance regulator class")
                                    → 5 hits; closest is c_BLV = 0.485 (different
                                    object: scalar fabric sound speed, not
                                    regulator-class-projected δ_speed).

Conclusion: NO substrate-first canonical exists in the framework's MCP/knowledge
base for the three required pins. Per the spawn prompt's Class-(f) HARD-HALT
band rule, this gate emits PRE-REG-INCOMPLETE and queues the canonical-sourcing
work as S88 carry-forward (`S88-DELTA-SPEED-MELLIN-CANONICAL-SOURCING`).

Inputs:
  - canonical_constants.py (probed for pins; pins MISSING → Class-(f) remediation)
  - script bytes

Output 4-tuple:
  (value='PRE-REG-INC_blocked_by_delta_speed_canonical_pins_MISSING',
   scheme=Mellin-cone-analytic-continuation,
   convention=delta-speed-asymmetric-inheritance-volovik-R3A,
   L_max=10)

Classification: PHONONIC

METHODOLOGY (when pins exist — preserved for S88 wire-up)
---------------------------------------------------------
δ_speed at τ_fold via Mellin-cone analytic continuation at substrate-distance-1
pole s=4 (a_4^{Mellin} regulator-pin tag per regulator-pin-discipline.md). For
each regulator class (Path-H, Path-C), evaluate δ_speed via Mellin-window
integral. Test (a) sign agreement with Volovik R3-A asymmetric-inheritance
prediction (Path-H: δ_speed > 0; Path-C: δ_speed < 0); (b) magnitude > 5σ noise
floor.

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediate variables tagged `# (local)`
- Class-(f) remediation: explicit emission of PRE-REG-INCOMPLETE on missing pins
- 3-tuple companion row REQUIRED for [SIGN] trigger
- Composite collapse: per gate-verdicts.md schema-v2 (BREAKDOWN dominates)
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
import canonical_constants as cc  # noqa: E402

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

GATE_ID = "S87-DELTA-SPEED-MELLIN-WINDOW"  # (local)
SCHEME = "Mellin-cone-analytic-continuation"  # (local)
CONVENTION = "delta-speed-asymmetric-inheritance-volovik-R3A"  # (local)
L_MAX = 10  # (local)

# Required canonical-pin names (plan §W3-3c.6)
REQUIRED_PINS = (
    "delta_speed_PathH",
    "delta_speed_PathC",
    "sigma_delta_speed_mellin_noise",
)  # (local)

OUT_NPZ = resolve_output(87, 's87_w3_3c_delta_speed_mellin_window.npz')
OUT_PNG = resolve_output(87, 's87_w3_3c_delta_speed_mellin_window.png')
OUT_JSON = resolve_output(87, 's87_w3_3c_delta_speed_mellin_window.json')
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
    # Add gate-distinguishing key to pinmap so audit_sha256 is unique per gate
    pins_aug = dict(pins)  # (local)
    pins_aug["_gate_id"] = GATE_ID
    pins_aug["_scheme"] = SCHEME
    pins_aug["_convention"] = CONVENTION
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
def check_required_pins():
    """Class-(f) remediation: probe canonical_constants.py for required pins.

    Returns
    -------
    (missing: list[str], present: dict[str, float])
    """
    missing = []  # (local)
    present = {}  # (local)
    for name in REQUIRED_PINS:
        if hasattr(cc, name):
            present[name] = getattr(cc, name)
        else:
            missing.append(name)
    return missing, present


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


def make_pre_reg_inc_plot(missing, png_path):
    """Diagnostic plot for PRE-REG-INC state — visualizes what would be plotted
    once the canonical pins exist (placeholder geometry per substitution chain
    Step 4: anti-correlated δ_speed around δ=0)."""
    fig, ax = plt.subplots(figsize=(8, 5))
    tau = np.linspace(0.185, 0.195, 11)  # (local) τ-sweep around τ_fold=0.190
    # Schematic anti-correlated trajectories (NOT canonical values; visual only)
    delta_H_schem = 1e-3 * (tau - 0.190) / 0.005  # (local) schematic, not pinned
    delta_C_schem = -delta_H_schem  # (local) anti-correlated, schematic
    ax.plot(tau, delta_H_schem, "b-", label="Path-H (schematic, sign>0)")
    ax.plot(tau, delta_C_schem, "r-", label="Path-C (schematic, sign<0)")
    ax.axvline(0.190, color="gray", linestyle="--", linewidth=0.7,
               label="τ_fold=0.190")
    ax.axhline(0, color="black", linestyle=":", linewidth=0.5)
    ax.set_xlabel("τ (Jensen flow parameter)")
    ax.set_ylabel("δ_speed (schematic; canonical PENDING)")
    ax.set_title(
        "§W3-3c δ_speed Mellin-window | PRE-REG-INC: canonical pins MISSING\n"
        f"missing: {', '.join(missing)}"
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(png_path, dpi=120)
    plt.close(fig)


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

    missing, present = check_required_pins()

    if missing:
        # Class-(f) HARD-HALT band: emit PRE-REG-INCOMPLETE; no placeholder.
        composite = "PRE-REG-INC"
        sign_v = "N/A"
        mag_v = "FAIL"  # cannot evaluate magnitude → conservatively FAIL on mag
        regime_v = "BREAKDOWN"  # canonical pins missing ⇒ regime undefined
        # Plan-pre-registered descriptive value (per
        # .claude/rules/mechanical-closure-discipline.md "value=" pattern):
        value = (
            "PRE-REG-INC_blocked_by_"
            "delta_speed_PathH_MISSING_"
            "delta_speed_PathC_MISSING_"
            "sigma_delta_speed_mellin_noise_MISSING"
        )

        print("=== Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL ===")
        print(f"  Missing pins: {missing}")
        print(f"  Present pins: {sorted(present.keys())}")
        print(f"  HARD-HALT band: D_max ≥ 3.0 (no substrate canonical exists)")
        print(f"  Verdict        = {composite}")
        print(f"  3-tuple        = sign={sign_v} mag={mag_v} regime={regime_v}")

        np.savez(OUT_NPZ,
                 verdict=composite,
                 missing_pins=np.array(missing, dtype=object),
                 present_pins=np.array(list(present.keys()), dtype=object),
                 hardalt_class="(f)_PIN_PLACEHOLDER_PENDING_SUBSTRATE_CANONICAL",
                 carry_forward="S88-DELTA-SPEED-MELLIN-CANONICAL-SOURCING",
                 L_max=L_MAX,
                 sign_verdict=sign_v,
                 magnitude_verdict=mag_v,
                 regime_verdict=regime_v)
        out_json = {
            "gate_id": GATE_ID,
            "verdict": composite,
            "value": value,
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "sign_verdict": sign_v,
            "magnitude_verdict": mag_v,
            "regime_verdict": regime_v,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "remediation_class": "(f)_PIN_PLACEHOLDER_PENDING_SUBSTRATE_CANONICAL",
            "missing_canonical_pins": missing,
            "carry_forward": "S88-DELTA-SPEED-MELLIN-CANONICAL-SOURCING",
            "mcp_audit_summary": {
                "list_constants_query": "delta_speed|sigma_delta_speed",
                "list_constants_hits": 0,
                "search_knowledge_substrate_first_canonical_found": False,
                "closest_unrelated_pin": "c_BLV (S64 Brillouin-Landau-Vortex sound speed; "
                                         "scalar fabric sound speed, NOT regulator-class-projected δ_speed)",
            },
        }
        OUT_JSON.write_text(json.dumps(out_json, indent=2), encoding="utf-8")
        make_pre_reg_inc_plot(missing, OUT_PNG)

        tag = (f"(value={value!r}, scheme={SCHEME}, "
               f"convention={CONVENTION}, L_max={L_MAX})")
        print(tag)
        append_verdict(composite, value, audit_sha, content_sha,
                       sign_v, mag_v, regime_v)
        wall = time.time() - t0  # (local)
        print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
        return 0

    # Future-S88 wire-up path (executed only if pins land in canonical_constants.py):
    raise NotImplementedError(
        "S88 wire-up: canonical pins exist; implement Mellin-cone analytic "
        "continuation at substrate-distance-1 pole s=4, sign+magnitude tests, "
        "regime band check. Spec frozen here."
    )


if __name__ == "__main__":
    sys.exit(main())
