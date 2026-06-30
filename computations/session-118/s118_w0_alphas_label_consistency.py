#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S118 W0-1 CF-S118-HK-ALPHAS-LABEL-CONSISTENCY — SCALE-AND-CHANNEL-TAGGING label-consistency audit
=================================================================================================

Gate: CF-S118-HK-ALPHAS-LABEL-CONSISTENCY ([AUDIT])
Classification: NON-PHONONIC (registry-hygiene / label-consistency audit; the underlying
  alpha_s observables are PHONONIC spectral-moment runnings, the GATE is methodology).

Pre-registered threshold (artifact-existence-with-content; NOT a numerical threshold):
  PART A (determination, numerical cross-check, rel_tol=1e-9):
    implied_ns(alpha_s) = sqrt(1 + alpha_s)   [S50-51 identity alpha_s = n_s^2 - 1]
    Branch A iff implied_ns(alpha_s_inflation_framework) == planck_ns (rel_tol 1e-9)
                 AND alpha_s_pivot_goldstone == 0.0 EXACT.
  PART B (PASS predicate, artifact-existence): the SCALE-AND-CHANNEL-TAGGING disambiguation
    annotation (four-alpha_s cross-link with (scale, channel) tags) is LANDED on the Row #3
    surface of falsifier-master-inventory.md.
  PASS iff (Branch A determined) AND (annotation present + must_contain patterns match).

This gate LEGITIMATELY imports canonical_constants (numerical n_s^2-1 cross-check across the
four alpha_s values) -> it is NOT a pure grep-verifier and takes NO grep-verifier exemption;
canonical_constants.py IS in the audit_sha256 pinmap.

Single-shot AFTER-pattern (build text in memory -> write_atomic_with_fsync -> re-read+verify
-> emit exactly one verdict line) per `.claude/rules/registry-landing.md` §"Bridge-Landing
Script Architecture" + `computations/_bridge_landing_script_template.py`. Surgical
string-insertion designated-writer patch (NOT a bulk append) per `feedback_framework-hygiene.md`.

Sage-verified at plan-freeze (RealField(80)):
  sqrt(1 - 0.08587279)          = 0.95610  (= framework gauge-invariant spectral-geometry n_s)
  sqrt(1 - 0.06896799000000009) = 0.96490  (= planck_ns EXACTLY, rel 4.83e-17 << 1e-9)
  alpha_s_pivot_goldstone       = 0.0 EXACT
=> Branch A: same pivot SCALE, distinct observable CONSTRUCTION.

Provenance: S118 W0-1 plan `sessions/session-plan/session-118-plan-w0.md` §W0-1.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Standard imports + path setup (SHARED_DIR before canonical import)
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import os
import re
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 2 — Canonical constants (legitimate consumer; n_s^2-1 cross-check)
# ---------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    alpha_s_substrate_distance_1,
    alpha_s_inflation_framework,
    alpha_s_pivot_goldstone,
    planck_ns,
)

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration
# ---------------------------------------------------------------------------

SESSION = "S118"                                                       # (local)
GATE_ID = "CF-S118-HK-ALPHAS-LABEL-CONSISTENCY"                        # (local)
SCHEME = "FALSIFIER-INVENTORY-SCALE-CHANNEL-LABEL-AUDIT"               # (local)
CONVENTION = "SCALE-AND-CHANNEL-TAGGING-nsSQ-minus-1-IMPLIED-NS"       # (local)
L_MAX = "N/A"                                                          # (local)

REL_TOL = 1e-9                                                         # (local) publication-precision-floored
NS_SUB_EXPECT = 0.95610                                                # (local) framework gauge-invariant n_s
NS_INFL_EXPECT = 0.96490                                               # (local) = planck_ns

CANONICAL = SHARED_DIR / "canonical_constants.py"
INVENTORY = (PROJECT_ROOT / "sessions" / "framework" / "registry"
             / "falsifier-master-inventory.md")

# Multi-line insertion anchor (unique): the close of the Row #3 augmentation cluster
# (T7-W2-FALS-6) immediately before the Rows #2 + #7 annotation header (L443).
ANCHOR = (
    "- **Status**: registered (READY-TO-INSTALL).\n\n"
    "### Rows #2 + #7 — Annotation: T7-W3-FALS-4 Rank-2 product detector "
    "orthogonality theorem registration (S86 W-3)"
)

# Stable marker used for idempotent re-run detection + verify.
ANNOTATION_MARKER = "Row #3 — Augmentation: S118 W0-1 SCALE-AND-CHANNEL-TAGGING"

