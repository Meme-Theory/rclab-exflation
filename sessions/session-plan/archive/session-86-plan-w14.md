# Session 86 Plan — Wave W14: Watchlist edits

**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-86-plan-w14.md`
**Theme**: 5 inventory edits + 1 NEW lab-falsifier row class to `sessions/framework/registry/falsifier-master-inventory.md`
**Item count**: 6 (rename internally W14-1 through W14-6 to disambiguate from `W{N}` watchlist row identifiers in partition §2.4)
**Wave-equivalent effort**: ~3-4h combined (mechanical inventory edits, no compute)
**Generated**: 2026-04-25

---

## §0. Wave W14 Summary

This wave consolidates six watchlist deltas onto the canonical inventory file `sessions/framework/registry/falsifier-master-inventory.md`. All deltas originate from mack 9A §III.3 W6-W13 synthesis (5 PAIR enrichments + 1 NEW row class). Five (W14-1 through W14-5) are atomic-scope edits to existing inventory rows (#1, #3, #7, #9, #12). The sixth (W14-6) creates a NEW row class spanning rows #13-#21 — the lab-falsifier suite covering 9 atomic terrestrial-lab predictions (3 sweet-spot + 6 cross-platform) routed via S82 W8-4 and 1B volovik solo. EVOI tag for the NEW class is `LAB-FALSIFIER` with P_decisive ∈ [0.30, 0.50] over a 5-yr terrestrial-lab horizon.

Classification META throughout: these are inventory/registry maintenance gates. No new physics derivations are produced; the wave packages already-PASSed S85 verdicts into the canonical observational-prediction inventory. PASS criterion is uniform: an edit lands correctly with all required cells present, all source SHAs cited, and `_plan_upstream_pin_validator.py` exit-0 on the resulting inventory diff. FAIL = any required cell missing, any cited SHA absent from the source-of-truth, or any registry-promotion violating prior `feedback_framework-hygiene.md` (no value mutation under "strengthening citation only" tags).

The wave consumes outputs from W11 (C5 SI-translation + C6 EVOI-tree), so W14-6 is **strictly downstream of W11** in the execution-time DAG. The other five edits (W14-1 through W14-5) have no execution-time dependency on W11 and can dispatch concurrently with it inside the assigned `mack-cosmic-bridge` agent budget.

---

## §0.5. Wave W14 Decision-Point Prerequisites

| Gate | Hard prerequisite | Reason |
|:-----|:------------------|:-------|
| W14-1 | none (S85 W7-7 + W10-2 verdict SHAs already pinned at S85 close) | inventory-only edit; verdict provenance is frozen |
| W14-2 | none (S85 W13-2 verdict SHA `f514d642fe2a80ac…` frozen) | inventory-only edit; W13-2 lives in `computations/s85_gate_verdicts.txt` |
| W14-3 | none (W13-2.Ω value 8.299e-58 frozen at S85 close) | inventory-only edit; (A)/(C) discriminator structure documents existing W13-2 verdict |
| W14-4 | none (S82 W3-4 + S67 + S85 W9-3 verdicts frozen) | 3-pathway expansion; all 3 verdicts are pre-S86 |
| W14-5 | none (W3-7 ε-sensitivity range 3.11e-9 → 4.27e-9 over ε ∈ {0.02163, 0.020} from S85 W3-7) | inventory edit annotates ε_pivot status as S86 SECTOR-1 carry-forward (cross-references W5a P3 — but as a **forward-reference annotation only**, not a runtime dependency) |
| W14-6 | **W11 C5 + C6 must complete first** (NEW lab-falsifier row class consumes per-platform σ_detect anchors from C5 + EVOI tree from C6) | P_decisive [0.30, 0.50] tag and SI-translation-pending status flags route through C5/C6 outputs |

**Cross-reference**: P11 (`S86-MASTER-INVENTORY-W6-W13-LAND` in W13) is the broader registry-write parent that this wave's 6 edits constitute the W6-W13 portion of. P11 lands all enrichments via the same dispatch agent (`mack-cosmic-bridge`); per partition §1 W14 sequencing note, leave P11 in W13 and execute these 6 edits as W14 sub-actions of the same registry-maintenance scope. No double-write risk: each W14-i edit operates on a distinct row range (#1, #3, #7, #9, #12, #13-#21), and P11 in W13 packages cross-row metadata (banner + table-of-contents update, NOT the per-row content).

---

## §I. Carry-Forward Items Mapping (6 rows)

| W14 internal ID | Partition §1 W14 ID | Source citation | Target row(s) | Edit class | Effort |
|:----------------|:--------------------|:----------------|:--------------|:-----------|:-------|
| W14-1 | W1 (watchlist) | mack 9A §III.3 #1 | Row #1 (w_0) | Sub-pin table 3 rows + audit-pin SHA | 30 min |
| W14-2 | W2 (watchlist) | mack 9A §III.3 #2 | Row #3 (α_s §VII.Ω) | SHA citation append | 15 min |
| W14-3 | W3 (watchlist) | mack 9A §III.3 #3 | Row #7 (CGWB ρ_AC) | New column + discriminator paragraph | 30 min |
| W14-4 | W4 (watchlist) | mack 9A §III.3 #4 | Row #9 (f_NL_folded) | 3-pathway sub-table | 45 min |
| W14-5 | W5 (watchlist) | mack 9A §III.3 #5 | Row #12 (A_s) | ε-sensitivity sub-note | 30 min |
| W14-6 | W6 (watchlist) | mack 9A §III.3 #6 + W8-4 + 1B volovik | NEW Rows #13-#21 | NEW row class (9 atomic predictions) | 1.5h |

Combined: 5 mechanical row updates + 1 NEW row class with 9 atomic predictions. Validator pass: `_plan_upstream_pin_validator.py --json` against the resulting inventory diff at S86 close.

---

## §W14-1. S86-WATCHLIST-W1-EDIT (Row #1 w_0)

**Carries forward**: partition §1 W14 item W1 (watchlist) — Row #1 w_0 sub-pin enrichment

### Field 1 — Gate ID
`S86-WATCHLIST-W1-EDIT`

### Field 2 — Trigger
`[VERIFY]` — verify the inventory edit lands all 3 sub-pin rows + W10-2 audit-pin SHA correctly.

### Field 3 — Classification
META — registry maintenance, not a physics gate.

### Field 4 — Agent type
`mack-cosmic-bridge` (this agent is the runner; self-blacklist not applicable since wave-owner = runner). NOT `gen-physicist` — observational-watchlist content + cross-reference to mack-track DESI-DR3 chain warrants the specialist.

### Field 5 — Hypothesis
The S85 W1a-5 / W7-7 / W10-2 w_0 verdict cluster is consolidated as a single inventory row #1 with explicit regulator-layer disambiguation: L=8 (W7-7), L=10 (canonical W1a-5), L=12 (split). Adding this 3-row sub-pin table + the W10-2 branch-(iv) audit-pin SHA reference makes the row downstream-citable for DESI DR3 contingency planning (W12 P8 + S85 W12 contingency tree).

### Field 6 — Method (complete dispatch prompt)

```
SUBJECT: S86-WATCHLIST-W1-EDIT — Row #1 (w_0) sub-pin table + audit-pin SHA reference

Read .claude/rules/agent-standards.md, .claude/rules/output-standards.md,
.claude/rules/gate-verdicts.md, and .claude/rules/phononic-framing.md before editing.

Target file: sessions/framework/registry/falsifier-master-inventory.md

Action: Edit Row #1 (w_0). Append immediately after the existing prediction
cell a 3-row regulator-layer sub-pin table with columns
(L_max | source verdict | w_0 value | scheme | content_sha256 | audit_sha256_short).

Sub-pin row contents (compute audit_sha256 from input-pin maps via
_dual_sha_uniqueness_audit.py at runtime — NEVER hardcode):
  1. L=8     — source: S85 W7-7 verdict in computations/s85_gate_verdicts.txt
              — w_0 value: per W7-7 verdict line
              — scheme: <as recorded in W7-7 verdict line>
              — content_sha256: <extract from s85 verdict file>
              — audit_sha256_short: <16-hex from companion comment row>
  2. L=10    — source: S85 W1a-5 (canonical) verdict in same file
              — w_0 value: -0.918 (Volovik partition canonical, per S85 §1.2)
              — scheme: SDW (per §1.2 W1a-5 row)
              — content_sha256: <from W1a-5 verdict line>
              — audit_sha256_short: <16-hex from companion>
  3. L=12    — source: split-regulator entry (NOT a single canonical pin —
                document explicitly that L=12 split means atlas-mean over the
                W12-4 5-regulator atlas)
              — w_0 value: <atlas-mean from W12-4 5-regulator atlas>
              — scheme: ATLAS-MEAN
              — content_sha256: <from W12-4 verdict line>
              — audit_sha256_short: <16-hex from companion>

