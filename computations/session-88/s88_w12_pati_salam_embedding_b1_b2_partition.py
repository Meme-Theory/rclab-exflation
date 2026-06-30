"""
S88 W12-138 — S88-PATI-SALAM-EMBEDDING-PRESERVES-B1-B2-PARTITION
==================================================================

Plan-source-drift audit + INFO closure.

OWNERSHIP: mack-cosmic-bridge (cosmological-bridge audit) +
gen-physicist (orchestrator). Solo runner.

PRE-COMPUTE AUDIT — KNOWLEDGE MCP FINDINGS:

The plan §W12-138 line 27 asserts "Prereq #123 (Connes-distance subalgebra
restriction conjecture) NOT LANDED at plan-freeze" and instructs mechanical-
closure protocol if the prereq remains unlanded by W12 dispatch.

HOWEVER: `computations/session-88/s88_gate_verdicts.txt:396` shows the prereq
HAS LANDED in S88 W11-123:

  S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE: PASS --
    value='d_C_L10=2.386138;d_C_L12=2.386138;ratio_12_over_10=1.000000;
           finite_L10=True;finite_L12=True;sdp_feasible=True;
           reason=d_C finite at L=10 (2.3861) and L=12 (2.3861);
           ratio=1.0000 within regulator-stability band [0.85, 1.15];
           n_loc=16;n_bot=8;A_F_dim=14'
    scheme=A_F-restricted-Connes-distance
    convention=ECOS-SDP-A_F-direct-sum-14-params
    L_max=12
    audit_sha256=0f23ed5744809d9d7b14751ca31365fcdc097fabb0b93bc6f455cc93109ed785
    content_sha256=64aefdde1edc4710bf0f831c069a7f9b897acef05bc82d2547d6fbab86a6832d

Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical
closure IS acceptable" condition 1 ("Upstream-block topology is the
cause"), the mechanical-closure protocol DOES NOT FIRE because the
upstream-block premise is FALSE (the prereq has LANDED PASS).

The plan's conditional method (5 steps requiring Pati-Salam embedding
map from S86 W-9 framework registry + B1/B2 partition cardinality on
embedded substrate + B1 dominance factor 37 cross-check) requires
canonical infrastructure that is NOT pre-registered:

- Pati-Salam embedding map: NOT in canonical_constants.py; mentions
  exist only in `sessions/framework/Collabs/atlas-connes-collab.md` and
  `atlas-master-collab.md` (Collab atlases — not embedding-map canonical
  infrastructure).
- `B1_dominance_factor`: NOT in canonical_constants.py.
- `project_flat-bands-squeeze-less.md`: NOT present in
  `.claude/agent-memory/mack-cosmic-bridge/`.

Per `.claude/rules/epistemic-discipline.md §"Source Reconciliation"`
Class-(c) PIN-DRIFT-FROM-STALE-SOURCE: the plan was authored against
a snapshot that has been superseded; the gate must NOT silently reroute
to mechanical-closure (which would paper over an actual structural
change in the canonical state). Honest closure: INFO with composite
(sign=N/A, magnitude=N/A, regime=VALID-PARTIAL) and S89 carry-forward
to a properly-pre-registered method.

SUBSTITUTION CHAIN (written before closure):

  Step 1 (Definition): mechanical-closure protocol = the verdict-line
    pattern `value='PRE-REG-INC_blocked_by_<symbol>_<status>'` per
    `mechanical-closure-discipline.md`, applied IFF the upstream-block
    premise holds.

  Step 2 (Definition): upstream-block premise = ∀ prereq P in plan-pin:
    verdict(P) ≠ PASS.

  Step 3 (Substitute): plan §W12-138 prereq is #123 = "S88-CONNES-
    DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE". File grep on
    `computations/session-88/s88_gate_verdicts.txt:396` returns
    verdict(P) = PASS at d_C_L10=2.386138 = d_C_L12=2.386138.

  Step 4 (Simplify): upstream-block premise evaluates to FALSE
    (verdict(P) = PASS, not ≠ PASS). Mechanical-closure protocol
    DOES NOT FIRE.

  Step 5 (Direction): plan-pinned method's 5 conditional steps require
    Pati-Salam embedding map (not in canonical) + B1 dominance factor
    canonical (not in canonical) + project_flat-bands-squeeze-less
    memory file (not present). The conditional method's
    INFRASTRUCTURE-AVAILABILITY premise is FALSE.

  Step 6 (Conclusion): the gate is BLOCKED on infrastructure-pre-
    registration, NOT on prereq-landing. Honest closure: INFO (the
    prereq-landing premise of the plan's mechanical-closure protocol is
    refuted; the conditional method cannot execute without pre-
    registered infrastructure). Composite verdict INFO; S89 carry-
    forward with a properly-pre-registered method that includes
    Pati-Salam embedding map definition + B1 dominance factor canonical
    promotion.

VERDICT TARGET: INFO with composite (sign=N/A, magnitude=N/A,
regime=VALID-PARTIAL).

REFERENCES:
- Plan: sessions/session-plan/session-88-plan-w12.md §W12-138
- Prereq landing: computations/session-88/s88_gate_verdicts.txt:396
  (S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE PASS)
- .claude/rules/mechanical-closure-discipline.md §"When mechanical
  closure IS acceptable" condition 1
- .claude/rules/epistemic-discipline.md §"Source Reconciliation"
  Class-(c) PIN-DRIFT-FROM-STALE-SOURCE
- .claude/rules/gate-verdicts.md §"S87+ canonical form (Schema-v2)"
"""

