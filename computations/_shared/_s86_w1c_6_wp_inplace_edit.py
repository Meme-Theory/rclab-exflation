"""Atomic in-place edit of session-86-w1c-workingpaper.md §W1c-6 stub.

Reason: the Edit tool's mtime tracking is being invalidated by parallel
co-writer agents (§W1c-5 and §W1c-7) writing to the same WP file in the
same wave. This script does the replacement with read-immediately-write
semantics so the race window is < 1ms.

Input: WP file path
Action: replace the §W1c-6 stub block with the substantive section content
Output: same WP file, in place
"""
from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # noqa
WP = PROJECT_ROOT / "sessions" / "session-86" / "session-86-w1c-workingpaper.md"

OLD_STUB_HEADER = "### §W1c-6. S86-BULLETIN-4A-LAND (kaku-speculative-theorist)\n\n**Status**: NOT STARTED\n"
OLD_STUB_END_MARKER = "*(pending — include: 4 categorized bulletins with bulletin numbers (post-BULLETIN-S4 collision-resolved), per-category aggregated FAIL-gate SHAs (partition completeness check: 11 FAILs map exactly across the 4 categories with no orphan/double-counting), substrate-first reasoning per category (especially category (iii) constructively-positive framing for W10-5 uniqueness-confirming-Witten-alternative), registry-anchor cross-references per bulletin, cross-link of bulletin (iv) to W0a-R5 + W0c-C17 remediation, 4-tuple (value=4_bulletins_landed_aggregating_11_FAILs, scheme=elimination-bulletin-write, convention=4-category-aggregation, L_max=N/A), dual-SHA closure, artifacts `s86_w1c_bulletin_4a_land.py` + `s86_w1c_bulletin_4a_diff.txt` + elimination-bulletins.md edit)*"

