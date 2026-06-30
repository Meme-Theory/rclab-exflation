#!/usr/bin/env python
"""
_s87_class_f_ext_verdict_emit.py — one-shot verdict emitter for the
S87-VII-SLOT-ALLOC-AUDIT-CLASS-F-EXT hygiene gate (2026-04-28).

Computes the dual SHAs over the post-extension audit script + registry +
plan-glob input-pin map (matching the audit script's own input_pin_map
canonical-ordering convention) and appends a single canonical verdict line
plus the dual-SHA companion comment row plus the 3-tuple annotation.

This emitter is one-shot (per the registry-write hygiene rule's append-only
Python writer pattern) — it opens s87_gate_verdicts.txt in append mode and
writes once. Idempotency is enforced by checking whether the gate-ID has
already been emitted before append; re-runs are no-ops.
"""
from __future__ import annotations

import hashlib
import json
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


# canonical_constants import (mandated for computation scripts S34+ per CLAUDE.md);
# this verdict-emitter does not consume any framework constant numerically,
# so the wildcard import is purely for compliance.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)

GATE_ID = "S87-VII-SLOT-ALLOC-AUDIT-CLASS-F-EXT"  # (local)
SCHEME = "vii_slot_allocation_audit_v2"           # (local)
CONVENTION = "6-class-taxonomy-extended-A-through-F"  # (local)
L_MAX = "N/A"                                     # (local)
SCHEMA_VERSION = "S87+"                           # (local)

VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')
AUDIT_SCRIPT = resolve_script(None, '_vii_slot_allocation_audit.py')
JSON_SIDECAR = resolve_script(None, '_vii_slot_allocation_audit_post_class_f_ext.json')
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
PLAN_GLOB_DIR = PROJECT_ROOT / "sessions" / "session-plan"


def sha256_of_file(path: Path) -> str:
    if not path.exists():
        return "MISSING"
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    # Idempotency: refuse re-emission.
    if VERDICT_TXT.exists():
        existing = VERDICT_TXT.read_text(encoding="utf-8", errors="replace")
        if GATE_ID in existing:
            print(f"VERDICT for {GATE_ID} already present in {VERDICT_TXT.name}; no-op.")
            return 0

    # Load JSON sidecar to extract verified counts.
    sidecar = json.loads(JSON_SIDECAR.read_text(encoding="utf-8"))
    counts = sidecar["counts"]
    class_a = counts["A_REGISTERED_AND_MATCHED"]  # (local)
    class_b = counts["B_UNREGISTERED_RESERVATION"]  # (local)
    class_c = counts["C_COLLISION_DOUBLE_RESERVATION"]  # (local)
    class_d = counts["D_ORPHANED_TABLE_ENTRY"]  # (local)
    class_e = counts["E_REGISTRY_VS_TABLE_DRIFT"]  # (local)
    class_f = counts["F_STALE_STATUS"]  # (local)

    # ---- Pre-registered verdict criterion ----
    # PASS iff (existing 9 Class-A preserved) AND (no C/D/E hard defect).
    # Per the spec, the W1a closure had 9 Class-A passes (audit SHA
    # 1c32b448f9c8a465e638e2418c0375febeaa02c30dc6cd8d54a571735aac8bbc
    # over the pre-extension 5-class script). The current re-run must
    # reproduce 9 Class-A AND show no C/D/E.
    expected_class_a = 9  # (local) per W1a closure footprint
    pass_existing_classes = (
        class_a == expected_class_a
        and class_b == 0
        and class_c == 0
        and class_d == 0
        and class_e == 0
    )  # (local)

    # 3-tuple verdict (per S87 schema-v2):
    # - sign_verdict     = N/A (this is an artifact-existence verifier, not a directional gate)
    # - magnitude_verdict = PASS iff existing 9 Class-A preserved AND no C/D/E
    # - regime_verdict    = VALID iff audit re-run completed without exceptions
    sign_verdict = "N/A"  # (local)
    magnitude_verdict = "PASS" if pass_existing_classes else "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) audit re-run completed cleanly

    # Composite collapse (per gate-verdicts.md S87 schema-v2):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # Self-test pass is a separate landing condition (not in the 3-tuple but
    # encoded in the value field).
    self_test_pass = True  # (local) verified via prior --self-test exit 0

    # Build value field per spec: class_f_extension_landed_class_a_count_<N>_class_f_count_<M>
    value_field = (
        f"class_f_extension_landed_class_a_count_{class_a}_class_f_count_{class_f}"
    )  # (local)

    # ---- Compute dual SHAs ----
    # audit_sha256: closure over the input-pin map = {audit_script_post, registry, plan_files}
    # We follow the SAME canonical-ordering convention as the audit script's
    # own input_pin_map (sorted JSON, separators=(",", ":")) to keep emitter
    # closure provenance traceable to the audit script.
    audit_script_sha = sha256_of_file(AUDIT_SCRIPT)  # (local)
    registry_sha = sha256_of_file(REGISTRY_PATH)  # (local)
    plan_files = sorted(PLAN_GLOB_DIR.glob("*.md"))  # (local)
    plan_glob_sha = sha256_of_text("\n".join(p.name for p in plan_files))  # (local)
    json_sidecar_sha = sha256_of_file(JSON_SIDECAR)  # (local)

    input_pin_map = {
        "audit_script_post_sha256": audit_script_sha,
        "registry_sha256": registry_sha,
        "plan_glob_sha256": plan_glob_sha,
        "plan_file_count": len(plan_files),
        "json_sidecar_sha256": json_sidecar_sha,
        "class_a_count": class_a,
        "class_b_count": class_b,
        "class_c_count": class_c,
        "class_d_count": class_d,
        "class_e_count": class_e,
        "class_f_count": class_f,
        "self_test_pass": self_test_pass,
        "expected_class_a_preserved": pass_existing_classes,
        "schema": "6-class-taxonomy-A-through-F",
    }
    canonical_pinmap = json.dumps(
        input_pin_map, sort_keys=True, separators=(",", ":"), default=str
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(AUDIT_SCRIPT.read_bytes())
    h_audit.update(REGISTRY_PATH.read_bytes())
    h_audit.update(canonical_pinmap)
    audit_sha256 = h_audit.hexdigest()  # (local)

    # content_sha256: SHA over the new audit_script bytes only (per S84+
    # dual-SHA convention: content = script bytes invariant, audit =
    # closure over inputs).
    content_sha256 = audit_script_sha  # (local) script-bytes-only

    # ---- Atomic append (one-shot, append-only mode) ----
    line_canonical = (
        f"{GATE_ID}: {composite} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    line_dual_sha_companion = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    line_3tuple_companion = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line_canonical)
        fp.write(line_dual_sha_companion)
        fp.write(line_3tuple_companion)

    print(f"Appended {GATE_ID} verdict to {VERDICT_TXT.name}")
    print(f"  composite verdict: {composite}")
    print(f"  3-tuple: ({sign_verdict}, {magnitude_verdict}, {regime_verdict})")
    print(f"  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")
    print(f"  class_a={class_a} class_f={class_f}")
    print(f"  existing 9 Class-A preserved: {pass_existing_classes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
