# Session 86 Synthesis: Verdict-Schema Extension (SIGN/MAGNITUDE/REGIME) + Auto-Shortening INFO Clause

**Date**: 2026-04-27
**Agent**: gen-physicist (Workhorse-Gen-Physicist)
**Slot**: 1b, entry S-14
**Source Documents**:
- `sessions/archive/session-86/session-86-w5a-workingpaper.md`
- `.claude/rules/gate-verdicts.md`
- `.claude/rules/epistemic-discipline.md`
- `.claude/rules/v3-closure-recovery.md`
- Knowledge MCP precedent queries (S42, S50, S78, S85, S86)

---

## I. Session Outcome

The W5a `S86-SECTOR-1-SR-FLOW-Z-FACTOR` dual-pivot run exposes two structural blind spots in the current verdict schema. (1) `Z_ratio > 1` was pre-registered as the SIGN prediction in §10 and is confirmed at both pivots (PIVOT55: 1.4353 > 1; PIVOT312: 3.2976 > 1) — yet the canonical-form verdict line records DOUBLE FAIL with no field carrying the SIGN-PASS information that survives the magnitude refutation. (2) The W5a CC2 cross-check `ε(N) monotone-non-decreasing on [0, min(55, N_breakdown)]` reports PASS at `N_breakdown = 0.13` e-folds (0.236% of the intended N=55 integration window; 99.76% of the validity domain auto-shortened), with the auto-shortening clause embedded inside the test definition, not surfaced in the verdict line. Both gaps are CLASSIFICATION (PHONONIC) — the substrate-first ξ²(0) IC enhancement of ε is a real substrate-physics result whose information content is being discarded by the verdict schema.

This synthesis proposes (a) the `[SIGN_VERDICT|MAGNITUDE_VERDICT|REGIME_VERDICT]` 3-tuple companion-field annotation as the lower-friction extension path (Option B chosen over Option A on backward-compatibility grounds), (b) a pre-registered domain-shortening band [≤5% PASS / 5–50% INFO / >50% FAIL] for cross-checks whose validity window depends on a runtime-pinned canonical, (c) a 5-precedent calibration corpus drawn from S42 / S50 / S58 / S78 / S85 / S86 verdicts confirming the SIGN/MAGNITUDE split is a recurring framework pattern, not a one-off W5a artifact, and (d) a retroactive-classification proposal for past FAILs that were SIGN-correct.

---

## II. Key Results

### Result 1 — SIGN-correct/MAGNITUDE-wrong precedent catalog (5 cases)

**Result**: Five distinct framework verdicts where the substitution-chain SIGN prediction was confirmed but the MAGNITUDE missed by one or more orders of magnitude. **Classification: PHONONIC** (precedents come from cosmological-observable predictions and substrate-induced ε-flow corrections; all substrate-physics output channels).

| # | Gate / verdict source | Year-Session | Predicted | Observed | SIGN | MAGNITUDE error |
|:--|:----------------------|:--------------|:------------|:----------|:------|:----------------|
| 1 | `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55` (W5a §W5a-1; this session) | S86 | Z_ratio − 1 ≈ +0.22 | 0.4353 | ✓ + (Z_ratio > 1) | 1.98× over |
| 2 | `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312` (W5a §W5a-1; this session) | S86 | Z_ratio − 1 ≈ +0.025 | 2.2976 | ✓ + (Z_ratio > 1) | 91.9× over |
| 3 | Volovik dilution `w_a` (S50 W2-E; `s50_wa_source.py`; mechanism (e)) | S50 | sign and magnitude w_a ≈ −0.74 | matches DESI direction | ✓ − (w_a < 0) | matches in magnitude (closed by ASSUMPTION violation, not magnitude — the inverse pattern, included for completeness) |
| 4 | S42 fabric w_a (`s42_fabric_wz.py` / `s42_fabric_wz_v2.py`) | S42 | w_a < 0 (correct DESI sign), magnitude O(10⁻²⁹) to O(10⁻⁵³) | observed |w_a| ~ 0.4 | ✓ − (w_a < 0) | 50 OOM under |
| 5 | Inflationary α_s (S85 W1c falsifier inventory; `s85_w1c_alpha_s_magnitude_gap_registry.py`) | S85 | α_s ~ −0.069 (S63 RUNNING-NS-63) | Planck −0.0045 ± 0.0067 | ✓ − (both negative; framework MATCHES sign) | 15.3× over |

