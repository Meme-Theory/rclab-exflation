# V3 Closure Recovery Procedure

## Scope

When the post-session `v3-closure-audit.sh` exits 1 (BLOCKING) or
emits a non-CLOSED verdict in `v3_ladder_audit.json`, the orchestrator
executes the procedure specified here. **No other recovery path is permitted.**
Ad-hoc "try again differently" remediation reintroduces the Class-1-7
execution-property failures the v3 ladder was built to prevent.

This specification pins the machinery parameters:

| Parameter                      | PIN                                            |
|:-------------------------------|:-----------------------------------------------|
| `MAX_ITERATIONS_PER_SIGNAL`    | 2                                              |
| `FALLBACK_STATUS_NAME`         | `"V3-NON-COMPLIANT"`                           |
| `RECOVERY_LOG_PATH`            | `sessions/session-{N}/recovery_iteration_log.json` |
| `USER_TRIGGER_CONDITIONS`      | enumerated 3-item set (Stage 3 below)          |
| `PROHIBITED_ACTIONS`           | enumerated 4-item set (bottom of doc)          |

## Stage 1: Automatic re-dispatch (max 2 iterations per signal)

The v3 ladder emits five boolean / coverage signals. For each failed
signal, the controller invokes the corresponding remediation exactly
once per iteration, up to `MAX_ITERATIONS_PER_SIGNAL = 2`. The
cap is a hard bound: a third attempt falls through to Stage 2.

### Per-signal remediation map

- **sig_1 = 0** — `_pru_cardinality_audit.py` reported D_PRU_raw > 0 for
  at least one gate, OR the tool did not run.
  - Remediation: parse the tool's JSON; for each gate with
    `D_PRU_raw = 1`, add the missing pin(s) to `machinery_pin_map` in
    the gate block.
  - Re-dispatch action: rerun `_pru_cardinality_audit.py`; if the
    aggregate falls to zero, signal clears.

- **sig_2 = 0** — at least one verdict line lacks dual-SHA
  (`content_sha256` + `audit_sha256` companion comment row absent).
  - Remediation: regenerate the verdict line by rerunning the gate's
    producing script with the updated dual-SHA template.
  - Re-dispatch action: `python computations/_shared/s{N}_{gate}.py`; the
    script appends the corrected canonical line and comment row. No
    manual edits to `s{N}_gate_verdicts.txt` are permitted.

- **sig_3 < coverage_threshold** — completion-queue log is sparse.
  - Remediation: **none**. sig_3 is an *observation*, not a target. A
    sparse log indicates agent dispatches that did not fire the
    `settings.json` PostToolUse hook, which is a harness-wiring defect
    for the NEXT session, not the current one.
  - Re-dispatch action: no-op; log the diagnostic for next-session
    carry-forward. sig_3 does not veto the ladder; it degrades the
    score but Stage 1 still resolves if sig_1, sig_2, sig_4, sig_5 clear.

- **sig_4 = 0** — at least one gate lacks the R3 YAML
  `schema_version` key in its plan-file gate block.
  - Remediation: edit the gate block in the plan file to add
    `schema_version: R3`; re-run `_yaml_gate_validator.py`.
  - Re-dispatch action: `python computations/_shared/_yaml_gate_validator.py`.

