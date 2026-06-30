#!/usr/bin/env python3
"""
S88 W2-12 — S88-METH-CROSS-PILLAR-BRIDGE-ANATOMY-K-COUNTER-MONITOR
==================================================================

Gate: S88-METH-CROSS-PILLAR-BRIDGE-ANATOMY-K-COUNTER-MONITOR (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class K-counter bookkeeping)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-12

Pre-registered threshold (per session-88-plan-w2.md §W2-12.9):
  PASS: K reaches 3 during S88; rule-file auto-flip triggered AND landed in same
        dispatch; methodology-wave-allowlist row appended.
  INFO: K reaches 2 → 2 (no S88 landings) OR K reaches 2 → 3 but rule-file flip
        deferred (BLOCKED).
  FAIL: K reaches 3 but rule-file flip NOT triggered (rule-file violation).

K-counter pre-S88: 2 (S86 W-5 §VII.AF.1 + S87 W11-5 FWD-C3 REGISTRY-FAIL).
S88 forward-bridge candidates: FWD-C1 (#21), FWD-C2 (#22), FWD-C3 (#23).
"""

from __future__ import annotations
from canonical_constants import *  # noqa: F401,F403

import hashlib, json, time, re
from pathlib import Path

GATE_ID = "S88-METH-CROSS-PILLAR-BRIDGE-ANATOMY-K-COUNTER-MONITOR"
SCHEME = "cross-pillar-bridge-anatomy-K-counter-monitor-S88"
CONVENTION = "auto-flip-SUGGESTION-to-MANDATORY-on-third-instance-landing"
L_MAX = "N/A"
K_PRE_S88 = 2     # (local) S86 W-5 + S87 W11-5
K_PROMOTION = 3   # (local)

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_meth_cross_pillar_bridge_anatomy_k_counter_monitor.py"
NPZ_OUT = T0 / "s88_w2_meth_cross_pillar_bridge_anatomy_k_counter_monitor.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"
CROSS_PILLAR_RULE = T0.parent / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
CANON_PY = T0 / "canonical_constants.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    return hashlib.sha256(json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> int:
    t_start = time.time()
    import numpy as np

    # 4.1 — Scan S88 verdict file for forward-bridge landings
    verdict_text = VERDICT_FILE.read_text(encoding="utf-8", errors="replace")
    fwd_c1_landings = len(re.findall(r"S88-FWD-C1[^:]*:\s*PASS", verdict_text))
    fwd_c2_landings = len(re.findall(r"S88-FWD-C2[^:]*:\s*PASS", verdict_text))
    fwd_c3_landings = len(re.findall(r"S88-FWD-C3[^:]*:\s*PASS", verdict_text))
    new_landings = fwd_c1_landings + fwd_c2_landings + fwd_c3_landings
    K_post_S88 = K_PRE_S88 + new_landings
    print(f"[W2-12] FWD-C1/C2/C3 landings during S88: C1={fwd_c1_landings}, C2={fwd_c2_landings}, C3={fwd_c3_landings}; total new = {new_landings}")
    print(f"[W2-12] K-counter pre-S88 = {K_PRE_S88}; K-counter post-S88 = {K_post_S88}")

    # 4.2 — Determine flip status
    if K_post_S88 >= K_PROMOTION:
        rule_flip_required = True
        # Check if rule-file flip has been triggered
        rule_text = CROSS_PILLAR_RULE.read_text(encoding="utf-8", errors="replace")
        rule_flip_landed = "Status: MANDATORY at K=3" in rule_text or "K = 3 ⇒  status = **MANDATORY**" in rule_text
    else:
        rule_flip_required = False
        rule_flip_landed = False

    print(f"[W2-12] Rule-file flip required: {rule_flip_required}; landed: {rule_flip_landed}")

    # 4.3 — Composite verdict per plan §W2-12.9
    if K_post_S88 >= K_PROMOTION and rule_flip_landed:
        composite = "PASS"
        verdict_kind = "PASS-K-3-reached-and-rule-file-flipped"
    elif K_post_S88 >= K_PROMOTION and not rule_flip_landed:
        composite = "FAIL"
        verdict_kind = "FAIL-K-3-reached-but-rule-file-flip-not-triggered"
    elif K_post_S88 == K_PRE_S88:
        composite = "INFO"
        verdict_kind = "INFO-K-2-status-holding-no-S88-forward-bridge-landings"
    else:
        composite = "INFO"
        verdict_kind = "INFO-K-counter-advance-not-yet-at-promotion-threshold"

    canon_sha = sha256_file(CANON_PY)
    rule_sha = sha256_file(CROSS_PILLAR_RULE)
    verdict_sha = sha256_file(VERDICT_FILE)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID, "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "K_pre_S88": K_PRE_S88, "K_promotion": K_PROMOTION,
        "fwd_c1_landings": fwd_c1_landings, "fwd_c2_landings": fwd_c2_landings, "fwd_c3_landings": fwd_c3_landings,
        "K_post_S88": K_post_S88,
        "input_canonical_constants_sha256": canon_sha,
        "input_cross_pillar_rule_sha256": rule_sha,
        "input_verdict_file_sha256": verdict_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    np.savez(NPZ_OUT,
        K_pre_S88=np.int64(K_PRE_S88),
        K_post_S88=np.int64(K_post_S88),
        K_promotion=np.int64(K_PROMOTION),
        fwd_c1_landings=np.int64(fwd_c1_landings),
        fwd_c2_landings=np.int64(fwd_c2_landings),
        fwd_c3_landings=np.int64(fwd_c3_landings),
        rule_flip_required=np.bool_(rule_flip_required),
        rule_flip_landed=np.bool_(rule_flip_landed),
        composite=composite, verdict_kind=verdict_kind,
        audit_sha256=audit_sha256, content_sha256=content_sha256)

    elapsed = time.time() - t_start
    value_str = (
        f"K_post_S88={K_post_S88};K_pre_S88={K_PRE_S88};K_promotion={K_PROMOTION};"
        f"fwd_c1={fwd_c1_landings};fwd_c2={fwd_c2_landings};fwd_c3={fwd_c3_landings};"
        f"rule_flip_required={rule_flip_required};rule_flip_landed={rule_flip_landed};"
        f"verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} # {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    tuple_line = f"# sign_verdict=N/A magnitude_verdict={composite} regime_verdict=VALID # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line); f.write(companion_line); f.write(tuple_line)

    print(f"[W2-12] DONE in {elapsed:.2f}s; composite={composite}; audit_sha256={audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
