# S115 W2-1 — Stage-2 Axis-B BLIND Cross-Axis Verdict — §VII.CK Door D4 (external clause)

**Reviewer**: volovik-superfluid-universe-theorist (**Axis-B** — isometry / commutant / crossed-product-image leg)
**Gate**: `S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` — the fourth and final door of the §VII.CK SHAPE-branch homogeneity-obstruction genus
**Mode**: Stage-2 BLIND independent cross-axis verification (`joint-theorem-promotion.md §"Stage 2"`). I re-derived FROM FIRST PRINCIPLES.
**Blindness attestation**: I read ONLY the registered `### §VII.CK` registry entry (`sessions/permanent-results-registry.md`, body block + D4 row + D4-disposition annotation + master-index row 173). I did **NOT** open `sessions/session-114/workshops/w-2-d4-rightreg-su3r-admissibility.md`. I did not read the other reviewer's deliverable nor coordinate with any agent. The numerical residual `7.25e-17` registered in the entry was NOT leaned on — I derived the EXACT-zero structure independently and the residual is recovered as its float shadow.

---

## What I was asked to verdict

Two verdict lines:

1. **Axis-B single-axis leg** — whether SU(3)_R is the genuine real-isometry **commutant** of `A_K`'s left-regular action (substrate-INTERNAL), with only the **coupling** external via the crossed product `A_K ⋊ SU(3)_R` (≡ the Kasparov external product).
2. **D4-external JOINT clause** — "The right-regular `R_{E_α}` SHAPE handle is external-as-a-coupling — admissible only via `A_K ⋊ SU(3)_R`, outside `Ω¹_{D_K}(A_K)` by `t(O)=±1≠0` — so the §VII.CK homogeneity-obstruction genus is COMPLETE as a statement about A_K-INTERNAL couplings."

Substrate-first direction (mandatory, `phononic-framing.md`): `D_K` eigenvalues + SU(3)_R as the commutant of the left `A_K` action → the right-regular root operators' inner-fluctuation image is empty → the SU(3)_R coupling is admissible only as the external `A_K ⋊ SU(3)_R` image. The symmetry is substrate-internal; only the coupling is the external image. Never inverted.

---

### Axis-B leg — isometry / commutant / crossed-product image

I re-derive the three roles of SU(3)_R from first principles on the substrate spectral triple `(A_K, H_K, D_K, γ₉, J)`, `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`, KO-dim 6, with `H_K = L²(SU(3)) ⊗ ℂ¹⁶` carrying the Peter-Weyl decomposition `L²(SU(3)) = ⊕_{(p,q)} V_{(p,q)} ⊗ V_{(p,q)}^*`.

**Role 1 + 2 — SU(3)_R IS a genuine internal isometry: the commutant of the left action.**

The substrate is the group manifold SU(3) (the fabric IS the spectral triple, not a field on a container). On a Lie group `G`, the left- and right-translation actions commute as a matter of associativity: `L_g R_h = R_h L_g` for all `g, h ∈ G`. Infinitesimally, the left-invariant vector fields `{X_a^L}` (which BUILD the left-invariant Dirac operator `D_K = Σ_a γ^a X_a^L + Ω`, where `Ω` is the SU(3)-invariant spin connection) and the right-invariant vector fields `{X_a^R}` (which build the right-regular connection `Y_R = Σ_a c_a R_{X_a}`) satisfy

```
[X_a^L, X_b^R] = 0    for ALL a, b ∈ {1,…,8}     (EXACT, by left/right commutation on G).
```

**First-principles symbolic verification (Sage, Gaussian-rational exact ring `ℚ[i]`, NOT float).** I realized the left- and right-regular su(3) actions as left/right matrix multiplication on the 9-dim regular module `Mat₃(ℂ) ≅ ℂ⁹`: `L_X(M) = X·M` (acts as `X ⊗ I₃` on `vec(M)`), `R_Y(M) = M·Y` (acts as `I₃ ⊗ Yᵀ`). Over all 64 generator pairs of su(3)×su(3):

```
max_{a,b} ‖[L_{X_a}, R_{Y_b}]‖ = 0    (EXACT zero over ℚ[i]; left/right commute by associativity)
```