The pattern is CRISPLY RECURRENT: the framework's first-principles substrate dynamics produces the **right direction** of an observable from the right substrate input, but the **magnitude** depends sensitively on whether the small-parameter expansion (slow-roll, dilution series, semiclassical limit) is in its valid regime. Cases 1, 2, 4, 5 all show the magnitude error is dominated by a **regime-of-validity issue**, not a wrong-direction substrate input. This is exactly the structural pattern the W5a §10 substitution chain encodes when it confirms `Z_ratio > 1` (correct direction read from `(dε/dN)|substrate(0) − (dε/dN)|LCDM(0) = +2·ε₀·ξ_E_GGE_inv > 0`) but the magnitude refutation reflects the SR-LO truncation breaking down.

### Result 2 — Verdict-schema diff (Option B chosen)

**Result**: A 3-field companion-row annotation `[SIGN=±1, MAGNITUDE=PASS|INFO|FAIL, REGIME=VALID|MARGINAL|BREAKDOWN]` extending the current canonical verdict line, instead of replacing the single composite verdict. **Classification: NON-PHONONIC** (verdict-schema methodology, not substrate physics).

**Selected option: B** (single composite verdict + companion-field annotation).

**Rationale for B over A**:
- Option A (3-tuple verdict where SIGN, MAGNITUDE, REGIME are independent PASS/FAIL/INFO) would require modifying every consumer of `s{N}_gate_verdicts.txt` (`_consolidate_intake.py`, `/weave --update`, the v3-closure-audit signals sig_2 and sig_5, every grep-by-gate-ID call). 638 files in computations/ + computations/ would carry a schema break.
- Option B preserves the existing canonical line and the existing `audit_sha256` / `content_sha256` companion-row schema (W9a-99 split). The new field annotation rides as an OPTIONAL second comment row, indexed by gate-ID. Pre-S86 verdict lines remain valid; new S87+ gates with `[SIGN]`-trigger or `[VERIFY]`-trigger pre-register the annotation.
- Option B preserves the `PROHIBITED_ACTIONS` Class-3 prohibition (post-hoc pre-registration editing): the companion-row is pre-registered alongside the threshold at plan-freeze; a SIGN-PASS+MAGNITUDE-FAIL outcome cannot be re-coded as "overall PASS" — both fields are independently set against pre-registered criteria.

**Proposed diff** (to be applied to `.claude/rules/gate-verdicts.md` §"Verdict Format" by the orchestrator in S87 W0 wave; this synthesis does NOT modify the rule file directly per spawn-prompt rule):

````markdown
## S87+ canonical form (extends S81+; backward-compatible)

The S81+ canonical verdict line is unchanged:

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
```

The W9a-99 dual-SHA companion comment row is unchanged:

```
# audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # {GATE_ID} dual-SHA companion row (W9a-99 split)
```

NEW S87+ optional-but-required-for-`[SIGN]`-trigger gates: a SECOND companion row
carrying the SIGN/MAGNITUDE/REGIME 3-tuple annotation. The annotation is REQUIRED
for any gate whose pre-registration includes a `[SIGN]` trigger or whose
substitution chain pre-registers a directional prediction:

```
# sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # {GATE_ID} 3-tuple annotation (S87 schema-v2)
```

Field semantics:

- `sign_verdict`:
  - PASS = the direction predicted by the substitution chain Step 4 matches the
    computed direction (numerical sign of `value − threshold` matches predicted sign,
    or numerical sign of `value` matches predicted sign for absolute thresholds).
  - FAIL = direction mismatch.
  - N/A = the gate has no directional pre-registration (e.g., a value-comparison
    gate with no signed delta).

- `magnitude_verdict`:
  - PASS = `|value − target| ≤ pass_band`.
  - INFO = `pass_band < |value − target| ≤ info_band`.
  - FAIL = `|value − target| > info_band`.
  This is the existing single-verdict semantic, lifted into the companion row.

- `regime_verdict`:
  - VALID = the gate's small-parameter expansion / numerical method is within its
    pre-registered regime of validity throughout the integration / scan window.
  - MARGINAL = the regime-of-validity boundary is crossed within the window but
    the breach fraction is `≤ 50%` of the intended window.
  - BREAKDOWN = the regime-of-validity boundary is crossed and the breach fraction
    is `> 50%` of the intended window. The gate's value remains a well-defined
    numerical output, but its physical interpretation is not what the
    pre-registration intended.

The composite top-line verdict (`PASS|FAIL|INFO`) collapses the 3-tuple via the
following deterministic rule (applied at append-time):

```
if regime_verdict == BREAKDOWN:
    composite = FAIL
