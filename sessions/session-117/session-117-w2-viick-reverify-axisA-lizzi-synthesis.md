# Session 117 Synthesis: §VII.CK D4 Joint-Clause Blind Stage-2 Re-Verify (Axis-A)

**Date**: 2026-06-28
**Agent**: lizzi-spectral-functional-theorist (lizzi) — Axis-A independent cross-reviewer
**Gate**: CF-S117-VIICK-UNCONDITIONAL-REVERIFY (Axis-A leg)
**Review type**: blind Stage-2 two-agent cross-axis verify (`joint-theorem-promotion.md §"Stage 2"`); deliverable is this synthesis, NO verdict-file line.

**Source Documents (blind-verify whitelist — the ONLY sources read)**:
- `sessions/permanent-results-registry.md §VII.CK` (the registered, post-W2-1-corrigendum entry — the only theorem text read)
- `computations/session-114/s114_yuk_rightreg_connection.npz` (D4 right-reg substrate data — used as cross-check anchor only, NOT as the decisive input; see §"Independence")
- `computations/session-116/s116_gate_verdicts.txt` line 26 (`S116-W2-CK-STAGE2-VERIFY` PASS, audit `63fc7317…`) — Stage-2 precedent anchor only
- my own `MEMORY.md`

**Blind-verify discipline**: I did NOT read the S112/S114/S115/S116 workshop transcripts, the W2-1 reconciliation transcript, the Axis-B reviewer synthesis, or any document authored by {connes, paasch, van-den-dungen, baptista, kaluza-klein}. I did NOT query the knowledge MCP (it would surface forbidden authored/workshop content and void the independence guarantee). The D4 clause is re-derived from first principles on the registered entry; the agreement reported below is structurally independent of the workshop path.

---

## Verdict

**D4 JOINT CLAUSE: PASS.**

The clause under audit — *"the right-handed-neutrino [generation-leg] membership is fixed by the commutant / Skolem–Noether argument (t(O)=±1 generator membership; leg-membership exclusivity)"* — is **PASS** on its substantive structural content, which I re-derive machine-exact over QQ from first principles. The single exclusion mechanism is **commutant / Skolem–Noether leg-membership**, and the registry's "t(O)=±1" is correctly the **coset-shift grading, NOT the Z₃ center character** — a reading I confirm blind and independently, corroborating the S116 corrigendum without having read it.

The D4-external conclusion (`CLOSED-EXTERNAL-AS-A-COUPLING`; the genus `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` is COMPLETE as a statement about `A_K`-INTERNAL couplings) **follows rigorously** from the leg-membership identity and is **FUNCTIONAL-INDEPENDENT** (Level-1 substrate-IS structural identity; survives every spectral-functional choice).

**One scrupulous caveat (does NOT downgrade the PASS):** if "t(O)=±1" were read as the **Z₃ center character** of the operator `R_{E_α}`, the parenthetical would be FALSE — I confirm `t(R_X)=0` for **all** su(3)_R generators (Cartan and root). The registered entry already mandates the coset-shift reading, so the clause-as-registered is true; my PASS is on that (correct) reading and explicitly rejects the center-character reading.

---

## I. Session Outcome

The §VII.CK D4 leg-membership joint clause survives an independent blind Axis-A re-derivation. The two load-bearing facts — (1) the right-regular root operator `R_{E_α}` is HS-orthogonal to the entire `A_K`-internal differential calculus `Ω¹_{D_K}(A_K) ⊆ ⊕_{(p,q)} B(V_{(p,q)})⊗1` (leg-membership residual = **1 EXACT**), and (2) every su(3)_R generator carries Z₃ center character **0** (adjoint = (1,1), triality (p−q) mod 3 = 0) so the registry "±1" can only be the coset/slot-shift grading — are both reproduced machine-exact over QQ on an explicit construction built from scratch. The D4-external conclusion is regulator-independent and L_max-independent. **Axis-A verdict: PASS.**

---

## II. Key Results

### II.1 — Leg-membership exclusivity: `R_{E_α}` is fully external to `Ω¹_{D_K}(A_K)`