Append below the sub-pin table a single-line W10-2 audit-pin SHA reference:
  "Branch-(iv) audit pin: W10-2 -- audit_sha256=<full 64-hex from W10-2
   verdict line>; framework w_0 = -0.842454 (substrate-compaction); see
   P9 (W13) for w_0_FW PRIMARY adjudication between Volovik partition
   -0.918 and substrate-compaction -0.842454."

DO NOT mutate the existing Row #1 prediction cell value. The edit is
ADDITIVE — sub-pin table + reference line, no rewrite of the original
row content.

Cross-check before commit:
  1. grep "W7-7" computations/s85_gate_verdicts.txt -- confirm verdict line exists
  2. grep "W1a-5" computations/s85_gate_verdicts.txt -- confirm verdict line exists
  3. grep "W10-2" computations/s85_gate_verdicts.txt -- confirm verdict line exists
  4. grep "W12-4" computations/s85_gate_verdicts.txt -- confirm verdict line exists

Output: edited sessions/framework/registry/falsifier-master-inventory.md (single file
diff, no .npz / .png / .json artifacts since this is a registry maintenance
edit).

Append verdict line to computations/s86_gate_verdicts.txt:
  S86-WATCHLIST-W1-EDIT|PASS|<sub_pin_count=3>|inventory|MD-EDIT|n/a|
  content_sha256=<sha of resulting falsifier-master-inventory.md>|
  audit_sha256=<closure of input-pin map>

Companion comment row per W9a-99 dual-SHA template.

GPU: NOT NEEDED (mechanical file edit; no eigvals / SVD / matmul).
OMP_NUM_THREADS: NOT NEEDED.
Python interpreter: NOT NEEDED unless invoking _dual_sha_uniqueness_audit.py
for SHA computation, in which case use phonon-exflation-sim/.venv312/
Scripts/python.exe.
```

### Field 7 — Machinery pin (PRDR)

| Pin | Value |
|:----|:------|
| `inventory_target_path` | `sessions/framework/registry/falsifier-master-inventory.md` |
| `target_row_id` | Row #1 (w_0) |
| `source_verdicts_pinned` | W7-7, W1a-5, W10-2, W12-4 (all in `computations/s85_gate_verdicts.txt`) |
| `s85_verdicts_input_sha` | `<computed-at-runtime — SHA256 of computations/s85_gate_verdicts.txt at S86 plan-freeze>` |
| `edit_rule` | ADDITIVE only — sub-pin table appended after existing prediction cell + single-line W10-2 audit-pin reference; no mutation of existing Row #1 content |
| `dual_sha_audit` | invoke `computations/_dual_sha_uniqueness_audit.py` post-edit to confirm no SHA collision against S85 verdicts |
| `validator` | `computations/_plan_upstream_pin_validator.py --json` exit 0 against post-edit inventory |

### Field 8 — Expected output 4-tuple
`(value=sub_pin_count=3, scheme=inventory, convention=MD-EDIT, L_max=n/a)` — META gate, L_max not applicable (the edit consolidates verdicts that span L=8/10/12).

### Field 9 — PASS / FAIL / INFO thresholds

| Verdict | Criterion | Tolerance rule |
|:--------|:----------|:---------------|
| PASS | All 6 cells present in each of 3 sub-pin rows + W10-2 reference line present + all 4 cited SHAs match `s85_gate_verdicts.txt` | RATIO: cell count = 18 (= 3 rows × 6 cols) AND reference line non-empty AND SHA-match exact |
| FAIL | Any cell missing OR any SHA mismatch | n_missing ≥ 1 OR n_sha_mismatch ≥ 1 |
| INFO | not applicable for this gate | — |

### Field 10 — Substitution chain
**Not required**. This gate makes no sign / direction / threshold claim. It is a mechanical inventory edit. Per `.claude/rules/math-scripts.md` §"When the chain is NOT required" — definitions-only statements with no direction claim are exempt.

### Field 11 — What PASSES / FAILS MEAN for solution space

PASS: Row #1 of falsifier-master-inventory becomes regulator-layer-disambiguated; downstream DESI DR3 contingency planning (W12 P8 sub-tree extension, S85 carry-forward chain) cites this row directly without ambiguity over which L_max produces which w_0 value. P9 (W13) w_0_FW PRIMARY adjudication has a single canonical row to cross-reference.

FAIL: Inventory remains regulator-blind on Row #1; DESI DR3 contingency tree must hardcode W7-7 / W1a-5 / W10-2 SHAs inline rather than citing the row, fragmenting the audit trail. Actionable: re-dispatch with corrected sub-pin table.

### Field 12 — Effort estimate
30 min (single-row inventory edit + 4-SHA cross-check via grep against s85 verdicts file).

### Field 13 — Substrate-framing reminder
w_0 is the equation-of-state at z=0. Framework derivation routes through the substrate-compaction timescape mechanism (clock variance from fiber tau-distribution heterogeneity) for branch-(iv) at -0.842454, and through the Volovik partition (q-theory CC residual) for canonical -0.918. Both are SUBSTRATE PROPERTIES of the spectral triple — w_0 emerges from D_K spectral structure, not from a separate dark-energy field "in" spacetime. This row is a substrate observable.

---

## §W14-2. S86-WATCHLIST-W2-EDIT (Row #3 α_s §VII.Ω)

**Carries forward**: partition §1 W14 item W2 (watchlist) — Row #3 α_s §VII.Ω strengthening citation

### Field 1 — Gate ID
`S86-WATCHLIST-W2-EDIT`

### Field 2 — Trigger
`[VERIFY]` — verify W13-2 joint-Fisher pin SHA citation lands without value mutation.

### Field 3 — Classification
META — registry maintenance.

### Field 4 — Agent type
`mack-cosmic-bridge` — observational watchlist + α_s-§VII.Ω cross-reference is mack-track. NOT `gen-physicist`.

### Field 5 — Hypothesis
Adding the W13-2 joint-Fisher pin SHA `f514d642fe2a80ac…` (full 64-char hexdigest extracted at runtime from `computations/s85_gate_verdicts.txt`) as a strengthening citation to Row #3 (α_s §VII.Ω) increases the row's audit-traceability without altering its prediction value or PASS/FAIL status.

### Field 6 — Method (complete dispatch prompt)

```
SUBJECT: S86-WATCHLIST-W2-EDIT — Row #3 (α_s §VII.Ω) joint-Fisher pin citation

Read the standard rule files (agent-standards, output-standards,
gate-verdicts, phononic-framing) before editing.

Target file: sessions/framework/registry/falsifier-master-inventory.md

Action: Locate Row #3 (α_s §VII.Ω) — current text references the
22.99σ W13-2 result against LCDM. Append a single citation line
in the row's "audit pins" sub-cell (or create the sub-cell if absent):

  "W13-2 joint-Fisher pin: content_sha256=<full 64-hex from W13-2
   verdict line in computations/s85_gate_verdicts.txt> --
   strengthening citation only; no value change to α_s prediction."

The expected SHA prefix is `f514d642fe2a80ac` (per partition §1 W14
W2 source). Extract the FULL 64-hex at runtime from the W13-2 verdict
line; do NOT hardcode a truncated form. Per .claude/rules/gate-verdicts.md
the canonical line uses the full 64-char SHA.

Cross-check before commit:
  1. grep "W13-2" computations/s85_gate_verdicts.txt -- confirm verdict line exists
  2. Confirm the extracted full-64-hex SHA begins with "f514d642fe2a80ac"
  3. Confirm Row #3 α_s value is UNCHANGED (-0.068968 from S85 §1.2 W13-2)

Output: edited sessions/framework/registry/falsifier-master-inventory.md.

Append verdict line:
  S86-WATCHLIST-W2-EDIT|PASS|<sha_citations_added=1>|inventory|MD-EDIT|n/a|
  content_sha256=<post-edit inventory SHA>|audit_sha256=<closure>

Companion comment row per W9a-99.

