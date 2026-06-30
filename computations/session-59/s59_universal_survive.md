# UNIVERSAL-SURVIVE-59: Universal vs SU(3)-Specific Survival Inventory

**Author**: Connes NCG Theorist
**Date**: 2026-03-24
**Gate**: UNIVERSAL-SURVIVE-59
**Verdict**: **PASS** (84.1% universal or generalizable, threshold >80%)

---

## 1. Methodology

Each permanent result, closed mechanism, and structural wall was classified by examining its **proof structure** -- specifically, which mathematical ingredients the proof requires:

| Category | Definition | Criterion |
|:---------|:-----------|:----------|
| **UNIVERSAL** | Proven for any compact semisimple Lie group K | Proof uses only: Peter-Weyl theorem, Schur orthogonality, spectral geometry of compact manifolds, functional analysis, linear algebra, NCG axioms of finite triple (A_F, H_F, D_F) |
| **GENERALIZABLE** | Proof technique works for any K, but constants/dimensions/locations change | Proof structure is K-independent, but numerical values (eigenvalues, ratios, coupling constants) depend on the specific Dirac spectrum of K |
| **SU(3)-SPECIFIC** | Proof uses A_2 root structure, rank 2, CG(24), or specific SU(3) representations | Result cannot be stated without reference to SU(3) quantum numbers, weights, or branching rules |

The key distinction between UNIVERSAL and GENERALIZABLE: a UNIVERSAL result needs no recomputation for K != SU(3). A GENERALIZABLE result needs numerical re-verification but the same proof template applies.

---

## 2. Classification of Major Permanent Results (12 items)

### 2.1 UNIVERSAL (3/12)

