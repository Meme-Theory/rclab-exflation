#!/usr/bin/env python3
"""
S83 W3-G42 -- DR3-LIVE-WATCH (Binary rectangle on (w_0, w_a))
==============================================================

Gate: S83-DR3-LIVE-WATCH ([AUDIT][PENDING-EVENT])

Pre-registered threshold:
  PASS iff DR3 central (w_0, w_a) lies within the rectangle
    R := [-1.05, -0.85] x [-0.2, 0.2]
  FAIL iff DR3 central (w_0, w_a) lies outside R
  PENDING-EVENT iff DESI DR3 data release has not yet occurred at script runtime.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py (closure hash; source of w0_FW, wa_FW)

Output 4-tuple:
  (w0_wa_status=PENDING, scheme=DESI-DR3-live-watch,
   convention=S59-pred-w0=-0.918, L_max=N/A)

Classification: PHONONIC / NON-PHONONIC (observational)

METHODOLOGY
-----------
Infrastructure-only. This script:
  (a) pre-registers the binary rectangle bounds R on (w_0, w_a);
  (b) imports framework predictions w0_FW = -0.918 (S59 VdD-Mack workshop) and
      wa_FW = 0.0 (four-fold locked, Volovik substrate-compaction partition) from
      canonical_constants.py;
  (c) documents the planned verdict logic for two contingencies at DR3 release:
        (i)  public cov matrix released -> compute chi^2 under DR3 bf + cov;
        (ii) no public cov -> 2D posterior rectangle containment test;
  (d) sets up a release-detection stub (local-file poll) that will activate the
      verdict computation when the DR3 bf file (or published w_0, w_a central +
      covariance) is dropped into `computations/_shared/desi_dr3_release/`;
  (e) emits a PENDING-EVENT verdict and saves the pre-registered rectangle +
      framework point + (cov-contingency) plan to s83_w3_g42_dr3_live_watch.npz.

When DR3 is released, a successor script will load this npz as input (SHA-pinned
into its own closure hash), apply the recorded verdict rule unchanged, and
append a follow-up verdict line overriding the PENDING-EVENT status.

DISCIPLINE
----------
- `from canonical_constants import *` for w0_FW, wa_FW.
- All intermediates tagged `# (local)`.
- SHA-256 of canonical_constants.py logged in first 20 lines of stdout.
- 4-tuple printed as final non-verdict line.
- Verdict line appended to s83_gate_verdicts.txt with full 64-char closure SHA.
- Verdict tag is PENDING-EVENT (not PASS/FAIL); DR3 not yet released.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
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


# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S83"                                                 # (local)
GATE_ID = "S83-DR3-LIVE-WATCH"                                  # (local)
SCHEME = "DESI-DR3-live-watch"                                  # (local)
CONVENTION = "S59-pred-w0=-0.918"                               # (local)
L_MAX = "N/A"                                                   # (local)

# Pre-registered binary rectangle R on (w_0, w_a).
# Half-widths chosen to exceed 2 x projected DR3 sigma(w_0) = 0.046
# and ~1.1 x projected sigma(w_a) = 0.177 (S71 DESI-DR3-SCENARIO-B-PRECISE-71).
RECTANGLE_W0 = (-1.05, -0.85)                                   # (local) pre-registered bounds
RECTANGLE_WA = (-0.2, 0.2)                                      # (local) pre-registered bounds

# Framework point (imported; NOT local) -- w0_FW = -0.918, wa_FW = 0.0
# from canonical_constants.py (S58 Volovik partition, S59 VdD-Mack).

# DR3 release detector stub -- poll target directory at runtime.
DR3_RELEASE_DIR = resolve_script(None, 'desi_dr3_release')                # (local) polling target
DR3_BF_EXPECTED_FILE = DR3_RELEASE_DIR / "desi_dr3_w0wa_bf.json"  # (local) stub
DR3_COV_EXPECTED_FILE = DR3_RELEASE_DIR / "desi_dr3_w0wa_cov.json"  # (local) stub

# Covariance-contingency plan (documentation only; applied at successor runtime).
COV_CONTINGENCY_PLAN = {                                        # (local)
    "case_i_cov_released": {
        "verdict_method": "chi^2 with released cov",
        "formula": (
            "delta = [w_0^DR3 - w0_FW, w_a^DR3 - wa_FW]; "
            "chi^2 = delta @ cov_inv @ delta.T"
        ),
        "note": (
            "Rectangle containment is still the primary verdict rule; "
            "chi^2 is ancillary OOM context."
        ),
    },
    "case_ii_no_public_cov": {
        "verdict_method": "2D rectangle containment test",
        "formula": (
            "PASS iff w_0^DR3 in RECTANGLE_W0 AND w_a^DR3 in RECTANGLE_WA."
        ),
        "note": (
            "Forecast sigma(w_0)_DR3 = 0.046, sigma(w_a)_DR3 = 0.177, "
            "rho = -0.85 (S71). If bf central alone is released without cov, "
            "the rectangle test is the only well-defined verdict rule."
        ),
    },
}

# Output destinations
OUT_NPZ = resolve_output(83, 's83_w3_g42_dr3_live_watch.npz')
VERDICT_TXT = resolve_output(83, 's83_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                        # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                   # (local)
    for p in inputs:
        sha = sha256_of(p)                                      # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    """Stable hash over all input SHAs (invariant to dict ordering).

    Includes GATE_ID, SCHEME, CONVENTION, L_MAX, rectangle bounds, framework
    point, and PENDING-EVENT tag in the hashed payload so the closure
    uniquely identifies this pre-registration snapshot.
    """
    items = sorted(pins.items())                                # (local)
    h = hashlib.sha256()                                        # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    # Include pre-registered scalars in closure
    payload = (
        f"GATE_ID={GATE_ID}\n"
        f"SCHEME={SCHEME}\n"
        f"CONVENTION={CONVENTION}\n"
        f"L_MAX={L_MAX}\n"
        f"RECTANGLE_W0={RECTANGLE_W0}\n"
        f"RECTANGLE_WA={RECTANGLE_WA}\n"
        f"w0_FW={w0_FW}\n"
        f"wa_FW={wa_FW}\n"
        f"STATUS_TAG=PENDING-EVENT\n"
    )                                                            # (local)
    h.update(payload.encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Release detection stub (local-file poll)
# ---------------------------------------------------------------------------

def detect_dr3_release():
    """Return (release_occurred, details_dict).

    If neither the bf file nor the cov file is present in DR3_RELEASE_DIR,
    return (False, {"reason": "no release files found"}).

    This stub is infrastructure-only: DR3 has NOT been released at session
    S83 (2026-04-18). Successor sessions will extend this function to (a)
    handle public release archives (e.g., DESI collaboration landing pages)
    and (b) load bf + cov JSON for the verdict pipeline.
    """
    if not DR3_RELEASE_DIR.exists():
        return False, {
            "reason": "DR3_RELEASE_DIR not present; pre-registration only",
            "release_dir": str(DR3_RELEASE_DIR),
        }
    bf_present = DR3_BF_EXPECTED_FILE.is_file()                 # (local)
    cov_present = DR3_COV_EXPECTED_FILE.is_file()               # (local)
    if not bf_present:
        return False, {
            "reason": "DR3 bf file not yet dropped",
            "bf_file": str(DR3_BF_EXPECTED_FILE),
            "cov_file_present": cov_present,
        }
    return True, {
        "bf_file": str(DR3_BF_EXPECTED_FILE),
        "cov_file_present": cov_present,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Verdict rule (defined pre-registration; applies at DR3 release)
# ---------------------------------------------------------------------------

def verdict_rule(w0_dr3, wa_dr3):
    """Apply the pre-registered rectangle containment rule.

    PASS iff both (w_0^DR3, w_a^DR3) lie within the pre-registered rectangle;
    FAIL otherwise.

    Not invoked during infrastructure-only run; encoded here for the successor
    to call unchanged when DR3 data arrives (SHA-pinned to this script).
    """
    in_w0 = RECTANGLE_W0[0] <= w0_dr3 <= RECTANGLE_W0[1]        # (local)
    in_wa = RECTANGLE_WA[0] <= wa_dr3 <= RECTANGLE_WA[1]        # (local)
    if in_w0 and in_wa:
        return "PASS"
    return "FAIL"


def sanity_check_framework_point():
    """Self-consistency: framework point (w0_FW, wa_FW) must lie inside R.

    This is a pre-registration sanity test: if the framework's own central
    prediction fell outside R, the rectangle would be mis-specified. A PASS
    here does NOT imply the gate passes -- the gate's verdict is about DR3
    DATA, not the framework point.
    """
    in_w0 = RECTANGLE_W0[0] <= w0_FW <= RECTANGLE_W0[1]         # (local)
    in_wa = RECTANGLE_WA[0] <= wa_FW <= RECTANGLE_WA[1]         # (local)
    mid_w0 = (RECTANGLE_W0[0] + RECTANGLE_W0[1]) / 2.0          # (local)
    mid_wa = (RECTANGLE_WA[0] + RECTANGLE_WA[1]) / 2.0          # (local)
    return {
        "framework_in_w0_box": bool(in_w0),
        "framework_in_wa_box": bool(in_wa),
        "framework_in_rectangle": bool(in_w0 and in_wa),
        "offset_w0_from_midpoint": float(w0_FW - mid_w0),
        "offset_wa_from_midpoint": float(wa_FW - mid_wa),
        "half_width_w0": (RECTANGLE_W0[1] - RECTANGLE_W0[0]) / 2.0,
        "half_width_wa": (RECTANGLE_WA[1] - RECTANGLE_WA[0]) / 2.0,
    }


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(status_tag, closure_sha):
    """Append a single-line verdict to s83_gate_verdicts.txt with full 64-char SHA pin.

    For PENDING-EVENT gates, the 'value' field encodes the infrastructure state.
    """
    value_str = (
        f"PENDING-EVENT_w0_pred={w0_FW}_wa_pred={wa_FW}"
        f"_rect_w0={RECTANGLE_W0}_rect_wa={RECTANGLE_WA}"
    )                                                           # (local)
    line = (
        f"{GATE_ID}: {status_tag} -- value={value_str!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )                                                            # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def main():
    t0 = time.time()                                            # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)                          # (local)
    closure = closure_hash(pins)                                # (local)
    print(f"  closure: {closure[:16]}...  (full: {closure})")
    print()

    # 2. Framework prediction (from canonical_constants)
    print(f"Framework prediction: w_0 = {w0_FW}, w_a = {wa_FW}")
    print(f"Pre-registered rectangle: w_0 in {RECTANGLE_W0}, w_a in {RECTANGLE_WA}")

    # 3. Self-consistency sanity (framework point inside rectangle)
    sanity = sanity_check_framework_point()                     # (local)
    print(f"Sanity (framework in rect): {sanity}")
    assert sanity["framework_in_rectangle"], (
        "Pre-reg misspec: framework point outside rectangle. "
        f"w0_FW={w0_FW}, wa_FW={wa_FW}, rect={RECTANGLE_W0, RECTANGLE_WA}"
    )

    # 4. Release detection stub (DR3 not released at S83)
    released, release_info = detect_dr3_release()               # (local)
    print(f"DR3 release detected: {released}")
    print(f"Release detection info: {release_info}")

    # 5. Verdict assembly
    if released:
        # Successor path (infrastructure-ready but not exercised at S83).
        # The successor script will (a) load bf + cov, (b) apply verdict_rule,
        # (c) append a new verdict line overriding PENDING-EVENT.
        status_tag = "VERDICT-SUCCESSOR-REQUIRED"                # (local)
        print(
            "WARNING: release detected but this script is infrastructure-only. "
            "Run the S83+ successor verdict script to apply verdict_rule."
        )
    else:
        status_tag = "PENDING-EVENT"                             # (local)

    # 6. Save all pre-registered state to npz (successor input)
    np.savez(
        OUT_NPZ,
        rectangle_w0=np.array(RECTANGLE_W0),
        rectangle_wa=np.array(RECTANGLE_WA),
        pred_w0=float(w0_FW),
        pred_wa=float(wa_FW),
        half_width_w0=(RECTANGLE_W0[1] - RECTANGLE_W0[0]) / 2.0,
        half_width_wa=(RECTANGLE_WA[1] - RECTANGLE_WA[0]) / 2.0,
        midpoint_w0=(RECTANGLE_W0[0] + RECTANGLE_W0[1]) / 2.0,
        midpoint_wa=(RECTANGLE_WA[0] + RECTANGLE_WA[1]) / 2.0,
        offset_w0_from_midpoint=float(w0_FW - (RECTANGLE_W0[0] + RECTANGLE_W0[1]) / 2.0),
        offset_wa_from_midpoint=float(wa_FW - (RECTANGLE_WA[0] + RECTANGLE_WA[1]) / 2.0),
        framework_in_rectangle=bool(sanity["framework_in_rectangle"]),
        release_detected=bool(released),
        status_tag=str(status_tag),
        closure_sha=str(closure),
        gate_id=str(GATE_ID),
        scheme=str(SCHEME),
        convention=str(CONVENTION),
        L_max=str(L_MAX),
        cov_plan_json=json.dumps(COV_CONTINGENCY_PLAN),
        release_info_json=json.dumps(release_info),
        # Projected DR3 sigmas (from S71 DESI-DR3-SCENARIO-B-PRECISE-71)
        sigma_w0_dr3_proj=0.046,
        sigma_wa_dr3_proj=0.177,
        rho_w0_wa_dr3_proj=-0.85,
        # Rectangle half-width in units of projected sigma
        half_width_w0_in_sigma=(RECTANGLE_W0[1] - RECTANGLE_W0[0]) / 2.0 / 0.046,
        half_width_wa_in_sigma=(RECTANGLE_WA[1] - RECTANGLE_WA[0]) / 2.0 / 0.177,
    )
    print(f"Wrote {OUT_NPZ}")

    # 7. Emit 4-tuple + append verdict
    value_summary = (
        f"PENDING-EVENT_w0_pred={w0_FW}_wa_pred={wa_FW}"
        f"_rect_w0={RECTANGLE_W0}_rect_wa={RECTANGLE_WA}"
    )                                                            # (local)
    tag = emit_4tuple(value_summary, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(status_tag, closure)

    # 8. Final summary
    wall = time.time() - t0                                     # (local)
    print(f"\n=== {GATE_ID}: {status_tag} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
