# Session 86 Plan — Wave W0b: Permanent-results-registry methodology entries + dual-SHA infra

**Wave owner (planner)**: gen-physicist (this document)
**Wave executor**: SPECIALIST per-gate (see §4 of each block; NOT gen-physicist)
**Output file (verdicts)**: `computations/s86_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)
**Working paper section**: `sessions/archive/session-86/session-86-working-paper.md` §W0b (one sub-section per gate)
**Date generated**: 2026-04-25
**Source manifest**: `sessions/session-plan/session-86-partition.md` §1 Wave W0b

---

## §0. Wave W0b Summary

Wave W0b lands FIVE methodology / infrastructure gates that together close the
remaining audit-and-registry gaps surfaced by the S85 closeout's reviewer
syntheses (R-class items R4, R7, R8, R9, R10). These are META-classification
gates: each one writes to a permanent registry (`canonical_constants.py`,
`sessions/permanent-results-registry.md`, `computations/s86_gate_verdicts.txt`)
or installs an audit script invoked from `.claude/hooks/post-session/v3-closure-audit.sh`.

**No physics computation occurs in W0b.** Each gate writes documentation,
methodology entries, audit infrastructure, or regenerates already-pinned
verdict lines under the W9a-99 dual-SHA template. The wave's role is to
foundationally clear the methodology shelf so the W8 three-layer CGWB ρ
adjudication (P6 + P7) and the v3-closure-audit Stage-1 sig_2/sig_5 channels
operate cleanly during S86 execution.

**Item count**: 5 (= 1 phrasing audit + 2 PRR methodology entries + 1 verdict
regen / companion-row canonicalization + 1 audit-script install).

**Aggregate effort**: 30 min + 0.2 wave + 0.1 wave + 0.3-0.5 wave + 2-3h
≈ 0.7-0.9 wave (single-agent equivalent if executed sequentially).

**Sequencing into S86**:
- W0b R8 three-layer-adjudication methodology entry MUST PRECEDE W8 (P6 + P7
  CGWB three-layer ρ gates cite this entry by keyword).
- W0b R7 single-name-conflation methodology entry routes the §VII.R / §VII.S
  registry slot W1a will populate (T2/T3 NCG-meta + perturbative ledger).
- W0b R4 c_fabric phrasing audit MUST PRECEDE any S86 gate that writes
  `c_fabric · M_KK` into a methods section without the Layer-B qualification.
- W0b R9 + R10 dual-SHA work is independent of physics-sequencing; lands as
  soon as the audit infrastructure exists.

---

## §0.5. Wave W0b Decision-Point Prerequisites

Each gate has a SINGLE decision: PASS (write succeeds, audit succeeds), FAIL
(write incomplete or audit false-positive on a by-design pattern), or INFO
(executable but flagged for downstream re-pin in S87).

**Pre-Wave checks** (orchestrator runs these BEFORE dispatching W0b):

1. `sessions/permanent-results-registry.md` exists and contains a §VII top
   matter with R / S / Q / M / B sub-section anchors (else R7 + R8 cannot
   land — bail to a registry-scaffold sub-wave).
2. `computations/canonical_constants.py` exists and contains the
   `c_fabric` symbol (else R4 cannot edit the docstring — bail).
3. `computations/s85_gate_verdicts.txt` exists with the 7 W7 single-SHA
   lines and 17 W6-W13 schema-1.5 entries enumerated by Lizzi 9A §C-1 (else
   R9 has no targets — bail).
4. `.claude/hooks/post-session/v3-closure-audit.sh` is writable (else R10
   cannot wire its invocation — bail).

If any prerequisite is missing, the orchestrator escalates to the user
BEFORE dispatching the wave.

**Per-gate decision rule**: each block's §9 (PASS/FAIL/INFO threshold) is
the only authority. No mid-execution renegotiation.

---

## §I. Carry-Forward Items Mapping

| Manifest ID | This-wave Gate ID | Source closeout / synthesis |
|:------------|:------------------|:----------------------------|
| R4 | `S86-CANONICAL-PHRASING-AUDIT` (c_fabric) | closeout §5.6; lizzi 9A; transit-dynamics 7B |
| R7 | `S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY` | closeout §5.7; 4 witnesses (2A SECTOR-split, 2B R_JK vs R_JE, 6A ρ three-layer, W12-2 bare K) |
| R8 | `S86-PRR-THREE-LAYER-ADJUDICATION` | closeout §5.7-2; mack 6A three-layer ρ commit |
| R9 | `S86-W7-SIG2-DUAL-SHA-REGEN` + `S86-S85-VERDICT-FILE-COMPANION-ROW-CANONICALIZATION` | W9a-99 dual-SHA template; lizzi 9A §C-1 (17 schema-1.5 entries) |
| R10 | `S86-DUAL-SHA-INFRASTRUCTURE` | closeout §5.10; v3-ladder sig_5 audit gap |

All five items are R-class (rule diff). They are META-classification (per
`.claude/rules/phononic-framing.md`): they govern how PHONONIC / GEOMETRIC
gates are written and audited, not the physics itself.

---

## §W0b-1. S86-CANONICAL-PHRASING-AUDIT (c_fabric)

### 1. Gate ID
`S86-CANONICAL-PHRASING-AUDIT`

### 2. Trigger
`[AUDIT]` — phrasing-audit gate; no sign/direction claim, but a ban on a
specific phrasing pattern.

### 3. Classification
**META** — methodology / canonical-constants documentation. Indirectly
PHONONIC: c_fabric is the substrate sound speed and its conflation with a
momentum cutoff `Λ` is a substrate-vs-emergent framing error.

### 4. Agent type — SPECIALIST (NOT gen-physicist)
**Assignment**: `connes-ncg-theorist`
**Rationale**: connes-ncg-theorist owns the spectral-action-side definitions
and the `M_KK` / cutoff hierarchy; the c_fabric-vs-Λ phrasing question is a
spectral-action convention question (Layer-A: substrate sound speed; Layer-B:
emergent momentum cutoff that happens to share the dimensionful product
`c_fabric · M_KK`). connes-ncg has the framework-internal authority to author
the corrected docstring without further appeal.

### 5. Hypothesis
A single substring search across `computations/` + `sessions/archive/session-86-plan-w3.md`
sections §401 and §543 will return **zero** occurrences of `Λ_eff = c_fabric · M_KK`
(or any case-insensitive / whitespace-permissive variant) AFTER the audit edit
is applied; AND `canonical_constants.py`'s `c_fabric` docstring will contain
the exact corrected wording.

### 6. Method (full dispatch prompt)

```
You are connes-ncg-theorist. Execute S86-CANONICAL-PHRASING-AUDIT.

Working directory: C:\sandbox\Ainulindale Exflation\

PRE-WORK (knowledge MCP):
  search_knowledge("c_fabric M_KK Lambda cutoff")
  get_constant("c_fabric")
  get_constant("M_KK")
  trace_entity("c_fabric")
  Confirm c_fabric's value + provenance + that it is the SUBSTRATE SOUND SPEED
  (a velocity, not a momentum cutoff).

EDIT 1 — canonical_constants.py docstring:
  Open computations/canonical_constants.py
  Locate the c_fabric definition block.
  Replace the existing docstring/comment with:
    "substrate sound speed (velocity scale, NOT a momentum cutoff)"
  The replacement must appear within 3 lines of the c_fabric assignment so
  any reader scanning the constant sees the qualification immediately.

EDIT 2 — drop forbidden phrasing from S86-W3 plan:
  IF sessions/session-plan/session-86-plan-w3.md exists, search §401 and §543
  for the literal substring "Λ_eff = c_fabric · M_KK" (also check ASCII variant
  "Lambda_eff = c_fabric * M_KK"). For every occurrence, drop the equation OR
  rewrite as "the dimensionful product c_fabric · M_KK (substrate sound speed
  times KK scale; NOT a momentum cutoff Λ unless explicitly Layer-B-qualified)".