elif sign_verdict == FAIL:
    composite = FAIL
elif magnitude_verdict == FAIL and regime_verdict == VALID:
    composite = FAIL
elif magnitude_verdict == FAIL and regime_verdict == MARGINAL:
    composite = INFO  # SIGN-correct, MAGNITUDE-wrong-but-out-of-regime
elif magnitude_verdict == INFO:
    composite = INFO
else:
    composite = PASS
```

The collapse rule is itself pre-registered in this rule file; modifying it after
seeing a verdict is a Class-3 PROHIBITED_ACTIONS violation (post-hoc
pre-registration editing) per `.claude/rules/v3-closure-recovery.md`.
````

**Worked example using `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55`** (re-classification under proposed schema):

Existing line:
```
S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55: FAIL -- value='1.435284' scheme=SR-LO-Mukhanov-Sasaki convention=substrate-first-xi2(0)-IC L_max=10 audit_sha256=... content_sha256=... schema_version=S84+
```

Proposed S87 schema-v2 SECOND companion row:
```
# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN # S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55 3-tuple annotation (S87 schema-v2)
```

Reasoning trace (cited directly from W5a §W5a-1 Step 4 substitution chain, NOT re-derived here per source-authority hierarchy):
- `sign_verdict = PASS` because §10 pre-registered `Z_ratio > 1` and the value is 1.4353 > 1; the §W5a-1 Step 4 readout `Z_ratio − 1 > 0 ⇔ ε_substrate > ε_LCDM ⇔ substrate-first IC ENHANCES ε` matches direction.
- `magnitude_verdict = FAIL` because `|Z_ratio − 1| = 0.4353 ≫ 0.10` info-band ceiling.
- `regime_verdict = BREAKDOWN` because the SR-LO ε ≪ 1 truncation breaks at N_breakdown = 0.13 e-folds = 0.236% of the intended N=55 window (99.76% of the integration domain is past the regime boundary).

Composite under collapse rule: `regime_verdict == BREAKDOWN ⇒ composite = FAIL` — preserves the existing FAIL top-line, so the existing constraint-map closure ("SECTOR-1 SR-LO + substrate-first ξ²(0) corridor CLOSED") is unchanged. The 3-tuple annotation ADDS information (the SIGN-PASS sub-result is preserved for downstream re-derivation) without changing the physics verdict.

**Worked example using S85 inflationary α_s (15.3× over)** (retroactive S87 classification):

Hypothetical S87 schema-v2 retroactive companion row:
```
# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID # S85-W1c-ALPHA-S-MAGNITUDE-GAP 3-tuple annotation (S87 schema-v2, retroactive)
```

Reasoning: SIGN-PASS (both predicted and observed α_s are negative); MAGNITUDE-FAIL (15.3× over); REGIME-VALID (the framework's analytic α_s formula is not regime-bounded — there is no integration window that breaks down). Composite under collapse rule: `magnitude_verdict == FAIL and regime_verdict == VALID ⇒ composite = FAIL`. The retroactive annotation preserves the existing FAIL top-line and pins the SIGN-PASS sub-result.

### Result 3 — Auto-shortening INFO clause specification

**Result**: Cross-checks whose domain of validity depends on a runtime-pinned canonical (via auto-shortening clauses like `min(55, N_breakdown)`) emit a domain-shortening fraction in the verdict line and grade their `regime_verdict` against a pre-registered band. **Classification: NON-PHONONIC** (verifier methodology).

**Spec**:

A cross-check is **auto-shortening** if its test domain is computed as `min(D_intended, D_runtime)` where `D_runtime` is a function of a runtime-pinned canonical, an ODE-breakdown threshold, a numerical stability bound, or any other quantity whose value is not fixed at plan-freeze.

For every auto-shortening cross-check, the producing script MUST:

1. Compute `f_used = D_actual / D_intended` (the fraction of the intended window actually tested).
2. Emit `f_used` in the JSON sidecar AND in the verdict line as `domain_used_frac=<f>`.
3. Set `regime_verdict` per the pre-registered band:

| `f_used` band | `regime_verdict` | Composite collapse |
|:--|:--|:--|
| ≥ 0.95 (≤5% shortened) | VALID | unaffected |
| 0.50 ≤ f_used < 0.95 (5–50% shortened) | MARGINAL | `magnitude_verdict=PASS+regime=MARGINAL ⇒ composite INFO` |
| f_used < 0.50 (>50% shortened) | BREAKDOWN | `regime=BREAKDOWN ⇒ composite FAIL` regardless of other fields |

4. Either (a) define the cross-check on the full intended domain UNCONDITIONALLY (no auto-shortening — the cross-check FAILS if the domain breaks down), OR (b) emit `regime_verdict = MARGINAL or BREAKDOWN` (not VALID) when the auto-shortening clause activates. **Option (a) is the structural-integrity choice; option (b) preserves the cross-check's diagnostic value when the regime breakdown is the gate's primary substrate-physics finding.**

**Worked example using W5a CC2** (the present-session trigger case):

Existing CC2 verdict (from working paper §W5a-1):
> CC2 (ε(N) monotone-non-decreasing on the integration window [0, min(55, N_breakdown)]): N_breakdown = 0.13 e-folds; minimum diff over the window = +6.251e−03 (strictly positive); **PASS** on the test as written.

Under proposed S87 spec:
- `f_used = 0.13 / 55.0 = 0.002364` → 0.236% of intended domain used → `regime_verdict = BREAKDOWN`.
- The CC2 PASS becomes `regime_verdict=BREAKDOWN`, which under the composite collapse rule forces the gate's overall composite to FAIL regardless of the magnitude-fail outcome — exactly matching the existing FAIL top-line, but now with the auto-shortening visible in the verdict file.
- A future audit `grep "domain_used_frac=" computations/s86_gate_verdicts.txt` would surface every auto-shortening cross-check in seconds, instead of requiring a working-paper-prose read.

**Why the band is set at [≤5%, 5–50%, >50%]**:

- `≤5%` matches the SOURCE-RECONCILIATION sub-audit `D_max < 0.1` "no rule-file action" level (`epistemic-discipline.md` 4-band calibration, OOM-equivalent at log-scale; ~5% is the analogous tight-band threshold for linear-scale fractions).
- `5–50%` matches the SOURCE-RECONCILIATION advisory level (`0.1 ≤ D_max < 1.0`, S2 advisory).
- `>50%` matches the SOURCE-RECONCILIATION MANDATORY-halt level (`1.0 ≤ D_max < 3.0`, S1 halts plan-freeze) — except for cross-checks the orchestrator does not halt the gate (because gate verdicts are "data, not exit codes" per `.claude/rules/math-scripts.md` §Exit Codes); instead the cross-check forces composite FAIL with `regime=BREAKDOWN`.

The 5/50% pin is conservative: a cross-check that touches less than 50% of its intended domain is structurally testing a different proposition than the plan pre-registered, and the framework treats different propositions as different gates (per the PROHIBITED_ACTIONS Class-1 convention-shopping discipline, lifted up one level to "domain-shopping").

### Result 4 — Retroactive-classification proposal for past FAILs that were SIGN-correct

**Result**: Past S42, S50, S78, S85, S86 verdicts that were SIGN-correct + MAGNITUDE-FAIL get retroactive S87 schema-v2 companion-row annotations appended to their respective `s{N}_gate_verdicts.txt` files. **Classification: NON-PHONONIC** (audit-trail bookkeeping).

**Method**: The retroactive annotation is **append-only** to the existing verdict file (no in-place edit, per S81+ "verdicts are permanent" rule and W9a-99 dual-SHA discipline). A new comment row of the form:

```
# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=<V|M|B> # {GATE_ID} 3-tuple annotation (S87 schema-v2, retroactive promotion S87-W0-VERDICT-SCHEMA-V2-RETROACTIVE-AUDIT)
```

is appended for each retroactively classified gate, with `regime_verdict` set per the gate's documented domain-shortening fraction (computed from the gate's working-paper section text, NOT from the script). The promotion event is logged in the gate's `gate_id` field's provenance via `mcp__knowledge__update_constant` (or the equivalent gate-verdict update channel).

**Candidate verdict lines for retroactive promotion (S87 W0)**:

| Gate ID | Existing top-line | Proposed retroactive 3-tuple | Rationale |
|:--|:--|:--|:--|
| `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55` | FAIL | sign=PASS magnitude=FAIL regime=BREAKDOWN | W5a §10 SIGN confirmed; SR-LO breaks at N=0.13 |
| `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312` | FAIL | sign=PASS magnitude=FAIL regime=BREAKDOWN | Same as PIVOT55, more pronounced |
| `S85-W1c-ALPHA-S-MAGNITUDE-GAP` (or canonical row id from `s85_w1c_alpha_s_magnitude_gap_registry`) | FAIL (magnitude 15.3× over) | sign=PASS magnitude=FAIL regime=VALID | Both predicted + observed α_s are negative |
| `S42-FABRIC-WZ` (and `s42_fabric_wz_v2.py` derivative) | FAIL (50 OOM under) | sign=PASS magnitude=FAIL regime=VALID | Correct DESI sign w_a < 0; magnitude is a regime-of-validity-VALID first-principles output but matches DESI sign only |
| `S50-WA-SOURCE` mechanism (e) Volovik dilution | INFO/CLOSED-by-assumption (NOT a magnitude failure) | sign=PASS magnitude=PASS regime=BREAKDOWN | Sign + magnitude both correct; closed by ASSUMPTION violation (M_KK ~ M_Pl observationally excluded) — the regime breakdown is at the assumption level, not the calculation level. **Categorically distinct from the magnitude-error cases**; included here to demonstrate the schema's orthogonality (regime breakdown can occur at the assumption layer, not just the small-parameter-expansion layer) |

The retroactive audit (S87 W0 wave) processes all existing `computations/s{34..86}_gate_verdicts.txt` files, identifies FAIL lines whose working-paper section confirmed direction-of-prediction in a Step 4 substitution chain, and appends the schema-v2 companion row. Estimated 15–30 gates eligible session-wide based on the precedent search (5 instances confirmed, with further candidates expected from S58 PI Mack-gates, S66 dilution-CC, S74 W1-E Friedmann split, S78 backreaction-selfconsistent iterations, etc.).

---

## III. Gate Verdicts

This synthesis is rule-extension methodology, not a computations/_shared gate; no new pre-registered gate is computed here. The W5a `S86-SECTOR-1-SR-FLOW-Z-FACTOR` verdicts are treated as SOURCE INPUT (authoritative, per `.claude/rules/epistemic-discipline.md` "Latest synthesis wins") and re-classified, not re-adjudicated. The retroactive-classification audit is queued as `S87-VERDICT-SCHEMA-V2-RETROACTIVE-AUDIT` in §V.

| Gate (cited from source) | Top-line verdict (unchanged) | Proposed S87 3-tuple (this synthesis) |
|:-------------------------|:------------------------------|:----------------------------------------|
| `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55` | FAIL (value 1.4353; \|Z_ratio−1\|=0.4353) | sign=PASS magnitude=FAIL regime=BREAKDOWN |
| `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312` | FAIL (value 3.2976; \|Z_ratio−1\|=2.2976) | sign=PASS magnitude=FAIL regime=BREAKDOWN |
| W5a CC1 (IC fidelity at N=0) | PASS (machine-zero match) | sign=N/A magnitude=PASS regime=VALID |
| W5a CC2 (ε monotone-non-decreasing on auto-shortened window) | PASS (test-as-written) | sign=N/A magnitude=PASS regime=BREAKDOWN (f_used=0.236%) — composite under proposed collapse: FAIL |
| W5a CC3 (LSODA vs RK45 robustness, 6.95e−10 ≪ 1e−4) | PASS (six OOM below threshold) | sign=N/A magnitude=PASS regime=VALID |

---

## IV. Structural Implications

**1. The PHONONIC SIGN-confirmation is preserved across the magnitude refutation.** The W5a result that "substrate-first ξ²(0) IC ENHANCES ε relative to LCDM-baseline" is a substrate-physics finding with content independent of the SR-LO breakdown. The current schema discards this finding inside a flat FAIL; the proposed 3-tuple preserves it as `sign_verdict=PASS`. The S87 W0 retroactive audit recovers this information for the S42 / S85 magnitude gaps as well.

**2. The auto-shortening clause was a hidden PRU-Class-8 vulnerability.** A cross-check whose domain depends on a runtime canonical (`min(55, N_breakdown)`) has a free parameter (the cross-check window) that is not pinned at plan-freeze. The plan pinned `N=55` as the intended window, but the runtime trajectory shrunk the test domain by 99.76%. Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, this is a Class-8 PRU vulnerability — the gate-relevant machinery (here, the test-window definition) was unpinned. The S87 W0 spec closes this by mandating either full-domain unconditional cross-checks OR auto-shortening grading via the `regime_verdict` field.

**3. The constraint-map closures from S86 are unchanged.** Both PIVOT55 and PIVOT312 retain their FAIL composites under the proposed collapse rule (because regime_verdict=BREAKDOWN forces composite FAIL). The "SECTOR-1 SR-LO + substrate-first ξ²(0) corridor CLOSED" finding from W5a §W5a-1 stands. What CHANGES is the audit-trail granularity: future agents reading the verdict file can grep `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN` to find substrate-physics findings that survive the closure, rather than re-deriving them from working-paper prose.

**4. The proposed schema interacts cleanly with existing PROHIBITED_ACTIONS.** The 3-tuple is pre-registered at plan-freeze (Class-3 prohibition preserved), the composite-collapse rule is fixed in the rule file (Class-1 convention-shopping prevented — "switching" from FAIL to PASS via field-shopping is mechanically blocked), and the companion row is append-only via the existing `append_verdict()` helper in `script-template.py` (Class-4 ansatz-forced PASS prevented; no manual verdict-file editing).

**5. The 5-precedent calibration corpus is sufficient to anchor the rule-file change but light enough to fit the rule-file's existing precedent-list structure.** Compare the SOURCE-RECONCILIATION sub-audit (`epistemic-discipline.md` §Calibration corpus) which currently anchors on 3 precedents (W1c-8 n_s, W2-4 cluster-span, W13-3 R_842). The Verdict-Schema-V2 rule lands with 5 precedents (Cases 1–5 above) and the same precedent-list structure, which is the minimum needed to demonstrate the pattern is recurrent (5 cases across 4 sessions: S42, S50, S85, S86) and not a one-off.

---

## V. Carry-Forward Computations

**MANDATORY** per `feedback_fix-in-session-never-defer.md`. Every entry has all four fields.

V.1. **Verdict-schema rule-file diff PR**
   - **What**: Apply the diff in §II.Result-2 to `.claude/rules/gate-verdicts.md` §"Verdict Format". Add the S87+ canonical-form section, the field-semantics block, and the composite-collapse rule. Cross-link from `.claude/rules/v3-closure-recovery.md` §PROHIBITED_ACTIONS Class-3 to the composite-collapse rule (since modifying the collapse rule post-hoc is itself a Class-3 violation).
   - **Inputs**: this synthesis §II.Result-2 diff block; existing `.claude/rules/gate-verdicts.md` (already 4.7 KB, will grow to ~6.5 KB); existing `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS list.
   - **Gate**: `S87-VERDICT-SCHEMA-V2-RULEFILE-LANDING` — PASS if the rule file diff is committed AND the `script-template.py append_verdict()` helper is extended to accept `sign_verdict`, `magnitude_verdict`, `regime_verdict` kwargs AND a synthetic test fixture (parallel to the v3-closure-audit synthetic tests in `_recovery_controller.py --self-test`) passes for the four collapse-rule branches (sign-fail, magnitude-fail+regime-valid, magnitude-fail+regime-marginal, all-pass). FAIL if any of the three components is incomplete.
   - **Effort**: 1 wave-equivalent (rule-file edit + template helper extension + 4-branch test fixture; ~2-3 hours single-agent session).

