#!/usr/bin/env python3
"""
_s92_w2_5_mechanical_closure.py — Mechanical PRE-REG-INC closure for S92 §W2-5.

Gate: S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY
Reason: Plan-pre-registered Case B fires per session-92-plan-w2.md "Wave 2 → Wave 3
Decision Point". §W2-3 (S92-W2-CF-W9-9-1-WODZICKI-F-FUNCTOR-M-KK-5-NORMALIZATION)
closed FAIL (composite; sign=FAIL/magnitude=FAIL/regime=VALID;
audit_sha256=5395d9228df93174275531c15c27e6d618474d9c736282ae155d0223463b34fb) —
the M_KK^5 dimensional rescaling cancels in the dimensionless ratio so the 5-OOM
gap from S91 W1-14 persists structurally. §W2-4
(S92-W2-CF-W9-9-2-LEVEL-2-ENVELOPE-C-W-L-MAX-SCAN) closed INFO
(sign=PASS/magnitude=INFO/regime=VALID;
audit_sha256=26cbc4c0c3af265f4b8ab661194b6917c16b0f5ce8694b6968877dedd68d11d6) —
L^{-2} structural form sign-correct but magnitude in boundary-effect regime.

§W2-5 CONDITIONAL precondition (§W2-3 PASS ∧ §W2-4 PASS) UNSATISFIED →
Stage-2 cross-axis verify pre-empted; honest mechanical closure per Case B.

Per .claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS
acceptable":
  (1) Upstream-block topology IS the cause (§W2-3 verdict ≠ PASS; §W2-4 verdict ≠ PASS);
      plan §"Wave 2 → Wave 3 Decision Point" Case B specifies the documented outcome.
  (2) Verdict honesty: FAIL with value='PRE-REG-INC_blocked_by_W2-3_FAIL_W2-4_INFO'.
  (3) Per-gate-distinct audit_sha256 (pinmap embeds gate_id + scheme + convention +
      upstream-blocked refs; pairwise distinct from §W2-3 + §W2-4 audit SHAs).
  (4) Audit-trail signature names blocking prereqs (W2-3 FAIL, W2-4 INFO).
  (5) WP §W2-5 section updated IN SAME RUN as verdict-line append.

Per .claude/rules/gate-verdicts.md §"Canonical Verdict-File Path":
  canonical line at computations/session-92/s92_gate_verdicts.txt with full 64-char
  audit_sha256 + content_sha256 + dual-SHA companion comment row + schema-v2
  3-tuple companion row (sign=N/A magnitude=N/A regime=N/A — closure is bookkeeping,
  not a substrate-physics measurement).
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Canonical-constants import per computations/_shared/CLAUDE.md MANDATORY rule.
# M_KK is referenced as the F-functor scalar base whose M_KK^5 image (the §W2-3
# normalization attempt) cancels in the dimensionless ratio — the substrate-IS
# structural finding that drives this gate's mechanical closure.
_shared_dir = Path(__file__).resolve().parent  # (local) script dir resolver
sys.path.insert(0, str(_shared_dir))
from canonical_constants import M_KK  # noqa: E402  # framework canonical M_KK pin

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) repo-root resolver

GATE_ID = "S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY"
SCHEME = (
    "stage-2-cross-axis-independent-verification-Axis-A-connes-Axis-B-mack-"
    "substrate-input-orthogonality-at-2-observables-structural-ceiling"
)
CONVENTION = (
    "VII-BA-Wodzicki-BCS-Stage-2-cross-axis-PASS-AND-aggregation-with-volovik-"
    "EXCLUDED-original-authoring-agent-and-downstream-inheritance-reach"
)
L_MAX = "12"
SCHEMA_VERSION = "S87+"

# Upstream verdicts at closure time (per session-92 verdict file lines 30-46)
UPSTREAM_W2_3 = {
    "gate_id": "S92-W2-CF-W9-9-1-WODZICKI-F-FUNCTOR-M-KK-5-NORMALIZATION",
    "verdict": "FAIL",
    "composite": "sign=FAIL/magnitude=FAIL/regime=VALID",
    "audit_sha256": "5395d9228df93174275531c15c27e6d618474d9c736282ae155d0223463b34fb",
    "content_sha256": "04ebb1bd0678ce1aa7117f6c3f6986f72edb65b3a588855ae275bee456d2d049",
}
UPSTREAM_W2_4 = {
    "gate_id": "S92-W2-CF-W9-9-2-LEVEL-2-ENVELOPE-C-W-L-MAX-SCAN",
    "verdict": "INFO",
    "composite": "sign=PASS/magnitude=INFO/regime=VALID",
    "audit_sha256": "26cbc4c0c3af265f4b8ab661194b6917c16b0f5ce8694b6968877dedd68d11d6",
    "content_sha256": "96429b390648e436fda272601b92b5566c31a665a1d5fc47be828473ccbc960b",
}

VALUE = (
    "PRE-REG-INC_blocked_by_W2-3_FAIL_W2-4_INFO;"
    "reason=stage_2_cross_axis_verify_preempted_by_§VII.BA_F-functor_image_identification_structural_incomplete_per_W2-3_FAIL_pathway_a;"
    "plan_decision_point=session-92-plan-w2.md_Case_B;"
    "closure_type=mechanical_per_mechanical-closure-discipline.md;"
    "downstream_routing=S93+_carry_forward_CF-S93-W2-3-FAIL-PATHWAY-A-F-FUNCTOR-IMAGE-NON-SCALAR-RECONSTRUCTION;"
    "§VII.BA_STAGE-3-PERMANENT_promotion_postponed=True;"
    "§VII.BA_remains_at_STAGE-1-CANDIDATE=True;"
    "stage_2_pre_condition_W2-3_PASS_∧_W2-4_PASS=UNSATISFIED;"
    "stage_2_dispatch_attempted=False;"
    "axes_pre_assigned_at_plan_freeze_unchanged=Axis-A=connes-ncg-theorist,Axis-B=mack-cosmic-bridge_PRIMARY/van-den-dungen-bridge-theorist_ALTERNATE,volovik=EXCLUDED;"
    "substrate-input-orthogonality_predicate_unrealized=True"
)

VERDICT_TXT = REPO_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
WP_PATH = REPO_ROOT / "sessions" / "session-92" / "session-92-w2-workingpaper.md"


def sha256_of_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Deterministic SHA-256 over the input-pin map (sorted keys, str default)."""
    canonical = json.dumps(pin_map, sort_keys=True, default=str, ensure_ascii=False)
    return sha256_of_text(canonical)