EDIT 3 — S86 plan-level phrasing constraint:
  Add a one-paragraph note to sessions/session-plan/session-86-context.md (if
  it has a "phrasing rules" section; otherwise to the W0b deliverable doc):
    "S86 plan-level constraint: c_fabric · M_KK is NEVER labeled 'Λ' without
    explicit Layer-B (emergent momentum cutoff) qualification. Layer-A use
    (substrate sound speed × KK scale) requires the dimensional reading; Layer-B
    use (emergent momentum cutoff in spectral-action language) requires explicit
    "Λ_emergent" notation and a one-line provenance citing AC-2010 §V or
    equivalent."

POST-WORK AUDIT:
  Use Grep to scan computations/ (recursive) AND
  sessions/session-plan/session-86-plan-w3.md for case-insensitive variants of
  "Lambda_eff.*c_fabric.*M_KK" and "Λ_eff.*c_fabric.*M_KK". Expected count: 0.

VERDICT EMISSION:
  Append ONE canonical line to computations/s86_gate_verdicts.txt using
  the dual-SHA template (W9a-99). Verdict 4-tuple:
    value=<count_of_remaining_forbidden_strings>
    scheme=<canonical_constants_py>
    convention=<phrasing_audit>
    L_max=N/A
  PASS iff value == 0; FAIL iff value > 0.
  Include companion comment row with content_sha256 (hash of edited
  canonical_constants.py docstring block) AND audit_sha256 (hash of grep
  result transcript).

WORKING-PAPER SECTION (≥15 lines):
  sessions/archive/session-86/session-86-working-paper.md §W0b-1
  Include: verdict line at top, before/after docstring diff, before/after grep
  count, the one-paragraph S86 plan-level constraint verbatim, and a
  ≥3-line Layer-A/Layer-B explanation of why c_fabric · M_KK is dimensionally
  a momentum but framework-internally a substrate-sound-speed × KK-scale
  product (not a true cutoff in the AC-2010 §V sense).

PROHIBITED:
  - Renaming c_fabric (it stays c_fabric).
  - Removing the c_fabric · M_KK product wherever it correctly appears as a
    dimensional check.
  - Editing canonical_constants.py to add a NEW constant (only the docstring
    is edited).
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin | Source |
|:---------------|:----|:-------|
| target_file_canonical | `computations/canonical_constants.py` | path-pinned |
| target_file_w3_plan | `sessions/session-plan/session-86-plan-w3.md` | path-pinned (if exists) |
| forbidden_pattern_set | {`Λ_eff = c_fabric · M_KK`, `Λ_eff=c_fabric·M_KK`, `Lambda_eff = c_fabric * M_KK`, `Lambda_eff=c_fabric*M_KK`} | enumerated (case-insensitive) |
| corrected_docstring_text | `"substrate sound speed (velocity scale, NOT a momentum cutoff)"` | verbatim |
| schema_version | `R3` | rule-file-v3 (W0a R1 will land first) |
| audit_tool | Grep with `-i` flag, recursive | tool-pinned |
| input_sha_canonical_constants_pre | `<computed-at-runtime>` | dynamic |
| input_sha_w3_plan_pre | `<computed-at-runtime>` (or `N/A` if file does not yet exist) | dynamic |

### 8. Expected output 4-tuple
`(value=<count_of_remaining_forbidden_strings>, scheme=canonical_constants_py, convention=phrasing_audit, L_max=N/A)`

### 9. PASS/FAIL/INFO threshold
- **PASS**: post-edit grep returns 0 occurrences of any forbidden_pattern_set
  member across `computations/` AND `sessions/session-plan/session-86-plan-w3.md`;
  AND `canonical_constants.py` contains the corrected docstring verbatim within
  3 lines of the c_fabric assignment.
- **FAIL**: post-edit grep returns ≥1 occurrence; OR docstring not updated.
- **INFO**: not applicable for this gate (binary PASS/FAIL).

Tolerance rule: ABSOLUTE (count of forbidden strings, integer).

### 10. Substitution chain (threshold)
```
Step 1 (definition):
  N_forbidden = | { (file, line) : line matches any pattern in forbidden_pattern_set
                      AND file ∈ computations/ ∪ {session-86-plan-w3.md} } |
  threshold = 0
Step 2 (substitute, post-edit):
  N_forbidden = grep_count(forbidden_pattern_set, target_files)
Step 3 (simplify):
  N_forbidden ≥ 0 (count is non-negative integer)
Step 4 (direction):
  N_forbidden == 0  ⇒  PASS
  N_forbidden  > 0  ⇒  FAIL
Conclusion: gate is binary on the post-edit grep count.
```

### 11. Solution-space meaning
- **PASS**: closes the c_fabric-as-Λ container-thinking corridor — agents
  reading `canonical_constants.py` get the substrate-sound-speed framing
  immediately; W3 plan no longer normalizes the misleading equation.
- **FAIL**: indicates the substitution missed at least one site; downstream
  W3 + W7 + W8 gates remain at risk of re-emitting the conflation. The fix
  is a re-dispatch, not a deferral.

### 12. Effort estimate
30 min (parallel to R3 cutoff_axis YAML work in W0a; no GPU; no compute).

### 13. Substrate-framing reminder
META-class. The rule itself enforces the substrate framing: c_fabric is a
substrate property (sound speed of the fabric), NOT a momentum cutoff in the
emergent QFT sense. The audit prevents W3 sections from sliding back into
container-thinking ("Λ is the cutoff that bounds the emergent QFT"). The
correct reading is: c_fabric · M_KK is a dimensional product that PROBES the
substrate's intrinsic scale — emergent observables that depend on it inherit
a substrate origin, they are not bounded by an external cutoff.

---

## §W0b-2. S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY

### 1. Gate ID
`S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY`

### 2. Trigger
`[VERIFY]` — registry-write gate; verifies that a methodology entry with the
named keyword and 4 witness citations is present in the permanent registry.

### 3. Classification
**META** — methodology entry to `sessions/permanent-results-registry.md` §VII.

### 4. Agent type — SPECIALIST (NOT gen-physicist)
**Assignment**: `lizzi-spectral-functional-theorist`
**Rationale**: lizzi cited the single-name-conflation pattern in his
synthesis (closeout §5.7); he is the originating reviewer and has the most
detailed inventory of the 4 witnesses (2A SECTOR-split, 2B R_JK vs R_JE,
6A ρ three-layer, W12-2 bare K). Lizzi-track ownership of the methodology
entry preserves citation provenance; gen-physicist as orchestrator could
draft the boilerplate but would lose the synthesis-author voice that the
permanent registry's §VII witness-citation entries preserve.

### 5. Hypothesis
After the gate runs, `sessions/permanent-results-registry.md` will contain a
new §VII.M (or successor) sub-section titled "Single-Name Conflation —
Methodology Entry" that names the four witnesses verbatim and is locatable
by the keyword string `single-name conflation`.

### 6. Method (full dispatch prompt)