GPU: NOT NEEDED.
```

### Field 7 — Machinery pin (PRDR)

| Pin | Value |
|:----|:------|
| `inventory_target_path` | `sessions/framework/registry/falsifier-master-inventory.md` |
| `target_row_id` | Row #3 (α_s §VII.Ω) |
| `source_verdict_pinned` | W13-2 in `computations/s85_gate_verdicts.txt` |
| `expected_sha_prefix` | `f514d642fe2a80ac` (16-hex; extract full 64-hex at runtime) |
| `s85_verdicts_input_sha` | `<computed-at-runtime>` |
| `edit_rule` | ADDITIVE — citation line only; α_s value cell UNCHANGED |
| `value_mutation_check` | grep Row #3 pre-edit vs post-edit; α_s value cell must be byte-identical |
| `validator` | `_plan_upstream_pin_validator.py --json` exit 0 |

### Field 8 — Expected output 4-tuple
`(value=sha_citations_added=1, scheme=inventory, convention=MD-EDIT, L_max=n/a)`

### Field 9 — PASS / FAIL / INFO thresholds

| Verdict | Criterion | Tolerance rule |
|:--------|:----------|:---------------|
| PASS | W13-2 SHA citation line present with full 64-hex (prefix matches `f514d642fe2a80ac`) AND Row #3 α_s value cell UNCHANGED (byte-identical pre/post) | RATIO: SHA-match exact AND value-cell byte-equal |
| FAIL | SHA prefix mismatch OR Row #3 α_s value cell mutated | n_sha_match=0 OR n_value_mutations≥1 |
| INFO | n/a | — |

### Field 10 — Substitution chain
**Not required**. Strengthening-citation-only edit; no direction claim.

### Field 11 — What PASSES / FAILS MEAN for solution space
PASS: α_s §VII.Ω row gains explicit joint-Fisher provenance, supporting downstream Fisher-PDF-pinned re-emissions (W12 C32). The 22.99σ separation between framework α_s = -0.068968 and Planck/ACT canonical α_s = +0.0023 ± 0.0063 (per P12 update) is now traceable to a single audited verdict line.

FAIL: Citation absent or value mutated; downstream Fisher-discount audits (S85 W4-6) lose the audit chain back to W13-2.

### Field 12 — Effort estimate
15 min.

### Field 13 — Substrate-framing reminder
α_s (running of the spectral index) is a substrate property — the framework prediction α_s = -0.068968 emerges from the D_K spectral curvature at the pivot scale, not from inflaton dynamics in spacetime. Row #3 anchors this substrate prediction against multi-experiment (Planck + ACT + future CMB-S4 + CMB-HD) pull from the SDW canonical α_s pin (P12).

---

## §W14-3. S86-WATCHLIST-W3-EDIT (Row #7 CGWB ρ_AC)

**Carries forward**: partition §1 W14 item W3 (watchlist) — Row #7 CGWB ρ_AC Companion-null-(C-regulator) column

### Field 1 — Gate ID
`S86-WATCHLIST-W3-EDIT`

### Field 2 — Trigger
`[VERIFY]` — verify Companion-null-(C-regulator) column lands with W13-2.Ω value 8.299e-58 + (A)/(C) discriminator paragraph.

### Field 3 — Classification
META — registry maintenance with substrate-direct content (CGWB is a substrate observable).

### Field 4 — Agent type
`mack-cosmic-bridge` — CGWB observational watchlist + LISA detector chain is mack-track. NOT `gen-physicist`.

### Field 5 — Hypothesis
Adding a Companion-null-(C-regulator) column to Row #7 (CGWB ρ_AC) with the W13-2.Ω value Ω_GW(LISA) = 8.299e-58 (the 45-OOM null per S85 §1.2) and a documenting paragraph for the (A) / (C) regulator-class discriminator structure makes Row #7 explicitly bipolar: (A)-regulator-class predicts O(10^-10) LISA-detectable Ω_GW, (C)-regulator-class predicts the W13-2.Ω 45-OOM null. Future LISA verdicts then map directly onto regulator-class adjudication.

### Field 6 — Method (complete dispatch prompt)

```
SUBJECT: S86-WATCHLIST-W3-EDIT — Row #7 (CGWB ρ_AC) Companion-null column + (A)/(C) discriminator

Read the standard rule files before editing.

Target file: sessions/framework/registry/falsifier-master-inventory.md

Action 1 — Add a Companion-null-(C-regulator) column to Row #7 (CGWB ρ_AC).
Column header: "C-regulator companion null Ω_GW(LISA)"
Cell value:    8.299e-58 (per S85 §1.2 W13-2 verdict; cite content_sha256
               from computations/s85_gate_verdicts.txt W13-2 line)

Action 2 — Append a documenting paragraph immediately below the row
(within the row's "Discriminator" or "Notes" sub-section, creating
the sub-section if absent):

  "(A) / (C) regulator-class discriminator structure: The 5-regulator
  atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} splits into pure-a_4
  family F_4 = {ζ, Zubarev, SDW} (the (A)-regulator class) and
  mixed-support family M = {cutoff_sqrt, anomaly} (the (C)-regulator
  class) per S85 W12-4 + lizzi S-7 §V.6 Mellin Strip Theorem. CGWB
  Ω_GW(LISA) is regulator-class-bipolar: (A) class predicts
  O(10^-10) LISA-detectable spectral density at f_LISA = 3 mHz
  (cross-ref CGWB-ABSOLUTE-PT family); (C) class predicts the
  W13-2.Ω 45-OOM null Ω_GW = 8.299e-58. A LISA detection at
  Ω_GW > 10^-12 falsifies (C); a LISA non-detection at
  Ω_GW < 10^-12 over the 4-yr nominal mission is consistent with
  both (with (C) the cleaner null). Cross-reference: S86 W8 P6/P7
  CGWB ⊥ α_s 3-arm × 3-layer commit; S86 W3 W0-7 re-emission;
  C7 L_max-direct."

DO NOT alter Row #7's existing primary prediction cell. The column
addition + discriminator paragraph are ADDITIVE.

Cross-check before commit:
  1. grep "W13-2" computations/s85_gate_verdicts.txt -- confirm
     Ω_GW(LISA)=8.299e-58 in the verdict line
  2. Confirm Row #7 primary prediction cell BYTE-UNCHANGED pre/post

Output: edited sessions/framework/registry/falsifier-master-inventory.md.

Append verdict line:
  S86-WATCHLIST-W3-EDIT|PASS|<column_added=1, paragraphs_added=1>|inventory|
  MD-EDIT|n/a|content_sha256=<post-edit inventory SHA>|audit_sha256=<closure>

Companion comment row.

