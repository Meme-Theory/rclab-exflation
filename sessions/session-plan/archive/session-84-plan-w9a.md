# Session 84 Plan — Wave 9a: Methodology V3 Closure (8 items)

**Session**: 84
**Wave**: 9a
**Theme**: Methodology v3 closure — PRU-audit tool, hook infrastructure, dual-SHA schema, R3 YAML template, canonical archival, ARTIFACTS PROMISED auto-generation, critical-path auto-detection, recovery-procedure specification.
**Planner**: gen-physicist
**Format**: compute (parallel independent agents, all single-agent meta-gates)
**Item count**: 8 (rows 97-104 from §4.J of `session-84-context.md`)
**All items classified**: NON-PHONONIC (methodology gates on tool / hook / plan-template implementation)
**All items dispatched to**: `gen-physicist` (meta-gates on infrastructure; no physics derivation)

---

## W9a Summary

Wave 9a is the infrastructure-closure half of the S84 methodology-debts-v3 campaign
pre-registered in S83. The 8 items here implement the *code and process* layer of
v3 closure: the PRU cardinality audit tool (sig_1 ladder-weight 4.000), the post-agent +
post-session hook infrastructure (sig_3 weight 3.750), the dual-SHA schema split
(sig_2 weight 1.585), the R3 YAML gate template (sig_4 weight 1.000), canonical
archival at session close, ARTIFACTS PROMISED auto-generation, critical-path
auto-detection, and the post-hook-failure recovery-procedure specification.

**Ladder recap** (S83 methodology-debts workshop):

| sig | weight | description |
|:----|:------:|:------------|
| sig_1 | 4.000 | PRU audit tool presence (BLOCKING veto if missing) |
| sig_2 | 1.585 | dual-SHA schema presence (audit_sha256 + content_sha256) |
| sig_3 | 3.750 | hook fire-log evidence (per-agent + per-session) |
| sig_4 | 1.000 | R3 YAML gate template adoption |
| sig_5 | 1.000 | audit_sha256 uniqueness across session |
| **total** | **11.335** | |

CLOSED threshold: >= 10.202 (90%). INFO: >= 6.801 (60%). FAIL: < 6.801 or sig_1 missing.

The **sig_1 veto** is what makes W9a-97 (PRU-TOOL) the prerequisite for every
other methodology closure signal: without the tool, the other four signals can
all PASS and the ladder still fails. Item 97 is therefore the critical-path head.

**Companion wave**: W9b (items 105-124 or equivalent methodology-overlap items)
runs in parallel once W9a-97, W9a-98, and W9a-99 are on-disk and green. See
`session-84-plan-w9b.md` for the companion items.

**PRU recurrence rate** (S83, empirical baseline): 4 of 62 gates = **6.45%**.
S84 target: D_PRU_raw = 0 across all plan-freeze-time gates (driven to zero
by the audit tool at plan authorship, not at execution).

**Dual-SHA preimage entropy**: S82 G59 case established H(gate | SHA) closed
from 1.585 bits (log_2(3) — three candidate audit-relevant input sets reduce
to one once both audit_sha256 and content_sha256 are emitted).

---

## W9a Decision Point Prerequisites

Before any other W9a item can complete:

1. **W9a-97 (PRU-TOOL)** must ship `_pru_cardinality_audit.py` in
   `computations/`. Once present, W9a-103 (CRITPATH) extends it.
2. **W9a-98 (HOOK-INFRA)** must ship both shell scripts in `.claude/hooks/`
   and wire `completion-queue.jsonl` emission. Required before W9a-104
   (RECOVERY-SPEC) has a target to remediate.
3. **W9a-99 (SHA-SPLIT)** must update the script template AND deliver the
   backward-compat shim BEFORE the template is first used on S84 gate scripts.

All 8 items can be dispatched in parallel subject to the user's concurrent-cap
of ~8 agents (`feedback_dispatch-discipline.md`). With 8 items and the cap at 8,
the wave dispatches as a single parallel batch with no rolling backfill
(per `feedback_dispatch-discipline.md`).

---

## §W9a-97 — S84-W1-CF-PRU-TOOL

### Gate ID
`S84-W9A-97-PRU-TOOL`

### Trigger
`[VERIFY]` — PASS/FAIL within factor 3 of threshold; the threshold
here is **strict binary** (D_PRU_raw(g) in {0, 1}), so the verify
discipline applies to the tool's own determination.

### Classification
**NON-PHONONIC** (methodology / tooling)

### Agent type
`gen-physicist` (meta-gate on PRU audit tool implementation)

### Hypothesis
A Python tool operating statically on (plan YAML gate block, AST-parsed
producing script) can enumerate every free parameter in the script's
execution graph and determine whether every such parameter is pinned
in the gate block. Output is binary D_PRU_raw(g) and rank-valued
D_PRU_rank(g) for coupling-graph rank. The tool's correctness is
itself gated: PRU cardinality of every S84 gate (itself) must drive
to zero.

### Method
Create `computations/_pru_cardinality_audit.py` with the following
components:

1. **Gate-YAML parser** (reads R3 YAML block from `session-84-plan-w9a.md`
   and companion wave plans via the `yaml` std library). Expected keys:
   `gate_id`, `machinery_pin_map`, `input_files`, `audit_discriminators`,
   `strict_PASS_boundary`, `operator`, `boundary_reachable_analytically`.

2. **Python AST parser** (uses `ast.parse` on the producing script
   referenced in the gate block). Walks the AST to enumerate:
   - `ast.Assign` nodes at module scope whose target names are NOT in
     `canonical_constants.__all__` AND are NOT tagged `# (local)`.
   - `ast.Call` nodes to known stochastic RNG (e.g., `np.random.*`,
     `torch.rand*`) and iterator control parameters (`range(N)`,
     `scan_step`, `eps_tol`, `L_max`).
   - `scheme=` / `convention=` / `L_max=` literals passed to downstream
     functions.

3. **Free-parameter set F_script** = union of {AST-discovered unpinned
   module-scope assigns} U {RNG seeds} U {iterator controls} U {numerical
   literals in call-args not imported from canonical}.

4. **Pinned-parameter set P_gate** = keys declared in `machinery_pin_map`
   of the gate-YAML block.

5. **D_PRU_raw(g)** = **1 if F_script NOT-SUBSET-OF P_gate else 0**.
   Binary PASS/FAIL emission.

6. **D_PRU_rank(g)** = rank of the coupling graph G_F where vertices are
   F_script elements and edges connect parameters that appear together in
   an AST call-arg list. Computed via `np.linalg.matrix_rank` on the
   adjacency matrix (small matrix, CPU fine; for |F|>=100 switch to
   `torch.linalg.matrix_rank`).

7. **Output format** (stdout + JSON):
   ```
   gate_id: {g}
   D_PRU_raw: {0|1}
   D_PRU_rank: {int}
   unpinned_params: [list]
   pinned_params: [list]
   coupling_edges: [list of (p_i, p_j)]
   verdict: PASS | FAIL
   ```

8. **Self-audit**: The tool itself has a gate-YAML block in this plan
   (§W9a-97 above). Running the tool on its own plan entry must emit
   D_PRU_raw = 0.

### PRDR (Pre-Registration Dry-Run)
Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness.
Static enumeration of tool's own free parameters:

- `AST_MODULE_SCOPE_ONLY` (bool) — **PIN**: True (skip function-local).
- `RNG_CALL_WHITELIST` (list) — **PIN**: `["np.random", "torch.rand",
  "random.", "scipy.stats"]` (enumerated before tool authorship).
- `ITERATOR_CONTROL_REGEX` (regex) — **PIN**:
  `^(N|L_max|scan_step|eps_tol|n_eval|max_iter|tol)$`.
- `CANONICAL_IMPORT_MODULE` (str) — **PIN**: `canonical_constants`.
- `COUPLING_GRAPH_THRESHOLD_FOR_GPU` (int) — **PIN**: 100.
- `YAML_SCHEMA_VERSION` (str) — **PIN**: `"R3"` (the template from W9a-100).

All 6 parameters enumerated and pinned; D_PRU_raw(self) = 0 by construction.

### 4-tuple (value, scheme, convention, L_max)
- **value**: D_PRU_raw aggregated across all S84 wave-plans (integer 0 expected)
- **scheme**: `static-AST` (no execution, no sampling)
- **convention**: `R3-YAML-parse` (gate block schema)
- **L_max**: `plan-freeze-time` (pre-execution, not per-eigenvalue cutoff)