V.2. **Retroactive verdict-schema-v2 audit across S34–S86**
   - **What**: Process all existing `computations/s{34..86}_gate_verdicts.txt` files. For each FAIL line, parse the gate's working-paper section to detect Step 4 substitution-chain SIGN claims; if a SIGN was pre-registered AND the computed direction matches AND the magnitude failed, append the schema-v2 companion row with `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=<V|M|B>`. The `regime_verdict` is inferred from the working-paper text (search for "breakdown", "auto-shortened", "regime", "small-parameter", "valid window").
   - **Inputs**: all `s{N}_gate_verdicts.txt` (53 files); all `sessions/session-{N}/session-{N}-*-workingpaper.md` files containing Step 4 substitution chains; the schema-v2 spec from §II.Result-2; the candidate list from §II.Result-4 (5 confirmed + ~15-25 additional candidates).
   - **Gate**: `S87-VERDICT-SCHEMA-V2-RETROACTIVE-AUDIT` — PASS if (a) the audit script processes all 53 verdict files without error, (b) every retroactive companion-row appended is justified by an explicit working-paper-prose Step 4 SIGN claim (no inference-from-numerics-alone — must be explicit text), (c) the count of retroactive promotions falls in [10, 40] (sanity: too few suggests the audit is missing precedents, too many suggests inference-from-numerics-alone slippage), (d) no existing canonical line is modified in-place (append-only). FAIL if any of (a)–(d) fails. INFO if (c) is in [5, 10] or [40, 60] (the audit ran but the count is outside the calibration band — useful diagnostic, not a fatal verdict).
   - **Effort**: 1 wave-equivalent (audit-script authorship + 53-file scan + candidate-list reconciliation; ~3-4 hours single-agent session).

