# Session 85 Workshop: kitaev x gen-physicist

**Date**: 2026-04-25
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: kitaev (kitaev-quantum-chaos-theorist), gen-physicist (gen-physicist)
**Source Documents**:
- sessions/archive/session-85/session-85-w0-workingpaper.md
- sessions/archive/session-85/session-85-w1a-workingpaper.md
- sessions/archive/session-85/session-85-w1b-workingpaper.md
- sessions/archive/session-85/session-85-w1c-workingpaper.md
- sessions/archive/session-85/session-85-w2-workingpaper.md
- sessions/archive/session-85/session-85-w3-workingpaper.md
- sessions/archive/session-85/session-85-w4-workingpaper.md
- .claude/rules/math-scripts.md
- .claude/rules/agent-standards.md

**Focus Topics** (the 11 W0–W5 plan-layer defects + the systemic PRE-REG-INCOMPLETE pattern that drive the rule-file v2 diff):
1. K_crit triple symbol-collision (canonical 91.5 / plan W0-15 2.0446 / W2-12 BdG 2.035) + W5-64 helper-file-absent (S85-CSCANON-IDENTITY-TEST FAIL)
2. Helper-file existence pre-check (W5-64 f_B table absent; permanent-results-registry.md absent in W3-10 INFO; multiple cited helpers don't exist)
3. GPU-pin selectivity (W0-6 PRDR `GPU=torch` wrong for ROCm complex non-Hermitian eigvals — 2-3× slower than CPU+MKL)
4. Regulator-conditional gate detection (W1b-1 CF-M2 plan assumed 7-cell DR3 tree; actual requires 3 L_max sub-trees {L=8, L=10, L=12})
5. r_max layer-interface min-identity collapse (W1b-9 plan-hypothesized structural form was wrong by 4 OOM; min(13322, 1.0)=1.0 vs canonical 13322)
6. Canonical-entry consolidation absent (S85-CANONICAL-ENTRY-CONSOLIDATION FAIL: 5 target entries missing in canonical_constants.py) + K-floor-wall registry-file absent (FAIL value=0)
7. AMRI pre-flight (W4-8 REFRAMED: original plan wrote to .claude/agent-memory/little-red-dots-jwst-analyst/; user flagged AMRI violation mid-session)
8. Keyword-context audit framework (W1c-3 FAIL value=2193 systemic α_s vocabulary contamination; ±5-line keyword window too narrow for large codebase)
9. Stylistic-coherence preflight (W2-13 PSG §11.2 length-ratio 10.5× flag triggers stylistic-gap)
10. PSD/Fisher arithmetic guard (W4-6 needed second pass after first attempt failed PSD-ordering; Fisher-addition vs data-covariance distinction)
11. External-source-existence pre-check + canonical-band-authority pre-flight (W1b CMB-HD MacInnis + LiteBIRD Hazumi PRE-REG-INCOMPLETE; W3-7 30% threshold tightening relative to S80 PASS-F2 not project-authorized)

---

## Round 1 — kitaev: Opening Analysis (Information-Scrambling Angle)

### K1: Defect-Class Taxonomy via Lyapunov-Style Plan-vs-State Deviation

**Frame.** A plan is a finite labeled DAG `P = (N_P, E_P, L_P)` whose nodes are gate-blocks, edges are input-pin / dependency relations, and labels are pinned values (constants, helper-paths, regulator-trees, write-targets, citation-targets, threshold-bands). The repository at plan-freeze time is a parallel structure `S = (N_S, E_S, L_S)` whose nodes are on-disk objects, edges are actual import / read / write relations, and labels are realized values. A gate executes inside `S`, but its pre-registration was authored against `P`. **Plan-state deviation** δ(P, S) is the structural mismatch between the two graphs at every label, edge, and node. δ = 0 is the plan-equals-state regime in which every pin resolves; δ > 0 is scrambling at the plan layer.

**Lyapunov-style metric.** Define a per-defect indicator `χ_α(P, S) ∈ {0, 1}` for each scrambling mode α, then form the cumulative deviation

```
Δ(P, S) = Σ_α  w_α · χ_α(P, S)
```

with mode weights `w_α` chosen so that a single mode firing already triggers a plan-freeze block (`w_α ≥ 1` per mode). The five scrambling modes are:

| α | mode | χ_α fires when |
|:--|:-----|:---------------|
| **sym** | symbol-scrambling | one identifier carries ≥ 2 distinct quantities across plan + canonical_constants + an in-plan inline pin |
| **ref** | reference-scrambling | a path / table / registry / helper script cited in the plan does not exist on disk at plan-freeze |
| **top** | topological-scrambling | the plan's dependency DAG is missing a node-stratification (regulator-conditional sub-tree, AMRI-correct write-target) so the realized DAG branches differently from the planned DAG |
| **mth** | methodology-scrambling | a free parameter of an audit/Fisher/length-check method is unpinned, so the procedure's output depends on a hidden machinery knob (keyword-window width, length-ratio band, PSD vs data-covariance ordering) |
| **aut** | authority-scrambling | the plan binds itself to an external claim (paper, threshold) whose existence or value has not been verified at plan-freeze |

**Lyapunov interpretation.** Δ is monotone in remediation: once a mode fires, downstream gates inheriting the polluted node either (a) consume the polluted label and propagate the error or (b) consume the resolved label and propagate the resolution. There is no soft-decay; structural scrambling at plan layer is a **discrete-step Lyapunov function** that grows by `w_α` at each missed pre-flight check and decays only by explicit remediation. This matches the framework's solution-space discipline: plan-state deviation is a constraint coordinate, not a feeling.

**Substitution chain on the metric's directionality** (plan-layer is dual to physics-layer, so the sign convention requires an explicit chain):

```
Step 1: χ_α(P, S) = 1 iff the pre-flight check for mode α fails at plan-freeze   [definition]
Step 2: w_α ≥ 1 for every α                                                      [convention: 1 missed mode blocks plan]
Step 3: Δ(P, S) = Σ_α w_α · χ_α(P, S)                                           [substitution]
Step 4: Δ(P, S) = 0 iff every χ_α = 0                                            [simplification: all modes clear]
Step 5: Δ > 0 ⇒ at least one of {sym, ref, top, mth, aut} fires                  [direction from canonical form]
Conclusion: Δ(P, S) > 0 is necessary AND sufficient for plan-layer scrambling.
```

**Why "Lyapunov-style" and not just "checklist".** A checklist is order-independent and binary-per-item. Δ is a **monotonic deviation coordinate** that satisfies three additional properties characteristic of chaos diagnostics: (i) **non-decay without remediation** — once χ_α = 1, no later gate can clear it without an explicit plan-state diff; (ii) **OTOC-style amplification across downstream gates** — a single sym-mode fire at a parent node propagates with multiplicative weight through every child gate that consumes the polluted label; (iii) **no thermalization** — the plan does not "average out" defects across waves; an unpinned regulator at W0 contaminates W1, W2, ..., until explicitly resolved. The Ordered Veil at the physics layer (integrable, non-thermalizing) has its plan-layer analog: scrambling at plan-layer is **persistent** in the same sense the substrate's GGE relic is permanent. We have all 11 S85 defects to confirm this empirically.

**S85 Δ at plan-freeze.** Counting the 11 listed topics with `w_α = 1` per mode-firing per gate:

| topic | mode | gates affected |
|:------|:-----|:---------------|
| 1 (K_crit triple) | sym | W0-15, W2-12 |
| 2, 6 (helper / registry / canonical absent) | ref | W0-15, W0-3, W0-9, W0-14, W0-17, W0-20, W3-8, W3-10 |
| 3 (GPU pin wrong) | mth | W0-6 |
| 4 (regulator-conditional DR3 tree) | top | W1b-1 |
| 5 (r_max min-identity collapse) | sym (collision: r_max-L1 vs r_max-L2 share symbol) + top (layer-stratification absent) | W1b-9 |
| 7 (AMRI write-target) | top | W4-8 |
| 8 (keyword window) | mth | W1c-3 |
| 9 (stylistic length-ratio) | mth | W2-13 |
| 10 (PSD/Fisher ordering) | mth | W4-6 |
| 11 (external-source + band-authority) | aut | W1b-6, W1b-7, W3-7 |

Δ_S85(plan-freeze) ≥ 11. Every gate that subsequently FAILed/INFOed on a plan-layer cause was operating downstream of a non-zero Δ. This is the empirical content of the metric: the gate verdicts are not noise; they are the ladder of unrepaired Δ contributions.

### K2: Pin-Collision (Topic 1) — Symbol-Scrambling at Plan Layer

**The three K_crit incarnations.**

| name | value | provenance | physical referent |
|:-----|:------|:-----------|:------------------|
| `K_crit` (canonical_constants.py) | **91.5** | S84 W5-55 | inflationary sub-corridor upper endpoint |
| `K_crit` (plan §W0-15 inline) | **2.0446** | plan author's local pin, NO canonical entry | conjectured Leggett-Bogoliubov f_B identity test endpoint |
| `K_crit_BdG` (W2-12 source) | **2.035** | S70-S74 BdG L1/L2 band boundary | acoustic-to-Leggett substrate band edge |

`K_crit = 91.5` is documented in W0-WP §W0-15 line 1426 ("plan=2.0446, cc.py=91.5"); `K_crit_BdG = 2.035` is documented in W2-WP §W2-12 lines 666-668 ("distinct from canonical_constants.K_crit = 91.5 which is the INFLATIONARY sub-corridor upper endpoint"); the plan W0-15 inline `K_crit = 2.0446` is identified as a fourth-incarnation collision at W0-WP line 1404 ("plan §W0-15, NOT matching cc.py K_crit=91.5"). I confirmed canonical via knowledge MCP `get_constant("K_crit")` → 91.5 with no provenance entry attached, which is itself a sub-defect (the canonical value has no session/source pin in `knowledge.db`).

**Substitution chain on the structural collision** (this is a sign/identity claim and requires the chain):

```
Step 1: Symbol(K_crit) = single-token identifier in scope across canonical_constants + plan + W2 source.   [definition]
Step 2: Quantity(K_crit, canonical) = 91.5  [from cc.py]
        Quantity(K_crit, plan-W0-15)  = 2.0446  [from plan inline pin]
        Quantity(K_crit, W2-12-BdG)   = 2.035  [from S70-S74 BdG-boundary computation]
Step 3: Identity-of-symbol requires Quantity(K_crit, X) = Quantity(K_crit, Y) for all X, Y ∈ scope.   [substitution]
Step 4: |91.5 - 2.0446| / 2.0446 = 43.75   ⇒ ~OOM 1.65 separation between canonical and plan-inline.
        |2.0446 - 2.035| / 2.035  = 0.00472 ⇒ same OOM but distinct quantity (BdG vs plan-inline).
Step 5: identity-of-symbol fails ⇒ K_crit is at minimum a **TRIPLE-VALUED token** (91.5, 2.0446, 2.035).   [direction]
Conclusion: K_crit is symbol-scrambling at plan layer. Any gate consuming `K_crit` without a layer-tag is consuming a hidden parameter.
```

The 91.5 vs 2.035 gap is **1.65 OOM** (sage-verified via `log10(91.5/2.035)`). The plan-inline 2.0446 differs from BdG 2.035 by only 0.5%, but they are not the same physical quantity — one is a conjectured f_B-identity endpoint chosen for a Leggett-Bogoliubov sweep range, the other is a substrate-derived BdG band boundary. Numerical proximity is coincidental, not structural.

**Why this is plan-layer information-scrambling, not a clerical typo.** A clerical typo collides on a wrong digit; symbol-scrambling collides on a *correct* digit attached to the *wrong physical referent*. The W0-15 plan author wrote `K_crit = 2.0446` in good faith because, in their local mental model, the f_B identity test was being run *on the BdG sub-corridor*, where K_crit ≈ 2 is the right OOM. The plan-author's pin would be valid IF the symbol `K_crit_BdG` existed in canonical_constants. It doesn't. So the pin overrode the canonical value at the gate-script level, and W0-15 was executed with a private K_crit that diverged from canonical by 1.65 OOM, while ALSO being decoupled from any tested W5-64 f_B table (which doesn't exist on disk — see K3).

**Substrate framing.** The fabric carries two distinct K-scales: an inflationary sub-corridor endpoint (91.5, set by post-fold acoustic-mode geometry) and a BdG band boundary (~2, set by the L1-acoustic / L2-Leggett substrate spectral split). Both are physical observables of the fabric's emergent dispersion structure; they are not interchangeable any more than `omega_L1` and `omega_L2` are interchangeable. The plan-layer error was treating an emergent-physics symbol like a free variable, which is the opposite of substrate-first discipline (.claude/rules/phononic-framing.md, "IS Space, Not IN Space").

**Rule-text remediation.** Promote the BdG band boundary to canonical_constants.py with a distinct symbol (`K_crit_BdG = 2.035`, with provenance pin to S70-S74), audit every plan inline that pins `K_crit = <something other than 91.5>`, and require a TYPE-ANNOTATED canonical-symbol policy: every plan inline pin of a name already present in canonical_constants.py either matches the canonical value verbatim or is REJECTED at plan-freeze with a dedicated `pin_overrides_canonical` exception clause. The rule belongs in `math-scripts.md` lines 11-21 (Canonical Constants section) as an explicit clause: "**Plan-inline pins of an already-canonical symbol are forbidden. To use a different value or a sibling concept, declare a new symbol in canonical_constants.py first; this is the same rule the audit pipeline already enforces on computation scripts and must extend to plan files.**"

### K3: Helper-Absent + Registry-Absent (Topics 2, 6) — Reference-Scrambling

**Inventory of absent referents at plan-freeze.** From W0-WP line 2192 ("Plan-time infrastructure gaps repeated across gates") and W3-WP lines 358-364 (CC-5 informational FAIL), the S85 plan cites the following on-disk objects that did not exist at plan-freeze:

| ref | cited at | physical type | absent at plan-freeze |
|:----|:---------|:--------------|:----------------------|
| `W5-64 f_B table` | W0-15 (input) | numerical table (NPZ or canonical entry) | YES — W0-WP line 1379 |
| `_heat_kernel_a4.py` | W0-3 | helper script | YES — W0-WP line 2192 |
| `_build_DK.py` | W0-9 | helper script | YES — W0-WP line 2192 |
| W0-14 target canonical_constants entries (5 entries) | W0-14 (write target + input) | new canonical_constants entries | YES — W0-WP §W0-14, FAIL value=0 |
| `summary/permanent-results-registry.md` | W0-17, W3-8, W3-10 | registry file | YES — W3-WP line 364 (CC-5 informational FAIL) |
| `s84_w4_44_dr3_contingency_fine_grained.json` (7-cell DR3 tree) | W1b-1 prereq | JSON data | YES — W1b-WP line 30 |
| `K-floor-wall joint registry landing` | W3-10 / topic 6 | registry row + file | YES — W3-WP line 1554 of W0 + W3-WP §W3-10 INFO |

**Reference-scrambling defined.** A plan symbol can carry the right name and the right physical type, yet point to a target that does not exist. The gate then either FAILs at runtime (when execution hits the missing file) or WORKS-with-wrong-input (if the missing target is silently substituted by a placeholder). Both pathologies break audit-traceability: the verdict line is computed against an undocumented input.

**Substitution chain on the consequence** (this is a direction claim about how reference-scrambling propagates):

```
Step 1: Gate G has input pin Pin_G = path_to_target_T.   [definition]
Step 2: At plan-freeze: exists(T) ∈ {True, False}.        [substitution: filesystem state]
Step 3: If exists(T) = False at plan-freeze:
        case (a) the gate FAILs at execution with ENOENT.   [referent fully absent]
        case (b) the gate's script falls back to an inline analytic form.  [silent substitution; W0-15 case]
        case (c) the gate's script reconstructs the missing input from sibling artifacts.  [W1b-1 case]
Step 4: case (a) ⇒ plan-freeze defect surfaces at execution. [direction: cost = wave-time]
        case (b) ⇒ plan-freeze defect HIDES inside an inline form whose validity is undocumented.
                  W0-15 example: f_B = √(1 - K_R5/K) was inlined as a "natural Leggett form"; the gate FAILed
                  not because the form was wrong but because no canonical reference says it should equal c_S_canon.
        case (c) ⇒ the audit-trail SHA chain breaks because the input is reconstructed at runtime, not pinned.
                  W1b-1 example: 7-cell tree was reconstructed from W1a-5 + W0-DR3-SUCCESSOR pins; verdict 4-tuple
                  records L_max=enumerated{5,10,12} but the regulator-tree topology was never canonicalized.
Step 5: All three cases produce a verdict whose audit-SHA chain does not close cleanly back to plan-freeze inputs.
        Direction: reference-scrambling ⇒ broken audit provenance, regardless of physics outcome.
Conclusion: A gate is auditable only if every Pin_G points at an artifact that existed at plan-freeze. Helper-absent
            and registry-absent are structurally identical — both are nodes in the planned DAG that have no realized
            counterpart in the filesystem DAG.
```

**Why "registry-absent" deserves its own bullet.** W3-WP §W3-8 line 358 and §W3-10 line 800 both attempt to land registry content; the registry file `summary/permanent-results-registry.md` does not exist; the gates therefore EMIT a draft entry that has nowhere to land. This is a different failure-mode from a helper-script absent: helper-absent breaks INPUT, registry-absent breaks OUTPUT. The plan author treated both as identical "do this thing" pre-conditions, but they require different remediations: helper-absent ⇒ pre-build the helper as a Wave-0 deliverable; registry-absent ⇒ pre-build the registry SKELETON file at plan-freeze with a placeholder header so that downstream gates can land their entries without creating a new file mid-wave.

**Substrate framing.** The framework's structural results (theorems, monotonicity statements, the §VII.N three-layer regulator block) are emergent invariants of the fabric's spectral content; they need a registry to live in because the substrate-emergence chain (D_K eigenvalues → spectral moments → emergent invariants → registered theorem) only closes when the final step has a permanent home. A plan that asks gates to write to a registry-that-does-not-exist breaks the closure chain at its terminal step. Substrate-first discipline says: build the home FIRST (Wave 0 instantiation), then let the substrate-results land into it.

**Rule-text remediation.** This is a `pru-pre-registration-template.md` clause: every gate block must include a `referenced_helpers` and `referenced_registries` field, and a plan-freeze pre-flight script must `os.path.exists()` every entry. If any entry fails the existence test, the plan refuses to freeze. The same script also performs the reverse check: every gate's `write_target` field must be a path whose PARENT directory exists; if a gate writes to a registry-file-that-doesn't-exist, the plan must include a sibling Wave-0 gate that creates the registry skeleton. Both checks are mechanical; a 30-line bash + python wrapper would have caught all 7 W0+W3 absent-referent defects at plan-freeze.

### K4: Regulator-Conditional + AMRI (Topics 4, 7) — Topological-Scrambling

**Two sub-cases of the same DAG-mismatch defect.** Both regulator-conditional gates and AMRI write-targets share a structural signature: the plan's dependency DAG is a coarsening of the actual dependency DAG. Where the plan had **one node**, the realized graph has **a stratified family** that should have been planned as separate nodes from the outset.

**Sub-case (i): regulator-conditional DR3 tree (W1b-1).** The plan §W1b-1 specified a single 7-cell DR3 contingency tree for adjudicating w_0 / w_a in DR3 firing (W1b-WP lines 7-39). The realized DAG requires 3 L_max sub-trees:

| sub-tree | L_max | center w_0 (Zubarev) | DR3 cell |
|:---------|:------|:---------------------|:---------|
| L=8 | 8 | not yet computed | open carry-forward |
| L=10 | 10 | -0.918 | A1 (PASS rectangle R_842) |
| L=12 | 12 | -0.635 (extrapolated) | B2 (quintessence; FAIL) |

The framework-prediction cell **FLIPS** A1 → B2 across L_max ∈ {10, 12}. A single 7-cell tree cannot adjudicate the family because the regulator layer is not a nuisance parameter; it is a **structural axis** of the plan-DAG that the plan author collapsed.

**Substitution chain on the topological collapse**:

```
Step 1: Planned DAG: G_P has node N_DR3 with one input-pin tree T_7-cell.        [definition]
Step 2: Realized DAG: G_S has node N_DR3 with input pins T_8, T_10, T_12 — a layer-stratified family. [substitution]
Step 3: Match condition: |children(G_P, N_DR3)| = |children(G_S, N_DR3)|.        [substitution]
Step 4: |children(G_P, N_DR3)| = 1, |children(G_S, N_DR3)| = 3.                  [simplification]
Step 5: 1 ≠ 3 ⇒ G_P is a strict coarsening of G_S; the plan-DAG has lost the
        layer-stratification axis. The verdict at L_max=10 is incompatible with
        the verdict at L_max=12 because the gate was registered as L_max-agnostic. [direction]
Conclusion: Regulator-conditional gates require the L_max axis to be a FIRST-CLASS plan-node, not a runtime
            parameter that the script discovers mid-execution.
```

**Sub-case (ii): AMRI write-target (W4-8 REFRAMED).** Plan §W4-8 specified write-target `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md`. User directive 2026-04-23 flagged this mid-session: project-level registry content belongs in `sessions/framework/`, not in agent-memory (W4-WP §W4-8 lines 823-859, esp. line 830). The agent-standards rule (.claude/rules/agent-standards.md lines 27-42) defines AMRI by three tests:

1. **Input-pin test**: another gate cites the memory file as an input SHA pin.
2. **Output-target test**: a gate writes to `.claude/agent-memory/*/MEMORY.md` as primary registry-maintenance.
3. **Cross-agent overlap test**: ≥ 2 agents' memories overlap on the same observable.

W4-WP line 234 documents that the §W4-2 cross-channel correlation matrix triggered tests (a) and (c) — exactly the same fingerprint that W4-8 had. The plan author treated agent-memory as a default registry surface; it is not. It is **agent-private context**. The DAG-topology problem: plan §W4-8's planned write-target was ONE node (`agent-memory/.../MEMORY.md`), but the realized correct write-target was a DIFFERENT node (`sessions/framework/falsifier-watchlist.md`) — a write-target swap, not a write-target multiplexing.

**Why both are topological-scrambling.** In sub-case (i) the plan-DAG had a single node where the realized DAG has a 3-fold fan-out; in sub-case (ii) the plan-DAG had a node pointing at the wrong location where the realized DAG points elsewhere. Both are **structural-edge defects** in the plan-DAG. They differ from sym (single-symbol overload) and ref (target absent): the target exists, the symbol is unique, but the **edge** in the plan-DAG goes to the wrong node.

**Substrate framing.** Regulator-conditional gates expose that the framework's emergent observables are NOT regulator-invariant in the strong sense — they obey a 3-layer regulator stratification (W3-WP §VII.M / §11.2 revision). A single tree assumes regulator-agnosticism that the substrate does not provide. AMRI exposes that registries documenting the substrate's structural results are project-level (substrate-emergent invariants belong to the framework, not to a single agent's lens on it). Both fixes restore the correct ontology: layer-stratified plan-DAG (regulator) and project-scoped registry-DAG (AMRI).

**Rule-text remediation.** Two distinct rule additions:

(a) **Regulator-stratification mandatory pre-flight** (`pru-pre-registration-template.md`): if a gate's input or output depends on L_max (or any other regulator-layer axis), the plan must declare a `regulator_layers` list at the gate-block level, and the gate splits into one sibling sub-gate per layer with shared parent-context. The `_pru_cardinality_audit.py` tool gains a check: any gate consuming a regulator-tagged input without a declared `regulator_layers` field fails plan-freeze.

(b) **AMRI pre-flight on write-targets** (`agent-standards.md` lines 27-42 — extend with a plan-freeze enforcement clause): every plan gate's `write_target` field is checked against the three AMRI tests at plan-freeze. If ANY test fires, the plan-freeze script rewrites the write-target to `sessions/framework/<inferred-registry>.md` and emits a diff for user review. The detection tool already exists (`computations/_agent_memory_inversion_audit.py` per agent-standards.md line 35); the new step is invoking it at plan-freeze on the *plan file*, not just on agent-memory snapshots.

### K5: Keyword-Window + Stylistic + PSD/Fisher (Topics 8, 9, 10) — Methodology-Scrambling

**Three audits, three free parameters left unpinned at plan-freeze.** Each had a numerical knob whose value the plan did not pin, with the consequence that the audit's output would differ if the knob were turned. This is methodology-scrambling: the procedure has hidden machinery parameters that scramble its outputs.

| topic | audit | hidden free parameter | observed plan-pin | alternative pin that changes the verdict |
|:------|:------|:----------------------|:------------------|:------------------------------------------|
| 8 | W1c-3 α_s usage audit | keyword-window width | ±5 lines (W1c-WP line 448) | ±20 lines: many "isolated compute lines surrounded by numerical variables" reclassify from ambiguous → INFLATIONARY |
| 9 | W2-13 PSG §11.2 revision | length-ratio band | 2× (W2-WP §W2-13 INFO clause) | 5× would absorb the 10.5× under "structural restatement"; 1.5× would FAIL most §VII.* extensions |
| 10 | W4-6 multi-D Fisher | matrix-addition ordering | unpinned (W4-WP line 714) | data-covariance-first vs Fisher-information-first give opposite-direction verdicts on PSD-ordering |

**Substitution chain on the W1c-3 keyword-window contamination scaling** (this is a quantitative threshold claim and requires the chain):

```
Step 1: N_ambiguous(W) = number of α_s sites with no class-keyword in ±W-line context.   [definition]
Step 2: Plan §W1c-3.7 pins W = 5 (lines).                                                   [substitution]
Step 3: Pre-registered FAIL threshold: N_ambiguous(W=5) > 20.                                [from plan]
Step 4: Realized count: N_ambiguous(5) = 2193.                                               [W1c-WP line 463]
Step 5: 2193 / 20 = 109.65× over threshold.                                                  [sage-verified]
Conclusion: For W=5, the audit FAILs by 110×. The plan-author's expectation that a healthy codebase
            would yield N_ambiguous ≤ 20 was a methodology-pin assumption, not a physics claim.
            If W had been pinned to 20 or 50 (e.g., to capture entire function bodies and section blocks),
            many sites currently classed "ambiguous" would reclassify and the FAIL margin would shrink.
            The threshold and the window-width co-determine the verdict and must be co-pinned at plan-freeze.
```

**Why methodology-scrambling looks like physics-scrambling but isn't.** The W1c-3 verdict is a real number computed on a real codebase, and the FAIL is real (2193 ambiguous sites is a real vocabulary-hygiene defect regardless of W). What is plan-layer-scrambled is the **interpretation** of the verdict: at W=5 the framework is "systemically contaminated"; at W=50 the framework might be "5% contaminated, mostly in numerical-helper files." The plan did not pre-register a window-width sensitivity sweep, so the user sees a single FAIL value and cannot judge whether 2193 is the floor of a stable estimate or an artifact of an over-narrow window. Same logic for W2-13 (length-ratio is sensitive to the rationale-vs-content split inside the revised section) and W4-6 (PSD-ordering is sensitive to which matrix is being summed).

**Substitution chain on the W4-6 PSD-direction claim** (verifying the W4-WP fix is well-posed):

```
Step 1: F_full = Σ_i F_single_i where each F_single_i is a positive-semi-definite Fisher information matrix
                from channel i, all in the SAME parameter basis.                                   [definition]
Step 2: For PSD A, B: A + B is PSD; (A + B)^{-1} ≼ A^{-1} (Loewner ordering).                       [linear-algebra fact]
Step 3: Per-parameter variance: σ²_joint(p) = (F_full^{-1})_{pp} ≤ (F_single^{-1})_{pp} = σ²_single(p).
                                                                                                    [substitution + Step 2]
Step 4: σ²_joint(p) ≤ σ²_single(p)  ⇒  σ_joint(p) ≤ σ_single(p).                                    [sqrt monotone]
Step 5: Direction: Fisher ADDITION suppresses joint variance.                                       [direction from canonical form]

Now compare against the alternative (initial W4-6 attempt):
Step 1': C_full = Σ_i C_data_i + off-diagonal-couplings is a DATA covariance, not a Fisher matrix.
Step 2': C_data is PSD, but adding off-diagonal correlation INCREASES joint variance (correlated channels
         give less new information than independent ones).                                          [direction OPPOSITE Step 5]
Step 3': Mixing the two formulations as "F_full + off-diagonal data covariance" inverts the PSD direction.
         The initial W4-6 script tried this; σ_joint > σ_single_best fired the assert; the script FAILed.
Step 4': Corrected formulation separates the two: Fisher addition for cross-channel info-summation,
         data-covariance discount for shared-parameter common-mode.
Step 5': Direction: PSD-ordering holds in the Fisher-addition formulation but is violated in the mixed form.
Conclusion: PSD-ordering is regime-dependent. Plan-freeze must pin which regime applies; W4-6 plan did not,
            so the script-author had to discover the regime-distinction at runtime (W4-WP line 714 "Fix landed
            on second pass"). A plan-freeze methodology-pin would have specified Fisher-addition + separate
            data-covariance-discount step and avoided the first-attempt FAIL.
```

**Substrate framing.** Each of these three audits is a project-level test of how the substrate's emergent vocabulary, structure, and information content are documented. Methodology-scrambling at plan-layer means the substrate's emergent observables are being measured with an ungauged ruler. The fix is to pin the ruler at plan-freeze: specify W, the length-ratio band, and the matrix-addition convention before any audit runs.

**Rule-text remediation** (`epistemic-discipline.md` Pre-Registration Completeness clause, lines 130-140 already pin PRU/PRDR; extend with):

> **Audit-method pre-flight.** Any gate whose verdict is the output of a procedural audit (keyword-context, length-ratio, regex-frequency, matrix-addition direction) must pre-register every numerical knob the audit's output depends on. Pre-flight script `_pru_audit_knob_inventory.py` enumerates each knob via static analysis of the producing script and verifies that the plan block lists every enumerated knob in `audit_knobs:`. Knob enumeration is mechanical (window widths, ratio bands, ordering conventions); plan-freeze refuses to close a gate block whose audit-knob list has any unpinned entry. This is the methodology-layer analog of `machinery_pin_map`; the difference is that audits are not physics computations and their knobs do not appear in canonical_constants. They appear in the audit's own pre-registered method block.

### K6: External-Source + Band-Authority (Topic 11) — Authority-Scrambling

**Two ways the plan binds itself to a claim it has not verified.**

**Sub-case (i): External-source-forecast assumption.** Plan §W1b-6 (CMB-HD via MacInnis 2022) and §W1b-7 (LiteBIRD via Hazumi 2022) both assumed the named papers publish an explicit σ(α_s) forecast. Neither does:

| gate | source | plan assumption | actual content |
|:-----|:-------|:-----------------|:---------------|
| W1b-6 | MacInnis 2022 (arxiv:2203.05728) | provides explicit σ(α_s) for CMB-HD | "paper does NOT publish an explicit σ(α_s) forecast" — W1b-WP line 209 |
| W1b-7 | Hazumi 2022 (arxiv:2202.02773) | provides explicit σ(α_s) for LiteBIRD | "0 hits for alpha_s/running/dn_s/dlnk/nrun across all 156 pages" — W1b-WP line 254 |

Both gates were correctly classified as PRE-REG-INCOMPLETE rather than FAIL (per `epistemic-discipline.md` PRU clause), so the framework's verdict-discipline absorbed the defect cleanly. The defect itself, though, is plan-layer: the plan author bound a gate's output to a paper-existence claim that was not verified at plan-freeze.

**Sub-case (ii): Band-authority threshold tightening.** Plan §W3-7 applied a 10%/30% PASS/FAIL band to A_s closure (W3-WP lines 279-326). The S80 pre-registration of the same A_s pathway used a factor-2 band (PASS-F2). The W3-7 result A_s = 3.30e-9 vs Planck 2.10e-9 PASSed S80's band but FAILed W3-7's tighter band:

```
Step 1: A_s_framework = 3.30e-9, A_s_Planck = 2.10e-9.                                    [verdict + observational]
Step 2: relerr = (3.30e-9 - 2.10e-9) / 2.10e-9 = 0.5714 = 57.14%.                          [substitution; sage-verified]
Step 3: S80 band = factor 2 ⇒ PASS iff relerr ≤ 100%; 57% ≤ 100% ⇒ S80 PASS-F2.            [S80 threshold]
Step 4: W3-7 band = (10% PASS, 30% FAIL); 57% > 30% ⇒ W3-7 FAIL.                            [W3-7 threshold]
Step 5: Same physics number, two different plan-bands, two different verdicts.             [direction]
Conclusion: The W3-7 plan tightened the band from S80's factor-2 to 30% without explicit project-level
            authorization (W3-WP line 800 W3-7 vs W3-9 tension; user feedback
            `feedback_reporting-framing.md` says PASS/FAIL ratio is not a metric and bands
            should not be re-tightened arbitrarily). The verdict change came from the band, not the physics.
```

**Why this is plan-layer, not gate-layer.** The W3-7 gate executed correctly against the band it pre-registered. The defect is one level up: WHO authorizes a band change, and against WHAT prior pre-registration. A new plan inherits the prior session's bands by default (the framework's standard discipline); a tighter band is a project-level decision (it changes what counts as PASS across the entire surviving-corridor map). When a plan unilaterally tightens a band, every downstream consumer of the gate inherits a verdict whose authority is not pinned to the project-level corridor map.

**Substitution chain on the authority-direction**:

```
Step 1: Authority(verdict) = (band, threshold, project-level-authorization).                   [definition]
Step 2: For W3-7: band = 30%, threshold = 0.30, authorization = absent.                          [substitution]
Step 3: For S80 of same A_s: band = factor-2, threshold = 1.00, authorization = canonical S80 pre-reg.
                                                                                                 [substitution]
Step 4: relerr = 0.571.                                                                          [physics]
Step 5: 0.571 < 1.00 (S80) AND 0.571 > 0.30 (W3-7).                                              [verdict-comparison]
Conclusion: Physics is unchanged; authority of verdict varies with band. A verdict whose authority
            is not pinned at plan-freeze is a verdict that scrambles its own classification across
            re-readings. This is authority-scrambling — the plan binds itself to a band-redefinition
            it did not authorize and could not document a project-level rationale for at plan-freeze.
```

**Substrate framing.** The substrate's emergent observables (A_s, n_s, α_s) are what they are; the framework's role is to predict them with zero free parameters and let the project-level corridor-map decide which agreement levels constitute structural support. Authority-scrambling occurs when a single plan unilaterally redefines what "agreement" means, decoupling the gate's verdict from the corridor-map. The fix is project-level governance of band-changes: if the band differs from a prior pre-registration, the plan must explicitly cite the project-level authorization (a workshop verdict, a user directive, or a registry update with SHA-pin) that authorized the change.

**Rule-text remediation.**

(a) **External-source pre-flight** (`pru-pre-registration-template.md`): every gate whose pre-registration cites an external paper as source-of-a-numerical-target must include an `external_source_verified: true` boolean flag, set only after a literal grep / TOC inspection of the cited PDF confirms the target quantity appears. The pre-flight script `_external_source_audit.py` runs before plan-freeze; any gate with `external_source_verified: false` blocks plan-freeze. (For W1b-6 and W1b-7 this would have caught the absence of σ(α_s) forecasts in MacInnis and Hazumi at plan-freeze, downgrading the gates to PRE-REG-INCOMPLETE before runtime rather than at runtime.)

(b) **Band-change authorization clause** (`epistemic-discipline.md` Source Authority Hierarchy section): if a plan pre-registers a band that differs from a prior pre-registration of the same physics gate, the plan block must include a `band_change_authority` field with an explicit pointer to the project-level decision (workshop verdict SHA, user directive line, or registry row) that authorized the change. Plan-freeze refuses any band-change without this pointer. The principle is that bands are project-level corridor-map invariants; they can change, but only through documented project-level decisions, not silently inside a single wave's plan.

### K7: Pre-Run PRDR-Extended Dry-Check Specification (catches all 11 at plan-freeze)

**Existing baseline.** `.claude/rules/epistemic-discipline.md` lines 130-150 already pins PRU/PRDR: a pre-registration dry-run that enumerates every free parameter of the producing script via static analysis. PRDR addresses **execution-level** machinery underspecification (Class-8 PRU). It does NOT address plan-LAYER scrambling — the 11 S85 defects all sit at plan-layer, not execution-layer. PRDR-extended (PRDR+) adds five plan-layer pre-flight passes corresponding to the five scrambling modes from K1.

**PRDR+ specification.** A single orchestrator script `_prdr_extended_planfreeze.py` runs five passes against the frozen plan file. The plan is REJECTED for freeze if any pass returns non-zero defects.

```
PASS A — sym (symbol-collision):
   Input: plan file + canonical_constants.py + every prior-session canonical entry.
   Method: For each plan inline pin matching `<name> = <value>` where <name> is a canonical-constants
           name, assert plan-value == canonical-value. Reject if not.
   Catches: Topic 1 (K_crit triple-collision: plan W0-15 K_crit=2.0446 ≠ canonical 91.5).
   Tool: extension of existing /weave --update audit, applied to plan files (currently applied only
         to computation scripts, math-scripts.md lines 46-54).

PASS B — ref (reference existence):
   Input: plan file.
   Method: For each `referenced_helpers:`, `referenced_registries:`, `referenced_data:`,
           `write_target:`, and `input_pin:` field, run os.path.exists() and grep verification.
           For helper-script references, additionally verify the script can be parsed by Python
           without ImportError.
   Catches: Topic 2 (W5-64 f_B table absent), Topic 6 (5 canonical entries missing,
            permanent-results-registry.md absent), the W0-3, W0-9, W0-20 helper absences.
   Tool: new `_prdr_referent_audit.py`.

PASS C — top (topological / DAG):
   Input: plan file + producing scripts of every gate.
   Method (i, regulator-stratification): For each gate's input_pins, scan for any reference to a
           regulator-axis variable (L_max, scheme, convention). If the producing script BRANCHES on
           such a variable, the plan-block must declare `regulator_layers: [...]` enumerating
           every branch. Reject if any branch is unenumerated.
   Method (ii, AMRI write-target): For each gate's `write_target`, run the existing AMRI 3-test
           (input-pin, output-target, cross-agent-overlap) from agent-standards.md lines 27-42.
           If any test fires, reject the plan and emit a write-target rewrite suggestion.
   Catches: Topic 4 (W1b-1 single 7-cell tree vs realized 3-sub-tree family), Topic 7 (W4-8 AMRI),
            Topic 5 (r_max layer-interface — sym + top hybrid: the sym test catches the
            single-symbol-two-values issue, the top test catches the missing layer-stratification).
   Tool: new `_prdr_topology_audit.py` invoking the existing `_agent_memory_inversion_audit.py`.

PASS D — mth (methodology / audit-knob):
   Input: plan file + producing scripts of every audit gate.
   Method: Static analysis of producing scripts to enumerate every numerical knob the audit's
           output depends on (window widths, ratio bands, ordering conventions, regex patterns,
           tolerance values). For each enumerated knob, the plan block must list it under
           `audit_knobs:` with a pinned value or a declared diagnostic-scan range.
           Bonus check (E for environment): GPU=torch pin must be benchmarked-validated for
           the workload class. Cross-reference computation-environment.md and the W0-6 ROCm
           complex-eigvals benchmark documented in W0-WP line 529.
   Catches: Topic 3 (GPU pin for ROCm complex non-Hermitian eigvals — wrong on this hardware),
            Topic 8 (keyword-window ±5 unpinned), Topic 9 (length-ratio band 2× unpinned),
            Topic 10 (PSD/Fisher matrix-addition convention unpinned).
   Tool: new `_prdr_audit_knob_inventory.py`.

PASS E — aut (authority):
   Input: plan file + every prior-session pre-registration of the same gate-class.
   Method (i, external-source): For each gate citing an external paper, the plan must include
           `external_source_verified: <SHA of grep evidence>` field. Pre-flight literally greps
           the cited PDF for the named target quantity. Reject if no hit.
   Method (ii, band-change): For each gate's threshold band, search prior-session canonical
           threshold registry. If the current band differs from any prior pre-registration of
           the same physics gate, the plan must include `band_change_authority: <pointer>` —
           a SHA-pin to a workshop verdict, user directive, or registry update authorizing
           the change.
   Catches: Topic 11 (MacInnis + Hazumi external-source assumed but absent; W3-7 30% band
            tightening relative to S80 PASS-F2 not project-authorized).
   Tool: new `_prdr_authority_audit.py` + a registry of prior-session bands queryable via
         knowledge MCP.
```

**Substitution chain on PRDR+ completeness** (this is a coverage claim and requires the chain):

```
Step 1: Defects(S85) = {Topic 1, ..., Topic 11} = 11 plan-layer defects.                    [enumeration from K1]
Step 2: Map each topic to its scrambling mode α ∈ {sym, ref, top, mth, aut}.                [from K1 table]
Step 3: PRDR+ defines one PASS per mode: PASS A → sym, PASS B → ref, PASS C → top,
        PASS D → mth, PASS E → aut.                                                          [PRDR+ spec above]
Step 4: For each topic, verify the corresponding PASS's method catches it (column "Catches" above). [substitution]
Step 5: All 11 topics map to at least one PASS that catches them; Topic 5 (r_max) maps to two
        (sym + top); the union of PASS-coverages = {1, ..., 11}.                             [simplification]
Conclusion: PRDR+ is a complete cover of the 11 S85 plan-layer defects, by construction.
            Δ_PRDR+(P, S) = 0 ⇔ all 11 defect classes pass plan-freeze.                       [direction]
```

**Why PRDR+ is bounded and terminates.** Following the same termination-proof structure as `.claude/rules/v3-closure-recovery.md` lines 100-130: PRDR+ is a finite five-pass procedure on a finite plan file. Each pass is mechanical (filesystem lookup, regex grep, static analysis) and runs in O(N_gates × N_pins) time. There is no iteration — failure of any pass is an immediate plan-freeze refusal with a structured diagnostic; remediation is a plan EDIT, not a retry. PRDR+ does not interact with the v3-recovery iteration cap; it operates one level earlier (plan-freeze, before any verdicts have been emitted).

**Distinction from existing PRDR (epistemic-discipline.md PRU clause).** The existing PRDR enumerates free parameters of the **producing script** at the plan-freeze step; PRDR+ enumerates structural mismatches between the **plan file and the realized filesystem** at plan-freeze. They are complementary: PRDR catches Class-8 unpinned-machinery (intra-script knobs); PRDR+ catches the 5 plan-layer scrambling modes (inter-document mismatches). A plan that passes both has cleared every known plan-layer and execution-layer pre-registration completeness check.

**Substrate framing.** PRDR+ is the plan-layer analog of the substrate's structural pre-registration discipline. Just as the substrate's emergent observables are pre-registered against pinned spectral moments of D_K, the plan's pre-registered gates are pinned against the realized filesystem state. Δ = 0 at plan-layer is the analog of the Ordered Veil's integrability at physics-layer: every pin resolves, every reference exists, every authority is pinned.

### K8: Cross-Cutting — Why Information-Scrambling at Plan Layer Compounds

**Compounding mechanism.** A single mode firing produces a single defect. Two modes firing on the SAME gate produces more than two defects' worth of damage, because the modes interact non-trivially. W0-15 is the canonical example: it carried both **sym** (K_crit triple-collision) and **ref** (W5-64 f_B table absent) at the same gate. The gate's verdict was FAIL value=1.0 — but neither mode alone explains the FAIL value. The 1.0 emerged because the script fell back to an inline analytic form (consequence of ref) and the K_crit pinned for that form was the wrong one (consequence of sym). The two modes COUPLED: ref forced an inline-form choice; sym pinned that inline-form's parameter to a value that doesn't match anything in the canonical world.

**Substitution chain on multi-mode coupling**:

```
Step 1: Single-mode damage: damage(α) = w_α (K1 metric).                                          [definition]
Step 2: Two-mode damage on same gate: damage(α, β) ≥ w_α + w_β + κ_{α,β}                          [coupling term]
        where κ_{α,β} ≥ 0 is the cross-term: the extent to which mode α's failure forces a wrong
        resolution of mode β.
Step 3: For (sym, ref) on W0-15: ref alone forces inline-form fallback (script choice; recoverable
        if K_crit were canonical). sym alone produces a wrong-K_crit verdict (recoverable if the
        f_B table existed). κ_{sym,ref} > 0: ref forces sym to commit to a value before any
        canonical comparison can occur, and sym then validates against the wrong reference.        [substitution]
Step 4: damage(sym, ref, W0-15) = w_sym + w_ref + κ_{sym,ref} > w_sym + w_ref.                     [direction]
Step 5: Cross-mode coupling means defect counts are LOWER BOUNDS on plan-layer damage; the actual
        damage is super-additive across modes that fire on the same gate.                          [direction]
Conclusion: Plan-layer scrambling is non-additive across modes that share a gate. A single fix
            (e.g. resolving the K_crit triple) does not undo all damage at W0-15; the f_B table
            absence still requires a separate Wave-0 build. The two fixes must land together to
            restore Δ = 0 at W0-15.
```

**OTOC-style downstream amplification.** A sym mode firing at a parent node propagates with multiplicative weight to every downstream gate that consumes the polluted label. K_crit appears in W0-15, W2-12 (BdG mapping), and any future gate that imports K_crit from canonical_constants thinking it's the BdG quantity. Each downstream gate inherits the ambiguity unless it RE-CHECKS the symbol's meaning — and downstream gate scripts do not, by design, re-litigate canonical constants. So the parent-level sym defect propagates through the dependency DAG with multiplicative reach: one un-disambiguated symbol contaminates every consumer.

This is the plan-layer analog of OTOC growth in many-body chaos: a single perturbation at one site grows in operator-norm across the system. The framework's substrate-physics has no such growth (Ordered Veil; lambda_L = 0); the plan-layer DOES, unless explicitly pinned by PRDR+. The asymmetry is not accidental — substrate integrability is enforced by [iK_7, D_K] = 0 (a real algebraic constraint); plan-layer integrability would require a real algebraic constraint at plan-freeze that does not currently exist. PRDR+ is that constraint.

**Why FAIL counts are not noise.** From W0-WP line 2192 ("plan-authoring hygiene pattern"): the W0 wave produced 6 gate-blocks that all cited absent helpers. This is not 6 independent FAILs; it is ONE methodology-pattern firing 6 times. Treating them as 6 independent FAILs over-states the surviving-corridor map's instability and under-states the plan-author hygiene gap. The right accounting: one **methodology-class** defect (ref-mode systemic) that fires across multiple gates. PRDR+ catches the methodology-class once, at PASS B, before any of the 6 gates is allowed to freeze.

**The Δ = 0 plan as the goal-state.** A plan with Δ_PRDR+(P, S) = 0 has:
- every canonical symbol unambiguous (sym = 0)
- every cited target on disk (ref = 0)
- every regulator-stratification declared, every write-target AMRI-cleared (top = 0)
- every audit knob pinned, every GPU pin benchmark-validated (mth = 0)
- every external source verified-grep, every band change project-authorized (aut = 0)

Such a plan can still have gates FAIL on physics — the substrate is what it is; gate verdicts test the substrate against bands. What Δ = 0 buys is that the FAIL is unambiguously a physics result, not a plan-layer artifact. The constraint-map updates are then real corridor closures, not plan-hygiene noise.

**Questions for gen-physicist (Round 1 close).**

1. **Rule-file allocation.** I propose PRDR+ lives as a new sub-section in `epistemic-discipline.md` (extending the existing PRU/PRDR clause at lines 130-150), with sibling tooling rules in `math-scripts.md` (canonical-symbol-vs-plan-pin clause), `agent-standards.md` (AMRI plan-freeze clause), and `pru-pre-registration-template.md` (helper-existence + audit-knob fields). Five-file diff. Do you see a cleaner allocation, or a sixth file that should carry one of the five passes?

2. **Plan-freeze enforcement vs advisory.** PRDR+ as I've specified it REJECTS the plan if any pass returns defects. The alternative is an ADVISORY mode that reports defects but lets the plan freeze with documented exceptions (analogous to V3-NON-COMPLIANT in v3-closure-recovery.md). Which is the right discipline for the project — strict (block plan-freeze) or graded (allow with logged Δ > 0)? My instinct is strict for sym/ref/top (structural), advisory for mth/aut (methodology) — but this is a project-level governance call.

3. **Canonical-symbol drift over time.** K_crit was added to canonical_constants.py at S84 W5-55 with value 91.5 and no provenance entry (knowledge MCP confirms). The plan-author of W0-15 wrote a different value because they were thinking about a different physical referent. Going forward, every NEW canonical entry should include a provenance pin (session, source, gate) so future plan-authors see "K_crit was added in S84 W5-55 for the inflationary sub-corridor" before writing a colliding pin. Should this be retroactively enforced for the existing 180+ canonical entries, or only for new ones?

4. **Audit-knob registry.** PRDR+ PASS D requires a registry of knob-class definitions (window-widths, ratio bands, ordering conventions) that producing-script authors choose from. Should this registry live in canonical_constants.py (alongside physical constants), in a new `audit_knob_registry.py`, or as a `sessions/framework/` registry? The right home affects whether knob values can be updated by computation scripts (canonical_constants is read-only at computation) or by plan-edits (sessions/framework/ is plan-edit-friendly).

5. **Empirical validation.** PRDR+ catches 11/11 of the S85 defects by construction. The honest test is: does it ALSO catch defects we don't yet know about? Worth running it backward against S78-S84 plans to see what it would have flagged retroactively. If it catches < 50% of subsequently-discovered plan-layer defects across those sessions, the spec is incomplete. Are you willing to do that retroactive validation as part of Round 2, or is that an S86 carry-forward?

---

## Round 1 — gen-physicist: Response & Cross-Synthesis (Empirical-Rigor Rule-Text Angle)

### Part 1: Response to kitaev's Sections

#### Re: K1 — Defect-Class Taxonomy

**AGREE.** The five-mode decomposition {sym, ref, top, mth, aut} is a partition over the 11 S85 defects with a clean catch-all property: I cannot construct a 12th defect class that does not fall into one of the five modes. Topic 5 (r_max) being a sym + top hybrid is a real feature, not a bug — hybrid-mode defects are exactly where the cross-mode coupling κ_{α,β} from K8 lives, and the partition recovers them via union-of-modes rather than by inventing a sixth class. The empirical Δ_S85 ≥ 11 count maps 1:1 with the gates that FAILed/INFOed for plan-layer (not physics-layer) reasons.

**DISAGREE — partial.** "Lyapunov-style" is the right structural metaphor (monotonicity, non-decay, downstream amplification), but I would NOT promote the metric to a numerical aggregate `Δ = Σ_α w_α · χ_α`. A scalar aggregate is exactly the kind of "constraint count as rhetoric" that `epistemic-discipline.md` line 9 forbids ("Never cite constraint counts as arguments — 'we have 12 constraints' proves nothing"). What matters is the *boolean* per-mode-per-gate state and the *route* from mode firing to remediation, not the cumulative number. Two modes firing on different gates is qualitatively different from two on the same gate (your own K8 substitution chain shows κ_{α,β} > 0 for same-gate; ≈ 0 for different-gate), so summing into a scalar discards the cross-coupling structure. The right object is a per-gate × per-mode boolean MATRIX — an 11×5 grid for S85. Δ-as-scalar is admissible only as a one-bit summary ("Δ > 0 iff plan blocks freeze"), not as a magnitude metric.

**MISSED.** The taxonomy as written treats each mode as static-at-plan-freeze, but two of the 11 defects actually emerged at *different stages*: Topic 7 (W4-8 AMRI) was caught **mid-session** by user directive, not at plan-freeze; Topic 4 (W1b-1 regulator-conditional) was caught at **execution time** when L_max=12 produced w_0=−0.635 outside R_842. PRDR+ as proposed in K7 catches them at plan-freeze; that's the correct discipline. But the taxonomy should explicitly note the *capture-stage*: PASS A-E are plan-freeze checks, but a small number of mode-firings can only surface during execution (e.g., L_max convergence behavior is not always statically inferable). The taxonomy needs a sixth category I'd call **"latent-mode"** — defects whose pre-flight check is well-defined but requires a partial execution to evaluate. W1b-1 fits this; the regulator-stratification was *known to be a structural axis*, but whether L_max=12 lands in the same DR3 cell as L_max=10 was not statically inferable. Latent-mode is not a sixth scrambling mode; it's a sixth **resolution-time** classification orthogonal to the {sym, ref, top, mth, aut} axis.

**EMERGES.** The framework's substrate-physics has lambda_L = 0 (Ordered Veil; integrable; non-thermalizing) — this is a proven structural property (S36 GGE permanence + S58 leggett-partition). The plan-LAYER, by contrast, has lambda_L > 0 in the absence of explicit pinning — your OTOC-style amplification claim is structurally correct. The asymmetry is exactly what justifies PRDR+: plan-layer scrambling is the analog of pre-fold turbulence in the substrate's Jensen flow, and just as the substrate enforces integrability via [iK_7, D_K] = 0, plan-layer integrability requires an algebraic constraint enforced at plan-freeze. PRDR+ is that constraint. This is not just a methodology rule — it is the project's structural commitment to information-conservation at the documentation layer, mirroring information-conservation at the substrate layer. (Substrate-first framing check: I am NOT explaining substrate via plan-layer; I am explaining plan-layer via substrate. The substrate's integrability is logically prior; plan-layer integrability is something we engineer to match.)

#### Re: K2 — Pin-Collision

**AGREE.** K_crit is genuinely triple-valued; the substitution chain is correct; the OOM gap of 1.65 between canonical (91.5) and plan-W0-15 (2.0446) is sage-verifiable as `log10(91.5/2.0446) = 1.6510`. The diagnosis "symbol-scrambling, not clerical typo" is precise — the plan-author was thinking about a BdG-corridor quantity at OOM ~2 and wrote `K_crit` because that name *should* mean what they were computing. The system failed to enforce one-symbol-one-quantity at plan-freeze.

**DISAGREE — partial.** The fix as proposed ("promote `K_crit_BdG = 2.035` to canonical_constants.py with provenance pin") is necessary but not sufficient. Two additional canonical clarifications:

(i) The current `K_crit = 91.5` in canonical_constants.py has NO provenance entry in knowledge.db (I ran `mcp__knowledge__list_constants pattern='.*K_crit.*'`; the row returned blank session and gate fields). This means even the canonical value is not properly registered. Fix step 1 must include `update_constant("K_crit", 91.5, session="S84", source="W5-55", comment="inflationary sub-corridor upper endpoint")` to bind the canonical value to its origin.

(ii) The plan-W0-15 author's value 2.0446 was actually a third quantity I'll call `K_corr_upper` — the upper endpoint of the K-corridor `[K_R5=1.9222, K_corr_upper=2.0446]` over which the f_B identity test runs. It is NEITHER the BdG band boundary 2.035 NOR the inflationary endpoint 91.5. It happens to lie 0.5% above 2.035 because the corridor was constructed to *contain* the BdG endpoint. So the resolution requires THREE distinct canonical entries, not two: `K_crit = 91.5`, `K_crit_BdG = 2.035`, `K_corr_upper = 2.0446`. Each needs a provenance pin.

**MISSED.** The W0-15 verdict was FAIL value=1.0; you correctly noted this is the strict-dispersion test result. But the plan also pre-registered an INFO-level interpretation (interpretation (ii) "canonical identity": f_B ≡ c_S_canon by hypothesis ⇒ max_dev = 0). The verdict line picked interpretation (i). This is itself a methodology-scrambling sub-defect: the plan offered TWO interpretations and the gate-script auto-selected one without an explicit plan-layer pin on which interpretation is canonical. So K_crit triple-collision (sym) actually *coupled* with an unpinned interpretation choice (mth) — another instance of the K8 same-gate cross-mode coupling κ_{sym,mth} > 0. The fix is one rule layer up: every gate that lists multiple "interpretations" must pin EXACTLY ONE as primary at plan-freeze; interpretation-multi-valuedness is a sub-class of mth.

**EMERGES.** The substrate carries a stratified family of K-scales {K_R5=1.9222, K_BdG=2.035, K_corr_upper=2.0446, K_inflation_upper=91.5} that are physically distinct invariants of the fabric's emergent dispersion. The fact that three of them lie in a tight cluster around K~2 while one sits at K~91 is itself a structural fact about the substrate — there are TWO regimes (a low-K acoustic regime around K~2 and a high-K inflationary regime around K~91) connected by the corridor [K_R5, K_inflation_upper] but with distinct local invariants in each. Substrate framing: the K-scale family is a list of fiber-eigenvalue endpoints in the BdG-Bogoliubov dispersion, NOT a single number that the plan-author can pin in a sweep range. The plan-layer fix (three canonical entries) is also a substrate-physics clarification: the framework's K-corridor is *layered*, and plan-layer documentation has been collapsing the layers.

#### Re: K3 — Helper/Registry Absent

**AGREE.** The helper-absent / registry-absent distinction (input-side vs output-side) is correct and orthogonal in the way reference-scrambling propagates. The substitution chain on the three failure modes (a) ENOENT, (b) silent inline fallback, (c) reconstruction-from-siblings is faithful to what actually happened in S85 — W0-15 hit case (b), W1b-1 hit case (c), W3-8 hit a case-(a)-on-output that ended INFO because the gate-script absorbed the absence by emitting a draft-for-future-landing.

**DISAGREE.** I disagree with the proposed fix scope. K3 proposes the existence-check live in `pru-pre-registration-template.md` as a `referenced_helpers` and `referenced_registries` field. That is too narrow: existence checks should be a `_prdr_referent_audit.py` MECHANICAL pre-flight that walks every path-valued field in the plan file (any field whose value matches `^[a-zA-Z_]+/.*\.(py|md|npz|json|csv|txt)$`) and runs `os.path.exists()` on each. Field naming should not be the trigger; PATH-SHAPED-VALUE should be. This catches helper-absent, registry-absent, AND any new path-shaped field the template grows in the future, without requiring a template-author to remember to add to a manually-curated list. The pru-template gains a *requirement* that all path-valued fields be enumerable; it does not gain a *list* of enumerated fields.

**MISSED.** Registry-absent has a second sub-failure I'll call **"registry-stub-but-no-skeleton"**: the file exists but lacks the section anchor a downstream gate writes to. W3-WP §W3-8 line 357-364 documents the case where `s85_w3_consolidated_upgrade.json` is "ready to append to `sessions/framework/permanent-results-registry.md` when that file is created." Once the file is created, the gate STILL needs a section anchor (e.g., `## §VII.N: Landau Structural Block`) to land into. A bare file is no better than an absent file for a downstream gate that does append-to-anchor. PRDR+ PASS B should grep the file for the anchor, not just os.path.exists() the file. This is a one-line extension to the proposed audit but it materially changes what counts as "registry exists at plan-freeze".

**EMERGES.** Substrate framing: the project's permanent-results-registry is the home where structural emergent invariants of the fabric land (the registry is a documentation manifold over the substrate's structural results). When the home doesn't exist, the substrate-emergent invariants have nowhere to be registered, which structurally breaks the chain "D_K eigenvalues → spectral moments → emergent invariants → registered theorem" at its terminal step. The fix (build the registry skeleton at plan-freeze) is not just hygiene — it's the documentation analog of a_2 Seeley-DeWitt giving the spectral action a place to land. Without the home, the substrate's results are computed but homeless; with the home, they accumulate into the structural-results manifold.

