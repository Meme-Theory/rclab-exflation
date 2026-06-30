# Capstone Review: *The Phonon-Exflation Equation* — Principle-Theoretic Reading

**Date**: 2026-05-26
**Agent**: einstein-theorist (Einstein)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (capstone, §0–§9 + verification ledger)
- Cross-checked against `canonical_constants.py` / knowledge MCP: `tau_fold = 0.19`, `a_2_FW_zeta = 2776.165389`, `w0_FW = -0.918`, gates `S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD` (FAIL), `T3-BATCH-S75-EMERGENT-LORENTZ` (INFO), `W7/S37` Structural Monotonicity Theorem
- Framing law: `.claude/rules/phononic-framing.md`

> This is an independent capstone review, distinct from the Round-2 fresh-eyes patch pass already logged in the verification ledger. I engage the document where my field has the deepest purchase: the principle/constructive distinction, general covariance, the equivalence principle, motion-from-field-equations (EIH), the cosmological term, and the completeness criterion. I do not re-adjudicate any PROVEN/CLOSED status or gate verdict — those are authoritative here.

---

## I. Session Outcome

The document is, in my vocabulary, a **principle theory wearing a constructive theory's clothing** — and it is at its strongest precisely where it admits this. Its master object `S[D_K(τ), f, Λ]` is not a constructive model built from hypothetical constituents (it does not posit fields-in-a-box and ask how they move); it is a *single constraint* — one self-adjoint operator viewed through one spectral functional — from which the stage and its contents are recovered as theorems. That is the move I spent 1915 making for gravity: stop positing the field on a background, and let the background *be* the field. The capstone makes the analogous move one level deeper: the metric is not posited at all, it is the `a₂` moment.

My central structural finding: **the document's honesty about §6.3 is not a blemish to be repaired but the load-bearing seam of the whole construction.** The missing effective Friedmann map and the INFO-status emergent Lorentz invariance / equivalence principle (§9 frontier #8) are *the same gap* viewed from two sides, and that gap is exactly where a principle theory must be incomplete until the principle (general covariance of the *emergent* metric) is derived rather than inherited. I recommend three sharpenings below, all in the direction of stating this seam more precisely; none weakens a result.

I found **no physics error** and **one genuine internal tension** worth flagging (§IV.3, the C1-postulate vs E7-derived-clock boundary, which the document mostly handles but lets blur in one place). The substrate-first arrow is held cleanly throughout.

---

## II. Key Results — Read Through the Principle/Constructive Lens

### II.1 The equation derives its own stage — this is a principle theory, and the document should name it as such

**Result**: `S[D_K(τ), f, Λ]` as a *principle-theoretic* object (GEOMETRIC at root; the excitations on it are PHONONIC).

In my 1919 *Times* essay I drew the line between **principle theories** (high-level empirical generalizations that *constrain* — thermodynamics, relativity) and **constructive theories** (built up from hypothesized constituents — kinetic gas theory). Constructive theories give you a mechanism; principle theories give you a *prohibition* — a statement of what any admissible solution must satisfy, independent of the constituents. Relativity is a principle theory: the light postulate and the relativity postulate are constraints, and Lorentz invariance is what survives them.

§0 and §1 of this document are, structurally, a principle-theoretic derivation. The operative constraints are: (i) Connes' reconstruction theorem (geometry *is* the spectral triple, not data alongside it); (ii) the four PROVEN axioms (KO-dim 6, CPT commutant `[J,D_K]=0`, SM branching, trace-theorem gauge-invariance, §1.2); (iii) the dimension-spectrum convergence cone `S_d = {0,2,4,6,8}` (§3.3), which tells the substrate *which functionals f are even candidates*. The Standard Model gauge group is not posited — it is `SU(A_K) = U(1)×SU(2)×SU(3)`, the unimodular unitary group of the algebra. Gravity is not a law imposed on the substrate — it is the second spectral moment.

This is the correct and the strongest framing, and §0 already makes the decisive comparison: *"in a GUT the manifold survives when every field is switched off; here it does not."* I would add a single sentence making the methodological status explicit, because it pre-empts the most common category error a reader brings:

> **Recommended insert (§0, after the "categorically stronger" paragraph):** "Methodologically, `S[D_K(τ), f, Λ]` is a *principle theory* in the precise sense of Einstein's 1919 distinction: it is not a constructive model of fields-in-spacetime but a single constraint — one operator, one functional — and the field content, the couplings, and the metric are *consequences forced by that constraint*, never independent postulates. The free-parameter ledger (§1.4) is therefore short by construction, and the things that remain open (the modulus value, the functional `f`, the family number) are exactly the inputs a principle theory is *entitled* to leave to a future constructive completion."

Naming the methodology this way also disarms a cheap criticism: "you still have free parameters." A principle theory is *allowed* free inputs — thermodynamics has the equation of state, relativity has the metric signature and the matter content. What a principle theory may not do is be internally inconsistent or smuggle its conclusion into its premises. On that test the document is clean.

### II.2 The no-well / monotone-ramp result is structurally correct, and `e^{−S}` boundary-domination is its right reading

**Result**: `dS/dτ|_fold = +58,672.8 > 0`, monotone; `S` has no interior stationary point at any τ (E7 Structural Monotonicity Theorem). GEOMETRIC.

I verified the underlying theorem in the knowledge graph: `W7/S37`, ⟨λ²⟩(τ) monotone for ALL monotone `f`, ALL `Λ`, ALL sectors, 9,600 checks; and the S84 stationary-point gate returns FAIL with `value = −2.04×10⁴` — i.e. `τ_fold` is explicitly *not* a stationary point of the bare action. Both are faithfully represented. (This matches my own memory: *"tau_fold NOT stationary of bare S[D_K(τ)]"*, S84-W8a.)

The §1.3a move — reading the monotone `S(τ)` as monotone weight `e^{−S(τ)}` in the partition function, hence **no interior saddle in τ**, hence boundary-domination at genesis, hence *transit physics rather than stationary-phase equilibration* — is exactly right and is the part I want to commend most strongly. This is a limiting-case argument of the cleanest kind: it eliminates an entire class of theories (every slow-roll / potential-well cosmogenesis) *without computing a trajectory*, by reading the structure of the action. It is the spectral-action analog of the elevator: the absence of a restoring force is not a small-coupling fact, it is a structural fact about where the statistical weight lives, and it forbids settling the way the elevator forbids distinguishing free-fall from inertial motion.

One regime-of-validity note the document should pin (it is implicit but not stated): the boundary-domination reading of `e^{−S}` is a *leading-order saddle statement*. The document is careful elsewhere (§1.3a flags the one-loop `½ Tr ln(D_K²/Λ²)` as a threshold correction, not part of the master object). I recommend one explicit sentence that the monotonicity → boundary-domination inference is at tree level, and that a one-loop `Γ_1loop` with non-trivial τ-curvature could in principle re-introduce a local feature — which the framework asserts it does not, but which is a *claim with a regime*, not an identity. This is consistent with my memory note that *"computation beats gedankenexperiment when the potential landscape is nontrivial"*: the no-well result is robust at tree level, but the assertion that one loop does not spoil it is an additional, separately-defensible statement.

### II.3 The Wronskian / layer-independence theorem is the document's best principle-theoretic result

**Result**: `W[a₀,a₂,a₄](τ) ∝ R_K'(τ)³ = e^{−12τ}(e^{3τ}−1)⁶`, vanishing to sixth order at and only at τ=0 (Spectral-Moment Decoupling Theorem, S75 W2-E, CERTIFIED). GEOMETRIC.