```
You are lizzi-spectral-functional-theorist. Execute S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY.

Working directory: C:\sandbox\Ainulindale Exflation\

PRE-WORK:
  Read sessions/permanent-results-registry.md and locate the §VII top matter.
  Identify the next available sub-section letter (likely §VII.M; verify by
  reading existing §VII.A through §VII.L).
  search_knowledge("single name conflation methodology")
  search_knowledge("R_JK R_JE substrate distance")
  search_knowledge("SECTOR-1 SECTOR-2 split")
  search_knowledge("rho three layer")
  search_knowledge("W12-2 bare K")
  Confirm the four witnesses are session-real (not hallucinated).

REGISTRY EDIT — append to sessions/permanent-results-registry.md:

  ## §VII.{LETTER}. Single-Name Conflation — Methodology Entry

  **Status**: METHODOLOGY (registry-level rule for S86+)
  **Source**: closeout §5.7 single-name-conflation pattern; 4 cited witnesses
  **Keyword**: "single-name conflation" (use this string in any cross-reference)

  **Pattern**: A single symbol (e.g. `R`, `K`, `ρ`, `SECTOR`) is used in two or
  more contexts that turn out to refer to distinct quantities once the underlying
  substrate-vs-emergent layering is resolved. The conflation appears benign at
  the gate-block level but produces verdict-line drift when downstream gates
  inherit the symbol without inheriting the layer.

  **Adjudication rule**: When two gates cite the same symbol but produce
  inconsistent values, the registry recommends a three-step disambiguation:
    (1) layer-tag each use as Layer-A (substrate, distance-2 from observable)
        or Layer-B (emergent, distance-1 from observable);
    (2) sub-script the symbol with the layer tag in canonical_constants.py
        AND in the gate block (e.g. K_substrate vs K_emergent);
    (3) re-emit the verdict line under the disambiguated symbol; the original
        verdict is not retracted but is annotated as "pre-disambiguation
        single-name conflation; see §VII.{LETTER}".

  **Cited witnesses** (4 sessions; do not edit without an additional witness):
    1. **2A SECTOR-1 vs SECTOR-2 split** (S85 transit-dynamics-theorist 2A
       synthesis): "SECTOR" used for both the SR-flow integration sector
       (SECTOR-1, distance-1 emergent inflationary observable) and the
       Mellin-kernel substrate sector (SECTOR-2, distance-2 substrate
       Mellin-pole at pivot). Disambiguation: pin SECTOR-1-EMERGENT vs
       SECTOR-2-SUBSTRATE in S86 plan blocks.
    2. **2B R_JK vs R_JE branch-(iv) formulation commit** (S85
       transit-dynamics-theorist 2B path-(c)): R_JK = K-functional at
       distance-2; R_JE = ξ_E_GGE^{−1} s=−1 spectral diagnostic at
       distance-1. Single-letter R hid the layer split until Path-(c)
       commit; resolved in S86 W4 P4.
    3. **6A ρ three-layer adjudication** (S85 mack-cosmic-bridge 6A): ρ
       quoted across three layers (LAYER-1 diagrammatic null, LAYER-2 atlas
       Monte Carlo, LAYER-3 substrate-prediction MC) without per-layer
       sub-scripting; resolved in S86 W8 P6 + P7 + W0b R8 methodology entry.
    4. **W12-2 bare K** (S85 §W12 bare-K verdict): K used unqualified for
       both K_crit (compactification scale, M_KK units) and K_crit_BdG
       (BCS condensate scale, energy units in BdG framework); resolved in
       S86 W0c C17 (K_crit_BdG canonical-constants registration).

  **Application**: Any S86+ gate that introduces a NEW single-letter symbol
  shared across two or more layers MUST cite this methodology entry in its
  gate block §3 (Classification) or §11 (Solution-space meaning) section and
  pre-register the layer subscript scheme.

  **Cross-reference**: §VII.{R8-LETTER} S86-PRR-THREE-LAYER-ADJUDICATION
  (six-A ρ as canonical instance).

(End of §VII.{LETTER} block.)

VERDICT EMISSION:
  Append ONE canonical line to computations/s86_gate_verdicts.txt:
    value=<lines_added_to_registry>
    scheme=<permanent_results_registry>
    convention=<methodology_entry>
    L_max=N/A
  PASS iff the new §VII.{LETTER} sub-section exists AND contains all 4 witness
  citations (2A SECTOR-split, 2B R_JK vs R_JE, 6A ρ three-layer, W12-2 bare K)
  AND contains the literal string "single-name conflation".
  FAIL iff any witness missing OR keyword absent.
  Companion row: content_sha256 (hash of new §VII.{LETTER} block) AND
  audit_sha256 (hash of grep transcript confirming all 4 witnesses + keyword).

WORKING-PAPER SECTION (≥15 lines):
  sessions/archive/session-86/session-86-working-paper.md §W0b-2
  Include verdict, the §VII letter chosen, the 4 witness one-line summaries,
  the cross-reference to R8 (§W0b-3 in this plan), and a 3-line note on why
  the methodology entry is registry-level (not agent-memory-level): per
  .claude/rules/agent-standards.md AMRI rule, methodology entries cited by
  multiple specialist agents' future plans must live in the permanent
  registry, not in agent memory.

PROHIBITED:
  - Renaming any of the 4 witnesses.
  - Adding a 5th witness (the gate is FAIL if witness count != 4 in this
    initial landing; future witnesses extend the entry via amendment, not
    insertion).
  - Editing §VII anchors that already exist (§VII.A-L).
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin | Source |
|:---------------|:----|:-------|
| target_registry | `sessions/permanent-results-registry.md` | path-pinned |
| target_subsection_letter | next-available `§VII.{LETTER}` (most likely `§VII.M`); pinned at runtime by reading existing §VII anchors | dynamic |
| witness_count | 4 (exactly) | enumerated; closeout §5.7 |
| witness_set | {2A-SECTOR-split, 2B-R_JK-vs-R_JE, 6A-ρ-three-layer, W12-2-bare-K} | enumerated verbatim |
| keyword_string | `single-name conflation` (verbatim, lowercase) | pinned |
| schema_version | R3 | rule-file-v3 |
| input_sha_registry_pre | `<computed-at-runtime>` | dynamic |

### 8. Expected output 4-tuple
`(value=<lines_added>, scheme=permanent_results_registry, convention=methodology_entry, L_max=N/A)`

### 9. PASS/FAIL/INFO threshold
- **PASS**: new §VII.{LETTER} block exists; contains all 4 witness citations
  verbatim by witness ID (2A, 2B, 6A, W12-2); contains literal string
  "single-name conflation"; cross-references R8 (S86-PRR-THREE-LAYER-ADJUDICATION).
- **FAIL**: any witness missing, keyword absent, or cross-reference missing.
- **INFO**: not applicable.

Tolerance rule: ABSOLUTE (boolean per witness; all four required).

### 10. Substitution chain (threshold)
```
Step 1 (definition):
  W = set of witness IDs present in new §VII.{LETTER} block, by literal grep
  W_required = {"2A", "2B", "6A", "W12-2"}
  K = boolean: literal string "single-name conflation" present in block
  X = boolean: cross-reference to S86-PRR-THREE-LAYER-ADJUDICATION present
Step 2 (substitute):
  PASS_predicate = (W == W_required) AND K AND X
Step 3 (simplify):
  Each conjunct evaluates to true/false from grep output; conjunction is
  monotone in each conjunct.
Step 4 (direction):
  If any conjunct is false → FAIL; else PASS.
Conclusion: gate is conjunctive on four enumerated grep checks.
```

### 11. Solution-space meaning
- **PASS**: closes the "single-name conflation appears innocuous at gate-block
  level but drifts at verdict level" corridor — every S86+ gate writing a
  shared single-letter symbol now has registry authority to layer-tag at
  pre-registration time.
- **FAIL**: indicates either witness drift (a synthesis mis-cite) or
  registry-format drift; re-dispatch with witness verification step.

### 12. Effort estimate
0.2 wave (≈ 1-2 h: text drafting + grep verification + companion-row hashing).

### 13. Substrate-framing reminder
META-class. The methodology entry itself enforces substrate-vs-emergent
layering: every witness pair (SECTOR, R, ρ, K) was a case where a single
symbol elided the substrate-emergent split. Future gates citing this entry
inherit the layering discipline by construction.

---

## §W0b-3. S86-PRR-THREE-LAYER-ADJUDICATION

### 1. Gate ID
`S86-PRR-THREE-LAYER-ADJUDICATION`

### 2. Trigger
`[VERIFY]` — registry-write gate; verifies methodology entry with the named
keyword and the generalization clause is present.

### 3. Classification
**META** — methodology entry to `sessions/permanent-results-registry.md` §VII.

### 4. Agent type — SPECIALIST (NOT gen-physicist)
**Assignment**: `mack-cosmic-bridge`
**Rationale**: mack authored the 6A three-layer ρ adjudication in his S85
synthesis; the methodology entry generalizes his sub-tree to "any future
joint-channel gate quoting ρ between two observables sharing a substrate
parameter". mack owns the joint-channel language and the LAYER-1 / LAYER-2 /
LAYER-3 vocabulary; his authorship preserves the diagrammatic / atlas-MC /
substrate-prediction-MC trichotomy in the registry voice.

### 5. Hypothesis
After the gate runs, `sessions/permanent-results-registry.md` will contain a
new §VII.{LETTER} sub-section titled "Three-Layer Adjudication for
Joint-Channel ρ Verdicts — Methodology Entry" containing the keyword string
"three-layer adjudication for joint-channel ρ verdicts" and a
generalization-clause that extends the 6A pattern to any joint-channel ρ
between two observables sharing a substrate parameter.

### 6. Method (full dispatch prompt)

```
You are mack-cosmic-bridge. Execute S86-PRR-THREE-LAYER-ADJUDICATION.

