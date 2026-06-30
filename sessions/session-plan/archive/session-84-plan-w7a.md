# Session 84 Plan — Wave 7a: Heterotic + F-theory + K-theoretic + Equivalence-Class Falsifiers (5 gates)

**Session**: 84
**Wave**: 7a (string/M-theory external-paradigm correspondences and falsifiers)
**Planner**: kaku-speculative-theorist
**Date**: 2026-04-18
**Format**: compute (parallel independent agents + long-horizon literature review)
**Scope**: Gates 72, 73, 74, 79, 80 from §4.G (string/M-theory/matrix-model extensions)

---

## W7a Summary

Wave 7a tests the framework against external physics paradigms: heterotic string theory (E_8 branching), F-theory (elliptic CY 4-folds), K-theoretic D-brane classification (Witten 1998), and the structural-equivalence-class claim that underlies the framework's uniqueness assertion. Three gates (72, 73, 74) are positive-correspondence probes: can an external construction host the framework's admissibility singleton? Two gates (79, 80) are pre-registered falsifiers: does ANY construction in the string landscape reproduce the framework's joint signature? Gates 79 and 80 are long-horizon — 79 is a formal equivalence-class statement that requires exhaustive literature catalog, 80 is a 6-month review targeting ~50 compactifications across the major families.

The wave is load-bearing for §VII.N landing (IKKT anti-correspondence + 11-dim exclusion, G32 PASS, G36 PASS) and for the rank-6 gear-machine classification (MG-0, MG-1, MG-2). If any W7a gate returns FAIL on the falsifier side, the framework's structural-uniqueness claim retreats from "sole surviving region" to "one of several candidates."

This wave partners with W7b (G36 stability extensions, Seeley-DeWitt match, twisted spectral triples, correspondence-table closure, §VII.N registry landing, KK tower) — together they execute §4.G in full.

---

## W7a Decision Point Prerequisites

Before Wave 8 consolidation, W7a outputs must include:

1. **Gate 72 (HET-DECOMP) verdict**: quantitative match score for Psi_+ under E_8 → E_6×SU(3) decomposition, measured against Slansky 1981 branching tables. Classification PASS/INFO/FAIL per threshold.
2. **Gate 73 (FTH-UPLIFT) verdict**: does SU(3) appear at a single discriminant-locus enhancement on ≥1 elliptic CY 4-fold with framework d_spatial=12 base? Enumeration bound reported.
3. **Gate 74 (DET-P-K-THEORY) verdict**: explicit K-theoretic uplift of det(P)=1 to Witten 1998 D-brane charge identity, or negative result with homotopy-level degree.
4. **Gate 79 (EQUIV-CLASS-FALSIF) verdict**: zero/one/≥1 constructions found exhibiting BOTH KO-dim=6 admissibility AND |E_cond|~L^4.68 scaling. This is the hardest test the framework's equivalence-class claim faces.
5. **Gate 80 (DYNAMICS-UNIQUENESS) status**: initiated 6-month literature review with at least 5/50 compactifications fully catalogued against the 4-signature joint predicate. Full verdict deferred to S90 (session +6).

Decision rule for W8 consolidation: if gates 72, 73, 74 jointly return NONE that admits structural-preserving map (no PASS on positive-correspondence side), AND gate 79 returns PASS (zero constructions match), THEN §VII.N (IKKT anti-correspondence + 11-dim exclusion) is LANDED as permanent. Otherwise, §VII.N landing is deferred pending resolution of the non-PASS gate.

---

## §W7a-72. S84-HET-DECOMP

**Gate ID**: S84-HET-DECOMP
**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (spectral triple representation content, not substrate excitation)
**Script**: `computations/s84_w7a_het_decomp.py`
**Agent type**: kaku-speculative-theorist

### Hypothesis
The framework's half-spinor representation Psi_+ = C^16 per generation (S7-8 permanent, KO-dim=6) is a sub-decomposition of the E_8 adjoint 248 under the branching chain E_8 → E_6 × SU(3) → SO(10) × U(1) × SU(3) → ... . If >50% of Psi_+ irreducibles appear in an E_8 decomposition with framework hypercharges intact, the framework's particle content admits a heterotic uplift.

### Background

- S7-8 permanent result: Psi_+ = C^16 = (2,1) ⊕ (1,2) ⊕ (3,1) ⊕ (3,2) ⊕ (1,1) ⊕ (3,1) ⊕ (1,1) under SU(3)_color × SU(2)_L × U(1)_Y of A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) — exactly one SM generation with hypercharges matching PDG.
- Heterotic E_8 × E_8: 248 = 248_L ⊕ 248_R with gauge group E_8 on each side.
- E_8 branching (Slansky 1981): 248 → (78, 1) ⊕ (1, 8) ⊕ (27, 3) ⊕ (27-bar, 3-bar) under E_6 × SU(3).
- Further branching: 27 of E_6 → (16, 1) ⊕ (10, -2) ⊕ (1, 4) under SO(10) × U(1).
- SO(10) 16 is the SM generation including right-handed neutrino — structurally related to Psi_+.
- Framework's A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) has no direct E_8 structure, but its SM quantum-number content may embed.

### Method

```
from canonical_constants import *  # tau_fold, M_KK, Vol_SU3, etc.
# (all E_8 branching constants are NOT canonical — load from tabulated Slansky 1981)

# Step 1: Load E_8 adjoint decomposition under E_6 × SU(3)
# (local) slansky_branch_table = {chain: [(irrep, multiplicity, weight), ...]}

# Step 2: Decompose each branch recursively down to SU(3)_C × SU(2)_L × U(1)_Y
# (local) sm_decomp = recursive_branch(e8_adjoint, chain=[E8, E6xSU3, SO10xU1xSU3,
#                                                        SU5xU1xU1xSU3, SU3CxSU2LxU1Y])

# Step 3: Identify Psi_+ = C^16 irreducibles (framework result from A_F)
# (local) psi_plus_reps = [(3,1,+1/3), (3,2,+1/6), (1,2,-1/2), (3-bar,1,-2/3),
#                         (3-bar,1,+1/3), (1,1,+1), (1,1,0)]  # 16-component

# Step 4: For each E_8 decomposition path, count matches to psi_plus_reps
# (local) match_score[path] = |psi_plus_reps intersect path_irreps| / 16

# Step 5: Classify hypercharge preservation
#   - framework_Y must match decomposition-inherited Y within rational equality
# (local) hypercharge_preserved[path] = all(Y_framework == Y_heterotic, ±normalization)

# Step 6: Compute best-match score across all paths
# (local) best_match = max_path(match_score if hypercharge_preserved else 0)

# Cross-checks:
#   (a) Gauge-invariance: check E_6 and SU(3) Casimirs consistent under branching
#   (b) Anomaly cancellation: verify tr(Y^3)=0 and tr(Y)=0 in candidate decompositions
#   (c) Family structure: 3 families require 3 copies of 27 of E_6 from E_8 × E_8
#   (d) KO-dimension: heterotic world-sheet is KO-dim=2; framework fiber is KO-dim=6
#       → structure-preserving map must bridge this difference (record obstruction)
```

