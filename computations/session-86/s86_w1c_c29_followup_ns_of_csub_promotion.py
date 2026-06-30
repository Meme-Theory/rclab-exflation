#!/usr/bin/env python3
"""
S86 W1c-8 followup — n_s_of_c_sub canonical-promotion verifier
==============================================================

Gate: S86-W1C-C29-FOLLOWUP-NS-OF-CSUB-PROMOTION ([VERIFY])

Promotion task (Task #11 in-session remediation under "No Technical Debt"):
  C29 (mack-cosmic-bridge, 2026-04-26) computed
      r_running = +0.02201 at c_sub = 3.647
  by deriving the substrate Mellin-tilt callable
      n_s(c_sub) = 1 - 2 * eps_baseline * (c_sub_baseline / c_sub)
  on-the-fly inside the C29 producing script, NOT as canonical
  infrastructure. C29 carry-forward bullet #2 requested promotion
  to canonical_constants.py for downstream gates (CMB-S4 forecast,
  CMB-HD forecast, Path-H/Path-C joint discrimination).

This verifier:
  (1) Imports the promoted callable n_s_of_c_sub + canonical anchors
      eps_baseline, c_sub_baseline from canonical_constants.py.
  (2) Calls n_s_of_c_sub(3.647) and cross-checks against C29's runtime
      n_s_0 = 0.9784607074 (WP §W1c-8 Runtime Values table).
  (3) Prints the substitution chain in stdout for audit.
  (4) Emits PASS iff |n_s_promoted - n_s_C29_runtime| / |n_s_C29_runtime|
      < 1e-12, FAIL otherwise.

Pre-registered threshold:
  PASS iff rel_diff < 1e-12 (effective Python float64 equality).
  FAIL if rel_diff >= 1e-12 (formula drift between C29 and promoted form).

Inputs (SHA-256 dual-pinned at runtime — first 20 lines of stdout):
  - computations/_shared/canonical_constants.py (now contains the callable)
  - computations/session-86/s86_w1c_c29_falsifier_promotion.py (source gate)
  - sessions/archive/session-86/session-86-w1c-workingpaper.md (source WP §W1c-8)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<n_s at c_sub=3.647>, scheme=canonical-promotion,
   convention=substrate-Mellin-tilt, L_max=N/A)

Classification: PHONONIC (n_s is the substrate scalar spectral index,
                a Mellin-tilt response of the substrate's spectral
                cascade re-weighting under c_sub variation).

DISCIPLINE
----------
- `from canonical_constants import *` (mandatory; first import)
- Every local intermediate tagged `# (local)`
- CPU-only path (formula evaluation; no matrices); OMP_NUM_THREADS=8 cap
  set BEFORE numpy import per .claude/rules/computation-environment.md
- Substitution chain printed verbatim (sign/direction claim about
  cross-check agreement is read off the canonical |rel_diff| form ONLY)
- Verdict line appended to s86_gate_verdicts.txt with dual-SHA companion
  comment row per S84+ schema
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import)
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

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
#
# This pulls in the freshly-promoted n_s_of_c_sub callable + the
# canonical anchors eps_baseline, c_sub_baseline.
# ---------------------------------------------------------------------------
from canonical_constants import (  # noqa: F401
    planck_ns,
    eps_baseline,
    c_sub_baseline,
    n_s_of_c_sub,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSION_DIR = PROJECT_ROOT / "sessions" / "session-86"

SESSION = "S86"                                                        # (local)
GATE_ID = "S86-W1C-C29-FOLLOWUP-NS-OF-CSUB-PROMOTION"                  # (local)
SCHEME = "canonical-promotion"                                         # (local)
CONVENTION = "substrate-Mellin-tilt"                                   # (local)
L_MAX_TAG = "N/A"                                                      # (local)

# Pre-registered C29 anchor + tolerance (machinery PRDR pins)
C_SUB_PROBE = 3.647                                                    # (local) C29 §6 Path-C anchor
N_S_C29_RUNTIME = 0.9784607074                                         # (local) WP §W1c-8 Runtime Values table; reproduce-and-compare anchor
PASS_REL_TOL = 1e-12                                                   # (local) float64 effective-equality tolerance

# Output destinations
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

# Inputs that feed the dual-SHA closure
INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(86, 's86_w1c_c29_falsifier_promotion.py'),
    SESSION_DIR / "session-86-w1c-workingpaper.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-SHA pin block (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path,
                     canonical_path: Path,
                     pins: dict) -> tuple:
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

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
# Section 5 — Substitution chain (printed verbatim before any compute)
# ---------------------------------------------------------------------------

def print_substitution_chain():
    print()
    print("=" * 78)
    print("SUBSTITUTION CHAIN — n_s_of_c_sub canonical-promotion cross-check")
    print("=" * 78)
    print()
    print("Step 1 — Definitions (substrate-first; Mellin-cone scheme):")
    print("  c_sub          := M_Pl_eff(k_pivot)^2 / M_Pl_eff(0)^2")
    print("                    [substrate Mellin-weight ratio; eq_166717]")
    print("  eps_eff(c_sub) := eps_baseline * (c_sub_baseline / c_sub)")
    print("                    [Mellin re-weighting at fixed pivot;")
    print("                     1/c_sub at leading Mellin order — C29 §6]")
    print("  n_s(c_sub)     := 1 - 2 * eps_eff(c_sub)")
    print("                  = 1 - 2 * eps_baseline * (c_sub_baseline / c_sub)")
    print("                    [substrate constant-mass spectral-tilt identity;")
    print("                     S43 transfer-function;")
    print("                     S85 W2-as-band-authority.md line 919]")
    print()
    print("  Anchors (from canonical_constants.py — promoted by this gate):")
    print(f"    planck_ns      = {planck_ns!r}")
    print(f"    eps_baseline   = (1 - planck_ns)/2 = {eps_baseline!r}")
    print(f"    c_sub_baseline = {c_sub_baseline!r}  (S78 W2-E central)")
    print()
    print("Step 2 — Substitute c_sub_value = 3.647 (C29 §6 Path-C anchor):")
    print(f"  ratio          = c_sub_baseline / c_sub_value")
    print(f"                 = {c_sub_baseline!r} / {C_SUB_PROBE!r}")
    print(f"                 = {(c_sub_baseline / C_SUB_PROBE)!r}")
    print(f"  eps_eff        = eps_baseline * ratio")
    print(f"                 = {eps_baseline!r} * {(c_sub_baseline / C_SUB_PROBE)!r}")
    print(f"                 = {(eps_baseline * (c_sub_baseline / C_SUB_PROBE))!r}")
    print()
    print("Step 3 — Simplify to canonical form:")
    print("  n_s_promoted   = 1 - 2 * eps_eff")
    n_s_canonical = 1.0 - 2.0 * (eps_baseline * (c_sub_baseline / C_SUB_PROBE))  # (local)
    print(f"                 = 1 - 2 * {(eps_baseline * (c_sub_baseline / C_SUB_PROBE))!r}")
    print(f"                 = {n_s_canonical!r}")
    print()
    print("Step 4 — Direction read off ONLY from canonical |rel_diff| form:")
    print(f"  rel_diff       := |n_s_promoted - N_S_C29_RUNTIME| / |N_S_C29_RUNTIME|")
    print(f"                  = |{n_s_canonical!r} - {N_S_C29_RUNTIME!r}|")
    print(f"                  / |{N_S_C29_RUNTIME!r}|")
    print(f"  PASS iff rel_diff < {PASS_REL_TOL!r} (float64 effective equality)")
    print(f"  FAIL iff rel_diff >= {PASS_REL_TOL!r} (formula drift)")
    print(f"  (sign/direction NOT pre-asserted; computed at runtime below.)")
    print("=" * 78)
    print()


# ---------------------------------------------------------------------------
# Section 6 — Compute (cross-check)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Call the promoted n_s_of_c_sub at c_sub=3.647 and cross-check
    against C29's runtime value 0.9784607074 (WP §W1c-8)."""
    # 1-arg call: uses canonical eps_baseline + c_sub_baseline defaults
    n_s_promoted_1arg = n_s_of_c_sub(C_SUB_PROBE)  # (local)

    # 3-arg call: explicit overrides match C29's positional signature
    n_s_promoted_3arg = n_s_of_c_sub(  # (local)
        C_SUB_PROBE,
        eps_baseline_arg=eps_baseline,
        c_sub_baseline_arg=c_sub_baseline,
    )

    # Direct-formula reproduction (no callable; pure algebra)
    n_s_direct = 1.0 - 2.0 * eps_baseline * (c_sub_baseline / C_SUB_PROBE)  # (local)

    # Cross-check #1: 1-arg vs 3-arg (must be identical-bit)
    diff_1v3 = abs(n_s_promoted_1arg - n_s_promoted_3arg)  # (local)

    # Cross-check #2: callable vs direct algebra (must be identical-bit)
    diff_call_vs_direct = abs(n_s_promoted_1arg - n_s_direct)  # (local)

    # Cross-check #3: callable vs C29 runtime (PASS criterion)
    abs_diff_vs_C29 = abs(n_s_promoted_1arg - N_S_C29_RUNTIME)  # (local)
    rel_diff_vs_C29 = abs_diff_vs_C29 / abs(N_S_C29_RUNTIME)  # (local)

    print()
    print("=" * 78)
    print("CROSS-CHECK RESULTS")
    print("=" * 78)
    print(f"  n_s_promoted (1-arg call)   = {n_s_promoted_1arg!r}")
    print(f"  n_s_promoted (3-arg call)   = {n_s_promoted_3arg!r}")
    print(f"  n_s_direct   (pure algebra) = {n_s_direct!r}")
    print(f"  N_S_C29_RUNTIME (WP §W1c-8) = {N_S_C29_RUNTIME!r}")
    print()
    print(f"  diff (1-arg vs 3-arg)         = {diff_1v3!r}")
    print(f"  diff (callable vs direct)     = {diff_call_vs_direct!r}")
    print(f"  abs_diff (callable vs C29)    = {abs_diff_vs_C29!r}")
    print(f"  rel_diff (callable vs C29)    = {rel_diff_vs_C29!r}")
    print(f"  PASS_REL_TOL                  = {PASS_REL_TOL!r}")
    print("=" * 78)
    print()

    return {
        "value": n_s_promoted_1arg,
        "n_s_promoted_1arg": n_s_promoted_1arg,
        "n_s_promoted_3arg": n_s_promoted_3arg,
        "n_s_direct": n_s_direct,
        "n_s_C29_runtime": N_S_C29_RUNTIME,
        "abs_diff_vs_C29": abs_diff_vs_C29,
        "rel_diff_vs_C29": rel_diff_vs_C29,
        "diff_1v3": diff_1v3,
        "diff_call_vs_direct": diff_call_vs_direct,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate evaluation + verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(rel_diff: float) -> str:
    """Read off PASS/FAIL ONLY from the canonical |rel_diff| form.

    PASS iff rel_diff < PASS_REL_TOL (=1e-12). The threshold corresponds
    to float64 effective equality: the C29 runtime value 0.9784607074
    is published to 10 sig-figs in the WP table; matching to <1e-12
    relative confirms zero-bit drift between the C29 in-script formula
    and the canonical-promoted callable.
    """
    if rel_diff < PASS_REL_TOL:
        return "PASS"
    return "FAIL"


def append_verdict(verdict: str,
                   value: float,
                   audit_sha: str,
                   content_sha: str) -> None:
    """Atomic append (single open('a') write) of canonical line +
    companion dual-SHA short-form comment row, per S84+ schema."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256={content_sha} audit_sha256={audit_sha}\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first part of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Print substitution chain
    print_substitution_chain()

    # 3. Compute cross-checks
    result = compute()
    value = result["value"]
    rel_diff = result["rel_diff_vs_C29"]

    # 4. Evaluate gate
    verdict = evaluate_gate(rel_diff)

    # 5. Emit 4-tuple + append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX_TAG)  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.3f}s) ===")
    if verdict == "PASS":
        print(f"  rel_diff = {rel_diff!r} < {PASS_REL_TOL!r}")
        print(f"  Promoted callable n_s_of_c_sub matches C29 runtime "
              f"to float64 effective equality.")
    else:
        print(f"  rel_diff = {rel_diff!r} >= {PASS_REL_TOL!r}")
        print(f"  Formula DRIFT between C29 in-script formula and "
              f"canonical-promoted callable.")

    # 7. Return 0 always (verdict is data; non-zero exit reserved for
    #    script breakage per .claude/rules/math-scripts.md §"Exit Codes
    #    and Verdict Semantics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
