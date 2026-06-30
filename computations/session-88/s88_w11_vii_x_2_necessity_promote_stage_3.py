#!/usr/bin/env python3
"""
S88 W11-133 — S88-VII-X-2-NECESSITY-PROMOTE-STAGE-3

Plan §W11-133: verify 6/6 NECESSITY anchors + Stage-2 cross-axis verify
+ promote §VII.X.2 STAGE-1-CANDIDATE → STAGE-3-PERMANENT.

Plan threshold:
  PASS iff (i) 6/6 anchor SHAs in s88 verdict file
        AND (ii) connes Stage-2 cross-review axis-A PASS + JOINT
        AND (iii) lizzi Stage-2 cross-review axis-B PASS + JOINT
        AND (iv) JOINT logical-AND across both verdicts
  INFO iff (i) AND Stage-2 returns INFO on any clause
  FAIL iff (i) fails OR Stage-2 returns FAIL on any clause

Substitution chain:
  Step 1: anchor_presence = (6/6 audit_sha256 retrievable from on-disk verdict files)
  Step 2: anchors_1_5 = W11-128/W11-129/W11-130/W11-131/W11-132 (just emitted, S88)
          anchor_6 = S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING (S87)
  Step 3: anchor_presence = TRUE (all 6 SHAs full-64-char on disk).
          Stage-2 independence = FALSE (solo execution; no separate cross-reviewer
          dispatch; structural-independence required by joint-theorem-promotion.md §"Stage 2"
          NOT satisfied) → Stage-2 verdict = INFO.
  Step 4: Composite verdict per plan §W11-133 line 343 = INFO (anchors complete;
          Stage-2 deferred to S89 proper cross-axis dispatch).

Solo-mode honest disclosure: per `agent-standards.md §"Completion Verification"`
+ `joint-theorem-promotion.md §"Stage 2"`, the protocol requires TWO INDEPENDENT
cross-reviewers on DIFFERENT axes operating WITHOUT prior workshop context. In
/rclab-solo mode, the orchestrator is one thread; while corpus-loading per
agent-ownership-takeover satisfies "context for review", it does NOT satisfy
"structural-independence dispatch protocol". This is a discipline-honest INFO,
not a PASS-by-self-cross-check.

Substrate framing: §VII.X.2 NECESSITY is a substrate-IS structural identity on
the algebra-axis-orthogonality K-counter; the joint-theorem-promotion 4-stage
pathway IS the framework's mechanism for converting workshop-internal candidates
into permanent structural theorems via independent cross-axis verification.
The structural-independence requirement is precisely to prevent "shared-context
agreement" failures (epistemic-discipline.md §"What Does NOT Count as Evidence"
item 2). Solo execution honestly defers to a properly-dispatched Stage-2.
"""
import os, sys, json, hashlib, time
from pathlib import Path
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'computations' / '_shared'))
from canonical_constants import M_KK, tau_fold

GATE_ID = "S88-VII-X-2-NECESSITY-PROMOTE-STAGE-3"  # (local)
SCHEME = "joint-theorem-promotion-4-stage"  # (local)
CONVENTION = "2-cross-reviewer-different-axis-no-workshop-context"  # (local)
L_MAX = 10  # (local)
WP_ID = "W11-133"  # (local)
SCHEMA_VERSION = "S87+"  # (local)

VERDICT_FILE_S88 = ROOT / 'computations' / 'session-88' / 's88_gate_verdicts.txt'
VERDICT_FILE_S87 = ROOT / 'computations' / 'session-87' / 's87_gate_verdicts.txt'
REGISTRY_FILE = ROOT / 'sessions' / 'permanent-results-registry.md'

# 6-anchor SHA enumeration set
ANCHOR_GATES = [
    ("S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION", VERDICT_FILE_S88, "1/6"),
    ("S88-LAMBDA-SA-S64-FINITE-L-COMPONENT-SUCCESSOR-EMISSION", VERDICT_FILE_S88, "2/6"),
    ("S88-LAMBDA-SA-S65-CONTINUUM-CONVERSE-WITNESS-EMISSION", VERDICT_FILE_S88, "3/6"),
    ("S88-LAMBDA-SA-S77-A0-R-PROTECTION-SUCCESSOR-EMISSION", VERDICT_FILE_S88, "4/6"),
    ("S88-LAMBDA-SA-C9-S86-W1-RATIO-EMISSION", VERDICT_FILE_S88, "5/6"),
    ("S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING", VERDICT_FILE_S87, "6/6 (W1a-6 original)"),
]


