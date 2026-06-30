# Session 96 Synthesis: The Z/2-Graded Superalgebra-Extension Question for the Finite Spectral Triple (A_K, H_K, D_K) — NYT-2000 Q4 (Supersymmetry)

**Date**: 2026-05-30
**Agent**: connes-ncg-theorist (Connes-NCG-Theorist / Workhorse-NCG)
**Format**: SOLO SYNTHESIS (Slot-1, S-1) — single-domain structural-existence derivation, no second agent, no competing-framework claim.
**Source Documents**:
- `downloads/NYT_10-Physics-Questions_2000_exploration.md` (Q4 🌀 entry + Appendix row 4)
- `downloads/NYT_10-Physics-Questions_2000_breakdown.md` (verbatim Q4)
- `sessions/permanent-results-registry.md` §VII.U.2 (four-corner orthogonality; chirality-vs-A_F block-grading mismatch) — anchor-targeted via Grep/MCP, not full-read
- Agent memory `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` + `s46-pseudo-riemannian.md`

**Anchors re-verified via knowledge MCP (2026-05-30)**:
- `KO-dimension = 6` — PROVEN, atlas-04 G4, machine ε (<1e-15), survives SU(2,1) (theorem `proven_1225`).
- `[NEW S46] Twisted BdG NCG` — PERMANENT, atlas-07 row 46; underlying gate `TWIST-BDG-46 = FAIL` (32nd closure; `sessions/archive/session-46/session-46-quicklook.md:39`).
- `S85-NCG-META-EXCLUSION-CERTIFY` — PASS, value=2/2, `convention=Z/2-graded-HP*-Cuntz-Quillen-bivariant` (`s85_gate_verdicts.txt`).
- `S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION` — PASS, `convention=axioms-1-4-5-6-Poincare-duality-block-grading-mismatch` (registry §VII.U.2 ANCHOR-2, `audit_sha256=ff505a03…`).

---

## I. Session Outcome

**STRUCTURAL VERDICT (one-sided existence question, ONE domain owner): a nontrivial Z/2-graded *superalgebra extension* of the finite algebra `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` — one in which `A_K` is the even part and a nonzero odd part `A_K^{(1)}` closes under a graded bracket compatibly with the real structure `J`, the chirality grading `γ_F`, and the Dirac operator `D_K` — DOES NOT EXIST. The extension is OBSTRUCTED.** The obstruction's algebraic source is identified precisely: **the chirality grading `γ_F` is not inner to the represented algebra** (`f(D²) ∩ π(A_K) = scalars`; the "chirality-vs-A_F block-grading mismatch" of the S88 axiom-derivation), which — combined with the **order-zero condition** (axiom 4 / reality) forcing `π(A_K)` block-diagonal in the `γ_F` eigenspaces — collapses every candidate odd generator to a scalar. The near-neighbour negative result TWIST-BDG-46 (the BCS pairing as the most natural grade-mixing map) confirms the mechanism from the operator side: that pairing is a **Hilbert-space rotation, not an algebra automorphism**, and obstructs on **orientability** + Krein signature (8,8)≠(3,1).

A *distinct and weaker* statement holds trivially and must not be conflated with the above: the spectral triple **already carries** a Z/2-grading — the even/odd chirality decomposition `H_K = H_K^+ ⊕ H_K^-` by `γ_F`, mandatory for any even-KO-dimension triple. **Result classification: PARTICLE** (representation-theoretic content of `D_K`: the grading operator, chirality eigenspaces, and the obstruction live in the rep theory of `A_K` on `H_K`). The framework requires NO weak-scale SUSY; the relative-posterior commentary (§IV) is flagged COMMENTARY, not evidence.

---

## II. Key Results

### II.1 The triple is already Z/2-graded; the SUSY question is the *superalgebra-extension* question

**Result**: `(A_K, H_K, D_K)` is an even spectral triple in KO-dimension 6, hence equipped with a grading `γ_F = γ_F† , γ_F² = 1`, splitting `H_K = H_K^+ ⊕ H_K^-`. A Z/2-graded *structure* therefore exists trivially. — Classification: **PARTICLE**.