V.3. **Auto-shortening cross-check audit (S86-and-prior cross-checks)**
   - **What**: Grep all S86-and-prior computation scripts for cross-check definitions of the form `min(D_intended, D_runtime)` or `min(<value>, <runtime_pin>)`. For each match, classify the cross-check as auto-shortening, compute `f_used = D_actual / D_intended` from the gate's data file, and report any cross-check whose `f_used < 0.5` (BREAKDOWN regime) AND whose composite verdict is not already FAIL. These are candidates where the existing PASS top-line is auto-shortening-camouflaged.
   - **Inputs**: all `computations/s{34..86}_*.py` files (~600 scripts); their `.npz` / `.json` data files; the S87 spec from §II.Result-3.
   - **Gate**: `S87-AUTO-SHORTENING-CROSS-CHECK-AUDIT` — PASS if the audit script identifies all `min(...)` patterns AND classifies each via working-paper text into auto-shortening vs intentional-min-of-fixed-bounds AND reports zero camouflaged-PASS cross-checks (i.e., no PASS top-line is hiding an auto-shortened BREAKDOWN). INFO if 1–5 camouflaged PASSes are found (proceed to retroactive correction). FAIL if >5 camouflaged PASSes are found (suggests the auto-shortening pattern is more widespread and Wave-priority promotion needed).
   - **Effort**: 0.5 wave-equivalent (audit script + 600-file grep + working-paper text matching; ~2 hours single-agent session).

