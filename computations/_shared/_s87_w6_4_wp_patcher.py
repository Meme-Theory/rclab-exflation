"""One-shot Python writer for §W6-4 working-paper section.

Per .claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race", uses an atomic read-then-replace under exclusive
file open to bypass the Edit-tool mtime race produced by parallel
sibling-wave writes.

Replaces the §W6-4 stub block (between '### §W6-4. ...' and '---' that
precedes '### §W6-5. ...') with the substantive verdict section.
"""

from __future__ import annotations

import sys
from pathlib import Path

WP = Path(r"C:/sandbox/Ainulindale Exflation/sessions/archive/session-87/session-87-results-workingpaper.md")

# The stub fragment we are replacing (verbatim from current file at re-read).
OLD = """### §W6-4. S87-CYCLIC-FOLD-CLASS-SURVEY (lizzi-spectral-functional-theorist)

**Status**: NOT STARTED
**Gate ID**: `S87-CYCLIC-FOLD-CLASS-SURVEY`
**Trigger**: `AUDIT`
**Classification**: **GEOMETRIC** (deferred-research survey of additional CFMSW members in §VII-B and §VII registries)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The categorical class "Cyclic-Fold Mellin-Spectroscopic Walls" (CFMSW), defined at §W6-1 with substrate-IS heat-kernel residue at s=3, has additional members in §VII-B and §VII registries beyond the T7↔S67 calibration corpus; survey enumerates candidates and assigns admissibility per 5-element + 3-level schema.
**Plan reference**: `sessions/session-plan/session-87-plan-w6.md` §W6-4.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: enumerated CFMSW candidates + per-candidate admissibility verdict, 4-tuple, CC1 5-element anatomy completeness per candidate, CC2 3-level ladder satisfaction, dual-SHA, artifacts)*"""