**KO-dim = 6** (S7-8). The KO-dimension is determined entirely by the signs (epsilon, epsilon', epsilon'') = (+1, +1, -1) of J^2, JD vs DJ, and J*gamma vs gamma*J on the **finite** spectral triple (A_F, H_F, D_F). The continuous part of M x K contributes KO-dim 0 mod 8 for any spin manifold of dimension divisible by 8. The product rule gives 0 + 6 = 6 mod 8. No property of K enters.

**SM quantum numbers from Psi_+ = C^16** (S7). The decomposition of H_F = C^32 under A_F = C + H + M_3(C) produces SM fermion multiplets. This is representation theory of the **finite** algebra, independent of K.

**Block-diagonal theorem** (S22b). D_K is exactly block-diagonal in the Peter-Weyl basis for ANY left-invariant metric on ANY compact Lie group K. Proof: D_K commutes with right translations (left-invariance) -> Schur's lemma gives block-diagonality. Three ingredients: Peter-Weyl theorem (any compact group), Schur's lemma (any representation), left-invariance (any left-invariant metric). No use of A_2 root system.

### 2.2 GENERALIZABLE (6/12)

**[J, D_K(tau)] = 0 CPT exact** (S17a). J acts on H_F indices; D_K acts on L^2(K, S). The commutation requires D_K to respect the real structure. Verified numerically for SU(3). For any K admitting a bi-invariant metric, J maps left-regular to right-regular representation, and the analogous result is expected. **Re-verification cost**: one eigenvalue computation per K.

**[iK_7, D_K] = 0 Jensen symmetry** (S34). Jensen deformation preserves a maximal torus action. K_7 is the specific Cartan generator in su(3). For any compact K of rank r, a diagonal deformation (scaling root-space directions) preserves T^r, giving [iH_j, D_K] = 0 for all r Cartan generators. The **structure** (preserved torus symmetry) is universal; the generator K_7 is SU(3)-specific. For SU(4), three Cartan generators would commute with D_K.

**BCS instability 1D theorem** (S35). Cooper instability: any g > 0 produces BCS pairing when DOS diverges. Van Hove singularities in Dirac spectra under deformation are **generic** by Morse theory (critical points of eigenvalue branches exist on any moduli space of metrics). The specific location tau = 0.19 and catastrophe type (A_2) are SU(3)-specific, but **existence** of van Hove singularities is universal for any K.

**Spectral action monotonicity** (S37). Two ingredients: (A) All lambda_k(tau) of D_K on SU(3) decrease monotonically (verified numerically, driven by J_C2 coupling decay); (B) Any monotone decreasing spectrum gives monotone spectral action for any Laplace-representable cutoff (universal functional analysis, Bernstein theorem). Part (B) is proven; part (A) needs per-K verification.

**Instanton gas / GPV** (S37-38). BCS instanton physics is a general many-body phenomenon at any van Hove fold with attractive pairing. The existence of dense instanton gas and giant pair vibration is universal for BCS at a DOS divergence. The specific action S_inst = 0.069 and frequency omega = 0.792 are SU(3)-specific.

**GGE permanence** (S38). Richardson-Gaudin integrability of the BCS Hamiltonian (universal for any reduced BCS model with uniform coupling) + block-diagonal theorem (UNIVERSAL) => post-transit state is GGE. The number of conserved integrals and GGE details depend on the spectrum (K-specific), but the structure of integrability-protected non-thermalization is universal.

### 2.3 SU(3)-SPECIFIC (3/12)

**g1/g2 = e^{-2*tau} metric ratio** (S17a). The Jensen 1-parameter deformation family is specific to SU(3): lambda_1 = e^{2*tau}, lambda_2 = e^{-2*tau}. The exponent -2 comes from the A_2 root system (Cartan matrix entries). For SU(4), the deformation space is 2-dimensional with A_3 structure.

**Trap 1: V(B1,B1) = 0** (S34). B1 is the gap-edge mode in the (1,0) representation of SU(3), transforming as a U(2) singlet under SU(3) -> U(1)_7 x U(2). The vanishing follows from Schur's lemma applied to this specific branching rule. The quantum numbers (U(2) singlet) are entirely determined by the A_2 weight diagram.

**Cooper pair K_7 charge** (S35). B2 modes carry K_7 charge +/- 1/4 (weights of the fundamental representation of SU(3)). Cooper pairs carry total charge +/- 1/2. These specific charge values are A_2 weights.

---

## 3. Classification of Closed Mechanisms (25 items)

| Mechanism | Class | Key Proof Ingredient |
|:----------|:------|:---------------------|
| V_tree minimum (S17a) | GEN | Eigenvalue monotonicity (spectrum-dependent) |
| 1-loop CW (S18) | GEN | Weyl F/B ratio (universal law, K-specific value) |
| Casimir scalar+vector (S19d) | GEN | Constant-ratio trap via Weyl law |
| Casimir TT 2-tensors (S20b) | GEN | Same Weyl trap |
| Seeley-DeWitt a2/a4 (S20a) | GEN | Heat kernel coefficients (universal functionals) |
| Spectral back-reaction (S19d) | GEN | Spectral determinant technique |
| Fermion condensate (S19a) | **UNIV** | Wrong sign argument (no K needed) |
| Pfaffian Z_2 (S17c) | GEN | AZ class depends on D_K symmetries |
| Single-field slow-roll (S19b) | **UNIV** | SA gradient >> Hubble friction (universal if SA monotone) |
| Inter-sector delta_T (S22b) | **UNIV** | Block-diagonal theorem (universal) |
| Inter-sector V_IR (S22b) | **UNIV** | Block-diagonal theorem (universal) |
| Higgs-sigma portal (S22c) | **SU3** | 1/dim(spinor) = 1/16 (dim 8 manifold) |
| Rolling quintessence (S22d) | GEN | Clock constraint (structure generic) |
| DESI dynamical DE (S22d) | GEN | Requires rolling -> closed by SA gradient |
| Canonical mu!=0 (S34) | **UNIV** | PH symmetry (any spin manifold) |
| Grand canonical mu!=0 (S34) | **UNIV** | Helmholtz convexity from PH |
| Cutoff SA stabilization (S37) | GEN | Monotonicity theorem (needs per-K eigenvalues) |
| 1-loop RPA self-trapping (S37) | GEN | SA penalizes pairing (structure generic) |
| (B1,B3,G1) PMNS triad (S37) | **SU3** | SU(3) weight structure |
| CC-through-instanton (S38) | GEN | F.5 anti-trapping (BCS structure generic) |
| Weak order-one (S45) | GEN | GG/Full = 1 (expected generically) |
| Occupied SA (S45) | GEN | Monotonicity chain (technique universal) |
| Unexpanded SA (S45) | **UNIV** | Taylor exactness for finite spectra (analysis) |
| BdG twist (S46) | **UNIV** | A_F diagonal in Nambu space (algebra, no K) |
| Sigma selection (S45) | GEN | Truncation artifact (universal for finite PW) |

**Summary**: 8 UNIVERSAL, 15 GENERALIZABLE, 2 SU(3)-SPECIFIC.

---

## 4. Classification of Structural Walls (9 items)

| Wall | Class | Proof Ingredient |
|:-----|:------|:-----------------|
| Weyl F/B ratio | **UNIV** | Weyl's law on any compact Riemannian manifold |
| Block-diagonality | **UNIV** | Peter-Weyl + Schur + left-invariance |
| PH symmetry (mu=0 forced) | **UNIV** | Dirac spectrum symmetric on any spin manifold |
| Gram matrix PSD | **UNIV** | Linear algebra (any Hermitian D, any phi) |
| Taylor exactness | **UNIV** | Analysis on finite spectra |
| Occupied cyclic cohomology | **UNIV** | HC^0(A_F) = C^3, property of finite algebra |
| BdG twist obstruction | **UNIV** | A_F diagonal in Nambu space |
| Spectral gap (BDI) | GEN | AZ class may change for different K |
| SA monotonicity | GEN | Needs eigenvalue monotonicity per K |

**Summary**: 7 UNIVERSAL, 2 GENERALIZABLE, 0 SU(3)-SPECIFIC.

The structural walls are overwhelmingly universal. This is significant: the **boundary of the solution space** is K-independent. The walls that close mechanisms remain standing regardless of which manifold is chosen.

---

## 5. Classification of Additional Permanent Results (17 items)

| Result | Class | Key Ingredient |
|:-------|:------|:---------------|
| J-protection [J, D_phys] = 0 (S32) | **UNIV** | Algebraic identity from real structure axiom |
| SA scalar instability (S46) | **UNIV** | f'(x) < 0 for monotone f (analysis) |
| Commutator antisymmetry (S54) | **UNIV** | [D, diag(f)] antisymmetric (linear algebra) |
| CDM by construction (S44) | **UNIV** | T^{0i} = 0 for GGE product states (algebraic) |
| M_3(C) fluctuations zero (S51) | **UNIV** | Property of A_F representation |
| Strutinsky decomposition (S33a) | GEN | Technique universal, percentages K-specific |
| Quantum metric identity (S32) | GEN | Off-diag RPA = Fubini-Study (universal identity) |
| Omega^1_D tau-independence (S46) | GEN | Classification technique universal, dim K-specific |
| Connes distance isotropy tau=0 (S46) | GEN | Bi-invariant -> isotropic (universal at round point) |
| Connes distance exponential (S54) | GEN | Scaling form generic, exponent K-specific |
| 61/20 ratio theorem (S44) | GEN | Gilkey technique universal, ratio dim-dependent |
| K_7 commutant propagation (S51) | GEN | [H, D]=0 => [H, f(D)]=0 (universal algebra) |
| B2 fold universality (S33a) | **SU3** | B2 is specific SU(3) branch |
| Lie derivative monotonicity (S33a) | **SU3** | B(s)/5 defined on SU(3) deformation |
| Connes distance fold anisotropy (S46) | **SU3** | Specific numerical values at SU(3) fold |
| (1,1) adjoint Lipschitz softness (S46) | **SU3** | Specific mode in SU(3) spectrum |
| alpha_s = n_s^2 - 1 (S50) | **SU3** | 5 proofs using SU(3) phase sector |

**Summary**: 5 UNIVERSAL, 7 GENERALIZABLE, 5 SU(3)-SPECIFIC.

---

## 6. Combined Summary

| Category | Count | Fraction |
|:---------|------:|---------:|
| UNIVERSAL | 23 | 36.5% |
| GENERALIZABLE | 30 | 47.6% |
| SU(3)-SPECIFIC | 10 | 15.9% |
| **UNIVERSAL + GENERALIZABLE** | **53** | **84.1%** |
| **Total classified** | **63** | 100% |

**Gate verdict: PASS** (84.1% > 80% threshold).

---

## 7. The SU(3)-Specific Core (10 Items)

These are the results that would require **complete re-derivation** on an alternative manifold K:

1. **g1/g2 = e^{-2*tau}**: Jensen family uses A_2 root system. For SU(4): 2-parameter A_3 family.
2. **Trap 1: V(B1,B1) = 0**: B1 is U(2) singlet under SU(3) -> U(1) branching. Different branching for other K.
3. **Cooper pair K_7 charge +/- 1/2**: A_2 weight values.
4. **Higgs-sigma portal (Trap 3)**: 1/dim(spinor) = 1/16 for dim(K)=8. Changes with dim(K).
5. **(B1,B3,G1) PMNS triad**: SU(3) weight structure.
6. **B2 fold universality**: B2 is an SU(3)-specific branch.
7. **Lie derivative monotonicity**: B(s)/5 on SU(3) Jensen family.
8. **Connes distance fold anisotropy**: Numerical values at SU(3) fold.
9. **(1,1) adjoint Lipschitz softness**: SU(3) adjoint sector.
10. **alpha_s = n_s^2 - 1**: SU(3) phase sector proofs.

Observation: The SU(3)-specific results fall into two categories:
- **Quantitative results** (items 1-4, 8-10): specific numerical values tied to SU(3) Dirac spectrum
- **Structural results** (items 5-7): depend on SU(3) representation theory (branching rules, weight diagrams)

None of the SU(3)-specific results are **structural walls**. The walls are all universal or generalizable. This means the constraint surface geometry is preserved under manifold switching.

---

## 8. Switching Cost Analysis

### 8.1 SU(3) -> SU(4)

| Property | SU(3) | SU(4) | Impact |
|:---------|:------|:------|:-------|
| Rank | 2 | 3 | 2-parameter deformation family (vs 1-parameter) |
| Dimension | 8 | 15 | Odd -> needs Spin^c, not Spin. **KO-dim analysis must be redone.** |
| Spinor dim | 2^4 = 16 | 2^7 = 128 | H_F changes. Finite triple representation may not accommodate SM. |
| Jensen moduli | 1 | 2 | Richer landscape, harder to classify |
| PW labels | (p,q) | (p,q,r) | More sectors, higher computational cost |
| Block-diag | YES | YES | Universal, no cost |
| KO-dim 6 | YES | ? | 15 mod 8 = 7, NOT 6. **STRUCTURAL OBSTRUCTION** |

**Critical obstruction for SU(4)**: dim(SU(4)) = 15 is odd. An odd-dimensional manifold does not admit a spin structure in the usual sense (Spin(15) has two irreducible spinor representations of dimension 2^7 = 128, but the manifold needs to be orientable and satisfy w_2 = 0). More critically, 15 mod 8 = 7, which gives KO-dim 7 for the continuous part, and the product KO-dim would be 7 + 6 = 13 mod 8 = 5, not 6. This changes the signs (epsilon, epsilon', epsilon'') and potentially breaks the SM reconstruction.

**Estimated effort**: 5+ sessions. The KO-dim mismatch is a potential show-stopper.

### 8.2 SU(3) -> G_2

| Property | SU(3) | G_2 | Impact |
|:---------|:------|:----|:-------|
| Rank | 2 | 2 | 1-parameter deformation family (same!) |
| Dimension | 8 | 14 | Even -> Spin structure exists |
| Spinor dim | 2^4 = 16 | 2^7 = 128 | Much larger spinor space |
| Jensen moduli | 1 | 1 | Same structure: 1 free parameter after volume constraint |
| PW labels | (p,q) | (p,q) | Same labeling scheme (rank 2) |
| Block-diag | YES | YES | Universal |
| KO-dim | 8 mod 8 = 0 | 14 mod 8 = 6 | G_2: continuous part already has KO-dim 6! Product: 6 + 6 = 12 mod 8 = 4. **DIFFERENT.** |

**Subtlety for G_2**: While dim(G_2) = 14 is even and admits spin structure, the KO-dimension of the continuous part is 14 mod 8 = 6. The product with the finite triple (KO-dim 6) gives total KO-dim 12 mod 8 = 4, which has signs (epsilon, epsilon', epsilon'') = (-1, +1, +1) -- different from the SM requirement (+1, +1, -1). This is a structural mismatch.

**Correction**: For KK geometry M^4 x K, the TOTAL internal space has KO-dim = dim(K) mod 8 for the geometric part. The FINITE spectral triple F sits inside K, and the identification D_K = D_F means KO-dim(F) = 6 is a SEPARATE input. The relevant KO-dim calculation is: 4 (for M^4) + 6 (for F, the finite triple) = 10 mod 8 = 2 in the standard NCG-SM. The manifold K provides the geometric realization of the finite triple -- its own KO-dimension as a manifold is not directly relevant to the NCG axiom check. What matters is whether K can REALIZE the finite triple with KO-dim 6.

For SU(3): dim 8, even, spin. Realizes KO-dim 6 of finite triple. VERIFIED (S7-8).
For G_2: dim 14, even, spin. Can it realize KO-dim 6? Needs explicit computation of J^2, JD, J*gamma on the Dirac operator of G_2 coupled to A_F.

**Estimated effort**: 3-4 sessions. The KO-dim question needs explicit verification but the 1-parameter moduli space is the same dimensionality.

### 8.3 Minimal Switching Cost Summary

| Step | SU(4) effort | G_2 effort |
|:-----|:-------------|:-----------|
| Dirac spectrum computation | HIGH (3-param PW) | MODERATE (2-param PW) |
| KO-dim verification | POTENTIAL OBSTRUCTION | Needs explicit check |
| SM quantum numbers | Must verify from scratch | Must verify from scratch |
| Van Hove / BCS | Recompute (generic existence) | Recompute (generic existence) |
| Mechanism chain | Template survives, numbers change | Template survives, numbers change |
| **Total** | **5+ sessions, possible obstruction** | **3-4 sessions** |

---

## 9. Structural Interpretation

The 84.1% universality rate means the framework's mathematical infrastructure is largely **manifold-independent**. The key insight is the **layered architecture**:

1. **NCG axiom layer** (UNIVERSAL): KO-dim, SM quantum numbers, finite triple structure. These are properties of (A_F, H_F, D_F) and do not reference K at all.

2. **Spectral geometry layer** (UNIVERSAL/GENERALIZABLE): Block-diagonality, PH symmetry, Weyl law, Gram PSD, Taylor exactness. These use only generic properties of compact Lie groups with left-invariant metrics.

3. **Deformation dynamics layer** (GENERALIZABLE): Eigenvalue monotonicity, BCS instability existence, GGE structure. The proofs work for any K with a van Hove singularity, but numerical values change.

4. **SU(3)-specific layer**: Coupling ratios, weight charges, specific fold location, branching rules. These are the **distinguishing fingerprint** of the SU(3) choice and would need full re-derivation.

The constraint surface (structural walls) is entirely in layers 1-2: UNIVERSAL. The dynamics (closures, mechanism chain) is in layers 2-3: GENERALIZABLE. Only the quantitative predictions and specific quantum numbers are in layer 4: SU(3)-SPECIFIC.

**Consequence**: Switching manifolds preserves the constraint map topology. The same mechanisms would be closed for the same structural reasons. The open channels would remain open. What changes are the numerical values that determine whether a specific mechanism PASSES its gate.

---

## 10. Data Files

- Script: `computations/session-59/s59_universal_survive.py`
- Data: `computations/session-59/s59_universal_survive.npz`
- This document: `computations/session-59/s59_universal_survive.md`