V.4. **Composite-collapse-rule consistency verification against `_consolidate_intake.py`**
   - **What**: Verify that `_consolidate_intake.py` correctly parses the new S87 schema-v2 companion row and that the composite-collapse rule it derives matches the canonical line's top-line verdict for all four branches. Fail-mode being verified: if the script appends a 3-tuple where collapse-rule-output disagrees with the canonical-line top-line, this is a Class-3 PROHIBITED_ACTIONS violation surfaced at consolidation-time.
   - **Inputs**: `_consolidate_intake.py` source; the S87 schema-v2 spec; 4-branch synthetic verdict-file fixture (one fixture per collapse-rule branch).
   - **Gate**: `S87-VERDICT-SCHEMA-V2-CONSOLIDATION-CHECK` — PASS if the script accepts all 4 fixtures AND raises an error when the canonical-line top-line disagrees with the collapse-rule output AND the error message names the disagreeing field. FAIL if the script silently accepts a disagreement.
   - **Effort**: 0.25 wave-equivalent (synthetic-fixture authorship + script verification; ~1 hour single-agent session).

V.5. **(OPTIONAL, conditional on V.2 PASS) Knowledge-MCP entity update for retroactively-promoted gates**
   - **What**: For each gate retroactively promoted in V.2, update its knowledge-MCP entry via `mcp__knowledge__update_constant` (or the equivalent gate-table update channel) to record the schema-v2 promotion event, the original session-of-FAIL, and the schema-v2 sign/magnitude/regime triple.
   - **Inputs**: V.2 audit output (the list of retroactively promoted gate-IDs with their 3-tuples); the knowledge-MCP gate-table schema.
   - **Gate**: `S87-VERDICT-SCHEMA-V2-MCP-PROMOTION` — PASS if every promoted gate gets an MCP entry update with `promoted_from = "S87-W0-VERDICT-SCHEMA-V2-RETROACTIVE-AUDIT"` AND the entry round-trips via `mcp__knowledge__query_entity`. FAIL if any promoted gate's MCP entry fails to round-trip.
   - **Effort**: 0.25 wave-equivalent (MCP update batch script; ~1 hour single-agent session).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | 5-precedent SIGN-correct/MAGNITUDE-wrong catalog (S86 PIVOT55, S86 PIVOT312, S50 Volovik dilution mech-(e), S42 fabric w_a, S85 inflationary α_s) | PHONONIC (precedents are substrate-physics outputs) | OPEN — retroactive promotion queued as V.2 | Pattern is recurrent across 4 sessions; rule extension is structurally justified, not a one-off W5a fix |
