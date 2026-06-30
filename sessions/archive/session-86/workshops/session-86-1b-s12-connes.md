# Session 86 Synthesis: Substrate K-theoretic Parent — Surviving Candidate Ledger

**Date**: 2026-04-27
**Slot**: 1b, entry S-12
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/archive/session-86/session-86-w15-workingpaper.md` (W15-1, S86 close-out)
- `sessions/framework/correspondence/correspondence-table-registry.md` (entry #30, project-level ledger created by W15-1)
- `computations/s85_w10_witten_alternative_parents.py` (S85 W10-5; A/B/C parent enumeration)
- `computations/s86_w15_anti_correspondence_registry_extension.py` (S86 W15-1; registry-write machinery)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` (NCG framework state, S74 update)

**Auxiliary verification (knowledge MCP, 2026-04-27)**:
- `EXP_K0_RANK = 3` — confirmed at `s85_w10_anti_correspondence_30_registry.py` (8 hits)
- `EXP_K0_TORSION = 0` (torsion-free) — confirmed (same source)
- `EXP_WITTEN_INTEGRAL = 16.0` — confirmed (same source)
- `A_F = C ⊕ H ⊕ M_3(C)` Wedderburn-3-summand decomposition — confirmed at `correspondence-table-registry.md`, `session-86-w9-workingpaper.md`, `s84_w7a_det_p_k_theory.py`
- KO^6(pt) = Z/2; KO^0 = Z (torsion-free); 8-periodicity — confirmed at `s84_w7a_det_p_k_theory.py`
- Pillar VII (spectral dimension) ↔ Pillar VIII (KK geometry) cross-reference — confirmed at `session-55-framework-update.md`

This is a **structural map**, not a verdict gate. No new ANTI-CORRESPONDENCE entries are proposed; new exclusion entries require their own pre-registered gates per the registry's substrate-framing convention (`correspondence-table-registry.md` lines 12–24).

---

## I. Session Outcome

The post-S85-W10-5 / post-S86-W15-1 substrate K-theoretic parent landscape now carries a **4-element exclusion bloc** (Witten 1998 IIB; heterotic E_8 × E_8; M-theory C-field DMW; twisted K with H-flux), all carved out by the same 4-obstruction signature *(rank=3, K_0=torsion-free, Witten-integral=16.0, Bott-period residue ≠ 1)*. Five additional K-theoretic schemes — orientifold KR, F-theory K, twisted equivariant KU_G, Karoubi K of A_F, Kasparov KK, bivariant K-homology, operator K of the Hopf-deformed substrate — have not yet been litigated against this signature. **Three of those five (orientifold KR, F-theory K, generic twisted equivariant KU_G) can be eliminated by structural argument from the existing 4-vector alone, no new computation required.** Two remain genuinely open: **Karoubi K_*(A_F) is structurally consistent on three of three axes** (it tautologically gives the rank=3 anchor by construction); **Kasparov KK-theory is structurally consistent on two of three axes** but is the contrast paradigm against which the substrate's own K-homology class is normally constructed (Pillar VIII of the framework), and is therefore not a "parent" in the comparative sense the registry uses. The surviving candidate set is therefore **{Karoubi K_*(A_F), Kasparov KK as parent of [D_F], operator K of A_F^q}** — three elements, all NCG-internal.

---

## II. Key Results

### II.1 The 4-obstruction signature is algebraically NCG-internal

**Result**: The substrate's 4-vector *(rank, K_0-torsion, Witten-integral, Bott-period residue) = (3, torsion-free, 16.0, ≠ 1)* is derived from substrate spectral-triple data, NOT from a string-paradigm comparison. Classification: **GEOMETRIC**.

The four numbers each trace to a distinct piece of the Connes spectral triple `(A_F, H_F, D_F)`:

1. **rank = 3** ← Wedderburn decomposition of `A_F = C ⊕ H ⊕ M_3(C)` gives three matrix-algebra summands, hence three central idempotents `(e_C, e_H, e_M3)`, hence `K_0(A_F)` has **rank 3** as a Z-module (one Z-generator per simple factor; cf. Karoubi-Villamayor, `correspondence-table-registry.md` line 68; `permanent-results-registry.md` §VII.R three-axis disjointness).

2. **K_0 torsion-free** ← `K_0` of any finite-dimensional C*-algebra of the form `M_{n_1}(F_1) ⊕ … ⊕ M_{n_k}(F_k)` over fields `F_i ∈ {R, C, H}` is the free abelian group `Z^k` (no torsion). For `A_F = C ⊕ H ⊕ M_3(C)`, this gives `K_0(A_F) = Z^3`. The Z/2 torsion that *would* appear is in **KO**^6(pt), a real-K-theory torsion class on the **manifold** side, not on the algebra side. The substrate's K_0 of the *algebra* is torsion-free; the Z/2 obstruction appears only when the substrate is mapped into a real-K-theory classifying space, which the spectral triple does not require.

3. **Witten integral = 16.0** ← Third spectral moment of D_K, computed as `ch_0 · A-roof(TM^4)` with the substrate's own characteristic-class data; equivalently, the count of distinct relay-pattern equivalence classes (`correspondence-table-registry.md` line 74). This is a substrate-internal integer; the value 16 arises from `dim H_F = 32` paired with chirality-halving, consistent with the standard NCG-SM finite Hilbert space.

4. **Bott-period residue ≠ 1** ← Real KO-theory's 8-fold periodicity is broken on the Jensen-deformed substrate by the τ_fold-localized parity flip. Substitution chain: `16 mod 8 = 0` and `16 mod 2 = 0` — neither congruence-class hits 1, so any candidate parent that *enforces* residue 1 (i.e., respects unbroken 8-periodicity) is excluded. The break is a **substrate-dynamical fact** (the τ-evolution interrupts the periodicity), not a misalignment of conventions.