### PRDR machinery pin

- Matrix computation: branching is combinatorial, not linear-algebra-heavy. torch.linalg NOT required (representation-theoretic enumeration only). GPU path: N/A.
- L_max: N/A (Peter-Weyl truncation is irrelevant to branching tables).
- Scheme: Slansky 1981 normalization (U(1)_Y = (1/6)(B-L) convention with appropriate factor-of-2 for SM).
- Convention: heterotic E_8 × E_8 embedding with trivial SU(3) Wilson line (Candelas-Horowitz-Strominger-Witten 1985 standard embedding).
- Scan range: all maximal subalgebras of E_8 (E_7 × SU(2), SO(16), E_6 × SU(3), SU(9)) at rank level 1; terminate on reaching SU(3)_C × SU(2)_L × U(1)_Y.
- Random seed: N/A (deterministic enumeration).

### Pass/Fail/INFO thresholds

- **PASS**: best_match >= 0.50 AND hypercharge_preserved == True AND anomaly_cancellation == True. Framework's Psi_+ admits structure-preserving embedding into E_8 adjoint via E_6 × SU(3) chain.
- **INFO**: 0.25 <= best_match < 0.50 OR best_match >= 0.50 with hypercharge mismatch. Partial embedding; framework shares algebraic skeleton but not full representation content.
- **FAIL**: best_match < 0.25. E_8 heterotic cannot host framework Psi_+ content.

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- Slansky 1981 branching table (hardcoded in script as tabulated dictionary): `<computed-at-runtime>` on script content
- Reference: CCM 2007 A_F derivation for framework quantum numbers: `<computed-at-runtime>`

### Expected output 4-tuple

`(value=best_match, scheme=Slansky1981, convention=standard_embedding, L_max=NA)`

### Substitution chain (hypercharge preservation)

Framework: Y_framework(psi) from CCM 2007 derivation of A_F = ℂ⊕ℍ⊕M_3(ℂ) at KO-dim=6.
Heterotic: Y_heterotic(psi) from E_8 → E_6×SU(3) → SO(10)×U(1)×SU(3) → SU(5)×U(1) → SU(3)_C×SU(2)_L×U(1)_Y branching with U(1)_Y identified via Georgi-Glashow SU(5) embedding.

Step 1: Y_framework(psi_L^u) = +1/6 [direct from A_F left-handed up quark]
Step 2: Y_heterotic(psi_L^u) = [from 27 of E_6 → 16 of SO(10) → 10 of SU(5)] = +1/6
Step 3: Match requires Y_framework == Y_heterotic for ALL 16 components of Psi_+
Step 4: Normalization: allowed rescaling Y → k·Y with single k across generation (preserved-up-to-normalization counts as match)

If Y_framework/Y_heterotic == const for all 16 entries → hypercharge_preserved = True.

### What PASS means for solution space

Framework admits heterotic uplift of representation content. Joins E_8 × E_8 family as one admissible host. Strengthens rank-6 gear-machine (MG-2) A_F classification: A_F is not arbitrary, but sits inside a standard string-theoretic branching. Anti-correspondence #X in W7b would downgrade from "no external embedding" to "heterotic embedding exists but KO-dim obstruction remains."

### What FAIL means for solution space

Framework's Psi_+ does NOT embed in E_8 via the standard heterotic branching. Sharpens §VII.N anti-correspondence: heterotic is not a parent paradigm. Combined with G32 (d=12 singleton, 11-dim excluded) and G36 (IKKT exclusion), narrows admissible string-theoretic hosts to zero — strengthening the framework's structural-uniqueness claim.

### Pictorial explanation

Imagine E_8 as a 248-dimensional chandelier hanging in representation-space. Heterotic physics slices the chandelier along symmetry-axis cuts (E_6, SO(10), SU(5), SM) to extract the 16 "bulbs" of one generation. The framework independently assembles those 16 bulbs from a different building — the algebra A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ). The question is: are the bulbs the SAME bulbs, or merely isomorphic copies with different wiring? If the hypercharges (the wiring) line up exactly, yes. If not, the framework and heterotic build the same lightshow from structurally different materials.

---

## §W7a-73. S84-FTH-UPLIFT

**Gate ID**: S84-FTH-UPLIFT
**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (compactification manifold classification, not substrate excitation)
**Script**: `computations/s84_w7a_fth_uplift.py`
**Agent type**: kaku-speculative-theorist

### Hypothesis

The SM gauge group (SU(3), SU(2), U(1)) can arise as a discriminant-locus enhancement on an elliptic Calabi-Yau 4-fold whose base is the framework's M_4 (d_spatial=12 — NOT the standard F-theory base which is P^3 or Fano 3-fold). If ≥1 such CY 4-fold exists with SU(3) at a single intersection point where SU(2) × U(1) meet, the framework admits F-theory uplift.

### Background

- F-theory: 12-dimensional (10+2 with 2 non-compact time directions effectively) theory compactified on elliptic fibration over 6-dimensional base → 4D effective theory. Singularities in the elliptic fiber (Kodaira classification: I_n, II, III, IV, IV*, III*, II*, I_n*) host gauge groups.
- Gauge groups localize on codim-1 divisors in base (7-branes), matter on codim-2, Yukawas on codim-3.
- Framework's d_spatial = 12 (G32 PASS, singleton with KO-dim=6, A_F=ℂ⊕ℍ⊕M_3(ℂ)).
- Standard F-theory: d_total = 12 (10 from elliptic fiber plus Type IIB dilaton/axion, 2 from fiber). Framework d_spatial=12 is DIFFERENT (it is spatial, not total; includes time).
- CY 4-fold base dim = 6 (in standard F-theory; compactifying to 4D). Framework's M_4 has d_spatial=12 → base would need to be 8-dimensional, violating standard F-theory structure.
- Reconciliation: either (a) framework is F-theory with non-standard base, or (b) reinterpret d_spatial=12 as total (including M_4 directions), putting base at 8 and fiber at 4 (non-elliptic).

### Method

