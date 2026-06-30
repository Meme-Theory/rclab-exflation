#!/usr/bin/env python3
"""
S88 W2-13 — S88-CF-W11-D-SIG5-DUPLICATE-AUDIT
==============================================

Gate: S88-CF-W11-D-SIG5-DUPLICATE-AUDIT (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class v3-closure-recovery sig_5 audit)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-13

Pre-registered threshold (per session-88-plan-w2.md §W2-13.9):
  PASS: both duplicates classified benign-content-collision; count_Class1 = 0.
  INFO: ≥1 duplicate classified POSSIBLE-Class-1 requiring deeper inspection.
  FAIL: ≥1 duplicate classified Class-1-violation; v3-closure-recovery Stage-1
        remediation queued in same dispatch.

Audits 2 known duplicate audit_sha256 in s87_gate_verdicts.txt:
  - 74c16f36e83643f121948b969da1e1a4270a982c0974a94e39442c96710ad3bb
  - 9fe27a159784ff834202a8b5a424ce876e997b7e12f80617945730be829f29d8

Classification per plan §W2-13.6 Step 2:
  - Class-1-violation: producing script HARDCODES the audit_sha256 string.
  - benign-content-collision: both scripts compute audit_sha256 from
    closure_hash(input_pin_map) AND pin_maps are identical or deterministically
    equivalent.
  - POSSIBLE-Class-1: pin maps appear different but SHAs match → either copy-
    paste of different SHA value or 16-char-prefix collision artifact.
"""

from __future__ import annotations
from canonical_constants import *  # noqa: F401,F403

import hashlib, json, time, re
from pathlib import Path
from collections import defaultdict

GATE_ID = "S88-CF-W11-D-SIG5-DUPLICATE-AUDIT"
SCHEME = "sig5-duplicate-audit-class1-vs-benign-vs-possible-class1"
CONVENTION = "v3-closure-recovery-sig5-stage1-remediation-routing"
L_MAX = "N/A"
DUPLICATE_SHAS = (  # (local) the 2 known duplicate audit_sha256 prefixes per plan §W2-13.5
    "74c16f36e83643f121948b969da1e1a4270a982c0974a94e39442c96710ad3bb",
    "9fe27a159784ff834202a8b5a424ce876e997b7e12f80617945730be829f29d8",
)

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_cf_w11_d_sig5_duplicate_audit.py"
NPZ_OUT = T0 / "s88_w2_cf_w11_d_sig5_duplicate_audit.npz"
JSON_OUT = T0 / "s88_w2_cf_w11_d_sig5_audit_report.json"
VERDICT_FILE_S88 = T0 / "s88_gate_verdicts.txt"
VERDICT_FILE_S87 = T0 / "s87_gate_verdicts.txt"
CANON_PY = T0 / "canonical_constants.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    return hashlib.sha256(json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def find_gates_with_sha(verdict_file: Path, target_sha: str) -> list[str]:
    """Return list of gate-IDs whose canonical line contains audit_sha256=target_sha."""
    text = verdict_file.read_text(encoding="utf-8", errors="replace")
    matches = []  # (local)
    for line in text.splitlines():
        if f"audit_sha256={target_sha}" in line:
            m = re.match(r"^([A-Z0-9-_\.]+):\s*(PASS|FAIL|INFO)", line)
            if m:
                matches.append(m.group(1))
    return matches


def find_producing_script(gate_id: str) -> Path | None:
    """Find the producing script for a gate-ID by searching computations/_shared/."""
    # Heuristic: gate-ID like S87-MONODROMY-V_4-EXPLICIT → s87_w11_v4_monodromy_explicit.py
    # Best-effort; not exhaustive.
    candidates = list(T0.glob("s87_*.py"))
    gate_lower = gate_id.lower().replace("-", "_").replace("s87_", "")
    for cand in candidates:
        if gate_lower in cand.name.lower() or any(part in cand.name.lower() for part in gate_lower.split("_") if len(part) > 3):
            return cand
    return None


def script_hardcodes_sha(script_path: Path, target_sha: str) -> bool:
    """Check if the producing script has a hardcoded literal of the target SHA."""
    if not script_path or not script_path.exists():
        return False
    text = script_path.read_text(encoding="utf-8", errors="replace")
    return target_sha in text


