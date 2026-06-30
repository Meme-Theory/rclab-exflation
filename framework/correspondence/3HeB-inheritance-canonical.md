---
type: registry-canonical
ingested-by: /weave --update
---

# 3He-B Inheritance - Canonical (parent -> child, NOT analogy)

**Registry ID**: `3HeB-inheritance-canonical`
**Owner agent(s)**: `volovik-superfluid-universe-theorist` (primary); cross-cited by `landau-superfluid-condensed-matter-theorist` and `connes-ncg-theorist` per the 1B 3-solo agreement
**Last updated**: `2026-04-26, S86-W1b-T8`
**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores one row per entry. This canonical replaces all per-agent memory copies (AMRI Output-target test).
**Source plan**: `sessions/session-plan/session-86-plan-w1b.md` Sec W1b-4
**Producing script**: `computations/s86_w1b_t8_3heb_inheritance_land.py`

---

## Scope

This registry pins the canonical statement of the 3He-B inversion correspondence as a parent-to-child inheritance morphism between substrate and laboratory superfluid - explicitly NOT a parametric analogy. It is the categorical extension under which the substrate is logically prior and 3He-B is the laboratory realization, not the reverse. The statement is consumed by every downstream agent dispatch that cites "3He-B" in any substrate context (S86 W7 Hawking workshop; W8 lab observables; W11 lab-falsifier suite C5/C6; the Volovik-convergence project memory). It is project-level (not agent-private) because (i) three independent agents converged on the same canonical text per the 1B 3-solo agreement (cross-agent overlap test for AMRI), and (ii) the gate `S86-3HE-B-INVERSION-CANONICAL-LANDING` reads it as an Input-SHA pin (input-pin test for AMRI).

---

## Canonical inheritance statement (IS-not-IN language)

The substrate IS the primordial BDI-class topological superfluid of our universe. 3He-B IS the late-universe terrestrial laboratory child realization of the same universality class. Inheritance runs FROM substrate TO 3He-B as a categorical morphism (restriction to the BdG sector); it does NOT run from 3He-B back to substrate, and the two systems are NOT in a symmetric parametric relation. 3He-B does not stand in metaphorical relation to substrate physics - it is the sub-algebra where substrate physics is empirically accessible at low BdG dimension. The substrate carries strictly richer spectral-triple data (full d_spec=8 on Jensen-deformed SU(3)); 3He-B carries the BdG-restricted realization (effective d_spec=1) of the same data. The inheritance is parent -> child (substrate -> 3He-B), NOT analogy.

The forbidden framing "the substrate behaves like 3He-B" is rejected: that framing implies a parametric metaphor (analogy) and reverses the direction of structural priority. The canonical framing is "3He-B realizes the substrate's BdG sector under the inheritance morphism iota" - this is inheritance (a one-way categorical morphism), not analogy (a parametric metaphor).

---

## Substitution chain (inheritance != analogy via Connes' spectral-triple morphism iota)