```
from canonical_constants import *

# Step 1: Enumerate Kreuzer-Skarke CY 4-folds with KS database
# (local) ks_4fold_list = load_kreuzer_skarke_4folds(h11_max=491, h31_max=491)
# ~1000-10000 4-folds with elliptic fibration structure

# Step 2: For each 4-fold, check base is compatible with framework M_4 (d_spatial=12)
# Option A: base dim = 3 + SU(3)-internal structure → reject (standard F-theory only)
# Option B: base dim = 8 → non-elliptic, but consistent with framework
# (local) framework_compatible = filter(ks_4fold_list, lambda cy: cy.base_dim in {3, 8})

# Step 3: For each compatible 4-fold, find discriminant locus and Kodaira-type singularities
# (local) disc_loci = [(cy, codim_1_divisors, kodaira_types) for cy in framework_compatible]

# Step 4: For each locus, check if SU(3) × SU(2) × U(1) all localize at a single point
# - SU(3) requires I_3 (split) or IV (non-split) fiber
# - SU(2) requires I_2 or III
# - U(1) requires Mordell-Weil rank 1 on the fibration
# (local) sm_single_point_count = sum(1 for cy in framework_compatible
#                                     if has_sm_at_single_intersection(cy))

# Step 5: For each cy with SM-at-single-point, verify matter content matches framework
# (local) matter_spectrum = compute_5_6_7_brane_intersections(cy)

# Cross-checks:
#   (a) Tadpole cancellation: Euler(CY4) = 24·N_D3 + ... must be satisfied
#   (b) Anomaly cancellation: chern-class integrals on CY4 match framework anomaly content
#   (c) Flux quantization: G_4 flux must be half-integer quantized
#   (d) Moduli stabilization: check compatibility with KKLT/LVS framework for base moduli
#   (e) Framework-specific: d_spatial=12 interpretation must be stated unambiguously
```

### PRDR machinery pin

- Matrix computation: CY 4-fold intersection numbers can require ≥100x100 matrices for Hodge computations → **torch.linalg on GPU MANDATORY**.
- L_max: N/A (topological).
- Scheme: Kreuzer-Skarke classification (standard convention, h^{1,1} + h^{2,1} + h^{3,1} + h^{2,2} = Euler/6 for CY 4-folds).
- Convention: F-theory compactification on elliptic CY 4-fold with section (Mordell-Weil group trivial for gauge embedding, non-trivial for U(1) factors).
- Scan range: KS-like catalog of elliptically fibered 4-folds; sample up to N=1000 4-folds with h^{1,1} ∈ [1, 50] to bound computation.
- Random seed: `seed=84073` for sampling order reproducibility; enumeration is deterministic.
- GPU path: torch.linalg on RX 9070 XT (ROCm) for Gram matrix SVD when h^{1,1} * h^{2,1} > 200.

### Pass/Fail/INFO thresholds

- **PASS**: ≥1 CY 4-fold in sampled catalog reproduces SM gauge group at SINGLE intersection point (codim-3 in base) AND base has dimension compatible with framework d_spatial=12 interpretation (either 3 with SU(3)-internal or 8).
- **INFO**: ≥1 CY 4-fold reproduces SM but at MULTIPLE disjoint points, OR reproduces SM with base dimension inconsistent with framework.
- **FAIL**: Zero CY 4-folds in sample reproduce SU(3) enhancement at framework-compatible base.

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- Kreuzer-Skarke 4-fold database excerpt (subset used, cached locally): `<computed-at-runtime>`
- F-theory conventions reference (Weigand 2010 TASI lectures formulas hard-coded): `<computed-at-runtime>`

### Expected output 4-tuple

`(value=sm_single_point_count, scheme=KS_4fold, convention=Weigand_TASI_2010, L_max=NA)`

### What PASS means for solution space

Framework admits F-theory uplift via non-standard base geometry. Compactification is not a free choice — it is dictated by d_spatial=12 constraint plus SM-at-single-point requirement. The 4-fold selection narrows dramatically (from ~473M total reflexive 4-polytopes to a countable subset). Strengthens MG-1 τ_fold=0.190 by providing an F-theoretic origin for the fold (disc-locus intersection).

### What FAIL means for solution space

F-theory cannot host the framework at its natural d_spatial=12 geometry. Sharpens §VII.N: framework sits outside F-theory landscape. Combined with HET-DECOMP FAIL (if it occurs) and G32 (11-dim excluded), the admissibility lattice collapses further to "no known string construction hosts the framework" — corroborating structural-equivalence-class uniqueness.

### Pictorial explanation

F-theory is a way of bundling extra dimensions into a fiber bundle whose fiber is a torus (elliptic curve). Singularities in the fiber — where the torus collapses — host gauge groups like SU(3). Imagine a landscape of crinkled paper (the base, 6D), and at certain ridges (codim-1 divisors), the paper pinches flat (the elliptic fiber degenerates). At intersections of three ridges, three gauge groups meet at a single point — that is where the SM could live. The test asks: given the framework demands a 12-dimensional spatial geometry (not 6), can the ridges still pinch correctly? Can the SM still meet at a single point? If yes (PASS), the framework and F-theory build the same picture with different blueprints. If no (FAIL), the framework's geometric floor-plan is incompatible with F-theory's.

---

## §W7a-74. S84-DET-P-K-THEORY

**Gate ID**: S84-DET-P-K-THEORY
**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (Kasparov KK^6 structural identity)
**Script**: `computations/s84_w7a_det_p_k_theory.py`
**Agent type**: kaku-speculative-theorist

### Hypothesis

The framework's permanent result det(P) = 1 (from S45, Poincaré pairing on Kasparov fundamental class of KK^6(A, A°)) admits K-theoretic reformulation as an anomaly-cancellation identity á la Witten 1998 "D-Branes and K-Theory" (JHEP 9812:019). If a structure-preserving map K_0(KK^6) → K-theory(M × X) exists that carries det(P)=1 to Witten's anomaly-cancellation identity, the framework's central structural identity admits a K-theoretic uplift.

### Background

- S45 permanent: det(P) = 1 where P is the Poincaré pairing matrix on KK^6(A_F, A_F°) Kasparov fundamental class. A_F° denotes the opposite algebra. KK^6 because KO-dim=6.
- Witten 1998: D-brane charges in Type IIB string theory live in K^0(X) (complex K-theory) or KO(X) (real K-theory depending on orientifold). Anomaly cancellation is a K-theoretic identity: Σ Q(D-brane) = 0 in K-theory mod torsion.
- Connes' non-commutative framework: K_0(A) for algebra A is defined via equivalence classes of projections; det(P)=1 is equivalent to invertibility of the Poincaré pairing in KK_0.
- Bridge: Kasparov's KK-theory extends to topological K-theory when A is commutative (A = C(X)); for A = ℂ⊕ℍ⊕M_3(ℂ), the bridge involves Morita equivalence and the finite-dim representation theory.
- Witten's identity: for a D-brane with charge Q in K^0(X), cancelation requires ∫_X ch(Q)·Â(TX) = 0 where ch is Chern character and Â is A-roof genus.

