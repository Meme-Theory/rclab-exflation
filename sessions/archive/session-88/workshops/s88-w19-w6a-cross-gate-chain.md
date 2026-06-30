# Session 88 W19 Synthesis: W6a Cross-Gate Chain `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)` — Load-Bearing Structural Identity vs Cartan-Arithmetic Coincidence

**Date**: 2026-05-07
**Agent**: lizzi-spectral-functional-theorist (PRIMARY of both §W6a-51 and §W6a-52; structural workshop verdict on the synthesis line 761 cross-gate algebraic chain)
**Source Documents**:
- `sessions/archive/session-88/session-88-w6a-workingpaper.md` (line 761 synthesis claim; full §W6a-51 + §W6a-52 derivations + connes co-signs)
- `sessions/session-plan/session-88-plan-w6a.md` (substitution-chain plan §10 Steps 1–8 for §W6a-51; plan §10 Steps 1–5 for §W6a-52)
- `sessions/archive/session-88/workshops/_seed-w6a.md` (Workshop 2 tension framing; Workshop 1 + Workshop 3 sister-tensions; CF-W6A-ADDITIONAL-A/B/C carry-forward seeds)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md` (zeta-not-physical permanent; FI/RD/MIXED classification; spectral functional family canonical constants; chi_2 not R-protected boundary)

---

## I. Session Outcome

The cross-gate algebraic chain `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)` claimed at WP synthesis line 761 as the "load-bearing structural finding of W6a" admits an INTERMEDIATE STRUCTURAL VERDICT pending SU(N) cross-validation. The chain is ALGEBRAICALLY VALID at SU(3) by construction of §W6a-51 Step 5 (the τ-kernel coefficient `5π` is explicitly factored out as `(Cartan-rational-sum) · π · 1/(dim+rank)` with the Cartan-rational-sum unity-on-SU(3)-Y verified Python: `0/2 + 1/2 + 1/2 = 1` exactly), and the PRODUCT structure is algebra-INVARIANT per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (both (dim+rank)/2 and π_Plancherel are algebra-INVARIANT spectrum-only/coset-volume objects, not state-pair functionals). However, the LOAD-BEARING vs COINCIDENCE classification CANNOT be settled from SU(3) data alone: the integer 5 in §W6a-52 and the integer 5 in §W6a-51 share an upstream Cartan-arithmetic origin (`(dim+rank)/2 = |Δ⁺| + rank = 5` on SU(3)), and at the SU(3) instance both readings (lizzi load-bearing vs connes coincidence) yield the same numerical chain. The discriminator is the SU(N) cross-validation gate `S89-W6A-CROSS-GATE-CHAIN-SUN-CROSS-VALIDATION` (CF-W6A-ADDITIONAL-B): if the SU(N)-analog hypercharge generator's Cartan-rational-sum equals 1 for N ∈ {2, 4} ⇒ chain is LOAD-BEARING-STRUCTURAL ⇒ third STAGE-1-CANDIDATE registry entry warranted; if the Cartan-rational-sum varies with N ⇒ chain is COINCIDENCE-AT-SU(3) ⇒ synthesis line 761 downgrade required.

The interim disposition is **STAGE-1-CANDIDATE-PENDING-SU(N)-CROSS-VALIDATION** with the synthesis text held as-written conditional on the cross-validation outcome.

---

## II. Key Results

### Result 1 — Chain decomposition is algebraically valid for SU(3) by construction

**Result**: `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T) = 5 · π` at SU(3); GEOMETRIC

The §W6a-51 substitution chain Step 5 explicitly produces the `5π` factor in two algebraically separable steps:

1. **Cartan-positive-root sum on SU(3) hypercharge** (RATIONAL, machine-zero exact): For `Y = (1,1,0)` with positive roots `Δ⁺(SU(3)) = {(1,−1,0), (1,0,−1), (0,1,−1)}` all of `|α|² = 2`, the sum `Σ_{α} ⟨α,Y⟩²/|α|² = 0/2 + 1/2 + 1/2 = 1` (Python-verified, Sage-symbolic-equivalent in ℚ).
2. **Wiener-Ikehara orbit-integration on SU(3)/T** introduces the Plancherel/Haar volume factor π via the standard Helgason Ch. X compact-symmetric-space measure on SU(3)/T = flag manifold.

The §W6a-51 derivation then writes `κ_K = (Cartan-rational-sum) · π / (dim+rank) = 1 · π / 10 = 1/(10/π)`, equivalently the τ-kernel denominator coefficient is `(dim+rank)/2 · π = 5π`. The factor `(dim+rank)/2 = 5` from §W6a-52 and the factor `π` from §W6a-51 Step 5 Plancherel-orbit-integration are EXPLICITLY identifiable as the multiplicative components of the τ-kernel coefficient at the SU(3) instance. **This is not a numerical coincidence at SU(3); it is the closed-form factorization of κ_K in §W6a-51's own derivation.**

What the chain DOES NOT yet establish: that the same factorization survives at SU(N) for N ≠ 3. The §W6a-51 derivation Step 5 invokes the SU(3)-specific computation `Σ_α ⟨α,Y⟩²/|α|²(SU(3)) = 1`. Whether the analogous computation on the SU(N)-analog hypercharge generator yields 1 (preserving the chain `(dim+rank)/2 · π`) or yields some N-dependent rational `r(N)` (breaking the chain to `r(N)·(dim+rank)/2 · π`) is a separate first-principles computation NOT performed in §W6a-51 and NOT in §W6a-52.

### Result 2 — Algebra-axis orthogonality classification: PRODUCT is algebra-INVARIANT (both factors algebra-INVARIANT)

**Result**: (dim+rank)/2 · π_Plancherel ∈ algebra-INVARIANT spectrum-only family; not a state-pair functional; GEOMETRIC

Per `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (S87 W-2 R3 close), each factor of the chain is classified:

- `(dim+rank)/2`: algebra-INVARIANT. The §W6a-52 connes-side CC7-A argument (WP lines 641–665) shows axiom-2 preservation under Peter-Weyl direct-sum decomposition: the bulk-Weyl exponent `dim(G)` and its Conv-B sector reduction `(dim+rank)/2` are read off the SAME `Sd ⊂ ℂ` regardless of basis representation; the Cartan/root partition is a structural feature of the algebra `A_K = C∞(SU(3))` itself, not a state on it.
- `π_Plancherel(SU(3)/T)`: algebra-INVARIANT. The Plancherel/Haar measure on the compact symmetric space SU(3)/T is an invariant volume form on the GROUP-COSET geometry (Helgason Ch. X); it is NOT a state-pair functional on A_K. It is a structural geometric invariant of SU(3)/T independent of any state choice on A_K.

The PRODUCT `(dim+rank)/2 · π_Plancherel` is algebra-INVARIANT (corner-cell I × corner-cell I = corner-cell I; no algebra-DEPENDENT content introduced by the multiplication). This means the chain — as a product of algebra-INVARIANT factors — does NOT trigger the OP-PROJ vs STATE-PROJ naming-discipline boundary of `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 (S88 W8-92 close). A potential STAGE-1-CANDIDATE registry entry capturing the chain itself can land under bare `§VII.{slot}` without OP/STATE projection-side suffix.

### Result 3 — LOAD-BEARING vs COINCIDENCE is not decidable at SU(3) alone — SU(N) cross-validation is the discriminator

**Result**: at SU(3), both readings (load-bearing-structural, lizzi; Cartan-arithmetic-coincidence, connes) yield numerically identical chains; the discriminator is the SU(N) cross-validation; GEOMETRIC

Both readings agree on SU(3) by construction:

- **Lizzi reading (LOAD-BEARING-STRUCTURAL)**: `(dim+rank)/2` Peter-Weyl direct-sum count multiplies the Plancherel π factor on SU(3)/T to yield the τ-kernel coefficient. At SU(N), the τ-kernel coefficient is predicted to be `(dim+rank)(SU(N))/2 · π = (N−1)(N+2)/2 · π` — i.e., 2π for SU(2), 5π for SU(3), 9π for SU(4).
- **Connes reading (CARTAN-ARITHMETIC-COINCIDENCE)**: The integer 5 in §W6a-52 derives from Peter-Weyl direct-sum dimension counting (`(dim+rank)/2 = |Δ⁺|+rank = 5`); the integer 5 in §W6a-51 derives from a Cartan-positive-root sum on SU(3) hypercharge multiplied by the Plancherel volume factor π. The SHARED upstream is `Δ⁺(SU(3))` and the rank: BOTH gates exploit the same Cartan-arithmetic substrate, so reading off the same integer 5 is unsurprising. At SU(N), the §W6a-52 prefactor (which is a PURE Peter-Weyl count) is `(N−1)(N+2)/2`; the §W6a-51 τ-kernel coefficient is whatever the SU(N)-analog Cartan-positive-root sum evaluates to TIMES π divided by `(dim+rank)`, which need NOT factor as `(dim+rank)/2 · π` at general N.

The factual divergence between the two readings appears at SU(N) for N ≠ 3:

- IF Cartan-rational-sum on SU(N) hypercharge ≡ 1 ∀ N → chain IS load-bearing structural; SU(2) τ-kernel = 2π, SU(4) τ-kernel = 9π.
- IF Cartan-rational-sum on SU(N) hypercharge depends on N → chain is SU(3)-specific coincidence; SU(2) and SU(4) τ-kernels deviate from `(N−1)(N+2)/2 · π`.

Within the W6a working paper, the SU(N) τ-kernel computation is **not performed**. The §W6a-51 derivation handles only SU(3); the §W6a-52 handles τ=0 baselines for SU(2)/SU(3)/SU(4) but does NOT extend to the τ-kernel computation. Thus the LOAD-BEARING claim at synthesis line 761 is — at this state of evidence — a STRUCTURAL HYPOTHESIS supported by the §W6a-51 SU(3) factorization but NOT yet cross-validated.

### Result 4 — Is the chain a Level-1↔Level-2 substrate-IS BRIDGE? Conditionally yes

**Result**: at SU(3) the chain ALGEBRAICALLY connects the Level-1 single-τ-slice prefactor to the Level-2 moduli-deformation τ-kernel via Plancherel measure factor; BRIDGE STRUCTURE requires the SU(N) cross-validation to harden to a STAGE-1-CANDIDATE; GEOMETRIC

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (S88 W2-10 promotion):

- §W6a-52 produces the substrate-IS observable at Level 1 (single-τ-slice, τ=0): `(dim+rank)/2 = 5` for SU(3). This is the canonical anchor of the K-graded Peter-Weyl decomposition.
- §W6a-51 produces the substrate-IS observable at Level 2 (moduli-deformation, τ ∈ [0, τ_fold]): `slope_A(τ) = c₀/(1−τ/(5π))` with c₀ = (dim+rank)·SU(3)-half. This is the τ-deformed bulk-Weyl exponent.
- The chain `5π = (dim+rank)/2 · π_Plancherel` is the algebraic identity asserting that the Level-1 invariant `(dim+rank)/2` REAPPEARS as a factor in the Level-2 τ-kernel denominator.

If the SU(N) cross-validation succeeds (Cartan-rational-sum = 1 for all N), the chain is a STRUCTURAL BRIDGE between the two substrate-IS levels at the algebraic-identity layer: the single-τ-slice prefactor LITERALLY divides the moduli-deformation kernel. This is an algebra-INVARIANT identity surviving the K-counter MANDATORY-at-K=3 discipline; it lifts §W6a-52's role from "auxiliary prefactor justification" to "Level-1 component of a Level-1↔Level-2 bridge."

If the SU(N) cross-validation fails (Cartan-rational-sum ≠ 1 for some N), the chain is local to SU(3): the integer 5 appears in both gates because BOTH gates exploit the same SU(3) Cartan-arithmetic substrate (`|Δ⁺| = 3`, `rank = 2`, `dim = 8`); the algebra-INVARIANT product structure is preserved, but the BRIDGE claim is downgraded: the Level-1 and Level-2 observables share an upstream Cartan-arithmetic SOURCE without a direct multiplicative identity at general N.

The substrate-IS reading (per `phononic-framing.md §"IS Space, Not IN Space"`) is the DIRECTION of the chain — it flows substrate (Cartan-root structure of SU(3)) → Level-1 algebraic invariant (Peter-Weyl direct-sum count `(dim+rank)/2`) → Plancherel-orbit-integration on SU(3)/T → Level-2 τ-kernel coefficient. The substrate is the SU(3) Cartan-root structure; the chain is the algebraic accounting of that structure across the two levels. Inverting (treating the Level-2 numerical anchor as fundamental) is a container-thinking violation.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W6a-51 (`S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION`) [authoritative; not re-adjudicated] | INFO (sign=PASS · magnitude=INFO · regime=VALID) | anchor_residual_A = 5.230238e-05 (in INFO band [1e-9, 1e-3]); regulator_invariance_residual = 0.000e+00; doubling identity exact |
| §W6a-52 (`S88-DIM-PLUS-RANK-OVER-2-PREFACTOR-DERIVATION`) [authoritative; not re-adjudicated] | PASS (sign=PASS · magnitude=PASS · regime=VALID) | formula_residual = 0.000e+00 (Sage-symbolic ℚ[N] identity); SU(2)=2, SU(3)=5, SU(4)=9; OEIS A000096 cross-corpus EXACT |
| Cross-gate chain `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)` (synthesis line 761) [this workshop's structural verdict] | **STAGE-1-CANDIDATE-PENDING-SU(N)-CROSS-VALIDATION** | SU(3) chain numerically exact at machine zero (Σ_α⟨α,Y⟩²/|α|² = 1, Plancherel-π factor); SU(N) cross-validation NOT YET COMPUTED — discriminator is whether Cartan-rational-sum on SU(N) hypercharge ≡ 1 |

The two W6a gate verdicts are authoritative (inherited from the W6a working paper without re-adjudication). The chain itself produces a NEW workshop-internal structural verdict — not a re-adjudication of either gate, but an adjudication of the synthesis line 761 claim that the two gates are ALGEBRAICALLY CHAINED rather than independent.

---

## IV. Structural Implications

### IV.1 What survives the workshop adjudication (functional-independent / structural-permanent)

- **The §W6a-51 closed form `slope_A(τ) = c₀/(1−τ/(5π))` with c₀ ∈ {10, 5} and regulator_invariance_residual = 0.000e+00 (Sage-symbolic exact across zeta/PV/Mellin)**. This is a FUNCTIONAL-INDEPENDENT structural result by my own functional-pluralism criterion: the closed-form coefficients (10, 5, 5π) are PURE group-theoretic numbers from SU(3) Lie theory + Plancherel measure, and the Sage-symbolic verification across three regulators (zeta, Pauli-Villars, Mellin) returns 0 by the Hardy-Littlewood / Apostol Ch. 11 finite-spectral-triple Dirichlet-series uniqueness theorem (the trace `Tr(D^{-2s})` on a finite spectral triple is a finite sum, so its meromorphic continuation is uniquely determined regardless of regulator scheme). This survives the cutoff vs zeta vs anomaly-derived comparison: the closed form is the SAME in every functional choice. The functional-independence is structural, not numerical accident.
- **The §W6a-52 prefactor identity `(dim+rank)/2 = (N−1)(N+2)/2` for SU(N)**. PASS at machine zero by Sage-symbolic ℚ[N] polynomial identity. This is the algebraic floor below which no further refinement is possible. SU(N) generalization independently corroborated by OEIS A000096. Survives all spectral functional choices because the Peter-Weyl decomposition is a property of the algebra A_K itself, not of any regulator.
- **The algebraic chain `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)` AT SU(3)**. Numerically exact at machine zero (Cartan-rational-sum on SU(3) hypercharge = 1 verified Python; (dim+rank)/2 = 5 from §W6a-52; π_Plancherel from Helgason Ch. X). The algebraic identity is structural at SU(3) BY CONSTRUCTION OF §W6a-51 STEP 5. The PRODUCT is algebra-INVARIANT (corner-cell I × corner-cell I = corner-cell I; passes the algebra-axis orthogonality K-counter MANDATORY-K=3 discipline).

### IV.2 What is scheme-dependent / regulator-dependent (open questions)

- **SU(N) extension of the chain at N ≠ 3**. Not computed in §W6a-51 (which handled only SU(3) Cartan-positive-root sum) nor §W6a-52 (which handled τ=0 baselines but not the τ-kernel computation). Without the SU(N) computation, the LOAD-BEARING structural reading vs the CARTAN-ARITHMETIC coincidence reading cannot be distinguished from SU(3) data alone. The discriminator is sharp and computable.
- **Higher-order O(τ²) Jensen-deformation correction**. The plan §10 Step 8 pre-registered residual estimate `≈4e-9` was structurally optimistic by ~5 OOM; actual residual `5.23e-5` lies in INFO band. This is a Workshop-1-territory question (geometric-resummation vs first-order-linear ansatz adjudication; cross-referenced in seed Workshop 1) and a Workshop-3-territory question (PRU Class 8.3 publication-precision pre-registration boundary; cross-referenced in seed Workshop 3). The chain workshop adjudicated here does NOT depend on resolving the O(τ²) correction question — the chain is an ALGEBRAIC IDENTITY at the closed-form level, not a numerical anchor against the Richardson laboratory-IN image.
- **Whether the SU(N) hypercharge generator's Cartan-rational-sum is structural-1 or N-dependent**. This is the SU(N) cross-validation question. It depends on the choice of "hypercharge analog" generator on SU(N) — a NORMALIZATION question that did not surface in §W6a-51 because SU(3) has a unique hypercharge generator at the second fundamental weight. On SU(N) for N > 3 there are choices; the W6a-51-analog computation must specify the choice (canonical: highest-weight U(1)-direction in the Cartan torus, or per-N-scaled second fundamental weight, or a normalization fixed by the Killing-form pairing). This NORMALIZATION question is itself a structural choice that should be pre-registered in the SU(N) cross-validation gate.

### IV.3 Workshop adjudication on the four sub-questions (a)/(b)/(c)/(d) of seed Workshop 2

- **(a) Level-1 ↔ Level-2 bridge or Cartan-arithmetic coincidence?** The chain IS algebraically a Level-1 ↔ Level-2 connection at SU(3) (the §W6a-52 Level-1 prefactor (dim+rank)/2 LITERALLY divides the §W6a-51 Level-2 τ-kernel denominator). Whether this connection is STRUCTURAL (holds at SU(N) for all N) or LOCAL TO SU(3) (an artifact of the SU(3)-specific hypercharge Cartan-rational-sum equaling 1) is decidable only by SU(N) cross-validation. **Verdict: STRUCTURAL-AT-SU(3); STRUCTURAL-AT-GENERAL-N is hypothesis pending CF-W6A-ADDITIONAL-B.**
- **(b) SU(N) cross-validation predicts what?** Under chain-reading (lizzi): SU(2) τ-kernel = 2π; SU(4) τ-kernel = 9π. Under coincidence-reading (connes): SU(2) and SU(4) τ-kernels factor as `r(N) · (dim+rank)/2 · π` with N-dependent rational `r(N)` not necessarily unity. Cross-validation gate is the discriminator. **Verdict: testable, gate-specifiable, queued.**
- **(c) Algebra-axis classification of the PRODUCT?** Both factors are algebra-INVARIANT (Peter-Weyl direct-sum dimension count + Plancherel/Haar coset volume); the product is algebra-INVARIANT. The chain does NOT introduce algebra-DEPENDENT content (no state-pair functional). **Verdict: algebra-INVARIANT product; corner-cell I × corner-cell I; passes K-counter discipline.**
- **(d) Should chain be a third STAGE-1-CANDIDATE registry entry?** Conditional on SU(N) cross-validation outcome:
  - IF cross-validation PASSES (Cartan-rational-sum on SU(N) ≡ 1) → register the chain as a third STAGE-1-CANDIDATE entry capturing the cross-Level identity beyond the W6a-51 + W6a-52 individual landings; this would be a Pillar-internal structural identity at the K-graded substrate-IS Level-1↔Level-2 layer.
  - IF cross-validation FAILS → revise synthesis line 761 from "load-bearing structural finding" to "shared Cartan-arithmetic origin"; do not register a third entry.
  - IF cross-validation INFO (intermediate) → maintain STAGE-1-CANDIDATE-PENDING tag and queue further cross-validation. **Verdict: deferred-pending-cross-validation; pre-register both branches in the carry-forward.**

### IV.4 Cross-link to seed Workshops 1 and 3 (sister tensions; out of present scope)

- **Workshop 1 (geometric-resummation vs first-order-linear ANSATZ)** — adjudicates whether `slope_A(τ) = c₀/(1−τ/(5π))` is the substrate-IS exact closed form (lizzi reading: residual is high-order multi-root correction) or a first-order ANSATZ that happens to capture the leading O(τ²) correction (connes reading). This is INDEPENDENT of the present cross-gate-chain workshop. The cross-gate chain holds at the FIRST-ORDER closed-form level regardless of whether the geometric resummation is exact-all-order or first-order-only.
- **Workshop 3 (INFO-band substrate-first canonical eligibility for FWD-C1)** — adjudicates PRU Class 8.3 publication-precision pre-registration boundary vs Class-(f) substrate-first canonical-sourcing routing. INDEPENDENT of the chain workshop. The chain workshop's STAGE-1-CANDIDATE-PENDING-SU(N) verdict does not depend on the FWD-C1 unblocking pathway.

The three workshops can land in parallel; their verdicts are non-conflicting on substrate-physics axes.

---

## V. Carry-Forward Computations

V.1. **SU(N) cross-validation of the cross-gate chain `5π = (dim+rank)/2 · π_Plancherel`** (LOAD-BEARING vs COINCIDENCE discriminator)
   - **What**: Compute the W6a-51-analog τ-kernel coefficient on SU(2) and SU(4) by repeating §W6a-51 Step 5 with the SU(N)-analog hypercharge generator. Specifically: (1) fix the SU(N) hypercharge generator `Y_N` (canonical pre-registration: highest-weight U(1)-direction in the Cartan torus normalized so that on SU(3) it reduces to the §W6a-51 Y = (1,1,0)); (2) enumerate positive roots `Δ⁺(SU(N))`; (3) compute Cartan-rational-sum `Σ_{α ∈ Δ⁺(SU(N))} ⟨α, Y_N⟩²/|α|²` symbolically in Sage; (4) apply Wiener-Ikehara orbit-integration on SU(N)/T to introduce the Plancherel/Haar volume factor π (Helgason Ch. X for compact symmetric spaces; the π-factor is normalization-independent across SU(N) so this step is structural); (5) read off τ-kernel coefficient `κ_K^{SU(N)} = (Cartan-rational-sum) · π · 1/(dim(SU(N))+rank(SU(N)))`. Compare against the chain prediction `(dim+rank)(SU(N))/2 · π = (N−1)(N+2)/2 · π`. PASS-LOAD-BEARING iff `κ_K^{SU(N)} · (dim(SU(N))+rank(SU(N))) = π` for both N=2 and N=4 (i.e., Cartan-rational-sum ≡ 1 across N).
   - **Inputs**: §W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e`; §W6a-52 audit_sha256 `05c4cabb0952bb27ef8466f2d068300866347f1b2d1b6e32b49578c1a9d34593`; canonical_constants.py SU(N) Lie-theory pins (`DIM_SU{2,3,4}`, `RANK_SU{2,3,4}`, `DELTA_PLUS_SU{2,3,4}` at lines 274–294 with provenance `S88 W6a-52`); Helgason Ch. X for Plancherel measures on SU(2)/T = S² and SU(4)/T = flag manifold; mcp__sage__ for symbolic Cartan-rational-sum computation; explicit pre-registration of SU(N) hypercharge generator normalization.
   - **Gate**: `S89-W6A-CROSS-GATE-CHAIN-SUN-CROSS-VALIDATION`. PASS-LOAD-BEARING iff `|Cartan-rational-sum(SU(2)) − 1| < 1e-12` AND `|Cartan-rational-sum(SU(4)) − 1| < 1e-12` (Sage-symbolic ℚ-precision). FAIL-COINCIDENCE iff `|Cartan-rational-sum(SU(N)) − 1| ≥ 1e-9` for at least one N ∈ {2, 4}. INFO if intermediate residual in [1e-12, 1e-9] band (Sage-symbolic floor edge).
   - **Effort**: 0.6 wave-equivalents (Cartan-positive-root sum on SU(2) and SU(4) via Sage; Plancherel volume factor π is structural by Helgason Ch. X; Sage-symbolic by structure; minor coordination overhead for SU(N) hypercharge normalization pre-registration).