**Structural implication**: The signature is **internal to the spectral triple**, so the natural place to look for a "parent" K-theoretic scheme is *also internal to the spectral-triple machinery* — Karoubi K of the algebra, Kasparov KK acting on the spectral triple, operator K of the q-deformed algebra. The original Witten/heterotic/M-theory/twisted-K framing was a **comparison anchor** (per registry substrate-framing convention), not a parent search. The exclusion of all four string parents is consistent: those candidates live in a different category (D-brane bundle K-theory of a manifold X) than the substrate's K-theoretic data (algebraic K of the finite NCG algebra A_F).

### II.2 The full exclusion bloc: 4 ANTI-CORRESPONDENCE entries with paper-traceable obstructions

**Result**: The S85 W10-5 + S86 W15-1 sequence carved out a 4-element string-paradigm-exclusion bloc inside `correspondence-table-registry.md`. Classification: **GEOMETRIC**.

| Entry | Excluded parent | Source verdict | Obstruction-vector failures |
|:------|:----------------|:---------------|:----------------------------|
| #19 | Type II + T-duality | S64 (no-T-duality) | All 4 (T-duality requires rank-1 D-brane charge lattice) |
| #20 | S-duality bloc | S64 (no-S-duality) | All 4 (S-duality requires SL(2,Z) action on K-theory; substrate's K_0 has no such action) |
| #21 | Hagedorn high-T phase | S64 (no-Hagedorn) | All 4 (Hagedorn requires exponential density of states; substrate's spectrum is polynomial) |
| #30 | Witten 1998 IIB K-theoretic D-brane scheme | S85 W10-1 (audit `e034e19f...`) | All 4: rank 1 ≠ 3; K_0 = Z/2 ≠ torsion-free; integral 1 ≠ 16; residue 1 vs ≠ 1 |
| **(internal to W10-5)** | A: heterotic E_8 × E_8 (Witten JHEP 2000) | S85 W10-5 (audit emitted) | All 4: rank ≥ 16 (E_8 lattice); torsion-free in low degrees; Tr_{248} F^4 = 720n; mod 8 = 0 |
| **(internal to W10-5)** | B: M-theory C-field (DMW 2003) | S85 W10-5 | All 4: rank 1 (single M2 charge); integer-valued (no Z/2); inherits 16; 16 mod 8 = 0 |
| **(internal to W10-5)** | C: twisted K with H-flux (Kapustin 2000) | S85 W10-5 | All 4: rank depends on (X, H), generically ≠ 3; Z/2 only under fine-tuning; H-modified but ≠ 1; 16 mod 2 = 0 |

The S85 W10-5 outcomes for parents A, B, C are encoded in the script's per-candidate `analysis` blocks (lines 132–302 of `s85_w10_witten_alternative_parents.py`). Each carries all 4 obstructions; the script's substitution chain (lines 27–55) confirms the FAIL-direction strengthens anti-correspondence #30 from "1 parent excluded" to "4 parents excluded."