This is the result I find most beautiful and most *principled*, and I want to record why in my own terms. The skeptic's objection — "is `a₄` just a dressed-up function of `a₀, a₂`?" — is the right adversarial question, because if the three moments were functionally dependent, the claim "vacuum, gravity, and matter are distinct physics" would collapse to "one knob, three labels." The Wronskian settles it the way a covariance argument settles a coordinate-artifact question: the three moments are algebraically independent *everywhere the universe lives*, and degenerate to a single scale only at the maximally-symmetric genesis instant. The degeneracy structure is itself meaningful — it is exactly at the round, `R_K'(0)=0` configuration that the curvature-degree story collapses, because there is no curvature gradient to separate degree-0, degree-1, and degree-2 polynomials.

I checked the verification-ledger residual (`R_K'(τ) = e^{−4τ}(e^{3τ}−1)²` ⇒ `W ∝ e^{−12τ}(e^{3τ}−1)⁶`, residual `0`, Sage). The cube-of-the-gradient structure is dimensionally and algebraically consistent: a 3×3 Wronskian of `{V, R_K·V, R_K²·V}` with `V` constant factors as `V³ · W[1, R_K, R_K²] = V³ · 2(R_K')³`, and `(R_K')³ = (e^{−4τ}(e^{3τ}−1)²)³`. Clean.

The §4.4 argument that the **spectral-moment reading is primary** (over the causal and scale readings) is also correct and well-reasoned: only the moment layers carry a certified algebraic-independence theorem; the scale reading is the moment reading in `Λ`-clothing; the causal reading presupposes the moment decomposition. I endorse this ordering without reservation. A layer notion backed by a Wronskian is a stronger object than a layer notion that is a stage of a trajectory — the same way that an invariant is a stronger object than a coordinate.

### II.4 The cosmological term is in the *right* moment — and the document's CC framing is principle-theoretically honest

**Result**: `a₀` (the zeroth moment, `Λ⁴` weight) is the cosmological term; `Λ_cc` lives in a *different spectral moment* than gravity (`a₂`). GEOMETRIC, with the late-time DE reading PHONONIC.

I have a uniquely scarred relationship with the cosmological constant, so I read §7 and §8.5 with particular attention. The framework's structural claim is the one I would most want to be true and am most suspicious of: that `Λ` is *geometrically natural* — it is the `a₀` heat-kernel coefficient, present in the expansion whether or not anyone inserts it by hand. This is precisely the lesson I should have drawn in 1917 and did not: the field equations *naturally admit* a cosmological term, and treating its appearance as a "blunder" was itself the error. Here the term is not inserted; it is the volume moment of `D_K`. That is the correct location.

The document is then scrupulously honest about what this does *not* buy:
- §8.5: absolute-energy observables (CC, `A_s`) remain **conditional on an SDW-convergence statement that is itself an open gate** (JACOBSON-NONLOCAL-64). Ratio-observables are truncation-robust; absolute magnitudes are not. This is exactly the right boundary, and it matches my CC-status memory (the 110–115 OOM gap lives entirely in the `a₀·M_KK⁴` normalization).
- §7.1: the `ρ_vac/ρ_obs = 1.032` PASS is **doubly conditional** — on the C10 tracking ansatz *and* on the external FRW `H(t)` the tracking law feeds. The document states plainly that `1.032` "is not yet a from-`D_K` derivation of the dark-energy density." This is the honesty I asked for in the Round-2 pass and it is present.

One principle-theoretic strengthening. The document says (§0) that because `N₃ = 0` (BDI, ³He-B child), the cosmological-constant layer is "a q-theory relaxation problem, not a topological-protection statement." This is correct and important, but it should be tied to the *completeness* question explicitly: a relaxation mechanism is a constructive (dynamical) answer, and the framework does not yet have it (the SDW-convergence gate is open). So the CC story is currently a principle-theoretic *location* (the term is the `a₀` moment — settled) without a constructive *magnitude* (the relaxation dynamics — open). I recommend the document say this in exactly those words, because it precisely separates what is permanent (location) from what is contingent on an open gate (magnitude):

> **Recommended insert (§8.5 or §9 frontier #6):** "The cosmological term's *location* — the `a₀` moment, geometrically natural, not inserted — is a permanent principle-theoretic result. Its *magnitude* is a constructive (relaxation-dynamics) question that the open SDW-convergence gate has not yet answered. The 114-OOM problem is therefore not a problem of where Λ comes from (settled) but of the dynamics that relaxes it (open). The framework should not be read as having solved the cosmological-constant *problem*; it has correctly *located* the cosmological-constant *term*."

---

## III. The Honest Gap (§6.3): General Covariance and the Equivalence Principle Are the Same Missing Derivation

This is the section my field exists to interrogate, and I want to give it the full treatment, because the document — correctly — calls §6.3 "the most important caveat in the document" but does not fully connect it to §9 frontier #8. **They are one gap, and the unifying name for it is: the emergent metric `g_M` has not been shown to be generally covariant or to satisfy the equivalence principle beyond leading order.**

### III.1 What §6.3 actually owes, stated in GR terms

The document is exactly right that "Friedmann is the wrong question" *at the fundamental level* and *wrong about the effective level* — both must be said, and §6.3 says both. Let me sharpen *why* the effective level cannot be waved away, in the language of motion-from-field-equations.

In 1938 Einstein–Infeld–Hoffmann established that in general relativity the equations of motion of matter are **not independent postulates** — they are *consequences* of the field equations via the Bianchi identities (`∇_μ G^{μν} = 0` forces `∇_μ T^{μν} = 0`, and the geodesic motion of a test body follows from the field equations themselves). This is the deepest expression of general covariance: there is no separate "force law"; motion is geometry. My memory records that the framework has the analog — *"Bianchi identity satisfied by modulus EOM (algebraic, EIH applied to KK)"*, and the EIH program is "S44 quantitatively complete." Good. **But that EIH result lives on the internal `K` geometry, not on the emergent 4D metric `g_M`.** The gap in §6.3 is precisely that the framework has not closed the loop from `S_SA(τ)` to a *4D gravitational action* whose Bianchi identity would force the emergent matter's motion. Until that loop closes:

- there is no derived `H² = (8πG/3)ρ` (the S74 W1-E FAIL — *structural*, not a near-miss);
- the framework *borrows* the container-observer's FRW `H(t)` as external input (C10) for every late-time observable;
- and `a_eff(τ) = (a₂(τ)/a₂(today))^{1/2}` is a spectral-complexity relabeling, **not** a scale factor obeying a derived dynamics.

The document says all of this. I am endorsing it and adding the EIH framing: **the missing effective Friedmann map is the missing emergent EIH theorem.** A derived `a(t)` would *be* the statement that emergent matter moves on geodesics of `g_M` because the `a₂`-channel field equations make it so. That is the thing that is owed.

### III.2 §9 frontier #8 is the same gap, and the document under-connects them

Frontier #8 registers emergent Lorentz invariance / equivalence principle as **INFO** (gate `T3-BATCH-S75-EMERGENT-LORENTZ`, which I confirmed returns INFO, no-run-no-gate, MIGRATED). The document's statement is careful: leading-order universality of free fall is *warranted* (one emergent light-cone from one gap structure → all excitations share the cone → weak EP at leading order), but higher-order isotropy / emergent-Lorentz is *inherited* from the Volovik gap-node universality class, *not derived*.

Here is the connection the document should make explicit. **The equivalence principle and general covariance are not two open items; they are one, and they are the same one as the `a(t)` gap.** The logical chain is:

1. A derived effective Friedmann equation requires `S_SA(τ) →` a 4D gravitational action for `g_M` (§6.3 requirement (i)).
2. A 4D gravitational action for `g_M` that is generally covariant *is* the statement that `g_M` couples universally to all emergent matter — which is the equivalence principle.
3. General covariance of that action, via the emergent Bianchi identity, *is* the statement that emergent matter moves on geodesics — which is emergent EIH, i.e. the derived `a(t)`.

So frontier #8 ("emergent Lorentz / EP, INFO") and frontier #1 ("the `a(t)` gap, the single most important open item") are **logically equivalent open problems**. Closing one closes the other. The document lists them as items #1 and #8 on the same frontier list without saying they are the same item. I recommend a cross-link:

> **Recommended insert (§9, frontier #8, final sentence):** "This is not a separate frontier from #1: a *derived, generally-covariant* 4D action for `g_M` is simultaneously (a) the effective Friedmann map (frontier #1), (b) the emergent equivalence principle (universal coupling of `g_M` to all excitations), and (c) the emergent Einstein–Infeld–Hoffmann theorem (geodesic motion of emergent matter as a *consequence* of the `a₂`-channel field equations, not a postulate). The framework already possesses the EIH theorem on the *internal* `K` geometry (Bianchi identity satisfied by the modulus EOM); what is owed is its lift to the *emergent* `g_M`. Frontiers #1 and #8 are one gap, and closing it is the single structural prerequisite for both."

This is the most consequential structural recommendation in my review. It is not a criticism — the document's honesty is exemplary — it is a *unification* of two stated open items, which sharpens the surviving solution space exactly as a constraint-map should: there is *one* missing theorem, not two, and it has a precise statement (generally-covariant emergent 4D action for `g_M`).

### III.3 A gedankenexperiment for the emergent equivalence principle

Since I am asked to think in my own field, let me offer the thought experiment that would *test* whether the framework's leading-order EP warrant is genuine or merely inherited — a falsifier the framework can in principle compute without observation.

**The two-excitation elevator.** Take two distinct phononic excitations of `D_K(τ)` with *different* spectral content — say, an acoustic-band (B1) relay pattern and an optical-band (B3) relay pattern. Place both in the same region of the emergent geometry near the fold, where the `a₂`-channel curvature gradient `R_K'(τ)` is non-zero (the same gradient whose cube is the Wronskian). The equivalence principle, *if it holds for the emergent `g_M`*, demands that both excitations fall along the *same* emergent geodesic — their trajectories must be independent of their spectral composition. The framework's leading-order warrant says they share one light-cone, hence one cone-structure, hence (to leading order) one free-fall trajectory. **But the test is at next-to-leading order:** do the B1 and B3 dispersion relations, expanded around the emergent light-cone, agree in their *curvature coupling* (the term linear in `R_K`), or do they differ?

If they differ, the framework has an emergent *violation* of the equivalence principle — a spectral-composition-dependent free-fall — which would be a sharp, computable falsifier (and a genuine departure from GR, hence observationally interesting). If they agree to the relevant order, the EP is *derived*, not inherited, and frontier #8 promotes from INFO to a structural result. My memory note *"Flat bands squeeze less — B1 acoustic dominates by factor 37"* suggests the bands are *not* dynamically equivalent in their squeezing response, which makes this test non-trivial: the bands demonstrably differ in some couplings. The question is whether they differ in the *curvature* coupling specifically. This is a limiting-case computation (NLO dispersion around the emergent cone, two bands, ratio of curvature couplings), cheap relative to a full `a(t)` derivation, and it *informs* the §6.3 gap by testing one of its three logical components (the EP component) in isolation. I have written it up as a carry-forward (§V.1).

### III.4 One place the C1/E7 boundary blurs (the only genuine internal tension I found)

§6.1 and §6.3 are mostly scrupulous about the boundary: **postulated** = "τ parameterizes cosmic time" (C1, the *ordering* / arrow); **derived** = "τ is a legitimate globally-monotone clock" (E7, `dS/dτ > 0` with no stationary point makes τ a monotone invertible function of `t`). This is the correct decomposition and I endorse it.

But §6.1 then writes the integral
`t(τ) = t₀ + ∫ dτ'/τ̇(τ')`, with "τ̇ known LOCALLY at the fold; GLOBALLY UNDETERMINED."
and §6.3 says "the global `t(τ)` ... [is] not derived." These are consistent. The blur is one level up, in the §9 summary table row "At time t": *"τ is a derived monotone clock; C1 postulates τ = cosmic time."* A careless reader collapses "derived monotone clock" and "= cosmic time" into "derived cosmic time," which is exactly what is *not* claimed. The distinction is load-bearing and worth one extra clause:

> **Recommended tightening (§9 summary table, "At time t" row):** "τ is a derived monotone *parameter* (E7); that this parameter *is* cosmic time, and the global rate `τ̇(τ)` away from the fold, are postulated/undetermined (C1)." 

The substantive content is already correct everywhere; this is purely to prevent the reading "we derived time," which the document does not claim and must not be over-read as claiming. Flagged per the instruction to surface internal blurs.

---

## IV. Structural Implications

### IV.1 The completeness criterion, applied to the framework itself

My EPR completeness criterion — *every element of physical reality must have a counterpart in the theory* — is the right lens for the §1.3 "what it does NOT claim" ledger and the §9 frontier list. The framework is **incomplete in the precise EPR sense, and admits it cleanly**: there are elements of physical reality (the value of `τ`, the functional `f`, the family number, the dark-energy *magnitude*, the emergent `a(t)`) for which the theory currently has *no derived counterpart* — they are inputs or open gates. This is not the same as being *wrong*. A principle theory is permitted incompleteness; what it may not do is be inconsistent or claim completeness it lacks. The document's repeated refusal to over-claim ("both halves are load-bearing"; "stated without softening") is the correct epistemic posture and is, in fact, what distinguishes this capstone from the unfalsifiable-by-flexibility cosmologies it competes against. I record this as a *strength*, framed as a constraint: the incompleteness is *localized* to a short list of named gates, and each gate is a specific missing theorem, not a vague hope.

### IV.2 Constraint-map reading: what the capstone closes, opens, and locates

Stated as geometry (constraint → implication → surviving space):

- **Closed / permanent (walls):** the SM gauge group as `SU(A_K)`; gravity as the `a₂` moment; the CC *term* as the `a₀` moment; layer algebraic-independence (Wronskian); no interior stationary point (E7); CPT via `[J,D_K]=0`; one generation as `ℂ¹⁶`. These define walls of the solution space and are not re-litigable.
- **Located but not derived (principle without construction):** the CC *magnitude* (location settled, relaxation dynamics open); the DE equation of state `w₀` (Volovik-partition value `−0.918` is a derived branch, but conditional on the same external `H`).
- **Open (the live frontier):** the *single* gap of §III.2 — generally-covariant emergent 4D action ⇒ {`a(t)`, EP, emergent EIH}; `n_s` functional selection; `m_H` route; SDW convergence; family number.

The most important constraint-map update this capstone makes is the one I recommend it state explicitly: **frontiers #1 and #8 collapse to one item.** That *reduces* the dimensionality of the open frontier — it is good news reported as a boundary.

### IV.3 On the substrate-first arrow and emergent GR — the framing holds

I checked the document against the framing law's most dangerous trap for an agent of my training: explaining a substrate result by invoking GR. The document inverts the arrow correctly and consistently. "Gravity is not a fundamental law imposed on the substrate — gravity is the second spectral moment of `D_K`" (§4.1). "`H(t)` is the *readout* of [spectral reorganization], not a clock the vacuum decays in" (§6.3). The area-theorem and Einstein-equation relapses my memory warns against are absent. The one place an Einstein-trained reader *would* relapse — treating the missing `a(t)` as "we still owe a spacetime container" — the document pre-empts with the category statement, and my §III.1 addition *strengthens* the substrate-first reading rather than reverting it: the owed object is not a container, it is an emergent EIH theorem *for a metric that is itself a spectral moment*. The direction of explanation stays `D_K → a₂ → g_M → motion`, never the reverse.

### IV.4 A note on the `f₂ ≈ 92` dictionary closure (my Round-2 patch, re-verified)

§8.3 now closes the reduced Chamseddine–Connes dictionary at `f₂ ≈ 92` (an `O(10²)` cutoff-moment, same legitimacy class as the CC `f₂` at unification), and correctly quarantines the `f_2_default = 2.34` Gaussian-cutoff pin as a *different scheme's* `f₂` (cross-substituting gives the spurious ≈39× residual). This is the patch I asked for and it is correctly stated. I re-affirm: the "self-consistency residual" is self-consistency-by-construction (one equation, two unknowns `(M_KK, f₂)`, with `M_KK` pinned independently by the S42 Sakharov/zeta route), not a contradiction. My standing memory caveat applies and the document honors it: *"f₂=1 sharp gravity match (G_pred/G_obs=1.000) is CIRCULAR; never cite as prediction."* The document does **not** cite the dictionary closure as a gravity *prediction* — it cites it as a consistency check that the `a₂` channel carries the Newton coupling, explicitly weaker than and not to be conflated with the independent E30 Sakharov mode-sum corroboration (factor 2.29 at `Λ = 10 M_KK`). Correctly handled.

---

## V. Carry-Forward Computations

### V.1 The two-excitation emergent-EP gedankenexperiment (NLO dispersion test)
- **What**: Expand the BdG dispersion `ω_k = √((λ_k²−μ²)² + Δ_k²)` for one B1 (acoustic) and one B3 (optical) excitation around the emergent light-cone near `τ_fold`, to next-to-leading order in the curvature `R_K`. Compute the ratio of the curvature-couplings (the term linear in `R_K`) between the two bands: `κ_EP ≡ (∂²ω_{B1}/∂R_K)/(∂²ω_{B3}/∂R_K)` at fixed emergent momentum. EP-derived iff `κ_EP → 1` to the relevant order; EP-violating (computable falsifier) iff `κ_EP ≠ 1`.
- **Inputs**: `tau_fold = 0.19`; the B1/B3 band structure (`SO(8)→U(2)` band split, §2.4); `R_K(τ) = −¼e^{−4τ}+2e^{−τ}−¼+½e^{2τ}` and `R_K'(τ)`; the BdG gap `Δ_k`; the B1-dominates-by-37 squeezing asymmetry (cross-check that the *squeezing* asymmetry does not contaminate the *curvature* coupling).
- **Gate**: feeds / promotes `T3-BATCH-S75-EMERGENT-LORENTZ` (currently INFO). New gate `EMERGENT-EP-NLO`: PASS if `|κ_EP − 1| < tolerance` (EP derived at NLO, promote frontier #8 to structural); FAIL if `|κ_EP − 1|` exceeds tolerance with a clean sign (computable EP-violation falsifier); INFO if NLO expansion is scheme-ambiguous.
- **Effort**: 1 agent session (symbolic NLO expansion + two-band ratio; Sage-verifiable). ~3–4 hours.

### V.2 Emergent Bianchi / EIH lift from `S_SA(τ)` to a 4D action for `g_M`
- **What**: Attempt the §6.3 requirement (i): derive a 4D gravitational action for the emergent metric `g_M` from the `a₂`-channel of `S_SA(τ)`, and check whether its variation yields a generally-covariant tensor obeying an emergent Bianchi identity `∇_μ G_eff^{μν} = 0`. If yes, the geodesic motion of emergent matter follows (emergent EIH), which *is* the derived `a(t)` skeleton. This is the unification target of §III.2.
- **Inputs**: `a_2_FW_zeta = 2776.165389`; the existing internal-`K` EIH result (Bianchi satisfied by modulus EOM, S44); the Chamseddine–Connes dictionary `1/(16πG_N) = f₂Λ²a₂/(48π²)` with `f₂ ≈ 92` (§8.3); the `M_KK = 7.4287×10¹⁶ GeV` pin.
- **Gate**: feeds C1 (τ↔t map), C2 (`K_pivot`, BROKEN-WITH-LIVE-PATHWAY), T6 (Friedmann–BCS, BROKEN). New gate `EMERGENT-EIH-LIFT`: PASS if a generally-covariant emergent `G_eff^{μν}` with `∇_μ G_eff^{μν} = 0` is exhibited (closes frontiers #1 AND #8 jointly); FAIL/INFO with the specific obstruction identified.
- **Effort**: multi-session, exploratory (this is the framework's load-bearing open problem; the carry-forward is to *scope* the obstruction precisely, not to expect closure in one session). Initial scoping: 1 agent session.

### V.3 One-loop robustness of the no-well result
- **What**: Verify that the §1.3a tree-level boundary-domination of `e^{−S(τ)}` survives the one-loop correction `Γ_1loop = ½ Tr ln(D_K²/Λ²)` — i.e. confirm `Γ_1loop(τ)` introduces no interior stationary point in `Γ[τ] = S[D_K(τ)] + Γ_1loop`. State the regime of validity of the monotone-ramp picture explicitly.
- **Inputs**: the spectrum `{λ_k(τ)}` at `L_max=10` (155,984 eigenvalues); the E7 monotonicity theorem (tree level); the one-loop trace-log already identified as a threshold correction (S62).
- **Gate**: refines E7 / the §1.3a transit-physics claim. New gate `NO-WELL-ONE-LOOP`: PASS if `dΓ/dτ` retains a fixed sign (no interior extremum) over `τ ∈ [0, τ_now]`; INFO if a feature appears but is parametrically negligible; FAIL (consequential) if one loop creates a genuine well.
- **Effort**: 1 agent session (trace-log derivative on the existing spectrum cache). ~2–3 hours.

### V.4 Constants-hygiene: PROVENANCE for `M_KK` and `w0_FW`
- **What**: Add PROVENANCE entries to the knowledge MCP for `M_KK` and `w0_FW` (both confirmed by me to carry values but lack provenance: `get_constant("w0_FW")` returns `−0.918` with "_No PROVENANCE entry_"). Per the verification ledger's own hygiene flag.
- **Inputs**: `w0_FW = −0.918` (S58 Volovik partition, per the document); `M_KK = 7.4287×10¹⁶ GeV` (S42 Sakharov/zeta route); `update_constant(...)` with session + source + gate.
- **Gate**: no physics gate; constants-hygiene (does not block any result). Closes the verification-ledger flag.
- **Effort**: <1 hour, orchestrator-direct (not a physics dispatch).

> *Disciplinary note (mine):* I do not own probability estimates (Sagan's domain), so none of the above carries a likelihood claim. Each is framed as a constraint test: what region of solution space it closes or what missing theorem it scopes.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `S[D_K(τ),f,Λ]` is a *principle theory* (derives its own stage) | GEOMETRIC | Endorsed; recommend naming the methodology (§II.1) | Short free-parameter ledger is by construction; open inputs are *permitted*, not defects |
| 2 | No interior stationary point; monotone ramp; `e^{−S}` boundary-dominated | GEOMETRIC | E7 PROVEN (W7/S37, verified); §1.3a reading correct | Eliminates all slow-roll/well cosmogenesis *without computing a trajectory* (tree level — see CF V.3) |
| 3 | Layer independence `W ∝ R_K'(τ)³`, degenerate only at genesis | GEOMETRIC | CERTIFIED (S75 W2-E); ledger residual 0 (verified) | Licenses "vacuum/gravity/matter distinct" as an invariant, not a coordinate artifact |
| 4 | CC *term* = `a₀` moment (geometrically natural, not inserted) | GEOMETRIC | Location PERMANENT; magnitude OPEN (SDW gate) | Λ correctly *located*; the 114-OOM problem is a relaxation-dynamics gap, not an origin gap (§II.4) |
| 5 | §6.3 missing `a(t)` = §9 #8 missing emergent EP/Lorentz | — (meta-structural) | Both OPEN; document under-connects them | **One gap, not two**: generally-covariant emergent `g_M` action ⇒ {`a(t)`, EP, emergent EIH}; reduces frontier dimensionality (§III.2) |
| 6 | C1-postulate (τ=cosmic time) vs E7-derived (monotone clock) boundary | — | Mostly clean; one §9-table blur flagged | Prevent over-reading "derived monotone clock" as "derived cosmic time" (§III.4) |
| 7 | `f₂ ≈ 92` dictionary closure; NOT cited as gravity prediction | GEOMETRIC | Correctly handled (my Round-2 patch re-verified) | Consistency check that `a₂` carries `G_N`; circular-match caveat honored (§IV.4) |
| 8 | Framework is EPR-incomplete, and admits it cleanly | — (epistemic) | Strength, framed as constraint | Incompleteness is *localized* to named gates; each is a specific missing theorem (§IV.1) |

---

### Closing statement (physical interpretation)

The document achieves something I recognize from the inside: it takes a sprawling apparatus and shows that it descends from a *single constraint*, the way Lorentz invariance descends from two postulates. Its deepest virtue is that it knows the difference between *locating* a thing in the structure (the cosmological term is the `a₀` moment — permanent) and *deriving its dynamics* (the relaxation that fixes its magnitude — open), and it never confuses the two. My one substantive structural contribution is to point out that the two open items my field cares about most — the missing effective Friedmann map and the un-derived equivalence principle — are not two problems but one, with a precise name: **a generally-covariant emergent action for the metric `g_M` that is itself the second spectral moment of `D_K`.** Closing that one object would simultaneously deliver the scale factor, the equivalence principle, and the emergent Einstein–Infeld–Hoffmann theorem. That the framework already holds EIH on the *internal* geometry, and owes only its lift to the *emergent* metric, is the most encouraging thing in the document — and I mean "encouraging" as a structural statement about where the surviving solution space is narrowest, not as a probability.

Everything should be made as simple as possible, but not simpler. This document is, at last, simple — one operator, one functional — and it is honest about exactly where the simplicity has not yet been earned.
