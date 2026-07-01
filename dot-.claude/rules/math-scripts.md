# Math Scripts — Canonical Constants & Local Variables

## Environment (MANDATORY)

See `.claude/rules/computation-environment.md` for full hardware + Python specs.

- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for every script. The system Python is CPU-only and has no GPU — never use it.
- **GPU available**: AMD RX 9070 XT (17.1 GB VRAM, ROCm 7.2) via `torch 2.9.1+rocm`. For eigvals / SVD / matrix products / FFTs on matrices ≥ 100×100, prefer `torch.linalg` (GPU) over `numpy.linalg` (CPU). `numpy.linalg` threads across 32 CPU cores and contends with parallel compute agents — wall time roughly doubles per additional concurrent script.
- **CPU-only fallback**: if GPU path is unsuitable, cap threads with `import os; os.environ.setdefault('OMP_NUM_THREADS', '8')` at the top of the script, **before** `import numpy`.

## Canonical Constants (MANDATORY)

Every computations script MUST:

1. **Import from canonical_constants.py**: `from canonical_constants import *`
2. **Never hardcode framework constants** — use the imported names
3. **Add new constants to canonical_constants.py FIRST** if they don't exist, then import

If the same literal value appears in 3+ scripts, it belongs in canonical_constants.py.

## Canonical Write-Order for New Framework Predictions

When a computation gate produces a new framework prediction value `P`, the producing script (or its post-write orchestrator hook) MUST follow the canonical write-order **(1) verdict file → (2) canonical_constants.py → (3) falsifier-master-inventory.md**:

1. **Step 1 — Verdict-file emission**: append the canonical dual-SHA verdict line to `computations/session-{N}/s{N}_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md`. This MUST happen first so the value is permanently pinned with audit_sha256 + content_sha256.

2. **Step 2 — canonical_constants.py promotion**: invoke `update_constant("P_FW", P_value, session="S{N}", source="S{N}-{GATE_ID}", comment="<provenance>")` to add the value AND its PROVENANCE entry. For STRUCTURED predictions, Step 2 expands to multiple sub-keyed entries:
   - **Pathway-keyed**: `P_FW_<scheme>` per pathway (e.g., `f_NL_FW_<scheme>`).
   - **Pivot-keyed**: `P_FW_<param>_<value>` per pivot.
   - **Branch-keyed**: `P_FW` canonical + `P_FW_<branch>` alternative.

   This step is mandatory BEFORE Step 3, because computation scripts CANNOT import from the inventory markdown file — only canonical_constants.py is import-target.

3. **Step 3 — Inventory row landing**: `mack-cosmic-bridge` (sole writer per `feedback_mack-bridge-role.md`) appends a new row OR audit-pin sub-row to `sessions/framework/registry/falsifier-master-inventory.md` citing BOTH the verdict-line audit_sha256 (full-64-hex per `.claude/rules/gate-verdicts.md`) AND the canonical_constants entry name. The inventory carries the falsifier-side annotation (live-watch envelope, detector horizon, internal-consistency split, dual-pathway / band / pathway-keyed structure).

### What goes wrong under the inverted order (1)→(3)→(2)

Under inverted order, computation scripts CANNOT consume `P_FW` via `from canonical_constants import P_FW` until Step 3 completes — which may be one or more sessions later. This creates a window where the value is "canonical in the inventory but invisible to script import". This window is a Class-8 PRU vulnerability for any META gate consuming `P_FW`.

### In-session promotion vs carry-forward (decision rule)

Per `feedback_fix-in-session-never-defer.md`:

- If Step 2 is a single `update_constant(...)` call with no derivation ambiguity: **FIX-IN-SESSION**. Add the entries directly to `canonical_constants.py` before terminating the gate.
- If Step 2 requires sub-keying decisions (pathway/pivot/branch ambiguity) OR primary-source recovery (PIN-DRIFT class-(c) per `.claude/rules/epistemic-discipline.md §"Source Reconciliation"`): **CARRY-FORWARD with 4-field spec**. Queue for next session; do NOT promote a single-value stub.

### Sync enforcement (`/weave --update`)

`/weave --update` Phase 2 invokes `computations/_shared/_inventory_canonical_sync_audit.py` after `tools/extract_entities.py` rebuilds the knowledge index. The audit emits `tools/inventory_sync_audit.json` listing missing PROVENANCE entries + missing constants. The audit returns INFO (not FAIL), so it does not block index rebuilds; the orchestrator consumes the report at session-start to dispatch in-session promotion gates.