# The four-alpha_s SCALE-AND-CHANNEL-TAGGING disambiguation annotation (Branch A).
# Pre-registered numbers; the script asserts the computed implied n_s match (rel_tol 1e-9)
# BEFORE landing.
ANNOTATION = """### Row #3 — Augmentation: S118 W0-1 SCALE-AND-CHANNEL-TAGGING label-consistency annotation (four-α_s cross-link; single-label-conflation guard)

> **Origin**: S118 W0-1 gate `CF-S118-HK-ALPHAS-LABEL-CONSISTENCY` [AUDIT] (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`). A SCALE-AND-CHANNEL-TAGGING label-consistency audit across the four substrate α_s observables, landing a disambiguation annotation so no downstream skim/aggregation collapses the four into one label (the `phononic-framing.md §"Scale-and-channel-tagging for running/tilt observables"` single-label-conflation trap). NO new value (canonical write-order Step 2 N/A — artifact-existence landing mints none); NO substrate-physics status change.

- **Determination (Branch A, Sage-verified at rel_tol 1e-9)**: the four α_s observables are mutually consistent ONLY under explicit (scale, channel) tagging — two of them sit at the SAME pivot SCALE but are DISTINCT observable CONSTRUCTIONS. Implied n_s = √(1+α_s): √(1−0.08587279) = 0.95610 (= framework gauge-invariant spectral-geometry n_s, the substrate/BZ scale) vs √(1−0.06896799) = 0.96490 = planck_ns EXACT (the OBSERVED CMB pivot; rel 4.83e-17 ≪ 1e-9), with alpha_s_pivot_goldstone = 0.0 EXACT.
- **The four-α_s (scale, channel) table** (the cross-link guard):

  | α_s observable | value | SCALE (implied n_s) | CHANNEL / construction | superseded? |
  |:---------------|:------|:--------------------|:-----------------------|:------------|
  | `alpha_s_substrate_distance_1` | −0.08587279 | substrate / BZ (n_s = 0.9561) | Pillar-II Mellin-residue running at substrate-distance s=3, INSIDE the BZ | NO (S92 AH-TR-1) |
  | `alpha_s_inflation_framework` (Row #3 "geometric pivot-local") | −0.06896799 | OBSERVED CMB pivot (n_s = planck_ns = 0.9649) | n_s²−1 algebraic identity@observed-pivot — a DERIVED shadow, NOT a substrate-IS running | **YES — SUPERSEDED-S92** |
  | `alpha_s_pivot_goldstone` | 0.0 (EXACT) | CMB pivot (P_{∇φ}=K⁰) | the substrate's ACTUAL Goldstone-pivot running (W9-2 / S92) | NO |
  | `α_s(primordial)` (Row #12 tilt leg) | ~0 | produced-spectrum / CMB pivot | Pillar-V GGE-relic Mode-Independent-Occupation tilt of the PRODUCED amplitude spectrum (CMB-S4 channel) | NO |

- **The conflation guard**: `alpha_s_inflation_framework = −0.06896799` and `alpha_s_pivot_goldstone = 0.0` share the SAME pivot SCALE (both at n_s = planck_ns), but are DIFFERENT observable CONSTRUCTIONS — the former is the SUPERSEDED-S92 n_s²−1 identity@observed-pivot (a derived algebraic shadow), the latter the substrate's actual Goldstone-pivot running. Which value a CMB detector reads at the pivot is set by `deg(T_{BZ→pivot})` (`phononic-framing.md`). They MUST NOT be collapsed to one label, nor confused with the substrate/BZ-scale `alpha_s_substrate_distance_1 = −0.08587279` (implied n_s = 0.9561, the Pillar-II substrate-distance running) or the Pillar-V Row #12 occupation tilt `α_s(primordial) ~ 0`.
- **Substrate framing (PHONONIC)**: the substrate IS the running — D_K eigenvalue spectrum → spectral-moment running at the substrate distance (`alpha_s_substrate_distance_1`, inside the BZ) AND the Goldstone-pivot running at the CMB pivot (`alpha_s_pivot_goldstone = 0.0`); the lab measures a transport-degree-selected IMAGE of these. The −0.06896799 identity@observed-pivot is a derived algebraic shadow at the observed scale (SUPERSEDED-S92), NOT a substrate-IS running. Direction preserved: substrate → spectral-moment running → transport-degree-selected detector image (no container inversion).
- **Cross-reference**: Row #3 primary cell (`alpha_s_inflation_framework` GEOMETRIC pivot-local) + its augmentations T7-W2-FALS-1 (CMB-S4 σ(α_s)≈2.1e-3 sign-test) / T7-W2-FALS-2 (CMB-HD magnitude+NLO) / T7-W2-FALS-6 (Fairbairn trend); Row #12.compute-S117-W0-ALPHAS-TILT-LANDING (the Pillar-V A_s-leg tilt `α_s(primordial) ~ 0`, which ALREADY carries the reciprocal SCALE-AND-CHANNEL-TAGGING cross-link to Row #3 — the bidirectional link is complete, so NO Row #12 edit is needed: explicit no-edit determination recorded here); `phononic-framing.md §"Scale-and-channel-tagging for running/tilt observables"`; §7 falsifier surface.
- **Provenance**: S118 W0-1 gate `CF-S118-HK-ALPHAS-LABEL-CONSISTENCY` [AUDIT], `scheme=FALSIFIER-INVENTORY-SCALE-CHANNEL-LABEL-AUDIT`, `convention=SCALE-AND-CHANNEL-TAGGING-nsSQ-minus-1-IMPLIED-NS`; verdict line in `computations/session-118/s118_gate_verdicts.txt` (emitted via the `emit_verdict` knowledge-MCP tool); producing/verifier script `computations/session-118/s118_w0_alphas_label_consistency.py` (imports canonical_constants for the n_s²−1 cross-check — NOT a grep-verifier; canonical_constants IS in the audit_sha256 pinmap). Canonical pins consumed: `alpha_s_substrate_distance_1 = -0.08587279` (S92), `alpha_s_inflation_framework = -0.06896799` (S85, SUPERSEDED-S92), `alpha_s_pivot_goldstone = 0.0` (S92), `planck_ns = 0.9649`. NO new canonical value (Step 2 N/A — artifact-existence landing mints none). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole writer for `falsifier-master-inventory.md` (AMRI-PROMOTED 2026-04-28).
- **Status**: registered (S118 W0-1 label-consistency annotation; Branch A — same pivot SCALE, distinct observable CONSTRUCTION)."""


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Determination (numerical cross-check)
# ---------------------------------------------------------------------------
def implied_ns(alpha_s: float) -> float:
    return math.sqrt(1.0 + alpha_s)  # (local)


