#!/usr/bin/env python3
"""S91 W0 R2 — Append 15 W2-1..W2-15 registry entries to methodology-wave-instances.md.

Per `.claude/rules/methodology-wave-allowlist.md` §"Edit discipline" item 4
(canonical append-helper pattern): writes rationale-prose entries to
`sessions/framework/registry/methodology-wave-instances.md` keyed by the
`### {gate_label} ({session}) — {sha}` heading per the post-W9-RULE-CLEANUP
schema (allowlist holds 3-column rows; registry holds rationale prose).

Format mirrored from existing W7-6 entry (lines 1858-1878 of registry file):
  - ### {gate_label} ({session}) — {sha256_of_plan_block}
  - **Provenance**: gate-ID + agent role + plan reference + sha citation
  - **Action / Rule extension**: structural summary of what the gate did
  - **Gate classification (M1∧M2∧M3∧M4 conjunction)**: per-test rationale
  - **Closure conditions**: verdict + audit_sha256 + content_sha256
  - **Cross-link**: rule files, registry sections, prior precedents
  - **Carry-forward** (where applicable): forward gate IDs for S91+
  - **Substrate framing**: layer-functor F image declaration

Source data:
  - Plan-block SHAs from `s91_w0_r2_w2_allowlist_shas.json` (this session)
  - Verdict-line audit_sha256s from `computations/session-90/s90_gate_verdicts.txt`
  - Gate titles from plan file `sessions/session-plan/session-90-plan-w2.md`

Per `feedback_no-asking-just-execute.md` housekeeping discipline:
in-session orchestrator-direct-write completion of the 15-row batch.
"""
import json
import sys
from pathlib import Path

