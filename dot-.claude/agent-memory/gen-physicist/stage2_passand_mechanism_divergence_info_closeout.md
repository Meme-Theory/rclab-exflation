# Stage-2 PASS-AND closeout: reviewers AGREE on conclusion, DIVERGE on mechanism → INFO + forward-route (not rewrite)

**Pattern** (S115 W2-1, §VII.CK D4 discharge): a Stage-2 blind two-axis verify of a registered JOINT clause where BOTH axes PASS the JOINT clause (conclusion holds) but ONE axis returns single-leg INFO because the registry's STATED MECHANISM is mis-stated. PASS-AND over {A-leg, B-leg, JOINT-A, JOINT-B} with one INFO, zero FAIL ⇒ **composite INFO** — the pre-registered outcome, NOT a forced PASS and NOT a forced FAIL. The blind protocol WORKING (it caught a genuine registry mechanism mis-statement) is the headline framing, not an agent failure.

## The load-bearing closeout moves (do exactly these; do NOT over-reach)

1. **Apply the operator literally.** `composite = PASS iff ALL∈{PASS}; any FAIL⇒FAIL; any INFO(no FAIL)⇒INFO`. In-script `assert composite=="INFO"`. Forcing PASS = ansatz-forced PASS (PROHIBITED Class 4); inventing a FAIL no reviewer emitted is equally wrong.

2. **INFO disposition = NO flip + STATUS pointer, NOT a mechanism rewrite.** The stage tag STAYS at the prior-determined state (here STAGE-3-PERMANENT, D4-open RETAINED). Per `Investigating-Workshops.md` Q1 + capstone-hygiene rule, a genuinely-unreconciled math/physics adjudication (mechanism-A vs mechanism-B, both reaching the same conclusion) is FORWARD-ROUTED with a `STATUS: Stage-2-INFO-deferred` pointer to a CF — it is NOT rewritten by the closeout, NOT silently down-tagged, and the contested text is RETAINED (audit-trail preservation). Do NOT apply the dissenting reviewer's corrigendum yourself (that's mack-cosmic-bridge sole-writer on the future CF); do NOT touch the sibling-clause (D1–D3) PERMANENT status.

3. **STATUS-pointer add = idempotent single-pass RMW on a UNIQUE tail-anchor.** Append after the exact verbatim tail-sentence of EACH affected registry block (here: the Four-door D4 row AND the D4-disposition annotation — both stated the contested mechanism). Idempotency sentinel = the `STATUS: …` marker substring; re-run is NO-OP. Atomic write (temp sibling + os.replace + fsync). In-script post-write HARD GUARDS: `stage_tag_intact`, `no_unconditional_landed`, `contested_text_retained`, `pointer_present_after`, `not missing_anchors` — assert all.

4. **The `no_unconditional_landed` sentinel must distinguish the BOLD TAG from prose mentions.** Guard on the literal `**STAGE TAG: STAGE-3-PERMANENT-UNCONDITIONAL` (the bold tag-flip), NOT bare `STAGE-3-PERMANENT-UNCONDITIONAL` (which appears 3× in prose "upgrade owed to…" mentions and is fine). Mis-guarding here would block a correct landing.

## Traps that bit me (dry-run BEFORE the real run)

- **Anchor byte-exactness**: the contested-mechanism guard string must be the EXACT on-disk token incl. backticks: `` `t(O)=±1≠0` center-character selection rule `` (NOT `t(O)=±1≠0 center-character…` — the registry has a backtick after `≠0`). Dry-run every anchor + sentinel substring against disk first; a missing match would assert-fail spuriously.
- **canonical_constants import**: this closeout lives in `session-N/` and the template's `from canonical_constants import *` is import-1. Add a Section-0 bootstrap `sys.path.insert(0, _shared)` BEFORE it (sibling idiom `s114_yuk_rightreg_connection.py:73-77`). The bare template does NOT bootstrap the path.

## sig_5 / cross-promotion independence

- Per-gate identity keys `{_gate_id,_scheme,_convention,_wp_id,_clause}` embedded in the pinmap ⇒ `audit_sha256` distinct from the SIBLING same-slot gate (W1-1 vs W2-1 on the SAME §VII.CK slot, different clause/reviewers).
- Two Stage-2 verifies on the SAME registry slot (D1–D3 then D4) MUST land with DISJOINT reviewer pairs (§EVOI.BF cross-promotion-independence): W1-1 {lizzi,kitaev} ⊥ W2-1 {spectral-geometer,volovik} = 4 distinct reviewers. Encode the `excluded_authors` + ∅-intersection guard IN the closeout (the `--check-reviewers` author-parser is unreliable on §VII.CK — prose-idiom authorship lines). See [[stage2_verify_reviewer_exclusion_audit_gap]].

## Corroboration-as-situational-awareness (does NOT change the verdict)

The MCP `search_knowledge` independently confirmed the dissenting axis's corrigendum (connes-r2.md PROVEN: "multiplicity leg is R_X-active; the correct wall is the commutant one" + the (W2) homogeneity-wall theorem). Record salient returns in the WP MCP-audit block, but the corroboration only confirms the contest is SUBSTANTIVELY GROUNDED — it does not flip INFO→FAIL (both mechanisms reach the same conclusion; the JOINT clause PASSes both axes).