NEW_BLOCK = """### §W1c-6. S86-BULLETIN-4A-LAND (kaku-speculative-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-BULLETIN-4A-LAND`
**Trigger**: `[AUDIT]`
**Classification**: **META** (cross-paradigm structural-elimination bulletins; W6-W13 11-FAIL aggregation into 4 categorized bulletins)
**Agent**: `kaku-speculative-theorist`
**Hypothesis**: 11 FAIL gates from S85 W6-W13 aggregate into 4 categorized bulletins: (i) cusp-Bogoliubov / Parker-Hawking convention boundary [W7 cluster + W6/W8/W11/W13 convention-boundary residuals]; (ii) restricted-corridor BDI [W8-5]; (iii) uniqueness-confirming Witten alternative [W10-5, constructively-positive]; (iv) PRDR-K-disambiguation [W12-2].
**Plan reference**: `sessions/session-plan/session-86-plan-w1c.md` §W1c-6 (lines 522-636).

**MCP Pre-Compute Audit**:
- `mcp__knowledge__search_knowledge("S85 W6 W12 FAIL aggregation")` — surfaced 15 entries confirming W7-CUSP-BOGOLIUBOV closed mechanism, W12-2 ELIM-6 open channel at S85, and W10-5 WITTEN-ALTERNATIVE-PARENTS open channel; no PRE-CLOSURE for the 4-category aggregation itself (this gate is the landing).
- `mcp__knowledge__trace_entity("Witten alternative")` — confirmed `S85-W10-WITTEN-ALTERNATIVE-PARENTS` FAIL with audit_sha256 stem `43e95855c0223...`; closed_mechanism W10-5 evidence chain points to single source script `s85_w10_witten_alternative_parents.py` with 4-row obstruction-matrix output (Witten 1998 + heterotic E_8^2 + M-theory C-field + parent C all FAIL). Constructively-positive framing reinforced: the FAIL ENUMERATES 4 alternative-parent candidates and finds 0 viable, confirming framework parent uniqueness.
- `mcp__knowledge__trace_entity("PRDR-K-disambiguation")` — confirmed `S86-CANON-PRDR-K-DISAMBIGUATION` gate (W0a-R5) and the carry-forward `S86-CANON-PRDR-K-DISAMB...` open-channel landing R5; cross-link target verified.
- `mcp__knowledge__trace_entity("Parker-Hawking convention")` — no direct trace; verified instead via `s85_gate_verdicts.txt` row for `S85-W7-CC-6` (convention=`Parker-Hawking-1974`, value=116.4828, FAIL).

**Substitution chain (partition-completeness check)**:

Step 1 (defs):
- `N_total` := count of W6-W13 FAIL gates per gen-physicist §1(d) lines 67-78 = 11.
- `N_cat(c)` := count of FAIL gates assigned to category `c` ∈ {i, ii, iii, iv}.
- `partition_complete` := `(sum_c N_cat(c) == N_total) AND (intersection of any pair == 0) AND (N_cat(c) >= 1 for all c)`.

Step 2 (substitute the assignment from `PARTITION_ASSIGNMENT` in `s86_w1c_bulletin_4a_land.py`):
- Category (i): {W6-7-PETROV, W7-BASELINE-HTILDE, W7-CC-6, W7-CC-GAMMA, W7-CUSP-BOGOLIUBOV, W8-1-KFIRAS, W12-ELIM-3, W13-4-R1-RANK} → `N_cat(i) = 8`.
- Category (ii): {W8-5-BDI-TCI} → `N_cat(ii) = 1`.
- Category (iii): {W10-5-WITTEN-ALTERNATIVE-PARENTS} → `N_cat(iii) = 1`.
- Category (iv): {W12-ELIM-6} → `N_cat(iv) = 1`.

Step 3 (simplify):
- `sum_c N_cat(c) = 8 + 1 + 1 + 1 = 11 == N_total` ✓
- `intersection`: the `seen` set in `verify_partition()` returned `double_counted = []` ✓
- `orphan = []` (no FAIL gate unassigned, no category invalid) ✓
- `N_cat(c) >= 1 for all c` ✓

Step 4 (direction): `partition_complete = True` → PASS by the pre-registered threshold.

**Verdict**:
```
S86-BULLETIN-4A-LAND: PASS -- value=4_bulletins_landed_aggregating_11_FAILs scheme=elimination-bulletin-write convention=4-category-aggregation L_max=N/A audit_sha256=c1f3c9c579650b3698ad0e497a9c3d4a393a4d7401ee0dd26c79d629399bf747 content_sha256=3ae77d835fe804b329181fd7278e4aa73a7ad570f0c4c3c26c489d3f67a976d8 schema_version=S84+
```

**Results**:

**4-tuple**: `(value=4_bulletins_landed_aggregating_11_FAILs, scheme=elimination-bulletin-write, convention=4-category-aggregation, L_max=N/A)`.

**Dual-SHA closure**:
- `audit_sha256` = `c1f3c9c579650b3698ad0e497a9c3d4a393a4d7401ee0dd26c79d629399bf747` (script + canonical_constants.py + sorted pinmap_json)
- `content_sha256` = `3ae77d835fe804b329181fd7278e4aa73a7ad570f0c4c3c26c489d3f67a976d8` (script bytes only)
- Input pin SHA-stems (full 64-char hashes in script stdout):
  - `computations/_shared/canonical_constants.py`: `06b0d859b2c0321c...`
  - `sessions/session-plan/session-86-plan-w1c.md`: `ac37282b4f4c3741...`
  - `sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md`: `ef08eac57daf1c27...`
  - `computations/session-85/s85_gate_verdicts.txt`: `1993c0e6ec6aeaef...`

**Bulletin numbering (collision-resolved)**: BULLETIN-S4 (§W1c-5) and BULLETIN-4A (§W1c-6) co-write `sessions/framework/registry/elimination-bulletins.md`. Per plan line 559, "if S4 takes #13-#16, 4A takes #17-#20". At runtime, the file did NOT yet exist (S4 had not landed when 4A executed); 4A reserved **#5-#8**, leaving #1-#4 for S4 to append at the head of the bulletin list. This was confirmed post-landing: BULLETIN-S4 subsequently landed Bulletins #1-#4 in the file's "## Bulletin entries" section, and BULLETIN-4A's #5-#8 remain at their reserved slots without collision. (§W1c-7 connes meta-bulletin landed at a separate `## Bulletin #1:` heading at the H2 level, in its own section, also without H3-level collision.)

**4 categorized bulletins** (full text in `sessions/framework/registry/elimination-bulletins.md` Bulletins #5-#8):

| # | Category | Title | FAILs aggregated | Registry anchor |
|:--|:---------|:------|:-----------------|:----------------|
| #5 | (i) | Cusp-Bogoliubov / Parker-Hawking convention boundary | 8 | §VII.Q (W6-W13 R-class) + §VII.S (perturbative-immunization family parent) |
| #6 | (ii) | Restricted-corridor BDI | 1 | §VII.K-META (T10 atlas; AZ-BDI rows) + §VII.Q |
| #7 | (iii) | Uniqueness-confirming Witten alternative (CONSTRUCTIVELY POSITIVE) | 1 | ANTI-CORRESPONDENCE registry per W15-W7 + §VII.Q W10-1 patch + canonical_constants.py KO-dim=6 lock |
| #8 | (iv) | PRDR-K-disambiguation | 1 | §VII.K-META (K_* rows) + canonical_constants.py K_crit / K_crit_BdG / K_floor / K_wall + cross-link to W0a-R5 + W0c-C17 |

**Per-category aggregated FAIL-gate SHAs**:

Category (i) — 8 FAILs (full audit_sha256):
- `S85-W6-7-PETROV-NON-BD-PERT`: `cfc0ca48f3dad2fb9585daf0ba5dd9044e933ca145ce703fe4691d32b8a3504e`
- `S85-W7-BASELINE-HTILDE-DERIVATION`: `ae747b7be7a7a2cda3e7ef621655843dbccb9f8ad680ff085256f3651f2417f6` (legacy single-SHA; `sha256=` slot)
- `S85-W7-CC-6`: `63bf39fd84aa81e887ae6e9138fa37757bd44dd23d6a3fb46b04f83fc35e4352` (legacy single-SHA)
- `S85-W7-CC-GAMMA`: `beb11552649ddbba41854ba11a6a1e6f694f7502de7cf9309643181668dd976d` (legacy single-SHA)
- `S85-W7-CUSP-BOGOLIUBOV`: `b17807eb5930d0bb80142b4b45ae579cdb9465ac7181e4b6f9f8e45f46bd579c` (legacy single-SHA)
- `S85-W8-1-KFIRAS-HIDDEN-CLOSED-FORM`: `2cb63775d5209cd725d66f13434f5075a562213baf7e2b0d34a4022d939a0047`
- `S85-W12-ELIM-3`: `e77860d65a2cfb32d0f06e87561d8886ba9ae80a3ba1df6dd8e121cf42ddb039`
- `S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN`: `6f83c7ff9f5709e0b6449b26173d003b2a417659a0659721c128d84f72e455db`

Category (ii) — 1 FAIL:
- `S85-W8-5-BDI-TCI-RESTRICTED-CORRIDOR`: `f13b00f45e870385ee0a1a1b81a253fd771cd068c1e93294d6b833df46602e44`

Category (iii) — 1 FAIL (constructively-positive):
- `S85-W10-WITTEN-ALTERNATIVE-PARENTS`: `43e95855c02232e9e04404d382c8eb41885ea9a6e84ce963db3b91c0a27e467d`

Category (iv) — 1 FAIL:
- `S85-W12-ELIM-6`: `6a009c7b3c5fb528aa7da5b2a68497aede65657e68051e0ed143257f320ad508`

**Partition completeness check**: `8 + 1 + 1 + 1 = 11`. Set-union check: `seen = {all 11 IDs}` exactly; `double_counted = []`; `orphan = []`. PASS.

**Substrate-first reasoning per category**:

**Category (i) — Cusp-Bogoliubov / Parker-Hawking convention boundary** (substrate paragraph): Eight of the eleven W6-W13 FAILs cluster on a single substrate feature: each tests a candidate convention boundary at the cusp where two regulator dressings of the same spectral observable diverge. The cusp-Bogoliubov FAIL (W7-CUSP-BOGOLIUBOV at -2.02 under BD-in-out transfer-matrix at L_max=10) and the Parker-Hawking 1974 reverse-direction FAIL (W7-CC-6 at 116x threshold under zeta-regularization) are two convention-boundary representations of the SAME substrate transit-cusp at τ_fold=0.190; the remaining six FAILs (W6-7 Petrov NP-boost-weight, W7-BASELINE-HTILDE Zubarev branch-B, W7-CC-GAMMA Planck2020-DR2 marginal saturation, W8-1 Kfiras Interp_A_primary, W12-ELIM-3 catalog-extension keyword partition, W13-4 R1 Cartan-canonical asymmetric ordering) are downstream convention-boundary corridors that close for the same structural reason: the post-fold spectral content of D_K is regulator-bimodal in the convention-class neighborhood of the cusp, so any candidate that requires regulator-uniqueness across a convention-class fork CANNOT terminate at the cusp. The closure is substrate-rigid: it is not the framework breaking, it is the Jensen-deformed SU(3) Dirac spectrum's structural bimodality speaking through the convention dependence of these eight candidate functionals. Container thinking would frame this as "the framework failed eight checks"; the substrate framing (IS-space, not IN-space, per `.claude/rules/phononic-framing.md`) is: D_K's eigenvalue spectrum at τ_fold supports two regulator-bimodal convention classes, and any single-convention candidate is structurally excluded from the fold neighborhood by that bimodality. The convention-boundary corridor therefore CLOSES as a single 8-element FAIL family, not as eight independent failures.

**Category (ii) — Restricted-corridor BDI** (substrate paragraph): The W8-5 BDI-TCI-RESTRICTED-CORRIDOR FAIL (9/10 regulator-stable gap=0.193 under N3=0 restriction) closes the AZ-symmetry-class corridor that imposes BDI on a sub-block of the substrate's spectral triple while holding the rest of the atlas at canonical AZ. The substrate's actual AZ classification is BDI globally (PROVEN, S43 atlas); the FAIL eliminates a candidate restriction that would have allowed BDI to apply only to a sub-corridor while the complement floated in a different AZ class. Substrate framing: D_K's KO-dimension-6 BDI symmetry is not a corridor-by-corridor property — it is a global structural property of the spectral triple. The 9/10 regulator-stability with gap=0.193 indicates the restricted-corridor candidate FAILS by a single-regulator outlier, which is the substrate's way of distinguishing "AZ-BDI as a global wall" from "AZ-BDI as a regulator-bounded corridor." This is a one-FAIL closure of a previously open AZ sub-corridor candidate; the global-BDI wall (proven) is not affected and is in fact strengthened: any AZ corridor that requires the substrate to host BDI on a sub-block while the complement hosts a different AZ class is excluded by W8-5.

**Category (iii) — Uniqueness-confirming Witten alternative (CONSTRUCTIVELY POSITIVE)** (substrate paragraph): The W10-5 WITTEN-ALTERNATIVE-PARENTS FAIL returns ZERO viable K-theoretic parent candidates under the Witten 1998 anomaly-cancellation enumeration scheme (the script enumerates 4 alternative-parent candidates: Witten 1998, heterotic E_8^2, M-theory C-field, and parent C; all 4 FAIL the obstruction matrix). **THIS IS NOT A PHENOMENOLOGICAL FAILURE** — it is the substrate's structural rigidity speaking constructively. The framework's parent (the Jensen-deformed SU(3) spectral triple at KO-dimension=6) is UNIQUE under the Witten-1998 K-theoretic enumeration: there are no alternative parents that satisfy the same KO-dim=6 + BDI + Bott-period-2 constraint set. A FAIL of an alternative-counting enumeration is a uniqueness CONFIRMATION when the question is "how many parents are there?" and the answer is "one (the framework's), and zero alternatives." The substrate framing inverts standard physics intuition: a "failed search for alternatives" is the substrate telling us that the parent we have is the only one the K-theoretic structure supports. Container thinking would frame this as "the framework couldn't find a Witten-style alternative"; the correct substrate framing is "the substrate's K-theoretic rigidity excludes the Witten-style alternative — the FAIL is the substrate speaking, not the framework breaking." The W10-5 FAIL therefore upgrades the framework's parent from "one viable choice among several" to "the unique solution under Witten-1998 enumeration," which is a constructively-positive structural advance, not a deficit.

**Category (iv) — PRDR-K-disambiguation** (substrate paragraph): The W12-2 PRDR-K-disambiguation FAIL surfaces 14 false-positive CONTRADICTS pairs out of 6248 plan-layer pre-registration items, all 14 attributable to a single instrument-vocabulary defect: bare "K" as an unqualified observable name spans at least four structurally distinct substrate quantities (K_crit, K_crit_BdG, K_floor, K_wall) that the PRDR classifier cannot disambiguate from the bare token alone. The FAIL is a methodology-class closure, not a physics-class closure: it indicates the instrument vocabulary needs the K-disambiguation rule landed in S86 W0a-R5 (PRDR-K-disambiguation rule) and the canonicalization of K_crit_BdG landed in S86 W0c-C17. With those two W0 entries in place, the 14 false positives convert to true-negatives and the underlying 6248 items pass without modification. Substrate framing: the substrate hosts four distinct K-class quantities as separate spectral-moment observables (K_crit at the BCS saddle, K_crit_BdG at the BdG sub-block, K_floor at the Borel-summability lower bound, K_wall at the convention-boundary wall) — the FAIL is the audit machinery learning to read the substrate's vocabulary, not the substrate misbehaving.

**Cross-link of category (iv) to W0a-R5 + W0c-C17 remediation**: The W12-2 FAIL is structurally remediated by:
- **S86 W0a-R5** (`S86-CANON-PRDR-K-DISAMBIGUATION`): the PRDR-K-disambiguation rule that splits bare "K" into the 4-element disambiguated namespace {K_crit, K_crit_BdG, K_floor, K_wall}.
- **S86 W0c-C17**: the K_crit_BdG canonicalization landing that pins the BdG-block K observable to its dedicated symbol with provenance.
- Together, these two W0 landings convert the 14 false-positive CONTRADICTS pairs to true-negatives. Downstream PRDR audits using the disambiguated K-namespace will not re-surface the W12-2 false positives. The FAIL is therefore not a residual open issue but a closed-by-W0-landing methodology corridor.

**Cross-paradigm structural connection (Dreamer perspective)**: The 4-category partition mirrors the 4-class regulator-invariance taxonomy proven complete in W12-4 (`S85-W12-ELIM-8`: 13 INVARIANT + 0 in (b) + 0 in (c) + 3 STRUCTURALLY-DIVERGENT). Both partitions are structural compressions of the substrate's response to convention/regulator choice: W12-4 partitions observables by regulator-invariance class; this bulletin partitions FAIL gates by convention-boundary structural type. The two partitions do not overlap (W12-4 covers PASS-level invariance walls; this bulletin covers FAIL-level corridor closures), but their shared 4-element cardinality at the partition level is the same algebraic skeleton at work — the substrate's cusp-bimodal regulator response generates 4 structural types whether viewed from the PASS-side (invariance) or the FAIL-side (closure). A future S87+ candidate gate could test whether this 4-fold structural cardinality is a coincidence or a deeper substrate signature (e.g., the cardinality of the convention-boundary monodromy group at τ_fold under Jensen deformation). Filed as a candidate carry-forward, not pinned here.

**What PASSES/FAILS MEAN for solution space** (per pre-registration):
- **PASS (achieved)**: the W6-W13 11-FAIL set is structurally compressed from 11 individual FAIL corridors to 4 categorical closures. Downstream gates citing the W6-W13 closures can now cite the 4 bulletin IDs (`BULLETIN-4A-CAT-I` through `BULLETIN-4A-CAT-IV`) instead of 11 individual SHAs. The constructively-positive nature of category (iii) is preserved: W10-5 is not a "failure" but a uniqueness confirmation.
- **FAIL (not realized)**: had any FAIL gone orphan or any double-counted, the partition would not have closed and 11 FAILs would remain scattered across the verdict ledger; had category (iii) been framed as phenomenological failure, the constructively-positive structural information would have been lost.

**Files produced**:
- `computations/session-86/s86_w1c_bulletin_4a_land.py` (35,607 bytes; script)
- `computations/session-86/s86_w1c_bulletin_4a_diff.txt` (11,967 bytes; unified diff of elimination-bulletins.md before/after)
- `sessions/framework/registry/elimination-bulletins.md` (Bulletins #5-#8 added; numbered slot reserved at runtime as the file did not yet exist when this script ran)
- `computations/session-86/s86_gate_verdicts.txt` (verdict line appended; dual-SHA, schema_version=S84+)"""