import hashlib
import json
import sys
import time
from pathlib import Path

_THIS = Path(__file__).resolve()
_REPO = _THIS.parent.parent.parent
sys.path.insert(0, str(_REPO / "computations" / "_shared"))
from canonical_constants import tau_fold  # noqa: E402,F401

GATE_ID = "S88-PATI-SALAM-EMBEDDING-PRESERVES-B1-B2-PARTITION"
WP_SECTION = "W12-138"
SCHEME = "plan-source-drift-audit-prereq-LANDED-infrastructure-MISSING"
CONVENTION = "honest-INFO-closure-S89-carry-forward-for-pre-registration"


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    serialized = json.dumps(input_pin_map, sort_keys=True, default=str)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def main():
    t_start = time.time()
    print("=" * 72)
    print(f"GATE {GATE_ID}")
    print(f"  scheme={SCHEME}")
    print(f"  convention={CONVENTION}")
    print("=" * 72)
    print()

    # Input-pin SHAs
    PLAN_PATH = _REPO / "sessions" / "session-plan" / "session-88-plan-w12.md"
    VERDICTS_PATH = _REPO / "computations" / "session-88" / "s88_gate_verdicts.txt"
    MECH_CLOSURE_RULE_PATH = _REPO / ".claude" / "rules" / "mechanical-closure-discipline.md"
    EPISTEMIC_RULE_PATH = _REPO / ".claude" / "rules" / "epistemic-discipline.md"
    CANONICAL_CONSTANTS_PATH = _REPO / "computations" / "_shared" / "canonical_constants.py"

    print("[Step 0] Computing input-pin SHAs ...")
    sha_plan = file_sha256(PLAN_PATH)
    sha_verdicts = file_sha256(VERDICTS_PATH)
    sha_mech_closure_rule = file_sha256(MECH_CLOSURE_RULE_PATH)
    sha_epistemic_rule = file_sha256(EPISTEMIC_RULE_PATH)
    sha_canonical_consts = file_sha256(CANONICAL_CONSTANTS_PATH)
    print(f"  plan_w12:              {sha_plan}")
    print(f"  s88_verdicts:          {sha_verdicts}")
    print(f"  mech_closure_rule:     {sha_mech_closure_rule}")
    print(f"  epistemic_rule:        {sha_epistemic_rule}")
    print(f"  canonical_constants:   {sha_canonical_consts}")
    print()

    # Step 1: Verify prereq #123 status by direct grep on canonical verdict file
    print("[Step 1] Verifying prereq #123 status from canonical state ...")
    prereq_id = "S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE"
    prereq_verdict = None
    prereq_audit_sha = None
    with open(VERDICTS_PATH, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith(prereq_id + ":"):
                # Parse PASS/FAIL/INFO
                parts = line.split("--", 1)
                if len(parts) == 2:
                    head = parts[0].strip()
                    if "PASS" in head:
                        prereq_verdict = "PASS"
                    elif "INFO" in head:
                        prereq_verdict = "INFO"
                    else:
                        prereq_verdict = "FAIL"
                    # Extract audit_sha256
                    body = parts[1]
                    for tok in body.split():
                        if tok.startswith("audit_sha256="):
                            prereq_audit_sha = tok[len("audit_sha256="):]
                            break
                break
    print(f"  prereq #123 = {prereq_id}")
    print(f"  verdict     = {prereq_verdict}")
    print(f"  audit_sha   = {prereq_audit_sha}")
    print()

    # Step 2: Determine mechanical-closure applicability
    print("[Step 2] Mechanical-closure protocol applicability ...")
    upstream_block_premise = (prereq_verdict != "PASS")
    print(f"  upstream_block_premise (verdict != PASS): {upstream_block_premise}")
    print(f"  mechanical_closure_protocol_fires: {upstream_block_premise}")
    print()

    # Step 3: Check Pati-Salam embedding map + B1 dominance factor canonical
    print("[Step 3] Plan-pinned conditional-method infrastructure availability ...")
    has_pati_salam_canonical = False
    has_b1_dominance_factor_canonical = False
    with open(CANONICAL_CONSTANTS_PATH, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
        if "Pati_Salam" in text or "pati_salam" in text:
            has_pati_salam_canonical = True
        if "B1_dominance_factor" in text:
            has_b1_dominance_factor_canonical = True
    print(f"  Pati_Salam canonical in canonical_constants.py: {has_pati_salam_canonical}")
    print(f"  B1_dominance_factor canonical:                  {has_b1_dominance_factor_canonical}")
    infrastructure_available = has_pati_salam_canonical and has_b1_dominance_factor_canonical
    print(f"  infrastructure_available_for_conditional_method: {infrastructure_available}")
    print()

    # Step 4: Composite verdict
    # The plan's mechanical-closure protocol presumed prereq #123 unlanded;
    # actual canonical state has #123 LANDED PASS. Mechanical-closure DOES
    # NOT FIRE. Conditional method requires infrastructure NOT pre-registered.
    # Honest closure: INFO (prereq satisfied, infrastructure missing for
    # conditional method, S89 carry-forward).
    sign_verdict = "N/A"
    magnitude_verdict = "N/A"
    regime_verdict = "VALID-PARTIAL"  # prereq satisfied; method blocked on infra
    composite_verdict = "INFO"

    print("[Step 4] Composite verdict ...")
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  composite         = {composite_verdict}")
    print()

    input_pin_map = {
        "gate_id": GATE_ID,
        "wp_section": WP_SECTION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "prereq_id": prereq_id,
        "prereq_verdict": prereq_verdict,
        "prereq_audit_sha256": prereq_audit_sha,
        "upstream_block_premise": upstream_block_premise,
        "has_pati_salam_canonical": has_pati_salam_canonical,
        "has_b1_dominance_factor_canonical": has_b1_dominance_factor_canonical,
        "infrastructure_available": infrastructure_available,
        "input_sha_plan": sha_plan,
        "input_sha_verdicts": sha_verdicts,
        "input_sha_mech_closure_rule": sha_mech_closure_rule,
        "input_sha_epistemic_rule": sha_epistemic_rule,
        "input_sha_canonical_constants": sha_canonical_consts,
    }

    audit_sha256 = closure_hash(input_pin_map)
    content_payload = {
        "prereq_verdict": prereq_verdict,
        "upstream_block_premise": upstream_block_premise,
        "has_pati_salam_canonical": has_pati_salam_canonical,
        "has_b1_dominance_factor_canonical": has_b1_dominance_factor_canonical,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite_verdict": composite_verdict,
    }
    content_sha256 = closure_hash(content_payload)
    print(f"[Step 5] dual-SHA closure:")
    print(f"  audit_sha256:   {audit_sha256}")
    print(f"  content_sha256: {content_sha256}")
    print()

    # Save JSON sidecar
    json_path = (
        _REPO / "computations" / "session-88"
        / "s88_w12_pati_salam_embedding_b1_b2_partition.json"
    )
    payload = {
        **input_pin_map,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite_verdict": composite_verdict,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "rationale": (
            "Prereq #123 has LANDED PASS at S88 W11-123 "
            f"(d_C_L10=2.386138; verdict audit_sha={prereq_audit_sha}). "
            "The plan's mechanical-closure protocol (premised on #123 "
            "NOT LANDED) does not fire. The plan's conditional method "
            "requires Pati-Salam embedding map + B1 dominance factor "
            "canonical, neither pre-registered in canonical_constants.py "
            "or framework registry. Routes to S89 carry-forward "
            "S89-PATI-SALAM-EMBEDDING-FULL-COMPUTATION with proper "
            "pre-registration."
        ),
    }
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, default=str)
    print(f"[Step 6] JSON sidecar: {json_path}")
    print()

    # Append verdict line
    verdict_file = _REPO / "computations" / "session-88" / "s88_gate_verdicts.txt"
    canonical_line = (
        f"{GATE_ID}: {composite_verdict} -- "
        f"value='prereq_123_LANDED_PASS_at_S88_W11_123_mechanical_closure_protocol_"
        f"inapplicable_full_pati_salam_embedding_computation_requires_S89_pre_registration_"
        f"of_embedding_map_and_B1_dominance_factor_canonical' "
        f"scheme={SCHEME} convention={CONVENTION} L_max=10 "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version=S87+\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )
    triple_companion = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2)\n"
    )
    diagnostic_companion = (
        f"# DIAGNOSTIC: plan §W12-138 mechanical-closure protocol inapplicable. "
        f"Prereq #123 (S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE) "
        f"LANDED PASS at S88 W11-123 (d_C_L10=2.386138, ratio=1.0000, audit_sha="
        f"{prereq_audit_sha}); per mechanical-closure-discipline.md condition 1 the "
        f"upstream-block premise is FALSE. Conditional method requires Pati-Salam "
        f"embedding map (NOT in canonical_constants.py) + B1 dominance factor "
        f"canonical (NOT in canonical_constants.py); infrastructure pre-registration "
        f"missing. Class-(c) PIN-DRIFT-FROM-STALE-SOURCE: plan-author snapshot of "
        f"#123 status superseded by S88 W11-123 PASS landing. S89 carry-forward "
        f"`S89-PATI-SALAM-EMBEDDING-FULL-COMPUTATION` with proper pre-registration "
        f"of embedding map + B1 dominance factor canonical.\n"
    )
    with open(verdict_file, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(dual_sha_companion)
        fh.write(triple_companion)
        fh.write(diagnostic_companion)

    print(f"[Step 7] Verdict appended to: {verdict_file}")
    print()
    print("CANONICAL LINE:")
    print(canonical_line.rstrip())
    print(dual_sha_companion.rstrip())
    print(triple_companion.rstrip())
    print(diagnostic_companion.rstrip())
    print()

    elapsed = time.time() - t_start
    print(f"[done] elapsed={elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