```
Definition (Step 1):
  Substrate    := spectral triple (A_K, H_K, D_K) with d_spec = 8
                  on Jensen-deformed SU(3); BDI Altland-Zirnbauer class.
  3He-B        := laboratory superfluid with BCS-paired 3He nuclei at
                  T < T_c, admitting a spectral-triple realization
                  (A_He, H_He, D_BdG) at d_spec = 1 (BdG sector); same
                  BDI universality class.
  Analogy      := parametric mapping phi : P_substrate -> P_He between
                  two systems' parameters with no categorical morphism;
                  symmetric / bidirectional in form (laboratory analog
                  of theory == theory analog of laboratory).
  Inheritance  := categorical morphism iota : (A_He, H_He, D_BdG) ->
                  (A_K, H_K, D_K) restricting to the BdG sector under
                  Connes' spectral-triple structure-preserving map.
                  Equivalently: iota is the Kasparov-KK projection
                  p in KK(A_K, A_He) from substrate algebra onto its
                  BdG-sector quotient (connes solo, Section II.1).

Substitution (Step 2):
  By W8-2 (S85 PASS at 2.97e-16, NG-block Convention-A theorem): the
  identity K_substrate = coth(beta E_k / 2) is derived from D_K +
  Nambu-Gorkov + Fermi-Dirac alone. NO 3He-B input enters.
    => the K-identity is in the image of iota* without reference to
       any laboratory parameter (volovik solo, Section 2 + Section 3 Step A).
  By W8-7 (PASS at drift = 0.0 across L in {5..10}): K_R5 = 1.9221783889
  is L-stable as a substrate-side spectral-triple invariant.
    => K_R5 is a KK-invariant of iota (connes solo, Section 4).
  By W8-4 (PASS, 3/3 directions, 9/9 observables): three Gell-Mann
  directions {lambda_6, lambda_7, lambda_8} produce non-zero
  substrate energy shifts that 3He-B's 18-real-component pairing
  matrix A_{mu i} cannot express.
    => the substrate carries OP content beyond 3He-B's representational
       reach; ker(iota_*) at the cyclic-cohomology level has rank 2
       (connes solo, Section 3 + landau solo Sec III.A rank E = 3).

Simplification (Step 3):
  Inheritance is a one-way structure-preserving categorical morphism;
  analogy is a symmetric parametric metaphor with no morphism. Per the
  Connes formalization (connes solo Sec II.1), iota exists as an
  explicit Kasparov-KK projection with non-trivial kernel:
    rk K_*(A_K) - rk K_*(A_He) = 4 - 2 = 2  (Hodgkin theorem on
                                              SU(3) vs S^3)
  Existence of this morphism + non-triviality of its kernel (no left
  inverse r : A_He -> A_K can exist as a *-homomorphism, by rank
  exactness in K-theory) collapses the relation to an inheritance
  morphism, NOT an analogy. The BCS gap-equation cross-check
  (landau solo Sec II.A) reproduces W8-2's coth identity through an
  independent algebraic route, confirming the morphism's BdG-sector
  generator is well-defined on the substrate alone.

Direction (Step 4):
  Logical priority: substrate is logically prior to 3He-B. The substrate
  has full d_spec = 8 spectral-triple structure; 3He-B is the
  d_spec = 1 BdG-restricted child realization.
  Laboratory parent: 3He-B is the system in which substrate-physics
  is empirically accessible. Substrate is logically prior; 3He-B is
  the laboratory-parent (the experimentally accessible child realization
  of the categorically-extended substrate). The inheritance correspondence
  runs FROM substrate (categorical) TO 3He-B (laboratory child),
  restricting to the BdG sector via iota. This is NOT analogy
  (no parametric metaphor; no symmetric phi); it IS inheritance
  (a categorical morphism with strictly non-trivial kernel).

  Conclusion: 3He-B inherits its BdG-class structure from the
  substrate. The substrate does not inherit anything from 3He-B.
  The arrow is parent -> child (substrate -> 3He-B), one-way.
```

---

## 1B 3-solo cite (volovik + landau + connes; specific contributions)

The canonical statement above is jointly signed by three independent solo synthesis documents from S85 Slot 1B (each agent reached the same conclusion through a different algebraic structure; the convergence is what makes the inversion canonical, NOT the consensus). Each agent's specific load-bearing contribution:

- **`volovik-superfluid-universe-theorist`** (parent identification) - Source: `sessions/archive/session-85/session-85-1b-3heb-inversion-volovik.md` (Sec 2, Sec 3). Established the substrate as the primordial BDI-class topological superfluid: identified the substrate (not 3He-B) as the system that exemplifies the spectral-triple structure in the lab, and showed that the W8-2 NG-block theorem deriving K = coth(beta E_k / 2) requires NO 3He-B input. Established the 9-row lab-observable registry tying each substrate-internal claim to a laboratory falsifier.