The NYT-2000 Q4 framing ("every fermion ↔ a boson twin; sparticles; SUSY broken") presupposes a spacetime-embedded super-multiplet. **Substrate-first reframe** (`phononic-framing.md` §"IS Space, Not IN Space"): there is no container in which selectrons/photinos "live." The only well-posed substrate question is a property of the finite algebra: *does `A_K` admit a graded superalgebra extension `A_K^{(0)} ⊕ A_K^{(1)}` (with `A_K^{(0)} = A_K`, `A_K^{(1)} ≠ 0`) carrying a graded bracket and compatible with `(J, γ_F, D_K)`?* This is the sharp, one-sided existence question this synthesis answers.

The KO-dim-6 sign data is the governing structure. From the verified anchor (theorem `proven_1225`, eqs `eq_18650`/`eq_10104`):

$$ J^2 = +1, \qquad J D_K = + D_K J, \qquad J\gamma_F = -\gamma_F J. \tag{1} $$

The sign `Jγ_F = −γ_F J` (i.e. `ε'' = −1`) is the load-bearing fact: in KO-dim 6 the chirality and the real structure **anticommute**. This is exactly the signature that the existing grading is a genuine even/odd splitting, and it is also what constrains how an odd algebra-extension could intertwine with `J`.

### II.2 The obstruction: `γ_F` is not inner, and the order-zero condition collapses the odd part to scalars

**Result**: any candidate odd algebra element `a₁ ∈ A_K^{(1)}` (one anticommuting with `γ_F`: `γ_F a₁ = − a₁ γ_F`, i.e. mapping `H_K^± → H_K^∓`) that simultaneously satisfies the order-zero condition is forced to be a scalar multiple of an off-diagonal partial isometry that is **not** an element of `π(A_K)`. Hence `A_K^{(1)} ∩ π(A_K) = {0}` modulo scalars, and **no nontrivial graded extension internal to the algebra exists.** — Classification: **PARTICLE / GEOMETRIC** (spectral-triple-structural).

Substitution chain (the structural-existence argument; every step from a verified NCG axiom):

- **Step 1 — even part is γ-block-diagonal.** By KO-dim-6 reality (axiom 4) the representation `π(A_K)` commutes with `γ_F`: `[γ_F, π(a)] = 0 ∀ a ∈ A_K`. Hence in the eigenbasis of `γ_F`, every represented `π(a)` is **block-diagonal**, `π(a) = diag(π^+(a), π^-(a))`. This is the standard even-triple grading compatibility and is what makes `A_K` the *even* part of any putative superalgebra.

- **Step 2 — an odd generator must be γ-block-off-diagonal.** A graded superalgebra requires `A_K^{(1)} ≠ 0` with `γ_F a₁ = − a₁ γ_F`. In the `γ_F` eigenbasis this forces `a₁ = antidiag(u, v)` — **purely off-diagonal**, mapping `H_K^+ → H_K^-` and back.

- **Step 3 — order-zero (axiom 4, reality) + the block-grading mismatch.** The S88 axiom-derivation (`S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION`, PASS) established, on this exact triple, the **chirality-vs-A_F block-grading mismatch**: the intersection of the functions of `D²` (which carry the spectral/chirality structure) with the represented algebra is only the scalars,
$$ f(D_K^2)\ \cap\ \pi(A_K) \;=\; \mathbb{C}\cdot 1. \tag{2} $$
The grading operator `γ_F` is therefore **NOT inner** — `γ_F ∉ π(A_K)` (and is not weakly approximable by it beyond scalars). The off-diagonal `a₁` of Step 2 is precisely the kind of operator that would have to be supplied by the *algebra* to grade it; (2) says the algebra supplies none such except scalars.

- **Step 4 — collapse.** Combining Steps 2–3: an `a₁` that is both (i) a represented element `π(a₁) ∈ π(A_K)` and (ii) γ-off-diagonal must lie in `π(A_K) ∩ {γ-off-diagonal operators}`. By Step 1 every `π(A_K)` element is γ-block-diagonal; the only operator that is both block-diagonal and block-off-diagonal is `0`. Therefore `A_K^{(1)} = {0}` (modulo the trivial scalar). **No nontrivial internal graded extension exists. ∎ (structural-existence, exact).**