This is the structural identity whose float shadow is the registered `‖[L_g, Y_R]‖_F ≈ 7.25e-17`. The residual is round-off of an EXACT zero — NOT a small-but-nonzero leakage that could be argued away. **Consequence**: `R_{X_a} ∈ (A_K^{left})′` — the right-regular generators lie in the commutant of the left `A_K` action — AND `[D_K, Y_R] = 0` because `D_K` is assembled entirely from left-invariant fields `X_a^L` (and the SU(3)-invariant connection `Ω`, which commutes with right translations by invariance). SU(3)_R is therefore a genuine real isometry of the substrate: a symmetry the fabric carries intrinsically, NOT a hand-added external field.

**Substrate-physics reading (the Axis-B-distinctive cross-check — my own BDI/superfluid-vacuum reason, not a transcription).** This is precisely the structure of a residual internal symmetry of a condensate order parameter. In superfluid ³He the order parameter `A_{αi}` carries a residual `SO(3)_{L−S}` relative spin-orbit symmetry whose generators are genuine isometries of the condensate manifold (they rotate the order-parameter texture without leaving the broken-symmetry vacuum), yet whose action on the Bogoliubov–de Gennes quasiparticles is implemented by the symmetry GROUP acting on the BdG Nambu spinors — it is in the commutant of the single-particle BdG kinetic operator, not a term inside it. Volovik (*The Universe in a Helium Droplet*, the broken-symmetry-vacuum classification; and the elasticity-tetrad / hydrodynamic-action papers) treats such residual symmetries as right-acting on the order-parameter manifold while the left action is the gauge/spectral content. The right-regular SU(3)_R here is the exact NCG analog: right translation on the group-manifold "condensate," commuting with the left-invariant `D_K` "BdG kinetic operator" by the same group-associativity that makes a residual order-parameter rotation commute with the quasiparticle dispersion. The commutant is internal; the question is only how it COUPLES to the quasiparticles.

**Role 3 — the fermion COUPLING is admissible only via the crossed product `A_K ⋊ SU(3)_R`.**

Being in the commutant is exactly the obstruction to being an inner fluctuation. Inner fluctuations of `D_K` are `Ω¹_{D_K}(A_K) = span{ a₀ [D_K, a₁] : a_i ∈ A_K }`. The operators `[D_K, a]` for `a ∈ A_K` map into `⊕_{(p,q)} B(V_{(p,q)}) ⊗ 1` — they act on the FIRST (gauge) Peter-Weyl factor and are `⊗1` on the SECOND (multiplicity/generation) factor (Skolem–Noether leg-membership; the S110 / §VII.BL mechanism, registry lines 21120/21155, confirmed via knowledge MCP). The right-regular generators act on the SECOND factor. A non-scalar generation handle is therefore necessarily OUTSIDE the left calculus — which is just Role 1+2 restated: the commutant is not reachable by the algebra's own differential calculus. So the SU(3)_R coupling cannot be turned on as an inner fluctuation; it can be coupled only by letting the group ACT on the algebra — i.e. via the crossed product `A_K ⋊ SU(3)_R`.

This crossed product IS the Kasparov external product (anchor confirmed via knowledge MCP: `s61_kasparov_product_verification.py`, "Kasparov product 6/6 conditions" PASS, atlas-07-permanent-results, S61; the framework's `A_K ⋊ G` coupling is realized as the external KK-product of the substrate triple with the group's regular-representation module). The group enters as the external acting group, not as a fluctuation of `D_K`.

**The load-bearing substrate distinction: "external-as-a-coupling" ≠ "an external field added IN a container."** This is the point I most carefully checked, because it is exactly where a container-thinking reviewer would mis-read the result. SU(3)_R is NOT a background field bolted onto a pre-existing spacetime stage. It is the substrate's OWN commutant — its own right-translation isometry, present in the fabric by the group structure itself. What is "external" is ONLY the inner-fluctuation IMAGE: the calculus `Ω¹_{D_K}(A_K)` is generated by the left algebra and, by the commutant property, simply does not contain the right-regular handle. The SHAPE coupling lives outside the INTERNAL calculus by the fabric's own triality arithmetic (Role 3 below), and is supplied by the substrate's own symmetry group acting through the crossed product. Direction preserved: `D_K (left-invariant) + SU(3)_R (its commutant) → inner-fluctuation image of the root handle is empty → coupling admissible only as the A_K ⋊ SU(3)_R image`. The substrate IS; the coupling-image is the external piece. This is faithful to `phononic-framing.md §"IS Space, Not IN Space"` — the same way a BEC acoustic white hole is a laboratory PROJECTION of the substrate transit, the SU(3)_R coupling is the external IMAGE of an intrinsic substrate isometry, not a field in a box.

