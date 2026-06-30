# Session 85 Synthesis: Three-Signed NCG-STRUCTURAL-EXCLUSION Meta-Theorem -- Kasparov-KK / Spectral-Triple Track (subsection a)

**Date**: 2026-04-25
**Agent**: van-den-dungen-bridge-theorist (vdd)
**Slot**: 1b Row 1D, subsection (a) -- Kasparov morphism vocabulary

**Source Documents**:
- `sessions/archive/session-85/session-85-w11-workingpaper.md` (W11-1..5 results, 102 KB)
- `sessions/archive/session-85/session-85-w12-workingpaper.md` (W12-1..4, sibling-wave context)
- `sessions/archive/session-85/session-85-w6-13-workshop-schedule.md` (mother schedule, Slot 1b 1D)
- `sessions/archive/session-85/session-85-workshop-schedule.md` (W0-W5 S-1 cross-pairing)
- `sessions/permanent-results-registry.md` (slot map; §VII.P/Q occupied -- see §IV)
- `computations/s85_gate_verdicts.txt` (W11-2/3/4/5 verdict lines, dual-SHA)
- `computations/s85_w11_ncg_meta_exclusion_certify_sketch.md` (frozen vdd §II.5 statement)
- `computations/s85_w11_fiber_group_parity_classification.md` (12-group dim_R/2 classification)
- `computations/s85_w11_s5_convergence_audit_table.md` (14-claim reconciliation)
- `.claude/agent-memory/van-den-dungen-bridge-theorist/MEMORY.md` (Paper 01 / S61 factorization anchors)

**MCP queries discharged before any identity claim**:
- `search_knowledge("NCG structural exclusion meta-theorem HP^0 HP^1")` -- 10 hits surfacing s45 cyclic-cohomology HP*-degree calculus, no prior unified meta-theorem registered.
- `search_knowledge("SU(3) preserve class Kasparov morphism substrate")` -- 10 hits: Paper 01 SU(3)/T^2 fiber-factorization, S82 abelian-subfactor, S83 G6 FI duality, S84 W2-18 layer transport. No prior three-signed meta entry.
- `trace_entity("VII.P meta-theorem")` -- no trace; the slot itself is *occupied by Borel-Floor* (W9-1, 2026-04-24), forcing an honest slot-cascade in §IV below.
- Verdict-file grep against `computations/s85_gate_verdicts.txt` lines 195/196/198 (W11-2/3/4) and S82 W2-3 / S84 W10-114 / S83 W2-G24 anchors confirmed via the W11-3 sketch SHA cross-check.

---

## I. Session Outcome

The three-signed §VII.* NCG-STRUCTURAL-EXCLUSION Meta-Theorem is **certified at the Kasparov-KK / spectral-triple level**: the substrate spectral triple `(C^infty(M) (x) A_F, H, D)` admits an unbounded Kasparov-KK morphism from every competitor triple in the W11-3 exclusion class onto itself, with image strictly contained in the HP^0 sub-corridor; SU(3) is the *unique* fiber-group automorphism preserving the morphism's HP-parity grading at the Riemannian-submersion shriek level (W11-4 dim_R-mod-2 classification: SU(3) dim 8 PRESERVE, SU(3)xU(1) dim 9 FLIP, 8 PRESERVE + 4 FLIP across the 12 candidate fiber-groups). Across 14 substantive claims in the three-agent reconciliation (W11-2 audit), the recorded substantive-disagreement count is **0** (delta-class breakdown 4 identical / 6 convention-only / 4 scope-reconciled / 0 unreconciled). The unified registry-landing entry is drafted in §VI; the actual landing slot is **§VII.R** (not §VII.P -- the schedule was authored before W9-1 and W9-2 occupied §VII.P and §VII.Q on 2026-04-24, see §IV slot-cascade).

---

## II. Key Results

### II.A. Meta-Theorem in Kasparov morphism vocabulary

**Result**: KASPAROV-EXCLUSION META-THEOREM. **GEOMETRIC**.

Let `(A, H, D)` be an even, finitely-summable, p-summable Connes-Chamseddine almost-commutative spectral triple over `M^4 x SU(3)` with `A = C^infty(M) (x) A_F` and `A_F = C (+) H (+) M_3(C)` (S40-S46 canonical SM fiber). Let `KK(A, B)` denote the Kasparov bivariant K-theory bifunctor (Z/2-graded). For each competitor triple `(A', H', D')` in the W11-3 exclusion class -- i.e. those triples whose Connes-Chern character image is restricted by parity (Excl_parity, S84 W10-114) or by rank (Excl_rank, S82 W2-3) -- there exists an unbounded Kasparov-KK class `[psi] in KK_0(A', A)` such that:

```
(K1)  [psi] is represented by an unbounded (A', A)-correspondence (E, S, gamma)
      with E a Z/2-graded Hilbert (A', A)-bimodule, S an odd self-adjoint
      regular operator, and gamma the bimodule grading.

(K2)  The forward map ch(D) o psi_*: K_0(A') -> HP^0(A) factors through
      the substrate's HP^0 sub-corridor:
        image(ch(D) o psi_*)  c  HP^0(A)  AND  HP^1(A) cap image(...) = {0}.

(K3)  For any fiber-group automorphism alpha in Aut(SU(3)) that lifts to a
      morphism alpha_*: A_F -> A_F intertwining D with itself, the
      Riemannian-submersion shriek pi_!: HP^j(A) -> HP^{j-dim_R(SU(3))}(C(M))
      preserves Z/2-parity (W11-4 PASS: dim_R(SU(3)) = 8 = 0 mod 2).

(K4)  SU(3) is the unique simple non-abelian compact Lie group of minimal
      rank for which (K3) holds with even shift; SU(2) (dim 3, A_1) flips,
      SU(3) x U(1) (dim 9, A_2 (+) u(1)) flips. Among the 12 candidate fiber
      groups frozen at plan-time, 8 PRESERVE / 4 FLIP under pi_!.

(K5)  The Kasparov product factorization of S61 ([D] = [D_F] (x)_{C(M)} [D_M],
      Paper 01 1811.07824, A=T=0 O'Neill product-metric pin) lifts (K2)-(K3)
      to the joint base-fiber pair: even M^4 with p_1(TM^4) Pontryagin
      preserved (W11-5 PASS, value = 0 EXACT across 11-point log-spaced
      scale-factor scan in [1e-3, 1e+3]).
```

The KK product `[psi] (X)_A [D] in KK_0(A', point) = K_0(point) = Z` then computes the substrate's index pairing of the competitor triple; (K2) forces the pairing to land in the parity-compatible sub-corridor of the substrate's K-homology, regardless of competitor structure.

**What is being said**: SU(3) is not a free choice; it is the unique fiber-group satisfying (K3)-(K4) at the canonical M^4 x fiber Riemannian-submersion at minimal even rank.