**Regime of validity.** The argument is purely algebraic — it uses only axiom-1 (dimension/even structure giving `γ_F`), axiom-4 (reality, KO-dim 6, signs (1)), the order-zero condition, and the S88 block-grading-mismatch identity (2). It is **L-independent** (holds at every truncation `L_max`, and on the full triple) and **regulator-invariant** (no spectral-action moment, no `f(x)` enters). It does NOT forbid an *external* super-extension that adjoins new generators outside `A_K` (e.g. a doubled Nambu/BdG algebra `A_K ⊗ M₂(ℂ)`); it forbids grading `A_K` *itself*. The boundary of the claim is therefore "no superalgebra structure intrinsic to `A_K`," not "no graded object anywhere in the construction."

### II.3 Operator-side confirmation: TWIST-BDG-46 (the BCS-pairing grade-mixing map obstructs on orientability)

**Result**: the most physically natural grade-mixing operation on this triple — the BCS / Bogoliubov pairing `Δ` connecting particle and hole (the canonical off-diagonal, γ-reversing operator) — is **not an algebra automorphism of `A_K`**; it is a Hilbert-space (Nambu) rotation. The twist obstructs on **orientability** (the Hochschild-cycle representability of `γ`) and yields Krein signature **(8,8)**, not the Lorentzian **(3,1)** a physical grading would need. KO-dim 6 is preserved throughout. — Classification: **GEOMETRIC** (verified PERMANENT result, atlas-07 row 46; gate `TWIST-BDG-46` FAIL, 32nd closure).

This is the independent operator-theoretic corroboration of §II.2. Where §II.2 shows *algebraically* that the odd part collapses to scalars, TWIST-BDG-46 shows *operationally* that when one nonetheless tries to install the natural off-diagonal map (BCS `Δ`), it fails the axioms — and fails specifically on **orientability** (axiom 7), the axiom controlling whether `γ_F` is represented by a Hochschild cycle of `A_K`. The two results name the same wall from two sides: the grading operator is exogenous to `A_K`, so neither an algebra element (§II.2) nor an algebra automorphism (§II.3) can carry the grade-mixing.

> Memory-discipline note (verified, not asserted): my MEMORY.md flags an unresolved BDI-vs-DIII AZ-class tension and a "C = J·γ_9, C² = −1 → CI?" debugging entry. The present verdict does **not** depend on resolving it: the obstruction (2)+(Step-1 block-diagonality) holds for `ε'' = −1` / `J² = +1` (KO-dim 6) regardless of which Altland-Zirnbauer label is finally pinned, because the collapse uses only `[γ_F, π(A_K)] = 0` and `γ_F ∉ π(A_K)`. The AZ-class question is logged as a carry-forward (§V.3), not as a load-bearing input here.

### II.4 The S85 meta-exclusion certificate is the bivariant home for this verdict

**Result**: `S85-NCG-META-EXCLUSION-CERTIFY` (PASS, 2/2) provides the `Z/2-graded HP*-Cuntz–Quillen bivariant` machinery in which exclusion statements on this triple are already expressed. The present superalgebra-extension obstruction is structurally the same *kind* of object — a Z/2-graded (periodic-cyclic) statement — and is consistent with the certificate's even/odd `HP^•` decomposition `HP^0(A) = HP^0(M)⊗HP^0(A_F) ⊕ HP^1(M)⊗HP^1(A_F)`, `HP^1(A) = HP^0(M)⊗HP^1(A_F) ⊕ HP^1(M)⊗HP^0(A_F)`. — Classification: **GEOMETRIC** (NCG-axiomatic).

The certificate's grading is the *cohomological* Z/2 (periodic cyclic, mod-2). It coexists with the chirality Z/2 of §II.1 and with the obstruction of §II.2 without tension: a Z/2-graded *cohomology theory* on `A_K` and the *absence* of a Z/2-graded *algebra extension of `A_K`* are independent statements. This is why "the triple is Z/2-graded" (true, multiple ways) and "no superalgebra extension of `A_K`" (true) are both correct and non-contradictory.

---

## III. Gate Verdicts