Working directory: C:\sandbox\Ainulindale Exflation\

PRE-WORK:
  Read sessions/permanent-results-registry.md §VII top matter; identify the
  next available sub-section letter AFTER R7's landing (run R7 first or
  coordinate sequencing with W0b-2).
  search_knowledge("three layer adjudication rho")
  search_knowledge("CGWB rho LAYER-1 LAYER-2 LAYER-3")
  search_knowledge("joint channel rho substrate parameter")
  Confirm the 6A three-layer commit is session-real (S85 mack-cosmic-bridge
  synthesis).

REGISTRY EDIT — append to sessions/permanent-results-registry.md AFTER §W0b-2 entry:

  ## §VII.{LETTER}. Three-Layer Adjudication for Joint-Channel ρ Verdicts — Methodology Entry

  **Status**: METHODOLOGY (registry-level rule for S86+ joint-channel gates)
  **Source**: S85 mack-cosmic-bridge 6A synthesis; W8 P6 + P7 instantiation
  **Keyword**: "three-layer adjudication for joint-channel ρ verdicts"

  **Pattern**: A joint-channel correlation coefficient ρ between two
  observables O_1 and O_2 that share a substrate parameter (e.g. c_sub,
  τ_fold, α_s, or any spectral-action moment) admits THREE methodologically
  independent verdict layers. Quoting ρ at any single layer without
  pre-registering the layer assignment elides the methodological independence
  the framework relies on for falsifier discrimination.

  **Three layers** (in order of substrate-distance):
    - **LAYER-1 (diagrammatic null)**: ρ_diagrammatic computed from the
      Wick-contraction structure with all substrate parameters held fixed at
      canonical pin values; expected ρ = 0 for uncorrelated observables;
      detects shared-parameter inheritance through diagram topology only.
    - **LAYER-2 (atlas Monte Carlo)**: ρ_atlas-MC computed by sampling the
      regulator atlas (e.g. 5-regulator atlas at L_max=10) and reading off
      the per-regulator (O_1, O_2) joint distribution; sign-convention and
      atlas-weighting pre-pinned (uniform / down-weighted / excluded subsets);
      detects regulator-induced inheritance.
    - **LAYER-3 (substrate-prediction MC)**: ρ_substrate-prediction-MC
      computed by Monte-Carloing the substrate parameters themselves over
      their substrate-prior distributions; reference Pearson |ρ| spot-check
      (e.g. 0.91 R3 spot-check from W13-2); detects substrate-origin
      inheritance.

  **Adjudication rule**: A joint-channel ρ verdict is well-formed iff its
  pre-registration block names the layer (LAYER-1 / LAYER-2 / LAYER-3) AND
  pre-pins the layer-specific machinery: for LAYER-2, atlas membership +
  weighting + sign convention; for LAYER-3, substrate-prior distributions +
  MC sample size + convergence criterion.

  **Generalization clause**: The three-layer scheme generalizes to ANY future
  joint-channel gate quoting ρ between two observables that share a substrate
  parameter, NOT just CGWB. Specifically, any gate of the form
    ρ(O_1, O_2 | shared substrate parameter p)
  where p is a registered canonical_constants.py value or a spectral moment,
  inherits this methodology entry's three-layer requirement. Pre-S86 ρ
  verdicts that did not name a layer are annotated as "pre-three-layer
  adjudication; see §VII.{LETTER}" but are not retracted.

  **Canonical instance**: W8 P6 (LAYER-1 diagrammatic + LAYER-2 atlas-MC for
  W13-2 ρ=0 commit) + W8 P7 (LAYER-3 substrate-prediction MC).

  **Cross-reference**: §VII.{R7-LETTER} S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY
  (ρ as the four-witness instance for single-name conflation).

(End of §VII.{LETTER} block.)

VERDICT EMISSION:
  Append ONE canonical line to computations/s86_gate_verdicts.txt:
    value=<lines_added_to_registry>
    scheme=<permanent_results_registry>
    convention=<methodology_entry>
    L_max=N/A
  PASS iff the new §VII.{LETTER} block exists AND contains the keyword
  "three-layer adjudication for joint-channel ρ verdicts" AND contains the
  generalization-clause literally referencing "joint-channel gate quoting ρ
  between two observables sharing a substrate parameter".
  FAIL iff keyword absent OR generalization clause absent.
  Companion row: content_sha256 (hash of new §VII.{LETTER} block) AND
  audit_sha256 (hash of grep transcript confirming keyword + clause).

WORKING-PAPER SECTION (≥15 lines):
  sessions/archive/session-86/session-86-working-paper.md §W0b-3
  Include verdict, the §VII letter chosen, the three-layer enumeration
  verbatim, the W8 P6 + P7 forward-pointer (these gates will INSTANTIATE the
  methodology entry, not just cite it), and a 3-line note on why
  joint-channel ρ requires registry authority (it is the falsifier-tree
  discriminator for inflation-vs-substrate routing per closeout §5.10
  EVOI ranking).

PROHIBITED:
  - Quoting numerical ρ values from W8 P6/P7 (those gates have not run yet;
    pre-quoting would be ansatz-forced PASS per S78 Class-2).
  - Editing the W8 plan file or pre-running its gates (W8 is a separate wave;
    R8 only writes the methodology entry that W8 will cite).
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin | Source |
|:---------------|:----|:-------|
| target_registry | `sessions/permanent-results-registry.md` | path-pinned |
| target_subsection_letter | next-available `§VII.{LETTER}` AFTER R7 lands | dynamic |
| keyword_string | `three-layer adjudication for joint-channel ρ verdicts` | verbatim |
| layer_count | 3 (LAYER-1 + LAYER-2 + LAYER-3) | enumerated |
| layer_set | {LAYER-1-diagrammatic, LAYER-2-atlas-MC, LAYER-3-substrate-prediction-MC} | enumerated verbatim |
| generalization_clause_substring | `joint-channel gate quoting ρ between two observables sharing a substrate parameter` | verbatim |
| schema_version | R3 | rule-file-v3 |
| input_sha_registry_pre | `<computed-at-runtime>` | dynamic |

### 8. Expected output 4-tuple
`(value=<lines_added>, scheme=permanent_results_registry, convention=methodology_entry, L_max=N/A)`

### 9. PASS/FAIL/INFO threshold
- **PASS**: new §VII.{LETTER} block exists; contains keyword string verbatim;
  contains generalization-clause substring verbatim; contains the three-layer
  enumeration with all three layer names; cross-references R7.
- **FAIL**: keyword absent, generalization clause absent, or any of the three
  layers missing.
- **INFO**: not applicable.

Tolerance rule: ABSOLUTE (boolean conjunction).

