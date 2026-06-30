# Capstone Equation Review — einstein

**Date**: 2026-05-29
**Agent**: einstein-theorist (Einstein)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (THE capstone, S95-era; reviewed in full)
- `.claude/rules/phononic-framing.md` (framing law — binding)
- `.claude/agent-memory/einstein-theorist/MEMORY.md` (my own prior structural results)
- Cross-checked: knowledge MCP (`w0_FW`, `a_2_FW_zeta`), `canonical_constants.py` provenance

---

## I. Session Outcome

The capstone is **structurally sound on the principle-theoretic axis and exemplary in its honesty about what it does not derive**. Its central claim — that the universe is the spectral action `S[D_K(τ), f, Λ]` of one Dirac operator, with gravity = the `a₂` Seeley–DeWitt moment, the cosmological term = the `a₀` moment, and matter = the `a₄` moment — is a genuine *principle theory* in my 1919 sense: a single high-level constraint from which the field content is read off the algebra, not a constructive model of fields-in-a-box. The document correctly identifies its own deepest gap as the absence of a derived, generally-covariant emergent 4D action for `g_M` (§6.3), and correctly recognizes that this *one* gap simultaneously is the effective-Friedmann map, the emergent equivalence principle, and the emergent Einstein–Infeld–Hoffmann theorem (frontier #8).

The single most important correction I record: **the document's strongest emergent-GR PASS results (κ_EP = 1 exact, the Noether-ratio = ½ conservation closure) are correctly flagged generic-identity-cored in §9** — they are the Lichnerowicz–Weitzenböck `R/4` coefficient and the Brans–Dicke diffeomorphism Noether identity of *any* spin Dirac operator, carrying no substrate value-content. This is a model of disciplined self-skepticism and I endorse it without reservation; it is exactly the distinction between *necessary* (follows from structure alone) and *contingent* that I demand. The genuinely substrate-specific content (single-spectral-triple ⇒ band-independence; `φ(τ) = a₂` derived not posited; the sign `a₂′ > 0`) lives one layer above the PASS values, and the document says so.

What remains PRELIMINARY or over-stated is small and localized: a Lichnerowicz convention note that is internally inconsistent with my memory's stated bound (flagged §IV); the `Z_fold` normalization ambiguity in the `G_N` dictionary (the document itself tags it PRELIMINARY); and a residual tension between "the equation derives its own stage" (§0) and the fact that the *full* Einstein equation `G_{μν} = 8πG T_{μν}` is explicitly *not* delivered (§6.3) — which the document handles correctly but a careless reader will over-read.

---

## II. Key Results

### 1. The container-removal argument (§0–§1) is a correct principle-theoretic statement

**Result**: The Chamseddine–Connes spectral action removes the manifold-and-metric-by-fiat that every GUT presupposes; by Connes' reconstruction theorem the geometry IS the spectrum of `D`, and `a₂(τ)` *recovers* the metric rather than assuming it. Classification: **GEOMETRIC** (the claim is about the spectral triple, not its excitations).

This is the part of the document closest to how I actually think. A constructive theory (kinetic gas, the Standard Model Lagrangian) builds from hypothetical constituents inside a given stage; a principle theory (thermodynamics, relativity) is a constraint any valid configuration must satisfy. The capstone's §1.4 names this explicitly and correctly: `S[D_K(τ), f, Λ]` is a principle theory, so the short free-parameter ledger is *entitled*, not lucky. The categorically-stronger claim — "switch off `D_K` and there is no `a₂`, hence no metric, hence no space" (§0) — is the correct articulation of why this is not a GUT. In a GUT the manifold survives when all fields are switched off; here it does not. I find no error in this reasoning.

The two-scalar exhaustion (trace + inner product, "no room for a third term") is now backed by a verified algebraic rigidity, `dim HH¹ = dim HH² = 0` (S95 W2-2, PASS). This converts what would have been a hand-waving counting argument into a structural theorem: every first-order associative deformation reduces to an inner fluctuation. I accept this as *necessary* (follows from the semisimplicity of `A_K` via Whitehead's first lemma), not contingent. It is the matrix-model/IKKT virtue stated precisely — the interaction structure is forced by the algebra rather than selected from inequivalent string-vertex options.

### 2. The no-interior-saddle / transit-not-slow-roll result is one-loop-robust

**Result**: `dS/dτ > 0` everywhere (E7, Structural Monotonicity, 9,600/9,600 checks), so `Z = Σ e^{−S(τ)}` has no interior saddle in `τ`; the universe transits rather than settling. The slow-roll relations `r = 16ε`, `n_s = 1 − 6ε + 2η` are INAPPLICABLE. Now extended: the *full* effective action `Γ[τ] = S + ½Tr ln(D_K²/Λ²)` retains fixed sign with zero interior sign-changes (S95 W2-3, PASS, 200-point grid, three routes). Classification: **GEOMETRIC** (a statement in the modulus) with **PHONONIC** consequence (the GGE relic).

This is the result I most want to defend, because the document defends it the right way. The inapplicability of `r = 16ε` is **structural, not a wrong number**: `r = 16ε` is a *theorem of the single-clock adiabatic vacuum*, derived from the same `c_s = 1`, single-field, slowly-varying background that validates the Bunch–Davies mode functions. The fold violates all three premises at once (diabatic sweep, BdG dispersion `c_s ≠ 1`, multi-mode squeezed GGE). When a relation's *derivation assumptions* are absent, its conclusion does not merely mismatch — it does not apply. This is precisely the kind of *Gedankenexperiment* elimination I value: one identifies that the premises fail and the entire class of slow-roll predictions is removed without computing a single tensor mode. The document earns this.

The boundary-domination reading (§1.3a) — an action with no interior stationary point is dominated by its boundary configuration, the genesis `τ=0` — is the spectral-action analog of a Gibbons–Hawking–York boundary-dominated path integral. I find this analogy sound and load-bearing: it makes "transit, not slow-roll" structurally inevitable rather than merely observed. The one-loop robustness (S95 W2-3) is the correct thing to have checked, because a tree-level-only monotonicity would be vulnerable to the objection that the loop term introduces an interior feature.

### 3. The Spectral-Moment Decoupling Theorem licenses "distinct physics, one operator"

**Result**: `a₀(τ), a₂(τ), a₄(τ)` are curvature polynomials of distinct degree (0,1,2), algebraically independent, Wronskian `W ∝ R_K′(τ)³ = e^{−12τ}(e^{3τ}−1)⁶`, vanishing to sixth order *only* at `τ=0` (S75 W2-E, CERTIFIED; Sage-verified this build). Classification: **GEOMETRIC**.

This is the keystone that turns "one operator" from a slogan into a defensible claim, and it answers the skeptic's only serious structural objection ("is `a₄` just a dressed `a₀, a₂`?"). The closed form is striking and I have re-derived its logic: the Wronskian of `{1, R_K, R_K²}` is `∝ R_K′³` for the elementary reason that distinct powers of a *moving* scalar are independent, and they collapse to one knob iff the scalar stops moving — which happens only at the maximally-symmetric genesis. So the layers degenerate at `τ=0` and separate the instant exflation begins. This is the *same* band-lifting (`SO(8) → U(2)` into B1/B2/B3) that §2.4 describes, restated at the moment level. The structural unity here is genuine and I record it as such.

The honest scorecard (§7.3) draws exactly the right inference from this theorem: observables across distinct moment layers (`a₀ × a₂ × a₄`) multiply as independent because the Wronskian certifies their independence, while observables *within* one layer (`Ω_DM` and `σ₈`, both `a₂`-channel) share a geometric origin and must NOT be multiplied. This is the correct use of a structural theorem to discipline a probability statement — and it is exactly where I would otherwise have objected to a naive product-of-likelihoods argument. The document pre-empts the objection.

### 4. The cosmological-constant treatment is the most nuanced I have seen, and correctly partitioned

**Result**: Non-inheritance of the 114-OOM catastrophe is *exact* via the Gibbs–Duhem equilibrium identity (`ε − μq = −P = 0`, S95 W5-3 EQUILIBRIUM-CC-WARRANT PASS, Sage-rational 0); the *observed* magnitude (`ρ_vac/ρ_obs = 1.032`, DILUTION-CC-66) is a non-equilibrium tracking residual conditional on C10 (`ρ_vac ∼ M_Pl²H²`, ASSUMED-PARTIALLY-PROVEN). Classification: **GEOMETRIC** location (`a₀` moment), **PHONONIC** magnitude (tracking-vacuum departure from equilibrium).

I have a uniquely invested stake in Λ — I introduced it, called it my greatest blunder, and the field equations admit it as geometrically natural. The capstone's treatment satisfies my standard for what an honest framework owes on Λ. It does NOT claim to have solved the cosmological-constant *problem*; it claims to have correctly *located* the term (the `a₀` moment, geometrically natural — not inserted by hand) and to have made the *equilibrium* value exactly zero by an identity rather than a tuning. The distinction is the whole game: the catastrophe is a container-EFT artifact of computing vacuum energy without a UV completion, and the substrate has its UV completion (`D_K`), so the bare term is removed by an identity (Clause A, warranted exactly) while the observed magnitude is the relaxation residual (Clause B, conditional on C10 and on the external `H`).

I particularly endorse the explicit declaration that the warrant is **thermodynamic (Gibbs–Duhem), not topological** — the substrate is ³He-B class (`N₃ = 0`, BDI), not ³He-A where Λ would be topologically protected. This matters because a reader who knows Volovik will reach for the topological-protection statement; the document forecloses that error. My memory records the matching constraint-map fact: "Mass problem IS CC problem; Weinberg no-go applies to Goldstone sector," and "the CC gap is ENTIRELY in `a₀` (geometric)." The capstone is consistent with both. The 1.032 closure is a genuine PASS *given* an external `H(t)` — which is the same undelivered effective-Friedmann map as the `a(t)` gap. The document says "doubly conditional" and I agree it is exactly doubly conditional, no more and no less.

### 5. The `a(t)` gap is correctly a category statement, and correctly = frontier #8

**Result**: No substrate-derived FRW scale factor. C1 (modulus → cosmic time) is POSTULATED; C2 (`K_pivot`) is BROKEN-WITH-LIVE-PATHWAY; T6 (Friedmann–BCS locking) is BROKEN (155,984-mode spectral action overwhelms 8-mode BCS by 133,200×). Two PROXY scale factors exist (`a_eff` from `a₂`; Connes-distance `a(τ)` with `q ∈ [−0.97, +0.81]`), neither promoted. Classification: **GEOMETRIC** gap with cosmological consequence.

This is the section where I, the GR specialist, would be most tempted to object — and the document disarms the objection before I can raise it. The Jacobson (1995) reading made microscopic is exactly right: the Einstein/Friedmann equations are equations of *state* of the emergent metric, derivable from horizon thermodynamics, so a substrate theory is *expected* not to contain a fundamental Friedmann equation. The `a₂` moment IS the Einstein–Hilbert action Jacobson recovers thermodynamically, and the framework's own `Z = Σ e^{−S}` is the partition function in question.

But — and the document says this in italics, which I applaud — "Friedmann is the wrong question" is right about the *fundamental* level and **wrong about the *effective* level**. The framework owes a *derived effective* Friedmann map, and it already *borrows* the container-observer's FRW `H(t)` for every late-time observable (caveat C10). Both must be said. The transit-axis reframing is the sharpest statement available: the missing object is a **back-reaction closure** `H² = f(ρ_relic, S_SA)`, not a kinematics gap — the kinematics (local sweep rate `τ̇`, full Bogoliubov spectrum) are in hand; what is absent is the equation promoting produced relic energy density into a source for the *global* expansion rate. The T6 FAIL is precisely the 155,984-vs-8-mode overwhelm. I record this as the honest formulation, and it is the seed for the highest-leverage §V item.

My own memory's EMERGENT-EIH-LIFT note (S95 W3-1, PASS) is the partial down-payment on this gap: the `a₂`-channel induced Einstein–Hilbert is a scalar-tensor theory with `φ(τ) = 1/(16πG_eff) = f₂Λ²a₂(τ)/(48π²)`, and the gravity-only obstruction `∇_μ G_eff^{μν} = (R/2)φ′ ≠ 0` (the `a₂′(τ)·∂_μτ` term) **cancels exactly on the modulus EOM** via the Noether identity `∇_μ(G_eff − ½T_mod) = ½(scalar EOM)(∇τ)`, ratio = ½ Sage-exact. This lifts the S25 spectral-Bianchi + S44 internal-K EIH to the *emergent* `g_M` — but as STRUCTURE, not magnitude. The seconds-normalization (`M_KK⁻¹ →` seconds) remains open. The document's §9 frontier #8 is consistent with this, and correctly downgrades it to "generic-identity-cored" at the value level.

### 6. The Ordered Veil information argument is sound and resolves an analog paradox

**Result**: Diabatic transit (`R_therm = t_therm/t_transit = 5251.82 ≫ 1`, S95 W5) freezes a pure-product GGE relic (`S_ent = 0`, S95 W5); `τ_fold` is a double-root extremal Killing horizon (`V = V′ = 0 ⟹ κ = 0, T_H = 0`), so zero Hawking temperature is the causal-side corroboration. Classification: **PHONONIC** (relic excitation content).

The information-theoretic reading touches my EPR/completeness instincts directly, and it is correct. The transit is a Bogoliubov transformation — unitary by construction. A thermalizing relic (`S_ent > 0`) would scramble that unitary into a mixed state, hiding the squeeze phase the way a black hole's thermal flux hides infalling information. The GGE stays pure: the Bogoliubov phase data is retained in the conserved charges. There is no Page curve to reproduce because nothing thermalizes, and the substrate carries no horizon-entropy debt out of the fold. This is the analog-gravity statement of completeness — every element of the physical reality of the squeeze has a counterpart in the conserved-charge data — and it is exactly the kind of consistency I require. The triple-leg certification (diabaticity `R_therm`, purity `S_ent = 0`, geometric `κ = 0`) is over-determination, which is the right standard. I note the document's honesty that the *surviving* claim is "diabatic transit-freeze, not integrability permanence" (S39 retraction: 13% non-separable channel, Brody β = 0.633) — the Ordered Veil is a statement about the transit, not about permanent integrability.

---

## III. Gate Verdicts

These are AUTHORITATIVE per the source; I cite, not re-adjudicate. Cross-checked against knowledge MCP where noted.

| Gate / Result | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| E7 Structural Monotonicity | PROVEN | `dS/dτ\|_fold = +58,672.8`; 9,600/9,600 checks |
| S95 W2-3 one-loop no-interior-saddle | PASS | 0 interior sign-changes, 200-pt grid, 3 routes |
| S95 W2-2 algebraic rigidity | PASS | `dim HH¹ = dim HH² = 0` |
| S75 W2-E Spectral-Moment Decoupling | CERTIFIED | `W ∝ R_K′³`, vanishes order-6 only at τ=0 |
| S95 W5-3 EQUILIBRIUM-CC-WARRANT (Clause A) | PASS | `ε − μq = −P = 0` (Sage-rational 0) |
| DILUTION-CC-66 (Clause B) | PASS (C10-conditional) | `ρ_vac/ρ_obs = 1.032` (0.01 OOM) |
| S95 W3-1 EMERGENT-EIH-LIFT (my memory) | PASS | Noether-ratio = ½, `∇_μ G_eff = 0` on-shell |
| S95 W3-5 κ_EP | EXACT (NLO; generic-cored) | `κ_EP = 1.000000` |
| S95 W4-5 12D cosmic censorship | PASS | NEC to `τ_NEC = 1.383`; singularity at τ→∞ censored |
| S95 W-1 asymmetric white hole | PROVEN (6 walls) | one entry sonic surface, open supersonic exit |
| S74 W1-E Friedmann closure | FAIL (structural) | 133,200× spectral/BCS overwhelm |
| C1 (τ ↔ cosmic time) | POSTULATED | — |
| C2 (`K_pivot`) | BROKEN-WITH-LIVE-PATHWAY | — |
| T3-BATCH-S75 emergent Lorentz (higher-order) | INFO (not PROVEN) | `α_LIV = 0` exactly at leading order |
| w₀ (Volovik partition) | LIVE | `w0_FW = −0.918` (MCP-confirmed canonical) |
| wₐ four-fold lock | LIVE WAGER | `0` (structural) vs `−0.72 ± 0.21` → 3.43σ |

---

## IV. Structural Implications

**What is solid (necessary, follows from structure alone).** The principle-theory framing (§0–§1); the gauge group as `SU(A_K)`; the two-scalar exhaustion (HH¹=HH²=0); KO-dim 6 and `[J, D_K] = 0` (my memory: machine-ε, 79,968 pairs); the no-interior-saddle transit (E7, one-loop-robust); the Spectral-Moment Decoupling Wronskian; volume preservation `det g_τ = 3⁸` (Sage-verified, exponent `2−6+4=0`); the equilibrium-CC non-inheritance identity. These define the walls of the solution space and I treat them as permanent.

**What is contingent (depends on inputs that remain open).** The `ε_H` sign and CMB tilt depend on the regularization scheme `f` — the document's FI/RD partition is the correct response (Functional-Invariant ratios survive; regulator-dressed observables must be *determined*). The red tilt is right *if* `f = √x`. The CC magnitude is C10-conditional. `m_H` is route-dependent. These are exactly what a principle theory is entitled to leave to a future completion, and the document's ledger `{τ, Λ, f₀, f₂, f₄} + t*` is honest.

**What is generic, not predictive (the discipline I most want preserved).** The κ_EP = 1 and Noether-ratio = ½ PASSes are generic-identity-cored — they are the Lichnerowicz `R/4` coefficient and the Brans–Dicke Noether contraction of *any* spin Dirac operator. The document's §9 update gets this exactly right: "weak EP at LO+NLO is STRUCTURALLY INEVITABLE on the single-operator postulate; value-generic" — NOT "the substrate uniquely PREDICTS κ_EP = 1 where a generic emergent-gravity model would differ." A genuine substrate EP *prediction* first appears at NNLO where `ν_b(C₂)` re-enters (`CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR`). This is the single best piece of self-skepticism in the document and it must not be diluted in any future presentation. Per `epistemic-discipline.md`, the two exact-PASSes are two consequences of ONE premise (single emergent metric), NOT two independent confirmations — I endorse this without qualification.

**CONFLICT FLAGGED — Lichnerowicz convention vs my memory.** §2.3 (corrected note, lines 176–180) states the bound "convention-free" as `λ² ≥ R_K(τ)/4 > 0`, with `R_K(0)/4 = ½` in the E3 rational normalization, and explicitly declines to print "≥ 3" beside the E3 curvature (where it would read `2/4 = 3`, false). My own memory carries the baseline figure "≥ 3" without the convention caveat. **The document is correct and my memory is the stale entry**: the "≥ 3" belongs to the dimensionful normalization (`R_K ≥ 12`), and the two differ by the factor-6 bi-invariant scale convention. I flag this so the record shows I cross-checked it and resolved in the document's favor; I will update my own memory's E5/Lichnerowicz line accordingly. This is not a physics error in the capstone — it is a fix the capstone already made.

**TENSION FLAGGED — "derives its own stage" vs the undelivered full Einstein equation.** §0 says the equation "derives the stage" (manifold + metric from `a₂`). §6.3 says the *full* Einstein equation `G_{μν} = 8πG T_{μν}` sourced by emergent matter is the open substrate→FRW loop, NOT a delivered result. These are reconcilable — and the document reconciles them (the EH *kinematic term* is delivered via `a₂`; the *sourced* field equation is not) — but the §0 phrasing "derives the stage" will be over-read by a referee as "derives Einstein's equations." The document's own §1.1/§1.3 hedge ("Einstein–Hilbert *kinematic* term") and §6.3 caveat are the correct guardrails; I record this as a presentational risk, not a contradiction. The honest statement is: **the equation derives the *kinematic skeleton* of the stage (the EH action and `g_M`); it does not yet derive the *dynamical* stage (the sourced, generally-covariant field equation closing to FRW).** Both halves load-bearing.

**UNSTATED ASSUMPTION FLAGGED — the τ_fold vs τ₀ split is correctly partitioned but the gauge-running between them is asserted, not shown here.** The reading conventions (§ preamble item 3) state the spectral physics is read at `τ_fold = 0.190` while the Weinberg angle (E26) is solved at `τ₀ = 0.2994`, and these are "never silently conflated." Good. But the document defers "the gauge-running between scales" to §7 — and §7 does not actually exhibit the running `τ_fold → τ₀`; it is asserted as "§7's business." This is a genuine (small) gap: the claim that the two operating points are connected by a *derived* RG flow is not demonstrated in the capstone. It is plausibly closed elsewhere in the corpus, but as written the capstone asserts a connection it does not show. Flagged for §V.

**Direction-of-explanation audit (framing law).** I checked every emergent-GR arrow in the document against `phononic-framing.md`. The document holds the substrate→emergent direction throughout: gravity is the `a₂` moment (not "Einstein's equations govern"); `H(t)` is the *readout* of spectral reorganization (not a clock the vacuum decays in); the area theorem is derived from spectral monotonicity (not invoked to explain the substrate). §6.3's framing-discipline paragraph ("refuse 'the vacuum energy decays *in* the expanding universe'; require 'the `M_Pl²H²` reservoir dilutes *as* the substrate's spectral complexity reorganizes'") is the correct container-relapse guard and I find no violation. The one place a reader will relapse is the borrowed FRW `H(t)` (C10) — but the document tags every such row with `†` and states the borrowing explicitly, which is the honest handling.

---

## V. Carry-Forward Computations

**This is the harvest.** Every open question I can identify on the emergent-GR / equivalence-principle / cosmological-constant axis, converted to a runnable computation. Each has all four fields.

```
V.1. Derived effective Friedmann map H² = f(ρ_relic, S_SA) — the back-reaction closure (frontier #1+#8)
   - What: Derive an effective 4D gravitational action for g_M from the τ-flow of S_SA(τ), then
     vary to obtain H²_eff. Concretely: take the EMERGENT-EIH-LIFT scalar-tensor action
     S_grav = ∫ φ(τ)R√g d⁴x with φ(τ) = f₂Λ²a₂(τ)/(48π²) (S95 W3-1), add the modulus kinetic +
     potential V(τ) = S_SA(τ) = a₀−a₂+a₄, and compute the (0,0) Friedmann constraint
     H²_eff = (1/3φ)[½τ̇² + V(τ) − 3Hφ̇]. Test whether the produced relic energy density
     ρ_relic (from N_pair, E_exc/E_cond = 443, §5.3) sources it consistently.
   - Inputs: a_2_FW_zeta = 2776.165389 (MCP-confirmed), a_0_FW_zeta = 6440, a_4_FW_zeta = 1350.7216
     (canonical_constants SECTION D); f₂ ≈ 92 (§8.3 reduced dictionary); R_K(τ) closed form (E3);
     S95 W3-1 npz (Noether chain, ratio=½); the modulus EOM from S44; E18 relic content.
   - Gate: Creates EFF-FRIEDMANN-CLOSURE. PASS if H²_eff(τ) is generally covariant AND reproduces
     a sensible q(τ) consistent with the Connes-distance proxy band q ∈ [−0.97, +0.81]
     (SCALE-FACTOR-54) to within 20%; FAIL if the 155,984-vs-8-mode overwhelm (T6) re-appears
     (i.e. the spectral action again cannot be closed against the relic source); INFO if covariant
     but seconds-normalization-blocked.
   - Effort: 6-10 hours, 2 agent sessions (1 to derive the variation, 1 to numerically integrate).

V.2. The M_KK⁻¹ → seconds normalization (the residual piece of the a(t) gap)
   - What: Pin the conversion from substrate time units (M_KK⁻¹) to physical seconds. The conformal
     embedding Ω(τ) (S95 W4-4) reproduces the Connes-distance q-range but leaves the overall
     time-scale undetermined. Compute the normalization by matching one anchored physical scale —
     e.g. requiring the post-fold frozen-plateau τ_now to coincide with the present Hubble time
     t_H given the borrowed H₀ — and report whether the match is consistent or over-determined.
   - Inputs: Ω(τ) conformal factor (S95 W4-4 npz); δt_transit = 1.130×10⁻³ M_KK⁻¹ (canonical);
     Mach = 13.75; c_fabric = 209.97 M_KK; H₀ (Planck); clock constraint E27 (|τ̇| < 2.4×10⁻⁶ τ₀/t_H).
   - Gate: Creates SECONDS-NORM. PASS if a single normalization constant reconciles δt_transit,
     the plateau freeze, AND the clock constraint simultaneously (over-determined → strong);
     FAIL if the three require mutually inconsistent normalizations; INFO if consistent but with
     one free constant remaining (under-determined).
   - Effort: 3-4 hours, 1 agent session.

V.3. NNLO equivalence-principle Casimir discriminator (the FIRST genuine substrate EP prediction)
   - What: Compute κ_EP at NNLO, where the band-specific Casimir eigenvalue ν_b(C₂) re-enters the
     ratio (the document states the LO+NLO κ_EP = 1 is generic; the prediction is at NNLO). For two
     distinct Peter-Weyl bands b, b′ (e.g. B1 acoustic vs B3 optical), expand D_K² = ∇*∇ + ¼R_K to
     second order in the heat-kernel and extract the band-dependent free-fall correction
     Δκ_EP = κ_EP(b) − κ_EP(b′) ∝ [C₂(b) − C₂(b′)].
   - Inputs: D_K spectrum at τ_fold (L_max=10 cache, 78,080 unique eigenvalues); Casimir labels
     C₂(p,q) per band; E5 Lichnerowicz decomposition; the band structure B1/B2/B3 (§2.4).
   - Gate: Creates CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR (named in §9). PASS if Δκ_EP ≠ 0 at machine
     precision (the substrate makes a genuine, value-bearing EP prediction distinguishing it from a
     generic single-metric emergent-gravity model); INFO if Δκ_EP = 0 (EP universality persists to
     NNLO — still generic); the SIGN and MAGNITUDE of Δκ_EP is the falsifiable content.
   - Effort: 5-7 hours, 1-2 agent sessions (heat-kernel NNLO is the hard part).

V.4. Higher-order emergent Lorentz isotropy — promote T3-BATCH-S75 from INFO to PROVEN or bound it
   - What: Test whether the single emergent light-cone g_M (from a₂) reproduces isotropy beyond
     leading order. Compute the leading anisotropy in the dispersion of high-k excitations on g_M
     across the three bands: does v_g(k) → c uniformly in direction, or does the SU(3) fiber
     structure imprint a directional dependence at O((k/M_KK)²)? Extract α_LIV at next order.
   - Inputs: BdG dispersion v_g(k) per band (Layer-2 cones, c_b² = v_g(k) on g_M); the a₂-emergent
     metric; the tensor-sector decoupling [T3] β_T = 0; M_KK = 7.4287×10¹⁶ GeV.
   - Gate: Feeds T3-BATCH-S75-EMERGENT-LORENTZ (currently INFO). PASS (promote to PROVEN) if
     α_LIV = 0 to next order across all bands; FAIL if a nonzero directional anisotropy appears at
     O((k/M_KK)²) — which would be a genuine (Planck-suppressed) LIV prediction, NOT a defect, and
     would need to be checked against Fermi-LAT/LHAASO bounds; INFO if band-dependent but below
     any detector horizon.
   - Effort: 4-6 hours, 1 agent session.

V.5. Exhibit the derived gauge-running τ_fold → τ₀ (close the asserted-but-unshown connection)
   - What: The capstone reads spectral physics at τ_fold = 0.190 and the Weinberg angle (E26) at
     τ₀ = 0.2994, asserting these are connected by "§7's gauge-running" without showing it. Compute
     the RG flow of sin²θ_W (and g₁/g₂ = e^{−2τ}) from τ_fold to τ₀ and verify the two operating
     points are connected by a derived flow, not a coincidence. Report the running explicitly.
   - Inputs: g₁/g₂ = e^{−2τ} (E-relation, my memory PROVEN); E26 Weinberg relation; the SM
     one-loop β-functions; the KK threshold scale M_KK.
   - Gate: Creates TAU-FOLD-TAU0-RUNNING. PASS if the standard SM running connects the spectral
     value at τ_fold to the E26 solution at τ₀ within the framework's stated precision; FAIL if the
     two operating points require an underived intermediate input; INFO if connected but
     scheme-dependent.
   - Effort: 3-5 hours, 1 agent session.

V.6. Resolve the Z_fold normalization in the G_N dictionary (the document's own PRELIMINARY tag)
   - What: §8.3 flags that the canonical S83 G_N dictionary form M_Pl_eff² = M_KK²a₂f₂^R/π²·Z_fold⁻¹
     and the §8.3 24π² form differ by the Z_fold normalization, "which should be pinned before either
     is cited as THE dictionary." Pin Z_fold by deriving it from the heat-kernel normalization
     convention and report which of the two dictionary forms is canonical.
   - Inputs: a_2_FW_zeta = 2776.165389; M_KK = 7.4287×10¹⁶ GeV; M_Pl,red; the S83 derivation;
     the Chamseddine–Connes 1/(16πG) = f₂Λ²a₂/(48π²) dictionary.
   - Gate: Creates Z-FOLD-PIN. PASS if Z_fold is fixed to a single value reconciling both forms
     (f₂ ≈ 92 should then be unambiguous); FAIL if the two forms cannot be reconciled at fixed a₂^ζ;
     INFO if Z_fold is convention-dependent (then declare the convention explicitly).
   - Effort: 2-3 hours, 1 agent session.

V.7. Emergent Bianchi identity on g_M beyond the linear (β_T = 0) order
   - What: The EMERGENT-EIH-LIFT (S95 W3-1) establishes ∇_μ G_eff^{μν} = 0 on-shell at the level
     where the Noether-ratio = ½ cancellation holds. Test whether the emergent Bianchi identity
     survives at second order in the metric perturbation (where the scalar-tensor coupling
     φ(τ) = a₂(τ) introduces curvature-dependent corrections), i.e. whether the emergent matter
     genuinely moves on geodesics of g_M as an Einstein–Infeld–Hoffmann consequence at NLO.
   - Inputs: S95 W3-1 npz (Noether chain); φ(τ) = f₂Λ²a₂(τ)/(48π²); a₂′(τ) > 0 sign (S64 W1-A,
     R-monotone, AM-GM); the modulus EOM (S44); [T3] scalar-tensor decoupling.
   - Gate: Creates EMERGENT-BIANCHI-NLO. PASS if ∇_μ G_eff^{μν} = 0 persists at NLO (emergent EIH
     geodesic motion confirmed beyond linear order — substantively advances frontier #8); FAIL if a
     non-cancelling source appears at NLO (the emergent EP breaks at second order); INFO if it holds
     only on a restricted class of perturbations.
   - Effort: 6-8 hours, 2 agent sessions.

V.8. SDW convergence test underneath the CC absolute magnitude (JACOBSON-NONLOCAL-64)
   - What: The CC ratio (1.032) is truncation-robust but the CC ABSOLUTE magnitude awaits a
     Seeley–DeWitt-convergence statement (frontier #6, the gate underneath frontier #5). Compute the
     a₀-moment vacuum-energy magnitude as a function of L_max (the truncation) and test whether it
     converges or diverges as L_max grows — i.e. whether any absolute a₀ vacuum energy can be
     promoted to physical status, or whether only the dimensionless ratio survives.
   - Inputs: a₀ raw mode-count (155,984 at L_max=10) vs a_0_FW_zeta = 6440; the L_max scan of the
     zeta-regulated a₀; the multiplicative-normalization-cancellation invariant (the FI ratio
     R₁ = a₀a₄/a₂² = 1.12865, Sage-verified); JACOBSON-NONLOCAL-64 status.
   - Gate: Feeds JACOBSON-NONLOCAL-64 (OPEN). PASS if the zeta-regulated a₀ converges with L_max
     (an absolute vacuum-energy magnitude becomes citable); FAIL if it diverges (only ratios are
     physical — the document's §8.5 honest boundary stands); INFO if it converges only under a
     specific regulator class (then tag the class). NOTE: per my memory, "Hausdorff impossibility
     for CC: 242 orders" — this gate should check against that wall, not re-open it.
   - Effort: 4-6 hours, 1 agent session.

V.9. The conformal-factor Ω(τ) embedding — promote SCALE-FACTOR-54 / W4-4 from INFO toward a derived proxy
   - What: The conformal embedding Ω(τ) reproduces the Connes-distance deceleration band q ∈
     [−0.97,+0.81] but only with the Connes-distance proxy, not a_eff (S95 W4-4, INFO; the two
     proxies are conformally distinct). Compute whether Ω(τ) can be derived from D_K (rather than
     constructed to fit q) by deriving the conformal weight from the a₂-moment flow directly, and
     test whether the two proxies (a_eff and Connes-distance a(τ)) can be unified under a single
     derived conformal map.
   - Inputs: a_eff(τ) = (a₂(τ)/a₂(today))^{1/2}; Connes-distance a(τ) (SCALE-FACTOR-54, q range);
     Ω(τ) construction (S95 W4-4 npz); R_K(τ) closed form; the 12D censorship structure (W4-5).
   - Gate: Feeds the a(t) gap (frontier #1). PASS if Ω(τ) is derived from D_K and unifies the two
     proxies (a real step toward a(t)); FAIL if the two proxies are irreducibly conformally distinct
     (then a(t) requires more than a conformal map); INFO if Ω(τ) is derivable but proxy-specific.
   - Effort: 4-6 hours, 1 agent session. DEPENDS ON V.1 (the effective Friedmann map constrains Ω).

V.10. The asymmetric-white-hole entry-surface falsifier F1 (a₂ kinematic-carrier observable)
   - What: §6.2 holds the "a₂ carries no observed quantum" claim PENDING falsifier F1 — a scan for a
     scalar-channel observable squeeze branch near the a₂ kinematic-carrier temperature 72.8 M_KK,
     an order of magnitude above the a₄ condensate-squeeze support ω ∈ [0.82, 1.06]. Compute the
     predicted spectral density of any scalar-channel squeeze in the band around 72.8 M_KK and
     confirm/deny the expected NULL.
   - Inputs: the analog-T ledger (a₂ surface T = 72.8 M_KK, κ = 457.66; a₄ surface T = 7.578 M_KK);
     the greybody Γ(ω) filter (S95 W4-3); the scalar-sector acoustic metric g_acoustic; the
     condensate-squeeze support window.
   - Gate: Creates WHITE-HOLE-F1. PASS (confirm composite emission) if the scalar-channel squeeze
     near 72.8 M_KK is NULL (the a₂ carrier is observationally invisible, as both readers predict);
     FAIL if a non-null scalar squeeze branch appears at 72.8 M_KK (the categorical "a₂ carries no
     observed quantum" breaks); INFO if below detector horizon either way.
   - Effort: 3-4 hours, 1 agent session.
```

Priority ordering on my axis: **V.1 is the single highest-leverage computation in the entire harvest** — it closes frontiers #1 and #8 jointly and is the document's own "single most important open item." V.3 (NNLO Casimir) is the first place the framework makes a *genuine, value-bearing* EP prediction rather than a generic identity, so it is the highest-value *discriminating* test. V.2 and V.6 are bounded normalization closures that unblock V.1. V.5 closes a small asserted-but-unshown gap I flagged in §IV.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Container-removal / principle-theory framing (§0–§1) | GEOMETRIC | SOLID | "One equation" is categorically stronger than a GUT; the short parameter ledger is *entitled*, not lucky |
| 2 | No-interior-saddle transit, one-loop-robust (E7, W2-3) | GEOMETRIC | PROVEN | `r = 16ε`/`n_s` slow-roll relations INAPPLICABLE *by absent premises*, not wrong number |
| 3 | Spectral-Moment Decoupling Wronskian (S75 W2-E) | GEOMETRIC | CERTIFIED | Licenses cross-layer likelihood-multiplication; degenerate only at genesis |
| 4 | CC: equilibrium non-inheritance exact (Clause A); magnitude C10-conditional (Clause B) | GEOMETRIC location / PHONONIC magnitude | PASS (doubly conditional) | Framework *locates* Λ (the a₀ moment, natural); has NOT solved the Λ *problem* |
| 5 | `a(t)` gap = frontier #8; back-reaction closure missing | GEOMETRIC | OPEN (honest category statement) | The single most important open item; → V.1 |
| 6 | Ordered Veil information argument (S_ent=0, κ=0, R_therm) | PHONONIC | PROVEN (3 legs) | Analog completeness; no Page curve because nothing thermalizes |
| 7 | κ_EP=1 / Noether-ratio=½ are generic-identity-cored | GEOMETRIC | EXACT but VALUE-GENERIC | Two consequences of ONE premise, NOT two confirmations; real prediction at NNLO (V.3) |
| 8 | Lichnerowicz "≥3" convention | GEOMETRIC | DOC CORRECT, my memory STALE | Document already fixed it; I update my memory, not the capstone |
| 9 | "Derives the stage" vs undelivered sourced Einstein eq | GEOMETRIC | TENSION (presentational) | Delivers EH *kinematic skeleton*; not the *dynamical* sourced field equation |
| 10 | τ_fold → τ₀ gauge-running asserted, not shown | PARTICLE | GAP (small) | → V.5 |
| 11 | Z_fold normalization in G_N dictionary | GEOMETRIC | PRELIMINARY (doc's own tag) | → V.6 |
| 12 | SDW convergence underneath CC absolute magnitude | GEOMETRIC | OPEN (JACOBSON-NONLOCAL-64) | Ratios robust; absolutes pending; → V.8 |

**Closing principle-theoretic verdict.** Everything should be made as simple as possible, but not simpler. This capstone makes the universe as simple as one operator and one functional — and refuses to make it simpler than that, by stating without softening that it does not select its own `τ`, does not determine `f`, does not derive `a(t)`, and does not predict the family number. That refusal is the document's greatest strength. The equation is a *principle theory*: it constrains, it derives its own kinematic stage, and it earns its short ledger. What it owes — the derived, generally-covariant effective action for `g_M` that would simultaneously be the Friedmann map, the equivalence principle, and the Einstein–Infeld–Hoffmann theorem — is exactly one object, and the harvest above is the path to it.