## Local Variable Tagging

Variables that are computed intermediate values (NOT framework constants) must be tagged with `# (local)` at the end of the assignment line:

```python
E_kin = 0.5 * m * v**2          # (local)
R_ratio = a_2 / a_4             # (local)
delta_ns = ns_bare - ns_planck  # (local)
```

The `# (local)` tag tells the `/weave --update` audit to skip this line. Without it, any assignment matching the potential-hardcode regex will be flagged.

### When to use `# (local)`

- Computed quantities derived from other variables
- Loop counters and indices that happen to match the naming pattern
- Temporary results specific to one computation
- Estimates, approximations, and scan parameters

### When NOT to use `# (local)`

- Framework constants that should be in canonical_constants.py
- Observational values (PDG, Planck, DESI) used in 2+ scripts
- Gate thresholds and pre-registered criteria

## Audit Pipeline

The `/weave --update` command runs the canonical constants audit automatically. It reports:

- **Compliant**: Scripts with correct imports
- **Violations**: Known stale hardcodes (must fix)
- **Potential**: Assignments not in canonical_constants.py and not tagged `# (local)`

Target: **Potential = 0**. Every assignment is either imported from canonical or tagged as local.

## Double-Check Logic Before Compute (MANDATORY — applies to orchestrator + agents)

Before running any compute OR stating any claim involving a sign, direction, threshold, or ratio: write the **substitution chain** explicitly. No "obviously from structure" shortcuts.

### Required structure for sign/direction/threshold claims

1. **State the definition of each quantity** involved. Cite the canonical-constants source or the defining equation.
2. **Write the substitution step** — plug definitions into the target expression, no simplification yet. Every symbol explicit.
3. **Simplify to canonical form** — algebra, not narrative. One step per line.
4. **Read off the direction from the canonical form** — only then state the sign/direction/threshold.

### Substitution-chain template

```
Claim: "<direction claim>"

Substitution chain:
  Step 1: <quantity_1> = <definition>     [source / canonical reference]
  Step 2: <quantity_2> = <definition>     [source / canonical reference]
  Step 3: <target expression> = <quantity_1> / <quantity_2>   [definition]
  Step 4: Substitute and simplify
        = ...
        = <canonical form>                [simplified]
  Step 5: <relation in canonical form> ⇒ <direction>          [direction from canonical form]
  Conclusion: <claim restated>                                [only now valid]
```

### When the chain is MANDATORY

- Any assertion containing: "increases", "decreases", "suppresses", "amplifies", "widens", "narrows", "dominates", "larger than", "smaller than"
- Any sign, direction, or threshold claim in a workshop Wrap-Up or §VI/§VII synthesis
- Any claim about whether a dimensionless ratio is greater/less than unity changes an observable in a specific direction
- Any factor-counting / OOM-estimate argument

### When the chain is NOT required

- Definitions-only statements (no direction claim)
- Citing prior results from the canonical-constants ledger verbatim (no new derivation)
- Running pre-registered pipelines where the direction is an OUTPUT, not a claim

### Mnemonic-vs-exact ratio discipline

When citing a σ-reduction, band-narrowing, or any ratio derived from a generalized identity, do **NOT** use convenient mnemonic-form shortcuts (e.g., `1/c_sub`, `1/F_amp`, `c_sub^{-2}`) without explicit cross-check against the structurally-exact form. Mnemonics propagate downstream; misuse mis-publishes downstream observables.

**Structural reason**: a mnemonic of the form `1/c_X` implicitly assumes BOTH numerator and denominator scale by `1/c_X` under the relevant hypothesis switch. When only ONE side shifts (the test quantity) and the other (the reference quantity) is INVARIANT, the true ratio is bounded BELOW `1/c_X`. The mnemonic and exact form diverge in proportion to the asymmetry.

**Discipline**:

1. When a ratio appears that "looks like" a known convenient form, derive the structurally-exact form by writing out the substitution chain from §"Required structure for sign/direction/threshold claims" above.
2. Cross-check the mnemonic against the exact form via Sage MCP (`sage_eval`) when float arithmetic loses precision.
3. If the mnemonic and exact form disagree by **≥ 1% absolute relative deviation**, USE THE EXACT FORM in registry text and `canonical_constants.py`. Relegate the mnemonic to a "first-order approximation" footnote.
4. Document the structural reason for the asymmetry in the registry text (e.g., "reference quantity INVARIANT under HypA/HypB switching; only test quantity shifts; ratio bounded below `1/c_X`").