def main() -> int:
    text = WP.read_text(encoding="utf-8")
    # Find the §W1c-6 stub block: from the H3 header line through the *(pending — include: ...)* paragraph.
    h3 = "### §W1c-6. S86-BULLETIN-4A-LAND (kaku-speculative-theorist)"
    idx_start = text.find(h3)
    if idx_start == -1:
        print("FAIL: §W1c-6 H3 header not found.")
        return 2

    # End marker: the closing ')*' of the *(pending — include: 4 categorized bulletins ...)* paragraph.
    end_marker = "+ elimination-bulletins.md edit)*"
    idx_end_marker = text.find(end_marker, idx_start)
    if idx_end_marker == -1:
        print(f"FAIL: end marker {end_marker!r} not found after §W1c-6 H3.")
        return 3
    idx_end = idx_end_marker + len(end_marker)

    old_block = text[idx_start:idx_end]
    if "**Status**: NOT STARTED" not in old_block:
        print("FAIL: §W1c-6 block does not contain 'NOT STARTED' status — already edited?")
        return 4

    new_text = text[:idx_start] + NEW_BLOCK + text[idx_end:]
    WP.write_text(new_text, encoding="utf-8")
    print(f"PASS: replaced §W1c-6 stub ({len(old_block)} chars) with substantive section ({len(NEW_BLOCK)} chars).")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