- **sig_5 = 0** — duplicate `audit_sha256` across two or more verdict
  lines in `computations/session-{N}/s{N}_gate_verdicts.txt`.
  - Remediation: one (or more) of the duplicates is a SHA-hardcoding
    error in the producing script (it is emitting a copy-pasted
    literal rather than computing the closure from the input-pin map).
    Flag the offending gate(s) for manual review, fix the producing
    script to compute `audit_sha256` from `closure_hash(pins)`, and
    rerun.
  - Re-dispatch action: `python computations/_shared/s{N}_{gate}.py` for
    each flagged gate.
  - **Option A `supersedes` tag protocol**: per `gate-verdicts.md §"Option A — sig_5 remediation
    pathway under absolute verdict permanence"`, the corrective canonical
    line emitted by the rerun MUST carry a `supersedes=<old_audit_sha>`
    tag in its `value=` field OR in its dual-SHA companion comment row.
    The original (duplicate-SHA) verdict line is RETAINED on disk per
    absolute verdict permanence; the corrective line is emitted via the
    `emit_verdict` knowledge-MCP tool carrying a `supersedes=<old_audit_sha>`
    token (race-safe, lock-serialized — `gate-verdicts.md` §"Race-Safe
    Emission"; NOT a raw `open("a")` append). Downstream consumers cite the latest
    non-superseded line per the Option A reading discipline. The
    `supersedes` tag carries the FULL 64-character original
    `audit_sha256` (never a 16-char head form). This protocol applies
    UNIFORMLY to all sig_5 remediations under the bounded-iteration
    structure (MAX_ITERATIONS_PER_SIGNAL = 2 still holds; each
    iteration that fires emits its own corrective line with its own
    `supersedes` tag pointing to the most-recent-prior canonical line
    for that gate-ID).
  - **Calibration corpus**: see `gate-verdicts.md §"Option A — sig_5
    remediation pathway under absolute verdict permanence"` for the
    retroactively-canonicalized corrective-emission policy.
  - **Class-3 PROHIBITED_ACTIONS interaction**: corrective emissions
    that retroactively edit a prior verdict line in-place (rather than
    appending a `supersedes`-tagged successor) are Class-3 violations
    (post-hoc audit-trail editing). The Option A protocol is the
    structural alternative that preserves the audit trail by
    construction. Adding a `supersedes` tag to a prior line by editing
    that prior line in-place is also a Class-3 violation; the tag
    lives on the SUCCESSOR line, never on the predecessor.

### Iteration tracking

Every Stage-1 re-dispatch writes one JSON line to the recovery log
`sessions/session-{N}/recovery_iteration_log.json`:

```json
{"signal": "sig_2",
 "iteration": 1,
 "remediation": "regenerated verdict line for S{N}-W3-M via dual-SHA template",
 "post_iter_status": "PASS",
 "ts": "<ISO-8601>"}
```

The controller refuses to append an entry with `iteration > MAX_ITERATIONS_PER_SIGNAL`;
such a request triggers a Stage-2 transition event.

### Bounded-iteration termination proof (substitution chain)

```
Definition 1: recovery(s)      = remediation action for signal s in {sig_1..sig_5}
Definition 2: iter_count(s)    = count of Stage-1 dispatches for s this session
Definition 3: stage(s, i)      = Stage_1 if i <= MAX_ITERATIONS_PER_SIGNAL AND status(s) != PASS
                                 Stage_2 if i  > MAX_ITERATIONS_PER_SIGNAL
                                 Stage_3 if user_trigger(s) holds

Substitute MAX_ITERATIONS_PER_SIGNAL = 2:
  stage(s, i) = Stage_1 if i <= 2 AND status(s) != PASS
                Stage_2 if i  > 2
                Stage_3 if user_trigger(s) holds

Simplify (enumerate): for each s, i monotone-increments 0 -> 1 -> 2 -> 3.
  At i = 3 the predicate "i > 2" becomes true, forcing Stage_2.
  Therefore Stage_1 executes AT MOST 2 dispatches per signal, and
  AT MOST 2 * 5 = 10 dispatches per session across the five signals.

Direction: Because MAX_ITERATIONS_PER_SIGNAL is a finite integer > 0 and
i is strictly non-decreasing, the procedure terminates in at most
2 * (number of failed signals) re-dispatches. With 5 signals, the
upper bound is 10 automatic dispatches per session.

Conclusion: Stage-1 is a bounded iteration; iterate-until-PASS
(Class-6) is ruled out BY CONSTRUCTION, not by convention.
```

## Stage 2: V3-NON-COMPLIANT fallback

If any signal remains failed after 2 Stage-1 iterations — OR if Stage-1
aborts because a remediation would require a PROHIBITED_ACTIONS step —
the session closes with status **V3-NON-COMPLIANT**.

- Handoff §1 (metadata) records `v3_ladder_status: "V3-NON-COMPLIANT"`.
- Handoff §7 (next-session recommendations) MUST include remediation of
  each unresolved signal as the **leading** carry-forward item.
- The session's verdicts **REMAIN VALID** — they are physics results
  with pre-registered thresholds. Only the v3-ladder closure is deferred.
  This separation (physics verdict vs methodology ladder) is the
  point of having the ladder as a distinct gate: verdicts are pinned
  to the pre-registered threshold; the ladder pins methodology hygiene.

The V3-NON-COMPLIANT status propagates into the `completion-queue.jsonl`
as a single event:

```json
{"event": "stage_transition", "from": "stage_1", "to": "stage_2",
 "session": "S{N}", "failed_signals": ["sig_1", "sig_5"],
 "ts": "<ISO-8601>"}
```

## Stage 3: User-intervention trigger

Stage 2 (fallback) fires AND any one of the following holds:

1. **sig_1 iteration count exceeded** — the PRU audit could not be driven
   to zero within the 2-iteration bound. This indicates a plan-authoring
   defect that remediation cannot mechanically fix (e.g., a pin the
   plan author did not envisage).

2. **sig_5 systematic duplication** — duplicate `audit_sha256` appears in
   3 or more verdict lines, indicating a SHA-hardcoding bug in a shared
   codegen library (e.g., the script template itself), not an isolated
   typo in one producing script.

3. **conflicting remediations** — `recovery_iteration_log.json` records
   two entries whose remediations contradict each other (the canonical
   pattern: a sig_2 fix regenerates a verdict line that invalidates the
   sig_4 YAML block reference, or a sig_4 schema bump breaks sig_2 dual-SHA).

When Stage 3 fires, the orchestrator **halts automatic dispatch** and
emits a user-ping event to `completion-queue.jsonl`:

```json
{"event": "stage_transition", "from": "stage_2", "to": "stage_3",
 "session": "S{N}", "trigger": "sig_1_iter_exceeded",
 "detail": "PRU audit failed to converge after 2 iterations on gates [G1, G3]",
 "ts": "<ISO-8601>"}
```

The user decides:
- **Accept V3-NON-COMPLIANT and close** — session ends with the flag; the
  trigger condition becomes the first item of next-session carry-forward.
- **Defer session close and manually intervene** — the user resolves the
  underlying issue by hand (plan edit, library patch, verdict-file
  surgery with audit trail); the controller records the manual
  intervention in the log as `{"stage": 3, "action": "manual", ...}`.

## PROHIBITED_ACTIONS (4-item pin)

The following actions are explicitly FORBIDDEN during recovery, in any
stage. They correspond to Class-1-7 execution-property failures.
Attempting any of them causes the controller to abort remediation and
transition immediately to Stage 3.

1. **Convention-shopping** — changing a gate's `convention` tag (or the
   underlying scheme/threshold) to reach PASS. The pre-registered
   convention is fixed at plan-freeze; re-running the gate under a
   different convention is a new gate, not a recovery.