### 10. Substitution chain (threshold)
```
Step 1 (definition):
  K = boolean: keyword string present (verbatim grep)
  G = boolean: generalization clause substring present (verbatim grep)
  L = set of layer names present in block
  L_required = {"LAYER-1", "LAYER-2", "LAYER-3"}
  X = boolean: cross-reference to R7 entry present
Step 2 (substitute):
  PASS_predicate = K AND G AND (L == L_required) AND X
Step 3 (simplify):
  All four conjuncts evaluate via grep; monotone in each.
Step 4 (direction):
  If any conjunct false → FAIL; else PASS.
Conclusion: gate is conjunctive on four grep predicates.
```

### 11. Solution-space meaning
- **PASS**: any S86+ joint-channel ρ gate has registry authority to demand
  layer pre-registration; closes the "ρ quoted at unspecified layer" corridor.
- **FAIL**: registry edit incomplete; W8 P6/P7 cannot cite the methodology
  cleanly. Re-dispatch with the missing element identified.

### 12. Effort estimate
0.1 wave (≈ 30 min: text drafting only; no compute).

### 13. Substrate-framing reminder
META-class. The methodology entry preserves the substrate-as-source framing:
LAYER-3 (substrate-prediction MC) is the deepest layer, sampling substrate
parameters themselves; LAYER-1 (diagrammatic) is the most-emergent layer,
holding substrate parameters fixed and varying only Wick-contraction
structure. The three-layer ordering encodes the substrate-distance hierarchy
explicitly — agents reading the entry inherit the framing without it being
stated as a separate rule.

---

## §W0b-4. S86-W7-SIG2-DUAL-SHA-REGEN + S86-S85-VERDICT-FILE-COMPANION-ROW-CANONICALIZATION

### 1. Gate ID
`S86-W7-SIG2-DUAL-SHA-REGEN` (paired with `S86-S85-VERDICT-FILE-COMPANION-ROW-CANONICALIZATION`)

This is a COMBINED gate: the verdict line addresses both the W7 single-SHA
regen and the schema-1.5 companion-row canonicalization. Both are
methodology-driven verdict-line edits under the W9a-99 dual-SHA template;
neither involves new physics computation.

### 2. Trigger
`[AUDIT]` — verdict-line audit gate; the threshold is "every flagged verdict
line carries a dual-SHA companion row".

### 3. Classification
**META** — verdict-file maintenance / dual-SHA infrastructure (per
`.claude/rules/gate-verdicts.md` S81+ form).

### 4. Agent type — SPECIALIST (NOT gen-physicist)
**Assignment**: `lizzi-spectral-functional-theorist`
**Rationale**: lizzi 9A §C-1 enumerated the 17 W6-W13 schema-1.5 entries
needing canonicalization; he authored the schema-1.5 → dual-SHA migration
spec. The 7 W7 single-SHA verdict lines are sig_2 v3-ladder failures that
correspond to gates lizzi already cited in his synthesis. Lizzi-track
ownership keeps the regen consistent with the schema-1.5 inventory's
authoritative description.

### 5. Hypothesis
After the gate runs, `computations/s85_gate_verdicts.txt` (or the S86
variant if the regen targets S86; specify per gate at execution time) will
contain dual-SHA companion rows for ALL 7 W7 verdict lines AND ALL 17 W6-W13
schema-1.5 entries enumerated by lizzi 9A §C-1.

### 6. Method (full dispatch prompt)

```
You are lizzi-spectral-functional-theorist. Execute the combined regen+canonicalization gate.

Working directory: C:\sandbox\Ainulindale Exflation\

PRE-WORK:
  Read .claude/rules/gate-verdicts.md (S81+ canonical form) and the W9a-99
  dual-SHA template (it is referenced in .claude/rules/v3-closure-recovery.md
  sig_2 remediation).
  Read computations/s85_gate_verdicts.txt and locate:
    (a) the 7 W7 verdict lines that lack a dual-SHA companion row
        (sig_2 = 0 v3-ladder signal); identify them by absence of a
        following comment row containing "content_sha256=" + "audit_sha256=";
    (b) the 17 schema-1.5 entries (W6 through W13) enumerated by lizzi 9A
        §C-1; their canonical line uses an older schema where companion
        rows are formatted differently.
  search_knowledge("W9a-99 dual SHA template")
  search_knowledge("schema 1.5 companion row")
  Build a TARGET_LIST of 24 verdict-line gate IDs (7 W7 + 17 schema-1.5).

PART 1 — W7 single-SHA regen (7 verdict lines):
  For EACH of the 7 W7 verdict lines:
    - Locate the producing script: computations/s85_w7_<gate>.py (or
      similar; identify by the canonical line's GATE_ID field).
    - Re-run the producing script with the W9a-99 dual-SHA template applied
      (the template appends BOTH the canonical 64-char sha256 closure AND
      the comment row with content_sha256 + audit_sha256).
    - Verify the new canonical line's sha256 matches the previous line's
      sha256 (the closure should be deterministic from the input-pin map;
      if it does not match, the script has a non-determinism bug — flag and
      stop, do NOT silently overwrite).
    - Append the new dual-SHA line + companion row to s85_gate_verdicts.txt
      as a NEW append (the verdict file is append-only; the original
      single-SHA line stays in the file as historical record).
  Constraint: USE the append helper from .claude/templates/script-template.py;
    DO NOT write your own truncate-and-rewrite code (S84 W1 race lesson).

PART 2 — schema-1.5 companion-row canonicalization (17 entries):
  For EACH of the 17 schema-1.5 W6-W13 entries:
    - Identify the schema-1.5 companion row (it exists but uses the older
      format).
    - Compute content_sha256 (= sha256 of the gate's primary output artifact,
      typically the .npz / .json file the script produced) and audit_sha256
      (= sha256 of the closure-hash transcript that the script printed in its
      first 20 lines of stdout).
    - Append a NEW canonicalized companion row in the W9a-99 format:
        # GATE_ID: content_sha256=<64-char> audit_sha256=<64-char>
    - Original schema-1.5 row stays as historical record.

PART 3 — verdict line for THIS gate:
  Append ONE canonical line to computations/s86_gate_verdicts.txt:
    value=<count_dual_sha_companions_post_regen>  (target: 7 + 17 = 24)
    scheme=<verdict_file_dual_sha_regen>
    convention=<W9a99>
    L_max=N/A
  PASS iff value == 24 AND every TARGET_LIST entry has exactly one new
  W9a-99 companion row.
  FAIL iff any TARGET_LIST entry lacks a new companion row, OR the closure
  sha256 mismatch from PART 1 fired.
  Companion row for THIS gate: content_sha256 (hash of the regen transcript)
  AND audit_sha256 (hash of the post-regen TARGET_LIST verification grep).

WORKING-PAPER SECTION (≥15 lines):
  sessions/archive/session-86/session-86-working-paper.md §W0b-4
  Include verdict, the 24 TARGET_LIST entries (7 + 17 enumerated with their
  GATE_IDs), the regen procedure summary, the closure sha256 match/mismatch
  status for each PART 1 entry, and a 3-line note on why historical lines
  stay in the verdict file (per .claude/rules/gate-verdicts.md "verdicts are
  permanent — no retroactive changes" — the new dual-SHA lines are NEW
  appends, not retractions of the original lines).

PROHIBITED:
  - Editing or deleting any historical verdict line (the file is append-only).
  - Hardcoding any sha256 (every hash is computed at runtime from the actual
    artifact; per .claude/rules/v3-closure-recovery.md sig_5 prohibition).
  - Using sys.exit(1) on FAIL (per .claude/rules/math-scripts.md exit-code
    discipline; FAIL is a verdict, exit 0 means script succeeded).
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin | Source |
|:---------------|:----|:-------|
| target_verdict_file_s85 | `computations/s85_gate_verdicts.txt` | path-pinned |
| target_verdict_file_s86 | `computations/s86_gate_verdicts.txt` (for THIS gate's verdict line) | path-pinned |
| target_count_W7_single_sha | 7 (lizzi 9A §C-1) | enumerated |
| target_count_schema_1_5 | 17 (lizzi 9A §C-1) | enumerated |
| target_total | 24 | derived |
| dual_sha_template_version | W9a-99 | rule-pinned |
| append_helper | `.claude/templates/script-template.py append_verdict()` | tool-pinned |
| closure_determinism_check | required: new sha256 == old sha256 for PART 1 | rule-pinned |
| schema_version | R3 | rule-file-v3 |
| input_sha_s85_verdict_file_pre | `<computed-at-runtime>` | dynamic |

### 8. Expected output 4-tuple
`(value=<count_dual_sha_companions_post_regen>, scheme=verdict_file_dual_sha_regen, convention=W9a99, L_max=N/A)`

### 9. PASS/FAIL/INFO threshold
- **PASS**: post-regen companion-row count for TARGET_LIST = 24; every
  PART 1 closure sha256 matched its pre-regen value (determinism confirmed);
  no historical verdict line was edited or deleted.
- **FAIL**: count < 24, OR any PART 1 closure sha256 mismatched (script
  non-determinism bug surfaced; flag for separate fix), OR a historical line
  was modified (file-integrity violation; this is a critical FAIL).
- **INFO**: count == 24 but ≥1 PART 2 schema-1.5 entry's content_sha256 could
  not be computed because its primary output artifact is no longer on disk
  (the gate is then PRE-REG-INCOMPLETE for that entry; reach for the script
  re-run path, do not synthesize a hash).

Tolerance rule: ABSOLUTE (count of new companion rows; integer).

### 10. Substitution chain (threshold)
```
Step 1 (definition):
  N_W7_post_regen = | { line ∈ s85_gate_verdicts.txt : line is W9a-99 companion
                          row for one of the 7 W7 GATE_IDs } |
  N_schema_1_5_post_regen = | { line ∈ s85_gate_verdicts.txt : line is W9a-99
                                  companion row for one of the 17 schema-1.5
                                  GATE_IDs } |
  N_total_post_regen = N_W7_post_regen + N_schema_1_5_post_regen
  N_target = 7 + 17 = 24