### Method

```
from canonical_constants import *

# Step 1: Load S45 det(P)=1 computation (already in computation archive)
# (local) P_matrix = load_s45_poincare_pairing_matrix()  # 8x8 (KK^6 rank from A_F)
# (local) det_P = np.linalg.det(P_matrix)  # MUST return 1.0 exactly

# Step 2: Compute Chern character of Kasparov fundamental class
# For A_F = ℂ⊕ℍ⊕M_3(ℂ), ch(fundamental_class) = trace over representation
# (local) ch_fundamental = compute_chern_character_AF(dim_rep=16)

# Step 3: Compute A-roof genus on the framework's effective M^4 manifold
# Â(TM^4) = 1 - p_1/24 + (7·p_1^2 - 4·p_2)/5760 + ...
# For M^4 flat (no curvature at τ=τ_fold), p_1=p_2=0 → Â=1
# (local) a_roof_M4 = 1.0

# Step 4: Attempt uplift: construct map
#   phi: KK^6(A_F, A_F°) → K^0(pt × M^4 × X_fiber)
# via (a) A_F viewed as 16-dim vector bundle over pt
#     (b) finite projection p_AF representing fundamental class
#     (c) X_fiber = Spin^c structure from KO-dim=6 → KO^6(pt) → K^0(pt) shift
# (local) phi_map = construct_KK_to_K_map(A_F, KO_dim=6)

# Step 5: Check that phi carries det(P)=1 to Witten's anomaly identity
# In Witten's language: Σ_i Q_i · Q_i^* = 1 (charge self-pairing = identity)
# (local) uplift_valid = (phi(det_P) == witten_anomaly_identity)

# Step 6: Classify uplift by homotopy level
#   STRONG: structure-preserving map exists at K_0 level (isomorphism on generators)
#   WEAK: homotopy equivalence at level of classifying spaces
#   NONE: no map exists (obstruction in higher KK-groups)
# (local) homotopy_level = classify_uplift_level(phi_map)

# Cross-checks:
#   (a) Bott periodicity: KK^6 ~ KK^{-2} via 8-fold periodicity → must match K-theory mod-8
#   (b) KO vs K: real vs complex K-theory differ for A_F with ℍ factor (reality)
#   (c) Torsion: Z/2 elements of KO^n must be correctly mapped
#   (d) Natural transformation: map must commute with Bott periodicity morphism
```

### PRDR machinery pin

- Matrix computation: 8x8 or 16x16 projections — small, CPU numpy.linalg sufficient. GPU path: N/A.
- L_max: N/A (K-theoretic, not spectral).
- Scheme: Kasparov KK-theory; complex K-theory for anomaly cancellation (Type IIB D-branes). Real KO-theory used for KO-dim=6 classification.
- Convention: Witten 1998 normalization (charges in K^0, anomaly integral over 10-dim spacetime).
- Scan range: N/A — this is a structural existence check, not a parameter scan.
- Random seed: N/A.

### Pass/Fail/INFO thresholds

- **PASS**: A structure-preserving map phi: KK^6(A_F, A_F°) → K^0(M^4 × X_fiber) exists that carries det(P)=1 to Witten's anomaly-cancellation identity at K_0 level. Map respects Bott periodicity and torsion classes.
- **INFO**: Map exists at homotopy level (classifying-space equivalence) but is not structure-preserving at K_0. Framework K-theoretic identity is homotopically equivalent to Witten's but algebraically distinct.
- **FAIL**: No map exists; obstruction identified in a specific KK-group (likely KK^6 torsion or Bott periodicity mismatch). Framework's det(P)=1 has no K-theoretic uplift.

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- S45 Poincaré pairing matrix (computation archive): `<computed-at-runtime>`
- Slansky 1981 table (for A_F representation content): `<computed-at-runtime>`
- Witten 1998 anomaly identity (hard-coded formula): `<computed-at-runtime>`

### Expected output 4-tuple

`(value=homotopy_level, scheme=Kasparov_KK, convention=Witten_1998, L_max=NA)`

### Substitution chain (uplift validity)

Step 1: det(P)=1 in KK^6(A_F, A_F°) [S45 permanent]
Step 2: Under Bott periodicity KK^6 → K^0 shift: index in K^0 = (det(P) phase / 2π) = 0 (no phase)
Step 3: Witten's anomaly-cancellation: Σ Q·Q^* = ch(fundamental class) ∧ Â(TX) integrated over X
Step 4: For A_F with 16-dim representation, ch(fund) = 16 (trace of identity on C^16)
Step 5: With M_4 flat (Â=1) and X_fiber carrying KO-dim=6 shift: integral = 16 mod torsion
Step 6: Witten requires integral = 1 in K^0 (single D-brane). If 16 ≡ 1 mod normalization choice, PASS; else FAIL.

### What PASS means for solution space

det(P)=1 is not merely an algebraic curiosity — it is a K-theoretic manifestation of D-brane anomaly cancellation. Framework's spectral triple becomes a "generalized D-brane configuration." This strengthens the KK^6 admissibility singleton (G32) by anchoring it in physical string-theory considerations. Promotes §VII.N to a K-theoretic classification result.

### What FAIL means for solution space

det(P)=1 has no string-theoretic uplift via K-theory. The identity is PURELY spectral-triple structural, not inherited from a higher-dimensional anomaly-cancellation condition. Framework's core identity stands ALONE as a non-commutative geometric fact with no K-theoretic parent. This is consistent with §VII.N framework-independence and G32 singleton — but weakens the hope that string theory "explains why" det(P)=1.

### Pictorial explanation

Think of det(P)=1 as a balance-sheet identity: every entry in the framework's fundamental spectral bookkeeping cancels to give a total of 1. Witten's D-brane story is a DIFFERENT balance sheet in string theory: the total charge of all D-branes on a spacetime must also balance to zero (or 1, with normalization). The question is: are these two balance sheets the SAME ledger written in different currencies (K-theory vs KK-theory)? If yes (PASS), Witten's physical intuition for why charges cancel applies to the framework. If no (FAIL), the framework's ledger is structurally its own — it balances for reasons intrinsic to non-commutative geometry, not for D-brane reasons. Either verdict is informative.