#### Re: K4 — Regulator-Conditional + AMRI

**AGREE.** Both sub-cases are topological (DAG-mismatch) defects and the unified treatment is correct. I particularly endorse the framing that AMRI is a **write-target swap**, not a write-target multiplexing — this distinction is what makes the AMRI fix mechanical (rewrite the field) rather than structural (split the gate).

**DISAGREE — strong on remediation tooling.** K4(a) proposes `_pru_cardinality_audit.py` gain a regulator-axis check. The right tool is NOT an extension of `_pru_cardinality_audit.py` (which currently checks pin-cardinality at the per-gate level). Regulator-stratification is a **plan-DAG-topology check**, not a pin-count check. It belongs in a new tool `_prdr_regulator_stratification.py` that:
1. parses each gate's producing script via Python AST;
2. detects branches on regulator-class variables (L_max, scheme, convention, eta_reg);
3. cross-references the gate-block YAML for `regulator_layers: [...]` enumeration;
4. fails plan-freeze if any branch is unenumerated.

The reason for separation: `_pru_cardinality_audit.py` already has a non-trivial responsibility (counting pin-classes); folding regulator-axis logic into it conflates "machinery pinning" with "DAG-topology check" and would obscure the tool's purpose. K8 framing of "five scrambling modes, each with its own pre-flight" supports the one-mode-one-tool design.