Step 2 (substitute, post-regen):
  Run grep with W9a-99 row pattern for each TARGET_LIST GATE_ID; count.
Step 3 (simplify):
  N_total_post_regen ∈ {0, 1, ..., 24} (each entry has at most one new
  W9a-99 companion row appended this gate).
Step 4 (direction):
  N_total_post_regen == 24  ⇒  PASS (with closure-determinism check)
  N_total_post_regen  < 24  ⇒  FAIL or INFO (per §9 distinction)
Conclusion: PASS requires conjunction of (count==24) AND
  (PART 1 closure sha256 all match) AND (no historical edit).
```

### 11. Solution-space meaning
- **PASS**: closes the v3-ladder sig_2 channel for S85 (no W7 verdict line is
  single-SHA anymore) AND closes the schema-1.5 documentation drift for the
  17 W6-W13 entries. S86 v3-closure-audit will not flag these gates again.
- **FAIL on count**: indicates a producing script does not yet emit dual-SHA
  format; carry forward to S87 as a script-template-update item.
- **FAIL on closure mismatch**: indicates a producing script is non-deterministic
  in its input-pin map (a serious bug — flag the gate for forensic review,
  do not silently overwrite).

### 12. Effort estimate
0.3-0.5 wave (≈ 2-4 h: 7 script re-runs + 17 hash computations + verification grep).

### 13. Substrate-framing reminder
META-class. The dual-SHA discipline pins audit-trail integrity: content_sha256
(the artifact) and audit_sha256 (the closure transcript) are TWO independent
witnesses that the gate's verdict was produced from the input-pin map, not
fabricated. This is the substrate-vs-emergent distinction at the audit level:
the artifact (content) is the substrate of the verdict; the closure (audit)
is the emergent provenance. Both must agree.

---

## §W0b-5. S86-DUAL-SHA-INFRASTRUCTURE

### 1. Gate ID
`S86-DUAL-SHA-INFRASTRUCTURE`

### 2. Trigger
`[AUDIT]` — script-install gate; threshold is "audit script exists, is invoked
by the post-session hook, and produces zero false-positives on the
by-design re-emission allowlist".

### 3. Classification
**META** — audit infrastructure (post-session hook chain).

### 4. Agent type — SPECIALIST (NOT gen-physicist)
**Assignment**: `kaku-speculative-theorist`
**Rationale**: kaku owns cross-paradigm registry edits and the audit-script
catalogue; the dual-SHA uniqueness audit is a sibling of the existing
`_pru_cardinality_audit.py`, `_yaml_gate_validator.py`, and
`_recovery_controller.py` audit scripts. kaku-track ownership maintains the
audit-script naming convention (`_<topic>_audit.py`) and the v3-closure-audit
hook integration pattern. The allowlist patterns (REFRAME / logspace fix /
regex fix) are CROSS-paradigm patterns surfaced across multiple specialists'
syntheses — kaku is the natural home for the cross-cutting infrastructure
piece.

### 5. Hypothesis
After the gate runs, `computations/_dual_sha_uniqueness_audit.py` will
exist as an importable module + invokable script; the post-session hook
`.claude/hooks/post-session/v3-closure-audit.sh` will invoke it as part of the
sig_5 channel; the script will produce zero false-positives when run against
the three allowlisted by-design re-emission patterns (REFRAME / logspace fix /
regex fix).

### 6. Method (full dispatch prompt)

```
You are kaku-speculative-theorist. Execute S86-DUAL-SHA-INFRASTRUCTURE.

Working directory: C:\sandbox\Ainulindale Exflation\