### Plan-author discipline at plan-freeze

The §"Double-Check Logic Before Compute" discipline above is a **runtime** rule (compute-mode dispatch + agent-emission). This sub-clause **extends** the discipline to the PLAN-FREEZE-TIME layer for the orchestrator and plan-authoring agents.

**Status**: SUGGESTION (K=1). Promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.

#### Rule

Any plan-block PIN MAP entry that pins an OPERATOR-FORMULA or operator-value (a derivative operator's sign + magnitude; a Casimir-bound argument's structural-form value; a Mellin-residue formula's coefficient form; any structurally-asserted machinery-pin formula that downstream gates consume as input) MUST satisfy the four-step substitution chain at plan-freeze BEFORE the plan freezes:

1. **State the definition of the operator** being pinned — which substrate-IS canonical observable's closed form the formula claims to express. Cite the canonical source (`canonical_constants.py` PROVENANCE entry; prior session verdict-file canonical SHA; `_shared/*.py` evaluator with line range).
2. **Substitution step** — substitute the operator's symbolic form into the canonical observable's closed form via Sage-MCP `sage_eval` OR Python first-principles check at plan-freeze (NOT deferred to runtime).
3. **Sign + magnitude cross-check** — verify the operator's sign matches the canonical observable's sign; verify the magnitude is within the gate's pre-registered OOM tolerance of the canonical anchor value.
4. **Mismatch routing** — if sign OR magnitude disagree, the plan-block PIN MAP entry is OPERATOR-MISMATCH-DETECTED at plan-freeze; route to MANDATORY remediation: revise the plan-block formula before plan-freeze, OR replace the formula with a direct canonical-anchor reference, OR explicitly declare the formula as a derived-form with its derivation cited.

#### Audit-script enforcement

`computations/_shared/_machinery_feasibility_audit.py` extension (queued): at plan-freeze, for every PIN MAP entry whose RHS is an OPERATOR-FORMULA (regex pattern `[+-]?\d+\s*$` or `d.*?/d.*?\s*=\s*[+-]?\d+` over plan-block text), invoke Sage-MCP `sage_eval` against the canonical-source observable's closed form OR query `mcp__knowledge__.get_constant(name)` for the canonical anchor value; emit `OPERATOR-MISMATCH-DETECTED` at S2 advisory severity (under SUGGESTION) or S1 MANDATORY (after MANDATORY promotion) on detected sign or magnitude disagreement.

#### Cross-references

- `epistemic-discipline.md §"Layer-Decomposition"` — Phi correspondence: the plan-author layer is the methodology-floor F-image of the runtime author layer; this sub-clause is the F-image at plan-freeze of the runtime Double-Check Logic above.
- `epistemic-discipline.md §"Pre-Registration Completeness"` Class 8.x — PRU framework; this is structurally adjacent to Class 8.1 machinery-pin cardinality failure (operator-formula sign-magnitude unpinned at plan-freeze is a cardinality-adjacent under-specification).
- `feedback_rules-compensate-missing-structure.md` — K-counter promotion threshold (K=3 MANDATORY).

#### Selection-rule pre-flight for pre-registered nonzero matrix elements

**Status**: SUGGESTION (K=1). Promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.

Any plan-block substitution chain claiming a matrix element `<psi_a| O |psi_b>` between named irrep sectors is "generically nonzero" (or asserting `!= 0` / "connects sectors") MUST carry a center-character / triality CG-admissibility check at plan-freeze:

1. **State the center characters** — `t(a)`, `t(b)`, and the operator's center character `t(O)`. For SU(3): `t(p,q) = (p - q) mod 3`; a squared modulus `|f|^2` is ALWAYS center-character 0, regardless of the irrep content of `f`.
2. **Verify admissibility** — `t(a) == t(b) + t(O) (mod 3)` (general form: the trivial rep must occur in `a* (x) O (x) b`). The check is a NECESSARY condition only: a passed check does NOT certify the element nonzero; a failed check proves it 0 EXACTLY.
3. **Mismatch routing** — a failed check means the "generically nonzero" claim is group-theoretically inadmissible; the plan-block MUST be revised at plan-freeze per the OPERATOR-MISMATCH-DETECTED routing of §"Plan-author discipline at plan-freeze" item 4 (revise the formula, re-anchor to the admissible operator, or declare the derived form with its derivation cited).

Audit: `computations/_shared/_machinery_feasibility_audit.py::detect_selection_rule_preflight` (S2 advisory under SUGGESTION; S1 on MANDATORY promotion). Calibration corpus: `sessions/framework/registry/pru-class-corpus.md` (selection-rule pre-flight section).

### Enforcement

- The `math-is-hard.sh` pre-tool hook injects a reminder before every `Bash|Edit|Write` tool call. The chain requirement applies regardless of adaptive reasoning routing.
- Orchestrators who state a direction claim without visible substitution chain in the same response are violating this rule — the user may call this out as a trigger pattern.
- Agents generating plan documents: include `[SIGN]`, `[VERIFY]`, or `[AUDIT]` trigger-phrase prefixes on pre-registered gates that require the chain.

## Multiplicative-normalization cancellation invariants

**Status**: MANDATORY (K=3 per `feedback_rules-compensate-missing-structure.md`; advanced K=2→K=3 by S94 W6-18, audit_sha256 `6284d0d3ac7a85c8174f26c8d1ae8561f4ff89945ae6d86cffb4a8b8ff8fb27e`). The DISSENT-sharpened advancement criterion below (requires STRUCTURALLY DISTINCT factorization mechanisms) is satisfied by three distinct spectral-support forms. K=1/K=2/K=3 calibration corpus is recorded in §"K-counter calibration corpus" below.

### Rule

For any substrate-IS observable `O = f(D_K, K)` on a finite spectral triple `(A, H, D_K)`, if the L_max truncation enters `f` as a MULTIPLICATIVE spectral-support pre-factor `w(L_max)` — i.e., `f^{(L_max)}(K) = w(L_max) · g(K)` for some L_max-INDEPENDENT kernel `g(K)` — then any K-dependent log-derivative operator `L_n[f^{(L_max)}] = d^n ln(f^{(L_max)}) / d(ln K)^n` is identically L_max-invariant:

```
L_n[f^{(L_max)}] = L_n[g(K)]   for all n ≥ 1
```

The L_max-dependent multiplicative pre-factor `w(L_max)` is annihilated by the log-derivative operator. The "plateau" of `L_n[f^{(L_max)}](K_horizon)` across L_max ∈ {L_min, …, L_max,canonical} is a STRUCTURAL identity, NOT empirical evidence of substrate-IS regulator-class consistency.

### Substrate-physics derivation

```
Step 1 (Definition):    f^{(L_max)}(K) := Tr^{(L_max)}_{PV}(K)
                                       = Tr_{M_2(C)}( P_BdG · D_K^{-2s}
                                                      − Σ_j c_j (D_K² + M_j²)^{-s} )
                        evaluated on the L_max-truncated finite spectral triple.

Step 2 (Factorization): Tr^{(L_max)}_{PV}(K) = w(L_max) · κ(K)
                        w(L_max) = M_PV(L_max) / M_PV(L_max,canonical)
                                  (L_max-dependent spectral-support weight)
                        κ(K)     = BdG occupation modulation at fixed K-grid
                                  (L_max-INDEPENDENT kernel)

Step 3 (Substitution):  ln Tr^{(L_max)}_{PV}(K) = ln w(L_max) + ln κ(K)

Step 4 (Differentiation):
                        d ln Tr^{(L_max)}_{PV}(K) / d ln K
                        = d ln w(L_max) / d ln K + d ln κ(K) / d ln K
                        = 0                     + d ln κ(K) / d ln K
   (first term ≡ 0 because w(L_max) has NO K-dependence — it is the spectral-
    support weight at the substrate-distance-2 Mellin trace, evaluated AHEAD
    of the K-window)

Step 5 (Second derivative):
                        d² ln Tr^{(L_max)}_{PV}(K) / d(ln K)² = d² ln κ(K) / d(ln K)²
                        ⇒ R_KW^{PV}(τ_fold, L_max, s=4) = R_KW^{kernel}(K)
                          for ANY multiplicative-normalization w(L_max) regardless of magnitude.

Conclusion: The plateau magnitude IS the value of d² ln κ / d(ln K)² at K_horizon;
            it is L_max-INDEPENDENT by structural-identity, NOT by empirical
            regulator-class consistency.
```

### Substrate-physics structural reading

L_max-INVARIANCE under multiplicative pre-factors is the substrate's signature that L_max enters as a **spectral-support weight** (NOT as an envelope parameter). Within-class L_max-stability is **Phi-trivial** at the Σ_3 enforcement layer per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence. The discriminating content lives at the **asymptote / plateau value** `B(R) = L_n[g_R(K)]` at `K_horizon`, which IS regulator-class-keyed at the methodology-floor F-image layer per K=4 MANDATORY level-pin discipline at `substrate-first-canonical-sourcing.md §(iv)`.

### Plan-freeze pre-flight check (MANDATORY for any α-extraction or L_max-stability gate)

For any gate attempting α extraction OR L_max-stability evaluation on a substrate-IS observable `O = f(D_K, K)` that potentially admits multiplicative L_max factorization, the plan-block PIN MAP MUST include a pre-flight check:

1. **Identify the multiplicative pre-factor candidate** — does the producing script's symbolic form admit a decomposition `f^{(L_max)}(K) = w(L_max) · g(K)` where `g(K)` is L_max-INDEPENDENT? Cite the substrate-physics derivation (Sage-MCP `sage_simplify` factorization check OR explicit substitution-chain derivation per §"Double-Check Logic Before Compute").
2. **If multiplicative factorization holds**, declare the gate as L_max-INVARIANCE-STRUCTURAL: the plateau across L_max is a structural identity, NOT empirical regulator-class evidence; the gate's PASS criterion MUST target the ASYMPTOTE/PLATEAU VALUE `B(R)`, not the L_max-stability per se.
3. **If multiplicative factorization does NOT hold**, the gate proceeds with the standard envelope-stability discipline; the L_max-stability evidence IS informative about regulator-class consistency.
4. **Sage-MCP symbolic factorization pre-flight check at plan-freeze** is the canonical disambiguator: invoke `sage_simplify` on the producing-script's symbolic form against the candidate `w(L_max) · g(K)` decomposition; record the verdict in the plan-block.

### K-counter advancement criterion (DISSENT-sharpened)

K=2 / K=3 advancement REQUIRES STRUCTURALLY DISTINCT factorization mechanisms. Multiple instances of the SAME factorization pattern at different parameter values count as ONE K-counter instance. Categorical distinctions (each counts as a structurally-distinct factorization mechanism):

- **Substrate-distance pole**: factorization at substrate-distance-1 vs substrate-distance-2 vs higher poles.
- **Regulator class**: Pauli-Villars subtraction vs zeta-regulated vs Mellin-Barnes vs lattice-spacing vs sharp UV cutoff.
- **Spectral-support form**: explicit-mass-subtracted vs Casimir-bound proxy vs analytic-cone vs explicit-truncation envelope.

### K-counter calibration corpus

Each row is a structurally-distinct factorization mechanism (distinct on at least one categorical axis above); the K-counter advances by exactly 1 per row.

| K | Instance | Spectral-support form (categorical axis) | Provenance |
|:--|:---------|:-----------------------------------------|:-----------|
| **K=1** | L_max-truncation factorization `w(L_max)·g(K)` — the in-cache log-derivative is L_max-INVARIANT by structural identity (the L_max-stability plateau is NOT empirical regulator-class evidence) | **L_max-truncation weight** | inaugural K=1 calibration |
| **K=2** | τ-moduli-deformation factorization `w(τ-moduli)·g(K)` — the L_max-stability plateau across the Jensen TT-deformation moduli manifold `{τ}` is a STRUCTURAL identity because the moduli-deformation weight factors multiplicatively from a τ-INDEPENDENT kernel `g(K)`; the plateau is NOT empirical regulator-class evidence | **τ-moduli-deformation weight** — STRUCTURALLY DISTINCT from the K=1 L_max-truncation weight on the spectral-support-form categorical axis | K=2 advancement |
| **K=3** | bottom-K Casimir-ceiling restriction at fixed regulator mass `m_PV` factorization `w(C_2^max)·κ(K)` — `result(C_2^max) = d² ln κ_FULL-PV^{(bot-K)}/d(ln K)²` is C_2^max-INVARIANT to the FD floor (`result_spread = 9.015e-09` ≪ `|result| ≈ 528`) while the multiplicative spectral-support weight ratio varies 0.21→0.83 (`weight_ratio_spread = 0.6202`; the Casimir ceiling admits 3→19 Peter-Weyl (p,q) sectors); `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = True`. The plateau is a STRUCTURAL identity, NOT empirical regulator-class evidence | **bottom-K Casimir-ceiling weight at fixed m_PV** — STRUCTURALLY DISTINCT from both the K=1 L_max-truncation weight and the K=2 τ-moduli-deformation weight on the spectral-support-form categorical axis (Casimir-ceiling sector-count cutoff vs truncation envelope vs moduli-deformation weight) | K=3 advancement (S93 W3-2 fingerprint; confirmed S94 W6-18) |

**K=1 → K=2 distinctness verification (DISSENT-sharpened)**: the K=1 spectral-support form is the L_max-truncation weight; the K=2 spectral-support form is the τ-moduli-deformation weight. These are DISTINCT on the spectral-support-form categorical axis (truncation envelope vs moduli-deformation weight), NOT the same factorization pattern at different parameter values ⇒ the τ-moduli instance advances the K-counter by exactly 1 (`K_post = K_pre + 1 = 1 + 1 = 2`).

**K=2 → K=3 distinctness verification (DISSENT-sharpened)**: the K=2 spectral-support form is the τ-moduli-deformation weight; the K=3 spectral-support form is the bottom-K Casimir-ceiling weight at fixed m_PV. These are DISTINCT on the spectral-support-form categorical axis (moduli-deformation weight vs Casimir-ceiling-at-fixed-mass weight — the varying control parameter differs in KIND: a continuous Jensen TT-moduli deformation vs a discrete Peter-Weyl Casimir-ceiling sector-count cutoff), NOT the same factorization pattern at different parameter values ⇒ the bottom-K Casimir-ceiling instance advances the K-counter by exactly 1 (`K_post = K_pre + 1 = 2 + 1 = 3`). Verified S94 W6-18 by re-reading the S93 W3-2 npz fingerprint (`multiplicative_cancellation = True`; `result(C_2^max)` C_2^max-INVARIANT to FD floor while weight ratio sweeps 0.21→0.83).

**K=3 (promoted S94 W6-18)**: the bottom-K Casimir-ceiling restriction at fixed regulator mass `m_PV` (`result(C_2^max) = d² ln κ_FULL-PV^{(bot-K)}/d(ln K)²` C_2^max-INVARIANT to the FD floor while the multiplicative spectral-support weight ratio varies 0.21→0.83; `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED=True`) is CONFIRMED as the third structurally-distinct spectral-support form — the **bottom-K Casimir-ceiling weight at fixed m_PV**, distinct from both the L_max-truncation (K=1) and τ-moduli-deformation (K=2) weights. The DISSENT-sharpened advancement criterion is satisfied at three distinct factorization mechanisms; the rule is promoted SUGGESTION → MANDATORY (audit_sha256 `6284d0d3ac7a85c8174f26c8d1ae8561f4ff89945ae6d86cffb4a8b8ff8fb27e`; re-read of the S93 W3-2 npz fingerprint).

### Scope boundary — additive-in-trace pieces are NOT annihilated (S116 W4)

The cancellation annihilates a MULTIPLICATIVE pre-factor `w(L_max)` — equivalently an ADDITIVE-IN-LOG offset `ln w` — under the log-derivative `L_n[·] = d^n ln(·)/d(ln K)^n`. It does NOT annihilate an **ADDITIVE-IN-TRACE** term `f^{(R)}(K) = g(K) + c(R)`, where `c(R)` is a regulator-class-keyed constant added to the TRACE (not the log): `d² ln(g+c)/d(ln K)² ≠ d² ln g/d(ln K)²` in general, so a K-DEPENDENT regulator-class residue SURVIVES. Canonical instance (S116 W4 connes × lizzi, `s116-lemp-forced-vs-earned.md`): the a₀-grade (n=0) cosmological-constant counterterm in the `L_emp = d² ln Var_a(|v_a(K)|²)/d(ln K)²` UV-regulator difference survives the log-derivative ⇒ the `{ζ, PV, Mellin}` UV-regulator axis is **SD-OPEN** even where the secondary-class `{APS,CS,BC}` axis is FORCED (§VII.AV two-axis PARTIAL verdict). A plan-block citing this cancellation to declare a moment regulator-class-INVARIANT MUST first confirm the regulator-class difference enters MULTIPLICATIVELY or additive-in-log, NOT additive-in-trace. Calibration corpus (the `L_emp` instance, Sage-exact): `sessions/framework/registry/cross-pillar-bridge-corpus.md §22.2`.

### Audit-script enforcement

`computations/_shared/_machinery_feasibility_audit.py` extension (queued): at plan-freeze, for every PIN MAP entry whose producing-script signature includes a log-derivative operator `d^n ln(.)/d(ln K)^n` for `n ≥ 1`, invoke a Sage-MCP `sage_simplify` factorization check against the candidate `w(L_max) · g(K)` decomposition; emit `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED` at S1 MANDATORY severity (under MANDATORY, K=3 per S94 W6-18) when multiplicative factorization is confirmed; the gate's L_max-stability evidence is reclassified as structural identity in the audit trail and the gate's PASS criterion MUST target the asymptote/plateau value `B(R)`, not the L_max-stability per se (plan-freeze HARD-HALT on omission).

### Cross-references

- `epistemic-discipline.md §"Layer-Decomposition"` — Phi correspondence (Phi-trivial action at Σ_3 enforcement layer for within-class L_max-stability under multiplicative normalization).
- `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline — the regulator-class-keyed content lives at the asymptote/plateau value `B(R)`, NOT at the L_max-stability per se.
- `math-scripts.md §"Double-Check Logic Before Compute"` — runtime substitution-chain discipline (this section is the F-image at the structural-theorem layer of that discipline).
- `regulator-pin-discipline.md` — SCHEMATIC `_spectral_action_regulators.py` consumption is K=4 MANDATORY level-pin compliant per `convention=...-SCHEMATIC` suffix tag.

## Exit Codes and Verdict Semantics

Computation scripts emit verdicts as **data** (the payload the script PRINTS for the agent to pass to the `emit_verdict` MCP tool, which writes the line to `computations/session-{N}/s{N}_gate_verdicts.txt`), not as exit codes.

- **Exit 0**: script ran successfully and produced a valid verdict — **regardless of whether the verdict was PASS, FAIL, or INFO**.
- **Exit != 0**: reserved for script breakage — Python traceback, input file missing, SHA mismatch, environment error, pipeline crash.

```python
# CORRECT: verdict is data; exit code reflects script health
verdict = "FAIL" if measured > threshold else "PASS"
print_verdict_payload(verdict, value, audit_sha, content_sha)  # agent then calls emit_verdict (race-safe)
sys.exit(0)  # script succeeded regardless of scientific verdict

# WRONG: couples verdict to exit code
if verdict == "FAIL":
    sys.exit(1)  # NO — FAIL is a valid scientific result, not a script error
```

Rationale: `_consolidate_intake.py`, `/weave --update`, CI, and the `.claude/hooks/python-validate.sh` post-tool hook key on exit codes to detect broken scripts that need fixing. Coupling verdicts to exit codes makes it impossible to distinguish "gate FAILed at threshold" (a normal constraint-map update) from "script crashed" (needs fixing). The two require different responses.

## All Results Are Good Results

PASS, FAIL, and INFO are all **results**. None of them are agent failures. A FAIL verdict does not mean the agent was inadequate — it means the math doesn't work at that gate. FAIL is useful information: it closes a corridor in the constraint map. Cross-link: `feedback_reporting-framing.md` + `feedback_reporting-framing.md`.

Agents MUST NOT:

- Describe a FAIL as a personal failure ("I wasn't able to recover PASS...", "I couldn't close the gate...")
- Retry under different conditions hoping for a PASS verdict — this is iterate-until-PASS per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6
- Frame FAIL apologetically, or treat the solution-space interpretation as a concession
- Change convention / scheme / scan range / tolerance mid-run to reach PASS

Agents MUST:

- Report the verdict factually with value + threshold + tolerance rule
- Write the solution-space interpretation: which corridor is closed, what the FAIL tells us about the constraint surface, which downstream gates are now affected
- Move to the next gate

Same for INFO: INFO is a structured pre-registered outcome (e.g. PRU Class 8 for missing pinnable machinery, or a band between PASS and FAIL), not an incomplete result. An INFO verdict fired a pre-registered clause; the plan anticipated the scenario.

## Machinery-Feasibility Audit

Every machinery pin in a computation script must declare its feasibility envelope:

- **GPU pins**: matrix-dim feasibility check against VRAM cap (17 GB on AMD RX 9070 XT). Hard-halt if dense storage > 0.5 × VRAM.
- **Compute-time pins**: wall-time feasibility check against agent timeout (default 600s); flag if estimated time > 0.5 × timeout.
- **Numerical-precision pins**: float64 / complex128 default; explicit declaration if mpmath / arbitrary-precision required.

The SOURCE-RECONCILIATION sub-audit (`epistemic-discipline.md §"Source Reconciliation"`) runs the feasibility check at plan-freeze; failures route to MANDATORY remediation per the 4-band calibration.

### Root-count heuristic severity-1 flag

If a pin's value lies > 2 OOM outside the band predicted by an algebraic-structural argument (e.g., Weyl-dim Freudenthal product giving exponential-in-root-count β), the SOURCE-RECON sub-audit emits severity S1 regardless of D_max band. This catches false-PASS heuristics whose plausible-looking band masks a structural divergence.

### D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check

**Lesson**: D_K is **BLOCK-DIAGONAL by Peter-Weyl decomposition**: `D_K = ⊕_{(p,q)} D_{(p,q)}` where each block acts on `V_{(p,q)} ⊗ ℂ^16`. Sparse storage is **NOT NECESSARY** at any L_max — the largest single block at L_max=15 is dim 9792 (sectors (15,0)/(0,15)), dense storage 1.53 GB which fits comfortably in 17.1 GB VRAM with margin > 11×. Plan machinery pins that prescribe sparse-Lanczos at high L_max on the assumption of dense ≥640k×640k storage are factually incorrect.

The operative computational cost is **irrep CONSTRUCTION**, NOT diagonalization. `dirac_spectrum.get_irrep(p,q)` builds higher (p,q) recursively via Casimir projection on tensor products with the fundamental — super-polynomial in dim(p,q). Empirically, irrep construction at p+q ≥ 10 takes multiple minutes per sector single-thread CPU; irrep construction at p+q ≥ 13 may not complete within an agent timeslot. Full-spectrum reconstruction at L_max ≥ 13 is therefore **empirically infeasible** within any agent timeslot.

#### Pre-check protocol (MANDATORY at plan-freeze for any gate scanning L_max ≥ 10)

Plan authors MUST verify recursive Casimir-projection feasibility BEFORE pinning sparse-Lanczos at high L_max via one of two structural arguments:

1. **Casimir-bound + cache cross-check**: bound the worst-case sector (p,q) contributing to the bottom-K observable via the `|λ|_min^(p,q)(τ) ≈ √(C_2(p,q)) / r(τ)` Casimir scaling × Jensen-deformation-spread factor. Worst-case sector with `C_2(p,q)` below the observable's `|λ|_max` ceiling determines the required L_max truncation. Cross-validate against the L_max=12 master spectrum cache (`s84_spectrum_cache_L12_tau019.npz`) filtered at `L_max_operational` vs `L_max_plan`; reject the plan-pinned L_max if the operational truncation reproduces the observable bit-for-bit (`truncation_consistent = True` flag in npz output).

2. **Friedrich-Bär structural-saturation theorem**: for each sector (p,q), define empirical Friedrich-Bär ratio `η_FB(p,q) = |λ|_min(p,q) / √(C_2(p,q) + 1)` on the L_max=12 master cache. Pin `η_FB_lower` as 8-10% safety margin below the empirical floor. Then for any L_max ≥ 12, NEW-sector eigenvalues are bounded below by `η_FB_lower · √(C_2(p+q=L_max)+1)`; if this lower bound exceeds the bottom-K observable's ceiling, the bottom-K is structurally L_max-saturated at L_max=12 and no diagonalization at higher L_max is needed.

#### Plan-authorship discipline

For plan authorship, the orchestrator MUST:

1. Before pinning any L_max ≥ 10 in a gate's machinery pin, verify recursive Casimir-projection feasibility per the Casimir-bound or Friedrich-Bär protocol above.
2. If the plan-pinned L_max is structurally redundant under the protocol, downgrade the operational L_max to the smallest p+q satisfying the Casimir-bound argument; record both `L_max_plan` and `L_max_operational` in the npz output keys.
3. If the plan-pinned L_max is empirically infeasible (irrep construction timeout) but the bottom-K observable is structurally saturated per Friedrich-Bär, replace sparse-Lanczos prescription with the saturation-theorem analytic argument and tag the verdict-line scheme accordingly.
4. Honest disclosure of any operational deviation from plan §6 machinery pin in the working-paper §"Methodology" subsection + verdict-line convention/scheme tag is **mandatory** per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 boundary (the deviation is in-session structural correction, NOT convention-shopping, IFF honestly disclosed; absent disclosure it falls under Class 1).
