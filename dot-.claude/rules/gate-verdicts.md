---
paths:
  - "computations/session-*/**"
  - "computations/investigation-*/**"
  - "computations/_shared/**"
  - "sessions/session-plan/**"
  - "sessions/investigation/**"
---

# Gate Verdict Standards

## Canonical Verdict-File Path (MANDATORY)

The ONE canonical location for every session's verdict file is:

```
computations/session-{N}/s{N}_gate_verdicts.txt
```

where `{N}` is the session number.

- Agents MUST append their verdict line to this path and no other.
- The variants `computations/_shared/s{N}_gate_verdicts.txt`, `sessions/session-{N}/s{N}_gate_verdicts.txt`, and `sessions/session-plan/s{N}_gate_verdicts.txt` are FORBIDDEN. If a plan document, rule file, or working-paper names any of these variants, treat it as a documentation bug and write to `computations/session-{N}/` anyway.
- When plan text is ambiguous (bare `s{N}_gate_verdicts.txt` with no directory prefix, as in many legacy plans), resolve to `computations/session-{N}/` by this rule.
- Rationale: `computations/session-{N}/s{N}_gate_verdicts.txt` is the file `/weave --update`, `_consolidate_t3_intake.py`, and downstream audit scripts grep. A verdict written elsewhere is an auditing blind spot. The per-session directory keeps each session's verdict log co-located with its scripts and data files; the prior `_shared/` convention created cross-session pile-up and made verdict-file scoping ambiguous.

## Investigation-Track Canonical Path

The **investigation pipeline** (`sessions/investigation/`, the parallel exploratory track driven by `/rclab-plan --investigation`, executed by `/rclab-coordinate`, analyzed by `/rclab-investigate`) carries its own verdict ledger, structurally mirroring the session track:

```
computations/investigation-{n}/inv{n}_gate_verdicts.txt
```

where `{n}` is the investigation number.

- Emit via `emit_verdict(session={n}, track="investigation", ...)`. The tool resolves and writes the `inv{n}` path; the `track` argument is the ONLY difference from a session emission. ALL other discipline (dual-SHA, sig_5 uniqueness, `supersedes=` Option-A correction, absolute verdict permanence, the canonical line grammar) applies IDENTICALLY across tracks — the tool enforces them track-agnostically.
- **Only `gate_type: compute` gates emit a verdict line.** `gate_type: review` and `gate_type: workshop` gates close by **artifact-existence-with-content** (their deliverable is a markdown synthesis / workshop document, not a numerical verdict) — they have NO verdict-file line, the same closure semantic as a METHODOLOGY-class wave per `.claude/rules/wave-classification.md §M1`. See the `gate_type` field in `.claude/templates/r3-yaml-gate-block.yaml`.
- The `s{N}_`/`inv{n}_` prefixes and `session-`/`investigation-` directory names are FORBIDDEN to cross: a session verdict never lands under `computations/investigation-*/` and vice versa. When investigation plan text is ambiguous (bare `gate_verdicts.txt`), resolve to `computations/investigation-{n}/inv{n}_gate_verdicts.txt` by this rule.
- **Track-local boundary (intentional)**: investigation verdict files under `computations/investigation-*/` are NOT swept by the session-scoped `/weave --update` extractor or `_consolidate_t3_intake.py` (both glob `computations/session-*/`). An investigation result enters the knowledge index only when it is *promoted into a session* — i.e., lifted as a carry-forward into a `/rclab-plan` session-mode plan and re-computed under a `session-{N}` gate. Investigations are an exploratory track that feeds the session pipeline; they are not themselves a permanent-results ledger. A result that must be permanent is migrated, not merely cited.

## Race-Safe Emission via the `emit_verdict` knowledge-MCP tool

The canonical MECHANISM for appending a verdict line is the knowledge-MCP tool
`emit_verdict` (server `knowledge`). It is the race-safe, syntax-forced replacement
for open-coded `append_verdict()` file writes in producing scripts.