GPU: NOT NEEDED.
```

### Field 7 — Machinery pin (PRDR)

| Pin | Value |
|:----|:------|
| `inventory_target_path` | `sessions/framework/registry/falsifier-master-inventory.md` |
| `target_row_id` | Row #7 (CGWB ρ_AC) |
| `source_verdict_pinned` | W13-2 (Ω_GW(LISA)=8.299e-58 component) in `s85_gate_verdicts.txt` |
| `column_value_pinned` | 8.299e-58 (cite verbatim from W13-2 verdict line) |
| `regulator_class_partition` | F_4 = {ζ, Zubarev, SDW} (A); M = {cutoff_sqrt, anomaly} (C); per S85 W12-4 + lizzi S-7 §V.6 |
| `falsification_threshold` | LISA Ω_GW > 10^-12 falsifies (C); cite as forward-falsifier (not a S86 gate) |
| `s85_verdicts_input_sha` | `<computed-at-runtime>` |
| `edit_rule` | ADDITIVE — new column + new sub-section; no mutation of existing Row #7 cells |
| `value_mutation_check` | byte-equal pre/post on Row #7 primary prediction cell |
| `validator` | `_plan_upstream_pin_validator.py --json` exit 0 |

### Field 8 — Expected output 4-tuple
`(value=column_added=1+paragraphs_added=1, scheme=inventory, convention=MD-EDIT, L_max=n/a)`

### Field 9 — PASS / FAIL / INFO thresholds

| Verdict | Criterion | Tolerance rule |
|:--------|:----------|:---------------|
| PASS | New column "C-regulator companion null Ω_GW(LISA)" present with value 8.299e-58 AND discriminator paragraph present (named (A)/(C) classes + 5-regulator partition + LISA falsification threshold cited) AND Row #7 primary cell byte-unchanged | RATIO: column-cell-count=1 AND paragraph-non-empty AND value-byte-equal pre/post |
| FAIL | Column missing OR value mismatch with 8.299e-58 OR paragraph missing or omitting (A)/(C) discriminator structure OR Row #7 primary cell mutated | any criterion failed |
| INFO | n/a | — |

### Field 10 — Substitution chain
**Not required**. Discriminator structure cites pre-existing W12-4 + lizzi S-7 §V.6 partition; no new direction claim.

### Field 11 — What PASSES / FAILS MEAN for solution space
PASS: Row #7 becomes the canonical CGWB regulator-class adjudication anchor. Future LISA data (mid-2030s nominal) maps directly onto (A) vs (C) class adjudication via this row. The 45-OOM Ω_GW gap between (A) ~ 10^-10 and (C) ~ 10^-58 is not an embarrassment — it is the cleanest single-detector regulator-class discriminator the framework offers.

FAIL: Inventory remains regulator-class-blind on CGWB; downstream LISA-Fisher integrations (W12 C32) and CGWB three-layer adjudication (W8 P6/P7) lose the bipolar prediction structure.

### Field 12 — Effort estimate
30 min.

### Field 13 — Substrate-framing reminder
CGWB Ω_GW is a SUBSTRATE OBSERVABLE — gravitational-wave background generated by phonon-relay patterns in the post-fold GGE relic, propagating on the emergent g_M metric. The (A)/(C) regulator-class structure is INTERNAL to the substrate spectral triple — different regulator choices select different a_4 spectral content, and a_4 is the gravity-channel spectral moment. (A)-class regulators preserve a_4 magnitude; (C)-class regulators suppress it ~45 OOM. This row is structurally substrate-direct.

---

## §W14-4. S86-WATCHLIST-W4-EDIT (Row #9 f_NL_folded 3-pathway)

**Carries forward**: partition §1 W14 item W4 (watchlist) — Row #9 f_NL_folded 3-pathway expansion

### Field 1 — Gate ID
`S86-WATCHLIST-W4-EDIT`

### Field 2 — Trigger
`[VERIFY]` — verify 3-pathway sub-table (S82 W3-4 / S67 / S85 W9-3) lands with all 4 fields per pathway.

### Field 3 — Classification
META — registry maintenance, partial overlap with W13 P10 (consolidates same 3 predictions in a separate dedicated registry file `sessions/framework/registry/f-nl-folded-pathway-registry.md`). The W14-4 inventory edit summarizes; P10 expands.

### Field 4 — Agent type
`mack-cosmic-bridge` — non-Gaussianity / SKA-1 / 21cm Fisher chain is mack-track.

### Field 5 — Hypothesis
Expanding Row #9 (f_NL_folded) from a single-value cell to a 3-pathway sub-table makes explicit that the framework predicts THREE distinct f_NL_folded values across THREE distinct mechanism pathways — S82 W3-4 GGE-equilateral 0.0547, S67 GGE-folded 0.129, S85 W9-3 analytic-template-folded 0.7685 — with each pathway carrying its own (scheme, convention, L_max, content_sha256) tuple.

### Field 6 — Method (complete dispatch prompt)

```
SUBJECT: S86-WATCHLIST-W4-EDIT — Row #9 (f_NL_folded) 3-pathway sub-table

Read the standard rule files before editing.

Target file: sessions/framework/registry/falsifier-master-inventory.md

Action: Replace Row #9's single-value f_NL_folded cell with a 3-row
sub-table. Columns: (Pathway | f_NL value | scheme | convention |
L_max | content_sha256 | audit_sha256_short).

Pathway rows (extract content_sha256 + audit_sha256_short from
the cited verdict files at runtime):

  Row A: S82 W3-4 GGE-equilateral
    f_NL value: 0.0547
    scheme:     <as recorded in S82 W3-4 verdict>
    convention: GGE-equilateral
    L_max:      <as recorded in S82 W3-4 verdict>
    content_sha256: <full 64-hex from computations/s82_gate_verdicts.txt
                     S82-W3-4 line>
    audit_sha256_short: <16-hex from companion>

  Row B: S67 GGE-folded
    f_NL value: 0.129
    scheme:     <as recorded in S67 verdict for GGE-folded computation>
    convention: GGE-folded
    L_max:      <as recorded>
    content_sha256: <full 64-hex from S67 verdict file>
    audit_sha256_short: <16-hex>

  Row C: S85 W9-3 analytic-template-folded
    f_NL value: 0.7685
    scheme:     <as recorded in S85 W9-3 verdict>
    convention: analytic-template-folded
    L_max:      <as recorded>
    content_sha256: <full 64-hex from computations/s85_gate_verdicts.txt
                     W9-3 line>
    audit_sha256_short: <16-hex>

Append a single-line cross-reference below the sub-table:
  "Cross-reference: P10 (W13) S86-FNL-FOLDED-PATHWAY-REGISTRY consolidates
   these 3 pathways at sessions/framework/registry/f-nl-folded-pathway-registry.md
   with fuller per-pathway derivation provenance. Falsifier alignment:
   SKA-1 σ(f_NL) ≈ 5.0 (per S85 W9-3 detector-sterile classification);
   CMB-S4 σ ≈ 5.0-6.9 (per S68 CMBS4-FNL-FORECAST); 21cm l_max ~ 10^5
   needed for detection."

DO NOT preserve the original single-value cell — REPLACE it with the
3-row sub-table. The replacement is a structural row-format upgrade,
not an additive enrichment, because the original 1-value form
mis-represented the framework as having a SINGLE f_NL_folded prediction.

Cross-check before commit:
  1. grep "W3-4" computations/s82_gate_verdicts.txt -- confirm 0.0547
  2. grep "W9-3" computations/s85_gate_verdicts.txt -- confirm 0.7685
  3. Locate S67 GGE-folded verdict in computations/ if necessary --
     confirm 0.129. If S67 verdict file is not in computations/,
     mark Row B's content_sha256 cell as
     "<S67-pre-canonical-verdict-format; reconstruct via session-67-final.md>"
     and proceed; flag as INFO if the reconstruction is ambiguous.

Output: edited sessions/framework/registry/falsifier-master-inventory.md.

Append verdict line:
  S86-WATCHLIST-W4-EDIT|PASS|<pathway_rows=3>|inventory|MD-EDIT|n/a|
  content_sha256=<post-edit inventory SHA>|audit_sha256=<closure>

Companion comment row.

GPU: NOT NEEDED.
```

### Field 7 — Machinery pin (PRDR)

| Pin | Value |
|:----|:------|
| `inventory_target_path` | `sessions/framework/registry/falsifier-master-inventory.md` |
| `target_row_id` | Row #9 (f_NL_folded) |
| `source_verdicts_pinned` | (S82 W3-4, value 0.0547), (S67 GGE-folded, value 0.129), (S85 W9-3, value 0.7685) |
| `s82_verdicts_input_sha` | `<computed-at-runtime — SHA256 of computations/s82_gate_verdicts.txt>` |
| `s85_verdicts_input_sha` | `<computed-at-runtime — SHA256 of computations/s85_gate_verdicts.txt>` |
| `s67_provenance` | locate S67 verdict in computations/ if available; if pre-canonical-verdict-format, cite session-67-final.md and flag for INFO if ambiguous |
| `edit_rule` | REPLACE single-value cell with 3-row sub-table; ADDITIVE on cross-reference line to P10 |
| `cross_reference_target` | P10 (W13) `S86-FNL-FOLDED-PATHWAY-REGISTRY` at `sessions/framework/registry/f-nl-folded-pathway-registry.md` |
| `validator` | `_plan_upstream_pin_validator.py --json` exit 0 |

### Field 8 — Expected output 4-tuple
`(value=pathway_rows=3, scheme=inventory, convention=MD-EDIT, L_max=n/a)`

### Field 9 — PASS / FAIL / INFO thresholds

| Verdict | Criterion | Tolerance rule |
|:--------|:----------|:---------------|
| PASS | All 3 pathway rows present with all 7 fields each (= 21 cells) AND P10 cross-reference line present AND values match (0.0547, 0.129, 0.7685) | RATIO: cell count = 21 AND value-match exact |
| FAIL | Any pathway row missing OR value mismatch OR cross-reference line missing | any criterion failed |
| INFO | S67 verdict provenance ambiguous (pre-canonical format and session-67-final.md reconstruction inconclusive) — Row B SHA cell flagged but Rows A and C clean | exactly 1 row's SHA-cell ambiguous; mark INFO with explicit Row-B-SHA-deferred annotation; downstream P10 (W13) resolves |

### Field 10 — Substitution chain
**Not required**. The 3-pathway expansion is a registry-format upgrade citing pre-existing verdicts; no new direction or threshold claim.

### Field 11 — What PASSES / FAILS MEAN for solution space
PASS: Row #9 becomes pathway-disambiguated. The framework's actual f_NL_folded prediction structure (3 mechanism-distinct values spanning ~14× spread between 0.0547 and 0.7685) is visible at-a-glance, eliminating the previous mis-framing as a single-value prediction. Future SKA-1 / CMB-S4 / 21cm IM data adjudicates between pathways, not between framework-and-LCDM.

FAIL: Inventory remains pathway-blind; downstream P10 W13 registry build misses its anchor row.

INFO (S67 ambiguity case): Same as PASS for downstream consumers, with explicit S86 carry-forward to P10 to resolve Row B SHA.

### Field 12 — Effort estimate
45 min (3-verdict cross-check across two session files + S67 archive lookup).

### Field 13 — Substrate-framing reminder
f_NL_folded is a SUBSTRATE OBSERVABLE — folded-shape non-Gaussianity in the GGE relic acoustic excitations, generated at the substrate fold. The 3 pathways are NOT three competing models — they are three DIFFERENT spectral-derivation routes through the same SUBSTRATE TRIPLE, each capturing different aspects (equilateral vertex, folded vertex, analytic-template integration) of the same underlying GGE bispectrum. The 14× spread between routes is a SCHEME-DEPENDENCE diagnostic, not a model uncertainty.

---

## §W14-5. S86-WATCHLIST-W5-EDIT (Row #12 A_s ε-sensitivity)

**Carries forward**: partition §1 W14 item W5 (watchlist) — Row #12 A_s ε-sensitivity sub-note

### Field 1 — Gate ID
`S86-WATCHLIST-W5-EDIT`

### Field 2 — Trigger
`[VERIFY]` — verify ε-sensitivity sub-note lands with range 3.11e-9 → 4.27e-9 over ε ∈ {0.02163, 0.020} + S86 SECTOR-1 carry-forward annotation.

### Field 3 — Classification
META — registry maintenance with explicit forward-pointer to S86 SECTOR-1 (W5a P3) ε_pivot resolution.

### Field 4 — Agent type
`mack-cosmic-bridge` — A_s observational watchlist + Planck pivot-scale chain is mack-track.

### Field 5 — Hypothesis
Adding an ε-sensitivity sub-note to Row #12 (A_s) documents that the framework's A_s prediction varies over the range 3.11e-9 → 4.27e-9 depending on the ε_H pivot value (small ε_H = 0.020 vs canonical ε_H = 0.02163), and that ε_pivot resolution is a pre-registered S86 SECTOR-1 carry-forward (W5a P3 SR-flow Z-factor integration). This makes the row's prediction-band visible AND documents its dependency on a separately-pinned downstream S86 gate.

### Field 6 — Method (complete dispatch prompt)

```
SUBJECT: S86-WATCHLIST-W5-EDIT — Row #12 (A_s) ε-sensitivity sub-note