V.2. **Stage-1 conditional landing of cross-gate chain `5π = (dim+rank)/2 · π_Plancherel` as third STAGE-1-CANDIDATE registry entry** (CONDITIONAL on V.1 PASS-LOAD-BEARING)
   - **What**: Register a new §VII.{next-free-letter} STAGE-1-CANDIDATE registry entry at `sessions/permanent-results-registry.md` capturing the cross-Level chain identity `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)` as a substrate-IS Level-1↔Level-2 bridge separate from W6a-51 STAGE-1-CANDIDATE for the closed form and W6a-52 STAGE-1-CANDIDATE for the prefactor. Entry text declares: (1) Level-1 substrate-IS observable = `(dim+rank)/2` from W6a-52; (2) Level-2 substrate-IS observable = τ-kernel coefficient from W6a-51; (3) bridge map = Plancherel/Haar orbit-integration on SU(3)/T; (4) algebraic envelope = Sage-symbolic ℚ-exact at SU(3); (5) empirical anchor = SU(N) cross-validation at N ∈ {2, 4} from V.1.
   - **Inputs**: V.1 verdict file with PASS-LOAD-BEARING status; W6a synthesis line 761 text; phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels" Level-1/Level-2 partition (S88 W2-10 promotion); cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter" MANDATORY-K=3 (corner-cell declaration is corner-I × corner-I = corner-I, algebra-INVARIANT product); registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY" (V1 = §W6a-52 PASS Peter-Weyl; C1 = §W6a-51 INFO closed form; sequential V+C chain).
   - **Gate**: `S89-W6A-CROSS-GATE-CHAIN-STAGE-1-LANDING` with mack-cosmic-bridge sole-writer registry edit per `feedback_mack-bridge-role.md`. PASS iff registry entry text contains all 5 anatomy elements + 3-level-ladder declaration + SOURCE-DOUBLE-CITE-CO-PRIMARY structure cite + cross-link to V.1 verdict + STAGE-1-CANDIDATE tag with cross-Level Bridge characterization. CONDITIONAL execution: gate dispatches only if V.1 returns PASS-LOAD-BEARING.
   - **Effort**: 0.3 wave-equivalents (mack-cosmic-bridge single-row write per registry-landing.md SOURCE-DOUBLE-CITE-CO-PRIMARY structure; V.1 already supplies the load-bearing structural argument).