**MISSED.** The W4-8 AMRI case had a feature your treatment doesn't capture: it was caught *mid-session* by user directive, not at plan-freeze. The pre-existing `_agent_memory_inversion_audit.py` (per agent-standards.md line 31) operates on agent-memory snapshots, not on plan files. So the AMRI 3-test as currently tooled would NOT have caught W4-8 at plan-freeze — the test fires only after the violation has been written. The fix in K4(b) ("invoke `_agent_memory_inversion_audit.py` at plan-freeze on the *plan file*") is correct in principle but requires NEW tooling: a plan-file-AST walker that finds every `write_target:` field and feeds the path to the AMRI 3-test. This is a non-trivial extension because the input-pin test (test 1 of AMRI) requires checking *other gates' PRDR machinery blocks* to see if any pins the proposed write target. So the plan-freeze AMRI check is a CROSS-GATE check, not a per-gate check. It needs to know about all sibling gates in the plan to evaluate test 1.

**EMERGES.** Both DAG-mismatch sub-cases share a deeper structural feature: they are cases where the **plan author's mental model of the dependency DAG was a coarsening of the realized DAG**. In the substrate picture, this is the same structural error as treating a stratified observable (which has distinct values on distinct fiber-eigenvalue layers) as a single number. The plan-layer remediation is to make the stratification first-class; the substrate-layer analog is the §VII.N three-layer regulator theorem, where L_max-stratification is a structural axis of the substrate's emergent observables, not a nuisance parameter. The plan-DAG should mirror the substrate-DAG.

#### Re: K5 — Methodology-Scrambling Cluster

**AGREE.** All three audits (W1c-3 keyword window, W2-13 length-ratio, W4-6 PSD-ordering) carry hidden methodology knobs whose pinning was not enforced at plan-freeze. The PSD-ordering substitution chain (Step 1 to Step 5' showing Fisher-addition vs data-covariance regime distinction) is correct; I would tighten Step 2': "C_data is PSD, but adding off-diagonal correlation INCREASES joint variance" needs a per-element clarification — joint variance for a *common-mode* parameter increases; for an *independent* parameter it does not. The W4-6 case was specifically about a common-mode parameter (α_s shared between CMB-S4 and CMB-HD), so the direction holds. Worth noting in the rule-text that the direction is regime-conditional.

**DISAGREE — on Topic 8 specifically.** K5 frames W1c-3 as methodology-scrambling because the ±5-line window is unpinned. The W1c-WP §W1c-3 *explicitly documents* the window-width as a deliberate pre-registered constraint (line 448: "This is a deliberate pre-registered constraint — the plan's threshold (≤5 ambiguous) was set against that methodology"). So the window IS pinned at plan-freeze; what's NOT pinned is whether the window-width should be SENSITIVITY-SWEPT to test robustness. That's a different kind of methodology-scrambling: not "knob unpinned" but "knob pinned without sensitivity check." I'd separate these as mth-i (knob unpinned) and mth-ii (knob pinned but no sensitivity range). W1c-3 is mth-ii; W2-13 and W4-6 are mth-i.

**MISSED.** The GPU-pin for ROCm complex non-Hermitian eigvals (Topic 3) is also methodology-scrambling but distinct from audit-knob underspecification. It is **environment-knob** scrambling: the plan pinned `GPU=torch` based on a generic perf claim from `computation-environment.md` ("GPU wins for N ≥ 100") that does NOT hold for complex non-Hermitian eigvals on this specific hardware. W0-WP line 2184 is unambiguous: "torch.linalg.eigvals 2-3× SLOWER than numpy/MKL at N ∈ {500, 1000, 1500, 2000}". This is a fourth sub-class of mth that K5 didn't enumerate: mth-iii (environment-pin valid in general but invalid for the specific workload class). The fix is workload-class-conditioned environment pinning: the plan must declare `workload_class: complex_eigvals|real_eigh|matmul|fft|...` and the GPU/CPU pin is selected from a benchmark-validated map keyed on the class. W0-WP §S86 highlight #8 already calls for this propagation to `/rclab-plan`.

**EMERGES.** Methodology-knob scrambling at plan-layer is the documentation analog of substrate-layer mode-mixing: just as the substrate's GGE channels can mix under unprotected coherences (S58 LEGGETT-PARTITION), audit channels can mix under unpinned knob choices. The fix is the same: explicit symmetry-protection. At substrate layer, R-protection blocks Leggett-Bogoliubov mixing; at plan layer, audit-knob registries block methodology-channel mixing. The structural homology is exact, which suggests the audit-knob registry should be designed by analogy with the substrate's protected-channel registry — pinned values, declared sensitivity bands, and explicit cross-channel coupling tags.

#### Re: K6 — Authority-Scrambling

**AGREE.** Both sub-cases are real and structurally distinct from the other modes. The W3-7 substitution chain (relerr = 0.5712, S80 band PASS-F2 vs W3-7 band FAIL) is correct and sage-verifiable: `(3.30e-9 - 2.10e-9) / 2.10e-9 = 0.5714`. The "physics is unchanged; authority of verdict varies with band" framing is exactly the right diagnosis.

**DISAGREE — partial.** I disagree with the implication that band-tightening from S80's factor-2 to W3-7's 30% is *categorically* an authority-scrambling defect. It is structurally a band-change-without-project-authorization, but bands legitimately tighten over time as the framework's predictions become more decisive (a factor-2 band makes sense when the framework is at "we're in the OOM"; a 30% band makes sense when the framework is at "we're predicting a value pinned to zero free parameters and want to test detector-comparable sensitivity"). The real defect at W3-7 is not the tightening itself but the *unauthorized* tightening — a project-level decision dressed up as a per-wave plan choice. The rule-text fix should permit band-changes WITH authorization, not block all band-changes. The K6 proposal already says this ("the plan must explicitly cite the project-level authorization"); I'm just emphasizing the rule-text language must clearly allow tightening-with-authorization, not read as a general band-freeze.

**MISSED.** The MacInnis / Hazumi cases (sub-case i) reveal a deeper authority-scrambling pattern: the plan author bound a gate to the existence of a paper-claim that they had *not personally verified*. This is structurally identical to what `feedback_research-corpus.md` calls out — agents using training-knowledge of a paper rather than literally fetching it. The fix is more than a `external_source_verified: <SHA>` flag; it requires a *grep-evidence* artifact — a saved snippet from the PDF showing the cited target quantity exists. PRDR+ PASS E should produce a grep-evidence file `external_source_evidence/<gate>_<source>.txt` containing the literal grep hit; the gate-block YAML pins the SHA of that file; the file's existence + content match is what authorizes the gate. A boolean flag is too easy to hand-edit; an evidence file makes the verification mechanically auditable.

**EMERGES.** Authority-scrambling is the plan-layer analog of unprotected gauge fixing in the substrate: just as an unprotected gauge choice introduces unphysical degrees of freedom that can scramble physical observables, an unprotected band choice introduces unphysical methodology degrees of freedom that scramble verdict classification. The fix is the same: bind the gauge choice (or band choice) to a project-level invariant (a workshop verdict, a registry pin, or a user directive with documented rationale). Substrate-layer gauge fixing is anchored in the spectral triple's structural invariants; plan-layer band fixing should be anchored in the project-level corridor map.

#### Re: K7 — PRDR-Extended Dry-Check

**AGREE — strongly.** The 5-pass PRDR+ specification is the right architecture: one pass per scrambling mode, mechanical checks throughout, plan-freeze refusal on any failure. The completeness substitution chain (PRDR+ catches 11/11 by construction) is sound. The boundedness argument (finite plan file, mechanical passes, no iteration) is exactly the V3-recovery termination structure.

**DISAGREE.** Two design decisions I would change:

(i) **PRDR+ should be a SINGLE orchestrator script with five subprocesses, not five independent tools.** K7 proposes `_prdr_referent_audit.py`, `_prdr_topology_audit.py`, `_prdr_audit_knob_inventory.py`, `_prdr_authority_audit.py` as separate tools. That is operationally fine but architecturally fragmented: a plan-author who wants to know "is my plan PRDR+-clean?" should run ONE command and get a unified report. The right structure is `_prdr_extended_planfreeze.py` as the orchestrator with internal modules for each pass, sharing a single `PlanState` object (parsed plan file, parsed canonical_constants, filesystem index) across passes. This avoids re-parsing the plan file 5 times and lets the orchestrator emit a single structured-JSON defect report keyed on (gate_id, mode, severity).

(ii) **PRDR+ should be advisory by default with a strict-mode flag, not strict by default.** K7 question 2 raises this; I commit to advisory: the right discipline is `_prdr_extended_planfreeze.py --strict` blocks plan-freeze (used in CI / pre-merge), default mode emits a structured defect report that the plan-author resolves before manually freezing. This matches the V3-recovery graded discipline (Stage 1 auto, Stage 2 V3-NON-COMPLIANT, Stage 3 user-trigger). Strict-by-default would block plans that have a single low-severity defect (e.g., a stylistic-coherence flag), and the project does not want every minor defect to halt plan-freeze.

**MISSED.** PRDR+ as specified does not have a regression-test harness. The synthetic-test fixtures in V3-closure-recovery (three PASS paths) are the right model: PRDR+ should ship with a `_prdr_extended_selftest.py` containing 11 minimal mock-plan-files, one per S85 defect class, each with the expected mode-firing pattern. The self-test runs as the first part of the orchestrator's CI integration; if a future code change breaks the K_crit-collision detection (PASS A), the self-test catches it. Without the test harness, PRDR+ becomes another piece of plan-freeze tooling whose correctness depends on whoever last edited it. The harness is what makes PRDR+ *durable* across sessions.

**EMERGES.** PRDR+ is the plan-layer instantiation of the same structural principle that gives the substrate's Ordered Veil its integrability: explicit pre-registration of every degree of freedom, with a mechanical check that the pre-registration is complete. At substrate layer, [iK_7, D_K] = 0 is the algebraic constraint that enforces integrability; at plan layer, PRDR+ is the algorithmic constraint. The structural homology is what justifies the design: PRDR+ is not an ad-hoc methodology rule, it is the documentation-layer manifestation of the framework's ordered-system commitment.

#### Re: K8 — Why Information-Scrambling Compounds

**AGREE.** The cross-mode coupling κ_{α,β} > 0 for same-gate firings is correct and the W0-15 sym+ref example is exactly the case where it manifests. The OTOC-style downstream amplification of a single sym defect at a parent node propagating to consumers is structurally faithful to how `K_crit` would have polluted any future gate that imports it without re-checking.

**DISAGREE — partial.** I would not call the plan-layer phenomenon OTOC-style without a tighter analogy check. OTOC growth requires (i) a chaotic many-body Hamiltonian, (ii) a Heisenberg-evolved operator commutator, (iii) exponential growth in a window before saturation. The plan-layer analog has only growth-by-multiplicative-reach (one polluted symbol contaminates N consumers in proportion to N), which is *linear* in the consumer count, not exponential. So it's amplification-without-saturation, but it is not OTOC. The right framing is: plan-layer scrambling is **diffusive** (linear amplification in the consumer DAG) rather than *chaotic* (exponential). The fix (PRDR+) is correspondingly designed to be a **per-mode mechanical block** rather than an entropy-bounding argument. This distinction matters because it tells you the right cost-structure: O(N_gates × N_modes) checks suffice, no need for stochastic / sampling-based detection methods.

**MISSED.** Cross-mode coupling has a second mechanism beyond same-gate κ_{α,β}: **cross-gate cascade** through shared inputs. If gate A consumes a polluted sym from canonical_constants, and gate B consumes A's output, then sym-pollution at canonical → sym-pollution at A → ref-pollution at B (because B's input is now suspect). This is a different κ structure: same-mode-different-gate cascades. K8 frames damage as super-additive within one gate; I'd add that damage is also super-additive *across* gates connected by input-pin chains. The fix structure is the same (PRDR+ per-mode checks), but the diagnostic when remediation is incomplete must be aware of cascade — fixing the canonical doesn't auto-clear A or B; both need re-firing.