---

## §W7a-79. S84-EQUIV-CLASS-FALSIF

**Gate ID**: S84-EQUIV-CLASS-FALSIF
**Trigger**: `[AUDIT]` (long-horizon falsifier; re-examines structural-equivalence-class claim)
**Classification**: GEOMETRIC (exhaustive catalog of external-paradigm constructions)
**Script**: `computations/s84_w7a_equiv_class_falsif.py` + literature review
**Agent type**: kaku-speculative-theorist

### Hypothesis

Pre-registered falsifier: if ANY string-theoretic construction in the published literature exhibits BOTH (a) KO-dimension = 6 (or admits a spectral triple at KO-dim = 6) AND (b) |E_cond| ~ L^4.68 (or non-linear power-law continuum-NCG scaling inconsistent with linear matrix-model classification), then the framework's structural-equivalence-class uniqueness claim is FALSIFIED.

### Background

- Framework's G32 PASS: d_spatial = 12 singleton; 11-dim M-theory excluded by 4 axiom violations (KO-dim shift, J² sign, Kasparov sector, Clifford spinor collapse).
- Framework's G36 PASS: |E_cond(L)| ~ L^4.681 with R² = 0.998 (vs IKKT matrix model's linear R² = 0.842). b_power = 4.680681 — a non-integer critical exponent indicating non-linear NCG scaling.
- Structural-equivalence-class claim (§VII.N in formation): the joint signature (KO-dim=6, A_F=ℂ⊕ℍ⊕M_3(ℂ), |E_cond|~L^4.68) is unique to the framework in the class of NCG spectral triples that admit observable-level gate closures.
- IKKT matrix model: excluded via R²=0.842 for linear fit, well below the R²=0.998 non-linear fit.
- Standard candidates: heterotic E_8 × E_8 (KO-dim=2, worldsheet), Type IIB (KO-dim=2), M-theory (d=11, excluded by G32), F-theory (d=12 total, different splitting), non-commutative tori (Connes 1980s, various KO-dim).

### Method

```
from canonical_constants import *

# Step 1: Exhaustive literature catalog — 3-stage search
# Stage A: String-theoretic constructions with KO-dim specification
# Stage B: Matrix models with power-law E_cond scaling
# Stage C: Cross-intersection: both A and B

# (local) lit_search_queries = [
#     "KO-dimension 6 spectral triple string theory",
#     "matrix model E_cond power law non-linear",
#     "NCG compactification Kasparov fundamental class",
#     "D-brane spectral triple bosonic action coupling",
#     "IKKT BFSS matrix model partition function",
#     "Kreuzer-Skarke KO-dim fiber classification",
# ]

# Step 2: Machine-search databases via mcp__paper-search tools
# (arxiv hep-th, math-ph; google scholar; pubmed irrelevant)
# (local) candidates = search_literature_batch(lit_search_queries, year_range=[1990, 2026])

# Step 3: For each candidate construction, extract KO-dim and E_cond scaling
# (local) catalog_rows = []
# for construction in candidates:
#     ko_dim = extract_ko_dimension(construction)
#     e_cond_scaling = extract_e_cond_scaling(construction)  # exponent in |E_cond|~L^p
#     catalog_rows.append((construction.paper_id, ko_dim, e_cond_scaling))

# Step 4: Joint-signature filter
# (local) joint_match = filter(catalog_rows,
#                              lambda row: row.ko_dim == 6 AND abs(row.e_cond_scaling - 4.68) < 0.5)

# Step 5: If joint_match non-empty, FAIL — structural-equivalence-class falsified
# (local) falsification_count = len(joint_match)

# Step 6: If joint_match empty, count near-misses (only one criterion satisfied)
# (local) one_criterion_only_ko = filter(catalog_rows, lambda r: r.ko_dim == 6)
# (local) one_criterion_only_ecd = filter(catalog_rows, lambda r: abs(r.e_cond_scaling-4.68)<0.5)

# Cross-checks:
#   (a) Completeness: catalog must cover the 5 major string-theory families
#       {Type IIA/IIB, heterotic E_8xE_8, heterotic SO(32), M-theory, F-theory}
#       plus NCG-specific programs (Connes-Chamseddine, Rennie-Varilly, etc.)
#   (b) Recency: include 2020-2026 arXiv submissions (framework emerged post-2020)
#   (c) Cross-language: check non-English literature for matrix-model results
#   (d) Double-blind: search inverse terms "NOT matching framework" to avoid confirmation bias
```

### PRDR machinery pin