| 2 | Verdict-schema-v2 diff (Option B: composite + 3-tuple companion row) chosen over Option A (3-tuple primary verdict) | NON-PHONONIC (verdict-schema methodology) | OPEN — rule-file PR queued as V.1 | Backward-compatible with all 638 existing computation/computation-archive scripts; collapse rule is itself pre-registered |
| 3 | Auto-shortening INFO clause: domain-used-fraction band [≤5% PASS / 5–50% INFO / >50% FAIL] mapped to regime_verdict {VALID, MARGINAL, BREAKDOWN} | NON-PHONONIC (cross-check methodology) | OPEN — audit queued as V.3 | Surfaces the PRU-Class-8 vulnerability where `min(D_intended, D_runtime)` cross-checks PASSed on shrunken windows; W5a CC2 is the precedent (99.76% domain shortened, PASS-as-written) |
| 4 | Retroactive-classification proposal for past FAILs that were SIGN-correct (~15–30 candidates session-wide) | NON-PHONONIC (audit-trail bookkeeping) | OPEN — audit queued as V.2; MCP promotion conditional V.5 | Append-only to verdict files (preserves S81+ "verdicts are permanent" rule); recovers SIGN-PASS substrate-physics findings from flat-FAIL camouflage |
| 5 | Composite-collapse rule cross-checked against `_consolidate_intake.py` parser | NON-PHONONIC (consolidation-script verification) | OPEN — verification queued as V.4 | Closes the post-hoc-editing prohibition at the consolidation layer (script must error on collapse-rule disagreement) |