### PASS / FAIL / INFO
- **PASS**: sum_g D_PRU_raw(g) = 0 across every S84 gate block in every
  wave plan file (W1 through W9b) at plan-freeze time. Tool emits
  JSON report with zero unpinned-param entries.
- **FAIL**: any gate in any S84 wave plan has D_PRU_raw = 1 at
  plan-freeze. Remediation: add the missing pin to the gate's
  `machinery_pin_map`; re-run the tool; iterate to zero.
- **INFO**: D_PRU_raw = 0 but D_PRU_rank > 3 for any gate (high coupling).
  High-coupling parameter sets are structurally valid (pinned) but signal
  that the gate's machinery-sensitivity surface is multi-dimensional; the
  verdict remains PASS but the gate is flagged for substitution-chain
  audit in its synthesis.

### Substitution chain
Required per `.claude/rules/math-scripts.md` (this claim contains "less
than" and "greater than" thresholds).

```
Definition 1: F_script(s) = {p : p is a free parameter in the AST of script s}
Definition 2: P_gate(g)   = {p : p appears as a key in g.machinery_pin_map}
Definition 3: D_PRU_raw(g, s) = 1 if F_script(s) \ P_gate(g) is non-empty else 0

Substitute (Definition 3 into the gate-plan freeze condition):
  S84 plan CLOSED iff for all (g, s) in plan: D_PRU_raw(g, s) = 0
  iff for all (g, s): F_script(s) \ P_gate(g) = empty set
  iff for all (g, s): F_script(s) SUBSET-OF P_gate(g)

Canonical form:
  plan is PRU-closed <=> F_script(s) SUBSET-OF P_gate(g) for every pair

Direction: if F_script(s) contains p NOT in P_gate(g), D_PRU_raw = 1
           and the gate is PRU-vulnerable (Class 8 failure).

Conclusion: sum_g D_PRU_raw(g) = 0 is the NECESSARY and SUFFICIENT
condition for plan-level PRU closure, which is sig_1 of the v3 ladder
(weight 4.000, VETO posture).
```

### Meaning
**PASS maps**: the S84 plan has zero pre-registration underspecification;
every free parameter in every producing script is pinned in its gate
block; execution-time freedom has been driven to zero at plan authorship.
Region of solution space constrained: plan-level Class-8 failure mode
(S78 execution-property-failure taxonomy) is **closed** for S84.

**FAIL maps**: at least one gate leaves at least one machinery parameter
unpinned. Gate verdicts from such a gate are PRU-contaminated: a subsequent
script tweak that changes the unpinned parameter produces a different
verdict with identical audit_sha256 (since the pin-map didn't change).
Closure by pin-map amendment is fast (one YAML edit per missing parameter);
the iteration terminates at most in O(|F_script|) steps per gate.

**INFO maps**: high coupling rank is a diagnostic, not a closure problem.
Flagged gates receive substitution-chain audit in §VI of their syntheses.

### Effort
**Files created**:
- `computations/_pru_cardinality_audit.py` (~400 lines, std-lib only)
- `computations/tests/test_pru_cardinality_audit.py` (~150 lines)
- `computations/_pru_audit_report.json` (tool output, regenerated
  per plan-freeze)

**Time**: ~1.5 days implementation + 0.5 day self-audit.

### Substrate framing
Tool is NON-PHONONIC (methodology). It operates on plan YAML and Python
AST, not on D_K eigenvalues or spectral action gradients. Its purpose is
to ensure that every gate downstream (which DOES touch substrate physics)
has its producing machinery fully pinned before execution, so that verdicts
are audit-reproducible. The tool itself is infrastructure; the gates it
audits can be PHONONIC / GEOMETRIC / PARTICLE / NON-PHONONIC.

---

## §W9a-98 — S84-W1-CF-HOOK-INFRA

### Gate ID
`S84-W9A-98-HOOK-INFRA`

### Trigger
`[VERIFY]` — PASS/FAIL against binary hook-fire-log evidence.

### Classification
**NON-PHONONIC** (methodology / harness infrastructure)

### Agent type
`gen-physicist` (meta-gate on shell hook implementation + settings.json wiring)

### Hypothesis
Two shell hooks — `completion-verify.sh` (ADVISORY, per-dispatch) and
`v3-closure-audit.sh` (BLOCKING, per-session) — can be wired via
`~/.claude/settings.json` (PostToolUse + Stop events) such that every
Agent completion emits a line to `completion-queue.jsonl` and every
session close triggers a ladder check against the 5-signal v3 CLOSED
threshold (>= 10.202). The BLOCKING posture means a failing session-close
audit holds the `/handoff` skill until remediated.

### Method
Create or modify the following files:

1. **`.claude/hooks/post-agent/completion-verify.sh`** (NEW, ADVISORY):
   - Event: PostToolUse on `Agent` tool
   - Reads the Agent output's `output_file` JSONL
   - Extracts every `write-target` declared in the prompt (via regex
     on prompt text for `ARTIFACTS PROMISED` block — hooked to W9a-102)
   - For each write-target, runs `stat` (existence) + `wc -l` (length)
   - Appends one JSON line to
     `.claude/hooks/logs/completion-queue.jsonl`:
     ```json
     {"agent_id": "{id}", "gate_id": "{g}", "write_targets": [...],
      "existence_checks": [...], "length_checks": [...],
      "advisory_status": "GREEN|YELLOW|RED", "ts": "{iso}"}
     ```
   - Exits 0 regardless (ADVISORY — does not block anything)

2. **`.claude/hooks/post-session/v3-closure-audit.sh`** (NEW, BLOCKING):
   - Event: Stop (session close) OR explicit `/handoff` invocation
   - Reads `computations/s84_gate_verdicts.txt`
   - Reads `.claude/hooks/logs/completion-queue.jsonl` (from all
     dispatches this session)
   - Computes the 5 signals:
     - sig_1: does `computations/_pru_cardinality_audit.py` exist
       AND was it run against the S84 plan AND did it emit D_PRU_raw = 0?
     - sig_2: does every S84 verdict line carry both `audit_sha256=<>`
       AND `content_sha256=<>` (not legacy single-SHA)?
     - sig_3: is `completion-queue.jsonl` non-empty AND does it cover
       >= 80% of verdicts?
     - sig_4: does every S84 gate block in plan files carry R3 YAML
       schema_version "R3"?
     - sig_5: are all `audit_sha256` values unique across the session
       verdict file?
   - Ladder score = 4.000 * sig_1 + 1.585 * sig_2 + 3.750 * sig_3 +
     1.000 * sig_4 + 1.000 * sig_5
   - Verdict: CLOSED (>= 10.202), INFO (>= 6.801), FAIL (< 6.801 OR
     sig_1 = 0)
   - If verdict != CLOSED AND verdict != INFO: exit 1 (BLOCKING)
   - Writes `sessions/archive/session-84/v3_ladder_audit.json` with full breakdown

3. **`~/.claude/settings.json`** (EDIT via `update-config` skill):
   - PostToolUse hook: matches `Agent` tool, runs `completion-verify.sh`
   - Stop hook: runs `v3-closure-audit.sh` in session-directory context
   - Both hooks receive ENV: `CLAUDE_SESSION_ID`, `CLAUDE_PROJECT_ROOT`

4. **`.claude/hooks/logs/completion-queue.jsonl`** (auto-created by hook)

5. **`/handoff` skill trigger**: the handoff skill (at
   `.claude/skills/handoff/` if it exists, else created as
   pass-through) invokes `v3-closure-audit.sh` first and blocks on
   non-zero exit.

### PRDR
- `HOOK_LOG_DIR` — **PIN**: `.claude/hooks/logs/`
- `COMPLETION_QUEUE_FILENAME` — **PIN**: `completion-queue.jsonl`
- `LADDER_WEIGHT_VECTOR` — **PIN**: `[4.000, 1.585, 3.750, 1.000, 1.000]`
- `CLOSED_THRESHOLD` — **PIN**: `10.202`
- `INFO_THRESHOLD` — **PIN**: `6.801`
- `SIG_1_VETO` — **PIN**: `True` (sig_1 = 0 forces FAIL regardless of total)
- `HOOK_POSTURE_POST_AGENT` — **PIN**: `ADVISORY` (exit 0 always)
- `HOOK_POSTURE_POST_SESSION` — **PIN**: `BLOCKING` (exit 1 on non-CLOSED)

### 4-tuple
- **value**: ladder score (float) + verdict (CLOSED | INFO | FAIL)
- **scheme**: `weighted-ladder-v3`
- **convention**: `sig_1-veto`
- **L_max**: `session-close` (audit runs once per session)

### PASS / FAIL / INFO
- **PASS**: both hook files exist, are executable, are wired in
  `settings.json`, and a test invocation of the post-session hook
  against S84's (partial-at-write-time) verdict file emits a
  well-formed `v3_ladder_audit.json`. Completion-queue log populates
  during the session's normal dispatches.
- **FAIL**: a hook is missing, is not wired, or the test invocation
  does not produce the expected JSON structure. Additionally: if the
  BLOCKING hook does not actually block on a synthetic FAIL test
  (negative control: manually corrupt the verdict file to force
  sig_5 = 0, confirm hook exits 1).
- **INFO**: hooks are wired but completion-queue covers < 80% of
  verdicts (coverage diagnostic). sig_3 computation reduces but does
  not veto. Remediation: verify the PostToolUse matcher is active
  for the Agent tool specifically.

### Substitution chain
```
Definition 1: sig_i in {0, 1} indicator for signal i
Definition 2: w = [4.000, 1.585, 3.750, 1.000, 1.000] weight vector
Definition 3: score = sum_i w_i * sig_i

Substitute:
  score_max = sum_i w_i = 4.000 + 1.585 + 3.750 + 1.000 + 1.000 = 11.335
  CLOSED_threshold = 0.9 * score_max = 10.2015 ~ 10.202 (rounded)
  INFO_threshold = 0.6 * score_max = 6.801

Simplify:
  CLOSED iff score >= 10.202 AND sig_1 = 1
  INFO   iff 6.801 <= score < 10.202 AND sig_1 = 1
  FAIL   iff score < 6.801 OR sig_1 = 0

Direction: sig_1 = 0 forces FAIL independent of score
  because sig_1 is the PRU audit and without it, all other
  signals can be gamed by an unpinned producing script.

Conclusion: sig_1 carries VETO posture at ladder evaluation time.
```

### Meaning
**PASS**: session-close discipline is enforced by the harness, not by
orchestrator vigilance. The S82 failure mode (observed in multiple
subagent dispatches: "verdict appended, working-paper section skipped")
is caught by completion-verify.sh within milliseconds of the Agent
tool returning. The BLOCKING post-session hook prevents `/handoff`
from succeeding until the 5-signal ladder meets CLOSED or INFO.

**FAIL**: session-close can proceed silently with incomplete v3 closure
(the S82-state-of-the-world). Orchestrator-only discipline has been
empirically insufficient (S82 agent-standards.md observed failure
mode). Remediation: repair hook wiring; re-run.

**INFO**: hooks fire but instrumentation is partial. Gate verdicts
remain valid; the ladder signals are soft-reduced.

### Effort
- `.claude/hooks/post-agent/completion-verify.sh` (~120 lines bash)
- `.claude/hooks/post-session/v3-closure-audit.sh` (~200 lines bash +
  `jq` JSON computation)
- `settings.json` hook-wiring edit (~20 lines JSON)
- Handoff-skill trigger (~30 lines if `.claude/skills/handoff/SKILL.md`
  exists; pass-through creation if not)
- Test fixtures: 1 synthetic verdict file + 1 synthetic completion-queue
  line for smoke-test

**Time**: ~2 days implementation + 0.5 day smoke-test.

### Substrate framing
NON-PHONONIC. Hooks operate on session file state (text, JSON, JSONL),
not on D_K eigenvalues or spectral content. Their purpose is to make
the v3 ladder a harness-enforced discipline, freeing the orchestrator
from per-dispatch artifact verification.

---

## §W9a-99 — S84-W1-CF-SHA-SPLIT

### Gate ID
`S84-W9A-99-SHA-SPLIT`

### Trigger
`[VERIFY]` — PASS/FAIL on template + shim correctness.

### Classification
**NON-PHONONIC** (methodology / SHA schema)

### Agent type
`gen-physicist` (meta-gate on script template + consolidator shim)

### Hypothesis
Splitting the single verdict-line SHA into two — `audit_sha256`
(script + canonical_constants + input-pin map) and `content_sha256`
(script file byte-content only) — resolves the S82 G59 ambiguity
(H(gate | SHA) = 1.585 bits of pre-image entropy when three candidate
input sets compute to the same single SHA). A backward-compat shim
in `_consolidate_intake.py` reads legacy single-SHA lines and
promotes them to audit_sha256-only (content_sha256 = "LEGACY-PRE-S84").

### Method
Edit or create:

1. **`computations/script-template.py`** (EDIT; see
   `.claude/templates/script-template.py` if that is the actual
   path):
   - Update Section 4 (SHA emission) to compute BOTH hashes
   - `audit_sha256 = sha256(script_path_bytes + canonical_constants_bytes
      + input_pin_map_json_bytes)`
   - `content_sha256 = sha256(script_path_bytes)` — script file only
   - Verdict-line emission format upgraded to:
     ```
     {GATE}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L>
       audit_sha256=<64> content_sha256=<64> schema_version=S84+
     ```
   - Legacy single `sha256=<>` form REMOVED from the S84+ template
     (still accepted by consolidator via shim)

2. **`computations/_consolidate_intake.py`** (EDIT):
   - Detect `schema_version=S84+` in verdict line (presence of
     BOTH keys); parse dual SHAs into record
   - Detect legacy (S81-S83) form with single `sha256=<>`; set
     `audit_sha256 = <legacy>` AND `content_sha256 = "LEGACY-PRE-S84"`
   - Reject malformed verdict lines (missing both `audit_sha256` and
     `sha256=`)
   - Emit warning (not error) on `content_sha256 = LEGACY-PRE-S84`
     — pre-S84 verdicts remain valid, just flagged as
     audit-schema-shallow

3. **`computations/_sha_split_demo.py`** (NEW, demo):
   - Run the new template on a trivial computation
   - Print both SHAs
   - Verify: same script + different canonical_constants_s84_frozen.py
     yields same content_sha256 but DIFFERENT audit_sha256
   - Verify: different script + same canonical + same inputs yields
     DIFFERENT content_sha256 AND DIFFERENT audit_sha256

4. **`computations/tests/test_sha_split.py`** (NEW):
   - Positive test: new-template script produces well-formed dual-SHA
     verdict line
   - Negative test: corrupting the pin-map changes audit_sha256 but
     NOT content_sha256
   - Negative test: corrupting a line in the script changes BOTH
   - Shim test: legacy S83 verdict line parses with
     `content_sha256 = LEGACY-PRE-S84`
   - Shim test: malformed line (missing both SHA forms) raises

### PRDR
- `AUDIT_SHA_INPUTS` — **PIN**: `script_bytes + canonical_bytes +
  pinmap_json_bytes`
- `CONTENT_SHA_INPUTS` — **PIN**: `script_bytes`
- `HASH_ALGORITHM` — **PIN**: `sha256` (no truncation in canonical line)
- `LEGACY_MARKER` — **PIN**: `"LEGACY-PRE-S84"` (content_sha256 value for
  pre-S84 verdicts)
- `SCHEMA_VERSION_TAG` — **PIN**: `"S84+"` (present as key in the new
  template, absent in legacy)

### 4-tuple
- **value**: count of S84 verdicts with both SHA fields present
- **scheme**: `dual-SHA`
- **convention**: `audit-and-content` split
- **L_max**: `per-verdict-line` (verdict-file scope)

### PASS / FAIL / INFO
- **PASS**: template emits both SHAs; shim reads both legacy and S84+
  forms without error; demo script shows expected differential
  sensitivity (canonical change flips audit but not content SHA);
  all 4 test fixtures pass.
- **FAIL**: template cannot emit both SHAs; shim rejects legacy forms
  (breaking S83 verdict intake); differential sensitivity test fails
  (content_sha256 responds to canonical changes, indicating the
  script-vs-canonical separation is not actually implemented).
- **INFO**: template emits both SHAs but the demo reveals a third
  hash-relevant input not captured (e.g., the Python interpreter
  version). Flagged for hash-input-set enumeration audit in a
  subsequent session.

### Substitution chain
```
Definition 1: audit_SHA(g) = sha256( bytes(script) || bytes(canonical) ||
                                     bytes(pinmap_JSON) )
Definition 2: content_SHA(g) = sha256( bytes(script) )
Definition 3: H(gate | SHA) = log_2 | pre-image set | (entropy in bits)

Substitute (S82 G59 observed case with single SHA):
  H(gate | single_SHA) = log_2(3) = 1.585 bits
  (three candidate input sets collapsed to one SHA)

With dual SHA:
  audit_SHA distinguishes by (canonical, pinmap) variation
  content_SHA distinguishes by (script) variation
  Joint pre-image set size <= 1 when both SHAs match

Canonical form:
  H(gate | (audit_SHA, content_SHA)) = 0 bits
  provided hash collisions are negligible (SHA-256 collision prob ~ 2^{-128})

Direction: moving from single-SHA to dual-SHA reduces audit-preimage
  entropy from 1.585 bits to 0 bits.

Conclusion: sig_2 (dual-SHA presence, weight 1.585) measures precisely
  this entropy reduction and is quantitatively calibrated to the S82
  G59 case — fully closing the ambiguity is worth 1.585 on the ladder.
```

### Meaning
**PASS**: S82 G59-class audit ambiguity (1.585 bits of entropy per
gate) is closed for all S84+ verdicts. Legacy verdicts (S81-S83)
retain their audit_sha256 under the LEGACY-PRE-S84 content marker;
they remain valid evidence but are flagged as audit-shallow.

**FAIL**: verdict files continue to carry single-SHA ambiguity; at
least one S84 gate will have a pre-image set of size > 1 with
non-trivial probability.

**INFO**: the partition is incomplete — a third input axis (Python
interpreter version, numpy/torch version) is unaccounted-for.
Remediation: add env_sha256 in a future session, not urgent for S84.

### Effort
- `script-template.py` edit: ~40 lines
- `_consolidate_intake.py` shim: ~30 lines (format detection + parsing)
- `_sha_split_demo.py` (new): ~80 lines
- `tests/test_sha_split.py`: ~120 lines

**Time**: ~1 day implementation + 0.25 day test validation.

### Substrate framing
NON-PHONONIC. SHA schema is harness-level; no substrate content.
Its closure is prerequisite for sig_2 of the v3 ladder.

---

## §W9a-100 — S84-W1-CF-PRDR-TEMPLATE

### Gate ID
`S84-W9A-100-PRDR-TEMPLATE`

### Trigger
`[VERIFY]` — PASS/FAIL on template adoption in every S84 gate block.

### Classification
**NON-PHONONIC** (methodology / plan template)

### Agent type
`gen-physicist` (meta-gate on YAML template implementation + plan
authorship discipline)

### Hypothesis
An R3 YAML gate-block template with an 8-item machinery-enumeration
checklist — if adopted by every S84 gate in every wave plan — captures
every free parameter before it becomes PRU-vulnerable at execution
time. The 8 checklist items are: operator, strict_PASS_boundary,
boundary_reachable_analytically, reachable_rationals, machinery_pin_map,
audit_discriminators, substitution_chain, input_files.

### Method
Create or edit:

1. **`.claude/templates/r3-yaml-gate-block.yaml`** (NEW, canonical
   template):
   ```yaml
   # R3 YAML Gate Block Template (S84+)
   gate_id: "{WAVE}-{INDEX}-{SLUG}"
   schema_version: "R3"
   trigger: "[SIGN|VERIFY|AUDIT|CHAIN|VERIFY-THEOREM]"
   classification: "[PHONONIC|GEOMETRIC|PARTICLE|NON-PHONONIC]"
   agent_type: "<agent-name>"
   hypothesis: "<one-sentence>"

   method:
     description: "<specific script / test procedure>"
     producing_script: "computations/<path>.py"

   # PRDR Checklist (8 items) — ALL required
   operator:
     type: "[equality|inequality|ratio|span|etc.]"
     form: "<mathematical form of the comparison>"

   strict_PASS_boundary:
     value: "<exact threshold number or expression>"
     direction: "[<=|>=|=|!=]"

   boundary_reachable_analytically:
     bool: true
     proof_ref: "<path to analytic derivation or 'null'>"

   reachable_rationals:
     includes_integer_mesh: true
     mesh_density: "<N points or 'continuous'>"

   machinery_pin_map:
     <param_name>: "<pinned value or scan>"
     # enumerate every free parameter from producing_script AST
     # must satisfy D_PRU_raw = 0 under _pru_cardinality_audit.py

   audit_discriminators:
     audit_sha256_inputs: ["script", "canonical", "pinmap"]
     content_sha256_inputs: ["script"]

   substitution_chain:
     required: true
     content: |
       Definition 1: ...
       Definition 2: ...
       Substitute: ...
       Canonical form: ...
       Direction: ...
       Conclusion: ...

   input_files:
     <logical_name>:
       path: "<relative path>"
       sha256: "<precomputed hash or '<computed-at-runtime>'>"

   # Gate verdict rubric
   PASS_meaning: "<what PASS maps in solution space>"
   FAIL_meaning: "<what FAIL maps>"
   INFO_meaning: "<what INFO maps>"

   effort:
     files_created: ["<list>"]
     estimated_time: "<hours or days>"

   substrate_framing: |
     <classification-respecting explanation,
      flow from D_K eigenvalues -> spectral moments -> observable>
   ```

2. **`.claude/templates/pru-pre-registration-template.md`** (EDIT):
   - Add pointer to `r3-yaml-gate-block.yaml` as the canonical machinery
     pin scaffold
   - Add validation rule: "If a gate block is not R3 YAML, it does not
     count toward sig_4."

3. **`computations/_yaml_gate_validator.py`** (NEW):
   - Parses each gate block in a plan file
   - Verifies all 8 checklist items are present with non-empty content
   - Emits per-gate PASS / FAIL on template compliance
   - Used by `_pru_cardinality_audit.py` as its gate-YAML source

4. **This plan file (`session-84-plan-w9a.md`)** — already uses the
   13-field spec compatible with R3 YAML (field names map to the 8
   checklist items + classification + agent_type + meaning + effort +
   substrate_framing).

### PRDR
- `CHECKLIST_ITEM_COUNT` — **PIN**: 8
- `REQUIRED_CHECKLIST_KEYS` — **PIN**: `["operator", "strict_PASS_boundary",
  "boundary_reachable_analytically", "reachable_rationals",
  "machinery_pin_map", "audit_discriminators", "substitution_chain",
  "input_files"]`
- `SCHEMA_VERSION` — **PIN**: `"R3"`
- `TEMPLATE_PATH` — **PIN**: `.claude/templates/r3-yaml-gate-block.yaml`
- `VALIDATOR_PATH` — **PIN**: `computations/_yaml_gate_validator.py`

### 4-tuple
- **value**: count of S84 gates with schema_version = "R3" AND all 8
  checklist items populated
- **scheme**: `R3-YAML-template`
- **convention**: `8-item-checklist`
- **L_max**: `plan-scope` (all wave-plan files)

### PASS / FAIL / INFO
- **PASS**: every S84 gate block (across all wave plan files)
  declares `schema_version: "R3"` (or equivalent structure matching
  the 13-field spec) AND all 8 machinery-checklist items are populated
  with non-empty content.
- **FAIL**: any S84 gate lacks schema_version "R3" OR has an empty
  checklist item.
- **INFO**: compliance at >= 90% but < 100%. Flagged for per-gate
  remediation before session close.

### Substitution chain
```
Definition 1: R3_compliant(g) = 1 if all 8 checklist items of g are
                                non-empty AND g.schema_version = "R3"
                                else 0
Definition 2: sig_4 = 1 if for all g in S84: R3_compliant(g) = 1 else 0

Substitute:
  sig_4 = product_{g in S84} R3_compliant(g)

Simplify:
  sig_4 = 1 iff all S84 gates compliant; sig_4 = 0 otherwise.

Direction: a single non-compliant gate drops sig_4 from 1 to 0, removing
  weight 1.000 from the ladder total.

Conclusion: template adoption discipline at plan authorship is the only
  path to sig_4 = 1. Post-hoc patching is not permitted (verdicts must
  cite the R3-compliant gate block that was frozen at plan time).
```

### Meaning
**PASS**: every S84 gate has its machinery enumerated at plan-authorship
time, via a canonical template with 8 required checklist items. PRDR
is no longer a discretionary prose section but a structured YAML block
validated by `_yaml_gate_validator.py` before plan freeze.

**FAIL**: gate blocks revert to prose-only PRDR; validator catches
missing items; remediation is straightforward (add missing items,
re-validate).

**INFO**: partial compliance. Flagged for plan-freeze blocker.

### Effort
- `r3-yaml-gate-block.yaml` template: ~90 lines
- `pru-pre-registration-template.md` edit: ~30-line addition
- `_yaml_gate_validator.py`: ~180 lines
- Adoption in this plan and W9b: already structured per 13-field spec
- Migration of other wave plans: done in parallel by each wave's planner

**Time**: ~1 day template + validator; ongoing per-wave during plan authorship.

### Substrate framing
NON-PHONONIC. Template schema; no D_K content. Provides the YAML scaffold
that `_pru_cardinality_audit.py` (W9a-97) consumes.

---

## §W9a-101 — S84-W1-CF-ARCHIVAL

### Gate ID
`S84-W9A-101-ARCHIVAL`

### Trigger
`[VERIFY]` — PASS/FAIL on byte-content archival at session close.

### Classification
**NON-PHONONIC** (methodology / reproducibility)

### Agent type
`gen-physicist` (meta-gate on session-close archival procedure)

### Hypothesis
Freezing the byte-content of `canonical_constants.py` at S84 session
close as `canonical_constants_s84_frozen.py` in `computations/`,
and recording the frozen file's SHA-256 in the S84 handoff's pinning
block, enables S85+ reproducibility of every S84 verdict. Any S84
verdict's audit_sha256 can be reconstructed from (its producing
script, the frozen canonical, the frozen pin-map) — a test that
becomes impossible once canonical is edited in-place for S85.

### Method
1. **`computations/canonical_constants_s84_frozen.py`** (NEW, at
   S84 session close):
   - Exact byte copy of `canonical_constants.py` at session-close time
   - Header comment block:
     ```python
     """
     canonical_constants snapshot: Session 84
     Frozen: {iso-timestamp of session close}
     Source SHA-256: {64-char hex of canonical_constants.py at freeze time}
     Purpose: enables S85+ audit_sha256 reconstruction of S84 verdicts.
     DO NOT EDIT. For S85+ constants, edit canonical_constants.py in place
     and create canonical_constants_s85_frozen.py at S85 close.
     """
     ```
   - File ends with `# FROZEN EOF` sentinel

2. **`computations/_archive_canonical.py`** (NEW, the archival script):
   - Runs at session close (or manually via `/handoff`)
   - Computes SHA-256 of current `canonical_constants.py`
   - Copies the file byte-for-byte to the frozen path
   - Prepends the header comment with timestamp + source SHA
   - Appends the sentinel
   - Verifies round-trip: SHA-256 of frozen file (minus header + sentinel)
     equals source SHA
   - Emits JSON record:
     ```json
     {"session": 84, "source_sha256": "<64>", "frozen_path":
      "computations/canonical_constants_s84_frozen.py",
      "frozen_at": "<iso>"}
     ```

3. **`sessions/archive/session-84/session-84-handoff.md`** (at close):
   - §6 (files created / modified) MUST list the frozen file path
   - New §6a "Canonical archival" subsection with the JSON record

4. **`.claude/hooks/post-session/v3-closure-audit.sh`** (W9a-98 already
   wires this; add archival check as sig_1 dependency):
   - If canonical_constants_s84_frozen.py does NOT exist at session close,
     do NOT set sig_1 = 1 (since audit_sha256 cannot be reconstructed
     post-session without the freeze)

### PRDR
- `FROZEN_FILENAME_FORMAT` — **PIN**:
  `"canonical_constants_s{N}_frozen.py"`
- `FREEZE_TIMESTAMP_FORMAT` — **PIN**: ISO-8601 UTC
- `SENTINEL_MARKER` — **PIN**: `"# FROZEN EOF"`
- `ROUND_TRIP_TOLERANCE` — **PIN**: exact byte-match required (zero
  tolerance; sensitivity to header stripping handled via SHA of
  source-only body, not including the prepended header)

### 4-tuple
- **value**: SHA-256 of `canonical_constants.py` at freeze time
- **scheme**: `byte-freeze`
- **convention**: `per-session-immutable`
- **L_max**: `session-scope`

### PASS / FAIL / INFO
- **PASS**: `canonical_constants_s84_frozen.py` exists at session close;
  header records timestamp + source SHA; round-trip SHA matches;
  handoff §6a records the JSON.
- **FAIL**: file missing, header malformed, round-trip SHA mismatch,
  or handoff section absent. Remediation: re-run `_archive_canonical.py`;
  amend handoff before close.
- **INFO**: file present but timestamp is more than 24h stale
  (canonical was edited post-freeze). Flag for re-freeze.

### Substitution chain
```
Definition 1: audit_sha256(g) = sha256(script_bytes || canonical_bytes_at_freeze
                                       || pinmap_bytes)
Definition 2: In S85+, canonical_bytes (current) != canonical_bytes_at_S84_freeze
              (in general, since canonical evolves)
Definition 3: reconstructibility(g, t) = 1 if can recompute audit_sha256(g)
                                         at time t using available archives,
                                         else 0

Substitute:
  reconstructibility(S84 gate, S85+ time) requires canonical_bytes_at_S84_freeze
    to be accessible
  This is provided only by canonical_constants_s84_frozen.py

Direction: without freeze, audit_sha256 becomes a one-way function in time;
  past verdicts cannot be audit-reproduced once canonical is edited.

Conclusion: byte-freeze at session close is NECESSARY for long-horizon
  audit closure; it is not a nice-to-have.
```

### Meaning
**PASS**: S84 verdicts remain audit-reproducible in S85+, S90+, etc.
Any future session can rerun the producing script against the frozen
canonical + frozen pin-map and verify that audit_sha256 matches the
verdict-file record.

**FAIL**: S84 verdicts become un-auditable once S85 edits canonical.
Structural provenance is lost; audit integrity collapses.

**INFO**: freeze timestamp stale — some post-freeze canonical edits
snuck in. Re-freeze required.

### Effort
- `canonical_constants_s84_frozen.py` generation: automated at close
- `_archive_canonical.py` (new): ~80 lines
- Handoff §6a amendment: template boilerplate
- Sig_1 dependency check in hook: ~10-line addition to W9a-98 script

**Time**: ~0.5 day implementation; execution is automatic at close.

### Substrate framing
NON-PHONONIC. Archival discipline. Indirect substrate relevance: the
freeze captures the numerical values of M_KK, tau_fold, Delta_BCS,
etc. as they stood during S84 verdict production, so any subsequent
substrate-physics claim ("S84 said m_H = 133.4 GeV at L_max -> inf")
remains reproducibly audit-anchored.

---

## §W9a-102 — S84-W1-CF-MANIFEST-AUTO

### Gate ID
`S84-W9A-102-MANIFEST-AUTO`

### Trigger
`[VERIFY]` — PASS/FAIL on ARTIFACTS PROMISED block auto-generation
coverage.

### Classification
**NON-PHONONIC** (methodology / prompt infrastructure)

### Agent type
`gen-physicist` (meta-gate on rclab-review skill extension)

### Hypothesis
Extending the `rclab-review` skill to auto-generate an
`ARTIFACTS PROMISED` JSON block in every compute-mode dispatch prompt
— derived from the gate's pre-registration block's `input_files`,
`method.producing_script`, and output-file declarations — makes the
completion-verify.sh hook (W9a-98) able to check artifact existence
mechanically rather than by prompt-text regex on a free-form
"deliverables" paragraph.

### Method
1. **`.claude/skills/rclab-review/SKILL.md`** (EDIT):
   - Add section: "ARTIFACTS PROMISED JSON block (compute-mode only)"
   - Specify that every compute-mode dispatch prompt generated by the
     skill MUST include an `ARTIFACTS PROMISED` block, formatted as:
     ```
     ## ARTIFACTS PROMISED
     ```json
     {
       "gate_id": "{G}",
       "script": "<path>",
       "verdict_line_target": "s{N}_gate_verdicts.txt",
       "data_files": [...],
       "plot_files": [...],
       "working_paper_sections": [{"section": "§<id>", "min_lines": 15}]
     }
     ```
   - The block is parsed by `completion-verify.sh` as structured JSON

2. **`.claude/skills/rclab-review/generate_manifest.py`** (NEW, or
   integrated into existing skill code):
   - Reads gate block (R3 YAML via `_yaml_gate_validator.py`)
   - Extracts:
     - `script` from gate.method.producing_script
     - `verdict_line_target` from session-plan context (`s{N}_gate_verdicts.txt`)
     - `data_files` from gate.method.description (regex on `.npz`,
       `.npy`, `.json`, `.csv` mentions)
     - `plot_files` from method (regex on `.png`, `.pdf`)
     - `working_paper_sections` from gate.classification + plan's
       working-paper ToC
   - Emits the JSON block into the prompt at the appropriate location
     (after §Substrate framing, before the "Begin" sigil)

3. **Spot audit**: 10% of S84 compute-mode dispatch prompts (e.g., 2 of
   ~20 W9a+W9b dispatches if dispatch count lands there) are sampled
   post-generation. The sampled prompts are manually verified to
   contain:
   - A well-formed `ARTIFACTS PROMISED` JSON block
   - The block's contents match what the gate block actually declares

4. **Audit results archived**:
   `sessions/archive/session-84/manifest_auto_audit.json` (per-sample pass/fail).

### PRDR
- `MANIFEST_BLOCK_HEADER` — **PIN**: `"## ARTIFACTS PROMISED"`
- `MANIFEST_JSON_KEYS` — **PIN**: `["gate_id", "script",
  "verdict_line_target", "data_files", "plot_files",
  "working_paper_sections"]`
- `SPOT_AUDIT_SAMPLE_FRACTION` — **PIN**: `0.10`
- `SPOT_AUDIT_SAMPLE_FLOOR` — **PIN**: 2 prompts minimum
- `WORKING_PAPER_SECTION_MIN_LINES` — **PIN**: 15 (stub threshold from
  `.claude/rules/agent-standards.md`)

### 4-tuple
- **value**: fraction of sampled S84 compute-mode prompts with
  well-formed ARTIFACTS PROMISED block
- **scheme**: `auto-generation + spot-audit`
- **convention**: `10%-sample`
- **L_max**: `session-scope`

### PASS / FAIL / INFO
- **PASS**: 100% of sampled prompts have well-formed blocks AND block
  contents match the gate block declarations. Auto-generation is
  functional.
- **FAIL**: < 90% of sampled prompts pass. Auto-generation is broken
  or the skill extension was not applied.
- **INFO**: 90-99% pass; minor template inconsistencies flagged for
  manual correction.

### Substitution chain
```
Definition 1: manifest_present(p) = 1 if prompt p has well-formed
                                    ARTIFACTS PROMISED JSON block
                                    else 0
Definition 2: manifest_accurate(p, g) = 1 if manifest contents match
                                        gate g's declarations else 0
Definition 3: pass_fraction = (1/|S|) sum_{p in S}
                              manifest_present(p) * manifest_accurate(p, g(p))
               where S is the sampled prompt set

Substitute:
  PASS iff pass_fraction = 1.0
  INFO iff 0.90 <= pass_fraction < 1.0
  FAIL iff pass_fraction < 0.90

Direction: a single malformed prompt in a sample of 2 drops pass_fraction
  to 0.5 -> FAIL. With |S| = 2 the grading is all-or-nothing;
  recommend |S| >= 5 for finer diagnostics if dispatch count allows.

Conclusion: sample-size discipline matters; the SPOT_AUDIT_SAMPLE_FLOOR
  of 2 is a minimum, not a target.
```

### Meaning
**PASS**: completion-verify.sh (W9a-98) has structured machine-readable
artifact manifests to check against, not prose regex. Verdict-appended-
but-section-skipped failure mode (S82 observed) is caught in milliseconds
with precise per-artifact diagnostics.

**FAIL**: manifests are absent or malformed; completion-verify.sh falls
back to prose regex (legacy, known-unreliable). Remediation: fix the
skill's generator.

**INFO**: coverage is partial; a few prompts need manual correction,
auto-generation mostly works.

### Effort
- SKILL.md edit: ~30 lines
- `generate_manifest.py`: ~150 lines
- Spot-audit harness: ~40 lines (scripted sampling)
- Audit archival: automatic

**Time**: ~1 day implementation + 0.25 day spot audit.

### Substrate framing
NON-PHONONIC. Prompt infrastructure. Downstream of the R3 YAML
template (W9a-100) and upstream of the completion-verify hook (W9a-98).

---

## §W9a-103 — S84-W1-CF-CRITPATH

### Gate ID
`S84-W9A-103-CRITPATH`

### Trigger
`[VERIFY]` — PASS/FAIL on per-wave dependency graph + critical_path flag
auto-population.

### Classification
**NON-PHONONIC** (methodology / dependency analysis)

### Agent type
`gen-physicist` (meta-gate on dependency-graph extension to PRU tool)

### Hypothesis
Extending `_pru_cardinality_audit.py` (or creating a sibling
`_critpath_audit.py`) to build a per-wave dependency graph from each
gate's `input_files` (incoming edges) and `method.producing_script`
outputs (outgoing edges), then setting `critical_path: true` on any
gate with non-empty outgoing-edge set, automates the
ADVISORY-vs-BLOCKING hook posture per gate.

### Method
Create or edit:

1. **`computations/_critpath_audit.py`** (NEW or extension of
   W9a-97):
   - Input: directory of wave plan YAML files (e.g., `session-84-plan-w{1..9}.md`)
   - Parse each gate's `input_files` (incoming edges: this gate depends
     on these files)
   - Parse each gate's `method.producing_script` + declared data outputs
     (outgoing edges: this gate produces these files)
   - Build directed graph G_wave per wave (nodes = gates, edges =
     file-flow dependencies)
   - For each gate g:
     - `outgoing_edges(g)` = gates g' such that some output of g is an
       input of g'
     - `critical_path(g)` = True if `outgoing_edges(g)` is non-empty
       AND at least one g' in outgoing_edges(g) has
       `critical_path(g') = True` OR g' is a terminal gate (no outgoing)
   - Emit JSON record per wave:
     ```json
     {
       "wave": "W9a",
       "gates": {
         "G1": {"critical_path": true, "incoming": [...], "outgoing": [...]},
         "G2": {...}
       },
       "graph_summary": {"nodes": N, "edges": E, "max_depth": D}
     }
     ```

2. **Hook posture per gate**:
   - `critical_path = true` -> hook posture BLOCKING (post-session hook
     exits 1 on failure)
   - `critical_path = false` -> hook posture ADVISORY (exit 0 always)
   - Per-gate posture written into
     `sessions/archive/session-84/hook_posture_map.json` consumed by
     `completion-verify.sh` (W9a-98)

3. **Auto-write back into plan YAML** (optional, controlled by flag):
   - If `--write-back` flag is passed, the tool modifies each gate
     block in-place to add `critical_path: true` or `critical_path: false`
   - Manual review required before plan freeze

4. **Self-test**: the tool runs on W9a itself.
   - Expected outgoing edges:
     - W9a-97 -> W9a-103 (CRITPATH depends on PRU-TOOL)
     - W9a-97 -> (all other gates, since PRU audit consumes all YAML)
     - W9a-98 -> W9b gates (hook infra gates all subsequent waves)
     - W9a-99 -> (every script produced in S84, via template)
     - W9a-100 -> every S84 gate block
     - W9a-101 -> S85+ (temporal dependency, flagged as "cross-session")
     - W9a-102 -> W9a-98 (manifests feed the hook)
     - W9a-104 -> W9a-98 (recovery targets the hook)
   - Expected critical_path flags: W9a-97, W9a-98, W9a-99, W9a-100,
     W9a-102 = True. W9a-101, W9a-103, W9a-104 = depends on
     outgoing-edge analysis at plan freeze.

### PRDR
- `GRAPH_LIBRARY` — **PIN**: `networkx` (std-install; CPU-local, no GPU)
- `CRITICAL_PATH_DEFINITION` — **PIN**: "has outgoing edges AND at least
  one outgoing target is critical_path or terminal"
- `HOOK_POSTURE_MAP_PATH` — **PIN**:
  `sessions/archive/session-84/hook_posture_map.json`
- `CROSS_SESSION_FLAG` — **PIN**: `"cross-session"` (marker for edges
  that leave S84, e.g., W9a-101 to S85)
- `WRITE_BACK_FLAG` — **PIN**: `"--write-back"` (explicit opt-in)

### 4-tuple
- **value**: (per-wave dependency graph JSON) + (critical_path flag
  per gate) + (hook posture map)
- **scheme**: `file-flow dependency`
- **convention**: `networkx directed graph`
- **L_max**: `plan-scope`

### PASS / FAIL / INFO
- **PASS**: per-wave dependency graph constructed for every S84 wave;
  every gate has `critical_path` flag assigned; hook posture map
  emitted; self-test on W9a recovers the expected flag pattern above.
- **FAIL**: graph construction fails (e.g., circular dependency),
  hook posture map absent, or self-test flag pattern deviates.
- **INFO**: graph built but some gates lack outgoing edges because
  their data-file declarations are ambiguous. Flagged for per-gate
  manual inspection.

### Substitution chain
```
Definition 1: G_wave = (V, E) directed graph where V = gates, E = file-flow
Definition 2: outgoing(g) = {g' : exists file f. f in outputs(g) AND
                                   f in inputs(g')}
Definition 3: critical_path(g) = True iff outgoing(g) non-empty
                                 AND (some g' in outgoing(g) is terminal
                                      OR critical_path(g') = True)

Substitute:
  Recursive definition; terminates because graph is acyclic
  (if gate topology is consistent; otherwise fail loudly).

Canonical form:
  critical_path(g) is the indicator of "g's artifacts are consumed by
  at least one other gate in the wave's critical chain."

Direction: if outgoing(g) is empty, critical_path(g) = False
  (terminal gate; hook posture ADVISORY).
  If outgoing(g) non-empty, posture = BLOCKING.

Conclusion: hook posture is derived structurally from the dependency
  graph, not assigned manually per gate.
```

### Meaning
**PASS**: BLOCKING vs ADVISORY hook posture is derived automatically
from the dependency graph at plan freeze. Manual assignment error
(e.g., S82 mis-labeling a critical dependency as ADVISORY, leading
to silent breakage) is eliminated.

**FAIL**: posture assignment reverts to manual. Works but is
error-prone.

**INFO**: partial automation; a subset of gates have ambiguous
data-file declarations and need manual inspection.

### Effort
- `_critpath_audit.py`: ~250 lines (includes networkx graph
  construction, BFS/DFS for critical-path propagation, JSON emission)
- Self-test on W9a: ~30 lines in test file
- Integration with `_pru_cardinality_audit.py`: extend shared YAML
  parser (~20-line edit)

**Time**: ~1 day implementation + 0.5 day self-test.

### Substrate framing
NON-PHONONIC. Dependency graph; no substrate content. Enables the
ADVISORY / BLOCKING posture split in the W9a-98 hook infrastructure,
which in turn carries sig_3 weight (3.750) on the v3 ladder.

---

## §W9a-104 — S84-W2-CF-RECOVERY-SPEC

### Gate ID
`S84-W9A-104-RECOVERY-SPEC`

### Trigger
`[VERIFY-THEOREM]` — specification-level correctness (recovery procedure
covers all hard-fail modes identified in the S82 + S83 retrospectives).

### Classification
**NON-PHONONIC** (methodology / recovery protocol)

### Agent type
`gen-physicist` (meta-gate on recovery-procedure specification + written
artifact)

### Hypothesis
A written recovery procedure — specifying orchestrator re-dispatch
attempts, maximum iteration count, fallback to V3-NON-COMPLIANT status,
and user-intervention trigger criteria — covers every hard-fail mode
of the post-session BLOCKING hook (W9a-98) without introducing
iterate-until-PASS or convention-shopping pathologies (S78 Class-1-7
execution failures).

### Method
Create:

1. **`.claude/rules/v3-closure-recovery.md`** (NEW, specification
   document):

   ```markdown
   # V3 Closure Recovery Procedure

   When `v3-closure-audit.sh` exits 1 (BLOCKING), the orchestrator
   executes this procedure. No other recovery path is permitted.

   ## Stage 1: Automatic re-dispatch (max 2 iterations)

   Identify which signal failed:
   - sig_1 = 0: `_pru_cardinality_audit.py` emitted D_PRU_raw > 0
     for at least one gate OR did not run. Remediation: fix the
     unpinned-parameter(s) flagged in the tool's JSON output, rerun
     tool. Re-dispatch: run tool; if D_PRU_raw = 0, proceed.
   - sig_2 = 0: at least one verdict line lacks dual-SHA. Remediation:
     regenerate verdict line using updated template. Re-dispatch:
     run the gate's producing script.
   - sig_3 < coverage_threshold: completion-queue log is sparse.
     Remediation: no action (log is an observation, not a target;
     sparse log = agent dispatches that didn't fire the hook, which
     is a settings.json wiring issue for NEXT session).
   - sig_4 = 0: at least one gate lacks R3 YAML schema_version.
     Remediation: edit the gate block; re-run `_yaml_gate_validator.py`.
   - sig_5 = 0: duplicate audit_sha256. Remediation: one of the
     duplicates is a SHA-hardcoding error in the producing script;
     flag for manual review; re-dispatch with fixed script.

   Re-dispatch count: max 2 iterations per signal. Tracking:
   `sessions/archive/session-84/recovery_iteration_log.json`:
   ```json
   {"signal": "sig_2", "iteration": 1, "remediation": "...",
    "post_iter_status": "PASS|FAIL", "ts": "<iso>"}
   ```

   ## Stage 2: V3-NON-COMPLIANT fallback

   If Stage 1 fails to reach CLOSED or INFO after 2 iterations per
   signal:
   - Session closes with status **V3-NON-COMPLIANT**
   - Handoff §1 (metadata) records status
   - Handoff §7 (next session recommendations) MUST include
     remediation of each unresolved signal as the leading item
   - The session's verdicts REMAIN VALID (they are physics results);
     only the v3-ladder closure is deferred

   ## Stage 3: User-intervention trigger

   If Stage 2 fires AND any of the following:
   - sig_1 iteration count > 2 (PRU audit cannot be driven to zero
     — indicates a deeper plan-authoring issue)
   - sig_5 duplicate audit_sha256 in 3+ verdict lines (indicates
     systematic SHA-hardcoding in a shared codegen library)
   - recovery_iteration_log.json contains conflicting remediations
     (e.g., sig_2 fix breaks sig_4)

   Then: **orchestrator halts** and pings user. No further automatic
   dispatch. User decides: accept V3-NON-COMPLIANT and close, OR
   defer session close and manually intervene.

   ## Non-permitted recovery actions

   The following are explicitly PROHIBITED during recovery (S78 Class
   1-7 execution-property failures):
   - Changing a gate's convention to reach PASS (convention-shopping)
   - Rerunning a gate with different scheme until PASS
     (iterate-until-PASS)
   - Retroactively editing the pre-registration threshold
     (post-hoc-reg)
   - Editing a verdict line other than by rerunning the producing
     script (ansatz-forced-PASS)

   If a remediation would require any of the above, abort recovery
   and proceed to Stage 3 user trigger.
   ```

2. **`computations/_recovery_controller.py`** (NEW,
   orchestrator-facing):
   - Parses `v3_ladder_audit.json` to identify failed signals
   - Dispatches per-signal remediation (calls `_pru_cardinality_audit.py`
     for sig_1, template regeneration for sig_2, etc.)
   - Tracks iteration count in `recovery_iteration_log.json`
   - Enforces max 2 iterations per signal
   - Emits transition events (Stage 1 -> Stage 2, Stage 2 -> Stage 3)
     into `completion-queue.jsonl`

3. **`sessions/archive/session-84/recovery_iteration_log.json`** (auto-created)

### PRDR
- `MAX_ITERATIONS_PER_SIGNAL` — **PIN**: 2
- `FALLBACK_STATUS_NAME` — **PIN**: `"V3-NON-COMPLIANT"`
- `USER_TRIGGER_CONDITIONS` — **PIN**: enumerated 3-condition set above
- `PROHIBITED_ACTIONS` — **PIN**: enumerated 4-action set above
- `RECOVERY_LOG_PATH` — **PIN**:
  `sessions/session-{N}/recovery_iteration_log.json`

### 4-tuple
- **value**: (specification document presence) + (controller script
  operational test)
- **scheme**: `3-stage recovery`
- **convention**: `max-2-iter + fallback + user-trigger`
- **L_max**: `per-session`

### PASS / FAIL / INFO
- **PASS**: `v3-closure-recovery.md` exists with all 3 stages documented;
  `_recovery_controller.py` is operational; a synthetic FAIL test
  (corrupt verdict file to force sig_5 = 0, trigger hook, invoke
  controller) produces the expected Stage-1 re-dispatch behavior; a
  synthetic unrecoverable FAIL test (corrupt in a way that no
  remediation can fix) triggers Stage 2 fallback; explicit test of
  Stage 3 user-trigger condition raises the expected halt.
- **FAIL**: specification missing or incomplete; controller absent
  or non-operational; synthetic tests do not produce expected stage
  transitions.
- **INFO**: specification exists and controller works but one of the
  3 user-trigger conditions has not been exercised by a synthetic
  test. Flagged for post-session manual walkthrough.

### Substitution chain
```
Definition 1: recovery(s) = remediation action for signal s
Definition 2: iter_count(s) = number of times recovery(s) has been
                              attempted this session
Definition 3: stage_transition(s, iter_count(s)) =
                Stage_1 if iter_count(s) <= 2 AND status != PASS
                Stage_2 if iter_count(s) > 2
                Stage_3 if user_trigger_condition(s) holds

Substitute:
  iterate-until-PASS would correspond to iter_count(s) unbounded
  -> excluded by MAX_ITERATIONS_PER_SIGNAL = 2

Canonical form:
  recovery procedure terminates in bounded time with one of three
  outcomes: CLOSED (Stage 1 success), V3-NON-COMPLIANT (Stage 2),
  or user-intervention (Stage 3).

Direction: bounded iteration prevents Class-1-7 execution failures
  from masquerading as recovery. PROHIBITED_ACTIONS list is the
  safety-net.

Conclusion: recovery is a SPECIFICATION, not a dynamical system.
  Its correctness is judged by spec completeness, not runtime
  behavior (though runtime tests confirm spec implementability).
```

### Meaning
**PASS**: post-session hook hard-fail has a well-defined, bounded
recovery procedure that does not admit iterate-until-PASS,
convention-shopping, or post-hoc pre-registration editing. V3
closure becomes either achieved (Stage 1), deferred with explicit
status (Stage 2), or escalated to user (Stage 3).

**FAIL**: no specification, so hard-fail triggers ad-hoc orchestrator
behavior. The S78 execution-property failure modes creep back in
through unconstrained remediation.

**INFO**: spec exists; controller works; one test path untested.

### Effort
- `v3-closure-recovery.md`: ~200 lines specification
- `_recovery_controller.py`: ~180 lines (signal-dispatch routing +
  iteration tracking + stage-transition emission)
- Synthetic test fixtures: ~100 lines (3 tests: Stage 1 success,
  Stage 2 fallback, Stage 3 trigger)

**Time**: ~1.5 days specification + 0.5 day controller + 0.5 day tests.

### Substrate framing
NON-PHONONIC. Recovery specification; no substrate content.
Completes the W9a v3-closure stack: W9a-97 through W9a-103 build
the closure machinery; W9a-104 specifies what happens when that
machinery reports failure.

---

## W9a -> W9b Parallel Dispatch Note

W9a and W9b are DESIGNED to dispatch in parallel. W9a is the
infrastructure-closure half (8 items, rows 97-104); W9b is the
methodology-overlap half (remaining items from the methodology
carry-forward cluster, specified in `session-84-plan-w9b.md`).

Dependency between W9a and W9b:
- W9b items that depend on the PRU tool (W9a-97), the hook infra
  (W9a-98), or the dual-SHA template (W9a-99) can start authorship in
  parallel, but execution is staged: run-when-ready after the 3
  prerequisite items green. This is enforced by the W9a-103
  critical-path tool (once it's itself green).

Cap discipline: the user's concurrent-agent cap is ~8. W9a has 8
items. If W9a + W9b exceeds 8 concurrent dispatches, W9b's non-dependent
items are staged into a second parallel batch after W9a completes.
Batches are discrete per `feedback_dispatch-discipline.md` — no rolling
backfill.

---

## W9a -> W10 Decision Point (joint with W9b)

W10 is the v3-closure-ladder evaluation wave. W10 dispatches when BOTH
W9a and W9b are complete on-disk (verdict lines present, scripts
delivered, working-paper sections populated).

W10 gate: **S84-W10-V3-LADDER-EVAL**
- Runs `v3-closure-audit.sh` against the full S84 verdict file
- Emits the 5-signal ladder JSON
- Records the final S84 methodology status (CLOSED | INFO |
  V3-NON-COMPLIANT) in the session handoff

If W10 returns CLOSED: S84 methodology closure is permanent. The
v3 ladder is registered as a reusable harness for S85+.

If W10 returns INFO: S84 closes with partial v3 compliance (ladder
score in [6.801, 10.202)). Handoff records which signals fell short;
S85 inherits the recovery recommendations.

If W10 returns V3-NON-COMPLIANT: W9a-104 recovery procedure
triggers; Stage 1 -> Stage 2 -> Stage 3 as applicable.

---

## W9a Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness,
the following machinery parameters are enumerated and pinned at
plan-freeze time for W9a:

### Shared machinery (across all 8 items)
- **Python version**: 3.12 (as `phonon-exflation-sim/.venv312/Scripts/python.exe`)
- **Bash version**: as shipped with Git-for-Windows bundled-sh
- **YAML parser**: PyYAML >= 6.0 (std-install)
- **Hash library**: Python `hashlib.sha256` (stdlib)
- **Graph library**: `networkx` (for W9a-103)
- **Hook-event model**: Claude Code `PostToolUse` + `Stop` (per
  `update-config` skill)
- **Settings path**: `~/.claude/settings.json` (user-level; project-level
  `.claude/settings.json` also supported)

### Per-item machinery
- **W9a-97 (PRU)**: AST module-scope only; 6 listed pins (see §W9a-97 PRDR)
- **W9a-98 (HOOK)**: ladder weights + thresholds + sig_1 veto + postures
  (see §W9a-98 PRDR)
- **W9a-99 (SHA)**: hash-input sets + legacy marker (see §W9a-99 PRDR)
- **W9a-100 (TEMPLATE)**: 8-item checklist + schema version (see §W9a-100)
- **W9a-101 (ARCHIVAL)**: filename format + timestamp format + sentinel
  (see §W9a-101)
- **W9a-102 (MANIFEST)**: block header + JSON keys + audit fraction
  (see §W9a-102)
- **W9a-103 (CRITPATH)**: graph library + critical-path definition +
  cross-session marker (see §W9a-103)
- **W9a-104 (RECOVERY)**: max iter + fallback name + user-trigger conditions
  + prohibited actions (see §W9a-104)

PRU cardinality D_PRU_raw(W9a) = 0 by construction under these enumerated pins.

---

## W9a Input-SHA Ledger

| Input File | Purpose | Expected SHA |
|:-----------|:--------|:-------------|
| `sessions/session-plan/session-84-context.md` | plan context source | `<computed-at-plan-freeze>` |
| `.claude/rules/gate-verdicts.md` | verdict format canon | `<computed-at-plan-freeze>` |
| `.claude/rules/session-handoffs.md` | handoff schema canon | `<computed-at-plan-freeze>` |
| `.claude/rules/epistemic-discipline.md` | PRU Class-8 canon | `<computed-at-plan-freeze>` |
| `.claude/rules/math-scripts.md` | canonical constants + substitution chain | `<computed-at-plan-freeze>` |
| `.claude/rules/agent-standards.md` | completion-verification S82 retrospective | `<computed-at-plan-freeze>` |
| `.claude/templates/pru-pre-registration-template.md` | PRDR scaffold source | `<computed-at-plan-freeze>` |
| `.claude/templates/script-template.py` | SHA-emission template | `<computed-at-plan-freeze>` |
| `computations/canonical_constants.py` | canonical values (to be frozen by W9a-101) | `<computed-at-plan-freeze>` |
| `computations/_consolidate_intake.py` | consolidator (to be extended by W9a-99 shim) | `<computed-at-plan-freeze>` |
| `s83_gate_verdicts.txt` (if present) | S83 single-SHA baseline for shim test | `<computed-at-plan-freeze>` |

SHA values are populated at plan-freeze time by running `shasum -a 256`
(or `hashlib.sha256` Python equivalent) over each listed file. The
resulting SHA ledger is stored in the W9a input-pin map (consumed by
`audit_sha256` computation in every W9a producing script).

Dynamic outputs (created by W9a items) are marked `<computed-at-runtime>`:
- `computations/_pru_cardinality_audit.py` (W9a-97 output)
- `.claude/hooks/post-agent/completion-verify.sh` (W9a-98 output)
- `.claude/hooks/post-session/v3-closure-audit.sh` (W9a-98 output)
- `computations/script-template.py` (W9a-99 edit)
- `.claude/templates/r3-yaml-gate-block.yaml` (W9a-100 output)
- `computations/_yaml_gate_validator.py` (W9a-100 output)
- `computations/canonical_constants_s84_frozen.py` (W9a-101 output,
  at session close)
- `computations/_archive_canonical.py` (W9a-101 output)
- `.claude/skills/rclab-review/SKILL.md` (W9a-102 edit)
- `.claude/skills/rclab-review/generate_manifest.py` (W9a-102 output)
- `computations/_critpath_audit.py` (W9a-103 output)
- `sessions/archive/session-84/hook_posture_map.json` (W9a-103 output)
- `.claude/rules/v3-closure-recovery.md` (W9a-104 output)
- `computations/_recovery_controller.py` (W9a-104 output)

These are verified at session close by the BLOCKING post-session hook
(W9a-98) against the ARTIFACTS PROMISED block (W9a-102) generated for
each W9a dispatch.

---

**End of W9a plan.** W9b specification in `session-84-plan-w9b.md`
(parallel-dispatch companion). W10 v3-ladder evaluation runs after
both waves complete per the decision-point above.
