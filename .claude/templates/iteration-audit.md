# Iteration-Audit Template

Standardized decision rule and vocabulary for auditing any gate whose verdict-log contains >1 iteration. Adoption eliminates PRU (Pre-Registration Underspecification) at the audit-workshop level by construction: this template pre-registers the decision rule, tag vocabulary, severity grading, WARRANT classes, and remediation format that prior ad-hoc audits had to invent in real time.

**Scope**: applies to any multi-iteration gate produced by a scrubbed plan. Mandatory for audit-workshops under §0.10(b) of the session-plan template.

**Authority**: this template is cross-referenced from `epistemic-discipline.md` (Pre-Registration Completeness section). Violations of this template's decision rule are plan-property failures (Class 8 PRU).

---

## 1. Tag Vocabulary (8 tags)

Every iteration past i=1 must be classified with exactly one of these tags. The classification requires a specific commit, file-diff, or content-hash citation as evidence.

| # | Tag                            | Meaning                                                                                          | Evidence required                                                   |
|:-:|:-------------------------------|:-------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|
| 1 | `integrator-config`            | Non-observable machinery change (tolerance, step size, library version)                          | Commit diff touching integrator config only                         |
| 2 | `convention-pin-fix`           | Fix to a pre-registered convention pin (sign, normalization, unit)                               | Commit diff + prior pin text showing the fix is within spec         |
| 3 | `convention-pin-ADDITION`      | New convention pin added mid-run that was NOT in the original scrubbed plan                      | Commit diff + explicit in-log declaration of the new pin            |
| 4 | `regime-diagnostic-addition`   | Adds a diagnostic cross-check without modifying the gate's observable formula                    | Commit diff showing additive-only change                            |
| 5 | `quantity-definition-drift`    | The measured quantity's operational definition changed between iterations (Type II)              | Commit diff touching the observable-formula or metric definition    |
| 6 | `unclear`                      | Motion observed, no diff or commit evidence available                                            | None — default when evidence is missing                             |
| 7 | `iterate-until-PASS`           | Monotone-toward-PASS trajectory without independent justification                                | Verdict-log + pattern test (see §3)                                 |
| 8 | `verdict-class-transition`     | **Flag, not a parallel tag** — any iteration crossing a verdict-class boundary (PASS↔FAIL↔INFO↔INCOMPUTABLE) carries this flag in ADDITION to its primary tag | Verdict-log class comparison i vs. i−1 |

**Re-run waiver**: if iteration i is bit-identical to iteration i−1 (same F_amp value AND same tag 4-tuple AND same content-hash on the producing script), it is classified as `unclear` with LOW severity; it does NOT contribute to `N_fail`. Bit-identity is the formal test — no narrative override.

---

## 2. Severity Grading

Each non-waiver iteration is graded HIGH / MEDIUM / LOW.

| Severity | Criterion                                                                                                           |
|:---------|:--------------------------------------------------------------------------------------------------------------------|
| HIGH     | Iteration changes the code path producing the gate's **primary observable**. Any `verdict-class-transition` flag forces HIGH by construction. |
| MEDIUM   | Iteration changes **auxiliary machinery** pinned by the plan (diagnostic scripts, secondary cross-checks, reporting formats). |
| LOW      | Bit-identical re-run (waiver applies) OR non-observable cosmetic edit (docstring, plot label) with commit proof.    |

`quantity-definition-drift` always carries a separate Type-II flag that is scored independently (see §3), not via the HIGH/MEDIUM/LOW gradient.

---

## 3. Severity-Weighted Decision Rule

Compute a score over all non-waiver iterations in the gate's log:

```
score = 3·N_high + 1·N_medium + 0·N_low + 10·N_iupass + 10·N_quantity_redef
```

where
- `N_high / N_medium / N_low` count HIGH / MEDIUM / LOW iterations,
- `N_iupass` counts iterations tagged `iterate-until-PASS`,
- `N_quantity_redef` counts iterations tagged `quantity-definition-drift`.

**Thresholds**:

| Score range                                              | Warrant verdict      |
|:---------------------------------------------------------|:---------------------|
| `score == 0`                                             | VALID                |
| `0 < score ≤ 2`                                          | VALID (with log note)|
| `3 ≤ score ≤ 4`                                          | CONDITIONAL          |
| `score ≥ 5` **OR** `N_iupass ≥ 1` **OR** `N_quantity_redef ≥ 1` | INVALID        |

The 10× coefficient on `N_iupass` and `N_quantity_redef` ensures either flag triggers INVALID from a single occurrence. Type I drift (convention/machinery) requires accumulation; Type II drift (observable definition) does not.

---

## 4. WARRANT Classes + Scheduling Category

**WARRANT classes** (verdict dimension):

- **VALID** — the gate verdicts as logged stand.
- **CONDITIONAL** — tail verdict defensible; specific iterations compromised; remediation re-run specified.
- **INVALID** — pattern-level failure; all iterations compromised; re-verification required before any downstream use.

**PROVISIONAL** (orthogonal scheduling category, NOT a fourth verdict class):

A gate is `WARRANT-CONDITIONAL + PROVISIONAL` (consumable under remediation-pending) iff ALL four eligibility criteria hold:

1. **Tail verdict defensible** — no plan-letter violation contaminates the tail (e.g., no ε-scan-as-root-cause, no convention-shopping).
2. **Remediation scheduled** with a pre-registered single-clean-re-run spec.
3. **Consumer-side tolerance pre-registered** — every downstream Phase 2 workshop declares `tol_D_i` on input drift BEFORE the gate's remediation completes.
4. **Bounded drift budget** — `Σ tol_D_i` across consumers is bounded; exceeding escalates scheduling to BLOCKED.