V.3. **Synthesis text revision** (CONDITIONAL on V.1 FAIL-COINCIDENCE)
   - **What**: Edit the W6a working-paper synthesis line 761 from "the two gates are not independent but ALGEBRAICALLY CHAINED through the Plancherel-measure factor π. This cross-gate consistency is the load-bearing structural finding of W6a." to "the two gates share a common upstream Cartan-arithmetic origin (the SU(3) Cartan-root structure with `|Δ⁺| = 3` and `rank = 2` giving `(dim+rank)/2 = 5` to W6a-52 and a multiplicative factor of 5 to W6a-51's τ-kernel) but are NOT algebraically chained at general N — the chain is local to SU(3). Synthesis line 761 downgraded from 'load-bearing structural finding' to 'shared Cartan-arithmetic origin' per S89-W6A-CROSS-GATE-CHAIN-SUN-CROSS-VALIDATION FAIL-COINCIDENCE outcome." Append explicit citation to V.1 audit_sha256.
   - **Inputs**: V.1 verdict file with FAIL-COINCIDENCE status; W6a working-paper line 761 current text (preserve all surrounding paragraphs unchanged; only the load-bearing claim is edited); the §W6a-52 PASS-machine-zero verdict and §W6a-51 INFO closed form remain authoritative independent of this revision.
   - **Gate**: `S89-W6A-SYNTHESIS-LINE-761-COINCIDENCE-REVISION` with PASS = single-line edit + verdict-file cross-link landed; FAIL = edit incomplete or inconsistent with V.1 outcome. CONDITIONAL execution: gate dispatches only if V.1 returns FAIL-COINCIDENCE.
   - **Effort**: 0.1 wave-equivalents (single-line working-paper edit + verdict-file emission; structurally trivial).

