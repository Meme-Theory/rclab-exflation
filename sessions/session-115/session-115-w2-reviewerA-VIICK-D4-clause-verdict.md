# Session 115 Wave 2 — §VII.CK D4-external clause: Axis-A BLIND cross-axis verdict (spectral-geometer)

**Date**: 2026-06-24
**Agent**: spectral-geometer (Axis-A — the Ω¹-membership / center-character selection-rule leg)
**Gate**: `S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (Stage-2 two-agent blind cross-axis verify of the §VII.CK D4-external JOINT clause)
**Blindness attestation**: I read ONLY the registered §VII.CK entry (`sessions/permanent-results-registry.md` body block + Four-door table D4 row + the D4-disposition annotation, lines ~22422–22460), the permanent-anchor lines 21118–21124 (Skolem–Noether leg-membership), and the knowledge-MCP entries for `proven_384` / §VII.BL. I did **NOT** open the S114 W-2 workshop transcript `sessions/session-114/workshops/w-2-d4-rightreg-su3r-admissibility.md`, nor the Axis-B reviewer deliverable, nor any agent's transcript. The selection rule below is re-derived from first principles (Z₃ center character + CG admissibility), not restated.

**Source Documents**:
- `sessions/permanent-results-registry.md` — registered §VII.CK entry (D1–D3 STAGE-3-PERMANENT; D4-disposition annotation), permanent anchors lines 21118–21124
- knowledge MCP — `proven_384` (`t(p,q)=(p−q) mod 3`); §VII.BL multiplicity-scalar / Skolem–Noether commutant mechanism; `connes-r2.md` PROVEN findings ("the multiplicity leg is `R_X`-active (right-regular)")
- Sage MCP (sagecell) — first-principles symbolic re-derivation of triality additivity + center character of su(3) generators + commutant/leg-membership exclusion

---

## I. Session Outcome

The D4-external **conclusion is TRUE and rigorously confirmed, A_F-independently**: the right-regular root operator `R_{E_α}` is genuinely OUTSIDE `Ω¹_{D_K}(A_K)`, so the SU(3)_R fermion coupling is external — admissible only via the crossed product `A_K ⋊ SU(3)_R` (Kasparov external product) — and the §VII.CK homogeneity-obstruction genus `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` IS COMPLETE as a statement about A_K-INTERNAL couplings. **JOINT clause: PASS** (via the commutant / leg-membership mechanism, which the registry also cites).

**However**, the *specific sub-mechanism the registry's D4 annotation states* — `t(R_{E_α}) = ±1 ≠ 0` via the Z₃ center-character selection rule — is **NOT correct as written**. Every su(3) Lie-algebra generator (Cartan AND root) lives in the adjoint `8 = (1,1)`, which has center character `t = 0`; equivalently, the center `z = ω·I` is a SCALAR and commutes with every generator, so `t(R_X) = 0` for ALL su(3)_R generators. The roots live in the ROOT lattice = kernel of the center character (`t(α₁)=t(α₂)=t(α₁+α₂)=0`). The `±1` the annotation cites is a **conflation of two distinct gradings** on the multiplicity leg: the Z₃ *center-character* grading (where roots carry `0`) vs. the *generation-slot-permutation* action (where off-diagonal roots DO move between the 3 generation slots). The correct exclusion mechanism is the **commutant / leg-membership** argument (the right action is the commutant of the left `A_K` action; left one-forms land in `⊕ B(V_{(p,q)}) ⊗ 1`, the right-root operator is `1 ⊗ E_α^*` which is non-scalar on the multiplicity factor and therefore NOT in `B(V) ⊗ 1`). **Axis-A leg as framed around the selection rule: INFO** — conclusion correct, stated selection-rule reason incorrect, correct reason supplied (mandatory corrigendum below).

---

## II. Key Results

### Axis-A leg — Ω¹-membership / t(O)=±1≠0 selection rule

**Result**: GEOMETRIC. Verdict on the leg **as literally framed (selection-rule justification): INFO**. The *conclusion* of the leg (`R_{E_α} ∉ Ω¹_{D_K}(A_K)`, A_F-independent) is TRUE; the *stated mechanism* (`t(R_{E_α})=±1`) is mis-stated. Correct mechanism = commutant/leg-membership.

I re-derived the chain the leg asks me to verify, step by step, from first principles. I report what survives and what does not.

#### Step 1 — the Z₃ center character is the triality `t(p,q)=(p−q) mod 3` (re-derived, confirmed)

The SU(3) center is `Z₃ = {I, ωI, ω²I}`, `ω = exp(2πi/3)`. The center element `z = ωI` acts on an irrep of highest weight `(p,q)` by the scalar `ω^{(p−q) mod 3}` (it is `ω^{n}` where `n` is the number of boxes mod 3 = `(p+2q) ≡ (p−q) mod 3`). Sage check on standard irreps:

| irrep | `(p,q)` | `t = (p−q) mod 3` |
|:------|:--------|:------------------|
| `3` | `(1,0)` | 1 |
| `3̄` | `(0,1)` | 2 |
| `8` (adjoint) | `(1,1)` | **0** |
| `1` (singlet) | `(0,0)` | 0 |
| `6` | `(2,0)` | 2 |
| `10` | `(3,0)` | 0 |
| `15` | `(2,1)` | 1 |

This matches `proven_384` exactly. **PASS.**

#### Step 2 — the CG selection rule (re-derived from first principles, confirmed)

Claim to verify: a nonzero inter-state matrix element `⟨ψ_a| O |ψ_b⟩` requires `t(a) ≡ t(b) + t(O) (mod 3)`; a FAILED congruence proves the element `0` EXACTLY.

First-principles derivation: triality is the value of the GROUP element `z = ωI` (a Z₃ center generator). On a tensor product `z` acts as `z ⊗ z`, i.e. by the PRODUCT of scalars `ω^{t₁}·ω^{t₂} = ω^{t₁+t₂}`. Every irreducible summand of `(p₁,q₁) ⊗ (p₂,q₂)` is an invariant subspace of `z ⊗ z`, hence carries the SAME center scalar `ω^{(t₁+t₂) mod 3}`. Therefore **triality is ADDITIVE under CG decomposition**. Sage verification against explicit SU(3) Clebsch–Gordan series (`WeylCharacterRing("A2")`):

| product | expected `t` | summand `t`-set | additive |
|:--------|:-------------|:----------------|:---------|
| `3 ⊗ 3` | `1+1=2` | `{(0,1):2, (2,0):2}` | ✓ |
| `3 ⊗ 3̄` | `1+2=0` | `{(0,0):0, (1,1):0}` | ✓ |
| `8 ⊗ 8` | `0+0=0` | `{(0,0),(0,3),(1,1),(2,2),(3,0)}` all `t=0` | ✓ |
| `3 ⊗ 8` | `1+0=1` | `{(0,2):1, (1,0):1, (2,1):1}` | ✓ |
| `10 ⊗ 3̄` | `0+2=2` | `{(2,0):2, (3,1):2}` | ✓ |
| `6 ⊗ 3̄` | `2+2=1` | `{(1,0):1, (2,1):1}` | ✓ |

Additivity holds on every tested product. The selection rule (trivial rep occurs in `a* ⊗ O ⊗ b` only if `t(a*)+t(O)+t(b) ≡ 0`, i.e. `t(a) ≡ t(b)+t(O)`) is therefore SOUND as a necessary condition. **PASS as a tool.**

#### Step 3 — `t(O)` for `O = R_{E_α}` (the DECISIVE step — where the registry chain BREAKS)

The leg asserts `t(R_{E_α}) = ±1`. I tested this directly. There are two candidate computations, and the result is unambiguous:

**(3a) Center character of a su(3) generator.** A root operator `E_α` is a weight vector of the ADJOINT rep `8 = (1,1)`, which has center character `t = (1−1) mod 3 = 0`. More fundamentally: the center `z = ωI` is a SCALAR matrix; for ANY Lie-algebra generator `X`, `z X z⁻¹ = (ωI) X (ω⁻¹I) = ω·ω⁻¹ X = X`. So every su(3) generator — Cartan H₁,H₂ AND every root E_{±α₁}, E_{±α₂}, E_{±θ} — is fixed by center conjugation, i.e. carries center character `ω⁰`. Hence

> **`t(R_X) = 0` for ALL su(3)_R generators, roots INCLUDED.**

**(3b) Triality SHIFT a root induces on a weight.** As a map on weights `μ → μ + α`, a root operator shifts the center character by `t(α)`, where `α` is read in the weight lattice. Expressing the simple roots in the fundamental-weight (ω) basis via the A₂ Cartan matrix `C = [[2,−1],[−1,2]]`: `α₁ = (2,−1)`, `α₂ = (−1,2)`, `θ = α₁+α₂ = (1,1)`. Then `t(α₁) = (2−(−1)) mod 3 = 0`, `t(α₂) = (−1−2) mod 3 = 0`, `t(θ) = (1−1) mod 3 = 0`. The roots live in the ROOT lattice, which is precisely the **kernel** of the center character. A root operator therefore maps a `t = k` weight vector to another `t = k` weight vector — it PRESERVES the triality grading. Acting within a single irrep `V_{(p,q)}`, `E_α` keeps the triality fixed at `t(p,q)`.

Both routes give the same answer: **`t(R_{E_α}) = 0`, NOT `±1`.** The registry's `t(O)=±1≠0` selection-rule chain is therefore **false as written**, and the substitution `0 ≠ ±1 (mod 3)` it advertises does not apply to `R_{E_α}` (whose center charge is `0`, not `±1`).

**Why the registry reached `±1` — the conflation, diagnosed.** The off-diagonal su(3)_R ROOT operators DO connect DIFFERENT generation slots: realizing the three generations as the three weights `|1⟩,|2⟩,|3⟩` of a fundamental multiplicity factor `V*`, the Cartan operators H₁,H₂ are generation-DIAGONAL while E_{α₁} (|2⟩→|1⟩), E_{α₂} (|3⟩→|2⟩), E_θ (|3⟩→|1⟩) are generation-OFF-DIAGONAL (Sage-confirmed). This generation-slot-permutation action is the TRUE physical content of "`R_{E_α}` is the off-diagonal SHAPE handle." But the generation-SLOT index (which of the 3 weights inside one fundamental factor) is a DIFFERENT grading from the Z₃ CENTER character (the `(p−q) mod 3` triality of the SECTOR). The "`±1`" describes the slot-shift (`|2⟩↔|1⟩` is a "neighbor" move), NOT a center charge. The registry's D4 narration overloaded the symbol `t` across these two gradings. The center-character selection rule does NOT exclude `R_{E_α}` — because, by center charge, `R_{E_α}` is coset-PRESERVING (`t(O)=0`), exactly as the S114 W3-1 prior-state INFO ("generation-DIAGONAL, `t(O)=0`") found before the annotation re-narrated it.

**Leg verdict (literal selection-rule framing): INFO.** The membership conclusion is correct; the selection-rule mechanism stated for it is not. The correct mechanism is supplied in §III below.

#### Step 4 — the CORRECT exclusion mechanism (commutant / leg-membership; supplied)

Why `R_{E_α} ∉ Ω¹_{D_K}(A_K)` is nonetheless TRUE, A_F-independently:

The substrate Hilbert space is the regular representation. By Peter–Weyl, `H_K ⊃ L²(SU(3)) = ⊕_{(p,q)} V_{(p,q)} ⊗ V*_{(p,q)}`:
- the LEFT-regular action `L_g` (and hence `A_K`'s left action and every commutator `[D_K, a]`, `a ∈ A_K`) acts on the FIRST factor `V_{(p,q)}` and is `⊗ 1` (SCALAR) on the multiplicity factor `V*_{(p,q)}` — this is the D3 / Skolem–Noether leg-membership fact (registry lines 21120/21155): `Ω¹_{D_K}(A_K) ⊆ ⊕ B(V_{(p,q)}) ⊗ 1`.
- the RIGHT-regular su(3)_R root operator acts on the SECOND factor as `1 ⊗ E_α^*`, which is NON-scalar on the multiplicity leg.

A non-scalar `1 ⊗ E_α^*` cannot lie in `B(V) ⊗ 1`. Explicit Sage commutant test on the fundamental sector `V ⊗ V* = ℂ³ ⊗ ℂ³`: pick `Y = diag(1,2,3)` on the multiplicity leg with `[Y, E_{α₁}] ≠ 0`; then `[1⊗E_{α₁}, 1⊗Y] ≠ 0`, whereas every genuine `M ⊗ 1` element satisfies `[M⊗1, 1⊗Y] = 0`. Hence `1 ⊗ E_α^* ∉ B(V) ⊗ 1 = ` the home of every left-`A_K` one-form. Therefore `R_{E_α} ∉ Ω¹_{D_K}(A_K)`. **∎**

This is the §VII.BL **commutant theorem** ("no algebra's differential calculus reaches its own commutant non-scalarly"): `SU(3)_R` is the commutant of `A_K`'s left-regular action (`[L_g, R_h] = 0`), and the left calculus is scalar on the leg the right action moves non-scalarly. The exclusion is manifestly **A_F-INDEPENDENT** — it is a statement about which tensor LEG operators occupy, with no reference to the finite algebra `A_F`. It holds at EVERY `L_max` (per-sector, identically). The framework's own R2 work (`connes-r2.md`, PROVEN) already records exactly this: "the multiplicity leg is `R_X`-active (right-regular)" and "Paasch's reason (`R_X`-inert ⇒ homogeneity-alone-forbids) is provably wrong; the correct wall is" the commutant/membership one — independent corroboration of this Axis-A finding.

> **Axis-A leg verdict: `A_leg_verdict: INFO`** — the membership CONCLUSION (`R_{E_α} ∉ Ω¹_{D_K}(A_K)`, A_F-independent) is rigorously TRUE, but via the COMMUTANT / leg-membership mechanism, NOT the `t(O)=±1≠0` center-character selection rule the leg is framed around. `t(R_{E_α}) = 0`, not `±1`. The registry's stated selection-rule justification requires the corrigendum in §III.

---

### D4-external JOINT clause

**Clause (verbatim target)**: "The right-regular `R_{E_α}` SHAPE handle is external-as-a-coupling — admissible only via `A_K ⋊ SU(3)_R`, outside `Ω¹_{D_K}(A_K)` by `t(O)=±1≠0` — so the §VII.CK homogeneity-obstruction genus is COMPLETE as a statement about A_K-INTERNAL couplings."

**Result**: GEOMETRIC. Verdict: **`JOINT_verdict: PASS`** (substantive structural content), **with a mandatory corrigendum** (the embedded `t(O)=±1` mechanism citation is replaced by the commutant/leg-membership mechanism).

I decompose the clause into its substantive structural assertions and verdict each:

1. **`R_{E_α}` is outside `Ω¹_{D_K}(A_K)`** — **TRUE** (§II Step 4, commutant/leg-membership, Sage-confirmed).
2. **It is admissible only via the crossed product `A_K ⋊ SU(3)_R`** — **TRUE**. `SU(3)_R` is the commutant of the left-`A_K` action, a genuine substrate isometry; an operator on a module that is NOT in the algebra's own differential calculus but IS in its commutant is adjoined precisely by the crossed product (≡ Kasparov external product). The right-regular connection is external-as-a-COUPLING (an overall `g_R` with the texture/phase forced around it), not external-as-the-whole-observable (the M_KK-magnitude case). Correct.
3. **A_F-independence** — **TRUE**. The commutant/leg-membership exclusion never references `A_F`; it is a tensor-leg statement holding at every `L_max`.
4. **The genus is COMPLETE as a statement about A_K-INTERNAL couplings** — **TRUE**. D1 (γ₉-odd trace ≡ 0), D2 (γ₉-even moment ⇒ C₂ only), D3 (A_K-cocycle generation-blind), and D4 (right-regular handle = the unique multiplicity-active candidate, and it is OUTSIDE the A_K-internal calculus) together exhaust the four-door disjunction. D4 was the ONE candidate with non-scalar leg content (it escapes the D1/D2/D3 walls precisely because it is `R_X`-active); showing it is external closes the last door. The genus `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` is COMPLETE for A_K-INTERNAL couplings.

5. **"by `t(O)=±1≠0`"** — **FALSE as written** (the only defective conjunct). `t(R_{E_α}) = 0`. This parenthetical mechanism citation must be corrected to the commutant/leg-membership mechanism (§III corrigendum). It is NOT load-bearing for the conclusion: removing the false `t(O)=±1` clause and substituting the (correct, A_F-independent, L_max-invariant) commutant argument leaves every substantive assertion (1)–(4) intact.

The substantive structural content of the JOINT clause — external-as-a-coupling, crossed-product home, A_F-independence, genus completeness — is rigorously TRUE. Only the embedded mechanism label is wrong, and it is replaceable without weakening the conclusion. Per the substrate-IS framing: `SU(3)_R` IS the substrate's own commutant (a real isometry, not an external field added IN a container); only the COUPLING is the external crossed-product image. Direction preserved: `D_K eigenvalues + Peter–Weyl leg structure → left-A_K calculus is multiplicity-scalar (D3) → R_{E_α} non-scalar on the multiplicity leg → R_{E_α} ∉ Ω¹_{D_K}(A_K) → external A_K ⋊ SU(3)_R`. Never inverted.

> **JOINT clause verdict: `JOINT_verdict: PASS`** (with mandatory corrigendum) — the D4-external conclusion and genus-completeness hold rigorously and A_F-independently via the commutant/leg-membership mechanism. The `t(O)=±1≠0` selection-rule mechanism cited in the clause is mis-stated (correct value `t(R_{E_α})=0`) and is replaced by the commutant argument; the substitution does not weaken the conclusion.

---

## III. Mandatory corrigendum to the §VII.CK D4-disposition annotation

The registered §VII.CK D4 annotation (and the Four-door D4 row) states the exclusion follows from "the `t(O)=±1≠0` center-character selection rule (the cross-generation handle SHIFTS triality cosets, `t(O)=±1`; every `A_K` one-form is coset-preserving, `t(O)=0`; `0≠±1 (mod 3)`)". This is **not correct** and should be corrected as follows:

- **Replace** the mechanism from "center-character selection rule with `t(R_{E_α})=±1`" **to** "the **commutant / Skolem–Noether leg-membership** mechanism": `Ω¹_{D_K}(A_K) ⊆ ⊕ B(V_{(p,q)}) ⊗ 1` (left calculus is scalar on the multiplicity leg, D3); `R_{E_α} = 1 ⊗ E_α^*` is non-scalar on that leg (right-regular = the commutant of the left action); a non-scalar `1 ⊗ E_α^*` is not in `B(V) ⊗ 1`; therefore `R_{E_α} ∉ Ω¹_{D_K}(A_K)`, A_F-independently, at every `L_max`.
- **Reason**: `t(R_X) = 0` for ALL su(3)_R generators (Cartan AND root), because every Lie-algebra generator sits in the center-blind adjoint `8 = (1,1)` (equivalently, the center `ωI` is scalar and commutes with every generator); the roots live in the root lattice = ker of the center character. There is no `t(O)=±1` to invoke.
- **The legitimate `±1`-flavored statement that IS true** (and should be stated as such, on the correct grading): the off-diagonal su(3)_R ROOT operators are generation-SLOT-OFF-DIAGONAL (they permute the 3 generation slots within a fundamental multiplicity factor), while the Cartan su(3)_R operators are generation-slot-diagonal. This generation-slot-permutation is what makes `R_{E_α}` the "off-diagonal SHAPE handle" — but it is the slot-index grading, NOT the Z₃ center-character grading, and it is NOT the reason `R_{E_α}` is outside `Ω¹` (that reason is the commutant/leg-membership argument).
- **W3-1 residual = 1.000000 readback**: the numerical residual=1 (the Cartan `Y_R` outside the left A_K-calculus) is consistent with — and is the numerical shadow of — the COMMUTANT mechanism, not the center-character one. It measures "outside the left calculus," i.e. leg-membership, exactly as the corrigendum states. (The W3-1 `t(O)=0` finding for the CARTAN `Y_R` is, in fact, the SAME `t(O)=0` that holds for the ROOT `R_{E_α}` — both are center-charge-0; the distinction W3-1 missed and the annotation over-corrected is the slot-permutation grading, not a center charge.)

This corrigendum is GEOMETRIC and in-session-correctable (a prose/mechanism-label fix on the registered §VII.CK D4 annotation + Four-door D4 row, sole writer per `feedback_mack-bridge-role.md`). It does NOT down-tag the §VII.CK structural status: the D4-external CONCLUSION and the genus completeness are correct, so the STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL flip is supported on the substance, PROVIDED the mechanism citation is corrected. The substrate-first direction is unchanged.

---

## IV. Structural Implications

- **The §VII.CK genus IS complete for A_K-INTERNAL couplings** (D1–D4 closed), and the closure is rigorous A_F-independently. The four-door disjunction is exhaustive: D1/D2/D3 close the A_K-built/Casimir/γ₉ classes; D4 closes the unique multiplicity-active candidate (right-regular) by showing it lives in the commutant, outside the algebra's own calculus. The fermion-mass SHAPE handle is external — the same external `ε_LX` / crossed-product channel that carries the §VII.BL magnitude.
- **The exclusion mechanism is the commutant, not a selection rule.** This is the substantive structural correction: the right wall is "no algebra's differential calculus reaches its own commutant non-scalarly" (§VII.BL), realized here on the Peter–Weyl tensor-leg split. The center-character selection rule (real and powerful — it is the §VII.BX CKM-texture / §VII.BL anchor) is the WRONG tool for D4, because su(3)_R generators are center-blind. Using the correct tool strengthens the result: the commutant exclusion is cleaner (a pure leg-membership statement) and more obviously A_F-independent and L_max-invariant than the (defective) selection-rule narration.
- **No new corridor opens.** The named external corridor (the crossed-product right-regular connection with its forced Z₃-circulant texture) is unchanged; its observable residue (CKM/PMNS forced texture) is tested by the separate `CF-S115-LEPTON-PMNS-FORCED-TEXTURE`, not by this genus flip.
- **Independence of this Axis-A finding.** This verdict was reached blind (no workshop transcript, no Axis-B coordination) and from first principles (Z₃ center character + CG admissibility + Peter–Weyl leg structure + explicit Sage commutant test). It happens to REPRODUCE the framework's own prior R2 PROVEN finding ("the multiplicity leg is `R_X`-active; the correct wall is the commutant one") — structurally independent corroboration of the corrigendum.

---

## V. Carry-Forward Computations

V.1. Correct the §VII.CK D4 mechanism citation (corrigendum landing)
   - **What**: edit the registered §VII.CK D4-disposition annotation + Four-door table D4 row to replace the `t(O)=±1≠0` center-character selection-rule mechanism with the commutant / Skolem–Noether leg-membership mechanism (`Ω¹_{D_K}(A_K) ⊆ ⊕ B(V_{(p,q)})⊗1`; `R_{E_α}=1⊗E_α^*` non-scalar on the multiplicity leg ⇒ ∉ `B(V)⊗1`), stating `t(R_X)=0 ∀ su(3)_R generators` and re-labeling the true `±1`-flavored fact as the generation-SLOT-permutation action (distinct grading). Preserve the substrate-IS direction and the STAGE-3 status.
   - **Inputs**: §VII.CK entry (`sessions/permanent-results-registry.md` ~lines 22439, 22460); §VII.BL commutant theorem; `proven_384`; `connes-r2.md` ("multiplicity leg is `R_X`-active"); this deliverable §III. No new compute (prose/mechanism-label fix).
   - **Gate**: feeds the W2 PASS-AND closeout (`S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`); the closeout MUST encode the corrigendum (the JOINT PASS is conditional on the mechanism being corrected to commutant). Sole writer `mack-cosmic-bridge` per `feedback_mack-bridge-role.md`. In-session fix per `feedback_fix-in-session-never-defer.md` (not a deferred CF if the closeout can apply it this wave).
   - **Effort**: < 1 hour, orchestrator-direct or 1 mack-cosmic-bridge dispatch (designated-writer reviewed patch, NOT a bulk append).

V.2. (Optional) Explicit crossed-product Ω¹ verification at the next Peter–Weyl sector
   - **What**: confirm the commutant/leg-membership exclusion at the (1,1) adjoint and (2,0) sectors (not just the fundamental): build `1 ⊗ E_α^*` and the left-`A_K` calculus image per sector, verify `1⊗E_α^* ∉ ⊕ B(V_{(p,q)})⊗1` and `[1⊗E_α^*, M⊗1]=0`-failure with non-commuting multiplicity-leg probe, across sectors `p+q ≤ 4`.
   - **Inputs**: `dirac_spectrum.py` (irrep builder), Peter–Weyl decomposition; canonical `tau_fold=0.19`. Sage finite-block.
   - **Gate**: new INFO gate `S116-VIICK-D4-COMMUTANT-MULTISECTOR` — PASS iff non-scalar-on-leg confirmed for every sector `p+q ≤ 4` (no numerical threshold; structural existence). Strengthens the corrigendum's L_max-invariance claim numerically.
   - **Effort**: 2–3 hours, 1 agent session (spectral-geometer or connes-ncg-theorist).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `t(p,q)=(p−q) mod 3` is the Z₃ center character; CG triality additivity holds | GEOMETRIC | PASS (re-derived, Sage-confirmed) | `proven_384` confirmed; selection rule sound as a tool |
| 2 | `t(R_{E_α}) = 0`, NOT `±1` (every su(3)_R generator is center-blind; roots in root lattice = ker) | GEOMETRIC | leg-as-framed INFO | registry `t(O)=±1` mechanism is mis-stated; needs corrigendum |
| 3 | `R_{E_α} ∉ Ω¹_{D_K}(A_K)`, A_F-independently, ∀ L_max (commutant/leg-membership; Sage commutant test) | GEOMETRIC | **conclusion TRUE** | the D4-external conclusion holds via the CORRECT mechanism |
| 4 | D4-external JOINT clause (external-as-a-coupling, crossed-product home, genus COMPLETE) | GEOMETRIC | **JOINT PASS** (with corrigendum) | §VII.CK genus complete for A_K-internal couplings; UNCONDITIONAL flip supported on substance |
| 5 | off-diagonal su(3)_R roots are generation-SLOT-permuting (the true `±1`-flavored fact, distinct grading) | GEOMETRIC | INFO | diagnoses the registry conflation; supplies the correct statement |

---

## Machine-readable clause-verdict block

```yaml
gate: S115-VIICK-D4-DISCHARGE-UNCONDITIONAL
axis: A
reviewer: spectral-geometer
blind: true            # workshop transcript NOT read; no Axis-B coordination
A_leg_verdict: INFO    # conclusion (R_{E_a} not in Omega^1, A_F-indep) TRUE; stated t(O)=±1 selection-rule mechanism MIS-STATED (correct t(R_X)=0); correct mechanism = commutant/leg-membership, supplied
JOINT_verdict: PASS    # external-as-a-coupling + crossed-product home + A_F-independence + genus COMPLETE all TRUE via commutant mechanism; the embedded "t(O)=±1" conjunct is the only defective part and is replaceable without weakening the conclusion
corrigendum_required: true   # §VII.CK D4 annotation + Four-door D4 row: replace t(O)=±1 selection rule with commutant/leg-membership mechanism; state t(R_X)=0 ∀ su(3)_R gens; re-label the true ±1 fact as generation-SLOT permutation
t_R_Ealpha: 0          # center character of EVERY su(3)_R generator (Cartan AND root) is 0; roots in root lattice = ker(center char)
exclusion_mechanism: commutant_leg_membership   # Omega^1_{D_K}(A_K) ⊆ ⊕ B(V_(p,q))⊗1 (D3/Skolem-Noether); R_{E_a}=1⊗E_a* non-scalar on multiplicity leg ⇒ ∉ B(V)⊗1
A_F_independent: true
L_max_invariant: true
genus_complete_A_K_internal: true
substitution_chain_0_neq_pm1_applies_to_R_Ealpha: false   # 0≠±1 is true arithmetic but t(R_{E_a})=0, so ±1 is the wrong value; chain does not gate the exclusion
```
