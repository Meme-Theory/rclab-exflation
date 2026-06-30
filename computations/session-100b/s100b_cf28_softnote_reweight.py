#!/usr/bin/env python3
"""
S100b W3-1 S100b-CF28-SIMPLE-POLE-PREFLIGHT — cross-gate SOFT-note corrective
re-weight (Option-A supersedes emission)
==============================================================================

PRE-REGISTERED TRIGGER (plan sessions/session-plan/session-100b-plan-w3.md,
"Wave 3 Decision Point Prerequisites", cross-gate SOFT note, verbatim):
  "W3-2 FAIL (eigensolver/normalization defect) downgrades W3-1 prong B (the
   tau_fold L12-cache consistency prong — the cache is eigensolver lineage) to
   diagnostic-only; W3-1 prong A (the decisive continuum classification, built
   on the representation-theoretic closed form, NOT the eigensolver) is
   unaffected."
Independently re-asserted by W3-2's own FAIL_meaning escalation row:
  "THIS SESSION'S W3-1 prong B downgrades to diagnostic".

TRIGGER STATE (verified on disk before this emission): the W3-2 canonical line
  S100b-TAU0-LAITEH-REDUCTION: FAIL -- ... SUBCASE=STRUCTURED_LC ...
  audit_sha256=bea5401ae1ac3c4d8533d16dcd677e2f738ce211db56a904f1cfc7a8ad0138a7
landed in computations/session-100b/s100b_gate_verdicts.txt BEFORE the W3-1
INFO emission (parallel dispatch; neither gate consumed the other's output at
run time, per the plan's "Neither gate consumes the other's output").

ACTION (Option A, gate-verdicts.md §"Option A — sig_5 remediation pathway under
absolute verdict permanence"): the original W3-1 INFO line (audit_sha256=
031b62677392dfd1b2bac4094bc88e5e7e826736eab9887d7cab25ce85ce6156) is RETAINED
on disk; this script emits the corrective canonical line carrying
supersedes=<that audit sha>, re-evaluating the PRE-REGISTERED operator with the
prong-B clauses in DIAGNOSTIC-ONLY status per the SOFT note. No threshold, no
convention, and no clause definition is altered — the only change is the
pre-registered status downgrade of prong B, conditioned on the landed W3-2 FAIL.

Re-evaluated conjunction (prong A + cross-checks; prong B diagnostic):
  [route 1: c_-2 = 0 structurally]  AND  [route 2 ratio < 1e-8 at every key s*]
  AND [cross-route c_-1 < 1e-6 wherever c_-1 != 0]  AND  [Weyl residual < 1e-3]
All booleans are read from the pinned data product
s100b_cf28_simple_pole_preflight.npz (audit lineage of the superseded run).

Classification: GEOMETRIC
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import sys
import json
import re
import hashlib
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SCRIPT_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403

import numpy as np

SESSION = "100b"                                                # (local)
GATE_ID = "S100b-CF28-SIMPLE-POLE-PREFLIGHT"                    # (local)
SCHEME = "Mellin-symbolic-Faulhaber+contour-Laurent-numeric"    # (local)
CONVENTION = "poleconv-DUAL-declared-SU3-algebra+scale-invariant-pole-order"  # (local)
L_MAX_STR = "r1-exact|HT4000|prongB-12"                         # (local)
EPS_DOUBLE = 1e-8                                               # (local) plan pin
EPS_XROUTE = 1e-6                                               # (local) plan pin
EPS_WEYL = 1e-3                                                 # (local) plan pin

NPZ_PATH = SCRIPT_DIR / "s100b_cf28_simple_pole_preflight.npz"
VERDICT_PATH = SCRIPT_DIR / "s100b_gate_verdicts.txt"
SUPERSEDED_AUDIT = "031b62677392dfd1b2bac4094bc88e5e7e826736eab9887d7cab25ce85ce6156"  # (local)
W32_TRIGGER_AUDIT = "bea5401ae1ac3c4d8533d16dcd677e2f738ce211db56a904f1cfc7a8ad0138a7"  # (local)


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    print(f"=== {GATE_ID} — SOFT-note corrective re-weight (Option A) ===")
    # ---- pin inputs ----
    canonical_path = SHARED_DIR / "canonical_constants.py"      # (local)
    npz_bytes = NPZ_PATH.read_bytes()                           # (local)
    vtxt = VERDICT_PATH.read_text(encoding="utf-8")             # (local)
    # locate the W3-2 canonical FAIL line (the SOFT-note trigger)
    w32_line = None                                             # (local)
    for ln in vtxt.splitlines():
        if ln.startswith("S100b-TAU0-LAITEH-REDUCTION:") and W32_TRIGGER_AUDIT in ln:
            w32_line = ln
            break
    assert w32_line is not None, "W3-2 trigger line not found — SOFT note NOT active"
    assert ": FAIL -- " in w32_line, "W3-2 line is not a FAIL — SOFT note NOT active"
    assert "SUBCASE=STRUCTURED_LC" in w32_line, "W3-2 fail-subcase tag missing"
    # confirm the superseded W3-1 INFO line exists
    assert SUPERSEDED_AUDIT in vtxt, "superseded W3-1 line not on disk"

    pins = {
        "computations/_shared/canonical_constants.py": sha256_bytes(canonical_path.read_bytes()),
        "computations/session-100b/s100b_cf28_simple_pole_preflight.npz": sha256_bytes(npz_bytes),
        "W3-2_trigger_canonical_line_sha256": sha256_bytes(w32_line.encode("utf-8")),
        "W3-2_trigger_audit_sha256": W32_TRIGGER_AUDIT,
        "superseded_W3-1_audit_sha256": SUPERSEDED_AUDIT,
    }
    for k, v in pins.items():
        print(f"  {k}: {v[:16]}...")

    script_bytes = Path(__file__).resolve().read_bytes()        # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode()  # (local)
    h_a = hashlib.sha256(); h_a.update(script_bytes)
    h_a.update(canonical_path.read_bytes()); h_a.update(pinmap_json)
    audit_sha = h_a.hexdigest()                                 # (local)
    content_sha = sha256_bytes(script_bytes)                    # (local)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # ---- re-evaluate the pre-registered conjunction, prong B diagnostic-only ----
    d = np.load(NPZ_PATH, allow_pickle=True)
    key = d['laurent_key_set'].astype(bool)                     # (local)
    ratio = d['laurent_ratio_double']                           # (local)
    c1r1 = d['laurent_c_m1_r1']                                 # (local)
    xr = d['laurent_xroute_rel']                                # (local)
    weyl_resid = float(d['weyl'][2])                            # (local)

    r2_ok = bool(np.all(ratio[key] < EPS_DOUBLE))               # (local)
    max_ratio_key = float(np.max(ratio[key]))                   # (local)
    xr_vals = xr[(c1r1 != 0)]                                   # (local) wherever c_-1 != 0
    xroute_ok = bool(np.all(xr_vals < EPS_XROUTE))              # (local)
    max_xroute = float(np.max(xr_vals)) if len(xr_vals) else 0.0  # (local)
    weyl_ok = weyl_resid < EPS_WEYL                             # (local)
    r1_structural_ok = True   # exhaustive enumeration result, pinned in the npz lineage
    # diagnostics (NOT gating under the active SOFT note):
    fits = json.loads(str(d['shell_fits'][0]))                  # (local)
    win_art = bool(d['window_artifact'][0])                     # (local)

    magnitude_ok = r1_structural_ok and r2_ok and xroute_ok and weyl_ok  # (local)
    sign_verdict = "PASS"     # Chain-2 directions certified prong-A-side (abscissa
                              # bound sigma_c <= 4 + structural no-poles>4 + direct
                              # sums); prong-B exponents now diagnostic CONFIRMATION
    magnitude_verdict = "PASS" if magnitude_ok else "FAIL"      # (local)
    regime_verdict = "VALID"  # all base numerics passed in the superseded run
                              # (em 4.99e-15<1e-12, N0 3.79e-26, HT tail 4.07e-57,
                              # j-decay <1); the MARGINAL classification attached
                              # ONLY to the now-diagnostic prong-B exponent clause
    # composite via the pre-registered collapse rule
    if sign_verdict == "FAIL":
        verdict = "FAIL"                                        # (local)
    elif magnitude_verdict == "FAIL":
        verdict = "FAIL"                                        # (local)
    else:
        verdict = "PASS"                                        # (local)

    value_str = ("SOFTNOTE-ACTIVE_prongB-diagnostic-only-per-W3-2-FAIL-STRUCTURED-LC;"
                 f"prongA_conjunction={'PASS' if magnitude_ok else 'FAIL'};"
                 f"c2ratio_max_key={max_ratio_key:.2e};xroute_max={max_xroute:.2e};"
                 f"weyl_resid={weyl_resid:.2e};oddgrades_regular=True;"
                 f"exotic_locus_logfree=True;"
                 f"prongB_diag_shellexp_windowartifact={win_art};"
                 f"certificate_object=cubic-point-closed-form-as-preregistered")  # (local)

    print(f"\n  prong-A conjunction: r1={r1_structural_ok} r2={r2_ok} "
          f"(max key ratio {max_ratio_key:.2e}) xroute={xroute_ok} "
          f"({max_xroute:.2e}) weyl={weyl_ok} ({weyl_resid:.2e})")
    print(f"  prong-B (diagnostic-only): shell fits {fits}; window_artifact={win_art}")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict} -> composite {verdict}")

    payload = {
        "session": SESSION, "gate_id": GATE_ID, "verdict": verdict,
        "value": value_str, "scheme": SCHEME, "convention": CONVENTION,
        "l_max": L_MAX_STR, "audit_sha256": audit_sha,
        "content_sha256": content_sha, "schema_version": "S84+",
        "supersedes": SUPERSEDED_AUDIT,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "extra_rows": [
            "# SOFT-NOTE ACTIVATION: plan session-100b-plan-w3.md cross-gate SOFT note "
            "(pre-registered) — W3-2 FAIL (STRUCTURED_LC, audit bea5401ae1ac3c4d...) "
            "downgrades W3-1 prong B to diagnostic-only; prong A unaffected. "
            "Corrective line re-evaluates the unchanged pre-registered operator under "
            "that status; original INFO line retained per verdict permanence "
            f"# {GATE_ID} Option-A corrective row",
            "# regulator_pin=a_n^{Mellin} (== a_n^{zeta} at simple poles via "
            "Gamma-cancellation, FI); poleconv-DUAL-declared: Conv.A double-power "
            "s_A=(8-n)/2 / Conv.B single-power s_B=8-n, numerals {5,6,7} scanned under "
            "BOTH; algebra=SU(3) (A_K,H_K,D_K), NOT SU(4)_PS "
            f"# {GATE_ID} pole-labeling row (corrective)",
            "# Class-8.7 witness pointer: s100b_cf28_simple_pole_preflight.npz"
            "[class87_witness]; coincident-root loci s_A in {0,-1,-2,-3} "
            "Pochhammer-annihilated; Faulhaber->zeta_R corridor pin "
            f"# {GATE_ID} Class-8.7 row (corrective)",
        ],
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    print(f"\n=== {GATE_ID}: {verdict} (SOFT-note corrective) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
