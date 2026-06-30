# Regulator-Pin Discipline (a_n Seeley-DeWitt Coefficient Tagging)

## Rule

Every NEW citation of a Seeley-DeWitt coefficient `a_n` in a computation script,
working-paper section, or plan-block MUST include an explicit regulator-pin
tag. Bare `a_n` (without superscript regulator tag) is FORBIDDEN going forward.

This rule is **forward-looking**: legacy scripts containing bare `a_n` are
in carry-forward triage (~20k bare-a_n hits across 638 files identified at
audit; manual semantic review queued — see §Carry-Forward).

## Tag Format

`a_n^{<regulator_name>}` where `<regulator_name>` is one of:

  - `ζ`        — zeta-function regularization
  - `Pauli-Villars` — Pauli-Villars regularization
  - `Mellin`   — Mellin-Barnes regularization
  - `lattice`  — lattice spacing regularization
  - `cutoff`   — sharp UV cutoff regularization

### Example

```
✗ Bare:    a_2 (regulator unspecified)
✓ Tagged:  a_2^{ζ}                  (zeta-regulated Seeley-DeWitt)
✓ Tagged:  a_2^{Pauli-Villars}      (PV-regulated Seeley-DeWitt)
✓ Tagged:  a_2^{Mellin}             (Mellin-regulated)
```

## Mellin Pole-Set Labeling (S_s vs curvature-degree grading n)

Every citation of a Mellin-cone residue pole `s=N` of `ζ_{D_K}(s)` MUST declare
BOTH (a) the printed zeta power convention and (b) whether `N` is the pole index
in the Mellin variable `s` or the curvature-degree grading `n`. Bare `s=N`
(no convention + no S_s/n declaration) is FORBIDDEN going forward.

### Rule

The pole set in the Mellin variable `s` and the curvature-degree grading `n`
are DISTINCT integer meshes related by the exact map `n = d − 2s` (double-power
convention `ζ_{D_K}(s)=Σ m_k λ_k^{−2s}`, poles at `s=(d−n)/2`) OR `n = d − s`
(single-power convention `ζ_{D_K}(s)=Σ m_k λ_k^{−s}`, poles at `s=d−n`). At d=8:

- Double-power (Conv. A): `S_s = {0,1,2,3,4}`  ;  `n = {0,2,4,6,8} = 8 − 2s`
- Single-power (Conv. B): `S_s = {0,2,4,6,8}`  ;  `n = {0,2,4,6,8} = 8 − s`

`{0,2,4,6,8}` is ALWAYS the curvature-degree grading `n` (the CM-1995
dimension-spectrum label); it is the s-pole set ONLY under the single-power
convention. Reading `n` as if it were the double-power `s` mis-locates each pole
by `Δ = n − s = 8 − 3s` — a factor-≈2 mislabel at the load-bearing poles (a₂, a₄).

### Tag format

A Mellin residue citation carries `convention=...-poleconv-{A-double|B-single}`
AND states `(pole_in_s=N_s, curvature_grade_n=N_n)` explicitly. Example:
`a₂` residue at `s=3` (Conv. A) ≡ `s=6` (Conv. B), both `n=2`.

### Cross-algebra caveat

When the residue is evaluated on an algebra EXTENSION (e.g. SU(4)_PS rank-4
`A_K^{PS}=ℂ⊕M₂(ℂ)_L⊕M₂(ℂ)_R⊕M₄(ℂ)`), the pole index lives on the extended
spectral triple's dimension spectrum, NOT the SU(3) `S_s`; the convergence
threshold shifts (shell-sum `L^{d−2s}` converges iff `s > d_eff/2`; rank-4 A₃
shifts the threshold +1 unit vs SU(3)). Declare the algebra alongside the pole.

### Audit

`computations/_shared/_a_n_regulator_pin_audit.py` is extended to flag bare
`s=N` Mellin-residue citations lacking the `poleconv-{A|B}` tag and the
`(pole_in_s, curvature_grade_n)` declaration. Bare `s=N` → SOURCE-RECONCILIATION
advisory (S2); promotes to MANDATORY at K=3 per
`feedback_rules-compensate-missing-structure.md`.

## Rationale

The numerical value of `a_n` depends on the regulator.
Bare `a_n` in a downstream script silently consumes the calling-context
regulator, which may differ from the producing-script regulator. This is a
Class-8 PRU vulnerability per `.claude/rules/epistemic-discipline.md`.