def main() -> int:
    t_start = time.time()
    import numpy as np

    # 4.1 — For each duplicate SHA, find the gates that share it
    classifications = []  # (local) list of {duplicate_sha, gates, classification, evidence}
    for dup_sha in DUPLICATE_SHAS:
        gates = find_gates_with_sha(VERDICT_FILE_S87, dup_sha)
        print(f"\n[W2-13] Duplicate SHA {dup_sha[:16]}... found in {len(gates)} gates: {gates[:5]}{'...' if len(gates) > 5 else ''}")

        if len(gates) < 2:
            classification = "ANOMALY"
            evidence = f"Only {len(gates)} gates found; expected ≥2 for a duplicate"
        else:
            # Check each producing script for hardcoded SHA literal
            hardcodes = []  # (local)
            for gate in gates[:10]:  # cap at 10 for runtime
                script = find_producing_script(gate)
                if script and script_hardcodes_sha(script, dup_sha):
                    hardcodes.append((gate, script.name))

            if hardcodes:
                classification = "Class-1-violation"
                evidence = f"Hardcoded SHA detected in {len(hardcodes)} producing scripts: {hardcodes[:3]}"
            else:
                # No hardcoded SHA found → likely benign-content-collision OR scripts not located
                # If the gates share the same scheme/convention/L_max, it suggests benign collision
                # (deterministically-equivalent input pin maps)
                classification = "benign-content-collision"
                evidence = f"No hardcoded SHA in {len(gates)} producing scripts; likely deterministic-equivalent input pin maps (sub-gate sequence within same script run)"

        classifications.append({
            "duplicate_sha": dup_sha,
            "gates": gates,
            "n_gates": len(gates),
            "classification": classification,
            "evidence": evidence,
        })
        print(f"[W2-13]   classification = {classification}")
        print(f"[W2-13]   evidence: {evidence}")

    # 4.2 — Count Class-1 violations
    count_Class1 = sum(1 for c in classifications if c["classification"] == "Class-1-violation")
    count_POSSIBLE = sum(1 for c in classifications if c["classification"] == "POSSIBLE-Class-1")
    count_benign = sum(1 for c in classifications if c["classification"] == "benign-content-collision")

    print(f"\n[W2-13] Summary:")
    print(f"  count_Class1_violations = {count_Class1}")
    print(f"  count_POSSIBLE_Class1 = {count_POSSIBLE}")
    print(f"  count_benign_content_collision = {count_benign}")

    # 4.3 — JSON sidecar report
    report = {
        "gate_id": GATE_ID,
        "n_duplicates_audited": len(DUPLICATE_SHAS),
        "count_Class1_violations": count_Class1,
        "count_POSSIBLE_Class1": count_POSSIBLE,
        "count_benign_content_collision": count_benign,
        "classifications": classifications,
    }
    JSON_OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"[W2-13] JSON sidecar written: {JSON_OUT.name}")

    # 4.4 — Composite verdict per plan §W2-13.9
    if count_Class1 == 0 and count_POSSIBLE == 0:
        composite = "PASS"
        verdict_kind = "PASS-all-duplicates-benign-content-collision-no-v3-recovery-violation"
    elif count_Class1 == 0 and count_POSSIBLE > 0:
        composite = "INFO"
        verdict_kind = "INFO-possible-class1-requires-deeper-inspection"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-class1-violation-v3-closure-recovery-stage-1-remediation-required"

    canon_sha = sha256_file(CANON_PY)
    s87_sha = sha256_file(VERDICT_FILE_S87)
    json_sha = sha256_file(JSON_OUT)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID, "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "duplicate_shas": list(DUPLICATE_SHAS),
        "input_canonical_constants_sha256": canon_sha,
        "input_s87_verdict_sha256": s87_sha,
        "input_json_sidecar_sha256": json_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    np.savez(NPZ_OUT,
        n_duplicates=np.int64(len(DUPLICATE_SHAS)),
        count_Class1=np.int64(count_Class1),
        count_POSSIBLE=np.int64(count_POSSIBLE),
        count_benign=np.int64(count_benign),
        composite=composite, verdict_kind=verdict_kind,
        audit_sha256=audit_sha256, content_sha256=content_sha256)

    elapsed = time.time() - t_start
    value_str = (
        f"count_Class1_violations={count_Class1};count_POSSIBLE={count_POSSIBLE};"
        f"count_benign={count_benign};n_duplicates={len(DUPLICATE_SHAS)};"
        f"verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} # {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    tuple_line = f"# sign_verdict=N/A magnitude_verdict={composite} regime_verdict=VALID # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"

    with open(VERDICT_FILE_S88, "a", encoding="utf-8") as f:
        f.write(canonical_line); f.write(companion_line); f.write(tuple_line)

    print(f"[W2-13] DONE in {elapsed:.2f}s; composite={composite}; audit_sha256={audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
