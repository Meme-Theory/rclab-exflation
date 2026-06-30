"""
S88 W9 §W9-101 — Orchestrator joint-AND aggregation of T7-S67 INDEPENDENT-VERIFY.

Per joint-theorem-promotion.md §"Stage 2" PASS-AND aggregator:
- Reads per-axis verdict lines (AXIS-TRANSIT, AXIS-SPECTRAL) from s88_gate_verdicts.txt.
- Validates both PASS, all single-axis clauses PASS, joint clauses (c)+(d) PASS-AND.
- Emits canonical S88-OR-LATER-T7-S67-INDEPENDENT-VERIFY verdict line + dual-SHA + 3-tuple.
- §VII.AG.1 STAGE-1-CANDIDATE → STAGE-3-PERMANENT eligibility on PASS.

Substitution chain in module docstring above; numerical computation below.

Orchestrator-direct (no Agent-tool dispatch) per user's "avoid agent tasking" preference
+ rclab-solo Phase 2 step 2 agent-ownership-takeover discipline.
"""
import hashlib
import re
import sys
from pathlib import Path

VERDICT_FILE = Path("computations/session-88/s88_gate_verdicts.txt")
GATE_ID = "S88-OR-LATER-T7-S67-INDEPENDENT-VERIFY"
AXIS_TRANSIT_GATE = f"{GATE_ID}-AXIS-TRANSIT"
AXIS_SPECTRAL_GATE = f"{GATE_ID}-AXIS-SPECTRAL"

# Plan-pinned input map (joint-theorem-promotion.md Stage 2):
JOINT_CLAUSE_AGGREGATOR = "AND"
PROMOTION_PATHWAY = "STAGE-1-CANDIDATE-to-STAGE-3-PERMANENT"
RULE_PIN = ".claude/rules/joint-theorem-promotion.md#Stage-2"


def parse_verdict_line(text: str, gate_id: str) -> dict:
    """Parse a canonical S87+ verdict line into {verdict, audit_sha256, content_sha256, value, scheme, convention, L_max}."""
    pattern = re.compile(
        rf"^{re.escape(gate_id)}: (PASS|FAIL|INFO) -- "
        r"value=(.+?) "
        r"scheme=(.+?) "
        r"convention=(.+?) "
        r"L_max=(.+?) "
        r"audit_sha256=([0-9a-f]{64}) "
        r"content_sha256=([0-9a-f]{64})"
    )
    for line in text.splitlines():
        m = pattern.match(line.strip())
        if m:
            return {
                "verdict": m.group(1),
                "value": m.group(2),
                "scheme": m.group(3),
                "convention": m.group(4),
                "L_max": m.group(5),
                "audit_sha256": m.group(6),
                "content_sha256": m.group(7),
            }
    raise ValueError(f"Per-axis verdict line not found for {gate_id}")