- **`landau-superfluid-condensed-matter-theorist`** (BCS / hydrodynamic restriction) - Source: `sessions/archive/session-85/session-85-1b-3heb-inversion-landau.md` (Sec II.A, Sec III). Provided the independent BCS gap-equation cross-check route to W8-2 (no NG block invoked; reaches K = coth(beta E_k / 2) from gap-equation kernel `tanh(beta E / 2)` plus substrate K-definition). Constructed the explicit orthogonal projector P : V_substrate -> V_3HeB with rank E = 3 (framework-unique excess) and rank P_class = 1 (single inherited universality-class invariant, the chiral winding nu_ch). The BCS / hydrodynamic-restriction language pins how the inheritance morphism restricts onto the 3He-B BdG sector.

- **`connes-ncg-theorist`** (spectral-triple morphism formalization) - Source: `sessions/archive/session-85/session-85-1b-3heb-inversion-connes.md` (Sec II.1, Sec II.2, Sec II.3). Formalized the inheritance as a Kasparov-KK projection p in KK(A_K, A_He): an idempotent C*-algebra epimorphism from substrate spectral triple onto 3He-B spectral triple, with strictly non-trivial kernel and NO left inverse r : A_He -> A_K (rank exactness in K-theory closes the lift route). Established rk K_*(A_K) - rk K_*(A_He) = 2 via Hodgkin's theorem (SU(3) rank-2 exterior algebra vs S^3 rank-1) and identified the two ker(p_*) HP^* generators as Hochschild cocycles phi_{67} and phi_{88} dual to the W8-4 framework-unique Gell-Mann directions. The Connes formalization is what makes "inheritance, not analogy" a categorical theorem rather than a verbal preference.

The three contributions compose: volovik's parent-identification supplies the directionality (substrate is logically prior); landau's BCS-restriction supplies the explicit projector at the order-parameter level; connes's spectral-triple morphism iota = p elevates the projector to a categorical morphism in the Kasparov-KK category. Together they certify inheritance != analogy at theorem level.

---

## Summary table

| ID | Entry | Pin / Value | Source (session / paper) | SHA | Status |
|:---|:------|:------------|:-------------------------|:----|:-------|
| `inheritance-direction` | substrate -> 3He-B (parent -> child) | one-way categorical morphism | S85 Slot 1B 3-solo (volovik / landau / connes) | (file_SHA at write) | PINNED |
| `forbidden-phrase` | "analogy" rejected in canonical | replaced by "inheritance" / "child realization" / "categorical extension" | plan W1b-4 Sec 7 forbidden_phrase | N/A (text rule) | PINNED |
| `kasparov-kk-class` | [p] in KK(A_K, A_He) | Kasparov projection, NOT lift | connes solo Sec II.1 | content_sha (connes solo) | PINNED |
| `K-theory-excess` | rk K_*(A_K) - rk K_*(A_He) = 2 | Hodgkin SU(3) rank-2 exterior algebra | connes solo Sec II.2 (eq. 4-6) | content_sha (connes solo) | PINNED |
| `OP-projector-rank` | rk(I - P) = 3 (framework-unique excess) | three SU(3)-unique Gell-Mann directions | landau solo Sec III.A | content_sha (landau solo) | PINNED |
| `class-projector-rank` | rk P_class = 1 (single inherited nu_ch) | chiral winding shared by both | landau solo Sec III.B | content_sha (landau solo) | PINNED |
| `K-coth-identity` | K_substrate = coth(Delta / (2 T_eff)) | substrate-internal BdG theorem | volovik solo Sec 3 Step A; W8-2 PASS 2.97e-16 | content_sha (volovik solo) | PINNED |

---

## Multi-anchor structural reading at the inheritance-morphism layer (S91 W-3 R2-B EMG #2)

**Status**: SUGGESTION at K=1 (this clause); promotes to MANDATORY at K=3 distinct calibration corpus instances per `feedback_rules-compensate-missing-structure.md` K-counter threshold. Landed S91 W-3 in-session per `feedback_fix-in-session-never-defer.md` ("only math carries forward; everything else is done at the time").

