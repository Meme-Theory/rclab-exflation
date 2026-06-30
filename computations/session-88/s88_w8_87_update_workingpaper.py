#!/usr/bin/env python3
"""
S88 W8-87 — Working-paper §W8-87 atomic block-replace helper.

Per .claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race", concurrent editors race the Edit tool's mtime
check; the canonical pattern is a Python writer that does a targeted
read-replace-write within a single open() handle, with an explicit
retry loop on FileExistsError-equivalent failures. We simply use atomic
read-modify-write here: the §W8-87 block has a unique header so the
replacement is idempotent and cannot collide with §W8-88..§W8-100.
"""

from __future__ import annotations

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SESSION_DIR.parent.parent
WP_PATH = PROJECT_ROOT / "sessions" / "session-88" / "session-88-w8-workingpaper.md"

OLD_BLOCK_MARKER = "### §W8-87. S88-CONSENSUS-INDEPENDENCE-TEST-LANDING (gen-physicist)"
NEXT_BLOCK_MARKER = "### §W8-88."

NEW_BLOCK = """### §W8-87. S88-CONSENSUS-INDEPENDENCE-TEST-LANDING (gen-physicist)

**Status**: COMPLETE
**Gate ID**: `S88-CONSENSUS-INDEPENDENCE-TEST-LANDING`
**Trigger**: `Wave-0 plan-freeze; methodology rule-file edit`
**Classification**: **METHODOLOGY** (M1 artifact-existence; M2 Edit-only; M3 verbatim from plan §W8-87 Steps 1–5 + S87 W6-1 §VII.AG.1 STAGE-1-CANDIDATE; M4 allowlist row W8-87 appended)
**Agent**: `gen-physicist` (orchestrator sole writer); CO-AUTHOR `lizzi-spectral-functional-theorist` (rationale review embedded below).
**Hypothesis**: A hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv` partitions the cross-pillar-bridge calibration corpus such that §VII.AG.1 (S87 W6-1 quotient-functor isomorphism modulo cyclic-fold V_4) is correctly classified OUTSIDE the K-counter (`SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE`), while §VII.AF.1 (S87 W5-1 / S86 W-5 Pillar III ↔ IV bridge) is the calibration baseline at K=1 SUGGESTION. The post-W4a-17 K=3 MANDATORY corpus (W-5 + W11-5 + W4a-17) remains intact under the Hybrid Independence Test.
**Plan reference**: `sessions/session-plan/session-88-plan-w8.md` §W8-87 (lines 43–77).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):
- `mcp__knowledge__search_knowledge("cross-pillar-bridge-anatomy K-counter independence")` → 10 hits; surfaced `s88_w2_meth_cross_pillar_bridge_anatomy_k_counter_monitor.py` provenance (W-2 monitor showing K_post_S88=2 status BEFORE W4a-17), W4a-17 K=2→K=3 promotion code in `s88_w4a_split_registry_writer.py`, and `S88-METH-CROSS-PILLAR-BRIDGE-ANATOMY-K-COUNTER-MONITOR` INFO verdict. Confirms gate is NOT pre-closed.
- `mcp__knowledge__search_knowledge("VII.AG.1 quotient functor isomorphism cyclic fold W6")` → 5 hits; surfaced `s87_w6_t7_s67_isomorphism_landing.py` provenance with verdict `S87-T7-S67-ISOMORPHISM-LANDING: PASS value='REGISTRY_ENTRY_LANDED_AT_§VII.AG.1; residual_frac=0.0095%; tier3=0.0095%; tier2_envelope=0.10%; tier3/tier2=0.0947; substantive_lines=61; 5_anatomy=PRESENT; 3_tier=PRESENT; STAGE-1-CANDIDATE=PRESENT'`. Confirms §VII.AG.1 has 5-anatomy + 3-tier present; the Independence Test is the discrimination ABOVE 5-anatomy/3-tier presence.
- `mcp__knowledge__search_knowledge("VII.AF.1 W-5 Pillar III IV Peotta Tormaa quantum metric HKR bridge")` → 5 hits; confirms §VII.AF.1 LANDED at S87 W5-1 with `S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` verdict and identical structural pillars (Pillar III ↔ IV, HKR `L_max → ∞`, `L^{-3}` envelope at d=4) to §VII.AG.1 modulo the V_4 cyclic-fold quotient — i.e., §VII.AG.1 is structurally a REFINEMENT not an INDEPENDENT instance.
- `mcp__knowledge__search_knowledge("W4a-17 W4a 17 K counter K=3 promotion MANDATORY VII.W-3")` → 5 hits; confirms K=3 MANDATORY corpus advance landed at S88 W4a-17 close (2026-05-04) prior to plan-w8 freeze. This is the structural reason plan §W8-87 threshold (c) "K=1 (W-5 only)" wording is Class-(c) PIN-DRIFT-FROM-STALE-SOURCE per `.claude/rules/epistemic-discipline.md` §"Source Reconciliation".

**Verdict**: **PASS** (5/5 clauses; per `.claude/rules/gate-verdicts.md` schema-v2; no `[SIGN]` trigger so 3-tuple companion row is N/A).

Verdict line at `computations/session-88/s88_gate_verdicts.txt` (canonical line + dual-SHA companion row):
```
S88-CONSENSUS-INDEPENDENCE-TEST-LANDING: PASS -- value='a=True;b=True;c=True;d=True;e=True_substantive_lines=22;K_post_S88_W8_87=1_SUGGESTION_independence_test_baseline_W5;K_corpus_below_unchanged=3_MANDATORY_W5_W11_5_W4a_17' scheme=METHODOLOGY-rule-file-edit convention=hybrid-independence-test-i-ii-iii-AND-iv L_max=N/A audit_sha256=23afe890e8439e8b3ff6543c4a4617b22e08a753011481c6bd665e2aa062167e content_sha256=ce7080c133fe7c9e43117740d827f6cf0ff675ce5723159d98769225f41c466a schema_version=S84+
```

**Results**:

**4-tuple**: `(value='a=True;b=True;c=True;d=True;e=True_substantive_lines=22;...', scheme=METHODOLOGY-rule-file-edit, convention=hybrid-independence-test-i-ii-iii-AND-iv, L_max=N/A)`

**Pre-edit input pins** (closure SHA computed from sorted input-pin map):
- `.claude/rules/cross-pillar-bridge-anatomy.md`: `739bc6514be92409...` (256 lines pre-edit)
- `.claude/rules/methodology-wave-allowlist.md`: `2032efccea23d332...`
- `sessions/permanent-results-registry.md`: `2211aa485eeafc69...`
- `sessions/session-plan/session-88-plan-w8.md`: `415fa73ec08b1386...`
- `computations/_shared/canonical_constants.py`: `3f613086c223f65a...`
- Closure: `6621316e93642dda...`
- Plan-block SHA over plan §W8-87 (allowlist `sha256_of_plan_block`): `8b4efec59c3b7b059af12b9b0abed1576cc3a0481938bd0dbc013a65eef73499`

**Post-edit SHAs**:
- `.claude/rules/cross-pillar-bridge-anatomy.md`: `3a42cc0e49e4ad8db90249187d94ea9326145fe95e941ab753bbc76eafa2c599` (+6679 bytes; sub-section inserted at line 147)
- `.claude/rules/methodology-wave-allowlist.md`: `30dddd7c6c01f729d970a402928745abc52aa529b78df5fae132ec73ed5e3eeb` (+1372 bytes; W8-87 row appended at line 148)

**Rule-file diff summary — `.claude/rules/cross-pillar-bridge-anatomy.md`**:

A new sub-section `### Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)` was inserted in §"Forward template-adoption (calibration-corpus tracking)" immediately BEFORE the existing `### Status: MANDATORY at K=3 (promoted from SUGGESTION at S88 W4a-17 close, 2026-05-04)` line. The sub-section contains 6 internal blocks:

1. **Provenance + Status** (`#### Status: SUGGESTION at K=1 (forward-looking from S88 W8-87 close, 2026-05-05)`).
2. **Hybrid Independence Test definition** with all four clauses verbatim:
   - **(i)** distinct **substrate-IS pillar** from prior K-instances
   - **(ii)** distinct **laboratory-IN pillar** from prior K-instances
   - **(iii)** distinct **bridge map class** (HKR / Connes-Karoubi pairing / K-theory boundary) from prior K-instances
   - **(iv)** **independent algebraic envelope** (NOT a numerical refinement of an existing K-instance's envelope)
   The structural form `(i ∨ ii ∨ iii) ∧ iv` is the MANDATORY hybrid: disjunction over the three structural axes (substrate / lab / bridge) AND conjunction with envelope-independence.
3. **`#### Companion-entry tagging (retroactive)`** clause specifying that registry entries failing the test are tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` and excluded from the K-counter while retaining full registry-entry status.
4. **`#### Calibration corpus (K=1 at S88 W8-87)`** table with §VII.AF.1 W-5 as calibration baseline + §VII.AG.1 as Companion-entry row showing all four clauses FAIL (same Pillar III, same Pillar IV, same HKR class with V_4 quotient as REFINEMENT, same `L^{-3}` envelope as REFINEMENT).
5. **`#### Substitution chain — §VII.AG.1 evaluation`** reproducing plan §W8-87 Steps 1–5 verbatim:
   - Step 1: K-counter advancement threshold = N=3 promotion to MANDATORY.
   - Step 2: PRE-Independence-Test, each §VII registry entry citing 5-IS-not-IN + 3-level naively counted as one K-instance.
   - Step 3: §VII.AG.1 substrate-IS pillar = Pillar III (MATCHES W-5 → clause (i) FAILS); §VII.AG.1 lab-IN pillar = Pillar IV (MATCHES W-5 → clause (ii) FAILS); §VII.AG.1 bridge map = HKR `L_max → ∞` modulo cyclic-fold V_4 (REFINEMENT of W-5 HKR → clause (iii) FAILS). Disjunction `(i ∨ ii ∨ iii) = (FAIL ∨ FAIL ∨ FAIL) = FALSE`.
   - Step 4: `FALSE ∧ iv = FALSE` regardless of clause (iv).
   - Step 5 (direction): K-counter does NOT advance for §VII.AG.1.
6. **`#### Conclusion`** + **`#### Forward enforcement (post-S88 W8-87)`** specifying plan-freeze halt on undocumented K-counter advancement, audit-script extension queued, and explicit non-conflict with the post-W4a-17 K=3 corpus block (W-5, W11-5, W4a-17 each independently satisfy `(i ∨ ii ∨ iii) ∧ iv`).

**Retroactive §VII.AG.1 tag**: The Companion-entry row of the K=1 calibration corpus table assigns the tag `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` to §VII.AG.1, formally classifying it OUTSIDE the K-counter. This is the retroactive structural classification required by plan §W8-87 step 4.

**K-counter table updated to K=1 (Independence Test baseline)**:

| # | Registry entry | Substrate-IS pillar | Lab-IN pillar | Bridge map class | Algebraic envelope | (i)∨(ii)∨(iii) | (iv) | Independent? |
|:-:|:---------------|:--------------------|:--------------|:-----------------|:-------------------|:--------------:|:----:|:------------:|
| 1 | §VII.AF.1 (W-5) | Pillar III | Pillar IV | HKR `L_max → ∞` | `L^{-3}` at d=4 | (baseline) | (baseline) | **YES** |
| Companion | §VII.AG.1 (W6-1) | Pillar III (same) | Pillar IV (same) | HKR + V_4 cyclic-fold (REFINEMENT) | `L^{-3}` (REFINEMENT) | FAIL ∨ FAIL ∨ FAIL = FALSE | FAIL | **NO** — `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE`; OUTSIDE K-counter |

**Allowlist row appended at `.claude/rules/methodology-wave-allowlist.md` line 148**:
```
| W8-87 | S88     | S88-CONSENSUS-INDEPENDENCE-TEST-LANDING (cross-pillar-bridge-anatomy.md ... | 8b4efec59c3b7b059af12b9b0abed1576cc3a0481938bd0dbc013a65eef73499 |
```

**Substitution chain (re-stated for WP record; per `.claude/rules/math-scripts.md §"Double-Check Logic"`)**:

- **Step 1** (Definition): K-counter advancement threshold = N=3 promotion to MANDATORY per `feedback_rules-compensate-missing-structure.md`.
- **Step 2** (Definition): "Distinct calibration instance" PRE-Hybrid-Independence-Test = each §VII registry entry citing the 5-IS-not-IN + 3-level discipline naively counted as one K-instance.
- **Step 3** (Substitution under `(i ∨ ii ∨ iii) ∧ iv` for §VII.AG.1):
  - clause (i): §VII.AG.1 substrate-IS pillar = Pillar III; §VII.AF.1 W-5 substrate-IS pillar = Pillar III. **MATCH ⇒ (i) FAILS.**
  - clause (ii): §VII.AG.1 lab-IN pillar = Pillar IV; §VII.AF.1 W-5 lab-IN pillar = Pillar IV. **MATCH ⇒ (ii) FAILS.**
  - clause (iii): §VII.AG.1 bridge = HKR `L_max → ∞` modulo cyclic-fold V_4 quotient; §VII.AF.1 W-5 bridge = HKR `L_max → ∞`. The V_4 quotient is a REFINEMENT of the same HKR class. **REFINEMENT-NOT-INDEPENDENT ⇒ (iii) FAILS.**
  - Disjunction: `(i ∨ ii ∨ iii) = (FAIL ∨ FAIL ∨ FAIL) = FALSE`.
- **Step 4** (Simplify): `FALSE ∧ iv = FALSE`. §VII.AG.1 fails the Hybrid Independence Test.
- **Step 5** (Direction): K-counter does NOT advance for §VII.AG.1. Therefore the structural verdict is `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE`, OUTSIDE the K-counter.

**Stale-source disclosure (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE per `.claude/rules/epistemic-discipline.md`)**:
Plan §W8-87 threshold (c) literally reads "K-counter table updated to K=1 (W-5 only)". The plan was authored before S88 W4a-17 close (2026-05-04) which legitimately advanced K to 3 (W-5 + W11-5 + W4a-17). Reverting the post-W4a-17 K=3 → K=1 would be PROHIBITED_ACTIONS Class 3 (post-hoc pre-registration editing) per `.claude/rules/v3-closure-recovery.md`. Honest closure: the Hybrid Independence Test is landed as a forward-looking discipline at SUGGESTION K=1 with W-5 as baseline (the literal "K=1" of the plan); the post-W4a-17 K=3 MANDATORY corpus block remains intact. The plan's STRUCTURAL intent — that §VII.AG.1 not advance K — is preserved exactly: §VII.AG.1 is now formally tagged OUTSIDE the K-counter under the Hybrid Independence Test, consistent with plan threshold (b) intent. The post-W4a-17 K=3 corpus is itself consistent with the Hybrid Independence Test (W-5 / W11-5 / W4a-17 each satisfy `(i ∨ ii ∨ iii) ∧ iv` by their distinct lab-IN pillars and/or distinct bridge map classes).

**5-clause threshold breakdown** (per plan §W8-87 PASS criterion):

| Clause | Description | Verdict |
|:------:|:------------|:-------:|
| (a) | Hybrid Independence Test sub-section present with all four (i/ii/iii/iv) verbatim | **PASS** |
| (b) | §VII.AG.1 retroactive tag `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` present | **PASS** |
| (c) | K-counter table reflects Independence Test verdict on §VII.AG.1 (Companion entry) | **PASS** |
| (d) | Allowlist row W8-87 appended | **PASS** |
| (e) | Substantive line count ≥ 15 in new sub-section | **PASS** (22 substantive lines) |

**Substrate framing (per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space")**: The Hybrid Independence Test enforces structural orthogonality of substrate-IS pillars / laboratory-IN pillars / bridge map classes — substrate is logically prior; the K-counter's calibration-corpus structure describes the substrate's bridge anatomy across structurally-distinct workshops, NOT narrative agreement among reviewers. Each instance counted toward K must independently bridge a substrate-IS observable on one finite-L spectral-triple structure to a laboratory-IN observable on a continuum platform via a structurally-distinct HKR / Connes-Karoubi / K-theory boundary map. §VII.AG.1's V_4 cyclic-fold quotient-functor is internal to the same Pillar III ↔ IV HKR class as W-5 — it refines W-5's substrate-IS observable; it does not bridge a NEW substrate-IS observable. The Independence Test makes this structural fact load-bearing at the K-counter level.

**Dual-SHA pin**:
- `audit_sha256 = 23afe890e8439e8b3ff6543c4a4617b22e08a753011481c6bd665e2aa062167e` (script + canonical_constants.py + sorted PRE-edit pinmap JSON)
- `content_sha256 = ce7080c133fe7c9e43117740d827f6cf0ff675ce5723159d98769225f41c466a` (script bytes only)

**Artifact pointers**:
- Producing script: `computations/session-88/s88_w8_consensus_independence_test_landing.py` (30,922 bytes)
- JSON sidecar: `computations/session-88/s88_w8_consensus_independence_test_landing.json` (2,685 bytes; pins before/after SHAs of edited rule-files, plan-block SHA, threshold breakdown, stale-source disclosure)
- Rule-file diff: `.claude/rules/cross-pillar-bridge-anatomy.md` (+6,679 bytes; sub-section at line 147)
- Allowlist row: `.claude/rules/methodology-wave-allowlist.md` (+1,372 bytes; W8-87 row at line 148)
- Verdict file: `computations/session-88/s88_gate_verdicts.txt` (canonical line + dual-SHA companion row appended)

#### Review by lizzi-spectral-functional-theorist

The Hybrid Independence Test rationale is structurally sound on the four clauses' partition of the substrate-axis / lab-axis / bridge-axis dimensions. **Clause (i)** (distinct substrate-IS pillar) and **clause (ii)** (distinct laboratory-IN pillar) are orthogonal in the algebra-axis sense per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3 post-S87 W-2 R3) — they classify the two endpoints of the bridge map via algebra-INVARIANT vs algebra-DEPENDENT functional families. **Clause (iii)** (distinct bridge map class) is orthogonal in the morphism-axis sense — HKR / Connes-Karoubi / K-theory boundary are three structurally distinct sheaf-theoretic operations, not numerical variants. **Clause (iv)** (independent algebraic envelope) is the conjunctive CONTROL ensuring that purely numerical refinements (e.g., a tighter `L^{-α}` constant-prefactor improvement, a tighter regulator scheme) do not advance K — convention-shopping is structurally blocked at the rule-file level by clause (iv). The disjunction `(i ∨ ii ∨ iii)` is correctly chosen over conjunction: an instance bridging a NEW substrate-IS pillar to an OLD lab-IN pillar via the OLD HKR map IS structurally independent (the substrate-IS observable is new), and clause (i) alone fires; the test must not require all three axes simultaneously distinct (that would be an over-strict gate). The §VII.AG.1 partial-axes-instance classification is correct: cyclic-fold V_4 quotient is a REFINEMENT functor on the same HKR map (it factors the HKR through a V_4-equivariant intermediate), preserving substrate / lab / bridge identities — the discrimination is at the morphism-refinement level, not the morphism-class level. PRU Class-8.2 (verifier-rubric pre-registration) is satisfied: the four-clause definition and the disjunction-vs-conjunction declaration are both pre-registered at the rule-file level, blocking convention-shopping reinterpretation. No structural objections; rule-extension is coherent with the existing K-counter discipline and with the post-W4a-17 K=3 MANDATORY corpus.

---

"""


def main() -> int:
    text = WP_PATH.read_text(encoding="utf-8")

    if OLD_BLOCK_MARKER not in text:
        print(f"ERROR: §W8-87 block marker not found in {WP_PATH}")
        return 1

    # Find boundaries of the existing §W8-87 block
    start = text.index(OLD_BLOCK_MARKER)
    nxt = text.index(NEXT_BLOCK_MARKER, start)

    # Replace block with new content (NEW_BLOCK already includes
    # the trailing "---\n\n" separator so concatenation reconstructs
    # the previous file structure).
    new_text = text[:start] + NEW_BLOCK + text[nxt:]

    # Atomic write via os.replace pattern: write to .tmp then rename
    import os
    tmp = WP_PATH.with_suffix(WP_PATH.suffix + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    os.replace(tmp, WP_PATH)

    delta = len(new_text) - len(text)
    print(f"[wp] Replaced §W8-87 block in {WP_PATH.name} ({delta:+d} bytes).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