**Triality selection-rule sub-derivation (why the inner-fluctuation image is EMPTY).** The center of SU(3) is `Z₃ = {ω^k I : ω = e^{2πi/3}}`; on irrep `(p,q)` it acts as `ω^{(p−q) mod 3}·Id`, giving triality `t(p,q) = (p−q) mod 3` (`proven_384`; registry §VII.BL line 21124; confirmed via knowledge MCP). First-principles exact check over `ℤ/3` (Sage):

- Every `A_K`-built one-form is triality-NEUTRAL: the `M₃(ℂ)` block is `3 ⊗ 3̄ = (1,1) ⊕ (0,0)`, both with `t = 0`; the left action preserves each Peter-Weyl `(p,q)` sector (Peter-Weyl: `G` acts on the first factor only ⇒ sector-preserving), so `t(A_K\text{-one-form}) = 0` EXACTLY.
- The generation triplet sits in the three center cosets `t ∈ {0,1,2}` (the framework's generation id). Any generation-MIXING (off-diagonal) handle `g ↔ g'` carries `t(O) = (g−g') mod 3 ∈ {1,2} = {+1,−1}`, NEVER `0`.
- Admissible inner fluctuation requires `t(O) = 0` (coset/sector-preserving). `0 ≢ 1 (mod 3)` and `0 ≢ 2 (mod 3)` ⇒ the off-diagonal SHAPE handle `R_{E_α}` (`t = ±1`) is group-theoretically EXCLUDED from `Ω¹_{D_K}(A_K)`: its inner-fluctuation image is EMPTY, EXACT at every `L_max` (a center-character superselection, regulator-invariant). The registered W3-1 `residual = 1.000000` is the numerical shadow of this exact exclusion.

This is the Axis-B-side completion of the picture: the SYMMETRY is internal (Role 1+2, the commutant), but the COUPLING it would supply is admissible only as the EXTERNAL crossed-product image (Role 3), because the only handle with non-scalar generation content (`t = ±1`) is exactly the one the center-character selection rule forbids from the internal calculus.

**Axis-B single-axis leg VERDICT: PASS.** SU(3)_R is the genuine real-isometry commutant of the left `A_K` action (`[D_K, Y_R] = 0` EXACT, Sage `ℚ[i]` over all 64 pairs = 0; the substrate's own right-translation isometry), and the fermion coupling it would supply is admissible only via the crossed product `A_K ⋊ SU(3)_R` (≡ Kasparov external product, S61 6/6 PASS), OUTSIDE `Ω¹_{D_K}(A_K)` by the `t(O) = ±1 ≠ 0` center-character selection rule (Sage `ℤ/3` exact). The symmetry is substrate-internal; only the coupling is the external image. The "external-as-a-coupling ≠ external field in a container" distinction holds substrate-first and is the correct reading.

---

### D4-external JOINT clause

> "The right-regular `R_{E_α}` SHAPE handle is external-as-a-coupling — admissible only via `A_K ⋊ SU(3)_R`, outside `Ω¹_{D_K}(A_K)` by `t(O)=±1≠0` — so the §VII.CK homogeneity-obstruction genus is COMPLETE as a statement about A_K-INTERNAL couplings."

Re-derived independently above. The three conjuncts each hold from first principles:

1. **`R_{E_α}` is external-as-a-coupling, admissible only via `A_K ⋊ SU(3)_R`** — PASS. `R_{E_α} ∈ (A_K^{left})′` (commutant, Sage-exact `[L,R]=0`), so it is not an inner fluctuation; the only way to couple it is the group acting on the algebra = the crossed product = the Kasparov external product (S61 anchor).
2. **outside `Ω¹_{D_K}(A_K)` by `t(O) = ±1 ≠ 0`** — PASS. Center-character selection rule, Sage `ℤ/3` exact: `t(\text{root handle}) = ±1`, `t(\text{A_K one-form}) = 0`, `0 ≢ ±1 (mod 3)` ⇒ empty image, regulator-invariant at every `L_max`.
3. **the genus is COMPLETE as a statement about A_K-INTERNAL couplings** — PASS. The four doors exhaust the candidate functional classes for a non-monotone sign-changing per-generation scalar built INTERNALLY: D1 (γ₉-graded odd-power trace, identically 0 by `{γ₉,D_K}=0`), D2 (γ₉-graded even spectral moment, C₂-only by `[J,D_K]=0` conjugation-evenness), D3 (γ₉-graded A_K-orientation cyclic cocycle, multiplicity-scalar by Skolem–Noether leg-membership), and D4 (the right-regular SU(3)_R connection — the ONE candidate with non-scalar leg-content, now closed-external by the commutant + triality arithmetic above). D4 was the only door that escaped D1 (γ₉-even ⇒ trace non-vanishing) and D3 (non-`A_K`-built), and it is closed as external-as-a-coupling. The obstruction is `A_F`-INDEPENDENT — the commutant theorem (no algebra's differential calculus reaches its own commutant non-scalarly) is a general structural fact, so no choice of finite algebra `A_F` re-opens it. Hence `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` is complete for A_K-INTERNAL couplings, and the fermion-mass SHAPE texture is external (the same `ε_LX` channel that carries the §VII.BL magnitude).

**One scope caution I am explicit about (does not change the verdict).** "COMPLETE as a statement about A_K-INTERNAL couplings" is the correct and bounded claim — and I verdict the clause AS STATED, which contains exactly that qualifier. The genus closes the INTERNAL homogeneity obstruction; it does NOT assert that the EXTERNAL crossed-product corridor delivers the observed SHAPE (that is a separate, falsifiable question — the registry's own D4-disposition notes the forced `Z₃`-circulant texture FALSIFIES quark-CKM and is RESONANT-CONDITIONAL for lepton-PMNS). The JOINT clause does not claim the external corridor succeeds; it claims the internal genus is complete and the handle is external. Both are true. The completeness is about the INTERNAL class, and the clause says exactly that.

**D4-external JOINT clause VERDICT: PASS.**

---

### Machine-readable clause-verdict block

```yaml
gate: S115-VIICK-D4-DISCHARGE-UNCONDITIONAL
reviewer: volovik-superfluid-universe-theorist
axis: B
axis_label: isometry / commutant / crossed-product-image leg
blind: true
read_only_source: "sessions/permanent-results-registry.md §VII.CK (body + D4 row + D4-disposition annotation + master-index row 173)"
forbidden_transcript_opened: false   # sessions/session-114/workshops/w-2-d4-rightreg-su3r-admissibility.md NOT opened
B_leg_verdict: PASS
JOINT_verdict: PASS
exact_checks:
  commutant_LR_commute: "max|[L_Xa,R_Yb]| = 0 EXACT over 64 su(3)xsu(3) pairs (Sage Q[i]); float shadow = registered 7.25e-17"
  triality_selection_rule: "t(A_K one-form)=0 ; t(root handle)=+-1 (mod 3) ; 0 != +-1 (mod 3) => inner-fluctuation image EMPTY (Sage Z/3 exact, L_max-invariant)"
anchors_confirmed:
  - "proven_384 / triality t(p,q)=(p-q) mod 3 (registry §VII.BL line 21124)"
  - "Skolem-Noether leg-membership / §VII.BL commutant-multiplicity-scalar (S110; registry 21120/21155)"
  - "Kasparov external product 6/6 PASS (S61 s61_kasparov_product_verification; atlas-07)"
note_for_closeout: "PASS-AND with Axis-A flips §VII.CK STAGE-3-PERMANENT -> STAGE-3-PERMANENT-UNCONDITIONAL (D4-open scope qualifier dischargeable)."
```

---

## Summary for the closeout

Both my verdicts are **PASS**. On a PASS-AND with the Axis-A (spectral-geometer) leg, §VII.CK re-scopes STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL: the D4 door is closed-external-as-a-coupling, the right-regular SU(3)_R handle is the substrate's own commutant isometry whose coupling enters only via the crossed product `A_K ⋊ SU(3)_R`, and the homogeneity-obstruction genus `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` is complete for A_K-INTERNAL couplings. The two load-bearing identities are EXACT (commutant `[L,R]=0` over `ℚ[i]`; triality `0 ≢ ±1 (mod 3)` over `ℤ/3`), not float-margin, and L_max-invariant. The substrate-first direction holds throughout: the symmetry is internal, only the coupling-image is external — "external-as-a-coupling," not "a field in a container."

I do NOT emit a verdict line to the verdict file — the closeout owns that.