Read the standard rule files before editing.

Target file: sessions/framework/registry/falsifier-master-inventory.md

Action: Append an ε-sensitivity sub-note to Row #12 (A_s). Locate the
row's "Notes" or "Scheme dependence" sub-cell (create if absent) and
append:

  "ε-sensitivity sub-note: A_s prediction varies over the range
  3.11e-9 → 4.27e-9 across ε_H ∈ {0.02163 (canonical, S77 SECTOR-1
  prior), 0.020 (alternate pivot per S85 W3-7 4-level taxonomy)}.
  The framework's A_s value is therefore pivot-conditional. ε_pivot
  RESOLUTION is a pre-registered S86 carry-forward — see W5a P3
  S86-SECTOR-1-SR-FLOW-Z-FACTOR (substrate-first ξ²(0) IC ODE
  integration; HARD DEPENDENCY on W4 P4 BRANCH-IV
  ξ_E_GGE^{-1} pin). Until P3 closes, Row #12 A_s prediction
  must be cited as a band, not a point. Cross-references:
  S85 W3-7 4-level unit-class taxonomy (Both-Pathways
  FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030); S86 W13 P1
  FROZEN-COMMIT-LANDING."

DO NOT mutate the existing Row #12 prediction cell. The sub-note is
ADDITIVE.

Cross-check before commit:
  1. grep "W3-7" computations/s85_gate_verdicts.txt -- confirm
     W3-7 4-level taxonomy verdict line exists
  2. Confirm 3.11e-9 / 4.27e-9 / ε ∈ {0.02163, 0.020} as cited from
     mack 9A §III.3 #5
  3. Confirm W5a P3 (S86-SECTOR-1-SR-FLOW-Z-FACTOR) appears in
     sessions/session-plan/session-86-plan-w5a.md as a
     pre-registered S86 gate (forward reference; if W5a plan
     file not yet committed, reference it as
     "<plan-file-pending>" and validator will accept until
     S86 plan-freeze when validator re-runs against the full
     S86 plan corpus)

Output: edited sessions/framework/registry/falsifier-master-inventory.md.

Append verdict line:
  S86-WATCHLIST-W5-EDIT|PASS|<sub_note_added=1>|inventory|MD-EDIT|n/a|
  content_sha256=<post-edit inventory SHA>|audit_sha256=<closure>

Companion comment row.

GPU: NOT NEEDED.
```

### Field 7 — Machinery pin (PRDR)

| Pin | Value |
|:----|:------|
| `inventory_target_path` | `sessions/framework/registry/falsifier-master-inventory.md` |
| `target_row_id` | Row #12 (A_s) |
| `epsilon_range_pinned` | ε_H ∈ {0.02163, 0.020}; A_s ∈ [3.11e-9, 4.27e-9] |
| `source_citation` | mack 9A §III.3 #5 |
| `forward_reference` | W5a P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` (ε_pivot resolution) |
| `cross_reference` | S85 W3-7 4-level taxonomy; S86 W13 P1 FROZEN-COMMIT-LANDING |
| `s85_verdicts_input_sha` | `<computed-at-runtime>` |
| `edit_rule` | ADDITIVE — sub-note only; existing Row #12 prediction cell unchanged |
| `value_mutation_check` | byte-equal pre/post on Row #12 primary cell |
| `validator` | `_plan_upstream_pin_validator.py --json` exit 0 (forward reference to W5a P3 accepted as pending until S86 plan-freeze) |

### Field 8 — Expected output 4-tuple
`(value=sub_note_added=1, scheme=inventory, convention=MD-EDIT, L_max=n/a)`

### Field 9 — PASS / FAIL / INFO thresholds

| Verdict | Criterion | Tolerance rule |
|:--------|:----------|:---------------|
| PASS | Sub-note present with full ε range + A_s range + S86 SECTOR-1 forward reference + S85 W3-7 cross-reference + S86 W13 P1 cross-reference AND Row #12 primary cell byte-unchanged | RATIO: 5 required content tokens present AND value-byte-equal pre/post |
| FAIL | Sub-note missing OR any required token missing OR Row #12 primary cell mutated | any criterion failed |
| INFO | n/a | — |

### Field 10 — Substitution chain
**Not required**. ε-sensitivity range is cited verbatim from mack 9A §III.3 #5; no new direction claim. (The directional statement "A_s varies OVER the range" is not a sign claim — it is a band declaration.)

### Field 11 — What PASSES / FAILS MEAN for solution space
PASS: Row #12 becomes ε-pivot-aware. Downstream LiteBIRD / CMB-S4 / Planck Fisher integrations cite the prediction as a [3.11e-9, 4.27e-9] band, not as a point that may be wrongly tested at the wrong pivot. The forward reference to W5a P3 makes the path-to-resolution explicit: when SECTOR-1 closes, the band collapses (or the sub-note is updated to reflect band-narrowing).

FAIL: Inventory remains ε-pivot-blind; A_s row mis-tested as a point against Planck A_s = 2.1e-9 (off-band, ~32% low) when the actual framework prediction is conditional on a separately-pinned ε pivot. This is the kind of mis-framing the FROZEN-PREDICTION-DISCIPLINE-COMMIT exists to prevent.

### Field 12 — Effort estimate
30 min.

### Field 13 — Substrate-framing reminder
A_s is the scalar amplitude at the pivot scale — emerges from the SUBSTRATE z-factor evolution under SR flow on the spectral triple. ε_H is itself a SUBSTRATE PROPERTY (slow-roll parameter computed from D_K spectral structure at the fold). The ε-sensitivity is NOT model-uncertainty — it is the framework's honesty that A_s and ε_H couple through the substrate's own SR flow, and ε_pivot pinning requires SECTOR-1 ODE integration (W5a P3) that has not closed yet.

---

## §W14-6. S86-WATCHLIST-W6-NEW-CLASS (Rows #13-#21 lab-falsifier suite)

**Carries forward**: partition §1 W14 item W6 (watchlist) — NEW row class #13-#21 lab-falsifier suite (9 atomic predictions: 3 sweet-spot + 6 cross-platform)

### Field 1 — Gate ID
`S86-WATCHLIST-W6-NEW-CLASS`

### Field 2 — Trigger
`[VERIFY]` — verify 9 NEW rows land with all 4 required fields per row + EVOI tag + P_decisive band.

