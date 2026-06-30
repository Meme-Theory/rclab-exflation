# Session 100a Synthesis: Connes-Distance Machinery — Formalization and Scope of the W2-4 Structural Results

**Date**: 2026-06-07
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/session-100a/session-100a-w2-workingpaper.md` (§W2-4 construction block (0) + items (1)(2); §W2-2/§W2-3 context; Wave-2 synthesis + constraint map)
- `computations/session-100a/s100a_gate_verdicts.txt` (S100a-CONNES-DISTANCE-LADDER canonical line + companion rows, lines 70–75; lineage + KO rows at lines 73–74)
- `sessions/permanent-results-registry.md` (§VII.BL STAGE-3-PERMANENT, lines 21034–21111; index row line 148; Corner-III table row line 13029)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` + `s99-generation-blindness-theorem.md` (S99 order-one-silence and four-lens results, cited as prior-session structural facts)

**Dispatch class**: review/synthesis. No computation executed; no verdict lines emitted. All gate verdicts cited are authoritative as recorded; nothing herein re-adjudicates them. The NEW content of this document is the **formal status, proofs, and scope** of three results the W2-4 gate reported but did not formalize — this text is Stage-0 candidate material (see AUTHORSHIP NOTE, §IV.4).

---

## I. Session Outcome

The three claimed-but-unformalized structural results of `S100a-CONNES-DISTANCE-LADDER` (INFO, audit `5e24db72e3e5121b445477e2433a3c50084a4c5951111297c439a2da9b63491a`) are here given their precise mathematical status: **(a)** the commutative channel-algebra cure of the S87/S88 CLASS-γ regulator divergence is a **THEOREM** (finiteness + *exact* regulator-independence for ANY connected commutative channel restriction of ANY finite spectral triple), not an empirical property of this triple — proof in §II.1; **(b)** the greybody star closed form d(v,g) = λ_g²(τ_fold) = 1/t_g is an instance of an exact **star-metric lemma** (proved in §II.2, with its counterexample boundary: non-star topology, gapless channels, and non-scalar channel couplings); **(c)** the first-order residual 2.0450 (REPORTED) disqualifies *only* axiom-complete-spectral-triple and operator-side claims, and disqualifies **nothing** the distance observable needs — the Connes metric is an (A, H, D)-level functional, and [J, D_F] = 0 plus all KO-dim-6 signs hold at machine zero. The resolution of generations lives in the algebra-DEPENDENT **state-pair metric**, NOT in the operator module — §VII.BL stands untouched; any future registry landing is **STATE-PROJ** by mandatory naming hygiene (§IV.2), and a concrete S101 landing recommendation with Stage-2 reviewer exclusions is given in §IV.3–IV.4.

---

## II. Key Results

### II.1 — Deliverable (a): the Commutative-Channel Cure is a THEOREM, not empirical

**Result**: **Theorem A (Commutative-Channel Finiteness and Exact Regulator-Freeness)** — PROVEN below from the Lipschitz-ball structure; classification **GEOMETRIC**. The S100a R-sweep flatness (max dev 1.79e-9 over 3 decades) is the numerical echo of an *exactly* R-independent quantity, with the solver tolerance (1e-8) as the only scale present.

**Setting.** Let H be a finite-dimensional complex Hilbert space, D = D† ∈ B(H), and let X = {1, …, N} index an orthogonal channel decomposition H = ⊕_{x∈X} H_x with projections P_x. Let the **channel algebra** be the self-adjoint part of C(X) ≅ ℂ^N acting diagonally,

    A_chan = { a = Σ_x a_x P_x : a_x ∈ ℝ }  ≅  ℝ^N,                          (1)

with pure channel states ε_x(a) = a_x. Define the **coupling graph** G(D) on vertex set X with an edge {x, y} (x ≠ y) iff P_x D P_y ≠ 0. The Connes distance and its Frobenius-regulated variant are

    d(ε_x, ε_y)   = sup { |a_x − a_y| : a ∈ A_chan, ‖[D, a]‖_op ≤ 1 },        (2)
    d_R(ε_x, ε_y) = sup { |a_x − a_y| : a ∈ A_chan, ‖[D, a]‖_op ≤ 1, ‖a‖_F ≤ R }. (3)

In the S100a gate: X = {v=(0,0); (1,0); (1,1); (3,0)}, A_chan = self-adjoint ℂ⁴ (the WP §W2-4 block (0) construction), H = ℂ¹⁶, and the constant direction is gauge-fixed in the SDP.

**Theorem A.** Let G(D) be connected. Then:
1. *(Finiteness)* d(ε_x, ε_y) < ∞ for every pair x, y ∈ X, with the supremum attained.
2. *(Exact regulator-independence)* There exists a finite activation threshold ρ* (the Frobenius norm of a gauge-fixed optimizer) such that d_R = d **exactly** for all R ≥ ρ*. The map R ↦ d_R is nondecreasing and constant on [ρ*, ∞); the R-flatness has slope identically zero, not asymptotically zero.
3. *(Converse / boundary)* If x and y lie in distinct components of G(D), then d(ε_x, ε_y) = ∞ and d_R grows **linearly** in R — the CLASS-γ regulator-divergence signature reproduced on the commutative side.
4. *(Generality)* Clauses 1–3 hold for the commutative channel restriction of ANY finite spectral triple; nothing in the proof references the SU(3) cache, τ_fold, or the star topology.