2. **Iterate-until-PASS** — dispatching the same gate repeatedly with
   different random seeds / scan ranges / tolerances until one run
   lands above threshold. Stage-1's 2-iteration cap prevents this
   structurally; PROHIBITED_ACTIONS also forbids it explicitly.

3. **Post-hoc pre-registration editing** — retroactively editing the
   plan file's `pass_threshold`, `pass_band`, or `tolerance_rule` after
   seeing the computed value. Plan edits after a verdict is appended
   are documentation-only and must be logged with a `post-hoc:` prefix.

4. **Ansatz-forced PASS** — manually editing the verdict line in
   `s{N}_gate_verdicts.txt` to claim PASS without rerunning the
   producing script. The verdict file is write-once-per-gate; the only
   permitted modification path is a script rerun that appends a new
   canonical line.

If a proposed Stage-1 remediation would require any of actions 1-4,
the controller aborts the remediation and emits a Stage-3
`prohibited_action_detected` event. This is the safety-net the
recovery procedure relies on: bounded iteration closes the
iterate-until-PASS pathway, and PROHIBITED_ACTIONS closes the
remaining four pathways.

## Interaction with the ladder score

- Stage 1 success → ladder score recomputed → CLOSED or INFO per the
  threshold table; session handoff records the final status.
- Stage 2 fallback → status = `V3-NON-COMPLIANT`; physics verdicts
  unchanged; next session's Wave-0 plan leads with the unresolved
  signals.
- Stage 3 trigger → orchestrator halts; user decides close vs manual.

## Specification vs runtime

Per the bounded-iteration termination proof above: the recovery procedure is a
**specification**, not a dynamical system. Its correctness is judged by
spec completeness (all 3 stages documented, PROHIBITED_ACTIONS
enumerated, iteration bound proven) rather than by favorable runtime
outcomes. The synthetic tests below confirm *implementability*; the
specification is what the orchestrator binds to, session after session.

## Synthetic test fixtures (three PASS paths)

The implementation in `computations/_shared/_recovery_controller.py` ships
with three synthetic tests:

1. **Stage-1 success on sig_5 duplicate** — corrupt one verdict line's
   `audit_sha256` to match another's, invoke the controller, verify
   Stage-1 remediation restores uniqueness and ladder returns CLOSED.
2. **Stage-2 fallback after 2-iter exhaust on sig_1** — inject a
   non-fixable PRU defect (a pin the tool cannot auto-remediate),
   verify the controller respects MAX_ITERATIONS_PER_SIGNAL and
   transitions to V3-NON-COMPLIANT.
3. **Stage-3 user-trigger on sig_1 iteration > 2** — force a third
   sig_1 attempt via test harness, verify the controller refuses and
   emits the user-ping event.

All three tests run in the `__main__` block of `_recovery_controller.py`
under the `--self-test` flag.
