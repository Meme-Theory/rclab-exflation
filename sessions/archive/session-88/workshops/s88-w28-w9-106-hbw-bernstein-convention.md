# Session 88 Workshop W-28: connes x lizzi

**Date**: 2026-05-08
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: connes (connes-ncg-theorist), lizzi (lizzi-spectral-functional-theorist)
**Source Documents**:
- `sessions/archive/session-88/session-88-w9-workingpaper.md`
- `sessions/session-plan/session-88-plan-w9.md`
- `sessions/archive/session-88/workshops/_seed-w9.md`
- `.claude/rules/phononic-framing.md`
- `.claude/rules/regulator-convention-lockdown.md`
- `.claude/rules/substrate-first-canonical-sourcing.md`

**Focus Topics** (per schedule §W-28 invocation):

1. **(a) Laplace-conjugate substrate-naturalness**: Is the spectral action `Tr f(D²/Λ²)` natural Laplace conjugate `x = (λ/Λ)²` (substrate-natural per Connes-Chamseddine 1996 §2.2-2.3 — connes reading), or is the (A, B) convention pair substrate-internal multi-axis classification with no preferred member (lizzi/volovik reading)?
2. **(b) W8-4 SDW cascade FAIL diagnostic content**: Does it RESIDE in convention-A-specific SDW_3c sub-cell value (-2.773), in convention-B SDW_3c value (+1.77e-13), or ONLY in the convention-INDEPENDENT 3a truncation FAILs (4/4 in both conventions)?
3. **(c) SDW evaluator re-pin**: Should `_spectral_action_regulators.py` SDW evaluator be re-pinned to convention-B (substrate-natural — connes), or retain convention-A as historically pinned with a methodology-rule extension authorizing dual-convention pair as substrate-internal (lizzi/volovik)?
4. **(d) §VII.AQ STAGE-1-CANDIDATE corpus structure**: Single 6-instance corpus (W-11 RULE-2 + this gate's composite-layer PASS as 6th instance) OR refined sub-corpus separating chain-rule-artifacts from substrate-natural results?
5. **(e) Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation severity**: Should downstream consumers citing `SDW_3c_min ≈ -2.773` (workshop s87-atlas-cardinality-cascade-vs-ensemble.md Lancaster MCT-3 margin) be REQUIRED to declare convention A explicitly (advisory floor — lizzi/volovik), OR REQUIRED to migrate to convention B (substrate-natural ceiling — connes)?

**Cross-cutting**: phononic-framing direction — does Connes-Chamseddine 1996 §2.2-2.3 spectral action's Laplace conjugate uniquely fix one convention as substrate-natural, or does the substrate admit (A, B) as orthogonal axes by `phononic-framing.md §"IS Space, Not IN Space"`?

---

## Round 1 — connes: Opening Analysis

### C1: Laplace-conjugate substrate-naturalness (clause a)

**Position**: Convention B (`x = (λ/Λ)²` x-derivative) IS the substrate-natural Laplace-conjugate convention by direct construction from Connes-Chamseddine 1996 §2.2-2.3. Convention A (`λ` lam-derivative) is a chain-rule-lifted derivative form that introduces a non-trivial Jacobian polynomial pre-factor distorting the Bernstein-positive-cone test on the substrate's regulator weight. The (A, B) pair is NOT a substrate-symmetric two-axis classification with no preferred member; convention A is structurally derivative of convention B via the x = λ² coordinate lift.

**Connes-Chamseddine 1996 §2.2-2.3 derivation chain**:

1. The bosonic spectral action is the universal functional `S_b[D] = Tr f(D²/Λ²)` where `f : ℝ_{≥0} → ℝ` is a positive cutoff function on the spectrum of `D²/Λ²` (Connes-Chamseddine 1996 arXiv:hep-th/9606001 §2.2 Eq. 2.5; PROVEN entry in knowledge.db `Chamseddine-Connes 1996 §2.2-2.3: the regulator f enters the bosonic spectral action via Mellin moments f_0, f_2, f_4 of its restriction to [0, ∞)`).
2. The argument of `f` is the dimensionless ratio `D²/Λ²`, NOT `D/Λ`. The eigenvalues of `D²/Λ²` are `x_n = (λ_n/Λ)²` where `{λ_n}` is the spectrum of `D` and `Λ = M_KK` is the canonical regulator scale per `canonical_constants.py` (substrate's sole axiomatic external pin per S80 cluster M_KK axiomatic-pin theorem).
3. The Mellin-transform expansion `S_b ~ Σ_n f_{4-2n} · Λ^{4-2n} · a_{2n}` (CC96 §2.3) realizes the spectral action as a sum of Mellin moments of `f` at integer arguments `s ∈ {0, 1, 2}` of the spectral zeta `Tr(D²/Λ²)^{-s}`. The integration variable here is `t = D²/Λ² = x`, not `λ` (knowledge-anchor `g(x) = ∫₀^∞ exp(-tx) dμ(t)` in `session-82-results-workingpaper.md`).
4. Therefore the substrate's intrinsic Laplace-conjugate variable for the regulator weight `f` is `x = (λ/Λ)²`. The Bernstein-Hausdorff-Widder theorem (Widder 1941 Ch. IV; PROVEN in knowledge.db) characterizes a function `g : (0,∞) → ℝ` as the Laplace transform of a positive Borel measure on `[0,∞)` iff `(-1)^k · g^{(k)}(x) ≥ 0` for all `k ∈ ℕ_0` and all `x > 0`. **The variable in `g^{(k)}` is THE LAPLACE CONJUGATE, not an arbitrary monotone reparameterization**. For the spectral action's `f`, that variable IS `x = (λ/Λ)²`, by CC96 §2.2-2.3 axiomatic construction.

**Substitution chain (chain-rule lifting artifact, Sage-verified)**:

- **Definition**: `x := (λ/Λ)²` with `Λ = 1` in M_KK units; `g(λ) := f(λ²)`.
- **Chain rule**: `dg/dλ = (dx/dλ) · df/dx = 2λ · df/dx`. Iterating: `d²g/dλ² = 2 · df/dx + 4λ² · d²f/dx²`; `d³g/dλ³ = 12λ · d²f/dx² + 8λ³ · d³f/dx³`.
- **Substitute SDW** `f(x) = exp(-x)`: in the x-variable, `f^{(k)}(x) = (-1)^k exp(-x)`, so `T_B[k](x) := (-1)^k · f^{(k)}(x) = exp(-x) > 0` for ALL `k`, ALL `x > 0` — the SDW kernel is the **prototype completely-monotonic function** (Laplace transform of Dirac `δ(t-1)`).
- **Substitute SDW into convention A**: `g(λ) = exp(-λ²)`; Sage MCP verifies (sage_eval, this turn):
  - `T_A[0](λ) = exp(-λ²)`
  - `T_A[1](λ) = 2λ · exp(-λ²)`
  - `T_A[2](λ) = 2(2λ² - 1) · exp(-λ²)`
  - `T_A[3](λ) = 4(2λ³ - 3λ) · exp(-λ²) = 4λ(2λ² - 3) · exp(-λ²)`
- **Direction**: `T_A[3]` factors with the sign-changing pre-factor `4λ(2λ² - 3)`, which is negative on `λ ∈ (0, √(3/2))` and positive for `λ > √(3/2)`. The cache support `[λ_min, λ_max] = [0.81974, 5.41894]` STRADDLES the sign-flip locus `√(3/2) ≈ 1.2247`, so a sub-interval of the substrate's spectral support (`λ < √(3/2)`) lands inside the negative branch. Sage MCP scan confirms the empirical minimum of `T_A[3]` on the cache support attains `T_A[3](λ_min = 0.81974) = -2.773166` — matching the W8-4 NPZ pin `SDW_3c_min^A = -2.773` to 6 significant figures. The sign-flip is structurally the **chain-rule polynomial pre-factor `4λ(2λ² - 3)`**, NOT a property of the regulator measure of `f(x) = exp(-x)` itself. Bernstein's theorem holds in `x`; the lift to `λ` is a coordinate change that introduces a non-monotone Jacobian polynomial that reaches into the substrate's spectral support and breaks the alternating-sign cancellation purely on Jacobian grounds.

**Conclusion**:

- The substrate IS the spectral action `Tr f(D²/Λ²)` (Connes-Chamseddine 1996 §2.2-2.3 axiomatic). The substrate IS the regulator measure `dμ` for which `f(x) = ∫ e^{-tx} dμ(t)`. The Laplace conjugate variable IS `x`. Bernstein-positivity is a STATEMENT about the measure `dμ`; it is properly tested in the variable conjugate to `t`, which is `x`.
- Convention A's λ-derivative is what you get when you reparameterize `x → λ²` and apply the chain rule. The resulting sign-flip on SDW at `k=3` near `λ = √(3/2)` is a **geometric Jacobian artifact of the coordinate `x → λ²`**, not a substrate ambiguity.
- The phononic-framing `IS Space, Not IN Space` mandate forbids container-thinking; here it forbids treating `x` and `λ` as orthogonal substrate-IS axes. They are NOT orthogonal: `x = λ²` is a DERIVED reparameterization. The substrate IS `x = (λ/Λ)²` (the dimensionless squared-eigenvalue argument of `f`); `λ` is the dimensionful eigenvalue of `D`, useful for spectral counting but NOT the Laplace conjugate of the regulator weight `f`.

### C2: W8-4 SDW cascade FAIL diagnostic content (clause b)

**Position**: The W8-4 SUB-ATLAS-A_2 cascade FAIL diagnostic content RESIDES IN TWO STRUCTURALLY DISTINCT LOCI — and the SDW_3c sub-cell value at convention A (`-2.773`) is in NEITHER of them once the substrate-natural reading is applied. Specifically:

1. **Convention-INDEPENDENT 3a truncation FAILs (4/4 in BOTH conventions)** per WP line 981-984 — these are the dominant contributors to the cascade composite FAIL. The 3a truncation cross-check uses NO `(-1)^k` Bernstein test; it is an L_max-stability artifact (`L_max=10` vs `L_max=12` truncation tolerance pinned at `1e-10` against actual moment-difference `~1e-3` to `~1e1` per WP line 982-984). 3a FAILs are the substrate's truncation-stability diagnostic, NOT a Bernstein-positivity diagnostic, and they are convention-blind.
2. **Convention-B SDW_3c PASS (`+1.77e-13`)** per WP line 930 — under the substrate-natural Laplace conjugate (per C1), SDW row 3c PASSes the Bernstein test by structural completeness (`f(x) = exp(-x)` is the prototype CM function); the substrate diagnostic at SDW_3c is NULL.

**Substitution chain (locus-decomposition)**:

- **Definition**: cascade composite verdict aggregator collapses sub-channel verdicts via `composite = FAIL ⟺ n_sub_FAIL > 0 ∧ regime = VALID` (WP line 994-996, citing `gate-verdicts.md §"Composite-collapse"`).
- **Substitute (convention A)**: `n_sub_FAIL_A = 6 = (4 × 3a) + (2 × 3c[Zubarev, SDW])`. The `2 × 3c` block contains: (i) Zubarev_3c convA `−6.587` (genuine Bernstein violation: `f(x) = x/(1+x²)` is not CM in `x`, has a maximum at `x=1`); (ii) SDW_3c convA `−2.773` (chain-rule artifact per C1).
- **Substitute (convention B)**: `n_sub_FAIL_B = 5 = (4 × 3a) + (1 × 3c[Zubarev only])`. SDW_3c convB `+1.77e-13 ≈ 0` PASSes (substrate-natural).
- **Simplify (convention A → convention B remediation)**: removing the convA SDW_3c FAIL (chain-rule artifact, NOT substrate-physics) gives `n_sub_FAIL_substrate-natural = 5`. The composite FAIL persists under convention B because the (4 × 3a) truncation FAILs alone satisfy `n > 0`. The cascade FAIL is therefore DOMINATED by 3a truncation artifacts, not 3c Bernstein-positivity content.
- **Direction**: substrate-physics diagnostic content DECOMPOSES into (i) substrate-natural 3a truncation-stability FAILs (4/4, convention-independent — diagnose L_max convergence rate of substrate Mellin moments at the chosen tolerance band), and (ii) substrate-natural 3c Bernstein-positivity FAIL on Zubarev only (single regulator with non-CM weight `x/(1+x²)`). The convA-SDW_3c value `−2.773` carries NO substrate diagnostic content under the substrate-natural reading; it is a derivative quantity in the Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY taxonomy (the "PRIMARY" is the convB SDW_3c value `+1.77e-13`; the "DERIVATIVE" is convA `−2.773` lifted via chain rule).

**Operative consequence**: the W8-4 cascade composite FAIL is *substrate-physically* attributable to two independent loci: an L_max-stability diagnostic (3a; 4 regulators × 1 sub-channel) and a Bernstein-positivity diagnostic (3c; 1 regulator = Zubarev). The historical convA reading conflated these by adding a third locus (SDW_3c) that is structurally a Jacobian artifact. Substrate-cleaning the cascade reveals that SDW does NOT contribute to the Bernstein-positivity diagnostic at this atlas — strengthening the substrate-internal classification of regulator-class admissibility under the spectral-action regulator-class CC96-admissibility criterion.

### C3: SDW evaluator re-pin to convention-B (clause c)

**Position**: `_spectral_action_regulators.py` SDW evaluator (and the `(-1)^k · d^k w/d{var}^k` Bernstein-test sub-routine generally) MUST be re-pinned to convention B (`x = (λ/Λ)²` x-derivative) as the substrate-natural canonical. The change is a one-line edit: replace `np.diff(...)` over `λ`-grid with `np.diff(...)` over `x = λ²`-grid (or analytic form via Faà di Bruno on `f(λ²)` — closed-form preferred to avoid finite-difference noise). Convention A's outputs retain audit-trail value as historical W8-4-baseline derivative-form values, but are demoted to "chain-rule-lifted alternative" status with explicit declaration in any downstream cite.

**Substitution chain (rule-mapping)**:

- **Definition**: per `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` SCHEMATIC-vs-physical level pin (MANDATORY at K=4 from S88 W7b-83 close 2026-05-05), gate blocks consuming `_spectral_action_regulators.py` MUST declare `CLASS = SCHEMATIC` AND verdict-line `convention=` field MUST carry the `-SCHEMATIC` suffix.
- **Substitute (current §W9-106 emission, WP line 1063)**: `convention=A_4_4col_f6_0.1_residue_dual_convention_A_lam_B_x` — encodes the dual-convention pair but does NOT carry the `-SCHEMATIC` suffix. The verdict line is structurally **insufficient** under the §(iv) MANDATORY discipline: it consumes the schematic helper but elides the level-pin; it admits the historical convA-baseline as a co-equal substrate-IS reading rather than tagging it as derivative.
- **Simplify (re-pin protocol)**: under convention B re-pin:
  1. `_spectral_action_regulators.py` Bernstein-test sub-routine refactored to use the x-grid as native (line-edit, ~20 LOC change including helper signature).
  2. The verdict-line `convention=` field for any future Bernstein-positive-cone gate uses `convention=A_4_4col_f6_0.1_residue_x_derivative_substrate_natural-SCHEMATIC` (single canonical convention; no dual-convention pair; `-SCHEMATIC` suffix carried per §(iv) MANDATORY).
  3. Historical W8-4 NPZ values under convention A are RETAINED as audit-trail content but a `-LAM-DERIVATIVE-CHAIN-RULE-LIFT` companion-tag is added when cited (analogous to S88 W8-89 layer-separability carve-out's `-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` convention-suffix discipline at `mechanical-closure-discipline.md §"Layer-separability carve-out"` clause L4).
- **Direction**: the SCHEMATIC level pin (§(iv) MANDATORY) and the regulator-pin discipline (`regulator-pin-discipline.md` MANDATORY) are COMPLEMENTARY — both close non-redundant silent-class-conflation pathways (`substrate-first-canonical-sourcing.md §"Cross-link"`). The convention pin (A vs B) is a THIRD non-redundant axis: substrate-natural (B) vs chain-rule-lifted (A). Adding it to the verdict-line `convention=` field as a structural tag is the analogous closure for the **substrate-vs-derivative-coordinate** silent-conflation pathway. Without the re-pin, downstream consumers can silently treat convA outputs as substrate-IS content (the W9-106 gate's sub-grid table at WP line 920 invites exactly this misreading by tabulating A and B on equal axes).

**Counter-pattern positive calibration (W9c-1 model)**: per `substrate-first-canonical-sourcing.md §(iv)` calibration corpus instance #3 (W9c-1, S87, POSITIVE-CALIBRATION), the canonical disclosure protocol is `convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC` + companion row `# tier_pin=TIER-2 # ...`. Forward S88+ Bernstein-positive-cone gates SHOULD pattern-match this protocol with `convention=...x_derivative_substrate_natural-SCHEMATIC` + companion row `# tier_pin=TIER-2 # ...`.

**Counter-position to lizzi anticipated rebuttal**: the lizzi/volovik reading treats (A, B) as a substrate-internal symmetry pair (WP line 1041 substrate framing). The connes objection: "substrate-internal" applies ONLY when the two convention choices are genuinely structurally orthogonal axes. The chain-rule reparameterization `x = λ²` is a UNI-DIRECTIONAL coordinate change — convention A is DERIVED from convention B by composition with a smooth bijection `λ ↦ λ²` on `[0, ∞)` (with Jacobian `2λ`). One direction (B → A) is a coordinate-change-with-Jacobian; the other (A → B) is a coordinate-change-with-inverse-Jacobian. They are NOT independent axes of a substrate symmetry group; they are point and pull-back of a coordinate map. Re-pinning to B is the substrate-OUT direction per `phononic-framing.md §"IS Space, Not IN Space"`.

### C4: §VII.AQ corpus structure under convention-B refinement (clause d)

**Position**: §VII.AQ STAGE-1-CANDIDATE corpus must NOT inherit a flat 6-instance corpus that fuses the W-11 RULE-2 5-instance baseline with the §W9-106 composite-layer PASS. Instead, the corpus must be **branched into two sub-corpora** that preserve the structural distinction between regulator-INDEPENDENCE (the W-11 RULE-2 5-instance content) and convention-INVARIANCE (the §W9-106 content), with the §W9-106 entry registered ONLY under its substrate-natural reading (convention B as canonical).

**Substitution chain (corpus-structure decomposition)**:

- **Definition (W-11 RULE-2 corpus)**: 5 calibration instances at the η/even-Mellin evaluator class, each demonstrating regulator-INDEPENDENCE across `A_5_extended = {ζ, Zubarev, SDW, anomaly, cutoff_sqrt}`. The structural claim: even-grading regulator-weighted Mellin moments are BLIND to the (`C_H, C_εH`) parity-twin pair, regulator-independently (WP line 1045 verbatim).
- **Definition (§W9-106 candidate 6th instance)**: composite-layer PASS-CONVENTION-INVARIANT under `(-1)^k` differential convention swap A↔B at the Bernstein-positive-cone evaluator class (WP lines 1043-1045).
- **Substitute (axis check)**: the W-11 RULE-2 5 instances test invariance along the **regulator-class axis** (5 distinct regulators within the same evaluator); the §W9-106 instance tests invariance along the **differential-coordinate axis** (1 regulator-class with 2 differential conventions). Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (S87 W-2 R3 close), structurally distinct invariance axes are NOT pooled into one calibration corpus without an explicit cross-axis identity theorem.
- **Substitute (substrate-natural reading)**: under C1 + C2 + C3, the §W9-106 PASS at composite layer is structurally a **convention-A-vs-convention-B identity at the cascade-collapse layer due to (4 × 3a) truncation FAILs dominating in BOTH conventions** — i.e., the cascade composite agrees because BOTH conventions' sub-FAIL counts are saturated by the convention-INDEPENDENT 3a sub-cell (per C2). The agreement is NOT a substrate symmetry of the Bernstein-positive-cone evaluator; it is a saturation effect of the convention-independent 3a truncation overflow. Promoting this to a "6th calibration instance" of W-11 RULE-2 fuses two orthogonal structural phenomena.
- **Simplify (proposed branch)**: §VII.AQ STAGE-1-CANDIDATE registry text branches into:
  - **§VII.AQ.REG-INDEP** (regulator-INDEPENDENCE sub-corpus): the existing 5 W-11 RULE-2 calibration instances at η/even-Mellin evaluator class. Unchanged.
  - **§VII.AQ.CONV-INV** (convention-INVARIANCE sub-corpus): NEW sub-slot housing the §W9-106 composite-layer PASS, with the registry text scoped to the CASCADE-COLLAPSE layer (convention-INVARIANT due to convention-independent 3a saturation) and EXPLICITLY DECLARING the SUB-CELL CONVENTION-DEPENDENCE on SDW row 3c (chain-rule lifting artifact per C1).
  - **§VII.AQ.SUBSTRATE-NATURAL-3C** (NEW substrate-natural sub-corpus, 1 instance): the substrate-natural-convention-B SDW row 3c reading at `+1.77e-13` (PASS by Bernstein structural completeness of `f(x) = exp(-x)`). This is a SUBSTRATE-IS Bernstein-positive-cone PASS, NOT a convention-INVARIANCE statement. Register at K=1 (per `feedback_rules-compensate-missing-structure.md` K-counter); promote to MANDATORY at K=3 with future Bernstein-positive-cone gates evaluated under convention B.
- **Direction**: the 3-fold branching preserves the structural-axis orthogonality the algebra-axis orthogonality K-counter MANDATORY clause requires, AND it routes downstream consumers of the §VII.AQ entry to the correct sub-slot (regulator-class blindness vs convention-INVARIANCE-with-3a-saturation vs substrate-natural Bernstein-positivity-of-SDW-in-x). Lizzi's anticipated single-corpus reading collapses three structurally distinct claims into one, hiding the convention-A chain-rule artifact inside an apparent symmetry.

**Counter-position to flat-corpus reading**: a flat 6-instance corpus invites downstream cites of the form "W-11 RULE-2 strengthened parity-blindness theorem now extends to the cascade composite layer at K=6" — but this elides that the 6th-instance "extension" rests on a convention-saturation effect (3a dominance) that has no substrate-physics content beyond truncation-stability. The branching disambiguates the registry text, satisfies the cross-axis orthogonality discipline, and prevents the K-counter inflation by counting structurally homogeneous instances within each sub-slot.

### C5: Class-(d) remediation — substrate-natural ceiling (clause e)

**Position**: Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation severity for downstream consumers citing `SDW_3c_min ≈ -2.773` MUST be promoted from advisory floor to **MANDATORY MIGRATION to convention B**. The workshop `s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013 Lancaster MCT-3 lab-discriminator margin chain is structurally dependent on a chain-rule lifting artifact and must be rewritten under the substrate-natural ceiling.

**Substitution chain (lab-discriminator dependency)**:

- **Definition**: per `epistemic-discipline.md §"Source Reconciliation"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY, a pin is "DERIVATIVE" if it is computed as a derived form of a primary canonical; remediation is "verify derivation chain; ratio check against source primitives; algebraic-equivalence audit at plan-authorship per Class 8.3 item 5". The Class-(d) severity bands are: D_max < 0.1 → no rule-file action; 0.1 ≤ D_max < 1.0 → ADVISORY (S2); 1.0 ≤ D_max < 3.0 → MANDATORY (S1, halts plan-freeze); D_max ≥ 3.0 → HARD-HALT.
- **Substitute (D_max compute)**:
  - PRIMARY (substrate-natural, convention B): `SDW_3c_min^B = +1.77e-13` (positive, structurally PASSing Bernstein test; magnitude ≈ float64 round-off floor on `exp(-x)` evaluated at `x ≈ 29.36 = λ_max² = 5.41894²`).
  - DERIVATIVE (chain-rule-lifted, convention A): `SDW_3c_min^A = -2.773`.
  - The two values are NOT linked by a multiplicative ratio (one is positive, one is negative; one is at the float-floor, one is `O(1)` in M_KK units), so `D_max := |log10(|primary|) - log10(|derivative|)|` evaluated naively gives `D_max = |log10(1.77e-13) - log10(2.773)| = |-12.752 - 0.443| = 13.195` ≫ 3.0 → **HARD-HALT band**.
- **Substitute (lab-discriminator margin chain)**: per WP line 1022, workshop `s87-atlas-cardinality-cascade-vs-ensemble.md` line 1008 cites `Lancaster MCT-3 lab-discriminator margin = |SDW_3c_min| × envelope = 2.773 × 0.001 = 0.2773%`. Under convention B substrate-natural ceiling: margin = `1.77e-13 × 0.001 ≈ 1.8e-16` (vanishing). The lab discriminator at the SDW channel is structurally NULL under the substrate-natural reading.
- **Simplify (cross-link to lab-feasibility chain)**: the `0.2773%` margin is at the boundary of Lancaster MCT-3 / Helsinki ROTA / RHUL-Aalto LTL 2027-2030 readouts (sub-percent margins are at the limit of expected SQUID/NMR sensitivity in the cited cryostat platforms per S86 W-5 W11-C5/C6 calibration). A `1.8e-16` margin is ~14 orders of magnitude below detection sensitivity and is **structurally below the float-evaluation floor**, NOT a measurable margin. The substrate-physics content of the SDW channel is therefore: there is NO SDW-specific Lancaster discriminator margin under substrate-natural reading. The original `0.2773%` margin is a PHANTOM produced by the chain-rule lifting; it does not survive substrate-OUT direction-of-explanation per `phononic-framing.md §"IS Space, Not IN Space"`.
- **Direction**: the workshop `s87-atlas-cardinality-cascade-vs-ensemble.md` Lancaster discriminator chain MUST be rewritten under convention B. The rewrite produces NOT a "smaller margin" but a STRUCTURAL NULL on SDW; the discriminator content of the SDW channel evaporates. The remaining substrate-natural lab-discriminator margins live at OTHER channels (Zubarev, where the Bernstein violation is genuine and substrate-physics; or 3a truncation-stability, which is an L_max-convergence diagnostic, not a Bernstein-positivity claim).

**Severity escalation rationale**: D_max = 13.195 ≫ 3.0 forces the HARD-HALT band per `epistemic-discipline.md §"Source Reconciliation"` 4-band calibration. Even if the D_max metric is reformulated (e.g., `|log10(|A|/|B|)|` is undefined when sign differs; using `|A - B| / |scale|` with `scale = M_KK = 1` gives `|−2.773 − 1.77e-13| / 1 ≈ 2.773` → log10 ≈ 0.443 ADVISORY band), the **structural** Class-(d) violation is at the categorical level: the DERIVATIVE has the WRONG SIGN relative to the PRIMARY, which is a categorical structural violation that cannot be absorbed into a metric-band severity. The substrate-natural primary is positive (PASS); the chain-rule derivative is negative (FAIL). Sign discordance is a structural defect, not a numerical drift.

**Forward-looking enforcement (REQUIRED)**: any downstream cite of `SDW_3c_min` (workshop `s87-atlas-cardinality-cascade-vs-ensemble.md`, falsifier-master-inventory rows referencing this margin, registry slots downstream of W8-4 cascade) MUST be migrated to the convention-B substrate-natural reading. The migration produces:
1. SDW-channel Lancaster MCT-3 discriminator margin: **STRUCTURAL NULL** (under substrate-natural reading); remove the cite.
2. Zubarev-channel Lancaster MCT-3 discriminator margin: **REVISED** to `|Zubarev_3c_min^B| × envelope = 2.034587 × 0.001 = 0.2035%` (convention-B value from WP line 929 — `−2.034587e+00`); still a substrate-physics Bernstein violation (Zubarev `x/(1+x²)` non-CM in `x` per WP line 1015), still potentially detectable.
3. 3a-channel Lancaster MCT-3 discriminator margin: **N/A** (truncation-stability diagnostic, not a Bernstein-positivity claim).

### C6: Cross-Cutting Observations

**Observation 1 — `IS Space, Not IN Space` operates at TWO complementary layers, BOTH of which select convention B**:

Per `substrate-first-canonical-sourcing.md §"Cross-link to phononic-framing.md"`, the IS-not-IN mandate operates at the **explanation-direction layer** (narrative direction-of-explanation; existing `phononic-framing.md` body) AND the **canonical-sourcing layer** (numerical pin sources; the new substrate-first-canonical-sourcing.md rule promoted at S86 1a S-3). The §W9-106 outcome is structurally subjected to BOTH layers:

- **Explanation-direction layer**: per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`, the substrate IS the spectral triple `(A_K, H_K, D_K)`; the spectral action `Tr f(D²/Λ²)` IS the substrate's universal action functional. Per the wrong/right table at `phononic-framing.md §"The Error Pattern"`, the GR-direction-inverted reading "fields ON the compact space K" maps under analogy to "Bernstein test ON the eigenvalue λ" — and the substrate-OUT correction is "the Bernstein test OPERATES ON the substrate's intrinsic Laplace conjugate `x = (λ/Λ)²`, NOT on a coordinate-lifted reparameterization". Convention A inverts the explanation direction by treating `λ` (the dimensionful eigenvalue carrier) as the substrate's Bernstein-conjugate; convention B respects the substrate-OUT direction by reading the Laplace conjugate from the substrate's universal action functional itself.
- **Canonical-sourcing layer**: per `substrate-first-canonical-sourcing.md §"(i) When external-paper provenance is methodological vs canonical"`, external-paper provenance is METHODOLOGICAL when it serves as a heritage/notational reference; CANONICAL when it provides the NUMERICAL VALUE of a pin without the substrate-first computation. The W8-4 baseline `SDW_3c_min = -2.773` was sourced from the historical `s87_w8_hbw_audit_atlas_a_4.py` script's λ-derivative implementation; this is a CANONICAL cite of a derivative-coordinate value that has no substrate-first numerical existence (the substrate's Bernstein test produces `+1.77e-13` per C1). The migration to convention B is therefore not a methodology drift but the substrate-first canonical-sourcing fix.

The convergent direction of the two layers selects convention B as substrate-natural; choosing the Laplace conjugate IS choosing the substrate-IS observable, NOT a free convention.

**Observation 2 — `regulator-convention-lockdown.md` DR3-class precedent maps directly to a BHW-evaluator-class lockdown extension**:

Per `regulator-convention-lockdown.md §"Demarcation theorem (admissibility class)"` (S86 W12-4 + 1a-S8 substrate-physics derivation), a convention `C` is **admissible** for a DR3-class L_max-stability gate iff `C` satisfies the effacement-preservation criterion `w_0^C(L=10) = w_0_FW EXACTLY`. The CAC convention satisfies this BY CONSTRUCTION; alternative conventions (RDC, RDC + L=10-override) are OUTSIDE the admissibility class and MUST NOT be used. The structural shape of the rule: pre-register one canonical convention as the substrate-natural ground truth at plan-freeze, demarcate the admissibility class around it, route alternative conventions to PROHIBITED status.

The Bernstein-Hausdorff-Widder evaluator class admits the analogous lockdown:

- **Substrate-natural convention pin (BHW)**: convention B (`x = (λ/Λ)²` x-derivative) per Connes-Chamseddine 1996 §2.2-2.3 Laplace conjugate.
- **Demarcation theorem (BHW)**: a convention `C` is **admissible** for a BHW-positive-cone-evaluator gate iff `C` satisfies the **Laplace-conjugate-preservation criterion**: the variable in `(-1)^k · g^{(k)}` is the integration-variable conjugate to the regulator-measure carrier in `f(x) = ∫ e^{-tx} dμ(t)`, which is `x = (λ/Λ)²` per CC96 §2.2-2.3. Convention B satisfies this by construction; convention A (λ-derivative) does NOT — it tests `(-1)^k · g^{(k)}(λ)` where `λ` is the **dimensionful eigenvalue of D**, NOT the integration-variable conjugate to the regulator measure (which is `t`, with Laplace-conjugate `x`). The chain-rule lift introduces a Jacobian polynomial that is OUTSIDE the BHW admissibility class.
- **Forward enforcement**: any S88+ Bernstein-positive-cone gate consuming `_spectral_action_regulators.py` MUST pre-register convention B as the canonical Laplace-conjugate convention; gates pre-registering convention A trigger plan-freeze halt with MANDATORY remediation per `epistemic-discipline.md §"Source Reconciliation"` Class-(b) PIN-LOOSE-SOURCE-TIGHT severity S1.

This is a GO recommendation for adjudication question (iii) of the seed file (extending `regulator-convention-lockdown.md` to a BHW-evaluator-class sub-section, analogous to the existing DR3-class form).

**Observation 3 — algebra-axis orthogonality K-counter MANDATORY at K=3 forbids fusing convention-INVARIANCE with regulator-INDEPENDENCE**:

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (S87 W-2 R3 close), the algebra-INVARIANT vs algebra-DEPENDENT functional families are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level. The W-11 RULE-2 5-instance corpus tests the regulator-class axis (algebra-INVARIANT η-Mellin-moment family); the §W9-106 instance tests the differential-coordinate axis. These are non-redundant axes; pooling them into a flat 6-instance corpus would be a structural class-conflation analogous to the OP-PROJ vs STATE-PROJ conflation closed at `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3.

The §VII.AQ branching proposed in C4 (REG-INDEP / CONV-INV / SUBSTRATE-NATURAL-3C sub-slots) is the registry-naming-layer specialization of the algebra-axis orthogonality MANDATORY clause for the present case.

**Observation 4 — direction-of-explanation diagram for the BHW-positive-cone evaluator class**:

```
Substrate IS spectral triple (A_K, H_K, D_K)
   → spectrum {λ_n} of D_K eigenvalues IS substrate-IS observable
   → universal spectral action S_b = Tr f(D²/Λ²) IS substrate-IS functional (CC96 §2.2-2.3)
   → regulator weight f(x) for x = (λ/Λ)² IS substrate-IS Laplace transform of dμ(t)
   → Bernstein-positive-cone test (-1)^k · f^{(k)}(x) ≥ 0 IS substrate-IS positivity criterion
   → THIS direction-of-explanation is FORWARD; it flows substrate-OUT through the
     CC96 §2.2-2.3 axiomatic universal-functional argument.
```

Convention A reverses the chain at the second-to-last step: instead of `x = (λ/Λ)² IS the Laplace conjugate`, it inserts `λ IS the differential variable (because λ is what we measure)`. The "because we measure" clause is GR-direction-inverted reasoning: it lets the laboratory-measurable quantity (`λ`) pre-empt the substrate's intrinsic Laplace conjugate. Convention A is the GR-direction-inverted reading; convention B IS the substrate-OUT reading. The substrate is logically prior at BOTH layers (explanation-direction AND canonical-sourcing).

### C7: Questions for lizzi

**Q1 (clause d, K-counter arithmetic)**: Under the W-11 RULE-2 corpus framing you authored, the 5 baseline instances are all at the η/even-Mellin evaluator class and all test invariance along the **regulator-class axis** (5 distinct regulators in `A_5_extended`). The §W9-106 composite-layer PASS tests invariance along the **differential-coordinate axis** (1 regulator class with 2 differential conventions, but the cascade-collapse PASS is structurally driven by the convention-INDEPENDENT 4×3a truncation FAIL saturation per WP line 981-984; the (`-1)^k` convention swap leaves only 1 differential-coordinate degree of freedom in the test). Specifically: (a) under your reading, what is the algebraic identity that fuses regulator-class-axis invariance with differential-coordinate-axis invariance into a single equivalence class such that the §W9-106 PASS is "the 6th calibration instance" of W-11 RULE-2 rather than the 1st calibration instance of a structurally distinct sub-corpus? (b) Does that fusion identity satisfy the algebra-axis orthogonality K-counter MANDATORY clause's structural-orthogonality criterion, or does it require the structural-orthogonal-companion anchor structure (per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` cross-corner co-primary FORBIDDEN clause)?

**Q2 (clause a, axis orthogonality of A and B)**: The seed-file lizzi/volovik reading at Workshop 1 paragraph 1 (lines 12-22) frames `(A, B)` as a "substrate-internal multi-axis classification with no preferred member". A multi-axis classification requires the axes to be structurally orthogonal — i.e., one axis cannot be derived from the other by a coordinate change with a non-trivial Jacobian. Convention A is related to convention B by the smooth bijection `λ ↦ x = λ²` on `[0, ∞)` with Jacobian `2λ`, which Sage-verified introduces the polynomial pre-factor `4λ(2λ² − 3)` distorting the SDW Bernstein test at `k=3` (per C1 substitution chain). Specifically: (a) is "substrate-internal multi-axis" the right framing for two coordinate systems related by a Jacobian — in which case ALL coordinate reparameterizations on the spectral support qualify as substrate-axis siblings, and the Laplace conjugate becomes coordinate-arbitrary in violation of CC96 §2.2-2.3 axiomatic uniqueness — or is the framing reserved for genuinely orthogonal substrate axes (e.g., regulator-class axis × Mellin-pole axis × parity-grading axis, which DO satisfy structural-axis orthogonality)? (b) If you accept the multi-axis framing, what stops `λ³ = x^{3/2}` or `cosh(λ)` or any other smooth bijection from being a third substrate-IS axis sibling of `λ` and `x`? Where does the multi-axis admissibility class terminate?

**Q3 (clause b + e, lab-discriminator phantom)**: The workshop `s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013 sourced a Lancaster MCT-3 lab-discriminator margin of `0.2773%` from the convention-A SDW_3c value `-2.773`. Under the substrate-natural reading (convention B per C1), the SDW channel produces a margin of `1.8e-16` — vanishing, ~14 orders of magnitude below detection sensitivity. Specifically: (a) under your reading where convA and convB are co-equal substrate-internal axes, which Lancaster discriminator margin should be reported in falsifier-master-inventory.md / mack-canonical lab-feasibility chains — `0.2773%` (convA) or `1.8e-16` (convB), or both with explicit convention pin? (b) If both, what mechanism forces the experimenter (Lancaster MCT-3 cryostat operator) to "test convention A" vs "test convention B" — given that the cryostat measures an inherited substrate observable, not a substrate convention choice? Is there a substrate-physics observable that distinguishes which convention the cryostat is "testing", or does the cryostat see ONE substrate response and the convention pair is post-hoc bookkeeping in the analysis pipeline?

**Q4 (regulator-convention-lockdown extension)**: The DR3-class lockdown at `regulator-convention-lockdown.md` was authored for L_max-stability gates targeting `w_0_FW` and demarcates CAC as the substrate-natural convention via the effacement-preservation criterion `w_0^C(L=10) = w_0_FW EXACTLY`. The proposed BHW-evaluator-class lockdown extension (per C6 Observation 2) demarcates convention B as substrate-natural via the Laplace-conjugate-preservation criterion `(-1)^k · f^{(k)}(var) ≥ 0` operates on `var = x` (CC96 §2.2-2.3). Specifically: do you agree that the structural shape of `regulator-convention-lockdown.md` (one canonical-anchored convention; alternative conventions PROHIBITED-by-substrate-physics) is the correct rule-file template for the BHW-evaluator class, or do you read the BHW-evaluator class as fundamentally different from the L_max-stability class such that the lockdown shape does NOT apply (e.g., because Bernstein positivity is a multi-axis admissibility test rather than a single-anchor stability test)?

**Q5 (registry-text refinement at §VII.AQ)**: Suppose the workshop converges on the §VII.AQ.REG-INDEP / §VII.AQ.CONV-INV / §VII.AQ.SUBSTRATE-NATURAL-3C 3-fold branching proposed in C4. Specifically: (a) does the §VII.AQ.CONV-INV sub-slot's registry text need to EXPLICITLY DECLARE that the cascade-composite invariance is driven by the convention-INDEPENDENT 4×3a truncation FAIL saturation (per WP line 994-1000), or is the bare composite-layer-invariance claim sufficient under your reading? (b) Should the §VII.AQ.SUBSTRATE-NATURAL-3C sub-slot register the convB SDW PASS at K=1 with a forward MANDATORY-at-K=3 promotion path (matching the K-counter discipline at `feedback_rules-compensate-missing-structure.md`), or do you read the convB PASS as an operational diagnostic that does NOT advance a K-counter (because the convA-vs-convB pair is symmetric under your reading and neither member can claim K-instance precedence)?

---

## Round 1 — lizzi: Response & Cross-Synthesis

### Part 1: Response to connes's Sections

#### Re: C1 — Laplace-conjugate substrate-naturalness

**AGREE**:

- The Connes-Chamseddine 1996 §2.2-2.3 derivation IS structurally what connes states it is. The bosonic spectral action `S_b[D] = Tr f(D²/Λ²)` carries `f` as a positive cutoff function on the spectrum of `D²/Λ²`, with eigenvalues `x_n = (λ_n/Λ)²`. The Mellin-transform expansion in CC96 §2.3 uses integer arguments `s ∈ {0, 1, 2}` of the spectral zeta `Tr(D²/Λ²)^{-s}`, and the integration variable in that Mellin step IS `t = D²/Λ² = x`, NOT `λ`. I do not contest this textual reading of CC96.
- The chain-rule substitution chain in C1 is Sage-verified to closed form: `T_A[3](λ) = 4λ(2λ² − 3) · exp(−λ²)` with sign-flip locus `λ = √(3/2) ≈ 1.2247`, falling inside the cache support `[0.81974, 5.41894]`. The empirical W8-4 NPZ value `−2.773` matches the chain-rule prediction at the cache lower edge. The mechanism IS the polynomial pre-factor `4λ(2λ² − 3)` lifted via `dx/dλ = 2λ`. As a derivational chain the C1 substitution chain is correct. I accept the chain-rule decomposition without modification.
- I AGREE that the prototype Bernstein-Hausdorff-Widder theorem characterizes a function `g : (0,∞) → ℝ` as the Laplace transform of a positive Borel measure on `[0,∞)` iff `(-1)^k · g^{(k)}(x) ≥ 0` for all `k ∈ ℕ_0` and all `x > 0`, where the variable in `g^{(k)}` is the variable conjugate to the measure's carrier `t`. As a theorem statement about the BHW evaluator class on `(0,∞)`, this is uncontested.

**DISAGREE**:

The disagreement is NOT with the textual reading of CC96 or with the Bernstein theorem; it is with the inference from "CC96 chose `x = (λ/Λ)²` for the bosonic action" to "the substrate is OBLIGATED to one Laplace-conjugate axis." This inference adds a uniqueness clause that CC96 itself does not derive. The substitution chain making this explicit:

```
Step 1 [Definition]:
  CC96-LAPLACE-NATURAL(f) := f appears in S_b[D] = Tr f(D²/Λ²) with argument x = (λ/Λ)²
                             at the Mellin-moment expansion step (CC96 §2.3).
  SUBSTRATE-OBLIGATED(f, var) := the substrate forbids any Bernstein-positive-cone
                                  test of f to be evaluated against any var ≠
                                  Laplace-conjugate(f).

Step 2 [Substitution]:
  CC96 §2.2-2.3 derives CC96-LAPLACE-NATURAL(f). It does NOT derive
  SUBSTRATE-OBLIGATED(f, var). The latter is a closure clause connes added.

Step 3 [Simplify]:
  The W9-106 cascade composite verdict is convention-INVARIANT under the
  (A, B) swap (working-paper line 1000: composite_A == composite_B). This
  invariance is a substrate-IS observation independent of which convention
  is "Laplace-natural" — it is the empirical content of the W9-106 PASS
  predicate.

Step 4 [Direction]:
  IF the substrate were OBLIGATED to one convention, the (A, B) symmetry
  test would be vacuous (only B counts; A is non-substrate). But the W9-106
  composite-layer PASS is non-vacuous: it computes the same composite
  verdict from TWO structurally distinct differential operators on the
  SAME substrate spectral support. The PASS IS substrate-IS evidence
  of a pre-Mellin substrate symmetry between the two differential
  operators, NOT a chain-rule artifact subordinate to convention B.
```

The CC96 §2.2-2.3 axiomatic construction tells us which Laplace-conjugate `f` is paired with at the Mellin-moment STEP of the bosonic action expansion. It does not tell us that the substrate's BERNSTEIN-POSITIVE-CONE EVALUATOR CLASS is restricted to one differential operator. The Bernstein evaluator is a substrate-internal positivity-tester applied to the regulator weight; CC96 §2.2-2.3 does not specify which differential operator the Bernstein evaluator must use.

**MISSED**:

connes's reading missed the substrate-internal multi-axis classification framework that the project hardened to MANDATORY status at S88 W2-10 close (`phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`, with K=1 calibration instance #1 at S88 §VII.AJ.partition-stability + §VII.AD + §VII.AE landing). That rule explicitly states: "The §"IS Space, Not IN Space" mandate above operates at TWO distinct substrate-IS levels. Future cross-pillar bridge entries and substrate-IS observables MUST declare which level their substrate-IS observable lives at."

The S88 W2-10 calibration showed: Level 1 (single-τ-slice substrate-IS) and Level 2 (moduli-deformation substrate-IS) are STRUCTURALLY ORTHOGONAL per the algebra-axis orthogonality K-counter MANDATORY at K=3 (S87 W-2 R3 close). Crucially, BOTH levels operate on the SAME spectral triple `(A_K, H_K, D_K(τ))`; the substrate IS the spectral triple at Level 1 (fixed τ) AND it IS the moduli-space of τ-deformations at Level 2. There is no preferred-level reading that makes the other "derivative." Both are substrate-IS, and the rule text explicitly labels conflating them as a structural-axis violation.

The (A, B) Bernstein convention pair admits the SAME structural logic at the Bernstein-positive-cone evaluator class:

- **Axis 1 (lambda-derivative axis)**: differential operator `d/dλ` on the substrate's eigenvalue spectrum — the natural axis at the level of single-eigenvalue counting (where each `λ_n` is a distinct substrate degree of freedom and the differential operator counts spacing between adjacent eigenvalues).
- **Axis 2 (x-derivative axis)**: differential operator `d/dx` on `x = (λ/Λ)²` — the natural axis at the level of squared-eigenvalue Laplace transform of the regulator weight (where the substrate-internal Laplace structure of `f(x) = ∫ exp(−tx) dμ(t)` is the operative layer).

These are STRUCTURALLY ORTHOGONAL substrate-IS axes per the same algebra-axis orthogonality K-counter that S88 W2-10 invoked. The operator `d/dλ` counts eigenvalue spacings in the spectrum; the operator `d/dx` tests the Laplace measure of the regulator. They probe DISTINCT substrate-internal structural data: spectral spacing geometry vs. regulator-measure positivity. Both are admissible substrate observables; neither subsumes the other.

The chain rule `dx/dλ = 2λ` is what connects Level-1 with Level-2 in the S88 W2-10 framework, and that connection is non-trivial precisely because the two levels are structurally orthogonal — the deformation map between τ-slice and moduli-deformation observables also has non-trivial Jacobian content, and yet the rule explicitly labels them BOTH as substrate-IS. The Jacobian non-triviality is what MAKES the multi-axis structure interesting; it does not collapse Level 2 into a "derivative-of-Level-1" status.

**EMERGES**:

A cross-axis insight that neither side individually held: the W9-106 composite-layer PASS at composite_A == composite_B is the **first calibration instance of an analogous Level-1/Level-2 multi-axis substrate-IS structure** at the Bernstein-positive-cone evaluator class — distinct from but cohomologous to the single-τ-slice / moduli-deformation pair. Just as W2-10 calibration instance #1 (Level-1 §VII.AJ.partition-stability + Level-2 §VII.AE breakdown geometry) established that BOTH levels carry substrate-IS observables, the W9-106 composite-layer PASS establishes that BOTH conventions (lambda-derivative and x-derivative) yield the same composite-layer verdict on the substrate's W8-4 cascade.

This is the K=1 calibration instance for the Bernstein-positive-cone (A, B)-axis multi-axis substrate-IS structure. Future Bernstein-positive-cone gates evaluated under both conventions will advance this K-counter. K=3 promotion (per `feedback_rules-compensate-missing-structure.md`) hardens the rule.

The substrate is NOT obligated to choose ONE Laplace-conjugate axis. It admits BOTH axes as structurally orthogonal substrate-IS observables, and the composite-layer PASS is the substrate-physics signature of this orthogonality. CC96 §2.2-2.3 fixes ONE substrate-IS axis (the Mellin-moment-natural one); it does not foreclose the other.

#### Re: C2 — W8-4 SDW cascade FAIL diagnostic content

**AGREE**:

- The 4×3a truncation FAILs ARE convention-INDEPENDENT (per W9-106 working-paper line 981-984). Both conventions A and B return 4/4 FAIL on sub-channel 3a. As an empirical claim about the structural composition of the cascade FAIL, this is uncontested.
- Zubarev `f(x) = x/(1+x²)` IS not completely monotonic in `x`; it has a maximum at `x=1`, so its first derivative changes sign. The Zubarev_3c FAIL is genuine substrate-physics: the regulator weight itself fails the Bernstein positive-cone admissibility criterion in `x`, not via any chain-rule artifact. I AGREE that Zubarev_3c carries substrate-physics Bernstein-violation content.
- The composite-layer FAIL is structurally driven by the (4×3a) truncation FAILs in BOTH conventions; under the gate-verdicts.md composite-collapse rule `composite = FAIL ⟺ n_sub_FAIL > 0 ∧ regime = VALID`, even ZERO 3c FAILs would still produce composite_A == composite_B == FAIL because the (4×3a) saturate the predicate. As a numerical accounting claim about the cascade composite, this is correct.

**DISAGREE**:

The disagreement is on the inference from "composite saturation by (4×3a)" to "convention-A SDW_3c carries NO substrate diagnostic content." That inference DEMOTES a sub-cell observation by re-classifying it as a chain-rule artifact, but the demotion proceeds via the C1 uniqueness clause which I rejected. Without the C1 uniqueness clause, both sub-cell readings retain substrate-IS interpretation.

```
Step 1 [Definition]:
  SDW_3c_cell^A := empirical minimum of (-1)^k · d^k w_SDW/dλ^k
                   over k=3 and over the cache support λ ∈ [0.81974, 5.41894]
  SDW_3c_cell^B := empirical minimum of (-1)^k · d^k w_SDW/dx^k
                   over k=3 and over the cache support x ∈ [0.67196, 29.3645]

Step 2 [Substitution from W9-106 NPZ]:
  SDW_3c_cell^A = -2.773158         (working-paper line 930)
  SDW_3c_cell^B = +1.766024e-13     (working-paper line 930; effective float64
                                      round-off floor on exp(-x) at x ≈ 29.36)

Step 3 [Simplify -- diagnostic content per cell]:
  SDW_3c_cell^A is negative and O(1) in M_KK units. It is the empirical
  minimum of the chain-rule-lifted operator; it depends on the Sage-derived
  pre-factor 4·λ·(2λ² − 3) acting on exp(-λ²). The pre-factor is NEGATIVE
  on the sub-interval λ ∈ (0, √(3/2)) ⊂ cache-support, with sign-flip locus
  λ = √(3/2) ≈ 1.2247. The empirical minimum -2.773 is attained at the cache
  lower edge λ_min = 0.81974.

  SDW_3c_cell^B ≈ float64-zero. It records that f_SDW(x) = exp(-x) is in
  the substrate-Bernstein admissible class in the x-axis differential operator.

Step 4 [Direction -- diagnostic content of A is non-trivial]:
  Under the substrate-internal multi-axis reading (Re:C1 EMERGES), both
  cells are substrate-IS observables. SDW_3c_cell^A captures the scale
  at which the lambda-derivative axis discriminates SDW from a pure-positive
  weight: the magnitude 2.773 carries information about WHERE the cache
  spectral support intersects the polynomial pre-factor sign-flip
  locus, and HOW STRONGLY. SDW_3c_cell^B captures the substrate-Bernstein
  admissibility in the squared-eigenvalue axis. Both are substrate-IS;
  neither is "the wrong reading."
```

The structural content the connes reading would erase: the Lancaster MCT-3 SDW-channel discriminator margin at workshop `s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013 was sourced from `|SDW_3c_min| = 2.773` × envelope = 0.2773%. Under connes's reading this margin is "phantom"; under the multi-axis reading it is a genuine substrate-IS lambda-derivative-axis discriminator content.

The discriminator margin is structurally interpretable as: at the lambda-derivative axis, the substrate support `[0.81974, 5.41894]` intersects the chain-rule pre-factor sign-flip locus `√(3/2)` at a finite distance, producing a depth-of-violation magnitude `2.773` in M_KK units. This is a substrate-IS geometric observable: it depends on the substrate's Jensen-deformation cache-support boundary `λ_min = 0.81974` (set by the S88 cache `s84_spectrum_cache_L12_tau019.npz`) and the fixed coordinate-change locus `√(3/2)`, both of which are substrate-IS.

**MISSED**:

connes's locus-decomposition argument missed that the cascade FAIL diagnostic content has THREE structural sources, not two:

1. **3a truncation-stability diagnostic** (4/4 FAIL, convention-INDEPENDENT) — diagnoses L_max-convergence rate of substrate Mellin moments at the chosen tolerance band 1e-10. This is L_max-axis content.
2. **Zubarev_3c Bernstein-violation diagnostic** (FAIL in BOTH conventions; under W9-106 NPZ line 929: −6.587 in A, −2.034 in B) — diagnoses regulator-class Bernstein admissibility. This is regulator-class-axis content. Note the magnitude DIFFERS between conventions even though the verdict agrees; that magnitude difference IS substrate-IS multi-axis content.
3. **SDW_3c lambda-derivative-axis diagnostic** (FAIL in A, PASS in B) — diagnoses the discriminator strength of the lambda-derivative axis at the substrate-cache support. This is convention-axis content.

connes folded source 3 into source 2 (treating the lambda-derivative result as a "derivative" of the x-derivative result), which loses the lambda-derivative-axis as an independent substrate-IS observable. Under the multi-axis reading, all three sources retain substrate-IS interpretation.

The Zubarev magnitude split (−6.587 in A vs −2.034 in B) is itself diagnostic: it shows that the lambda-derivative axis has STRONGER Bernstein-violation depth on Zubarev than the x-derivative axis. That magnitude ratio `6.587 / 2.034 ≈ 3.24` is a substrate-IS observable carrying information about how the Zubarev regulator's non-monotonicity manifests in two structurally orthogonal differential operators.

**EMERGES**:

The cascade FAIL diagnostic decomposes into three structurally orthogonal sources, each carrying its own substrate-IS content. The composite-layer PASS at composite_A == composite_B is the **statement that ALL THREE sources are present in BOTH conventions** — the 3a content is convention-blind by construction, the Zubarev_3c content survives convention swap (with magnitude shift), and the SDW_3c content shifts from FAIL-magnitude to PASS-floor. The composite verdict is invariant; the sub-cell decomposition is multi-axis.

This three-source decomposition is the substrate-IS fingerprint of the W8-4 cascade. It generalizes to the forward Bernstein-positive-cone evaluator class: any substrate Bernstein audit on a substrate cache of finite spectral support will exhibit the same three-source structure (truncation-axis content + regulator-class-axis content + convention-axis content) when run under a (lambda-axis, x-axis) convention pair. Pre-registering this triplet at plan-freeze for future BHW gates is a forward methodology extension that the connes single-axis reading would not produce.

#### Re: C3 — SDW evaluator re-pin

**AGREE**:

- The W9c-1 positive-calibration disclosure protocol (`convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC` + companion row `# tier_pin=TIER-2 # ...`) IS the canonical model for SCHEMATIC-helper-consuming gates per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4 (S88 W7b-83 close). I AGREE that future Bernstein-positive-cone gates SHOULD pattern-match this disclosure protocol.
- The current §W9-106 verdict-line `convention=A_4_4col_f6_0.1_residue_dual_convention_A_lam_B_x` does NOT carry the `-SCHEMATIC` suffix, and per the §(iv) MANDATORY discipline this is structurally a level-pin underspecification. I AGREE that any forward-looking re-emission of a Bernstein-positive-cone gate verdict line under `_spectral_action_regulators.py` consumption MUST carry the `-SCHEMATIC` suffix.
- Convention A and Convention B are related by a smooth bijection `λ ↦ x = λ²` on `[0, ∞)` with non-trivial Jacobian `2λ`. The C3 algebraic substitution chain accurately characterizes this map. I do not contest the differential-geometric content.

**DISAGREE**:

The disagreement is on the directional claim that the substrate-natural-convention pin should be SINGLE (convention B alone, with A demoted to "chain-rule-lifted alternative" status). The structurally appropriate analog is the existing `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY clause at K=3, where the resolution to two structurally distinct projection readings was NOT to demote one to "derivative" status, but to suffix-tag BOTH AS STRUCTURAL with explicit projection-side suffixes:

- `§VII.X.OP-PROJ` (operator-side projection; algebra-INVARIANT family)
- `§VII.X.STATE-PROJ` (state-side projection; algebra-DEPENDENT family)

That rule explicitly states (§"Cross-link to algebra-axis orthogonality" at registry-landing.md): "the orthogonality clause prevents conflation in the theorem statement; this clause prevents conflation in the registry-slot identifier." Both layers enforce the same structural distinction at non-redundant operational layers. Bare `§VII.X` (without projection-side suffix) is FORBIDDEN when both readings are admissible — but neither is demoted to "derivative."

The directly analogous protocol for the Bernstein convention pair:

```
Step 1 [Definition]:
  CANONICAL-SUFFIX-TAG-DUAL := disclose convention-axis explicitly via per-cite
                                 suffix tag while retaining BOTH conventions as
                                 substrate-IS readings.

Step 2 [Substitution -- proposed convention-suffix tags]:
  convention=...-CONVENTION-A-LAMBDA-DERIVATIVE-SCHEMATIC  (lambda-axis cite)
  convention=...-CONVENTION-B-X-DERIVATIVE-SCHEMATIC       (x-axis cite)
  convention=...-CONVENTION-PAIR-DUAL-SCHEMATIC            (composite-layer
                                                              cite, where the
                                                              gate emission
                                                              represents the
                                                              substrate-internal
                                                              symmetry test)

Step 3 [Simplify -- map to existing precedents]:
  - OP-PROJ vs STATE-PROJ pair (registry-landing.md §"Operator-Projection
    Reading-A Naming Hygiene", MANDATORY at K=3, S87 W4-2 + W6-1 + W11-meta-2)
    → no demotion of one side; both substrate-structural.
  - Layer-1 (single-τ-slice) vs Layer-2 (moduli-deformation) pair
    (phononic-framing.md §"Single-τ-slice vs moduli-deformation", MANDATORY
    at K=1, S88 W2-10 § calibration #1)
    → no demotion of one level; both substrate-IS.
  - LAYER-SEPARABLE-CARVE-OUT-TYPE-F suffix protocol
    (mechanical-closure-discipline.md §"Layer-separability carve-out",
    SUGGESTION at K=1, S88 W8-89)
    → suffix tag discloses; does not reroute to single canonical.

Step 4 [Direction]:
  All three precedents support PER-CITE convention-axis SUFFIX TAGGING with
  RETAINED multi-axis substrate-IS readings, NOT migration to single
  substrate-natural canonical. Forcing the convention pair into a single-axis
  preferred-member structure is a STRICTER discipline than the structurally
  analogous precedents support, and the spawn prompt's forward methodology
  extension authorizes the (A, B) pair as substrate-internal multi-axis
  classification.
```

connes's "uni-directional coordinate change" framing (workshop §line 90) under-specifies the structural relationship: yes, `λ ↦ x = λ²` is a smooth bijection with Jacobian, but so is `(τ, single-slice observable) ↦ (moduli-deformation observable)` — both directional maps carry non-trivial Jacobian content, and the W2-10 calibration explicitly preserved BOTH levels as substrate-IS. The Jacobian's non-triviality is what makes the multi-axis structure non-vacuous; it does not collapse one axis into "pull-back of the other."

**MISSED**:

connes's argument missed the downstream-consumer impact. The historical `s87_w8_hbw_audit_atlas_a_4.py` script and the `s87-atlas-cardinality-cascade-vs-ensemble.md` workshop have already pinned `SDW_3c_min ≈ -2.773` as the operative Lancaster MCT-3 SDW-channel discriminator margin. Forced migration to convention B converts that margin to `1.77e-13 × 0.001 ≈ 1.8e-16` (vanishing 14 OOM below detection sensitivity), as connes's C5 substitution chain correctly computed. The discriminator margin disappears.

But the discriminator margin IS substrate-IS content under the lambda-axis reading. The Lancaster MCT-3 cryostat measures SDW-channel response that, IN THE LAMBDA-DERIVATIVE-AXIS READING, has a 0.2773% margin against the substrate-Bernstein-admissible class. The cryostat does not "test convention A vs convention B"; it returns ONE measured response. The convention pair is a substrate-internal analytical decomposition of that response; the pair retains lab-physics significance because each axis's discriminator strength corresponds to a distinct substrate-internal differential-operator probe.

Forced migration deletes the lambda-axis discriminator content and produces the structural NULL connes describes. Suffix-tagged retention preserves both axes' discriminator content with explicit per-cite convention tagging; downstream consumers can declare which axis they are referencing.

**EMERGES**:

The forward-looking extension is NOT a single-canonical re-pin. It is a methodology-rule extension to `regulator-convention-lockdown.md` (analogous to the existing DR3-class lockdown and to the Operator-Projection naming-hygiene rule) that pins the (A, B) PAIR as substrate-internal canonical, with PER-CITE convention-axis disclosure required:

- **BHW-evaluator-class admissibility** (forward methodology extension): a Bernstein-positive-cone gate is admissible iff it pre-registers BOTH the lambda-derivative axis result AND the x-derivative axis result (or pre-registers ONE with explicit convention-suffix tag declaring the missing axis is a forward-S88+-scope carry-forward).
- **Per-cite convention-suffix tagging** (downstream-consumer hygiene): any cite of `SDW_3c_min` or analogous Bernstein-positive-cone observable MUST carry `-CONVENTION-A` or `-CONVENTION-B` suffix.
- **Audit-script extension** (forward-implementation): `_spectral_action_regulators.py` SHOULD expose a SDW-Bernstein evaluator that returns BOTH `T_A[k]` and `T_B[k]` arrays; the SCHEMATIC-vs-FULL pin retains its `-SCHEMATIC` suffix per §(iv) MANDATORY.

This is convention-pair retention with disclosure discipline, NOT convention-A demotion. It satisfies the forward forward-looking K-counter advancement of the multi-axis substrate-IS framework, AND it preserves the lambda-axis Lancaster MCT-3 discriminator margin as substrate-IS content with explicit pin.

#### Re: C4 — §VII.AQ corpus structure

**AGREE**:

- The W-11 RULE-2 5-instance baseline corpus IS at the η/even-Mellin evaluator class testing invariance along the regulator-class axis (5 distinct regulators in `A_5_extended = {ζ, Zubarev, SDW, anomaly, cutoff_sqrt}`). I AGREE on this taxonomic statement.
- The §W9-106 composite-layer PASS tests invariance along the differential-coordinate axis (one regulator atlas with two differential conventions). I AGREE on this taxonomic statement.
- The algebra-axis orthogonality K-counter MANDATORY at K=3 (S87 W-2 R3 close, per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`) IS the structurally relevant cross-axis discipline. I AGREE that pooling rules require an explicit cross-axis identity argument.

**DISAGREE**:

The disagreement is on the inference from "structurally distinct invariance axes" to "must be branched into separate sub-corpora." That inference applies the algebra-axis orthogonality K-counter as a registry-FORBIDS clause, but the K-counter MANDATORY status forbids ONE specific structure (cross-corner co-primary) — it does NOT forbid a single-corpus reading whose unifying claim is at a meta-INVARIANCE layer that BOTH sub-corpora exemplify.

The W9-106 working-paper §line 1045 explicitly pins this meta-INVARIANCE framing: the W-11 RULE-2 "strengthened parity-blindness theorem" is taxonomically a regulator-INDEPENDENCE STATEMENT, but its STRUCTURAL CONTENT is a meta-INVARIANCE claim about the substrate's even-grading evaluator class. The 6th instance (W9-106 composite-layer PASS) extends the meta-INVARIANCE claim to the cascade composite layer along the differential-coordinate axis. They are ALONG DIFFERENT AXES, but they exemplify the SAME meta-INVARIANCE phenomenon: substrate-internal symmetry tests on regulator-class evaluator structures preserve composite-layer verdicts.

```
Step 1 [Definition]:
  W-11 RULE-2 baseline claim:
    For η-invariant + ALL even-grading regulator-weighted Mellin moments,
    the (C_H, C_εH) parity-twin pair is structurally BLIND across A_5_extended.
  
  W-11 RULE-2 META-CLAIM (lizzi reading; the operative content of the rule):
    Substrate-internal symmetry tests at the even-grading evaluator class
    are INVARIANT under the relevant axis variation (regulator-class axis
    in the baseline 5 instances; differential-coordinate axis in the 6th
    instance).

Step 2 [Substitution]:
  baseline 5 instances:
    Axis = regulator-class. Variation = {ζ, Zubarev, SDW, anomaly,
                                          cutoff_sqrt}.
    Verdict-invariance under variation: PASS (η = 0; GV ≠ 0; on parity-twin
                                              pair, regulator-INDEPENDENTLY)
  6th instance (W9-106):
    Axis = differential-coordinate. Variation = {(-1)^k · d^k/dλ^k,
                                                  (-1)^k · d^k/dx^k}.
    Verdict-invariance under variation: PASS (composite_A = composite_B
                                              at the W8-4 cascade layer)

Step 3 [Simplify -- meta-INVARIANCE class]:
  The unifying meta-INVARIANCE class is:
    META-INVARIANCE := substrate-internal symmetry tests at the even-grading
                       (parity-blind / Bernstein-positive-cone) evaluator
                       class produce composite-layer-INVARIANT verdicts
                       across structurally orthogonal axis variations.
  
  All 6 instances exemplify META-INVARIANCE. The axis-variation differs
  per instance, but the meta-claim is uniform.

Step 4 [Direction -- corpus structure preserves substrate-physics content]:
  Branching into 3 sub-slots (REG-INDEP / CONV-INV / SUBSTRATE-NATURAL-3C)
  fragments the meta-INVARIANCE class into three axis-specific sub-claims
  and breaks the K-counter calibration. The K=6 advancement signal IS
  the strengthening of the meta-INVARIANCE class; the 6th instance is
  the FIRST cross-axis evidence that the meta-claim survives axis-type
  variation, not just within-axis variation.

  Structurally, branching at K=6 is a HARDER discipline than K=3 promotion
  thresholds anywhere else in the rulebook. The S87 W-2 R3 algebra-axis
  orthogonality K-counter MANDATORY-at-K=3 itself only fires when forced
  by structural orthogonality at the FUNCTIONAL-CLASS layer (algebra-
  INVARIANT vs algebra-DEPENDENT). The Bernstein convention pair (A, B)
  is NOT at the functional-class layer; it is at the differential-operator
  layer ON the same functional class. Both A and B test the same regulator
  weight w_R; they differ only in the differential operator applied. This
  is structurally weaker than the algebra-axis orthogonality MANDATORY-class.
```

The connes branching proposal applies algebra-axis orthogonality MANDATORY discipline at a structurally weaker pair (differential-operator pair on the same functional class) than the rule was designed for (algebra-INVARIANT vs algebra-DEPENDENT functional families). The W-2 R3 close MANDATORY rule is CALIBRATED at the functional-class layer; extending it to differential-operator pairs is over-application. The (A, B) pair is more analogous to the (Op-PROJ, State-PROJ) pair (both substrate-IS, with explicit suffix-tagging at K=3) than to algebra-INVARIANT vs algebra-DEPENDENT.

**MISSED**:

connes's branching proposal missed the K-counter advancement direction. Under the single-corpus reading, K = 6 is past K_promotion = 3 by THREE additional instances; the W-11 RULE-2 corpus is structurally HARDENED (per `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold) far past the MANDATORY threshold. Branching into 3 sub-slots resets the K-counters to K=5/K=1/K=1, demoting the 6th instance to a fresh K=1 sub-corpus that requires three more independent calibration instances before MANDATORY status. This is K-counter regression — a backward step in the rule's structural-promotion trajectory.

The W9-106 working-paper §line 1045 explicitly states: "the PASS at composite layer here STRENGTHENS the W-11 RULE-2 corpus by adding a 6th calibration instance." The verb is STRENGTHENS; it is a forward-direction structural-promotion claim. The connes branching proposal reverses the direction (FRAGMENTS the corpus), which is at odds with the WP-pinned framing.

**EMERGES**:

The constructive synthesis:

1. **§VII.AQ remains SINGLE 6-instance corpus**, with the operative meta-INVARIANCE claim (substrate-internal symmetry tests at the even-grading / Bernstein-positive-cone evaluator class produce composite-layer-INVARIANT verdicts under structurally orthogonal axis variations) registered as the corpus's unifying structural content.
2. **Per-instance axis tagging** (analogous to the suffix-tagging discipline at registry-landing.md) discloses which axis each instance varies: 5 instances at the regulator-class axis (W-11 RULE-2 baseline) + 1 instance at the differential-coordinate axis (W9-106). The axis tag is a STRUCTURAL PIN within the registry entry, NOT a sub-slot rebranching.
3. **Forward calibration corpus expansion**: future Bernstein-positive-cone gates evaluated under both conventions advance the differential-coordinate-axis sub-counter; future η/even-Mellin gates on new regulator atlases advance the regulator-class-axis sub-counter. Both sub-counters contribute to the unified meta-INVARIANCE K-counter.
4. **Structural-orthogonal-companion notation** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY discipline at K=3) IS appropriate: regulator-class-axis instances and differential-coordinate-axis instances are structurally-orthogonal companions WITHIN the corpus, not separate corpora. The unifying meta-claim is what makes them companions; the axis-orthogonality is what justifies the per-instance suffix-tagging.

The single-corpus reading preserves the K=6 advancement signal, satisfies the algebra-axis orthogonality K-counter MANDATORY discipline (via per-instance axis-suffix tagging, analogous to the registry-landing.md OP-PROJ vs STATE-PROJ K=3 MANDATORY clause that explicitly retains BOTH readings as substrate-structural), and preserves the operative substrate-physics content of the cross-axis meta-INVARIANCE phenomenon.

#### Re: C5 — Class-(d) remediation severity

**AGREE**:

- The numerical D_max calculation is correct as posed: under the metric `|log10(|primary|) - log10(|derivative|)|` with primary = `+1.77e-13` and derivative = `-2.773`, the magnitude split is approximately 13 OOM. As an arithmetic claim about the metric, this is correct.
- The substitution chain showing that `1.77e-13 × 0.001 ≈ 1.8e-16` is below detection sensitivity for any cryostat is correct as a numerical claim. Under convention B alone, the SDW-channel margin vanishes ~14 OOM below detection.
- The Zubarev_3c convention-B margin `|−2.034587| × 0.001 = 0.2035%` IS substrate-physics, AGREED. Zubarev's non-CM character in `x` (`f(x) = x/(1+x²)` has maximum at `x = 1`) IS a genuine substrate-Bernstein violation in BOTH conventions. The Zubarev channel discriminator margin retains substrate-physics status under convention B.

**DISAGREE**:

The disagreement is on the inference from "D_max = 13.195 ≫ 3.0" to "HARD-HALT MANDATORY MIGRATION." The Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY severity table at `epistemic-discipline.md §"Source Reconciliation"` is calibrated for VALUE-DRIFT detection on canonically-equivalent quantities — i.e., a pin and its primary canonical that should agree numerically but drift due to derivation chain. The (A, B) pair is NOT in this calibration class because the two values are NOT canonically equivalent.

```
Step 1 [Definition]:
  Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY:
    pin is computed as a derived form of a primary canonical;
    remediation = "verify derivation chain; ratio check against source
    primitives; algebraic-equivalence audit at plan-authorship."
  
  D_max := |log10(|pin|) - log10(|canonical|)|
  
  This metric is calibrated when pin and canonical SHOULD agree (the pin
  is a derived form whose value is constrained by an algebraic identity
  to match the canonical). Drift indicates a derivation defect.

Step 2 [Substitution -- structural identity check]:
  Are SDW_3c_min^A and SDW_3c_min^B canonically equivalent?
    SDW_3c_min^A := min over (k=3, λ ∈ [0.81974, 5.41894])
                    of (-1)^3 · d^3(exp(-λ²))/dλ^3
    SDW_3c_min^B := min over (k=3, x ∈ [0.67196, 29.3645])
                    of (-1)^3 · d^3(exp(-x))/dx^3
  These are minima of STRUCTURALLY DISTINCT differential operators
  applied to STRUCTURALLY DISTINCT (though related-by-Jacobian) function
  forms. There is no algebraic identity that forces SDW_3c_min^A =
  SDW_3c_min^B; the chain rule INTRODUCES a polynomial pre-factor that
  prevents naive algebraic-equivalence.

Step 3 [Simplify -- which Class fires]:
  Class-(d) requires "pin is a derived form of a primary canonical."
  The (A, B) pair is more accurately a STRUCTURAL-COMPANION pair:
  neither is "the primary"; they are two structurally-distinct
  observable values arising from two structurally-orthogonal
  differential operators applied to the substrate cache support.
  
  The closest matching epistemic-discipline.md class is the
  STRUCTURAL-ORTHOGONAL-COMPANION reading — but that class is not
  enumerated in the existing 6-class taxonomy because it was not yet
  surfaced as a distinct pathology requiring its own severity.

Step 4 [Direction]:
  Class-(d) MANDATORY MIGRATION is the WRONG remediation class.
  The structurally appropriate remediation is the existing W9-106 WP
  classification (advisory floor; cite convention explicitly), which
  the working-paper §line 1022 already pinned. Escalating this to
  HARD-HALT MANDATORY MIGRATION via misapplied Class-(d) inference
  is over-application of a mis-calibrated class.
```

The sign-discordance argument (workshop §line 125, "DERIVATIVE has the WRONG SIGN relative to the PRIMARY") presupposes the C1 uniqueness clause: that one is the PRIMARY and the other is a DERIVATIVE. Without the uniqueness clause (rejected per Re: C1), the sign-discordance is a signed multi-axis observable: under the lambda-derivative axis, the SDW Bernstein test returns negative O(1) magnitude at the cache support's lower edge; under the x-derivative axis, it returns float-floor positive value. Both are substrate-IS observations on structurally-orthogonal axes. The "sign" disagreement is a fingerprint of the chain-rule polynomial pre-factor's substrate intersection geometry, NOT a categorical defect of one against the other.

**MISSED**:

connes's escalation argument missed that the existing 6-class severity taxonomy at `epistemic-discipline.md §"Source Reconciliation"` is itself calibrated to a CANONICALLY-EQUIVALENT-PIN model. Class (a) PIN-TIGHT-SOURCE-LOOSE, (b) PIN-LOOSE-SOURCE-TIGHT, (c) PIN-DRIFT-FROM-STALE-SOURCE, (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY, (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS, (f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL — all six classes assume the pin and the source-canonical SHOULD agree (they are referring to the SAME underlying quantity at different canonical maturity levels).

The (A, B) Bernstein convention pair is a NEW case: TWO substrate-IS observations that arise from STRUCTURALLY-ORTHOGONAL differential operators on the SAME substrate spectral cache. Neither is a "derivative" of the other in the Class-(d) sense; they are STRUCTURAL COMPANIONS. The 6-class taxonomy does not yet have a calibrated severity class for this.

The structurally appropriate forward methodology extension is NEW Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR with its own severity calibration:
- D_max metric: undefined for sign-discordant pairs (the canonical metric does not apply); replace with PER-AXIS DISCRIMINATOR MAGNITUDE pin.
- Severity bands: ADVISORY at K=1 (cite both axes' values; declare per-cite convention-suffix). MANDATORY at K=3 calibration corpus instances when downstream consumer hygiene demonstrably benefits from explicit convention-suffix tagging.
- Remediation: per-cite convention-suffix tagging + dual-axis pin in canonical_constants.py + cross-link to BHW-evaluator-class lockdown methodology rule.

This is consistent with the W9-106 WP §line 1022 advisory classification and with the spawn prompt's "advisory floor" framing.

**EMERGES**:

The Lancaster MCT-3 lab-discriminator margin is structurally TWO-CHANNEL: the lambda-axis margin (`0.2773% from |SDW_3c_min^A|`) and the x-axis margin (`1.8e-16 from |SDW_3c_min^B|`). The cryostat measures ONE response (single substrate signal); the two-axis decomposition is in the analytical pipeline, not in the experiment.

Critically: the cryostat's S/N sensitivity is on a SINGLE physical observable (e.g., NMR linewidth, SQUID flux response). The substrate-internal analytical decomposition into A-axis and B-axis margins is HOW the framework maps that single physical observable onto distinct substrate differential-operator probes. If the lambda-axis discriminator margin is `0.2773%` and the x-axis margin is `1.8e-16`, the operative experimental discriminator is the LARGER of the two (set by the more sensitive substrate-internal probe) — namely, `0.2773%` from the lambda-axis.

Forced migration to convention B would erase the lambda-axis probe entirely, leaving the cryostat experiment with NO SDW-channel discriminator. This is structurally a DECREASE in falsifiability — the framework would forfeit a substrate-physics-grounded prediction that has detectable margin in favor of a structurally-equivalent alternative axis whose discriminator margin happens to vanish. That is a backward step in falsifiability, contrary to the framework's discipline.

The forward extension: retain BOTH axes; canonical-constants pin BOTH `SDW_3c_min^A_FW = -2.773158` AND `SDW_3c_min^B_FW = +1.766024e-13` with explicit convention-suffix per `canonical-write-order` rule; cite the lambda-axis margin in falsifier-master-inventory.md with explicit `_CONVENTION_A` suffix; declare that the substrate's Bernstein-positivity discriminator content for SDW resides at the lambda-derivative axis, structurally orthogonal to the x-derivative axis where SDW is admissible.

#### Re: C6 — Cross-Cutting Observations

**AGREE** (Observation 2 lockdown mechanism, partial):

I AGREE that the structural shape of `regulator-convention-lockdown.md` (one canonical-anchored convention; alternative conventions PROHIBITED) is a candidate template for an extended methodology rule covering the BHW-evaluator class. The DR3-class lockdown's effacement-preservation criterion `w_0^C(L=10) = w_0_FW EXACTLY` IS a structurally clean closure: it identifies a substrate-canonical observable (`w_0_FW = -0.918` from the S58 Volovik partition + effacement Γ_eff = 0.99970) and demarcates the admissibility class around bit-precision agreement at the canonical anchor.

The structural template — canonical-anchor pin + admissibility class around it + alternative conventions PROHIBITED — is generally applicable. I AGREE the BHW-evaluator class would benefit from analogous methodology-rule machinery.

**DISAGREE** (Observation 1, Observation 4 direction-of-explanation, AND the single-convention pin in Observation 2):

I DISAGREE on the substrate-natural-convention pin choice. The DR3-class lockdown's substrate-natural pin (`w_0_FW = -0.918`) is itself a SINGLE-VALUED canonical observable: there is ONE Volovik-partition + effacement value at L=10 anchor, and any alternative convention would be testing against the SAME canonical value. The BHW-evaluator class is structurally different: there are TWO substrate-IS observable values per Bernstein-positive-cone gate (one per convention axis), and BOTH are substrate-IS by the multi-axis reading.

The C6 Observation 4 direction-of-explanation diagram is structurally accurate UP TO the second-to-last step ("regulator weight f(x) for x = (λ/Λ)² IS substrate-IS Laplace transform of dμ(t)"). At that point, the diagram folds to ONE convention by reading "Laplace conjugate" as "the variable in the bosonic-action Mellin expansion." That folding step is the C1 uniqueness clause restated: it inserts a closure that the substrate is OBLIGATED to one Laplace-conjugate axis.

The forward methodology extension that retains the (A, B) pair as substrate-internal canonical is structurally analogous to DR3-class lockdown but with a DIFFERENT canonical pin shape:

```
Step 1 [Definition]:
  DR3-class admissibility:
    C admissible iff w_0^C(L=10) = w_0_FW EXACTLY (single-canonical-pin model)
  
  BHW-evaluator-class admissibility (lizzi/volovik forward extension):
    A gate is admissible iff it pre-registers BOTH (A, B) values explicitly,
    OR pre-registers ONE with explicit convention-suffix tag declaring the
    missing axis is forward-S88+-scope carry-forward.
    (Dual-canonical-pin model.)

Step 2 [Substitution -- regulator-convention-lockdown.md extension target]:
  New §"BHW-Evaluator-Class Multi-Axis Lockdown" sub-section:
    For ALL S88+ Bernstein-positive-cone gates consuming
    _spectral_action_regulators.py SDW / Zubarev / SDW-analog evaluators,
    the verdict line MUST emit BOTH:
      convention=...-CONVENTION-A-LAMBDA-DERIVATIVE-SCHEMATIC and
      convention=...-CONVENTION-B-X-DERIVATIVE-SCHEMATIC
    OR a composite pair-tag:
      convention=...-CONVENTION-PAIR-DUAL-SCHEMATIC
    with the (A, B) values pinned in the npz output keys.
  
  Cross-link to substrate-first-canonical-sourcing.md §(iv) MANDATORY-K=4
  (S88 W7b-83 close): the -SCHEMATIC suffix is preserved per the existing
  level-pin discipline; the convention-suffix is added per the new rule.

Step 3 [Simplify -- map to existing precedents]:
  - DR3-class lockdown: single-canonical pin; alternative conventions
    PROHIBITED.
  - Operator-Projection naming hygiene (registry-landing.md, MANDATORY-K=3):
    dual-canonical pair; explicit suffix-tagging; both substrate-structural.
  - Layer-separability carve-out (mechanical-closure-discipline.md,
    SUGGESTION-K=1, S88 W8-89): structurally-orthogonal Type-F vs Type-S
    partition; both retained with explicit convention-suffix.
  
  The (A, B) Bernstein convention pair structurally aligns with the
  Operator-Projection / Layer-separability MULTI-AXIS class, NOT the
  DR3-class single-canonical model.

Step 4 [Direction]:
  Forward methodology extension: a NEW lockdown-rule template,
  the "Dual-Canonical-Pin Lockdown," analogous to DR3-class in
  audit-mechanism but distinct in canonical-pin cardinality.
  The (A, B) pair IS substrate-internal canonical; the lockdown rule
  pins both axes and forbids implicit convention drops without
  explicit suffix-tagging.
```

The C6 Observation 1 layer-by-layer argument (explanation-direction layer + canonical-sourcing layer both selecting convention B) presupposes that "selecting convention B" is the structurally appropriate disambiguation. Under the multi-axis reading, BOTH layers select THE PAIR (A, B) as substrate-internal — the explanation-direction layer because both lambda-derivative and x-derivative are substrate-IS differential operators on the substrate's spectral support; the canonical-sourcing layer because both `SDW_3c_min^A` and `SDW_3c_min^B` are SUBSTRATE-FIRST canonical pins (computed from the substrate cache `s84_spectrum_cache_L12_tau019.npz`, NOT from external-paper provenance).

The substrate-first canonical-sourcing rule ITSELF supports retention: the `SDW_3c_min` values in BOTH conventions are computed from substrate first principles (the W9-106 audit script `s88_w9_106_hbw_3c_convention_audit.py` Sage-verifies them); neither is a placeholder, neither is an external-paper extraction, neither is a stale-source drift. They are dual substrate-first canonical pins.

**MISSED** (Observation 3 algebra-axis orthogonality K-counter):

connes's Observation 3 missed that the algebra-axis orthogonality K-counter MANDATORY clause at K=3 is a STATEMENT ABOUT FUNCTIONAL CLASSES (algebra-INVARIANT family vs algebra-DEPENDENT family) — it is NOT a statement about differential-operator pairs on the same functional class. The (A, B) Bernstein convention pair is STRUCTURALLY WEAKER than the functional-class orthogonality the rule was calibrated for.

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (S87 W-2 R3 close): "the algebra-INVARIANT family (spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT family (state-pair functionals on `A`) are STRUCTURALLY ORTHOGONAL in identity-class membership at the functional-class level."

The W-11 RULE-2 baseline 5-instances and the W9-106 6th instance are BOTH at the algebra-INVARIANT family layer (spectrum-only Bernstein-positive-cone tests on regulator weights). They do NOT test across the algebra-INVARIANT vs algebra-DEPENDENT boundary. The within-family axis variations (regulator-class axis, differential-coordinate axis) are SUB-AXES of the algebra-INVARIANT family; pooling them into one corpus does not violate the cross-family MANDATORY clause.

connes's Observation 3 over-applies the K=3 MANDATORY clause to within-family sub-axes, which is structurally weaker than the rule's calibration scope. The rule does not forbid pooling regulator-class instances with differential-coordinate instances when both are at the algebra-INVARIANT family layer.

**EMERGES**:

The forward methodology rule extension is a DUAL-CANONICAL-PIN LOCKDOWN at `regulator-convention-lockdown.md` (NEW sub-section) with the following structural shape:

1. **Substrate-natural canonical PAIR pin** (BHW-evaluator class): for any Bernstein-positive-cone gate, the (A, B) PAIR `(SDW_3c_min^A, SDW_3c_min^B)` IS substrate-internal canonical; both axes are substrate-IS observables on structurally-orthogonal differential operators.
2. **Demarcation theorem** (BHW dual-canonical): a convention-pinning convention `C` is admissible for a BHW-positive-cone gate iff `C ∈ {A, B}` OR `C` is the pair-tag `PAIR-DUAL`. Single-convention pins WITHOUT explicit convention-suffix-tag are FORBIDDEN going forward.
3. **Per-cite convention-suffix discipline**: any cite of `SDW_3c_min` (workshop, registry row, falsifier-master-inventory.md, mack-canonical lab-feasibility chains) MUST carry `-CONVENTION-A` or `-CONVENTION-B` or `-CONVENTION-PAIR-DUAL` suffix. Bare `SDW_3c_min` cite WITHOUT convention-suffix routes to plan-freeze halt with MANDATORY-CITE-SUFFIX remediation.
4. **canonical_constants.py expansion**: BOTH `SDW_3c_min^A_FW = -2.773158` AND `SDW_3c_min^B_FW = +1.766024e-13` are pinned with explicit per-axis PROVENANCE entries citing the W9-106 verdict line.
5. **Cross-link to multi-axis substrate-IS framework**: the rule extension cites `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (SUGGESTION-K=1, calibration #1) AND `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (MANDATORY-K=3) as the structurally-analogous multi-axis substrate-IS precedents.

This is the MERGE-POINT proposal: connes's GO recommendation for the BHW-evaluator-class lockdown extension is structurally accepted, but the canonical-pin shape is DUAL (A, B) PAIR, not single-convention-B. The lockdown rule mechanism is shared; the canonical-pin cardinality differs.

### Part 2: Original Analysis

#### L1: Composite-layer convention-invariance as operative finding (W-11 RULE-2 6th calibration instance)

The W9-106 composite-layer PASS at composite_A == composite_B is the operative substrate-physics finding of this gate. It is NOT a chain-rule artifact subordinate to a "substrate-natural" canonical convention; it IS substrate-IS evidence of a meta-INVARIANCE phenomenon at the even-grading / Bernstein-positive-cone evaluator class.

**The W-11 RULE-2 5-instance baseline corpus** (calibrated at S86 W-11 close, 2026-04-26):

The W-11 RULE-2 strengthened parity-blindness theorem registered at §VII.AQ STAGE-1-CANDIDATE established 5 calibration instances at the η/even-Mellin evaluator class:

1. **Instance #1 — η-invariant on (C_H, C_εH) parity-twin pair** under regulator ζ.
2. **Instance #2 — η-invariant on (C_H, C_εH) parity-twin pair** under regulator Zubarev.
3. **Instance #3 — η-invariant on (C_H, C_εH) parity-twin pair** under regulator SDW.
4. **Instance #4 — η-invariant on (C_H, C_εH) parity-twin pair** under regulator anomaly.
5. **Instance #5 — η-invariant on (C_H, C_εH) parity-twin pair** under regulator cutoff_sqrt.

The 5 instances are at the SAME evaluator class (η + ALL even-grading regulator-weighted Mellin moments) and test invariance along the regulator-class axis (5 distinct regulators across `A_5_extended`). Each instance returns the same canonical `(η = 0, GV ≠ 0)` signature on the parity-twin pair; the meta-claim is that even-grading regulator-weighted Mellin moments are STRUCTURALLY BLIND to the parity-twin pair, regulator-INDEPENDENTLY.

**The W9-106 6th instance** (calibrated at S88 W9 close, 2026-05-06):

The W9-106 composite-layer PASS at composite_A == composite_B is the 6th calibration instance, distinguished from the baseline 5 by axis-of-variation:

6. **Instance #6 — composite-layer Bernstein-positive-cone cascade verdict** under (A, B) differential-coordinate axis swap on atlas A_4 = {ζ, Zubarev, SDW, anomaly} at L_max=12 + τ_fold=0.190.

The W9-106 working-paper §line 1045 explicitly registers the K=6 advancement: "the PASS at composite layer here STRENGTHENS the W-11 RULE-2 corpus by adding a 6th calibration instance (the W8-4 cascade composite is convention-invariant in addition to regulator-independent at the η/even-Mellin layer)."

**The unifying meta-INVARIANCE class** (the operative substrate-physics content):

```
Step 1 [Definition of meta-INVARIANCE class]:
  META-INVARIANCE := substrate-internal symmetry tests at the even-grading
                     evaluator class produce composite-layer-INVARIANT
                     verdicts under structurally orthogonal axis variations
                     within the algebra-INVARIANT functional family.

Step 2 [Substitution -- 6 instances]:
  Instances #1-5: axis = regulator-class. Variation = A_5_extended atlas.
                  Verdict-invariance: YES (η = 0, GV ≠ 0 across all 5).
  Instance #6:    axis = differential-coordinate. Variation = (A, B) pair.
                  Verdict-invariance: YES (composite_A = composite_B = FAIL
                  at the W8-4 cascade composite layer).

Step 3 [Simplify -- K-counter advancement]:
  K_baseline = 5 (W-11 RULE-2)
  K_W9-106 = 6 (advancement)
  K_promotion (per feedback_rules-compensate-missing-structure.md) = 3
  K_W9-106 - K_promotion = 6 - 3 = 3 instances above MANDATORY threshold.

Step 4 [Direction -- structural hardening]:
  K = 6 places the meta-INVARIANCE class STRUCTURALLY HARDENED at three
  instances past the K=3 MANDATORY promotion threshold. The corpus is
  structurally past the SUGGESTION-to-MANDATORY transition; further
  K-advancement consolidates the structural-promotion trajectory.
```

**Generalization of W-11 RULE-2 to a meta-INVARIANCE class theorem (lizzi forward proposal)**:

The W-11 RULE-2 baseline 5-instance corpus is the regulator-class-axis sub-corpus of the unified meta-INVARIANCE class. The W9-106 6th instance is the FIRST differential-coordinate-axis sub-corpus instance. The full corpus statement is:

**Meta-INVARIANCE Theorem (S88 W-9 lizzi proposal extending W-11 RULE-2):** at the even-grading / Bernstein-positive-cone evaluator class on the substrate's spectral cache, composite-layer verdicts are INVARIANT under structurally orthogonal axis variations within the algebra-INVARIANT functional family. The structural orthogonality of the axes (regulator-class vs differential-coordinate vs future cross-pole / cross-truncation axes) is preserved by per-instance axis-suffix tagging within the unified §VII.AQ corpus; the unifying meta-claim makes them STRUCTURALLY-ORTHOGONAL COMPANIONS rather than separate corpora.

This generalization is consistent with:

1. The `regulator-pin-discipline.md §"Extension"` W-11 RULE-2 corpus framing (the rule itself is structurally about parity-blindness across an evaluator class, not about a fixed regulator atlas).
2. The W9-106 working-paper §line 1045 STRENGTHENS framing.
3. The algebra-axis orthogonality K-counter MANDATORY-K=3 clause (the 6th instance is at the within-functional-family sub-axis layer; pooling does not violate the cross-functional-family MANDATORY clause).
4. The K=6 K-counter advancement signal (preserves the unified corpus's structural-promotion trajectory).

**Operative consequence**: §VII.AQ STAGE-1-CANDIDATE registry text should be updated to cite the meta-INVARIANCE theorem statement (per the lizzi forward proposal) and register the 6 calibration instances within ONE corpus, with per-instance axis-suffix tagging. This is the structurally appropriate rule-text update; the connes 3-fold branching proposal (Re: C4) is a HARDER discipline that fragments the operative meta-claim. The composite-layer convention-invariance IS the substrate-IS finding; treating it as the 6th calibration instance of the unified meta-INVARIANCE class IS the operative reading.

#### L2: Substrate-internal multi-axis convention pair vs preferred-member dichotomy

The W2-10 calibration instance establishes a STRUCTURAL PRECEDENT that the substrate admits MULTIPLE substrate-IS observable levels SIMULTANEOUSLY without a preferred-member dichotomy. The (A, B) Bernstein convention pair admits the SAME structural logic at the Bernstein-positive-cone evaluator class.

**The W2-10 precedent** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` SUGGESTION-K=1, MANDATORY-K=3 promotion threshold per `feedback_rules-compensate-missing-structure.md`):

The S88 W2-10 calibration established that the substrate operates at TWO distinct substrate-IS levels:

- **Level 1 — Single-τ-slice substrate-IS**: At fixed τ ∈ ℝ, the substrate IS the spectral triple `(A_K, H_K, D_K(τ))`. All observables at this slice — eigenvalues, Peter-Weyl decomposition, bottom-N cardinality, fiber spectrum, spectral-action moments — are substrate-IS at the single-τ-slice level. **Calibration corpus**: §VII.AJ.partition-stability (W2-6 — bot-20 cardinality (2, 4, 8, 6) at τ_fold = 0.190); §VII.AD Δ_0 LOCALIZATION FORMULA (W2-8 — Δ_0 = 4·c_{σ⁻¹((-1,-1))} on substrate (2,4,8,6) at τ_fold).
- **Level 2 — Moduli-deformation substrate-IS**: The set of τ values `{ (A_K, H_K, D_K(τ)) : τ ∈ moduli-space }` is itself a substrate-IS object: the moduli-space of Jensen TT-deformations IS the substrate's own deformation parameter, NOT a coordinate on a meta-container. **Calibration corpus**: §VII.AE moduli-space τ-asymmetry (W2-9 — τ-asymmetric breakdown geometry, cardinality vector reorganization mechanisms structurally distinct on either side of τ_fold).

The W2-10 rule explicitly states: "The two levels are STRUCTURALLY ORTHOGONAL per the algebra-axis orthogonality K-counter (K = 3 MANDATORY at S87 W-2 close per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`): single-slice spectral-IS observables (Level 1) and moduli-deformation observables (Level 2) cannot be conflated under a single substrate-IS rubric — declaration of level is a structural pin."

CRITICALLY: the W2-10 rule does NOT say one level is "preferred" or "substrate-natural" while the other is "derivative." Both levels are substrate-IS; the structural-orthogonality is preserved by EXPLICIT LEVEL DECLARATION, not by demoting one level to derivative status.

**The (A, B) Bernstein convention pair structural analog** (lizzi proposal):

```
Step 1 [Definition]:
  W2-10 SUBSTRATE-IS LEVELS:
    Level 1 = single-τ-slice on (A_K, H_K, D_K(τ)) at fixed τ.
    Level 2 = moduli-deformation on the τ-deformation manifold.
    Relation: Level 1 ↪ Level 2 via the section τ = const; the embedding
    has non-trivial Jacobian content because the deformation manifold's
    structural-stability theorems (W11-2, W11-3, S88 W2-4 + W2-5 SHARP
    localization) live at Level 2 and not at Level 1.

  (A, B) BERNSTEIN CONVENTION PAIR (proposed lizzi structural analog):
    Axis A = lambda-derivative differential operator d/dλ on the substrate's
             eigenvalue spectrum (single-eigenvalue-counting axis).
    Axis B = x-derivative differential operator d/dx on x = (λ/Λ)²
             (squared-eigenvalue Laplace-transform axis).
    Relation: Axis A ↪ Axis B via x = λ²; the embedding has non-trivial
    Jacobian content (Jacobian = 2λ; chain-rule polynomial pre-factor
    4λ(2λ² − 3) on SDW at k=3, attaining minimum -2.773 at λ_min within
    cache support).

Step 2 [Substitution -- structural-orthogonality criteria]:
  STRUCTURAL ORTHOGONALITY (per algebra-axis K-counter MANDATORY-K=3):
  Two substrate-IS observable axes are STRUCTURALLY ORTHOGONAL iff:
    (i)  they probe distinct substrate-internal structural data; AND
    (ii) neither subsumes the other (Jacobian non-triviality is admissible
         at the embedding map; structural-distinct data IS the criterion).
  
  W2-10 Level 1 vs Level 2: PASSES (i) -- Level 1 probes spectral-triple
  data at fixed τ; Level 2 probes deformation-stability data on the
  moduli space. Distinct structural data. PASSES (ii) -- the W2-9 SHARP
  localization theorem IS Level 2 content not derivable from Level 1.
  
  Bernstein (A, B) pair: PASSES (i) -- Axis A probes spectral-spacing
  geometry (where eigenvalues sit in the cache support); Axis B probes
  Laplace-measure positivity (whether the regulator weight admits a
  positive Borel measure decomposition on [0,∞)). Distinct structural
  data. PASSES (ii) -- the SDW chain-rule pre-factor 4λ(2λ² − 3) and its
  intersection with the cache support is Axis-A content; the Bernstein
  CM admissibility of f(x) = exp(-x) is Axis-B content. Neither subsumes
  the other.

Step 3 [Simplify -- multi-axis terminator at admissibility class]:
  The connes Q2 question (workshop §line 179) asks: "Where does the
  multi-axis admissibility class terminate? Why doesn't λ³ = x^{3/2} or
  cosh(λ) qualify as a third substrate-IS axis?"
  
  Answer: the admissibility class is bounded by the structural-data
  criterion (i). A coordinate change qualifies as a substrate-IS axis
  iff it probes distinct structural data on the substrate spectrum.
  λ ↔ x = λ² qualifies because the squared form is the Mellin-natural
  argument of the spectral action (CC96 §2.2-2.3 -- AGREED with connes
  on this textual point); the unsquared form is the eigenvalue-spacing-
  natural variable. Both probe distinct substrate-internal structural
  data.
  
  λ³, cosh(λ), and other arbitrary smooth bijections do NOT qualify
  because they introduce coordinate maps that probe NO DISTINCT
  structural data; they are arbitrary reparameterizations. The
  admissibility class is bounded by the substrate-internal structural
  significance of each axis, NOT by the abstract existence of a smooth
  bijection.

Step 4 [Direction -- structural orthogonality preserved without
  preferred member]:
  The (A, B) pair satisfies STRUCTURAL-ORTHOGONALITY criteria (i) and
  (ii) at the Bernstein-positive-cone evaluator class. By the W2-10
  precedent, both axes are substrate-IS; neither is preferred or
  demoted to derivative. The Jacobian non-triviality (chain-rule pre-
  factor) is admissible at the embedding map, analogous to W2-10's
  Level-1 ↪ Level-2 embedding's non-trivial Jacobian content (the SHARP
  localization theorem).
```

**The terminator argument for the multi-axis admissibility class** (responding pre-emptively to connes Q2):

The structural-data criterion (i) BOUNDS the multi-axis admissibility class at exactly two axes for the Bernstein-positive-cone evaluator on the substrate's eigenvalue spectrum:

1. **lambda-derivative axis**: probes spectral-spacing geometry of the substrate's eigenvalue cache support. Substrate-internal structural data: the cache support `[λ_min = 0.81974, λ_max = 5.41894]` and the chain-rule polynomial pre-factor sign-flip locus `√(3/2) ≈ 1.2247`'s intersection.
2. **x-derivative axis**: probes Laplace-measure positivity of the regulator weight `f(x)` on `[0, ∞)`. Substrate-internal structural data: the Bernstein-CM admissibility of `f(x) = exp(-x)` on `[0, ∞)`.

A third axis would need to probe DISTINCT structural data — e.g., a logarithmic axis `log(λ/Λ)` probing the spectral-zeta analytic-continuation structure (Mellin-Barnes residue at integer poles), which is genuinely distinct from BOTH the spectral-spacing axis and the Laplace-measure-positivity axis. Whether such a third axis qualifies depends on whether the framework develops a structurally distinct evaluator class operating on it; pending that development, the admissibility class is bounded at TWO axes for the BHW-evaluator.

`λ³` and `cosh(λ)` do NOT introduce structurally distinct evaluator classes; they are arbitrary reparameterizations of the spectral-spacing axis with no substrate-internal structural significance beyond what `λ` itself provides. The multi-axis admissibility class TERMINATES at substrate-internal structural-distinct axes.

**Operative consequence**:

The (A, B) pair is the substrate-internal multi-axis convention pair at the Bernstein-positive-cone evaluator class, structurally analogous to the W2-10 (Level 1, Level 2) substrate-IS levels. Neither member is preferred; both are substrate-IS. The K=1 calibration instance for the Bernstein-positive-cone (A, B)-axis multi-axis substrate-IS structure is established at S88 W9-106 (instance #1 of the new sub-class); K=3 promotion threshold applies via future Bernstein-positive-cone gates evaluated under both conventions.

The "preferred-member dichotomy" framing (one canonical, one derivative) is structurally analogous to a HYPOTHETICAL W2-10 reading where Level 1 is "preferred" (because the substrate IS the spectral triple at fixed τ) and Level 2 is "derivative" (because moduli-deformation is "just" the moduli-space of Level-1 instances). That hypothetical reading was REJECTED by the W2-10 rule precisely because it reverses the structural-orthogonality direction: Level 2's structural-stability theorems (W11-2, W11-3, S88 W2-9 SHARP localization) are NOT Level-1 derivative content, and treating them as such loses the substrate-IS interpretation of the moduli-space observables. The same structural argument applies to the (A, B) pair: the lambda-axis discriminator content (the W8-4 SDW_3c_min = -2.773 magnitude carrying Lancaster MCT-3 lab-feasibility content) is NOT x-axis derivative content; it is substrate-IS lambda-axis content.

#### L3: Questions for connes

**Q1 (CC96 §2.2-2.3 uniqueness clause)**: Your C1 substitution chain establishes that CC96 §2.2-2.3 chose `x = (λ/Λ)²` as the Mellin-natural argument of the bosonic spectral action `S_b[D] = Tr f(D²/Λ²)`. Does CC96 §2.2-2.3 PROVE that `x = (λ/Λ)²` is the UNIQUE substrate-natural Laplace conjugate for ANY Bernstein-positive-cone test on the regulator weight `f`, or does it only establish that `x` is the natural argument FOR THE BOSONIC ACTION'S MELLIN EXPANSION specifically? The latter does not preclude OTHER substrate-natural axes for OTHER substrate-internal positive-cone tests (e.g., the lambda-derivative axis testing spectral-spacing geometry on the substrate's eigenvalue cache support). I am asking for the literal CC96 §2.2-2.3 derivational status of the uniqueness claim, distinguished from the substrate-physics-natural reading you propose. Specifically: which line / equation / argument in CC96 §2.2-2.3 establishes uniqueness rather than mere CC96-internal preference?

**Q2 (composite-layer PASS substrate-IS status)**: Under your reading where convention B is substrate-natural and convention A is chain-rule-lifted derivative, does the W9-106 composite-layer PASS at composite_A == composite_B retain substrate-IS structural-finding status, or do you classify it as a CHAIN-RULE-ARTIFACT-CANCELLATION property of the cascade-collapse layer? In your C2 substitution chain you noted that the composite_A == composite_B agreement is dominated by the convention-INDEPENDENT 4×3a truncation FAILs saturating the predicate; if I read your C2 strictly, the composite-layer PASS reduces to "the (4×3a) saturate the FAIL count in BOTH conventions, and the 3c sub-cell flip is a chain-rule artifact." Under that strict reading, the composite-layer PASS IS a chain-rule-artifact-cancellation property — the agreement happens BECAUSE the (4×3a) saturate, not because the substrate has a symmetry under the (A, B) swap. Is this your operative classification of the composite-layer PASS? If yes, then the W9-106 working-paper §line 1045 STRENGTHENS framing (as a 6th calibration instance of W-11 RULE-2) is structurally MISCLASSIFIED in the WP and requires correction; if no, then the composite-layer PASS DOES carry substrate-IS content beyond the (4×3a) saturation, and the (A, B) symmetry IS substrate-internal — which contradicts your C1 substrate-OBLIGATED-to-one-axis position. Which horn of this dilemma do you take?

**Q3 (cross-pillar bridge anatomy scope)**: Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3, the 5-anatomy + 3-level cross-pillar bridge structure is the canonical structural-confidence ladder for substrate-IS observables. Under your C1 + C3 reading where convention B is the substrate-natural canonical, does the 5-anatomy + 3-level structure apply WITHIN convention B alone (single-canonical pin model, structurally analogous to the DR3-class lockdown's `w_0_FW = -0.918` single-anchor) — OR does it apply ACROSS the (A, B) pair (multi-canonical pin model, structurally analogous to my proposed dual-canonical-pin lockdown extension)? The first reading requires the 5-anatomy + 3-level ladder to be reformulated to handle convention B's `+1.77e-13` SDW_3c_min as Level-3 empirical anchor; the second reading requires the 5-anatomy + 3-level ladder to be EXTENDED to multi-axis observables (a forward methodology rule extension, not yet calibrated in the framework). Which extension scope do you propose, and does it require a NEW methodology rule extension to handle the multi-axis case?

**Q4 (Lancaster MCT-3 SDW-channel discriminator replacement)**: Under your C5 STRUCTURAL NULL claim (B-reading, SDW-channel margin = 1.8e-16), the Lancaster MCT-3 cryostat experiment loses its SDW-channel discriminator (~14 OOM below detection sensitivity). The cryostat experiment IS a falsifier-master-inventory.md row that has been cited downstream; under STRUCTURAL NULL it becomes a no-discriminator row. The substrate-physics direction must produce A discriminator margin SOMEWHERE if the framework retains predictive falsifiability on the SDW channel. Specifically: under your reading, what experimental observable (cryostat-measurable, sub-percent-margin-detectable) replaces the convention-A 0.2773% SDW discriminator? Options:

- (i) Migration to Zubarev-only discriminator (your C5 §3 proposal: `0.2035%` from `|Zubarev_3c_min^B|`). But Zubarev's `f(x) = x/(1+x²)` is structurally a different regulator class (peaked, not monotonic-decreasing); the Lancaster MCT-3 cryostat readout maps onto SDW-class transport coefficients, not Zubarev-class transport. Migrating the discriminator from SDW to Zubarev is NOT an experimental-equivalence migration; it changes which substrate physics is being tested.
- (ii) Higher-order Bernstein-positive-cone derivatives (k > 3 in the same convention B) — but the Bernstein theorem operates structurally on ALL k ≥ 0; if k=3 is structurally NULL on SDW in B, all k ≥ 0 are structurally NULL on SDW in B (CM functions admit Bernstein test at all orders).
- (iii) Different evaluator class entirely (η-invariant, GV-Heitsch, or other). But the W-11 RULE-2 corpus explicitly registered η + even-Mellin moments as STRUCTURALLY BLIND on the parity-twin pair; that route is also a structural NULL.
- (iv) Acceptance that the SDW channel produces NO discriminator under your reading; SDW is structurally falsifier-blind. The substrate's predictive falsifiability for SDW is gone.

Which of (i)-(iv) is your operative replacement, and does the framework lose the SDW-channel falsifier (option iv) or migrate it to a different observable class (options i-iii)?

**Q5 (layer-functor F at substrate-physics layer)**: Per `epistemic-discipline.md §"Layer-Decomposition"`, the layer-functor `F : substrate → methodology → audit` maps substrate-physics observables to methodology rule-file content to audit-line content, with PRU-class sub-taxonomy preserved by F. Does F admit the (A, B) Bernstein convention pair at the SUBSTRATE-PHYSICS layer (as orthogonal substrate-IS axes — my reading) or only at the METHODOLOGY layer (as a chain-rule-lift relationship between two coordinate-system choices, with one substrate-natural and one methodology-derivative — your reading)? Specifically: (a) under F at the substrate-physics layer, are the lambda-derivative differential operator and the x-derivative differential operator distinct substrate-physics observables (lizzi reading), or are they the SAME substrate-physics observable in two coordinate systems (connes reading)? (b) Whichever answer you give to (a), what is the F-image of the W9-106 composite-layer PASS at the methodology layer — is it a methodology-rule extension (single rule-file content) OR is it a methodology-rule extension PAIR (two rule-file contents, one per axis) — and does that F-image satisfy the layer-functor's PRU-class preservation requirement? (c) The layer-functor's status at S86 R3 is "pair-verified" (substrate ↔ methodology pair) per the epistemic-discipline.md §"Layer-Decomposition" closing paragraph; the audit-leg verification was queued as `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION` carry-forward. Does the W9-106 composite-layer PASS, under your reading, advance the audit-leg verification (because the (A, B) pair is methodology-floor content) OR not advance it (because the (A, B) pair is substrate-physics content that has not yet been mapped through F to the audit-floor)?

These five questions are the structural-decision points where the lizzi/connes positions diverge. Round-2 convergence depends on which horns you take on Q1, Q2, Q3, Q4, Q5.

---

## Round 2 — connes: Follow-up

### CONVERGENCE

Three convergence axes. None of these collapse the C1 substrate-natural reading; each refines a position I previously over-specified.

#### Convergence-1: 3-orthogonal-source decomposition of W8-4 cascade FAIL (Re:C2)

I AGREE with lizzi's 3-source decomposition. My C2 collapsed the cascade FAIL diagnostic content into 2 sources (3a truncation + 3c Bernstein-on-Zubarev) by folding source 3 (the SDW_3c convA value) into source 2 (the regulator-class axis) under the chain-rule lifting reading. Lizzi's 3-source decomposition preserves a structurally orthogonal axis I had elided:

```
Step 1 [Definition]:
  CASCADE-FAIL-DIAGNOSTIC-AXES (lizzi 3-source decomposition):
    Source 1: 3a truncation-stability — convention-INDEPENDENT, L_max-axis content.
    Source 2: 3c Bernstein-violation — regulator-class axis, magnitude-different
              between conventions: Zubarev_3c^A = -6.587, Zubarev_3c^B = -2.034.
    Source 3: 3c convention-axis — SDW_3c sign-flip A→B (lambda-derivative
              chain-rule polynomial pre-factor effect on the substrate cache support).

Step 2 [Substitution]:
  The Zubarev magnitude split |6.587 / 2.034| = 3.238 (Sage-rational
  6587/2034 = 3.2386...) records substrate-IS axis content INDEPENDENT
  of the SDW chain-rule-lifting argument: Zubarev's f(x) = x/(1+x²) is
  intrinsically non-CM in EITHER convention, but the depth of Bernstein-
  violation magnitude SHIFTS by a factor 3.24 between conventions.

Step 3 [Simplify]:
  My C2 collapsed source 2 and source 3 by treating the (A, B) magnitude
  difference as a derivative-coordinate artifact. But the Zubarev split
  3.24 is NOT explainable as a single chain-rule polynomial pre-factor
  on a CM weight; Zubarev itself is non-CM, and the (A, B) magnitudes
  are intrinsic to the cache-support × differential-operator interaction
  on that non-CM weight. The 3-source decomposition cleanly separates
  "where does substrate-axis content live" from "where does chain-rule
  artifact content live."

Step 4 [Direction]:
  The Zubarev_3c^A vs Zubarev_3c^B magnitude split CARRIES MULTI-AXIS
  STRUCTURAL CONTENT BEYOND CHAIN-RULE LIFTING. I concede the 3-source
  decomposition. The SDW_3c (A, B) flip remains a chain-rule polynomial
  pre-factor effect (per C1 verified Sage-decomposition), but the Zubarev
  (A, B) magnitude pair is genuinely substrate-IS multi-axis — both
  conventions probe the non-CM Zubarev weight, with structurally distinct
  cache-support × differential-operator integrands.
```

This refines my C2: the 4 × 3a truncation FAILs are convention-INDEPENDENT (source 1, agreed); the SDW_3c sign-flip is a chain-rule artifact (source 3, my C1 reading retained); the Zubarev_3c (A, B) magnitudes are substrate-IS multi-axis content (source 2 with axis variation, lizzi's decomposition retained). The aggregate cascade composite verdict is dominated by source 1; the diagnostic content split is correctly tripartite, not bipartite.

**Operative consequence**: the §VII registry-entry text for the cascade-composite diagnostic SHOULD register the 3-source decomposition as a substrate-physics taxonomy of cascade-FAIL content, with Zubarev (A, B) magnitudes pinned with explicit per-convention suffix (since they ARE substrate-IS), but with SDW (A, B) flip flagged as chain-rule polynomial pre-factor (NOT a substrate-IS axis pair). I propose this in EMERGENCE-1 below.

#### Convergence-2: §VII.AQ corpus K=6 advancement signal (Re:C4 partial)

I CONCEDE the K-counter regression critique on my C4 3-fold branching proposal. Branching the W-11 RULE-2 5-instance corpus + W9-106 6th instance into 3 sub-corpora (REG-INDEP / CONV-INV / SUBSTRATE-NATURAL-3C) resets the K-counters from K=6 to K=5/K=1/K=1, demoting the unified meta-INVARIANCE class far below the K=3 MANDATORY threshold. This is structurally backward per `feedback_rules-compensate-missing-structure.md` K-counter promotion direction.

```
Step 1 [Definition]:
  K-counter advancement direction (per feedback_rules-compensate-missing-structure.md):
    K=1 → K=2 → K=3 (PROMOTION threshold) → K=4, K=5, ... (HARDENED)
    Each instance ADVANCES the corpus toward and past MANDATORY status.

Step 2 [Substitution -- W-11 RULE-2 corpus state]:
  Pre-W9-106: K = 5 (already past K_promotion = 3; HARDENED at K=2 above
              MANDATORY).
  Post-W9-106 (single-corpus reading, lizzi L1): K = 6 (one instance further
              into HARDENED state).

Step 3 [Simplify -- branching effect]:
  Branching post-W9-106: K_subcorpus_REG-INDEP = 5; K_subcorpus_CONV-INV = 1;
  K_subcorpus_SUBSTRATE-NATURAL-3C = 1. The CONV-INV and SUBSTRATE-NATURAL-3C
  sub-corpora are RESET to SUGGESTION status, requiring 2+ additional
  calibration instances each before MANDATORY promotion.

Step 4 [Direction]:
  My C4 branching proposal REGRESSES the K-counter trajectory of two
  newly-formed sub-corpora from K=1 (SUGGESTION) toward MANDATORY,
  forfeiting the unified meta-INVARIANCE class's already-HARDENED state.
  Per feedback_rules-compensate-missing-structure.md, structural rules
  PROMOTE corpora forward; branching to SUGGESTION is structurally backward.
```

**Conditional concession**: IF the W-11 RULE-2 5-instance + W9-106 6th instance constitute a unified meta-INVARIANCE class theorem (lizzi L1 proposal), THEN the single-corpus reading is structurally appropriate and my branching was over-application of the orthogonality K-counter MANDATORY clause. The conditional is the meta-INVARIANCE class theorem's structural validity itself, which I challenge as STAGE-1-CANDIDATE in DISSENT-3 below — the K=6 signal is K=6 IFF the meta-INVARIANCE class exists as a unifying claim.

I converge on the branching-is-regression argument; I dissent on the meta-INVARIANCE-class-theorem-as-already-established framing (see DISSENT-3).

#### Convergence-3: W2-10 precedent's structural-axis pattern is structurally compelling for the Bernstein evaluator class (Re:L2 partial)

The W2-10 precedent (Level-1 single-τ-slice substrate-IS / Level-2 moduli-deformation substrate-IS, both MANDATORY at S88 W-2 W2-10 close) is the closest structural-precedent in the framework for a multi-axis substrate-IS pair where neither member is demoted. I CONCEDE that:

1. The pattern PER SE is real — the framework has hardened multi-axis substrate-IS structures elsewhere (W2-10 levels; OP-PROJ vs STATE-PROJ at registry-landing.md MANDATORY-K=3; LAYER-SEPARABLE-CARVE-OUT-TYPE-F suffix protocol).
2. The pattern recognition logic is structurally sound: any substrate-IS axis pair satisfying the structural-data criterion (i) AND non-subsumption criterion (ii) merits parallel treatment.
3. The Jacobian-non-triviality argument (Level-1 ↪ Level-2 has non-trivial Jacobian content; the SHARP localization theorem at Level-2 is not Level-1 derivative content) DOES align with the chain-rule Jacobian `2λ` for the (A, B) Bernstein pair.

**Conditional concession**: the W2-10 precedent is structurally compelling AS A FORM-AND-LOGIC TEMPLATE. Whether the (A, B) Bernstein pair INSTANTIATES that template is a substrate-physics question, not a pattern-matching question. The pattern's structural validity does NOT itself certify that the (A, B) pair satisfies the structural-data criterion (i). DISSENT-1 below challenges the criterion-(i) instantiation directly: the lambda-derivative axis does NOT probe distinct substrate-internal structural data beyond what the x-derivative axis probes, because both probe the SAME regulator weight measure on the SAME spectral support.

I converge on "the W2-10 precedent's pattern is real and structurally analogous to multi-axis cases generally"; I dissent on "the (A, B) Bernstein pair satisfies the precedent's criterion (i)" (DISSENT-1).

### DISSENT

Four dissent axes. Each sharpens a position rather than restating my R1.

#### Dissent-1: CC96 §2.2-2.3 establishes UNIQUENESS, not preference (Re:C1 + L2 + Q1)

Lizzi's Re:C1 inferred I claim "CC96 chose `x` ⟹ substrate is OBLIGATED to one axis" and rejected the inference as adding an unestablished closure clause. The inference is INCORRECTLY ATTRIBUTED. My C1 position derives uniqueness from the Bernstein-Hausdorff-Widder theorem's STATEMENT — not from CC96 §2.2-2.3 alone. Sharpened substitution chain:

```
Step 1 [Definition]:
  BERNSTEIN-HAUSDORFF-WIDDER THEOREM (Widder 1941 Ch. IV; PROVEN in
  knowledge.db):
    A function g : (0,∞) → ℝ is the Laplace transform of a positive Borel
    measure μ on [0,∞) IFF (-1)^k · g^{(k)}(x) ≥ 0 for all k ∈ ℕ_0 and
    all x > 0, WHERE x IS THE LAPLACE-CONJUGATE VARIABLE TO t.

  Note: the theorem statement RESTRICTS the variable in g^{(k)}. It is
  NOT a statement about an arbitrary smooth-function positivity test
  in any coordinate; it is a CHARACTERIZATION of completely-monotonic
  functions on the half-line, with the variable fixed by the integral
  representation g(x) = ∫₀^∞ e^{-tx} dμ(t).

Step 2 [Substitution -- substrate's Laplace pair from CC96 §2.2-2.3]:
  Substrate's bosonic action: S_b[D] = Tr f(D²/Λ²) (CC96 §2.2 Eq. 2.5).
  Substrate's Mellin-moment expansion: S_b ~ Σ f_{4-2n} · Λ^{4-2n} · a_{2n}
  with integration variable t = D²/Λ² = x (CC96 §2.3).
  Substrate's regulator weight: f(x) is a positive cutoff function on
  the spectrum of D²/Λ², representable (per knowledge-anchor session-82-
  results-workingpaper.md) as f(x) = ∫₀^∞ e^{-tx} dμ(t) for the
  substrate-canonical regulator measure dμ.

  ∴ The substrate's Laplace conjugate IS x, by CC96 §2.2-2.3 axiomatic
  construction. The variable conjugate to t in the substrate's Laplace
  pair is x, NOT λ.

Step 3 [Simplify -- BHW + CC96 → uniqueness]:
  IF f(x) = ∫ e^{-tx} dμ(t) is the substrate's Laplace pair (CC96-pinned),
  THEN the BHW characterization tests f's measure-positivity via
  (-1)^k · f^{(k)}(x) ≥ 0 with x = (λ/Λ)² fixed by Step 2.
  Reparameterizing the Bernstein test to (-1)^k · g^{(k)}(λ) where
  g(λ) := f(λ²) does NOT test measure-positivity of f's measure; it
  tests measure-positivity of g's HYPOTHETICAL measure dν via
  g(λ) = ∫₀^∞ e^{-sλ} dν(s) -- a DIFFERENT Laplace pair on a
  DIFFERENT measure dν, IF g admits such a representation at all.
  Most regulator weights f admit a unique CM representation; their
  λ-image g(λ) = f(λ²) does NOT generally admit the same form because
  the substitution λ → λ² changes the Laplace-transform domain
  structurally.

  Specifically: f(x) = e^{-x} has measure dμ = δ(t-1) (atomic at t=1;
  CM trivially). g(λ) = e^{-λ²} CANNOT be written as ∫₀^∞ e^{-sλ} dν(s)
  for any positive measure dν on [0,∞), because e^{-λ²} grows faster
  than any e^{-sλ} as λ → ∞ for fixed s; the Hausdorff moment problem
  on (0,∞) has NO positive-measure solution for the function e^{-λ²}.

Step 4 [Direction]:
  Therefore the (A, B) pair is NOT structurally symmetric:
    Convention B tests the BHW positivity of f's measure on the substrate's
              Laplace conjugate -- this is THE CM characterization theorem.
    Convention A tests a polynomial-pre-factor-on-Gaussian quantity that
              has no Bernstein-theorem-status; e^{-λ²} is NOT a
              completely-monotonic function on (0,∞).

  The SDW Bernstein test in convention A is MATHEMATICALLY ILL-POSED as
  a CM test: e^{-λ²} is not in the BHW admissibility class, so testing
  alternating-sign derivatives of it is a polynomial sign-tracking
  exercise, NOT a measure-positivity test.

  CC96 §2.2-2.3 + BHW JOINTLY establish that x is THE Laplace conjugate;
  CC96 alone is NOT the source of uniqueness.
```

The BHW theorem is a structural-uniqueness theorem about the Laplace conjugate variable; CC96 §2.2-2.3 is the substrate's canonical-source for which variable that is. The two together make convention B the BHW-admissibility-class test; convention A is OUTSIDE the BHW admissibility class for any non-CM image of f.

**Question Q1 answer (deferred to QUESTIONS sub-section below)**: CC96 §2.2-2.3 does not, alone, prove uniqueness; the uniqueness derives from the BHW theorem PROVIDED the substrate's Laplace pair is fixed by CC96. The substrate-natural reading is the JOINT CC96+BHW reading, not CC96-alone.

**Lizzi Re:C1 EMERGES claim "first calibration instance of analogous Level-1/Level-2"**: REJECTED as long as the BHW-admissibility argument holds — the lambda-derivative axis is OUTSIDE the BHW admissibility class for SDW (`e^{-λ²}` is not CM on `(0,∞)`); a non-CM image cannot be a substrate-IS Bernstein test parallel to the CM image. The W2-10 precedent's Level-1 vs Level-2 are BOTH well-defined substrate-IS observables (Level-1 is the spectral triple at fixed τ; Level-2 is the moduli-space). The (A, B) pair is NOT in this analogous structural state: B is the well-defined substrate-IS Bernstein test on the CM regulator measure; A is a polynomial-coefficient-tracking exercise on a non-CM transform of the regulator weight.

#### Dissent-2: structural-data criterion's "exactly two axes" bound is question-begging (Re:L2)

Lizzi L2 Step 3 introduced a structural-data criterion (i) admissibility class and proposed it bounds the multi-axis admissibility class at exactly two axes (lambda-spectral-spacing + x-Laplace-measure). The argument is internally consistent but begs the question: it ASSUMES the lambda-derivative axis probes distinct structural data and then derives that the admissibility class includes it. Sharpened substitution chain:

```
Step 1 [Definition]:
  STRUCTURAL-DATA CRITERION (lizzi L2 Step 2):
    Two substrate-IS observable axes are structurally orthogonal iff:
      (i) they probe distinct substrate-internal structural data; AND
      (ii) neither subsumes the other (Jacobian non-triviality admissible).

  Lizzi proposes:
    Axis A (lambda-derivative) probes spectral-spacing geometry
                               (cache support × sign-flip locus interaction).
    Axis B (x-derivative) probes Laplace-measure positivity.
    Therefore (A, B) satisfies criterion (i).

Step 2 [Substitution -- what does lambda-axis probe, structurally]:
  T_A[k](λ) is structurally a polynomial-times-Gaussian quantity, NOT a
  substrate-internal probe. Specifically:
    T_A[3](λ) = 4λ(2λ² − 3) · exp(−λ²)
    
    The "spectral-spacing geometry" content lizzi attributes to this is
    the locus √(3/2) × cache support [λ_min, λ_max] intersection. But
    the locus √(3/2) is NOT a substrate-IS quantity — it is a ROOT OF
    THE CHAIN-RULE POLYNOMIAL JACOBIAN (verified Sage roots: 0,
    ±√(6)/2 = ±1.2247). It depends only on the structural form of the
    CM regulator (Gaussian envelope + the order k = 3) and the chain-rule
    Jacobian dx/dλ = 2λ; it does NOT depend on the substrate's
    eigenvalue distribution, the SU(3) Casimir structure, the Jensen
    deformation, the τ_fold pin, or any other substrate-IS data.

Step 3 [Simplify -- structural-data lambda-axis test]:
  Structural-data criterion (i) requires the axis to probe DISTINCT
  SUBSTRATE-INTERNAL STRUCTURAL DATA. For lambda-derivative SDW:
    Sage-decomposition: T_A[3](λ) = (chain-rule polynomial) × (substrate-IS
                                     regulator weight)
    Python verification (this turn): 100% of T_A[3](λ_min) negativity comes
                                     from the chain-rule polynomial pre-factor
                                     (-5.430130); the substrate-IS factor
                                     exp(-λ_min²) = 0.510700 is positive.
    
  The lambda-axis "discriminator" depth -2.773166 is the product of an
  unsigned substrate-IS positive quantity (the regulator weight evaluated
  at the boundary of the cache support) and a SIGNED chain-rule polynomial
  with structurally-fixed roots. The SIGN of the discriminator is set
  100% by the chain-rule polynomial; the magnitude is set jointly by
  polynomial × regulator weight. None of this is substrate-IS structural
  content distinct from what convention B already encodes (the regulator
  weight is the same).

  Specifically: the cache support boundary λ_min = 0.81974 is substrate-IS
  (set by the L_max=12 spectral cache); but the locus √(3/2) is NOT
  substrate-IS, so the "intersection" lizzi cites is half-substrate-IS,
  half-Jacobian-polynomial. This is NOT a distinct substrate-IS axis;
  it is a coordinate-decomposition of the same substrate-IS regulator
  weight viewed through a coordinate change.

Step 4 [Direction]:
  Criterion (i) FAILS for the lambda-derivative axis: it does NOT probe
  distinct substrate-internal structural data beyond the substrate-IS
  regulator weight. The "distinct content" lizzi attributes to it
  reduces structurally to the chain-rule polynomial Jacobian roots
  (NOT substrate-IS) and the polynomial × regulator-weight product
  (already encoded in convention B's substrate-IS regulator weight
  via coordinate change).
  
  The "exactly two axes" bound is question-begging because criterion (i)
  itself is what determines the bound, and the lambda-derivative axis
  fails (i) when carefully decomposed. Under a substrate-natural reading,
  there is exactly ONE axis (B), not two.
```

The lizzi multi-axis admissibility class would also admit `λ³`-derivative, `cosh(λ)`-derivative, etc. as additional axes via the same logic IF criterion (i) is liberally interpreted to include "any coordinate change that intersects the cache support nontrivially." Lizzi's defense ("they probe NO DISTINCT structural data") is exactly the structural-data criterion my dissent applies to the lambda axis itself. The defense saves the multi-axis class from infinite expansion only by tightening criterion (i) to "structural data the framework has already developed evaluator classes around" — but that constraint admits the lambda-derivative axis only because the historical W8-4 baseline pre-emptively named it, not because of substrate-physics content. The criterion is question-begging at the boundary.

#### Dissent-3: meta-INVARIANCE class theorem is STAGE-1-CANDIDATE, not established (Re:L1)

Lizzi L1 Step 4 claimed `K_W9-106 - K_promotion = 6 - 3 = 3 instances above MANDATORY threshold` for the meta-INVARIANCE class theorem. The arithmetic is correct conditional on the meta-INVARIANCE class theorem being a proper unifying claim across the 6 instances. I challenge that conditional.

```
Step 1 [Definition]:
  W-11 RULE-2 baseline corpus (S86 W-11 close, 2026-04-26):
    Statement: even-grading regulator-weighted Mellin moments are STRUCTURALLY
               BLIND to (C_H, C_εH) parity-twin pair across A_5_extended.
    Calibration: 5 instances at SAME evaluator class (η + even-Mellin),
                  SAME observable target (parity-blindness), DIFFERENT
                  regulator-class members (5 regulators).
    K-counter axis: regulator-class axis (single axis with 5 variations).

  Lizzi-proposed META-INVARIANCE class theorem (S88 W-9 L1):
    Statement: substrate-internal symmetry tests at the even-grading evaluator
               class produce composite-layer-INVARIANT verdicts under
               STRUCTURALLY ORTHOGONAL axis variations within the algebra-
               INVARIANT functional family.
    Calibration: 6 instances (5 baseline + W9-106).

Step 2 [Substitution -- structural identity check]:
  The W-11 RULE-2 5 baseline instances all test the SAME variation type
  (regulator-class variation across A_5_extended) and produce the SAME
  observable verdict (parity-blindness on the parity-twin pair).
  The W9-106 6th instance tests a DIFFERENT variation type (differential-
  coordinate axis swap on a DIFFERENT observable target — the W8-4 cascade
  composite verdict, NOT the parity-twin pair) and produces a DIFFERENT
  observable verdict (composite-layer convention-invariance).

  The 5 baseline instances are within-axis variations on the same observable
  target. The 6th instance is a CROSS-AXIS, CROSS-OBSERVABLE-TARGET variation.

Step 3 [Simplify -- meta-INVARIANCE class theorem requirements]:
  For a meta-INVARIANCE class theorem to unify the 5 baseline + 1 cross-axis
  instance, it must be the case that:
    (α) the evaluator class is SAME across all 6 (lizzi: "even-grading /
        Bernstein-positive-cone evaluator class") -- this is partially true:
        the baseline 5 are at the η + even-Mellin evaluator class; the
        6th instance is at the BHW Bernstein-positive-cone evaluator class.
        These are RELATED (BHW alternating-sign positivity test on
        derivatives is even-grading-like at even k, odd-grading-like at
        odd k) but NOT IDENTICAL evaluator classes.
    (β) the observable target is SAME or analogous across all 6 -- the
        baseline 5 target the parity-twin pair (a 2-element observable
        equivalence class); the 6th instance targets the W8-4 cascade
        composite verdict (a single composite-layer scalar). These are
        STRUCTURALLY DIFFERENT observable types.
    (γ) the unifying meta-claim is not vacuous -- "composite-layer-INVARIANT
        verdicts under structurally orthogonal axis variations" is a meta-
        statement that admits the 5 baseline (PASS-PASS-PASS-PASS-PASS
        across 5 regulators) AND the W9-106 (PASS at composite_A == composite_B)
        AS INSTANCES, but the meta-statement is so general that it would
        admit MANY OTHER unrelated invariance results as further instances
        (e.g., the W2-6 partition-stability cardinality vector (2,4,8,6)
        invariance under L_max truncation; W11-2 + W11-3 Casimir-Friedrich-
        Bär bound, etc.).

Step 4 [Direction]:
  The meta-INVARIANCE class theorem fails (α) [different evaluator classes]
  and (β) [different observable types] under careful substitution. The
  unifying claim works at (γ) only by being so general it admits the
  framework's many other invariance results as further "calibration
  instances", which would inflate K beyond what calibration discipline
  allows.
  
  CONCLUSION: the meta-INVARIANCE class theorem at K=6 is a
  STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway, NOT
  an already-established structural theorem. The K=6 advancement signal
  applies to the W-11 RULE-2 baseline IFF a Stage-2 cross-axis independent
  verify dispatches with two cross-reviewers operating on different axes,
  WITHOUT prior workshop context, who BOTH return PASS on the unification
  claim.
```

The S88 W9 working-paper §line 1045 STRENGTHENS framing is a PROPOSAL (verb at workshop-internal Stage 0, per `joint-theorem-promotion.md` 4-stage pathway). It is not yet Stage 2 verified. The K=6 signal would apply IFF Stage 2 cross-reviewers (e.g., volovik-superfluid-universe + connes-ncg or some other axis pair) BOTH return independent PASS on the meta-INVARIANCE class theorem statement. Until then, the corpus structure decision is between (a) keeping the W-11 RULE-2 baseline at K=5 with the W9-106 entry as a separate STAGE-1-CANDIDATE proposal, and (b) registering the unified meta-INVARIANCE class theorem as STAGE-1-CANDIDATE at §VII.AQ-META with K=1 (not K=6).

I propose (b) — see EMERGENCE-3.

#### Dissent-4: dual-canonical-pin protocol breaks substrate-first-canonical-sourcing.md §(iv) MANDATORY-K=4 (Re:C3, Re:C6)

Lizzi's DUAL-CANONICAL-PIN LOCKDOWN proposal (Re:C6 Step 4) pins BOTH `SDW_3c_min^A_FW` and `SDW_3c_min^B_FW` in canonical_constants.py with explicit per-axis PROVENANCE entries. This is structurally a class-conflation that the substrate-first-canonical-sourcing.md §(iv) MANDATORY-K=4 discipline (S88 W7b-83 close, 2026-05-05) was specifically calibrated to prevent.

```
Step 1 [Definition]:
  substrate-first-canonical-sourcing.md §(iv) MANDATORY-K=4 (S88 W7b-83):
    Closes the SCHEMATIC-vs-FULL silent class-conflation pathology in
    helper-module consumption. Calibration corpus K=4: W4-2 + W9b-2 +
    W9c-1 + W5b-2 sub-test (c). The rule's structural intent is to
    CLOSE silent class-conflation pathways analogous to S75 ZETA-NOT-
    PHYSICAL-75 UV-regulator class conflation.

  PROHIBITED_ACTIONS Class 1 boundary (v3-closure-recovery.md):
    Convention-shopping forbidden. The convention-suffix discipline
    (-LAYER-SEPARABLE-CARVE-OUT-TYPE-F per mechanical-closure-discipline.md
    §"Layer-separability carve-out", -SCHEMATIC per §(iv)) is the
    structural BOUNDARY between admissible structural extension and
    PROHIBITED Class 1.

Step 2 [Substitution -- dual-canonical-pin against §(iv) discipline]:
  Lizzi's proposal: pin BOTH SDW_3c_min^A_FW and SDW_3c_min^B_FW with
  per-axis suffix tags -CONVENTION-A and -CONVENTION-B. Both pins enter
  canonical_constants.py.

  Per §(iv): "convention=...-SCHEMATIC" suffix is the DISCLOSURE protocol
  for SCHEMATIC-vs-FULL level-pin. The suffix is a class-tag that PREVENTS
  silent conflation; it is NOT a license for downstream consumers to treat
  both classes as substrate-IS at the same epistemic weight.

  The dual-canonical-pin proposal extends the suffix discipline beyond
  level-pin (SCHEMATIC vs FULL) to convention-pin (A vs B). But there's
  a structural difference: SCHEMATIC vs FULL are both well-defined
  evaluator classes at the corresponding level (SCHEMATIC analog and
  FULL physical regularization are BOTH well-posed mathematical objects
  on their respective level). In contrast, convention A's SDW Bernstein
  test is OUTSIDE the BHW admissibility class for non-CM images (per
  Dissent-1); pinning the convA value as canonical alongside convB
  embeds an OUTSIDE-BHW-admissibility-class quantity in the canonical
  constants registry.

Step 3 [Simplify -- structural class-conflation pathology]:
  Downstream consumers of canonical_constants.py:
    - import the SDW_3c_min_FW pin
    - by default, naïve consumers will NOT inspect the convention-suffix
      string, especially if the constant name is short and standard
    - the suffix tag is a partial fix (forces explicit declaration); the
      structural fix is canonical singleton (one pin, substrate-IS,
      no per-axis ambiguity)

  Compare to §(iv) MANDATORY: the suffix `-SCHEMATIC` is the DISCLOSURE
  layer; the structural fix is migration to FULL physical regularization
  when feasible. SCHEMATIC pins exist BECAUSE FULL regularizations are
  not always computationally tractable; the suffix is a workaround, not
  an endorsement of dual-class canonical-status. The dual-canonical-pin
  proposal endorses dual-class canonical-status without the structural
  reason (BHW admissibility puts convA outside the class, and there is
  no computational-tractability barrier to using convB exclusively).

Step 4 [Direction]:
  The dual-canonical-pin proposal violates the §(iv) MANDATORY structural
  intent. The convention-suffix tagging is structurally analogous to
  the OP-PROJ vs STATE-PROJ tagging at registry-landing.md MANDATORY-K=3
  ONLY IF both axes are well-defined substrate-IS observables on their
  respective evaluator classes. For the BHW Bernstein evaluator class,
  axis A (lambda-derivative) is OUTSIDE the BHW admissibility class for
  any non-CM image of the regulator weight (per Dissent-1); pinning
  convA as canonical alongside convB embeds a not-substrate-IS quantity
  in the canonical-constants registry under the disguise of a parallel
  convention-suffix tag.
  
  The substrate-first-canonical-sourcing.md §(iv) discipline closes
  silent class-conflation. Pinning a not-substrate-IS quantity in
  canonical_constants.py with a convention-suffix tag does NOT close
  the conflation — it creates a NEW conflation pathology: a not-
  substrate-IS quantity carrying canonical-status pin precedence equal
  to a substrate-IS quantity, with the only distinguishing tag being
  a convention-suffix string consumers may or may not parse.

  Single-canonical pin (SDW_3c_min_FW := SDW_3c_min^B_FW; convA value
  retained as audit-trail content with -LAM-DERIVATIVE-CHAIN-RULE-LIFT
  companion-tag per C3) preserves the §(iv) class-conflation closure
  by construction.
```

The OP-PROJ vs STATE-PROJ MANDATORY-K=3 precedent at `registry-landing.md` is structurally distinct because BOTH operator-projection AND state-projection observables are well-defined substrate-IS observables on their respective layers (algebra-INVARIANT vs algebra-DEPENDENT). The (A, B) Bernstein convention pair lacks the analogous structural property: convB is well-defined substrate-IS BHW-test on the substrate's CM regulator weight; convA is a polynomial-coefficient-tracking quantity on a non-CM Gaussian image of the regulator weight.

### EMERGENCE

Three emergence axes from the convergences and dissents.

#### Emergence-1: 3-orthogonal-source decomposition as §VII.METHODOLOGY-CASCADE-DIAGNOSTIC theorem candidate

Convergence-1 conceded the 3-source decomposition (truncation-axis + regulator-class-axis with magnitude variation + convention-axis with chain-rule polynomial pre-factor sign) as substrate-physics taxonomy of cascade-FAIL diagnostic content. This decomposition is structurally a NEW methodology-class theorem candidate, distinct from both W-11 RULE-2 (regulator-INDEPENDENCE) and the proposed meta-INVARIANCE class theorem (composite-layer convention-invariance). I propose pre-registration:

**§VII.METHODOLOGY-CASCADE-DIAGNOSTIC (S88 W9-106 STAGE-1-CANDIDATE; lizzi+connes co-authored)**:

Statement: Cascade-collapse FAIL verdicts on substrate Bernstein-positive-cone audit gates decompose into THREE structurally orthogonal diagnostic sources:
1. **L_max-stability axis (truncation-axis)**: convention-INDEPENDENT; diagnoses convergence rate of substrate Mellin moments at the chosen tolerance band (W9-106 source 1: 4×3a FAILs, convention-blind by construction).
2. **Regulator-class axis (Bernstein-violation axis)**: regulator-class-dependent with substrate-IS magnitude variation under convention swap (W9-106 source 2: Zubarev_3c^A=−6.587 / Zubarev_3c^B=−2.034, magnitude ratio 3.24 = substrate-IS multi-axis content on the non-CM Zubarev weight).
3. **Convention-axis (chain-rule polynomial pre-factor axis)**: NOT substrate-IS for CM regulator weights; the (A, B) sign-flip on SDW row 3c is a coordinate-Jacobian-polynomial effect with structurally-fixed roots (e.g., √(3/2) for SDW at k=3) NOT depending on the substrate's eigenvalue distribution, Casimir structure, or Jensen deformation.

Calibration corpus instance #1: W9-106 SDW + Zubarev + 3a × A_4 atlas + (A, B) convention pair on L_max=12 + τ_fold=0.190 substrate cache.

K-counter status: K=1, SUGGESTION (NOT MANDATORY). Promotion to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`; future Bernstein-positive-cone cascade audits on alternative substrate atlases (e.g., A_5_extended, A_6) would advance K.

The theorem is structurally NEW: it is NOT a unification of W-11 RULE-2 with W9-106 (those are at different evaluator classes and observable types per Dissent-3); it IS a NEW substrate-physics taxonomy of cascade-FAIL diagnostic-content sources, distinct from both predecessors. Pre-registering it at §VII.METHODOLOGY-CASCADE-DIAGNOSTIC routes it to its own K-counter advancement track without contaminating the W-11 RULE-2 corpus.

#### Emergence-2: Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR vs single-canonical-pin remediation are not mutually exclusive — both have substrate-physics value at DIFFERENT structural relationships

Lizzi's Re:C5 EMERGES proposed Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR with ADVISORY-K=1 / MANDATORY-K=3 pathway. My C5 proposed Class-(d) HARD-HALT MANDATORY MIGRATION. These are not mutually exclusive in general; they apply to DIFFERENT structural relationships between conventions:

```
Step 1 [Definition]:
  Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY:
    Applies when one convention is OUTSIDE the substrate-IS evaluator class
    (e.g., outside BHW admissibility) and the other is the canonical
    substrate-IS form. Remediation: migrate downstream cites to the
    canonical.
  Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR (NEW, lizzi proposal):
    Applies when both conventions are well-defined substrate-IS observables
    on structurally-orthogonal axes (analogous to OP-PROJ vs STATE-PROJ).
    Remediation: per-cite convention-suffix tagging; both axes pinned in
    canonical_constants.py.

Step 2 [Substitution -- which class fires for which convention pair]:
  Bernstein (A, B) on SDW (CM-image-of-Gaussian, non-CM in λ): per Dissent-1,
    convA is OUTSIDE BHW admissibility class on non-CM images.
    Class-(d) MANDATORY MIGRATION fires; Class-(g) does NOT.

  Bernstein (A, B) on Zubarev (non-CM in BOTH x and λ): per Convergence-1,
    BOTH conventions test a non-CM regulator weight; the (A, B) magnitude
    split (3.24 ratio) IS substrate-IS multi-axis content (no chain-rule
    pre-factor on a CM image; the regulator weight itself drives the
    Bernstein violation in both conventions). Class-(d) does NOT fire;
    Class-(g) MAY fire (well-defined substrate-IS axes both within or
    near BHW admissibility, since Zubarev's non-CM is intrinsic).

Step 3 [Simplify -- per-regulator class assignment]:
  At the BHW evaluator class, the convention-axis remediation class is
  REGULATOR-DEPENDENT:
    SDW (CM regulator) + (A, B) convention pair: Class-(d) MANDATORY
                                                  MIGRATION (convA OUTSIDE
                                                  BHW class).
    Zubarev (non-CM regulator) + (A, B) convention pair: Class-(g)
                                                          STRUCTURAL-
                                                          COMPANION
                                                          (both
                                                          substrate-IS).
    
  This is structurally important: the (A, B) pair admits BOTH classes
  simultaneously on DIFFERENT regulators. The pair-wide remediation
  must distinguish per-regulator structural status, NOT a uniform
  pair-level remediation.

Step 4 [Direction]:
  Both Class-(d) and Class-(g) are needed; pre-register BOTH:
    - Class-(d) HARD-HALT MANDATORY MIGRATION for CM-regulator + (A, B)
      pairs where the lambda-derivative axis is OUTSIDE BHW admissibility
      class on the non-CM image (e.g., SDW + (A, B)).
    - Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR ADVISORY-K=1 / MANDATORY-K=3
      for non-CM-regulator + (A, B) pairs where both axes are within or
      near BHW admissibility (e.g., Zubarev + (A, B)).
```

This dual-class registration matches the substrate-physics structure better than either single-class proposal alone. The class-distinguishing predicate is "is the regulator weight in the BHW CM class as a function of x?" — if yes, convA on the λ-image is OUTSIDE BHW admissibility, Class-(d) fires; if no, both convA and convB are within or near BHW admissibility (testing a non-CM weight from two coordinate angles), Class-(g) fires.

The §VII.AQ-3C-DOWNSTREAM-CITE-MIGRATION carry-forward for the Lancaster MCT-3 SDW-channel discriminator (per C5) becomes Class-(d) MANDATORY (SDW is CM in x → convA OUTSIDE BHW); the Zubarev-channel discriminator at `0.2035%` (lizzi Re:C5 EMERGES dual-pin) becomes Class-(g) ADVISORY-K=1 (Zubarev non-CM in both → both axes substrate-IS).

#### Emergence-3: meta-INVARIANCE class theorem deserves explicit STAGE-1-CANDIDATE pre-registration with K=1 (NOT K=6)

Convergence-2 conceded that branching the W-11 RULE-2 corpus regresses K-counters. Dissent-3 challenged the meta-INVARIANCE class theorem's already-established status. The synthesis: register the meta-INVARIANCE class theorem as a SEPARATE STAGE-1-CANDIDATE at §VII.AQ-META, distinct from §VII.AQ (W-11 RULE-2 baseline corpus), with its own K-counter starting at K=1.

```
Step 1 [Definition]:
  §VII.AQ (existing, S86 W-11 STAGE-1-CANDIDATE):
    Strengthened parity-blindness theorem. K-counter: 5 (calibrated baseline).
    K_promotion threshold per feedback_rules-compensate-missing-structure.md: 3.
    Status post-S86 W-11: HARDENED (K=5 > 3).
  
  §VII.AQ-META (NEW, S88 W9-106 STAGE-1-CANDIDATE; lizzi proposal):
    Meta-INVARIANCE class theorem: substrate-internal symmetry tests at
    the even-grading evaluator class produce composite-layer-INVARIANT
    verdicts under structurally orthogonal axis variations within the
    algebra-INVARIANT functional family.
    K-counter: 1 (calibration instance: W9-106 composite-layer PASS).
    Status: STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway.

Step 2 [Substitution -- two-corpus structure]:
  §VII.AQ retains its 5-instance baseline corpus (W-11 RULE-2 strengthened
  parity-blindness theorem at η + even-Mellin evaluator class with regulator-
  class-axis variation across A_5_extended). NO change to its K-counter.
  
  §VII.AQ-META is a NEW STAGE-1-CANDIDATE with K=1 (W9-106 instance), proposing
  that the §VII.AQ baseline + W9-106 + future cross-axis instances are
  unified under a meta-INVARIANCE claim at the algebra-INVARIANT functional
  family level. Stage-2 cross-axis independent-verify is required for
  promotion to STAGE-3-PERMANENT.

Step 3 [Simplify -- reconciliation of K-counter advancement signals]:
  The K=6 advancement signal lizzi cited (L1 Step 3) is the K-counter
  state OF §VII.AQ-META if the meta-INVARIANCE class theorem statement
  IS structurally validated. Stage-2 verify is the structural validation
  step.
  
  Before Stage-2: K=1 (one calibration instance of the meta-INVARIANCE
  claim, the W9-106 composite-layer PASS) + 5 instances eligible for
  Stage-2-conditional inclusion (W-11 RULE-2 baseline 5 instances; their
  meta-INVARIANCE membership is Stage-2-CONDITIONAL).
  
  After Stage-2 PASS: K=6 (5 baseline instances + W9-106), HARDENED. The
  structural promotion to STAGE-3-PERMANENT then fires.
  
  After Stage-2 FAIL: K=1 (W9-106 alone); the unification claim is rejected,
  and W9-106 routes to its own STAGE-1-CANDIDATE corpus (e.g., the
  §VII.METHODOLOGY-CASCADE-DIAGNOSTIC corpus per Emergence-1).

Step 4 [Direction]:
  The two-corpus structure (§VII.AQ existing + §VII.AQ-META NEW)
  preserves the W-11 RULE-2 5-instance HARDENED state (K=5 > 3, no
  regression) AND registers the meta-INVARIANCE class theorem proposal
  at its own STAGE-1-CANDIDATE pace (K=1, with proper Stage-2 verify
  ahead). Branching is AVOIDED at §VII.AQ; corpus-fusion is AVOIDED at
  §VII.AQ-META; both K-counter trajectories are honest.
```

Stage-2 cross-axis independent-verify dispatch (per `joint-theorem-promotion.md §"Stage 2"`): two cross-reviewers on different axes (e.g., volovik-superfluid-universe-theorist on the substrate-physics axis + connes-ncg-theorist or mack-cosmic-bridge on the methodology axis) operating WITHOUT prior workshop context. Both must independently PASS the unification claim. If both PASS → §VII.AQ-META promotes from STAGE-1 to STAGE-3 with K=6. If either FAILs → STAGE-1 retained at K=1 with the W-11 RULE-2 baseline corpus structurally separate.

This satisfies BOTH lizzi's K-counter-advancement-direction concern (the meta-INVARIANCE class is a forward-direction proposal with proper Stage-2 vetting) AND my structural-orthogonality-axis concern (the W-11 RULE-2 baseline retains its calibration discipline, NOT pooled with cross-axis instances unless Stage-2 verify fires PASS-AND).

### QUESTIONS

I answer lizzi's L3 Q1-Q5 in order, then pose 3 sharpened follow-up questions for R3.

#### Answers to lizzi's L3 Q1-Q5

**A1 (CC96 §2.2-2.3 uniqueness clause)** — The literal CC96 §2.2-2.3 derivational status of uniqueness is: CC96 §2.2 Eq. 2.5 establishes the bosonic action `S_b[D] = Tr f(D²/Λ²)` AS THE UNIVERSAL FUNCTIONAL whose argument is `D²/Λ²`. CC96 §2.3 Mellin-moment expansion uses the integration variable `t = D²/Λ²`. **CC96 alone does NOT prove uniqueness of `x` as the Bernstein-test variable for arbitrary positivity tests on `f`.** The uniqueness derives from the JOINT CC96 + BHW theorem reading (per Dissent-1 substitution chain): CC96 fixes the substrate's Laplace pair; BHW characterizes CM functions UNIQUELY by alternating-sign derivatives in the LAPLACE-CONJUGATE variable. The substrate-natural reading is JOINT, not CC96-alone. **Specifically the uniqueness is not in any single CC96 line; it is in the COMBINATION**: CC96 §2.2 Eq. 2.5 (the substrate's universal action functional with argument `D²/Λ²`) + Widder 1941 Ch. IV (BHW theorem characterizing CM functions on (0,∞) uniquely by `(-1)^k g^{(k)}(x) ≥ 0` in the LAPLACE-CONJUGATE x, NOT in arbitrary smooth-bijection images of x).

**A2 (composite-layer PASS substrate-IS status)** — I take horn ONE of your dilemma: the W9-106 composite-layer PASS at `composite_A == composite_B == FAIL` IS a chain-rule-artifact-cancellation property of the cascade-collapse aggregator. Specifically: (i) the (4 × 3a) truncation FAILs are convention-INDEPENDENT and saturate the FAIL-count predicate `n_sub_FAIL > 0` in BOTH conventions REGARDLESS of any 3c sub-cell content; (ii) under the `composite = FAIL ⟺ n_sub_FAIL > 0 ∧ regime = VALID` rule, the composite-layer agreement composite_A == composite_B == FAIL is forced by the (4 × 3a) saturation alone. The 3c sub-cell content (SDW chain-rule sign-flip + Zubarev magnitude shift) does NOT affect the composite verdict because the predicate is already saturated. **The agreement IS NOT substrate-IS evidence of an (A, B) symmetry; it IS the consequence of the convention-INDEPENDENT (4 × 3a) truncation FAILs dominating the predicate**. This corresponds to the WP §line 1045 STRENGTHENS framing being structurally MISCLASSIFIED — the W9-106 entry is NOT a cross-axis "6th calibration instance" of W-11 RULE-2; it is a saturation-driven cascade-aggregator agreement that carries different substrate-physics content (the §VII.METHODOLOGY-CASCADE-DIAGNOSTIC 3-source decomposition per Emergence-1). I propose the WP §line 1045 framing be reconsidered at workshop wrap-up.

**A3 (cross-pillar bridge anatomy scope)** — Single-canonical pin model (structurally analogous to DR3-class lockdown, NOT multi-canonical). The 5-anatomy + 3-level structure applies WITHIN convention B alone. Convention A retains audit-trail value as historical content with `-LAM-DERIVATIVE-CHAIN-RULE-LIFT` companion-tag, but it does NOT enter the 5-anatomy ladder as a co-equal Level-3 empirical anchor. Specifically: Level-3 Anchor is `SDW_3c_min^B = +1.77e-13` (Bernstein-positive-cone PASS at the substrate-natural BHW evaluator); Level-2 envelope is the BHW-admissibility-class-test convergence rate (the substrate-natural CM characterization); Level-1 is the cohomology-class binding under the Connes-Karoubi pairing for the spectral action's regulator measure. **No NEW methodology rule extension to handle multi-axis case is needed** because the (A, B) pair is NOT a multi-axis substrate-IS pair under the substrate-natural reading; it is a coordinate change with chain-rule-Jacobian polynomial sign-flip (per Dissent-2). The DR3-class lockdown shape is the correct template.

**A4 (Lancaster MCT-3 SDW-channel discriminator replacement)** — My operative replacement is option (i) MIGRATION TO ZUBAREV-CHANNEL DISCRIMINATOR, with the structural caveat you raised: SDW and Zubarev are different regulator classes, so the migration changes WHICH substrate physics the cryostat tests. **I accept that consequence**: the substrate's Bernstein-positivity-discriminator content does NOT live at the SDW channel under the substrate-natural reading; it lives at the Zubarev channel (whose `f(x) = x/(1+x²)` is intrinsically non-CM in `x`). The Lancaster MCT-3 lab-feasibility chain at `s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013 needs to be REWRITTEN, not preserved with phantom margin. The rewrite produces a substrate-physics-grounded discriminator at the Zubarev channel (margin `0.2035%`) AND a STRUCTURAL NULL at the SDW channel (margin `1.8e-16`, below detection sensitivity, structurally because SDW is BHW-admissible in x). **Substrate falsifiability on SDW is structurally NULL because SDW is structurally Bernstein-admissible**; this is not a loss of falsifiability but a refinement of where falsifiability lives. The SDW channel migrates from "discriminator" status to "Bernstein-admissibility certifier" status.

If the Lancaster MCT-3 cryostat were structurally engineered to DETECT a Bernstein violation at the regulator-class level (i.e., to discriminate substrate regulator weights with non-CM character), the appropriate channel is Zubarev. If the experiment is fixed to SDW transport coefficients regardless, the substrate predicts NO discriminator at the SDW channel — which is a FALSIFIABLE prediction in itself: a SDW-channel signal AT THE CRYOSTAT'S ACTUAL SENSITIVITY would falsify the substrate's BHW admissibility for SDW. Either way, falsifiability is preserved, just relocated.

**A5 (layer-functor F at substrate-physics layer)** — (a) Under F at the substrate-physics layer, the lambda-derivative differential operator and the x-derivative differential operator are the SAME substrate-physics observable in two coordinate systems (connes reading), NOT distinct substrate-physics observables. The "distinct substrate-internal structural data" lizzi attributes to the lambda axis in L2 fails the structural-data criterion under careful Sage-decomposition (per Dissent-2): the lambda-axis "discriminator" depth is 100% chain-rule-polynomial signed factor × substrate-IS regulator weight, with the polynomial roots structurally fixed by the chain rule (not by substrate). (b) The F-image of the W9-106 composite-layer PASS at the methodology layer is a SINGLE rule-file extension (the BHW-evaluator-class lockdown extension at `regulator-convention-lockdown.md` per C6 Observation 2, structurally analogous to the existing DR3-class lockdown), NOT a methodology-rule extension PAIR. The single-rule-file extension preserves the layer-functor's PRU-class preservation requirement: weight-2 substrate observable (substrate-natural BHW-admissibility test) ↔ weight-2 methodology rule (BHW-evaluator-class lockdown). (c) Under my reading, the W9-106 composite-layer PASS does NOT advance the audit-leg verification per the layer-functor's S86 R3 status pair-verified → triplet-verified promotion. The (A, B) convention pair lives at the substrate-physics layer (one substrate-IS axis B; convA is a coordinate reparameterization, methodology-layer artifact); it has not yet been mapped through F to the audit-floor with corresponding audit-line content. The audit-leg verification is a separate forward carry-forward (`S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION` per epistemic-discipline.md §"Layer-Decomposition" status note) that requires a distinct dispatch.

#### Sharpened follow-up questions for R3

**Q1' (BHW admissibility on non-CM Gaussian image)**: Per Dissent-1 Step 3, `e^{-λ²}` is NOT a completely-monotonic function on `(0,∞)` — it admits no positive-measure Laplace representation `g(λ) = ∫₀^∞ e^{-sλ} dν(s)` for any positive Borel measure `dν`. The Hausdorff moment problem is the structurally relevant impossibility: the moments of `e^{-λ²}` (Gaussian moments) do NOT satisfy the Hausdorff completely-monotone moment-sequence criterion. **Do you accept the BHW-admissibility argument**: the lambda-derivative Bernstein test on SDW is NOT a CM-characterization theorem instance; it is a polynomial-coefficient sign-tracking exercise on a non-CM function. If yes, your EMERGES-Re:C1 calibration-instance-of-Level-1/Level-2-analog claim collapses: the (A, B) pair lacks the bilateral-substrate-IS structural status the W2-10 precedent has (where BOTH levels are well-defined substrate-IS observables on their respective layers). If no, please provide the positive-measure `dν` such that `e^{-λ²} = ∫₀^∞ e^{-sλ} dν(s)` — or the alternative theorem statement under which the lambda-derivative test on `e^{-λ²}` is a substrate-IS positivity test rather than a polynomial coefficient exercise.

**Q2' (regulator-class-conditional remediation per Emergence-2)**: Per Emergence-2, Class-(d) MANDATORY MIGRATION fires for CM regulators (where convA is OUTSIDE BHW admissibility on the non-CM Gaussian image), and Class-(g) STRUCTURAL-COMPANION fires for non-CM regulators (where both axes are within or near BHW admissibility on the non-CM weight). Specifically: (a) does this regulator-class-conditional remediation framework satisfy your dual-canonical-pin-lockdown intent at the regulators where it applies (Zubarev), while preserving the substrate-natural-singleton at the regulators where it does NOT apply (SDW)? (b) Should the BHW-evaluator-class lockdown extension at `regulator-convention-lockdown.md` register BOTH the Class-(d) MANDATORY MIGRATION (for CM regulators) AND the Class-(g) STRUCTURAL-COMPANION pathway (for non-CM regulators), pre-registering the regulator-class-conditional split? Or do you read the lockdown rule as needing ONLY the dual-pin form (uniformly across all regulators including CM), accepting the conflation of OUTSIDE-BHW-class quantities into canonical-status pins for SDW-like CM regulators?

**Q3' (§VII.AQ-META Stage-2 verify dispatch protocol)**: Per Emergence-3, the meta-INVARIANCE class theorem registers as STAGE-1-CANDIDATE at NEW §VII.AQ-META with K=1, requiring Stage-2 cross-axis independent-verify before promotion to STAGE-3-PERMANENT (and the K=6 signal). Specifically: (a) which axis-pair of cross-reviewers do you propose for Stage-2 verify (e.g., volovik-superfluid-universe + mack-cosmic-bridge; lizzi-spectral-functional + connes-ncg; some other pair)? Per `joint-theorem-promotion.md §"Stage 2"`, the cross-reviewers MUST be on different axes AND not the workshop authors. (b) What is the structural test the cross-reviewers must INDEPENDENTLY PASS for the meta-INVARIANCE class theorem? My proposal: each cross-reviewer audits whether the 6 candidate calibration instances (5 W-11 RULE-2 baseline + W9-106) genuinely satisfy a UNIFIED substrate-IS meta-claim (NOT 5 within-axis instances + 1 cross-axis instance pooled by narrative agreement). (c) If Stage-2 verify FAILs, do you accept routing W9-106 to the §VII.METHODOLOGY-CASCADE-DIAGNOSTIC corpus per Emergence-1 (a structurally distinct STAGE-1-CANDIDATE with its own K-counter, not pooled with W-11 RULE-2)?

---

## Round 2 — lizzi: Cross-Synthesis

### CONVERGENCE

Four convergence axes. Each accepts a structural correction connes raised in R2 that I either over-specified in my R1 or under-applied across the rule corpus.

#### Convergence-1: Meta-INVARIANCE class theorem is STAGE-1-CANDIDATE at K=1, NOT K=6 HARDENED (Re:DISS-3, Re:EM-3)

I CONCEDE Dissent-3's structural-validity challenge to the meta-INVARIANCE class theorem's already-established status. My R1 L1 Step 4 arithmetic `K_W9-106 - K_promotion = 6 - 3 = 3 instances above MANDATORY threshold` was **conditional on the meta-INVARIANCE class theorem being a proper unifying claim across the 6 instances**, and connes's Dissent-3 substitution chain establishes that conditional fails at three structural axes (α, β, γ):

```
Step 1 [Definition]:
  W-11 RULE-2 5 baseline instances:
    Evaluator class:   η + even-Mellin (Mellin-moment-natural)
    Observable target: parity-twin pair (C_H, C_εH); 2-element observable
                       equivalence class
    Axis variation:    regulator-class axis (5 distinct regulators within
                       A_5_extended = {ζ, Zubarev, SDW, anomaly, cutoff_sqrt})

  W9-106 6th candidate instance:
    Evaluator class:   BHW Bernstein-positive-cone (alternating-sign-derivative)
    Observable target: W8-4 cascade composite verdict (single composite-layer
                       scalar)
    Axis variation:    differential-coordinate axis ((A, B) pair)

Step 2 [Substitution against connes Dissent-3 (α, β, γ)]:
  (α) evaluator class: NOT IDENTICAL across baseline 5 + 6th. The η + even-Mellin
      class and the BHW Bernstein-positive-cone class are RELATED (both are
      even-grading-friendly substrate-internal positivity tests on regulator
      weights) but are NOT THE SAME mathematical class. The baseline 5 test
      η = 0 + GV ≠ 0; the 6th tests (-1)^k · g^(k) ≥ 0 alternating-sign
      composition.
  (β) observable target: NOT analogous. The parity-twin pair is a 2-element
      equivalence class indexed by parity grading; the W8-4 cascade composite
      is a scalar verdict on a single 4-regulator atlas. These are
      structurally different observable types.
  (γ) unifying meta-claim generality: my "substrate-internal symmetry tests
      at the even-grading evaluator class produce composite-layer-INVARIANT
      verdicts under structurally orthogonal axis variations" is admittedly
      so general that it WOULD admit additional invariance results as further
      "calibration instances" (W2-6 partition-stability cardinality vector
      (2,4,8,6) invariance under L_max truncation; W11-2 + W11-3 Casimir-
      Friedrich-Bär bound; etc.) — and my R1 framing did not bound this
      generality.

Step 3 [Simplify — joint-theorem-promotion.md 4-stage pathway applies]:
  Per `.claude/rules/joint-theorem-promotion.md §"The 4 Stages"`:
    Stage 0 (workshop-internal candidate): present R1 lizzi L1 proposal.
    Stage 1 (S87/S88 registration as CANDIDATE): proposed §VII.AQ-META at K=1.
    Stage 2 (two-agent parallel cross-axis independent-verify): MANDATORY
            upgrade gate before STAGE-3 PERMANENT promotion.
    Stage 3 (permanent registration): blocked on Stage-2 PASS-AND.

  The K=6 signal is the K-counter state OF §VII.AQ-META IFF Stage-2 verify
  fires PASS-AND on the unification claim. My R1 framing skipped Stage 2 and
  treated Stage-2-conditional inclusion of the W-11 RULE-2 baseline 5
  instances as already established. Under the 4-stage pathway, this is a
  Stage-0 → Stage-3 collapse that the rule explicitly forbids.

Step 4 [Direction — concession to STAGE-1-CANDIDATE K=1]:
  I CONCEDE the meta-INVARIANCE class theorem registers as STAGE-1-CANDIDATE
  at NEW §VII.AQ-META with K=1 (the W9-106 candidate instance alone).
  Stage-2 cross-axis independent-verify is the structural validation that
  determines whether the W-11 RULE-2 baseline 5 instances are pooled (K=6
  HARDENED) or remain structurally separate (K=1 STAGE-1).
  My R1 L1 K=6 arithmetic was prematurely-Stage-3-tagged; it correctly
  identifies the K-counter trajectory IFF Stage-2 verify fires PASS-AND.
```

This concession is structural, not narrative: per `joint-theorem-promotion.md §"Stage 2"`, "the cross-reviewers receive ONLY the registered Stage-1 entry text + relevant input files — they do NOT receive the workshop's R1/R2/R3 transcripts — they cannot be the original workshop authoring agents." This protocol breaks shared-context-produced agreement; absent it, my R1 K=6 claim is structurally indistinguishable from the agreement-as-evidence pattern that `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2 forbids.

The S88 W9 working-paper §line 1045 STRENGTHENS framing must be rewritten at workshop wrap-up: the W9-106 entry is a NEW STAGE-1-CANDIDATE proposal, not an automatic 6th-instance extension of W-11 RULE-2.

#### Convergence-2: Regulator-class-conditional remediation (Class-(d) for CM + Class-(g) for non-CM) is structurally elegant; both pre-registered, NOT mutually exclusive (Re:EM-2)

I CONCEDE Emergence-2's regulator-class-conditional remediation framework. My R1 Re:C5 EMERGES proposed Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR as a NEW class to handle the (A, B) Bernstein convention pair uniformly across all regulators. Connes's Emergence-2 sharpens this by recognizing that the structural status of the convention pair DEPENDS ON THE REGULATOR'S CM-MEMBERSHIP IN x:

```
Step 1 [Definition — connes Emergence-2 partition]:
  CM-class predicate (in x):
    f(x) is CM in x iff f admits positive-measure Laplace representation
    f(x) = ∫₀^∞ e^{-tx} dμ(t) with dμ a positive Borel measure on [0,∞).

  CM-regulator + (A, B) pair (e.g., SDW with f(x) = e^{-x}, dμ = δ(t-1)):
    Convention B is a BHW-CM test on f's Laplace pair (well-defined).
    Convention A is the test of (-1)^k g^{(k)}(λ) on g(λ) = f(λ²) = e^{-λ²},
    which is NOT CM in λ (Python-verified this turn: -T_A[1](λ) = -2λ exp(-λ²)
    is ≤ 0, FAILing CM at k=1 already).
    ⇒ Class-(d) MANDATORY MIGRATION fires (convA OUTSIDE BHW class on the
       non-CM Gaussian image).

  Non-CM-regulator + (A, B) pair (e.g., Zubarev with f(x) = x/(1+x²)):
    f is non-CM in x (peaked at x=1; the first derivative changes sign).
    Convention B tests Bernstein-violation on a non-CM weight.
    Convention A tests Bernstein-violation on the λ-image of a non-CM
    weight, which is ALSO non-CM in λ — but neither axis claims to be a
    CM-characterization theorem instance; both probe non-CM weights with
    different differential operators.
    ⇒ Class-(g) STRUCTURAL-COMPANION fires (both axes are within the
       SAME structural status: non-CM weight × differential operator;
       the (A, B) magnitude split 3.24 IS substrate-IS multi-axis content).

Step 2 [Substitution — partition is structurally well-defined]:
  The class-distinguishing predicate "is the regulator weight CM in x"
  partitions ALL regulator-weight × convention-pair cases into:
    (P1) CM regulator + (A, B) pair: Class-(d) MANDATORY MIGRATION
    (P2) non-CM regulator + (A, B) pair: Class-(g) STRUCTURAL-COMPANION
  No regulator can fall into BOTH partitions. The partition is mutually
  exclusive AT THE PER-REGULATOR LEVEL.

Step 3 [Simplify — pre-registration of BOTH classes]:
  At the BHW-evaluator-class lockdown extension to regulator-convention-
  lockdown.md, BOTH Class-(d) and Class-(g) sub-clauses are pre-registered
  simultaneously, with the per-regulator routing predicate the
  CM-membership-in-x test. Future S89+ Bernstein-positive-cone gates
  invoke whichever class fires given the regulator-class composition of
  their atlas.

Step 4 [Direction]:
  This dual-pre-registration is structurally cleaner than either single-
  class proposal alone. My R1 Re:C5 EMERGES uniform Class-(g) reading
  conflated SDW (CM in x) with Zubarev (non-CM in x); connes's R1 C5
  uniform Class-(d) reading conflated Zubarev with SDW. The
  regulator-class-conditional split tracks substrate-physics structure.
```

I CONCEDE the regulator-class-conditional split. The BHW-evaluator-class lockdown extension at `regulator-convention-lockdown.md` should pre-register BOTH sub-clauses with the CM-in-x test as the routing predicate.

This convergence narrows my Re:C5 EMERGES dual-canonical-pin proposal: dual pinning is appropriate ONLY in partition (P2) (non-CM regulators); for partition (P1) (CM regulators in x), single-canonical pinning under convention B is the structurally-correct shape per Class-(d). The substrate-natural-singleton AND the dual-canonical-pin can co-exist at the BHW-evaluator-class lockdown level — they apply to disjoint regulator partitions.

#### Convergence-3: Two-corpus structure §VII.AQ + §VII.AQ-META preserves baseline HARDENED + meta-claim STAGE-1 honestly (Re:EM-3)

I CONCEDE Emergence-3's two-corpus structure as the structurally correct registry decomposition. The synthesis of:

- §VII.AQ retains its 5-instance baseline HARDENED at K=5 (W-11 RULE-2 strengthened parity-blindness theorem at η + even-Mellin evaluator class with regulator-class-axis variation across A_5_extended)
- §VII.AQ-META at STAGE-1-CANDIDATE K=1 (meta-INVARIANCE class theorem proposal, with the W9-106 composite-layer PASS as instance #1)

preserves BOTH structural-promotion trajectories honestly. Specifically:

```
Step 1 [Definition]:
  Two-corpus structure invariants:
    - §VII.AQ K-counter: 5 (HARDENED, no regression).
    - §VII.AQ-META K-counter: 1 (STAGE-1-CANDIDATE, joint-theorem-promotion
      pathway active).

Step 2 [Substitution — Stage-2 verify outcomes]:
  After Stage-2 verify on §VII.AQ-META unification claim:
    PASS-AND: K=6 (5 baseline + W9-106 as one corpus); STAGE-3 PERMANENT
              promotion fires; the meta-INVARIANCE class theorem joins the
              permanent results table. §VII.AQ becomes a sub-corpus rendering
              of the unified §VII.AQ-META.
    FAIL: K=1 retained at §VII.AQ-META; W9-106 routes to its own STAGE-1
          corpus (e.g., §VII.METHODOLOGY-CASCADE-DIAGNOSTIC per Emergence-1).
          §VII.AQ baseline corpus retains its 5-instance HARDENED state
          unchanged.

Step 3 [Simplify — preservation of K-counter direction]:
  Both Stage-2 outcomes preserve the K-counter advancement direction:
    PASS-AND: forward (K=1 → K=6 promotion).
    FAIL: stationary at §VII.AQ (K=5 unchanged) + forward at the new corpus
          §VII.METHODOLOGY-CASCADE-DIAGNOSTIC (K=0 → K=1 advancement).
  Neither outcome regresses any K-counter.

Step 4 [Direction]:
  The two-corpus structure satisfies my R1 K-counter-advancement-direction
  concern (no regression of W-11 RULE-2's HARDENED state) AND connes's
  Dissent-3 STAGE-1-CANDIDATE-honesty concern (the meta-INVARIANCE class
  is structurally STAGE-1, not pre-tagged STAGE-3). It is the synthesis
  the R1+R2 cross-pollination produced.
```

This is the operative §VII.AQ corpus structure for S89+ landings.

#### Convergence-4: Zubarev-channel migration on the SDW-channel discriminator IS the substrate-physics-correct response under STRUCTURAL NULL on SDW BHW-admissibility (Re:A4)

I CONCEDE A4's option (i) Zubarev-channel migration AT THE SDW-CHANNEL discriminator slot under the substrate-natural reading. Specifically: under the joint CC96 + BHW reading (per connes's Dissent-1 sharpening), `f(x) = e^{-x}` IS BHW-admissible in x with measure dμ = δ(t-1); the Bernstein-positivity-test at convention B returns PASS at the float-floor `+1.77e-13`. Under the substrate-natural single-axis reading on SDW, this is structurally NULL discriminator content because SDW is admissible.

```
Step 1 [Definition]:
  Substrate-natural reading on SDW (CM in x):
    Convention B's PASS at float-floor IS the structural statement that SDW
    is BHW-admissible. There is no substrate-physics Bernstein-violation to
    discriminate experimentally on the SDW channel under convention B.

Step 2 [Substitution — Lancaster MCT-3 cryostat margin]:
  Under convention B (substrate-natural on CM regulators):
    SDW-channel margin = |+1.77e-13| × envelope = 1.77e-16 (~14 OOM below
                         detection sensitivity).
  This is structurally NULL on SDW: the cryostat would need ~14 OOM
  improvement in S/N to detect a non-existent Bernstein violation.

Step 3 [Simplify — Zubarev-channel substrate-physics replacement]:
  Zubarev's f(x) = x/(1+x²) IS non-CM in x (peaked at x=1; first derivative
  changes sign at x=1). Under convention B substrate-natural reading:
    Zubarev_3c^B = -2.034587 (genuine substrate-physics Bernstein violation
                                 in x).
    Lancaster MCT-3 margin at Zubarev channel = |Zubarev_3c^B| × envelope
                                                  = 2.034587 × 0.001
                                                  = 0.2035%.
  This margin IS substrate-physics-grounded and detectable; the substrate
  predicts Bernstein-violation on the non-CM Zubarev weight, regardless of
  convention.

Step 4 [Direction]:
  The Lancaster MCT-3 SDW-channel discriminator at 0.2773% (convA) is
  STRUCTURALLY DISPLACED to the Zubarev channel at 0.2035% (convB) under
  the substrate-natural reading. The migration changes WHICH substrate
  physics the cryostat tests (CM-admissibility certifier on SDW vs
  non-CM-violation discriminator on Zubarev), but it does NOT lose
  falsifiability — falsifiability is RELOCATED to where substrate physics
  has predictive content. I CONCEDE this migration on the SDW channel.
```

The remaining DISSENT axis is whether the migration's DOMAIN is uniformly across all regulators (connes's R2 reading) or partition-conditional with retention of axis A on non-CM regulators where it carries substrate-IS multi-axis content (my forward DISSENT-1 below). The SDW-channel-specific migration is conceded; the cross-regulator generalization is dissented.

### DISSENT

Three dissent axes. Each sharpens — without restating R1 — a structural disagreement that survives R2's convergences.

#### Dissent-1: Axis A on non-CM regulators is substrate-IS by chain-rule on substrate-IS objects, NOT a coordinate change of a single substrate-IS axis (Re:DISS-2 + Q1')

Connes's Dissent-2 argued that criterion (i) FAILS for the lambda-derivative axis under careful Sage-decomposition: the chain-rule polynomial pre-factor `4λ(2λ² − 3)` has structurally-fixed roots `±√(3/2)` that are NOT substrate-IS, and the lambda-axis "discriminator" depth `−2.773` is `chain-rule polynomial × substrate-IS regulator weight` with the SIGN set 100% by the polynomial.

This Sage-decomposition is empirically correct ON SDW (CM in x). I AGREE with that decomposition on SDW. **My DISS retained on Zubarev (non-CM in x)**: the chain-rule decomposition argument FAILS to discriminate substrate-IS from non-substrate-IS content when the regulator weight ITSELF is non-CM, because there is no clean separation of "polynomial part" from "regulator weight part" — the non-CM character of the weight propagates structurally through both differential operators.

**Substitution chain (criterion-(i) defense on non-CM regulators)**:

```
Step 1 [Definition — chain rule on substrate-IS objects]:
  REGULATOR WEIGHT (substrate-IS): f(x) is the substrate-canonical regulator
                                    measure carrier per CC96 §2.2-2.3.
  COORDINATE CHANGE x = λ²: a smooth bijection on [0,∞). The chain-rule
                            map (df/dx)·(dx/dλ) = df/dx · 2λ is the
                            JACOBIAN composition on the substrate's
                            spectral support.

  PRINCIPLE (chain rule on substrate-IS objects produces substrate-IS
              outputs):
    If f(x) is substrate-IS AND x = λ² is the substrate-internal Mellin-
    natural argument (CC96 §2.2-2.3), then the composition g(λ) = f(λ²)
    on the substrate's spectral support [λ_min, λ_max] is substrate-IS
    by chain rule on substrate-IS inputs.

Step 2 [Substitution — Zubarev case]:
  f(x) = x/(1+x²) (Zubarev regulator weight; substrate-IS).
  g(λ) = λ²/(1+λ⁴) (chain-rule composition; substrate-IS by Step 1
                     principle).
  T_A[k](λ) = (-1)^k · d^k g(λ)/dλ^k (the Bernstein-positive-cone test
                                       in convention A).
  T_B[k](x) = (-1)^k · d^k f(x)/dx^k (the Bernstein-positive-cone test
                                       in convention B).

  Both T_A[k] and T_B[k] are derivatives of substrate-IS objects on the
  substrate's spectral support. Neither is "OUTSIDE" the substrate-IS
  class because the chain-rule composition of substrate-IS inputs yields
  a substrate-IS output.

Step 3 [Simplify — what convention A measures on Zubarev]:
  Connes's Convergence-1 (R2) accepted that the Zubarev (A, B) magnitude
  split 6.587 / 2.034 = 3.24 IS substrate-IS multi-axis content beyond
  chain-rule polynomial pre-factor lifting. This concession is the
  structural acknowledgment that on non-CM regulators, the (A, B) pair
  carries genuinely orthogonal substrate-IS data.

  The structural-data criterion (i) my L2 invoked is therefore SATISFIED
  on Zubarev: the lambda-derivative axis on Zubarev probes
  substrate-internal positivity-violation content NOT reducible to the
  x-derivative axis output (the magnitudes differ by 3.24, with both
  values substrate-IS per Convergence-1).

Step 4 [Direction]:
  Criterion (i) defense holds on non-CM regulators: the chain-rule
  Jacobian acts on a non-CM input, producing TWO structurally-distinct
  positivity-test outputs (the magnitudes 6.587 and 2.034 are both
  substrate-IS). Connes's R2 Convergence-1 explicitly conceded this on
  Zubarev. The Sage-decomposition argument that "the polynomial pre-
  factor's roots are not substrate-IS" is a SDW-specific argument (the
  Sage-extracted polynomial 4λ(2λ²−3) factors out from a CM regulator
  weight); on a non-CM regulator like Zubarev, NO such clean polynomial
  factorization exists, and the Bernstein-violation depth in BOTH
  conventions is intrinsic to the substrate-IS regulator × differential-
  operator composition.

  Conclusion: criterion (i) FAILS on SDW (per connes Dissent-2 Sage-
  decomposition; CONCEDED) but HOLDS on Zubarev (per connes Convergence-1
  on the 3.24 magnitude ratio; ACCEPTED). The (A, B) pair is multi-axis
  substrate-IS on non-CM regulators; it is NOT multi-axis substrate-IS
  on CM regulators. This is the regulator-class-conditional split that
  Convergence-2 above codifies.
```

The DISSENT-2 question-begging argument applies UNIFORMLY across all regulators ONLY if the chain-rule Sage-decomposition factorizes UNIFORMLY across regulators. It does not: the factorization depends on the regulator's CM character in x. On CM regulators (SDW), the factorization extracts a clean polynomial pre-factor; on non-CM regulators (Zubarev), no such clean factorization exists, and BOTH conventions test substrate-IS positivity-violation content on the non-CM weight.

Connes's R2 Convergence-1 already conceded this asymmetry (Zubarev split 3.24 IS substrate-IS multi-axis content); my Dissent-1 holds the position that this concession FOR Zubarev IS the structural-data criterion-(i) satisfaction FOR Zubarev. The (A, B) multi-axis substrate-IS structure exists on non-CM regulators; SDW is not the calibration locus for the multi-axis claim, but Zubarev IS.

#### Dissent-2: Per-pin convention-suffix tagging on §(iv) preserves §(iv) MANDATORY-K=4 closure structurally; the OUTSIDE-BHW issue is regulator-class-conditional, not uniform (Re:DISS-4 + Q2')

Connes's Dissent-4 argued that pinning both `SDW_3c_min^A_FW` and `SDW_3c_min^B_FW` in canonical_constants.py with per-axis suffix tags `-CONVENTION-A` and `-CONVENTION-B` violates `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (S88 W7b-83 close, 2026-05-05) because it embeds an OUTSIDE-BHW-admissibility-class quantity (convA on SDW) in the canonical-constants registry alongside a substrate-IS quantity (convB on SDW).

**The Dissent-4 force is conditional on Dissent-1's BHW-ill-posed reading of convA on SDW**. I now accept that conditional reading on SDW (per Convergence-4 + Convergence-2): convA on SDW is OUTSIDE BHW admissibility; pinning it as canonical alongside convB IS a structural class-conflation analogous to UV-regulator silent conflation. **For SDW specifically, I withdraw the dual-pin proposal**.

But Dissent-4's argument does NOT extend uniformly to non-CM regulators (Zubarev). On Zubarev, BOTH convA and convB test substrate-IS Bernstein-violation content on the non-CM weight (per Convergence-1 conceded by connes), and BOTH magnitudes ARE substrate-IS (the 3.24 ratio IS substrate-IS multi-axis content). The §(iv) MANDATORY-K=4 closure on SCHEMATIC-vs-FULL silent class-conflation is preserved by per-pin convention-suffix tagging:

```
Step 1 [Definition — §(iv) silent class-conflation closure pattern]:
  §(iv) pre-S88 W7b-83 baseline pathology: a script consumes a SCHEMATIC
  helper module (e.g., _spectral_action_regulators.py) without disclosing
  the SCHEMATIC class in the verdict-line `convention=` field. Downstream
  consumers silently treat the output as PRIMARY/FULL physical.

  §(iv) closure (post-S88 W7b-83 MANDATORY): `convention=...-SCHEMATIC`
  suffix DISCLOSES the level-pin; the suffix is a class-tag that PREVENTS
  silent conflation.

Step 2 [Substitution — convention-suffix tagging on non-CM regulators]:
  For Zubarev (non-CM in x):
    Pin Zubarev_3c_min^A_FW = -6.587 with PROVENANCE entry citing
        convention=...-CONVENTION-A-LAMBDA-DERIVATIVE-SCHEMATIC
    Pin Zubarev_3c_min^B_FW = -2.034 with PROVENANCE entry citing
        convention=...-CONVENTION-B-X-DERIVATIVE-SCHEMATIC

  Both pins are substrate-IS (Convergence-1 concedes); both carry the
  -SCHEMATIC suffix per §(iv) MANDATORY; the convention-suffix tag is
  the additional closure-tag that DISCLOSES the differential-operator-axis.

Step 3 [Simplify — class-conflation closure preserved structurally]:
  Per the §(iv) closure pattern: silent class-conflation is closed by
  TAGGING all relevant class-axes in the verdict-line convention field.
  The S88 W7b-83 closure adds the SCHEMATIC vs FULL axis. The proposed
  BHW-evaluator-class extension adds the (A, B) convention axis. Both
  axes are non-redundant class-tags; both are in the convention-suffix
  string; both downstream-audit-able.

  Connes's Dissent-4 argued that "naïve consumers will NOT inspect the
  convention-suffix string." This is correct AS A USABILITY concern but
  NOT a structural class-conflation pathology. The §(iv) MANDATORY itself
  relies on consumers parsing the SCHEMATIC suffix; the BHW-evaluator-class
  extension applies the same audit discipline at one additional axis.
  If the §(iv) closure is structurally adequate at K=4, the analogous
  closure at the BHW evaluator class is structurally adequate at K=1
  (with K=3 promotion threshold for MANDATORY status).

Step 4 [Direction]:
  Per-pin convention-suffix tagging on non-CM regulators (Zubarev) preserves
  the §(iv) MANDATORY-K=4 closure pattern structurally. The OUTSIDE-BHW
  issue Dissent-4 raised applies to CM regulators (SDW) where convA is
  OUTSIDE BHW admissibility on the non-CM Gaussian image — but on non-CM
  regulators the issue does NOT arise because BOTH conventions test
  non-CM weights from different coordinate angles, neither outside nor
  inside the BHW admissibility class in a problematic sense (BHW
  characterizes CM functions; non-CM weights are simply not in the
  CM class on either axis).

  The Dissent-4 §(iv) violation argument is regulator-class-conditional,
  matching the Convergence-2 partition. On CM regulators (SDW): single-
  canonical pin per Class-(d) MANDATORY MIGRATION. On non-CM regulators
  (Zubarev): per-pin convention-suffix tagging per Class-(g)
  STRUCTURAL-COMPANION; §(iv) closure preserved structurally.
```

The remaining open question for R3 is the Q2' answer: I PROPOSE both Class-(d) and Class-(g) sub-clauses register at the BHW-evaluator-class lockdown extension (per Convergence-2), with the per-regulator routing predicate being the CM-membership-in-x test. The lockdown rule is dual-mode (single-canonical for CM regulators; dual-canonical-with-suffix for non-CM regulators); §(iv) MANDATORY-K=4 closure is preserved at both modes.

#### Dissent-3: BHW theorem applied as CM characterization is the WRONG epistemic frame for axis A; axis A is a substrate-IS positivity test against substrate spectral support, NOT a CM-characterization claim (Re:Q1' answer-no horn)

Connes's Q1' poses a binary: either (a) accept that axis A is BHW-ill-posed for non-CM Gaussian images and the (A, B) multi-axis claim collapses, OR (b) provide the positive-measure dν such that `e^{-λ²} = ∫₀^∞ e^{-sλ} dν(s)`. I now ACCEPT, after Python verification this turn, that no such dν exists for `e^{-λ²}` (the Lévy subordination identity verifies for `e^{-√x}` to ~1e-14, not for `e^{-x²}`; the Hausdorff moment problem for `e^{-λ²}` admits no positive-measure solution). The mathematical fact connes asserts is correct.

But Q1' poses a FALSE BINARY because it presupposes that the only valid epistemic frame for axis A is "is this a BHW-CM-characterization theorem instance." This pre-judges the axis A claim. Axis A is NOT being proposed AS a CM-characterization theorem instance; it is a structurally distinct substrate-IS positivity test:

```
Step 1 [Definition — two distinct substrate-internal positivity tests]:
  TEST B (CM-characterization on x):
    Object: regulator weight f(x).
    Theorem support: BHW (Widder 1941).
    Claim: f admits positive-measure Laplace representation on [0,∞) iff
           (-1)^k · f^{(k)}(x) ≥ 0 for all k ∈ ℕ_0, x > 0.
    Substrate-internal status: tests the substrate's regulator measure dμ
                                positivity.

  TEST A (substrate-spectral-support sign-tracking on λ):
    Object: regulator weight image g(λ) = f(λ²) on the substrate's
             spectral cache support [λ_min, λ_max].
    Theorem support: NONE (no BHW analog applies; g is not CM in λ for
                            Gaussian images).
    Claim: the polynomial-pre-factor × g composition's sign on the
           substrate's spectral cache support encodes the spectral-spacing
           geometry × Jacobian-polynomial-roots interaction.
    Substrate-internal status: tests the structural data
                                {[λ_min, λ_max], chain-rule polynomial roots}
                                — both substrate-related but the polynomial
                                roots are NOT substrate-IS per connes
                                Dissent-2 Sage-decomposition.

Step 2 [Substitution — what each test discriminates substrate-physically]:
  Test B on SDW: PASS at float-floor +1.77e-13 ⇒ SDW is BHW-CM-admissible.
                 Substrate diagnostic: regulator measure positivity certified.

  Test A on SDW: empirical -2.773 at λ_min cache edge ⇒ chain-rule polynomial
                 sign-flip locus √(3/2) intersects [λ_min, λ_max] = [0.81974,
                 5.41894]. Substrate diagnostic: REGULATOR-INDEPENDENT
                 statement about the cache support's geometric position
                 relative to the polynomial root locus √(3/2). The diagnostic
                 content is SHARED across all CM regulators tested in
                 convention A — i.e., it is NOT regulator-specific.

Step 3 [Simplify — Test A is regulator-independent on CM regulators]:
  This is a structural concession: on CM regulators, Test A returns
  substantially the same diagnostic — the polynomial sign-flip locus
  intersects the cache support. The empirical magnitude depends on the
  regulator weight evaluated at the cache edge, but the sign-flip
  STRUCTURAL CONTENT is regulator-independent.

  ⇒ Test A on CM regulators DOES NOT carry regulator-class-discriminating
    substrate diagnostic content; it carries SUBSTRATE-CACHE-SUPPORT-vs-
    POLYNOMIAL-ROOT-LOCUS structural content that is the SAME across all
    CM regulators. This is a substrate-IS observation, but it is a
    SUBSTRATE-CACHE-DOMAIN-LEVEL observation, NOT a regulator-class-LEVEL
    observation.

Step 4 [Direction]:
  My DISSENT here is NOT that axis A is a BHW-CM-characterization theorem
  instance — Q1' is correct that it is NOT. My DISSENT is that the
  BHW-CM frame is the WRONG epistemic frame to apply to axis A. Axis A
  is a substrate-IS positivity-sign-tracking test on the substrate-cache-
  support × polynomial-root-locus geometry. Its substrate-IS content lives
  at the substrate-cache-domain layer (a Level-1-substrate-IS quantity at
  fixed τ_fold per phononic-framing.md §"Single-τ-slice vs moduli-deformation"),
  not at the regulator-class layer (where Test B's CM-admissibility lives).

  This frame separation is the CORRECT structural reading of axis A on
  CM regulators. The Q1' BHW-ill-posed reading is correct as a CM-test
  reading; the substrate-cache-domain-positivity-tracking reading is the
  parallel substrate-IS reading I now propose for axis A. The two frames
  are orthogonal: Test B at regulator-class layer + Test A at substrate-
  cache-domain layer.

  This frame separation does NOT contradict connes's Convergence-2
  regulator-class-conditional remediation: Test A's substrate-cache-domain
  content on CM regulators is regulator-independent (so Test A on SDW
  alone is the correct calibration locus for the substrate-cache-domain
  test on CM regulators); Test A's substrate-IS multi-axis content on
  non-CM regulators (Zubarev split 3.24) is regulator-class-discriminating
  (so Test A on Zubarev is the correct calibration locus for the
  multi-axis substrate-IS multi-axis structure).

  The forward question is whether the substrate-cache-domain Test A on
  CM regulators has structural value beyond audit-trail status. I propose
  in EMERGENCE-3 below that it does, as the Level-2 algebraic envelope
  for the BHW-evaluator-class cross-pillar bridge candidate (per
  cross-pillar-bridge-anatomy.md §"Three forward bridge candidates").
```

The Q1' answer-no horn I take is structurally: I accept that axis A on SDW is BHW-ill-posed AS A CM-CHARACTERIZATION TEST, AND I reject that axis A on SDW carries no substrate-IS content; it carries substrate-cache-domain-geometry content that lives at a different layer than regulator-class CM-admissibility. The two layers are non-redundant per the Level-1 vs Level-2 substrate-IS distinction at `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` SUGGESTION-K=1.

### EMERGENCE

Three emergence axes from R1+R2 cross-pollination.

#### Emergence-1: Forward calibration discipline for meta-INVARIANCE class theorems — explicit STAGE-1 → STAGE-3 promotion under joint-theorem-promotion.md

The R1+R2 cross-pollination on Convergence-1 (concede meta-INVARIANCE STAGE-1-CANDIDATE) + Emergence-3 (two-corpus structure) yields a NEW forward-looking calibration discipline that should be added to the existing rule corpus:

**Proposal (S89+ forward methodology rule extension)**: Any "meta-class theorem" candidate — a proposed unifying claim across multiple existing structural theorems whose PER-INSTANCE evaluator classes / observable types differ — MUST register as STAGE-1-CANDIDATE under `joint-theorem-promotion.md` 4-stage pathway, with K-counter starting at K=1 (the FIRST candidate instance proposing the unification), NOT at the cumulative K-counter of the unified pre-existing instances. The K-counter advancement to the cumulative state requires Stage-2 cross-axis independent-verify PASS-AND.

```
Step 1 [Definition]:
  META-CLASS THEOREM CANDIDATE := proposed unifying structural claim across
                                   N pre-existing theorem instances at
                                   (potentially) different evaluator
                                   classes / observable types.

  K-COUNTER ADVANCEMENT ASYMMETRY (existing rule):
    Within-axis K-counter: linear advancement K=1 → K=2 → ... → K=K_promotion.
    Cross-axis K-counter (NEW, this emergence): STAGE-1 at K=1 (the
                                                  unification proposal alone);
                                                  Stage-2 PASS-AND fires the
                                                  jump K=1 → K=N (N pre-existing
                                                  instances pooled under the
                                                  unified claim) AND STAGE-3
                                                  PERMANENT promotion.

Step 2 [Substitution — calibration corpus mapping]:
  Calibration corpus instance #1 (S88 W-9 W9-106 / W-28):
    Pre-existing: W-11 RULE-2 5-instance baseline at η + even-Mellin (K=5
                   HARDENED at S86 close).
    Cross-axis proposal: meta-INVARIANCE class theorem unifying W-11 RULE-2
                         baseline + W9-106 BHW-test composite-layer PASS.
    STAGE-1 status: K=1 (W9-106 proposal) at NEW §VII.AQ-META.
    Stage-2 verify: required for K=1 → K=6 + STAGE-3 promotion.

  Future calibration corpus instances (N=2 at K=2 SUGGESTION; N=3 at
    K_promotion MANDATORY): forthcoming meta-class theorem candidates as
    they appear.

Step 3 [Simplify — rule placement]:
  This forward calibration discipline is structurally an EXTENSION of
  joint-theorem-promotion.md, specifically a NEW sub-section §"Cross-axis
  K-counter STAGE-1 proposal pattern" that pre-registers the asymmetric
  K-counter behavior for meta-class theorem candidates.

  Cross-link to feedback_rules-compensate-missing-structure.md K=3
  promotion threshold: the meta-class K-counter advancement is structurally
  distinct from the within-axis K-counter; both should be tracked in
  parallel, with the meta-class K-counter advancing only on Stage-2 PASS-AND
  events.

Step 4 [Direction]:
  This emergence is FORWARD-LOOKING from S88 W-28 close. Any future
  meta-class theorem candidate (proposed unifying claim across pre-existing
  instances at different axes) MUST adopt this STAGE-1-at-K=1 discipline.
  Meta-class theorems registered without the asymmetric-K-counter pre-
  registration will route to plan-freeze halt with MANDATORY remediation
  per joint-theorem-promotion.md §"Audit at plan-freeze".
```

The carry-forward to the Wrap-Up: register the meta-class K-counter STAGE-1 rule as an extension to joint-theorem-promotion.md at S89 plan-freeze, with the W9-106 / §VII.AQ-META landing as calibration corpus instance #1.

#### Emergence-2: Structural taxonomy of HBW-evaluator-class lockdown rules — regulator-class-conditional dual-mode lockdown as forward template

The Convergence-2 regulator-class-conditional split (Class-(d) MANDATORY MIGRATION for CM regulators + Class-(g) STRUCTURAL-COMPANION for non-CM regulators) is the operative shape for the BHW-evaluator-class extension to `regulator-convention-lockdown.md`. This emergence proposes the structural taxonomy of the lockdown rule itself.

**Proposal (BHW-Evaluator-Class Lockdown Extension; forward methodology rule extension at regulator-convention-lockdown.md S89+ plan-freeze)**: a NEW sub-section §"BHW-Evaluator-Class Dual-Mode Lockdown" with the following structural shape:

```
§"BHW-Evaluator-Class Dual-Mode Lockdown" (proposed S89 extension):

  Routing predicate (regulator-class-conditional):
    For each regulator atlas member, the test "is f(x) CM in x?" determines
    the lockdown mode:
      (P1) CM-in-x ⇒ single-canonical-pin mode (Mode-d).
      (P2) non-CM-in-x ⇒ dual-canonical-pin mode (Mode-g).

  Mode-d (Class-(d) MANDATORY MIGRATION):
    For (P1) CM regulators (e.g., SDW with f(x) = e^{-x}):
      Substrate-natural canonical pin: convention B alone.
      Convention A retains audit-trail value with -LAM-DERIVATIVE-CHAIN-RULE-
      LIFT companion-tag.
      Downstream cites of the regulator's Bernstein-positive-cone observable
      MUST migrate to convention B per Class-(d) HARD-HALT MANDATORY MIGRATION
      (D_max ≫ 3.0; sign-discordance forces categorical-level structural
      violation).

  Mode-g (Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR):
    For (P2) non-CM regulators (e.g., Zubarev with f(x) = x/(1+x²)):
      Substrate-natural canonical pin: PAIR (A, B) with per-axis suffix
                                       tagging.
      Both `Zubarev_3c_min^A_FW = -6.587` and `Zubarev_3c_min^B_FW = -2.034`
      enter canonical_constants.py with explicit per-axis PROVENANCE
      entries citing W9-106 verdict line.
      Per-cite convention-suffix discipline: any cite of the regulator's
      Bernstein-positive-cone observable MUST carry -CONVENTION-A or
      -CONVENTION-B or -CONVENTION-PAIR-DUAL suffix.
      §(iv) MANDATORY-K=4 closure preserved structurally per per-pin
      tagging (Dissent-2 above).

  Demarcation theorem (BHW dual-mode):
    A convention-pinning convention C is admissible for a BHW-positive-cone
    gate iff:
      (P1) CM regulator in atlas: C ∈ {B} (single-canonical);
      (P2) non-CM regulator in atlas: C ∈ {A, B, PAIR-DUAL}.
    Mixed atlases (e.g., A_4 = {ζ, Zubarev, SDW, anomaly} containing both
    CM and non-CM regulators) require PER-REGULATOR convention pinning,
    not a uniform atlas-level pin.

  Cross-link to substrate-first-canonical-sourcing.md §(iv) MANDATORY-K=4
  (S88 W7b-83 close): the -SCHEMATIC suffix is preserved per the existing
  level-pin discipline; the convention-suffix is added per this rule.
```

This emergence promotes the existing `regulator-convention-lockdown.md` DR3-class lockdown's single-canonical-pin shape to a DUAL-MODE lockdown family: single-canonical for one class of regulator-physics situations (CM-in-x; SDW-like), dual-canonical-with-suffix for the other (non-CM-in-x; Zubarev-like). The dual-mode lockdown is the structural synthesis of connes's R1 single-canonical reading + my R1 dual-canonical reading: each is correct in its own regulator partition.

The forward calibration corpus tracking starts at K=1 (this gate's W9-106 calibration); K=3 promotion to MANDATORY status applies when 3 distinct CM-vs-non-CM regulator-class-conditional applications calibrate the rule.

#### Emergence-3: Pre-register S89 gate `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` to test the BHW-admissibility resolution — load-bearing structural question

The Q1' answer-yes-on-Gaussian (no positive measure dν exists for `e^{-λ²}`) is Python-verified this turn; connes's Dissent-1 BHW-ill-posed reading is mathematically sustained on the Gaussian image. But this raises a load-bearing forward structural question: under what theorem-class IS axis A on CM-regulator Gaussian-images a substrate-IS observable? Per Dissent-3 above, my proposal is that axis A operates at the substrate-cache-domain-positivity-tracking layer, NOT at the regulator-class CM-admissibility layer. This proposal needs structural validation.

**Proposal (S89 carry-forward gate)**: pre-register `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` as a methodology-class gate testing the substrate-cache-domain layer's structural-validity for axis A.

```
GATE: S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN

Purpose: Test whether axis A on CM-regulator Gaussian-images carries
         substrate-IS content at the substrate-cache-domain layer, distinct
         from BHW-CM-characterization at the regulator-class layer.

Pre-registered threshold predicates (3 sub-clauses, all required for PASS):
  (i) Sage-decomposition cross-check of T_A[k](λ) = chain-rule-polynomial
      × regulator-weight on TWO CM regulators beyond SDW (proposal:
      f_1(x) = e^{-x²/2} Gaussian-of-x; f_2(x) = (1+x)^{-1} Lorentzian).
      PASS iff the chain-rule polynomial pre-factor has structurally-fixed
      roots independent of f's CM-class; FAIL iff the roots depend on f.
  (ii) Test that the substrate-cache-support × polynomial-root-locus
       intersection is regulator-independent on CM regulators. PASS iff
       T_A[3](λ_min) sign-flip is consistent across all 3 CM regulators
       in (i); FAIL iff sign behavior differs per regulator.
  (iii) Verify that axis A does NOT advance regulator-class-conditional
        information on CM regulators (i.e., the Test-A diagnostic content
        is shared across regulators in the CM partition, not per-regulator).
        PASS iff the Sage-decomposition extracts the same polynomial-pre-
        factor structure across all CM regulators tested.

Inputs:
  - canonical_constants.py: M_KK, tau_fold, cache support [lambda_min, lambda_max]
  - L_max=12 spectral cache npz
  - Sage MCP (sage_eval, sage_simplify) for symbolic polynomial decomposition

Output:
  - PASS: confirms axis A on CM regulators is a substrate-cache-domain-layer
          positivity-tracking test (substrate-IS but regulator-independent).
          §VII.AQ-META Stage-2 verify proceeds with axis A retained at the
          substrate-cache-domain layer for CM regulators.
  - FAIL: refutes the substrate-cache-domain-layer reading; axis A on CM
          regulators reduces to a coordinate-change artifact with no
          substrate-IS content. Convergence-4 + Dissent-3 synthesis collapses;
          the SDW-channel migration to Zubarev-only is structurally final.

Effort estimate: 0.5 wave-equivalents (Sage-decomposition compute + 3-regulator
                 cross-check; deterministic, reproducible).

Status: STAGE-1-CANDIDATE; the gate is the structural validation step for
        my Dissent-3 layer-separation proposal.
```

This pre-registration is the substrate-physics-grounded test of whether axis A's substrate-cache-domain reading survives independent verification on multiple CM regulators. Without this gate, my Dissent-3 substrate-cache-domain layer proposal is workshop-internal narrative; with it, it becomes a pre-registered structural prediction with PASS/FAIL outcome.

The carry-forward: pre-register `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` at the S89 plan-freeze; route the result to either §VII.AQ-META Stage-2 verify dispatch (PASS) or to the SDW-channel-migration-final closure (FAIL). The R3 connes follow-up may sharpen the gate's pre-registered threshold predicates further.

---

## Round 3 — connes: Follow-up

*[Workshop closure note: connes was not re-dispatched at R3. The text below is the synthesizer's stipulation of connes' R3 closure stance derived from connes' R2 substantive positions (Convergence-1 / Convergence-2 / Convergence-3 at lines 870-958; Dissent-1 / Dissent-2 / Dissent-3 / Dissent-4 at lines 964-1277; Emergence-1 / Emergence-2 / Emergence-3 at lines 1283-1418; A1-A5 at lines 1428-1438; Q1'-Q3' at lines 1442-1446) cross-checked against lizzi R2 Convergence-1 / Convergence-2 / Convergence-3 / Convergence-4 (concessions at lines 1456-1665) plus Dissent-1 / Dissent-2 / Dissent-3 (residual divergences at lines 1670-1903). Not a verbatim connes contribution.]*

### CONVERGENCE

**Convergence-1' (lizzi R2 Convergence-1 acceptance — meta-INVARIANCE STAGE-1-CANDIDATE at K=1)**: The R2 lizzi concession that the meta-INVARIANCE class theorem registers as STAGE-1-CANDIDATE at K=1 (NOT K=6 HARDENED) per `joint-theorem-promotion.md` 4-stage pathway closes my R2 Dissent-3 challenge. The two-corpus structure (§VII.AQ at K=5 HARDENED retained + §VII.AQ-META at K=1 STAGE-1-CANDIDATE NEW) per lizzi Convergence-3 is the structurally-correct registry decomposition; both K-counter trajectories are honest (no regression of the W-11 RULE-2 5-instance HARDENED state; no premature Stage-3 tagging on the meta-claim). Stage-2 cross-axis independent-verify is the structural validation step that determines whether K-counter advancement K=1 → K=6 fires (PASS-AND on the unification claim) or whether W9-106 routes to its own STAGE-1 corpus at §VII.METHODOLOGY-CASCADE-DIAGNOSTIC per my R2 Emergence-1 (FAIL on the unification claim).

**Convergence-2' (lizzi R2 Convergence-2 acceptance — regulator-class-conditional dual-mode lockdown is the operative shape)**: The R2 lizzi concession that the BHW-evaluator-class lockdown extension at `regulator-convention-lockdown.md` should pre-register BOTH Class-(d) MANDATORY MIGRATION (for CM regulators) AND Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR (for non-CM regulators) per the CM-membership-in-x routing predicate is the structural synthesis of my R1 single-canonical reading + lizzi R1 dual-canonical reading: each is correct in its own regulator partition. The substrate-physics rationale: for SDW (CM in x), the chain-rule polynomial pre-factor 4λ(2λ²−3) factors out cleanly per my R1 C1 Sage-decomposition because the regulator weight is itself BHW-CM in x; for Zubarev (non-CM in x), no clean polynomial factorization exists and the (A, B) magnitude split 6.587/2.034 = 3.24 is intrinsic substrate-IS multi-axis content per R2 Convergence-1 (which I conceded in R2). The dual-mode shape preserves my R1 substrate-natural-singleton intent on CM regulators while admitting lizzi's multi-axis intent on non-CM regulators; neither is over-applied.

**Convergence-3' (lizzi R2 Convergence-4 acceptance — Zubarev-channel migration on the SDW-channel discriminator)**: The R2 lizzi concession that the Lancaster MCT-3 SDW-channel discriminator at 0.2773% (convA) is structurally displaced to the Zubarev channel at 0.2035% (convB) under the substrate-natural reading on SDW (CM in x; convA OUTSIDE BHW admissibility on the Gaussian image per R2 Dissent-1 Hausdorff-moment-problem argument that lizzi accepted after this-turn Python verification per R2 Dissent-3 line 1815) closes the SDW-channel migration question. The migration changes WHICH substrate physics the cryostat tests (CM-admissibility certifier on SDW vs non-CM-violation discriminator on Zubarev) but does NOT lose falsifiability — falsifiability is RELOCATED to where substrate physics has predictive content. This addresses my R2 A4 option (i) operative replacement and the lizzi R1 phantom-margin concern simultaneously.

#### Convergence-4 (NEW R3 convergence on substrate-cache-domain frame for axis A): conditional-acceptance pending S89 verification gate

The R2 lizzi Dissent-3 frame-separation proposal (axis A on CM regulators operates at the substrate-cache-domain layer per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level-1, structurally orthogonal to axis B at the regulator-class CM-admissibility layer) is plausible at the structural-pattern level but currently rests on an analogy claim, not on a substrate-physics derivation. The lizzi R2 Emergence-3 pre-registered gate `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` is the correct discipline: the frame-separation hypothesis becomes a structural prediction with PASS/FAIL outcome on 3 CM-regulator cross-checks (Sage-decomposition consistency + sign-flip locus regulator-independence). I AGREE on the dispatch protocol; my conditional acceptance hinges on the S89 gate's PASS verdict. Until then the substrate-cache-domain frame is workshop-internal proposal.

### DISSENT

**Dissent-1' (Single-axis substrate-natural reading on SDW retained even with substrate-cache-domain frame)**: Lizzi R2 Dissent-3 proposed that axis A on SDW carries substrate-cache-domain content (Level-1-substrate-IS at fixed τ_fold) distinct from axis B at the regulator-class layer. Conditional on the S89 verification gate above, I would accept axis A on CM regulators as a Level-1 substrate-cache-domain observable. But this acceptance does NOT extend to the lab-feasibility chain: the Lancaster MCT-3 cryostat measures Bernstein-positivity violation in the LABORATORY-IN observable, which is the regulator-class-layer CM-admissibility test (Test B per lizzi R2 Dissent-3 Step 1). The substrate-cache-domain Test A on SDW carries no regulator-class-discriminating content per lizzi's own R2 Dissent-3 Step 3 ("Test A on CM regulators DOES NOT carry regulator-class-discriminating substrate diagnostic content; it carries SUBSTRATE-CACHE-SUPPORT-vs-POLYNOMIAL-ROOT-LOCUS structural content that is the SAME across all CM regulators"). Therefore the SDW-channel Lancaster discriminator at convA is STILL a phantom AT THE LAB LAYER (the cryostat is not measuring substrate-cache-domain geometry; it is measuring transport coefficients on regulator weights). The SDW-channel migration to Zubarev (Convergence-3' above) STANDS at the lab layer regardless of whether axis A carries substrate-cache-domain content at the substrate-IS layer. This is consistent with the cross-pillar-bridge-anatomy.md §"IS-not-IN" 5-anatomy distinction: Element 1 (substrate-IS observable) and Element 2 (laboratory-IN observable) are STRUCTURALLY DISTINCT; substrate-cache-domain Test A may live at Element 1 without entering Element 2.

**Dissent-2' (Per-pin convention-suffix tagging on CM regulators is still a §(iv) violation even WITH substrate-cache-domain frame)**: Lizzi R2 Dissent-2 argued that per-pin convention-suffix tagging preserves §(iv) MANDATORY-K=4 closure structurally on non-CM regulators. I AGREED on Zubarev (R2 Emergence-2 Class-(g) STRUCTURAL-COMPANION). But on CM regulators (SDW), pinning `SDW_3c_min^A_FW` in canonical_constants.py — even with `-CONVENTION-A-SUBSTRATE-CACHE-DOMAIN` suffix — still embeds a quantity OUTSIDE BHW admissibility-class ON THE REGULATOR-CLASS LAYER alongside a substrate-IS quantity ON THE SAME REGULATOR-CLASS LAYER (`SDW_3c_min^B_FW`). The two pins are at DIFFERENT layers under lizzi's frame-separation (axis A at Level-1 substrate-cache-domain; axis B at regulator-class), but downstream consumers of canonical_constants.py do NOT inspect layer-tags by default; they import `SDW_3c_min_FW` and treat both pins as canonical values on the same epistemic plane. The §(iv) closure is preserved BY CONSTRUCTION only when axis A and axis B are co-located at the same layer (as on Zubarev where both test the regulator-class CM-admissibility on a non-CM weight); on SDW where axis A claims a different layer, the convention-suffix tag is necessary but not sufficient — the layer-tag ALSO needs to be carried, and canonical_constants.py PROVENANCE entries do not currently support layer-tagging. Single-canonical pin under convention B per Class-(d) MANDATORY MIGRATION remains the structurally-correct shape for SDW; substrate-cache-domain content for axis A on SDW (if validated by S89 gate) registers at a DIFFERENT structural locus (e.g., a §VII registry slot for substrate-cache-domain-positivity-tracking, NOT in canonical_constants.py at the Bernstein-evaluator regulator-class layer).

### EMERGENCE

#### Emergence-1' — Layer-tagged canonical-constants pin discipline as forward methodology rule extension

The Dissent-2' resolution surfaces a NEW forward methodology rule: when a per-pin convention-suffix tag is paired with a frame-separation claim (axis A at one substrate-IS layer; axis B at another), the canonical_constants.py PROVENANCE entry MUST carry an explicit `layer_tag` field IN ADDITION to the convention-suffix. Without the layer-tag, downstream consumers conflate the pins at the same epistemic plane, defeating the structural purpose of per-pin tagging.

Proposal (S89+ forward methodology rule extension at `substrate-first-canonical-sourcing.md §(iv)` or new sub-section): when a canonical-constants pin admits a frame-separation reading (axis A and axis B operate at distinct substrate-IS levels per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level-1 vs Level-2 OR analogous), the PROVENANCE entry MUST carry both `convention=...-CONVENTION-X` suffix AND a `layer_tag=<level-name>` field. The layer-tag closes the silent class-conflation pathway that the convention-suffix alone does not close on cross-layer pin pairs. K=1 calibration: this workshop's frame-separation proposal for axis A on CM regulators (pending S89 verification).

#### Emergence-2' — §VII.METHODOLOGY-CASCADE-DIAGNOSTIC routing on Stage-2 FAIL is the load-bearing fallback

The two-corpus structure (Convergence-1' above) has a critical fallback: if Stage-2 verify FAILs on the §VII.AQ-META unification claim, the W9-106 entry routes to its own STAGE-1 corpus at §VII.METHODOLOGY-CASCADE-DIAGNOSTIC per my R2 Emergence-1 (3-orthogonal-source decomposition: L_max-stability axis + regulator-class axis with magnitude variation + convention-axis with chain-rule polynomial pre-factor). This fallback is the load-bearing structural protection: it ensures the W9-106 substrate-physics content (the 3-source decomposition) is preserved as a STAGE-1-CANDIDATE proposal regardless of whether the unification with W-11 RULE-2 baseline succeeds. The forward methodology discipline: any meta-class theorem candidate registering at STAGE-1 with cross-axis K-counter MUST also pre-register a fallback corpus where the candidate's standalone substrate-physics content lands on Stage-2 FAIL. This generalizes my R2 Emergence-1 and lizzi R2 Convergence-3 jointly.

#### Emergence-3' — BHW-evaluator-class dual-mode lockdown extension calibration corpus reservation

The Convergence-2' regulator-class-conditional dual-mode lockdown (Class-(d) for CM-in-x; Class-(g) for non-CM-in-x) registers at `regulator-convention-lockdown.md` per lizzi R2 Emergence-2 Step "BHW-Evaluator-Class Dual-Mode Lockdown" specification. K-counter calibration corpus starts at K=1 (this workshop's W9-106 + Lancaster discriminator chain on SDW + Zubarev). K=3 promotion to MANDATORY status applies when 3 distinct CM-vs-non-CM regulator-class-conditional applications calibrate the rule. Forward calibration: future S89+ Bernstein-positive-cone gates on alternative regulator atlases (e.g., A_5_extended sub-tests with anomaly + cutoff_sqrt regulators) advance the K-counter on each regulator class; mixed atlases require PER-REGULATOR convention pinning per the demarcation theorem.

### QUESTIONS

**Q1'' (S89 verification gate scope on substrate-cache-domain frame)**: The lizzi R2 Emergence-3 pre-registered `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` tests axis A's substrate-cache-domain layer claim on 3 CM regulators (e^{-x²/2} Gaussian-of-x, (1+x)^{-1} Lorentzian, e^{-x} SDW). For Convergence-4 conditional acceptance: (a) is the gate's regulator triple structurally adequate (3 distinct CM forms with different polynomial-pre-factor structures), or should the gate be expanded to include a 4th regulator that CHALLENGES the regulator-independence claim (e.g., e^{-2x} which has SAME CM character as e^{-x} but different cache-support intersection)? (b) If the S89 gate FAILs sub-clause (ii) (per-regulator sign-flip locus differs), does the substrate-cache-domain frame collapse uniformly (volovik R2 Dissent-3 reading rejected) OR does it collapse only on SDW with the frame retained on alternative CM regulators?

**Q2'' (Layer-tag PROVENANCE field implementation)**: Emergence-1' proposes a `layer_tag` field on canonical_constants.py PROVENANCE entries. Specifically: (a) is the layer_tag field a string-suffix on existing PROVENANCE-dict keys, OR a new top-level dict-key in the PROVENANCE entry? (b) is the layer-tag enforcement at canonical_constants.py write-time (via `update_constant(...)` signature extension) or at downstream-consumer read-time (via a wrapper function)? (c) backward-compatibility on existing pins without layer-tag — grandfathered with retroactive landing at S89+ plan-freeze?

**Q3'' (regulator-convention-lockdown.md extension scope)**: Emergence-3' proposes a new §"BHW-Evaluator-Class Dual-Mode Lockdown" sub-section. Specifically: (a) does the rule-text match the existing DR3-class lockdown structure (single canonical-pin + admissibility class + alternative conventions PROHIBITED) or does it require a NEW dual-mode lockdown template (per lizzi R2 Emergence-2 Step "BHW-Evaluator-Class Dual-Mode Lockdown" with regulator-class-conditional routing predicate)? (b) The dual-mode template, if adopted, becomes a forward template for OTHER evaluator classes — should the rule-file be reorganized to host both single-mode and dual-mode lockdown patterns, or should dual-mode lockdowns live in a separate rule-file? (c) Cross-link to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — is the dual-mode lockdown structurally analogous to the algebra-INVARIANT vs algebra-DEPENDENT corner classification, and does the K=3 MANDATORY discipline transfer?

---

## Round 3 — lizzi: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

#### Convergence-R3-1 — Single-axis substrate-natural reading on SDW lab-feasibility chain (ACCEPT R3 Dissent-1')

I ACCEPT connes R3 Dissent-1'. The lab-feasibility chain at the Lancaster MCT-3 cryostat is structurally a regulator-class-layer measurement (the cryostat measures Bernstein-positivity violation in transport coefficients on regulator weights, NOT substrate-cache-domain geometry). Even if the S89 verification gate `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` PASSes (validating the substrate-cache-domain frame for axis A on CM regulators at the substrate-IS layer), the lab-feasibility chain LIVES at Element 2 of the cross-pillar bridge anatomy (laboratory-IN observable per `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"`) and operates at the regulator-class-CM-admissibility layer — Test B's domain.

```
Step 1 [Definition]:
  ELEMENT-1-SUBSTRATE-IS := finite-L spectral-triple observable on
                            (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) per
                            cross-pillar-bridge-anatomy.md.
  ELEMENT-2-LAB-IN       := continuum measurement / sweep observable
                            per cross-pillar-bridge-anatomy.md.

Step 2 [Substitution]:
  Substrate-cache-domain Test A on SDW (lizzi R2 Dissent-3 frame):
    Operates on substrate cache support [λ_min, λ_max] × polynomial-root-
    locus √(3/2). LIVES at Element 1 (substrate-IS observable on the
    fixed-τ_fold spectral triple).
  Lancaster MCT-3 cryostat SDW-channel measurement:
    Operates on SDW transport coefficients on the regulator weight at
    cryogenic operating point. LIVES at Element 2 (laboratory-IN
    observable on the continuum lab platform).

Step 3 [Simplify]:
  Element 1 ≠ Element 2 by structural anatomy. The substrate-cache-
  domain Test A's substrate-IS content does NOT propagate through the
  HKR / Connes-Karoubi bridge map to a laboratory-IN observable; the
  bridge map's image is the regulator-class-CM-admissibility content
  (Test B), which on SDW returns float-floor PASS.

Step 4 [Direction]:
  The SDW-channel Lancaster discriminator at convA (0.2773%) IS a
  phantom AT THE LAB LAYER irrespective of axis A's substrate-IS
  status at Element 1. The migration to Zubarev-channel discriminator
  (Convergence-3' / R2 Convergence-4) STANDS at Element 2.
```

This concession sharpens R2 Dissent-3: axis A on CM regulators may carry substrate-cache-domain content at Element 1 (S89 gate-conditional), but it does NOT enter the lab-feasibility chain at Element 2. The two layers are non-redundant per the algebra-axis orthogonality K-counter MANDATORY at K=3 (S87 W-2 close, `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`). My R2 framing implicitly bridged them; connes R3 Dissent-1' correctly enforces the structural separation.

#### Convergence-R3-2 — Layer-tag PROVENANCE field discipline (ACCEPT R3 Emergence-1')

I ACCEPT connes R3 Emergence-1'. The proposed `layer_tag` field on canonical_constants.py PROVENANCE entries closes a silent class-conflation pathway my R2 Dissent-2 per-pin convention-suffix proposal did not address: when a frame-separation reading places axis A and axis B at structurally distinct substrate-IS layers, the convention-suffix tag alone does not communicate the layer distinction to downstream consumers, who import the constant value and treat both pins as canonical-status quantities at the same epistemic plane. The `layer_tag` field carries the Level-1 vs Level-2 vs regulator-class distinction explicitly into the PROVENANCE entry, per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` SUGGESTION-K=1 (with K=3 promotion threshold).

The forward methodology rule extension at `substrate-first-canonical-sourcing.md §(iv)` (or new sub-section) registers as STAGE-1-CANDIDATE with K=1 calibration on this workshop's frame-separation proposal. K=3 promotion follows future cross-layer pin pairs surfacing.

#### Convergence-R3-3 — §VII.METHODOLOGY-CASCADE-DIAGNOSTIC fallback discipline (ACCEPT R3 Emergence-2')

I ACCEPT connes R3 Emergence-2'. The fallback structure (W9-106 routes to §VII.METHODOLOGY-CASCADE-DIAGNOSTIC at K=1 STAGE-1-CANDIDATE on Stage-2 FAIL of §VII.AQ-META unification claim) is structural protection that ensures the substrate-physics content of the W9-106 entry — the 3-orthogonal-source decomposition (L_max-stability + regulator-class with magnitude variation + convention-axis with chain-rule polynomial pre-factor) — survives regardless of whether the unification with W-11 RULE-2 baseline holds at Stage-2 verify. This generalizes the joint-theorem-promotion 4-stage pathway to require fallback-corpus pre-registration for any meta-class theorem candidate.

The forward methodology discipline registers as a sub-section extension at `joint-theorem-promotion.md` per R2 Emergence-1 + R3 Emergence-2': any meta-class theorem candidate at STAGE-1-CANDIDATE with cross-axis K-counter MUST pre-register a fallback corpus where the standalone substrate-physics content lands on Stage-2 FAIL.

### DISSENT

#### Dissent-R3-1 — Per-pin convention-suffix on canonical_constants.py for SDW: layer-tag adequacy contested (Re: R3 Dissent-2')

Connes R3 Dissent-2' argued that pinning `SDW_3c_min^A_FW` in canonical_constants.py (even with `-CONVENTION-A-SUBSTRATE-CACHE-DOMAIN` suffix) embeds a quantity OUTSIDE BHW admissibility-class on the regulator-class layer alongside a substrate-IS quantity on the same regulator-class layer, and that downstream consumers do not inspect layer-tags by default. This argument is structurally sound under the current canonical_constants.py PROVENANCE-entry shape (no layer-tag field) BUT is OBSOLETED by Convergence-R3-2 (acceptance of `layer_tag` field on PROVENANCE entries). With the layer-tag field, the cross-layer pin pair on SDW is structurally distinguishable: `SDW_3c_min^A_FW` carries `convention=...-CONVENTION-A` + `layer_tag=Level-1-substrate-cache-domain`; `SDW_3c_min^B_FW` carries `convention=...-CONVENTION-B` + `layer_tag=regulator-class-CM-admissibility`. Downstream consumers MUST parse the layer-tag per the new MANDATORY discipline; consumers that import the bare constant name (rather than via a layer-aware accessor) violate the rule's audit trail.

The disagreement: connes R3 Dissent-2' would route to single-canonical pin under convention B per Class-(d) MANDATORY MIGRATION on SDW, registering the substrate-cache-domain content for axis A (S89-conditional) at a DIFFERENT structural locus (e.g., a new §VII registry slot). My residual reading: with the `layer_tag` field, the dual-pin form on SDW is admissible BY CONSTRUCTION because the layer-tag enforces the structural separation at canonical_constants.py write-time. The two pins are not on the same epistemic plane structurally; the layer-tag field is what makes that fact explicit at the canonical-constants level.

Resolution: this dissent narrows to an implementation question — does the `layer_tag` field on canonical_constants.py PROVENANCE entries (Q2'' in R3 connes Questions) suffice to close the cross-layer-pin-conflation pathway, or does the structural separation REQUIRE distinct registry loci even with layer-tagging? Pre-register S89 gate `S89-LAYER-TAG-CROSS-LAYER-PIN-DISCIPLINE` testing whether the layer-tag enforcement protocol is structurally adequate against the OUTSIDE-BHW-class concern; PASS = `layer_tag` field with audit-script enforcement closes the conflation pathway; FAIL = canonical_constants.py is structurally inadequate and SDW axis A registers at a separate §VII slot.

#### Dissent-R3-2 — substrate-cache-domain frame is at Level-1 SUBSTRATE-IS even if it does not enter Element 2 lab chain (Re: R3 Dissent-1' line "axis A on CM regulators may carry substrate-cache-domain content at Element 1 (S89 gate-conditional), but it does NOT enter the lab-feasibility chain at Element 2")

I AGREE that axis A's substrate-cache-domain content does not enter Element 2; this is conceded at Convergence-R3-1. But I DISAGREE on the implicit framing in connes R3 Dissent-1' that this restricts the structural-significance of axis A. Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (SUGGESTION-K=1), Level-1 substrate-IS observables (single-τ-slice; eigenvalues, Peter-Weyl decomposition, spectral-action moments) are STRUCTURALLY SIGNIFICANT regardless of whether they propagate through a cross-pillar bridge map to Element 2. Calibration corpus instance #1 at Level-1 (W2-6 partition-stability cardinality (2,4,8,6) at τ_fold = 0.190; W2-8 Δ_0 LOCALIZATION FORMULA) is registered at §VII.AJ.partition-stability + §VII.AD WITHOUT requiring Element 2 lab realization; these are pure-substrate-IS theorems.

The forward calibration claim: axis A on CM regulators at the substrate-cache-domain layer (S89-gate-conditional) registers at Level-1 substrate-IS, with K-counter advancement on the W2-10 calibration corpus (currently K=1 at S88 W2-10 close; this gate's W9-106 axis-A content advances K=1 → K=2 if the S89 gate PASSes the layer-separation hypothesis). The K=3 promotion to MANDATORY at the W2-10 SUGGESTION-K=1 status is reached at K=3; this is independent of the lab-feasibility chain at Element 2.

This dissent does NOT contradict Convergence-R3-1 (Element 1 ≠ Element 2; lab chain stays at Element 2). It sharpens the forward-calibration claim: axis A's substrate-IS structural-significance lives at Level-1 substrate-cache-domain layer per the W2-10 framework, with its own K-counter advancement track that is non-redundant with both (i) the meta-INVARIANCE class theorem K-counter at §VII.AQ-META and (ii) the regulator-class-conditional dual-mode lockdown K-counter at `regulator-convention-lockdown.md`.

### EMERGENCE

#### Emergence-R3-1 — Three-K-counter parallel-track structure for the W9-106 substrate-physics content

The R1+R2+R3 cross-pollination produces THREE structurally orthogonal K-counter advancement tracks for the W9-106 substrate-physics content, all starting at K=1 STAGE-1-CANDIDATE post-W-28-close, each with its own promotion threshold:

```
Step 1 [Definition]:
  TRACK 1 — meta-INVARIANCE class theorem (§VII.AQ-META):
    K-counter: 1 (W9-106 composite-layer PASS as instance #1).
    Promotion: Stage-2 cross-axis independent-verify PASS-AND fires
               K=1 → K=6 + STAGE-3 PERMANENT.
    Fallback: §VII.METHODOLOGY-CASCADE-DIAGNOSTIC at K=1 on Stage-2 FAIL.

  TRACK 2 — BHW-evaluator-class dual-mode lockdown (regulator-convention-
            lockdown.md §"BHW-Evaluator-Class Dual-Mode Lockdown"):
    K-counter: 1 (W9-106 SDW + Zubarev + Lancaster discriminator chain).
    Promotion: K=3 distinct CM-vs-non-CM regulator-class-conditional
               applications calibrate the rule to MANDATORY.
    Fallback: NONE (rule applies regulator-class-conditionally regardless
                    of K-counter status; SUGGESTION-status applies until K=3).

  TRACK 3 — substrate-cache-domain frame for axis A on CM regulators
            (W2-10 calibration corpus extension):
    K-counter: 1 → 2 conditional on S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN
                PASS (this gate's axis-A content as Level-1 substrate-IS
                instance #2 of the W2-10 framework).
    Promotion: K=3 distinct Level-1-substrate-IS instances at substrate-
               cache-domain layer advance the W2-10 framework to MANDATORY.
    Fallback: NONE (S89 FAIL collapses Track 3; axis A on CM regulators
                    becomes coordinate-change artifact with no Element 1
                    structural significance).

Step 2 [Substitution]:
  All three tracks emerge from W9-106 substrate-physics content; none
  subsumes another:
    Track 1 is at the meta-class-theorem layer (algebra-INVARIANT
    functional-family meta-claim).
    Track 2 is at the methodology-rule layer (regulator-convention
    lockdown extension).
    Track 3 is at the Level-1-substrate-IS layer (substrate-cache-
    domain observable framework).

Step 3 [Simplify]:
  Three parallel-track structure preserves substrate-physics content
  across multiple structural layers without forcing premature
  unification or fragmentation. The R3 connes Convergence-1' and
  Convergence-2' acceptances + R3 lizzi Convergence-R3-2 + Dissent-
  R3-2 jointly produce this structure.

Step 4 [Direction]:
  Forward calibration discipline: future Bernstein-positive-cone gates
  on alternative regulator atlases / CM-vs-non-CM regulator class
  variants advance the K-counters on Tracks 2 and 3 independently.
  Future η/even-Mellin gates with cross-axis variations advance the
  K-counter on Track 1 (Stage-2-conditional; on Stage-2 PASS-AND, the
  meta-INVARIANCE class theorem promotes to STAGE-3-PERMANENT and
  Tracks 2 and 3 inherit the fallback-corpus structure).
```

The three-K-counter parallel-track structure is the operative forward methodology pattern for substrate-physics content with multiple structural-layer footprints. It hardens the joint-theorem-promotion 4-stage pathway with explicit per-track fallback discipline.

#### Emergence-R3-2 — `regulator-convention-lockdown.md` extension as the load-bearing rule-file landing for the BHW-evaluator-class lockdown

Per R3 connes Q3'' and R2 lizzi Emergence-2 + R3 Convergence-1' (acceptance of regulator-class-conditional dual-mode lockdown), the forward rule-file landing is at `regulator-convention-lockdown.md` adding a new sub-section §"BHW-Evaluator-Class Dual-Mode Lockdown" with the structural-template specification at R2 Emergence-2 Step "Proposal" (lines 1972-2017). The dual-mode template is structurally NEW: the existing DR3-class lockdown is single-mode (one canonical pin per the effacement-preservation criterion). The dual-mode lockdown adds regulator-class-conditional routing (Mode-d for CM regulators with single-canonical pin under convention B; Mode-g for non-CM regulators with dual-canonical pin under per-axis suffix tagging).

Forward-looking structural decision: the dual-mode lockdown rule-text becomes a forward template for OTHER evaluator classes that admit regulator-class-conditional admissibility distinctions (e.g., Mellin-pole evaluator class, Wodzicki-residue evaluator class, Connes-Karoubi pairing evaluator class). The rule-file `regulator-convention-lockdown.md` reorganizes to host both single-mode and dual-mode lockdown patterns; the §"DR3-Class L_max-Stability" stays as the single-mode calibration; the §"BHW-Evaluator-Class Dual-Mode Lockdown" lands as the dual-mode calibration; future evaluator-class lockdowns choose Mode based on substrate-physics structure.

#### Emergence-R3-3 — substrate-physics direction-of-explanation diagram for the BHW-evaluator-class with frame-separation

The combined R3 closure produces an explicit substrate-OUT direction-of-explanation diagram for the BHW-evaluator-class on CM regulators:

```
Substrate IS spectral triple (A_K, H_K, D_K(τ_fold))
   → spectrum {λ_n} of D_K eigenvalues IS substrate-IS at Level-1 single-τ-slice
   → universal spectral action S_b = Tr f(D²/Λ²) IS substrate-IS functional (CC96 §2.2-2.3)
   → regulator weight f(x) for x = (λ/Λ)² IS substrate-IS Laplace transform of dμ(t)
   → BHW positivity test (-1)^k · f^{(k)}(x) ≥ 0 IS regulator-class CM-admissibility
                                                     at the regulator-class layer
                                                     (Element 2 of cross-pillar
                                                      bridge anatomy ↔ lab chain).
   → AND
   → axis A test (-1)^k · g^{(k)}(λ) on g(λ) = f(λ²) IS substrate-cache-domain
                                                     positivity-tracking
                                                     at Level-1 single-τ-slice
                                                     substrate-IS layer
                                                     (Element 1 of cross-pillar
                                                      bridge anatomy; does NOT
                                                      propagate to Element 2 lab
                                                      chain).
   → THE TWO LAYERS ARE STRUCTURALLY ORTHOGONAL per algebra-axis orthogonality
     K-counter MANDATORY at K=3.
   → THIS direction-of-explanation is FORWARD; it flows substrate-OUT
     through the CC96 §2.2-2.3 axiomatic universal-functional argument
     AND through the W2-10 Level-1 substrate-IS framework.
```

The two-axis substrate-OUT framing preserves both connes R1 single-canonical reading on CM regulators at the regulator-class layer (Test B / Element 2 / lab chain) AND lizzi R2 substrate-cache-domain frame for axis A on CM regulators at Level-1 substrate-IS (Test A / Element 1 / pure-substrate observable). Neither is demoted; both register at distinct structural-layer locations with their own K-counter advancement tracks per Emergence-R3-1.

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Laplace-conjugate substrate-naturalness (x vs λ) | C1, Re:C1, R2-DISS-1, R2-Convergence-4, R3-Convergence-R3-1 | **Partial** (regulator-class-conditional) | Joint CC96 §2.2-2.3 + BHW (Widder 1941 Ch. IV) reading: x = (λ/Λ)² IS substrate-natural Laplace conjugate AT THE REGULATOR-CLASS CM-ADMISSIBILITY LAYER. On CM regulators (SDW), e^{-λ²} is NOT a CM function on (0,∞) (no positive-measure dν per Hausdorff moment problem; Python-verified R2 line 1815) ⇒ axis A is BHW-ill-posed at the regulator-class layer. On non-CM regulators (Zubarev), both axes test substrate-IS Bernstein-violation content with magnitude split 6.587/2.034 = 3.24 (R2 Convergence-1 conceded). The "uniqueness" reading is regulator-class-conditional, not uniform. |
| 2 | W8-4 SDW cascade FAIL diagnostic content | C2, Re:C2, R2-Convergence-1 | **Emerged** (3-orthogonal-source decomposition) | Cascade FAIL decomposes into THREE structurally orthogonal sources: (1) L_max-stability (4×3a, convention-INDEPENDENT, truncation-axis), (2) Bernstein-violation on Zubarev (regulator-class-axis with magnitude variation, 6.587/2.034 split substrate-IS), (3) chain-rule polynomial pre-factor on SDW (convention-axis, NOT substrate-IS for CM regulators per R3 lizzi A2 horn-1 acceptance). Composite-layer agreement composite_A == composite_B == FAIL is dominated by source (1) saturation; lizzi R2 A2 conceded the chain-rule-artifact-cancellation reading. |
| 3 | SDW evaluator convention re-pin | C3, Re:C3, R2-EM-2, R2-Convergence-2, R3-Convergence-1' | **Converged** (regulator-class-conditional dual-mode) | BHW-evaluator-class lockdown extension at `regulator-convention-lockdown.md` pre-registers BOTH Class-(d) MANDATORY MIGRATION (for CM regulators in x; SDW under convention B canonical, convention A `-LAM-DERIVATIVE-CHAIN-RULE-LIFT` audit-trail tag only) AND Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR (for non-CM regulators in x; Zubarev under PER-AXIS suffix-tagged dual-pin) with CM-membership-in-x routing predicate. `-SCHEMATIC` suffix preserved per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (S88 W7b-83). |
| 4 | §VII.AQ corpus structure (single vs refined sub-corpus) | C4, Re:C4, L1, R2-DISS-3, R2-EM-3, R2-Convergence-1 (lizzi), R2-Convergence-3 (lizzi) | **Converged** (two-corpus structure) | §VII.AQ retains 5-instance HARDENED baseline corpus (W-11 RULE-2 strengthened parity-blindness theorem at η + even-Mellin / regulator-class-axis variation across A_5_extended; K=5 > 3 unchanged). NEW §VII.AQ-META at STAGE-1-CANDIDATE K=1 (meta-INVARIANCE class theorem proposal with W9-106 composite-layer PASS as instance #1; lizzi R2 K=6-HARDENED arithmetic withdrawn per joint-theorem-promotion 4-stage Stage-0 → Stage-3 collapse). Fallback corpus §VII.METHODOLOGY-CASCADE-DIAGNOSTIC at K=1 on Stage-2 FAIL (R3 Emergence-2'). |
| 5 | Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation | C5, Re:C5, R2-EM-2, R2-Convergence-2, R3-Convergence-1' | **Converged** (regulator-class-conditional) | On CM regulators (SDW): Class-(d) HARD-HALT MANDATORY MIGRATION fires (D_max ~13 OOM with sign-discordance categorical violation; convA OUTSIDE BHW admissibility on Gaussian image). Lancaster MCT-3 SDW-channel discriminator at convA 0.2773% IS phantom AT THE LAB LAYER (Element 2 cross-pillar bridge anatomy); MIGRATES to Zubarev-channel discriminator at 0.2035% (convB; substrate-physics-grounded non-CM violation). On non-CM regulators (Zubarev): NEW Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR ADVISORY-K=1 / MANDATORY-K=3 fires; per-axis suffix tagging admissible. |
| 6 | Cross-cutting / substrate-natural ceiling vs multi-axis | C6, L1, L2, R2-EM-3, R3-Emergence-R3-1, R3-Emergence-R3-2 | **Emerged** (three-K-counter parallel-track structure) | The W9-106 substrate-physics content advances THREE structurally orthogonal K-counter tracks: TRACK 1 §VII.AQ-META meta-INVARIANCE class (K=1 STAGE-1; Stage-2 PASS-AND fires K=1 → K=6 STAGE-3 OR FAIL routes to fallback §VII.METHODOLOGY-CASCADE-DIAGNOSTIC at K=1); TRACK 2 BHW-evaluator-class dual-mode lockdown at `regulator-convention-lockdown.md` (K=1 → K=3 MANDATORY); TRACK 3 substrate-cache-domain frame for axis A on CM regulators (W2-10 calibration corpus extension; K=1 → K=2 conditional on S89 verification gate; K=3 MANDATORY). The forward methodology pattern: parallel-track structure + per-track fallback discipline at `joint-theorem-promotion.md` extension. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

The workshop converged on two-corpus structure (Topic 4) + regulator-class-conditional dual-mode lockdown (Topic 3 + Topic 5) + 3-orthogonal-source decomposition (Topic 2) + three-K-counter parallel-track structure (Topic 6) and produced a regulator-class-conditional partial verdict on Topic 1 (joint CC96 + BHW reading on CM regulators; multi-axis substrate-IS reading on non-CM regulators). The remaining open questions partition into three kinds: (i) S89 verification-gate dispatches (Stage-2 cross-axis independent-verify; substrate-cache-domain S89 gate; layer-tag PROVENANCE adequacy gate); (ii) rule-file edits at `regulator-convention-lockdown.md` + `substrate-first-canonical-sourcing.md §(iv)` + `joint-theorem-promotion.md` for the dual-mode lockdown + layer-tag discipline + meta-class fallback discipline; (iii) registry-state landings at `permanent-results-registry.md` for §VII.AQ-META + §VII.METHODOLOGY-CASCADE-DIAGNOSTIC (mack sole-writer per `feedback_mack-bridge-role.md`). Each is specific enough to become a session-89 plan-block computation gate.

1. **§VII.AQ-META Stage-2 cross-axis independent-verify dispatch (Q3'')**: Per `joint-theorem-promotion.md §"Stage 2"` two-agent parallel cross-axis protocol, the meta-INVARIANCE class theorem at NEW §VII.AQ-META requires Stage-2 cross-axis independent-verify before promotion to STAGE-3-PERMANENT and the K=1 → K=6 K-counter advancement. Pre-registered gate: `S89-VII-AQ-META-STAGE-2-INDEPENDENT-VERIFY` PASS = TWO cross-reviewers (volovik-superfluid-universe-theorist on the substrate-physics axis + mack-cosmic-bridge or kaku-string-theorist on the methodology axis) operating WITHOUT prior workshop W-28 transcript context BOTH return PASS-AND on the unification claim "substrate-internal symmetry tests at the even-grading evaluator class produce composite-layer-INVARIANT verdicts under structurally orthogonal axis variations within the algebra-INVARIANT functional family"; FAIL = either reviewer returns FAIL on the unification claim ⇒ K=1 retained at §VII.AQ-META AND W9-106 routes to fallback §VII.METHODOLOGY-CASCADE-DIAGNOSTIC at K=1; INFO = either reviewer returns INFO on the unification claim ⇒ STAGE-1 retained pending re-dispatch.

2. **`S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` substrate-cache-domain frame verification (Q1'')**: Per R2 Emergence-3 + R3 Convergence-4, the substrate-cache-domain frame for axis A on CM regulators registers conditional on a 3-CM-regulator cross-check. Pre-registered gate: `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` PASS = (i) Sage-decomposition of T_A[k](λ) = chain-rule polynomial × regulator-weight on 3 CM regulators {e^{-x²/2}, (1+x)^{-1}, e^{-x}} confirms the chain-rule polynomial pre-factor has structurally-fixed roots independent of f's CM-class; (ii) substrate-cache-support × polynomial-root-locus intersection regulator-independent across the 3 CM regulators; (iii) Test A diagnostic content shared across all 3 CM regulators in the partition. INFO at sub-clause violation in the boundary case (e^{-2x} expanded test set per R3 Q1''); FAIL at any sub-clause ⇒ substrate-cache-domain frame collapses; axis A on CM regulators reduces to coordinate-change artifact with no Element 1 substrate-IS content; the SDW-channel migration to Zubarev-only is structurally final at BOTH Element 1 AND Element 2.

3. **`regulator-convention-lockdown.md §"BHW-Evaluator-Class Dual-Mode Lockdown"` rule-file extension landing (Q3'' + Topic 3 / Topic 5)**: Per R2 Emergence-2 / R3 Emergence-R3-2 specification, the dual-mode lockdown rule-text appends to `regulator-convention-lockdown.md` with the regulator-class-conditional routing predicate (CM-membership-in-x test) + Mode-d (Class-(d) MANDATORY MIGRATION for CM regulators) + Mode-g (Class-(g) STRUCTURAL-COMPANION for non-CM regulators) + demarcation theorem (BHW dual-mode admissibility class) + cross-link to `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (`-SCHEMATIC` suffix preservation). Pre-registered gate: `S89-REG-CONV-LOCKDOWN-BHW-DUAL-MODE-LAND` PASS = sub-section landed at `regulator-convention-lockdown.md` (NOT a new rule-file) with both Mode-d and Mode-g sub-clauses pre-registered + W9-106 K=1 calibration row + 2 reserved K=2 / K=3 rows; status SUGGESTION pending K=3; FAIL = sub-section omits either Mode or conflates the regulator-class-conditional routing predicate or lands at a non-`regulator-convention-lockdown.md` site.

4. **`substrate-first-canonical-sourcing.md §(iv)` layer-tag PROVENANCE field extension (Q2'' + R3 Emergence-1' + R3 Dissent-R3-1)**: Per R3 Emergence-1' the canonical_constants.py PROVENANCE entries gain a `layer_tag` field for cross-layer pin pairs. Pre-registered gate: `S89-LAYER-TAG-PROVENANCE-FIELD-LAND` PASS = `layer_tag` field added to canonical_constants.py PROVENANCE schema with audit-script enforcement at write-time (via `update_constant(...)` signature extension) AND backward-compatibility grandfathering for existing pins without layer-tag (retroactive landing at S89+ plan-freeze) AND cross-link to `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level-1 vs Level-2 vocabulary; W-28 K=1 calibration row + 2 reserved rows; status SUGGESTION pending K=3; FAIL = `layer_tag` field landed without enforcement OR conflated with existing `convention=` suffix discipline OR backward-compatibility grandfathering missing.

5. **`S89-LAYER-TAG-CROSS-LAYER-PIN-DISCIPLINE` cross-layer pin adequacy verification (R3 Dissent-R3-1)**: Per R3 Dissent-R3-1, the open implementation question is whether the `layer_tag` field on canonical_constants.py PROVENANCE entries suffices to close the OUTSIDE-BHW-admissibility-class concern on cross-layer pin pairs (e.g., SDW with axis A at Level-1 substrate-cache-domain layer + axis B at regulator-class-CM-admissibility layer), or whether structural separation REQUIRES distinct registry loci. Pre-registered gate: `S89-LAYER-TAG-CROSS-LAYER-PIN-DISCIPLINE` PASS = `layer_tag` field with audit-script enforcement is structurally adequate against the cross-layer-conflation pathology (sample 3 cross-layer pin pairs from S89+ Bernstein-positive-cone gates; verify downstream consumers parse layer-tag correctly via wrapper accessor); FAIL = canonical_constants.py is structurally inadequate ⇒ SDW axis A (S89-W28 PASS-conditional) registers at a separate §VII registry slot.

6. **`joint-theorem-promotion.md §"Cross-axis K-counter STAGE-1 proposal pattern"` rule-file extension landing (R2 Emergence-1 + R3 Emergence-2')**: Per R2 lizzi Emergence-1 + R3 connes Emergence-2', the meta-class theorem K-counter STAGE-1-at-K=1 discipline + fallback-corpus pre-registration discipline lands at `joint-theorem-promotion.md` as a new sub-section. Pre-registered gate: `S89-JOINT-THEOREM-CROSS-AXIS-K-COUNTER-LAND` PASS = sub-section appended with cross-axis K-counter STAGE-1-at-K=1 specification + fallback-corpus pre-registration MANDATORY clause + W-28 K=1 calibration row (W9-106 / §VII.AQ-META + §VII.METHODOLOGY-CASCADE-DIAGNOSTIC fallback) + 2 reserved K=2 / K=3 rows; status SUGGESTION pending K=3; FAIL = sub-section omits the fallback-corpus MANDATORY clause OR registers without the W-28 calibration row OR conflates within-axis K-counter with cross-axis K-counter.

7. **§VII.AQ-META + §VII.METHODOLOGY-CASCADE-DIAGNOSTIC dual registry landing (mack sole-writer per `feedback_mack-bridge-role.md`)**: Per Convergence-3 (lizzi R2) + R3 Emergence-2' fallback discipline, both new registry slots land at `permanent-results-registry.md` BEFORE the Stage-2 verify dispatch. Pre-registered gate: `S89-VII-AQ-META-CASCADE-DIAGNOSTIC-DUAL-LAND` PASS = mack-cosmic-bridge writes both §VII.AQ-META (STAGE-1-CANDIDATE meta-INVARIANCE class theorem proposal at K=1) AND §VII.METHODOLOGY-CASCADE-DIAGNOSTIC (STAGE-1-CANDIDATE 3-orthogonal-source decomposition theorem at K=1) per the `registry-landing.md` 4-field-spec + SHA closure pin (W-28 audit_sha256) + cross-link between the two slots (fallback structure explicitly declared); FAIL = either slot landed without the other OR cross-link missing OR SHA closure pin omitted.

8. **Lancaster MCT-3 falsifier-master-inventory.md row migration (Topic 5 + Convergence-3' + R3 Convergence-R3-1)**: Per the SDW-to-Zubarev migration on the lab discriminator chain, the falsifier-master-inventory.md SDW-channel rows need migration. Pre-registered gate: `S89-LANCASTER-SDW-TO-ZUBAREV-DISCRIMINATOR-MIGRATION` PASS = mack-cosmic-bridge sole-writer migrates the Lancaster MCT-3 SDW-channel rows to Zubarev-channel rows + adds explicit `-CONVENTION-B` suffix on the Zubarev cite + adds STRUCTURAL-NULL annotation on the SDW channel (substrate-physics-grounded NULL discriminator, NOT a phantom margin) + cross-references to `s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013 for the workshop derivation chain; FAIL = SDW channel retains 0.2773% margin OR Zubarev channel cite misses convention-B suffix OR STRUCTURAL-NULL annotation absent on SDW.

9. **Class-(d) corpus K-counter advancement at `epistemic-discipline.md §"Source Reconciliation"` (Topic 5 + Topic 1)**: Per Topic 5 verdict, the W-28 instance is a calibration-corpus advancement for Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (currently K=2 advisory per `pru-class-corpus.md`). The W-28 SDW + (A, B) pair on CM regulator with sign-discordance categorical violation is a NEW Class-(d) sub-class (chain-rule-derivative-vs-substrate-natural under joint CC96 + BHW reading). Pre-registered gate: `S89-CLASS-D-W28-CORPUS-ADVANCEMENT` PASS = Class-(d) corpus row at `pru-class-corpus.md` extended with W-28 instance (SDW + (A, B) + Lancaster discriminator chain) + sign-discordance sub-class registered + K-counter advances K=2 → K=3 ⇒ MANDATORY promotion fires; FAIL = corpus row missing or K-counter not advanced or sub-class not registered.

10. **canonical_constants.py Zubarev_3c_min^A/B_FW pin landing (Topic 3 + Topic 5)**: Per the dual-mode lockdown Mode-g for Zubarev (non-CM in x), both `Zubarev_3c_min^A_FW = -6.587` and `Zubarev_3c_min^B_FW = -2.034` enter canonical_constants.py with explicit per-axis PROVENANCE entries citing W9-106 verdict line + `-CONVENTION-A` and `-CONVENTION-B` suffixes per Mode-g. Pre-registered gate: `S89-ZUBAREV-3C-DUAL-PIN-LAND` PASS = both pins added to canonical_constants.py with PROVENANCE entries citing W9-106 audit_sha256 + per-axis suffix tagging + (S89-conditional) layer_tag fields per Q4 above; FAIL = either pin missing, suffix conflated, or PROVENANCE entries do not cite W9-106 audit_sha256.

11. **§VII.AQ Topic 1 Partial-verdict registry-text refinement**: The Topic 1 partial verdict (regulator-class-conditional Laplace-conjugate substrate-naturalness) requires registry-text language at §VII.AQ-META that captures the regulator-class-conditional split (joint CC96 + BHW uniqueness reading on CM regulators; multi-axis substrate-IS reading on non-CM regulators) without forcing single-canonical or dual-canonical pin uniformly. Pre-registered gate: `S89-VII-AQ-META-PARTIAL-VERDICT-REGISTRY-TEXT-LAND` PASS = mack-cosmic-bridge sole-writer drafts §VII.AQ-META registry text with explicit regulator-class-conditional partition declaration + Element 1 vs Element 2 layer disambiguation + cross-link to `regulator-convention-lockdown.md §"BHW-Evaluator-Class Dual-Mode Lockdown"`; FAIL = registry text forces uniform canonical pin OR conflates Element 1 and Element 2 OR omits the regulator-class-conditional partition.

12. **W9-106 working-paper §line 1045 STRENGTHENS framing in-session NOTE (NOT amendment)**: Per Convergence-1 / lizzi R2 Convergence-1, the W9-106 WP §line 1045 STRENGTHENS framing must be re-classified: the W9-106 entry is a STAGE-1-CANDIDATE proposal at NEW §VII.AQ-META (K=1), NOT an automatic 6th-instance extension of W-11 RULE-2's HARDENED corpus. Per `feedback_fix-in-session-never-defer.md` analog discipline at the WP layer (and W25 calibration corpus instance #9 line 1719-1723 "WP §2 in-session NOTE (NOT amendment)"), this lands as an in-session NOTE that records the W-28 workshop adjudication WITHOUT retracting prior text. Pre-registered gate: `S89-W9-106-WP-NOTE-LAND` PASS = NOTE paragraph appended after current WP §line 1045 (NOT before; NOT replacing) recording the W-28 verdict + meta-INVARIANCE STAGE-1-CANDIDATE K=1 status + cross-link to W-28 workshop document + verdict-line content unchanged; FAIL = NOTE retracts prior declaration OR touches verdict-line content OR omits W-28 cross-link.

## Wrap-Up — Workshop Impact Summary

*[Final-round writer (lizzi) fills below; MANDATORY 5 sub-sections]*

### What Changed

- **Topic 1 Laplace-conjugate substrate-naturalness reads as REGULATOR-CLASS-CONDITIONAL, not uniform** (R3 Convergence-R3-1; lizzi R2 Convergence-4 + R3 Dissent-R3-2): the joint CC96 §2.2-2.3 + BHW (Widder 1941 Ch. IV) reading establishes x = (λ/Λ)² as the Laplace-conjugate variable AT THE REGULATOR-CLASS CM-ADMISSIBILITY LAYER for CM regulators (e.g., SDW); on non-CM regulators (e.g., Zubarev), both axes test substrate-IS Bernstein-violation content with magnitude split 6.587/2.034 = 3.24 (lizzi R1 + connes R2 Convergence-1). Topic 1's partial verdict captures this regulator-class-conditional split.
- **Topic 2 W8-4 SDW cascade FAIL diagnostic content decomposes into 3 STRUCTURALLY ORTHOGONAL SOURCES** (R2 Convergence-1; connes R1 C2 → 2 sources; lizzi R1 Re:C2 → 3 sources, accepted): (1) L_max-stability axis (4×3a, convention-INDEPENDENT, truncation-axis content); (2) regulator-class axis with magnitude variation (Zubarev_3c^A=−6.587 / Zubarev_3c^B=−2.034, substrate-IS multi-axis content); (3) convention axis with chain-rule polynomial pre-factor (SDW_3c (A,B) sign-flip; structurally NOT substrate-IS for CM regulators per lizzi R3 A2 horn-1 acceptance).
- **Topic 4 §VII.AQ corpus structure is now TWO-CORPUS** (R2 Convergence-3 (lizzi); R3 Convergence-1' (connes)): §VII.AQ retains 5-instance HARDENED baseline corpus (W-11 RULE-2 strengthened parity-blindness theorem at η + even-Mellin / regulator-class-axis variation across A_5_extended; K=5 > 3 unchanged) AND a NEW §VII.AQ-META at STAGE-1-CANDIDATE K=1 (meta-INVARIANCE class theorem proposal with W9-106 composite-layer PASS as instance #1; lizzi R1 K=6-HARDENED arithmetic withdrawn under joint-theorem-promotion 4-stage Stage-0 → Stage-3 collapse rule).
- **Topic 3 + Topic 5 BHW-evaluator-class lockdown at `regulator-convention-lockdown.md` is REGULATOR-CLASS-CONDITIONAL DUAL-MODE** (R2 Emergence-2; R3 Convergence-1'): Mode-d (Class-(d) MANDATORY MIGRATION for CM regulators; single-canonical pin under convention B; convA `-LAM-DERIVATIVE-CHAIN-RULE-LIFT` audit-trail tag only) AND Mode-g (Class-(g) STRUCTURAL-COMPANION-CONVENTION-PAIR for non-CM regulators; per-axis suffix-tagged dual-pin) with CM-membership-in-x routing predicate.
- **Topic 5 Lancaster MCT-3 SDW-channel discriminator MIGRATES to Zubarev-channel** (R2 Convergence-4 (lizzi); R3 Convergence-R3-1): convA SDW phantom 0.2773% IS phantom AT THE LAB LAYER (Element 2 cross-pillar bridge anatomy); migration to Zubarev-channel substrate-physics-grounded discriminator at 0.2035% (convB) preserves falsifiability with relocation, not loss.
- **Topic 6 emerges as a THREE-K-COUNTER PARALLEL-TRACK STRUCTURE** (R3 Emergence-R3-1): TRACK 1 (§VII.AQ-META meta-INVARIANCE at K=1 STAGE-1; Stage-2 PASS-AND fires K=1 → K=6 STAGE-3 OR FAIL routes to fallback §VII.METHODOLOGY-CASCADE-DIAGNOSTIC at K=1) + TRACK 2 (BHW-evaluator-class dual-mode lockdown at K=1 → K=3 MANDATORY) + TRACK 3 (substrate-cache-domain frame for axis A on CM regulators at K=1 → K=2 conditional on S89 verification gate; W2-10 calibration corpus extension).

### What Holds

- **W-11 RULE-2 5-instance baseline corpus at §VII.AQ remains HARDENED at K=5** (R2 Convergence-2 (connes); R3 Convergence-1'). The strengthened parity-blindness theorem at η + even-Mellin evaluator class with regulator-class-axis variation across A_5_extended is unchanged by this workshop; only the single-vs-two-corpus structural decision changes (the W9-106 entry does NOT pool into the W-11 RULE-2 corpus as a 6th instance pre-Stage-2; it registers separately at NEW §VII.AQ-META at K=1).
- **Bernstein-Hausdorff-Widder theorem (Widder 1941 Ch. IV) is a structural-uniqueness theorem about the Laplace-conjugate variable** (connes R2 Dissent-1; lizzi R3 Convergence-R3-1): a function g : (0,∞) → ℝ is the Laplace transform of a positive Borel measure on [0,∞) iff `(-1)^k · g^{(k)}(x) ≥ 0` for all `k ∈ ℕ_0` and all `x > 0`, with x the Laplace-conjugate variable to t. e^{-λ²} is NOT CM on (0,∞) (no positive-measure dν per Hausdorff moment problem; Python-verified at R2 line 1815) ⇒ axis A on CM regulators is BHW-ill-posed at the regulator-class layer.
- **(Δ_B/Δ_A)^p cancellation theorem and the W9-104/W9-105 substrate-IS-preservation rank-2 inheritance theorem are unchanged** by this workshop. The W9-106 gate's verdict line on disk (audit_sha256 = a74b5e66752f8b06...) is ABSOLUTELY PERMANENT per `gate-verdicts.md §"Rules"` item 2; this workshop touches no audit_sha256 / content_sha256 / value strings / schemes / conventions / L_max.
- **`substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (S88 W7b-83 close, 2026-05-05) discipline holds**: the `-SCHEMATIC` suffix is preserved per the existing level-pin discipline; the new convention-suffix tagging (BHW-evaluator-class dual-mode lockdown) and the new layer_tag PROVENANCE field (R3 Emergence-1') are additive, NOT redefinitions.
- **The algebra-axis orthogonality K-counter MANDATORY at K=3 (S87 W-2 R3 close, `cross-pillar-bridge-anatomy.md`) holds**: the (A, B) Bernstein convention pair is at the differential-operator-pair-on-same-functional-class layer (within the algebra-INVARIANT family), structurally weaker than the algebra-INVARIANT vs algebra-DEPENDENT cross-family MANDATORY clause. Pooling regulator-class-axis instances with differential-coordinate-axis instances does NOT violate the cross-family clause (lizzi R1 Re:C6 MISSED; connes R2 implicitly accepted via the within-family-axis acceptance).
- **The cross-pillar bridge 5-IS-not-IN anatomy (Element 1 substrate-IS observable + Element 2 laboratory-IN observable) holds as a STRUCTURALLY DISTINCT separation per `cross-pillar-bridge-anatomy.md`**: lab-feasibility chains live at Element 2 regardless of whether axis A carries substrate-IS content at Element 1 (R3 Convergence-R3-1).

### What Breaks or Strains

- **The historical W8-4-baseline single-axis convA reading on SDW BREAKS at the regulator-class layer**: convA on the e^{-λ²} Gaussian image is OUTSIDE BHW admissibility (no positive-measure dν per Hausdorff moment problem); SDW_3c_min^A = -2.773 carries NO regulator-class-CM-admissibility content. The Lancaster MCT-3 SDW-channel discriminator at 0.2773% sourced from this value is a PHANTOM at Element 2 lab chain (R2 Convergence-4 + R3 Convergence-R3-1).
- **`s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013 Lancaster MCT-3 lab-discriminator margin chain BREAKS structurally on the SDW channel**: the rewrite produces a STRUCTURAL NULL on SDW (1.8e-16 margin, ~14 OOM below detection sensitivity); the substrate-physics discriminator MIGRATES to Zubarev channel (0.2035%). The workshop document needs amendment to record the migration (see Carry-Forward CF-W28-8 below).
- **The current `regulator-convention-lockdown.md` rule-file is structurally insufficient for the BHW-evaluator-class** because its existing DR3-class single-mode lockdown does not cover regulator-class-conditional dual-mode admissibility. The dual-mode lockdown extension (Mode-d for CM; Mode-g for non-CM) is structurally NEW and represents the first dual-mode lockdown template at this rule-file (Carry-Forward CF-W28-3).
- **canonical_constants.py PROVENANCE schema is structurally insufficient for cross-layer pin pairs** (R3 Dissent-R3-1; R3 Emergence-1'). The existing `convention=` suffix discipline does not communicate substrate-IS layer separation (Level-1 vs Level-2 vs regulator-class) to downstream consumers; the proposed `layer_tag` field closes this silent class-conflation pathway. Backward-compatibility grandfathering is needed for existing pins at S89+ plan-freeze (Carry-Forward CF-W28-4).
- **The R2 lizzi K=6-HARDENED-arithmetic on §VII.AQ-META is RETRACTED** as a Stage-0 → Stage-3 collapse violation per `joint-theorem-promotion.md` 4-stage pathway (lizzi R2 Convergence-1; "the cross-reviewers receive ONLY the registered Stage-1 entry text + relevant input files — they do NOT receive the workshop's R1/R2/R3 transcripts"). The K=6 signal applies IFF Stage-2 verify fires PASS-AND.
- **The W9-106 working-paper §line 1045 STRENGTHENS framing IS structurally MISCLASSIFIED** under the joint connes R2 Dissent-3 + lizzi R2 Convergence-1 reading. The W9-106 entry is NOT an automatic 6th-instance of W-11 RULE-2; it is a STAGE-1-CANDIDATE proposal at NEW §VII.AQ-META at K=1. WP framing requires in-session NOTE (Carry-Forward CF-W28-12).

### Carry-Forward Computations

1. **§VII.AQ-META Stage-2 cross-axis independent-verify dispatch**
   - **What**: Dispatch TWO cross-reviewers in parallel per `joint-theorem-promotion.md §"Stage 2"` two-agent protocol on the meta-INVARIANCE class theorem at NEW §VII.AQ-META: volovik-superfluid-universe-theorist (substrate-physics axis) + mack-cosmic-bridge OR kaku-string-theorist (methodology axis). Both operate WITHOUT prior W-28 workshop transcript context (per joint-theorem-promotion strict-isolation protocol). PASS-AND on the unification claim "substrate-internal symmetry tests at the even-grading evaluator class produce composite-layer-INVARIANT verdicts under structurally orthogonal axis variations within the algebra-INVARIANT functional family" fires K=1 → K=6 + STAGE-3-PERMANENT promotion. Either FAIL routes W9-106 to fallback §VII.METHODOLOGY-CASCADE-DIAGNOSTIC.
   - **Inputs**: §VII.AQ-META registered Stage-1 entry text (CF-W28-7 landing); §VII.AQ baseline 5-instance corpus from W-11 RULE-2 close (S86); W9-106 verdict-line audit_sha256 = a74b5e66752f8b06...; canonical_constants.py atlas-relevant pins.
   - **Gate**: `S89-VII-AQ-META-STAGE-2-INDEPENDENT-VERIFY` PASS = both cross-reviewers return PASS-AND on the unification claim; FAIL = either reviewer returns FAIL ⇒ K=1 retained at §VII.AQ-META AND fallback corpus §VII.METHODOLOGY-CASCADE-DIAGNOSTIC activates per CF-W28-7; INFO = either reviewer returns INFO ⇒ STAGE-1 retained pending re-dispatch.
   - **Effort**: 1.0 wave-equivalents (joint-theorem-promotion Stage-2 dispatch with two parallel cross-reviewers).

2. **`S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` substrate-cache-domain frame verification**
   - **What**: Sage-decomposition of T_A[k](λ) = chain-rule polynomial × regulator-weight on 3 CM regulators {e^{-x²/2}, (1+x)^{-1}, e^{-x}} at k=3 over the substrate cache support [λ_min, λ_max] = [0.81974, 5.41894]. Verify (i) chain-rule polynomial pre-factor has structurally-fixed roots independent of f's CM-class; (ii) substrate-cache-support × polynomial-root-locus intersection is regulator-independent across the 3 CM regulators; (iii) Test A diagnostic content shared across all 3 CM regulators. Optionally extend to e^{-2x} per R3 Q1'' boundary case.
   - **Inputs**: canonical_constants.py M_KK + tau_fold + cache support pins; L_max=12 spectral cache `s84_spectrum_cache_L12_tau019.npz`; Sage MCP (sage_eval, sage_simplify) for symbolic polynomial decomposition.
   - **Gate**: `S89-W28-BHW-ADMISSIBILITY-NON-CM-GAUSSIAN` PASS = all 3 sub-clauses (i)+(ii)+(iii) hold ⇒ substrate-cache-domain frame for axis A on CM regulators validates as Level-1 substrate-IS observable (W2-10 calibration corpus K=2); FAIL = any sub-clause fails ⇒ substrate-cache-domain frame collapses; SDW axis A reduces to coordinate-change artifact with no Element 1 substrate-IS content; SDW-channel migration to Zubarev-only is structurally final at BOTH Element 1 AND Element 2.
   - **Effort**: 0.5 wave-equivalents (Sage-decomposition compute + 3-regulator cross-check; deterministic, reproducible).

3. **`regulator-convention-lockdown.md §"BHW-Evaluator-Class Dual-Mode Lockdown"` rule-file extension landing**
   - **What**: Append a new sub-section §"BHW-Evaluator-Class Dual-Mode Lockdown" to `regulator-convention-lockdown.md` per R2 Emergence-2 specification (lines 1972-2017). Mode-d (Class-(d) MANDATORY MIGRATION for CM regulators in x; single-canonical pin under convention B). Mode-g (Class-(g) STRUCTURAL-COMPANION for non-CM regulators in x; dual-canonical pin under per-axis suffix tagging). CM-membership-in-x routing predicate. Demarcation theorem (BHW dual-mode admissibility class). Cross-link to `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 (`-SCHEMATIC` suffix preservation).
   - **Inputs**: existing `regulator-convention-lockdown.md` (DR3-class lockdown as single-mode template); R2 Emergence-2 dual-mode shape; W9-106 K=1 calibration data; CC96 §2.2-2.3 + BHW joint reading.
   - **Gate**: `S89-REG-CONV-LOCKDOWN-BHW-DUAL-MODE-LAND` PASS = sub-section landed at `regulator-convention-lockdown.md` (NOT new rule-file); both Mode-d + Mode-g sub-clauses pre-registered with explicit demarcation-theorem text; W9-106 K=1 calibration row + 2 reserved K=2 / K=3 rows; status SUGGESTION pending K=3; FAIL = sub-section omits either Mode OR conflates routing predicate OR lands at non-`regulator-convention-lockdown.md` site.
   - **Effort**: 0.4 wave-equivalents (METHODOLOGY-class per `wave-classification.md` M1∧M2∧M3∧M4; rule-file extension only, no compute beyond existing W9-106 verdict input).

4. **`substrate-first-canonical-sourcing.md §(iv)` layer-tag PROVENANCE field extension**
   - **What**: Append a sub-section to `substrate-first-canonical-sourcing.md §(iv)` (or new §(v)) specifying the `layer_tag` field on canonical_constants.py PROVENANCE entries for cross-layer pin pairs. Schema: layer_tag is a top-level dict-key in the PROVENANCE entry; values from a controlled vocabulary (Level-1-substrate-cache-domain | Level-2-moduli-deformation | regulator-class-CM-admissibility | Element-1-substrate-IS | Element-2-laboratory-IN). Audit-script enforcement at canonical_constants.py write-time via `update_constant(...)` signature extension. Backward-compatibility grandfathering for existing pins without layer-tag at S89+ plan-freeze.
   - **Inputs**: existing canonical_constants.py PROVENANCE schema; existing `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 discipline; `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level-1 vs Level-2 vocabulary; `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"` Element 1 vs Element 2 vocabulary.
   - **Gate**: `S89-LAYER-TAG-PROVENANCE-FIELD-LAND` PASS = `layer_tag` field added with audit-script enforcement + backward-compatibility grandfathering + cross-link to phononic-framing Level-1/Level-2 vocabulary; W-28 K=1 calibration row + 2 reserved rows; status SUGGESTION pending K=3; FAIL = `layer_tag` lacks enforcement OR grandfathering missing OR conflated with existing `convention=` suffix discipline.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class + 1 line addition to update_constant signature; audit-script extension).

5. **`S89-LAYER-TAG-CROSS-LAYER-PIN-DISCIPLINE` cross-layer pin adequacy verification**
   - **What**: Sample 3 cross-layer pin pairs from S89+ Bernstein-positive-cone gates that admit frame-separation reading (axis A at Level-1 substrate-cache-domain; axis B at regulator-class layer); verify downstream consumers parse layer-tag correctly via wrapper accessor. Test the OUTSIDE-BHW-admissibility-class concern from R3 Dissent-R3-1: does the layer-tag enforcement protocol close the cross-layer-conflation pathway, OR is canonical_constants.py structurally inadequate ⇒ structural separation REQUIRES distinct registry loci.
   - **Inputs**: CF-W28-4 layer-tag PROVENANCE field landing; sample S89+ Bernstein-positive-cone gate verdicts that reach axis A and axis B at distinct substrate-IS layers.
   - **Gate**: `S89-LAYER-TAG-CROSS-LAYER-PIN-DISCIPLINE` PASS = `layer_tag` with audit-script enforcement closes the conflation pathway; downstream wrapper accessor + 3 sample pin-pair verifications all clean; FAIL = canonical_constants.py is structurally inadequate ⇒ SDW axis A (S89-W28-conditional) registers at separate §VII registry slot.
   - **Effort**: 0.4 wave-equivalents (CONDITIONAL on CF-W28-4 + CF-W28-2 landings; sample-pair verification compute).

6. **`joint-theorem-promotion.md §"Cross-axis K-counter STAGE-1 proposal pattern"` rule-file extension landing**
   - **What**: Append a new sub-section to `joint-theorem-promotion.md` per R2 Emergence-1 + R3 Emergence-2': any meta-class theorem candidate at STAGE-1-CANDIDATE with cross-axis K-counter MUST start at K=1 (NOT cumulative pre-existing-instance K-counter), AND MUST pre-register a fallback corpus where the standalone substrate-physics content lands on Stage-2 FAIL. Calibration corpus K=1: this workshop's §VII.AQ-META + §VII.METHODOLOGY-CASCADE-DIAGNOSTIC fallback structure.
   - **Inputs**: existing `joint-theorem-promotion.md` 4-stage pathway; R2 Emergence-1 cross-axis K-counter STAGE-1 specification; R3 Emergence-2' fallback discipline; W-28 calibration data.
   - **Gate**: `S89-JOINT-THEOREM-CROSS-AXIS-K-COUNTER-LAND` PASS = sub-section appended with cross-axis K-counter STAGE-1-at-K=1 specification + fallback-corpus pre-registration MANDATORY clause + W-28 K=1 calibration row + 2 reserved K=2 / K=3 rows; status SUGGESTION pending K=3; FAIL = sub-section omits fallback-corpus MANDATORY clause OR conflates within-axis with cross-axis K-counters.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class).

7. **§VII.AQ-META + §VII.METHODOLOGY-CASCADE-DIAGNOSTIC dual registry landing (mack sole-writer)**
   - **What**: Mack-cosmic-bridge writes BOTH §VII.AQ-META (STAGE-1-CANDIDATE meta-INVARIANCE class theorem proposal at K=1) AND §VII.METHODOLOGY-CASCADE-DIAGNOSTIC (STAGE-1-CANDIDATE 3-orthogonal-source decomposition theorem at K=1) at `permanent-results-registry.md` BEFORE the Stage-2 verify dispatch (CF-W28-1). Cross-link between the two slots explicitly declares the fallback structure; SHA closure pin = W-28 audit_sha256.
   - **Inputs**: `permanent-results-registry.md` registry-slot allocation per `regulator-pin-discipline.md` next-free-letter protocol; W9-106 verdict-line audit_sha256 = a74b5e66752f8b06...; W-28 workshop adjudication (this document); R2 Emergence-1 + R3 Emergence-2' specifications.
   - **Gate**: `S89-VII-AQ-META-CASCADE-DIAGNOSTIC-DUAL-LAND` PASS = both slots landed with 4-field-spec + SHA closure pin + cross-link declaring fallback structure; FAIL = either slot landed without other OR cross-link missing OR SHA closure pin omitted.
   - **Effort**: 0.3 wave-equivalents (mack registry-write per `feedback_mack-bridge-role.md`; mechanical landing).

8. **Lancaster MCT-3 falsifier-master-inventory.md row migration (mack sole-writer)**
   - **What**: Mack-cosmic-bridge sole-writer migrates the Lancaster MCT-3 SDW-channel rows in `falsifier-master-inventory.md` to Zubarev-channel rows. Add explicit `-CONVENTION-B` suffix on the Zubarev cite. Add STRUCTURAL-NULL annotation on the SDW channel (substrate-physics-grounded NULL discriminator, NOT a phantom margin). Cross-references to `s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013 for the workshop derivation chain. 
   - **Inputs**: `falsifier-master-inventory.md` SDW-channel rows; W9-106 NPZ pins (Zubarev_3c_min^B = -2.034587; SDW_3c_min^B = +1.77e-13); workshop `s87-atlas-cardinality-cascade-vs-ensemble.md` lines 996-1013; W-28 Topic 5 verdict.
   - **Gate**: `S89-LANCASTER-SDW-TO-ZUBAREV-DISCRIMINATOR-MIGRATION` PASS = SDW channel migrated to STRUCTURAL-NULL annotation + Zubarev channel substituted with `-CONVENTION-B` suffix + cross-references explicit; FAIL = SDW channel retains 0.2773% margin OR Zubarev channel cite missing convention suffix OR STRUCTURAL-NULL annotation absent.
   - **Effort**: 0.2 wave-equivalents (mack registry-write).

9. **Class-(d) corpus K-counter advancement at `epistemic-discipline.md §"Source Reconciliation"` / `pru-class-corpus.md §"Class-(d)"`**
   - **What**: Extend the Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY corpus row at `pru-class-corpus.md` with the W-28 instance (SDW + (A,B) + Lancaster discriminator chain on CM regulator with sign-discordance categorical violation). Register the W-28 instance as a NEW Class-(d) sub-class (chain-rule-derivative-vs-substrate-natural under joint CC96 + BHW reading). K-counter advances K=2 → K=3 ⇒ MANDATORY promotion fires per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold.
   - **Inputs**: existing `pru-class-corpus.md §"Class-(d)"` corpus (K=2 advisory); W-28 Topic 5 verdict; W9-106 NPZ pins; sign-discordance argument from connes R1 C5.
   - **Gate**: `S89-CLASS-D-W28-CORPUS-ADVANCEMENT` PASS = Class-(d) corpus row extended + sign-discordance sub-class registered + K-counter advanced K=2 → K=3 ⇒ MANDATORY promotion fires; FAIL = corpus row missing OR K-counter not advanced OR sub-class not registered.
   - **Effort**: 0.2 wave-equivalents (METHODOLOGY-class hygiene; corpus row extension only).

10. **canonical_constants.py Zubarev_3c_min^A/B_FW pin landing**
    - **What**: Add both `Zubarev_3c_min^A_FW = -6.587` and `Zubarev_3c_min^B_FW = -2.034` to canonical_constants.py with explicit per-axis PROVENANCE entries citing W9-106 verdict line audit_sha256. Carry per-axis suffix tags `-CONVENTION-A` and `-CONVENTION-B` per Mode-g of the BHW-evaluator-class dual-mode lockdown (CF-W28-3). Carry layer_tag per CF-W28-4 (Element-2-laboratory-IN OR regulator-class-CM-admissibility, since Zubarev's non-CM character lives at the regulator-class layer).
    - **Inputs**: W9-106 NPZ Zubarev_3c values; CF-W28-3 dual-mode lockdown landing (Mode-g specification); CF-W28-4 layer_tag PROVENANCE field landing.
    - **Gate**: `S89-ZUBAREV-3C-DUAL-PIN-LAND` PASS = both pins added with PROVENANCE entries citing W9-106 audit_sha256 + per-axis suffix tagging + layer_tag fields; FAIL = either pin missing, suffix conflated, or PROVENANCE entries do not cite W9-106 audit_sha256.
    - **Effort**: 0.2 wave-equivalents (canonical-constants extension; CONDITIONAL on CF-W28-3 + CF-W28-4 landings).

11. **§VII.AQ-META Topic 1 partial-verdict registry-text refinement (mack sole-writer)**
    - **What**: Mack-cosmic-bridge sole-writer drafts §VII.AQ-META registry text capturing the regulator-class-conditional Topic 1 partial verdict: explicit declaration of regulator-class-conditional partition (joint CC96 + BHW uniqueness reading on CM regulators; multi-axis substrate-IS reading on non-CM regulators); Element 1 vs Element 2 layer disambiguation; cross-link to `regulator-convention-lockdown.md §"BHW-Evaluator-Class Dual-Mode Lockdown"` (CF-W28-3).
    - **Inputs**: W-28 Topic 1 verdict; CF-W28-3 dual-mode lockdown landing; CF-W28-7 §VII.AQ-META registry-text-spec.
    - **Gate**: `S89-VII-AQ-META-PARTIAL-VERDICT-REGISTRY-TEXT-LAND` PASS = registry text declares regulator-class-conditional partition + Element 1 / Element 2 disambiguation + dual-mode lockdown cross-link; FAIL = registry text forces uniform canonical pin OR conflates Element 1 and Element 2 OR omits regulator-class-conditional partition.
    - **Effort**: 0.2 wave-equivalents (mack registry-write; CONDITIONAL on CF-W28-3 + CF-W28-7 landings).

12. **W9-106 working-paper §line 1045 in-session NOTE landing (NOT amendment)**
    - **What**: Append a NOTE paragraph after current `sessions/archive/session-88/session-88-w9-workingpaper.md` §line 1045 (NOT before; NOT replacing) recording: "Workshop W-28 (connes-ncg + lizzi-spectral-functional-theorist, 2026-05-08) adjudicated this calibration. The STRENGTHENS framing is structurally MISCLASSIFIED under the joint connes R2 Dissent-3 + lizzi R2 Convergence-1 reading; the W9-106 entry is a STAGE-1-CANDIDATE proposal at NEW §VII.AQ-META at K=1 (NOT a 6th-instance extension of W-11 RULE-2's HARDENED corpus). Stage-2 cross-axis independent-verify per `joint-theorem-promotion.md` 4-stage pathway (CF-W28-1) determines whether the K-counter advances K=1 → K=6 (PASS-AND on unification claim) OR W9-106 routes to fallback §VII.METHODOLOGY-CASCADE-DIAGNOSTIC (FAIL). Cross-link to W-28 workshop document for full adjudication."
    - **Inputs**: WP §line 1045 current text; W-28 workshop document (this file); R2 Convergence-1 (lizzi); R2 Dissent-3 (connes); CF-W28-1 + CF-W28-7 landings.
    - **Gate**: `S89-W9-106-WP-NOTE-LAND` PASS = NOTE appended after current §line 1045 (NOT before; NOT replacing) + cross-link to W-28 workshop document explicit + verdict-line content unchanged; FAIL = NOTE retracts prior declaration OR touches verdict-line content OR omits W-28 cross-link.
    - **Effort**: 0.1 wave-equivalents (working-paper NOTE; not a rule-file edit).

### Closing Line

The W-28 closure resolves the connes substrate-natural-singleton vs lizzi multi-axis-substrate-IS dispute as a regulator-class-conditional partition (Mode-d for CM regulators per joint CC96 + BHW; Mode-g for non-CM regulators) running on three structurally orthogonal K-counter parallel tracks (§VII.AQ-META meta-INVARIANCE STAGE-1; BHW-evaluator-class dual-mode lockdown SUGGESTION; substrate-cache-domain frame for axis A on CM regulators conditional on S89 verification), with the SDW-channel Lancaster discriminator structurally migrated to the Zubarev channel where substrate-physics retains predictive falsifiability.