def closure_hash_dict(d):
    return hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")).hexdigest()


def grep_audit_sha(verdict_file, gate_id):
    """Locate gate's most-recent canonical line and extract audit_sha256."""
    with open(verdict_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    matches = [l for l in lines if l.startswith(f"{gate_id}:")]
    if not matches:
        return None
    canonical = matches[-1]  # most recent
    # extract audit_sha256=<64hex>
    import re
    m = re.search(r"audit_sha256=([0-9a-f]{64})", canonical)
    if m:
        return m.group(1)
    return None


def main():
    t0 = time.time()  # (local)
    print(f"[{GATE_ID}] §VII.X.2 NECESSITY STAGE-1 → STAGE-3 promotion check")

    # Step (i): 6 anchor SHA presence
    print("\n  --- Step (i): 6 anchor SHA presence ---")
    anchor_shas = {}  # (local)
    n_present = 0  # (local)
    for gid, vf, label in ANCHOR_GATES:
        sha = grep_audit_sha(vf, gid)
        anchor_shas[gid] = sha
        if sha:
            n_present += 1
            print(f"  ✓ Anchor {label} {gid}: audit_sha256 = {sha}")
        else:
            print(f"  ✗ Anchor {label} {gid}: NOT FOUND in {vf.name}")

    anchor_presence = (n_present == 6)  # (local)
    print(f"\n  Anchor presence: {n_present}/6 → {'TRUE' if anchor_presence else 'FALSE'}")

    # Step (ii) + (iii): Stage-2 cross-axis verify
    # Per joint-theorem-promotion.md §"Stage 2", this requires TWO INDEPENDENT
    # cross-reviewers (connes-ncg-theorist on spectral-functional axis;
    # lizzi-spectral-functional-theorist on NCG-axiomatic axis) operating WITHOUT
    # prior workshop context, dispatched in parallel, JOINT clauses PASS-AND'd.
    #
    # In /rclab-solo mode (this script's execution context):
    #   - One thread (the solo runner) executes all gates
    #   - Per-axis corpus-loading per agent-ownership-takeover provides context
    #     for review but DOES NOT satisfy structural-independence (the corpus
    #     contains the workshop-internal R3 closure synthesis from S87 W1a-6;
    #     no separate cross-reviewer dispatch produces a verdict from-scratch
    #     against the registered Stage-1 entry alone).
    #   - The structural-independence requirement is precisely to prevent
    #     shared-context agreement failures (epistemic-discipline.md §"What
    #     Does NOT Count as Evidence" item 2).
    #
    # Honest disclosure: solo execution CANNOT structurally satisfy Stage-2.
    # Per plan §W11-133 INFO band: "anchors complete but Stage-2 returns INFO
    # on at least one clause; partial promotion deferred to S89".
    print("\n  --- Step (ii)+(iii): Stage-2 cross-axis cross-review ---")
    print("  Solo-mode honest disclosure:")
    print("    Stage-2 protocol per joint-theorem-promotion.md requires TWO")
    print("    INDEPENDENT cross-reviewers on DIFFERENT axes operating WITHOUT")
    print("    prior workshop context. /rclab-solo execution is one thread; the")
    print("    structural-independence dispatch protocol is NOT satisfied.")
    print("    → Stage-2 verdict = INFO (deferred to S89 proper cross-axis dispatch)")
    stage2_axis_a = "INFO_DEFERRED_solo_no_independent_dispatch"  # (local)
    stage2_axis_b = "INFO_DEFERRED_solo_no_independent_dispatch"  # (local)
    stage2_joint_and = "INFO_DEFERRED"  # (local)

    # Composite verdict
    if anchor_presence and stage2_joint_and == "PASS":
        verdict = "PASS"
        reason = "anchors_6_of_6_present AND Stage-2 cross-axis JOINT-AND PASS; STAGE-1-CANDIDATE → STAGE-3-PERMANENT"
        registry_action = "FLIP-STAGE-1-TO-STAGE-3"
    elif anchor_presence:
        verdict = "INFO"
        reason = (f"anchors_6_of_6_present (PASS clause i) but Stage-2 cross-axis dispatched in /rclab-solo "
                  f"single-thread mode CANNOT structurally satisfy joint-theorem-promotion.md "
                  f"§Stage 2 independence requirement; promotion deferred to S89 proper "
                  f"cross-axis dispatch (carry-forward S89-VII-X-2-STAGE-2-INDEPENDENT-VERIFY)")
        registry_action = "STAGE-1-CANDIDATE-PRESERVED_promotion_deferred_S89"
    else:
        verdict = "FAIL"
        reason = f"anchor_presence FAILED: {n_present}/6 SHAs found"
        registry_action = "STAGE-1-CANDIDATE-PRESERVED_anchor_incomplete"

    pinmap = {  # (local)
        "_gate_id": GATE_ID, "_wp_id": WP_ID, "_scheme": SCHEME,
        "_convention": CONVENTION, "_L_max": L_MAX,
        "anchor_presence": anchor_presence,
        "n_anchors_present": n_present,
        "anchor_shas": anchor_shas,
        "stage2_axis_a": stage2_axis_a,
        "stage2_axis_b": stage2_axis_b,
        "stage2_joint_and": stage2_joint_and,
        "registry_action": registry_action,
    }
    audit_sha256 = closure_hash_dict(pinmap)  # (local)

    # Build verdict line value-string with all 6 anchor SHAs short-form
    anchor_sha_list = ";".join(
        f"a{idx+1}={(sha[:16] if sha else 'MISSING')}" for idx, (gid, _, _) in enumerate(ANCHOR_GATES)
        for sha_inner in [anchor_shas[gid]]  # nested-comprehension name capture
        if (sha := sha_inner) is not None or True  # always proceed
    )  # (local) — robust list construction

    # Simpler value-string
    anchor_sha_short = ";".join(
        f"a{i+1}_{(anchor_shas[gid][:8] if anchor_shas[gid] else 'MISS')}"
        for i, (gid, _, _) in enumerate(ANCHOR_GATES)
    )  # (local)

    val_str = (
        f"verdict={verdict};anchor_presence={anchor_presence};n_anchors={n_present}/6;"
        f"anchors_short={anchor_sha_short};"
        f"stage2_axis_a={stage2_axis_a};stage2_axis_b={stage2_axis_b};"
        f"stage2_joint_and={stage2_joint_and};registry_action={registry_action};"
        f"reason={reason}"
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{val_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={{CONTENT_SHA}} schema_version={SCHEMA_VERSION}"
    )  # (local)
    content_sha256 = hashlib.sha256(
        canonical_line.replace("{CONTENT_SHA}", "PLACEHOLDER").encode("utf-8")
    ).hexdigest()  # (local)
    canonical_line = canonical_line.replace("{CONTENT_SHA}", content_sha256)
    short_a = audit_sha256[:16]; short_c = content_sha256[:16]  # (local)
    companion_dual = (
        f"# audit_sha256_short={short_a} content_sha256_short={short_c} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"plan §W11-133 §VII.X.2 STAGE-1 → STAGE-3 promotion check; "
        f"6/6 anchors present; Stage-2 cross-axis deferred S89 (solo single-thread mode)"
    )  # (local)
    sign_v = "PASS" if verdict == "PASS" else ("FAIL" if verdict == "FAIL" else "N/A")
    mag_v = verdict; regime_v = "VALID"
    companion_3t = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"[VERIFY-THEOREM] gate; INFO disclosure: solo-mode Stage-2 cannot satisfy structural-independence per joint-theorem-promotion.md"
    )  # (local)
    companion_meth = (
        f"# methodology_class=METHODOLOGY-M1-artifact-existence "
        f"# {GATE_ID} orchestrator-direct-write per wave-classification.md §Dispatch consequences; "
        f"registry_action={registry_action}"
    )  # (local)

    with open(VERDICT_FILE_S88, "a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_dual + "\n")
        f.write(companion_3t + "\n")
        f.write(companion_meth + "\n")
    print(f"\n  Verdict appended: audit_sha256 = {audit_sha256}")

    # Registry edit: do NOT flip STAGE-1 → STAGE-3 (deferred per joint-theorem-promotion.md)
    print(f"\n  Registry action: {registry_action}")
    print(f"  permanent-results-registry.md §VII.X.2 NOT modified; STAGE-1-CANDIDATE preserved.")
    print(f"  Carry-forward: S89-VII-X-2-STAGE-2-INDEPENDENT-VERIFY (proper 2-agent parallel dispatch)")

    elapsed = time.time() - t0  # (local)
    print(f"\n  Total wall: {elapsed:.2f}s")
    print(f"  Verdict: {verdict} — {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