## Audit

The audit script `computations/_shared/_a_n_regulator_pin_audit.py` greps
for bare `a_n` patterns matching the regex `\ba_(\d+)\b(?!\^)` and flags
violations.

```
python computations/_shared/_a_n_regulator_pin_audit.py             # report mode
python computations/_shared/_a_n_regulator_pin_audit.py --json      # machine-readable
python computations/_shared/_a_n_regulator_pin_audit.py --new-only  # only NEW files
```

`/weave --update` may auto-run this audit.

## Carry-Forward

Pre-existing `computations/_shared/` + historical session archives
contain ~20,343 bare `a_n` hits across 638 files. Auto-
retrofit of all of these via mechanical regex inference is over-broad
(many matches are NON-Seeley-DeWitt: plain variable names, string
literals, lattice-spacing `a_n` symbols, generic indices). The audit
verdict was FAIL with diagnostic; the manual semantic-review
task is queued as `A-N-SEELEY-DEWITT-RETROFIT`.

In the interim, NEW files MUST comply. The audit
script flags violations; the rule applies to FUTURE-AUTHORED files.

## Extension: Sage-Exact Rationals for Ω_GW Regulator-Class Values

The regulator-pin discipline above (a_n Seeley-DeWitt tagging) is extended to **regulator-class-tagged Ω_GW values**. Future falsifier-design citing the Ω_GW(LISA) regulator-class predictions MUST use Sage-exact rationals (not round-figure approximations).

### Rule

When citing Ω_GW^(R) for regulator-class R ∈ {(A), (C), (intermediate-classes)}, the published value MUST be the Sage-exact rational form (or its full-float64 image) — NOT the round-figure estimate. Round-figure forms understate or overstate the value by structurally significant factors.

### Calibration corpus

| Quantity | Round-figure (FORBIDDEN) | Sage-exact (REQUIRED) |
|:---------|:-------------------------|:----------------------|
| `Ω_GW^(C)` (Companion-null at LISA frequency) | `1e-57` | `8.299e-58` (exact) |
| `Ω_GW^(A) / Ω_GW^(C)` split (A-class vs C-class) | `~45 OOM` | `47.081 OOM` (Sage-verified) |

The `1e-57` round-figure differs from `Ω_GW^(C) = 8.299e-58` by only `1.205×` = `0.081 OOM` (SAME decade: `1e-57 / 8.299e-58 = 1.205`; the round figure OVERSTATES by a hair, it does NOT understate by `~10×`). For the SINGLE VALUE `Ω_GW^(C)`, the binding reason to publish the Sage-exact rational is publication-precision hygiene (Class-8.3 per `epistemic-discipline.md §"Pre-Registration Completeness"`), NOT an order-of-magnitude blunder. The OOM-significance lives in the `(A)/(C)` SPLIT (`47.081 OOM` Sage-exact vs the `~45 OOM` round figure), not in the single-value round-off — cite the Sage-exact form for BOTH, but scope the rationale correctly per quantity.

### Discipline

1. **Compute Ω_GW^(R) via Sage QQ** when the regulator-class value enters a falsifier-master-inventory row, a registry entry, or a canonical_constants pin
2. **Cite the source SHA** alongside the value
3. **Forbid round-figure substitution in registry text** — registry entries cite the Sage-exact value; round figures permitted ONLY in narrative prose with explicit "approximately" qualifier and a parenthetical pointer to the Sage-exact pin
4. **Audit at plan-freeze**: cross-check any Ω_GW citation against canonical_constants.py for regulator-class tagging; missing Sage-exact form → SOURCE-RECONCILIATION advisory (S2)

This extension applies the Class-8.3 publication-precision pre-registration rule (epistemic-discipline.md §"Pre-Registration Completeness") to Ω_GW specifically, where the structural significance of the (A)/(C) regulator-class split makes round-figure substitution false-PASS-prone.

## Extension: β_shell FI Classification at d=4 Substrate-Distance s* = 3 (advisory until K=3)