def determine_branch() -> dict:
    ns_sub = implied_ns(alpha_s_substrate_distance_1)            # (local) -> 0.95610
    ns_infl = implied_ns(alpha_s_inflation_framework)           # (local) -> 0.96490
    rel_infl_vs_planck = abs(ns_infl - planck_ns) / planck_ns   # (local)
    rel_sub_vs_9561 = abs(ns_sub - NS_SUB_EXPECT) / NS_SUB_EXPECT  # (local)
    rel_infl_vs_expect = abs(ns_infl - NS_INFL_EXPECT) / NS_INFL_EXPECT  # (local)
    sub_distinct_from_planck = abs(ns_sub - planck_ns) / planck_ns > 1e-3  # (local)
    gold_zero = (alpha_s_pivot_goldstone == 0.0)                # (local)
    branch_A = bool(
        (rel_infl_vs_planck < REL_TOL)
        and gold_zero
        and sub_distinct_from_planck
        and (rel_sub_vs_9561 < 1e-4)
        and (rel_infl_vs_expect < REL_TOL)
    )
    return {
        "ns_sub": ns_sub,
        "ns_infl": ns_infl,
        "rel_infl_vs_planck": rel_infl_vs_planck,
        "rel_sub_vs_9561": rel_sub_vs_9561,
        "sub_distinct_from_planck": sub_distinct_from_planck,
        "gold_zero": gold_zero,
        "branch_A": branch_A,
    }


# ---------------------------------------------------------------------------
# Section 6 — Single-shot landing (build -> write_atomic_with_fsync -> verify)
# ---------------------------------------------------------------------------
def build_patched_text(original: str) -> tuple[str, bool]:
    """Return (new_full_text, inserted_now). Idempotent: if the annotation marker
    is already present, return the original unchanged (inserted_now=False)."""
    if ANNOTATION_MARKER in original:
        return original, False
    if original.count(ANCHOR) != 1:
        raise RuntimeError(
            f"insertion anchor not unique (count={original.count(ANCHOR)}); refusing to patch")
    head, sep, tail = ANCHOR.partition(
        "\n\n### Rows #2 + #7 — Annotation: T7-W3-FALS-4")
    # head == "- **Status**: registered (READY-TO-INSTALL)."
    replacement = head + "\n\n" + ANNOTATION + sep + tail
    new_text = original.replace(ANCHOR, replacement, 1)
    return new_text, True


def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


