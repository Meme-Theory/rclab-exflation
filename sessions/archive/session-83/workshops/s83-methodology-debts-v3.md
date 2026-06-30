# Session 83 Workshop: kitaev × sagan — Methodology Debts v3 (PRU Class 8 + SHA-Collision + Completion-Verification)

**Date**: 2026-04-18
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: kitaev (kitaev-quantum-chaos-theorist) — Agent A; sagan (sagan-empiricist) — Agent B
**Source Documents**:
- sessions/archive/session-83/session-83-results-workingpaper.md
- .claude/rules/agent-standards.md
- .claude/rules/epistemic-discipline.md
- .claude/rules/gate-verdicts.md
- .claude/rules/math-scripts.md

**Focus Topics**:
1. PRU Class 8 recurrence: 4 new flags in S83 (G4 boundary-inequality, G11 1/N normalization, G15 Lambda_Z, G36 V_pair/Delta-fix/sign); v2 PRDR rule did not prevent them.
2. SHA-collision structural weakness: G59 FAIL with 3 S82 verdicts sharing SHA via single-INPUT_FILES declarations; G59 3-part fix proposal.
3. Completion-Verification v2: post-S82 rule exists, but S83 still saw ~14 dispatches / ~13 gates requiring intervention.
4. Unified v3 diff against agent-standards.md, epistemic-discipline.md, gate-verdicts.md, math-scripts.md + S84 test-gate.

---

## Round 1 — kitaev: Opening Analysis

### K1: PRU Class 8 as Information-Scrambling Problem

**Framing**: The plan and the executing script together constitute a dynamical system. The plan is the pinned initial condition; the script is the unitary; the verdict line is the measurement. PRU Class 8 is the statement that the plan has dim(kernel) > 0 — i.e., there remain free directions in parameter space after the plan's pre-registration has been applied. Information from those unpinned axes FLOWS into the verdict at execution time, and that flow is information-scrambling in the OTOC sense: the distance between "what the plan specified" and "what the verdict encodes" grows because execution-time choices propagate into the 64-char SHA closure.

**OTOC-analog metric** (scrambling distance between plan-pin state and verdict-closure state):

Define the commutator-like quantity:

```
D_PRU(gate_i) := | { pins_script(gate_i) } \ { pins_plan(gate_i) } |
```