### Field 3 — Classification
META — registry maintenance, with substrate-direct content (lab-analog observables are substrate predictions).

### Field 4 — Agent type
`mack-cosmic-bridge` — terrestrial-lab observational watchlist + S82 W8-4 lab-analog cross-channel chain is mack-track.

### Field 5 — Hypothesis
Creating a NEW row class spanning rows #13-#21 of `sessions/framework/registry/falsifier-master-inventory.md` — populated with 9 atomic lab-analog predictions (3 sweet-spot from W8-4 + 6 cross-platform per mack 9A §III.3 #6 + 1B volovik solo) — gives the framework an explicit terrestrial-lab observational portfolio with EVOI tag `LAB-FALSIFIER` and P_decisive ∈ [0.30, 0.50] over a 5-yr horizon. Each row carries (δE_a / observable-magnitude / platform / SI-translation-pending status) as the four canonical fields.

### Field 6 — Method (complete dispatch prompt)

```
SUBJECT: S86-WATCHLIST-W6-NEW-CLASS — NEW Rows #13-#21 lab-falsifier suite

Read the standard rule files before editing.

Target file: sessions/framework/registry/falsifier-master-inventory.md

Action: Add NEW row class spanning rows #13-#21 (9 atomic rows) at the
end of the inventory's primary table. Use the following row template
per atomic prediction:

| # | Observable | δE_a (energy scale) | Magnitude (M_KK-normalized) | Platform | SI-translation status |
|:--|:-----------|:---------------------|:----------------------------|:---------|:----------------------|
| 13 | <name> | <energy>             | <ratio>                     | <lab>    | <pending / pinned>    |

The 9 rows decompose as 3 sweet-spot + 6 cross-platform. Source data:
W8-4 (3 sweet-spot, per S85 §1.2 W8-4 with ³He-A + FeSe + ¹⁷³Yb
explicit values δω_K/ω_K=1.7267, K_anis/K_0=1.8226, 3-body
Γ-ratio=2.8500), plus 6 cross-platform observables per mack 9A §III.3
#6 + 1B volovik solo (extract specific observables + magnitudes from
W11 C5 SI-translation output and W11 C6 EVOI-tree output —
cross-reference the working-paper sections those gates write).

Sweet-spot (W8-4 source) — Rows #13-#15:
  #13: ³He-A δω_K/ω_K  — magnitude 1.7267 (M_KK-normalized) —
       platform ³He-A — SI-translation status: PINNED-via-W11-C5
       (cite W11 C5 verdict content_sha256 from
       computations/s86_gate_verdicts.txt at runtime)
  #14: FeSe K_anis/K_0  — magnitude 1.8226 — platform FeSe —
       SI status: PINNED-via-W11-C5
  #15: ¹⁷³Yb 3-body Γ-ratio — magnitude 2.8500 — platform ¹⁷³Yb
       optical lattice — SI status: PINNED-via-W11-C5

Cross-platform (mack 9A §III.3 #6 + 1B volovik) — Rows #16-#21:
Extract the 6 observable specifications from W11 C5 + C6 outputs.
Each row carries (δE_a, M_KK-normalized magnitude, platform name,
SI-translation status). If W11 C5 / C6 outputs not yet committed at
the time this gate dispatches, mark each row's "Magnitude" and
"SI-translation status" cells as
"<pending W11 C5/C6 outputs; populate at S86 plan-freeze>"
and tag the gate INFO until W11 closes.

Atop the new row class, add a banner row:
  "## Lab-falsifier suite (rows #13-#21) -- 9 atomic predictions
   -- EVOI tag: LAB-FALSIFIER -- P_decisive band: [0.30, 0.50]
   over 5-yr terrestrial-lab horizon (per mack 9A §III.3 #6 +
   W8-4 + 1B volovik solo). Cross-references: W11 C5
   S86-LAB-SI-TRANSLATION (per-platform σ_detect literature
   anchors); W11 C6 S86-LAB-FALSIFIER-EVOI-TREE (5-yr decision
   tree per row); W12 C30 S86-DETECTOR-READINESS-9-CELL
   (lab-analogs ³He-B + K-STAR cell)."

Cite the source SHA chain explicitly:
  - W8-4 source: extract content_sha256 from
    computations/s85_gate_verdicts.txt W8-4 line
  - W11 C5 source: extract content_sha256 from
    computations/s86_gate_verdicts.txt W11-C5 line
    (PENDING — populate at runtime once W11 closes; if W11
    has not closed yet, mark INFO and dispatch this gate
    AFTER W11)
  - W11 C6 source: same pattern as C5

Cross-check before commit:
  1. Confirm W11 C5 + C6 verdict lines exist in computations/
     s86_gate_verdicts.txt (this gate is HARD-DEPENDENT on W11
     completion; if W11 verdicts not yet present, defer to
     post-W11 dispatch)
  2. Confirm W8-4 verdict in computations/s85_gate_verdicts.txt
     (3 sweet-spot magnitudes 1.7267, 1.8226, 2.8500)
  3. Confirm 9 rows present (3 sweet-spot + 6 cross-platform)
  4. Confirm banner row present with EVOI tag, P_decisive band,
     and 3 cross-references (W11 C5, W11 C6, W12 C30)

Output: edited sessions/framework/registry/falsifier-master-inventory.md.

Append verdict line:
  S86-WATCHLIST-W6-NEW-CLASS|PASS|<new_rows=9>|inventory|
  MD-EDIT|n/a|content_sha256=<post-edit inventory SHA>|
  audit_sha256=<closure of input-pin map including W11 C5/C6 SHAs>

Companion comment row.

GPU: NOT NEEDED.
```

### Field 7 — Machinery pin (PRDR)