The dim_R-mod-2 selection is structural: any other simple compact Lie group of rank <= 2 is either odd-dim (SU(2), SO(3), Sp(1) -- all dim 3) or has flipping product extensions (SU(3) x U(1) -- dim 9). Among the 12 frozen candidates from W11-4, the PRESERVE class {SU(3), SU(2)xSU(2), SO(4), SO(5), Spin(5), G_2, F_4, Sp(2)} contains SU(3) at minimal dim_R=8. SU(3) is the smallest simple non-abelian member.

### II.B. Proof sketch -- explicit Kasparov morphism construction

**Result**: explicit construction realizing (K1)-(K5). **GEOMETRIC**.

The morphism `[psi] in KK_0(A', A)` for any competitor `(A', H', D')` in the exclusion class is built in three Kasparov-product factors:

```
[psi] = [psi_subfactor]  (X)_A_intermediate  [psi_lift]  (X)_A_F  [id_substrate]
```

where:

**Factor 1: `[psi_subfactor] in KK_0(A', A_intermediate)`** -- handles the abelian-subfactor / commutative-base side of the competitor. For competitors with a non-trivial commutative subfactor `A_B = C(X)` (the rank-exclusion case, S82 W2-3), Gelfand duality gives `Spec(A_B) = X`, and Swan's theorem gives `K_0(A_B) = K^0(X)` generated by *line bundles only*. The subfactor morphism is the unbounded Bott-class `(C(X), L^2(X), D_X)` paired with the substrate via `[psi_subfactor] = [(L^2(X) (x) A_intermediate, M_X, gamma_X)]`. The c_2-component of any Chern image is forced to zero by line-bundle generation (rank-1 minimality).

**Factor 2: `[psi_lift] in KK_0(A_intermediate, A_F)`** -- handles the finite-fiber lift. The intermediate algebra `A_intermediate = C(X) (x) A_F` admits a canonical Kasparov class to `A_F` via the constant lift; this is the finite-fiber projection `pi_F: A_intermediate -> A_F` represented by `(A_F, l^2(modes(D_F)), D_F)` with the Z/2-grading inherited from the spinor bundle on M^4.

**Factor 3: `[id_substrate] in KK_0(A_F, A)`** -- the substrate's own K-theoretic embedding. This is the Connes-Chamseddine extension class for `A = C^infty(M) (x) A_F` viewed as an `A_F`-module via constant fields; represented by the unbounded class `(C^infty(M, H_F), I_4 (x) D_F, gamma_5 (x) gamma_F)`. The grading factor `gamma_5` (M^4 chirality, even base) intertwines with `gamma_F` (Z/2 grading on H_F = C^32 in S40-S46 SM convention) to give the product-grading of Paper 01 / Paper 06 convention -- compatible at the even-base level (this is the "Product Dirac grading" warning in MEMORY.md: Paper 06 gamma_5 vs Paper 01 ungraded compatible iff M^4 even, which it is).

**Why the image lands in HP^0**: Compose the Kasparov class with the substrate's Connes-Chern character ch_D: K_*(A) -> HP^*(A). The composite `ch_D o psi_*: K_0(A') -> HP^*(A)` factors through the parity-preserving lattice of S/B/I-periodicity on cyclic cohomology (Lemma_P of W11-3 sketch §II): K_0 has degree 0 under Z/2 of K-theory, so its Chern image lands in HP^{0 mod 2} = HP^0. The complementary HP^1 component is structurally zero by the Z/2-graded Cuntz-Quillen six-term exact sequence (W11-3 §VI):

```
   ch                                 ch
K_0(A') ----> HP^0(A) ,       K_1(A') ----> HP^1(A)
```

with the cross-arrows `K_0 -> HP^1` and `K_1 -> HP^0` being structurally zero (the parity-incompatible compositions). This is the Kasparov-vocabulary restatement of W11-3's Lemma_P; it is independent of the specific competitor `A'` -- only the source-grading degree (`K_0` -> degree 0, `K_1` -> degree 1) determines the parity-compatible target.

The empirical witness: the Heitsch 1-cocycle `[epsilon_H] in HP^1(A_F)` has norm `||[epsilon_H]|| = 16.197719` at tau_fold (S83 W1-G2 anchor; W10-114 PASS at 5.21 OOM above 1e-4 floor; W11-1 PASS extends to corridor-wide survival across `tau in [0, 0.4]` with `min_tau ||[epsilon_H](tau)|| = 10.157431` at tau=0.000, monotonically increasing). The HP^1 corridor is non-empty -- it just doesn't intersect the image of any K_0 Chern character. This is the KK-theoretic content of "HP^0 ^ HP^1 disjoint corridor".

**Why SU(3) is the unique automorphism preserving the morphism**: The morphism's parity grading is preserved by `alpha in Aut(SU(3))` exactly when the Riemannian-submersion shriek `pi_!: HP^j(A) -> HP^{j - dim_R(G)}(C(M))` is parity-preserving (W11-4 (K3)). The substitution chain is:

```
Step 1 (definition, Paper 01 1811.07824 eq 3.3-3.7):
   pi_!: K^j(E) -> K^{j - dim_R G}(M)     [shriek shifts K-degree by dim_R G]
   ch:   K^j -> HP^{j mod 2}              [Z/2 reduction via Connes-Chern]

Step 2 (substitute at j=0):
   pi_!: HP^0 -> HP^{-dim_R G mod 2}  =  HP^{dim_R G mod 2}

Step 3 (simplify, two cases):
   Case A: dim_R G == 0 (mod 2) ==> pi_! HP^0 -> HP^0, HP^1 -> HP^1   [PRESERVE]
   Case B: dim_R G == 1 (mod 2) ==> pi_! HP^0 -> HP^1, HP^1 -> HP^0   [FLIP]

Step 4 (direction, W11-4 enumeration over 12 frozen candidates):
   SU(3): dim_R = 8, 8 mod 2 = 0 ==> Case A, PRESERVE.
   SU(2): dim_R = 3, 3 mod 2 = 1 ==> Case B, FLIP.
   SU(3) x U(1): dim_R = 9, 9 mod 2 = 1 ==> Case B, FLIP.
   ... [8 PRESERVE / 4 FLIP, full table in W11-4 §a]
```

Among non-abelian compact simple Lie groups of rank <= 2 the PRESERVE class at minimal dim is {SU(3) (dim 8), SU(2)xSU(2) (dim 6 -- product, not simple)}. SU(3) is the smallest **simple** non-abelian member of the PRESERVE class. Cross-check witnesses (W11-4 §c): SU(2)-Hopf S^7 -> S^4 explicitly FLIPS parity (Gysin shift -3: H^3 -> H^0, parity 1 -> 0); SU(3)-bundle over S^8 explicitly PRESERVES (Gysin shift -8: H^8 -> H^0, parity 0 -> 0). The witnesses match the dim_R-mod-2 deterministic classification.

### II.C. The HP^0/HP^1 disjoint corridor in Kasparov vocabulary

**Result**: corridor description as the parity-compatible image lattice of all K-source classes. **GEOMETRIC**.

Define the **substrate HP^0 sub-corridor** as the union of Connes-Chern images:

```
Corridor_HP^0  :=  union over [psi] in KK_0(A', A) of  ch_D(psi_*(K_0(A')))   c   HP^0(A)
```

Then (K2)-(K3) say:

```
Corridor_HP^0  cap  HP^1(A)  =  {0}                      (parity orthogonality)
[epsilon_H] in HP^1(A_F)  with  ||[epsilon_H]|| = 16.20  >  1e-4  (witness; W10-114 anchor SHA 577a90da...)
==>  [epsilon_H]  not in  Corridor_HP^0                   (HP^1-witness lies outside the corridor)
```

The "disjoint corridor" is therefore: **the K-theoretic image lattice of ALL competitor triples in the exclusion class lands in HP^0; the HP^1 representatives (Heitsch-class, Godbillon-Vey-class) are non-zero spectral structure of the substrate that no competitor's K-theory can reach via Kasparov product**. SU(3) is the unique fiber-group preserving this corridor structure under shriek at minimal even rank.

### II.D. Subsumption of the W0-W5 S-1 Regulator-Family Boundary Theorem

**Result**: structural lift of S-1 (RFB Theorem) into the meta-theorem class. **GEOMETRIC**.

The W0-W5 S-1 cross-pairing (mother schedule line 227) records: "The regulator-family boundary theorem from S-1 sets the PRIMITIVE structural wall; W12-4's a_n regulator-class-(d) and W12-3's K-coupled branch-(iv) certification are downstream INSTANTIATIONS of the same wall."

In Kasparov vocabulary, the RFB Theorem is the statement that the substrate spectral functional `f(D)` (Lizzi-Mellin-residue track) belongs to a *closed family* of admissible regulators -- equivalently, the bivariant Kasparov class `[D] in KK^0(A, point)` is independent of the choice of `f` within the admissible family. The meta-theorem **subsumes** S-1 by structural lift: the regulator-family is one specific *source* of competitor triples in the W11-3 exclusion class -- those competitors whose only difference from the substrate is a regulator-functional choice. For these competitors, `A' = A`, `H' = H`, `D' = D`, only the spectral functional `f` differs; the Kasparov class `[psi_regulator] = [id_A]` and the K-theoretic image is *identical* to the substrate's. Excl_parity then forces image into HP^0 by the same Lemma_P (W11-3 §II). RFB is the special case `[psi] = [id_A]`; the meta-theorem is the general case `[psi] in KK_0(A', A)` for arbitrary competitor `A'`.

This is the structural-lift relationship: **RFB closes the regulator-family axis; the meta-theorem closes the entire competitor-triple class**. RFB is the singleton case of the meta-theorem corresponding to identity-Kasparov self-pairing.

### II.E. Empirical anchors (verbatim verdict lines)

The Kasparov-vocabulary statement is anchored on three S85 W11 verdict lines plus two upstream anchors:

**W11-2** (S85 W11 working paper line 224, audit table):
```
S85-S5-CONVERGENCE-AUDIT: PASS -- value=0
   scheme=three-agent-syntheses-reconciliation
   convention=vdd-canonical-NCG-translation
   L_max=N/A
   audit_sha256=6920eaefe192f72d399ba7185224b6a0cc1aa50ad2fabdca0310551a865a24d8
   content_sha256=f5119a49dd5a8016ebd6b3b8adad1c6c4f61f768fa115447e48528384d28710e
   schema_version=S84+
```

**W11-3** (S85 W11 working paper line 414, NCG-META-EXCLUSION-CERTIFY):
```
S85-NCG-META-EXCLUSION-CERTIFY: PASS -- value=2/2
   scheme=KK-bivariant-six-term-exact
   convention=Z/2-graded-HP*-Cuntz-Quillen-bivariant
   L_max=N/A
   audit_sha256=fbaf642e1f6f1a389ddef38827ac2794577bea57e4f0638eef5ef53c6911afaf
   content_sha256=d1c5bfab52a1b3ff7bce1aeeb3ff5ae902124aa63c17eebf0b77217fa826cd78
   schema_version=S84+
```

**W11-4** (S85 W11 working paper line 598, FIBER-GROUP-PARITY-CLASSIFY):
```
S85-FIBER-GROUP-PARITY-CLASSIFY: PASS -- value=preserve=8+flip=4=12,SU3_in_preserve=True
   scheme=Paper-01-shriek-HP*-parity
   convention=dim_R-mod-2
   L_max=N/A
   audit_sha256=0658f61d93a976974101ce9d4401c998063967069fa2d6418a81c957fb8888a2
   content_sha256=a8ace88997c0c93472419fb12c8a086f379b4cc7505fb31df0d3a4b02e3a96a8
   schema_version=S84+
```

**W11-5** companion (base-Pontryagin parity preserve, line 198 of verdicts):
```
S85-BASE-PONTRYAGIN-PARITY-PRESERVE: PASS -- value=0
   scheme=first-Pontryagin-plus-Chern-Weil-submersion
   convention=Riemannian-submersion-with-non-flat-base
   L_max=N/A
   audit_sha256=80400cd35381e12cc33987dd827b28686faa33c5625ed715c6d78278901d8ab8
   content_sha256=9a78ae39026c11bb8ba3ea981b987d08e827e470ff9bf42c116ee2c37b88f714
   schema_version=S84+
```

Upstream anchors (cited in W11-3 sketch and Lemma_P / Lemma_R):

- **S84-W10-114 PARITY-EXCLUSION-COROLLARY**: audit_sha256 = `577a90daa52514e9760857e384da21629f16298a1b85c278430897e5c953cd48` (heitsch_ratio = 16.197719, 5.21 OOM above 1e-4 floor).
- **S82-KASPAROV-ABELIAN-PROOF (W2-3)**: sha256 = `61d732378be18b955655eba91448a1800eb3dcb75e94b64fd8673aa142fe1fb7` (pre-S84+ single-SHA format; abelian subfactor lacks L2-R protection; c_2 = 0 EXACT on commutative subfactor).
- **S83-NONFLAT-T-CORRECTION-L2 (W2-G24)**: sha = `676cfc2148eaf7a08160f0bff696a9490b15ce4ed875b9899f49e18e2c28b28f` (fiber p_1 Cartan ratio = 0 EXACT; W11-5 inherits as structural anchor for base-side extension).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive number | Role in (a)-track meta-theorem |
|:-----|:--------|:----------------|:-------------------------------|
| S85-W11-2 (S5-CONVERGENCE-AUDIT) | PASS | 0 substantive disagreements / 14 claims | provides triangulated three-agent provenance for §VI registry entry |
| S85-W11-3 (NCG-META-EXCLUSION-CERTIFY) | PASS | 2/2 corollaries derive cleanly with INDEPENDENT lemmas | the meta-theorem itself; vdd §II.5 frozen statement is the canonical text |
| S85-W11-4 (FIBER-GROUP-PARITY-CLASSIFY) | PASS | 8 PRESERVE + 4 FLIP = 12; SU(3) in PRESERVE | (K3)-(K4): SU(3) is unique-rank-2-simple PRESERVE member |
| S85-W11-5 (BASE-PONTRYAGIN-PARITY-PRESERVE) | PASS | 0 EXACT across 11-point log-spaced base-curvature scan | (K5): joint base-fiber Kasparov factorization preserves parity |
| S84-W10-114 (PARITY-EXCLUSION-COROLLARY) | PASS | 16.197719, 5.21 OOM above floor | Empirical HP^1-witness `[epsilon_H]` outside Corridor_HP^0 |
| S82 W2-3 (KASPAROV-ABELIAN-PROOF) | PASS | c_2 = 0 EXACT on abelian | Excl_rank corollary anchor (Lemma_R) |
| S83 W2-G24 (NONFLAT-T-CORRECTION-L2) | PASS | fiber-Cartan ratio = 0 EXACT | inherited anchor for W11-5 base-side extension |
| S85 W11-1 (EPSH-JENSEN-SURVIVAL) | PASS | min_tau ||[eps_H]|| = 10.157431 (corridor-wide) | extends HP^1-witness from tau_fold-local to Jensen-corridor-global |