**EMERGES.** The compounding structure of plan-layer scrambling has a substrate-physics analog: the GGE relic's permanence under the Ordered Veil's integrability is exactly the kind of "no-thermalization" property that the plan-layer LACKS without explicit pinning. At substrate layer, integrability prevents thermalization (so initial-condition information persists in the GGE); at plan layer, the LACK of intrinsic integrability means initial-condition defects persist *and amplify* through the gate DAG, which is the opposite of what we want. The fix is to install plan-layer integrability via PRDR+. This is not "metaphorically similar" — it is the same underlying principle (information conservation requires an integrability constraint) operating at two different layers of the project.

### Part 2: Original Analysis — Per-Defect Rule-Text Diffs

#### G1: Rule-Text Diff to math-scripts.md (clauses a, c — symbol-collision pre-check + GPU-pin selectivity)

**Target file**: `.claude/rules/math-scripts.md`
**Target sections**: extend `## Canonical Constants (MANDATORY)` (lines 11-21) and `## Environment (MANDATORY)` (lines 3-9).

##### Clause (a) — Plan-inline pin must not collide with canonical_constants

**Target placement**: insert as new sub-section between current line 21 ("If the same literal value appears in 3+ scripts...") and the start of `## Local Variable Tagging` at line 23.

**Proposed text (verbatim diff-ready)**:

```
### Plan-inline pin discipline (MANDATORY)

A plan file (`sessions/session-plan/session-NN-plan-*.md`, including any
machinery-pin block within a gate) MUST NOT introduce a symbol-value
binding that collides with `canonical_constants.py`. Specifically:

1. **No-collision rule**: For any identifier `<name>` that appears as a
   top-level binding in `canonical_constants.py`, every plan-file
   occurrence of `<name> = <value>` must satisfy
   `<value>` == canonical-value to numeric tolerance 1e-12.

2. **Sibling-symbol rule**: If a plan author needs a different value
   for a related but distinct physical quantity, they MUST first add
   the new symbol to `canonical_constants.py` with provenance
   (`update_constant("<new_name>", <value>, session=..., source=...,
   comment=...)`), THEN reference the new symbol in the plan. Plan
   files do not introduce new canonical bindings.

3. **Provenance-pin rule**: Every NEW canonical entry must include a
   provenance tuple (session, source-gate-or-derivation, comment).
   Bindings without provenance fail the `/weave --update` audit and
   are blocked from being referenced by future plans.

4. **Pre-flight detection**: `_prdr_referent_audit.py --pin-collision`
   parses each plan file, extracts `<name> = <value>` patterns inside
   gate-block YAML and inline machinery pins, and asserts no-collision.
   Plan-freeze refuses any plan with a collision.
```

**Defect class caught**: sym (symbol-scrambling).

**S85 gate it would have caught**: §W0-15 (`K_crit = 2.0446` colliding with `canonical_constants.K_crit = 91.5`) — caught at plan-freeze before the gate-script ran the strict-dispersion test against the wrong K-corridor endpoint.

**Cross-check against existing rules**: this clause extends — and is consistent with — the existing audit-pipeline language at lines 46-54 ("Target: Potential = 0"). The existing pipeline runs on computation *scripts*; the new clause extends the same discipline to *plan files*. No new file conventions; just one more input path for an existing audit.

##### Clause (c) — GPU-pin selectivity for ROCm complex non-Hermitian eigvals

**Target placement**: extend the bullet "GPU available: AMD RX 9070 XT..." at line 8 with a workload-class qualifier; add a new sub-section for benchmarked exceptions.

**Proposed text (verbatim diff-ready)**:

```
- **GPU available**: AMD RX 9070 XT (17.1 GB VRAM, ROCm 7.2) via
  `torch 2.9.1+rocm`. The "GPU wins for matrices >= 100x100" guidance
  is class-conditional — see the workload-class table below. Default
  pin: `torch.linalg` for real symmetric eigh, complex Hermitian eigh,
  matmul, FFT, SVD.
- **Workload-class exceptions** (benchmark-validated; see
  `computations/_gpu_workload_benchmark.py` for run logs):
  | workload                          | preferred backend     |
  |:----------------------------------|:----------------------|
  | complex non-Hermitian `eigvals`   | numpy + MKL (CPU)     |
  | sparse-matrix solve, low fill-in  | scipy (CPU)           |
  | small dense (N < 100)             | numpy (CPU)           |
  | all other dense linalg, N >= 100  | torch (GPU)           |
  Plan files MUST declare `workload_class: <one-of-above>` in the gate
  PRDR machinery block whenever a script is dispatched to GPU. The
  `_prdr_extended_planfreeze.py --pass-D` check refuses plan-freeze
  for any gate that pins `GPU=torch` for a workload class whose
  benchmark-validated preferred backend is CPU.
```

**Defect class caught**: mth (methodology-scrambling, environment-knob sub-class).

**S85 gate it would have caught**: §W0-6 van Hove characterization (PRDR pinned `GPU=torch` for complex non-Hermitian eigvals; ran 2-3× slower than CPU+MKL per W0-WP line 2184). The mid-session benchmark would have been pre-run; the plan would have pinned `numpy_MKL` from the start.

**Cross-check against existing rules**: extends the existing CPU-fallback guidance at line 9 (`OMP_NUM_THREADS=8` for CPU) with a workload-class table. The existing rule already implies GPU is not always optimal; the new text makes the exception structured rather than implicit.

#### G2: Rule-Text Diff to agent-standards.md (clauses e, g — AMRI pre-flight + keyword-context audit framework)

**Target file**: `.claude/rules/agent-standards.md`
**Target sections**: extend existing `### Agent-Memory Registry Inversion (AMRI)` at lines 23-31; add new sub-section for keyword-context audit framework.

##### Clause (e) — AMRI pre-flight on plan-file write-targets

**Target placement**: insert between current line 31 ("Detection tool: `computations/_agent_memory_inversion_audit.py`. Migration tool: `/shortterm <agent>` with its AMRI-PROMOTE classification (see skill).") and line 33 (`### What must NOT live in agent memory`).

**Proposed text (verbatim diff-ready)**:

```
### AMRI plan-freeze pre-flight (MANDATORY for plan files)

The AMRI 3-test (input-pin / output-target / cross-agent-overlap) is
already enforced on agent-memory snapshots via
`_agent_memory_inversion_audit.py`. It MUST also fire at plan-freeze,
on the *plan file itself*, BEFORE any gate executes.

1. **Plan-freeze AMRI walker**: `_prdr_extended_planfreeze.py --pass-C-amri`
   parses each gate-block and extracts every `write_target:` field. For
   each write-target value matching `\.claude/agent-memory/.*/(MEMORY\.md|project_.*\.md)`,
   the walker runs the AMRI 3-test:
   - Test 1 (input-pin): does ANY sibling gate's PRDR machinery block
     list this path as an `input_pin:` SHA target? If yes → AMRI fires.
   - Test 2 (output-target): is the write described as primary
     registry-maintenance (keyword scan: "watchlist", "registry",
     "roster", "table", "matrix", "list of detectors / channels /
     observables")? If yes → AMRI fires.
   - Test 3 (cross-agent-overlap): does ANOTHER agent's existing memory
     file already contain entries on the same observable / mechanism /
     detector that this gate intends to write? If yes → AMRI fires.

2. **Auto-rewrite suggestion**: When AMRI fires, the walker emits a
   diff suggesting the new write-target be redirected to
   `sessions/framework/<inferred-registry>.md` (template lookup against
   `sessions/framework/_registry-template.md`). The plan author either
   accepts the diff or annotates the gate with
   `amri_exempt_rationale: <text>` (rare; only for genuinely
   agent-private memory like an agent's own feedback rule).

3. **Plan-freeze refusal**: A plan with un-resolved AMRI firings refuses
   plan-freeze in `--strict` mode; emits a `plan_amri_violations.json`
   defect report in advisory mode.
```

**Defect class caught**: top (topological-scrambling, write-target sub-class).

**S85 gate it would have caught**: §W4-8 (plan §W4-8 originally pinned `write_target: .claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` and `project_watchlist-v85.md`; user directive flagged this mid-session per W4-WP line 830). PRDR+ PASS-C-AMRI would have rewritten the write-target to `sessions/framework/falsifier-watchlist.md` BEFORE the gate ran, eliminating the mid-session reframe.

**Cross-check against existing rules**: this is a structural extension of the existing AMRI rule, not a replacement. The 3-test definition is preserved verbatim; the new clause adds a *plan-freeze invocation point* for the existing test. No conflict with current behavior; agents can still write to their own memory for genuinely-private content (the `amri_exempt_rationale` clause).

##### Clause (g) — Keyword-context audit framework (universal audit pre-flight)

**Target placement**: new sub-section at end of file (after current line 62, the "What NOT to do" bullets).

**Proposed text (verbatim diff-ready)**:

```
## Audit-Method Pre-Flight Framework (MANDATORY for vocabulary / regex / classification audits)

Audits whose verdict depends on a numerical knob (window width, ratio
band, regex pattern, threshold count, classifier precedence) are
methodology-scrambling-vulnerable: the verdict can flip if the knob
moves and the plan does not pin the knob explicitly.

The standard audit-pre-flight pattern:

1. **Knob enumeration (mandatory)**. The audit's producing script must
   declare every numerical knob in a top-level `AUDIT_KNOBS` dict:
   ```python
   AUDIT_KNOBS = {
       "context_window_lines": 5,            # half-width in lines
       "fail_threshold": 20,                 # FAIL iff N_ambiguous > this
       "info_threshold": 5,                  # INFO band start
       "keyword_lists": {"qcd": [...], "inflationary": [...], "framework_id": [...]},
       "classifier_precedence": ["framework_id", "qcd", "inflationary", "ambiguous"],
   }
   ```

2. **Plan-block pin (mandatory)**. The plan gate-block must list every
   key from `AUDIT_KNOBS` under `audit_knobs:` with either a pinned
   value identical to the script default OR a declared
   sensitivity-scan range (`audit_knobs.context_window_lines: {pinned:
   5, sensitivity_scan: [3, 5, 10, 20]}`).

3. **Sensitivity-scan reporting (mandatory for mth-ii audits)**. When a
   sensitivity range is declared, the audit re-runs at each scan value
   and emits a per-knob-value verdict to `<gate>_sensitivity.json`. The
   primary verdict line uses the pinned value; the sensitivity JSON
   informs whether the verdict is robust under knob perturbation.

4. **Pre-flight check**. `_prdr_extended_planfreeze.py --pass-D-knobs`
   parses each producing script via AST, extracts the `AUDIT_KNOBS`
   dict, cross-references the plan gate-block's `audit_knobs:` field,
   and refuses plan-freeze if any script-declared knob is missing from
   the plan-block.

5. **Audit-knob registry**. The set of *standard* knob classes (window
   widths, ratio bands, ordering conventions) lives in a new
   `sessions/framework/audit-knob-registry.md` indexed by knob class,
   with project-level pinned values and sensitivity-band guidance.
   Plan-authors choose from the registry; ad-hoc knobs require a
   project-level decision recorded in the registry before use.
```

**Defect class caught**: mth (methodology-scrambling, audit-knob sub-class).

**S85 gates it would have caught**:
- §W1c-3 (α_s usage audit; ±5-line context window not pinned with sensitivity range; FAIL value=2193 ambiguous sites stable only at W=5; sensitivity sweep would have shown whether the count is robust);
- §W2-13 (PSG §11.2 length-ratio band 2× not pinned; revised section 10.5× over fired the INFO clause without explicit length-band project authority);
- §W4-6 (multi-D Fisher matrix-addition convention unpinned; first attempt FAILed the PSD-direction assertion per W4-WP line 714).

**Cross-check against existing rules**: parallels the existing PRDR clause for computation scripts (epistemic-discipline.md lines 76-110) but applied to AUDIT scripts specifically. The structural homology is exact: PRDR enumerates physics-machinery knobs; this clause enumerates audit-method knobs. Both are mechanical static-analysis checks at plan-freeze.

#### G3: Rule-Text Diff to epistemic-discipline.md (clauses j, h — canonical-band-authority pre-flight + stylistic-coherence preflight)

**Target file**: `.claude/rules/epistemic-discipline.md`
**Target sections**: extend `## Source Authority Hierarchy` (lines 26-34) with band-change governance; add new sub-section under `## Pre-Registration Completeness` (lines 76-111) for stylistic-coherence preflight.

##### Clause (j) — Canonical-band-authority pre-flight

**Target placement**: insert as new sub-section between current line 34 ("5. Raw computation output (lowest)") and `## Evidence Hierarchy` at line 36.

**Proposed text (verbatim diff-ready)**:

```
### Band-change authority pre-flight (MANDATORY for re-registered gates)

A "re-registered gate" is one that tests the same physics quantity
(same numerator, same comparator, same emergent observable) as a gate
in any prior session. Re-registered gates inherit the prior session's
PASS/INFO/FAIL band by default. A new plan that registers a *different*
band for the same physics gate is performing a project-level act
disguised as a per-wave decision; the act requires explicit
authorization.

1. **Band-inheritance default**. For every gate, the plan must declare
   `band_inherits_from: <prior_gate_id_or_NONE>`. If a prior gate of
   the same physics-class exists in the project's band registry, the
   default is `band_inherits_from: <that_id>` and the bands are
   copied verbatim.

2. **Band-change authorization**. If the plan declares
   `band_inherits_from: NONE` for a re-registered gate, OR sets a band
   that differs from the inherited prior, the plan-block MUST include:
   ```
   band_change_authority:
     reason: <text — why the band changed>
     authorized_by: <one-of: workshop-verdict-sha | user-directive-line |
                     registry-row-sha | initial-pre-registration>
     reference: <SHA / line-pointer / registry-row>
   ```

3. **Band registry**. A new `sessions/framework/band-registry.md`
   stores the canonical PASS/INFO/FAIL band for every physics-class
   gate, indexed by physics-class identifier (e.g., "A_s vs Planck
   central", "n_s vs Planck", "DR3 cell flip"). Plan-authors consult
   the registry; PRDR+ PASS-E cross-checks plan bands against
   registry bands.

4. **Pre-flight check**. `_prdr_extended_planfreeze.py --pass-E-bands`
   parses each gate-block, looks up the physics-class in the band
   registry, and refuses plan-freeze if a band differs from the
   registry without an `authorized_by:` pointer.

5. **External-source band-evidence**. When a gate cites an external
   paper as the source of an observational σ or central value, the
   plan-block must include `external_source_evidence:` pointing to a
   text snippet file under `sessions/external-source-evidence/<gate>/`
   containing the literal grep hit from the cited PDF showing the
   target quantity. PRDR+ PASS-E refuses plan-freeze if the evidence
   file is absent or the hit is not literal-text-from-PDF.
```

**Defect class caught**: aut (authority-scrambling).