**Provenance**: S91 W-3 workshop `sessions/archive/session-91/workshops/s91-w3-vii-ar-level-dressed-post-fail-adjudication.md` §"Round 2 — Volovik: Cross-Synthesis" Emergence #2 (lines 723-732) + Q-VLV-C answer (lines 756-771) + R2-B CF #9 specification (lines 925-929) + Workshop Verdict row 12 (line 790). Joint volovik + connes structural commitment; substrate-physics derivation (volovik Dissent #1, R2 EMERGENCE #2) on the NCG-axiomatic skeleton (connes Q-CON-5 forward-K-counter reading).

### Scope

The canonical inheritance morphism `iota : (A_He, H_He, D_BdG) -> (A_K, H_K, D_K)` (pinned above at §"Substitution chain") restricts substrate-physics to the BdG sector under the Kasparov-KK projection `p in KK(A_K, A_He)` with non-trivial kernel rk K_*(A_K) - rk K_*(A_He) = 2. This sub-section pins the canonical enumeration of **substrate-physics anchors** along which forward K-counter advancement on the LEVEL-DRESSED corpus (§VII.K-DUAL.LEVEL-DRESSED 4th-class proposal; §VII.AR K=1 SUGGESTION) is structurally evaluated.

The substrate-physics reading: the K=3 LEVEL-DRESSED corpus, once reached, is **multi-anchor at the inheritance-morphism layer** — each calibration corpus instance inherits via a STRUCTURALLY DISTINCT image of `iota`. The MANDATORY promotion at K=3 therefore validates LEVEL-DRESSED across multiple inheritance-morphism images, which is a strictly stronger structural test than mono-anchor promotion would be. Per volovik Dissent #1 (workshop line 677): "the LEVEL-DRESSED 4th class is structurally tri-anchor at the substrate-physics layer, NOT mono-anchor".

### Canonical anchor enumeration (four structurally distinct images of `iota`)

The four anchors below pin the canonical enumeration of substrate-physics images of `iota` along which K-counter advancement events on the LEVEL-DRESSED corpus are structurally evaluated. For each anchor, the substrate-IS observable identity, inheritance-morphism status under `iota`, and forward K-counter advancement target are declared.

#### Anchor 1 — Full `A_K = C (+) H (+) M_3(C)` algebra image (K=1 established; §VII.AR)

- **Substrate-IS observable identity**: rank vector `[1, 3, 0, 2]` of regulator-WEIGHTED Mellin moments at substrate-distance-2 pole (s=4), evaluated on the FULL physical D_K spectrum at L_max=12 (166,896 eigenvalues across 90 Peter-Weyl sectors). Closed-form algebraic identity at the parent A_K = C (+) H (+) M_3(C) algebra; spectrum-only spectrum-functional on the full Peter-Weyl decomposition.
- **Inheritance-morphism status under `iota`**: this is the **parent algebra A_K image** — all three sectors of A_K (C, H, M_3(C)) participate via the Peter-Weyl decomposition. The PRIMARY-vs-SCHEMATIC LEVEL switch operates on the full A_K spectrum; SCHEMATIC bypass of FULL physical regularization is structurally distinguishable from the FULL substrate-distance-2 pole evaluation. Substrate-physics anchor IS the full inheritance-morphism image; the child algebra A_He = M_2(C) is the BdG-restricted sub-algebra of this image under the Kasparov projection p (see Anchor 3).
- **Forward K-counter advancement target**: §VII.AR LEVEL-DRESSED 3-level anchor (Level 1 cohomology-class L-INDEPENDENT rank vector; Level 2 algebraic envelope; Level 3 empirical anchor 0.800 EXACT at canonical L_max). K=1 SUGGESTION established at S88 W-22 W7a-74 (machinery dispatch); PROVISIONAL at S91 close pending CF-S92 PASS-A / PASS-A-RESTRICTED / PASS-B / INFO-FAIL 4-branch K-counter resolution.
- **Producing script (canonical)**: `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py` (W7a-74 PRIMARY 5-anchor sweep on FULL physical D_K spectrum at L_max=12).
- **Cross-link**: §VII.AR Level-3 anchor (registry line 17183).