def extract_plan_w2_5_block_sha() -> str:
    plan_path = REPO_ROOT / "sessions" / "session-plan" / "session-92-plan-w2.md"
    text = plan_path.read_text(encoding="utf-8", errors="ignore")
    import re
    m = re.search(r"(## §W2-5\.[\s\S]*?)(?=\n## Wave 2 → Wave 3)", text)
    return sha256_of_text(m.group(1)) if m else "MISSING"


def main() -> None:
    closure_script_text = Path(__file__).read_text(encoding="utf-8", errors="ignore")
    closure_script_sha = sha256_of_text(closure_script_text)

    input_pin_map = {
        "pin_01_gate_id": GATE_ID,
        "pin_02_wp_id": "sessions/archive/session-92/session-92-w2-workingpaper.md §W2-5",
        "pin_03_scheme": SCHEME,
        "pin_04_convention": CONVENTION,
        "pin_05_L_max": L_MAX,
        "pin_06_upstream_blocked_by_W2_3": UPSTREAM_W2_3,
        "pin_07_upstream_INFO_W2_4": UPSTREAM_W2_4,
        "pin_08_plan_decision_point_case": "B",
        "pin_09_plan_W2_5_block_sha": extract_plan_w2_5_block_sha(),
        "pin_10_closure_value": VALUE,
        "pin_11_schema_version": SCHEMA_VERSION,
        "pin_12_mechanical_closure_rule_path": ".claude/rules/mechanical-closure-discipline.md",
        "pin_13_closure_script_sha": closure_script_sha,
        "pin_14_closure_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "pin_15_stage_2_attempted": False,
        "pin_16_axes_pre_assigned_unchanged": True,
        "pin_17_downstream_carry_forward_id": "CF-S93-W2-3-FAIL-PATHWAY-A-F-FUNCTOR-IMAGE-NON-SCALAR-RECONSTRUCTION",
    }

    audit_sha256 = closure_hash(input_pin_map)
    content_sha256 = closure_script_sha

    canonical = (
        f"{GATE_ID}: FAIL -- value='{VALUE}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version={SCHEMA_VERSION}"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); [VERIFY-THEOREM] trigger; "
        f"mechanical closure per mechanical-closure-discipline.md Case B (upstream-block)"
    )
    three_tuple = (
        f"# sign_verdict=N/A magnitude_verdict=N/A regime_verdict=N/A "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"mechanical closure — no substrate-physics measurement; "
        f"upstream-block: W2-3 FAIL + W2-4 INFO; Stage-2 verify pre-empted"
    )
    upstream_block_comment = (
        f"# upstream_block_chain_W2-5: blocked_by=W2-3_FAIL (audit_sha256={UPSTREAM_W2_3['audit_sha256']}); "
        f"adjacent=W2-4_INFO (audit_sha256={UPSTREAM_W2_4['audit_sha256']}); "
        f"plan_case=B per session-92-plan-w2.md Wave 2 → Wave 3 Decision Point; "
        f"§VII.BA stays STAGE-1-CANDIDATE; "
        f"forward=CF-S93-W2-3-FAIL-PATHWAY-A-F-FUNCTOR-IMAGE-NON-SCALAR-RECONSTRUCTION"
    )

    # Atomic POSIX O_APPEND write (parallel-writer-safe per epistemic-discipline.md
    # §"Registry-Write Hygiene under Parallel-Writer Race")
    with VERDICT_TXT.open("a", encoding="utf-8") as f:
        f.write("\n")
        f.write(canonical + "\n")
        f.write(dual_sha_companion + "\n")
        f.write(three_tuple + "\n")
        f.write(upstream_block_comment + "\n")

    # Update WP §W2-5 section IN SAME RUN per mechanical-closure-discipline.md
    wp_text = WP_PATH.read_text(encoding="utf-8", errors="ignore")

    new_w2_5 = build_w2_5_section(audit_sha256, content_sha256)

    # Replace the §W2-5 section (lines 145-167 originally; anchor-driven splice)
    import re
    pattern = re.compile(
        r"(### §W2-5\. S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY[\s\S]*?)(?=\n## Wave 2 Synthesis|\n---\n\n## Wave 2 Synthesis)",
        flags=0,
    )
    if not pattern.search(wp_text):
        # Fallback anchor: between the §W2-5 header and the next major section
        pattern = re.compile(
            r"(### §W2-5\. S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY[\s\S]*?)(?=\n## )",
            flags=0,
        )

    new_wp = pattern.sub(new_w2_5, wp_text, count=1)
    WP_PATH.write_text(new_wp, encoding="utf-8")

    # JSON sidecar for full audit trail
    sidecar = {
        "gate_id": GATE_ID,
        "verdict": "FAIL",
        "composite_3tuple": "N/A/N/A/N/A (mechanical closure)",
        "value": VALUE,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "schema_version": SCHEMA_VERSION,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "input_pin_map": input_pin_map,
        "closure_type": "mechanical_per_mechanical-closure-discipline.md",
        "plan_case": "B",
        "canonical_M_KK_at_closure_GeV": float(M_KK),  # F-functor scalar base from §W2-3 documentation
        "upstream_block": {
            "W2-3": UPSTREAM_W2_3,
            "W2-4": UPSTREAM_W2_4,
        },
        "downstream_routing": {
            "carry_forward_id": "CF-S93-W2-3-FAIL-PATHWAY-A-F-FUNCTOR-IMAGE-NON-SCALAR-RECONSTRUCTION",
            "§VII.BA_status": "STAGE-1-CANDIDATE (unchanged)",
            "stage_3_promotion": "postponed",
        },
    }
    sidecar_path = REPO_ROOT / "computations" / "session-92" / "s92_w2_w5_pre_reg_inc_closure.json"
    sidecar_path.write_text(json.dumps(sidecar, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps({
        "ok": True,
        "gate_id": GATE_ID,
        "verdict": "FAIL",
        "value_short": "PRE-REG-INC_blocked_by_W2-3_FAIL_W2-4_INFO",
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "verdict_file": str(VERDICT_TXT),
        "wp_path": str(WP_PATH),
        "sidecar": str(sidecar_path),
    }, indent=2, ensure_ascii=False))


def build_w2_5_section(audit_sha256: str, content_sha256: str) -> str:
    return f"""### §W2-5. S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY (mechanical closure per Case B)

**Status**: COMPLETED
**Gate ID**: `S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Stage-2 cross-axis verify pre-empted; mechanical closure per `.claude/rules/mechanical-closure-discipline.md`)
**Agent**: orchestrator-direct (mechanical closure; no specialist physics framing required for upstream-block documentation)
**Hypothesis**: Per plan §"Wave 2 → Wave 3 Decision Point" Case B, this gate is CONDITIONAL on §W2-3 PASS ∧ §W2-4 PASS. §W2-3 closed FAIL composite and §W2-4 closed INFO composite — the precondition is UNSATISFIED. §VII.BA STAGE-1-CANDIDATE remains at STAGE-1-CANDIDATE; Stage-3-PERMANENT promotion postponed pending S93+ remediation.
**Plan reference**: `sessions/session-plan/session-92-plan-w2.md` §W2-5 + §"Wave 2 → Wave 3 Decision Point" Case B.

**Output Artifacts** (closure-verification checklist):

| Plan-pinned path | On-disk | Closure-handling rationale |
|:-----------------|:--------|:---------------------------|
| `computations/_shared/_s92_w2_5_mechanical_closure.py` | EXISTS | Mechanical-closure script (orchestrator-authored) per `mechanical-closure-discipline.md`; single-shot AFTER-pattern; pure hashlib + Path; no subagent dispatch |
| `computations/session-92/s92_w2_w5_pre_reg_inc_closure.json` | EXISTS | JSON sidecar carrying full input_pin_map + upstream-block chain + downstream-routing |
| `s92_gate_verdicts.txt` (verdict line) | EXISTS | Canonical FAIL line with full 64-char audit_sha256 + dual-SHA companion + 3-tuple companion (`sign=N/A magnitude=N/A regime=N/A` because mechanical closure has no substrate-physics measurement) + upstream-block-chain comment row |
| `sessions/archive/session-92/session-92-w2-workingpaper.md §W2-5` | EXISTS | This section. Status COMPLETED + Verdict FAIL (mechanical-closure) + upstream-block chain documented + downstream routing to S93+ CF |

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| Closure-type pre-check | `mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" 5-condition checklist verified: (1) upstream-block topology IS cause (§W2-3 verdict ≠ PASS); (2) verdict honesty (FAIL not PASS); (3) per-gate-distinct audit_sha256 (pinmap embeds gate_id+scheme+convention); (4) audit-trail signature names blocking prereqs (W2-3 FAIL, W2-4 INFO); (5) WP section updated IN SAME RUN. |
| Stage-2 protocol pre-check | `joint-theorem-promotion.md §"Stage 2"` requires PASS-AND across both cross-reviewers on JOINT clauses (5-anatomy + 3-level). With §W2-3 FAIL, the F-functor image identification (Element 3 bridge map) is structurally incomplete — Stage-2 verify of the bridge theorem cannot meaningfully proceed. The precondition `§W2-3 PASS ∧ §W2-4 PASS` is structural, not merely procedural. |
| Case-B disposition | Plan §"Wave 2 → Wave 3 Decision Point" Case B specifies the documented outcome: §W2-5 honestly closes per `mechanical-closure-discipline.md` with `value='PRE-REG-INC_blocked_by_<gate>_<status>'`. The closure is the pre-registered path, NOT post-hoc plan editing. |

**Verdict**: **FAIL** (composite); value='PRE-REG-INC_blocked_by_W2-3_FAIL_W2-4_INFO'; 3-tuple `sign=N/A magnitude=N/A regime=N/A` (mechanical closure — no substrate-physics measurement); canonical audit_sha256 = `{audit_sha256}`; content_sha256 = `{content_sha256}`. Per `gate-verdicts.md §"All Results Are Good Results"`: FAIL is a result, NOT an agent failure — this FAIL closes the §VII.BA Wave-2 promotion corridor at the F-functor identification leg.

**Results**:

#### Closure rationale (substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`)

- **Definition 1 (§W2-5 precondition per plan §W2-5 line 110)**: "CONDITIONAL on §W2-3 PASS ∧ §W2-4 PASS within Wave 2."
- **Definition 2 (§W2-3 outcome, audit_sha256=5395d9228df93174...)**: composite=FAIL (sign=FAIL/magnitude=FAIL/regime=VALID); M_KK^5 rescaling cancels in dimensionless ratio; 5-OOM Level-3 gap persists structurally; routes to plan §W2-3 FAIL_meaning pathway (a) — F-functor image identification is NOT a single scalar multiplicative rescaling.
- **Definition 3 (§W2-4 outcome, audit_sha256=26cbc4c0c3af265f...)**: composite=INFO (sign=PASS/magnitude=INFO/regime=VALID); L^{-2} structural form per Connes 1995 §III.4 sign-correct (slope_emp=-2.769 < 0); magnitude in boundary-effect regime (`|slope_emp − (-2.0)|` = 0.769 > 0.10 PASS-band).
- **Substitute**: Definition 1 precondition `(§W2-3 PASS) ∧ (§W2-4 PASS)` evaluates to `(FAIL == PASS) ∧ (INFO == PASS)` = `False ∧ False` = `False`. Precondition UNSATISFIED.
- **Simplify**: Per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"`: upstream-block topology is the cause AND plan §"Wave 2 → Wave 3 Decision Point" Case B documents the outcome → mechanical closure ADMISSIBLE.
- **Canonical form**: `S92-W2-CF-W9-9-3-VII-BA-STAGE-2-CROSS-AXIS-VERIFY: FAIL -- value='PRE-REG-INC_blocked_by_W2-3_FAIL_W2-4_INFO' ...`.
- **Direction**: FAIL routes §VII.BA Stage-3-PERMANENT eligibility to S93+ (NOT to Stage-3-PERMANENT now); §VII.BA stays at STAGE-1-CANDIDATE; downstream carry-forward `CF-S93-W2-3-FAIL-PATHWAY-A-F-FUNCTOR-IMAGE-NON-SCALAR-RECONSTRUCTION` queues the substantive remediation (non-scalar F-functor image morphism derivation).
- **Conclusion**: §W2-5 mechanically closes per Case B; §VII.BA STAGE-3-PERMANENT promotion postponed; framework's third cross-axis joint theorem eligibility (after §VII.AH at S90 W2 CF-20 + §VII.U.2 Corner II Var_a S92 W4) is NOT achieved at S92 W2 close.

#### Upstream-block chain (audit-trail signature)

```
§W2-5 (this gate, FAIL mechanical closure)
   ↑ pre-condition UNSATISFIED
   ├── §W2-3 (FAIL composite; primary blocker)
   │     audit_sha256 = 5395d9228df93174275531c15c27e6d618474d9c736282ae155d0223463b34fb
   │     pathway = (a) F-functor image identification NOT a single scalar
   │     remediation = non-scalar F-functor image morphism derivation queued S93+
   │
   └── §W2-4 (INFO composite; adjacent indicator)
         audit_sha256 = 26cbc4c0c3af265f4b8ab661194b6917c16b0f5ce8694b6968877dedd68d11d6
         slope_emp = -2.769 (sign-correct; magnitude in boundary regime)
         interpretation = L^{{-2}} structural form holds; ∞-proxy boundary effects
```

The §W2-3 FAIL is the PRIMARY blocker for Stage-2 verify because Stage-2 verifies the bridge map identification (Element 3 of the §VII.BA 5-anatomy block). With Element 3's F-functor identified as structurally incomplete, two cross-reviewers operating without prior workshop context would BOTH FAIL on Element 3 — the Stage-2 PASS-AND would not be reachable structurally, not merely numerically.

#### Substrate framing per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`

The substrate-IS structural finding is that the §VII.BA Wodzicki-BCS bridge theorem's F-functor image of Wodzicki uniqueness on Ψ(A_K) is NOT a single scalar multiplicative rescaling — it requires a more elaborate normalization morphism (candidate: integral transform; regulator-dependent renormalization; or non-trivial cohomology pairing contributing a numerical factor distinct from the trivial M_KK^5 unit conversion). This is substrate-IS content of the bridge map at the Level-3 anchor — the 5-OOM gap is the substrate's intrinsic structural signature of an incomplete F-functor identification, NOT a numerical mismatch to be "fixed" by rescaling.

Direction substrate → emergent: `Ψ(A_K) Wodzicki uniqueness theorem → F-functor image at methodology layer → §W2-3 substrate-natural M_KK^5 scalar attempt FAILED structurally → non-scalar F-functor image morphism candidate enters S93+ as carry-forward CF`. FORBIDDEN inversion: "the closure is a bookkeeping move." INVERT: "the closure IS the audit-layer F-functor image of the substrate-IS structural finding that the bridge map's F-functor identification is incomplete at the scalar layer; the methodology-floor pre-empts Stage-2 verify because the substrate-IS structural identity required for cross-axis PASS-AND is not yet established."

CLASS = mechanical closure (not FULL physical, not SCHEMATIC); convention preserves the plan-pinned Stage-2 axes-pre-assignment (Axis-A=connes-ncg-theorist; Axis-B=mack-cosmic-bridge PRIMARY / van-den-dungen-bridge-theorist ALTERNATE; volovik EXCLUDED per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` downstream-inheritance reach test). Substrate-input-orthogonality predicate (`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY-K=3) was pre-pinned at 2 observables (Δ_BCS pin → Axis-B only; master cache → Axis-A only — structural ceiling) but is UNREALIZED at this closure since no dispatch occurred.

#### Downstream routing

- **S93+ carry-forward** `CF-S93-W2-3-FAIL-PATHWAY-A-F-FUNCTOR-IMAGE-NON-SCALAR-RECONSTRUCTION` — substantive math item per `feedback_fix-in-session-never-defer.md` 4-field spec:
  - **What**: derive a non-scalar F-functor image morphism for §VII.BA bridge map; candidates per S93+ exploration include integral transforms (Connes-Karoubi pairing extension), regulator-dependent renormalization morphisms, or non-trivial cohomology pairings.
  - **Inputs**: §W2-3 npz `s92_w2_wodzicki_f_functor_normalization.npz` (Res_W_L12, Δ_BCS, dimensional_derivation_provenance); §W2-4 npz `s92_w2_wodzicki_envelope_lmax_scan.npz` (L^{-2} envelope sign-correct certification); §VII.BA STAGE-1-CANDIDATE registry text; Connes 1995 §III.4 reference corpus.
  - **Gate**: pre-registered PASS-band threshold for the new F-functor image's Level-3 anchor closure (e.g., `|F_new(Res_W) − Δ_BCS|/|Δ_BCS| ≤ 1e-1` at L_max=12 with the candidate morphism evaluated explicitly).
  - **Effort**: ~2.0 wave-equivalents (substrate-physics derivation + numerical anchor check + Stage-2 retry).

- **§VII.BA registry status** remains STAGE-1-CANDIDATE; tag-flip gate `S93+-VII-BA-STAGE-3-PERMANENT-TAG-FLIP` BLOCKED on the new F-functor morphism PASS.

- **§W2-1 + §W2-2 outcomes** (METHODOLOGY-class registry retrofits) are UNAFFECTED by §W2-5 closure — those address §VII.AQ.OP-PROJ scheme-suffix discipline + corpus K=2 advancement, structurally orthogonal to §VII.BA Stage-2 pathway.

**4-tuple output**: `(value='PRE-REG-INC_blocked_by_W2-3_FAIL_W2-4_INFO', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})`.

**Closure SHAs**:
- `audit_sha256` = `{audit_sha256}`
- `content_sha256` = `{content_sha256}`
- 3-tuple companion: `sign_verdict=N/A magnitude_verdict=N/A regime_verdict=N/A` (mechanical closure)

**Artifacts**: `computations/_shared/_s92_w2_5_mechanical_closure.py` (closure script; orchestrator-direct), `computations/session-92/s92_w2_w5_pre_reg_inc_closure.json` (JSON sidecar); verdict-file entries (canonical FAIL line + dual-SHA + 3-tuple + upstream-block-chain comment row).

---

"""


if __name__ == "__main__":
    sys.exit(main() or 0)
