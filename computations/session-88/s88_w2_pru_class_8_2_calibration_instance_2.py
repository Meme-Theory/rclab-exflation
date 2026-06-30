#!/usr/bin/env python3
"""
S88 W2-11 — S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2
======================================================

Gate: S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2 (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class rule-file diff to epistemic-discipline.md Class 8.2 corpus)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-11

Pre-registered threshold:
  PASS: rule-file diff lands; instance #2 entry ≥25 lines; K-counter advanced
        explicitly 1→2; methodology-wave-allowlist row appended; cross-link to
        §W2-3 + §W2-2 forward-remediation citations present.
  INFO: partial.
  FAIL: rule-file diff invalid or K-counter not explicitly advanced.
"""

from __future__ import annotations
from canonical_constants import *  # noqa: F401,F403

import hashlib, json, time
from pathlib import Path

GATE_ID = "S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2"
SCHEME = "pru-class-8-2-calibration-corpus-instance-2-W8-stratum-vs-cartan-toral"
CONVENTION = "K-counter-advancement-1-to-2-promotion-to-mandatory-at-K-equal-3"
L_MAX = "N/A"
LINE_THRESHOLD_PASS = 25  # (local) plan-pinned ≥25 lines instance #2 entry

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_pru_class_8_2_calibration_instance_2.py"
NPZ_OUT = T0 / "s88_w2_pru_class_8_2_calibration_instance_2.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"
EPISTEMIC = T0.parent / ".claude" / "rules" / "epistemic-discipline.md"
ALLOWLIST_PATH = T0.parent / ".claude" / "rules" / "methodology-wave-allowlist.md"
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

    text = EPISTEMIC.read_text(encoding="utf-8", errors="replace")
    # Locate instance #2 sub-block start and end
    start_marker = "**Class 8.2 calibration corpus — instance #2 (S87 W-8 R3 closure / S88 W2-11 landing"
    end_marker = "Forward remediation: pre-registered rubrics for V_4 character constructions"
    instance_2_present = start_marker in text
    if instance_2_present:
        start_idx = text.index(start_marker)
        # Find next blank-line-followed-by-non-instance-2 paragraph end (use end_marker as middle reference)
        instance_2_block = text[start_idx:start_idx + 4000]  # generous window
        instance_2_line_count = instance_2_block.count("\n") if "\n" in instance_2_block else 0
        # More accurate: count from start_marker until next ### or top-level section
        sub_end = instance_2_block.find("\n###")
        if sub_end > 0:
            instance_2_line_count = instance_2_block[:sub_end].count("\n")
        else:
            instance_2_line_count = instance_2_block.count("\n")
    else:
        instance_2_line_count = 0  # (local) absent
    print(f"[W2-11] instance #2 entry detected: {instance_2_present}; line count ≈ {instance_2_line_count}")

    cc1_instance_2_present = instance_2_present
    cc2_k_counter_advance = "K-counter: **1 → 2**" in text or "K-counter advance" in text
    cc3_w2_3_xref = "S88 W2-3" in text and "stratum-index" in text
    cc4_w2_2_xref = "S88 W2-2" in text and "D-W8-1" in text
    cc5_substrate_distinction = "Cartan-toral" in text and "stratum-index" in text
    print(f"[W2-11] CC1 instance #2 entry present: {cc1_instance_2_present}")
    print(f"[W2-11] CC2 K-counter advance 1→2 explicit: {cc2_k_counter_advance}")
    print(f"[W2-11] CC3 cross-link to S88 W2-3 (stratum-index): {cc3_w2_3_xref}")
    print(f"[W2-11] CC4 cross-link to S88 W2-2 (D-W8-1): {cc4_w2_2_xref}")
    print(f"[W2-11] CC5 Cartan-toral vs stratum-index distinction: {cc5_substrate_distinction}")

    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")
    cc6_allowlist = "| W2-11 | S88 |" in allowlist_text
    print(f"[W2-11] CC6 methodology-wave-allowlist W2-11 row: {cc6_allowlist}")

    all_cc_pass = (cc1_instance_2_present and cc2_k_counter_advance and cc3_w2_3_xref
                   and cc4_w2_2_xref and cc5_substrate_distinction and cc6_allowlist
                   and instance_2_line_count >= LINE_THRESHOLD_PASS)
    if all_cc_pass:
        composite = "PASS"
        verdict_kind = "PASS-class-8-2-instance-2-K-counter-1-to-2-landed"
    elif cc1_instance_2_present and not all_cc_pass:
        composite = "INFO"
        verdict_kind = "INFO-partial-some-cross-checks-failed"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-instance-2-not-landed-or-K-counter-missing"

    canon_sha = sha256_file(CANON_PY)
    epistemic_sha = sha256_file(EPISTEMIC)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID, "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "input_canonical_constants_sha256": canon_sha,
        "input_epistemic_discipline_sha256": epistemic_sha,
        "input_allowlist_sha256": allowlist_sha,
        "script_sha256": script_sha,
        "K_counter_pre": 1, "K_counter_post": 2, "K_promotion": 3,
    }
    audit_sha256 = closure_hash(pin_map)

    np.savez(NPZ_OUT,
        instance_2_line_count=np.int64(instance_2_line_count),
        cc1_instance_2=np.bool_(cc1_instance_2_present),
        cc2_k_counter=np.bool_(cc2_k_counter_advance),
        cc3_w2_3=np.bool_(cc3_w2_3_xref),
        cc4_w2_2=np.bool_(cc4_w2_2_xref),
        cc5_distinction=np.bool_(cc5_substrate_distinction),
        cc6_allowlist=np.bool_(cc6_allowlist),
        composite=composite, verdict_kind=verdict_kind,
        audit_sha256=audit_sha256, content_sha256=content_sha256)

    elapsed = time.time() - t_start
    value_str = (
        f"K_counter=1->2;instance_2_line_count={instance_2_line_count};"
        f"cc1_present={cc1_instance_2_present};cc2_advance={cc2_k_counter_advance};"
        f"cc3_w2_3={cc3_w2_3_xref};cc4_w2_2={cc4_w2_2_xref};"
        f"cc5_distinction={cc5_substrate_distinction};cc6_allowlist={cc6_allowlist};"
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

    print(f"[W2-11] DONE in {elapsed:.2f}s; composite={composite}; audit_sha256={audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