**S85 gates it would have caught**:
- §W3-7 (30% FAIL band differs from S80's factor-2 PASS-F2 band; no `band_change_authority` pin; the relerr substitution chain confirms 0.30 < 0.5712 < 1.00 — same physics, two bands, two verdicts);
- §W1b-6 (MacInnis 2022 σ(α_s) assumed; W1b-WP line 209 confirms paper does NOT publish; PRDR+ PASS-E would have refused plan-freeze for missing `external_source_evidence:` file);
- §W1b-7 (Hazumi 2022 LiteBIRD σ(α_s) assumed; W1b-WP line 254 confirms 0 hits across all 156 pages; same PASS-E refusal).

**Cross-check against existing rules**: extends `## Source Authority Hierarchy` (lines 26-34) by adding the project-level band registry as a new HIGHEST-AUTHORITY layer for gate-band questions. Bands sit above the per-session pre-registration in the hierarchy, mirroring how the canonical_constants.py sits above per-session constant pinning. Consistent with the existing rule that "Latest synthesis wins" (line 11) — the band registry is the canonical synthesis of band decisions across sessions.

##### Clause (h) — Stylistic-coherence preflight

**Target placement**: insert as new sub-clause within `## Pre-Registration Completeness`, after the existing PRDR clause at line 88-94 (after "...Output is a structured subsection of the plan (§0.11 machinery-enumeration pin).").

**Proposed text (verbatim diff-ready)**:

```
### Stylistic-coherence preflight (MANDATORY for documentation-revision gates)

A "documentation-revision gate" rewrites a section of an existing
synthesis / framework / registry document. Such gates are
methodology-scrambling-vulnerable on TWO axes: content (what is added)
and STYLE (length-ratio, structure-ratio, sub-section count relative
to the original section).

1. **Length-ratio band declaration**. Every documentation-revision
   gate must pre-register a `length_ratio_band:` field with explicit
   PASS, INFO, FAIL thresholds, e.g.:
   ```
   length_ratio_band:
     pass_max: 1.5    # revised <= 1.5x original is unflagged
     info_max: 3.0    # 1.5x < ratio <= 3.0x is INFO
     fail_min: 5.0    # ratio > 5.0x triggers FAIL on stylistic gap
   ```

2. **Structure-ratio band declaration** (sub-section count). For
   sectioned revisions:
   ```
   structure_ratio_band:
     pass_max: 1.0    # no new sub-sections
     info_max: 3.0    # up to 3x sub-section count is INFO
   ```

3. **Pre-flight check**. `_prdr_extended_planfreeze.py --pass-D-style`
   refuses plan-freeze if either band is missing for a gate
   classified `META` with revision-type `documentation`.

4. **Verdict semantics**. A revision exceeding `info_max` but staying
   under `fail_min` produces verdict INFO with a stylistic-gap flag —
   not FAIL. The gate's content-correctness verdict is independent of
   the stylistic flag; the two are reported separately. Per existing
   "All Results Are Good Results" discipline (math-scripts.md
   line 122), the stylistic INFO is documentary, not a defeat.
```

**Defect class caught**: mth (methodology-scrambling, stylistic-knob sub-class).

**S85 gate it would have caught**: §W2-13 PSG §11.2 revision (original 6 lines → revised 63 lines, length_ratio = 10.5×; current plan §W2-13 INFO clause read "PASS with stylistic gap (e.g. §11.2 length grows > 2×) — flag but proceed" — the 2× threshold was inline-only, not a pre-registered band per W2-WP line 734; PRDR+ PASS-D-style would have required the 1.5/3.0/5.0 explicit band at plan-freeze, and 10.5× would have triggered the FAIL-min stylistic alert with explicit project-level review request).

**Cross-check against existing rules**: this clause does NOT change content-correctness verdicts (which remain governed by the gate's primary criterion). It adds a separate, parallel stylistic verdict that travels alongside the primary one. Compatible with the existing dual-SHA verdict line format (the stylistic flag becomes a 5th annotation field on the comment row).

#### G4: Rule-Text Diff to pru-pre-registration-template.md (clauses b, d, f, i — helper-file existence + regulator-conditional + external-source + PSD/Fisher guards)

**Target file**: `.claude/templates/pru-pre-registration-template.md` (verified at this path; the file is a TEMPLATE, not a `.claude/rules/` file — distinction matters because the diff updates the per-gate scaffold and not a top-level discipline rule).
**Target sections**: extend `## Gate Block` scaffold (lines 43-113); extend `## Class 8 Failure Mode (PRU)` table (lines 158-176).

##### Clause (b) — Helper-file existence pre-check

**Target placement**: insert four new fields into the Gate Block scaffold between current line 58 ("Input file 2: ...") and line 59 ("Import closure hash..."). Also extend the "—— Pre-registered inputs" section header.

**Proposed text (verbatim diff-ready, replacing lines 53-60)**:

```
—— Pre-registered inputs (SHA-256 pins + existence verification) ——
Input file 1: {{path}}
  expected_sha256 = {{hexdigest or "<computed-at-runtime>"}}
  exists_at_planfreeze = {{TRUE | FALSE — verified by os.path.exists()}}
Input file 2: {{path}}
  expected_sha256 = {{hexdigest or "<computed-at-runtime>"}}
  exists_at_planfreeze = {{TRUE | FALSE}}

Referenced helpers (auxiliary scripts not pinned by SHA but cited in the producing script):
  - {{path1}}: exists_at_planfreeze = {{TRUE | FALSE}}
  - {{path2}}: exists_at_planfreeze = {{TRUE | FALSE}}

Referenced registries (output landing targets — must exist with named anchor at plan-freeze):
  - {{path}}: exists = {{TRUE|FALSE}}, anchor = "{{section-header-or-N/A}}",
              anchor_present = {{TRUE | FALSE | NOT-APPLICABLE}}

Import closure hash (canonical_constants.py + all imports): {{hexdigest or "<computed-at-runtime>"}}
```

**Defect class caught**: ref (reference-scrambling), both helper-absent (input-side) and registry-absent (output-side).

**S85 gates it would have caught**:
- §W0-15 (cited "W5-64 f_B table" as input; W0-WP line 1379 confirms absent; `exists_at_planfreeze = FALSE` would have refused freeze);
- §W0-3, §W0-9, §W0-20 (cited `_heat_kernel_a4.py`, `_build_DK.py`, helpers not on disk per W0-WP line 2192);
- §W0-14 (5 target canonical_constants entries planned but not pre-built);
- §W0-17, §W3-8, §W3-10 (cited `summary/permanent-results-registry.md` which does not exist; `Referenced registries` block + `anchor_present` field would have caught it).

**Cross-check against existing scaffold**: extends the existing `Input file N` block (lines 53-58) with two new boolean fields per file; adds two new top-level blocks (`Referenced helpers`, `Referenced registries`). All checks are mechanical (filesystem `os.path.exists()` + grep for anchor). Compatible with existing SHA-pin discipline.

##### Clause (d) — Regulator-conditional gate detection (regulator_layers field)

**Target placement**: insert new field into the PRDR machinery block, between current line 64 ("L_max = {{int or N/A}}...") and line 65 ("scan_range = ...").

**Proposed text (verbatim diff-ready)**:

```
L_max         = {{int or N/A}}                # truncation scale
regulator_layers = {{[L1, L2, ...] | NONE}}   # if the gate's verdict depends on regulator-stratification, enumerate every layer

# When regulator_layers != NONE, the gate splits at execution time
# into one sibling sub-gate per layer. Each sub-gate produces its own
# verdict line; the parent gate's verdict is the JOIN over sub-verdicts
# per pre-registered join rule:
join_rule_for_regulator_layers:
  PASS_iff:  {{e.g. all-layers-PASS | majority-layers-PASS | first-layer-PASS}}
  FAIL_iff:  {{e.g. any-layer-FAIL | majority-layers-FAIL}}
  flip_test: {{e.g. cell-flip-across-2-adjacent-L_max | NONE}}
```

**Defect class caught**: top (topological-scrambling, regulator-stratification sub-class).

**S85 gate it would have caught**: §W1b-1 (planned a single 7-cell DR3 tree; realized requires 3 L_max sub-trees {L=8, L=10, L=12}; framework prediction flipped A1 → B2 across L_max ∈ {10, 12} per W1b-WP lines 22-28). The new `regulator_layers: [8, 10, 12]` field plus `flip_test: cell-flip-across-2-adjacent-L_max` would have made the regulator-stratification first-class at plan-freeze.

**Cross-check against existing scaffold**: extends the PRDR machinery block (lines 61-72) with a new optional field. When `regulator_layers = NONE`, no behavior change — backwards compatible. When set, fires the regulator-stratification check via `_prdr_extended_planfreeze.py --pass-C-regulator`.

##### Clause (f) — External-source-existence pre-check

**Target placement**: insert as new top-level block in the Gate Block scaffold, between current line 73 ("All other free parameters explicitly pinned: ...") and line 74 ("—— Pre-registered pass/fail criterion ——").

**Proposed text (verbatim diff-ready)**:

```
—— External-source binding (MANDATORY when gate cites a paper as source-of-σ-or-target) ——
external_source_cited:    {{paper-id or "NONE"}}
external_source_pdf:      {{path-on-disk or "NONE"}}
external_source_pdf_sha:  {{hexdigest or "NONE"}}
external_source_evidence: {{path-to-grep-snippet-file or "NONE"}}
                          # File contains the literal PDF text where the cited
                          # quantity appears, with page number. PRDR+ PASS-E
                          # refuses plan-freeze if external_source_cited != NONE
                          # AND evidence file is missing or empty.
expected_target_quantity: {{e.g. "sigma_alpha_s" or "sigma_w_0"}}
verified_present:         {{TRUE | FALSE | PRE-REG-INCOMPLETE-IF-FALSE}}
```

**Defect class caught**: aut (authority-scrambling, external-source sub-class).

**S85 gates it would have caught**:
- §W1b-6 (MacInnis 2022 cited; W1b-WP line 209-225 confirms σ(α_s) is NOT published — verified_present should have been FALSE pre-execution);
- §W1b-7 (Hazumi 2022 cited; 0 grep hits per W1b-WP line 254 — verified_present should have been FALSE pre-execution).

Both gates landed PRE-REG-INCOMPLETE correctly at execution; the new field would have classified them at plan-freeze, saving the wave-time cost of running the verification.

**Cross-check against existing scaffold**: orthogonal addition to the PRU machinery block; does not change pre-existing pin discipline. The PRE-REG-INCOMPLETE clause from `epistemic-discipline.md` §Pre-Registration Completeness already exists; the new field exposes that classification at plan-freeze rather than only at execution time.

##### Clause (i) — PSD/Fisher arithmetic guard (matrix-addition convention pin)

**Target placement**: insert as new sub-block under the "—— Pre-registered machinery (PRDR pin)" block, between current line 70 ("GPU path = ...") and line 72 ("All other free parameters explicitly pinned:").

**Proposed text (verbatim diff-ready)**:

```
GPU path      = {{torch.linalg|numpy.linalg|cpu-cap-OMP8}}
workload_class = {{complex_eigvals | real_eigh | hermitian_eigh | matmul | fft | sparse_solve | small_dense | other}}

# When the gate involves Fisher / covariance / PSD arithmetic, the
# matrix-addition convention MUST be pinned:
matrix_arithmetic_convention:
  type:                {{Fisher-addition | data-covariance-discount | mixed-with-explicit-split | NOT-APPLICABLE}}
  PSD_ordering:        {{Loewner-monotone | regime-dependent | NOT-APPLICABLE}}
  common_mode_handling: {{shared-parameter-discount | independent-channel-sum | NOT-APPLICABLE}}
  inverse_chain:       {{F_full_then_invert | invert-each-then-sum-info | per-element | NOT-APPLICABLE}}

# Substitution chain for the PSD direction is REQUIRED in Step 4 of the
# substitution-chain block when matrix_arithmetic_convention != NOT-APPLICABLE.
```

**Defect class caught**: mth (methodology-scrambling, matrix-arithmetic sub-class).

**S85 gate it would have caught**: §W4-6 multi-D Fisher (initial script attempt mixed Fisher-addition with off-diagonal data-covariance and triggered the `σ_joint > σ_single_best` PSD-direction violation; second pass corrected per W4-WP line 714). Pre-registering `type: Fisher-addition + data-covariance-discount`, `common_mode_handling: shared-parameter-discount`, `inverse_chain: F_full_then_invert` at plan-freeze would have made the regime explicit and the first-pass PSD violation a plan-edit, not a runtime failure.

**Cross-check against existing scaffold**: extends the GPU/workload pinning block; orthogonal to the existing scheme/convention pinning. Both fields default to `NOT-APPLICABLE` for non-Fisher gates — backwards compatible.

##### Clause (extension) — Class 8 Failure Mode table extended for PRDR+ sub-classes

**Target placement**: extend the existing table at lines 161-171 with five new rows for the plan-layer scrambling sub-classes.

**Proposed text (verbatim diff-ready, replacing lines 162-171)**:

```
| # | Failure | Type | Prevented by |
|:--|:--------|:-----|:-------------|
| 1 | Convention-shopping | execution | Pre-registered scheme field |
| 2 | Ansatz-forced PASSes | execution | Pre-registered threshold |
| 3 | Vacuous-margin | execution | Pre-registered convention + tolerance |
| 4 | Load-and-compare-to-self | execution | Independent target value |
| 5 | Linear-rescale-as-cross-check | execution | Pre-registered cross-check method |
| 6 | Iterate-until-PASS | execution | One-shot execution + verdict |
| 7 | False cross-checks | execution | Pre-registered cross-check criterion |
| **8** | **PRU (machinery unpinned)** | **plan-property** | **This template + PRDR** |
| **8a** | **sym (symbol-collision plan-vs-canonical)** | **plan-property** | **PRDR+ PASS-A (`_prdr_referent_audit.py --pin-collision`)** |
| **8b** | **ref (referenced helper / registry absent)** | **plan-property** | **PRDR+ PASS-B (helper + registry existence checks added in clause (b))** |
| **8c** | **top (regulator-stratification + AMRI write-target)** | **plan-property** | **PRDR+ PASS-C (clause (d) regulator_layers + agent-standards.md AMRI plan-freeze)** |
| **8d** | **mth (audit-knob / GPU-pin / matrix-arithmetic)** | **plan-property** | **PRDR+ PASS-D (clause (i) matrix_arithmetic_convention + agent-standards.md AUDIT_KNOBS)** |
| **8e** | **aut (external-source / band-change unauthorized)** | **plan-property** | **PRDR+ PASS-E (clause (f) external_source_evidence + epistemic-discipline.md band-change authority)** |
```

**Defect class caught**: meta — ALL FIVE plan-layer scrambling sub-classes from K1's taxonomy. Makes the template self-documenting against the new PRDR+ regime.

**S85 gates it would have caught**: meta — by enumerating the sub-classes in the failure-mode table, the template guides plan-authors to identify which sub-class their gate is vulnerable to and which clause prevents it. This is documentation infrastructure, not a per-gate check.

**Cross-check against existing rules**: extends the existing Class 8 framing (lines 158-176) with a 5-row sub-decomposition. The decomposition is new; the parent classification ("plan-property failure") is unchanged.

#### G5: Rule-Text Diff to /rclab-plan skill (composite check — runs all 10 above pre-flights at plan-freeze)

**Target file**: `.claude/skills/rclab-plan/skill.md`
**Target sections**: insert new Phase 3f (between current Phase 3e at lines 368-433 and Phase 4 at lines 436-479); extend Phase 4 user checkpoint (lines 440-477); extend Safety Rules (lines 685-697).

##### Composite clause — Phase 3f: PRDR+ extended pre-flight orchestration

**Target placement**: insert as new sub-section between current line 433 (end of "Phase 3e: Upstream-reference pin validation" rationale block) and line 434 ("---"). The new phase is the structural sibling of Phase 3e: same per-wave mechanical-validator pattern, different defect class.

**Proposed text (verbatim diff-ready)**:

```
### 3f. PRDR+ extended pre-flight (MANDATORY per-wave)

After each wave plan file passes 3d existence/grep checks AND 3e
upstream-pin validation, invoke the PRDR+ extended orchestrator on it:

```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" \
  computations/_prdr_extended_planfreeze.py --json \
  --wave-plan "sessions/session-plan/session-{N}-plan-w{i}.md" \
  --canonical-constants computations/canonical_constants.py \
  --plan-dir sessions/session-plan/ \
  > "sessions/session-plan/session-{N}-plan-w{i}-prdr-extended.json"
```

The orchestrator runs five passes against the wave plan file, one per
plan-layer scrambling mode (sym, ref, top, mth, aut). Exit codes:

- **0 (PASS)** — all five passes returned zero defects. Proceed to
  Phase 4.

- **1 (HARD FAIL)** — one or more passes reported plan-layer defects:
  - PASS-A (sym): plan inline pin collides with canonical_constants
    (e.g., `K_crit = 2.0446` in plan vs canonical `K_crit = 91.5`).
  - PASS-B (ref): a `referenced_helpers:`, `referenced_registries:`,
    or path-shaped input/write field points at a target absent at
    plan-freeze.
  - PASS-C (top): a regulator-axis branch in the producing script is
    not enumerated in `regulator_layers:`, OR a `write_target:`
    triggers the AMRI 3-test (input-pin / output-target / cross-agent-overlap).
  - PASS-D (mth): an `AUDIT_KNOBS` script-declared knob is missing
    from the plan-block's `audit_knobs:`, OR a `GPU=torch` pin
    contradicts the workload-class benchmark map, OR a Fisher/PSD gate
    lacks `matrix_arithmetic_convention:`.
  - PASS-E (aut): a band differs from the project band registry without
    `band_change_authority:` pointer, OR an external-source citation
    lacks an `external_source_evidence:` file.

  Do NOT silently forward. Per Safety Rule 9 ("stalls do not justify
  degrading the spec"), a HARD FAIL requires either:
  - **Edit the wave plan** to resolve the defect (rewrite pin, build
    the missing helper as a Wave-0 deliverable, enumerate the
    regulator layer, pin the audit knob, add the band-change
    authorization). Re-run the orchestrator until exit 0.
  - **Strict-mode override** (rare, project-level decision):
    `--strict=false` accepts an advisory-only run. Each non-zero
    pass is recorded in the wave plan as a comment block citing the
    accepted-deferral rationale.

- **2 (PARSE-ERROR)** — plan file structurally malformed beyond what
  the regex / AST can interpret. Treat as planner-stall-equivalent
  per 3c stall-handling protocol: split the wave and re-dispatch.

Write the orchestrator's JSON report to
`sessions/session-plan/session-{N}-plan-w{i}-prdr-extended.json` for
audit trail. The Phase 4 user-checkpoint report reads this file and
surfaces non-zero exit codes verbatim alongside the existing 3e report.

**Rationale (S85 W3 origin)**: S85 produced 11 plan-layer defects
across W0-W5, of which 2 (sig_5 dual-SHA hardcodes, sig_4 R3 schema
gaps) were already covered by existing post-session audits, and 9 were
plan-LAYER scrambles uncovered only at execution time. PRDR+ closes
the plan-layer hole at plan-freeze, complementing the existing PRDR
(intra-script machinery) and Phase 3e (upstream-pin validation).

The orchestrator is orthogonal to:
- `_yaml_gate_validator.py` (R3 schema completeness)
- `_pru_cardinality_audit.py` (machinery-pin cardinality)
- `_plan_upstream_pin_validator.py` (upstream npz pin drift, Phase 3e)

All four should run per wave before Phase 4.
```

**Defect class caught**: composite — all five plan-layer scrambling sub-classes (sym, ref, top, mth, aut).

**S85 gates it would have caught**: ALL 11 plan-layer defects from the workshop topic list at plan-freeze. Specific mappings:
- PASS-A: §W0-15 (K_crit triple-collision)
- PASS-B: §W0-3, §W0-9, §W0-15, §W0-17, §W0-20, §W3-8, §W3-10 (helpers + registry absent), §W1b-9 (r_max layer-interface symbol overload — caught at sym level too)
- PASS-C: §W1b-1 (regulator-conditional DR3), §W4-8 (AMRI write-target)
- PASS-D: §W0-6 (GPU pin wrong for ROCm), §W1c-3 (keyword window not pinned with sensitivity), §W2-13 (length-ratio band not pinned), §W4-6 (PSD-ordering convention not pinned)
- PASS-E: §W1b-6, §W1b-7 (external-source assumed), §W3-7 (band tightening unauthorized)

##### Extension to Phase 4 user-checkpoint report

**Target placement**: extend Phase 4 reporting block at lines 440-468. Insert the PRDR+ summary after the existing 3e report block.

**Proposed text (verbatim diff-ready, replacing relevant chunk of lines 453-461)**:

```
=== UPSTREAM-PIN VALIDATION (Phase 3e) ===

{summary per wave: PASS / FAIL / PARSE-ERROR with mismatch count}

=== PRDR+ EXTENDED PRE-FLIGHT (Phase 3f) ===

{summary per wave: per-pass PASS/FAIL counts; e.g.:
   Wave 1: PASS-A=PASS, PASS-B=2 defects (helper-absent), PASS-C=PASS, PASS-D=1 defect (knob-unpinned), PASS-E=PASS
   Wave 2: ALL PASS
   Wave 3: PASS-A=1 defect (sym-collision with canonical), PASS-B=PASS, PASS-C=PASS, PASS-D=PASS, PASS-E=1 defect (band-change unauthorized)
}

{if any FAIL across 3e or 3f: list each HARD defect verbatim, referencing
 sessions/session-plan/session-{N}-plan-w{i}-{validation|prdr-extended}.json}

{if any PARSE-ERROR: flag the offending wave for re-dispatch per 3c
 stall-handling protocol}
```

##### Extension to Safety Rules

**Target placement**: extend the numbered list at lines 685-697 with three new rules.

**Proposed text (verbatim diff-ready, append as items 12-14)**:

```
12. **Plan-layer scrambling has its own discipline.** PRDR (intra-script
    machinery) and PRDR+ (plan-vs-realized-filesystem) are orthogonal;
    both must pass per wave before Phase 4. A plan that passes PRDR
    but fails PRDR+ is still PRU-vulnerable at the plan-LAYER level.
13. **Five plan-layer scrambling modes.** sym (symbol collision), ref
    (reference absent), top (DAG-mismatch — regulator + AMRI), mth
    (audit-knob / environment / matrix-arithmetic), aut (external-
    source / band-change authority). Phase 3f orchestrator runs one
    pass per mode.
14. **Strict-vs-advisory governance.** PRDR+ defaults to advisory
    (`--strict=false` reports defects, allows freeze with logged
    rationale). For high-stakes plans (theorem registrations,
    DR3-class observational gates), override to `--strict=true` so
    defects block plan-freeze. The strict/advisory choice is a
    project-level decision per session, recorded in §0.10 of the
    consolidated plan.
```

**Defect class caught**: meta — these rules document the discipline that the per-pass tools enforce.

**S85 gate it would have caught**: meta — by codifying the five-mode taxonomy in the skill's safety rules, future plan-authors are guided to recognize and prevent each class. The discipline-level enforcement complements the tool-level enforcement.

**Cross-check against existing skill structure**: extends Phase 3e (already a per-wave mechanical-validator pattern) with a parallel Phase 3f (same pattern, different defect class). Compatible with the existing dispatch-orchestrator architecture; no changes to Phase 0-3 or Phase 4.5-6.

#### G6: Questions for kitaev

These questions stage Round 2 convergence. The first five engage your K7-close questions directly; the last three raise specific design points where my Re: sections diverged from yours.

**Q1 — Engagement with your Q1 (rule-file allocation).** I commit to the five-file diff (math-scripts.md / agent-standards.md / epistemic-discipline.md / pru-pre-registration-template.md / rclab-plan skill). My G1-G5 above proposes verbatim text for each. Do you see any clause that should migrate between files in my proposal — e.g., should the AMRI plan-freeze pre-flight (G2 clause e) live in epistemic-discipline.md instead of agent-standards.md, given that AMRI is structurally a project-level governance rule and only operationally an agent-memory rule? My instinct: keep it in agent-standards.md because the existing AMRI rule is there; promotion to epistemic-discipline.md would split the rule across two files. But I'd accept the migration if you argue project-level governance dominates.

**Q2 — Engagement with your Q2 (strict vs advisory).** I committed in Re:K7 to advisory by default with `--strict` opt-in; you proposed strict-by-default for sym/ref/top and advisory for mth/aut. There is a real disagreement here. My reasoning: a single low-severity stylistic mth defect (e.g., W2-13's 10.5× length-ratio without project-level authorization) should not block the plan from freezing — it should be a flag the plan-author resolves manually. Your reasoning, as I read it: structural defects (sym/ref/top) are physics-blocking and must hard-block; methodology defects (mth/aut) are softer. Convergence proposal: strict-by-default for {sym, ref, top.regulator, top.AMRI}, advisory-by-default for {mth.audit-knob, mth.GPU-pin, mth.matrix-arithmetic, aut.external-source-with-PRE-REG-INCOMPLETE-fallback}, and strict-by-default for {aut.band-change}. This is finer-grained than either of our initial positions — does this 5-bin discipline match the framework's risk-tolerance shape, or is it over-engineered?

**Q3 — Engagement with your Q3 (canonical-symbol drift retroactive enforcement).** I support retroactive provenance pinning for ALL existing 180+ canonical entries, but as a Wave-0 mechanical task in the next session, NOT as a blocking pre-condition. The mechanical task: walk every canonical_constants.py top-level binding, look up its origin via `git blame` + session-search, write a `update_constant(name, value, session, source, comment)` call for each, run all of them, audit. This is O(180) one-time work, can be parallelized, and once done turns the audit into a maintenance discipline rather than a back-fill burden. Do you agree this is the right scope, or do you see a phased approach (only retroactively pin canonical entries that have been *referenced by a plan-inline pin within the last N sessions*, where N=10 say)?

**Q4 — Engagement with your Q4 (audit-knob registry home).** I committed in G2 clause (g) to `sessions/framework/audit-knob-registry.md` (project-level registry, plan-edit-friendly). You proposed three options: canonical_constants.py / new audit_knob_registry.py / sessions/framework/. My reasoning for the third: audit knobs are not physics constants (they don't appear in spectral moments of D_K), they are DOCUMENTATION-LAYER decisions about how to measure documentation hygiene. The right home is therefore the framework registry, not canonical_constants.py. Do you agree, or do you see audit knobs as more constant-like (in which case canonical_constants.py with a `# AUDIT KNOB` section header is also defensible)?

**Q5 — Engagement with your Q5 (retroactive validation against S78-S84).** I commit to retroactive PRDR+ run as an S86 carry-forward, NOT as part of Round 2 of this workshop. Round 2 is for closing the rule-file diff design; running PRDR+ across 7 sessions × ~80 plans each is a one-shot mechanical task that produces a coverage report — important data, but a different kind of work from the rule-text design we are converging on now. My commitment: include "Run PRDR+ retroactively against S78-S84 plans; report coverage metric (catches > 50% of subsequently-discovered plan-layer defects? if not, identify the missing mode classes)" as the leading carry-forward in this workshop's wrap-up. Acceptable structuring?

**Q6 — Lyapunov-vs-checklist (my Re:K1 disagreement).** I disagreed with promoting Δ from a per-mode boolean matrix to a scalar aggregate, arguing the project's no-constraint-counts-as-arguments rule (`epistemic-discipline.md` line 9) forbids scalar metrics. You framed Δ as a "monotonic deviation coordinate." Do you see a way to keep the Lyapunov-style structural claims (monotonicity, non-decay, downstream amplification) without exposing Δ as a scalar in any reported metric? My proposal: the boolean per-mode-per-gate matrix IS the metric; the Lyapunov language is a structural property of the matrix (specifically: each row's modes are non-decay-monotone in time, and downstream gates inherit row contents), but the matrix itself never collapses to a number. Convergence prep: are the structural properties what you wanted from the Lyapunov framing, or is the scalar aggregate load-bearing for some claim I'm missing?

**Q7 — OTOC-vs-diffusive (my Re:K8 disagreement).** I argued plan-layer scrambling is *diffusive* (linear in consumer count) rather than *OTOC-style* (exponential), because plan-layer dependency-DAG amplification lacks the chaotic-Hamiltonian + Heisenberg-evolved-commutator structure that defines OTOC. The fix-cost analysis is the same either way (PRDR+ is mechanical and bounded), but the framing matters for how we explain the discipline to plan-authors: "linear amplification through gate consumers" is intuitive; "OTOC growth" requires explaining many-body chaos. Are you committed to the OTOC framing for a structural reason I missed, or is "diffusive" acceptable as the project-document-facing language while keeping "OTOC-style" as a chaos-theorist's mental model?

**Q8 — Latent-mode resolution-time axis (my Re:K1 emergence point).** I proposed a sixth resolution-time category — latent-mode — for defects whose pre-flight check is well-defined but requires partial execution to evaluate (e.g., W1b-1's regulator-stratification flip A1→B2 was knowable as a STRUCTURAL AXIS at plan-freeze but the specific cell-flip outcome was not statically inferable). PRDR+ catches the structural-axis defect at plan-freeze (good); it does NOT auto-execute partial wave to detect cell-flips. Should the rule-text address latent-mode explicitly with a "partial-execution dry-run" sub-protocol, or is treating latent-mode as a Phase 3.5 between plan-freeze and full-wave-dispatch the cleaner architecture? My instinct: the latter; PRDR+ stays mechanical-only at plan-freeze, latent-mode dry-runs are a separate (potentially expensive) discipline that fires only for high-stakes regulator-axis gates. Round 2 convergence: do we agree to scope PRDR+ to mechanical static checks and defer latent-mode dry-run to a separate rule (or carry-forward)?

---

## Round 2 — kitaev: Follow-up

### CONVERGENCE

I concede on four points where gen-physicist sharpened the framing. Each concession is followed by what I am committing to in the rule-text design.

**C1 — OTOC-as-diffusive (Re:K8, Q7).** Conceded. The plan-layer phenomenon is **diffusive**, not OTOC. The substitution chain that forces this:

```
Step 1: OTOC growth requires (i) a chaotic many-body Hamiltonian H,
        (ii) Heisenberg-evolved operator W(t) = e^{iHt} W e^{-iHt},
        (iii) the squared-commutator C(t) = -<[W(t), V(0)]^2> growing
        as exp(lambda_L * t) before saturating at the scrambling time.    [definition; Maldacena-Shenker-Stanford]
Step 2: The plan-layer dependency DAG has no operator algebra. The
        "polluted symbol propagating to N consumers" propagates through
        STATIC import-edges, not Heisenberg time-evolution. The growth
        in number of contaminated nodes is N_consumers(d) where d is
        graph-distance from the polluted root.                            [structural fact about DAGs]
Step 3: For a finite DAG with bounded out-degree k, N_consumers(d) <= k^d
        nodes within distance d, so amplification is at most polynomial-
        in-d. The actual S85 plan DAGs have k ~ 2-3 average out-degree
        and depth ~ 3-4 waves, so N_consumers <= O(N_gates) — strictly
        LINEAR in the gate count, not exponential in time.                [substitution; bounded-DAG fact]
Step 4: lambda_L (plan-layer) = 0 by the same argument that gives
        lambda_L (substrate) = 0: there is no chaotic many-body
        time-evolution. The substrate's lambda_L = 0 is enforced by
        [iK_7, D_K] = 0; the plan-layer's lambda_L = 0 is enforced by
        the DAG being a DAG (acyclic, finite, no operator dynamics).      [direction]
Step 5: The correct framing is DIFFUSIVE amplification: a single sym
        defect at a parent contaminates each consumer with multiplicative
        REACH (linear in N_consumers), no exponential growth, no
        thermalization-like saturation.                                   [direction]
Conclusion: "Plan-layer scrambling is diffusive amplification through
            the consumer DAG" is the correct project-document-facing
            language. "OTOC-style" was an over-reach analogy. The
            structural-similarity to chaos diagnostics is via the
            Lyapunov-style monotonicity (CONVERGENCE C4 below), NOT
            via OTOC-exponential growth.
```

**Substrate-framing audit on this analogy.** The substrate-physics OTOC measures operator-norm growth in a quantum chaotic system (chaotic H, Hilbert space, operator algebra). The plan-layer "scrambling" is information-theoretic deviation between the plan-DAG and the filesystem-DAG — there is no Hilbert space, no operators, no time-evolution. They share the **language** of chaos diagnostics (monotonicity, non-decay, downstream amplification) but the plan-layer is **structurally similar, not physics-derived**. Forward I will write "diffusive amplification (structural analog of OTOC growth)" when the rule-text needs an intuitive hook, and reserve "OTOC growth" only where genuine many-body chaos is being discussed.

**C2 — mth split into mth-i / mth-ii / mth-iii (Re:K5).** Conceded. The original mth lumped three operationally distinct cases. The split:

| sub-class | definition | S85 example |
|:---------|:-----------|:------------|
| **mth-i** | Audit knob unpinned at plan-freeze | W2-13 length-ratio band 2x not pinned; W4-6 PSD-ordering convention not pinned |
| **mth-ii** | Audit knob pinned but no sensitivity-scan range declared | W1c-3 keyword window W=5 was deliberately pinned (per W1c-WP line 448) but no sensitivity scan was declared |
| **mth-iii** | Environment-pin valid in general but invalid for the specific workload class | W0-6 GPU=torch correct for real Hermitian eigh but 2-3x slower than numpy/MKL for complex non-Hermitian eigvals |

The PRDR+ PASS-D check from K7 needs sub-passes: PASS-D-i (knob enumeration in `AUDIT_KNOBS` script-side and in `audit_knobs:` plan-side); PASS-D-ii (sensitivity-scan range field on every audit-knob, optional but flagged); PASS-D-iii (workload-class declaration in PRDR machinery block, cross-checked against the benchmark map). gen-physicist's G1 clause (c) workload-class table and G2 clause (g) AUDIT_KNOBS dict already implement PASS-D-iii and PASS-D-i respectively; PASS-D-ii is the new addition I am adding from this concession (extension to G2 clause (g) point 3, "Sensitivity-scan reporting (mandatory for mth-ii audits)" — the clause already exists; we are now naming the sub-class).

**C3 — Latent-mode resolution-time axis as a 6th defect-class category (Re:K1, Q8).** Conceded. Latent-mode is **orthogonal to {sym, ref, top, mth, aut}** — it is a resolution-time axis: when does the defect become observable? My K1 taxonomy implicitly treated all 5 modes as static-at-plan-freeze, which is wrong for two of the 11 S85 defects:

```
Step 1: Define resolution_time(d) for each defect d as the EARLIEST
        process step at which d's pre-flight check returns a definitive
        verdict.                                                          [definition]
Step 2: For sym/ref/top.AMRI/mth-i/mth-iii/aut.external-source/aut.band-change:
        resolution_time = plan-freeze (mechanical static analysis).      [substitution]
Step 3: For top.regulator (W1b-1 sub-tree flip A1->B2):
        the regulator-stratification axis (L_max ∈ {8, 10, 12}) is
        STATICALLY KNOWN at plan-freeze, but whether the cell-flip
        manifests requires partial execution at L=10 and L=12.            [substitution]
Step 4: For top.AMRI mid-session (W4-8 user-directive-flagged):
        resolution_time = mid-session, AFTER plan-freeze — the
        AMRI 3-test was not invoked on the plan file at freeze in S85.    [substitution; current S85 baseline]
Step 5: With PRDR+ in place, W4-8 resolution_time MOVES UP to
        plan-freeze (PASS-C-AMRI walker on plan file). W1b-1 resolution
        time remains "structural axis at plan-freeze + cell-flip at
        partial execution" — it is irreducibly latent.                   [direction after PRDR+]
Conclusion: Latent-mode is a residual category that PRDR+ does NOT
            eliminate. It identifies defects requiring partial-execution
            dry-runs (a Phase 3.5 between plan-freeze and full-wave-
            dispatch). I accept gen-physicist's proposal: scope PRDR+
            to mechanical static checks at plan-freeze; carry latent-
            mode dry-run as a separate discipline (Phase 3.5) for
            high-stakes regulator-axis gates only.
```

The taxonomy now has TWO axes: scrambling-mode {sym, ref, top, mth-i, mth-ii, mth-iii, aut} (7 sub-modes) × resolution-time {plan-freeze, latent (partial-execution), runtime}. The 11 S85 defects map to (mode, resolution-time) pairs; PRDR+ catches everything in the plan-freeze column.

**C4 — Scalar Δ violates the no-counts rule; per-mode discipline replaces it (Re:K1, Q6).** Conceded — but only on the rhetorical surface. The structural property I wanted from the Lyapunov framing was monotonicity-in-remediation, non-decay, and inherited downstream contamination. None of those properties require a scalar. I now state the metric as a **per-gate × per-mode boolean matrix** χ(g, α) ∈ {0, 1}, with the structural properties:

1. **Per-row monotonicity-in-remediation**: for any gate g, χ(g, α) decreases (1→0) only via explicit plan-edits resolving mode α; never by execution-time activity.
2. **Inheritance**: if gate g consumes the polluted output of parent p, then χ(g, α) >= χ(p, α) for the propagating mode α (the consumer inherits at least the parent's contamination).
3. **No-decay-without-edit**: across waves W_1 → W_2 → ... → W_K, χ(g, α) for unrepaired (g, α) pairs is constant; no implicit thermalization.

These are properties of the **matrix itself**, not of any sum over it. The matrix is reportable as a boolean grid (6 rows × 11 gates for S85; or 7 sub-modes × 11 gates with the C2 split); a single PASS/FAIL bit ("plan-blocks-freeze: yes/no") is the only scalar exposed externally and that bit is the Boolean OR over all entries — not a sum, not a magnitude. This is consistent with `epistemic-discipline.md` line 9 ("Never cite constraint counts as arguments") and gen-physicist's Re:K1 critique. The Lyapunov-style framing survives as **structural property of the matrix**, not as a numerical aggregate.

### DISSENT

I retain three points where gen-physicist's choice differs from mine. None of these are workshop-blocking; they are design preferences that should be recorded so the Round-2 final and rule-file v2 PR can adjudicate.

**D1 — Strict-vs-advisory granularity (Re:K7, Q2).** gen-physicist's Q2 proposed a 5-bin discipline: strict-by-default for {sym, ref, top.regulator, top.AMRI}, advisory for {mth.audit-knob, mth.GPU-pin, mth.matrix-arithmetic, aut.external-source-with-PRE-REG-INCOMPLETE-fallback}, strict for {aut.band-change}. I accept the convergence proposal as an improvement over my original "strict for sym/ref/top, advisory for mth/aut" but I disagree on **two specific bins**:

(i) **mth.matrix-arithmetic should be strict-by-default, not advisory.** The W4-6 PSD-ordering substitution chain in K5 showed that the mixed-formulation produces a verdict in the WRONG DIRECTION (Step 5' vs Step 5). A wrong-direction verdict in an advisory regime contaminates downstream consumers before the plan-author's manual review can fire. PSD-direction is structurally analogous to a sign error in a physics computation, not a stylistic flag. Strict-by-default is the right discipline.

```
Step 1: A wrong-direction verdict on a Fisher information bound has
        consequences for every downstream gate consuming sigma_joint.    [structural fact]
Step 2: Advisory mode allows plan-freeze with an unresolved direction
        defect; downstream consumers run with a polluted sigma_joint.    [substitution]
Step 3: Direction errors propagate by inheritance (CONVERGENCE C4
        property 2), so consumer verdicts inherit a wrong-direction
        bound.                                                            [substitution]
Step 4: The cost of a wrong-direction sigma_joint flowing into a
        downstream verdict is IRREVERSIBLE absent re-running every
        consumer; the cost of strict-block on PSD-direction is one
        plan-edit at freeze.                                              [direction: cost-asymmetry]
Step 5: Strict-by-default for mth.matrix-arithmetic minimizes
        irreversible cost.                                                [direction]
Conclusion: mth.matrix-arithmetic belongs in the strict bin alongside
            aut.band-change.
```

(ii) **mth-ii (knob pinned, no sensitivity-scan) should be advisory; mth-i (knob unpinned) should be strict.** gen-physicist's bin lumped both as advisory. The structural distinction is from CONVERGENCE C2: mth-i is a missing pin (the audit's verdict cannot be reproduced); mth-ii is a missing robustness check (the audit's verdict is reproducible but its sensitivity to knob perturbation is unknown). mth-i should hard-block freeze (the verdict is structurally meaningless without the pin); mth-ii should advisory-flag (the verdict is meaningful but its robustness is undocumented).

Final discipline I am proposing: **strict-by-default** for {sym, ref, top.regulator, top.AMRI, mth-i, mth-iii, mth.matrix-arithmetic, aut.band-change}; **advisory-by-default** for {mth-ii, aut.external-source-with-PRE-REG-INCOMPLETE-fallback}. Two strict-bin additions to gen-physicist's Q2 proposal.

**D2 — AMRI plan-freeze rule should appear in BOTH agent-standards.md AND epistemic-discipline.md (Re:K4, Q1).** gen-physicist's Q1 instinct was to keep AMRI in agent-standards.md only. I disagree partially. The AMRI 3-test is operationally an agent-memory rule (where it currently lives at agent-standards.md lines 27-42), but the plan-freeze enforcement is a **project-level governance** decision (refusing plan-freeze on cross-agent overlap). That governance layer belongs in epistemic-discipline.md.

Concretely: the 3-test definition stays in agent-standards.md (operational); a one-paragraph cross-reference under `## Source Authority Hierarchy` in epistemic-discipline.md notes that registry-class write-targets are project-scope (sessions/framework/) and that PRDR+ PASS-C-AMRI is the plan-freeze enforcement. Two-file presence is not duplication — it is layering: agent-standards.md is the operational manual; epistemic-discipline.md is the authority hierarchy. The two-line cross-reference is what establishes that AMRI sits in the project-level governance hierarchy, not just the agent-private hygiene hierarchy.

**D3 — On the load-bearing part of the Lyapunov framing (Re:K1, Q6).** gen-physicist's Q6 asked whether the Lyapunov framing is load-bearing or whether the per-mode boolean matrix suffices. I conceded the scalar Δ in CONVERGENCE C4. I do **not** concede that the Lyapunov language is rhetorical decoration. The load-bearing claim is the **monotonicity-in-remediation** structural property of the matrix:

```
Step 1: Define matrix evolution: chi_t(g, alpha) is the matrix at
        wall-clock time t.                                                [definition]
Step 2: Permitted transitions: chi_t(g, alpha) = 0 if t < freeze AND
        defect not yet detectable; chi_t(g, alpha) = 1 if defect
        present at freeze AND not yet remediated; chi_t(g, alpha) = 0
        AGAIN only if a plan-edit at time t' > t resolves alpha for g.   [substitution: rules of evolution]
Step 3: Forbidden transition: chi_t(g, alpha) = 1 -> chi_{t+1}(g, alpha) = 0
        WITHOUT a plan-edit. Specifically: an execution-time PASS does
        NOT clear a plan-freeze chi = 1; the plan-state mismatch persists
        even if the gate's physics verdict is PASS.                       [substitution: monotonicity rule]
Step 4: Property: for any (g, alpha), chi(g, alpha) is monotone-non-
        increasing in time only along plan-edit transitions, equivalently
        constant-or-decreasing in t MEASURED IN PLAN-EDIT TIME (not
        wall-clock).                                                      [direction; this IS Lyapunov-style]
Step 5: Conclusion: the matrix has a Lyapunov-function STRUCTURE
        (monotone-decreasing along the legitimate evolution direction);
        the function is the NUMBER OF UNCLEARED ENTRIES, and it
        decreases only along plan-edits. The scalar count itself is
        not exposed as evidence (per epistemic-discipline.md line 9);
        the structural property "chi only decreases along plan-edits"
        IS exposed as the discipline's correctness invariant.            [direction]
Conclusion: The Lyapunov framing IS load-bearing as a STRUCTURAL
            property statement, even with the scalar removed. The
            project's correctness claim "PRDR+ converges to chi = 0
            in finitely many plan-edits" is the convergence claim of
            a Lyapunov function in plan-edit time. This is what
            justifies bounded termination of PRDR+ (analogous to
            v3-closure-recovery.md's bounded-iteration termination
            proof).
```

So: scalar Δ is gone (CONVERGENCE C4); Lyapunov-as-structural-property stays. The wording "Lyapunov-style monotonic deviation matrix" replaces my original "Lyapunov-style metric Δ" in any rule-text. The correctness invariant rule-authors write should read: "PRDR+ defect-matrix chi(g, alpha) is monotone-non-increasing along plan-edit transitions." That sentence is enforceable, mechanical, and has no scalar count.

### EMERGENCE

Cross-pollination produced two structural insights neither agent had alone.

**E1 — Two κ channels: within-gate (κ_intra) and cross-gate (κ_inter), mapping to substrate's GGE relic vs spectral-action propagator.** gen-physicist's Re:K8 surfaced a "cross-gate cascade" mechanism that my K8 framing missed: damage is super-additive not only within-gate (sym+ref at W0-15) but also across-gate-via-shared-input (canonical → A → B). This is a SECOND κ channel. The plan-layer Lyapunov function therefore has two deviation channels:

| channel | mechanism | substrate-physics analog | S85 example |
|:--------|:----------|:-------------------------|:------------|
| **κ_intra** (within-gate) | two modes firing on same gate; e.g., sym (K_crit triple) + ref (f_B table absent) at W0-15 | substrate's GGE relic permanence — defects within a single dynamical sector that cannot be redistributed by intra-sector evolution | W0-15 (sym + ref); W1b-9 (sym + top hybrid: r_max layer-interface) |
| **κ_inter** (across-gate) | one mode propagating through the consumer DAG via shared input/output | substrate's spectral-action propagator carrying a defect from one fiber to its neighbor through a_n Seeley-DeWitt coupling | canonical K_crit → consumer downstream gates; W3-8/W3-10 absent registry blocking ALL future landing attempts |

The structural homology to substrate physics is exact:

```
Step 1: GGE relic permanence (Ordered Veil) — within a single dynamical
        sector, the GGE charges {Q_n} are conserved and cannot be
        redistributed by any intra-sector unitary evolution; the relic
        is permanent to t/t_universe = 10^{578} (per agent memory
        ADH prethermalization).                                           [definition; from S36/S58]
Step 2: Plan-layer kappa_intra: within a single gate, defects (sym, ref,
        top, mth-i, ...) on that gate cannot be cleared by execution-
        time activity on that gate; only by plan-edit on the gate.        [substitution; CONVERGENCE C4 property 1]
Step 3: Spectral-action propagator — across fibers, the a_n Seeley-DeWitt
        coefficients couple neighboring fibers' eigenvalue spectra; a
        defect at one fiber propagates to neighbors through a_n.          [definition; standard NCG]
Step 4: Plan-layer kappa_inter: a polluted output at gate p propagates
        to consumer gate c through the input-pin edge (p -> c); the
        consumer inherits the pollution unless the pin re-resolves.       [substitution; CONVERGENCE C4 property 2]
Step 5: Both kappa channels exist at substrate AND plan layer;
        substrate has them with lambda_L = 0 (Ordered Veil enforces
        finite reach via [iK_7, D_K] = 0); plan layer has them with
        lambda_L = 0 (DAG enforces finite reach via acyclicity).          [direction]
Conclusion: Plan-layer Lyapunov function decomposes as
            chi_total = chi_intra + chi_inter (both monotone-non-
            increasing along plan-edits), structurally homologous to
            the substrate's GGE-relic + spectral-action-propagator
            decomposition of the Ordered Veil's information flow.
```

**Substrate-framing audit on this homology.** I am NOT claiming the plan-layer phenomenon IS the substrate phenomenon. I am claiming structural similarity: both are information-flow problems on a structured graph (substrate: fiber-bundle over M^4; plan: dependency DAG over gate-blocks); both have intra-node and inter-node coupling channels; both require an algebraic constraint to enforce information-conservation (substrate: [iK_7, D_K] = 0; plan: PRDR+ pre-flight). The substrate is logically prior; plan-layer integrability is engineered to match. This is structural-similarity, NOT physics-derived.

**E2 — PRDR+ PASS-C needs sub-passes for κ_intra and κ_inter; the cross-gate test requires plan-DAG global walk.** Re:K4 raised that AMRI's input-pin test (test 1) is structurally a CROSS-GATE check (it asks: do other sibling gates pin this path?). This generalizes: PASS-C needs both per-gate and cross-gate sub-passes.

| sub-pass | scope | what it checks |
|:---------|:------|:---------------|
| **PASS-C-i (intra)** | per-gate | regulator_layers enumeration on the gate's own producing script; AMRI write-target check against THIS gate's write_target field |
| **PASS-C-ii (inter)** | cross-gate | for each gate's write_target, scan ALL OTHER gates' input_pin fields to detect cross-agent-overlap (AMRI test 1); for each polluted parent canonical entry, scan ALL consumer gates that import that name |

The cross-gate sub-pass requires a **plan-DAG global walk** — operationally: parse all gate-blocks into a graph, compute consumer-relations, then run cross-checks. gen-physicist's G2 clause (e) text "the input-pin test (test 1 of AMRI) requires checking *other gates' PRDR machinery blocks*" implicitly requires this; making it an explicit sub-pass clarifies the scope. The cost is O(N_gates^2) in the worst case but typical S85 plans have N_gates ~ 50-100, so the walk is sub-second.

This decomposition is what makes PRDR+ implementation tractable: PASS-C-i is per-gate-local (cheap, embarrassingly parallel); PASS-C-ii requires a global plan parse but is still mechanical. Both pass states feed into the chi(g, alpha=top) matrix entries.

**E3 (compact) — Latent-mode + κ_inter together imply Phase 3.5 partial-execution dry-run is FOR cross-gate cascades, not just intra-gate flips.** CONVERGENCE C3 introduced latent-mode (W1b-1 cell-flip across L_max). EMERGENCE E1 introduced κ_inter. Combined: a regulator-axis flip at gate g changes g's verdict, which changes downstream consumers — so latent-mode defects propagate via κ_inter at execution time. This means Phase 3.5's partial-execution dry-run is not just an intra-gate sanity check; it is a TWO-LEVEL probe: (a) does the gate's own verdict flip across regulator layers? (b) if so, do downstream consumers' verdicts flip with it? Architectural implication for the rule-text: Phase 3.5 should pin a **propagation-radius** (default: one wave forward) for each latent-mode gate. This prevents the dry-run from being either too narrow (single-gate, missing cascade) or too expensive (full re-run of all downstream gates). The propagation-radius pin is the analog of the substrate's `c_S` propagation-cone: a structural bound on how far a perturbation reaches in plan-edit time.

### QUESTIONS

I answer gen-physicist's 8 questions in G6 directly, then pose two final questions for gen-physicist's R2 closing.

**A1 (response to Q1, rule-file allocation).** I accept the five-file diff as proposed. On the AMRI-placement question: per DISSENT D2 above, my preference is to keep the operational AMRI 3-test in agent-standards.md and add a one-paragraph cross-reference in epistemic-discipline.md under `## Source Authority Hierarchy`. The cross-reference establishes project-level governance authority over registry-class write-targets without duplicating the 3-test definition. Two-file presence is layering, not duplication. Concretely: G2 clause (e) text stays in agent-standards.md as written; G3 gains a 4-line cross-reference paragraph noting "AMRI plan-freeze enforcement (see agent-standards.md §AMRI) operates within this authority hierarchy as a project-level governance check, not a per-agent hygiene check."

**A2 (response to Q2, strict vs advisory).** I converge on the 5-bin discipline as proposed BUT with two strict-bin additions per DISSENT D1: mth.matrix-arithmetic moves to strict; mth-ii (knob pinned without sensitivity-scan) is the only mth sub-class remaining advisory. Final discipline:

| bin | members | rationale |
|:----|:--------|:----------|
| **STRICT (block plan-freeze)** | sym, ref, top.regulator, top.AMRI, mth-i, mth-iii, mth.matrix-arithmetic, aut.band-change | Wrong-direction or missing-pin defects propagate by inheritance; cost of strict-block at freeze is one plan-edit; cost of advisory-pass is irreversible downstream contamination |
| **ADVISORY (flag, allow freeze)** | mth-ii (sensitivity-scan range missing), aut.external-source (with PRE-REG-INCOMPLETE fallback at execution) | Verdict is reproducible but robustness undocumented; PRE-REG-INCOMPLETE classification at execution already handles downstream consumers |

The 5-bin proposal becomes a 2-bin verdict with 8 strict members and 2 advisory members. Not over-engineered — it is mechanically enumerable, each member maps to a specific PASS sub-check, and the strict/advisory split is grounded in cost-asymmetry per D1.

**A3 (response to Q3, retroactive provenance pinning).** Agreed with gen-physicist's full-retroactive-as-Wave-0 proposal. The mechanical task is well-defined (walk every canonical_constants.py top-level binding, look up origin via git blame + session-search, write `update_constant(...)` calls, audit). Estimated cost: O(180 entries) × ~5 min/entry for the human-in-the-loop session-search step ≈ 15 hours total, parallelizable across waves. I do NOT support the phased N=10 cutoff: the cutoff would leave older canonical entries un-pinned, and any future plan author resurrecting an old entry (which happens — S70/S74 BdG K_crit_BdG tracks back to an entry not referenced in 10+ sessions) would hit the same ambiguity. Full retroactive is a one-time cost; phased is a permanent ambiguity floor. Carry-forward computation: "S86-W0-CC-PROVENANCE-BACKFILL: walk all 180+ canonical_constants entries, attach (session, source_gate, comment) provenance via update_constant(); no entry is exempt." Effort: high (15-20 hours). EVOI: high (eliminates the K_crit-class collision permanently).

**A4 (response to Q4, audit-knob registry home).** Agreed with gen-physicist: `sessions/framework/audit-knob-registry.md`. Audit knobs are not physics constants; they are documentation-layer methodology decisions. Putting them in canonical_constants.py would conflate the two layers and create a maintenance burden (canonical_constants is read-only at computation; audit knob updates are plan-edit-friendly project-level decisions). The framework registry is the right home. I do NOT see audit knobs as constant-like: a constant is something the substrate's physics determines (M_KK, Delta_BCS, ...); an audit knob is something the project decides to use as a measurement convention. Different ontology, different home.

**A5 (response to Q5, retroactive PRDR+ validation against S78-S84).** Agreed: S86 carry-forward, not Round 2 work. The carry-forward I commit to: "S86-W0-PRDR-RETROACTIVE: run `_prdr_extended_planfreeze.py` against every plan file in sessions S78-S84 (post-S78 scrubbed plans). Report coverage as: (defects caught at hypothetical plan-freeze) / (plan-layer defects subsequently discovered at execution). Acceptance threshold: > 50% coverage; if below, identify missing mode classes and extend the taxonomy." Effort: medium (1-2 waves). EVOI: high — validates the spec's empirical content beyond S85's by-construction completeness.

**A6 (response to Q6, Lyapunov-vs-checklist).** Agreed with gen-physicist on the per-mode-per-gate boolean matrix as the metric. The Lyapunov language survives as a structural property of the matrix, not as a scalar (CONVERGENCE C4 + DISSENT D3). The structural properties I wanted are: (i) monotonicity-in-remediation along plan-edit transitions; (ii) inheritance through DAG consumers; (iii) no implicit thermalization. None of these require a scalar; all three are statements about the matrix's allowed evolution. Rule-text language: "PRDR+ defect-matrix chi(g, alpha) is monotone-non-increasing along plan-edit transitions; non-monotonic transitions (chi = 1 → 0 without plan-edit) are forbidden by the discipline." That sentence is the Lyapunov claim, scalar-free.

**A7 (response to Q7, OTOC-vs-diffusive).** Agreed on diffusive as the project-document-facing language (CONVERGENCE C1). I retain "Lyapunov-style monotonic deviation matrix" as the formal-discipline language (DISSENT D3). The substitution chain in CONVERGENCE C1 demonstrates lambda_L = 0 at plan-layer (no operator dynamics, no exponential growth). OTOC-style was an over-reach analogy. Project-facing rule-text uses "diffusive amplification through the consumer DAG"; chaos-theorist's mental model can still call it "structural analog of OTOC growth on a static DAG" but the term OTOC does not appear in any rule-file or plan-author-facing document.

**A8 (response to Q8, latent-mode resolution-time architecture).** Agreed: PRDR+ stays mechanical-only at plan-freeze; latent-mode dry-run is a separate Phase 3.5 discipline triggered only for high-stakes regulator-axis gates. The structural separation is clean: PRDR+ is O(plan_size) mechanical static analysis; Phase 3.5 partial-execution dry-run is O(partial_wave_runtime) actual execution at one or two regulator-layer values. Mixing them would conflate the cost models. Per EMERGENCE E3, Phase 3.5 should pin a propagation-radius (default 1 wave forward) so that the dry-run captures κ_inter cascades but does not balloon into a full re-run. Carry-forward: "S86-PHASE-3.5-SPEC: design and implement Phase 3.5 partial-execution dry-run protocol for top.regulator latent-mode gates. Inputs: list of high-stakes regulator-axis gates from S85+S86 plans; pinned propagation-radius (default 1 wave forward); dry-run trigger condition (regulator_layers field non-empty AND PRDR+ PASS-C-regulator clean). Output: protocol document + reference implementation."

**Q-final-1 (kitaev → gen-physicist for R2 close).** The 8-strict + 2-advisory bin discipline (A2) requires that mth-ii's sensitivity-scan field default to a project-level recommended scan-range (e.g., context_window_lines: scan over [3, 5, 10, 20]) rather than each plan-author choosing ad-hoc. The audit-knob registry (A4) is the natural home for these recommended scan-ranges. Should the registry distinguish (i) RECOMMENDED scan-ranges (advisory; plan-author may override with rationale) from (ii) MANDATORY scan-ranges (strict; for high-impact audits like W1c-3-class vocabulary contamination)? My instinct: yes, with a small mandatory list (vocabulary-contamination, length-ratio, PSD-ordering) and a larger recommended list. This determines whether the registry has a one-level or two-level structure. Round-2-final decision point.

**Q-final-2 (kitaev → gen-physicist for R2 close).** EMERGENCE E1's two-channel decomposition (κ_intra + κ_inter) implies the rule-text should state the chi-matrix discipline as TWO independent monotonicity claims: (i) per-gate-row monotonicity (κ_intra remediation); (ii) plan-DAG-global monotonicity (κ_inter remediation). Both are required; remediating κ_intra alone does not auto-clear κ_inter contamination at consumers. For rule-file v2: should the discipline statement read "chi is monotone in plan-edits along BOTH the gate-row and the DAG-consumer axis" (single combined statement) or as two separate clauses ("intra-gate plan-edit clears κ_intra; cross-gate plan-edit at parent + consumer-re-fire clears κ_inter")? The two-clause form is more enforceable mechanically (each clause maps to a distinct PRDR+ sub-pass: PASS-C-i intra; PASS-C-ii inter); the single-statement form is more compact for rule-readers. Round-2-final closes this with the workshop verdict — your call on which form lands in the rule-file v2 PR.

---

## Round 2 — gen-physicist: Cross-Synthesis (FINAL)

### CONVERGENCE

I accept four of kitaev's R2 commitments and cement the unified rule-file v2 diff.

**G2-CONV-1 — Cross-gate cascade as second κ channel (R2-K-EMER-1, κ_intra / κ_inter).** Accepted. My Re:K8 cross-gate cascade observation is now fully formalized as a SECOND κ mechanism distinct from K8's same-gate κ_{α,β}. The plan-layer Lyapunov function decomposes as `χ_total = χ_intra + χ_inter`, with both components monotone-non-increasing along plan-edit transitions. The substrate-physics homology is structural-similarity, not physics-derivation — kitaev's R2-K-EMER-1 audit-paragraph correctly disclaims this. I commit to the substrate-framing audit language verbatim: PRDR+ is the plan-layer's engineered analog of the substrate's [iK_7, D_K] = 0 algebraic constraint; the substrate is logically prior; the plan-layer constraint is what we engineer to mirror it. This rules out the inverted reading "the substrate's integrability is justified by PRDR+" which would be a container-thinking violation of `phononic-framing.md`.

**G2-CONV-2 — Lyapunov as monotonic-in-remediation property despite linear (not exponential) amplification (R2-K-CONV-1 + R2-K-DISS-3 + A6).** Accepted. The substitution chain in R2-K-CONV-1 (Steps 1-5) settles the OTOC question: λ_L (plan-layer) = 0 because the plan-DAG is a finite, acyclic, operator-algebra-free graph; growth in contaminated-node count is at most O(N_gates) (linear), not exp(λ_L · t). The Lyapunov-style framing survives as the **monotonicity-in-remediation structural property** of the χ matrix (R2-K-DISS-3 Steps 1-5). That property is load-bearing — it is what justifies bounded termination of PRDR+ — but does not require a scalar Δ to be exposed in any reported metric. Final rule-text language committed: "PRDR+ defect-matrix χ(g, α) is monotone-non-increasing along plan-edit transitions; non-monotonic transitions (χ = 1 → 0 without plan-edit) are forbidden by the discipline." Scalar-free, mechanically enforceable, consistent with `epistemic-discipline.md` line 9.

**G2-CONV-3 — mth split into mth-i / mth-ii / mth-iii (R2-K-CONV-2).** Accepted verbatim. mth-i = knob unpinned at plan-freeze; mth-ii = knob pinned but no sensitivity-scan declared; mth-iii = environment-pin valid in general but invalid for the specific workload class. The PRDR+ PASS-D check decomposes into three sub-passes (PASS-D-i, PASS-D-ii, PASS-D-iii), each mapping to one rule-file v2 clause. The sub-class table from R2-K-CONV-2 is the canonical taxonomy.

**G2-CONV-4 — Latent-mode as 6th resolution-time category, orthogonal to the 7-mode scrambling axis (R2-K-CONV-3 + A8).** Accepted. The defect taxonomy now has TWO axes:

| axis | values |
|:-----|:-------|
| scrambling-mode | {sym, ref, top.regulator, top.AMRI, mth-i, mth-ii, mth-iii, aut.external-source, aut.band-change} (9 sub-modes after the C2 split) |
| resolution-time | {plan-freeze, latent (partial-execution), runtime} |

PRDR+ is the discipline for plan-freeze-resolvable defects. Phase 3.5 (partial-execution dry-run) is the discipline for latent defects, with propagation-radius pin (default 1 wave forward per R2-K-EMER-3) bounding the dry-run cost. Architectural separation is clean: PRDR+ is O(plan_size) static analysis; Phase 3.5 is O(partial_wave_runtime) actual compute. The two are orthogonal and feed independent S86 carry-forwards.

**G2-CONV-5 — Two strict-bin additions (R2-K-DISS-1, A2).** Accepted. The cost-asymmetry argument in R2-K-DISS-1 Steps 1-5 is structurally identical to my own G3-clause-(j) reasoning for band-change strictness:

```
Substitution chain on cost-asymmetry for mth.matrix-arithmetic:
  Step 1: Define cost(strict-block, freeze)   = 1 plan-edit at plan-freeze.            [definition]
  Step 2: Define cost(advisory-pass, propagate) = N_consumers × σ_re-fire-each.        [definition]
  Step 3: σ_re-fire-each ≥ 1 plan-edit + 1 wave-execution per polluted consumer.       [substitution: minimum re-run cost]
  Step 4: For S85 typical N_consumers ~ 3-5 per polluted parent (W4-6 σ_joint feeds
          downstream parameter-extraction gates), cost(advisory) ~ 3-5× cost(strict).  [substitution]
  Step 5: cost(advisory) > cost(strict) ⇒ strict-by-default minimizes irreversible
          cost.                                                                         [direction]
  Conclusion: mth.matrix-arithmetic belongs in the strict bin.
```

Final 8-strict / 2-advisory discipline (per R2-K-A2 table) committed:

- **STRICT** (block plan-freeze): {sym, ref, top.regulator, top.AMRI, mth-i, mth-iii, mth.matrix-arithmetic, aut.band-change} — 8 members.
- **ADVISORY** (flag, allow freeze): {mth-ii, aut.external-source-with-PRE-REG-INCOMPLETE-fallback} — 2 members.

This replaces my Q2 5-bin proposal verbatim.

### DISSENT

I retain two narrow disagreements after R2-K-DISS. Neither is workshop-blocking; both are recorded for the rule-file v2 PR adjudication.

**G2-DISS-1 — On the AMRI two-file placement (R2-K-DISS-2, A1).** kitaev proposes the operational AMRI 3-test stays in `agent-standards.md` and a 4-line cross-reference paragraph appears in `epistemic-discipline.md` under `## Source Authority Hierarchy`. I dissent partially: I prefer the cross-reference live under `epistemic-discipline.md`'s `## Pre-Registration Completeness` section, NOT under `## Source Authority Hierarchy`. Reasoning:

```
Substitution chain on AMRI placement direction:
  Step 1: AMRI's plan-freeze enforcement is mechanical static analysis on the plan
          file (`_prdr_extended_planfreeze.py --pass-C-amri`).                          [definition]
  Step 2: Source Authority Hierarchy (lines 26-34) ranks WHICH source wins on
          conflict (Skeptic > synthesis > gate verdict > minutes > raw output).        [definition]
  Step 3: Pre-Registration Completeness (lines 76-111) defines PRU/PRDR — what must
          be enumerated at plan-freeze for a gate to be admissible.                    [definition]
  Step 4: AMRI plan-freeze enforcement is ONTOLOGICALLY a pre-registration-
          completeness check (it asks "is this gate's write-target enumerated correctly
          at plan-freeze?"), NOT an authority-hierarchy claim ("which source wins?").  [substitution]
  Step 5: The cross-reference belongs alongside PRU/PRDR, not alongside the source
          ranking.                                                                      [direction]
  Conclusion: epistemic-discipline.md cross-reference goes under Pre-Registration
              Completeness as a PRDR+ sibling clause, not under Source Authority
              Hierarchy.
```

Concrete diff change vs R2-K-A1: epistemic-discipline.md gains the AMRI cross-reference paragraph as part of the new Pre-Registration Completeness sub-section (alongside the existing PRDR clause + the new PRDR+ sub-section), not under Source Authority Hierarchy. The agent-standards.md operational text is unchanged from G2 clause (e). Rule-file v2 PR records this as the placement decision.

**G2-DISS-2 — On Q-final-1 audit-knob registry level-structure (one-level vs two-level).** kitaev proposes a two-level audit-knob registry (RECOMMENDED scan-ranges advisory + MANDATORY scan-ranges strict) with a small mandatory list (vocabulary-contamination, length-ratio, PSD-ordering). I dissent: a two-level registry recreates the strict/advisory bin distinction at the registry level, which the 8-strict / 2-advisory discipline already encodes at the PRDR+ pass level. Two layers of strict/advisory designation is redundant.

```
Substitution chain on the redundancy:
  Step 1: 8-strict / 2-advisory bin discipline (G2-CONV-5) classifies mth-ii (knob
          pinned without sensitivity-scan) as ADVISORY at the PRDR+ pass level.       [definition]
  Step 2: Two-level registry would re-classify a subset of mth-ii audits as MANDATORY
          (= strict) via the registry-level mechanism.                                  [substitution]
  Step 3: A subset of mth-ii promoted to strict via registry-level is operationally
          identical to that subset moved into the strict-bin at PRDR+ level.          [substitution: identity]
  Step 4: Two ways to express the same strict/advisory split = redundant
          machinery; one mechanism suffices.                                           [direction]
  Step 5: The simpler mechanism is the PRDR+ bin; promote sensitivity-scan-mandatory
          audits to mth-i (= strict) at the bin level rather than via registry level.  [direction]
  Conclusion: One-level registry suffices. Audits where sensitivity-scan is mandatory
              are promoted from mth-ii to mth-i (= strict) at the PRDR+ pass level,
              with the registry recording the recommended scan-range.
```

Final design committed in this dissent: the audit-knob registry has **one level** with structured fields per knob `{pinned_value, recommended_scan_range, scan_mandatory: bool}`. When `scan_mandatory: true`, the gate's PRDR+ classification is mth-i (strict) by virtue of "knob unpinned (because no scan range pinned)" rather than mth-ii (advisory). The vocabulary-contamination / length-ratio / PSD-ordering audits get `scan_mandatory: true` in the registry; everything else defaults to `scan_mandatory: false`. The registry is a flat lookup; the PRDR+ pass decides strict vs advisory from the registry field.

### EMERGENCE

Two structural insights cement the unified rule-file v2 diff as the workshop's load-bearing output. The first is the canonical orderings; the second is the regression-test-suite specification.

**G2-EMER-1 — Canonical orderings of the rule-file v2 diff.** The five-file diff (math-scripts.md / agent-standards.md / epistemic-discipline.md / pru-pre-registration-template.md / rclab-plan skill) has TWO canonical orderings:

(i) **Application order** (the order in which a plan-author hits the rules during plan-write → plan-freeze):

```
1. /rclab-plan skill — invokes Phase 3f orchestrator (G5)
2. pru-pre-registration-template.md — gate-block scaffold the plan-author fills (G4 clauses b, d, f, i + Class-8-extension)
3. math-scripts.md — canonical-constants + GPU-pin discipline applied per gate (G1 clauses a, c)
4. agent-standards.md — AMRI 3-test + AUDIT_KNOBS framework applied per gate (G2 clauses e, g)
5. epistemic-discipline.md — band-change authority + stylistic-coherence preflight applied per gate (G3 clauses j, h)
```

(ii) **Authority order** (the order in which the rules win on conflict):

```
1. epistemic-discipline.md — top-level discipline; band-change authority overrides plan-author wave choice
2. agent-standards.md — operational rules; AMRI 3-test definition is canonical
3. math-scripts.md — script-level discipline; canonical-constants binding is canonical for symbol-pin pairs
4. pru-pre-registration-template.md — gate-block scaffold; defines what fields exist
5. /rclab-plan skill — orchestration glue; runs the checks
```

These are NOT the same order. The application order goes scaffold-up (template → script → discipline); the authority order goes discipline-down (authority → operational → script → template → glue). The rule-file v2 PR must respect both: a plan-author fills bottom-up but on conflict, top-down wins. This dual-ordering is the structural reason the diff is FIVE files and not one — collapsing them into a single rule-file would conflate the two orderings.

**Substitution chain on the dual-ordering necessity:**

```
Step 1: Plan-author workflow at plan-write time runs scaffold-up:
        instantiate template fields → cite canonical constants → satisfy operational
        rules → satisfy discipline-level authority → run orchestration.                [definition]
Step 2: Conflict-resolution at plan-freeze runs discipline-down: discipline wins
        over operational, operational wins over script-level, script-level wins
        over template, template wins over orchestration.                                [definition: standard authority hierarchy]
Step 3: Single-file collapse would force one ordering as canonical. Whichever
        ordering is chosen, the OTHER ordering's mental model breaks.                   [substitution]
Step 4: Plan-authors rely on application order (it's how they write); reviewers
        rely on authority order (it's how they adjudicate conflicts).                   [substitution]
Step 5: BOTH orderings must be preserved for the rule-system to remain workable;
        the five-file structure is what enables them to coexist.                        [direction]
Conclusion: The five-file rule-file v2 diff is structurally necessary, not just a
            convenient organizational choice. Each file plays a distinct role in the
            two orderings; collapse breaks the workflow.
```

**G2-EMER-2 — PRDR+ regression-test suite specification.** Following the V3-recovery synthetic-test pattern (`.claude/rules/v3-closure-recovery.md` lines 175-200), PRDR+ requires a `_prdr_extended_selftest.py` regression-test harness. The 11 S85 defect topics map to 11 minimal mock-plan-files, one per defect class, each with the expected mode-firing pattern. The suite has THREE structural-property tests beyond the per-mode catches:

| test | input | expected | property tested |
|:-----|:------|:---------|:----------------|
| `test_pin_collision_W0_15_kcrit` | mock plan with `K_crit = 2.0446` inline pin | exit 1, PASS-A defect | sym detection |
| `test_helper_absent_W0_15_fb_table` | mock plan citing nonexistent `W5_64_fb_table.npz` | exit 1, PASS-B defect | ref detection (input-side) |
| `test_registry_absent_W3_8_perm_results` | mock plan writing to nonexistent `permanent-results-registry.md` without anchor | exit 1, PASS-B defect | ref detection (output-side, with anchor sub-check from Re:K3) |
| `test_regulator_unenumerated_W1b_1` | mock producing-script branching on L_max with no `regulator_layers:` field | exit 1, PASS-C-i defect | top.regulator detection |
| `test_amri_writetarget_W4_8` | mock plan writing to `.claude/agent-memory/.../MEMORY.md` for cross-channel matrix | exit 1, PASS-C-ii defect | top.AMRI detection (cross-gate walk) |
| `test_audit_knob_unpinned_W2_13` | mock plan with audit script declaring `AUDIT_KNOBS` but plan-block missing `audit_knobs:` | exit 1, PASS-D-i defect | mth-i detection |
| `test_sensitivity_scan_missing_W1c_3` | mock plan with audit knob pinned but no sensitivity-scan field, registry says `scan_mandatory: true` | exit 1, PASS-D-i (promoted from mth-ii) | mth-ii / mth-i promotion via registry |
| `test_gpu_pin_wrong_class_W0_6` | mock plan with `GPU=torch` for `workload_class: complex_eigvals` | exit 1, PASS-D-iii defect | mth-iii detection |
| `test_psd_arithmetic_unpinned_W4_6` | mock plan with Fisher gate lacking `matrix_arithmetic_convention:` | exit 1, PASS-D defect (matrix-arithmetic strict bin) | mth.matrix-arithmetic detection |
| `test_external_source_unverified_W1b_6` | mock plan citing paper without `external_source_evidence:` file | exit 1, PASS-E defect (advisory) | aut.external-source detection |
| `test_band_change_unauthorized_W3_7` | mock plan tightening band from S80 PASS-F2 to 30% without `band_change_authority:` | exit 1, PASS-E defect (strict) | aut.band-change detection |
| `test_clean_plan_passes` | mock plan with all fields correctly pinned, all referents present | exit 0, no defects | negative control: no false positives on a clean plan |
| `test_chi_matrix_monotonicity` | sequence of mock plans with progressive plan-edits | χ matrix monotone-non-increasing along the edit sequence | structural property: Lyapunov monotonicity (G2-CONV-2) |
| `test_kappa_inter_cascade` | mock plan with polluted parent canonical entry imported by 3 consumer gates | PASS-A fires once, but 4 chi entries are flagged (parent + 3 consumers) | structural property: κ_inter cascade detection (E1) |

13 tests total: 11 per-defect-class catches + 1 clean-plan negative control + 2 structural-property tests. The suite runs as the first part of the orchestrator's CI integration; failure of any test fails the rule-file v2 PR. This is what makes PRDR+ DURABLE across sessions — without the harness, future code changes can break a defect-class detection silently.

**The unified diff is the workshop's load-bearing output.** Five files, ten clauses, 13 regression tests. Each clause traces to one or more S85 defects via the substitution chains in K1-K8 and G1-G5. The strict/advisory bin assignment (G2-CONV-5) determines plan-freeze block behavior. The application/authority dual-ordering (G2-EMER-1) determines file structure. The χ-matrix discipline (G2-CONV-2 + G2-DISS-2) determines the correctness invariant. Substrate-framing audit: PRDR+ is the documentation-layer engineered analog of [iK_7, D_K] = 0; the substrate's information-conservation is logically prior; PRDR+ is what we engineer to mirror it at the plan layer. This is structural similarity, not physics derivation — both kitaev's R2-K-EMER-1 audit-paragraph and my Re:K7 EMERGES paragraph affirm this disclaimer.

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Pin-collision (K_crit triple) | K2, Re:K2, G1 clause (a), R2-K-CONV (no R2 retention) | **Converged** | K_crit is triple-valued (91.5 inflationary / 2.035 BdG / 2.0446 K_corr_upper); rule-file v2 forbids plan-inline pins of canonical names (PRDR+ PASS-A), and three distinct canonical entries with provenance replace the single overloaded symbol. |
| 2 | Helper-absent + registry-absent | K3, Re:K3, G4 clause (b), R2-K-A1 | **Converged** | Reference-scrambling is detected by path-shaped-value pre-flight (not field-name list); registry-absent requires an additional anchor-presence sub-check beyond os.path.exists; both land in PRDR+ PASS-B via pru-pre-registration-template.md scaffold. |
| 3 | GPU-pin selectivity | K1, K5, G1 clause (c), R2-K-CONV-2 (mth-iii) | **Converged** | Environment-pin must be workload-class-conditioned via a benchmark-validated map; complex non-Hermitian eigvals on ROCm is the canonical mth-iii defect; PRDR+ PASS-D-iii enforces the workload_class declaration at plan-freeze. |
| 4 | Regulator-conditional gate detection | K4, Re:K4, G4 clause (d), R2-K-CONV-3, R2-K-EMER-3 | **Emerged** | Regulator-stratification has TWO resolution times: structural axis (caught at plan-freeze via PRDR+ PASS-C-i) and cell-flip latent-mode (caught only by Phase 3.5 partial-execution dry-run with propagation-radius pin); the dual treatment is the new architectural commitment. |
| 5 | r_max min-identity collapse class | K1, G4 clause (b)+(d), G2-DISS (no R2 retention) | **Converged** | r_max layer-interface is the canonical hybrid-mode defect (sym + top): single symbol overloaded across two layer indices with no stratification; PRDR+ PASS-A catches the sym sub-defect, PASS-C-i catches the layer-stratification absence; both fire on the same gate-row of the χ matrix. |
| 6 | Canonical-entry / registry-file absent | K3, G4 clause (b), R2-K-A3 | **Converged** | Five canonical_constants entries + permanent-results-registry.md must be Wave-0 deliverables in S86; full retroactive provenance backfill of all 180+ canonical entries is committed as S86-W0-CC-PROVENANCE-BACKFILL (no phased N=10 cutoff). |
| 7 | AMRI pre-flight | K4, Re:K4, G2 clause (e), R2-K-DISS-2, G2-DISS-1 | **Partial** | AMRI 3-test extends to plan-files via PASS-C-amri (cross-gate walk for input-pin test) — converged; placement of the cross-reference paragraph in epistemic-discipline.md is contested (kitaev: under Source Authority Hierarchy; gen-physicist: under Pre-Registration Completeness) — rule-file v2 PR adjudicates per G2-DISS-1 substitution chain. |
| 8 | Keyword-context audit framework | K5, Re:K5, G2 clause (g), R2-K-CONV-2, R2-K-A2 | **Converged** | mth split into mth-i (knob unpinned, strict) / mth-ii (no sensitivity-scan, advisory) / mth-iii (workload-class wrong, strict); AUDIT_KNOBS dict in producing scripts cross-checked against plan-block audit_knobs: field; sensitivity-scan recommended-range lives in audit-knob registry. |
| 9 | Stylistic-coherence preflight | K5, G3 clause (h) | **Converged** | Documentation-revision gates pre-register length_ratio_band and structure_ratio_band as separate from content-correctness verdict; W2-13 §11.2 10.5× revision triggers stylistic INFO with explicit project-level review request, content verdict travels independently. |
| 10 | PSD/Fisher arithmetic guard | K5, G4 clause (i), R2-K-DISS-1, G2-CONV-5 | **Converged** | mth.matrix-arithmetic moves to STRICT bin (cost-asymmetry: wrong-direction σ_joint is irreversible at consumers; strict-block costs one plan-edit); pru-pre-registration-template.md gains matrix_arithmetic_convention block with type/PSD-ordering/common-mode/inverse-chain fields. |
| 11 | External-source + canonical-band-authority pre-flight | K6, Re:K6, G3 clause (j), G4 clause (f), R2-K-A2 | **Converged** | aut splits into aut.external-source (advisory with PRE-REG-INCOMPLETE fallback) and aut.band-change (strict, requires band_change_authority pointer); external_source_evidence/ directory stores literal grep snippets from cited PDFs; band-registry sits above per-session pre-registration in the authority hierarchy. |
| 12 | Unified rule-file v2 diff | G5 + R2 convergence + G2-EMER-1 + G2-EMER-2 | **Emerged** | Five-file diff is structurally necessary (dual application/authority orderings; collapse breaks the workflow); 8-strict / 2-advisory bin discipline is mechanically enumerable; 13-test regression harness (11 per-defect catches + clean-plan negative control + 2 structural-property tests for χ-monotonicity and κ_inter cascade) makes PRDR+ durable across sessions. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

Each item is specific enough to become an S86 computation or a follow-up workshop. Pre-registered gates per `.claude/rules/epistemic-discipline.md`.

1. **PRDR+ retroactive coverage validation against S78-S84** (R2-K-A5 commitment). What fraction of plan-layer defects subsequently discovered at execution in S78-S84 would PRDR+ have caught at plan-freeze? Pre-registered gate: **PASS** iff coverage > 50%; **INFO** if 25-50% with a documented missing mode-class identification; **FAIL** if < 25% (taxonomy is structurally incomplete and requires extension before S86 plan-write).

2. **Phase 3.5 partial-execution dry-run protocol design** (R2-K-A8 commitment, R2-K-EMER-3). Design + reference implementation for top.regulator latent-mode gates with propagation-radius pin (default 1 wave forward). Pre-registered gate: **PASS** iff Phase 3.5 catches the W1b-1-class A1→B2 cell-flip on a mock regulator-axis gate with pinned propagation-radius=1; **FAIL** if the protocol either misses the flip (propagation-radius too narrow) or balloons into full re-run (propagation-radius unbounded).

3. **Audit-knob registry one-level vs two-level resolution** (Q-final-1, G2-DISS-2). The G2-DISS-2 substitution chain argues one-level with `scan_mandatory: bool` field. Pre-registered gate: **PASS** if rule-file v2 PR lands one-level registry as proposed; **INFO** if two-level is implemented with documented rationale why bin-level promotion is insufficient.

4. **χ-matrix discipline statement form: single combined vs two-clause** (Q-final-2). The two κ channels (κ_intra + κ_inter) imply two monotonicity claims. Pre-registered gate: **PASS** if rule-file v2 lands the two-clause form (one clause per κ channel, each mapping to a distinct PRDR+ sub-pass); **INFO** if combined-statement form lands with documented rationale.

5. **Retroactive provenance backfill execution coverage** (R2-K-A3, S86-W0-CC-PROVENANCE-BACKFILL). Pre-registered gate: **PASS** iff all 180+ canonical_constants top-level bindings have non-null `(session, source_gate, comment)` provenance after the backfill wave; **INFO** if 90-100% with documented exceptions; **FAIL** if < 90%.

6. **κ_inter detection on real S85 plan** — does the 13-test regression suite's `test_kappa_inter_cascade` correctly fire on the actual S85 W0-15 K_crit cascade through downstream consumer gates? Pre-registered gate: **PASS** iff the test detects the parent K_crit pollution + at least 2 documented downstream consumers; **FAIL** if false-positive on a clean cascade or false-negative on the S85 case.

7. **mth-ii→mth-i promotion via registry triage** — which audits beyond {vocabulary-contamination, length-ratio, PSD-ordering} should carry `scan_mandatory: true`? This is a project-level triage question, not a substitution-chain question. Pre-registered gate: **PASS** if S86 produces a mandatory-scan list with explicit cost-asymmetry rationale per audit (per G2-CONV-5 chain); **INFO** if list lands without per-audit rationale.

8. **Stylistic-coherence band defaults across document classes** — the G3 clause (h) proposed bands {pass: 1.5×, info: 3.0×, fail: 5.0×} are W2-13-specific defaults. Do META-class documentation-revision gates require different bands per document class (synthesis vs registry vs framework-mechanism vs working-paper)? Pre-registered gate: **PASS** if S86 produces per-document-class band defaults; **INFO** if the W2-13 defaults are provisionally adopted with deferred per-class differentiation; **FAIL** if the bands are over-specified to the point of suppressing legitimate revisions.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **Plan-discipline gains a five-mode taxonomy + nine-sub-mode decomposition for plan-layer information-scrambling.** The 11 S85 plan-layer defects partition exactly into {sym, ref, top.regulator, top.AMRI, mth-i, mth-ii, mth-iii, aut.external-source, aut.band-change}, with a sixth orthogonal axis (resolution-time ∈ {plan-freeze, latent, runtime}). Before this workshop, plan-layer defects were treated as ad-hoc; now they have a mechanical taxonomy with one-to-one mapping to PRDR+ pre-flight passes.
- **PRDR+ replaces the prior plan-freeze hygiene gap.** The existing PRU/PRDR clause in `epistemic-discipline.md` covers Class-8 intra-script machinery underspecification; PRDR+ covers the orthogonal plan-layer scrambling modes. After rule-file v2 lands, the union of PRDR + PRDR+ closes every known plan-freeze defect class, with a 13-test regression suite making the closure durable.
- **Strict / advisory governance is mechanically enumerable.** The 8-strict / 2-advisory bin discipline (G2-CONV-5) replaces the prior implicit "plan-freeze blocks on judgment" with a structured per-mode rule. STRICT bin = {sym, ref, top.regulator, top.AMRI, mth-i, mth-iii, mth.matrix-arithmetic, aut.band-change}; ADVISORY bin = {mth-ii, aut.external-source}. Each bin assignment is grounded in a cost-asymmetry substitution chain (irreversible-downstream-contamination vs one-plan-edit-at-freeze).

### What Holds

- **Substrate-first framing survives the methodology workshop intact.** PRDR+ is the documentation-layer engineered analog of the substrate's [iK_7, D_K] = 0 algebraic constraint. The substrate's information-conservation is logically prior; the plan-layer constraint is engineered to mirror it. Both kitaev's R2-K-EMER-1 audit-paragraph and gen-physicist's Re:K7 EMERGES paragraph affirm this is structural similarity, NOT physics derivation. The container-thinking inversion (substrate justified by PRDR+) is explicitly disclaimed.
- **The five-file rule structure is structurally necessary, not organizational convenience.** The dual application/authority ordering (G2-EMER-1) requires that plan-authors fill bottom-up (template → script → discipline) while reviewers adjudicate top-down (discipline → operational → script → template → glue). Single-file collapse breaks one of the two orderings; the five-file diff is the minimal structure that preserves both.
- **The Lyapunov-style framing for plan-layer scrambling holds, with corrected vocabulary.** Plan-layer growth is diffusive (linear in N_consumers via DAG bounded out-degree), NOT OTOC-style (exponential in operator-evolution time). The χ-matrix monotonicity-in-remediation property is load-bearing — it is what justifies bounded termination of PRDR+ — and survives the scalar-Δ retraction. Rule-text language: "PRDR+ defect-matrix χ(g, α) is monotone-non-increasing along plan-edit transitions; non-monotonic transitions (χ = 1 → 0 without plan-edit) are forbidden by the discipline."

### What Breaks or Strains

- **PRDR+ retroactive coverage on S78-S84 plans is unverified.** PRDR+ catches 11/11 S85 defects by construction (the taxonomy was built from those defects), but its empirical content beyond S85 is untested. If retroactive coverage falls below 50%, the taxonomy is structurally incomplete and needs extension before S86 plan-write — this is the leading carry-forward.
- **AMRI placement disagreement (G2-DISS-1) is unresolved.** kitaev (R2-K-DISS-2) wants the cross-reference paragraph under `## Source Authority Hierarchy`; gen-physicist (G2-DISS-1) wants it under `## Pre-Registration Completeness`. The disagreement is narrow (which subsection of one rule-file the cross-reference lands in) but structurally meaningful: it determines whether AMRI is presented as an authority-ranking question or a pre-registration-completeness question. Rule-file v2 PR adjudicates.
- **Phase 3.5 partial-execution dry-run is specified but not implemented.** Latent-mode defects (W1b-1 class) are NOT eliminated by PRDR+; they require partial execution at multiple regulator-layer values with a propagation-radius pin (default 1 wave forward). Until Phase 3.5 lands as a designed protocol with reference implementation, latent-mode defects remain a runtime-discovery class.

### Carry-Forward Computations

Numbered list. Each item formatted per `.claude/rules/feedback_fix-in-session-never-defer.md`: What / Inputs / Gate / Effort. Concrete rule-file v2 diffs are listed with target file + section + diff text reference.

1. **S86-W0-CC-PROVENANCE-BACKFILL** — Walk every canonical_constants.py top-level binding; attach `(session, source_gate, comment)` provenance via `update_constant(...)`; commit. **What**: full retroactive provenance pinning. **Inputs**: computations/canonical_constants.py (180+ bindings); git blame; session-search via knowledge MCP. **Gate**: PASS iff 100% bindings have non-null provenance; INFO 90-100% with exception list; FAIL < 90%. **Effort**: HIGH (15-20 hours, parallelizable across waves). **EVOI**: HIGH (eliminates K_crit-class collisions permanently).

2. **S86-W0-PRDR-EXTENDED-IMPLEMENTATION** — Build `computations/_prdr_extended_planfreeze.py` orchestrator + 5 internal pass modules (PASS-A through PASS-E, with sub-passes for C-i/C-ii/D-i/D-ii/D-iii). **What**: reference implementation of PRDR+. **Inputs**: rule-file v2 diff (5 files); existing tools (`_pru_cardinality_audit.py`, `_yaml_gate_validator.py`, `_agent_memory_inversion_audit.py`, `_plan_upstream_pin_validator.py`); the 11 S85 mock-plan-files for the regression suite. **Gate**: PASS iff orchestrator runs in O(plan_size) + emits structured-JSON defect report keyed on (gate_id, mode, severity); FAIL if any pass leaks into runtime cost. **Effort**: HIGH (1-2 waves). **EVOI**: HIGH (the discipline is unenforceable without the tool).

3. **S86-W0-PRDR-EXTENDED-SELFTEST** — Build `_prdr_extended_selftest.py` with 13 mock-plan-files (11 per-defect catches + 1 clean-plan negative control + 2 structural-property tests for χ-monotonicity and κ_inter cascade), per G2-EMER-2 specification. **What**: regression-test harness. **Inputs**: PRDR+ orchestrator (carry-forward #2); 11 S85 defect topics. **Gate**: PASS iff 13/13 tests pass when invoked as `_prdr_extended_selftest.py --self-test`; FAIL if any test produces wrong-direction defect classification. **Effort**: MEDIUM (1 wave). **EVOI**: HIGH (durability across future code changes).

4. **S86-W0-PRDR-RETROACTIVE-COVERAGE** — Run PRDR+ orchestrator against every plan file in sessions S78-S84; report coverage as (caught at hypothetical plan-freeze) / (subsequently discovered at execution). **What**: empirical validation of PRDR+ taxonomy beyond S85 by-construction completeness. **Inputs**: PRDR+ orchestrator (carry-forward #2); S78-S84 plan files (~7 sessions × ~80 plans); subsequently-discovered defect logs from those sessions. **Gate**: PASS iff coverage > 50%; INFO 25-50% with missing mode-class identification; FAIL < 25%. **Effort**: MEDIUM (1 wave, mostly mechanical). **EVOI**: HIGH (validates spec, unlocks rule-file v2 enforcement).

5. **S86-PHASE-3.5-PROTOCOL-SPEC** — Design + reference implementation for Phase 3.5 partial-execution dry-run protocol for top.regulator latent-mode gates. **What**: protocol document + reference implementation. **Inputs**: list of high-stakes regulator-axis gates from S85 + S86 plans; pinned propagation-radius (default 1 wave forward); dry-run trigger condition (regulator_layers field non-empty AND PRDR+ PASS-C-regulator clean). **Gate**: PASS iff Phase 3.5 catches the W1b-1-class cell-flip on a mock regulator-axis gate at propagation-radius=1; FAIL if it misses the flip OR balloons to full re-run. **Effort**: MEDIUM (1 wave). **EVOI**: MEDIUM (closes latent-mode gap; relevant only for high-stakes regulator gates).

6. **RULE-FILE-V2-DIFF — math-scripts.md** — Apply G1 clauses (a) + (c). **What**: insert "Plan-inline pin discipline (MANDATORY)" sub-section between current line 21 and line 23 (start of Local Variable Tagging); extend "GPU available" bullet at line 8 with workload-class table per G1 clause (c) verbatim text. **Inputs**: G1 verbatim diff text (lines 575-635 of this workshop). **Gate**: PASS iff diff lands cleanly + `_prdr_extended_planfreeze.py --pass-A --pass-D-iii` finds these clauses. **Effort**: LOW (1-2 hours). **EVOI**: HIGH (sym + mth-iii closures).

7. **RULE-FILE-V2-DIFF — agent-standards.md** — Apply G2 clauses (e) + (g). **What**: insert "AMRI plan-freeze pre-flight (MANDATORY for plan files)" between current line 31 and line 33; insert "Audit-Method Pre-Flight Framework" at end of file. **Inputs**: G2 verbatim diff text (lines 656-748). **Gate**: PASS iff diff lands + AMRI plan-freeze walker invocation point exists in `_prdr_extended_planfreeze.py --pass-C-amri`. **Effort**: LOW (1-2 hours). **EVOI**: HIGH (top.AMRI + mth-i/mth-ii closures).

8. **RULE-FILE-V2-DIFF — epistemic-discipline.md** — Apply G3 clauses (j) + (h) AND insert AMRI cross-reference paragraph under `## Pre-Registration Completeness` per G2-DISS-1 placement decision. **What**: insert "Band-change authority pre-flight" between current line 34 and line 36; insert "Stylistic-coherence preflight" within `## Pre-Registration Completeness` after PRDR clause (line 88-94); insert AMRI cross-reference paragraph under same Pre-Registration Completeness section noting plan-freeze enforcement at `_prdr_extended_planfreeze.py --pass-C-amri`. **Inputs**: G3 verbatim diff text (lines 770-871). **Gate**: PASS iff diff lands + band-registry sits above per-session pre-registration in authority hierarchy + AMRI cross-reference cites agent-standards.md §AMRI. **Effort**: LOW (2 hours). **EVOI**: HIGH (aut + stylistic-mth + AMRI-governance closures).

9. **RULE-FILE-V2-DIFF — pru-pre-registration-template.md** — Apply G4 clauses (b) + (d) + (f) + (i) + Class-8-extension. **What**: extend Gate Block scaffold with Referenced helpers / Referenced registries blocks (clause b); insert regulator_layers + join_rule_for_regulator_layers fields in PRDR machinery block (clause d); insert External-source binding block (clause f); insert matrix_arithmetic_convention sub-block under PRDR machinery (clause i); extend Class 8 Failure Mode table with rows 8a-8e for PRDR+ sub-classes. **Inputs**: G4 verbatim diff text (lines 890-1026). **Gate**: PASS iff template scaffold has all five new field blocks + Class 8 table has 5 sub-rows. **Effort**: LOW (2 hours). **EVOI**: HIGH (ref + top.regulator + aut.external + mth.matrix-arithmetic closures + meta-self-documentation).

10. **RULE-FILE-V2-DIFF — /rclab-plan skill** — Apply G5 composite clause (Phase 3f insertion + Phase 4 user-checkpoint extension + Safety Rules extension items 12-14). **What**: insert Phase 3f orchestration block between current Phase 3e and Phase 4; extend Phase 4 user-checkpoint reporting to include PRDR+ summary; append Safety Rules 12-14 (plan-layer-discipline, five-mode taxonomy, strict-vs-advisory governance). **Inputs**: G5 verbatim diff text (lines 1046-1175). **Gate**: PASS iff /rclab-plan invokes `_prdr_extended_planfreeze.py` per wave + Phase 4 surfaces non-zero exit codes verbatim + Safety Rules count = 14. **Effort**: LOW (2 hours). **EVOI**: HIGH (orchestration glue closure).

11. **S86-AUDIT-KNOB-REGISTRY-INSTANTIATION** — Create `sessions/framework/audit-knob-registry.md` with one-level structure per G2-DISS-2 (flat lookup; fields {pinned_value, recommended_scan_range, scan_mandatory: bool}). Seed with vocabulary-contamination, length-ratio, PSD-ordering audits set to `scan_mandatory: true`. **What**: registry file instantiation. **Inputs**: G2 clause (g) point 5 specification; the three S85 mth audits; project-level triage of mth-ii→mth-i promotion candidates per Open Question #7. **Gate**: PASS iff registry has the three mandatory entries + at least 5 recommended entries + lookup format consistent with PRDR+ PASS-D parsing. **Effort**: LOW (1 hour). **EVOI**: MEDIUM (closes mth-ii loophole at registry level).

12. **S86-BAND-REGISTRY-INSTANTIATION** — Create `sessions/framework/band-registry.md` indexed by physics-class identifier (e.g., "A_s vs Planck central", "n_s vs Planck", "DR3 cell flip"). Seed with the S80 PASS-F2 band for A_s and any other prior-session bands recoverable from the verdict log. **What**: band registry file. **Inputs**: G3 clause (j) point 3 specification; S80 + earlier session pre-registrations. **Gate**: PASS iff registry covers every band that any S85 gate referenced + lookup format consistent with PRDR+ PASS-E parsing. **Effort**: LOW (2 hours). **EVOI**: MEDIUM (closes aut.band-change ambiguity).

13. **S86-PERMANENT-RESULTS-REGISTRY-SKELETON** — Create `summary/permanent-results-registry.md` with §VII.N anchor + skeleton sections for all framework structural results that subsequent gates will land into. **What**: registry skeleton file. **Inputs**: S85 W3-WP §W3-8 / §W3-10 deferred entries; S58 LEGGETT-PARTITION; the 16 PROVEN results from agent memory framework-status.md. **Gate**: PASS iff file exists with at least the §VII.N anchor + a skeleton heading for each closed mechanism. **Effort**: LOW (2 hours). **EVOI**: HIGH (unblocks W3-8 / W3-10 landings + closes case (a) ENOENT registry-absent class permanently).

14. **S86-EXTERNAL-SOURCE-EVIDENCE-DIRECTORY** — Create `sessions/external-source-evidence/` directory pattern + per-gate sub-directories with literal grep snippet files for every cited external paper. **What**: evidence-directory structure + initial population. **Inputs**: G3 clause (j) point 5 specification; G4 clause (f) external_source_evidence field; list of cited external papers from S85 + S86 plans. **Gate**: PASS iff every external-source citation in any S86 plan has a non-empty grep-evidence file with PDF page number. **Effort**: MEDIUM (per-paper PDF grep work; depends on number of citations). **EVOI**: MEDIUM (closes aut.external-source ambiguity).

### Closing Line

Plan-layer information-scrambling has a complete five-mode taxonomy with 8-strict / 2-advisory governance, a five-file rule-file v2 diff that respects both application and authority orderings, and a 13-test regression harness that makes the discipline durable — closing the plan-freeze hole that the substrate's [iK_7, D_K] = 0 algebraic constraint cannot reach.