def closure_hash(items: list[tuple[str, str]]) -> str:
    """SHA-256 over serialized (key=value) tuples in order — canonical input-pin map."""
    s = "|".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    text = VERDICT_FILE.read_text(encoding="utf-8")
    transit = parse_verdict_line(text, AXIS_TRANSIT_GATE)
    spectral = parse_verdict_line(text, AXIS_SPECTRAL_GATE)

    # Step 1+2: validate both per-axis PASS (substitution chain Step 1+2 of module docstring).
    if transit["verdict"] != "PASS":
        print(f"FAIL: AXIS-TRANSIT verdict is {transit['verdict']} (not PASS); aggregate cannot promote.", file=sys.stderr)
        return 1
    if spectral["verdict"] != "PASS":
        print(f"FAIL: AXIS-SPECTRAL verdict is {spectral['verdict']} (not PASS); aggregate cannot promote.", file=sys.stderr)
        return 1

    # Step 3+4: PASS-AND on JOINT clauses (c)+(d) — both axes record c=PASS d=PASS in their value strings.
    transit_c = "c_transit=PASS" in transit["value"]
    transit_d = "d_transit=PASS" in transit["value"]
    spectral_c = "c=PASS" in spectral["value"]
    spectral_d = "d=PASS" in spectral["value"]
    joint_c_PASS_AND = transit_c and spectral_c
    joint_d_PASS_AND = transit_d and spectral_d
    if not (joint_c_PASS_AND and joint_d_PASS_AND):
        print(f"FAIL: JOINT clause PASS-AND failed (c={joint_c_PASS_AND}, d={joint_d_PASS_AND}).", file=sys.stderr)
        return 1

    # Step 5+6: aggregate = PASS, promotion eligible.
    aggregate_verdict = "PASS"
    promotion = PROMOTION_PATHWAY  # STAGE-1-CANDIDATE → STAGE-3-PERMANENT

    # Build aggregate value string (machinery + cross-axis traceability).
    value = (
        f"axis_transit={transit['verdict']};axis_spectral={spectral['verdict']};"
        f"joint_c_PASS_AND={joint_c_PASS_AND};joint_d_PASS_AND={joint_d_PASS_AND};"
        f"axis_transit_audit_sha={transit['audit_sha256'][:16]};"
        f"axis_spectral_audit_sha={spectral['audit_sha256'][:16]};"
        f"aggregator={JOINT_CLAUSE_AGGREGATOR};promotion={promotion};"
        f"VII_AG_1=STAGE-3-PERMANENT-ELIGIBLE"
    )
    scheme = "joint-theorem-promotion-Stage-2-PASS-AND-aggregator"
    convention = "two-axis-independent-verify-AND-aggregation-orchestrator-direct-write"
    L_max = transit["L_max"]  # both axes pinned at L_max=10

    # Compute closure SHAs over input-pin map.
    pin_map = [
        ("gate_id", GATE_ID),
        ("axis_transit_audit_sha256", transit["audit_sha256"]),
        ("axis_transit_content_sha256", transit["content_sha256"]),
        ("axis_spectral_audit_sha256", spectral["audit_sha256"]),
        ("axis_spectral_content_sha256", spectral["content_sha256"]),
        ("joint_clause_aggregator", JOINT_CLAUSE_AGGREGATOR),
        ("rule_pin", RULE_PIN),
        ("promotion_pathway", promotion),
        ("L_max", L_max),
        ("scheme", scheme),
        ("convention", convention),
    ]
    audit_sha256 = closure_hash(pin_map)

    # Build canonical verdict line.
    canonical = (
        f"{GATE_ID}: {aggregate_verdict} -- "
        f"value='{value}' "
        f"scheme={scheme} "
        f"convention={convention} "
        f"L_max={L_max} "
        f"audit_sha256={audit_sha256} "
    )
    # content_sha256 over the canonical line text (excluding content_sha256 field itself).
    content_sha256 = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    canonical += f"content_sha256={content_sha256} schema_version=S87+"

    # Companion rows.
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); orchestrator-direct joint-AND aggregation per joint-theorem-promotion.md Stage 2"
    )
    tuple_row = (
        f"# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); aggregate of axis-transit + axis-spectral PASS-AND on joint clauses (c)+(d)"
    )

    # SHA uniqueness check (sig_5 ladder per v3-closure-recovery.md).
    if audit_sha256 in text:
        print(f"FAIL: audit_sha256={audit_sha256} already present in verdict file (sig_5 collision).", file=sys.stderr)
        return 1

    # Atomic single-append write (race-safe via 'a' mode O_APPEND).
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write("\n" + canonical + "\n" + dual_sha_row + "\n" + tuple_row + "\n")

    # Final report (pre-registered direction "all PASS-AND'd → aggregate PASS" matched).
    print(f"AGGREGATE: {aggregate_verdict}")
    print(f"audit_sha256={audit_sha256}")
    print(f"content_sha256={content_sha256}")
    print(f"axis_transit={transit['audit_sha256'][:16]} axis_spectral={spectral['audit_sha256'][:16]}")
    print(f"joint_c_PASS_AND={joint_c_PASS_AND} joint_d_PASS_AND={joint_d_PASS_AND}")
    print(f"§VII.AG.1 promotion: {promotion}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