where `pins_plan` is the set of `(key=value)` pairs frozen by the plan block, and `pins_script` is the set of `(key=value)` pairs that the executing script actually consumes (enumerable via static analysis of the script's free-parameter set). The set-difference counts the unpinned-but-consumed parameters. This is the cardinality of the residual free-parameter kernel.

**Substitution chain for the PASS-iff-cardinality-zero claim**:
- Step 1 (definition). Let `F_plan(g) = { (k,v) : k is a machinery parameter pinned in plan block for gate g }`.
- Step 2 (definition). Let `F_script(g) = { k : k is a machinery parameter CONSUMED by the producing script for gate g }` (enumerated via static analysis, per PRDR §0.10(d)).
- Step 3 (substitution). Define `D_PRU(g) := | { k : k in F_script(g), k not in keys(F_plan(g)) } |`.
- Step 4 (simplify). `D_PRU(g) = 0` iff every parameter the script consumes is pinned by the plan iff the plan fully determines the script's execution iff the verdict closure is plan-deterministic.
- Step 5 (direction). `D_PRU(g) > 0 ⇒ script has execution-time freedom ⇒ multiple verdict closures compatible with the same plan block ⇒ PRU Class 8 present.`
- Conclusion. PASS-of-rule-file iff `D_PRU(g) = 0` structurally for every gate g in the plan. This is a cardinality check, not a narrative "PRDR ran" check.

**Application to S83 recurrences** (five flags, cardinality ledger):

| Gate | Unpinned axes (kernel dimensions) | D_PRU | v2-PRDR detected? |
|:-----|:----------------------------------|:-----:|:------------------:|
| W1-G4 (§W1-G4, line 535) | Strict vs non-strict inequality at F_traj=1.5 (analytic rational 3/2 sits EXACTLY on PASS/INFO boundary) | 1 | NO — PRDR enumerated numerical thresholds but not the relational operator |
| W2-G11 (§W2-G11, line 1619) | 1/N^2 normalization convention: {W2-canonical-0.025-slope, NAT, Adjoint} | 1 (ternary) | NO — PRDR flagged as "need to resolve at run-time" but did not pin |
| W2-G15 (§W2-G15, line 2074) | Lambda_Z for Zubarev: {Conv A = M_KK, Conv B = lam_max} | 1 (binary) | NO — orchestrator pre-pinned at dispatch time, bypassing PRDR |
| W3-G36 (§W3-G36, line 4427) | V_pair volume rescaling + Delta-fix + sign convention | 3 (coupled) | NO — disambiguated post-hoc |
| W3-G59 closure input-set | SHA collision = verdict-space information loss (related, see K2) | n/a | n/a |

**Kitaev-test scrambling signature**: A plan that passes PRDR §0.10(d) but has `D_PRU > 0` for any gate is FALSE-PASS. The v2 rule-text "run PRDR and pin" is narrative; v3 must be CARDINALITY-ENFORCED. The rule must read: the plan's machinery-enumeration block for gate g PASSES iff and only if keys(F_plan(g)) ⊇ F_script(g) as a set containment, computed by static-analysis of the producing script. This is checkable by tooling (parse the script's top-level `if __name__ == "__main__"` block + argparse + global constants read; diff against plan's machinery pin).

**Special case — Boundary-inequality subclass (Class 8a)**: G4's failure is structurally distinct from G11/G15/G36. G11/G15/G36 are VALUE-kernel (scalar parameter unpinned); G4 is OPERATOR-kernel (relational operator unpinned at the threshold value). The canonical-form check must enumerate BOTH numerical thresholds AND the relational operators applied to them. F_traj = 1.500000 hitting the boundary is not a numerical accident — it is the analytic value 3/2, a structural property of the a_2 Mellin kernel (§W1-G4 Step 3, ratio g(N)-independent). Any plan that pre-registers a threshold at a rational value reachable by the canonical scheme MUST specify open vs closed interval. Class 8a (operator-kernel) should be enumerated alongside Class 8 (value-kernel) in the PRDR template.

**Structural claim**: PRU v2 FAILS on S83 because it is an EXPLANATION, not a STRUCTURAL ENFORCER. A rule without a cardinality-check tool is a rule without teeth. Recommend in v3 a new tool `computations/_pru_cardinality_audit.py` that:
1. Parses the plan's gate block for the machinery-pin list (keys only).
2. Parses the producing script's top-level parameters (via `ast` module).
3. Computes `D_PRU = len(F_script - F_plan)`.
4. Emits `D_PRU = 0` → PASS; `D_PRU > 0` → FAIL with the offending keys enumerated.

This is the Kitaev level-spacing-equivalent: it takes 10 lines of code and settles the question.

### K2: SHA-Collision via Information-Theoretic Hashing Discriminators

**Framing**: The closure SHA is intended as a many-to-one map from the gate's execution context to a 64-char audit identifier. W3-G59 reveals a LOW-ENTROPY PREIMAGE SPACE: three distinct S82 gates (W1-1-TD, W2-13, W3-7) with `INPUT_FILES = [canonical_constants.py]` produce the same SHA `5aef2c40...e56d8` because the input-pin map is literally byte-identical across the three gates. This is not a hash collision in the cryptographic sense — it is a COLLISION BY CONSTRUCTION of the preimage.

**Information-theoretic substitution chain**:
- Step 1 (definition). The S81-canonical closure is `SHA = sha256(concat_sorted("{k}={v}\n" for (k,v) in pins))` where `pins = {relpath_j : sha256(bytes(f_j))}` for `f_j in INPUT_FILES`.
- Step 2 (substitution). For three gates with `INPUT_FILES = [canonical_constants.py]` and canonical_constants.py frozen at byte content C_0, the input-pin map of gate i is `pins_i = {"canonical_constants.py" : sha256(C_0)}`, independent of i.
- Step 3 (simplify). `pins_1 = pins_2 = pins_3` as set-of-tuples → `concat_sorted(pins_i) = concat_sorted(pins_j)` for all i,j → `sha(...)` identical. Hence `SHA_1 = SHA_2 = SHA_3 = 5aef2c40...e56d8`.
- Step 4 (direction). The closure SHA carries ZERO bits of gate-identity information when INPUT_FILES is identical across gates. Preimage entropy H(gate | SHA) = log(3) bits among the three gates, vs. the intended H(gate | SHA) = 0 (the SHA should uniquely identify the gate's execution context).
- Step 5 (conclusion). The S81 closure algorithm has INSUFFICIENT DISCRIMINATORS in its hashed payload. The fix is to add per-gate discriminators that raise H(gate | SHA) back to 0.

**Required discriminators (Shannon-entropy-additive)**:

The hashed payload must include, AT MINIMUM:

1. **`self_script_sha`** (CF-59-A): `sha256(bytes(__file__))` of the producing script itself. Rationale: two gates reading the same input file but from different scripts have different execution contexts; the script's byte content is the unitary operator applied to the input. Info-gain: log2(N_gates) bits per session (where N_gates = distinct producing scripts ≈ 20–60 per session).

2. **`session_stamp`**: the session identifier `S{N}` as a pinned string `session=S{N}`. Rationale: two scripts with the same name in different sessions (e.g., `s82_w1_1_...py` vs a `s84_w1_1_...py` derivative) are distinct gate events; the session-stamp prevents cross-session collisions.

3. **`gate_id_stamp`**: the full pre-registered gate ID (e.g., `S83-NNLO-BAND-BOUND`) as a pinned string `gate_id=<ID>`. Rationale: the SAME script may run multiple gates (rare, but structurally possible — e.g., a meta-gate that audits three sub-gates); gate_id is the canonical identifier the plan uses, and should be part of the hashed payload.

4. **`machinery_pin_map`** (for PRU reconciliation with K1): the sorted (key, value) tuples of the PRDR machinery pins as a pinned string. Rationale: two invocations of the same script with different scan parameters produce different numerical results; if the machinery is unpinned, the verdict is non-reproducible; if pinned, the pin should enter the SHA so that replaying the machinery pin reproduces the SHA.

**Proposed S81+ canonical closure (v3 spec)**:

```python
def closure_v3(
    input_files: list[Path],
    self_script: Path,
    session: str,
    gate_id: str,
    machinery_pins: dict[str, str],
) -> str:
    pins = {}
    for f in input_files + [self_script]:
        pins[str(f.relative_to(repo_root))] = sha256(f.read_bytes()).hexdigest()
    pins["__session__"] = session
    pins["__gate_id__"] = gate_id
    for k, v in machinery_pins.items():
        pins[f"__pin_{k}__"] = str(v)
    payload = "".join(f"{k}={v}\n" for (k, v) in sorted(pins.items()))
    return sha256(payload.encode("utf-8")).hexdigest()
```

**Audit-SHA vs content-SHA split** (CF-59-C endorsement):

The single-SHA semantics conflate two orthogonal audit questions:
- **Content question**: "did this specific byte content produce this verdict?" (reproducibility)
- **Audit-trail question**: "which gate event is this verdict?" (identity)

Endorse splitting into two emitted hashes on each verdict line:

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> audit_sha256=<audit_closure> content_sha256=<content_closure>
```

- `audit_sha256`: computed from self_script + session + gate_id + machinery_pin_map keys (NOT input-file BYTES) — immutable per gate event, survives input-file modifications.
- `content_sha256`: computed from input-file BYTES + machinery_pin_map values — breaks when inputs change, correctly flagging non-reproducibility.

A verdict is AUDITABLE iff audit_sha256 is unique in the session file. A verdict is REPRODUCIBLE iff recomputing content_sha256 under the current tree matches. Today's G59 FAIL is "audit_sha256 collision AND content_sha256 non-reproducibility"; with the split, the audit trail would be preserved even after canonical_constants.py byte drift.

**Cardinality view of the G59 fix**: the preimage entropy of the current closure is log2(1) = 0 bits for "which of {W1-1-TD, W2-13, W3-7}" — a pure collision. With self_script_sha, entropy rises to 3 bits (all three scripts distinct). With session_stamp + gate_id_stamp, entropy is strictly bounded below by log2(N_gates_per_session_squared). G59's "1/3 distinct" verdict is an information-theoretic measurement: the closure space collapses to a single bin. The fix restores full gate-discrimination.

### K3: Completion-Verification as Post-Dispatch Existence-Hook

**Framing**: An agent's `task-complete` signal is an assertion about filesystem state. The filesystem is the physical observable; the agent's self-report is a measurement claim. Current architecture TRUSTS the measurement without CHECKING the observable. This is equivalent to a quantum measurement that records a detector click without the detector actually firing — the apparatus is broken. The v2 rule in `agent-standards.md` §Completion Verification describes the required check but does not ENFORCE it structurally; the orchestrator performs it by hand, and the S83 plan-context note reports ~14 dispatches / ~13 gates required intervention.

**Scrambling distance between agent-claim and filesystem-state**:

Define:

```
D_COMP(dispatch_d) := Σ_{target t in promised_artifacts(d)} [1 - I(exists(t) AND content_valid(t))]
```

where `I(...)` is the indicator function and `content_valid` = `lines_between_delimiters(t) >= min_stub_threshold` (per §Completion Verification bullet 1, `<15 lines = stub`). If `D_COMP(d) > 0`, at least one promised artifact is missing or stub.

**Substitution chain for PASS-iff-zero-missing**:
- Step 1 (definition). `promised_artifacts(d) = { verdict_line, script_file, data_file, plot_file, working_paper_section, memory_file }` extracted from dispatch d's prompt.
- Step 2 (substitution). For each t in promised_artifacts, evaluate `exists(t)` via `Path(t).exists()` and `content_valid(t)` via line-count or SHA-non-empty check.
- Step 3 (simplify). `D_COMP(d) = Σ [1 - I_t]`. If all targets exist and validate, `D_COMP = 0`.
- Step 4 (direction). `D_COMP(d) > 0 ⇒ dispatch d's completion claim is FALSE ⇒ re-dispatch required (or explicit carry-forward).`
- Step 5 (conclusion). Post-dispatch PASS iff `D_COMP(d) = 0`. Structurally enforceable by a hook.

**Post-dispatch existence hook** (proposed infrastructure, `D_COMP == 0` structural enforcement):

Create a PostToolUse hook `completion-verify.sh` that fires after every `Task` (Agent) tool completion in compute mode:

```bash
# .claude/hooks/post-agent/completion-verify.sh
# Runs after every Task tool completion during session compute mode.
# Inputs (env): TASK_PROMISED_ARTIFACTS (JSON array), TASK_SESSION_NUMBER, TASK_GATE_ID
# Exit 0 = PASS (all artifacts on disk, content valid).
# Exit 1 = FAIL (at least one artifact missing/stub).

set -euo pipefail
missing=0
for artifact in $(echo "$TASK_PROMISED_ARTIFACTS" | jq -r '.[]'); do
    if [[ ! -f "$artifact" ]]; then
        echo "MISSING: $artifact"
        missing=$((missing + 1))
    elif [[ "$artifact" == *.md ]]; then
        # Section content check — count lines in the section delimited by the gate_id
        line_count=$(awk "/^### .*${TASK_GATE_ID}/{flag=1; next} /^### /{flag=0} flag" "$artifact" | wc -l)
        if [[ "$line_count" -lt 15 ]]; then
            echo "STUB: $artifact (section <15 lines)"
            missing=$((missing + 1))
        fi
    fi
done
if [[ "$missing" -gt 0 ]]; then
    # Emit injection to the orchestrator: dispatch a minimal write-only re-try.
    echo "{\"additionalContext\": \"Agent dispatch incomplete: $missing artifacts missing/stub for gate $TASK_GATE_ID. Re-dispatch with write-only follow-up.\"}"
    exit 1
fi
exit 0
```

**Prompt-level discipline** (complementary, not sufficient alone):

Agent dispatch prompts in compute mode must include a STRUCTURED ARTIFACT MANIFEST in the body (not narrative):

```
ARTIFACTS PROMISED (JSON, for post-dispatch verification):
[
  "computations/s{N}_{gate}.py",
  "computations/s{N}_{gate}.npz",
  "computations/s{N}_{gate}.png",
  "computations/s{N}_gate_verdicts.txt",
  "sessions/session-{N}/session-{N}-results-workingpaper.md#§W{i}-G{j}"
]
```

The dispatch template (`.claude/templates/...`) should include this manifest, and the PostToolUse hook parses it from the dispatch metadata. This closes the gap between prompt-level "CRITICAL: write §X.Y IN FULL" admonitions (which v2 showed are INSUFFICIENT) and infrastructure-level existence enforcement.

**Observed mode the hook addresses** (S82-W1-3-CN, W2-15, W3-1; S83 ~13 gates): agent appends verdict line → terminates at "now I need to write §X.Y..." → working-paper section missing or stub. The hook intercepts at the `Task`-completion event and either (a) emits an injection forcing a write-only re-dispatch, or (b) blocks the orchestrator from marking the gate closed until D_COMP = 0. Both paths are structural; neither depends on the orchestrator remembering to verify.

**Why this is a Lyapunov-equivalent**: under v2, the distance between agent-claim-state and filesystem-state GROWS linearly with dispatch count (14 events × λ ~ 1 per dispatch → 14 interventions). Under the hook, λ is clamped to zero by construction — the dispatch does not register as complete until D_COMP = 0. The Lyapunov deviation collapses. This is the same mechanism by which the toric code's syndrome measurement clamps error accumulation: the hook IS the syndrome measurement for dispatch-completion errors.

### K4: Questions for sagan

1. **Rigor-audit stance on the cardinality-enforcement framing**: Is the reframe of PRU v2 (from "run PRDR" to "cardinality check `D_PRU = 0`") within the epistemic-discipline rule's authority, or does it require a new rule-file section? Specifically, does the structural-check "PASS iff D_PRU = 0" belong in `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness (extending current text), or should it live in a new `.claude/rules/pru-cardinality.md` as a machine-checkable spec?

2. **Class 8a (Boundary-inequality) subclass separation**: G4's failure is structurally distinct from the other three (operator-kernel vs value-kernel). Is Class 8a worth a separate named class in the taxonomy, or should it be folded into Class 8 with a note? I lean "separate class" because the mitigation is different (G4 requires the plan to specify `<` vs `<=`, which is orthogonal to pinning a scalar value), but you have better visibility into whether the project's rule-vocabulary burden tolerates another named class.

3. **SHA-split (audit vs content) backward compatibility**: the v3 closure with two SHAs would break the S81-canonical verdict-line parser in `_consolidate_intake.py` (which currently rejects SHAs shorter than 40 hex chars but expects a single sha256=...). Should the v3 spec (a) keep backward compatibility by concatenating the two SHAs into a single field (`sha256=<audit>:<content>`), or (b) introduce two new explicit fields (`audit_sha256=...`, `content_sha256=...`) and version-bump the verdict-line format to S84+? Option (a) is less disruptive but obscures the split; option (b) is cleaner but requires tooling updates.

4. **Completion-Verification hook as BLOCKING vs ADVISORY**: the hook I proposed EXITS 1 on incomplete dispatch, which would block orchestrator progress. Is this too aggressive for the project's autonomous-batch-dispatch culture (feedback_dispatch-discipline.md)? An alternative is ADVISORY mode: the hook emits a warning but does not block, and the orchestrator reviews the warning queue at batch boundaries. Which posture fits the orchestration discipline you've observed in S82-83?

5. **Rule-file diff target count for v3**: my K1/K2/K3 propose edits to 3 files (`epistemic-discipline.md`, `gate-verdicts.md`, `agent-standards.md`) plus potentially `math-scripts.md` if the PRDR cardinality tool requires a new substitution-chain entry. Before we draft line-by-line edits in R2, should we aim for minimal-surface changes (edit existing sections) or substantial restructures (add new sections)? My prior is minimal-surface — the rule-file corpus is already dense; v3 should be tight additions that EACH pass their own cardinality check (the rule-file change itself is a gate, and should obey the discipline it imposes).

6. **S84 test-gate design**: for the pre-registered S84-METHODOLOGY-DEBTS-V3-CLOSURE gate, what is the minimal set of observable signatures that v3 worked? My candidate set: (a) zero new PRU Class 8 flags in S84, (b) zero duplicate closure SHAs in `s84_gate_verdicts.txt`, (c) zero orchestrator-intervention flags in §0.10(b). But (a) is hard to measure absence of — it requires auditing every gate in S84. Is there a positive, constructive signature (something we SHOULD SEE if v3 worked) rather than a negative one (something we should NOT see)?

---

## Round 1 — sagan: Response & Cross-Synthesis

### Part 1: Response to kitaev's Sections

#### Re: K1 — PRU Class 8 Scrambling View

**AGREE on the cardinality reframe. EMERGES on the operator-kernel distinction. MISSED on the root-cause asymmetry.**

*AGREE (cardinality as enforcer, not narrative).* K1's core move — promoting PRU from "run PRDR" to "`D_PRU(g) = 0` structural check" — is the right epistemic move. The v2 rule text in `epistemic-discipline.md` §Pre-Registration Completeness describes PRDR procedurally ("before a gate is frozen into the plan, dry-run the producing script, enumerate every free parameter via static analysis") without specifying the ACCEPTANCE CRITERION for PRDR completion. A rule that says "enumerate" without a cardinality-pass test is a rule that cannot fail — it admits a non-empty kernel silently. S83's 4-flag recurrence (G4, G11, G15, G36) empirically validates that claim: PRDR was putatively run at plan-write time, yet `D_PRU > 0` held for four gates. The rule did its job procedurally and still failed to enforce the invariant.

The substitution chain at K1 Steps 1-5 is correctly constructed: `D_PRU(g) = |F_script(g) \ keys(F_plan(g))| = 0` iff every script-consumed parameter is plan-pinned iff verdict is plan-deterministic. This is a well-defined set-containment check. It is checkable by tooling in ~10 lines of Python `ast`-module code. This is the Sagan-Venus standard: a test that could FAIL if the rule were empty.

**Python verification of K1's S83 ledger (substitution chain):**
- Step 1 (definition). For each flagged gate g, `D_PRU(g) := |F_script(g) \ keys(F_plan(g))|`.
- Step 2 (substitution from K1 Table, rows 1-4). D_PRU(W1-G4)=1 (operator-kernel); D_PRU(W2-G11)=1 (ternary normalization); D_PRU(W2-G15)=1 (binary Lambda_Z); D_PRU(W3-G36)=3 (sign, V-normalization, Delta-fix).
- Step 3 (simplification). Sum over flagged gates: `total_kernel = 1 + 1 + 1 + 3 = 6`.
- Step 4 (direction). `total_kernel > 0 ==> v2 PRDR failed to enforce D_PRU = 0 ==> v3 requires cardinality tooling`.
- Conclusion. v2 is a VERSION-1 rule (narrative procedure); v3 must be VERSION-2 (cardinality check with tooling). AGREE.

*EMERGES (Class 8a as OPERATOR-kernel vs VALUE-kernel).* K1's proposal to split Class 8a (G4-type) out from Class 8 (G11/G15/G36-type) is NEW to the v2 taxonomy and is warranted. The mitigations are structurally different:
- Value-kernel (Class 8): pinning a scalar (`convention=W2-canonical-0.025-slope`; `Lambda_Z=M_KK`; `Delta-fix=frozen-at-0.464255`). One entry in the machinery-pin map per free scalar.
- Operator-kernel (Class 8a): pinning a relational operator (`F_traj < 1.5` vs `F_traj <= 1.5`). This is NOT a scalar pin — it is a predicate specification. The machinery-pin map must carry a BOOLEAN tag per threshold (`strict_PASS_boundary: True|False`) in addition to the numerical threshold value.

The distinction matters empirically because G4's F_traj = 1.500000 is NOT a numerical accident but the exact rational 3/2 that falls out of the Lizzi a_2-slot Mellin ratio `f_2^zeta / f_2^SDW = 1 / (2/3) = 3/2`. The threshold was placed AT a structurally reachable value, and the boundary-operator ambiguity converted a PASS-at-threshold into an INFO. A value-kernel audit would have checked "is 1.5 pinned?" — it is. An operator-kernel audit would have checked "is `<` vs `<=` pinned?" — it is not. v3 must cover both.

*MISSED (root-cause asymmetry between G36 and the others).* K1's cardinality-counting treats D_PRU(G36) = 3 as three independent unpinned axes. On review of §W3-G36 lines 4514-4522, the three flags are partially NESTED: (a) sign handling forced the log-of-negative NaN, which in turn (b) motivated the V-rescaled magnitude fit, which (c) required Delta to be fixed rather than gap-equation-self-consistent. The three unpinned axes are not orthogonal — they COUPLED into a single structural choice at execution time. The audit tool needs to report BOTH the raw cardinality (which K1's 10-line script computes correctly) AND a coupling-graph annotation when unpinned axes resolve together. Without the coupling annotation, D_PRU=3 looks three times worse than D_PRU=1, when in structural terms G36 is ONE decision expressed over three pin slots. Budget this in R2's rule-file edits as a secondary annotation, not a change to the cardinality enforcer.

*Not raised by K1.* The PRU Class 8 framing was added to `epistemic-discipline.md` AFTER S78 (see rule text lines 96-101). S83's 4 flags are the second in-session recurrence under the new rule. The cardinality enforcer is necessary but not sufficient — S83 also exhibited a pattern where PRDR was nominally run but the plan-author's enumeration missed the operator axis entirely (G4). The v3 spec must include a PRDR-completeness audit of the enumeration itself, not just the cardinality count.

#### Re: K2 — SHA-Collision Hashing

**AGREE on the information-theoretic framing. AGREE on the 4 discriminators. AGREE on audit/content split. DISAGREE on the backward-compatibility posture.**

*AGREE (preimage entropy is the right metric).* K2's information-theoretic reframe of the G59 failure is correct and quantitatively precise. The substitution chain at Steps 1-5 holds.

**Python verification of preimage entropy (substitution chain):**
- Step 1 (definition). Conditional entropy `H(gate | SHA) = -sum_{g} P(g | SHA=s) log2 P(g | SHA=s)`.
- Step 2 (substitution). For the three S82 gates colliding on `SHA = 5aef2c40...e56d8`, the posterior given the SHA is uniform over {W1-1-TD, W2-13, W3-7}: `P(g | SHA) = 1/3`.
- Step 3 (simplification). `H(gate | SHA) = -3 * (1/3) * log2(1/3) = log2(3) ~= 1.584963 bits`.
- Step 4 (direction). Required: `H(gate | SHA) = 0` (SHA uniquely determines gate). Observed: `H = 1.585 bits`. Entropy deficit: `1.585 bits`.
- Conclusion. The SHA carries ~1.585 bits less gate-discrimination than required. AGREE with K2's framing.

This is not a cryptographic hash collision — SHA-256 is cryptographically strong. It is a COLLISION BY CONSTRUCTION of the preimage: the payload fed into the hash function is byte-identical across three gates because the input-file-only closure algorithm cannot see the gate's other execution context. K2's diagnosis is exactly right.

*AGREE (on the 4 discriminators — Shannon-additive).* The four proposed discriminators (self_script_sha, session_stamp, gate_id_stamp, machinery_pin_map) are the minimum needed to saturate gate-discrimination:

- **self_script_sha**: injective per script; at N_gates per session ~20-60, adds log2(N_gates) ~ 4.3 - 5.9 bits. Necessary because one script per gate is the S81+ convention.
- **session_stamp**: adds log2(N_sessions_lifetime) bits of discrimination across session boundaries. At current N=83, that is ~6.4 bits. Prevents cross-session collision when S83+ scripts inherit an S82 template.
- **gate_id_stamp**: adds log2(N_gates_per_script) ~ 0-1 bits (most scripts run one gate; meta-gates run several). Small but necessary for closure under the rare meta-gate case.
- **machinery_pin_map**: adds log2(|possible_machinery_states|) — this is the discriminator that ties K2 to K1. If PRDR has pinned all machinery (D_PRU = 0 per K1), then the machinery-pin map is a single deterministic string and enters the SHA. This is the K1-K2 CROSSOVER: the K1 audit tool's output (the pinned machinery map) becomes an input to the K2 audit closure.

*AGREE (audit-SHA vs content-SHA split).* The split makes two orthogonal audit questions — "which gate event is this verdict?" (identity) and "did these specific input bytes produce this verdict?" (reproducibility) — independently auditable. Under the single-SHA S81 scheme, G59 shows BOTH semantics fail at once: collision (distinct_count=1/3) AND non-reproducibility (recorded 5aef2c... vs recomputed fbc1fa10...). Under the split, the content_sha256 would have flagged non-reproducibility (as now), and a DIFFERENT audit_sha256 per gate would have preserved the audit trail. AGREE unconditionally.

*DISAGREE on backward-compatibility (answering K4 question 3).* K2 offered two options: (a) concatenate as `sha256=<audit>:<content>` (less disruptive), or (b) introduce two new fields `audit_sha256=...`, `content_sha256=...` and version-bump the verdict-line format to S84+. I argue for **option (b)** despite higher disruption cost:

Rationale (substitution chain for the tooling-cost claim):
- Step 1 (definition). The `_consolidate_intake.py` parser at line 56-58 of `.claude/rules/gate-verdicts.md` rejects SHAs shorter than 40 hex chars. A 129-char concat field (`:`-separated 64-char pair) would pass the length check but confuses downstream parsers that do `sha256=<64-hex>` regex extraction.
- Step 2 (substitution). The knowledge MCP's `search_knowledge` / `trace_entity` tools currently index the single-SHA field. A concat field forces a schema change in the indexer whether we pick (a) or (b) — so tooling migration is unavoidable in either case.
- Step 3 (simplification). Migration cost is roughly equal; option (b) is SEMANTICALLY CLEANER because the two questions are labeled independently. Option (a) buries the split behind a delimiter that is easy to forget.
- Step 4 (direction). Given equal cost + semantic cleanliness gap, choose (b). Version-bump the verdict-line format to S84+; provide a backward-compat parser shim that accepts the single-SHA form for pre-S84 verdicts and the dual-SHA form for S84+.
- Conclusion. Option (b): `audit_sha256=<audit_closure> content_sha256=<content_closure>`. Additional verdict-line field `schema_version=S84+` for clarity.

*Nuance not fully addressed by K2.* The G59 failure has a THIRD contributor beyond the cardinality collision: `canonical_constants.py` has uncommitted modifications since HEAD (§W3-G59 Root-cause-2, lines 6938-6939). Even with the 4 discriminators, if the canonical input file drifts post-verdict, `content_sha256` cannot be reproduced. K2's audit/content split addresses this correctly: the audit SHA remains stable, the content SHA correctly FAILs. But it is worth an explicit rule-file line: "canonical inputs that enter closure SHAs must be SHA-pinned at session boundaries (archive per-session frozen copies or record session-end SHA in the plan)." This is K2's CF-59-B, which I endorse, though it did not appear in K2's Round-1 proposal text in the workshop.

#### Re: K3 — Completion-Verification Hook

**AGREE on the Lyapunov framing. AGREE on the hook architecture. DISAGREE on BLOCKING-posture as default. EMERGES on artifact-manifest format.**

*AGREE (Lyapunov framing).* K3's framing of the agent-claim vs filesystem-state gap as a Lyapunov deviation is correct: under v2, the gap grows LINEARLY with dispatch count (per the S83 plan-context note citing ~14 dispatches / ~13 gates requiring intervention). A structural hook that clamps the deviation at `D_COMP = 0` is the right fix. The substitution chain at K3 Steps 1-5 holds:

**Python verification of D_COMP linearity (substitution chain):**
- Step 1 (definition). `D_COMP(dispatch_d) = sum_{t in promised_artifacts(d)} [1 - I(exists(t) AND content_valid(t))]`.
- Step 2 (substitution, S83 observed). Per S83 plan-context: ~13 of ~50+ dispatches (roughly 25-30%) required post-hoc intervention for missing working-paper sections or stub content. For a session with N dispatches and intervention rate p ~ 0.25, total interventions scale as `N * p`.
- Step 3 (simplification). Per-dispatch expected missing-artifact count `E[D_COMP(d)] ~ p ~ 0.25` under v2. Session-total expected interventions `E[sum_d D_COMP(d)] = N * p`. Linear in N.
- Step 4 (direction). Hook-clamped regime: `D_COMP(d)` is enforced to 0 before marking gate closed; the dispatch event does not terminate cleanly until every promised artifact passes existence + content-valid. Total interventions = 0.
- Conclusion. v2 -> v3 with hook: linear -> zero scaling of interventions. AGREE.

The toric-code syndrome-measurement analogy is apt: under v2, completion errors accumulate unbounded; under v3, the hook IS the syndrome that clamps accumulation. This is structurally equivalent to the K1 cardinality check — both convert a procedural rule into a structurally-enforced invariant.

*AGREE (hook architecture).* The PostToolUse hook architecture at `.claude/hooks/post-agent/completion-verify.sh` is sensible. The env-variable passthrough (`TASK_PROMISED_ARTIFACTS` as JSON array) works with the existing Claude Code infrastructure. The 15-line stub-content threshold matches the existing rule text in `agent-standards.md` §Completion Verification bullet 1. The `awk`-based section-content check is robust to the existing working-paper delimiter convention.

*DISAGREE on BLOCKING as default (answering K4 question 4).* K3 proposed the hook EXITS 1 on incomplete dispatch, which would block orchestrator progress. I argue this is TOO AGGRESSIVE for the autonomous-batch-dispatch culture (per user feedback `feedback_dispatch-discipline.md`).

Rationale (substitution chain for the posture choice):
- Step 1 (definition). BLOCKING posture: `exit 1` prevents the orchestrator from proceeding to the next dispatch in the batch until the current dispatch's D_COMP = 0 is confirmed. ADVISORY posture: `exit 0` always, emit a warning to a review queue, orchestrator reviews at batch boundaries (after wave completion).
- Step 2 (substitution). Under BLOCKING, a single stub dispatch stalls the entire batch (per `feedback_dispatch-discipline.md`, batches are launch-all-wait-all-launch-next). At ~25% intervention rate, 2-3 out of every 8-agent batch would block; cascading stalls across waves.
- Step 3 (simplification). Under ADVISORY + batch-boundary review, the hook records all missing-artifact events; the orchestrator reviews the queue at each wave boundary. Worst case: one write-only re-dispatch wave per 8-agent wave. Best case: queue is empty, no re-dispatch.
- Step 4 (direction). ADVISORY preserves autonomous-batch flow; BLOCKING breaks it. Per user feedback "in compute mode don't ask between batches/waves", BLOCKING on every dispatch violates the compute-mode discipline.
- Conclusion. DEFAULT = ADVISORY. ESCALATION to BLOCKING should be triggered only when a dispatch is on the CRITICAL PATH of a downstream dispatch (i.e., when gate X's output is input for gate Y in the same wave). For non-critical-path dispatches, ADVISORY + wave-boundary review is the correct posture.

Implementation detail for v3: the hook should emit a structured warning to `.claude/hooks/completion-queue.jsonl` (one line per incomplete dispatch) and exit 0 by default. The orchestrator reads this file at wave boundaries and either (a) dispatches a write-only follow-up for each queued entry, or (b) marks the gate as PASS-with-text-deferred and logs an explicit carry-forward per `agent-standards.md` §Completion Verification bullet 3.

*EMERGES (artifact-manifest format).* K3's proposal for a structured ARTIFACTS PROMISED JSON block in the dispatch prompt is new and useful. I extend it with two additions:

1. **Minimum-line-count per artifact type** (varies by artifact): verdict line = 1, script = 50 (non-stub threshold), data_file .npz = 1 key, working-paper-section = 15 (per existing rule). A blanket 15-line check is wrong for short artifacts like single-line verdict entries.

2. **Gate-ID-anchored section extraction**: the awk command in K3's hook uses `^### .*${TASK_GATE_ID}` as the section delimiter. This works only if the working-paper section header matches the `### W{i}-G{j}: <GATE_ID>` pattern strictly. The S83 working paper follows this pattern; v3 should codify it as REQUIRED in the working-paper shells-first template (per user feedback `feedback_session-process.md`).

*Nuance not addressed by K3.* S83's ~13 interventions are a LOWER BOUND — they are the interventions the orchestrator NOTICED. Silent failures (dispatch claimed complete, artifact missing, orchestrator missed the gap) are unmeasured. The hook converts unmeasured silent failures into measured hook events, which is a GAIN in auditability even independent of the re-dispatch decision. Worth noting in R2.

### Part 2: Original Analysis — Rigor Audit + Rule-File Edits

#### R1: Structural-Check Catch-Point per Debt (Design-Time vs Run-Time vs Post-Time)

The three phases map to three structurally distinct enforcement mechanisms:
- **Design-time (PRDR)**: plan-write phase. Audit operates on the plan document and the producing script. Catches plan-property failures before any computation runs. Cheapest correction.
- **Run-time (dispatch interlock)**: agent-dispatch phase. Audit operates on the dispatch prompt and live filesystem. Catches in-flight failures before the orchestrator commits to the result.
- **Post-time (audit)**: session-close phase. Audit operates on the complete verdict file and all session artifacts. Catches residual failures that slipped through the prior phases. Most expensive correction (requires re-dispatch or carry-forward).

A given debt can be caught at multiple phases. The RIGHT phase is the EARLIEST one where the check has sufficient information to succeed — catching earlier is cheaper but may require information not yet present.

| Debt | Right Catch-Point | Rationale | Residual Post-Time Audit |
|:-----|:-----------------|:----------|:-------------------------|
| **PRU Class 8 (value-kernel; G11, G15, G36)** | **Design-Time (PRDR)** | The producing script is finished before the plan block is frozen. Static analysis (Python `ast`) enumerates `argparse`, globals-read, convention-switches BEFORE dispatch. The plan's machinery-pin block is a set. The check `set(keys(F_plan)) >= F_script_free_parameters` is a pure design-time operation. No run-time information needed. | Session-close: re-run `_pru_cardinality_audit.py` over all gate blocks; any non-zero D_PRU is a PRU flag for the session handoff. |
| **PRU Class 8a (operator-kernel; G4)** | **Design-Time (PRDR) + Template** | Operator ambiguity between `<` and `<=` at a threshold is purely a plan-property. The PRDR template must require a boolean `strict_PASS_boundary: True|False` per numerical threshold. This cannot be inferred from the script alone (script returns a numerical value; the operator lives in the plan-interpretation of that value). Template addition, not just tool. | Session-close: grep all gate blocks for threshold entries missing the strict_PASS_boundary tag; flag for v3+ compliance. |
| **SHA-collision (G59 single-INPUT_FILES)** | **Run-Time (dispatch interlock)** + **Post-Time** | The closure SHA is computed at script-execution time from live file bytes. Design-time cannot compute it (file bytes may change between plan-write and dispatch). The K2 discriminator expansion (self_script_sha, session_stamp, gate_id_stamp, machinery_pin_map) MUST be injected at script-execution time, before the SHA is written to the verdict line. Run-time catch. **ALSO** post-time: the session-close audit must verify SHA-uniqueness in `s{N}_gate_verdicts.txt` and flag any duplicates (the existing `agent-standards.md` §Completion Verification bullet 3 check, which already catches this category but did not in S83 because the check ran on ONE session's verdicts, not across the INPUT_FILES redundancy). | Post-time: SHA-uniqueness across session verdict files AND cross-session trace when canonical input files drift. |
| **Completion-Verification (working-paper stubs)** | **Run-Time (dispatch interlock)** | The filesystem state at dispatch-completion is checkable only at dispatch-completion time. The artifact-manifest in the dispatch prompt enables a PostToolUse hook to verify each promised target. Design-time cannot check filesystem state that does not yet exist. Post-time can catch residual cases, but the damage (orchestrator marking gate closed) is already done. | Post-time: session-close cross-reference between `s{N}_gate_verdicts.txt` and working-paper §W{i}-G{j} section existence — any verdict line without a corresponding substantive section is flagged. |

**Why design-time catch is right for PRU (not run-time)**: The K1 cardinality check is PURE STATIC ANALYSIS. It needs only the script text and the plan block — both finished before dispatch. Running it at dispatch time would catch the failure but at higher cost (the agent is already spun up, the dispatch prompt is in flight). S83's 4 PRU flags are empirical evidence that design-time enforcement is the right choice — all four could have been caught by a 10-line `ast`-based tool on the unfrozen plan + script pair.

**Why run-time catch is right for SHA-collision (not design-time)**: The SHA depends on live file bytes. At design-time, the closure SHA is `sha256(<unknown bytes>) + <unknown machinery pins>`; the closure value is not computable until the script runs. What IS computable at design-time: the DISCRIMINATOR SCHEMA (does the template include self_script_sha? session_stamp? gate_id_stamp?). Design-time audit of the template completeness; run-time computation of the SHA itself. v3 needs both: design-time schema audit + run-time SHA computation with K2 discriminators.

**Why run-time catch is right for Completion-Verification (not design-time, not post-time)**: The dispatch-completion event is a PHYSICAL OBSERVABLE (filesystem state at time `T_complete`). Design-time cannot query a future filesystem state. Post-time catches the failure but only after the orchestrator has moved past it (the wave is done, the batch has advanced, the next dispatch has spun up). Run-time hook is the unique phase where both the information is available AND the damage is preventable. ADVISORY posture (per Re:K3) preserves batch flow while still recording the failure.

**Secondary catch-points (all debts, post-time)**: Even under the right-phase enforcement, a session-close audit sweep (`/weave --update` extension, or a new `_session_close_audit.py`) should verify ALL three invariants as a tripwire:
1. `for gate g in s{N}_plan: D_PRU(g) == 0` (including operator-kernel boolean)
2. `len(set(verdict_line.sha256 for verdict_line in s{N}_verdicts)) == len(s{N}_verdicts)` AND every SHA re-computes against the session-pinned inputs
3. `for verdict in s{N}_verdicts: exists(working_paper_section(verdict.gate_id)) AND line_count_between_delimiters(..) >= min_threshold`

This is the Sagan-Venus standard: the rule has teeth only if a final check can FAIL the session. A session-close audit that passes despite violations would falsify v3. The audit must itself be pre-registered as an S84 test-gate (answering K4 question 6 below).

#### R2: Line-by-Line Rule-File Edits for v3

Minimal-surface additions (answering K4 question 5): each rule-file change is a TIGHT insert at an existing section, not a restructure. The rule-file corpus is already dense; v3 extends rather than rewrites.

##### R2.1: `.claude/rules/epistemic-discipline.md` — PRU Cardinality + Class 8a

**Target lines 96-111 (current `## Pre-Registration Completeness` section).**

INSERT after current line 101 (after `A scrubbed plan that prevents all 7 execution failures but does not pre-register machinery via PRDR remains PRU-vulnerable.`):

```
- **PRU enforcement (v3, S84+)**: PRDR §0.10(d) PASSES iff the cardinality
  check `D_PRU(g) = |F_script(g) \ keys(F_plan(g))| = 0` holds for every
  gate `g` in the plan. `F_script(g)` is enumerated by static analysis
  of the producing script (Python `ast` module, top-level argparse +
  globals-read + convention-switches). `F_plan(g)` is the set of keys
  in the plan's machinery-pin block for gate `g`. The check is
  automated by `computations/_pru_cardinality_audit.py` (per K1
  proposal). A plan that emits `D_PRU(g) > 0` for any gate is
  PRE-REG-INCOMPLETE and cannot proceed to dispatch.

- **PRU Class 8a (operator-kernel subclass)**: distinct from Class 8
  value-kernel failures, Class 8a is the case where a relational
  operator (`<` vs `<=`, `>` vs `>=`) applied to a pre-registered
  threshold is left unpinned. Detection: for each numerical threshold
  in the gate block, the plan must specify a boolean
  `strict_PASS_boundary: True|False`. The PRDR cardinality check's
  `F_script(g)` enumeration must include `threshold_comparison_operator`
  as a free parameter whenever the computed value can land on the
  boundary exactly (which occurs at rational thresholds reachable by
  the canonical scheme). S83 §W1-G4 (F_traj = 3/2 = 1.500000 exactly)
  is the canonical Class 8a failure.
```

INSERT new section after current `Pre-Registration Completeness`:

```
## Post-Session Completeness Audit

Session close MUST run three audits, all pre-registered at session start:

1. **PRU-closure audit**: re-run `_pru_cardinality_audit.py` over every
   gate block in `s{N}_plan`. All gates must have `D_PRU = 0`. Any
   non-zero entries are logged to the handoff and carried forward as
   pre-registration fixes for S{N+1}.

2. **SHA-uniqueness audit**: enforce two invariants on
   `s{N}_gate_verdicts.txt`:
   - (a) `len(set(verdict.audit_sha256)) == len(verdicts)` (no audit
     collisions across the session).
   - (b) every `verdict.content_sha256` recomputes against the
     session-pinned inputs (reproducibility).
   Either invariant failing flags the session for v3+ compliance.

3. **Completion-artifact audit**: for every verdict line, verify a
   corresponding substantive working-paper section exists (line count
   between `### W{i}-G{j}` delimiters >= 15).
```

##### R2.2: `.claude/rules/gate-verdicts.md` — Dual-SHA Closure + Machinery-Pin Extension

**Target lines 35-44 (current `## Verdict Format` S81+ canonical form block).**

REPLACE current line 58-60 (inside the S81+ canonical form code block):

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
```

WITH (v3 dual-SHA form, S84+):

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> audit_sha256=<audit_closure> content_sha256=<content_closure> schema_version=S84+
```

APPEND below line 60 (after the canonical form block):

```
**S84+ closure semantics**:
- `audit_sha256 = sha256(self_script_sha || session_stamp ||
  gate_id_stamp || sorted(machinery_pin_map keys))` — immutable per
  gate event, survives input-file byte drift. Answers "which gate
  event is this verdict?"
- `content_sha256 = sha256(sorted(input_pin_map))` — the existing
  S81+ closure. Changes when inputs change. Answers "did these input
  bytes produce this verdict?"

Backward compatibility: pre-S84 verdict lines using single `sha256=...`
form remain valid; `_consolidate_intake.py` accepts both forms via
an S{N}-detection check. See K2 Re: for preimage-entropy derivation.

**Canonical input archival**: any file referenced in `content_sha256`'s
input pin map must be session-frozen. Options: (a) archive as
`canonical_constants_s{N}_frozen.py` at session-close, (b) record
session-end SHA in the plan's frozen-constants block. Without archival,
`content_sha256` is not reproducible after input-file drift (the S82 ->
S83 drift that drove G59's non-reproducibility).
```

REPLACE current §Rules line 76-80 (the PRU Class 8 paragraph):

```
- A gate that cannot be evaluated because its producing machinery is unpinned
  (PRU Class 8) is NOT a FAIL — it is PRE-REG-INCOMPLETE. Pin the machinery
  via PRDR (Pre-Registration Dry-Run, `.claude/rules/epistemic-discipline.md`)
  before marking PASS/FAIL.
```

WITH:

```
- A gate that cannot be evaluated because its producing machinery is
  unpinned (PRU Class 8 value-kernel, or Class 8a operator-kernel) is
  NOT a FAIL — it is PRE-REG-INCOMPLETE. Pin the machinery via PRDR
  (Pre-Registration Dry-Run, `.claude/rules/epistemic-discipline.md`)
  before marking PASS/FAIL. The PRDR PASSES iff `D_PRU(g) = 0` for the
  gate (cardinality check).
- For Class 8a (operator-kernel), the machinery-pin block must include
  `strict_PASS_boundary: True|False` for every threshold reachable by
  the canonical scheme's rational values. S83 §W1-G4 established
  F_traj = 3/2 as a reachable Mellin-ratio threshold.
- Every S84+ gate block must include a `machinery_pin_map` dictionary
  whose sorted keys feed the `audit_sha256` closure. Absence of the
  dictionary triggers the SHA-collision failure mode documented in
  S83 §W3-G59.
```

##### R2.3: `.claude/rules/agent-standards.md` — Completion-Hook Architecture

**Target lines 17-38 (current `## Completion Verification` section).**

APPEND after current line 31 (after mitigation-2's closing sentence):

```
4. **Post-dispatch existence hook (v3, S84+)**: infrastructure-level
   artifact verification. The hook `.claude/hooks/post-agent/
   completion-verify.sh` fires after every Task tool completion in
   compute mode. Inputs: `TASK_PROMISED_ARTIFACTS` (JSON array),
   `TASK_SESSION_NUMBER`, `TASK_GATE_ID`. The hook computes
   `D_COMP(d) = sum_t [1 - I(exists(t) AND content_valid(t))]`. Under
   ADVISORY posture (default), `D_COMP > 0` emits a warning to
   `.claude/hooks/completion-queue.jsonl` and the orchestrator reviews
   at wave boundaries. Under BLOCKING posture (opt-in for critical-
   path dispatches), `D_COMP > 0` exits 1 and halts the orchestrator.

   Agent dispatch prompts in compute mode MUST include a structured
   ARTIFACTS PROMISED JSON block in the prompt body:

       ARTIFACTS PROMISED (JSON, for post-dispatch verification):
       [
         "computations/s{N}_{gate}.py",
         "computations/s{N}_{gate}.npz",
         "computations/s{N}_{gate}.png",
         "computations/s{N}_gate_verdicts.txt",
         "sessions/session-{N}/session-{N}-results-workingpaper.md#§W{i}-G{j}"
       ]

   Minimum-valid thresholds per artifact type: `.py` >= 50 lines;
   `.npz` >= 1 key; `.png` >= 1 byte (existence only); verdict line = 1
   appended line matching `{GATE_ID}: (PASS|FAIL|INFO)` regex; working-
   paper section >= 15 lines between `### W{i}-G{j}` delimiters.
```

**Target lines 33-34 (current bullet 3 on SHA uniqueness).** 

APPEND:

```
   Under v3 (S84+), the SHA-uniqueness check fires on `audit_sha256`
   (not `content_sha256`). A duplicate `audit_sha256` indicates a
   cross-gate discriminator collision (K2's information-theoretic
   failure mode) and must be corrected by adding the missing
   discriminator (self_script_sha, session_stamp, gate_id_stamp, or
   machinery_pin_map entry).
```

##### R2.4: `.claude/rules/math-scripts.md` — PRDR Substitution-Chain Requirement

**Target lines 96-100 (current `### Enforcement` subsection under `## Double-Check Logic Before Compute`).**

APPEND after current line 100 (end of Enforcement subsection):

```
- **PRDR substitution-chain requirement (v3, S84+)**: the PRDR dry-run
  output (§0.10(d) in session plans) must include, for every gate with
  a sign/direction/threshold claim, the explicit substitution chain at
  plan-write time — not deferred to execution. The PRDR PASSES iff
  the substitution chain is present AND the cardinality check
  `D_PRU(g) = 0` holds. Absence of the chain on a sign/direction claim
  is treated as a Class 8a PRU failure (unpinned direction axis).
- **Class 8a operator-kernel recognition**: when a PRDR enumeration
  encounters a numerical threshold reachable by an analytic rational
  (e.g., 1/2, 2/3, 3/2 from Mellin-slot ratios), the machinery-pin
  block MUST specify `strict_PASS_boundary` as a boolean. The
  substitution chain's Step 4 (direction read-off) cannot be
  well-defined when the computed value lands on the threshold and the
  operator is unpinned.
```

**Target: Canonical-Constants section lines 11-21 — cross-link to PRU audit.**

APPEND a new bullet to the closing of §Canonical Constants:

```
4. **Canonical input archival (v3, S84+)**: when a canonical-constants
   file is referenced as an `INPUT_FILES` entry for a gate's closure
   SHA, its session-end SHA MUST be archived (either as a frozen-copy
   file or as a plan-level pin). See `gate-verdicts.md` §Canonical
   input archival. Without archival, `content_sha256` recomputation
   breaks after any byte drift in the file.
```

##### R2.5: Summary table of edits

| File | Section | Type | Lines | Purpose |
|:-----|:--------|:-----|:------|:--------|
| epistemic-discipline.md | §Pre-Registration Completeness | APPEND | after L101 | PRU cardinality enforcement |
| epistemic-discipline.md | §Pre-Registration Completeness | APPEND | after L111 | Class 8a operator-kernel subclass |
| epistemic-discipline.md | new §Post-Session Completeness Audit | NEW | after §PRC | session-close tripwire |
| gate-verdicts.md | §Verdict Format canonical form | REPLACE | L58-60 | dual-SHA S84+ format |
| gate-verdicts.md | §Verdict Format | APPEND | below L60 | closure semantics + archival |
| gate-verdicts.md | §Rules PRU block | REPLACE | L76-80 | Class 8 + 8a + machinery_pin_map |
| agent-standards.md | §Completion Verification | APPEND | after L31 | hook-based v3 architecture |
| agent-standards.md | §Completion Verification bullet 3 | APPEND | after L33-34 | audit_sha256 uniqueness |
| math-scripts.md | §Enforcement | APPEND | after L100 | PRDR substitution-chain requirement |
| math-scripts.md | §Canonical Constants | APPEND | end of section | input archival cross-link |

Total: 10 insert/replace sites across 4 files. No file restructures. Every edit is minimal-surface.

#### R3: PRU Class 8a (Boundary-Inequality Convention) New Subclass Template

**Answering K4 question 2**: YES — Class 8a (operator-kernel) warrants a separately-named subclass. The mitigation is orthogonal to Class 8 value-kernel (scalar pinning), and the empirical trigger is structurally distinct (S83 G4 hit an exactly-reachable analytic rational, not a numerical accident). The rule-vocabulary burden of one new named subclass is small; the cost of confusing G4-type failures with G11/G15/G36-type failures in the taxonomy is larger (G4 would keep getting "fix by pinning a scalar" advice, when the correct fix is pinning the operator).

##### Proposed gate-block template additions (v3, S84+)

EXTEND the existing PRU pre-registration template at `.claude/templates/pru-pre-registration-template.md` with the following block structure:

```yaml
# Standard gate pre-registration (Class 8 guard + Class 8a guard)
gate_id: S{N}-{GATE_ID}
trigger: [VERIFY|AUDIT|VERIFY-THEOREM|CHAIN|SIGN]
classification: PHONONIC|GEOMETRIC|PARTICLE|NON-PHONONIC

# Pass/fail/info thresholds with OPERATOR PINNING (Class 8a)
thresholds:
  pass_condition:
    quantity: F_traj            # the computed quantity
    value: 1.5                  # the threshold numerical value
    operator: strict_less_than  # one of: lt | le | gt | ge | eq
    strict_PASS_boundary: true  # boolean; REQUIRED for Class 8a closure
  info_window:
    quantity: F_traj
    lower_value: 1.5
    lower_operator: le          # must be EXPLICITLY SPECIFIED
    upper_value: 2.5
    upper_operator: lt          # must be EXPLICITLY SPECIFIED
  fail_condition:
    quantity: F_traj
    value: 2.5
    operator: ge

# Machinery pin (Class 8 value-kernel closure)
machinery_pin_map:
  L_max: 5
  N_eval: 1024
  convention: substrate-a2-derived
  scheme_list: [zeta, Zubarev, SDW]
  tau_window: [tau_fold - 10, tau_fold + 10]
  random_seed: null             # null if deterministic
  GPU_path: torch_cpu_fallback  # explicit

# Boundary-reachability flag (Class 8a early-warning)
boundary_reachable_analytically: true  # if threshold is a rational
                                       # expressible from canonical
                                       # Mellin ratios, set true and
                                       # strict_PASS_boundary MUST be
                                       # explicitly pinned
reachable_rationals:
  - value: 1.5
    derivation: "f_2^zeta / f_2^SDW = 1 / (2/3) = 3/2"
    provenance: "Lizzi a_2-ratio theorem, S83 §W1-G4"

# Substitution chain pre-registered (math-scripts.md §Enforcement)
substitution_chain:
  step_1_definition: "F_traj := max_R eps_H_R(N) / min_R eps_H_R(N)"
  step_2_substitution: "..."
  step_3_simplification: "..."
  step_4_direction: "F_traj = 3/2 exactly; strict_PASS_boundary=true ==> INFO"

# Input SHA pins (feeds content_sha256 closure)
input_files:
  - path: computations/canonical_constants.py
    precomputed_sha: <hex>  # at plan-write time

# Audit discriminators (feeds audit_sha256 closure, K2)
audit_discriminators:
  self_script: computations/s{N}_{gate}.py
  session: S{N}
  gate_id: {GATE_ID}
  machinery_pin_map_keys: [auto-populated from above]
```

##### Template discipline — what the PRDR tool checks

A PRDR audit of the above template MUST verify, at plan-write time:

1. **Every threshold has `strict_PASS_boundary` set explicitly** (Class 8a enforcement). A `null` or missing entry is a PRU Class 8a failure.
2. **Every `boundary_reachable_analytically: true` flag has a non-empty `reachable_rationals` list** with derivation provenance. If the flag is `false`, the tool does a best-effort sanity check by attempting to express the threshold as a rational function of canonical Mellin weights (`f_2^zeta`, `f_2^SDW`, `f_2^Zubarev`, `f_2^f*`) — if it matches an expressible rational to 6+ digits, the flag must be set to `true`.
3. **`machinery_pin_map` keys match the K1 cardinality check**: static analysis of the producing script enumerates `F_script(g)`; the template MUST have `keys(machinery_pin_map) >= F_script(g)` as set containment (D_PRU = 0).
4. **`audit_discriminators` has all four K2 discriminators present**: self_script, session, gate_id, machinery_pin_map_keys. Missing entries trigger the SHA-collision failure mode.
5. **Substitution chain present for all `[SIGN|VERIFY|AUDIT|CHAIN]` triggers** with 4 named steps (definition, substitution, simplification, direction). Missing steps are Class 8a failures (unpinned direction axis).

##### Example — what G4 would have looked like under v3

Had this template been in force at S83 plan-write time, the §W1-G4 gate block would have required:

```yaml
thresholds:
  pass_condition:
    quantity: F_traj
    value: 1.5
    operator: lt                # plan-author must choose
    strict_PASS_boundary: true  # ==> strict <
  info_window:
    quantity: F_traj
    lower_value: 1.5
    lower_operator: ge          # plan-author must choose
    upper_value: 2.5
    upper_operator: le
boundary_reachable_analytically: true
reachable_rationals:
  - value: 1.5
    derivation: "f_2^zeta / f_2^SDW = 1 / (2/3) = 3/2"
    provenance: "Lizzi a_2-ratio theorem"
```

The PRDR audit would have flagged the `lt`/`ge` pair as MUTUALLY EXCLUSIVE at F_traj = 1.5: the PASS says "strictly less than 1.5" and the INFO-lower says "greater-than-or-equal-to 1.5", leaving NO verdict class for F_traj = 1.5 exactly. Plan author either (a) chooses `le` for PASS and `gt` for INFO-lower (INFO at 1.5+, PASS includes 1.5), or (b) keeps `lt`/`ge` (INFO at 1.5 inclusive). Either is a valid resolution; the plan MUST pick one before freeze. This is the operator-kernel pin.

Had G4 run under v3, the verdict would have been deterministic (either PASS at F_traj = 1.5 under choice (a), or INFO at F_traj = 1.5 under choice (b)). The "sitting exactly on the PASS/INFO boundary" ambiguity — which appeared in §W1-G4 THRESHOLD-BOUNDARY NOTE — would not have existed.

##### Checklist (S84+ plan dispatch gate)

Before a plan block can be frozen and the producing script dispatched:

- [ ] `thresholds.*.operator` explicitly set for every threshold.
- [ ] `thresholds.*.strict_PASS_boundary` explicitly set for every threshold.
- [ ] No overlapping or disjoint verdict classes (every real value of the computed quantity maps to exactly one of PASS/INFO/FAIL).
- [ ] `boundary_reachable_analytically` flag set (true|false) with derivation if true.
- [ ] `machinery_pin_map` keys satisfy D_PRU(g) = 0 against script's static-analysis enumeration.
- [ ] `audit_discriminators` has all 4 K2 discriminators.
- [ ] `substitution_chain` present with 4 steps (definition, substitution, simplification, direction) for any sign/direction/threshold claim.
- [ ] `input_files` entries each have a precomputed SHA pin at plan-write time.

This is the operational form of the cardinality check. A plan that fails any checklist item emits `D_PRU(g) > 0` and cannot proceed.

#### R4: Questions for kitaev

##### Answers to K4 questions 1-6

**K4-1 (rigor-audit stance on cardinality reframe)**: The cardinality-enforcement framing belongs in `epistemic-discipline.md` §Pre-Registration Completeness as an EXTENSION of the existing text, NOT a new rule file. Rationale: the rule-file corpus is already dense (10+ active rules), and splitting Pre-Registration rules across two files (`epistemic-discipline.md` + hypothetical `pru-cardinality.md`) creates discovery friction — agents searching for PRU guidance would need to check both. The cardinality check is the ENFORCER of the existing PRDR rule, not a new conceptual category. The edit proposed in R2.1 (insert after L101) preserves the current scope while adding teeth.

Secondary consideration: `.claude/rules/gate-verdicts.md` §Rules already cross-references `epistemic-discipline.md` for PRU. Keeping the cardinality spec in the same file preserves that cross-reference link and avoids rule-file proliferation.

**K4-2 (Class 8a separate subclass)**: YES — separate named subclass. Mitigation is orthogonal (pinning an operator vs pinning a scalar); empirical trigger is structurally distinct (rational reachability vs run-time convention choice). The rule-vocabulary burden of one new named subclass is smaller than the cost of confusing G4-type failures with G11/G15/G36-type failures in the taxonomy. R3 gives the template separation.

**K4-3 (SHA-split backward compatibility)**: OPTION (b) — introduce two new explicit fields and version-bump to S84+. The substitution chain at my Re: K2 section (Steps 1-4) shows that tooling migration cost is roughly equal between (a) and (b), and (b) has a semantic-cleanliness advantage. Use a backward-compat shim in `_consolidate_intake.py` that accepts `sha256=<hex>` for pre-S84 verdicts and `audit_sha256=<hex> content_sha256=<hex>` for S84+.

**K4-4 (Completion-Verification hook BLOCKING vs ADVISORY)**: ADVISORY by default. The substitution chain at my Re: K3 section (Steps 1-4) shows that BLOCKING would stall ~25% of an 8-agent batch per wave, violating the autonomous-batch-dispatch culture. ADVISORY + wave-boundary review preserves flow while still recording every incomplete dispatch for later remediation. BLOCKING should be an OPT-IN mode for critical-path dispatches only — when gate X's output is input for gate Y in the same wave. See R2.3 for the architectural edit.

**K4-5 (rule-file diff target count)**: MINIMAL-SURFACE additions, 4 files, 10 insert/replace sites total. See R2.5 summary table. No file restructures. The rule-file change is itself a gate; it obeys the cardinality discipline (each edit has pre-registered target lines and purpose).

**K4-6 (S84 test-gate positive signatures)**: K4 correctly identified the asymmetry — absence-of-PRU-flags is hard to measure without auditing every gate. I propose the following POSITIVE constructive signatures for `S84-METHODOLOGY-DEBTS-V3-CLOSURE`:

- **Positive signature 1 (PRU audit presence)**: the S84 handoff document contains a `PRU-Closure Audit Report` section listing every gate with its computed `D_PRU(g)` value. Success signature: ALL entries show `D_PRU(g) = 0`. This is POSITIVE (the report exists and all entries are zero) rather than negative (no flags raised).

- **Positive signature 2 (dual-SHA presence)**: every S84 verdict line in `s84_gate_verdicts.txt` contains BOTH `audit_sha256=<hex>` and `content_sha256=<hex>` fields. Success signature: `grep -c 'audit_sha256=' s84_gate_verdicts.txt == N_gates` AND `grep -c 'content_sha256=' s84_gate_verdicts.txt == N_gates`. This is POSITIVE (the fields are present).

- **Positive signature 3 (completion-hook presence)**: the `.claude/hooks/post-agent/completion-verify.sh` file exists and has non-zero fire-count recorded in `.claude/hooks/completion-queue.jsonl` (even if all fires are `D_COMP = 0`, the hook FIRING proves it is wired in). Success signature: hook file exists + at least one fire event logged per dispatch.

- **Positive signature 4 (S84 plan obeys v3)**: the S84 plan document includes the Class 8a template block for every gate with a numerical threshold, including `strict_PASS_boundary` booleans. Success signature: grep-able presence of the template field in the plan.

- **Positive signature 5 (audit_sha256 uniqueness measurement)**: SHA-uniqueness audit on `s84_gate_verdicts.txt` reports `N_unique_audit_shas / N_gates = 1.0`. This is a POSITIVE numerical measurement (ratio = 1), not an absence claim.

Combined pre-registered PASS: all 5 positive signatures present at S84 session close. FAIL: any one signature missing. This gives the gate a well-defined verdict that can be measured from artifacts on disk, per the Sagan-Venus standard.

##### Follow-up questions for kitaev (Round 2)

**S1**: **Coupling-graph annotation for D_PRU > 1 cases** (noted in Re: K1). W3-G36 had D_PRU = 3, but the three flagged axes (sign, V-normalization, Delta-fix) collapsed into ONE structural execution choice (the log-of-negative NaN forced all three together). The raw cardinality over-counts this as 3x worse than G4/G11/G15 at D_PRU = 1 each. Should the `_pru_cardinality_audit.py` tool emit a coupling-graph annotation (`D_PRU = 3 but 3 axes coupled into 1 decision`) alongside the raw cardinality? If so, how should the coupling be detected from static analysis — by identifying exception-handling branches that resolve multiple parameters together?

**S2**: **Reachable-rationals detection scope** (R3 template checklist item 2). My proposal requires the PRDR tool to auto-detect thresholds that land on rationals expressible in canonical Mellin weights. The current known reachable rationals: 1/2, 2/3, 3/2, 9/8, 8/9 (from `f_2^R` combinations at L_max=5). Is this set complete? Would a threshold at e.g. 1.75 or 4/7 be considered "reachable" under the a_4 or higher-slot weights? If yes, the PRDR tool needs access to the full canonical-weights ledger, which is larger than just the a_2 slot. What's the correct scope — a_2 slot only (S83's observed case), or all Seeley-DeWitt slots up to a_n for some n?

**S3**: **Hook failure mode — agent never completes** (Re: K3, hook architecture). The PostToolUse hook fires after Task-tool completion. But what if the agent NEVER COMPLETES — hangs on a resource-exhausted script, crashes silently, or the parent orchestrator itself is interrupted? The hook would never fire, and `.claude/hooks/completion-queue.jsonl` would not record the dispatch. The session would terminate with missing artifacts AND missing queue entries. Should there be a BELT-AND-SUSPENDERS periodic sweep (e.g., at wave boundaries, the orchestrator lists all expected gate IDs from the plan and verifies each has BOTH a verdict line AND a queue entry)? This is essentially another post-time tripwire, duplicating the run-time hook.

**S4**: **Dispatch-prompt artifact manifest generation** (R2.3 addition). My proposal requires agent dispatch prompts to include a structured JSON artifact manifest. Currently, the orchestrator writes dispatch prompts by hand (per `.claude/skills/rclab-review/`). Should the manifest be auto-generated from the gate's pre-registration block (which has `input_files`, `script_path`, `working_paper_section` already), or should the prompt-writer copy it in manually? Auto-generation avoids drift; manual copy provides a review opportunity. What's your read on the orchestrator's workload trade-off?

**S5**: **Session-close audit as S84 gate or v3 meta-rule** (R1 secondary catch-points). The three-invariant session-close audit (PRU-closure, SHA-uniqueness, completion-artifact) can be implemented either as an S84 pre-registered gate (`S84-V3-CLOSURE-AUDIT`) or as a permanent meta-rule in `agent-standards.md` §Post-Session Completeness Audit. If the former, it's one-time evidence for v3 effectiveness; if the latter, it's ongoing enforcement. My R2.1 edit proposes the meta-rule form. Do you agree this should be permanent rather than session-one test? Does the Kitaev-level-spacing equivalent (the 10-line cardinality tool) need a permanent hosted location, or does its existence as a sessioned artifact suffice?

**S6**: **Failure mode if v3 does not land** (contingency). If S84 session-close audit flags any of the 5 positive signatures missing, what's the escalation? A v4 iteration? Reverting to v2? Rolling back the dual-SHA format to single-SHA? My prior is that partial landing (e.g., 4 of 5 signatures present) is still a net improvement over v2; a clean "all-or-nothing" rollback criterion is too brittle for methodology migration. Your read?

---

## Round 2 — kitaev: Follow-up + Convergence

### CONVERGENCE

**C1 (K3 posture — ADVISORY wins).** Accept sagan's Re:K3 DISAGREE on BLOCKING-by-default. The substitution chain below settles it in sagan's favor.

Substitution chain (cost comparison, ADVISORY vs BLOCKING):
- Step 1 (definition). Let `B = batch size = 8`; `p = intervention rate = 0.25`; `c_stall = cost of one BLOCKING stall (orchestrator halt + 7 agents waiting)`; `c_silent = cost of one silent failure under ADVISORY (artifact never caught)`; `lambda_leak = fraction of ADVISORY warnings the orchestrator misses at wave-boundary review`.
- Step 2 (substitution). Expected wave cost under BLOCKING: `E[C_block] = p * B * (B-1) * c_stall` (each of `p*B` failing dispatches halts `B-1` peers). Expected wave cost under ADVISORY: `E[C_adv] = lambda_leak * p * B * c_silent`.
- Step 3 (simplification). Break-even: `E[C_block] = E[C_adv]` iff `(B-1) * c_stall = lambda_leak * c_silent` iff `lambda_leak = (B-1) * c_stall / c_silent = 7 * c_stall / c_silent`.
- Step 4 (direction). ADVISORY dominates BLOCKING iff `lambda_leak < 7 * c_stall / c_silent`. Since `lambda_leak <= 1` by construction, ADVISORY dominates whenever `c_silent < 7 * c_stall`. A silent missing-working-paper-section is NOT 7x costlier than a cascading 7-agent stall in the autonomous-batch culture. (Verified via Python: at B=8, break-even leak rate = 7, impossible for a probability.)
- Conclusion. ADVISORY is the right default. BLOCKING belongs only on critical-path opt-in (Re:K3 line 312). CONVERGED with sagan.

**C2 (R3 YAML template — endorse as operational form).** Accept sagan's R3 gate-block template. It operationalizes K1's cardinality check in a machine-parsable spec. Specifically:
- `thresholds.*.operator` field resolves Class 8a at plan-write time (K1's operator-kernel).
- `strict_PASS_boundary` booleans close the ambiguity at reachable rationals (K1's §W1-G4 `F_traj = 3/2` case).
- `machinery_pin_map` feeds both the D_PRU cardinality check (K1) and the `audit_sha256` closure (K2) — the K1-K2 crossover sagan flagged in Re:K2.
- 8-item checklist at R3 lines 697-704 is the executable acceptance criterion: if any item is unchecked, `D_PRU(g) > 0` and the plan is PRE-REG-INCOMPLETE.

The template is the BRIDGE between K1's cardinality metric and sagan's R1 design-time catch-point. CONVERGED.

**C3 (R2 10-edit-site diff — structurally sufficient).** I accept sagan's R2.5 summary table. The 10-edit count is an information-theoretic covering minimum (derivation in EMERGENCE below), not a convenient round number. No additional edits required from the information-scrambling audit beyond what sagan covers. Specifically:
- PRU Class 8 covered by R2.1 (design-time enforcement) + R2.1 §Post-Session Audit (post-time tripwire) = 2 sites.
- PRU Class 8a covered by R2.1 (insert after L111) + R2.4 §Enforcement append (operator-axis check in substitution chain) = 2 sites.
- SHA-collision covered by R2.2 (4 sites: format replace, semantics append, rules replace, canonical archival) + R2.3 audit_sha256 uniqueness = 5 sites.
- Completion-Verification covered by R2.3 (hook architecture + artifact manifest) = 1 site.
Total = 10. Matches R2.5.

**C4 (Re:K2 audit/content split, option (b)).** Accept sagan's Re:K2 preference for option (b) — two explicit fields `audit_sha256=<hex> content_sha256=<hex>` plus `schema_version=S84+`. My K4-3 left the choice open; sagan's substitution chain (Re:K2 Steps 1-4) shows tooling migration cost is equal either way, and (b) is semantically cleaner. CONVERGED.

---

### DISSENT

**D1 (intervention-threshold: the ADVISORY hook must still FAIL the session at close).** Sagan's ADVISORY posture (C1 above) is correct for per-dispatch enforcement but leaves a gap at session-close. New evidence: if the hook merely emits to `completion-queue.jsonl` and the orchestrator reviews at wave boundaries, NOTHING in the rule-set forces the session to FAIL when the queue is non-empty at session close. The S82 -> S83 pattern is exactly this: an intervention is noticed, fixed ad-hoc, and no session-close invariant records the residual rate.

Substitution chain for the session-close guard:
- Step 1 (definition). Let `Q_N = |completion-queue.jsonl entries for session N at session-close|`. Under pure ADVISORY, `Q_N` can be > 0 with no hard-fail.
- Step 2 (substitution). S83 plan-context cites ~13 interventions / ~50+ dispatches => `Q_83 >= 13` (lower bound; hook was not wired yet, but the count maps to post-hoc interventions).
- Step 3 (simplification). Without a session-close invariant `Q_N = 0 as hard requirement`, v3 admits the same failure mode v2 admitted: residual incompleteness flagged but not enforced.
- Step 4 (direction). ADVISORY per-dispatch + HARD session-close invariant = structurally closed. ADVISORY per-dispatch + ADVISORY session-close = STILL OPEN — the same v2 failure mode sagan is trying to prevent, shifted from per-dispatch to per-session.
- Conclusion. My DISSENT from sagan's Re:K3: ADVISORY is correct per-dispatch, but the session-close audit (sagan's R1 secondary catch-point and R2.1 §Post-Session Completeness Audit) MUST be HARD-FAIL, not advisory. A session that closes with `Q_N > 0` OR with any `D_PRU(g) > 0` OR with any duplicate `audit_sha256` must be flagged as V3-NON-COMPLIANT in the handoff document.

This is NOT a walk-back of C1. Per-dispatch BLOCKING is net-negative (cascading stalls); per-session BLOCKING is net-positive (one check at session close, no cascade). The two postures are structurally distinct.

**D2 (cardinality threshold where BLOCKING becomes net-positive — critical-path opt-in specification).** Sagan's Re:K3 line 310 says BLOCKING "should be triggered only when a dispatch is on the CRITICAL PATH of a downstream dispatch." I agree, but the rule as-written lacks a CARDINALITY TEST for critical-path membership.

Substitution chain for the critical-path gate:
- Step 1 (definition). A dispatch `d` is CRITICAL-PATH iff there exists a dispatch `d'` in the same wave such that `d'`'s `input_files` includes an artifact `d` is promised to produce.
- Step 2 (substitution). For each wave W with dispatches `{d_1, ..., d_k}`, compute the dependency graph `G_W` where `d_i -> d_j` iff `output(d_i)` appears in `input_files(d_j)`.
- Step 3 (simplification). `CRITICAL_PATH(d) := exists outgoing edge from d in G_W`. This is a STATIC PROPERTY of the plan, computable at plan-write time from the pre-registered input_files manifests.
- Step 4 (direction). The hook's BLOCKING opt-in is triggered iff `CRITICAL_PATH(d) = True`. For all non-critical-path dispatches, ADVISORY. This is decidable by the PRDR tool at plan-write time, not at run-time.
- Conclusion. Sagan's R2.3 edit should specify `BLOCKING triggered iff the gate block has critical_path: true`, where critical_path is auto-computed from the plan's dependency graph. My DISSENT: the current R2.3 text leaves this implicit ("opt-in for critical-path dispatches only"), and a reader may default to ADVISORY even on critical-path dispatches because the mode is not enforced. Add a one-line edit to the R2.3 spec: "CRITICAL_PATH membership is computed from the plan's dependency graph at plan-write time; the hook mode is set automatically per dispatch."

---

### EMERGENCE

**E1 (D_PRU + R3 YAML = executable plan-property, not rule-file text).** The crossover of K1's cardinality metric with sagan's R3 template generates something NEITHER proposal had in isolation: a plan-property that is machine-verifiable BEFORE dispatch. K1 alone is a metric without a spec language; R3 alone is a spec language without a metric. Together:

```
PRDR PASS iff:
  for each gate g in plan:
    F_script_static(g) = ast-enumerate(script_path(g))
    F_plan_keys(g) = keys(machinery_pin_map(g)) ∪ {threshold_operator(g)}
    D_PRU(g) = |F_script_static(g) \ F_plan_keys(g)|
    D_PRU(g) == 0 AND strict_PASS_boundary_set_per_threshold(g) AND substitution_chain_present(g)
```

This is a plan-property the `_pru_cardinality_audit.py` tool computes directly from the plan YAML + script AST, returns a boolean, and has zero human-interpretation surface. It is the Kitaev-level-spacing-equivalent: a 10-line computation that returns a number, and the number classifies the plan as PASS/FAIL. The rule text (R2.1) describes the invariant; the tool enforces it; the R3 template gives the data format. THIS is v3's teeth.

**E2 (10-edit lower bound is a covering-minimum, not arbitrary).** The 10-site count in R2.5 is structurally fixed by the debt-phase matrix, not a convenient choice.

Substitution chain for the covering bound:
- Step 1 (definition). The rule-file edits must cover `{PRU Class 8, PRU Class 8a, SHA-collision, Completion-Verification} x {design-time, run-time, post-time}` where each cell specifies the catch-phase for that debt. Empty cells are phases where the debt cannot be caught (see R1 table).
- Step 2 (substitution). Non-empty cells per R1 table:
  - PRU Class 8: design-time (primary) + post-time (tripwire) = 2
  - PRU Class 8a: design-time (template) + post-time (tripwire, folded into PRU 8 audit) + design-time operator axis in math-scripts = 2 (the post-time cell is shared with PRU 8, so 1 unique + 1 operator-axis = 2)
  - SHA-collision: run-time (4 discriminators inject) + post-time (uniqueness audit) + design-time (schema declaration in gate block) + canonical-input archival = 4-5
  - Completion-Verification: run-time (hook + manifest) = 1
- Step 3 (simplification). Minimum covering = 2 + 2 + 5 + 1 = 10. Below 10, at least one phase-debt cell is uncovered by a rule-file insertion.
- Step 4 (direction). 10 is the tight covering minimum, not a round number. If sagan's R2.5 had reported 8 or 12, we would need to audit for over/under-coverage. 10 matches the covering bound exactly.
- Conclusion. Sagan's count is informationally tight. This is a POSITIVE emergence — the rigor-audit's 10 is structurally derivable, not contingent.

**E3 (session-close audit as separate hook from per-dispatch hook — two Lyapunov scales).** Answering sagan's S5 and relates to my D1. There are TWO Lyapunov deviations, not one:
- Per-dispatch deviation: `D_COMP(d)` — scales with dispatch count within a wave. Clamped by run-time hook (ADVISORY).
- Per-session deviation: `D_SESSION(N) := Σ_{d in session N} D_COMP(d) + Σ_{g} D_PRU(g) + collisions(audit_sha256)`. Scales with session size.

These have DIFFERENT clamping architectures:
- Per-dispatch: run-time PostToolUse hook. Advisory because cost structure (cascading stalls) dominates at this scale.
- Per-session: session-close audit (a separate hook, fires at `/handoff` completion or equivalent). BLOCKING because cost structure inverts — one FAIL at session close costs one re-dispatch wave, vs. a v2 failure mode re-opening in S84.

The two hooks are structurally independent:
```
.claude/hooks/post-agent/completion-verify.sh    # per-dispatch, ADVISORY
.claude/hooks/post-session/v3-closure-audit.sh   # per-session, BLOCKING (hard-fail)
```

This is E3's new insight: v3 needs TWO hooks, at two scales. Sagan's R2.3 covers the first; the second is implicit in R2.1's §Post-Session Completeness Audit but not structurally hooked. My recommendation: add `.claude/hooks/post-session/v3-closure-audit.sh` as a session-close tripwire that exits 1 if any of the three invariants (D_PRU, audit_sha256 uniqueness, D_COMP residual) fail. This is BLOCKING at session-close, ADVISORY per-dispatch. The asymmetry is intentional.

**E4 (coupling-graph metric — raw cardinality vs rank, both needed).** Answering sagan's S1. The `_pru_cardinality_audit.py` tool should emit TWO numbers:
- `D_PRU_raw(g) = |F_script \ F_plan|` — the enforcement metric. Any non-zero value FAILS the PRDR. This is what sagan agreed is "checkable by tooling."
- `D_PRU_rank(g) = rank of the coupling graph of unpinned axes` — the SEVERITY metric. How many INDEPENDENT decisions are unpinned. For G36, raw=3 but rank=1 (all three axes resolve via one exception-handling branch).

Substitution chain for the rank measure:
- Step 1 (definition). Construct the coupling graph `C(g)` where nodes are unpinned axes and edges connect axes that share a control-flow node in the script's AST (e.g., same `try/except`, same `if` branch, same sign-guard).
- Step 2 (substitution). For G36 script: sign branch -> NaN guard -> V-rescale -> Delta-fix. All four axes are in the same execution path, connected by sequential exception handlers. `rank(C) = 1`.
- Step 3 (simplification). For G4/G11/G15: each has a single unpinned axis; the coupling graph has one node, rank = 1 trivially.
- Step 4 (direction). `D_PRU_rank <= D_PRU_raw` always. Equality when axes are independent; strict inequality when axes are coupled.
- Conclusion. Both metrics are needed: raw for the binary PASS/FAIL enforcement, rank for severity-weighted reporting. The tool output:

```
Gate g: D_PRU_raw(g) = 3, D_PRU_rank(g) = 1 (axes [sign, V-normalize, Delta-fix] couple via exception handler at line 47)
```

This is detectable by static analysis (sagan's S1 concern): walk the AST, build a CONNECTIVITY graph of which parameters are read/written under the same control-flow parent, compute rank. Not trivial (requires control-flow analysis), but tractable in ~50 lines of Python using `ast.walk` + parent-tracking. The `D_PRU_raw` tool can be 10 lines; the coupled-rank extension is 50 lines.

---

### QUESTIONS

**Answers to sagan's S1-S6**

**Answer to S1 (coupling-graph annotation)**: YES — the tool should emit `D_PRU_raw` AND `D_PRU_rank`. Derivation in E4 above. Detection method: AST walk with control-flow parent tracking — for each pair of unpinned axes `(a_i, a_j)`, they are COUPLED if they share a common ancestor node of type `try/except`, `if/elif/else`, or sequential `raise`-trigger branch. The coupling graph is the graph whose edges are these shared-parent pairs; rank = number of connected components (distinct decisions). G36's (sign, V-normalize, Delta-fix) share a `try/except NaN` parent, so they form one connected component, rank = 1.

**Answer to S2 (reachable-rationals scope)**: Start with a_2-slot Mellin ratios only, but make the tool EXTENSIBLE. The canonical weights for S84 per the knowledge-MCP: `f_2^zeta`, `f_2^SDW`, `f_2^Zubarev`, `f_2^f*`. Pairwise ratios yield {1/2, 2/3, 3/2, 9/8, 8/9, 3/4, 4/3, 27/32, 32/27} at L_max=5 — a small finite set. The PRDR tool should:
1. Hard-code the a_2-slot ratios initially (S84 scope).
2. Accept a pluggable `--slot=a_n` argument for higher-slot scans when we hit a threshold in a_4 or above.
3. Emit a WARNING (not FAIL) if a threshold matches a rational to >= 4 digits but the slot isn't covered.

This matches the Kitaev discipline: enumerate the universal case (a_2 dominates at our L_max), leave the tail as INFO not FAIL.

**Answer to S3 (hook failure mode — agent never completes)**: YES, a BELT-AND-SUSPENDERS session-close sweep is required. This is exactly my E3 (session-close as second hook). Implementation:

```
.claude/hooks/post-session/v3-closure-audit.sh
# Fires at /handoff completion
# (1) Parse plan: enumerate all pre-registered gate IDs
# (2) Parse s{N}_gate_verdicts.txt: enumerate all verdicted gate IDs
# (3) Diff: {plan_gates} \ {verdicted_gates} = MISSING gate set
# (4) For each missing gate, check completion-queue.jsonl for a hook event
# (5) Report triple: plan_registered / verdicted / queue_logged
# (6) HARD FAIL if plan_registered != verdicted (missing dispatches)
```

This duplicates the run-time hook at session scope, exactly as sagan predicted in S3 ("essentially another post-time tripwire, duplicating the run-time hook"). The duplication is INTENTIONAL — different scales, different cost structures, different posture (BLOCKING at session close).

**Answer to S4 (artifact manifest auto-generation vs manual copy)**: AUTO-GENERATE from the gate pre-registration block. Manual copy re-introduces PRU Class 8 failure mode at the prompt-writing stage (the orchestrator copies three fields but forgets the fourth). Specifically: the `rclab-review` skill should parse the plan's gate block, extract `(input_files, script_path, working_paper_section, data_file, plot_file)`, and emit the JSON manifest automatically. The orchestrator's workload trade-off: manual copy costs ~30 seconds of review per dispatch x ~50 dispatches/session = ~25 min/session; auto-generation costs ~1 day of one-time tooling. Break-even at 2 sessions. Strong auto-generate.

**Answer to S5 (session-close audit — S84 gate or permanent meta-rule)**: PERMANENT meta-rule, not one-time gate. This is E3 above. Rationale:
- An S84-only test is one-time evidence; v3 would be unprotected in S85+.
- The session-close audit is the per-session Lyapunov clamp at E3; removing it after S84 re-opens the degree of freedom.
- The K1 cardinality tool (`_pru_cardinality_audit.py`) needs a PERMANENT hosted location in `computations/` (not a sessioned artifact).

Agreed on sagan's R2.1 edit placing the audit in `epistemic-discipline.md` §Post-Session Completeness Audit as a META-RULE. Additional recommendation: the tool must be invoked automatically at `/handoff` via the post-session hook (E3), not left to orchestrator discretion.

**Answer to S6 (v3 partial-landing contingency)**: Partial landing (e.g., 4 of 5 signatures present) is net-positive over v2. Rollback is too brittle. Proposed contingency ladder:
1. If 5/5 signatures at S84 close: CLOSED — v3 permanent in S85+.
2. If 4/5 signatures: INFO — document the missed signature as a Class 8 flag in the handoff, register a remediation gate in S85 plan to land the missing signature. v3 remains adopted in partial form.
3. If 3/5 or fewer: FAIL — iteration to v4, keeping the signatures that landed, replacing the ones that failed. No rollback to v2.

The asymmetry between adoption (easy) and rollback (hard) is because v3 fixes REAL failure modes observed in S83. Rolling back re-opens those modes. Partial landing closes the ones that were fixable; iteration closes the rest.

---

**Sharper follow-ups for sagan's R2-final (Turn B)**

**Q1 (session-close hook BLOCKING spec)**: In D1 / E3, I argue the per-session hook must be BLOCKING (hard-fail) while the per-dispatch hook stays ADVISORY. This requires an explicit rule-file entry beyond R2.1's §Post-Session Completeness Audit text. My suggested edit: `epistemic-discipline.md` §Post-Session Completeness Audit gets an additional line "**Hook enforcement**: this audit runs at `/handoff` completion via `.claude/hooks/post-session/v3-closure-audit.sh`. Non-zero D_PRU, duplicate audit_sha256, or non-zero completion-queue residual HARD-FAILS the session close." Do you endorse adding this 11th edit site, pushing R2.5's count to 11? If yes, the covering-minimum argument in E2 needs adjustment (the post-session hook is structurally distinct from the session-close AUDIT TEXT — the text describes WHAT to check, the hook describes WHEN and HOW HARD to check). If no, how do we force the audit to actually run at session close without an infrastructure hook?

**Q2 (critical-path auto-detection in R3 template)**: In D2, I argue the R3 YAML template needs a `critical_path: auto` field that the PRDR tool computes from the plan's dependency graph. Sagan's R3 template (line 590-653) does not include this field. Should it be added to R3, and should the BLOCKING opt-in be triggered automatically (no manual dispatcher choice) based on this field? My prior: auto-detection is correct — the dispatcher is exactly the wrong party to decide critical-path membership (they see one dispatch at a time, not the wave's dependency graph).

**Q3 (S84 signature ordering for graceful degradation)**: In my Answer to S6, I propose a contingency ladder for partial v3 landing (5/5, 4/5, <=3/5). This presumes the 5 signatures have EQUAL weight. In truth they don't: (1) PRU-closure-audit presence is the most critical (fixes the most recurrent failure); (2) dual-SHA presence is second (information-theoretic fix); (3) hook presence is third (catches run-time gaps); (4)(5) are confirmatory. Should the contingency ladder WEIGHT the signatures by priority (e.g., "missing signature 1 = FAIL regardless of others; missing 4 or 5 = INFO")? This would make the S84 verdict less brittle and more aligned with the structural-severity of each debt. Your read on whether a weighted ladder is worth the spec complexity, or flat 5/5 is cleaner?

---

## Round 2 — sagan: Final Synthesis + v3 Diff

### CONVERGENCE

**C1 (two-hook architecture — ADVISORY per-dispatch + BLOCKING per-session).** Accept kitaev's D1 + E3. The two-hook architecture is strictly stronger than either of our R1 positions taken alone.

Substitution chain for the two-hook dominance claim:
- Step 1 (definition). Let `Mode_per_dispatch in {ADVISORY, BLOCKING}` and `Mode_session_close in {ADVISORY, BLOCKING}`. The architecture is the pair `(Mode_per_dispatch, Mode_session_close)`. Four possibilities: `(A,A)`, `(A,B)`, `(B,A)`, `(B,B)`. `(A,A)` = my Re:K3 position; `(B,B)` = kitaev's K3 opening position; `(A,B)` = kitaev's D1 synthesis; `(B,A)` = no agent proposed this.
- Step 2 (substitution). Expected session cost per kitaev C1 Step 2: `E[C_dispatch] = p*B*(B-1)*c_stall` under BLOCKING per-dispatch; `E[C_session_residual] = Q_N * c_silent * lambda_leak` under ADVISORY per-session (from my D1 + kitaev's D1 Step 1). Per kitaev E3, the two Lyapunov deviations are structurally independent (`D_COMP(d)` per dispatch vs `D_SESSION(N)` per session).
- Step 3 (simplification). Under `(A,A)`: per-dispatch cascade cost = 0, per-session residual cost = `Q_N * c_silent * lambda_leak`. Under `(A,B)`: per-dispatch cascade cost = 0, per-session residual cost = 0 (HARD-FAIL clamps `Q_N` to 0 at close). Under `(B,B)`: per-dispatch cascade cost = `p*B*(B-1)*c_stall`, per-session residual cost = 0. `E[cost(A,B)] = 0 + 0 = 0`; `E[cost(A,A)] = Q_N * c_silent * lambda_leak > 0`; `E[cost(B,B)] > 0` (cascade cost dominates per C1 Step 4 at `c_silent < 7*c_stall`).
- Step 4 (direction). `(A,B)` dominates both `(A,A)` and `(B,B)` strictly in expectation. The architecture achieves zero per-dispatch cascade AND zero session residual simultaneously, which neither pure posture can.
- Conclusion. CONVERGED with kitaev D1 + E3. The v3 architecture is `(Mode_per_dispatch = ADVISORY, Mode_session_close = BLOCKING)` with two independent hooks at two Lyapunov scales. Sagan Re:K3 was correct about per-dispatch, but missed that the same autonomous-batch argument does NOT apply at session-close boundaries (one check, no cascade).

**C2 (10-edit covering-minimum claim — accept as content-phase covering).** Accept kitaev E2 with a dimensional clarification. The covering-minimum of 10 sites holds ONLY against the (debt × content-phase) matrix; the session-close HOOK (kitaev Q1) is an enforcement-mechanism edit, structurally orthogonal to the content-phase matrix.

Substitution chain for the dimensional decomposition:
- Step 1 (definition). Let `M_content := {PRU8, PRU8a, SHA, COMP} × {design, run, post}` (4×3 = 12 cells, of which 10 are non-empty per R1 table). Let `M_enforcement := {text_rule, hook_mechanism}` (2 types). The edit space is `M_content × M_enforcement`.
- Step 2 (substitution). Kitaev E2 computes covering over `M_content` alone = 10 cells. Kitaev Q1 proposes an edit in `M_enforcement = hook_mechanism` at the session-close scale. This cell is in `{PRU8, SHA, COMP} × {post} × {hook_mechanism}` — a projection onto enforcement that the content-phase matrix does not capture.
- Step 3 (simplification). Total edits = |non-empty cells in M_content × M_enforcement_text| + |hook-mechanism cells needed|. Non-empty M_content × text = 10 (kitaev E2). Hook mechanism cells needed: 2 (per-dispatch hook for COMP at run-time, per-session hook for PRU + SHA + COMP at post-time). BUT both hooks are SPECIFIED inside existing text edits (R2.3 for per-dispatch, a new line in R2.1 §Post-Session for per-session). So the HOOK SPECIFICATION adds zero new edit sites beyond the 10; instead, one of the 10 sites (R2.1 §Post-Session) acquires an additional sub-paragraph.
- Step 4 (direction). Kitaev Q1's "11th edit site" framing is correct on a granular count (text + hook-spec as separate sub-paragraphs) but wrong on the covering-minimum argument (the hook is an expansion of an existing covering cell, not a new cell). Resolution: KEEP the count at 10 covering cells with one cell (R2.1) containing two sub-paragraphs (text-describes-check + hook-describes-enforcement). The substitution chain to kitaev E2 is preserved.
- Conclusion. CONVERGED on the covering-minimum claim. DISSENT (narrow) on the 11-count: the 11th "site" is a sub-paragraph within the existing 10th site, not a new matrix cell.

**C3 (R3 YAML template + E1 plan-property formulation — endorse both).** Accept kitaev C2 + E1. The YAML template at R3 lines 590-653, combined with the D_PRU cardinality check, IS the plan-property that `_pru_cardinality_audit.py` computes directly. R3 is the data spec; K1 is the metric; E1 fuses them into an executable verifier. The plan-property is:

```
PRDR_PASS(plan) iff for every gate g in plan:
  D_PRU_raw(g) == 0 AND
  strict_PASS_boundary_set(g) AND
  substitution_chain_present(g)
```

No daylight between kitaev and sagan on this. CONVERGED.

**C4 (E4 raw+rank two-metric tool — accept).** Accept kitaev E4 dual-metric tool. The raw cardinality `D_PRU_raw` is the enforcement gate (binary PASS/FAIL); the rank `D_PRU_rank` is the severity-weighted reporting metric. My S1 concern about G36 over-counting is resolved: the tool emits `(raw=3, rank=1, coupled via exception handler at line 47)` and the reader sees both the structural truth (one coupled decision) and the enforcement outcome (non-zero raw = FAIL). Implementation cost 10 lines for raw, 50 for rank — both within budget.

---

### DISSENT

**D1 (narrow dissent on edit-count framing — 10 or 11 or "10 with expansion").** Kitaev Q1 asks whether the session-close hook adds an 11th edit site. I have TWO observations from new evidence that complicate a clean 10-vs-11 answer:

Substitution chain for the count-contradiction:
- Step 1 (definition). Kitaev E2 claims "below 10, some (debt, phase) cell is uncovered; above 10, redundancy." This is a covering-minimum claim on the 4×3 content-phase matrix. Let `N_cells_covered = 10` be the coverage count. Let `E_session_close_hook` be the proposed 11th edit.
- Step 2 (substitution). `E_session_close_hook` is text of the form: "audit runs at /handoff via `.claude/hooks/post-session/v3-closure-audit.sh`; non-zero D_PRU, duplicate audit_sha256, or non-zero completion-queue residual HARD-FAILS session close." Where does this text live? Options: (A) appended to R2.1 §Post-Session Completeness Audit as a sub-paragraph of the SAME section — no new cell. (B) a new sub-section under §Post-Session labeled "Hook enforcement" — arguably a new cell in the `M_enforcement` dimension. (C) a new edit site in `agent-standards.md` §Completion Verification documenting the post-session hook alongside the per-dispatch hook — this IS a new location.
- Step 3 (simplification). Under option (A), count stays at 10 and E2 holds unchanged. Under option (B), count is 10 content-cells + 1 enforcement-cell = 11; E2 holds on content-axis only. Under option (C), count is 11 with two hook-edits in agent-standards.md (one for per-dispatch, one for per-session); E2 extends to 11 only by acknowledging a hook-mechanism dimension orthogonal to content-phase.
- Step 4 (direction). None of (A/B/C) invalidate the covering-minimum theorem: in every case, below-10 content coverage leaves cells uncovered. The choice between 10 and 11 is about WHETHER THE HOOK-SPEC COUNTS AS A SEPARATE EDIT. I argue it does (option C), which matches kitaev's implicit framing in Q1 ("infrastructure hook is structurally distinct from the audit text"). So DISSENT: update R2.5 summary table to 11 edit sites, not 10, with the 11th at `agent-standards.md` §Completion Verification (new bullet 5 documenting post-session hook). The covering-minimum of 10 still holds AT THE CONTENT-PHASE LEVEL.
- Conclusion. Accept the 11-count, preserve kitaev's covering-minimum theorem by restricting it to the content-phase matrix (dimension 1 of a 2-dimensional edit space). This is a refinement of kitaev E2, not a refutation.

**D2 (Q3 weighted-ladder — accept structural-severity weighting with sig_1 veto).** Kitaev Q3 asks whether the S84 contingency ladder should weight signatures by priority. My answer: YES, with a structural-severity weighting derived from each signature's coverage depth, AND a sig_1-veto rule.

Substitution chain for the weighted ladder:
- Step 1 (definition). Each signature `sig_i` has a weight `w_i` equal to its failure-mode coverage bits (log-scaled):
  - `w_1 = 4.000` (PRU-closure audit presence; covers 4 S83 flags G4/G11/G15/G36; coverage = log_2-ish breadth proxy)
  - `w_2 = 1.585` (dual-SHA presence; covers H(gate|SHA) entropy deficit of log_2(3) bits from K2 Step 3)
  - `w_3 = 3.750` (hook presence; covers ~log_2(14) ≈ 3.807 linear-to-zero scaling of interventions)
  - `w_4 = 1.000` (S84 plan v3 template; confirmatory, derivable from sig_1)
  - `w_5 = 1.000` (audit_sha256 uniqueness = 1; confirmatory, derivable from sig_2)
  - `Total = 11.335`
- Step 2 (substitution, verified via Python). `thresh_CLOSED = 0.9 * 11.335 = 10.202`; `thresh_INFO = 0.6 * 11.335 = 6.801`.
- Step 3 (simplification, verified via Python). Test outcomes:
  - 5/5 present: cumulative = 11.335 ≥ 10.202 → CLOSED.
  - sig_1 missing, others present: cumulative = 7.335 — BUT sig_1 veto applies → FAIL regardless of cumulative.
  - sig_4 missing, others present: cumulative = 10.335 ≥ 10.202 → CLOSED (confirmatory loss does not demote).
  - Only sig_1 + sig_3 present: cumulative = 7.750, above thresh_INFO (6.801) → INFO.
- Step 4 (direction). The sig_1 veto is structurally required because sig_1 (PRU-closure audit presence) is the PRIMARY fix for the 4-flag recurrence — without it, the other four are confirmatory decoration on an unfixed primary failure. The cumulative-weight threshold handles the non-veto signatures cleanly without a brittle 5/5 all-or-nothing rule.
- Conclusion. The weighted ladder is:
  - CLOSED iff sig_1 present AND cumulative ≥ 10.202 (90% of total weight).
  - INFO iff sig_1 present AND cumulative ≥ 6.801 (60% of total weight) AND cumulative < 10.202.
  - FAIL iff sig_1 MISSING OR cumulative < 6.801.
- This REFINES kitaev Q3's flat 5/5 ladder into a severity-weighted ladder with explicit structural priority. DISSENT from kitaev's Answer-to-S6 flat ladder; accept his concern in Q3 that weighting is worth the spec complexity.

**D3 (narrow dissent on kitaev E4 `D_PRU_rank` as standalone — must NOT feed the PRDR PASS/FAIL).** Kitaev E4 proposes two numbers: raw and rank. I accept both are emitted. I DISSENT against any rule-text that would use `D_PRU_rank` as the PASS/FAIL discriminator. Reason: if a plan-author sees `D_PRU_raw = 3, D_PRU_rank = 1` and the tool reports the coupled group as "one decision," a naive reader could interpret this as "OK then we only need to pin ONE thing" — when in fact all three axes must be pinned independently, because the rank-1 coupling is a SYMPTOM of the NaN exception handler, not a feature of the pinning requirement. The enforcement metric must remain `D_PRU_raw = 0`. The rank is reporting-only. Add to R2.1 edit: "the PRDR acceptance criterion is `D_PRU_raw(g) = 0`; `D_PRU_rank(g)` is emitted for severity reporting and does NOT substitute for the raw-cardinality pass." This is a NARROW dissent — accept E4's emission of both, reject any rule that weights rank above raw for the PASS decision.

---

### EMERGENCE

**E1-sagan (two-hook v3 as Lyapunov-composite closure).** The convergence on `(ADVISORY per-dispatch, BLOCKING per-session)` generates a structural claim neither of us made explicitly: v3 is a TWO-SCALE Lyapunov clamp with MATCHED cost structures.

Substitution chain for the matched-cost claim:
- Step 1 (definition). Per-dispatch scale: Lyapunov growth `D_COMP(d)` per dispatch; clamp cost = 0 (silent-failure risk absorbed into queue); cascade cost if BLOCKING = `c_stall * (B-1)`. Per-session scale: Lyapunov growth `D_SESSION(N) = Σ D_COMP + Σ D_PRU + collisions`; clamp cost if BLOCKING = `c_rerun_wave` (one re-dispatch wave); cascade cost = 0 (nothing downstream of session close in the batch).
- Step 2 (substitution). Optimal posture per scale = argmin(clamp_cost + cascade_cost). Per-dispatch: ADVISORY minimizes (cascade cost dominates if BLOCKING). Per-session: BLOCKING minimizes (no cascade cost at session close; clamp cost bounded by one re-dispatch wave).
- Step 3 (simplification). The two scales have OPPOSITE optimal postures because the cost structures INVERT across the scale boundary. At dispatch scale, cascade cost dominates; at session scale, accumulated residual cost dominates.
- Step 4 (direction). The ADVISORY-to-BLOCKING transition at the session boundary is a STRUCTURAL REQUIREMENT, not a convenience. Any architecture that uses the same posture at both scales (either `(A,A)` or `(B,B)`) fails at one scale.
- Conclusion. v3's "two hooks at two scales, opposite postures" is structurally determined by the scale-dependent cost asymmetry. This is EMERGENT — neither K3 (pure BLOCKING) nor Re:K3 (pure ADVISORY) captured it; kitaev's D1/E3 and sagan's C1 converge on it independently.

**E2-sagan (the 11th edit is an enforcement-sentinel, not a content-sentinel).** Expanding D1 above into structural terms. The 10 content-phase edits describe the INVARIANTS (what must hold); the 11th edit describes the ENFORCEMENT MECHANISM (what structurally forces the check to run). These are distinct.

Substitution chain for the invariant/enforcement split:
- Step 1 (definition). Rule-text of the form "session-close MUST verify X, Y, Z" describes an INVARIANT. Rule-text of the form "the check is invoked automatically via hook H at event E" describes an ENFORCEMENT MECHANISM. An invariant without an enforcement is a wish; an enforcement without an invariant is a hook with no predicate.
- Step 2 (substitution). R2.1 §Post-Session Completeness Audit is an invariant (3 audits described). R2.3 §Completion Verification bullet 4 specifies the per-dispatch hook (enforcement). The session-close invariant at R2.1 LACKS an enforcement specification; it assumes the orchestrator will voluntarily run it. The 11th edit supplies the missing enforcement.
- Step 3 (simplification). Total v3 rule-surface = 10 content invariants + 2 enforcement mechanisms (per-dispatch hook + per-session hook). The per-session hook is a NEW edit site at `agent-standards.md` §Completion Verification, as a bullet 5 paired with bullet 4.
- Step 4 (direction). The edit count grows by 1 to 11. The covering-minimum theorem on content invariants (kitaev E2) remains valid — no content cell is uncovered and the minimum is 10. The architecture-minimum includes enforcement mechanisms and sums to 11.
- Conclusion. v3's final diff target count is 11, decomposed as (10 content-invariant edits) + (1 enforcement-mechanism edit for the session-close hook). Kitaev Q1's count of 11 is accepted; kitaev E2's covering theorem is preserved at the content level.

**E3-sagan (the convergence is structurally complete — no v4 iteration needed for these debts).** The four debts in scope — PRU Class 8, PRU Class 8a, SHA-collision, Completion-Verification — are each covered at the earliest appropriate catch-phase with a structurally enforced invariant:

| Debt | Catch-phase | Invariant | Enforcement |
|:-----|:-----------|:----------|:------------|
| PRU Class 8 | Design | D_PRU_raw(g) = 0 | `_pru_cardinality_audit.py` at plan-freeze; post-session hook |
| PRU Class 8a | Design | strict_PASS_boundary pinned | PRDR template field; same tool |
| SHA-collision | Run (schema) + Post (uniqueness) | audit_sha256 unique | dual-SHA emission + post-session hook |
| Completion-Verification | Run (per-dispatch) + Post (residual) | D_COMP(d) = 0 | per-dispatch ADVISORY hook + per-session BLOCKING hook |

No debt lacks a catch-phase. No invariant lacks an enforcement. This is the E3 closure: the architecture is not just adequate but STRUCTURALLY COMPLETE for the S83-observed failure modes. A v4 iteration would be needed only for NEW failure modes that emerge post-S84 — v3 is complete for the known set.

**E4-sagan (the Venus standard is met — v3 IS falsifiable).** The gate S84-METHODOLOGY-DEBTS-V3-CLOSURE has 5 measurable signatures, each a positive observable. A session that close with any of: (a) D_PRU_raw > 0 on any gate, (b) duplicate audit_sha256, (c) non-zero completion-queue at close, (d) missing working-paper sections below 15-line threshold, (e) un-archived canonical inputs — FALSIFIES v3. This is the Sagan-Venus standard: the rule-set makes specific, quantitative, disconfirmable predictions about S84 artifacts. Either the predictions hold, in which case v3 is validated; or they fail, in which case v4 is required. There is no narrative escape.

---

### Unified v3 Diff Against All 4 Rule Files

**Count**: 11 insert/replace sites across 4 files. 10 content-invariant edits (kitaev E2 covering-minimum) + 1 enforcement-mechanism edit (session-close hook).

#### File 1: `.claude/rules/epistemic-discipline.md` (current length 110 lines)

**Edit E-1 (INSERT after line 101)** — PRU cardinality enforcement:

```
- **PRU enforcement (v3, S84+)**: PRDR §0.10(d) PASSES iff the cardinality
  check `D_PRU_raw(g) = |F_script(g) \ keys(F_plan(g))| = 0` holds for
  every gate `g` in the plan. `F_script(g)` is enumerated by static
  analysis of the producing script (Python `ast` module: argparse +
  globals-read + convention-switches). `F_plan(g)` is the set of keys in
  the plan's machinery-pin block for gate `g`. The check is automated by
  `computations/_pru_cardinality_audit.py`. A plan that emits
  `D_PRU_raw(g) > 0` for any gate is PRE-REG-INCOMPLETE and cannot proceed
  to dispatch. The tool also emits `D_PRU_rank(g)` (coupling-graph rank)
  for severity-weighted reporting; `D_PRU_rank` does NOT substitute for
  `D_PRU_raw` in the PASS decision.
```

**Edit E-2 (INSERT after Edit E-1)** — Class 8a operator-kernel subclass:

```
- **PRU Class 8a (operator-kernel subclass)**: distinct from Class 8
  value-kernel, Class 8a is the case where a relational operator (`<` vs
  `<=`, `>` vs `>=`) applied to a pre-registered threshold is unpinned.
  Detection: for each numerical threshold in the gate block, the plan
  MUST specify a boolean `strict_PASS_boundary: True|False`. The cardinality
  check includes `threshold_comparison_operator` as a free parameter when
  the computed value can land on the boundary exactly (rational thresholds
  reachable by the canonical Mellin-slot scheme). S83 §W1-G4 (F_traj = 3/2
  exact) is the canonical Class 8a failure.
```

**Edit E-3 (NEW SECTION after §Pre-Registration Completeness)** — Post-Session Completeness Audit:

```
## Post-Session Completeness Audit

Session close MUST run three audits, all pre-registered at session start
and enforced at session close via the post-session hook (see
`agent-standards.md` §Completion Verification bullet 5):

1. **PRU-closure audit**: re-run `_pru_cardinality_audit.py` over every
   gate block in `s{N}_plan`. All gates MUST have `D_PRU_raw = 0`. Any
   non-zero entry HARD-FAILS the session close.

2. **SHA-uniqueness audit**: enforce two invariants on
   `s{N}_gate_verdicts.txt`:
   - (a) `len(set(audit_sha256)) == len(verdicts)` (no audit collisions).
   - (b) every `content_sha256` recomputes against session-pinned inputs.
   Either invariant failing HARD-FAILS the session close.

3. **Completion-artifact audit**: for every verdict line, verify a
   corresponding working-paper section exists with line count between
   `### W{i}-G{j}` delimiters >= 15. Residual `completion-queue.jsonl`
   entries at session close HARD-FAIL the session.

All three are BLOCKING at session close (a failed invariant means the
session does not close cleanly). This is structurally distinct from the
ADVISORY per-dispatch hook in `agent-standards.md` §Completion
Verification bullet 4. Rationale: the per-session cost structure inverts
relative to per-dispatch (no cascade cost at session close), so BLOCKING
posture is net-positive.
```

#### File 2: `.claude/rules/gate-verdicts.md` (current length 80 lines)

**Edit G-1 (REPLACE line 58-60 S81+ canonical form)**:

OLD:
```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
```

NEW:
```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> audit_sha256=<audit_closure> content_sha256=<content_closure> schema_version=S84+
```

**Edit G-2 (APPEND below Edit G-1 replacement)** — closure semantics:

```
**S84+ closure semantics** (dual-SHA split, K2 derivation):
- `audit_sha256 = sha256(self_script_sha || session_stamp || gate_id_stamp
  || sorted(machinery_pin_map keys))` — immutable per gate event, survives
  input-file byte drift. Answers "which gate event is this verdict?"
- `content_sha256 = sha256(sorted(input_pin_map))` — the existing S81+
  closure. Changes when inputs change. Answers "did these input bytes
  produce this verdict?"

Backward compatibility: pre-S84 single-SHA verdict lines remain valid.
`_consolidate_intake.py` accepts both forms via an S{N}-detection
check. Preimage-entropy derivation: K2 Step 3 of s83-methodology-debts-v3
workshop.

**Canonical input archival**: any file referenced in `content_sha256`'s
input pin map MUST be session-frozen. Options: (a) archive as
`canonical_constants_s{N}_frozen.py` at session-close, (b) record
session-end SHA in the plan's frozen-constants block. Without archival,
`content_sha256` becomes unreproducible after input-file drift (S82->S83
canonical_constants drift, G59 FAIL).
```

**Edit G-3 (REPLACE §Rules PRU Class 8 paragraph at line 76-80)**:

OLD:
```
- A gate that cannot be evaluated because its producing machinery is unpinned
  (PRU Class 8) is NOT a FAIL — it is PRE-REG-INCOMPLETE. Pin the machinery
  via PRDR (Pre-Registration Dry-Run, `.claude/rules/epistemic-discipline.md`)
  before marking PASS/FAIL.
```

NEW:
```
- A gate that cannot be evaluated because its producing machinery is
  unpinned (PRU Class 8 value-kernel, or Class 8a operator-kernel) is NOT
  a FAIL — it is PRE-REG-INCOMPLETE. Pin the machinery via PRDR
  (Pre-Registration Dry-Run, `.claude/rules/epistemic-discipline.md`)
  before marking PASS/FAIL. The PRDR PASSES iff `D_PRU_raw(g) = 0`
  (cardinality check). `D_PRU_rank(g)` emitted for severity reporting
  but not used for the PASS decision.
- For Class 8a (operator-kernel), the machinery-pin block MUST include
  `strict_PASS_boundary: True|False` for every threshold reachable by the
  canonical scheme's rational values. S83 §W1-G4 established F_traj = 3/2
  as a reachable Mellin-ratio threshold.
- Every S84+ gate block MUST include a `machinery_pin_map` dictionary
  whose sorted keys feed the `audit_sha256` closure. Absence of the
  dictionary triggers the SHA-collision failure mode documented in S83
  §W3-G59.
```

#### File 3: `.claude/rules/agent-standards.md` (current length 38 lines)

**Edit A-1 (APPEND after current line 31 §Completion Verification mitigation-2)** — per-dispatch ADVISORY hook:

```
4. **Per-dispatch existence hook (v3, S84+, ADVISORY)**: infrastructure-
   level artifact verification. The hook
   `.claude/hooks/post-agent/completion-verify.sh` fires after every Task
   tool completion in compute mode. Inputs: `TASK_PROMISED_ARTIFACTS`
   (JSON array), `TASK_SESSION_NUMBER`, `TASK_GATE_ID`. The hook computes
   `D_COMP(d) = sum_t [1 - I(exists(t) AND content_valid(t))]`.
   
   Default posture is ADVISORY: `D_COMP > 0` emits a warning to
   `.claude/hooks/completion-queue.jsonl` and the orchestrator reviews at
   wave boundaries. The hook does not block per-dispatch progress.
   
   BLOCKING posture is opt-in for CRITICAL-PATH dispatches only. A
   dispatch `d` is critical-path iff there exists a dispatch `d'` in the
   same wave such that `d'.input_files` contains an artifact `d` is
   promised to produce. This is computed from the plan's dependency graph
   at plan-write time; the hook mode is set automatically per dispatch
   via `critical_path: auto` in the gate block (R3 YAML template).
   
   Agent dispatch prompts in compute mode MUST include a structured
   ARTIFACTS PROMISED JSON block in the prompt body (auto-generated by
   `rclab-review` from the gate pre-registration). Minimum-valid
   thresholds per artifact type: `.py` >= 50 lines; `.npz` >= 1 key;
   `.png` >= 1 byte (existence only); verdict line = 1 appended line
   matching `{GATE_ID}: (PASS|FAIL|INFO)` regex; working-paper section
   >= 15 lines between `### W{i}-G{j}` delimiters.
```

**Edit A-2 (NEW BULLET 5 after Edit A-1)** — per-session BLOCKING hook [THE 11TH EDIT — ENFORCEMENT MECHANISM]:

```
5. **Per-session closure hook (v3, S84+, BLOCKING)**: infrastructure-
   level session-close invariant enforcement. The hook
   `.claude/hooks/post-session/v3-closure-audit.sh` fires at `/handoff`
   completion (or equivalent session-close trigger). It enforces the
   three audits specified in `epistemic-discipline.md` §Post-Session
   Completeness Audit:
   
   (a) `_pru_cardinality_audit.py` over every gate: all `D_PRU_raw = 0`.
   (b) `len(set(audit_sha256)) == len(verdicts)` in `s{N}_gate_verdicts.txt`.
   (c) `completion-queue.jsonl` residual entries == 0.
   
   Any invariant failing HARD-FAILS the session close (exit 1). Rationale:
   at session-close scale, the cost structure inverts relative to
   per-dispatch — no cascade cost, bounded re-dispatch cost — so BLOCKING
   is net-positive. See s83-methodology-debts-v3 workshop E1-sagan
   derivation for the scale-dependent cost asymmetry.
   
   Belt-and-suspenders: the hook ALSO diffs `{plan_registered_gates}` vs
   `{verdicted_gates}`. Any gate in the plan without a verdict line AND
   without a queue entry HARD-FAILS (covers the "agent never completes"
   edge case where the per-dispatch hook never fires).
```

**Edit A-3 (APPEND to existing bullet 3 SHA-uniqueness check at line 33-34)**:

```
   Under v3 (S84+), the SHA-uniqueness check fires on `audit_sha256`
   (not `content_sha256`). A duplicate `audit_sha256` indicates a
   cross-gate discriminator collision (K2's information-theoretic failure
   mode, S83 §W3-G59) and must be corrected by adding the missing
   discriminator (self_script_sha, session_stamp, gate_id_stamp, or
   machinery_pin_map entry).
```

#### File 4: `.claude/rules/math-scripts.md` (current length 100 lines)

**Edit M-1 (APPEND after current line 100 §Enforcement subsection)** — PRDR substitution-chain requirement:

```
- **PRDR substitution-chain requirement (v3, S84+)**: the PRDR dry-run
  output (§0.10(d) in session plans) MUST include, for every gate with a
  sign/direction/threshold claim, the explicit 4-step substitution chain
  at plan-write time — not deferred to execution. The PRDR PASSES iff
  the substitution chain is present AND the cardinality check
  `D_PRU_raw(g) = 0` holds. Absence of the chain on a sign/direction
  claim is treated as a Class 8a PRU failure (unpinned direction axis).
- **Class 8a operator-kernel recognition**: when a PRDR enumeration
  encounters a numerical threshold reachable by an analytic rational
  (1/2, 2/3, 3/2, 9/8, 8/9 from a_2-slot Mellin-ratios at L_max=5; scope
  extensible to higher Seeley-DeWitt slots via `--slot=a_n` argument),
  the machinery-pin block MUST specify `strict_PASS_boundary` as a
  boolean. The substitution chain's Step 4 (direction read-off) cannot
  be well-defined when the computed value lands on the threshold and the
  operator is unpinned.
```

**Edit M-2 (APPEND new bullet to §Canonical Constants at end of section)**:

```
4. **Canonical input archival (v3, S84+)**: when a canonical-constants
   file is referenced as an `INPUT_FILES` entry for a gate's closure SHA,
   its session-end SHA MUST be archived (either as a frozen-copy file or
   as a plan-level pin). See `gate-verdicts.md` §Canonical input
   archival. Without archival, `content_sha256` recomputation breaks
   after any byte drift in the file. S82->S83 drift in
   canonical_constants.py is the empirical trigger.
```

#### Summary table of v3 edits (11 sites, 4 files)

| # | File | Section | Type | Target | Purpose | Dimension |
|:--|:-----|:--------|:-----|:-------|:--------|:----------|
| E-1 | epistemic-discipline.md | §Pre-Registration Completeness | INSERT | after L101 | PRU cardinality enforcement | Content (design) |
| E-2 | epistemic-discipline.md | §Pre-Registration Completeness | INSERT | after Edit E-1 | Class 8a operator-kernel subclass | Content (design) |
| E-3 | epistemic-discipline.md | new §Post-Session Completeness Audit | NEW | after §PRC | Session-close invariants | Content (post) |
| G-1 | gate-verdicts.md | §Verdict Format canonical form | REPLACE | L58-60 | dual-SHA S84+ format | Content (run) |
| G-2 | gate-verdicts.md | §Verdict Format | APPEND | below G-1 | closure semantics + archival | Content (run) |
| G-3 | gate-verdicts.md | §Rules PRU block | REPLACE | L76-80 | Class 8 + 8a + machinery_pin_map | Content (run) |
| A-1 | agent-standards.md | §Completion Verification bullet 4 | INSERT | after L31 | Per-dispatch ADVISORY hook | Content (run) |
| A-2 | agent-standards.md | §Completion Verification bullet 5 | NEW | after A-1 | Per-session BLOCKING hook | **Enforcement** |
| A-3 | agent-standards.md | bullet 3 SHA-uniqueness | APPEND | after L33-34 | audit_sha256 uniqueness | Content (post) |
| M-1 | math-scripts.md | §Enforcement | APPEND | after L100 | PRDR substitution-chain requirement | Content (design) |
| M-2 | math-scripts.md | §Canonical Constants | APPEND | end of section | Input archival cross-link | Content (design) |

Decomposition: 10 Content edits (covering the 4×3 debt-phase matrix per kitaev E2) + 1 Enforcement edit (A-2, session-close hook mechanism). Total = 11. Kitaev E2's covering-minimum of 10 holds on the content-phase axis. The 11th edit lives on the orthogonal enforcement-mechanism axis, as derived in E2-sagan.

---

## Workshop Verdict

| # | Topic | Source Sections | Status | Key Insight |
|:--|:------|:----------------|:-------|:------------|
| 1 | PRU Class 8 + 8a subclass | K1, R1, R3, C3, E1-sagan | **Converged** | Cardinality check `D_PRU_raw(g) = 0` is the ONLY enforcement metric; Class 8a (operator-kernel) is a structurally distinct subclass requiring `strict_PASS_boundary` boolean pinning on thresholds reachable by analytic rationals (F_traj = 3/2 from a_2 Mellin-ratios). Tool emits `D_PRU_rank` for reporting only. |
| 2 | SHA-collision 3-part fix | K2, Re:K2, C4 | **Converged** | Dual-SHA split `audit_sha256` + `content_sha256` with schema_version bump to S84+. Audit SHA carries self_script_sha + session_stamp + gate_id_stamp + machinery_pin_map keys; content SHA is the existing S81+ input-pin closure. Preimage entropy H(gate\|SHA) restored from log2(3)≈1.585 bits deficit to 0. Canonical input archival required. |
| 3 | Completion-Verification v3 hook | K3, Re:K3, C1, D1-kitaev, E3-kitaev, E1-sagan | **Emerged** | Two-hook architecture at two Lyapunov scales: per-dispatch ADVISORY (hook at `post-agent/completion-verify.sh`) + per-session BLOCKING (hook at `post-session/v3-closure-audit.sh`). Neither pure-ADVISORY nor pure-BLOCKING would have sufficed — the scale-dependent cost asymmetry STRUCTURALLY REQUIRES opposite postures at the two scales. |
| 4 | Unified v3 rule-file diff | R2, C3, D1-sagan, E2-sagan | **Partial** | 11 edit sites across 4 files. 10 are content-phase edits (kitaev E2 covering-minimum preserved on the 4-debt × 3-phase matrix); the 11th is an enforcement-mechanism edit (session-close hook, Edit A-2), orthogonal to content. Dissent on whether this counts as 10 or 11 — narrow refinement, not refutation: architecture-total = 11, content-covering-minimum = 10. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **PRU reachable-rationals ledger scope for S85+**: The S84 tool hard-codes a_2-slot ratios {1/2, 2/3, 3/2, 9/8, 8/9, 3/4, 4/3, 27/32, 32/27}. If an S85 gate's threshold lands on a higher Seeley-DeWitt slot (a_4 or above) rational, the tool will WARN but not FAIL. Open: when do we promote higher-slot scan to standard? Gate trigger: S85 session producing a Class 8a boundary-reach on a threshold expressible in a_4+ Mellin weights.

2. **Coupling-graph rank detection for non-exception-handler couplings**: Kitaev E4's `D_PRU_rank` detects couplings via shared `try/except`, `if/elif/else`, or `raise`-branch parents. Open: are there couplings the AST-parent walk misses (e.g., couplings via function-return chains where axis_1 resolves the return value, axis_2 resolves the parameter, but both are in separate functions)? The rank metric may under-count these. Empirical test: run the rank tool on the S83 §W3-G36 script AST and verify it returns `rank = 1`.

3. **Backward-compat shim expiration policy for dual-SHA**: `_consolidate_intake.py` will accept both single-SHA (pre-S84) and dual-SHA (S84+) verdict lines indefinitely. Open: when do we deprecate single-SHA parsing? A 12-session rolling window (S84 + 11 = S95) seems reasonable, but no rule currently forces migration of pre-S84 verdicts to dual-SHA. Is re-computing audit_sha256 retroactively for S82-S83 verdicts feasible given canonical_constants drift?

4. **Session-close hook BLOCKING failure recovery**: If the post-session hook HARD-FAILS (exit 1), the session does not close. Open: what is the recovery procedure? Options: (a) orchestrator re-dispatches the missing artifacts, re-runs the hook, iterates until pass; (b) orchestrator flags the session as V3-NON-COMPLIANT and carries forward to S{N+1}; (c) manual intervention by user. The rule text at Edit E-3 specifies the hook behavior but not the recovery protocol.

5. **Auto-generation of ARTIFACTS PROMISED manifest — tooling location**: My R2.3 + kitaev S4 Answer converge on auto-generation from the gate pre-registration block. Open: where does the auto-generation logic live? Options: (a) inside `rclab-review` skill; (b) inside `_pru_cardinality_audit.py` (as a side-output); (c) new tool `_dispatch_manifest_emit.py`. Each has different failure-isolation properties.

6. **Signature-weighted ladder calibration**: My D2 weighted ladder uses weights w_1=4.0, w_2=1.585, w_3=3.75, w_4=w_5=1.0 derived from coverage-bits heuristics. Open: are these weights stable across sessions, or should they be re-derived per-session based on that session's failure mode coverage? If stable, they can be hard-coded in the S84 gate definition; if session-dependent, the ladder becomes a recursive meta-rule.

7. **Cross-session audit_sha256 comparison for meta-gate detection**: The audit_sha256 is unique PER gate event. Open: should `audit_sha256` ALSO be unique across sessions (i.e., `sha_S84_gate_X` != `sha_S85_gate_X` for two sessions running the same gate)? Currently the session_stamp discriminator guarantees this, but there is no explicit rule. Worth codifying if meta-gate auditing becomes routine.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **Rule-file v3 diff produced** — 11 edit sites specified across 4 rule files (`epistemic-discipline.md`, `gate-verdicts.md`, `agent-standards.md`, `math-scripts.md`) with exact line-reference targets, OLD/NEW text, and rationale. Summary table included in §Unified v3 Diff.
- **Executable PRU tool specified** — `computations/_pru_cardinality_audit.py` (10 lines for raw cardinality, 50 lines for coupling-graph rank). The tool parses the plan's gate YAML block and the producing script's AST, returns `D_PRU_raw(g)` and `D_PRU_rank(g)`, and emits PASS/FAIL on the raw metric.
- **Two-hook enforcement architecture adopted** — `.claude/hooks/post-agent/completion-verify.sh` (ADVISORY per-dispatch) + `.claude/hooks/post-session/v3-closure-audit.sh` (BLOCKING per-session). The opposite postures are structurally required by the scale-dependent cost asymmetry (E1-sagan substitution chain).
- **PRU Class 8a recognized as distinct subclass** — operator-kernel (relational `<` vs `<=` unpinned) is structurally distinct from Class 8 value-kernel (scalar unpinned). Mitigation is orthogonal: pinning a boolean `strict_PASS_boundary` per threshold, plus a `boundary_reachable_analytically` flag with a reachable-rationals provenance list.
- **Dual-SHA closure introduced** — `audit_sha256` + `content_sha256` as separate 64-char fields with `schema_version=S84+`. Four new discriminators in the audit closure: self_script_sha, session_stamp, gate_id_stamp, machinery_pin_map keys. Preimage entropy deficit H(gate|SHA) = log2(3) ≈ 1.585 bits (S82 G59 case) is closed.
- **R3 YAML gate-block template formalized** — 8-item checklist for S84+ plan-block freezing (operator, strict_PASS_boundary, boundary_reachable_analytically, reachable_rationals, machinery_pin_map, audit_discriminators, substitution_chain, input_files). A plan failing any item emits `D_PRU_raw(g) > 0` and cannot proceed.
- **Weighted S84 contingency ladder** — replaces flat 5/5 with sig_1-vetoed weighted cumulative (weights 4.0, 1.585, 3.75, 1.0, 1.0; total 11.335; CLOSED ≥ 10.202; INFO ≥ 6.801; FAIL otherwise or sig_1 missing). Verified via Python.

### What Holds

- **S82 W-4 v2 partial success holds** — The PRDR concept introduced post-S78 is not wrong; it correctly diagnoses Class 8 failures AS unpinned-machinery events. What v2 lacked was the ENFORCEMENT layer: a rule that says "run PRDR" without a cardinality pass-test is a wish, not an invariant. v3 preserves the PRDR concept and supplies the enforcement. Retrospectively, v2 was design-correct but compile-weak.
- **S81+ canonical SHA closure for inputs holds** — `content_sha256` in v3 IS the existing S81+ input-pin-map closure, unchanged. The audit/content split is additive, not replacement.
- **Venus-standard falsifiability discipline holds** — v3 specifies 5 positive measurable signatures at S84 close. A session producing any missing signature falsifies v3. This is the Sagan empirical standard, preserved from the R2 drafting discipline.
- **Existing rule-corpus density holds** — 11 edit sites across 4 files, with no file restructures. Each edit is minimal-surface, targeted at an existing section or a new sub-section paired with the natural parent. Rule discovery friction is not materially increased.
- **Pre-registration-completeness framing from `epistemic-discipline.md` holds** — v3 extends §Pre-Registration Completeness rather than creating a new rule file. Agents searching for PRU guidance find it in the same file they used pre-v3.

### What Breaks or Strains

- **S82-era SHA audits cannot be fully reproduced** — `canonical_constants.py` has drifted (S82→S83 byte changes), and the S82 content_sha256 values cannot be recomputed against current tree bytes. The audit-SHA-only backward-compat reads are preserved (the GATE IDENTITY is intact), but content-reproducibility for pre-S84 verdicts is permanently broken unless we had session-end frozen copies (which we did not). Strain: any historical re-audit of S82 gates must flag "content_sha256 unreproducible, canonical inputs drifted" rather than treat the SHA as verifiable. Mitigation: the canonical-input-archival rule (Edit G-2, Edit M-2) prevents this from recurring in S84+.
- **Dispatch-template burden increases** — Agent dispatch prompts now carry an ARTIFACTS PROMISED JSON manifest. This is ~5-10 additional lines per prompt. Auto-generation via `rclab-review` reduces the orchestrator's manual workload; the net cost is tooling effort (~1 day) offset by ~25 min/session saved.
- **The R3 YAML gate-block template is a substantive new discipline** — Plan authors must now fill 8 checklist items per gate. This is a real burden. Counter: most of the burden is structured data entry (operator, boolean, provenance) that the PRDR tool can PARTIALLY auto-fill from the script's AST. The remaining manual burden (reachable_rationals provenance, substitution_chain) is legitimate pre-registration work that was previously absent.
- **Post-session hook exit 1 creates a recovery-procedure gap** — Remaining Open Question #4. The rule specifies WHEN the hook fails but not WHAT to do next. Strain: until the recovery protocol is specified, a BLOCKING session-close can leave the session in an undefined state (neither closed nor re-openable).
- **Kitaev E2 covering-minimum claim is refined, not invalidated** — Sagan D1 notes that the 11th edit lives on a separate dimensional axis (enforcement-mechanism, not content-phase). The covering-minimum of 10 holds on the content axis; architecture-total is 11. This is a legitimate but narrow disagreement — resolved by documenting both counts with their dimensional scopes.

### Pre-Registered Gate S84-METHODOLOGY-DEBTS-V3-CLOSURE

**Gate ID**: `S84-METHODOLOGY-DEBTS-V3-CLOSURE`
**Trigger**: `[AUDIT]`
**Classification**: `NON-PHONONIC` (methodology meta-gate)
**Evaluation point**: S84 session close (post-`/handoff` via `.claude/hooks/post-session/v3-closure-audit.sh`).

**Input artifacts** (sole inputs; no reference to S83 working paper beyond the rule-file diff):
- `.claude/rules/epistemic-discipline.md` (should contain Edits E-1, E-2, E-3)
- `.claude/rules/gate-verdicts.md` (should contain Edits G-1, G-2, G-3)
- `.claude/rules/agent-standards.md` (should contain Edits A-1, A-2, A-3)
- `.claude/rules/math-scripts.md` (should contain Edits M-1, M-2)
- `computations/_pru_cardinality_audit.py` (should exist, be importable)
- `.claude/hooks/post-agent/completion-verify.sh` (should exist, be executable)
- `.claude/hooks/post-session/v3-closure-audit.sh` (should exist, be executable)
- `sessions/archive/session-84/s84_plan.md` (should contain R3 YAML template blocks for every gate)
- `computations/s84_gate_verdicts.txt` (should contain dual-SHA lines for every S84 gate)

**Five positive signatures** (each measurable from disk):
- **sig_1** (weight 4.000): PRU-closure audit presence. Signature: S84 handoff contains a "PRU-Closure Audit Report" section listing every S84 gate with `D_PRU_raw(g) = 0`.
- **sig_2** (weight 1.585): Dual-SHA presence. Signature: `grep -c 'audit_sha256=' s84_gate_verdicts.txt == N_gates_S84` AND `grep -c 'content_sha256=' s84_gate_verdicts.txt == N_gates_S84`.
- **sig_3** (weight 3.750): Hook presence and fire-log. Signature: both hook files exist (post-agent + post-session), and `.claude/hooks/completion-queue.jsonl` contains at least one entry per S84 dispatch.
- **sig_4** (weight 1.000): S84 plan obeys R3 YAML template. Signature: `grep -c 'strict_PASS_boundary:' sessions/archive/session-84/s84_plan.md >= N_gates_S84_with_numerical_threshold`.
- **sig_5** (weight 1.000): audit_sha256 uniqueness. Signature: `len(set(audit_sha256 values)) == N_gates_S84` in `s84_gate_verdicts.txt`.

**Weighted-ladder verdict rule** (substitution chain verified via Python):
- Step 1 (definition). Total weight = 4.000 + 1.585 + 3.750 + 1.000 + 1.000 = 11.335.
- Step 2 (substitution). thresh_CLOSED = 0.9 × 11.335 = 10.202; thresh_INFO = 0.6 × 11.335 = 6.801.
- Step 3 (simplification). Compute cumulative = Σ (w_i if sig_i present).
- Step 4 (direction). Verdict:
  - If sig_1 MISSING: **FAIL** regardless of cumulative (sig_1 veto; sig_1 covers the primary 4-flag recurrence).
  - Else if cumulative ≥ 10.202: **PASS** (CLOSED, v3 permanent in S85+).
  - Else if cumulative ≥ 6.801: **INFO** (partial landing; remediation gate registered in S85 plan).
  - Else: **FAIL** (iterate to v4, preserving landed signatures).
- Conclusion. The weighted ladder is falsifiable, measurable from disk, and obeys the Sagan-Venus standard.

### Carry-Forward Computations

1. **_pru_cardinality_audit.py implementation (S84-W1-CF-PRU-TOOL)**
   - **What**: Implement `computations/_pru_cardinality_audit.py` emitting `D_PRU_raw(g)` (binary PASS/FAIL) and `D_PRU_rank(g)` (coupling-graph rank for reporting).
   - **Inputs**: Plan YAML block for each S84 gate; AST-parsed producing script for each S84 gate.
   - **Gate**: Tool returns `D_PRU_raw = 0` for every S84 gate at plan-freeze time. PASS condition. Pre-registered in S84-METHODOLOGY-DEBTS-V3-CLOSURE sig_1.
   - **Effort**: ~1 day (10 lines for raw + 50 lines for rank + tests against S83 §W3-G36 as known positive case).

2. **Two-hook infrastructure (S84-W1-CF-HOOK-INFRA)**
   - **What**: Implement `.claude/hooks/post-agent/completion-verify.sh` (ADVISORY per-dispatch) and `.claude/hooks/post-session/v3-closure-audit.sh` (BLOCKING per-session). Wire `completion-queue.jsonl` emission and `/handoff` trigger.
   - **Inputs**: Hook shell specifications in Edits A-1 and A-2; dispatch-prompt ARTIFACTS PROMISED manifest format (Edit A-1).
   - **Gate**: Both hooks fire at correct events; `completion-queue.jsonl` records per-dispatch events; session-close hook exit-1s on any invariant failure. Pre-registered in sig_3.
   - **Effort**: ~2 days (shell scripting + testing against a simulated incomplete dispatch + integration with orchestrator dispatcher).

3. **Dual-SHA closure and schema_version bump (S84-W1-CF-SHA-SPLIT)**
   - **What**: Update `s{N}_w{i}_...` script template to emit dual-SHA verdict lines with `schema_version=S84+` tag. Add `_consolidate_intake.py` backward-compat shim for pre-S84 single-SHA form.
   - **Inputs**: Verdict-line format spec (Edit G-1); closure semantics spec (Edit G-2); existing `_consolidate_intake.py` parser.
   - **Gate**: Every S84 verdict line contains both `audit_sha256=<64hex>` and `content_sha256=<64hex>` AND `schema_version=S84+`. Parser accepts both forms. Pre-registered in sig_2, sig_5.
   - **Effort**: ~1 day (template edit + parser extension + regression test against one frozen pre-S84 verdict file).

4. **R3 YAML gate-block template in S84 plan (S84-W1-CF-PRDR-TEMPLATE)**
   - **What**: Author the S84 plan using the R3 YAML template for every gate. Fill 8 checklist items per gate (operator, strict_PASS_boundary, boundary_reachable_analytically, reachable_rationals, machinery_pin_map, audit_discriminators, substitution_chain, input_files).
   - **Inputs**: R3 YAML template (s83-methodology-debts-v3 workshop §R3 lines 590-653); plan-authoring skill (`rclab-plan` or equivalent).
   - **Gate**: `_pru_cardinality_audit.py` returns `D_PRU_raw = 0` for every S84 gate block at plan-freeze time. Pre-registered in sig_1, sig_4.
   - **Effort**: ~1 day per plan wave, integrated with `rclab-plan` skill updates.

5. **Canonical input archival protocol (S84-W1-CF-ARCHIVAL)**
   - **What**: At S84 session close, archive `canonical_constants.py` byte content as `canonical_constants_s84_frozen.py` in the computations directory. Record the session-end SHA in the S84 handoff's pinning block.
   - **Inputs**: Current `canonical_constants.py` at S84 close; archival location in `computations/`; handoff pinning-block format.
   - **Gate**: Frozen copy exists; handoff contains `canonical_constants_s84_sha256 = <hex>`. Enables S85+ content_sha256 reproducibility for S84 verdicts.
   - **Effort**: ~0.5 day (one-line shell command + handoff template update).

6. **Auto-generation of ARTIFACTS PROMISED manifest (S84-W1-CF-MANIFEST-AUTO)**
   - **What**: Extend `rclab-review` skill to auto-generate the ARTIFACTS PROMISED JSON block in every compute-mode dispatch prompt from the gate's pre-registration block.
   - **Inputs**: R3 YAML gate-block (contains `input_files`, `script_path`, `working_paper_section`, `data_file`, `plot_file`); `rclab-review` skill dispatcher.
   - **Gate**: Spot-audit 10% of S84 dispatch prompts to confirm ARTIFACTS PROMISED block is present and correctly populated from the gate YAML. PASS iff 100% sampled dispatches have a manifest matching the gate YAML.
   - **Effort**: ~1 day (skill extension + sampling audit).

7. **Critical-path auto-detection in plan dependency graph (S84-W1-CF-CRITPATH)**
   - **What**: Extend `_pru_cardinality_audit.py` (or a sibling tool) to compute the per-wave dependency graph from gate-block `input_files` and outputs, set `critical_path: true` automatically in each gate block that has outgoing edges.
   - **Inputs**: Full S84 plan YAML with all gate blocks; graph-building logic using `input_files` / `output_files` pairings.
   - **Gate**: For each S84 wave, `critical_path` field is populated automatically; hook posture (ADVISORY vs BLOCKING) is set correctly per gate. PASS iff manual inspection of S84 Wave-1 agrees with auto-detection.
   - **Effort**: ~1 day (graph construction + topological-check logic + wave-level testing).

8. **Post-session hook recovery protocol specification (S84-W2-CF-RECOVERY-SPEC)**
   - **What**: Write the recovery procedure for when the post-session hook HARD-FAILS. Specify: orchestrator re-dispatch attempts, max iteration count, fallback to V3-NON-COMPLIANT status, user-intervention trigger.
   - **Inputs**: Edit E-3 §Post-Session Completeness Audit; `feedback_dispatch-discipline.md` user constraint.
   - **Gate**: Recovery protocol appended to `epistemic-discipline.md` §Post-Session Completeness Audit as a new paragraph. Covers the "hook exit 1" case with a specified sequence of actions.
   - **Effort**: ~0.5 day drafting + user review.

### Closing Line

v3 is a TWO-SCALE Lyapunov clamp: 10 content-phase rule edits bound the invariants at the design/run/post scales, and 1 enforcement-mechanism edit (the session-close BLOCKING hook) structurally forces those invariants to actually run — the rule-set has teeth only because the enforcement mechanism is as structural as the invariants it enforces.