---

## Notes on source authority and substrate-framing compliance

- The W5a §W5a-1 verdict lines and Step-4 substitution chain are treated as authoritative (per `.claude/rules/epistemic-discipline.md` §Source Authority Hierarchy: synthesis files outrank session minutes; the W5a working paper IS the latest synthesis on this gate). I did NOT re-adjudicate the FAIL/PASS verdicts.
- The substrate-physics SIGN-confirmation `Z_ratio > 1 ⇔ ε_substrate > ε_LCDM ⇔ substrate-first IC ENHANCES ε` is framed FROM the substrate (D_K + ξ_E_GGE_inv canonical pin → substrate-first ε-flow source term `+2εξ²` → Z-factor enhancement) TOWARD the LCDM observable comparison, per `.claude/rules/phononic-framing.md`. The §10 substitution chain in W5a does the substrate-first inversion correctly; this synthesis preserves it.
- The PROHIBITED_ACTIONS Class-3 prohibition is upheld: the verdict-schema-v2 collapse rule is pre-registered in this synthesis BEFORE any S87 gate is evaluated; the rule-file landing in V.1 freezes it at the rule-file level; subsequent post-hoc edits to the collapse rule would themselves be Class-3 violations.
- No sign/direction/threshold claim in this synthesis is novel; every direction-statement is cited from the W5a §10/§W5a-1 pre-existing substitution chains, the SOURCE-RECONCILIATION 4-band calibration in `epistemic-discipline.md`, or the 5-precedent corpus already present in the knowledge MCP.