def verify_landed(text: str) -> dict:
    marker_ok = ANNOTATION_MARKER in text                       # (local)
    block_ok = ANNOTATION in text                               # (local)
    mc1 = re.search(
        r"(SCALE-AND-CHANNEL-TAGGING|scale-and-channel|identity@observed-pivot"
        r"|labels mutually consistent)", text) is not None      # (local)
    mc2 = re.search(
        r"(planck_ns|0\.9649|0\.9561|alpha_s_pivot_goldstone)", text) is not None  # (local)
    anchor_consumed_once = text.count(ANNOTATION_MARKER) == 1    # (local)
    return {
        "marker_ok": marker_ok,
        "block_ok": block_ok,
        "must_contain_1": mc1,
        "must_contain_2": mc2,
        "anchor_consumed_once": anchor_consumed_once,
        "all_ok": bool(marker_ok and block_ok and mc1 and mc2 and anchor_consumed_once),
    }


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "") -> dict:
    payload: dict = {
        "session": 118,
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
    if companion_note:
        payload["companion_note"] = companion_note
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    print(f"  canonical_constants.py: {sha256_of(CANONICAL)[:16]}...")
    print(f"  falsifier-master-inventory.md (pre): {sha256_of(INVENTORY)[:16]}...")
    print()

    # PART A — determination (numerical n_s^2-1 cross-check)
    det = determine_branch()
    print("--- PART A: determination (implied n_s = sqrt(1 + alpha_s)) ---")
    print(f"  alpha_s_substrate_distance_1 = {alpha_s_substrate_distance_1}  -> implied n_s = {det['ns_sub']:.6f}  (substrate/BZ scale)")
    print(f"  alpha_s_inflation_framework  = {alpha_s_inflation_framework}  -> implied n_s = {det['ns_infl']:.6f}  (=planck_ns? rel={det['rel_infl_vs_planck']:.2e})")
    print(f"  alpha_s_pivot_goldstone      = {alpha_s_pivot_goldstone}  (==0.0 EXACT: {det['gold_zero']})")
    print(f"  planck_ns                    = {planck_ns}")
    print(f"  ns_sub distinct from planck_ns: {det['sub_distinct_from_planck']}")
    print(f"  => Branch A (same pivot SCALE, distinct observable CONSTRUCTION): {det['branch_A']}")
    print()

    if not det["branch_A"]:
        # The pre-registered determination failed -> INFO (a third scale surfaced or a
        # canonical drifted). Route to Q1 workshop per the plan INFO rubric. Do NOT land.
        audit_sha = sha256_text(
            sha256_of(Path(__file__).resolve()) + sha256_of(CANONICAL)
            + json.dumps({"determination": det, "branch_A": False}, sort_keys=True,
                         default=str))
        content_sha = sha256_text("INFO:determination-not-Branch-A:" + json.dumps(det, sort_keys=True, default=str))
        val = (f"determination_not_Branch_A_rel_infl={det['rel_infl_vs_planck']:.2e}_"
               f"gold_zero={det['gold_zero']}_NO_LANDING")
        print_verdict_payload("INFO", val, audit_sha, content_sha,
                              companion_note="S118 W0-1 INFO: implied-n_s determination did not resolve to Branch A; Q1-workshop route per plan §W0-1 INFO rubric")
        print(f"\n=== {GATE_ID}: INFO (wall {time.time()-t0:.2f}s) ===")
        return 0

    # PART B — single-shot landing (build -> write+fsync -> re-read+verify)
    original = INVENTORY.read_text(encoding="utf-8")
    new_text, inserted_now = build_patched_text(original)
    if inserted_now:
        write_atomic_with_fsync(new_text, INVENTORY)
        print("--- PART B: annotation INSERTED (surgical, single-shot) ---")
    else:
        print("--- PART B: annotation ALREADY PRESENT (idempotent no-op) ---")

    landed = INVENTORY.read_text(encoding="utf-8")  # final re-read (post-fsync)
    vr = verify_landed(landed)
    print(f"  verify: {vr}")
    print()

    verdict = "PASS" if vr["all_ok"] else "FAIL"

    # Dual-SHA: audit over (script || canonical || pinmap); content over the landed annotation text.
    script_path = Path(__file__).resolve()
    pins = {
        str(CANONICAL.relative_to(PROJECT_ROOT)).replace("\\", "/"): sha256_of(CANONICAL),
        str(INVENTORY.relative_to(PROJECT_ROOT)).replace("\\", "/"): sha256_of(INVENTORY),
    }
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_path.read_bytes())
    h_audit.update(CANONICAL.read_bytes())
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()                 # (local)
    content_sha = sha256_text(ANNOTATION)           # (local) patched-section text

    value = ("artifact-exists(Row#3 SCALE-AND-CHANNEL-TAGGING four-alpha_s annotation); "
             "Branch_A=True; ns_sub=0.95610(BZ) ns_infl=0.96490=planck_ns; "
             "alpha_s_inflation_framework SUPERSEDED-S92 identity@observed-pivot; "
             "Row#12 reciprocal cross-link present (no Row#12 edit needed)")
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(verdict, value, audit_sha, content_sha)
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time()-t0:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