# Canonical-constants import per `computations/_shared/CLAUDE.md` MANDATORY discipline.
# This script computes SHAs + emits text, doesn't actively use framework constants,
# but the import satisfies the project rule.
_SHARED_DIR = Path(__file__).resolve().parent  # (local) script-dir resolver
sys.path.insert(0, str(_SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403,E402
except Exception as _e:
    print(f"WARNING: canonical_constants.py import failed: {_e}", file=sys.stderr)

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) project root
INSTANCES_FILE = REPO_ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"  # (local)
SHAS_JSON = REPO_ROOT / "computations" / "_shared" / "s91_w0_r2_w2_allowlist_shas.json"  # (local)

# Per-gate rationale dict keyed by gate_label ("W2-1".."W2-15") with:
#   gate_id   : full S90-* gate identifier
#   audit_sha : verdict-line audit_sha256 (full 64-char) from gate-verdicts.txt
#   content_sha: verdict-line content_sha256 (full 64-char)
#   verdict   : PASS|FAIL|INFO at closure
#   summary   : 1-2 sentence structural summary of what the gate accomplished
#   m1_basis  : PASS-predicate-type rationale (artifact-existence-with-substantive-content)
#   m2_basis  : producing-operation-type rationale (Edit/Write on rule-files or registry)
#   m3_basis  : source-of-truth-type rationale (verbatim sub-diff from upstream)
#   cross_link: comma-separated cross-link target paths
#   carry_fwd : forward S91+ dependency (if any)
#   substrate_framing: layer-functor F image one-sentence summary

GATE_ENTRIES = {  # (local) batched 15-entry rationale corpus
    "W2-1": {
        "gate_id": "S90-VII-AAU-VII-AV-WITHDRAWN-IN-FAVOR-OF-S90-LANDING-CLEANUP",
        "audit_sha": "b11aa86295cc973169eba137a6b1e26a27ddf13315aa778cb77d0348a25bf7a1",
        "content_sha": "af1d66304fdc138233af962d83ca80053e57f6b1bcaa57dfe55669b560dff99e",
        "verdict": "PASS",
        "cf": "CF-18",
        "summary": "Registry-hygiene cleanup retracting §VII.AAU + §VII.AV slot-pre-allocations made redundant by S90 W7 CF-45 chirality-rescoping (which superseded those slot reservations with §VII.AT.OP-PROJ + §VII.AW.OP-PROJ landings). 6-of-6 checks: AAU supersedes pin + AU provenance pin + AV supersedes pin + line-drift handling via anchor-text matching + AFTER-pattern compliance + dual-registration cross-link.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: §VII.AAU slot text retraction landed AND §VII.AV slot text annotation landed AND supersedes-chain cross-links emitted AND 6-of-6 checks pass. Not a numerical comparison.",
        "m2_basis": "Producing operations: `Edit` on `sessions/permanent-results-registry.md` for §VII.AAU + §VII.AV slot retraction; static-string grep for 6-of-6 post-edit verification. NO numerical computation; NO eigenvalue evaluation.",
        "m3_basis": "Verbatim sub-diff from S90 W7 CF-45 chirality-rescoping landing (W7-6 instance entry at registry lines 1858-1878); §VII.AAU + §VII.AV slot reservations originally pre-allocated at S89, rendered redundant by W7-6 §VII.AT.OP-PROJ + §VII.AW.OP-PROJ landings.",
        "cross_link": "`sessions/permanent-results-registry.md` §VII.AAU + §VII.AV (retracted); `sessions/framework/registry/methodology-wave-instances.md` ### W7-6 (S90) entry (upstream W7 CF-45 source); `.claude/rules/registry-landing.md §\"Bridge-Landing Script Architecture (single-shot pattern)\"`",
        "carry_fwd": "None (terminal cleanup; downstream §VII.AT + §VII.AW substrate-physics deferred to S91+ per W-5 CF-W5-5 — see W7-6 instance Carry-forward).",
        "substrate_framing": "The §VII.AAU + §VII.AV slot retraction IS the methodology F-image of substrate-IS slot-occupancy reconciliation per `epistemic-discipline.md §\"Layer-Decomposition\"`. The substrate-IS 4-corner cardinality at S90 close is unchanged; the registry-layer cleanup canonicalizes the slot-allocation state consistent with the W7-6 §VII.AT + §VII.AW landings.",
    },
    "W2-2": {
        "gate_id": "S90-VII-NEXT-SUBSTRATE-CLOCK-UNIQUENESS-THEOREM-STAGE-1-CANDIDATE-LANDING",
        "audit_sha": "86d4414497f82dbd30d2ad6bc03299e09dfb9beddc497b0ab2b8c8c71622de85",
        "content_sha": "e1d2cc0761a606a6d3787fcf5e9186b94496f60406b5e30dbd6e3cf75fe78f7c",
        "verdict": "PASS (after Option-A supersedes; original FAIL audit_sha256=da4f9f261a801680c3c01e1389d6e9c66df027e44520704335ed97ac350293ae)",
        "cf": "CF-19",
        "summary": "STAGE-1-CANDIDATE landing for substrate-clock-uniqueness theorem at §VII.AW.OP-PROJ slot (joint-theorem-promotion 4-stage pathway entry). 19-of-19 checks at corrective: 5-criteria saturation evidence + 5-anatomy IS-not-IN + Level-1 single-τ-slice declaration + 5 upstream substrate-physics SHA pins from W3-1/W3-3/W3-4/W3-5/W3-6 + xi_KZ_FW = 0.018760052113614718.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: §VII.AW.OP-PROJ STAGE-1-CANDIDATE registry entry landed AND 5-anatomy + 5-criteria + Level-1 declaration + Stage-1 tag all present AND single-shot AFTER-pattern emission compliant.",
        "m2_basis": "Producing operations: `Edit` on `sessions/permanent-results-registry.md` (§VII.AW.OP-PROJ STAGE-1-CANDIDATE slot creation). Upstream substrate-physics computation references via SHA pins to W3-1/3/4/5/6 verdict lines (those gates were COMPUTE-class; this gate is the methodology-layer registry landing of their joint substrate-clock-uniqueness conclusion).",
        "m3_basis": "Verbatim sub-diff from W3-1 (xi_KZ extraction) + W3-3 (cocycle evaluation) + W3-4 (V_4-symmetry verify) + W3-5 (clock candidate scan) + W3-6 (uniqueness PASS-AND aggregation) per plan §W2-2; 5-anatomy specification from `cross-pillar-bridge-anatomy.md §\"Forward template-adoption\"` STAGE-1-CANDIDATE template.",
        "cross_link": "`sessions/permanent-results-registry.md` §VII.AW.OP-PROJ STAGE-1-CANDIDATE; `.claude/rules/joint-theorem-promotion.md §\"Stage 1\"`; `.claude/rules/cross-pillar-bridge-anatomy.md §\"Forward template-adoption\"`; `.claude/rules/phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"` Level-1 K=2 MANDATORY; W3-1 / W3-3 / W3-4 / W3-5 / W3-6 verdict lines in `computations/session-90/s90_gate_verdicts.txt`",
        "carry_fwd": "(1) `S91-VII-AW-OP-PROJ-STAGE-2-CROSS-AXIS-VERIFY` — Stage-2 PASS-AND with two cross-reviewers on opposite axes (Axis-A and Axis-B; EXCLUDED reviewers = workshop authors per joint-theorem-promotion.md Stage-2 protocol). (2) S90 W2 CF-19 sub-step originally proposed a 5-criteria substrate-clock-uniqueness Stage-1 verify; substrate-physics intact in upstream W3-* gates; Stage-2 is the next promotion event in 4-stage pathway.",
        "substrate_framing": "The Stage-1-CANDIDATE landing IS the methodology F-image of substrate-IS clock-candidate-uniqueness at the spectral-triple algebra layer per `epistemic-discipline.md §\"Layer-Decomposition\"`. The substrate-IS observable is xi_KZ_FW = 0.018760052113614718 derived from upstream W3-* gates; the registry layer encodes this as a STAGE-1-CANDIDATE entry pending Stage-2 cross-axis verification.",
    },
    "W2-3": {
        "gate_id": "S90-VII-AH-STAGE-3-PERMANENT-PROMOTION",
        "audit_sha": "a9a8d4c2691f5042481477f5a37958345d42c7c47f8e52755c6106bfc8ab7978",
        "content_sha": "46b608bb4808b7c6027c3e886636b9111f2105b21778f9d5b87024f9391d8bb7",
        "verdict": "PASS",
        "cf": "CF-20",
        "summary": "FIRST framework cross-axis joint theorem to reach STAGE-3-PERMANENT eligibility. §VII.AH (substrate-input-orthogonality + obs2/obs3 PASS-AND at structural ceiling per S89 W4-7 Stage-2 audit_sha256=4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a). Advances joint-theorem-promotion substrate-input-orthogonality clause K-counter K=2 → K=3 (SUGGESTION → MANDATORY promotion). 8-of-8 checks pass.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: §VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT tag promotion landed in registry AND K-counter advancement landed in `joint-theorem-promotion.md` AND two-file atomic edit verified.",
        "m2_basis": "Producing operations: `Edit` on `sessions/permanent-results-registry.md` (STAGE-1-CANDIDATE → STAGE-3-PERMANENT tag update at §VII.AH) + `Edit` on `.claude/rules/joint-theorem-promotion.md §\"Substrate-input-orthogonality clause\"` (K=2 → K=3 promotion event + status SUGGESTION → MANDATORY). No numerical computation.",
        "m3_basis": "Verbatim K-counter advancement event derived from S89 W4-7 Stage-2 PASS-AND result (obs2 + obs3 PASS 8/8 at structural ceiling; FIRST instance WITHOUT substrate-input-overlap caveat); rule extension verbatim from joint-theorem-promotion.md §\"Substrate-input-orthogonality clause\" calibration corpus K=2 entry which pre-registered the K=3 promotion predicate.",
        "cross_link": "`sessions/permanent-results-registry.md` §VII.AH STAGE-3-PERMANENT; `.claude/rules/joint-theorem-promotion.md §\"Stage 2\"` Axis-B Selection Protocol + §\"Substrate-input-orthogonality clause\"`; `computations/session-89/s89_gate_verdicts.txt:80` S89 W4-7 Stage-2 verdict audit_sha256=4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a",
        "carry_fwd": "Forward calibration: K=3 MANDATORY status applies to ALL Stage-2 PASS-AND dispatches at S91+; substrate-input-orthogonality predicate becomes structural ceiling for joint-theorem Stage-2 verifications. NEXT framework theorem to enter the pathway: §VII.U.2 Corner II Var_a STAGE-1-CANDIDATE (W6 CF-51 landing; awaits S91 Stage-2 dispatch).",
        "substrate_framing": "The STAGE-3-PERMANENT promotion IS the methodology F-image of substrate-input-orthogonality at the joint-theorem K-counter layer per `epistemic-discipline.md §\"Layer-Decomposition\"`. Direction of explanation: substrate-IS structural-input independence on obs2/obs3 (different data files, distinct decision pipelines) → methodology K-counter advancement → registry STAGE-3-PERMANENT tag. The promotion does NOT add new substrate physics; it canonicalizes pre-existing substrate-IS structural orthogonality at the methodology-rule layer.",
    },
    "W2-4": {
        "gate_id": "S90-VII-W-3-LAB-ELEMENT-2-OE-FORM-RETROFIT",
        "audit_sha": "51e85090b49da9948a3beff5d6128118374c411d635c388a7eeda5fcc2a06350",
        "content_sha": "11bd540f95b4c49cb7afd50fbfaf766b08b6a5e944c896e5467e0ad719edd446",
        "verdict": "PASS",
        "cf": "CF-21",
        "summary": "Element-2 OE-form retrofit on §VII.W-3.LAB STAGE-1-CANDIDATE entries (the 3He-B + 3He-A inheritance-falsifier W11-C5 + W11-C6 calibration corpus). Names canonical projectors Π^vortex_B-phase + Π^µSR_A-phase replacing prose-only Element-2 specifications. Advances Element-2-OE-form K-counter K=2 → K=3 (S86 W-5 W11-C5 + W11-C6 K=2 → W2-4 K=3 MANDATORY at plan-freeze).",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: §VII.W-3.LAB OE-form Element-2 specifications landed (`Π^vortex_B-phase` + `Π^µSR_A-phase` projector names present) AND positive-match regex satisfied AND prose-anchor retired AND W4-3 INFO → PASS retroactive promotion documented. 12-of-12 checks.",
        "m2_basis": "Producing operations: `Edit` on `sessions/permanent-results-registry.md` §VII.W-3.LAB (Element-2 specification update for W11-C5 + W11-C6 sub-entries) + `Edit` on `.claude/rules/cross-pillar-bridge-anatomy.md §\"Element 2 OE-form discipline\"` (K=2 → K=3 promotion event + status MANDATORY at S88+ plan-freeze restated).",
        "m3_basis": "Verbatim 2-instance batch retrofit per the cross-pillar-bridge-anatomy.md K-counter advancement: prose-only Element-2 specifications at W11-C5 + W11-C6 replaced with OE-form (`\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_-]+\\)` pattern match). Calibration corpus updated per the rule's §\"Element 2 OE-form discipline\" calibration table.",
        "cross_link": "`sessions/permanent-results-registry.md` §VII.W-3.LAB W11-C5 + W11-C6 sub-entries; `.claude/rules/cross-pillar-bridge-anatomy.md §\"Element 2 OE-form discipline\"`; `sessions/framework/registry/cross-pillar-bridge-corpus.md §2` Element-2 OE-form calibration corpus; `.claude/rules/inheritance-falsifier-protocol.md` calibration corpus (W11-C5 + W11-C6)",
        "carry_fwd": "None (K=3 MANDATORY promotion saturates the K-counter; forward S91+ Element-2 specifications MUST satisfy OE-form regex at plan-freeze per the rule's now-MANDATORY status).",
        "substrate_framing": "The OE-form retrofit IS the methodology F-image of substrate-IS projector-trace structure per `epistemic-discipline.md §\"Layer-Decomposition\"`. The substrate IS the projector Π acting on the BdG sub-algebra; the laboratory-IN observable IS the integrated trace over the BZ (B-phase) or µSR ensemble (A-phase). The OE-form `∫_{BZ} Tr(Π^vortex_B-phase) dk` makes the substrate ↔ laboratory bridge map explicit at the registry-text layer.",
    },
    "W2-5": {
        "gate_id": "S90-VII-AR-STAGE-2-PENDING-A36-SUB-CLAIM-ADVANCEMENT",
        "audit_sha": "8b6ac827d81effac95ad6efb2182c1b4c8711c67a0593f84391c201bbe97690a",
        "content_sha": "0bc9b60e3d795754772ba30f7d1cae2f3f749ae92468fc13c7b6017f2c07460f",
        "verdict": "FAIL (PRE-REG-INC mechanical closure; blocked on W8 CF-60 FULL-TIER W7a-74 PRIMARY evaluator PASS-A or PASS-B; deferred to S91+)",
        "cf": "CF-22",
        "summary": "Mechanical-closure verdict-line emission for §VII.AR Stage-2 advancement pending W8 CF-60 prerequisite. CF-60 PASS not found in S90 verdict log → §VII.AR registry text unchanged at STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION; substrate-physics intact; W5-7 upstream audit pin captured. Mechanical-closure-discipline ALL-5-CLAUSES PASS.",
        "m1_basis": "PASS-predicate (under mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\") is artifact-existence-with-substantive-content: registry §VII.AR text PRESERVED unchanged at STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION AND PRE-REG-INC verdict line emitted with honest disclosure of blocking prereq + re-dispatch path. FAIL is the structurally-correct closure under upstream-block topology (prereq W8 CF-60 has verdict ≠ PASS).",
        "m2_basis": "Producing operations: NO registry edit (mechanical closure preserves §VII.AR text); single-shot AFTER-pattern verdict-line emission with PRE-REG-INC value-string disclosure. Re-dispatch path is S91+ after CF-60 PASS lands with Option-A `supersedes` tag.",
        "m3_basis": "Verbatim plan-section authority at `session-90-plan-w2.md §W2-5 line 585`; mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\" 5-clause admissibility — all 5 clauses PASS per the verdict value-string. W5-7 upstream cross-tier confirmation gate audit_sha=884db5e02fff4d97 captured as future-dispatch reference.",
        "cross_link": "`sessions/permanent-results-registry.md` §VII.AR (unchanged at STAGE-1-CANDIDATE-PENDING-CROSS-TIER-CONFIRMATION); `.claude/rules/mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\"`; `.claude/rules/gate-verdicts.md §\"Option A — sig_5 remediation pathway under absolute verdict permanence\"` (re-dispatch protocol); `computations/session-90/s90_gate_verdicts.txt:128` CF-55 Reading A verdict (upstream cross-link); `computations/session-89/s89_gate_verdicts.txt:80` W5-7 substrate-physics anchor.",
        "carry_fwd": "(1) `S91-VII-AR-STAGE-2-INDEPENDENT-VERIFY` (re-dispatch after CF-60 PASS): Stage-2 dispatch with Axis-A + Axis-B cross-reviewers + Option-A `supersedes=8b6ac827d81effac95ad6efb2182c1b4c8711c67a0593f84391c201bbe97690a` tag. (2) W8 CF-60 FULL-TIER PRIMARY evaluator dispatch (the upstream prereq this gate is blocked on); W7a-74 PRIMARY evaluator script; effort ~1.0-1.5 we per W-5 CF-W5-5.",
        "substrate_framing": "The PRE-REG-INC mechanical closure IS the methodology F-image of substrate-IS upstream-block topology per `epistemic-discipline.md §\"Layer-Decomposition\"`. Substrate-physics on §VII.AR is intact; the methodology layer encodes the upstream-prereq-pending state via the FAIL verdict's `value='PRE-REG-INC_blocked_by_CF-60_pending'` honest disclosure pattern. This is NOT a substrate failure; it is a registry-state pending-prereq deferral with structurally-correct closure.",
    },
    "W2-6": {
        "gate_id": "S90-VII-AN-REGISTRY-ANCHOR-RECONCILIATION",
        "audit_sha": "8c21b471c1f65ba6a15612276c85edf3730ac5b3f6c1cf42de203a2ac2b17317",
        "content_sha": "ea9928a5fa1b223ea8daa24f9dec0f150298361504d0fec735307d02f817e578",
        "verdict": "PASS",
        "cf": "CF-23",
        "summary": "§VII.AN registry-anchor reconciliation: verifies the cited upstream producing script `s82_w3_9_as_adjacent_obs.py` exists (line count 461, content_sha=f82840affbb544a2) and resolves the W6-2 audit stale-flag. Path-a (script-exists) outcome selected. Closes K=4 NEGATIVE-CALIBRATION corpus instance 4 at `substrate-first-canonical-sourcing.md §(i)`. 7-of-7 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: §VII.AN registry anchor citation verified against upstream producing script existence + content_sha + W6-2 audit stale-flag resolved + provenance annotation added. NOT a numerical comparison.",
        "m2_basis": "Producing operations: filesystem stat + sha256 over `computations/session-82/s82_w3_9_as_adjacent_obs.py` + `Edit` on `sessions/permanent-results-registry.md §VII.AN` provenance annotation. No numerical computation.",
        "m3_basis": "Verbatim from W6-2 audit flag resolution + substrate-first-canonical-sourcing.md §(i) K=4 NEGATIVE-CALIBRATION corpus instance 4 closure. The §VII.AN registry anchor cite verified against upstream filesystem reality.",
        "cross_link": "`sessions/permanent-results-registry.md §VII.AN` (provenance annotation added); `computations/session-82/s82_w3_9_as_adjacent_obs.py` (upstream producing script); `.claude/rules/substrate-first-canonical-sourcing.md §(i)` K=4 corpus instance 4; `computations/_shared/_registry_landing_audit.py` Class-(g) audit (S90 W1-1 K=1 calibration); W5a-44 NEGATIVE-CALIBRATION FAIL audit_sha256=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b",
        "carry_fwd": "Class-(g) audit re-run (S91 W0 R1 — `s88_b32_b33_supersedes_emission.py` + `s82_w3_9_as_adjacent_obs.py` Route-A/B headers added in-session at S91 W0 prep, closes the Class-(g) S2 advisory at PASS).",
        "substrate_framing": "The §VII.AN anchor reconciliation IS the methodology F-image of substrate-IS provenance-chain commutativity per `epistemic-discipline.md §\"Layer-Decomposition\"`. Direction of explanation: substrate-IS upstream script body (`s82_w3_9_as_adjacent_obs.py` 461 lines) → registry-anchor citation → audit-layer Class-(g) verification of F-image commutativity.",
    },
    "W2-7": {
        "gate_id": "S90-W6A-PLAN-FILE-OR-DOWNSTREAM-ANCHOR-RECONCILIATION",
        "audit_sha": "c9775456c6399c21edbe8a324cc485a8be4cbee2fae58a56ba3ba515584a3910",
        "content_sha": "da67d5ccfd44282fdba58705d6e1e362e111208be669768baaf332ad1ff21e2b",
        "verdict": "PASS (after Option-A supersedes; original FAIL audit_sha256=c0fa4b0d80142d27480013c031b5d2fa9d5660468faf8d06cc9e0f73b79f90e2 from git-restore subprocess error)",
        "cf": "CF-24",
        "summary": "Restored `sessions/session-plan/session-88-plan-w6a.md` (641 lines, content_sha=293c7f1ef60692c3) from git commit c008ebfc to resolve downstream citation drift in session-88-w6a-workingpaper + workshops w18/w19/w20. NO canonical_constants provenance entries cite w6a (Path-B unnecessary). 5-of-5 checks. Demonstrates Option-A `supersedes` pattern under script-bug-corrective.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: `session-88-plan-w6a.md` restored (641 lines, content_sha verified) AND downstream citation reachability verified (3 downstream files reference w6a; all resolve post-restore) AND Option-A supersedes successor emitted.",
        "m2_basis": "Producing operations: `git restore --source=c008ebfc -- 'sessions/session-plan/session-88-plan-w6a.md'` (canonical Path-A); post-restore content_sha verification; downstream citation grep (zero canonical_constants cites → no Path-B remediation needed). Option-A `supersedes` corrective trio emission per `gate-verdicts.md §\"Option A — sig_5 remediation pathway\"`.",
        "m3_basis": "Plan §W2-7 specified Path-A (git-restore) as primary recovery; Path-B (downstream citation rewrite) as fallback. Path-A succeeded under corrective (initial attempt FAILed on subprocess error; corrective branch used `commit=c008ebfc` instead of `commit=911763e7` deletion commit). Option-A supersedes tag carries old audit_sha = `c0fa4b0d80142d27480013c031b5d2fa9d5660468faf8d06cc9e0f73b79f90e2`.",
        "cross_link": "`sessions/session-plan/session-88-plan-w6a.md` (restored); `sessions/archive/session-88/session-88-w6a-workingpaper.md` (downstream consumer); `sessions/archive/session-88/workshops/s88-w18-*.md` + `s88-w19-*.md` + `s88-w20-*.md` (downstream consumers); `.claude/rules/gate-verdicts.md §\"Option A — sig_5 remediation pathway under absolute verdict permanence\"` (supersedes protocol)",
        "carry_fwd": "None (recovery complete; downstream consumers now reference restored plan-file).",
        "substrate_framing": "The plan-file restoration IS the methodology F-image of substrate-IS audit-trail permanence per `gate-verdicts.md §\"Option A\"` absolute verdict permanence. The Path-A restoration preserves the substrate-IS audit trail by RE-PRODUCING the historical artifact from git (not editing the verdict file); the Option-A supersedes tag preserves audit-trail integrity at the verdict-file layer (original FAIL retained; corrective PASS appended with supersedes tag).",
    },
    "W2-8": {
        "gate_id": "S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN",
        "audit_sha": "d530a682a3c96e930b2253c32f1dcd1866081c4213aeed47ec374a678a283812",
        "content_sha": "04e60219e3e34385afd44613cc22d7a0a36a90ff3e8cd379b50a722f2ca76c65",
        "verdict": "PASS",
        "cf": "CF-25",
        "summary": "§VII.U.2 Corner-II Reading-B lock-in via three-machinery convergence (Wedderburn + parse-tree + F_traj). 4-axis fingerprint INVARIANT × s=4 × MIXED-RD F_traj × LEVEL-DRESSED-K2-pending. Cell-I retraction annotated. Unblocks W1-CF-2 + W6-CF-49 + W6-CF-51 downstream landings. 7-of-7 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: §VII.U.2 Corner-II Reading-B lock-in text landed AND 4-axis fingerprint (algebra-INVARIANT × Mellin pole s=4 × regulator-invariance MIXED-RD × layer LEVEL-DRESSED) declared AND Cell-I retraction annotated AND clause-(e) parse-tree cross-link present AND 3 downstream gates unblocked.",
        "m2_basis": "Producing operations: `Edit` on `sessions/permanent-results-registry.md §VII.U.2` Corner II row text + Cell I retraction annotation + clause-(e) parse-tree cross-link + W4-30 §VII.AS routing note. No numerical computation; the three-machinery convergence (Wedderburn decomposition + parse-tree decision procedure + F_traj a_2-ratio FI theorem) was upstream substrate-physics work in W6-related computes, this gate is the methodology-layer registry lock-in.",
        "m3_basis": "Verbatim from W-3 R2 + R3 freeze (Reading-B lock-in via three-machinery convergence per `sessions/archive/session-90/workshops/s90-w3-m3c-kernel-cross-morphism-convergence.md`). Three-machinery argument: Wedderburn decomposition (M_3(ℂ)-kernel structure) + parse-tree decision procedure (§VII.U.2 clause (e)) + F_traj a_2-ratio FI theorem (substrate-distance-1 atlas-row at L_k=1) all independently converge on Corner-II classification for Var_a observable.",
        "cross_link": "`sessions/permanent-results-registry.md §VII.U.2` Corner-II Reading-B lock-in (post-W2-8 state); `sessions/archive/session-90/workshops/s90-w3-m3c-kernel-cross-morphism-convergence.md` (Reading-B convergence workshop); `.claude/rules/cross-pillar-bridge-anatomy.md §\"Algebra-axis orthogonality K-counter\"` MANDATORY at K=3 (4-corner classification); `.claude/rules/registry-landing.md §\"Parse-Tree Expansion Pre-Registration\"` (clause (e) parse-tree cross-link)",
        "carry_fwd": "Forward downstream landings now unblocked: (1) W1-CF-2 §VII.U.2 Var_a corrigendum dual-symbol convention (W4 CF-2 landed in S91 W0 prep). (2) W6-CF-49 §VII.AY annotation. (3) W6-CF-51 §VII.U.2 Corner-II Var_a STAGE-1-CANDIDATE landing (landed S90 W6 — see W6-1 instance).",
        "substrate_framing": "The Reading-B lock-in IS the methodology F-image of substrate-IS Corner-II classification at the §VII.U.2 parse-tree decision-procedure layer per `epistemic-discipline.md §\"Layer-Decomposition\"`. The three-machinery convergence at substrate-physics layer (Wedderburn + parse-tree + F_traj) IS the substrate-IS structural evidence; the registry-layer Reading-B lock-in IS the F-image at methodology layer canonicalizing the Corner-II tag.",
    },
    "W2-9": {
        "gate_id": "S90-VII-AF-1-OP-PROJ-ANNOTATION-CLARIFICATION-AND-W5-V4-LINE-401-PARENTHETICAL",
        "audit_sha": "d0e59404e9ebf6ffd1540416af3d72aa01bb03a6697e5d218c56b8a07740a202",
        "content_sha": "cb7b818cbabcb1005770d056cfea7a8af8a7b62ba8798286dd9ce7abf661be8f",
        "verdict": "PASS",
        "cf": "CF-26",
        "summary": "§VII.AF.1.OP-PROJ annotation clarification: disambiguates 3 derived scalars (R_universal = 1.9200 + STRICT_F4 = 1.030902 + err_STRICT = 0.0095%). Adds Conv-9 HP1 near-invariance cite + W5 V4 line 401 parenthetical + q_connes_a verbatim provenance. Joint lizzi + connes CO-SIGN. 8-of-8 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: §VII.AF.1.OP-PROJ annotation block landed with 3-scalar disambiguation + Conv-9 cite + W5 V4 parenthetical + q_connes_a provenance + joint CO-SIGN attribution.",
        "m2_basis": "Producing operations: `Edit` on `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ` annotation block. The 3 derived scalars (R_universal, STRICT_F4, err_STRICT) are pre-existing canonical pins from prior compute waves; this gate is the registry-text annotation clarifying their disambiguation.",
        "m3_basis": "Verbatim from W-2 CF-3 lizzi + connes joint sign-off (workshop wrap-up); q_connes_a paragraph copied verbatim from prior W-2 §V.4 freeze; Conv-9 HP1 near-invariance cite from `sessions/framework/registry/cross-pillar-bridge-corpus.md`.",
        "cross_link": "`sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ` (annotation block landed); `sessions/archive/session-90/workshops/s90-w2-chi-prime-weight-canonicalization.md §V.4` (joint lizzi + connes signoff); `sessions/framework/registry/cross-pillar-bridge-corpus.md §10` Element-3 fiducial-anchor binding; `computations/_shared/canonical_constants.py` (R_universal + STRICT_F4 + err_STRICT canonical pins)",
        "carry_fwd": "None (annotation clarification is terminal; future §VII.AF.1.OP-PROJ landings reference this annotation block for disambiguation).",
        "substrate_framing": "The annotation block IS the methodology F-image of substrate-IS R_universal vs STRICT_F4 vs err_STRICT scalar-distinction per `epistemic-discipline.md §\"Layer-Decomposition\"`. The 3 substrate-IS scalars are structurally distinct moments at substrate-distance-1 pole; the registry-layer annotation makes the distinction visible to downstream consumers without consulting upstream compute workshops.",
    },
    "W2-10": {
        "gate_id": "S90-CANONICAL-CONSTANTS-R-UNIVERSAL-HP1-STRICT-F4-CLASS-D-PROVENANCE-UPDATE",
        "audit_sha": "c46718287e0d2fe0288c165c18f51d35b3548b74726cd820e33d107b12468d11",
        "content_sha": "2dc0e1d50ec446726674fa329ce257b513e37fb33f45ea8397211b5709823281",
        "verdict": "PASS (joint atomic emission with CF-28; shared audit_sha256 reflects two-pin atomic write)",
        "cf": "CF-27",
        "summary": "canonical_constants.py provenance update for R_universal_HP1_STRICT_F4 with Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY tag per `epistemic-discipline.md §\"Source Reconciliation\"` Class-(d). Cross-cites primary canonical eps_H_HP1_norm = 16.197719; derivative relation `1.030902 = 1/0.970024 (modulo publication precision)`. 7-of-7 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: canonical_constants.py PROVENANCE entry for R_universal_HP1_STRICT_F4 added with Class-(d) tag + derivative-relation declaration + cross-cite to eps_H_HP1_norm + name-drift warning for S88 W1b1 lines 129-133.",
        "m2_basis": "Producing operations: `Edit` on `computations/_shared/canonical_constants.py` PROVENANCE dict (R_universal_HP1_STRICT_F4 entry with Class-(d) provenance). Joint atomic with CF-28 (eps_H_HP1_norm primary canonical added in same atomic write).",
        "m3_basis": "Verbatim from `.claude/rules/epistemic-discipline.md §\"Source Reconciliation\"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY taxonomy. Derivative relation `R_universal = 1/eps_H_HP1_norm` substantiated by prior compute workshops; this gate is the canonical_constants provenance landing.",
        "cross_link": "`computations/_shared/canonical_constants.py` PROVENANCE entries for R_universal_HP1_STRICT_F4 + eps_H_HP1_norm (joint atomic emission); `.claude/rules/epistemic-discipline.md §\"Source Reconciliation\"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY; `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ` (downstream consumer); S88 W1b1 lines 129-133 (name-drift warning source)",
        "carry_fwd": "None (provenance landing terminal; future R_universal_HP1_STRICT_F4 citations in downstream gates MUST cite the canonical_constants.py provenance entry, which provides the Class-(d) PIN-DERIVATIVE relation to eps_H_HP1_norm primary canonical).",
        "substrate_framing": "The Class-(d) PIN-DERIVATIVE tag IS the methodology F-image of substrate-IS algebraic-identity relation per `epistemic-discipline.md §\"Layer-Decomposition\"`. The substrate-IS algebraic identity `R_universal * eps_H_HP1_norm = 1` (modulo publication precision); the methodology layer encodes this via cross-citation in the PROVENANCE field rather than independent canonical pinning of both quantities.",
    },
    "W2-11": {
        "gate_id": "S90-CANONICAL-CONSTANTS-EPS-H-HP1-NORM-PROVENANCE-ADDITION",
        "audit_sha": "c46718287e0d2fe0288c165c18f51d35b3548b74726cd820e33d107b12468d11",
        "content_sha": "2dc0e1d50ec446726674fa329ce257b513e37fb33f45ea8397211b5709823281",
        "verdict": "PASS (joint atomic emission with CF-27; shared audit_sha256)",
        "cf": "CF-28",
        "summary": "canonical_constants.py provenance addition for eps_H_HP1_norm primary-canonical tag with BZ-trace definition (ζ regulator + τ_fold=0.190 + L_max=10) + Level-1 single-τ-slice declaration per `phononic-framing.md §\"Single-τ-slice vs moduli-deformation\"` K=2 MANDATORY. Downstream consumer cite to R_universal derivative. 8-of-8 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: canonical_constants.py PROVENANCE entry for eps_H_HP1_norm added with primary-canonical tag + BZ-trace definition + Level-1 declaration + downstream cross-cite.",
        "m2_basis": "Producing operations: `Edit` on `computations/_shared/canonical_constants.py` PROVENANCE dict (eps_H_HP1_norm primary entry). Joint atomic with CF-27 (R_universal_HP1_STRICT_F4 derivative entry added in same atomic write).",
        "m3_basis": "Verbatim from `.claude/rules/phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"` K=2 MANDATORY Level-1 declaration discipline; BZ-trace definition canonical per Connes-Marcolli 2008 ch.1 quantum-metric integrated trace; ζ regulator + τ_fold + L_max pinned per S89 W2-6 substrate-physics computation.",
        "cross_link": "`computations/_shared/canonical_constants.py` PROVENANCE entry for eps_H_HP1_norm; `.claude/rules/phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"` K=2 MANDATORY; `sessions/permanent-results-registry.md §VII.AF.1.OP-PROJ` (downstream consumer citing eps_H_HP1_norm); W2-10 CF-27 (joint atomic emission partner)",
        "carry_fwd": "None (primary-canonical landing terminal; future eps_H_HP1_norm citations consume the canonical_constants.py PROVENANCE entry directly).",
        "substrate_framing": "The eps_H_HP1_norm primary-canonical tag IS the methodology F-image of substrate-IS Level-1 single-τ-slice observable per `phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"`. The substrate IS the BZ-trace integrand `Tr g_ab^{(P_0)}(k; τ_fold)` evaluated at fixed τ_fold = 0.190 with ζ regulator at L_max=10; the methodology layer canonicalizes this as a primary pin with explicit Level-1 declaration discipline.",
    },
    "W2-12": {
        "gate_id": "S90-FALSIFIER-INVENTORY-ROW-3-ALPHA-S-CANONICAL-UPDATE",
        "audit_sha": "92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27",
        "content_sha": "ce2da88eadea84c5b771a5b08e27aeceb7a24dd4a475320b029b715f607dad8d",
        "verdict": "PASS",
        "cf": "CF-29",
        "summary": "falsifier-master-inventory.md Row-3 (α_s_canonical) updated to new substrate value -8587279/100000000 = -0.085 872 79; gap σ = 12.15 vs Planck-2018 / 13.99 vs Aiola-2020; FIRST multi-σ observational falsifier within near-term detector reach. Historical α_s_inflation_framework annotation retained for audit trail. Audit-pin sub-row CF-29 appended below pre-existing row. Route-B identity at substrate-distance-1 pole s=3 canonical. 12-of-12 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: Row-3 updated with new α_s_canonical value AND gap-σ values added AND first-multi-σ-falsifier tag added AND historical annotation retained AND audit-pin sub-row appended AND Route-B identity citation present.",
        "m2_basis": "Producing operations: `Edit` on `sessions/framework/registry/falsifier-master-inventory.md` Row-3 (α_s_canonical) value update + sub-row CF-29 append. mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. No numerical computation; α_s_canonical pin comes from upstream S88 W5a-37 + W8-100 supersedes (canonical_constants `alpha_s_canonical_pin = Fraction(-8587279, 100000000)`).",
        "m3_basis": "Verbatim from `computations/_shared/canonical_constants.py` `alpha_s_canonical_pin` provenance entry (S88 W8-100 Option-A successor landing); gap-σ values verbatim from S89 W7a (audit_sha=01c1ac83569dc92f) and S89 W4-4 (audit_sha=e3da1d13442029a0) substrate-physics anchors; Route-B substrate-distance-1 pole s=3 canonical per §VII.AN-CORRIGENDUM.",
        "cross_link": "`sessions/framework/registry/falsifier-master-inventory.md` Row-3 + audit-pin sub-row CF-29; `computations/_shared/canonical_constants.py` alpha_s_canonical_pin provenance; `sessions/permanent-results-registry.md §VII.AN-CORRIGENDUM` (Route-B canonical); `feedback_mack-bridge-role.md` (mack sole-writer discipline); S89 W7a + W4-4 substrate-physics anchors",
        "carry_fwd": "Forward observational dispatch (S91+): (1) CMB-S4 forecast monitoring (predicted ~38σ detection by 2030 LO; mack-cosmic-bridge polling per `mack-observational-constraints.md` schedule). (2) CMB-HD forecast (predicted ~80σ LO by 2034). (3) Aiola-2020 follow-up if data refresh occurs.",
        "substrate_framing": "The α_s_canonical update IS the methodology F-image of substrate-IS Route-B canonical (n_s² − 1 identity) per `phononic-framing.md §\"IS Space, Not IN Space\"`. Direction of explanation: substrate IS n_s_FW_exact = Fraction(9561, 10000) at substrate-distance-1 pole s=3 → algebraic identity α_s = n_s² − 1 → canonical_constants pin → falsifier-inventory Row-3 → observational detector horizon table. The first-multi-σ-falsifier tag canonicalizes the substrate's first multi-σ observational discriminator.",
    },
    "W2-13": {
        "gate_id": "S90-DR3-BINDING-PROTOCOL-READINESS-AUDIT",
        "audit_sha": "23f662b36cf0afcf5cc4d034f75bfde0e45793ff0afc68cd90152249964342fb",
        "content_sha": "eadb77d46b6c16785953785d187a242c02d2aa9860246236dfa5bafcccce09e0",
        "verdict": "FAIL (3-of-6 readiness items pass; INFO band per pre-registered threshold ≥ 5-of-6 PASS)",
        "cf": "CF-30",
        "summary": "DR3 binding-protocol 6-item readiness audit: item A FAIL + item B PASS + item C PASS + item D PASS + item E FAIL + item F FAIL → 3-of-6 readiness. DR3 window-open date 2026-04-23 (already past); w0_FW canonical = -0.918 (Volovik partition) + w0_FW_R842 = -0.842454 (Branch IV substrate-compaction alternative). FAIL is structurally informative — closes a corridor in the constraint map.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: audit-report JSON at `s90_w2_dr3_binding_protocol_readiness_audit.json` AND 6-item checklist evaluated AND readiness threshold (5-of-6 PASS) tested against measured (3-of-6 PASS) → FAIL under pre-registered threshold. NO ad-hoc relabeling.",
        "m2_basis": "Producing operations: readiness-audit-no-write-expected scheme; `Write` of audit-report JSON; NO registry edit, NO canonical_constants update, NO falsifier-inventory change. The FAIL verdict is data, not a script breakage. 6-item checklist enumeration is deterministic procedural verification per plan §W2-13.",
        "m3_basis": "Verbatim 6-item DR3 binding-protocol checklist from S90 plan §W2-13. Items: (A) DR3 data window status; (B) w0_FW canonical pin present; (C) w0_FW_R842 alternative branch pin present; (D) Branch IV substrate-compaction methodology landed; (E) DR3 likelihood-pipeline ready; (F) DR3 detector-horizon table populated. Each item has a binary PASS/FAIL per pre-registered evidence.",
        "cross_link": "`computations/session-90/s90_w2_dr3_binding_protocol_readiness_audit.json` (audit report); `computations/_shared/canonical_constants.py` w0_FW = -0.918 + w0_FW_R842 = -0.842454; `sessions/framework/registry/mack-observational-constraints.md` (DR3 detector horizon); `.claude/rules/regulator-convention-lockdown.md` DR3 L_max-stability discipline",
        "carry_fwd": "3-gap remediation queued (3 FAILing items A + E + F) for S91+. Per S91 context-file v2 §\"Falsifier watchlist\" item 7: T0.4 already in-session-completed at S91 W0 prep (DR3 detector-horizon table populated in falsifier-master-inventory under T0.6 batch). Remaining 2 items (A + E) for S91 mack-cosmic-bridge sole-writer dispatch.",
        "substrate_framing": "The 3-of-6 FAIL IS the methodology F-image of substrate-IS DR3 binding-protocol readiness state at S90 close. FAIL is structurally informative — closes a corridor in the constraint map per `feedback_reporting-framing.md`. The 3 PASS items (B + C + D) represent substrate-IS w0 canonical + alternative-branch + methodology landed; the 3 FAIL items (A + E + F) represent observational-pipeline + detector-horizon readiness gaps to be closed at S91+.",
    },
    "W2-14": {
        "gate_id": "S90-FALSIFIER-INVENTORY-ROW-2-R-DUAL-PATHWAY-UPDATE",
        "audit_sha": "e95b63d39dcb4500e709e9e14bbe1fdd9127cf932438ca415eecb1517249c39e",
        "content_sha": "4b389ac33011de7df8854c06d14892ad7bba9cfeb6ec98fe2321d8aedcbca927",
        "verdict": "PASS",
        "cf": "CF-31",
        "summary": "falsifier-master-inventory.md Row-2 (r dual-pathway) audit-pin sub-row CF-31 appended. Citations: BK-Array 2026 sha=b1eb9e61ece7b046; LiteBIRD n_T sha=f5a285d8548129b0; S89 W7a/W7b/W4-4 cross-links. Mnemonic-vs-exact K=2 annotation: 16577/31705 = 0.5229 NOT 1/c_sub = 0.4468 (14.54% understatement). σ-band LiteBIRD: 1.6666 to 2.7776 σ. S87 W4-42 plan-pin vs S84 BK pre-reg drift disclosed. 11-of-11 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: Row-2 audit-pin sub-row CF-31 appended AND BK + LiteBIRD + S89 SHA cross-links present AND mnemonic-vs-exact K=2 annotation present AND σ-band declared AND plan-pin drift disclosure present.",
        "m2_basis": "Producing operations: `Edit` on `sessions/framework/registry/falsifier-master-inventory.md` Row-2 (r dual-pathway) audit-pin sub-row append. mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`.",
        "m3_basis": "Verbatim from S86 W-3 RULE-2 mnemonic-vs-exact-ratio discipline at `.claude/rules/math-scripts.md §\"Mnemonic-vs-exact ratio discipline\"`; σ-band 1.6666-2.7776 from S87 W4-42 LiteBIRD discrimination; BK-Array 2026 + LiteBIRD n_T SHA pins from upstream substrate-physics anchors (S89 W7a + W7b + W4-4).",
        "cross_link": "`sessions/framework/registry/falsifier-master-inventory.md` Row-2 audit-pin sub-row CF-31; `.claude/rules/math-scripts.md §\"Mnemonic-vs-exact ratio discipline\"` (K=1 baseline + K=2 annotation); S89 W7a + W7b + W4-4 substrate-physics anchors; S87 W4-42 LiteBIRD discrimination σ-band source",
        "carry_fwd": "Forward observational dispatch: BK-Array 2026 data refresh monitoring + LiteBIRD STRUCTURAL-FLOOR 2032+ detection per `mack-observational-constraints.md` polling schedule.",
        "substrate_framing": "The Row-2 update IS the methodology F-image of substrate-IS r dual-pathway σ-reduction theorem per `phononic-framing.md §\"IS Space, Not IN Space\"`. Substrate-IS Path-H invariant + Path-C shifted under HypA/HypB switching → σ-reduction = 16577/31705 = 0.5229 (Sage-exact) NOT 1/c_sub = 0.4468 (mnemonic). The 14.54% understatement annotation pins the structurally-exact reduction at registry layer.",
    },
    "W2-15": {
        "gate_id": "S90-MACK-OBSERVATIONAL-CONSTRAINTS-S89-UPDATE",
        "audit_sha": "0c4f72aff536ae8567dcef3f11cf41306a693b0f22fca83ed8dc663431cb13b4",
        "content_sha": "52be77e6a3b81c564fbe57ac3e2211271f4e93ecc47c72e9900bba0a1cce2548",
        "verdict": "PASS",
        "cf": "CF-32",
        "summary": "mack-observational-constraints.md S89-close snapshot appended: n_s_FW = 9561/10000 + α_s_canonical = -8587279/100000000 + joint χ²_diag = 43.09 + gap-σ values + first-multi-σ-falsifier tag + detector-horizon table + substrate-framing mandatory paragraph + AMRI-promoted-canonical declaration. CF-29 dependency PASS at audit_sha256 = 92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27. 18-of-18 checks.",
        "m1_basis": "PASS-predicate is artifact-existence-with-substantive-content: S89-close snapshot appended AND all 18 required elements present (canonical pins + gap-σ + detector horizon + substrate framing + AMRI declaration + CF-29 dependency PASS verification + first-multi-σ tag).",
        "m2_basis": "Producing operations: `Edit` on `sessions/framework/registry/mack-observational-constraints.md` (S89-close snapshot append). mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. AMRI-promoted canonical: this registry was AMRI-promoted at S87 W0 (canonical reference snapshot; cross-link table to sister registries falsifier-master-inventory + branch-iv-canonical + pre-registered-observations).",
        "m3_basis": "Verbatim from S89 close synthesis (n_s_FW + α_s_canonical pins + gap-σ values verbatim from upstream substrate-physics anchors); first-multi-σ-falsifier tag promoted from CF-29 (W2-12) dependency at audit_sha=92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27.",
        "cross_link": "`sessions/framework/registry/mack-observational-constraints.md` (S89-close snapshot); `sessions/framework/registry/falsifier-master-inventory.md` Row-3 (CF-29 partner); `computations/_shared/canonical_constants.py` n_s_FW_exact + alpha_s_canonical_pin; `feedback_mack-bridge-role.md` (mack sole-writer); `.claude/rules/agent-standards.md §\"Agent-Memory Registry Inversion (AMRI)\"` (AMRI-promoted canonical history)",
        "carry_fwd": "Forward observational monitoring: CMB-S4 (~2030 LO ~38σ detection) + CMB-HD (~2034 LO ~80σ detection) + Aiola-2020 follow-up. Polling schedule per `mack-observational-constraints.md` polling protocol.",
        "substrate_framing": "The S89-close snapshot IS the methodology F-image of substrate-IS observational-constraint state at S89 close per `phononic-framing.md §\"IS Space, Not IN Space\"`. Direction of explanation: substrate IS n_s_FW + α_s_canonical Fraction-exact pins → canonical_constants entries → mack-observational-constraints snapshot → detector horizon table → observational-pipeline forecast. The AMRI-promoted-canonical declaration acknowledges this registry IS the methodology-layer F-image of mack's domain-expert synthesis of substrate-IS predictions vs observational anchors.",
    },
}

# Plan-block SHAs loaded from JSON sidecar (computed by sister script s91_w0_r2_w2_allowlist_sha_compute.py)
def main():
    if not SHAS_JSON.exists():
        print(f"ERROR: SHAs JSON not found at {SHAS_JSON}", file=sys.stderr)
        sys.exit(1)
    shas_data = json.loads(SHAS_JSON.read_text(encoding="utf-8"))
    sha_by_gate = {b["gate_label"]: b["sha256_of_plan_block"] for b in shas_data}  # (local)

    # Compose append block
    append_block = "\n"  # (local) leading newline for visual separation

    for gate_label in [f"W2-{i}" for i in range(1, 16)]:
        if gate_label not in GATE_ENTRIES:
            print(f"WARNING: missing entry for {gate_label}", file=sys.stderr)
            continue
        e = GATE_ENTRIES[gate_label]
        plan_sha = sha_by_gate.get(gate_label, "MISSING")
        entry = []  # (local) per-gate lines
        entry.append(f"### {gate_label} (S90) — {plan_sha}\n")
        entry.append("\n")
        entry.append(f"**Provenance**: gate-ID `{e['gate_id']}` ({e['cf']}); agent `mack-cosmic-bridge` sole-writer per `feedback_mack-bridge-role.md`; orchestrator-direct-write per `wave-classification.md §\"Dispatch consequences\"`; plan reference `sessions/session-plan/session-90-plan-w2.md §{gate_label}`; plan-block sha256 `{plan_sha}`.\n")
        entry.append("\n")
        entry.append(f"**Action**: {e['summary']}\n")
        entry.append("\n")
        entry.append("**Gate classification (M1∧M2∧M3∧M4 conjunction)**:\n")
        entry.append(f"- **M1** (PASS-predicate type): {e['m1_basis']}\n")
        entry.append(f"- **M2** (producing-operation type): {e['m2_basis']}\n")
        entry.append(f"- **M3** (source-of-truth type): {e['m3_basis']}\n")
        entry.append(f"- **M4** (Allowlist membership): this row appends gate-ID `{gate_label}` to `methodology-wave-allowlist.md` with `sha256_of_plan_block = {plan_sha}` (over the §{gate_label} plan-block from `## §{gate_label}.` heading through next `## §` heading or EOF).\n")
        entry.append("\n")
        entry.append(f"**Closure conditions**: {e['verdict']} verdict (`computations/session-90/s90_gate_verdicts.txt` line emitted at single-shot AFTER-pattern). audit_sha256=`{e['audit_sha']}`; content_sha256=`{e['content_sha']}`.\n")
        entry.append("\n")
        entry.append(f"**Cross-link**: {e['cross_link']}.\n")
        entry.append("\n")
        entry.append(f"**Carry-forward**: {e['carry_fwd']}\n")
        entry.append("\n")
        entry.append(f"**Substrate framing**: {e['substrate_framing']}\n")
        entry.append("\n")
        append_block += "".join(entry)

    # Append to instances file
    if not INSTANCES_FILE.exists():
        print(f"ERROR: instances file not found at {INSTANCES_FILE}", file=sys.stderr)
        sys.exit(1)

    pre_len = INSTANCES_FILE.stat().st_size  # (local)
    with open(INSTANCES_FILE, "a", encoding="utf-8", newline="\n") as f:
        f.write(append_block)
        f.flush()
    post_len = INSTANCES_FILE.stat().st_size  # (local)

    print(f"Append complete: {post_len - pre_len} bytes added ({len(append_block)} bytes in block).")
    print(f"15 W2 entries (W2-1..W2-15) appended to {INSTANCES_FILE.name}")


if __name__ == "__main__":
    main()