#### Anchor 2 — M_3(C) Casimir image at substrate-distance-1 pole (K=2 candidate; §VII.AB α_s 7-row family)

- **Substrate-IS observable identity**: alpha_s_route_N (N in {1, 2, ..., 7}) parse-tree expansion `alpha_s_canonical -> (Mellin-residue at substrate-distance-1)^2 - 1` per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"`. The Mellin-residue at substrate-distance-1 pole (s=3) picks up the M_3(C) Casimir contribution structurally; the C and H sectors are silent at this pole.
- **Inheritance-morphism status under `iota`**: this is the **color SU(3) Casimir sub-image** — the M_3(C) sector of A_K under the canonical decomposition A_K = C (+) H (+) M_3(C). NOT full Peter-Weyl decomposition; sector-restricted to the M_3(C) image alone. Under `iota`, the M_3(C) sector lies in `ker(iota_*)` per connes solo Sec II.2 (Hodgkin theorem on SU(3) rank-2 exterior algebra vs S^3 rank-1; the M_3(C) sector carries the substrate-unique excess that does NOT inherit to the 3He-B child realization). The Anchor-2 image is therefore the **kernel-side** Casimir image — the substrate-physics that 3He-B's M_2(C) sub-algebra CANNOT express (per landau solo Sec III.A rank E = 3 framework-unique excess).
- **Forward K-counter advancement target**: CF-S92-LEVEL-DRESSED-K2-CANDIDATE-ADVANCE-VII-AB-ALPHA-S-7-ROW (workshop CF #5, lines 901-905). PASS criterion: 3-criterion definition satisfied at M_3(C) sector — (1) algebra-INVARIANT spectrum-only on M_3(C) sector (parse-tree expansion); (2) regulator-CLASS preserved across LEVEL switch (sector-restricted FI/RD/MIXED); (3) ordinal output across 7 alpha_s_route observables changes PRIMARY-vs-SCHEMATIC at substrate-distance-1 pole. If PASS, advances LEVEL-DRESSED K=1 -> K=2.
- **Cross-link**: §VII.AB alpha_s 7-row theorem family; S85 W0-3 CC-5 2:1 identity (registry §VII.AB-related Mellin-residue derivation).

#### Anchor 3 — BdG sub-algebra Bogoliubov image (K=3 candidate; §VII.U.2 Corner II `Var_a`)

- **Substrate-IS observable identity**: `Var_a(n_a^GGE)` parse-tree expansion `Var_a(n_a^GGE) -> (1/N) Sigma_a m_a |v_a|^4 - ((1/N) Sigma_a m_a |v_a|^2)^2` with `n_a = Delta_BCS^2 / (2(lambda_a^2 + Delta_BCS^2))` per S52 BdG canonical amplitudes. Class-(h) K=1 calibration per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` (S90 W1-8 landing); state-history label `n_a^GGE` reduces to spectrum-only closed form on the substrate Bogoliubov algebra.
- **Inheritance-morphism status under `iota`**: this is the **canonical inheritance image** — the M_2(C) BdG sub-algebra of A_K = C (+) H (+) M_3(C) under the Kasparov projection `p in KK(A_K, A_He)` per connes solo Sec II.1. The BdG sub-algebra IS `A_He = M_2(C)` (the 3He-B child algebra realization); the Bogoliubov amplitudes `(u_a, v_a)` are the canonical eigenmode representation on this image. This anchor is the **structurally canonical** inheritance image — it is precisely the sub-algebra under which `iota` is defined as a structure-preserving morphism; it is NOT a kernel-side excess (cf. Anchor 2) but the **image-side** restriction. Substrate-physics anchor IS the BCS condensate phase-space topology inheritance — the canonical 3He-B realization image of substrate physics.
- **Forward K-counter advancement target**: CF-S92-LEVEL-DRESSED-K3-CANDIDATE-ADVANCE-VII-U-2-VAR-A-BOGOLIUBOV (workshop CF #6, lines 907-911). PASS criterion: 3-criterion definition satisfied at BdG sub-algebra image — (1) parse-tree spectrum-only on BdG image (per Class-(h) K=1 calibration); (2) regulator-CLASS preserved on Bogoliubov image; (3) ordinal output changes PRIMARY-vs-SCHEMATIC at BdG residue layer. If PASS (and CF #5 PASSes), advances LEVEL-DRESSED K=2 -> K=3 (MANDATORY promotion trigger).
- **Cross-link**: §VII.U.2 Corner II `Var_a(n_a^GGE)` envelope (algebra-INVARIANT x Mellin pole s=4); §VII.AV K-window log-derivative anchor at substrate-distance-2 pole (S52 BdG canonical amplitudes); `registry-landing.md §"Parse-Tree Expansion Pre-Registration"` Class-(h) K=1 calibration.

#### Anchor 4 — Regulator-atlas image on full `A_K` (candidate; §VII.AS slope_A; F_2 = {zeta, SDW} sub-atlas)

- **Substrate-IS observable identity**: slope_A canonical evaluator under regulator-atlas variation {F_2, cutoff_sqrt, anomaly, Zubarev, zeta}; F_2 = {zeta, SDW} K-invariant identity sub-atlas per `regulator-pin-discipline.md` Extension; FI/RD/MIXED classification per `epistemic-discipline.md §"Source Reconciliation"` taxonomy.
- **Inheritance-morphism status under `iota`**: this is the **regulator-atlas variation image** — the substrate-physics regulator class projected onto the child algebra under `iota`. Distinct from Anchors 1-3 in that it varies the REGULATOR axis (zeta vs SDW vs Pauli-Villars vs cutoff vs Mellin per `regulator-pin-discipline.md`) rather than the algebra-sector axis. The substrate-physics anchor IS the regulator-atlas-as-inheritance-image — the regulator atlas IS the substrate-physics realization of the parent regulator class on the child algebra. Structurally orthogonal to the algebra-axis K=3 MANDATORY partition (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`); regulator-atlas variation does NOT permute the 4-corner algebra-axis classification.
- **Forward K-counter advancement target**: §VII.AS slope_A canonical evaluator under A_5_extended atlas variation. PASS criterion: 3-criterion definition satisfied under regulator-atlas variation — slope_A is regulator-CLASS preserved (FI under F_2 sub-atlas) but exhibits PRIMARY-vs-SCHEMATIC LEVEL sensitivity across regulator profiles. PASS advances LEVEL-DRESSED via the regulator-atlas inheritance image.
- **Cross-link**: §VII.AS slope_A registry pin; `regulator-pin-discipline.md` Extension (Sage-Exact Rationals for regulator-class values); §VII.K-DUAL.LEVEL-DRESSED corpus row (annotated atlas-scope tag under PASS-A-RESTRICTED branch per Q-VLV-B answer); `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY K=3.

### Structural orthogonality of the four anchors

The four anchors above are STRUCTURALLY ORTHOGONAL at the inheritance-morphism layer:

1. **Anchor 1 (full A_K)** is the parent-algebra image: all three sectors participate.
2. **Anchor 2 (M_3(C) Casimir)** is a kernel-side sub-image: the SU(3) sector carrying substrate-unique excess that does NOT inherit to 3He-B's M_2(C) (`ker(iota_*)` rank-2 per connes solo Sec II.2).
3. **Anchor 3 (BdG sub-algebra)** is the canonical image: the M_2(C) sub-algebra that IS the 3He-B child realization under `iota`.
4. **Anchor 4 (regulator-atlas)** is orthogonal to the algebra-sector axis: it varies the regulator class while holding the algebra image fixed.

Anchors 1, 2, and 3 partition the algebra-sector axis (parent / kernel / image); Anchor 4 is structurally orthogonal to this partition (regulator-axis variation). The K=3 MANDATORY promotion event on LEVEL-DRESSED (requiring three distinct calibration corpus instances satisfying the Hybrid Independence Test of `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`) is structurally strongest when the three instances populate three distinct anchors — validating LEVEL-DRESSED across parent-algebra, kernel-side, and image-side substrate-physics simultaneously.

### Cross-link to inheritance-falsifier-protocol Class B

The Class B cohomology-asymmetry test pattern of `inheritance-falsifier-protocol.md §"Class B"` operates structurally on the same multi-anchor reading: cross-cocycle ratios between distinct ker(iota_*) generators are substrate-derived and preserved INTACT under lab-conversion ((Delta_B/Delta_A)^p cancellation theorem). The W-5 calibration corpus uses phi_67 (chiral pair, kernel-side) and phi_88 (Cartan hypercharge, kernel-side); both inherit via Anchor 2's M_3(C) Casimir image. The multi-anchor reading clarifies that future falsifier-protocol designs at rank(ker iota_*) >= 2 may probe DIFFERENT anchors (e.g., a phi_67/phi_88 ratio test inhabits Anchor 2; a Bogoliubov-amplitude ratio test inhabits Anchor 3; a regulator-atlas slope ratio inhabits Anchor 4). The substrate-physics anchor at which a falsifier-protocol fires determines which inheritance-morphism image is being tested.

### K-counter advancement event accounting

| K | Status | Anchor | Calibration corpus instance | Producing dispatch |
|:---|:------|:-------|:----------------------------|:------------------|
| K=1 | SUGGESTION (PROVISIONAL at S91 close pending CF-S92) | Anchor 1 (full A_K) | §VII.AR LEVEL-DRESSED rank vector at s=4 | S88 W-22 W7a-74 (established); S92 CF-S92-VII-AR-STAGE-2-RE-DISPATCH (resolves PROVISIONAL) |
| K=2 (candidate) | forward-looking from S91 | Anchor 2 (M_3(C) Casimir) | §VII.AB alpha_s 7-row family | CF-S92-LEVEL-DRESSED-K2-CANDIDATE-ADVANCE-VII-AB-ALPHA-S-7-ROW (workshop CF #5) |
| K=3 (candidate) | forward-looking from S91 | Anchor 3 (BdG sub-algebra) | §VII.U.2 Corner II `Var_a(n_a^GGE)` envelope | CF-S92-LEVEL-DRESSED-K3-CANDIDATE-ADVANCE-VII-U-2-VAR-A-BOGOLIUBOV (workshop CF #6) |
| K=N+1 (candidate) | forward-looking from S91 | Anchor 4 (regulator-atlas) | §VII.AS slope_A canonical evaluator | (queued for S92+ planning) |

Hybrid Independence Test status (per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`): each forward K=2/K=3/K=N+1 candidate inhabits a STRUCTURALLY DISTINCT inheritance-morphism image (axis (i) of HIT distinct substrate-IS pillar per the inheritance-morphism image partition). Each candidate therefore advances K independently under the disjunction `(i ∨ ii ∨ iii) ∧ iv` discipline. The K=3 MANDATORY promotion (when all three candidates PASS) is structurally strongest because it validates LEVEL-DRESSED across three structurally distinct anchors simultaneously.