When citing the d=4 per-shell shell-sum exponent β_shell at substrate-distance s* = 3, the published value MUST be tagged FI (Functional-Invariant) per `epistemic-discipline.md §"Source Reconciliation"` FI/RD/MIXED taxonomy. β_shell is INVARIANT across the F_2 = {ζ, SDW} K-invariant identity sub-atlas — it is the SHELL-axis specialization of the F_2-class FI theorem (parent: F_traj a_2-ratio FI theorem; same algebra-INVARIANT axis inheritance).

### Discipline

1. **FI tag required**: β_shell citations MUST tag FI class when entering `canonical_constants.py` pin OR registry-text observable specification.
2. **Cross-link to parent theorem**: β_shell inherits FI classification from the F_traj a_2-ratio FI theorem at locked-norm L_k=1.
3. **Sage-Q citation**: β_shell value MUST be cited as Sage-Q exact (per `regulator-pin-discipline.md §"Extension: Sage-Exact Rationals"` above); round-figure forms are FORBIDDEN in canonical pins.
4. **Plan-freeze audit**: when β_shell appears in a plan PIN MAP, verify FI class tag is present; missing FI tag → SOURCE-RECONCILIATION advisory (S2) per `epistemic-discipline.md §"Source Reconciliation"` Class-(b) PIN-LOOSE-SOURCE-TIGHT extension.

Calibration corpus: `sessions/framework/registry/cross-pillar-bridge-corpus.md`.

## Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — Calibration Corpus Extension