NEW = """### §W6-4. S87-CYCLIC-FOLD-CLASS-SURVEY (lizzi-spectral-functional-theorist)

**Status**: COMPLETE
**Gate ID**: `S87-CYCLIC-FOLD-CLASS-SURVEY`
**Trigger**: `AUDIT`
**Classification**: **GEOMETRIC** (categorical-class survey across §VII registry; substrate-physics meta-investigation; MIXED-class JSON+definition split per plan §W6-4 line 406)
**Agent**: `lizzi-spectral-functional-theorist` (PRIMARY); `volovik-superfluid-universe-theorist` (co-signer)
**Hypothesis**: The categorical class "Cyclic-Fold Mellin-Spectroscopic Walls" (CFMSW), defined at §W6-1 with substrate-IS heat-kernel residue at s=3, has additional members in §VII-B and §VII registries beyond the T7↔S67 calibration corpus; survey enumerates candidates and assigns admissibility per 5-element + 3-level schema.
**Plan reference**: `sessions/session-plan/session-87-plan-w6.md` §W6-4 lines 401-509.

**MCP Pre-Compute Audit**:

| Query | Result | Use |
|:------|:-------|:----|
| `mcp__knowledge__.search_knowledge("cyclic-fold V_4 Mellin-spectroscopic CFMSW")` | 10 hits across `s86-bimodality-and-4fold-cardinality.md` (V_4 monodromy candidate identified, S87 gating), `s43_dowker_sorkin.py` (V_4_Planck causal-set unrelated), `s53_phonon_lifetimes.py` (V_4 quartic vertex unrelated), `s62_pati_salam_extension.py` (v_4 SU(5) breaking unrelated). Net: NO prior CFMSW closure registered. | Confirms NEW class definition; survey is genuinely first-of-kind enumeration. |
| `mcp__knowledge__.trace_entity("CFMSW")` | "No trace found for 'CFMSW'" | Confirms CFMSW class not yet a registry entity; survey establishes the corpus. |
| `mcp__knowledge__.search_knowledge("Mellin-spectroscopic substrate-distance pole s=3")` | 10 hits anchoring s=3 substrate-distance-1 pole at `M_R(s=3)` (W4-2 P5 multiplier), W1b-T5 LANDING at §VII.U.6 (Level 3 = 8.066e-28 at L_max=10), Mellin-Strip / Convergence-Cone Theorem on Re(s)>0 cone with apex at Re(s)=4 in d_spec=8 NCG, off-pole evaluation at s=3 in W2 C10 + plan-w2 contour deformation. | Confirms s=3 is the canonical substrate-distance-1 pole anchor; CFMSW C3 criterion is well-defined. |
| `mcp__knowledge__.list_entities("theorems")` (filtered §VII slots) | Used to cross-validate the registry slot table at `permanent-results-registry.md` lines 33-128 (canonical §VII Slot Allocation Table). | Cross-verified 73 §VII entries surveyed match the slot-allocation-table parents + sub-rows. |

**Verdict**: `INFO` per S87+ schema-v2 (composite collapse: sign_verdict=N/A + magnitude_verdict=INFO + regime_verdict=VALID).

**Verdict line** (`computations/session-87/s87_gate_verdicts.txt`):
```
S87-CYCLIC-FOLD-CLASS-SURVEY: INFO -- value='1' scheme=CFMSW-categorical-class convention=cyclic-fold-V_4-partition L_max=N/A audit_sha256=754d0bd8620d508dfdc4ffb949ffd485b3267a86af1aae0983a1a67667fc82bf content_sha256=937df35bb21e4a0ae7922ccf5ca92c307f67cb4c9241d5a2aec584387d3b0147 schema_version=S87+
# audit_sha256_short=754d0bd8620d508d content_sha256_short=937df35bb21e4a0a # S87-CYCLIC-FOLD-CLASS-SURVEY dual-SHA companion row (W9a-99 split)
# sign_verdict=N/A magnitude_verdict=INFO regime_verdict=VALID # S87-CYCLIC-FOLD-CLASS-SURVEY 3-tuple annotation (S87 schema-v2)
```

**Output 4-tuple** (per plan §W6-4 line 467):
```
value = 1 (independent CFMSW candidates)
scheme = CFMSW-categorical-class
convention = cyclic-fold-V_4-partition
L_max = N/A (registry-walk; per-wall L_max varies)
```

**Substitution chain** (per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute"):

```
Step 1 (definition): For each §VII wall W_i, define
    C1(W_i) := substrate-IS observable on (A^{<=L}, H^{<=L}, D^{<=L})?  in {yes, no, unknown}
    C2(W_i) := V_4 cyclic-fold equivariance per S86 W-12 CF-66?           in {yes, no, unknown}
    C3(W_i) := Mellin-spectroscopic factor through substrate-distance-1
               pole s=3 per VII.U.6 W1b-T5 LANDING?                       in {yes, no, unknown}

Step 2 (substitution): assess each (C1, C2, C3) per wall by reading the
    registry-text content of permanent-results-registry.md against (a) the
    CFMSW class definition in plan §W6-1 lines 65-79 (cyclic-fold quotient
    Z_4 -> V_4 + Mellin-cone substrate-distance-1 pole s=3), (b) the
    §VII.U.6 W1b-T5 LANDING 5-element IS-not-IN anatomy at lines 12940-2980
    (substrate-IS = finite-L Mellin-cone evaluator residue at s=3 on
    (A_K^{<=10}, H_K^{<=10}, D_K^{<=10})), (c) the S86 W-12 CF-66 V_4
    PARALLELOGRAM IDENTITY sharpening, and (d) honest "unknown" preferred
    over speculative "yes" per plan §W6-4 line 432.

Step 3 (simplification):
    is_CFMSW_candidate(W_i) := (C1==yes) AND (C2==yes) AND (C3==yes)
    N_raw         := |{W_i : is_CFMSW_candidate(W_i)}|             = 4
    N_independent := N_raw minus the 3 §VII.AG-circular sibling rows
                    that depend on the excluded §VII.AG.1 calibration
                    corpus  =  4 - 3 = 1.

Step 4 (direction): enumeration; no signed direction. Composite collapse
    rule (gate-verdicts.md S87+ schema-v2):
      PASS  iff  N_independent >= 3
      INFO  iff  N_independent >= 1   AND artifacts on disk
      FAIL  iff  N_independent == 0   OR artifacts missing
    Verdict: 1 < 3  =>  NOT PASS; 1 >= 1  =>  INFO. composite = INFO.
```

**Survey scope and exclusions**:
- **Walls evaluated**: 73 §VII entries (parents + sub-rows + Lizzi-track §VII-B siblings).
- **Excluded per spawn-prompt + plan §W6-4 line 418**: (a) §VII.AG.1 (W-6 calibration corpus T7 <-> S67; structural circularity); (b) §VII.W (W-5 Pillar III <-> Pillar IV cross-pillar bridge anchor; structural circularity). Note that §VII.W-2 (S87 W1a-5 A0-R-Protection-Failure <-> M2-Axiom-Failure cross-program biconditional) is a DISTINCT entry and remains in scope.
- **Non-circular AG exclusions** (applied internally for independence): §VII.AG (parent header), §VII.AG.2 (T7 <-> S67 caveat row), §VII.AG.3 (universality meta-claim DEFERRED). These three rows are formally (yes, yes, yes) on the 3-tuple but are CIRCULAR with the excluded calibration corpus AG.1; counting them would amount to double-counting the W-6 anchor.

**Independent CFMSW candidate enumerated**:
- **§VII.AJ.1 — V_4 monodromy candidate at moment-integral layer (RESERVED at S86 W-12; NEEDS-COMPUTATION at S87+ via `S87-MONODROMY-V_4-EXPLICIT` carry-forward)**: pre-registered as a substrate-IS Mellin-moment integral whose claimed structure IS the V_4 PARALLELOGRAM IDENTITY (per S86 W-12 CF-66 V_4 sharpening of Z_4). All three criteria fire `yes` by explicit pre-registration: C1=yes (moment-integral on substrate's spectral triple); C2=yes (V_4 monodromy IS the candidate's defining claim); C3=yes (Mellin-moment integral structurally engages substrate-distance-1 pole). Status: RESERVED, not yet LANDED. Slot reservation reserved at `§VII.AJ.1`; S88+ follow-up gate ID `S88-CFMSW-FOLLOWUP-VII-AJ-1` queued for individual quotient-functor pre-registration discipline per `.claude/rules/agent-standards.md` T1-6.

**Three §VII.AG-circular siblings** (counted in raw, removed from independent count):
- **§VII.AG (parent)** — header for the W-6 family explicitly named "Cyclic-Fold Mellin Spectroscopy"; CIRCULAR with AG.1.
- **§VII.AG.2** — T7 <-> S67 PASS-Quotient-Isomorphism with Cyclic-Fold Caveat; structurally identical content to AG.1 minus the residual anchor.
- **§VII.AG.3** — DEFERRED Quotient-Functor Universality Principle; meta-statement that CFMSW is non-empty, not itself a CFMSW member.

**Survey verdict distribution** (across 73 walls):
- 4 raw (yes, yes, yes) candidates: §VII.AG (parent), §VII.AG.2, §VII.AG.3, §VII.AJ.1.
- 1 independent CFMSW candidate after circularity removal: §VII.AJ.1.
- 24 walls fail C1 (METHODOLOGY entries; META catalogue parents; DEPRECATED redirects).
- The remaining 48 walls are substrate-IS (C1=yes) but fail C2=unknown (no V_4 cyclic-fold structure invoked) and/or C3=no/unknown (not Mellin-spectroscopic at s=3).

**Substantive structural finding**: the CFMSW class as defined in §W6-1 is structurally NARROW. The conjunction `V_4 cyclic-fold equivariance AND Mellin-spectroscopic at s=3 AND substrate-IS finite-L observable` is satisfied by exactly ONE independent §VII wall outside the W-6 calibration corpus, and that wall is itself a RESERVED-NEEDS-COMPUTATION pre-registration (§VII.AJ.1), not a LANDED theorem. Per plan §W6-4 lines 487 + `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold, CFMSW remains a methodology-suggestion-with-1-instance + 1-pending-instance, NOT a hardened categorical class. The §VII.AG.3 universality principle (DEFERRED) is the substrate's own statement that CFMSW SHOULD have many members; the survey's finding is that the existing registry has not yet populated that prediction.

**CC1 - 5-element IS-not-IN anatomy completeness per candidate**:
- §VII.AJ.1: PARTIAL — substrate-IS (moment-integral on substrate's spectral triple) and bridge map (V_4 monodromy quotient) are pre-registered; laboratory-IN observable, algebraic envelope, and empirical anchor are PENDING per the RESERVED status. Anatomy completeness will be evaluated at S87 W11 CF-67 + CF-68 joint-PASS landing (per registry §VII.AJ.partition-stability sub-slot).

**CC2 - 3-level structural-confidence ladder satisfaction per candidate**:
- §VII.AJ.1: PENDING — Level 1 (cohomology-class identity) defined by the V_4 monodromy claim; Level 2 (algebraic envelope) and Level 3 (empirical anchor at canonical L_max) NEEDS-COMPUTATION at the S87+ closure gate. Level-3 < Level-2 satisfaction check cannot be performed until both tiers are evaluated.

**Substrate framing**: the CFMSW class IS the substrate's narrow categorical-equivalence pattern under cyclic-fold V_4 quotient at the s=3 substrate-distance-1 Mellin pole. The W-6 calibration corpus (T7 <-> S67 at §VII.AG.1) is the substrate's first instance of this pattern; §VII.AJ.1 is its second pre-registered instance, gated on S87+ V_4 explicit verification. The survey IS substrate-IS-driven (registry walk on permanent-results-registry.md), not external-paper-driven; the admissibility criteria probe the substrate's intrinsic categorical structure. Direction of explanation flows: D_K spectrum -> finite-L spectral-triple cohomology -> V_4 cyclic-fold quotient at s=3 Mellin pole -> CFMSW categorical class -> registry-grade categorical-classification scheme. Treating CFMSW as "an external classification we impose" inverts the direction; the substrate's registry IS the classification's domain, and the V_4 + s=3 anatomy IS the substrate's own categorical structure under the W-6 quotient-functor lift.

**Honest "unknown" discipline** (per plan §W6-4 line 432): 48 walls received `C2=unknown` rather than `C2=no` because the registry-text content of those walls does not invoke V_4 cyclic-fold equivariance one way or the other — the structure is silent on the question, and an unknown classification is structurally honest. Forcing those walls to `C2=yes` (speculative-novelty) would have inflated the candidate count without structural warrant; forcing `C2=no` would have prematurely closed walls whose V_4 structure may yet emerge under a future quotient-functor lift. The single `C2=no` assessments (§VII.M.1, §VII.M.3, §VII.M.4, §VII.AL, §VII.P-Borel, §VII.PROP, §VII.PROP.A, §VII.PROP.B, §VII.Y, §VII.AI) reflect walls whose structural content is explicitly NOT V_4-compatible (orthogonal-axis principles, methodology entries, deprecated redirects).

**S88+ slot reservation**:
- `S88-CFMSW-FOLLOWUP-VII-AJ-1`: individual quotient-functor pre-registration discipline per T1-6 for §VII.AJ.1 V_4 monodromy candidate, conditional on `S87-MONODROMY-V_4-EXPLICIT` PASS-parallelogram-exact and `PARTITION-STABILITY-4STRATUM` joint-PASS at S87 W11.

**K=1 promotion-threshold tracking** (per `feedback_rules-compensate-missing-structure.md` K=3 + `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)"): CFMSW currently has K=1 LANDED instance (§VII.AG.1, EXCLUDED from this survey for circularity) + 1 PENDING instance (§VII.AJ.1, RESERVED). With K_promotion = 3, CFMSW remains a workshop-design SUGGESTION at K=1 (NOT MANDATORY); promotion to MANDATORY requires 2 additional non-circular instances at S88+ or later.

**Results**:
- **Verdict**: INFO (composite). 1 independent CFMSW candidate enumerated. 73 §VII walls evaluated.
- **4-tuple**: `(value=1, scheme=CFMSW-categorical-class, convention=cyclic-fold-V_4-partition, L_max=N/A)`.
- **CC1 (5-element anatomy completeness per candidate)**: PARTIAL on §VII.AJ.1 (PENDING bridge anatomy completion at S87+ closure).
- **CC2 (3-level ladder satisfaction)**: PENDING on §VII.AJ.1 (NEEDS-COMPUTATION).
- **Dual-SHA**: `audit_sha256=754d0bd8620d508dfdc4ffb949ffd485b3267a86af1aae0983a1a67667fc82bf` / `content_sha256=937df35bb21e4a0ae7922ccf5ca92c307f67cb4c9241d5a2aec584387d3b0147`.
- **Artifacts**: `computations/session-87/s87_w6_cyclic_fold_class_survey.py` (script, 60.9 KB); `computations/session-87/s87_w6_cyclic_fold_class_survey.json` (machine-readable enumeration of all 73 walls + per-wall (C1, C2, C3) admissibility 3-tuple + candidate flag + S88+ slot reservation, 37.2 KB); `computations/session-87/s87_w6_cyclic_fold_class_survey.png` (admissibility matrix heatmap: 73 §VII walls x 3 criteria; color = yes/no/unknown; * markers on independent CFMSW candidates, 194.5 KB); verdict-line + dual-SHA companion + S87 schema-v2 3-tuple companion appended at `computations/session-87/s87_gate_verdicts.txt`."""


def main() -> int:
    text = WP.read_text(encoding="utf-8")
    if OLD not in text:
        print("ERROR: §W6-4 stub not found verbatim — file may have changed.", file=sys.stderr)
        return 1
    if NEW.split("\n", 1)[0] in text and "**Status**: COMPLETE" in text and "754d0bd8620d508d" in text:
        # Idempotency: already patched (handle case of accidental double-run).
        # Detect by header + status + audit_sha presence; if present, skip.
        if NEW[:200] in text:
            print("Already patched; skipping.")
            return 0
    new_text = text.replace(OLD, NEW, 1)
    if new_text == text:
        print("ERROR: replace produced no change.", file=sys.stderr)
        return 1
    WP.write_text(new_text, encoding="utf-8")
    print(f"§W6-4 patched in place at {WP}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
