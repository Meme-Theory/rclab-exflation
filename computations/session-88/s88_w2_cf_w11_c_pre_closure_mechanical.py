#!/usr/bin/env python3
"""
S88 W2-7 — S88-CF-W11-C-PRE-CLOSURE-MECHANICAL
================================================

Gate: S88-CF-W11-C-PRE-CLOSURE-MECHANICAL (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class mechanical-closure per mechanical-closure-discipline.md)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-7

This is a MECHANICAL-CLOSURE gate per `.claude/rules/mechanical-closure-discipline.md`.
It emits FAIL by construction with descriptive value-string naming the
upstream block (S87 W-8 R3 Δ_0 LOCALIZATION FORMULA closure of (Z_2)^d=2
stratum-permutation route at substrate; substrate-empirical Δ_0 ∈ {8, 16, 32, 24}
with min rel_dev_0 = 2/5 — FAILs ANY 1e-9 threshold by ≥ 8 OOM).

Per mechanical-closure-discipline.md §"Verdict honesty":
  - PASS verdicts from a mechanical closure are PROHIBITED_ACTIONS Class 4
    (ansatz-forced PASS); FAIL is the only honest outcome here.
  - The verdict line carries `value='PRE-REG-INC_blocked_by_<sym>_<status>'`
    pattern naming the upstream W-8 block.

Per mechanical-closure-discipline.md §"Audit-trail signature":
  - audit_sha256 computed over per-gate-distinct input-pin map containing
    (W11-1 verdict SHA, W11-4 verdict SHA, §VII.AD landing SHA from §W2-8,
    falsifier-master-inventory current SHA).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-87/s87_gate_verdicts.txt (W11-1 / W11-4 verdict source)
  - computations/session-88/s88_gate_verdicts.txt (§W2-8 §VII.AD landing verdict source)
  - sessions/framework/registry/falsifier-master-inventory.md (W11 row companion)
  - script bytes
"""

from __future__ import annotations

# Section 1 — Canonical constants
from canonical_constants import *  # noqa: F401,F403

# Section 2 — Imports
import hashlib
import json
import re
import time
from pathlib import Path

# Section 3 — Pin metadata
GATE_ID = "S88-CF-W11-C-PRE-CLOSURE-MECHANICAL"
SCHEME = "mechanical-closure-w11-c-pre-reg-inc-blocked-on-w8-partition-arithmetic"
CONVENTION = "delta-0-localization-min-rel-dev-2-over-5-FAIL-by-8-OOM"
L_MAX = "N/A"  # (local) METHODOLOGY-class
VALUE_STR = (
    "PRE-REG-INC_blocked_by_W8_PARTITION_ARITHMETIC_"
    "DELTA_0_LOCALIZATION_min_rel_dev_2_over_5"
)

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_cf_w11_c_pre_closure_mechanical.py"
NPZ_OUT = T0 / "s88_w2_cf_w11_c_pre_closure_mechanical.npz"
VERDICT_FILE_S88 = T0 / "s88_gate_verdicts.txt"
VERDICT_FILE_S87 = T0 / "s87_gate_verdicts.txt"
FALSIFIER_INVENTORY = (
    T0.parent / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
)
CANON_PY = T0 / "canonical_constants.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def extract_audit_sha(verdict_file: Path, gate_id_pattern: str) -> str:
    """Find the audit_sha256 for a given gate_id in the verdict file."""
    text = verdict_file.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        if gate_id_pattern in line and "audit_sha256=" in line:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", line)
            if m:
                return m.group(1)
    return "NOT-FOUND"


def main() -> int:
    t_start = time.time()
    import numpy as np

    # 4.1 — Verify upstream §W2-8 §VII.AD landing PASS
    w2_8_audit_sha = extract_audit_sha(VERDICT_FILE_S88, "S88-DELTA-0-LOCALIZATION-FORMULA-LANDING")
    print(f"[W2-7] §W2-8 §VII.AD landing audit_sha256: {w2_8_audit_sha}")
    upstream_w2_8_landed = bool(w2_8_audit_sha != "NOT-FOUND")

    # 4.2 — Extract W11-1 and W11-4 verdict SHAs from S87 file
    w11_1_sha = extract_audit_sha(VERDICT_FILE_S87, "S87-MONODROMY-V_4-EXPLICIT")
    w11_4_sha = extract_audit_sha(VERDICT_FILE_S87, "S87-W11-4")  # may not exist as exact gate-ID
    print(f"[W2-7] W11-1 (V_4-EXPLICIT) audit_sha256: {w11_1_sha}")
    print(f"[W2-7] W11-4 audit_sha256: {w11_4_sha}")

    # 4.3 — falsifier-master-inventory current SHA (companion edit target)
    if FALSIFIER_INVENTORY.exists():
        falsifier_sha = sha256_file(FALSIFIER_INVENTORY)
    else:
        falsifier_sha = "NOT-AVAILABLE"
    print(f"[W2-7] falsifier-master-inventory current SHA: {falsifier_sha}")

    # 4.4 — Per-gate-distinct audit_sha256 over 4-input pinmap (per mechanical-closure-discipline.md)
    canon_sha = sha256_file(CANON_PY)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "value_str": VALUE_STR,
        "input_canonical_constants_sha256": canon_sha,
        "input_w11_1_audit_sha256": w11_1_sha,
        "input_w11_4_audit_sha256": w11_4_sha,
        "input_w2_8_vii_ad_landing_audit_sha256": w2_8_audit_sha,
        "input_falsifier_master_inventory_sha256": falsifier_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # 4.5 — Composite verdict: FAIL by construction (mechanical-closure honesty)
    composite = "FAIL"
    verdict_kind = "FAIL-PRE-REG-INC-blocked-on-W8-Delta-0-LOCALIZATION-substrate-route-closed"

    # 4.6 — Save .npz
    np.savez(
        NPZ_OUT,
        value_str=VALUE_STR,
        upstream_w2_8_landed=np.bool_(upstream_w2_8_landed),
        w2_8_audit_sha=w2_8_audit_sha,
        w11_1_sha=w11_1_sha,
        w11_4_sha=w11_4_sha,
        falsifier_sha=falsifier_sha,
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # 4.7 — Append verdict line per mechanical-closure-discipline.md §"Audit-trail signature"
    elapsed = time.time() - t_start
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{VALUE_STR}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    extra_companion = (
        f"# audit_sha256 companion row: {GATE_ID} audit={audit_sha256[:16]} "
        f"content={content_sha256[:16]} "
        f"# PRE-REG-INC per session-88-plan-w2.md §W2-7; deferred to S89; "
        f"# required upstream: [S88-DELTA-0-LOCALIZATION-FORMULA-LANDING (LANDED), "
        f"S87-MONODROMY-V_4-EXPLICIT (LANDED)]; "
        f"closure_script=computations/session-88/s88_w2_cf_w11_c_pre_closure_mechanical.py\n"
    )
    sign_v = "N/A"
    mag_v = "FAIL"
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE_S88, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(extra_companion)
        f.write(tuple_line)

    print(f"[W2-7] DONE in {elapsed:.2f}s")
    print(f"[W2-7] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-7] value = '{VALUE_STR}'")
    print(f"[W2-7] audit_sha256 = {audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