| Pin | Value |
|:----|:------|
| `inventory_target_path` | `sessions/framework/registry/falsifier-master-inventory.md` |
| `target_row_range` | NEW Rows #13-#21 (9 atomic rows) |
| `evoi_tag_pinned` | `LAB-FALSIFIER` |
| `p_decisive_band` | [0.30, 0.50] over 5-yr terrestrial-lab horizon |
| `sweet_spot_count` | 3 (Rows #13-#15) — ³He-A δω_K/ω_K=1.7267, FeSe K_anis/K_0=1.8226, ¹⁷³Yb 3-body Γ-ratio=2.8500 |
| `cross_platform_count` | 6 (Rows #16-#21) — populated from W11 C5 + C6 outputs |
| `source_w8_4` | S85 W8-4 verdict in `computations/s85_gate_verdicts.txt` (sweet-spot magnitudes) |
| `source_w11_c5` | W11 `S86-LAB-SI-TRANSLATION` in `computations/s86_gate_verdicts.txt` (cross-platform observables + per-platform σ_detect) |
| `source_w11_c6` | W11 `S86-LAB-FALSIFIER-EVOI-TREE` in `computations/s86_gate_verdicts.txt` (EVOI level + 5-yr decision tree per observable) |
| `source_volovik_1b` | 1B volovik solo (S85 closeout reference) |
| `source_mack_9a_iii_3_6` | mack 9A §III.3 #6 |
| `s85_verdicts_input_sha` | `<computed-at-runtime>` |
| `s86_verdicts_input_sha` | `<computed-at-runtime>` (must include W11 C5/C6 lines) |
| `edit_rule` | NEW row class — append at end of primary inventory table; banner row + 9 atomic rows + cross-references; no mutation of existing inventory |
| `hard_dependency` | W11 C5 + W11 C6 must complete and verdict lines present before this gate dispatches |
| `validator` | `_plan_upstream_pin_validator.py --json` exit 0 |

### Field 8 — Expected output 4-tuple
`(value=new_rows=9, scheme=inventory, convention=MD-EDIT, L_max=n/a)`

### Field 9 — PASS / FAIL / INFO thresholds

| Verdict | Criterion | Tolerance rule |
|:--------|:----------|:---------------|
| PASS | All 9 NEW rows present with all 4 required fields each (δE_a, magnitude, platform, SI-translation status) AND banner row present (EVOI tag + P_decisive band + 3 cross-references) AND W8-4 + W11 C5 + W11 C6 SHAs cited in audit_sha256 closure | RATIO: cell count = 36 (= 9 rows × 4 fields) AND banner-row content tokens = 5 (EVOI tag, P_decisive low, P_decisive high, 3 cross-references) AND SHA citations = 3 |
| FAIL | Any row missing OR any of the 4 fields incomplete in any row OR banner missing OR SHA citation absent for any required source | any criterion failed |
| INFO | W11 C5 / C6 not yet closed at dispatch time → cross-platform Rows #16-#21 marked "<pending W11 C5/C6 outputs>"; sweet-spot Rows #13-#15 + banner clean; gate dispatched in INFO mode until W11 closes; auto-promote to PASS post-W11 closure | exactly W11 dependency unresolved AND sweet-spot rows + banner complete |

### Field 10 — Substitution chain
**Not required**. NEW row class consolidates pre-existing W8-4 + 1B volovik observables + W11 C5/C6 outputs; no new direction or threshold claim. EVOI tag and P_decisive band are pinned from mack 9A §III.3 #6 + S85 closeout, not derived in this gate.

### Field 11 — What PASSES / FAILS MEAN for solution space

PASS: Inventory now contains a structured terrestrial-lab portfolio. 9 atomic predictions, each pointing at a specific platform (³He-A, FeSe, ¹⁷³Yb, plus 6 from W11 C5) with a defined magnitude, defined δE_a energy scale, and explicit SI-translation status. The framework crosses from "cosmological-only" to "cosmological + lab-analog" prediction posture. Each row is dispatchable as a forward-falsifier — when a lab-analog measurement publishes (³He-A frequency-shift datasets, FeSe ARPES K-anisotropy, ¹⁷³Yb optical-lattice 3-body decay), the row's PASS/FAIL/refute is mechanically determinable. P_decisive [0.30, 0.50] reflects 5-yr terrestrial-lab maturity uncertainty (some platforms have publication horizons inside 5 yrs, others may slip). EVOI tag `LAB-FALSIFIER` distinguishes these from cosmological tags (CMB-S4, DESI DR3, LISA, etc.) and routes them to the lab-analog readout in `sessions/framework/correspondence/cross-channel-correlation-matrix.md`.

FAIL: Lab-falsifier suite remains absent from the canonical inventory; W11 C5 / C6 outputs orphaned (computed but not registered); framework's terrestrial-lab posture remains scattered across W8-4 + W11 working papers without a single consolidated registry entry. P11 (W13) cannot land its NEW row class enrichment.

INFO (W11 not yet closed at dispatch time): Sweet-spot rows + banner committed; cross-platform rows annotated as pending. Auto-promotes to PASS once W11 closes and this gate re-dispatches with the W11 C5/C6 verdict SHAs available. This is the canonical INFO use-case per `feedback_reporting-framing.md` + `feedback_reporting-framing.md` — INFO is a structured pre-registered outcome, not a failure.

### Field 12 — Effort estimate
1.5h (NEW row class with 9 atomic rows + 4-field-per-row population + banner + 3 SHA citations).

### Field 13 — Substrate-framing reminder
The lab-falsifier suite is the framework's MOST SUBSTRATE-DIRECT observational channel. Each lab observable measures a SUBSTRATE PROPERTY at low-energy / accessible-platform conditions:
- ³He-A is a child correspondence per S85 1B 3-solo (the substrate's fold dynamics inherit ³He-A's transition kinematics — NOT analogy, parent → child);
- FeSe K_anis/K_0 measures band-structure anisotropy that maps onto the substrate's BdG corridor structure;
- ¹⁷³Yb 3-body Γ-ratio measures threshold-resonance kinematics analogous to the substrate's instanton-gas density.
The 6 cross-platform observables (W11 C5/C6) extend this to additional condensed-matter and AMO platforms. Each row is a substrate-IS-NOT-IN-spacetime test: lab observables probe the substrate's INTERNAL spectral content directly, not its emergent metric. EVOI = LAB-FALSIFIER reflects this — terrestrial labs are the framework's only access to the substrate at low-energy non-cosmological conditions.

---

## §X. Wave W14 → Downstream Decision Point

Wave W14 consolidates inventory state for **W15 P13 EVOI-table refresh** (FINAL late-S86 wave) + downstream sessions. Specifically:

1. **W15 P13 EVOI refresh** consumes the post-W14 inventory state — the W14-6 NEW lab-falsifier row class adds 9 atomic predictions to the canonical link inventory, contributing to `P_work_complete` recomputation per `feedback_framework-hygiene.md`. P13 must run AFTER W14 to capture this contribution.

2. **S87+ DESI DR3 contingency** (from W12 C33 + S85 W12 contingency tree) cites Row #1's 3-row sub-pin table (W14-1 output) directly. Without W14-1 PASS, S87 contingency tree must hardcode SHAs inline.

3. **S87+ LISA-Fisher integration** cites Row #7's (A)/(C) discriminator structure (W14-3 output). Without W14-3 PASS, LISA forecast remains regulator-class-blind on CGWB.

4. **S87+ SKA-1 / 21cm Fisher consolidation** cites Row #9's 3-pathway sub-table (W14-4 output). Without W14-4 PASS, f_NL_folded forecast tests against single mis-framed value.

5. **S87+ LiteBIRD A_s integration** cites Row #12's ε-sensitivity sub-note (W14-5 output). Without W14-5 PASS, A_s tested as point against Planck off-band (~32% low).

6. **S86-S91+ terrestrial-lab data ingest** cites Rows #13-#21 (W14-6 output). Without W14-6 PASS, lab-analog data has no canonical row to land against.

**Decision-tree dependencies**: W14 has NO physics-dependent decision tree (no PASS/FAIL/INFO outcome from one W14 sub-gate gates another). All 6 sub-gates dispatch independently within the constraint that W14-6 awaits W11 closure.

---

## §0.10. Wave W14 Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness PRDR (Pre-Registration Dry-Run): every gate-relevant machinery parameter is enumerated below with its pin status.

### W14-1 (Row #1 w_0)
| Free parameter | Pin status | Pin value or rule |
|:---------------|:-----------|:------------------|
| `inventory_target_path` | PINNED | `sessions/framework/registry/falsifier-master-inventory.md` |
| `target_row_id` | PINNED | Row #1 (w_0) |
| `sub_pin_count` | PINNED | 3 (L=8, L=10, L=12) |
| `source_verdicts` | PINNED | W7-7, W1a-5, W10-2, W12-4 |
| `s85_verdicts_input_sha` | computed-at-runtime | SHA256 of `computations/s85_gate_verdicts.txt` at S86 plan-freeze |
| `audit_sha256` | computed-at-runtime | `closure_hash(input_pin_map ∪ machinery_pin_map)` via `_dual_sha_uniqueness_audit.py` |
| `edit_rule` | PINNED | ADDITIVE only |
| `value_mutation_check` | PINNED | byte-equal pre/post on Row #1 primary cell |
| `validator` | PINNED | `_plan_upstream_pin_validator.py --json` exit 0 |

### W14-2 (Row #3 α_s §VII.Ω)
| Free parameter | Pin status | Pin value or rule |
|:---------------|:-----------|:------------------|
| `inventory_target_path` | PINNED | (same) |
| `target_row_id` | PINNED | Row #3 (α_s §VII.Ω) |
| `expected_sha_prefix` | PINNED | `f514d642fe2a80ac` (full 64-hex computed at runtime) |
| `value_mutation_check` | PINNED | α_s value cell byte-identical pre/post |
| `s85_verdicts_input_sha` | computed-at-runtime | as above |
| `audit_sha256` | computed-at-runtime | as above |

### W14-3 (Row #7 CGWB ρ_AC)
| Free parameter | Pin status | Pin value or rule |
|:---------------|:-----------|:------------------|
| `inventory_target_path` | PINNED | (same) |
| `target_row_id` | PINNED | Row #7 (CGWB ρ_AC) |
| `column_value_pinned` | PINNED | 8.299e-58 |
| `regulator_class_partition` | PINNED | F_4 = {ζ, Zubarev, SDW} (A); M = {cutoff_sqrt, anomaly} (C) |
| `falsification_threshold_cite` | PINNED | LISA Ω_GW > 10^-12 falsifies (C) |
| `value_mutation_check` | PINNED | byte-equal pre/post on Row #7 primary cell |
| `s85_verdicts_input_sha` | computed-at-runtime | as above |
| `audit_sha256` | computed-at-runtime | as above |

### W14-4 (Row #9 f_NL_folded 3-pathway)
| Free parameter | Pin status | Pin value or rule |
|:---------------|:-----------|:------------------|
| `inventory_target_path` | PINNED | (same) |
| `target_row_id` | PINNED | Row #9 (f_NL_folded) |
| `pathway_count` | PINNED | 3 (S82 W3-4, S67, S85 W9-3) |
| `pathway_values` | PINNED | (0.0547, 0.129, 0.7685) |
| `s67_provenance_rule` | PINNED | locate in `computations/`; if pre-canonical, cite `summary/session-67-final.md` and flag INFO if ambiguous |
| `cross_reference_target` | PINNED | P10 (W13) `S86-FNL-FOLDED-PATHWAY-REGISTRY` |
| `s82_verdicts_input_sha` | computed-at-runtime | SHA256 of `computations/s82_gate_verdicts.txt` |
| `s85_verdicts_input_sha` | computed-at-runtime | as above |
| `audit_sha256` | computed-at-runtime | as above |

### W14-5 (Row #12 A_s ε-sensitivity)
| Free parameter | Pin status | Pin value or rule |
|:---------------|:-----------|:------------------|
| `inventory_target_path` | PINNED | (same) |
| `target_row_id` | PINNED | Row #12 (A_s) |
| `epsilon_range_pinned` | PINNED | ε_H ∈ {0.02163, 0.020}; A_s ∈ [3.11e-9, 4.27e-9] |
| `forward_reference` | PINNED | W5a P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` |
| `cross_references` | PINNED | S85 W3-7 4-level taxonomy; S86 W13 P1 FROZEN-COMMIT-LANDING |
| `value_mutation_check` | PINNED | byte-equal pre/post on Row #12 primary cell |
| `s85_verdicts_input_sha` | computed-at-runtime | as above |
| `audit_sha256` | computed-at-runtime | as above |

### W14-6 (NEW Rows #13-#21 lab-falsifier suite)
| Free parameter | Pin status | Pin value or rule |
|:---------------|:-----------|:------------------|
| `inventory_target_path` | PINNED | (same) |
| `target_row_range` | PINNED | NEW Rows #13-#21 (9 atomic rows) |
| `evoi_tag` | PINNED | `LAB-FALSIFIER` |
| `p_decisive_band` | PINNED | [0.30, 0.50] over 5-yr horizon |
| `sweet_spot_magnitudes` | PINNED | (1.7267 ³He-A, 1.8226 FeSe, 2.8500 ¹⁷³Yb) per W8-4 |
| `cross_platform_count` | PINNED | 6 (rows #16-#21, populated from W11 C5/C6 outputs) |
| `hard_dependency` | PINNED | W11 C5 + W11 C6 verdict lines present before dispatch |
| `info_clause` | PINNED | if W11 not closed: sweet-spot + banner committed, cross-platform marked pending, gate INFO; auto-promote to PASS post-W11 |
| `s85_verdicts_input_sha` | computed-at-runtime | SHA256 of `computations/s85_gate_verdicts.txt` |
| `s86_verdicts_input_sha` | computed-at-runtime | SHA256 of `computations/s86_gate_verdicts.txt` (must include W11 C5/C6 lines) |
| `audit_sha256` | computed-at-runtime | `closure_hash(input_pin_map ∪ machinery_pin_map)` |
| `validator` | PINNED | `_plan_upstream_pin_validator.py --json` exit 0 |

**PRU Class 8 audit**: All 6 sub-gates have every gate-relevant machinery parameter either PINNED or marked `computed-at-runtime` with explicit derivation rule. No free parameters left unpinned. PRDR closure complete.

---

## §0.11. Wave W14 Input-SHA Ledger

Per `.claude/rules/gate-verdicts.md` Pre-Registration Protocol §1: every input file the dispatch scripts read is enumerated below with its SHA-256 pin status.

| Input file | SHA pin status | Used by |
|:-----------|:---------------|:--------|
| `computations/s85_gate_verdicts.txt` | `<computed-at-runtime>` (dynamic; must equal value at S86 plan-freeze) | W14-1 (W7-7, W1a-5, W10-2, W12-4 lines), W14-2 (W13-2 line), W14-3 (W13-2 line for Ω_GW=8.299e-58), W14-5 (W3-7 line), W14-6 (W8-4 line for sweet-spot magnitudes) |
| `computations/s82_gate_verdicts.txt` | `<computed-at-runtime>` | W14-4 (S82 W3-4 line for f_NL = 0.0547) |
| `computations/s86_gate_verdicts.txt` | `<computed-at-runtime>` (dynamic; must include W11 C5 + W11 C6 verdict lines before W14-6 dispatch) | W14-6 (W11 C5 + W11 C6 lines) |
| `computations/` (S67 GGE-folded verdict) | `<computed-at-runtime>` if file present; else cite `summary/session-67-final.md` | W14-4 Row B (S67 f_NL = 0.129) |
| `summary/session-67-final.md` | `<computed-at-runtime>` (fallback for S67 provenance) | W14-4 Row B if S67 verdict file absent |
| `sessions/framework/registry/falsifier-master-inventory.md` | `<computed-at-runtime>` (pre-edit SHA captured for value-mutation check on W14-1, W14-2, W14-3, W14-5; post-edit SHA used as content_sha256 in all 6 verdict lines) | all 6 sub-gates (target file) |
| `sessions/session-plan/session-86-plan-w5a.md` | forward reference (accepted as `<plan-file-pending>` until S86 plan-freeze) | W14-5 (cross-reference to W5a P3) |
| `sessions/session-plan/session-86-plan-w11.md` | forward reference | W14-6 (cross-reference to W11 C5/C6) |
| `sessions/session-plan/session-86-plan-w13.md` | forward reference | W14-1 (cross-reference to P9), W14-4 (cross-reference to P10), W14-5 (cross-reference to P1) |

**Closure**: All 6 sub-gates' `audit_sha256` is computed at runtime from the input-pin map ∪ machinery-pin map via `_dual_sha_uniqueness_audit.py`. Per `.claude/rules/v3-closure-recovery.md` sig_5: never hardcode `audit_sha256` literal — compute from `closure_hash(pins)`. Cross-session uniqueness check post-S86 close: every W14 audit_sha256 must be unique across the S86 verdict file.

---

## §0.12. Validator + Recovery Protocol

Per `.claude/rules/v3-closure-recovery.md` Stage 1-3 procedure:

- **Stage 1 (per-signal automatic re-dispatch, max 2 iterations)**: if `_plan_upstream_pin_validator.py --json` returns non-zero on any of the 6 sub-gates' resulting inventory diff, re-dispatch the offending sub-gate with the validator-flagged pin updated. PROHIBITED: convention-shopping, iterate-until-PASS, post-hoc pre-registration editing, ansatz-forced PASS.
- **Stage 2 (V3-NON-COMPLIANT fallback)**: if any sub-gate exhausts 2 Stage-1 iterations without converging, the wave closes with V3-NON-COMPLIANT status; verdicts remain valid but next-session recommendations lead with the unresolved sub-gate(s).
- **Stage 3 (user trigger)**: fires per `.claude/rules/v3-closure-recovery.md` enumerated triggers; orchestrator halts and emits user-ping event.

**Bounded iteration proof**: Each W14 sub-gate has a single failure mode (validator non-zero on inventory diff). Stage-1 cap of 2 iterations × 6 sub-gates = max 12 automatic re-dispatches. Bounded; iterate-until-PASS structurally excluded.

---

## §0.13. Substrate-Framing Reminder (Wave-Level)

Per `.claude/rules/phononic-framing.md`: every observation lands FROM the substrate TOWARD emergent physics. The 5 inventory edits (W14-1 through W14-5) anchor existing substrate observables (w_0 from compaction-vs-Volovik, α_s from spectral curvature, CGWB from phonon-relay GGE, f_NL_folded from substrate fold acoustic non-Gaussianity, A_s from substrate z-factor SR flow). The NEW lab-falsifier row class (W14-6) is the framework's most substrate-direct observational portfolio — terrestrial labs probe the SUBSTRATE INTERNAL spectral content at accessible energies, with ³He-A serving as the canonical parent correspondence (per S85 1B 3-solo) rather than analogy.

NEVER frame W14 outputs as "predictions for spacetime observables" — they are predictions for substrate observables that are MEASURED via emergent-spacetime detectors. The cosmological detectors (LISA, BK-Array, DESI DR3, LiteBIRD, CMB-S4) probe substrate properties at very-low-energy emergent-spacetime conditions; the lab detectors (³He-A, FeSe, ¹⁷³Yb, plus 6 cross-platform) probe substrate properties at higher-energy / lab-accessible conditions. Both classes test the same substrate.

W14-3 (CGWB) and W14-6 (lab) are particularly substrate-direct: CGWB Ω_GW measures gravity-channel a_4 spectral content; lab observables measure direct fiber-spectrum properties without the substrate-to-emergent-spacetime translation that cosmological observables require.

---

**End of Wave W14 plan.** Output target: 6 W14 sub-gate verdict lines committed to `computations/s86_gate_verdicts.txt` at wave close, plus the modified `sessions/framework/registry/falsifier-master-inventory.md` reflecting all 6 atomic edits. Validator must exit 0 against the post-W14 inventory diff.