**Why**: a raw `open(path, "a")` append is NOT atomic across processes on Windows.
Under concurrent writers it loses updates — a later writer's buffered flush can land at
a stale end-of-file offset and overwrite lines appended in between. `emit_verdict`
serializes every write behind a cross-process `O_EXCL` lockfile (portable Win+POSIX) and
enforces the line grammar, so the race cannot arise.

**Division of labor**: the producing script computes the two SHAs (only it holds the
input-pin map and the content target) plus the value payload; the agent then calls
`emit_verdict` with those values. The tool owns everything else — it forces the canonical
grammar, serializes the append, and rejects malformed or duplicate emissions.

**What the tool enforces (syntax-forced)**:
- `verdict ∈ {PASS, FAIL, INFO, PRE-REG-INC}` (enum).
- `audit_sha256` / `content_sha256` are full 64-char lowercase hex (truncated SHAs are unrepresentable).
- the `[SIGN]` 3-tuple (`sign_verdict` / `magnitude_verdict` / `regime_verdict`) is an
  all-three-or-none group — a partial 3-tuple is rejected.
- **sig_5 at write-time**: a reused `audit_sha256` (the copy-pasted-SHA bug) is rejected; a
  second canonical line for a gate that already has one is rejected UNLESS a
  `supersedes=<old 64-hex audit_sha256>` token is supplied (the Option-A correction path).
- the value payload may not contain the `'` value-delimiter character.

**Idempotent**: re-calling with the same `(gate_id, audit_sha256)` is a NO-OP, not a
duplicate line. **Canonical path**: the tool resolves and writes
`computations/session-{N}/s{N}_gate_verdicts.txt` from its `session` argument — the exact
path the section above mandates. Optional `extra_rows` (each `#`-prefixed) carry per-gate
companion annotations (EMERGENCE-1 detail, `regulator_pin`, etc.).

The producing-script workflow IS migrated to this path: `.claude/templates/script-template.py`
provides `print_verdict_payload` (the script prints the payload, never writes the verdict file),
and the `rclab-*` dispatch prompts instruct the agent to call `emit_verdict`. A producing script
that still open-codes a verdict-file `open("a")` append is non-compliant and MUST be migrated; if
a legacy script genuinely cannot be migrated before dispatch, serialize the verdict-emitting gates
(one writer at a time) as the interim guard.

## Pre-Registration Protocol