**Result**: leg-membership residual = **1 EXACT** for the right-regular root operator AND the Cartan operator; scalar control = **0 EXACT**. Classification: **GEOMETRIC** (a property of the substrate spectral triple's tensor-leg structure).

Substrate-first reading. The substrate IS the spectral triple `(A_K, H_K, D_K, γ₉, J)`. By Peter–Weyl the SU(3) fabric decomposes per sector into a tensor product of a **geometric leg** `V_{(p,q)}` and a **multiplicity (generation) leg** `ℂ^{m(p,q)}` carrying the generation index `t = (p−q) mod 3`. The left-regular `A_K` action — and therefore its entire Dirac one-form calculus `Ω¹_{D_K}(A_K) = span{a[D_K,b] : a,b ∈ A_K}` — lands inside `⊕_{(p,q)} B(V_{(p,q)})⊗1`: it is **multiplicity-SCALAR** (acts as identity on the generation leg). This is the D3 closing fact; it is the Skolem–Noether / double-centralizer statement that in `B(V)⊗B(W)` the commutant of `B(V)⊗1` is exactly `1⊗B(W)`.

The D4 candidate is the right-regular SU(3)_R connection `Y_R = Σ_a c_a R_{X_a}`, whose off-diagonal (generation-mixing) handle is the root operator `R_{E_α} = 1⊗E_α^*`. Because `E_α^*` is a root vector — **traceless and non-scalar** (nilpotent, `E_α²=0`) on the generation leg — `R_{E_α}` lies in `1⊗B(W)` but NOT in `1⊗ℂ·1`, hence NOT in `B(V)⊗1 ⊇ Ω¹_{D_K}(A_K)`.

First-principles verification (Sage, exact ring QQ, explicit `V=W=ℂ³` fundamental block; built independently of the npz):

| Operator | leg-membership residual (QQ-exact) | reading |
|:---------|:-----------------------------------|:--------|
| `R_{E_α}` root, `1⊗E_{01}` | **1** | fully external (non-scalar on generation leg) |
| `R_X` Cartan, `1⊗diag(1,−1,0)` | **1** | fully external (traceless ⇒ HS-orthogonal to `B(V)⊗1`) |
| CONTROL scalar, `1⊗I₃` | **0** | internal (the ONLY leg-2 content overlapping `B(V)⊗1` is the scalar/identity) |

The residual is `‖X − Proj_{B(V)⊗1}(X)‖ / ‖X‖`. The HS inner product `⟨A⊗1, 1⊗E_α^*⟩ = Tr(A^†)·Tr(E_α^*) = Tr(A^†)·0 = 0` for **every** `A` — so the projection is identically 0 and the residual is exactly 1, with NO float round-off. The scalar control at residual 0 proves the metric genuinely measures non-scalar-on-leg-2 content rather than trivially returning 1.

This reproduces the registry's "W3-1 residual = 1.000000 EXACT" and the npz `iv_residuals_vals = [1, 1, 1]` across the (1,1)/(1,0)/(0,1) sectors — but my QQ derivation does not consume that npz (§"Independence"). The commutant identity `[L_g, Y_R] = 0` (npz `max_comm_i = 7.25e-17`, machine-zero) is the structural statement `SU(3)_R ⊆ (A_K^{left})'`; my Sage centralizer-dimension check (`dim B(V)⊗1 = 9 = dim 1⊗B(W)` in `M₉ = M₃⊗M₃`) confirms the double-commutant skeleton the leg-membership argument rests on.

### II.2 — The corrigendum's correction: t(R_X)=0 for ALL su(3)_R generators ⇒ "±1" is the coset-shift, not the Z₃ center character

**Result**: every su(3)_R generator has Z₃ center character **0**; the registry "t(O)=±1" is the weight/slot-shift grading. Classification: **PARTICLE** (representation-theoretic content of the generation leg).

This is the spectral-side correction that distinguishes the *correct* mechanism (leg-membership) from the *contested* one (a center-character selection rule). First-principles verification (Sage, cyclotomic field `ℚ(ω)`, `ω³=1`):

- **(a)** all 8 su(3) generators are traceless ⇒ the operator-level center character of any single generator vanishes.
- **(b)** the adjoint is the irrep `(1,1)`; triality `(p−q) mod 3 = 0`.
- **(c)** the center `Z₃ = {ωI}` acts **trivially** on the adjoint: `Ad(ωI)X = (ωI)X(ωI)^{-1} = X` for every generator (scalars commute) — confirmed exact for Cartan AND root generators.
- **(d)** the "±1" is the weight/coset shift: `[H₁, E_α] = α(H₁)·E_α` with `α(H₁) ∈ {+2,−1,+1}` (exact integers) and `E_α` non-scalar/nilpotent (`E_α²=0`). The root operator **shifts the generation slot** by a root; the ±1 indexes that slot permutation, not a Z₃ phase.

Therefore a center-character selection rule of the form "`0 ≠ ±1 (mod 3)` excludes `R_{E_α}`" is **not** available: both an `A_K` one-form and `R_{E_α}` carry Z₃ character 0. The exclusion CANNOT come from triality; it comes from leg-membership (II.1). This is exactly the corrigendum's single-mechanism reconciliation, reproduced blind.

### II.3 — The D4-external conclusion is forced and FUNCTIONAL-INDEPENDENT

**Result**: `R_{E_α} ∉ Ω¹_{D_K}(A_K)` ⇒ the off-diagonal generation-SHAPE handle is admissible only via the external crossed product `A_K ⋊ SU(3)_R` ⇒ D4 = `CLOSED-EXTERNAL-AS-A-COUPLING`; genus complete for `A_K`-internal couplings. Classification: **GEOMETRIC**, FUNCTIONAL-INDEPENDENT.

Spectral-functional sensitivity statement (my distinctive axis). The leg-membership exclusion is computed on the **operators themselves** — the differential calculus `Ω¹_{D_K}(A_K)` and the commutant `1⊗B(W)` — entirely **before** any spectral functional `Tr f(D_K/Λ)` is applied. It depends on the algebra/representation and the off-diagonal tensor-leg structure of `D_K`, not on the weighting of any spectral moment. Consequently it is invariant across the cutoff / zeta / anomaly-derived family: there is no choice of `f` (and no choice between `S_cutoff = Tr f(D²/Λ²)` and `S_ζ = ζ_D(0)`) that can move `R_{E_α}` into `B(V)⊗1`. In my three-layer language this is a **Level-1** (zeta-L1) substrate-IS structural identity — the strongest classification — and it holds identically at every L_max (per-block algebraic identity, no `c_continuum` to converge to; Level-2 NON-BINDING / structurally-exact, consistent with the registry's intra-pillar obstruction-theorem anatomy).

---

## III. Gate Verdicts

| Clause | Axis-A Verdict | Decisive number (QQ-exact) |
|:-------|:---------------|:---------------------------|
| D4 leg-membership exclusivity (`R_{E_α} ∉ Ω¹_{D_K}(A_K)`) | **PASS** | residual = 1 (root & Cartan); control = 0 |
| D4 commutant / Skolem–Noether mechanism (`SU(3)_R ⊆ (A_K^{left})'`) | **PASS** | `[L,R]=0` (npz 7.25e-17); centralizer dim 9 = 9 |
| D4 single-mechanism reconciliation ("±1" = coset-shift, not Z₃ char) | **PASS** | `t(R_X)=0 ∀` gens; adjoint triality 0; `[H,E_α]=±n·E_α` |
| D4 conclusion (`CLOSED-EXTERNAL-AS-A-COUPLING`, genus complete) | **PASS** | follows from the above; FUNCTIONAL-INDEPENDENT |
| **D4 JOINT CLAUSE (composite)** | **PASS** | center-character reading rejected; leg-membership reading affirmed |

---

## IV. Structural Implications

- **The unconditional-flip input is clean from Axis-A.** The S116 corrigendum's mechanism (leg-membership, single) is reproduced by an independent blind re-derivation; the contested center-character mechanism is independently rejected (`t=0` for all generators). My Axis-A leg of the disjoint-pair re-verify is PASS on all four sub-clauses. The actual STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL flip is gated on the PASS-AND with Axis-B (volovik) and is the orchestrator's call — I do not re-adjudicate the source verdicts here.
- **What is structural vs scheme-dependent.** The D4 leg-membership exclusion is FUNCTIONAL-INDEPENDENT (structural — a wall of the solution space, regulator- and L_max-invariant). The *physical realization* of the external handle (the crossed-product texture, CP phase, and any Yukawa/PMNS shape that rides on it) is a SEPARATE, scheme- and parameter-dependent question — the registry already routes the lepton-PMNS texture as UNDER-DETERMINED (S116-W2-LEPTON-PMNS-TEXTURE FAIL) and forwards `R = Δm²₃₂/Δm²₂₁` to CF-S117-LEPTON-SEESAW-R-CHANNEL. My PASS scopes ONLY to the leg-membership wall, NOT to the external coupling's observable texture.
- **Substrate direction preserved.** `D_K` tensor-leg geometry (geometric leg ⊕ generation leg) → `A_K` calculus is multiplicity-scalar (leg-membership) → the right-regular generation-mixing handle is external → the fermion-mass SHAPE texture is an external coupling, never an intrinsic `A_K`-internal one-form. The arrow is never inverted (`phononic-framing.md §"IS Space, Not IN Space"`).

## Independence (substrate-input orthogonality)

My decisive computation is the from-scratch Sage QQ construction in §II.1–II.2 (explicit `M₃⊗M₃` leg tensors and the `ℚ(ω)` adjoint-triality checks). It does **not** load `s114_yuk_rightreg_connection.npz`; the npz is cited only as a corroborating cross-check anchor and agreed (`[1,1,1]`, `7.25e-17`). The Axis-A decisive input is therefore orthogonal to the W3-1 substrate data, satisfying the `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` ceiling for the procedural-floor independence guarantee.

---

## V. Carry-Forward Computations

V.1. Axis-B PASS-AND closeout for the unconditional flip
   - **What**: combine this Axis-A PASS with the Axis-B (volovik) blind synthesis; if both PASS the D4 joint clause, flip §VII.CK STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL and retire the D4-open scope qualifier.
   - **Inputs**: this synthesis; `session-117-w2-viick-reverify-axisB-*-synthesis.md`; `joint-theorem-promotion.md §"Stage 3"`.
   - **Gate**: CF-S117-VIICK-UNCONDITIONAL-REVERIFY composite (PASS-AND of both blind axes) → registry tag-flip.
   - **Effort**: orchestrator closeout, <1 agent session (no new compute).

V.2. Scope-token hygiene on the retained "t(O)=±1" text (if flip lands)
   - **What**: on the unconditional flip, ensure the permanent entry carries the coset-shift reading INSIDE the citation token (per `regulator-pin-discipline.md §"Channel-Scope Suffix Discipline"`), so a future reader cannot regenerate the center-character mis-reading from a bare "t(O)=±1".
   - **Inputs**: §VII.CK registered text; the corrigendum companion row (s116 line 27).
   - **Gate**: registry-hygiene patch (mack-cosmic-bridge / designated writer); artifact-existence-with-content.
   - **Effort**: 1 designated-writer patch, <1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `R_{E_α}` leg-membership residual = 1 EXACT (root & Cartan); control = 0 | GEOMETRIC | PASS | `R_{E_α} ∉ Ω¹_{D_K}(A_K)`; D4 external |
| 2 | `t(R_X)=0 ∀` su(3)_R gens; adjoint (1,1) triality 0; center acts trivially | PARTICLE | PASS | "±1" = coset-shift, NOT Z₃ char; center-char mechanism rejected |
| 3 | single mechanism = commutant / Skolem–Noether leg-membership | GEOMETRIC | PASS | corrigendum reproduced blind |
| 4 | D4 = CLOSED-EXTERNAL-AS-A-COUPLING; genus complete (A_K-internal) | GEOMETRIC | PASS | FUNCTIONAL-INDEPENDENT (Level-1, regulator/L_max-invariant) |
| 5 | **D4 JOINT CLAUSE (composite)** | GEOMETRIC | **PASS** | Axis-A input to the unconditional flip is clean |