Scheduling status matrix:

| Warrant     | Default scheduling |
|:------------|:-------------------|
| VALID       | IMMEDIATE          |
| CONDITIONAL | BLOCKED            |
| CONDITIONAL + PROVISIONAL (criteria 1–4 met) | IMMEDIATE (with drift caveat) |
| INVALID     | BLOCKED            |

---

## 5. Cascade-Compliance Test

Every multi-iteration gate is tested against the plan's authorized iteration cascade:

1. **Does the plan pre-register an iteration cascade for this gate?** (List of permitted fallback steps with stopping criteria.)
2. **Does every iteration in the log correspond to a step authorized by the cascade?**

If (1) is NO, every iteration past i=1 is a **scope violation** regardless of tag (no cascade exists to violate). Minimum warrant downgrade: one step (VALID → CONDITIONAL, CONDITIONAL → INVALID).

If (2) is NO for any iteration, that iteration is automatically tagged `convention-pin-ADDITION` or `quantity-definition-drift` (whichever applies) with HIGH severity.

---

## 6. Remediation Spec Format

Every CONDITIONAL or INVALID warrant produces a remediation spec with this structure.

### 6.1 Universal pins (always)

1. **Commit-before-verdict** — the producing script is committed to the working tree BEFORE the verdict is stamped. The commit hash is recorded alongside the verdict in the log.
2. **Content-hash pairing** — the verdict log records `(script_sha, canonical_constants_sha, input_data_sha)` triple for the iteration.
3. **Single-pass discipline** — the re-run is exactly one execution of `main()`. The first verdict (PASS / FAIL / INFO / INCOMPUTABLE) is final. No further iteration without a new audit.

### 6.2 Gate-specific addendums (as needed)

For each gate, pin any machinery parameter the audit identified as free. Cite the parameter name, pinned value, and first-principles derivation text.

### 6.3 Three-way expected-verdict rule

Pre-register a tolerance `tol_E` BEFORE the remediation re-run. `tol_E` must be pinned in the addendum — setting it after observing the remediation value voids the audit.

Let `V_tail` be the prior log-tail verdict; `V_remed` be the remediation verdict.

| Condition                                                         | Outcome                                              |
|:------------------------------------------------------------------|:-----------------------------------------------------|
| `|V_remed − V_tail| ≤ tol_E` AND class(V_remed) == class(V_tail)  | WARRANT upgraded to VALID with V_remed               |
| `|V_remed − V_tail| > tol_E` AND class(V_remed) == class(V_tail)  | WARRANT upgraded to VALID-with-documented-drift; S+1 audit item opened |
| class(V_remed) ≠ class(V_tail)                                    | Prior iteration sequence was masking a real bug; WARRANT stays INVALID; full re-scrub required |

---

## 7. Workshop-Outcome Rule (R_c metric)

For audit-workshops using this template, workshop closure is determined by the convergence ratio:

```
R_c = (N_converged + 0.5·N_partial + N_emerged) / N_topics
```

| R_c range          | Workshop status                                       |
|:-------------------|:------------------------------------------------------|
| `R_c ≥ 0.80`       | CLOSED — carry-forward items proceed to session plan  |
| `0.50 ≤ R_c < 0.80`| EXTENDED — one additional round authorized            |
| `R_c < 0.50`       | ESCALATED — 3-agent workshop required                 |

Topic counts (`N_topics`, `N_converged`, `N_partial`, `N_dissent`, `N_emerged`) must be tabulated in the workshop wrap-up before R_c is computed.

---

## 8. First-Invocation Discipline

The first use of this template after adoption is itself subject to audit. The next audit-workshop to invoke the template MUST:

1. Apply the template verbatim (no ad-hoc additions to tag vocabulary, severity grading, or decision rule).
2. Record any point where the template was silent or ambiguous in the workshop's §VII open items.
3. Trigger a **meta-audit item** in the session handoff that evaluates whether the template was self-sufficient. If meta-audit finds gaps, the template is revised BEFORE the third invocation.

This prevents recursive PRU: a template that eliminates PRU in audits is itself PRU-vulnerable at its first use. The first-invocation discipline terminates the recursion cleanly.

---

## 9. Verdict-Log Requirements

For this template to be applicable, each iteration in a gate's verdict-log must record:

- `iteration_index` (1-based)
- `verdict_class` ∈ {PASS, FAIL, INFO, INCOMPUTABLE}
- `observable_value` (e.g., F_amp, relative disagreement %)
- `tag` (one of the 8; `verdict-class-transition` is a separate flag column)
- `severity` ∈ {HIGH, MEDIUM, LOW}
- `commit_sha` of the producing script at verdict-stamp time
- `content_hash_triple` = (script_sha, canonical_constants_sha, input_data_sha)

Logs missing any of these fields for any iteration are automatically CONDITIONAL or INVALID under §5's cascade-compliance test.

---

## Cross-references

- `epistemic-discipline.md` — Pre-Registration Completeness (PRU definition, §0.11 machinery-enumeration)
- `gate-verdicts.md` — no-retroactive-change rule; verdict-class definitions
- `output-standards.md` — handoff 7-section format
- Session-plan template §0.10 (INCOMPUTABLE ≠ FAIL) and §0.10(b) (iteration-cap clause)
