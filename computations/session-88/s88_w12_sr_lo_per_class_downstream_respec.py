"""
S88 W12-144 — S88-SR-LO-PER-CLASS-DOWNSTREAM-RESPEC
====================================================

Downstream-consumer audit of canonical N_breakdown per-class regulator-
tagging coverage per `regulator-pin-discipline.md` §"Tag Format"
extension to N_breakdown.

PRE-COMPUTE AUDIT — Grep results (ripgrep, PCRE-compatible regex):
- per-class-tagged pattern `N_breakdown_(HypA|HypB|HypC|HypD)_FW`: 2 hits
  (both meta-references in plan §W12-144 + WP §W12-144 specifying the
   audit's own pattern; NOT actual canonical-constants usage)
- bare pattern `\bN_breakdown\b`: 67 hits across 10 files including
  computations/_shared/_s87_w9a_2_3_wp_patcher.py (7),
  sessions/permanent-results-registry.md (5), various plan/archive
  files.
- Effective per-class-tagged usage: 0 (all 2 tagged hits are spec
  meta-references)
- Practical per-class-tagged ratio: 2/(2+67) = 2.90%
- Plan PASS threshold: ≥80% per-class-tagged.
- 2.90% < 80% ⇒ FAIL.

VERDICT: FAIL — respec batch required; S89 carry-forward
`S89-N-BREAKDOWN-PER-CLASS-RESPEC-BATCH` registered.

Substitution chain:
  Step 1 (Def): per_class_tagged_ratio := tagged_hits / (tagged_hits + bare_hits)
  Step 2 (Sub): tagged_hits = 2; bare_hits = 67
  Step 3 (Simp): ratio = 2 / (2 + 67) = 0.02898550724637681
  Step 4 (Dir): 0.02898 < 0.80 (pass_threshold) ⇒ FAIL
  Step 5 (Concl): respec batch required; ~67 bare references must be
                  per-class-tagged via regulator-pin-discipline.md §"Tag
                  Format" extended to N_breakdown.
"""

import hashlib
import json
import sys
from pathlib import Path

_THIS = Path(__file__).resolve()
_REPO = _THIS.parent.parent.parent
sys.path.insert(0, str(_REPO / "computations" / "_shared"))
from canonical_constants import tau_fold  # noqa: E402,F401

GATE_ID = "S88-SR-LO-PER-CLASS-DOWNSTREAM-RESPEC"
WP_SECTION = "W12-144"
SCHEME = "downstream-consumer-audit-N_breakdown-per-class-regulator-tagging"
CONVENTION = "regulator-pin-discipline-md-tag-format-extended-to-N_breakdown"

TAGGED_HITS = 2          # (local) ripgrep result on canonical pattern
BARE_HITS = 67           # (local) ripgrep result on bare pattern
PASS_THRESHOLD = 0.80    # (local) plan §W12-144 pin


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(d: dict) -> str:
    return hashlib.sha256(json.dumps(d, sort_keys=True, default=str).encode()).hexdigest()


def main():
    print("=" * 72)
    print(f"GATE {GATE_ID}")
    print("=" * 72)
    print()

    # Substitution chain (step-by-step verification)
    total = TAGGED_HITS + BARE_HITS
    ratio = TAGGED_HITS / total
    pass_predicate = ratio >= PASS_THRESHOLD
    composite_verdict = "PASS" if pass_predicate else "FAIL"
    sign_verdict = "N/A"
    magnitude_verdict = "PASS" if pass_predicate else "FAIL"
    regime_verdict = "VALID"

    print("[Substitution chain]")
    print(f"  Step 1 (Def): per_class_tagged_ratio := tagged / (tagged + bare)")
    print(f"  Step 2 (Sub): tagged_hits = {TAGGED_HITS}; bare_hits = {BARE_HITS}")
    print(f"  Step 3 (Simp): ratio = {TAGGED_HITS}/{total} = {ratio:.6f}")
    print(f"  Step 4 (Dir): {ratio:.4f} < {PASS_THRESHOLD} ⇒ {composite_verdict}")
    print(f"  Step 5 (Concl): respec batch required (~{BARE_HITS} bare references)")
    print()

    plan_path = _REPO / "sessions" / "session-plan" / "session-88-plan-w12.md"
    canonical_constants_path = _REPO / "computations" / "_shared" / "canonical_constants.py"
    reg_pin_rule_path = _REPO / ".claude" / "rules" / "regulator-pin-discipline.md"
    sha_plan = file_sha256(plan_path)
    sha_canonical = file_sha256(canonical_constants_path)
    sha_reg_pin = file_sha256(reg_pin_rule_path)

    input_pin_map = {
        "gate_id": GATE_ID,
        "wp_section": WP_SECTION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "tagged_hits": TAGGED_HITS,
        "bare_hits": BARE_HITS,
        "pass_threshold": PASS_THRESHOLD,
        "input_sha_plan": sha_plan,
        "input_sha_canonical": sha_canonical,
        "input_sha_reg_pin": sha_reg_pin,
    }
    audit_sha = closure_hash(input_pin_map)
    content_sha = closure_hash({
        "ratio": ratio, "verdict": composite_verdict,
        "sign": sign_verdict, "magnitude": magnitude_verdict, "regime": regime_verdict,
    })
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # Save JSON sidecar
    json_path = _REPO / "computations" / "session-88" / "s88_w12_sr_lo_per_class_downstream_respec.json"
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump({
            **input_pin_map,
            "ratio": ratio,
            "composite_verdict": composite_verdict,
            "sign_verdict": sign_verdict,
            "magnitude_verdict": magnitude_verdict,
            "regime_verdict": regime_verdict,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "rationale": (
                f"Per-class-tagged usage = {TAGGED_HITS}/{total} = {ratio:.4%}; "
                f"both tagged hits are meta-references in plan §W12-144 + WP "
                f"(NOT actual canonical-constants usage). Effective usage = 0%. "
                f"Bare hits = {BARE_HITS} across 10 files. Plan PASS threshold "
                f"≥80% violated; respec batch required."
            ),
        }, fh, indent=2)

    verdict_file = _REPO / "computations" / "session-88" / "s88_gate_verdicts.txt"
    canonical_line = (
        f"{GATE_ID}: {composite_verdict} -- "
        f"value='per_class_tagged_ratio={ratio:.6f}_below_pass_threshold_{PASS_THRESHOLD};"
        f"tagged_hits={TAGGED_HITS}_meta_references_only;bare_hits={BARE_HITS}_across_10_files;"
        f"effective_per_class_tagged_usage_zero;respec_batch_required_for_67_bare_references' "
        f"scheme={SCHEME} convention={CONVENTION} L_max=N/A "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )
    triple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2)\n"
    )
    diag = (
        f"# DIAGNOSTIC: ripgrep audit of N_breakdown citations across "
        f"computations/, sessions/framework/registry/, and canonical_constants.py "
        f"shows per-class-tagged ratio 2.90% << pre-reg 80% threshold. "
        f"Per-class regulator discipline NOT YET propagated; substantive respec "
        f"batch required. Top-hit files for bare N_breakdown: "
        f"sessions/session-plan/session-88-plan-w12.md (18); session-87-plan-w9b.md (19); "
        f"computations/_shared/_s87_w9a_2_3_wp_patcher.py (7); permanent-results-registry.md (5). "
        f"S89 carry-forward `S89-N-BREAKDOWN-PER-CLASS-RESPEC-BATCH` registered.\n"
    )
    with open(verdict_file, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(dual_sha)
        fh.write(triple)
        fh.write(diag)
    print(f"\n[done] verdict appended to {verdict_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