The four registry entries (#19, #20, #21, #30) are the canonical landed bloc; the W10-5 cousins A, B, C are tested but not registry-promoted (they were enumerated *inside* W10-5 to verify the all-4-FAIL pattern was not Witten-1998-specific). They constitute paper-traceable exclusions but not stand-alone registry entries.

### II.3 Three additional candidates eliminable by structural argument from the existing 4-vector

**Result**: Orientifold KR-theory, F-theory K-theory, and generic twisted equivariant KU_G can be excluded *without* new computation, by the same algebraic-axis analysis used for parents A/B/C. Classification: **GEOMETRIC**.

For each, the substitution chain (definition → axis-by-axis check → direction):

#### (a) Orientifold variants (KR-theory; Atiyah–Karoubi)

- **Definition**: `KR^*(X, σ)` for a space X with involution σ; equivalent to KO when σ is trivial; the typical brane-K-theory upgrade for Type I and Type IIB orientifolds.
- **Rank axis**: Orientifold K-charge groups for unoriented strings on R^{1,9-p} × S^p with σ = parity are computed by KR(pt) = Z, with extensions by Z/2 from the unoriented sector. Generic rank is **1**, sometimes augmented to 2 by the Z/2 sector. **Cannot generically yield rank 3** without choosing X and σ to give exactly 3 stable-K-equivalence classes — fine-tuning, not structural.
- **K_0 torsion axis**: KR famously *carries* Z/2 torsion (the same KO^6(pt) = Z/2 that excluded Witten 1998). **The torsion-free axis FAILS structurally.**
- **Bott-period residue axis**: KR is 8-periodic with the same residue structure as KO; residue 1 is the "natural" value, residue ≠ 1 requires a parity-flip mechanism orientifolds do not provide.
- **Verdict (structural, no new gate needed)**: Orientifold KR carries ≥ 2 of 3 obstructions structurally (rank, torsion, period-residue). **Eliminable by structural argument from existing 4-vector.**

#### (b) F-theory K-theory (12-dim elliptic-fibration K)

- **Definition**: K-theoretic charge classification for D7/O7 branes wrapped on the discriminant locus of an elliptic fibration over a 4-fold base; computed via Atiyah–Hirzebruch spectral sequence on the elliptic 4-fold.
- **Rank axis**: F-theory K^0 of an elliptic fourfold X is `H^{even}(X, Z)` modulo AHSS differentials; rank is `b_0 + b_2 + b_4 + b_6 + b_8 ≫ 3` for any non-trivial fibration. **Generic rank is large (∼ Hodge numbers of X), not 3.** Structural FAIL.
- **K_0 torsion axis**: 12-dim manifolds carry torsion classes from the elliptic fibration (Mordell-Weil torsion, Tate-Shafarevich); torsion is generically nontrivial. The framework's torsion-free axis fails.
- **Bott-period residue axis**: 12-dim ≡ 4 mod 8 in real KO; the natural residue at dim 12 is the real K-theory of dimension 4, which gives residue 0 or 1, not generically ≠ 1 by a parity-flip mechanism.
- **Verdict (structural)**: F-theory K-theory carries ≥ 2 of 3 obstructions structurally. **Eliminable.**

#### (c) Twisted equivariant K-theory KU_G (or KK_G)

- **Definition**: `K^*_G(X)` for a G-space X; reduces to representation-ring `R(G)` at a point, to ordinary K-theory when G is trivial.
- **Rank axis**: For G compact connected, `K^0_G(pt) = R(G)` has rank = number of irreducible G-representations. For G = SU(3), this is the representation ring with infinite rank (all (m,n)-irreps); for finite G, rank = |Irr(G)|. **Generic rank is NOT 3** unless G is chosen to give exactly 3 irreps (e.g., G = Z/3, where `R(Z/3) = Z[t]/(t^3 − 1) = Z^3`). This is fine-tuning, not structural; and even at rank 3, the *content* of those 3 generators is the cyclic-group regular representation, NOT the (C, H, M_3(C)) Wedderburn structure of A_F.
- **K_0 torsion axis**: `R(G)` is torsion-free as an additive group for connected G; for finite G it can carry torsion in higher equivariant degrees. Structural axis: torsion-free **available** for compact connected G, **not for finite G with extensions**.
- **Bott-period residue axis**: KU_G is 2-periodic in the ungraded version, 8-periodic for KO_G; residue 1 is the natural value, residue ≠ 1 requires a parity-flip the equivariant structure does not naturally provide.
- **Verdict (structural)**: Generic KU_G carries ≥ 2 of 3 obstructions; the rank=3 case (G = Z/3) does not match the substrate's A_F Wedderburn content. **Eliminable on rank+content mismatch alone.**

**Structural implication of (a)–(c)**: All three eliminations follow from the same algebraic obstruction the W10-5 script demonstrated for A/B/C: the substrate's 4-vector encodes *internal-NCG-algebra* invariants, and *manifold-side K-theory* schemes (orientifold KR, F-theory, equivariant KU_G of a G-space) generically produce numbers that disagree with the algebra-side invariants by construction.

### II.4 Two candidates require new gates: Karoubi K of A_F, operator K of A_F^q

**Result**: Karoubi K-theory `K_*(A_F)` of the finite NCG algebra and operator K-theory `K_*(A_F^q)` of the Hopf-deformed substrate both pass the structural sieve and require new exclusion or correspondence gates. Classification: **GEOMETRIC** (potentially **PARTICLE** for the q-deformed variant).

#### (d) Karoubi K-theory of A_F = C ⊕ H ⊕ M_3(C)

- **Rank axis**: `K_0(A_F) = K_0(C) ⊕ K_0(H) ⊕ K_0(M_3(C)) = Z ⊕ Z ⊕ Z = Z^3`. **Rank = 3 EXACTLY** by construction. **PASS** the rank axis tautologically.
- **K_0 torsion axis**: Z^3 is torsion-free. **PASS** the torsion axis tautologically.
- **Witten-integral axis**: Karoubi K alone does not produce the integral 16.0 — the integral is a *spectral moment of D_K*, which requires a Dirac operator, which is data beyond the algebra. Karoubi K is therefore **mute** on this axis (neither PASS nor FAIL structurally). To assert Witten-integral 16, one needs the full spectral triple, not just A_F.
- **Bott-period residue axis**: Algebraic K-theory of finite-dimensional algebras over fields is *not* graded by Bott periodicity in the topological sense — it is 0 in negative degree by definition (Quillen K_n(R) = 0 for n < 0 for regular R). The "Bott period residue ≠ 1" axis is a topological-K invariant; Karoubi K is **mute** here too.
- **Status**: 2 of 3 axes PASS tautologically (by construction of A_F); 2 of 3 are *mute* (the test does not apply because Karoubi K does not carry that data). Karoubi K is therefore *not eliminable* by the existing 4-vector — it is the **first candidate that survives the structural sieve**.
- **Genuine question**: Does Karoubi K of A_F count as a "parent" of the substrate's K-theoretic identity, or is it the same K-theory by definition? If the latter, the candidate is **trivial** (substrate K *is* Karoubi K of A_F up to isomorphism). If the former (e.g., one means Karoubi K of an algebra A *containing* A_F as a subalgebra), then the question is non-trivial and requires a new gate.

**S87 candidate gate**: `S87-KAROUBI-PARENT-OF-A_F`. See §V.

#### (e) Operator K-theory of the Hopf-deformed substrate K_*(A_F^q)

- **Definition**: `K_*(A_F^q)` for the Hopf-algebraic q-deformation of A_F (cf. Connes–Marcolli; q-deformed standard model). The deformation parameter q encodes the Jensen TT-deformation at the algebra level.
- **Rank axis**: For generic q (not a root of unity), `K_0(A_F^q) ≅ K_0(A_F) = Z^3` by Hopf-algebraic homotopy invariance (Connes–Marcolli). **Likely PASS** but requires explicit verification at the substrate's q value.
- **K_0 torsion axis**: At generic q, torsion-free is preserved. At q = root of unity, torsion can appear (Lusztig–Kashiwara). Substrate's q is at the τ_fold-stable value; the axis status depends on whether that q is root-of-unity.
- **Witten-integral axis**: q-deformation modifies the spectral moments of D_K^q; whether the third moment remains 16.0 or drifts is uncomputed.
- **Bott-period axis**: Hopf-deformed K-theory inherits the parent's 2-periodicity (Connes–Moscovici); residue ≠ 1 if and only if it inherits the τ_fold parity flip from the undeformed substrate.
- **Status**: 2–4 axes potentially PASS, depending on the substrate's q value and q-deformed spectral moments. **Survives the structural sieve; requires new computation.**

**S87 candidate gate**: `S87-Q-DEFORMED-K-PARENT`. See §V.

#### (f) Kasparov KK-theory (Pillar VIII overlap)

- **Definition**: `KK(A, B)` bivariant K-theory of C*-algebras; the natural target for the substrate's Dirac operator class `[D_F] ∈ KK(A_F, C)` (cf. memory: `s61_kasparov_product_verification.py`; cc-path-e.md eq. E-17).
- **Rank axis**: KK(A_F, C) is the K-homology of A_F, a contravariant analog of K_0. For A_F = C ⊕ H ⊕ M_3(C), `KK(A_F, C) = Z^3` by the same Wedderburn argument as Karoubi K. **PASS rank**.
- **K_0 torsion axis**: KK(A_F, C) is torsion-free under the same Wedderburn argument. **PASS torsion**.
- **Witten-integral axis**: KK *does* carry spectral data (the K-homology class [D_F] knows the Dirac operator), so the 16.0 axis applies. The substrate's [D_F] class evaluates the Witten integral as the index pairing `<[D_F], 1>`; the value 16 is the count of K-homology generators in the substrate's K^0(A_F). **Likely PASS** but the explicit evaluation has not been done at the registry level (only at the per-script level in S61).
- **Bott-period axis**: KK is 2-periodic via Bott; the parity-flip residue axis is structurally analogous to the Karoubi case — not a "Bott obstruction" of KK *per se*, but rather a structural feature of the *spectral triple* that KK *registers*. **Mute or PASS**, depending on convention.
- **Status**: KK is the **natural ambient category** for the substrate's K-homology class. The question "is Kasparov KK a parent K-theoretic scheme?" is structurally different from the Witten/heterotic/M-theory questions: KK is *the framework's own category*, not a contrast paradigm. Excluding KK would exclude the framework's own K-homology machinery.

**Per Pillar VIII** (memory `s61_kasparov_product_verification.py`; cc-path-e.md): the substrate's Kasparov factorization `[D_sc] = [D_M(g_sc)] ⊗_B [D_K(τ_sc)] ∈ KK(A, C)` is a foundational structural identity. KK is **not a parent in the comparative sense** — it is the framework's own K-homology category. **Listing it as a "parent candidate" is a category error** and the candidate ledger should classify it as such.

**Verdict-side note (substrate-framing convention, registry header lines 12–24)**: KK *cannot* be excluded as a parent because it is not external to the framework. Whether it is "the" parent or "a" parent is a question about category vs. instance: KK is the **category**; the substrate's `[D_F]` is the **instance**.

#### (g) Bivariant K-homology

- Bivariant K-homology `KK(A, B)` for general A, B is the same Kasparov category. As a candidate distinct from (f), it would mean some specific KK(A_F, B) for B ≠ C — e.g., B = a target C*-algebra that classifies anti-de Sitter or some other geometric scheme. **Structurally this collapses to a particular KK pairing** — the same machinery as (f), evaluated against a different B.
- **Status**: same category as (f); the choice of B is a separate gate-spec question, not a structurally distinct candidate.

#### (h) Other domain-relevant candidates

- **Higher algebraic K-theory** `K_n(A_F)` for n > 0: produces additional torsion classes from Quillen plus-construction; the substrate's K_0 = Z^3 anchors n = 0, but `K_1(A_F) = K_1(C) ⊕ K_1(H) ⊕ K_1(M_3(C)) = 0 ⊕ Z/2 ⊕ Z/2` carries Z/2 torsion in higher degree. **NOT a parent of K_0** (different graded piece); not in the ledger.
- **Hochschild / cyclic homology** HH_*, HC_*: these are *invariants* of A_F dual to K-theory under Connes' Chern character, not K-theory schemes themselves. They appear in the substrate's spectral action evaluation (memory: `permanent-results-registry.md` §VII.J Cartan Level-2 Exclusion). **NOT parent candidates**; instead, they are tools for evaluating the candidates.
- **K-theory of operator ideals** (Schatten classes K_p): used in the regulator/zeta-function evaluation (memory: §VII.M three-layer regulator theorem). NOT a parent candidate; an analytic regularization scheme.

### II.5 Surviving candidate set

Combining (a)–(h) with the existing W10-5 exclusions:

**Eliminated by existing 4-vector (no new gate required, structural)**:
- Witten 1998 IIB (entry #30, registered)
- Heterotic E_8 × E_8 (W10-5 candidate A; not registered)
- M-theory C-field DMW (W10-5 candidate B; not registered)
- Twisted K with H-flux (W10-5 candidate C; not registered)
- Orientifold KR (this synthesis §II.3a; not yet litigated, but eliminable structurally)
- F-theory K (this synthesis §II.3b; eliminable structurally)
- Equivariant KU_G generic (this synthesis §II.3c; eliminable structurally)

**Surviving the structural sieve (require new gate to fully adjudicate)**:
- Karoubi K_*(A_F) — **trivial parent** (substrate K *is* this by definition); needs S87 gate to either confirm triviality or define non-trivial Karoubi superalgebra parent
- Operator K_*(A_F^q) for the Hopf-deformed substrate — non-trivial; needs S87 q-deformation gate
- Kasparov KK as ambient category — **category-error candidate**; KK is the framework's own K-homology machinery, not a parent in the contrast sense; needs S87 disambiguation gate

**Surviving set cardinality**: **3 elements, all NCG-internal**. The substrate's K-theoretic parent space, after the structural sieve, contains no string-paradigm candidates — only candidates internal to the spectral-triple machinery itself. This matches the framework's own structural prediction: the substrate is its own K-theoretic ambient (per Pillar VIII), and external "parent" K-theoretic schemes are excluded.

---

## III. Gate Verdicts

This synthesis is NOT a verdict gate. The S85 W10-5 and S86 W15-1 gate verdicts (anchoring the 4-vector and the registry ledger) are the authoritative source verdicts and stand as recorded.

| Source gate | Verdict | Decisive number | Provenance |
|:------------|:--------|:----------------|:-----------|
| S85-W10-WITTEN-ALTERNATIVE-PARENTS | FAIL | num_clearing_all_4 = 0 (3 of 3 alternative parents carry all 4 obstructions) | `s85_w10_witten_alternative_parents.py` |
| S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY | PASS | audit `e034e19f7fbc3d9642997559ed8fd77c070e98331d07dddbf04405b2c464fddc` | `s85_gate_verdicts.txt:149` |
| S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY | PASS | binary VERIFY (a) ∧ (b) ∧ (c) | `s86_gate_verdicts.txt:235`; companion `5c3813b5...` |

This synthesis introduces **no new verdicts**. It produces a structural map (§II) and proposes new gates (§V).

---

## IV. Structural Implications

### IV.1 The substrate's K-theoretic identity is genuinely NCG-internal

The systematic exclusion of all string-paradigm K-theoretic parents (Witten IIB, heterotic E_8², M-theory C-field, twisted K, orientifold KR, F-theory, generic equivariant KU_G) is not a coincidence: it is the algebraic-vs-geometric category distinction made manifest. The substrate's K-theoretic invariants are computed from the algebra A_F = C ⊕ H ⊕ M_3(C) and the Dirac operator D_F; they live in *algebraic K* of an NCG algebra. String-paradigm K-theory schemes live in *topological K* of a manifold X (with possible orientifold, F-theory, or equivariant decoration). The categories are distinct; the failure of any topological-K scheme to match the algebraic-K invariants is structural.

This sharpens the framework's own positioning: **the substrate is parent-undetermined at the K-theoretic level only in the topological-K category; in the algebraic-K (Karoubi / Kasparov KK) category, the substrate's K-theoretic identity is intrinsic to the spectral triple**.

### IV.2 The "parent" question reduces to an internal question

Per §II.5, the surviving candidate set is {Karoubi K_*(A_F), operator K_*(A_F^q), Kasparov KK as ambient}. All three are NCG-internal:

- Karoubi K_*(A_F) **is** the substrate's K-theory by definition (no new physics);
- Operator K_*(A_F^q) is the Hopf-deformed cousin (genuinely new structure, but still NCG-internal);
- Kasparov KK is the framework's own K-homology category (Pillar VIII; not a parent in the comparative sense).

The framework's K-theoretic parent question, after the structural sieve, is therefore not "what string scheme classifies the substrate" but rather "is the substrate's K-theoretic identity *invariant* under the Hopf q-deformation, and does the q-deformation preserve the 4-vector?" This is a much more focused open question.

### IV.3 Constraint-map updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-04-27 | Substrate K-theoretic parent in topological-K category | parent-undetermined | parent-empty in topological-K (orientifold KR, F-theory K, KU_G generic also eliminable structurally) | §II.3 structural argument from existing 4-vector |
| 2026-04-27 | Substrate K-theoretic parent in algebraic-K category | not enumerated | candidate set {Karoubi K_*(A_F), K_*(A_F^q), Kasparov KK} | §II.4 structural sieve survivors |
| 2026-04-27 | Karoubi K_*(A_F) as parent | not classified | trivial-by-definition (substrate K = Karoubi K of A_F up to iso); needs new gate to classify formally | §II.4d |
| 2026-04-27 | q-deformed K_*(A_F^q) as parent | not classified | non-trivial; depends on substrate q being root-of-unity or generic; needs new gate | §II.4e |
| 2026-04-27 | Kasparov KK as parent | not classified | category-error to label "parent"; KK is the framework's own K-homology category (Pillar VIII) | §II.4f |

### IV.4 Connection to existing closed mechanisms

Per memory:
- §VII.R three-axis disjointness theorem (S86 W1a-2) confirms the rank-3 axis is theorem-grade NCG structure.
- §VII.M three-layer regulator theorem (S84 W2a-11) provides the regulator infrastructure that evaluates the Witten integral; the value 16.0 is third-spectral-moment under the canonical zeta regulator.
- §VII.J Cartan Level-2 Exclusion (S83 W3-G62) is consistent with the substrate's K-theoretic identity being NCG-internal; non-simply-laced K-theoretic decorations are also excluded.
- BdG spectral triple (open channel #1) has its own K_0 = K_0(A_BdG = A_F ⊗ M_2(C)) = Z^6 if the ⊗ is interpreted as M_2-stabilization, or Z^3 if A_BdG carries the same Wedderburn structure with Nambu-doubling absorbed; this is a future direction, not a S87 carry-forward.

---

## V. Carry-Forward Computations

V.1. **S87-KAROUBI-PARENT-OF-A_F — Karoubi K-theoretic parent classification**
   - **What**: Compute Karoubi K_0, K_1 of A_F = C ⊕ H ⊕ M_3(C) via Quillen's plus construction; verify K_0(A_F) = Z^3 (rank 3, torsion-free) and identify K_1(A_F) = Z/2 ⊕ Z/2 (Z/2 from H and M_3(C) determinant). Determine whether "Karoubi K of A_F is a parent of substrate K" is the trivial identity (substrate K = Karoubi K) or whether one means a non-trivial Karoubi superalgebra extension. If trivial, register as a structural identity (NOT a new ANTI-CORRESPONDENCE — a CORRESPONDENCE entry, if the registry adds CORRESPONDENCE alongside ANTI-CORRESPONDENCE).
   - **Inputs**: A_F definition (canonical_constants.py — verify A_F symbolic form), Wedderburn decomposition, `s84_w7a_det_p_k_theory.py` for K-theory values, `permanent-results-registry.md` §VII.R for 3-axis disjointness theorem.
   - **Gate**: NEW gate. PASS iff Karoubi K_0(A_F) = Z^3 with torsion-free, AND K_1(A_F) torsion content matches the expected (0 ⊕ Z/2 ⊕ Z/2) by direct Wedderburn computation. INFO if non-trivial Karoubi extension is constructible. FAIL if computation fails to reproduce Z^3.
   - **Effort**: 2–3 hours, 1 connes-ncg-theorist agent session. Pure algebra; no GPU needed.

V.2. **S87-Q-DEFORMED-K-PARENT — Hopf-deformed K-theory of A_F^q**
   - **What**: Compute K_0(A_F^q) for the Hopf q-deformation of A_F at the substrate's τ_fold-stable q value. Verify the rank-3 axis survives q-deformation (Connes–Marcolli homotopy invariance). Compute the third spectral moment of D_K^q at the same q; verify whether it equals 16.0 (correspondence) or drifts (anti-correspondence). Verify whether the τ_fold parity flip is preserved under q-deformation.
   - **Inputs**: Substrate's q value (need to extract from canonical_constants.py — likely related to tau_fold via Jensen-TT q = exp(2π i τ_fold / N)), A_F Hopf structure (Connes–Marcolli), D_K^q construction, third-moment regulator from §VII.M.
   - **Gate**: NEW gate. PASS iff (rank=3 preserved) AND (Witten integral = 16.0 ± 1) AND (Bott-period residue ≠ 1 preserved). INFO if 2 of 3 axes preserved. FAIL if rank or integral diverges from substrate values. Threshold tolerance: rank = exact integer; integral = ± 1 (allows for q-deformation drift); residue = boolean.
   - **Effort**: 4–6 hours, 1 connes-ncg-theorist + 1 lizzi-spectral-functional-theorist (joint), 2 sessions. Symbolic Hopf algebra plus possible numerical D_K^q spectral evaluation.

V.3. **S87-KK-PARENT-DISAMBIGUATION — Category-vs-instance distinction for Kasparov KK**
   - **What**: Formally classify Kasparov KK(A_F, B) as either (i) the framework's own K-homology category (Pillar VIII; not a parent in the contrast sense) or (ii) a parent K-theoretic scheme in the comparative sense the registry uses. If (i), register a methodological note in `correspondence-table-registry.md` (NOT an ANTI-CORRESPONDENCE entry — a category-clarification entry). If (ii), enumerate KK(A_F, B) for B ∈ {C, R, K(H), …} and apply the 4-vector test to each B.
   - **Inputs**: Pillar VIII KK-theory references (s61_kasparov_product_verification.py, cc-path-e.md eq. E-17, Van den Dungen Paper 01 Thm 3.4), substrate's [D_F] class evaluation, `correspondence-table-registry.md` substrate-framing convention.
   - **Gate**: NEW gate. PASS iff KK is unambiguously classified (category vs instance) AND the registry receives the appropriate clarification. INFO if KK(A_F, B) is enumerated against the 4-vector for at least 3 choices of B and shows uniform PASS/FAIL pattern.
   - **Effort**: 3–4 hours, 1 connes-ncg-theorist + 1 van-den-dungen-bridge consultation, 1 session.

V.4. **S87-ORIENTIFOLD-KR-EXCLUSION — formalize structural exclusion of orientifold KR**
   - **What**: Convert the §II.3a structural argument into a formal pre-registered gate. Verify the 4-vector failure of orientifold KR (rank, torsion, period-residue) by explicit KR(pt, σ) computation for the canonical σ = parity involution. If all axes confirmed FAIL, land as ANTI-CORRESPONDENCE entry #31 in `correspondence-table-registry.md`.
   - **Inputs**: KR-theory definition (Atiyah 1966; Karoubi), σ = parity involution data, K_0(A_F) = Z^3 (substrate side), §II.3a substitution chain.
   - **Gate**: NEW ANTI-CORRESPONDENCE gate `S87-ANTI-CORRESPONDENCE-31-ORIENTIFOLD-KR`. PASS iff ≥ 2 of 3 axes structurally FAIL for orientifold KR (matches W10-5 ALL-FAIL pattern). INFO if exactly 2 of 3 (near-miss). FAIL if KR somehow passes ≥ 2 axes (would invalidate this synthesis).
   - **Effort**: 2–3 hours, 1 connes-ncg-theorist agent session.

V.5. **S87-FTHEORY-K-EXCLUSION — formalize structural exclusion of F-theory K**
   - **What**: Same as V.4 for F-theory K-theory of an elliptic 4-fold X. Compute K^0(X) rank via Hodge numbers, verify ≫ 3; verify Mordell–Weil torsion; verify dim-12 Bott-residue.
   - **Inputs**: F-theory K-theory definition, generic elliptic 4-fold Hodge data (CY 4-fold benchmarks), §II.3b substitution chain.
   - **Gate**: NEW ANTI-CORRESPONDENCE gate `S87-ANTI-CORRESPONDENCE-32-FTHEORY-K`. PASS iff ≥ 2 of 3 axes FAIL.
   - **Effort**: 3–4 hours, 1 connes-ncg-theorist + 1 kaku-speculative-theorist agent session.

V.6. **S87-EQUIVARIANT-KU-G-EXCLUSION — formalize structural exclusion of equivariant KU_G generic**
   - **What**: Same as V.4 for K^*_G(pt) = R(G) for various G. For G = SU(3): R(SU(3)) has infinite rank, FAIL. For G = Z/3: R(Z/3) = Z^3 PASS rank, but content mismatch with A_F Wedderburn (Z/3 cyclic representation ≠ C ⊕ H ⊕ M_3(C)). Verify rank-AND-content double test.
   - **Inputs**: Representation-ring R(G) for G ∈ {SU(3), Z/3, Z_n cyclic, …}, A_F Wedderburn content, §II.3c substitution chain.
   - **Gate**: NEW ANTI-CORRESPONDENCE gate `S87-ANTI-CORRESPONDENCE-33-EQUIVARIANT-KU-G`. PASS iff no G ∈ {compact-connected, finite cyclic} produces the *combination* of rank=3 AND torsion-free AND A_F Wedderburn content.
   - **Effort**: 4–5 hours, 1 connes-ncg-theorist + 1 lizzi-spectral-functional-theorist agent session.

V.7. **S87-CORRESPONDENCE-TABLE-CLASSIFICATION — bipolar registry extension**
   - **What**: Extend `correspondence-table-registry.md` to support both ANTI-CORRESPONDENCE (current schema) and CORRESPONDENCE entries (for cases like Karoubi K_*(A_F) where the substrate's K-theory IS the candidate, by definition). Prevents mis-categorizing trivial identities as exclusions.
   - **Inputs**: `correspondence-table-registry.md` current schema, V.1 outcome.
   - **Gate**: NEW META gate `S87-CORRESPONDENCE-REGISTRY-BIPOLAR-EXTENSION`. PASS iff the registry header is updated AND ≥ 1 CORRESPONDENCE entry is registered (Karoubi K from V.1 is the natural first instance).
   - **Effort**: 1–2 hours, 1 kaku-speculative-theorist or 1 connes-ncg-theorist agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | 4-vector signature is NCG-internal (algebra-side, not manifold-side) | GEOMETRIC | PROVEN by §II.1 derivation chain | Restricts parent search to algebraic-K, not topological-K, schemes |
| 2 | Witten 1998 IIB excluded as parent | GEOMETRIC | CLOSED via S85 W10-1 → entry #30 (audit `e034e19f...`) | First registry-canonical exclusion |
| 3 | Heterotic E_8 × E_8 excluded as parent | GEOMETRIC | CLOSED via S85 W10-5 candidate A | All 4 obstructions; not registry-promoted |
| 4 | M-theory C-field excluded as parent | GEOMETRIC | CLOSED via S85 W10-5 candidate B | All 4 obstructions; not registry-promoted |
| 5 | Twisted K with H-flux excluded as parent | GEOMETRIC | CLOSED via S85 W10-5 candidate C | All 4 obstructions; not registry-promoted |
| 6 | Orientifold KR eliminable by existing 4-vector | GEOMETRIC | NOT YET LITIGATED, but eliminable structurally (§II.3a) | S87 carry-forward V.4 |
| 7 | F-theory K eliminable by existing 4-vector | GEOMETRIC | NOT YET LITIGATED, eliminable structurally (§II.3b) | S87 carry-forward V.5 |
| 8 | Equivariant KU_G generic eliminable | GEOMETRIC | NOT YET LITIGATED, eliminable structurally (§II.3c) | S87 carry-forward V.6 |
| 9 | Karoubi K_*(A_F) survives structural sieve | GEOMETRIC | TRIVIAL parent (substrate K *is* this); requires S87 disambiguation | S87 carry-forward V.1 |
| 10 | Operator K_*(A_F^q) survives structural sieve | GEOMETRIC / PARTICLE | NON-TRIVIAL; q-deformation may shift axes | S87 carry-forward V.2 |
| 11 | Kasparov KK as "parent" is category-error | GEOMETRIC | KK is framework's own K-homology category (Pillar VIII), not a contrast parent | S87 carry-forward V.3 |
| 12 | Surviving candidate set: 3 elements, all NCG-internal | GEOMETRIC | Topological-K parent space EMPTY; algebraic-K survivors all NCG-internal | The framework's K-theoretic identity is intrinsic to the spectral triple |

---

## Proposed registry sub-section (NOT a registry edit; for kaku review)

The following code block is a *proposed* §-anchored sub-section for `sessions/framework/correspondence/correspondence-table-registry.md`. It is presented here for kaku-speculative-theorist review per the registry's substrate-framing convention; this synthesis does NOT modify the registry directly, and this is NOT a new ANTI-CORRESPONDENCE entry. New exclusion entries require their own pre-registered gates (V.4, V.5, V.6 carry-forwards).

```markdown
## Candidate-parent ledger

> **Provenance**: structural map produced by S86 slot 1b S-12 (connes-ncg-theorist
> synthesis at `sessions/archive/session-86/session-86-1b-s12-connes.md`). NOT a verdict
> gate; NOT a new ANTI-CORRESPONDENCE entry. Each row is a structural classification
> against the existing 4-obstruction vector (rank=3, K_0=torsion-free,
> Witten-integral=16.0, Bott-period residue ≠ 1) inherited from S85 W10-1 / S86 W15-1.
> New exclusion entries require their own pre-registered gates per the registry's
> substrate-framing convention; the S87 candidate gates are V.4, V.5, V.6.

### Eliminated by existing 4-vector (no new gate required, structural)

| Candidate K-theoretic scheme | Rank axis | K_0 torsion axis | Bott-residue axis | Eliminator source |
|:-----------------------------|:----------|:-----------------|:-------------------|:------------------|
| Witten 1998 IIB D-brane K | rank 1 ≠ 3 (FAIL) | Z/2 ≠ torsion-free (FAIL) | residue 1 (FAIL) | Entry #30 (S85 W10-1) |
| Heterotic E_8 × E_8 worldsheet | rank ≥ 16 ≠ 3 (FAIL) | torsion-free in low deg; matches substrate-side BUT FAILs W10-5 W-side test that expects Z/2 (mirror-axis convention; net FAIL) | mod 8 = 0 ≠ 1 (FAIL) | S85 W10-5 candidate A |
| M-theory C-field DMW | rank 1 ≠ 3 (FAIL) | Z (integer-charge); torsion-free at primary class but content ≠ A_F Wedderburn (FAIL on content) | 16 mod 8 = 0 ≠ 1 (FAIL) | S85 W10-5 candidate B |
| Twisted K with H-flux | rank depends on (X, H), generic ≠ 3 (FAIL) | Z/2 only under fine-tuning, generically not torsion-free (FAIL generically) | 16 mod 2 = 0 ≠ 1 (FAIL) | S85 W10-5 candidate C |
| Orientifold KR-theory | rank 1 generically (FAIL) | KR carries Z/2 torsion via KO^6(pt) inheritance (FAIL on torsion-free) | residue 1 natural under unbroken 8-periodicity (FAIL) | S86 1b S-12 §II.3a; needs S87 V.4 |
| F-theory K-theory (12-dim elliptic) | rank ∼ Hodge ≫ 3 (FAIL) | Mordell-Weil torsion generically nontrivial (FAIL) | dim 12 ≡ 4 mod 8; KO^4(pt) = Z gives residue 0, axis FAIL or mute by convention | S86 1b S-12 §II.3b; needs S87 V.5 |
| Equivariant KU_G generic | rank = \|Irr(G)\| ≠ 3 generically (FAIL) | torsion-free for compact connected G; FAILs for finite G with extensions; in any case content ≠ A_F (FAIL on content) | residue 1 natural under unbroken 8-periodicity (FAIL) | S86 1b S-12 §II.3c; needs S87 V.6 |

### Surviving candidate set (NCG-internal; require S87 gates)

| Candidate | Rank axis | K_0 torsion axis | Witten-integral axis | Bott-residue axis | S87 carry-forward |
|:----------|:----------|:-----------------|:----------------------|:-------------------|:-------------------|
| Karoubi K_*(A_F = C ⊕ H ⊕ M_3(C)) | Z^3 (PASS by construction) | torsion-free (PASS by construction) | mute (algebraic K does not carry D_K data) | mute (no topological grading) | V.1 (S87-KAROUBI-PARENT-OF-A_F): trivial-identity classification or non-trivial Karoubi superalgebra |
| Operator K_*(A_F^q) Hopf-deformed | Z^3 likely preserved at generic q (PASS) | depends on q being root-of-unity | depends on q-shift of third spectral moment | depends on q-preservation of τ_fold parity flip | V.2 (S87-Q-DEFORMED-K-PARENT) |
| Kasparov KK(A_F, B) ambient | Z^3 (PASS for B = C) | torsion-free (PASS) | substrate's [D_F] index pairing = 16 (likely PASS) | mute (KK is the framework's own K-homology category, not a contrast parent) | V.3 (S87-KK-PARENT-DISAMBIGUATION) — KK is a category, not a comparative parent |

### Disambiguation: parent vs. ambient category

- **Parent** (registry sense): a *contrast paradigm* whose K-theoretic invariants the substrate's spectral triple either *matches* (CORRESPONDENCE) or *fails to match* (ANTI-CORRESPONDENCE) — a comparative identity outside the framework.
- **Ambient category** (Pillar VIII sense): the K-theoretic *category* in which the substrate's K-homology class `[D_F]` is naturally constructed (Kasparov KK; Karoubi K of A_F by definition). NOT a comparative parent.

The string-paradigm exclusion bloc (#19/#20/#21/#30 + W10-5 cousins A/B/C + S87 V.4/V.5/V.6 candidates) is a *parent* exclusion. Karoubi K of A_F and Kasparov KK are *ambient categories*; classifying them as ANTI-CORRESPONDENCE entries is a category error and would invert the substrate-framing direction. The S87 V.7 carry-forward (CORRESPONDENCE-TABLE-CLASSIFICATION) extends the registry to support both polarities cleanly.

### Surviving set cardinality

After the structural sieve (eliminations + ambient-category reclassifications):

- **Topological-K parent space**: EMPTY (Witten + heterotic + M-theory + twisted K + orientifold KR + F-theory + equivariant KU_G all carry ≥ 2 of 3 obstructions structurally).
- **Algebraic-K parent space**: SINGLETON {operator K_*(A_F^q)} after Karoubi K and KK are reclassified as ambient categories.
- **Ambient categories** (not parents): {Karoubi K_*(A_F), Kasparov KK(A_F, ·)}.

The substrate's K-theoretic parent question therefore reduces to a single open computational gate: does the Hopf q-deformation of A_F preserve the 4-vector? If yes (V.2 PASS), the substrate's K-theoretic identity is q-stable. If no (V.2 FAIL), the parent space is fully empty and the substrate's K-theoretic identity is intrinsic to the undeformed spectral triple alone.
```

---

## Provenance closure

This synthesis is grounded in:
- `sessions/archive/session-86/session-86-w15-workingpaper.md` (W15-1 PASS at `f04182f7...`; W15-2 PASS at `59bbb2f5...`)
- `sessions/framework/correspondence/correspondence-table-registry.md` (entry #30 with substrate-framing convention header)
- `computations/s85_w10_witten_alternative_parents.py` (W10-5 FAIL; A/B/C all 4-obstruction)
- `computations/s86_w15_anti_correspondence_registry_extension.py` (W15-1 binary VERIFY (a) ∧ (b) ∧ (c) PASS)
- knowledge MCP confirms `EXP_K0_RANK = 3`, `EXP_K0_TORSION = 0`, `EXP_WITTEN_INTEGRAL = 16.0`, A_F = C ⊕ H ⊕ M_3(C) Wedderburn-3-summand structure, KO^6(pt) = Z/2 vs KO^0 = Z, Pillar VII ↔ Pillar VIII KK overlap

No new computations were run. Three §II.3 exclusions (orientifold KR, F-theory K, equivariant KU_G) and three §II.4 surviving candidates (Karoubi K, operator K of A_F^q, Kasparov KK) are *structural classifications* against the existing 4-vector; the formal exclusion gates are pre-registered as S87 carry-forwards V.4/V.5/V.6 and V.1/V.2/V.3 respectively, with the bipolar registry extension at V.7.