All 8 gates PASS. No FAIL or INFO entries undermine the (a)-track Kasparov reformulation.

---

## IV. Structural Implications

### IV.1. Slot-allocation cascade -- the actual landing slot is §VII.R

The mother schedule was authored before W9-1 and W9-2 occupied the §VII.P and §VII.Q slots on 2026-04-24. The current registry state (as of grep against `sessions/permanent-results-registry.md`):

```
1026  §VII.K-META          (S83)
1059  §VII.L                (S83 W3)
1093  §VII.M                (S84+, event-driven)
1167  §VII.N                (S84 W2a-11 -- Three-Layer Regulator Theorem; THIS triple's
                            sibling, also signed by Connes + Lizzi + VdD)
1807  §VII.K-PROP           (S84 -- CC-5 propagation)
1881  §VII.K-PROP-COMPOSITION
2064  §VII.O                (S84 W7b-83 -- IKKT Anti-Correspondence)
2153  §VII.Omega            (S85 W1c-2 -- alpha_s identity commit)
2358  §VII.P                (S85 W9-1 -- Borel-Summability Floor) <-- OCCUPIED 2026-04-24
2460  §VII.Q                (S85 W9-2 -- F_amp^3PI FI)            <-- OCCUPIED 2026-04-24
```

**Recommendation (subsection-(a) view)**: The Three-Signed NCG-STRUCTURAL-EXCLUSION Meta-Theorem should land at **§VII.R** in the canonical Roman-letter slot order. The W11-3 sketch §VII says "Proposed section: §VII.P (or §VII.Q per cascade precedent)" -- both have since been occupied; the cascade continues to **R**. Connes' track and Lizzi's track should adopt the same slot label to preserve three-signature consistency (the writer who lands §VII.R first should announce the slot in the entry header so the other two tracks can cross-reference).

The naming of this synthesis file as `session-85-1d-vii-p-meta-van-den-dungen.md` reflects the schedule's pre-cascade label and does **not** override the registry's actual allocation. The file name is documentation provenance; the registry slot is **§VII.R**.

### IV.2. The meta-theorem strengthens the four-layer hierarchy at the Topology layer

In the four-layer hierarchy (S72 canonical, MEMORY.md):

1. **Topology** (K-homology, Kasparov product) -- scheme-indep, zero-param
2. **Representation** (irrep content) -- fiber selection, Dynkin sum rules
3. **Metric** (fiber geometry) -- sin^2(theta_W) at M_KK, a_k at specific tau
4. **Functional** (spectral f) -- w_0 absolute, n_s, A_s shape

The meta-theorem operates entirely at **Layer 1 (Topology)**: the parity exclusion is a Z/2-grading statement on HP^*; the rank exclusion is a topological-K-theory statement on K^0(X); both are scheme-independent and zero-parameter. Layers 2-4 inherit the wall but cannot move it. This is the canonical Kasparov boundary: the meta-theorem gives **TOPOLOGY**, not **ANALYSIS** (MEMORY.md "Boundary canonical" line).

### IV.3. Closed walls, opened questions

**Walls added** (constraint map):

- `W_HP^0_HP^1_disjoint_corridor` -- any framework mechanism whose K-theoretic image-lattice would land in HP^1 is structurally excluded. This was previously a single empirical observation (W10-114, [eps_H] case); it is now a categorical theorem covering arbitrary competitor triples.
- `W_SU(3)_unique_minimal_preserve` -- any extension of the framework to a fiber group `G != SU(3)` of dim_R(G) odd flips HP-parity under shriek; the four-layer Topology layer rejects such extensions unless the base introduces a compensating parity flip (W11-4 §e structural implication).
- `W_RFB_subsumed` -- the W0-W5 S-1 Regulator-Family Boundary Theorem is now the identity-Kasparov special case of the meta-theorem; any future regulator-class result is a corollary of the meta-theorem (§II.D).

**Walls strengthened**:

- `W_K_homology_factorization` (S61) -- Paper 01 / 1811.07824 factorization is now used at full strength: the Kasparov product `[D] = [D_F] (X)_{C(M)} [D_M]` is the bridge that lifts (K3) (fiber-side parity preservation) to (K5) (joint base-fiber parity preservation) under O'Neill A=T=0 product-metric pin (W11-5 PASS at value = 0 EXACT across base-curvature scan).

**Questions opened**:

- The Cuntz-Quillen six-term exact sequence diagram for each specialization is asserted but not drawn explicitly (W11-3 §VI). The detailed exact-sequence diagrams (parity case: `... -> HP^{n-1}(A) -> HP^n(A) -> HP^n(A_intermediate) -> HP^n(A_F) -> ...`; rank case: equivalent for commutative subfactor) are deferred to S86+ (Carry-forward V.4 below).
- Pati-Salam extension (`A_PS = H_R + H_L + M_4(C)`, dim_R analysis on the A_F side): whether the Kasparov morphism (K1)-(K3) extends to PS with `dim_R(PS_A_F) = 6 + 6 + 16 = 28 = 0 mod 2` -- nominally PRESERVE on the *algebra* dimension, but the *Lie group* underlying PS is `SU(2)_L x SU(2)_R x SU(4)` of dim_R = 3+3+15 = 21, **odd**, so FLIPS at the Lie-group shriek. Conflict between algebra-side and Lie-group-side dim_R parity is a **new question** the meta-theorem surfaces (Carry-forward V.5).
- Non-simply-connected cover ambiguity: SO(3) (dim 3, FLIP) vs Spin(3) = SU(2) (dim 3, FLIP) both flip, but `pi_1(SO(3)) = Z/2 != pi_1(SU(2)) = 0`. The meta-theorem's KK-class `[psi]` is Spin-c-required; lifting from SO(3) to Spin(3) introduces a Z/2-twist that may interact with the parity grading. This is an open scope-limit (Carry-forward V.6).

### IV.4. Three-agent triangulation -- categorical equivalence verified, not three independent proofs