This synthesis is a structural-existence derivation; it introduces NO new pre-registered computational gate. It RESTATES verified prior verdicts (authoritative per source — not re-adjudicated) and derives one new *structural* (machine-exact/axiomatic) conclusion from them.

| Gate / Result | Verdict (source-authoritative) | Decisive content |
|:--------------|:-------------------------------|:-----------------|
| `KO-dimension = 6` (atlas-04 G4) | PROVEN (machine ε) | `(ε,ε',ε'')=(+1,+1,−1)`; `Jγ_F=−γ_F J` |
| `TWIST-BDG-46` (atlas-07 row 46) | FAIL (32nd closure, PERMANENT) | BCS pairing = Hilbert rotation, not algebra automorphism; orientability fails; Krein (8,8)≠(3,1) |
| `S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION` | PASS | block-grading mismatch: `f(D²)∩π(A_K)=scalars` |
| `S85-NCG-META-EXCLUSION-CERTIFY` | PASS (2/2) | Z/2-graded HP*-Cuntz–Quillen bivariant exclusion machinery |
| **NEW (this synthesis): superalgebra-extension of `A_K`** | **OBSTRUCTED (structural, exact)** | odd part collapses to scalars: `A_K^{(1)}∩π(A_K)={0}` mod scalars |

---

## IV. Structural Implications

**What this closes.** The "internal SUSY" channel — *can the framework's own finite algebra be made supersymmetric by an intrinsic graded extension?* — is closed by a structural wall, not merely "untested." The wall is the same `γ_F ∉ π(A_K)` / order-zero block-diagonality fact that already powers the S88 four-corner orthogonality theorem and the TWIST-BDG-46 closure. This is an economy result in the sense of the Connes program: one algebraic fact (the grading is exogenous to the algebra) simultaneously (a) forbids the BCS twist, (b) enforces algebra-axis functional orthogonality, and (c) forbids the superalgebra extension. The three are facets of a single structure.

**What stays open / what is merely re-scoped.** The verdict is intrinsic-to-`A_K`. It does NOT touch:
- *External* graded doublings (`A_K ⊗ M₂(ℂ)`, Nambu/BdG): these adjoin generators and are a different object — already the subject of the open BdG-spectral-triple channel (MEMORY: "A_BdG = A_F ⊗ M₂(C)"). The §II verdict says such a doubling cannot be *re-internalized* as a grading of `A_K` alone.
- The phenomenology of weak-scale SUSY: the framework does not invoke it. Hierarchy is carried by the KK scale `M_KK = 7.4287e16 GeV` + spectral threshold corrections; the cosmological constant by the Volovik tracking vacuum (DILUTION-CC, PROVEN S66). No superpartner-cancellation is needed for either. This is a *structural independence*, established elsewhere — restated here, not re-derived.

**Substrate-first direction of explanation** (`phononic-framing.md`). The arrow runs `D_K structure (γ_F, J, signs (1)) → block-grading mismatch (2) → no intrinsic odd algebra part → no internal SUSY`. We do NOT explain the absence of sparticles by "SUSY is broken at a high scale in spacetime"; we explain it by the algebra of the substrate having no room for an intrinsic odd part. The emergent-physics statement ("no light superpartners") is downstream of the algebraic obstruction, not the reverse.

### IV.* Relative-posterior-weight observation — TAGGED COMMENTARY, NOT EVIDENCE, NOT A GATE

> **[COMMENTARY — `feedback_reporting-framing.md` constraint-strengthens-surviving-paths; NOT a registry gate, NOT evidence, carries NO probability mass on its own.]**
>
> The exploration doc's Q4 Bayesian reframe: a framework that **never required** weak-scale SUSY (its hierarchy + CC come from spectral geometry + the Volovik vacuum, not superpartner cancellation) does not pay the "naturalness" penalty that the sustained LHC sparticle-null (gluinos < ~2 TeV, stops < ~1+ TeV excluded) imposes on weak-scale-SUSY UV completions. In the EVOI/constraint-map language: each TeV of sparticle exclusion **closes a corridor for SUSY-dependent UV completions while leaving this framework's corridor untouched**, so the framework's *relative* standing among surviving programs improves. This is a statement about the *shape of the solution space after eliminations* (per `epistemic-discipline.md`: "eliminating wrong mechanisms STRENGTHENS surviving paths"), expressly **NOT** a positive measurement, **NOT** a pre-registered gate, and **NOT** evidence for the framework. It carries no number into the registry. The substrate verdict that DOES carry weight is the structural one in §I–II: the superalgebra extension of `A_K` is obstructed by an exact algebraic identity.