The Class-(c) PIN-DRIFT-FROM-STALE-SOURCE class in `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" is extended with a NEW calibration corpus instance.

### Stale-source instance

A plan threshold cited a stale view of what `η` (eta-invariant) could detect — a view that was post-superseded by the Bulletin #2 promotion (even Seeley-DeWitt parity-blindness theorem promoted from candidate to wall).

The plan asked: "Does η discriminate between the (C_H, C_epsH) parity-twin pair?" By the post-supersession canonical, the answer is structurally NO (η is even-grading by BDI ±-pair theorem; HP^1 content is odd-grading by parity orthogonality; even cannot decode odd). The plan threshold was structurally testing the wrong hypothesis (what η could detect under the pre-supersession view) rather than the post-supersession canonical.

### Composite verdict pattern

The verdict closed as **composite INFO** (sign=PASS, magnitude=FAIL, regime=VALID): literal η-threshold tests a hypothesis Bulletin #2 already disproved. Both bulletins close STRUCTURALLY in-session via the canonical (η = 0, GV ≠ 0) signature on the (C_H, C_epsH) parity-twin pair:
- Bulletin #1 (ε_H J-parity wall) → CONFIRMED-DEMOTED-SCHEME-DEPENDENT
- Bulletin #2 (even Seeley-DeWitt parity-blindness theorem) → CONFIRMED-PROMOTED-PARITY-BLINDNESS (strengthened to ALL even-grading regulator-weighted Mellin moments)

### Rule discipline

Plan-freeze validators citing a threshold whose source was published BEFORE a supersession event (here: the Bulletin #2 promotion) MUST:

1. **Re-query the canonical** via `mcp__knowledge__.get_constant(name)` or `trace_entity(mechanism)` for the most-recent canonical view
2. **Compare the plan threshold against the post-supersession canonical** — if the plan threshold is testing a hypothesis the supersession event already disproved, route to PIN-DRIFT-FROM-STALE-SOURCE Class-(c) remediation
3. **Re-pin to current canonical** OR **document the legacy-test rationale** explicitly in the plan-block (e.g., "this gate tests the literal η-threshold per the pre-supersession view; expected to FAIL the literal threshold; structurally PASSes under the post-supersession canonical via the (η=0, GV≠0) signature")

### Forward-looking remediation

Future joint-probe gates targeting HP^1 detection MUST use **odd-grading observables** (GV-Heitsch, K-theoretic torsion, η-Cheeger-Simons secondary classes) — never η alone. This calibration corpus instance establishes a permanent design rule extending the Class-(c) PIN-DRIFT-FROM-STALE-SOURCE class with a concrete supersession-event precedent.

### Cross-link — four-axis orthogonality (UV-regulator × Level × Binding × MACHINERY-SCOPE)

The regulator-pin discipline (a_n^{regulator} at the UV-regulator axis) is COMPLEMENTARY to four other pin axes that close non-redundant silent-class-conflation pathologies. The five axes are pairwise independent. (The heading retains its historical "four-axis" name for cross-reference stability; the Counting axis is the fifth row.)

| Axis | Pin form | Closes | Substrate analog |
|:-----|:---------|:-------|:-----------------|
| UV-regulator (this rule) | `a_n^{ζ}`, `a_n^{Pauli-Villars}`, `a_n^{Mellin}`, `a_n^{lattice}`, `a_n^{cutoff}` | UV-regulator silent class-conflation | `UV_REGULARIZATION_CONFLATION` PASS |
| Level (`substrate-first-canonical-sourcing.md §(iv)`) | `convention=...-SCHEMATIC` suffix + CLASS pin (FULL/SCHEMATIC) + companion row `# tier_pin=TIER-2` | SCHEMATIC vs FULL physical silent class-conflation | K=4 calibration corpus |
| Binding | `convention=...-CANONICAL-IMPORT-BINDING` vs `-SUBSTRATE-NATURAL-BINDING` suffix | Canonical-import-binding vs substrate-natural-binding silent class-conflation (e.g., Level-3 anchor PASS via canonical-import pin while substrate-natural compute returns null) | §VII.AF.1 canonical-import-binding; §VII.AV substrate-natural-binding |
| MACHINERY-SCOPE | `convention=...-CACHE-PROJECTION` vs `-FULL-LEAF-FOLIATION` suffix (Cheeger-Simons 1985 §II) | Cache-projection-truncated observable (foliation-blind) vs full-leaf-foliation-truncated observable (foliation-aware) | Reading A scheme-INDEPENDENT to within 1e-3 M_KK² |
| Counting (intensive/extensive) | `convention=RATIO-NORMALIZED-TRACE-MEAN` vs `convention=RATIO-BLOCKSUM` | Intensive-vs-extensive silent class-conflation on degenerate-channel functionals (discriminator domain: any per-channel functional on a spectral-triple channel with multiplicity n_g > 1; the two classes differ by the channel's K₀-rank factor n_g, topological) | mass/position-class = state evaluation ρ_g(f(D)) with ρ_g = P_g/Tr(P_g); width/degeneracy/occupation/action-moment-class = weighted trace n_g·ρ_g(f(D)) |
| Mass-dimension/parity | `convention=…-DA-<n>-PARITY-<even\|odd>` suffix on transport-degree consumers | silent dimensional-class/parity conflation (a transport degree imported across `d_A`/parity classes with no `d_A`-tag — e.g. the W3 `deg_T=2.0` EVEN imported onto a `d_A=+1` ODD temperature, a degree right for the `d_A=0` morphism sector but wrong-parity for an odd-`d_A` scale leg) | §23.0(5) parity selection rule (`d_A=0` even-morphism sector vs `d_A=odd` sign-locked `M_KK^1` scale leg) |

**Status**: UV-regulator MANDATORY; Level MANDATORY at K=4; Binding SUGGESTION at K=2; MACHINERY-SCOPE SUGGESTION at K=2; Counting SUGGESTION at K=1 (→ MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`; a gate can PASS all four prior axes while silently unpinned on counting — pairwise independence is empirical, see the calibration corpus); Mass-dimension/parity SUGGESTION at K=1 (S110 W4; → MANDATORY at K=3; substrate: corpus §23.0(5) parity selection rule — a transport-degree consumer can PASS all five prior axes while silently unpinned on the transported observable's `d_A`/parity). K-counter advancement on Binding + MACHINERY-SCOPE axes requires the **Hybrid Independence Test** at `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`: `(i ∨ ii ∨ iii) ∧ iv` where (i) distinct substrate-IS pillar from prior K-instances; (ii) distinct laboratory-IN pillar; (iii) distinct bridge map class; (iv) independent algebraic envelope. K=3 MANDATORY promotion threshold per `feedback_rules-compensate-missing-structure.md`.

**Phi-correspondence framing**: the 4-axis orthogonality is a methodology-rule F-image of substrate-IS structural orthogonality per `epistemic-discipline.md §"Layer-Decomposition"`. Level-pin axis pathology classes as Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (not Class-(f) PIN-PLACEHOLDER); orthogonality is invariant under the (d)-vs-(f) reclassification.

**All four axis pins MUST be carried** in the verdict-line `convention=` field when their respective discriminator applies. A producing script may PASS one axis while FAILing another — e.g., correctly tagging `a_n^{Mellin}` (UV-regulator pin compliant) while consuming the SCHEMATIC `_spectral_action_regulators.py` Mellin helper (level-pin violator) — that gate FAILs the level-pin audit even though it PASSes the regulator-pin audit. A producing script may correctly tag `-FULL-LEAF-FOLIATION` (MACHINERY-SCOPE pin compliant) while citing a canonical-import binding on a substrate-natural-binding observable (Binding-axis violator). The four pins are independent (orthogonal axes); each is MANDATORY at plan-freeze for any gate whose observable inhabits the corresponding axis discriminator domain.

**Positive-calibration model**: future SCHEMATIC-helper-consuming scripts SHOULD pattern-match `convention=<scheme>-SCHEMATIC` + companion row `# tier_pin=TIER-2` cross-linking to `substrate-first-canonical-sourcing.md §(iv)`.

**Audit**: level-pin enforcement via `computations/session-88/s88_w7b_lf_e_schematic_module_audit.py` (forward-extensible to plan-freeze auditor `_substrate_first_provenance_audit.py`). Binding-axis audit `_hybrid_independence_test_audit.py` (queued). MACHINERY-SCOPE audit `_machinery_scope_axis_audit.py` (queued; regex `convention=.*-(CACHE-PROJECTION|FULL-LEAF-FOLIATION)\b`; HARD-HALT remediation on absent suffix when observable is foliation-sensitive).

Calibration corpora + K-counter advancement records: `pru-class-corpus.md §12` (Level axis) + `cross-pillar-bridge-corpus.md` (Binding + MACHINERY-SCOPE forward calibration) + `pru-class-corpus.md §20` (Counting axis). Counting-axis audit `_counting_axis_audit.py` (queued; regex `convention=RATIO-(NORMALIZED-TRACE-MEAN|BLOCKSUM)\b`; S2 advisory under SUGGESTION).

### 2-bit `L_max`-FLAT-vs-`m_PV`-FLOWING anchor-vs-diagnostic fingerprint (SUGGESTION at K=1)

For an anchor-vs-evaluator dispute where two evaluators of a putatively-shared substrate-distance-N pole observable disagree by a large factor, the PAIR `(L_max-behavior, m_PV-behavior)` is a 2-bit structural signature: a canonical anchor is `L_max`-SATURATED + `m_PV`-value-DEFINING; a regulator-class diagnostic is `L_max`-FLAT (const offset) + `m_PV`-FLOWS to the anchor; a truncation artifact is `L_max`-FLOWS (`O(L^{−α})` → anchor); a genuinely-different operator does not flow to THIS anchor on EITHER axis. Load-bearing caveat: requires BOTH axes SEPARATELY scannable; if the pipeline ties regulator mass to truncation the signature DEGENERATES. Large-factor test: a genuine regulator-class shift is bounded `O(moment-ratio spread) ≈ O(20%)`; a factor far exceeding this is NOT a regulator shift but a different structural relationship. Full directive + K=1 calibration corpus: `sessions/framework/registry/cross-pillar-bridge-corpus.md §22`.

## Extension: Channel-Scope Suffix Discipline for Register Citations of Channel-/Parity-Scoped PERMANENT Theorems (SUGGESTION at K=1)

Register-surface citations of channel-/parity-scoped PERMANENT theorems MUST carry the scope inside the citation token itself. Canonical instance: write 'S41 W1-2 (T-channel S_F^Connes = 0; channel-scoped per S56 W4 Correction 1)' — never bare 'S41 W1-2, exact', never 'seesaw = 0'. Design rationale: scope-inside-the-token is the register-side analog of contrast-inside-the-output (the W5-2 producing script prints the linear-[C2,D_F] pitfall contrast in its own output rows so the wrong reading cannot regenerate from the artifact); separable parentheticals do not survive consolidation/aggregation steps (the L2 mint — and both headline-vs-correction instances that REACHED registers escaped through exactly such steps; see the workshop E-3 2/2-escaped-vs-2/2-caught split). Forward generalization: any PERMANENT theorem whose physical content is channel-/parity-scoped (T-channel vs P-channel; gamma9-odd vs even) receives the same treatment; the K-counter advances on distinct theorems, not repeat citations of S41.

**Status**: SUGGESTION at K=1; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.

Calibration corpus: `sessions/framework/registry/pru-class-corpus.md` (channel-scope suffix section).