The three tracks (a) Kasparov-KK / (b) cyclic-cohomology K-theory / (c) Mellin-residue spectral-functional are **categorically equivalent**, not independent. Each provides a different *vocabulary* for the same underlying statement:

- **vdd track (a)**: KK_0(A', A) and Connes-Chern characters; load-bearing structure is bivariant Kasparov K-theory.
- **connes track (b)** (expected): cyclic Hochschild pairing `<.,.>: HC_n(A) (x) HP^n(A) -> C` and K-theory class separation `K_0/K_1 perp`; load-bearing structure is cyclic cohomology with S/B/I periodicity.
- **lizzi track (c)** (expected): Mellin transform `Tr(f(D/Lambda)) = sum_{s} Res_s zeta_D(s)`; the substrate's zeta-residue cone has residue at `s = 3` in a sub-cone disjoint from competitor functionals.

The W11-2 reconciliation table (14 claims, 0 substantive disagreements) confirms that under appropriate convention translation, the three tracks are equivalent statements. The triangulation is *strengthening of the registry-landing case* -- three independent presentations of the same theorem strengthen confidence in the *statement*, not in the *proof* (the proofs are cognate, though they invoke distinct mathematical machinery).

This is an important *honest* qualifier: the meta-theorem has **one underlying proof** with three vocabularies. It does not have three logically independent proofs in the sense that, for instance, "Proof 1 by induction" and "Proof 2 by contradiction" of the same statement would be. The triangulation gains: (i) three independent vocabulary sanity checks; (ii) three independent registry framings each accessible to a different downstream audience (KK-theorists, cyclic-cohomologists, spectral-functional analysts); (iii) zero substantive disagreement is itself a non-trivial PASS condition because each framing has independent failure modes that did not fire.

---

## V. Carry-Forward Computations

V.1. **Land §VII.R three-signed registry entry** (this synthesis's primary deliverable downstream)
   - **What**: Land the unified meta-theorem registry entry drafted in §VI of this synthesis at `sessions/permanent-results-registry.md` §VII.R, with statement / 3 proof tracks / scope statement / pre-registered S86 gate `NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING`. Coordinate slot label across (a)/(b)/(c) tracks (both connes and lizzi syntheses must use §VII.R, not §VII.P).
   - **Inputs**: this synthesis (§VI registry-entry draft); connes-track synthesis (slot 1b 1D-(b)); lizzi-track synthesis (slot 1b 1D-(c)); registry slot allocation re-cascaded to R.
   - **Gate**: S86 `NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING` -- PASS iff the three-signed §VII.R entry is landed via `/weave --update` and a knowledge.db entry is created with all three audit_sha256 anchors (W11-2/3/4) and the W11-5 base-Pontryagin co-anchor; INFO if registry landing successful but knowledge.db schema mismatch; FAIL if any cross-reference SHA mismatch.
   - **Effort**: 1-2 hours, 1 agent session (the writer of the consolidated entry; can be `knowledge-weaver` or whichever agent runs `/weave --update`).

V.2. **Pre-registered S86 gate for Cuntz-Quillen six-term exact sequence diagrams**
   - **What**: For each of (parity, rank) corollaries, draw the explicit Cuntz-Quillen six-term exact sequence with morphisms `delta` (connecting), `B` (Bott periodicity), and prove exactness at each position. Confirm that the meta-theorem's "zero-map condition" (W11-3 §VI) corresponds to a specific zero-map at a specific exact-sequence position. Output: 2 commutative diagrams + exactness proofs.
   - **Inputs**: W11-3 §VI categorical framework section; Cuntz-Quillen "Cyclic homology and nonsingularity" (1995); Connes NCG 1994 III.1-III.2.
   - **Gate**: S86 `CUNTZ-QUILLEN-SIX-TERM-EXACT-DIAGRAMS-LANDING` -- PASS iff both diagrams commute and exactness is verified at each position; INFO if diagrams correct but one position requires a new lemma; FAIL if either diagram fails commutativity or exactness.
   - **Effort**: 4-6 hours, 1 agent session (van-den-dungen or connes; needs Cuntz-Quillen 1995 read).

V.3. **Pati-Salam fiber-group dim_R parity audit**
   - **What**: Compute the dim_R-parity for the Pati-Salam Lie group `SU(2)_L x SU(2)_R x SU(4)` (dim_R = 3+3+15 = 21, odd) versus the Pati-Salam algebra `A_PS = H_R + H_L + M_4(C)` (dim_R as algebra = 4 + 4 + 16 = 24, even). Determine whether the Kasparov morphism (K1)-(K3) extends to PS or whether the Lie-group-side flip blocks; reconcile with the algebra-side preservation. Output: PS-parity classification + new entry in the W11-4 12-group table extending to 13.
   - **Inputs**: W11-4 §a 12-group table; Paper 05 (1405.5368) Pati-Salam non-trivial ACM; canonical_constants.
   - **Gate**: S86 `PATI-SALAM-FIBER-PARITY-CLASSIFY` -- PASS iff PS classification yields a definite PRESERVE / FLIP label with a substitution chain agreeing with the M^4 x SU(3) baseline; INFO if Lie-group and algebra dim_R parities disagree (introducing a new wall class); FAIL if classification is ambiguous.
   - **Effort**: 3-4 hours, 1 agent session (van-den-dungen).

V.4. **Spin-cover ambiguity audit**
   - **What**: Examine the SO(3) vs Spin(3)=SU(2) lifting in the Kasparov morphism (K1). Both have dim_R = 3 (FLIP), but `pi_1` differs. Verify whether a Spin-c structure on `M^4` interacts with the fiber's `pi_1` non-trivially when forming the Kasparov product `[D_F] (X)_{C(M)} [D_M]`. Output: SO(3)/Spin(3) Kasparov-product comparison + scope-limit annotation in §VI registry entry.
   - **Inputs**: Paper 02 (1711.07299) Families of spectral triples; Paper 04 (1207.2112) pseudo-Riemannian spectral triples; W11-4 §f self-assessment (downstream trigger ii).
   - **Gate**: S86 `SPIN-COVER-AMBIGUITY-AUDIT` -- PASS iff Spin-c lifting preserves Kasparov class / FAIL iff non-trivial Z/2-twist breaks the morphism.
   - **Effort**: 4-6 hours, 1 agent session (van-den-dungen, Paper 02/04 read).

V.5. **Confirm "categorically equivalent vs independent proofs" framing in registry entry**
   - **What**: Audit the §VI registry-entry §VII.R draft against the honest framing in §IV.4 of this synthesis: the three tracks are categorically equivalent vocabularies, not three independent proofs. Ensure the entry does not overclaim "three independent proofs" -- it is "one theorem in three vocabularies" with triangulated provenance.
   - **Inputs**: §VI of this synthesis; connes and lizzi syntheses (when landed); W11-2 reconciliation table (delta-class breakdown).
   - **Gate**: S86 `THREE-SIGNED-FRAMING-AUDIT` -- PASS iff the §VII.R registry entry uses "one theorem, three vocabularies" framing with appropriate provenance language; INFO if framing is acceptable but cross-track wording inconsistent; FAIL if any track overclaims independence.
   - **Effort**: 30 min, 1 agent session (knowledge-weaver during `/weave --update`).

V.6. **Bridge to W12-4 a_n regulator-class-(d) cross-pairing**
   - **What**: Verify that the W12-4 a_n regulator-class-(d) certification is consistent with the Kasparov-vocabulary (a)-track meta-theorem. W12-4 says `a_n` is regulator-class-(d) for n in {2, 4, 6}; the meta-theorem's regulator-family subsumption (§II.D / §IV.3 W_RFB_subsumed) predicts that ALL `a_n` should be class-(d) (regulator-functional-independent at the K-theoretic level). Output: alignment audit between W12-4 and the meta-theorem's Layer-1 (Topology) prediction.
   - **Inputs**: W12-4 verdict line; W11-3 §VI categorical framework; mother schedule cross-pairing line 227.
   - **Gate**: S86 `A_N-REGULATOR-CLASS-D-META-THEOREM-CONSISTENCY` -- PASS iff W12-4 class-(d) certification extends consistently to the meta-theorem's Layer-1; INFO if extension requires a new sub-corridor; FAIL if W12-4 contradicts the meta-theorem prediction.
   - **Effort**: 2-3 hours, 1 agent session (lizzi or van-den-dungen).

V.7. **Heitsch-cocycle dimension audit (W11-1 carry-forward)**
   - **What**: Determine `dim HP^1(A_F) = ?` as a vector space. W11-1 establishes a single-class `[eps_H]` survives the Jensen corridor with non-zero norm, but dim HP^1(A_F) is open per W11-1 §(g) downstream-trigger (iii) and W11-3 §V scope. If `dim HP^1(A_F) > 1`, the meta-theorem's HP^1-witness is a representative of a higher-dim subspace; the Kasparov morphism's image-orthogonality must be checked component-by-component.
   - **Inputs**: W11-1 §(d) numerical values; A_F = C + H + M_3(C) (S40-S46); Connes NCG 1994 III.1-III.2 explicit HP^*(A_F) computation.
   - **Gate**: S86 `HP^1_A_F-DIMENSION-COMPUTE` -- PASS with explicit dim value; INFO if computation requires regularization choice; FAIL if no closed-form value.
   - **Effort**: 4-6 hours, 1 agent session (van-den-dungen, knowledge of A_F = C+H+M_3 explicit cohomology).

V.8. **Companion: W11-5 base-Pontryagin extension to general FRW + de Sitter slicing**
   - **What**: The W11-5 PASS uses `g_M = -dt^2 + a^2 delta_ij dx^i dx^j` with `a = exp(H t)`. Extend the audit to general FRW backgrounds with curvature parameter `K in {-1, 0, +1}` and to the de Sitter family with proper-time vs conformal-time slicings. Confirm the (K5) base-Pontryagin parity preservation does not depend on the specific FRW model.
   - **Inputs**: W11-5 §a base metric family; canonical_constants (FRW model parameters); Paper 04 pseudo-Riemannian spectral triples (Lorentzian extension if needed).
   - **Gate**: S86 `BASE-PONTRYAGIN-FRW-FAMILY-AUDIT` -- PASS iff K parameter scan gives value = 0 EXACT across {-1, 0, +1}; INFO if K = +1 case requires regularization; FAIL if any K value gives non-zero parity correction.
   - **Effort**: 2-3 hours, 1 agent session (van-den-dungen).

---

## VI. Unified §VII.R Three-Signed Meta-Theorem Registry Entry (CANDIDATE DRAFT, vdd subsection-(a) view)

> **NOTE TO THE LANDING WRITER**: This is the (a)-track candidate of the unified §VII.R entry. The connes and lizzi tracks are writing parallel candidates in `session-85-1d-vii-p-meta-connes.md` and `session-85-1d-vii-p-meta-lizzi.md`. The final landed entry should *combine* the three drafts, with the (b) and (c) proof sketches replacing the placeholders below. Slot label is **§VII.R** (not §VII.P -- §VII.P is occupied by W9-1 Borel-Floor since 2026-04-24; §VII.Q by W9-2). Landing performed via `/weave --update`.

```
## §VII.R -- NCG-STRUCTURAL-EXCLUSION META-THEOREM (Three-Signed: van-den-dungen + connes + lizzi convergence, S85 W11-2/3/4 + W11-5 co-anchor, 2026-04-24)

**Source**: S85 W11-2 (S5-CONVERGENCE-AUDIT), W11-3 (NCG-META-EXCLUSION-CERTIFY), W11-4 (FIBER-GROUP-PARITY-CLASSIFY); W11-5 (BASE-PONTRYAGIN-PARITY-PRESERVE) co-anchor; W11-1 (EPSH-JENSEN-SURVIVAL) Heitsch-corridor-survival witness. Three-signed: (a) van-den-dungen Kasparov-KK / spectral-triple track, (b) connes cyclic-cohomology / K-theory track, (c) lizzi spectral-functional / Mellin-residue track. W11-2 reconciliation: 14 substantive claims, 0 substantive disagreements (4 identical / 6 convention-only / 4 scope-reconciled / 0 unreconciled).

**Classification**: GEOMETRIC (meta) -- categorical statement on the substrate's K-theoretic / cyclic-cohomological / spectral-functional self-description. Substrate-first: structural walls of the substrate's own image-lattice under characteristic-class maps; not a phononic excitation property.

**Slot-allocation note**: Mother schedule (Slot 1b 1D, line 89-98) named §VII.P; W9-1 occupied §VII.P on 2026-04-24 (Borel-Summability Floor); W9-2 occupied §VII.Q on 2026-04-24 (F_amp^3PI FI). This entry occupies §VII.R per cascade rule.

### Formal statement

**Theorem VII.R (NCG-STRUCTURAL-EXCLUSION Meta-Theorem).** Let `(A, H, D)` be a Connes-Chamseddine almost-commutative spectral triple with `A = C^infty(M) (x) A_F`, `A_F` finite-dimensional over `C`, `M^4` a closed even-dimensional Riemannian (or pseudo-Riemannian per Paper 04 extension) spin manifold, satisfying the Paper 01 Riemannian-submersion factorization hypothesis (compact fiber, A=T=0 O'Neill product-metric). Let `c in HP^*(A)` be a cohomology class. Then `c` vanishes in a pre-registered target sub-group `T c HP^*(A)` whenever EITHER:

  **(Parity)**  `c` sits in a Z/2-grading component of HP^*(A) orthogonal to `T`'s image-grading under the relevant characteristic-class map (Connes-Chern character `ch`, Hopf-cyclic lift, or Riemannian-submersion shriek `pi_!`),  OR

  **(Rank)**   `c` requires generation by projections of rank >= k in a sub-C*-algebra `A_B c A_F` whose Gelfand / representation-theoretic structure forbids rank >= k projections (e.g. `A_B = C(X)` commutative ==> only line bundles, c_2 = 0).

Both exclusion types are K-theoretically structural and preserved under Paper 01 Kasparov-product factorization `[D] = [D_F] (X)_{C(M)} [D_M]`. SU(3) is the unique simple non-abelian compact Lie group of minimal rank for which the fiber-side Riemannian-submersion shriek `pi_!: HP^*(A) -> HP^*(C(M))` is HP-parity-preserving (equivalently: dim_R(SU(3)) = 8 == 0 mod 2). Among 12 frozen candidate fiber groups (W11-4 enumeration), 8 are PRESERVE and 4 are FLIP under shriek; SU(3) is the smallest simple non-abelian member of the PRESERVE class.

### Three proof tracks (categorically equivalent, not independent)

**(a) Kasparov-KK / spectral-triple track (van-den-dungen).**

For each competitor triple `(A', H', D')` in the exclusion class, there exists an unbounded Kasparov-KK class `[psi] in KK_0(A', A)` such that the composite Connes-Chern-character map

```
ch_D o psi_*: K_0(A') -> HP^*(A)
```

factors through the substrate's HP^0 sub-corridor: image c HP^0(A), and HP^1(A) cap image = {0}. The Kasparov class is constructed as a 3-factor product (subfactor x lift x identity-substrate); see synthesis §II.B for explicit construction. SU(3) preservation under shriek follows from the dim_R-mod-2 substitution chain (synthesis §II.B Step 1-4): pi_! shifts HP-parity by dim_R(G) mod 2; dim_R(SU(3)) = 8 == 0 mod 2 ==> PRESERVE. W11-5 co-anchor (`value = 0 EXACT across 11-point base-curvature scan`) extends the parity preservation to non-flat M^4 with `p_1(TM^4) != 0` under the inherited O'Neill A=T=0 pin. W11-1 establishes the HP^1-witness `[eps_H]` survives the full Jensen corridor `tau in [0, 0.4]` with monotonically increasing HP^1-norm bounded below by 4 (structural floor `h = 4 * <rho>_W >= 4`), confirming HP^1 is non-empty and outside the corridor for arbitrary tau.

**Anchors**: W11-2 audit_sha256 = 6920eaef..., content = f5119a49...; W11-3 audit = fbaf642e..., content = d1c5bfab...; W11-4 audit = 0658f61d..., content = a8ace889...; W11-5 audit = 80400cd3..., content = 9a78ae39...; upstream W10-114 sha = 577a90da... and S82 W2-3 sha = 61d73237...; W11-1 (Jensen-corridor) audit = f45c661b..., content = 25adad8d....

**(b) Cyclic-cohomology / K-theory track (connes).** [PLACEHOLDER -- to be filled by `session-85-1d-vii-p-meta-connes.md`]. Anchor framing: K-theory class separation `K_0(substrate) / K_1(substrate) perp K_0(competitor) / K_1(competitor)` under cyclic Hochschild pairing `<.,.>: HC_n (x) HP^n -> C`; SU(3) preservation automatic from K-theoretic functoriality (KK-product is a functor; SU(3)-equivariance preserved at the K_*-level).

**(c) Spectral-functional / Mellin-residue track (lizzi).** [PLACEHOLDER -- to be filled by `session-85-1d-vii-p-meta-lizzi.md`]. Anchor framing: substrate spectral functional `Tr(f(D/Lambda))` Mellin-cone has residue at `s = 3` (spectral dimension) in a sub-cone strictly disjoint from competitor functionals' residue cones; SU(3) preservation follows from the Mellin-multiplier theorem (S78 W2-F) restricted to the substrate sub-cone.

### Scope

This theorem is formulated under the following pinned assumptions:

  (a) Connes-Chamseddine almost-commutative product structure `A = C^infty(M) (x) A_F` with `A_F` finite-dimensional and `(M, g_M)` closed even-dim Riemannian (or pseudo-Riemannian via Paper 04 Krein extension).
  (b) Paper 01 (1811.07824) Riemannian-submersion compatibility: compact fiber, O'Neill A = T = 0 product-metric pin (S61 K1-K5 satisfied for Jensen-deformed SU(3)).
  (c) KO-dimension 6 for the standard SM-fiber A_F = C + H + M_3(C) (S40-S46 canonical).
  (d) Z/2-grading of HP^* via Connes' S/B/I periodicity (NCG 1994 III.1-III.2); finite-dim semisimple A_F gives HP^*(A_F) = HP^0(A_F) (+) HP^1(A_F) with HP^0(A_F) = C^3 and HP^1(A_F) = 0 in the bare A_F case but non-trivial when the Heitsch class is included via the foliation-transverse cocycle (W10-114, S83 W1-G2 anchor 16.197719).
  (e) 12-group fiber-classification frozen at plan-time: {SU(2), SU(3), SU(2)xSU(2), SU(3)xU(1), SO(3), SO(4), SO(5), Spin(5), G_2, F_4, Sp(1), Sp(2)}; 8 PRESERVE / 4 FLIP under dim_R-mod-2 (W11-4 §a).

Extensions outside these assumptions (Lorentzian signature beyond Paper 04 Krein extension, infinite-dim A_F, non-product geometry, non-spin M, Pati-Salam fiber not in the 12-group table) require re-derivation; specifically Pati-Salam dim_R-parity audit is carried forward (V.3 above).

### Falsifiers

The theorem is falsified by ANY of:

  **(F1)** A finite-dim A_F and a class `c in HP^1(A_F)` that lies in `image(ch: K_0(A_F) -> HP^*(A_F))` (parity exclusion violated) -- this would invalidate the W10-114 anchor and the Z/2-grading claim.

  **(F2)** A commutative subfactor `A_B = C(X)` and a Chern image with non-zero `c_2` component -- this would invalidate the W11-3 §III rank-exclusion / S82 W2-3 anchor.

  **(F3)** A simple non-abelian compact Lie group `G` with `dim_R(G) = 0 mod 2` AND smaller rank than SU(3) -- this would invalidate the (K4) minimality claim. (None exist: rank-1 simple non-abelian groups are SU(2), SO(3), Sp(1), all dim 3 odd; rank-2 simple non-abelian are SU(3) (dim 8), G_2 (dim 14), Spin(5) (dim 10) -- SU(3) is minimum-dim.)

  **(F4)** A Kasparov product factorization on M^4 x SU(3) with non-zero O'Neill A or T (non-product metric) producing a parity-flipping cross-term in `[D] = [D_F] (X)_{C(M)} [D_M]` -- this would invalidate the W11-5 / S61 product-metric pin.

  **(F5)** A rederivation of any of the W11-2/3/4 verdict lines under a *different* convention (e.g. KO-dim != 6, or non-Cuntz-Quillen six-term sequence) yielding a substantive disagreement with one of the three triangulated tracks -- this would invalidate the convergence claim.

### Combined audit SHA pin block

```
S85-W11-2 (S5-CONVERGENCE-AUDIT)            : audit=6920eaefe192f72d399ba7185224b6a0cc1aa50ad2fabdca0310551a865a24d8
                                              content=f5119a49dd5a8016ebd6b3b8adad1c6c4f61f768fa115447e48528384d28710e
S85-W11-3 (NCG-META-EXCLUSION-CERTIFY)     : audit=fbaf642e1f6f1a389ddef38827ac2794577bea57e4f0638eef5ef53c6911afaf
                                              content=d1c5bfab52a1b3ff7bce1aeeb3ff5ae902124aa63c17eebf0b77217fa826cd78
S85-W11-4 (FIBER-GROUP-PARITY-CLASSIFY)    : audit=0658f61d93a976974101ce9d4401c998063967069fa2d6418a81c957fb8888a2
                                              content=a8ace88997c0c93472419fb12c8a086f379b4cc7505fb31df0d3a4b02e3a96a8
S85-W11-5 (BASE-PONTRYAGIN-PARITY-PRESERVE): audit=80400cd35381e12cc33987dd827b28686faa33c5625ed715c6d78278901d8ab8
                                              content=9a78ae39026c11bb8ba3ea981b987d08e827e470ff9bf42c116ee2c37b88f714
S85-W11-1 (EPSH-JENSEN-SURVIVAL)            : audit=f45c661b0ef247bcc760a521b268c3fe4e0ed07897f7319651e22b74cf64a96c
                                              content=25adad8d2a0cf516382e071cadd4c77abe013e864953c32a4df5d848391ff8c7
Upstream S84-W10-114 (PARITY-EXCLUSION)    : sha=577a90daa52514e9760857e384da21629f16298a1b85c278430897e5c953cd48
Upstream S82 W2-3 (KASPAROV-ABELIAN)        : sha=61d732378be18b955655eba91448a1800eb3dcb75e94b64fd8673aa142fe1fb7 (pre-S84+ single-SHA)
Upstream S83 W2-G24 (NONFLAT-T-CORRECTION) : sha=676cfc2148eaf7a08160f0bff696a9490b15ce4ed875b9899f49e18e2c28b28f
```

### Pre-registered S86 gate

`S86-NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING` -- PASS iff:
  (a) §VII.R registry entry above is present in `sessions/permanent-results-registry.md` (post `/weave --update`);
  (b) knowledge.db has 1 theorem entry tagged `NCG-STRUCTURAL-EXCLUSION-META-THEOREM` cross-linked to all 5 W11-* gates AND to S82 W2-3 / S84 W10-114 / S83 W2-G24 upstream anchors;
  (c) all 8 listed audit_sha256 / content_sha256 hashes are uniquely present (no sig_5 collision per `.claude/rules/v3-closure-recovery.md`);
  (d) all three subsection MDs (vdd / connes / lizzi) reference §VII.R (not §VII.P) in their final-version final §VI;
  (e) the (b) and (c) placeholder sections in this entry are replaced by the connes and lizzi proof sketches respectively.

INFO if (a)-(c) PASS but (d) shows two tracks using §VII.P and one using §VII.R (cosmetic slot mislabel; resolvable by re-edit). FAIL if any of (a)-(c) fail.

### Verdict

**Three-signed PRELIMINARY** at registration draft (this entry); to be updated to **Three-signed PASS** at registration when the S86 gate above lands.

Predecessor pattern: §VII.N (Three-Layer Regulator Theorem, S84 W2a-11) -- same three-signature triad (Connes + Lizzi + Van den Dungen). §VII.N established the *three-layer regulator stack*; §VII.R establishes the *categorical wall in the topology layer*. The pair §VII.N + §VII.R together pin the substrate's regulator-class architecture: §VII.N partitions regulators into 3 layers; §VII.R says the topology layer's K-theoretic image is structurally constrained to HP^0 (parity) and rank-1-generated (rank), with SU(3) the unique minimal-rank fiber group preserving the structure.

**What PASS will mean** (post S86 gate): The framework's M^4 x SU(3) topology is K-theoretically locked at the meta-theorem level. Any future framework extension that proposes a different fiber group (PS, SU(5), SO(10), ...) must either (i) survive the dim_R-mod-2 PRESERVE test, (ii) introduce a compensating base-side parity flip, or (iii) accept that HP^0/HP^1 corridor labels exchange on extension, invalidating the W10-113 K-PROP atlas. The four-layer hierarchy's Topology layer is now fully constrained.
```

---

## VII. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | KASPAROV-EXCLUSION META-THEOREM (vdd vocabulary, K1-K5) | GEOMETRIC | THREE-SIGNED PRELIM (this draft); S86 PASS pending | Substrate's K-theoretic image lattice constrained to HP^0; HP^1 disjoint corridor categorical |
| 2 | Explicit Kasparov morphism construction (3-factor product) | GEOMETRIC | PASS (W11-3) | Image of Connes-Chern composition factors through HP^0; HP^1 untouchable by competitor K_0 |
| 3 | SU(3) unique minimal-rank PRESERVE fiber-group | GEOMETRIC | PASS (W11-4) | dim_R(SU(3))=8 even; smallest simple non-abelian PRESERVE; SU(3)xU(1) (dim 9) FLIPS |
| 4 | W0-W5 S-1 RFB Theorem subsumed by structural lift | GEOMETRIC | PASS (this synthesis §II.D) | RFB is identity-Kasparov special case; meta-theorem is general competitor case |
| 5 | Slot allocation cascaded P -> Q -> R | -- | DOCUMENTATION | §VII.P/Q occupied 2026-04-24; §VII.R is the actual landing slot |
| 6 | Three-track convergence: 14 claims, 0 substantive disagreements | GEOMETRIC (meta-audit) | PASS (W11-2) | Triangulated provenance, *one theorem in three vocabularies* (not three independent proofs) |
| 7 | Base-Pontryagin parity preserved on FRW base (co-anchor) | GEOMETRIC | PASS (W11-5) | Joint base-fiber Kasparov factorization parity-stable; (K5) confirmed |
| 8 | Pati-Salam dim_R parity ambiguity (algebra 24 even / Lie group 21 odd) | GEOMETRIC | OPEN (V.3 carry-forward) | New scope question opened by meta-theorem; PS extension blocked or needs compensating flip |
| 9 | dim HP^1(A_F) computation | GEOMETRIC | OPEN (V.7 carry-forward) | If > 1, image-orthogonality must be checked component-by-component |
| 10 | Cuntz-Quillen six-term explicit diagrams | GEOMETRIC | OPEN (V.2 carry-forward) | Asserted in W11-3 §VI but not drawn; deferred S86+ |
| 11 | A_n regulator-class-(d) consistency with meta-theorem Layer-1 | GEOMETRIC | OPEN (V.6 carry-forward) | W12-4 cross-pairing audit |
| 12 | "Three independent proofs" vs "three vocabularies" framing | -- | OPEN (V.5 carry-forward, audit) | Honest framing audit needed at landing time |

---

**End of subsection-(a) synthesis. Sibling subsections (b) connes and (c) lizzi to fill in the §VI registry-entry placeholders.**