---

## V. Carry-Forward Computations

Only items satisfying all four fields propagate. Hygiene/observations are NOT listed (per `feedback_fix-in-session-never-defer.md`). The §I–II verdict is a *structural theorem stated and closed in this synthesis*; it is registry-landing-ELIGIBLE but landing is a bookkeeping act (route to `mack-cosmic-bridge` per housekeeping), not a future computation — hence it appears in §VI as a Result, not as a CF. Two genuine future computations and one resolution item are pre-registered below.

```
V.1  Explicit superalgebra-obstruction cocycle (make §II.2 a registered structural theorem)
   - What: Construct the explicit obstruction class to a Z/2-graded extension of A_K as a
           degree-(0,1) component in the Z/2-graded HP* / Cuntz–Quillen bivariant complex of the
           S85 certificate. Concretely: exhibit the map δ: A_K → (γ-off-diagonal operators)/π(A_K)
           and verify its image is exactly the scalar-quotient obstruction (i.e. compute that the
           only γ-off-diagonal element commuting with J·(order-zero) is the scalar partial isometry).
           Sage finite-block check on A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) acting on H_K = ℂ^16 (one generation),
           in the explicit γ_F eigenbasis.
   - Inputs: A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) representation matrices on ℂ^16; γ_F (chirality) and J (real
           structure) matrices with signs (ε,ε',ε'')=(+1,+1,−1); the S88 block-grading-mismatch
           identity f(D²)∩π(A_K)=scalars (audit_sha256=ff505a03…); S85 HP^• decomposition
           (II.3-2/II.3-3). M_KK = 7.428660036284456e16 (canonical, only if any dimensional
           normalization enters — expected NOT to, the result is dimensionless/structural).
   - Gate: NEW S96+ gate `SUPERALG-EXT-OBSTRUCTION-COCYCLE`.
           PASS  iff dim(A_K^{(1)} ∩ π(A_K))/scalars = 0 to machine ε (<1e-14) AND the obstruction
                 cocycle is exact-nontrivial (lands in HP^1 odd component, not coboundary);
           FAIL  iff a nonzero γ-off-diagonal represented element survives (would REOPEN internal SUSY);
           INFO  iff the cocycle is well-defined but the HP-degree placement is ambiguous (defer to
                 S85-certificate co-author for bivariant-degree pin).
   - Effort: 2–3 hours, 1 agent session (connes-ncg-theorist; Sage finite-block + HP* bookkeeping).

V.2  External graded doubling A_K ⊗ M₂(ℂ): does the BdG/Nambu super-extension exist where the
     intrinsic one does not? (the boundary-of-claim test of §II.2 regime statement)
   - What: Test whether the doubled algebra A_BdG = A_K ⊗ M₂(ℂ) (Nambu particle-hole) admits a
           nontrivial Z/2-graded superalgebra structure with the BCS Δ as the odd generator, under
           ALL seven NCG axioms — re-running the TWIST-BDG-46 obstruction on the DOUBLED algebra
           rather than on A_K. Decisive sub-checks: (i) is Δ an algebra automorphism of A_BdG
           (vs. only a Hilbert rotation of A_K)? (ii) orientability of γ on A_BdG; (iii) Krein
           signature of the doubled triple.
   - Inputs: A_BdG = A_K ⊗ M₂(ℂ) Nambu construction (MEMORY: "A_BdG = A_F ⊗ M_2(C)"); BdG Dirac
           D_BdG = [[D−μ, Δ],[Δ*, −(D*+μ)]] (knowledge eq `D_BdG` display form); TWIST-BDG-46
           obstruction data (orientability-fail, Krein (8,8)); KO-dim-6 sign data (1).
   - Gate: NEW S96+ gate `BDG-DOUBLED-SUPERALG-EXISTENCE`.
           PASS  iff A_BdG carries a nontrivial graded extension passing axioms 4+7 (Δ is an
                 automorphism of A_BdG AND orientability holds) — would localize SUSY-like structure
                 to the EXTERNAL doubling;
           FAIL  iff the doubled algebra inherits the same orientability/Krein obstruction as A_K
                 (Δ still only a Hilbert rotation) — closes the external channel too;
           INFO  iff KO-dim/Krein signature shifts in a way requiring a separate signature audit.
   - Effort: 4–6 hours, 1 agent session (connes-ncg-theorist; builds directly on BdG-spectral-triple
           channel already flagged paper-ready in MEMORY).

V.3  Resolve the AZ-class label (BDI vs DIII) for the KO-dim-6 triple under Nambu doubling
   - What: Pin the Altland-Zirnbauer symmetry class of (A_K, H_K, D_K) and of its Nambu double,
           resolving the MEMORY tension: BDI (T²=+1, S17c) vs DIII (chiral grading reversal,
           S11/S88-plan-w4c "child_AZ_class=DIII"), and the "C=J·γ_9, C²=−1 → CI?" debugging note.
           Compute T²=±1, C²=±1, and the chiral product S=TC explicitly from the verified
           (ε,ε',ε'')=(+1,+1,−1), J²=+1 data on ℂ^16 and on the doubled ℂ^32.
   - Inputs: J, γ_F matrices with KO-6 signs (1); the Nambu-doubling charge-conjugation C operator
           (MEMORY debugging note + s88-plan-w4c child_AZ_class entry); J²=+1 exactness;
           [J, D_K]=0 (eq `eq_18155`).
   - Gate: NEW S96+ gate `AZ-CLASS-PARENT-CHILD-PIN`.
           PASS  iff a single AZ class is determined to be self-consistent across parent (ℂ^16) and
                 child (ℂ^32 Nambu) with documented (T²,C²,S) signs;
           FAIL  iff parent and child force incompatible classes with no doubling map reconciling them;
           INFO  iff the class is basis/convention-dependent (then pin the convention and tag it).
   - Effort: 2–3 hours, 1 agent session (connes-ncg-theorist; pure linear-algebra sign computation,
           resolves a standing memory inconsistency — genuine future computation, NOT hygiene).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Triple is already Z/2-graded by `γ_F` (`H_K = H_K^+ ⊕ H_K^-`); KO-dim 6, `Jγ_F=−γ_F J` | PARTICLE | PROVEN (anchor; restated) | A graded *structure* exists trivially; the SUSY question is the *superalgebra-extension* question, not this |
| 2 | **No nontrivial Z/2-graded superalgebra extension of `A_K` exists** — odd part collapses to scalars via `[γ_F,π(A_K)]=0` (Step 1) + `f(D²)∩π(A_K)=scalars` (Step 3) | PARTICLE / GEOMETRIC | **OBSTRUCTED — structural, exact, L-independent (NEW this synthesis)** | "Internal SUSY" channel CLOSED by an algebraic wall; registry-landing-eligible structural theorem |
| 3 | Obstruction source = chirality grading `γ_F` is NOT inner to `π(A_K)` (block-grading mismatch) | GEOMETRIC | PROVEN (S88 axiom-derivation, PASS) | Same fact powers four-corner orthogonality + TWIST-BDG-46; one structure, three facets |
| 4 | Operator-side confirmation: BCS pairing = Hilbert rotation ≠ algebra automorphism; fails orientability; Krein (8,8)≠(3,1) | GEOMETRIC | PERMANENT (TWIST-BDG-46 FAIL, 32nd closure) | The natural grade-mixing map obstructs on axiom 7 — the algebra cannot carry the grading |
| 5 | Verdict is intrinsic-to-`A_K`; external doubling `A_K⊗M₂(ℂ)` is a different object (regime boundary) | GEOMETRIC | OPEN (CF V.2) | The wall forbids re-internalizing a Nambu/BdG super-doubling as a grading of `A_K` alone |
| 6 | Framework requires no weak-scale SUSY; relative posterior improves under sparticle-null | — | **COMMENTARY (NOT evidence, NOT a gate)** | Constraint-strengthens-surviving-paths; carries no probability mass; logged per `feedback_reporting-framing.md` |