PRE-WORK:
  Read .claude/rules/v3-closure-recovery.md sig_5 specification (the v3 ladder
  fires sig_5 = 0 when duplicate audit_sha256 appears across two or more
  verdict lines; the existing remediation flags the duplicate but does not
  distinguish "by-design re-emission with same closure" from "SHA-hardcoding
  bug").
  Read .claude/hooks/post-session/v3-closure-audit.sh and locate the sig_5
  computation block.
  Read existing audit scripts as templates:
    computations/_pru_cardinality_audit.py
    computations/_yaml_gate_validator.py
  Match the script's signature, exit-code conventions, and JSON output format.

PART 1 — script implementation:
  Create computations/_dual_sha_uniqueness_audit.py with this signature:

    """Per-session sig_5 audit — dual-SHA uniqueness with by-design allowlist.

    Usage:
      python computations/_dual_sha_uniqueness_audit.py \
          --session SN \
          --verdict-file computations/s{N}_gate_verdicts.txt \
          --allowlist-file computations/_dual_sha_allowlist.json \
          --output sessions/session-{N}/sig_5_audit.json

    Exit codes:
      0   audit succeeded; sig_5 status determined (PASS / FAIL written to JSON)
      1   audit failed (script error: missing input, parse error)
      (no exit on physics verdict — sig_5 status is a JSON field, not exit code)
    """

  Functional spec:
    1. Read the verdict file; parse every "# GATE_ID: content_sha256=...
       audit_sha256=..." companion row.
    2. Build dict { audit_sha256 → list of GATE_IDs with that sha }.
    3. For each audit_sha256 with >1 GATE_ID (a duplicate):
         a. Look up the GATE_IDs in the allowlist.
         b. If ALL GATE_IDs in the duplicate set are allowlisted under a
            shared by-design pattern (REFRAME / logspace fix / regex fix),
            mark the duplicate as ALLOWED (sig_5 status PASS for this set).
         c. Else mark as FORBIDDEN (sig_5 status FAIL for this set).
    4. Write sessions/session-{N}/sig_5_audit.json with fields:
         { "session": "S86",
           "total_companion_rows": int,
           "duplicate_audit_sha_sets": [
             {"audit_sha256": "...", "gate_ids": [...], "status": "ALLOWED|FORBIDDEN",
              "allowlist_pattern": "REFRAME|logspace_fix|regex_fix|null"}
           ],
           "sig_5_overall": "PASS|FAIL",
           "false_positive_count": int }
    5. Exit 0 (always; verdict is in the JSON).

PART 2 — allowlist file:
  Create computations/_dual_sha_allowlist.json with three allowlisted
  patterns; each entry is a JSON object with fields:
    { "pattern_name": "REFRAME|logspace_fix|regex_fix",
      "description": "<one-line rationale>",
      "gate_id_glob": "<glob pattern matching GATE_IDs that re-emit by design>",
      "added_session": "S86",
      "added_by_audit": "S86-DUAL-SHA-INFRASTRUCTURE" }

  REFRAME entry:
    pattern_name: "REFRAME"
    description: "REFRAME re-emissions inherit prior closure SHA when the
                  reframing is a label change with identical input-pin map"
    gate_id_glob: "*-REFRAME-*"

  logspace_fix entry:
    pattern_name: "logspace_fix"
    description: "logspace numeric-stability fix re-emits same closure when
                  the fix is mathematically identity (e.g. a log-domain
                  rewrite of the same expression)"
    gate_id_glob: "*-LOGSPACE-FIX-*"

  regex_fix entry:
    pattern_name: "regex_fix"
    description: "regex-pattern fix re-emits same closure when the fix
                  corrects a bug whose triggering input was filtered out
                  by the original regex (so the closure-relevant subset of
                  inputs is unchanged)"
    gate_id_glob: "*-REGEX-FIX-*"

PART 3 — hook integration:
  Edit .claude/hooks/post-session/v3-closure-audit.sh to invoke the new
  script in the sig_5 block:
    python computations/_dual_sha_uniqueness_audit.py \
      --session "$SESSION_NUMBER" \
      --verdict-file "computations/s${SESSION_NUMBER}_gate_verdicts.txt" \
      --allowlist-file "computations/_dual_sha_allowlist.json" \
      --output "sessions/session-${SESSION_NUMBER}/sig_5_audit.json"
  Read the JSON's sig_5_overall field; surface to the audit-summary stdout
  block. Do NOT exit non-zero on sig_5_overall = FAIL (the v3-closure
  controller decides remediation; the hook just reports).

PART 4 — synthetic test (false-positive check):
  Create computations/test_dual_sha_uniqueness_audit.py with three test
  cases:
    1. Inject two GATE_IDs both matching `*-REFRAME-*` with the same
       audit_sha256; expect sig_5_overall = PASS, status = ALLOWED.
    2. Inject two GATE_IDs both matching `*-LOGSPACE-FIX-*` with the same
       audit_sha256; expect sig_5_overall = PASS, status = ALLOWED.
    3. Inject two GATE_IDs that match neither allowlist pattern with the
       same audit_sha256; expect sig_5_overall = FAIL, status = FORBIDDEN.
  Run the test; record false_positive_count == 0 across allowlisted patterns.

VERDICT EMISSION:
  Append ONE canonical line to computations/s86_gate_verdicts.txt:
    value=<false_positive_count_on_allowlisted_patterns>  (target: 0)
    scheme=<dual_sha_uniqueness_audit>
    convention=<sig_5_allowlist_v1>
    L_max=N/A
  PASS iff:
    (a) computations/_dual_sha_uniqueness_audit.py exists + executable
    (b) computations/_dual_sha_allowlist.json exists with the 3
        enumerated patterns
    (c) v3-closure-audit.sh invokes the new script in the sig_5 block
    (d) synthetic test false_positive_count == 0
  FAIL iff any (a)-(d) is violated.
  Companion row: content_sha256 (hash of new audit script + allowlist json
  + hook diff combined) AND audit_sha256 (hash of synthetic-test transcript).

WORKING-PAPER SECTION (≥15 lines):
  sessions/archive/session-86/session-86-working-paper.md §W0b-5
  Include verdict, the script signature verbatim, the three allowlisted
  patterns enumerated with their gate_id_glob, the hook diff (5-10 lines),
  the three synthetic test outcomes, and a 3-line note on why allowlisting is
  necessary (REFRAME / logspace_fix / regex_fix re-emit by mathematical
  identity; the v3-ladder sig_5 channel without an allowlist would flag
  these as bugs and the controller would loop on Stage-2 fallback per
  v3-closure-recovery.md).

PROHIBITED:
  - Hardcoding any audit_sha256 in the test fixtures (compute from synthetic
    GATE_IDs at test time; per v3-closure-recovery.md sig_5 hardcoding
    prohibition).
  - Adding a 4th allowlist pattern without registry-level approval (the
    allowlist is an exception list, not a default; the gate is FAIL if
    pattern count > 3 in this initial install).
  - Editing the existing _pru_cardinality_audit.py or _yaml_gate_validator.py
    (only the new audit script + allowlist + hook line are added).
```

### 7. Machinery pin (PRDR)

| Free parameter | Pin | Source |
|:---------------|:----|:-------|
| script_path | `computations/_dual_sha_uniqueness_audit.py` | path-pinned |
| allowlist_path | `computations/_dual_sha_allowlist.json` | path-pinned |
| hook_path | `.claude/hooks/post-session/v3-closure-audit.sh` | path-pinned |
| allowlist_pattern_count | 3 (exactly: REFRAME, logspace_fix, regex_fix) | enumerated |
| allowlist_patterns | {REFRAME, logspace_fix, regex_fix} | enumerated verbatim |
| synthetic_test_count | 3 (one per pattern + one negative control = 3 enumerated above) | enumerated |
| false_positive_target | 0 | rule-pinned |
| script_exit_code_convention | exit 0 always (verdict in JSON, not exit code; per math-scripts.md) | rule-pinned |
| schema_version | R3 | rule-file-v3 |
| input_sha_v3_audit_sh_pre | `<computed-at-runtime>` | dynamic |

### 8. Expected output 4-tuple
`(value=<false_positive_count>, scheme=dual_sha_uniqueness_audit, convention=sig_5_allowlist_v1, L_max=N/A)`

### 9. PASS/FAIL/INFO threshold
- **PASS**: script exists + allowlist exists with 3 patterns + hook invokes
  it + synthetic test false_positive_count == 0.
- **FAIL**: any of the four PASS conjuncts fails. Most common failure:
  hook-integration line missing (the script exists but is never invoked at
  session close, so sig_5 audit silently does nothing).
- **INFO**: not applicable (binary).

Tolerance rule: ABSOLUTE (false positive count; integer).

### 10. Substitution chain (threshold)
```
Step 1 (definition):
  S = boolean: script file exists at script_path
  A = boolean: allowlist file exists at allowlist_path with 3 patterns
  H = boolean: v3-closure-audit.sh contains invocation of script
  N_fp = synthetic-test count of false positives on allowlisted patterns
Step 2 (substitute):
  PASS_predicate = S AND A AND H AND (N_fp == 0)
Step 3 (simplify):
  Each conjunct evaluates from filesystem + grep + test execution.
Step 4 (direction):
  All four conjuncts true → PASS; any false → FAIL.
Conclusion: gate is conjunctive on four checks.
```

### 11. Solution-space meaning
- **PASS**: closes the v3-ladder sig_5 false-positive corridor — by-design
  re-emissions (REFRAME / logspace fix / regex fix) no longer trigger the
  Stage-2 V3-NON-COMPLIANT fallback; v3-closure controller can distinguish
  intentional re-emission from SHA-hardcoding bugs.
- **FAIL on hook-integration**: the script exists but the hook does not
  invoke it; sig_5 still fires its old logic (no allowlist) and S86 sessions
  with intentional re-emissions will hit V3-NON-COMPLIANT incorrectly.
  Fix: re-edit the hook.
- **FAIL on false-positive count > 0**: the allowlist pattern logic has a
  bug; the gate flags an allowlisted re-emission. Fix: debug the
  pattern-matching code.

### 12. Effort estimate
2-3 h (script implementation + allowlist + hook edit + synthetic tests; no
GPU; pure Python + bash).

### 13. Substrate-framing reminder
META-class. The audit script enforces audit-trail integrity at session close:
the `audit_sha256` field encodes the closure-hash provenance of every gate;
duplicate audit_sha256 across gates is either intentional (mathematical
identity at the input-pin level — REFRAME / logspace_fix / regex_fix) or
fabricated (SHA-hardcoding bug). The allowlist is the rule-pinned rule for
distinguishing the two. Substrate-framing analog: the audit script
distinguishes "two emergent observations of the same substrate computation"
(intentional duplicate) from "two emergent labels on the same fabricated
artifact" (bug). Only the former is allowed.

---

## §X. Wave W0b → Downstream Decision Point

**Per-gate downstream consequences for S86**:

- **R4 PASS** unblocks W3 §401/§543 from re-emitting the c_fabric/Λ
  conflation; if R4 FAILs, W3 dispatch must include a phrasing-guard step
  in its prompt.
- **R7 PASS** populates the §VII registry slot W1a (T2/T3) will cite when
  landing the NCG-Meta-Theorem at §VII.R; if R7 FAILs, W1a's T2 landing
  text must inline the witnesses rather than cross-referencing the entry.
- **R8 PASS** is a HARD prerequisite for W8 P6 + P7; if R8 FAILs, W8 cannot
  cite the methodology entry by keyword and the three-layer adjudication
  must be re-justified inline at W8 dispatch (extra ~2 h W8 effort).
- **R9 PASS** clears 24 v3-ladder sig_2 / schema-1.5 flags; if R9 FAILs
  partially (e.g. count = 20/24), the remaining 4 are carried into S87 as
  a "verdict-file companion-row backlog" item.
- **R10 PASS** installs the sig_5 allowlist infrastructure for the S86
  post-session hook; if R10 FAILs, S86 close-out hits the OLD sig_5 logic
  and any intentional re-emission triggers V3-NON-COMPLIANT.

**Aggregate W0b PASS decision**: ALL FIVE gates must PASS for W0b to be
considered methodologically clean. Partial PASS (3-4 of 5) is acceptable for
S86 execution to proceed — the failed gate(s) are carried forward into S87
W0a-equivalent; the W0b Stage-2 fallback `V3-NON-COMPLIANT` is then logged
into S86's handoff §1 metadata per `.claude/rules/v3-closure-recovery.md`.

**Concurrent dispatch within W0b**: All 5 gates are MUTUALLY INDEPENDENT at
execution time (R7 and R8 share the §VII anchor sequence but R8 reads R7's
§VII letter assignment at runtime; the orchestrator dispatches R7 FIRST,
waits for completion, then R8). R4, R9, R10 are independent of all others
and run fully parallel. Effective parallelism: 4 concurrent (R4 + R7 → R8 +
R9 + R10), with R8 sequenced after R7.

---

## §0.10. Wave W0b Machinery-Enumeration Pin (PRDR)

Per `.claude/rules/epistemic-discipline.md` PRDR / PRU prevention, every
free parameter of every producing artifact in W0b is enumerated below.
Any unpinned parameter detected at execution time triggers
PRE-REG-INCOMPLETE (Class-8 INFO verdict, not FAIL).

### R4 (`S86-CANONICAL-PHRASING-AUDIT`)
- target_file_canonical: `computations/canonical_constants.py` ✓
- target_file_w3_plan: `sessions/session-plan/session-86-plan-w3.md` (only
  if file exists at execution; else N/A) ✓
- forbidden_pattern_set: 4 enumerated patterns ✓
- corrected_docstring_text: verbatim string ✓
- audit_tool: Grep `-i` recursive ✓
- schema_version: R3 ✓

### R7 (`S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY`)
- target_registry: `sessions/permanent-results-registry.md` ✓
- target_subsection_letter: dynamic-at-runtime (next available §VII letter) ✓
- witness_count: 4 ✓
- witness_set: 4 enumerated witnesses ✓
- keyword_string: `single-name conflation` (verbatim, lowercase) ✓
- schema_version: R3 ✓

### R8 (`S86-PRR-THREE-LAYER-ADJUDICATION`)
- target_registry: `sessions/permanent-results-registry.md` ✓
- target_subsection_letter: dynamic-at-runtime, AFTER R7 lands ✓
- keyword_string: `three-layer adjudication for joint-channel ρ verdicts` ✓
- layer_count: 3 ✓
- layer_set: {LAYER-1, LAYER-2, LAYER-3} ✓
- generalization_clause_substring: verbatim ✓
- schema_version: R3 ✓

### R9 (combined regen + canonicalization)
- target_verdict_file_s85: `computations/s85_gate_verdicts.txt` ✓
- target_verdict_file_s86: `computations/s86_gate_verdicts.txt` (THIS
  gate's verdict line) ✓
- target_count_W7_single_sha: 7 ✓
- target_count_schema_1_5: 17 ✓
- target_total: 24 ✓
- dual_sha_template_version: W9a-99 ✓
- append_helper: `.claude/templates/script-template.py append_verdict()` ✓
- closure_determinism_check: required, PART 1 only ✓
- schema_version: R3 ✓

### R10 (`S86-DUAL-SHA-INFRASTRUCTURE`)
- script_path: `computations/_dual_sha_uniqueness_audit.py` ✓
- allowlist_path: `computations/_dual_sha_allowlist.json` ✓
- hook_path: `.claude/hooks/post-session/v3-closure-audit.sh` ✓
- allowlist_pattern_count: 3 ✓
- allowlist_patterns: {REFRAME, logspace_fix, regex_fix} ✓
- synthetic_test_count: 3 ✓
- false_positive_target: 0 ✓
- script_exit_code_convention: exit 0 always ✓
- schema_version: R3 ✓

**PRU-cardinality target**: D_PRU_raw == 0 across all five gates after this
plan lands. The `_pru_cardinality_audit.py` tool (W0a R2) MUST report 0
unpinned parameters when run on this plan.

---

## §0.11. Wave W0b Input-SHA Ledger

Per `.claude/rules/gate-verdicts.md`, every input file each producing artifact
reads MUST have either a precomputed SHA-256 pin or a `<computed-at-runtime>`
marker.

| Gate | Input file | SHA-256 |
|:-----|:-----------|:--------|
| R4 | `computations/canonical_constants.py` (pre-edit) | `<computed-at-runtime>` |
| R4 | `sessions/session-plan/session-86-plan-w3.md` (pre-edit, if exists) | `<computed-at-runtime>` (or N/A) |
| R7 | `sessions/permanent-results-registry.md` (pre-edit) | `<computed-at-runtime>` |
| R7 | closeout reference (4-witness inventory) — NOT READ by gate, only by planner | N/A (out of gate scope) |
| R8 | `sessions/permanent-results-registry.md` (post-R7 state) | `<computed-at-runtime>` (depends on R7 closure) |
| R9 | `computations/s85_gate_verdicts.txt` (pre-regen) | `<computed-at-runtime>` |
| R9 | each W7 producing script `computations/s85_w7_*.py` (per-line SHA) | `<computed-at-runtime>` per script |
| R9 | each schema-1.5 entry's primary output artifact `.npz` / `.json` | `<computed-at-runtime>` per artifact |
| R10 | `.claude/hooks/post-session/v3-closure-audit.sh` (pre-edit) | `<computed-at-runtime>` |
| R10 | template audit scripts `computations/_pru_cardinality_audit.py` and `_yaml_gate_validator.py` (read-only, as templates) | `<computed-at-runtime>` (read-only) |

All `<computed-at-runtime>` markers are resolved at gate execution and
written into the verdict line's closure SHA; the closure SHA itself is
SHA-256 of the ordered input-pin map per
`.claude/templates/script-template.py` Section 4.

---

**End of Wave W0b plan.** Five META-class registry / methodology / audit
gates; no physics computation; ~0.7-0.9 wave aggregate effort; all five
mutually independent at execution (R7 → R8 sequencing only; R4, R9, R10
fully parallel).