- Matrix computation: catalog enumeration is text-processing and combinatorial — not linear algebra. GPU path: N/A.
- L_max: N/A (framework E_cond scaling fit at L=10 from G36; candidate papers must specify their L).
- Scheme: joint-signature predicate; binary (match/no-match) per paper.
- Convention: KO-dim = 6 interpreted strictly (not modulo 8 equivalence unless paper explicitly uses KO-dim mod 8); |E_cond|~L^p with 4.18 <= p <= 5.18 (±0.5 band around framework's 4.68) counts as match.
- Scan range: published literature from 1990 (birth of modern NCG physics) through 2026 April.
- Random seed: N/A.

### Pass/Fail/INFO thresholds

- **PASS**: falsification_count == 0 (zero constructions in literature exhibit both criteria). Framework's structural-equivalence-class uniqueness UPHELD.
- **INFO**: falsification_count == 0 BUT one_criterion_only_ko >= 1 AND one_criterion_only_ecd >= 1 (boundary cases — each criterion reproduced independently). Structural-equivalence-class stands but is not "maximally isolated."
- **FAIL**: falsification_count >= 1. Structural-equivalence-class claim FALSIFIED. Specific construction cited as counter-example. §VII.N landing DEFERRED pending resolution.

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- Literature search output (JSONL manifest of candidates reviewed): `<computed-at-runtime>`
- Framework's own G32 + G36 verdict file (S83): `<computed-at-runtime>`

### Expected output 4-tuple

`(value=falsification_count, scheme=joint_signature, convention=band_4.18_to_5.18, L_max=NA)`

### What PASS means for solution space

Zero constructions in literature satisfy both criteria. Framework occupies a UNIQUE structural position — no extant string-theoretic or NCG paradigm reproduces the joint KO-dim=6 + non-linear-E_cond signature. §VII.N lands as permanent. Strengthens rank-6 gear-machine classification: framework is the sole known member of its equivalence class.

### What FAIL means for solution space

At least one extant construction matches both criteria. Framework is NOT unique in its equivalence class. The matching construction becomes a potential "parent paradigm" — framework may admit uplift into it. §VII.N landing DEFERRED; structural-uniqueness claim RETREATS to "well-motivated but not unique." EVOI priority shifts toward characterizing the map to the matching construction.

### Pictorial explanation

Imagine a vast library of every theoretical-physics paper ever written. Each paper proposes a different "fingerprint" — a unique combination of dimensional content and scaling behavior. The framework's fingerprint is (KO-dim=6, power 4.68). The falsifier walks the library, comparing every paper's fingerprint to the framework's. If the walk completes with no match, the framework's fingerprint is unique — it is a NEW structural species. If a match is found, the framework has a sibling, and the question becomes: did they evolve independently, or is one a descendant of the other? Zero matches = unique species. One match = siblings, and we need to write a new phylogenetic tree.

### Carry-forward provision

Because this is long-horizon (literature catalog spans decades), the gate is EVALUATED INCREMENTALLY across S84-S88. Initial verdict at S84 close reports `falsification_count` based on the first-pass catalog (target: 50+ papers reviewed). Extended review in subsequent sessions updates the count. Falsification is MONOTONE — once a matching construction is found, the verdict becomes FAIL permanently (no retraction). Absence of match is PROVISIONAL until catalog is exhaustive.

---

## §W7a-80. S84-DYNAMICS-UNIQUENESS-GATE

**Gate ID**: S84-DYNAMICS-UNIQUENESS-GATE
**Trigger**: `[AUDIT]` (6-month literature review; systematic catalog)
**Classification**: PHONONIC (dynamics signatures are substrate-transit phenomena)
**Script**: `computations/s84_w7a_dynamics_uniqueness.py` + 6-month literature catalog
**Agent type**: kaku-speculative-theorist + mack-cosmic-bridge (observational liaison)

### Hypothesis

Systematic catalog of ~50 compactifications across major string/M-theory/F-theory families for joint dynamics signatures: {(i) cubic boundary condition at τ_fold = 0.19 ± 0.02 with integer-3 exponent, (ii) n_T > 0 curvature-locked at CMB scales, (iii) ≥10× frequency hierarchy between spectator and modulus modes, (iv) 4-speed ordering c_mod > c_BLV > c_BA > c_L}. If ANY construction reproduces ALL 4 signatures, the framework's dynamics are absorbed into that construction — UNIQUENESS FALSIFIED.

### Background

- Framework's joint dynamics signature is the most restrictive filter across all observables:
    - Signature (i): S42 τ_fold = 0.19 (3He-B inheritance), cubic-BC from S83 PRIMARY 188.34 GeV derivation.
    - Signature (ii): S64 n_T = +0.4676, BLUE tilt, Jensen-curvature-locked (NOT accessible at CMB scales per G46 transfer FAIL).
    - Signature (iii): 4-mode frequency hierarchy from S77+ substrate-action analysis (omega_mod > omega_BLV > omega_BA > omega_L by factors ≥10×).
    - Signature (iv): 4-speed ordering c_mod > c_BLV > c_BA > c_L from S77+ dispersion-relation analysis.
- Compactification families to catalog (target ~50):
    - KKLT (Kachru-Kallosh-Linde-Trivedi 2003) — Type IIB with flux
    - Racetrack (Kallosh-Linde 2004) — multi-exponential moduli stabilization
    - LVS (Large Volume Scenario, Conlon-Quevedo 2005)
    - Silverstein-Westphal (axion monodromy, 2008)
    - Heterotic Calabi-Yau 3-fold (CHSW 1985, many variants)
    - M-theory on G_2 manifolds (Acharya-Witten 2001)
    - F-theory on Calabi-Yau 4-folds (~500 classes from KS restriction)
    - CFT-side (matrix models, Liouville, WZW) — dim-reduction to dynamics
    - Various combinations

### Method

```
from canonical_constants import *

# Step 1: Build compactification catalog — primary literature
# (local) catalog_sources = {
#     'kklt': ['Kachru-Kallosh-Linde-Trivedi 2003', 'Denef 2008 review', ...],
#     'racetrack': ['Kallosh-Linde 2004', 'Kallosh-Sorbo 2008', ...],
#     'lvs': ['Conlon-Quevedo 2005', 'Cicoli-Quevedo review 2011', ...],
#     'silv_west': ['Silverstein-Westphal 2008', 'McAllister-Silverstein-Westphal 2010', ...],
#     'heterotic_cy3': ['CHSW 1985', 'Anderson-Gray-Lukas-Palti survey 2012', ...],
#     'm_g2': ['Acharya-Witten 2001', 'Acharya 2002', ...],
#     'f_cy4': ['Weigand TASI 2010', 'Krause-Mayrhofer-Weigand 2011', ...],
#     'cft_dyn': ['matrix model review 2002', 'Liouville dyn 2010', ...],
# }
# Total target: ≥50 distinct compactifications

# Step 2: For each compactification, extract 4-signature predictions or dynamics:
# (local) sig_extract = {}
# for paper in catalog_sources:
#     # Signature 1: does paper predict cubic-BC at specific tau with integer-3 exponent?
#     sig_extract[paper]['cubic_bc'] = extract_cubic_bc_prediction(paper)
#     # Signature 2: does paper predict n_T > 0 curvature-locked?
#     sig_extract[paper]['blue_nt'] = extract_tensor_tilt(paper)
#     # Signature 3: does paper predict 10x frequency hierarchy?
#     sig_extract[paper]['freq_hier'] = extract_mode_frequencies(paper)
#     # Signature 4: does paper predict 4-speed ordering c_mod>c_BLV>c_BA>c_L?
#     sig_extract[paper]['speed_order'] = extract_speed_hierarchy(paper)

# Step 3: Joint-signature filter (ALL 4 required)
# (local) full_match = filter(sig_extract.items(),
#                             lambda (paper, sigs): all(sigs[key] for key in
#                                                        ['cubic_bc','blue_nt','freq_hier','speed_order']))
# (local) three_of_four = filter(sig_extract.items(),
#                                lambda (paper, sigs): sum(sigs[key] for key in sigs) == 3)

# Step 4: Verdict computation
# (local) N_all_four = len(full_match)
# (local) N_three_of_four = len(three_of_four)

# Step 5: Per-family breakdown (track which families approach signature closure)
# (local) per_family_count = aggregate_by_family(full_match, three_of_four)

# Cross-checks:
#   (a) Sampling bias: catalog must span all 8 families (not just KKLT variants)
#   (b) Year coverage: pre-2000, 2000-2010, 2010-2020, 2020-2026 quarters
#   (c) Review-paper triangulation: cite at least 3 independent reviews per family
#   (d) Negative controls: include ΛCDM slow-roll inflaton as null-hypothesis entry
#   (e) Framework entry: include phonon-exflation as control (should satisfy all 4)
```

### PRDR machinery pin

- Matrix computation: catalog aggregation — no linear algebra. GPU path: N/A.
- L_max: N/A.
- Scheme: 4-signature joint predicate with per-signature tolerances
    - cubic_bc: tau within [0.15, 0.25] AND exponent in [2.5, 3.5]
    - blue_nt: n_T > 0 at CMB pivot scale (k = 0.05 Mpc^-1) with explicit model prediction
    - freq_hier: omega_max / omega_min >= 10 with ≥4 distinct modes
    - speed_order: explicit strict inequality chain c_mod > c_BLV > c_BA > c_L
- Convention: each paper independently surveyed; no cherry-picking; include all papers in a family.
- Scan range: all compactification literature 1985-2026.
- Random seed: N/A (deterministic catalog).
- Catalog size: ≥50 papers required to declare catalog "representative"; ≥200 required for "exhaustive."

### Pass/Fail/INFO thresholds

- **PASS**: N_all_four == 0 AND N_three_of_four ∈ [0, 2]. Zero constructions reproduce all 4 signatures; at most 2 reproduce 3 of 4. Framework dynamics are STRUCTURALLY UNIQUE.
- **INFO**: N_all_four == 0 AND N_three_of_four >= 3. Zero full matches but ≥3 constructions approach within one signature. Uniqueness stands but proximity constructions warrant follow-up.
- **FAIL**: N_all_four >= 1. At least one compactification reproduces all 4 signatures. Framework dynamics are ABSORBED into that construction. Specific paper cited. §VII.N + rank-6 gear-machine classification require revision.

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- Literature catalog manifest (JSONL, ≥50 papers with 4-signature extraction): `<computed-at-runtime>`
- Framework's own S42, S64, S77+ dynamics predictions file: `<computed-at-runtime>`
- Canonical 4-signature constants (tau_fold=0.19, n_T=+0.4676, mode frequencies, speed hierarchy): `<computed-at-runtime>`

### Expected output 4-tuple

`(value=(N_all_four, N_three_of_four), scheme=joint_signature_4, convention=per_family_tolerance, L_max=NA)`

### What PASS means for solution space

Zero compactifications in ≥50-paper catalog reproduce all 4 dynamics signatures simultaneously. Framework's dynamics are UNIQUE in the known string-theory landscape. Strengthens MG-1 τ_fold=0.190 uniqueness (no other construction lands at this specific value with cubic-BC). Jointly with W7a-79 PASS, §VII.N lands as permanent + upgrades rank-6 gear-machine to "sole known host."

### What FAIL means for solution space

At least one compactification reproduces all 4 signatures. Framework dynamics are absorbed. The matching construction becomes the prime candidate for "parent paradigm." Immediate consequences:
- §VII.N landing DEFERRED pending uplift-to-parent analysis
- Rank-6 gear-machine (MG-0, MG-1, MG-2) retreats from "unique classification" to "instance of broader class"
- Framework predictions become consistency checks, not signatures
- Mark N_all_four matches for S85 detailed uplift construction

### Pictorial explanation

Imagine ~50 different compactification physicists, each holding a blueprint for how extra dimensions might be organized. The framework holds a 4-signature predicate like a biometric: (fingerprint shape, iris pattern, voice print, gait). The test walks all 50 physicists, checks each for the 4 biometric features in combination. Zero full matches means the framework's biometric is unique — no one else has the same fingerprint AND iris AND voice AND gait. One full match means there is a hidden twin. Given how restrictive the joint predicate is (multiplicatively reducing acceptance probability), a zero-match outcome is expected but not guaranteed. The test IS the test.

### Carry-forward provision

Because this is a 6-month literature review, the verdict is INCREMENTALLY REPORTED over S84-S90. Target milestones:
- S84 close: catalog ≥5/50 with 4-signature extraction attempted; initial per-family breakdown.
- S85 close: catalog ≥15/50.
- S87 close: catalog ≥35/50.
- S90 close: catalog ≥50/50; full PASS/INFO/FAIL verdict.
Falsification is MONOTONE (once an all-4 match is found, verdict FAILs permanently). Absence of match is PROVISIONAL until catalog target reached.

---

## W7a → W7b Parallel Dispatch Note

W7a (gates 72, 73, 74, 79, 80) and W7b (gates 75, 76, 77, 78, 81, 82, 83, 84) are INDEPENDENT parallel waves — no gate in W7a depends on a gate in W7b. Dispatch cap (≤8 concurrent agents per session rule) accommodates both waves simultaneously: 5 W7a agents + up to 3 W7b agents at a time. Gates 79 and 80 are long-horizon — their S84 verdicts are PROVISIONAL and extend across S85-S90.

W7b gate 78 (S84-CORRESPONDENCE-TABLE-CLOSURE) consumes the W7a verdicts as inputs: if W7a gates return (HET-DECOMP=FAIL, FTH-UPLIFT=FAIL, DET-P-K-THEORY=FAIL, EQUIV-CLASS-FALSIF=PASS), the correspondence table gains 3 new ANTI entries and the open-lead count drops to zero. If any W7a positive-correspondence gate returns PASS, correspondence table gains a new GENUINE entry.

---

## W7a → W8 Decision Point (joint with W7b)

At S84 close, W7a contributes to the joint W7+W8 decision:

**Scenario A** (all W7a gates aligned favorably):
- HET-DECOMP = FAIL, FTH-UPLIFT = FAIL, DET-P-K-THEORY = FAIL
- EQUIV-CLASS-FALSIF = PASS, DYNAMICS-UNIQUENESS (provisional) = PASS
- Consequence: §VII.N lands at S84 close; rank-6 gear-machine classification UPGRADED.

**Scenario B** (mixed):
- One or more positive-correspondence gates PASS (framework admits external uplift)
- EQUIV-CLASS-FALSIF = PASS
- Consequence: §VII.N lands with uplift-map characterization appended; framework admits parent paradigm.

**Scenario C** (falsified):
- EQUIV-CLASS-FALSIF = FAIL, OR
- DYNAMICS-UNIQUENESS (provisional) = FAIL
- Consequence: §VII.N landing DEFERRED; structural-uniqueness claim retreats; uplift-to-parent becomes HIGH EVOI target for S85.

The decision at W8 depends on the specific scenario. Prompter builds decision-tree scaffolding in the S84 working paper §VII.N-DECISION-TREE.

---

## W7a Machinery-Enumeration Pin (§0.11)

Per PRDR (Pre-Registration Dry-Run) requirement (.claude/rules/epistemic-discipline.md §PRU), every gate-relevant machinery parameter is enumerated below. Any parameter listed here but left as "<free>" indicates PRU vulnerability — the plan MUST declare these as diagnostic or pin a value before dispatch.

| Gate | Parameter | Pinned value | Source |
|:-----|:----------|:-------------|:-------|
| 72 | branching_normalization | Slansky 1981 | Slansky Phys. Rep. 79:1 |
| 72 | heterotic_embedding | standard (CHSW 1985) | Candelas et al. NPB 258:46 |
| 72 | U(1)_Y_convention | (1/6)(B-L) with SU(5) Georgi-Glashow | PDG 2024 |
| 73 | CY_4fold_catalog | KS restricted subset, N<=1000 sample | Kreuzer-Skarke 2000 |
| 73 | F_theory_convention | Weigand TASI 2010 | arXiv:1009.3497 |
| 73 | base_dim | {3, 8} alternative interpretations | framework d_spatial=12 |
| 73 | torch.linalg | GPU on RX 9070 XT, ROCm 7.2 | canonical |
| 73 | OMP_NUM_THREADS | 8 (CPU fallback for small 4-folds) | .claude/rules/math-scripts.md |
| 73 | random_seed | 84073 | reproducibility |
| 74 | Kasparov_KK_normalization | Connes-Skandalis 1984 | CS Publ. RIMS 20:1139 |
| 74 | Witten_anomaly_convention | Witten 1998 JHEP 9812:019 | D-Branes and K-Theory |
| 74 | Bott_periodicity | 8-fold real, 2-fold complex | standard |
| 79 | literature_search_range | 1990-2026 | NCG physics birth to present |
| 79 | KO_dim_tolerance | strict (no mod-8) unless paper specifies | auditable |
| 79 | E_cond_exponent_band | [4.18, 5.18] (framework 4.68 ± 0.5) | G36 uncertainty |
| 79 | search_engines | arxiv, google_scholar, INSPIRE-HEP | multi-source |
| 80 | catalog_size_target | 50 min / 200 goal | representative/exhaustive |
| 80 | signature_tolerances | (0.15<=tau<=0.25, n_T>0, ratio>=10x, strict speed order) | per-signature |
| 80 | family_coverage | all 8 families (min 5 papers each) | sampling bias control |
| 80 | year_quartile_coverage | all 4 quartiles (pre-2000, 2000-2010, 2010-2020, 2020+) | recency control |
| 80 | review_paper_triangulation | ≥3 independent reviews per family | triangulation |

Diagnostic-declared (non-PASS/FAIL impact):

- Gate 72: family count in heterotic-CY3 landscape (diagnostic; feeds into per-family PASS proximity)
- Gate 73: per-4-fold matter spectrum (diagnostic; only presence of SM-at-single-point is gate-relevant)
- Gate 79: near-miss catalog (one-criterion matches, INFO-level only)
- Gate 80: N_three_of_four (INFO-level; gate-relevant only if N_all_four == 0)

---

## W7a Input-SHA Ledger

All ledger entries are `<computed-at-runtime>` — SHAs will be written to verdict lines upon script execution. Canonical SHA discipline: 64-character hexdigest mandatory (per .claude/rules/gate-verdicts.md); dual-SHA schema_version=S84+ with both `audit_sha256` and `content_sha256`.

| Gate | Inputs | SHA status |
|:-----|:-------|:-----------|
| 72 | canonical_constants.py, slansky_branching_table.json, AF_quantum_numbers.json | all `<computed-at-runtime>` |
| 73 | canonical_constants.py, ks_4fold_excerpt.json, weigand_tasi_formulas.json | all `<computed-at-runtime>` |
| 74 | canonical_constants.py, s45_poincare_matrix.npy, witten_anomaly_identity.txt | all `<computed-at-runtime>` |
| 79 | canonical_constants.py, lit_search_manifest.jsonl, s83_g32_g36_verdicts.txt | all `<computed-at-runtime>` |
| 80 | canonical_constants.py, compactification_catalog.jsonl, s42_s64_s77_dynamics.txt | all `<computed-at-runtime>` |

Closure SHA = SHA-256(sorted ordered input-pin map). Every script prints closure SHA in first 20 lines of stdout; verdict line is final non-verdict line with closure SHA appended.

Dual-SHA schema (S84+):
- `audit_sha256`: SHA-256 of input-pin map (reproducibility)
- `content_sha256`: SHA-256 of script source (tamper detection)

Both mandatory on verdict line per S84+ schema.

---

## W7a Expected Outputs

Per-gate deliverables required before S84 verdict-log close:

- `computations/s84_w7a_het_decomp.py` (non-stub, non-trivial size)
- `computations/s84_w7a_fth_uplift.py`
- `computations/s84_w7a_det_p_k_theory.py`
- `computations/s84_w7a_equiv_class_falsif.py`
- `computations/s84_w7a_dynamics_uniqueness.py`
- `computations/s84_gate_verdicts.txt` appended with 5 verdict lines (gates 72, 73, 74, 79 INITIAL, 80 INITIAL)
- Working-paper §VII.N (IKKT anti-correspondence + 11-dim exclusion) with W7a results incorporated and landing decision
- Working-paper §VII.N-DECISION-TREE scaffold
- Literature catalog manifest files (JSONL) for gates 79, 80
- Carry-forward entries for S85 W7a-continuation (gates 79, 80 incremental review)

---

## W7a Closing Note

Gates 72-74 are positive-correspondence tests — they ask "can the framework be uplifted into an external paradigm?" Gates 79-80 are negative-correspondence falsifiers — they ask "does an external paradigm exhibit the framework's joint signature?" The two tests are ASYMMETRIC: a PASS on positive correspondence and a PASS on negative falsifier are both informative, but in different directions. Positive PASS + negative PASS = framework has uplift but is unique in joint signature (highly desirable). Positive FAIL + negative PASS = framework is structurally isolated, admits no uplift, but is unique (the §VII.N scenario, favored by G32+G36 priors). Positive FAIL + negative FAIL = framework is structurally isolated but has a twin with all 4 signatures somewhere — the most informative FAIL outcome, because it identifies a parent paradigm while respecting §VII.N anti-correspondences.

The wave is designed so that ALL four outcome-quadrants are maximally informative for the constraint map. No dispatch returns null information.