1. **Before computation**: Define the gate in `sessions/session-plan/` with the
   full block required by plan §4.5 of `script-review-plan.md` (see the
   PRU template at `.claude/templates/pru-pre-registration-template.md` for the
   scaffold). Every gate block MUST include:
   - **Gate ID** (e.g., `V-1`, `M-3`, `T3-<SCRIPT>`)
   - **Trigger**: `[SIGN]`, `[VERIFY]`, `[AUDIT]`, `[VERIFY-THEOREM]`, or `[CHAIN]`
   - **Classification**: PHONONIC | GEOMETRIC | PARTICLE | NON-PHONONIC
   - **Hypothesis being tested** (one sentence)
   - **Pass/fail/INFO threshold** — quantitative, with RATIO/ABSOLUTE/THEOREM
     tolerance rule stated explicitly
   - **Machinery pin (PRDR)**: `N_eval`, `L_max`, `scan_range`, `step_size`,
     `tolerance`, `scheme`, `convention`, `random_seed`, `GPU path`. A gate that
     leaves any of these unpinned is PRU-vulnerable (Class 8 failure; see
     `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness).
   - **Input SHA-256 pins** for every file the script reads (static files get
     precomputed hashes; dynamic inputs are marked `<computed-at-runtime>`).
   - **Expected output 4-tuple**: `(value=<v>, scheme=<s>, convention=<c>, L_max=<L>)`
   - **Substitution chain**: required for any sign/direction/threshold claim,
     per `.claude/rules/math-scripts.md` §Double-Check Logic Before Compute.
   - **What PASSES and what FAILS mean** for the solution space (the boundary
     the gate maps, not rhetoric)

2. **During computation**: Run the script, record raw numerical output. The
   script MUST log the SHA-256 of every input in the first 20 lines of stdout
   and emit the closure hash. The 4-tuple output tag is printed as the final
   non-verdict line.

3. **After computation**: Compare output to pre-registered threshold. Append a
   single verdict line to `computations/session-{N}/s{N}_gate_verdicts.txt` (see
   "Canonical Verdict-File Path" above):
   ```
   {GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
   ```
   The SHA-256 pin is MANDATORY for all new verdicts.

## Verdict Format

Legacy verdict blocks in plan/handoff docs remain valid in this form:

```
Gate {{GATE_ID}}: {{PASSED|FAILED}}
  Threshold: {{CRITERION}}
  Computed:  {{VALUE}}
  Verdict:   {{PASS/FAIL with brief explanation}}
```

**Canonical form** (required in `computations/session-{N}/s{N}_gate_verdicts.txt`):

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
```

The closure SHA is the SHA-256 of the ordered input-pin map (see the new-script
template at `.claude/templates/script-template.py`, Section 4).

## Schema-v2 canonical form (extends the SHA-pinned form; backward-compatible)

The canonical verdict line is unchanged:

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
```

The dual-SHA companion comment row is unchanged:

```
# audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # {GATE_ID} dual-SHA companion row
```

NEW optional-but-required-for-`[SIGN]`-trigger gates: a SECOND companion row
carrying the SIGN/MAGNITUDE/REGIME 3-tuple annotation. The annotation is REQUIRED
for any gate whose pre-registration includes a `[SIGN]` trigger or whose
substitution chain pre-registers a directional prediction:

```
# sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # {GATE_ID} 3-tuple annotation (schema-v2)
```

### Field semantics

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

### Composite-collapse rule (PRE-REGISTERED — modifications are Class-3 violations)

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

Modifying this collapse rule after seeing a verdict is a Class-3 PROHIBITED_ACTIONS
violation (post-hoc pre-registration editing) per `.claude/rules/v3-closure-recovery.md`.

#### Plan-frozen gate-block operator precedence (applicability guards)

When a gate's plan-frozen R3 gate-block operator pre-registers a composite semantic that conflicts with the generic collapse rule above, the PLAN-FROZEN operator takes precedence — PROVIDED the producing gate emits a mandatory pre-declared disclosure extra-row (a `# composite-precedence:` companion row naming the plan anchor and the generic-collapse reading being overridden), DECLARED in the plan BEFORE evaluation. Structural gap this closes: applicability GUARDS (INFO-on-inapplicability as a first-class outcome) have no axis in the 3-tuple — `regime=BREAKDOWN` is the nearest encoding but forces `composite=FAIL`, which is wrong: applicability is a guard, not the hypothesis. This clause COMPOSES WITH the collapse rule; it does not modify it — the generic collapse remains the default for every gate whose plan block does not pre-register a conflicting operator, and a precedence invocation WITHOUT the pre-declared extra-row is a Class-3 boundary violation (post-hoc semantics editing) per `.claude/rules/v3-closure-recovery.md`. **Status**: SUGGESTION (K=1; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`). Calibration corpus: `sessions/framework/registry/pru-class-corpus.md` (plan-frozen-operator precedence section; the CORE-vs-fringe override clause at §19 is the ADJACENT prior on a DIFFERENT axis — it overrides a sign=FAIL label via four guards at the gate-semantic layer; this clause governs operator-vs-generic-collapse precedence at the plan-freeze layer; both compose with, neither modifies, the collapse rule).

### Auto-shortening clause discipline (cross-checks with runtime-pinned domain)

A cross-check is **auto-shortening** if its test domain is computed as
`min(D_intended, D_runtime)` where `D_runtime` is a function of a runtime-pinned
canonical, an ODE-breakdown threshold, a numerical stability bound, or any other
quantity whose value is not fixed at plan-freeze.

For every auto-shortening cross-check, the producing script MUST:

1. Compute `f_used = D_actual / D_intended` (the fraction of the intended window
   actually tested).
2. Emit `f_used` in the JSON sidecar AND in the verdict line as `domain_used_frac=<f>`.
3. Set `regime_verdict` per the pre-registered band:

| `f_used` band | `regime_verdict` | Composite collapse |
|:--|:--|:--|
| ≥ 0.95 (≤5% shortened) | VALID | unaffected |
| 0.50 ≤ f_used < 0.95 (5–50% shortened) | MARGINAL | `magnitude_verdict=PASS+regime=MARGINAL ⇒ composite INFO` |
| f_used < 0.50 (>50% shortened) | BREAKDOWN | `regime=BREAKDOWN ⇒ composite FAIL` regardless of other fields |

4. Either (a) define the cross-check on the full intended domain UNCONDITIONALLY
   (no auto-shortening — the cross-check FAILS if the domain breaks down), OR
   (b) emit `regime_verdict = MARGINAL or BREAKDOWN` (not VALID) when the
   auto-shortening clause activates.

Option (a) is the structural-integrity choice; option (b) preserves the
cross-check's diagnostic value when the regime breakdown is the gate's primary
substrate-physics finding.

The 5/50% pin matches the SOURCE-RECONCILIATION 4-band calibration in
`.claude/rules/epistemic-discipline.md` at the linear-fraction analog of the
log-OOM bands.

### Worked example — `S{N}-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55`

Existing canonical line:
```
S{N}-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55: FAIL -- value='1.435284' scheme=SR-LO-Mukhanov-Sasaki convention=substrate-first-xi2(0)-IC L_max=10 audit_sha256=... content_sha256=... schema_version=S84+
```

Schema-v2 SECOND companion row:
```
# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN # S{N}-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55 3-tuple annotation (schema-v2)
```

- `sign_verdict = PASS`: §10 pre-registered `Z_ratio > 1`; computed value 1.4353 > 1; direction matches.
- `magnitude_verdict = FAIL`: `|Z_ratio − 1| = 0.4353 ≫ 0.10` info-band ceiling.
- `regime_verdict = BREAKDOWN`: SR-LO ε ≪ 1 truncation breaks at N_breakdown = 0.13 e-folds = 0.236% of intended N=55.
- Composite under collapse rule: `regime_verdict == BREAKDOWN ⇒ composite = FAIL` — preserves the existing FAIL top-line, but pins the SIGN-PASS sub-result for downstream re-derivation.

## Rules

- Gate criteria are defined BEFORE computation — never after seeing results
- Verdicts are permanent — no retroactive changes (see §"Option A — sig_5 remediation pathway under absolute verdict permanence" below for the unified policy text)
- Only the Skeptic evaluates whether a gate verdict is meaningful
- Record verdicts in the session file AND update knowledge index via `/weave --update`
- Canonical verdict lines MUST carry the `sha256=<closure>` pin (per plan §4).
  **The closure SHA MUST be the full 64-character hexdigest** — never a
  head-truncated prefix. `computations/_shared/_consolidate_t3_intake.py`
  rejects verdict lines with SHAs shorter than 40 hex chars. The 16-char
  head form is allowed in the prose sections of the verdict file for
  human scan-readability, but NEVER in the first canonical line.
- A gate that cannot be evaluated because its producing machinery is unpinned
  (PRU Class 8) is NOT a FAIL — it is PRE-REG-INCOMPLETE. Pin the machinery
  via PRDR (Pre-Registration Dry-Run, `.claude/rules/epistemic-discipline.md`)
  before marking PASS/FAIL.

### Option A — sig_5 remediation pathway under absolute verdict permanence

This sub-section IS the unified policy text resolving the collision between the "verdicts are permanent" rule (this file) and the sig_5 SHA-uniqueness remediation prescription at `.claude/rules/v3-closure-recovery.md §"Stage 1: Automatic re-dispatch"` sig_5 sub-section; both rule-files cross-link to this anchor.

When `v3-closure-recovery.md` sig_5 detects duplicate `audit_sha256` across verdict lines, OR when a producing script emits a corrective verdict line after a prior FAIL/INFO emission for any of the following structural reasons:

- **rubric calibration**: the verifier rubric returned FAIL/INFO on an intermediate emission and the producing script's corrective branch re-runs the verifier after applying a deterministic correction (Class-8.2 PRU verifier-rubric pre-registration boundary)
- **script-bug fix**: the producing script's emission logic had a bug (mis-counted lines, malformed regex, stale section pointer) and the corrective branch emits the corrected line
- **SHA-hardcoding bug fix**: the producing script was emitting a copy-pasted literal `audit_sha256` rather than computing the closure from the input-pin map
- **any other in-script correction emitted within the same dispatch**

the policy under absolute verdict permanence (Option A; user-adjudicated) is:

1. **Original verdict line is RETAINED on disk.** The original line is never overwritten, deleted, or edited in-place. Verdict permanence is absolute at the byte level on `s{N}_gate_verdicts.txt`.
2. **Corrective verdict line is APPENDED with `supersedes=<old_audit_sha>` tag.** The corrective canonical line carries a `supersedes=<full-64-char-old-audit-sha>` token in its `value=` field OR in the dual-SHA companion comment row, naming the original audit_sha256 the corrective line replaces in the audit-trail-canonical reading.
3. **Downstream consumers cite the LATEST NON-SUPERSEDED line as canonical.** Orchestrators, audit scripts, `/weave --update`, `_consolidate_intake.py`, and any other tool that resolves a gate's canonical verdict MUST follow the supersession chain: scan all canonical lines for the gate-ID, identify each line that is named in another line's `supersedes=` token, exclude those superseded lines from the canonical reading, and treat the latest non-superseded line as authoritative.
4. **Audit trail is preserved by construction.** The chain `original FAIL/INFO → corrective PASS (with supersedes tag)` is queryable via `grep` on the verdict file; the `supersedes` tag is the authoritative pointer between an original and its corrective.
5. **Forward emission discipline.** Every corrective verdict line MUST carry the `supersedes` tag at emission time. A corrective line that does NOT carry the tag is a Class-8.2 PRU pre-registration violation per `.claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` AND a v3-closure-recovery.md PROHIBITED_ACTIONS Class-3 boundary risk (post-hoc audit-trail editing if the tag is added later).
6. **Retroactive canonicalization for legacy corrective emissions.** Corrective emissions predating this protocol (no `supersedes` tag at emission time) are retroactively canonicalized under the "latest non-superseded" rule with the LATEST PASS line as canonical and the prior FAIL/INFO line as superseded. NO retroactive disk-edit of those lines is performed (verdict permanence prevails); the supersession chain is reconstructed at consumer-read time via gate-ID grouping.

#### Retroactively-canonicalized corrective emissions

Corrective-emission instances predating this protocol (a prior FAIL/INFO line and a later corrective PASS line for the same gate-ID, emitted with no `supersedes` tag) are canonicalized under rule (6): the LATEST PASS line per gate-ID is canonical, the prior line(s) superseded, with NO retroactive disk-edit (verdict permanence prevails). The supersession chain for any such gate is reconstructed at consumer-read time by grouping canonical lines by gate-ID in the session's `s{N}_gate_verdicts.txt`. Forward consumers MUST adopt the supersession-chain reading discipline.

#### Cross-link

See `.claude/rules/v3-closure-recovery.md §"Stage 1: Automatic re-dispatch"` sig_5 sub-section for the recovery-side complement: the sig_5 remediation prescription (re-run script, append new canonical line) is preserved INTACT, and the appended line MUST carry the `supersedes=<old_audit_sha>` tag per this Option A protocol.