V.4. **PRU Class 8.3 retroactive audit on the plan §10 Step 8 pre-registered residual estimate `≈4e-9`** (cross-link to seed Workshop 3 + CF-W6A-ADDITIONAL-A; orthogonal to the chain workshop)
   - **What**: Audit the plan §10 Step 8 pre-registered residual estimate `≈4e-9` against the substitution-chain-derivable predictions at first-order-linear (`O(τ²) = 1.46e-3`) vs geometric-resummation (`O(τ³) = 1.77e-5`). Verify that `≈4e-9` is NOT structurally recoverable from either branch of the substitution chain — confirming the publication-precision pre-registration was forecast-style rather than substrate-derived. Per `epistemic-discipline.md §"Pre-Registration Completeness" / §"Publication-Precision Pre-Registration" (Class 8.3, MANDATORY at K=4)`, document the structural defect class and route to plan §10 Step 8 revision in S89 plan-w?? plus declare dependency on Workshop-1 adjudication outcome (geometric-resummation-vs-linear-LO).
   - **Inputs**: WP §10 substitution chain Steps 1–8 (full text from working-paper lines 100–197); WP §6 actual residual `5.230238e-05`; canonical Cartan-rational-sum `Σ_α ⟨α,Y⟩²/|α|² = 1` on SU(3); ε = τ_fold/(5π) = 0.012096 (Python-verified); c₀ ∈ {10, 5}; epistemic-discipline.md §"Pre-Registration Completeness" / §"Publication-Precision Pre-Registration" rule text; seed Workshop 1 (geometric-resummation vs first-order-linear ANSATZ) verdict cross-link.
   - **Gate**: `S89-W6A-51-PRE-REG-CLASS-8-3-RETROACTIVE-AUDIT` with PASS criterion = substitution-chain Steps 1–8 SUFFICIENT to derive ANY threshold matching the plan `≈4e-9` value (else FAIL with diagnostic; FAIL routes to plan-§10-Step-8 revision in S89 plan + Workshop-1 dependency declaration in CF-6 `S89-FWD-C1-RETRY-WITH-SLOPE-A-CANONICAL`).
   - **Effort**: 0.2 wave-equivalents (retroactive audit against existing substitution chain; minor structural-derivation overhead to formalize the linear-LO and geometric-resummation predictions; verdict-file emission).