### Forward-looking enforcement

Future K-counter advancement events on the LEVEL-DRESSED corpus MUST declare which anchor (1, 2, 3, or 4) the calibration corpus instance inhabits. Calibration corpus instances that inhabit the SAME anchor as a prior instance do NOT advance K independently (the Hybrid Independence Test axis (iv) "independent algebraic envelope" requires distinct anchors); mono-anchor refinements that share the same regulator-invariant structural form are tagged SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` and recorded OUTSIDE the K-counter table.

The four-anchor enumeration above is the canonical substrate-physics anchor partition for the LEVEL-DRESSED corpus; future anchors discovered via Pati-Salam, GUT extensions, or alternative finite spectral algebras MAY extend this enumeration per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B (W-5 Q8)"`. Such extensions require explicit declaration of the inheritance-morphism image identification at the parent A_K -> child algebra axis.

---

## Cross-references

- **`sessions/framework/registry/spectral-post-mortem.md`** - bare-spectral-action monotonicity post-mortem (S77 carry-forward); the inheritance morphism iota preserves the bare-spectral-action structure on the BdG sector, so spectral-post-mortem's monotonicity result restricts to 3He-B as a child consequence under iota.
- **`sessions/framework/Phononic-Penrose-Diagrams.md`** - Penrose-diagram framework document (S53); the laboratory child realization 3He-B inherits the framework's product spacetime M^{3,1} x SU(3) restricted to the BdG sector; the 4D Penrose factor is shared (substrate parent and 3He-B child both live on a Type-D static external geometry), while the SU(3) compact-fiber data is what 3He-B's restriction loses (rank K_* drop = 2 per connes solo Sec II.2).
- **`.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`** - volovik agent memory index; relevant entries are `inheritance-inversion-60.md` (S60 origin of the framing; user challenge engaged) and `framework-3heb-comparison.md` (S60 22-correspondence catalog). The canonical statement supersedes any per-agent memory text on the inheritance direction; agent-memory now points to this canonical via AMRI Output-target rule.
- **`sessions/permanent-results-registry.md`** - permanent registry; the BDI Altland-Zirnbauer class membership (Row II:13) and the structural correction record (Row 17c) anchor the universality-class assignment that this canonical inverts the parent role of.