**Proof.**

*Step 1 (commutator structure).* For a ∈ A_chan,

    [D, a] = Σ_{x≠y} (a_y − a_x) P_x D P_y,                                   (4)

since P_x [D, a] P_y = P_x D P_y a_y − a_x P_x D P_y = (a_y − a_x) P_x D P_y and the diagonal blocks cancel. Hence the Lipschitz seminorm L(a) := ‖[D, a]‖_op depends only on the edge differences a_y − a_x over G(D).

*Step 2 (seminorm kernel).* By (4), L(a) = 0 ⟺ a_x = a_y across every edge ⟺ a is constant on each connected component. For G(D) connected: ker L = ℝ·1 — the kernel is **state-blind** (ε_x(1) = ε_y(1) ∀x, y).

*Step 3 (finiteness).* On the quotient V := A_chan / ℝ·1 (dimension N − 1 < ∞), L descends to a genuine norm. The unit ball B_L = {[a] ∈ V : L(a) ≤ 1} is closed, bounded (norm-equivalence on a finite-dimensional space), hence compact. The objective f_{xy}([a]) = a_x − a_y is well-defined on V (constants cancel) and linear, hence attains a finite maximum on B_L. This maximum is d(ε_x, ε_y). ∎(1)

*Step 4 (exact regulator-independence).* Fix a gauge representative a* of an optimizer (traceless, or a*_v = 0 as in the gate's SDP), and set ρ* := ‖a*‖_F < ∞. Substitution chain for the direction claim:

    Step 4.1: feasible set of (3) at R′ ≥ R contains that at R     [definition (3)]
    Step 4.2: sup over a superset is ≥ sup over the subset          ⇒ d_R nondecreasing in R
    Step 4.3: for R ≥ ρ*, a* is feasible for (3)                    ⇒ d_R ≥ f(a*) = d
    Step 4.4: feasible set of (3) ⊆ feasible set of (2)             ⇒ d_R ≤ d
    Conclusion: d_R = d exactly for all R ≥ ρ*.                      ∎(2)

*Step 5 (converse).* If x, y are in distinct components, a_λ := λ·1_{C(x)} (indicator of x's component, scaled) has L(a_λ) = 0 and separates the states: f_{xy}(a_λ) = λ. Unregulated: λ → ∞ gives d = ∞. Regulated: λ ≤ R/‖1_{C(x)}‖_F gives d_R ≥ R/‖1_{C(x)}‖_F — linear growth in R. ∎(3)

*Step 6 (generality).* Steps 1–5 use only: finite dimensionality, D = D†, diagonal action of a commutative channel algebra, and connectivity. ∎(4) □

**Why the full-M_n(ℂ) route diverges (the structural contrast).** For A = M_n(ℂ)_sa the seminorm kernel is the self-adjoint commutant {D}′_sa ⊇ {f(D) : f real Borel}, of dimension ≥ #spec(D) ≥ 2 — and these kernel elements DO separate states supported on distinct D-spectral subspaces (generation states are exactly of this type). Scaling a separating kernel element reproduces Step 5 verbatim: d = ∞ unregulated, d_R ∝ R regulated. This is the S87/S88 CLASS-γ behavior recorded in the lineage companion row (line 73: "full M_n(C) regulator-divergent … any f(D²) commutes with D"; machinery value `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY = 0.9800418463588636`, INFO CLASS-γ). The dichotomy is now sharp and two-sided:

> **Regulator divergence ⟺ the Lipschitz-seminorm kernel separates the state pair.** The full matrix algebra always fails this for generation states (kernel = {D}′, state-separating); the connected commutative channel restriction always passes it (kernel = ℝ·1, state-blind).

**Scope precision (what remains empirical at this triple).** Two items only: (i) the *location* of the activation threshold ρ* — the observed 3-decade flatness from R = 10·ω_max upward shows ρ* ≤ 10·ω_max here, a triple-specific number Theorem A does not fix; (ii) the distance VALUES themselves (the cache floors). Both clauses of the cure — finiteness and exact R-flatness — are theorem-level and portable. Note also the cure is not "the same M_n(ℂ) observable, now finite": restricting the test algebra defines the canonical metric **of the channel state space** (the IKM finite-point setting, as the WP names it); the S88 full-algebra number 0.98004… is a different, regulator-pinned observable and remains INFO CLASS-γ.

**STRUCTURAL VERDICT on (a): THEOREM** (Theorem A clauses 1–4; hypotheses: finite triple, diagonal commutative channel algebra, connected coupling graph, constants gauge-quotiented). At the S100a triple every hypothesis is verified: the star graph is connected (t_g = 1/ω_g > 0 for all three channels since all floors ω_g > 0 at τ_fold), and the SDP gauge-fixed the constant direction. The R-sweep dev 1.79e-9 and SDP-vs-closed-form dev 2.5e-9 sit at the solver floor (tol 1e-8), consistent with an exactly-flat quantity.

---

### II.2 — Deliverable (b): the Greybody Star-Metric Lemma (with counterexample boundary)

**Result**: **Lemma B** — the closed form d(v, g) = 1/t_g is EXACT on any finite star, in operator-norm generality; the leaf–leaf Pythagorean form is exact for scalar couplings; both are invariant under isospectral J-doubling. Classification **GEOMETRIC**. The gate's SDP verification (2.5e-9) and doubling-invariance (1.8e-9) are numerical confirmations of exact statements.

**Setting.** Star graph: center channel v, leaves g = 1, …, n. D couples center-to-leaf only: writing S_g := P_v D P_g : H_g → H_v (no leaf–leaf couplings, P_g D P_h = 0 for g ≠ h leaves), and a ∈ A_chan with x_g := a_g − a_v. From (4),

    [D, a] = Σ_g x_g ( S_g  −  S_g† )  (block off-diagonal, v ↔ leaves),       (5)

and a two-line block computation gives the exact norm identity

    ‖[D, a]‖_op² = ‖ Σ_g x_g² S_g S_g† ‖_op   (operator on H_v).               (6)

[Derivation of (6): with W := Σ_g x_g S_g ι_g : ⊕_g H_g → H_v, the nonzero blocks of [D,a]†[D,a] are WW† on H_v and W†W on ⊕H_g; ‖WW†‖ = ‖W†W‖ = ‖W‖².]

**Lemma B.**
1. *(Center-to-leaf, EXACT, operator-norm generality)* d(ε_v, ε_g) = 1/‖S_g‖_op. For scalar couplings ‖S_g‖ = t_g this is d(v, g) = 1/t_g; with the greybody pin t_g = 1/ω_g, ω_g = λ_g²(τ_fold) (channel D²-floor from the L=12 cache):

        d(ε_v, ε_g) = ω_g = λ_g²(τ_fold)   EXACTLY.                            (7)

2. *(Leaf-to-leaf, Pythagorean)* d(ε_g, ε_h) ≥ ( t_g^{−2} + t_h^{−2} )^{1/2}, with **equality** iff S_g S_g† and S_h S_h† attain their operator norms on a common unit vector of H_v — in particular, equality whenever the couplings are channel-scalars (the S100a case: per chirality/particle-antiparticle copy each channel slot is one-dimensional). The triangle inequality gives the two-sided pinch

        ( t_g^{−2} + t_h^{−2} )^{1/2}  ≤  d(g, h)  ≤  1/t_g + 1/t_h,            (8)

   strictly below the path sum — the finite-triple metric is **not** a geodesic/path metric.
3. *(Doubling / direct-sum invariance)* If D′ = ⊕_α D_α on H′ = ⊕_α H_α is a direct sum of stars with identical coupling norms per channel (isospectral copies), and A_chan acts channel-diagonally and copy-blindly, then d′ = d exactly, since ‖[D′, a]‖ = max_α ‖[D_α, a]‖ produces the same feasible set. The BDI J-doubling (antiparticle star on the conjugate sectors (0,1)/(1,1)/(0,3)) satisfies the hypothesis to the conjugate-floor-equality precision 1.2e-15; the observed doubling dev 1.8e-9 is solver-floor-dominated and consistent, since d depends on the couplings with local Lipschitz exponent 1 (|∂(1/t)/∂t| = 1/t² ⇒ relative dev in d ≈ relative dev in t).

**Proof of (1).** *Lower bound*: take x_g = 1/‖S_g‖, all other x_h = 0; by (6), ‖[D,a]‖ = |x_g|·‖S_g‖ = 1, feasible, objective = 1/‖S_g‖. *Upper bound*: for ANY feasible a, positive-semidefinite (Weyl) monotonicity in (6) gives 1 ≥ ‖Σ_h x_h² S_h S_h†‖ ≥ x_g² ‖S_g S_g†‖ = x_g² ‖S_g‖², so |x_g| ≤ 1/‖S_g‖. Both bounds coincide. ∎

**Proof of (2).** Setting x_k = 0 for k ∉ {g, h} is WLOG (removing PSD terms from (6) only enlarges feasibility at fixed (x_g, x_h), and the objective ignores the other coordinates). Subadditivity λ_max(P + Q) ≤ λ_max(P) + λ_max(Q) shows the true feasible set CONTAINS the ellipse {x_g² t_g² + x_h² t_h² ≤ 1}, whose maximum of x_g − x_h is the Pythagorean value (max of c·x on {xᵀQx ≤ 1} is (cᵀQ⁻¹c)^{1/2}) — hence "≥". With a shared norm-attaining vector ξ, λ_max(x_g²Q_g + x_h²Q_h) ≥ ⟨ξ, ·ξ⟩ = x_g²t_g² + x_h²t_h² shows the feasible set is CONTAINED in the ellipse — hence equality. The upper pinch in (8) is the triangle inequality for (2), valid for any state triple. ∎

**Proof of (3).** [D′, a] = ⊕_α [D_α, a]; the operator norm of a direct sum is the max over summands; identical per-copy norms give an identical feasible set, hence identical suprema. ∎

**Numerical confirmation against the gate (consistency check, not new evidence).** Closed form (7) against the cache floors λ_g(τ_fold) = (0.83589351, 0.87297503, 1.24826413): d = (0.698718, 0.762085, 1.558163) λ²-units — the verdict line's d-vector verbatim; SDP dev 2.5e-9. Lemma B(2) reproduces the gate's reported pairwise diagnostic: d(e, μ) = (1.558163² + 0.762085²)^{1/2} = 1.734545, d(μ, τ) = (0.762085² + 0.698718²)^{1/2} = 1.033915, ratio = 1.6776 = the verdict's `W_pairwise_diag=1.6776`. Lemma B(1) makes the gate's two structural identities corollaries: (i) *undeformed-Casimir corollary* — at bi-invariant scaling ω_g ∝ C₂(g) on the triality tower C₂ = (4/3, 3, 6), the vacuum-referenced widening is W = (6−3)/(3−4/3) = **9/5 exactly**; (ii) *fold-deformation factor* — at τ_fold the measured W_Connes = Δ₁/Δ₂ = 0.796078/0.063367 = 12.562884 = (9/5) × 6.979380, the same chord-slope factor as §W2-3's floor decomposition (bit-identical agreement between the two gates). The lemma thereby converts the widening question into pure floor spectroscopy of D_K — the metric adds no freedom of its own.

**Counterexample boundary (where the closed forms stop).**
- **Non-star topology**: any leaf–leaf coupling (P_g D P_h ≠ 0) breaks identity (6); both the v-to-g closed form and the Pythagorean form lose their proofs. No closed form is claimed beyond the star — the SDP of (2) remains the evaluator (finite and regulator-free by Theorem A as long as the graph stays connected).
- **Gapless channel** (ω_g → 0, i.e., t_g → ∞): d(v, g) → 0 — metric state-merging. The regime of (7) is all floors strictly positive, which holds at τ_fold (min floor 0.698718 λ²-units).
- **Non-scalar (multiplicity-resolving) channel couplings**: clause (1) survives verbatim with 1/‖S_g‖_op; clause (2) degrades to the lower bound in (8), saturated only under top-singular-subspace alignment. This is exactly the ε_LX-relevant boundary: a generation-texture WITHIN a channel block (the §VII.BL complement direction) preserves the center-to-leaf ladder but deforms the leaf–leaf geometry — the first place a structured ε_LX would show up metrically.

**Dimensional consistency.** The greybody star is a metric generator, not the physical D_K: [t_g] = [S_g] = M_KK⁻² (inverse cache-floor units), so by (7) [d] = M_KK² — distances in λ²-units, exactly as the verdict line states ("lam2-units"). The Connes formula (2) is unit-covariant (d scales as 1/[D]); the mass-map exponent d/ℓ is dimensionless since ℓ = 0.120408 carries the same cache-units² (gate item (4)); the overall mass scale is the non-physical centering constant of the OLS. The κ = 1 cache-unit choice is absorbed into ℓ and is not a parameter (WP block (0)).

---

### II.3 — Deliverable (c): First-Order Scope Statement

**Result**: **Scope Statement C** — the REPORTED first-order residual max‖[[D_F, a], b°]‖ = 2.0450 keeps §VII.BL standing and disqualifies precisely the operator-side claims; it disqualifies nothing the state-pair metric needs. Classification **GEOMETRIC**.

**The facts (authoritative, lines 73–74 + WP §W2-4 item (1)).** On the J-doubled construction: |J² − 1| = 0.0; ‖[J, D_F]‖ = 1.6e-15 (forced by the BDI conjugate-floor equality 1.2e-15); ‖{J, γ}‖ = 0.0 (ε″ = −1); ‖{γ, D_F}‖ = 0.0 — the full KO-dimension-6 sign triple (ε, ε′, ε″) = (+1, +1, −1) verified at machine zero. The order-one residual 2.0450 is REPORTED, not asserted zero.

**What the violation does NOT disqualify:**
1. **The distance observable itself.** The Connes distance (2) is a functional of (A, H, D) alone: it requires D = D† and bounded commutators (automatic in finite dimension) — no J, no γ, no order-one, no orientability, no Poincaré duality enter its definition, its finiteness (Theorem A), or the closed forms (Lemma B). Every number in the d-ladder is order-one-blind by construction.
2. **The reality verification.** [J, D_F] = 0 holds at 1.6e-15: the construction sits in the reality-COMPATIBLE class that §VII.BL clause (e) requires of any ε_LX-type object ("reality-compatible, order-one-constrained, outside every A_K-module"). Reality and order-one are independent axioms; passing one while reporting the other is consistent, and is the §VII.BL-predicted signature.
3. **The KO-dim-6 / BDI classification** of the doubled triple's sign structure — verified independently at machine zero, untouched by order-one.
4. **A future STATE-PROJ registry landing** of Theorem A + Lemma B + the generation-resolution existence result (strict ladder, rel spread 0.5516; regulator-invariant 1.79e-9). None of these clauses cites order-one anywhere in hypothesis or proof.
5. **§VII.BL itself.** The residual is the obstruction theorem's *expected signature*, not a counterexample: a generation-RESOLVING coupling set on the multiplicity bundle lies outside every A_K-built module (inner, twisted-inner Ω¹_σ, opposite-action) — the star's couplings are external data (cache floors), not elements of the Hochschild-image Ω¹_{D_K}(A_K). The constraint-map row records this correctly: *resolution lives in the state-pair metric, NOT the operator; the operator side stays §VII.BL-obstructed.*

**What the violation DOES disqualify:**
1. Any claim that (A_mult or A_K, H_F, D_F; J, γ) is an **axiom-complete finite real spectral triple** (7 NCG axioms). It is not: order-one fails at 2.0450 on the gate's test set, in the same wall-class as the framework's standing 4.000 on the (ℍ, ℍ) pair of the bare product geometry — a *separate instance* of the same class, NOT the same number; neither supersedes the other.
2. Any **OP-PROJ-side landing** claiming generation resolution by an operator-module or spectrum-only functional — that would contradict §VII.BL (STAGE-3-PERMANENT) and is excluded.
3. Treating D_F as an **inner fluctuation** D + A + JAJ⁻¹ of any A_K-triple, or invoking on D_F any spectral-action conclusion whose derivation USES order-one (e.g., the first-order-based splitting of inner fluctuations into gauge + Higgs sectors) without independent re-derivation.
4. Reading the magnitude 2.0450 as a calibrated physical scale — it is test-set- and normalization-convention-dependent; REPORTED means exactly that.

**Precision-scoping note (module-membership vs order-one violation — flagged, not a conflict).** The companion row's phrase "generation-resolving D_F lies outside every A_K-bimodule" is accurate as **module-membership** (§VII.BL E2: nonzero component in the multiplicity-acting summand ⊕ 1_{V_{(p,q)}} ⊗ M_{m(p,q)}(ℂ), orthogonal to the Hochschild 1-cochain image). It should NOT be strengthened to "generation resolution forces an order-one violation": the S99 order-one-silence result (Sage-exact, recorded in agent memory; conditional on an order-one-admissible internal block) shows arbitrary generation textures riding on admissible internal blocks satisfy [[D_F, a], Jb*J⁻¹] = 0 identically, because A_K acts as the identity on the multiplicity index. The 2.0450 here is sourced by THIS star's inter-sector orbital couplings (vacuum reference channel ↔ Peter-Weyl generation channels), whose internal structure was chosen for the metric, not optimized for order-one admissibility. Both directions are now scoped: the residual neither evidences a forced violation nor any evasion of §VII.BL.

---

## III. Gate Verdicts

(From the source documents; authoritative, not re-adjudicated.)

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S100a-CONNES-DISTANCE-LADDER | INFO (sign=PASS, magnitude=INFO, regime=VALID) | W_Connes = 12.562884 ∉ [1.80, 1.89]; spread 7.1378 e-folds ∈ [6,10]; d = (0.698718, 0.762085, 1.558163) λ²-units; R-sweep dev 1.79e-9; SDP dev 2.5e-9; first-order residual 2.0450 REPORTED |
| S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY (lineage, companion row line 73) | INFO (CLASS-γ) | 0.9800418463588636 — full M_n(ℂ), regulator-DIVERGENT |
| S100a-CASIMIR-WIDENING (§W2-3 context) | FAIL | W = −4.663502 outside all three bands; slope ratio 6.979380 |
| S100a-YUKAWA-OVERLAP-OFFDIAG (§W2-2 context) | INFO | spread 1.1031 e-folds; e-channel = (3,0); |w| = 1/√6 exact |
| S100a-DUAL-Z3-PHI-POINTS (§W2-1 context) | PASS | c(φ) = {1/9, 1/3, 1/3} exact; lepton-only lever |

---

## IV. Structural Implications

### IV.1 Constraint-map consequences

- **The S87/S88 regulator wall is now a two-sided dichotomy theorem** (§II.1): CLASS-γ divergence ⟺ seminorm-kernel separation of the state pair. The full-M_n(ℂ) channel is closed *structurally* (kernel always state-separating for generation states); the connected commutative channel restriction is open *structurally* (kernel always state-blind). The cure is portable to any finite triple in the framework — nothing SU(3)-specific is consumed. (The registry's Corner-III row, line 13029, records the full-M_n(ℂ) route's divergence and a distinct A_F STRICT residual 1.054e-01 from S87 S-2 — a different observable than the 0.98004 machinery value; the two must not be conflated in future citations.)
- **The widening question is now pure floor spectroscopy** (Lemma B): the metric route adds no shape freedom — W_Connes = (9/5) × (chord-slope factor), exactly. The floor-graded widening corridor stays CLOSED on both routes (W2-3/W2-4, bit-identical decomposition); the surviving corridor is whole-block heat-trace couplings, already queued as `CF-S101-W2-BLOCKTRACE-WIDENING` (W2 WP). Substrate reading: the fabric's state-pair metric inherits the Jensen fold's van-Hove floor compression verbatim; the Casimir 9/5 shape survives only at whole-block spectral content.
- **Generation resolution is located**: in the algebra-DEPENDENT state-pair functional (Connes metric on the channel state space), with the operator side §VII.BL-obstructed — the framework's fermion-mass reframe (S99) gains its first regulator-invariant, theorem-backed metric realization. The electron IS the channel the fabric transmits least (most greybody-suppressed, most distant: e = (3,0), two-route consistent with the overlap functional).
- **m_tau_PDG = 1.77686 GeV** (promoted in-gate with provenance) resolves the m_tau name-collision for all future PDG charged-lepton anchors; the S42 modulus mass `m_tau = 2.062` (M_KK units) is untouched.

### IV.2 STATE-PROJ declaration (mandatory naming hygiene)

Per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (MANDATORY at K=3): the theorem complex formalized here admits both projection-side readings — the operator-side reading exists and is **negative** (§VII.BL: no generation-resolving D_F inside any A_K-module; Corner I), while the state-side reading is **positive** (the Connes distance ladder resolves generations; Connes distances are the rule's own canonical example of the state-side family). Therefore:

> **DECLARATION**: any registry landing of the W2-4 structural results MUST carry the **`.STATE-PROJ`** suffix; a bare §VII.{slot} identifier is FORBIDDEN. The entry declares **Corner/Cell IV** (algebra-DEPENDENT state-pair functional) per `permanent-results-registry.md §VII.U.2`. Cross-corner co-primary with §VII.BL (Corner I) is **FORBIDDEN** per the algebra-axis orthogonality K-counter (MANDATORY at K=3); the correct anchor structure is **STRUCTURAL-ORTHOGONAL-COMPANION** to §VII.BL. This is the wave's constraint-map row made registry-grade: *resolution lives in the state-pair metric, NOT the operator — the operator side stays §VII.BL-obstructed while the algebra-DEPENDENT state-pair functional resolves generations.*

Defensive compliance item: although "greybody" is not in the Class-(h) state-history pattern set, the landing text SHOULD carry a parse-tree expansion block (greybody label → t_g = 1/ω_g → ω_g = λ_g²(τ_fold) → per-sector D_K² cache floors at L_max=12 — a closed-form reduction to substrate-algebra data), defusing any `MISSING-PARSE-TREE-EXPANSION` advisory at plan-freeze.

### IV.3 Registry-eligibility recommendation (feeding a possible S101 landing)

**RECOMMENDED — eligible NOW as STAGE-1-CANDIDATE, structural clauses only:**

- **Slot**: next-free letter, ≥ §VII.BM at this writing (grep 2026-06-07: no §VII.BM exists; the runtime all-header-level scan per `epistemic-discipline.md §"Registry-Write Hygiene"` remains mandatory at landing). Suffix **`.STATE-PROJ`** per §IV.2.
- **Entry class**: intra-pillar structural theorem on the spectral-triple axis (precedents §VII.BJ, §VII.BK: NOT a cross-pillar bridge ⇒ 5-anatomy N/A — and it must NOT be dressed as one: there is no HKR/K-theory/Connes-Karoubi bridge map to a laboratory-IN observable; the ℓ-calibration is a one-parameter PDG-anchored OLS (R² = 0.9228), NOT a zero-free-parameter map, and declaring it a bridge would trip the Level-2 binding/non-binding HARD-HALT).
- **Clauses** (Stage-0 candidate content, all herein): (i) Theorem A (commutative-channel finiteness + exact regulator-freeness, with the two-sided CLASS-γ dichotomy); (ii) Lemma B (star-metric closed forms (7)–(8) + doubling invariance + boundary); (iii) generation-resolution existence on the state-pair metric (strict ladder, rel spread 0.5516; regulator-invariant 1.79e-9/3 decades) with Scope Statement C as the first-order scope rider; (iv) the undeformed-Casimir corollary W → 9/5 and fold factor 6.979380 as **annotations at INFO scope, NON-LOAD-BEARING** (per the Level-3 annotation discipline analog — the shape question is open and queued).
- **Anchors**: PRIMARY = `S100a-CONNES-DISTANCE-LADDER` (audit `5e24db72e3e5121b445477e2433a3c50084a4c5951111297c439a2da9b63491a`; npz `computations/session-100a/s100a_connes_distance_ladder.npz`); Stage-0 text = this synthesis; STRUCTURAL-ORTHOGONAL-COMPANION = §VII.BL (NOT co-primary, §IV.2); supporting cross-check (non-clause) = Item-6 e-sector match (e = (3,0) both routes). Lineage citation = S88 machinery value with its INFO CLASS-γ tag intact.
- **EXCLUDED from the entry** (would be over-claims): any widening/shape clause (floor corridor CLOSED; the block-trace corridor must run first — `CF-S101-W2-BLOCKTRACE-WIDENING`, amended by the S2-1 counting-convention workshop before S101 plan-freeze per the WP addendum); any 7-axiom real-spectral-triple claim (Scope C); any OP-PROJ generation-resolution claim (§VII.BL); any "ε_LX derived from A_K" claim (would contradict §VII.BL — the star couplings are external cache data).
- **Writer routing**: §VII structural entry, NOT a §7 falsifier-surface row ⇒ mack-cosmic-bridge sole-writer does NOT apply (precedent: §VII.BL provenance note); the S101 wave's designated registry writer lands it via the single-shot AFTER pattern (`registry-landing.md §"Bridge-Landing Script Architecture"`), batched naturally with the already-queued `CF-W2-2` (W2-1 Z₃ landing) wave.
- **Pathway**: STAGE-1-CANDIDATE at landing → Stage-2 two-agent cross-axis verify (spec in §V.3, reviewer exclusions in §IV.4) → Stage-3 flip on PASS-AND.

### IV.4 AUTHORSHIP NOTE (binding for Stage-2)

This synthesis **is Stage-0 candidate text**. Its author, **connes-ncg-theorist, is thereby Stage-0 author of the candidate theorem complex and is EXCLUDED from any later Stage-2 cross-review** of the resulting registry entry, per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` (condition 2: original-authoring-agent exclusion with downstream-inheritance reach) — and doubly so, since connes-ncg-theorist was also the W2-4 gate's executing agent. This restates the S99 E1 lesson verbatim: at S99 W3-1 the original connes axis-A Stage-2 leg on §VII.BL was a Stage-2 audit-item-3 violation (Stage-0 co-author reviewing own theorem), caught at session-close and re-dispatched to van-den-dungen-bridge-theorist, with the compromised line `13998949…` retained on disk under Option-A supersession. **Suggested Stage-2 pairing** (subject to the dispatch-time `--check-reviewers --strict` static leg + downstream-inheritance grep): Axis-A (NCG-axiomatic): van-den-dungen-bridge-theorist OR lizzi-spectral-functional-theorist; Axis-B (substrate/state-pair): volovik-superfluid-universe-theorist OR landau-condensed-matter-theorist. Substrate-input-orthogonality is designable: Axis-A audits Theorem A/Lemma B from first principles (no npz); Axis-B audits the numerical clauses from the npz (single-loader).

### IV.5 Cross-source consistency flags

1. **Gate-name lineage wrinkle (naming-only)**: the machinery gate is cited as `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY` (verdict companion row) and as `…-IDENTITY-CONJECTURE` registered in `s87_gate_verdicts.txt` with producing script `s87_w1b_connes_distance_finite_spectrum_identity.py` (WP MCP-audit row) — an S88-named gate living in the S87 verdict file. Future consumers should resolve by producing script + value (0.9800418463588636), not session prefix. No substantive conflict.
2. **Order-one attribution precision** (§II.3 note): module-membership (§VII.BL) vs order-one-violation are distinct predicates; the WP/companion-row phrasing is correct under the module reading and should not be cited as "generation resolution forces order-one violation". Flagged as scoping, not conflict.
3. **R-sweep value**: 1.8e-9 (Focus/WP rounding) vs 1.79e-9 (companion row) — same number.
4. **Distinct full-algebra residuals**: 0.9800418463588636 (S88 machinery value) vs 1.054e-01 (A_F STRICT residual, S87 S-2, registry Corner-III row line 13029) are different observables on the divergent route; do not conflate (§IV.1).

---

## V. Carry-Forward Computations

(MATH follow-ups only, per the dispatch's carry-forward discipline; the registry-eligibility recommendation and naming-hygiene declarations are in-document, §IV.2–IV.4, ready for the S101 landing wave. `CF-S101-W2-BLOCKTRACE-WIDENING` already exists in the W2 WP and is NOT duplicated here; it remains the primary shape-corridor gate.)

**V.1. Block-coupling star-metric lemma verification (Lemma B clauses (1)–(2) at the boundary)**
- **What**: Construct star triples with non-scalar channel couplings S_g (operator blocks with non-aligned top singular subspaces) and verify: (i) d(v, g) = 1/‖S_g‖_op exact (SDP vs closed form); (ii) d(g, h) > (t_g⁻² + t_h⁻²)^{1/2} strictly for non-aligned blocks, with equality restored under engineered alignment — the saturation criterion of Lemma B(2). One synthetic family + one physical instance using L=12 cache floors as the scalar part plus a multiplicity-textured perturbation (the ε_LX-boundary probe of §II.2).
- **Inputs**: SDP machinery from `computations/session-100a/s100a_connes_distance_ladder.py` (cvxpy CLARABEL, gauge-fixing); `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7…`) for the physical instance; no new diagonalization.
- **Gate**: `S101-STAR-METRIC-BLOCK-LEMMA` — PASS iff closed-form/SDP rel dev ≤ 1e-7 on clause (i) across the family AND the clause-(ii) strictness witness shows d − Pythagorean ≥ 1e-3 (relative) for the non-aligned construction with equality (≤ 1e-7) under alignment; FAIL if any clause-(i) instance deviates (would falsify the operator-norm form of Lemma B(1)); INFO if solver convergence blocks a sub-case.
- **Effort**: ~0.5 agent-session (closed forms + ~30 small SDPs).

**V.2. Disconnected-graph CLASS-γ reproduction (Theorem A clause 3 boundary)**
- **What**: Sever one star edge (set t_g = 0) and run the Frobenius-regulated SDP over the same 3-decade R-sweep: verify d_R for the severed pair grows with fitted log-log slope d ln d_R/d ln R = 1 (linear divergence, the commutative CLASS-γ signature of Theorem A Step 5) while all connected pairs stay R-flat; report the activation threshold ρ* for the connected pairs (the one empirical residue identified in §II.1).
- **Inputs**: same SDP machinery and cache floors as V.1; R-sweep grid from `s100a_connes_distance_ladder.py` (R = 10/100/1000 × ω_max, extended one decade each way).
- **Gate**: `S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY` — PASS iff |slope − 1| ≤ 1e-3 on the severed pair AND connected-pair R-dev ≤ 1e-8 AND measured ρ* ≤ 10·ω_max (consistency with the S100a observed flatness window); FAIL on slope ≠ 1 (would falsify the linear-divergence form); INFO if the severed-pair SDP is unbounded-flagged before the largest R (acceptable degenerate confirmation, reported as such).
- **Effort**: ~0.3 agent-session.

**V.3. Stage-2 cross-axis verify of the S101 STATE-PROJ candidate (conditional on the §IV.3 landing)**
- **What**: Two-agent parallel cross-axis independent verification of the landed STAGE-1-CANDIDATE entry: Axis-A re-derives Theorem A + Lemma B from first principles reading ONLY the registry entry (no npz, no workshop/synthesis transcripts); Axis-B re-verifies the numerical clauses (d-ladder, R-sweep flatness, KO signs, first-order residual REPORTED status) from the npz alone; JOINT clause (generation-resolution-in-state-pair-metric-while-operator-side-obstructed) PASS-AND'd across both verdicts.
- **Inputs**: the landed registry entry text; `computations/session-100a/s100a_connes_distance_ladder.npz` (Axis-B only, satisfying substrate-input-orthogonality); reviewer exclusion set {connes-ncg-theorist} enforced via `_joint_theorem_independent_verify_audit.py --check-reviewers --strict` + downstream-inheritance grep (§IV.4).
- **Gate**: `S101-CONNES-STATEPROJ-STAGE2-VERIFY` — PASS iff both single-axis clause sets PASS and the JOINT clause PASSes in BOTH verdicts (logical AND) ⇒ Stage-3 flip at session-end synthesis; any clause FAIL holds the entry at STAGE-1 with the failing clause routed to remediation; any INFO documents Stage-2-INFO-deferred.
- **Effort**: 2 parallel agent-sessions (~1 each) + orchestrator aggregation.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Theorem A: commutative-channel restriction ⇒ Connes distance finite + EXACTLY regulator-free (connected graph; gauge-quotiented constants); converse: disconnection ⇒ linear-in-R CLASS-γ divergence | GEOMETRIC | PROVEN (this synthesis, Stage-0 text); numerics consistent (R-dev 1.79e-9 at solver floor) | The S87/S88 regulator wall becomes a two-sided dichotomy; the cure is portable to any finite triple — structural, not empirical-at-this-triple (empirical residue: only the threshold location ρ* and the distance values) |
| 2 | Lemma B: star metric d(v,g) = 1/‖S_g‖ EXACT (greybody: = λ_g²(τ_fold)); leaf-leaf Pythagorean exact for scalar couplings; doubling-invariant; boundary = non-star edges / gapless channels / non-scalar couplings | GEOMETRIC | PROVEN (this synthesis); SDP 2.5e-9, doubling 1.8e-9, W_pairwise 1.6776 reproduced | Widening = pure floor spectroscopy (W = (9/5)×6.979380 exact decomposition); metric adds no shape freedom; ε_LX-texture boundary identified at the leaf-leaf clause |
| 3 | Scope C: first-order residual 2.0450 REPORTED disqualifies 7-axiom and OP-PROJ claims ONLY; distance formula needs (A,H,D) alone; [J,D_F]=0 and KO-dim-6 signs at machine zero; §VII.BL stands | GEOMETRIC | SCOPED (this synthesis; gate values authoritative) | A STATE-PROJ landing is unblocked; operator-side claims remain §VII.BL-obstructed; module-membership ≠ forced order-one violation (S99 silence result) |
| 4 | STATE-PROJ declaration + Cell-IV corner + STRUCTURAL-ORTHOGONAL-COMPANION anchor structure vs §VII.BL | methodology (registry hygiene) | DECLARED in-document (§IV.2) | Bare-slot landing FORBIDDEN; cross-corner co-primary with §VII.BL FORBIDDEN |
| 5 | S101 registry-eligibility recommendation: land structural clauses (i)–(iii) + annotations as STAGE-1-CANDIDATE at ≥ §VII.BM.STATE-PROJ; exclude shape/7-axiom/OP-PROJ claims | methodology (registry routing) | RECOMMENDED (§IV.3); Stage-2 spec V.3 | Feeds the S101 landing wave; batched with CF-W2-2; shape corridor stays with CF-S101-W2-BLOCKTRACE-WIDENING |
| 6 | AUTHORSHIP: connes-ncg-theorist = Stage-0 author (this text) + W2-4 gate agent ⇒ EXCLUDED from Stage-2 review (S99 E1 lesson) | methodology (process) | BINDING (§IV.4) | Stage-2 reviewers drawn from {vdd, lizzi} × {volovik, landau} with strict static + inheritance checks |