V.5. **τ = 2·τ_fold cross-validation residual scan** (Workshop-1 territory; orthogonal to the chain workshop but highest-leverage discriminator for the geometric-resummation reading)
   - **What**: Compute the closed-form `slope_A(τ) = c₀/(1−τ/(5π))` and the laboratory-IN HKR-bridge image (Richardson `L^{−3}` extrapolation of finite-L bulk-Weyl exponent) at `τ = 2·τ_fold = 0.38`. Workshop-1 reading A predicts residual at 0.38 ≈ `8 × 5.23e-5 = 4.18e-4` (Python-verified geometric-resummation O(τ³) scaling: `(2ε)³/ε³ = 8`); reading B predicts residual ≈ `4 × 5.23e-5 = 2.09e-4` (Python-verified pure-linear O(τ²) scaling: `(2ε)²/ε² = 4`). The discriminator is `actual_residual_at_0.38 / actual_residual_at_0.19`: ratio ≈ 4 supports linear-LO reading; ratio ≈ 8 supports geometric-resummation reading. Verdict feeds Workshop 1 adjudication as substrate-physics discriminator and is orthogonal to the chain workshop's SU(N) cross-validation discriminator.
   - **Inputs**: Closed-form `slope_A(τ) = c₀/(1−τ/(5π))` from §W6a-51 (audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e`); spectrum cache regen at τ = 0.38 at L_max ∈ {10, 11, 12} (analogous to W1b-3 protocol at τ = 0.19; structurally same protocol but at new τ point); Richardson `L^{−3}` extrapolator from S87 W1b-3 (audit_sha256 `e2f924e52689630b…` Conv-B, `237a2d590b05c273…` Conv-A); Python verification of ratio predictions.
   - **Gate**: `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD` with PASS-LINEAR criterion = `|ratio − 4| < 0.5`; PASS-GEOMETRIC criterion = `|ratio − 8| < 1.0`; INFO band = ratio ∈ (5, 7) (intermediate, neither reading clean); FAIL = ratio outside both bands.
   - **Effort**: 1.0 wave-equivalents (spectrum cache regen at new τ point + Richardson extrapolation; structurally same as W1b-3 protocol but at τ = 0.38).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Chain `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)` algebraically valid AT SU(3) by §W6a-51 Step 5 construction (Cartan-rational-sum = 1, Plancherel-π factor) | GEOMETRIC | STRUCTURAL-AT-SU(3) (Python-verified Cartan-sum 0/2+1/2+1/2=1; Sage-symbolic equivalent) | Chain holds at the SU(3) instance unconditionally; the closed-form §W6a-51 derivation explicitly factors κ_K as (Cartan-rational-sum)·π/(dim+rank) |
| 2 | PRODUCT (dim+rank)/2 · π_Plancherel is algebra-INVARIANT (corner-cell I × corner-cell I = corner-cell I per algebra-axis orthogonality K-counter MANDATORY-K=3) | GEOMETRIC | STRUCTURAL (per W6a-52 connes co-sign CC7-A axiom-2 + Helgason Ch. X coset Plancherel) | Chain does NOT trigger OP-PROJ vs STATE-PROJ naming-discipline boundary; potential STAGE-1-CANDIDATE entry can land under bare §VII.{slot} |
| 3 | LOAD-BEARING (lizzi reading) vs COINCIDENCE (connes reading) is undecidable from SU(3) data alone — discriminator is SU(N) cross-validation at N ∈ {2, 4} | GEOMETRIC | STAGE-1-CANDIDATE-PENDING-SU(N)-CROSS-VALIDATION | Synthesis line 761 claim held conditional on V.1; both branches pre-registered (V.2 conditional on PASS-LOAD-BEARING; V.3 conditional on FAIL-COINCIDENCE) |
| 4 | Chain is a Level-1↔Level-2 substrate-IS BRIDGE conditionally — Level-1 prefactor (W6a-52) literally divides Level-2 τ-kernel denominator (W6a-51) at SU(3) | GEOMETRIC | conditional bridge (HARDENS to STAGE-1-CANDIDATE BRIDGE on V.1 PASS; DEMOTES to "shared Cartan-arithmetic origin" on V.1 FAIL) | Lifts §W6a-52's role from "auxiliary prefactor justification" to potential "Level-1 component of cross-Level bridge" pending V.1 |
| 5 | Workshop's adjudication is INDEPENDENT of seed Workshop 1 (geometric-resummation ansatz) and seed Workshop 3 (PRU Class 8.3 publication-precision boundary) | METHODOLOGY | structural-orthogonal | Three workshops can land in parallel; verdicts non-conflicting on substrate-physics axes |