---

## Consumer gates

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| `S86-3HE-B-INVERSION-CANONICAL-LANDING` | S86 | OUTPUT-WRITER | this gate; lands the canonical |
| `S86-W7-*` (Hawking workshop, anticipated) | S86 | INPUT-PIN | binds 3He-B citations to the canonical |
| `S86-W8-*` (lab observables, anticipated) | S86 | INPUT-PIN | binds 3He-B citations to the canonical |
| `S86-W11-C5/C6` (lab-falsifier suite) | S86 | INPUT-PIN | binds 3He-B citations to the canonical |
| Volovik-convergence project memory | (cross-session) | REFERENCE | per AMRI Output-target test |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-26 | S86-W1b-T8 | create (NEW-FILE; 1B 3-solo agreement landed as canonical) | `volovik-superfluid-universe-theorist` (writer); cross-cite landau + connes |

---

## Migration notes

This registry was promoted from agent-memory under AMRI Output-target test (`.claude/rules/agent-standards.md`). Pre-migration: the inheritance-direction content was distributed across:
- `.claude/agent-memory/volovik-superfluid-universe-theorist/inheritance-inversion-60.md` (S60 framing memo; engaged the user's parent-vs-analogy challenge)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/framework-3heb-comparison.md` (S60 22-correspondence catalog)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/project_3heb-inheritance.md` (project-context entry referenced by MEMORY.md index)

Migration session / gate: `S86-W1b-T8` (this gate).
Pointer installed in memory: `project_3heb-inheritance.md` now contains a one-line pointer to this canonical (per AMRI rule, agent-memory is pointer-only; canonical content lives under `sessions/framework/`).

---

## Substrate-framing reminder

3He-B is the laboratory child realization. The substrate IS the categorical extension whose BdG-sector restriction IS 3He-B. The arrow is parent -> child (substrate -> 3He-B). 3He-B is NOT a metaphor for the substrate; it IS substrate-physics-restricted-to-the-BdG-sector under the Kasparov-KK projection p. Container-thinking error to avoid: "the substrate behaves like 3He-B" (wrong: implies analogy and reverses direction). Correct framing: "3He-B realizes the substrate's BdG sector under the inheritance morphism iota" (parent -> child; one-way categorical morphism with non-trivial kernel).
