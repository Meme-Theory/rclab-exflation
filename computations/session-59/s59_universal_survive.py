"""
S59 UNIVERSAL-SURVIVE-59: Universal vs SU(3)-Specific Survival Inventory
Connes NCG Theorist

Classifies all permanent results, closed mechanisms, and structural walls into:
  UNIVERSAL    - proven for any compact semisimple Lie group K
  GENERALIZABLE - proof technique works for any K, but constants/dimensions change
  SU3_SPECIFIC  - proof uses A_2 root structure, rank 2, CG(24), or dim=8

Outputs: s59_universal_survive.npz with classification counts and gate verdict.
"""

import numpy as np

# ============================================================
# CLASSIFICATION CATEGORIES
# ============================================================
UNIVERSAL = "UNIVERSAL"
GENERALIZABLE = "GENERALIZABLE"
SU3_SPECIFIC = "SU(3)-SPECIFIC"

# ============================================================
# 1. MAJOR PERMANENT RESULTS (12 items from task specification)
# ============================================================

permanent_results = {
    # --- Result: KO-dimension = 6 ---
    # Proof structure: KO-dim is determined by the signs (eps, eps', eps'') of J^2, JD vs DJ,
    # J*gamma vs gamma*J. For the NCG Standard Model, these signs come from A_F = C + H + M_3(C)
    # acting on H_F = C^32. The algebra A_F and its representation are CHOSEN to reproduce
    # SM quantum numbers. The KO-dim 6 is a property of the FINITE spectral triple (A_F, H_F, D_F),
    # not of SU(3) geometry per se. The verification that D_K on SU(3) is compatible with
    # KO-dim 6 uses the spin structure on an 8-manifold (KO-dim 0 mod 8 for dim 8 manifold,
    # then 6 from the finite part). Any compact 8-manifold with spin structure gives KO-dim 0
    # for the continuous part. The KO-dim 6 of the finite part is INDEPENDENT of which
    # manifold K is.
    "KO-dim = 6": {
        "classification": UNIVERSAL,
        "proof_uses": "NCG axioms on (A_F, H_F, D_F). Signs (eps,eps',eps'')=(+1,+1,-1) "
                      "from representation theory of A_F = C+H+M_3(C) on H_F = C^32. "
                      "Continuous part contributes KO-dim 0 for ANY spin 8-manifold. "
                      "Product rule: 0 + 6 = 6 mod 8.",
        "K_dependence": "None. KO-dim 6 is a property of the finite triple, not of K.",
        "session": "S7-8"
    },

    # --- Result: SM quantum numbers from Psi_+ = C^16 ---
    # The SM particle content is encoded in H_F = C^32 = C^16 + C^16 (particle + antiparticle).
    # The C^16 decomposes under A_F = C + H + M_3(C) to give exactly the SM fermion
    # representations. This is a property of the ALGEBRA and its representation,
    # not of SU(3) geometry.
    "SM quantum numbers from C^16": {
        "classification": UNIVERSAL,
        "proof_uses": "Representation theory of A_F on H_F. The algebra A_F = C+H+M_3(C) "
                      "and its action on C^32 determine SM quantum numbers. "
                      "This is the finite spectral triple, independent of K.",
        "K_dependence": "None. H_F is the same regardless of which compact K is used.",
        "session": "S7"
    },

    # --- Result: [J, D_K(tau)] = 0 CPT exact ---
    # J is the charge conjugation operator of the finite triple. D_K is the Dirac operator
    # on the compact manifold K. The commutativity [J, D_K] = 0 was verified numerically
    # at machine epsilon for SU(3). The proof structure: J acts on the finite part (H_F),
    # D_K acts on the continuous part (L^2(K, S)). In the product triple M x F, the total
    # Dirac operator is D = D_M tensor 1 + gamma_M tensor D_F. For the almost-commutative
    # product, J_total = J_M tensor J_F (up to signs from KO-dim). The commutation [J_total, D_total] = 0
    # follows from the individual commutation relations, which depend on KO-dimensions.
    # For the INTERNAL D_K alone: [J_F, D_K] = 0 requires that D_K commutes with the
    # real structure of the finite triple. This was verified NUMERICALLY on SU(3).
    # On a general compact K, the analogous D_K would be a different operator, and
    # [J_F, D_K] = 0 would need re-verification. However, the STRUCTURE of the proof
    # (J_F acts on internal indices, D_K is a geometric operator on K) is universal.
    "[J, D_K(tau)] = 0 CPT exact": {
        "classification": GENERALIZABLE,
        "proof_uses": "J acts on H_F indices. D_K acts on L^2(K, S). For the product triple, "
                      "[J, D_K] = 0 requires D_K to respect the real structure. On SU(3), "
                      "this was verified numerically. The TECHNIQUE (checking J-commutation "
                      "of the Dirac operator) applies to any K, but the RESULT depends on "
                      "the specific Dirac spectrum of K and how it couples to H_F.",
        "K_dependence": "Technique universal. Result needs re-verification for each K. "
                        "Likely holds for any K admitting a bi-invariant metric (J maps "
                        "left-regular to right-regular representation).",
        "session": "S17a"
    },

    # --- Result: g1/g2 = e^{-2*tau} metric ratio ---
    # This is the ratio of gauge couplings derived from the metric on the internal space.
    # For SU(3) with Jensen deformation: lambda_1 = e^{2tau}, lambda_2 = e^{-2tau} (x3),
    # lambda_3 = e^{tau} (x4). The coupling ratio depends on the SPECIFIC parameterization
    # of the deformation family, which is tied to the root system of SU(3).
    # For a general K, the deformation family would be parameterized by rank(K) parameters,
    # and the coupling ratios would depend on the specific Dynkin indices.
    "g1/g2 = e^{-2*tau} metric ratio": {
        "classification": SU3_SPECIFIC,
        "proof_uses": "Jensen 1-parameter deformation of bi-invariant metric on SU(3). "
                      "lambda_1 = e^{2tau}, lambda_2 = e^{-2tau}. The exponential form and "
                      "the specific exponent -2 come from the A_2 root system (simple roots "
                      "at 120 degrees, Cartan matrix entries). For SU(4), the deformation "
                      "family is 2-dimensional (rank 3), with different Dynkin indices.",
        "K_dependence": "Fully SU(3)-specific. The Jensen family uses A_2 Weyl group symmetry. "
                        "For K = SU(4), the deformation space is 2D with A_3 structure.",
        "session": "S17a"
    },

    # --- Result: Block-diagonal theorem ---
    # D_K is exactly block-diagonal in the Peter-Weyl basis for ANY left-invariant metric
    # on K. Proof: Peter-Weyl decomposition is the decomposition of L^2(K) into irreps of
    # K x K (left x right regular representation). The Dirac operator D_K, being left-invariant,
    # commutes with right translations. By Schur's lemma, D_K cannot mix different irreps
    # of the right-regular representation. This gives exact block-diagonality.
    # This proof uses: (1) Peter-Weyl theorem (any compact group), (2) Schur's lemma
    # (any representation), (3) left-invariance of the metric (any left-invariant metric
    # on any compact Lie group). FULLY UNIVERSAL.
    "Block-diagonal theorem": {
        "classification": UNIVERSAL,
        "proof_uses": "Peter-Weyl theorem (any compact group K) + Schur's lemma + "
                      "left-invariance of metric. D_K commutes with right translations, "
                      "hence is block-diagonal in Peter-Weyl sectors. No use of A_2 "
                      "root system, rank, or dimension of K.",
        "K_dependence": "None. Holds for ANY compact Lie group with ANY left-invariant metric.",
        "session": "S22b"
    },

    # --- Result: Trap 1: V(B1,B1) = 0 ---
    # B1 is the gap-edge singlet in the SU(3) Dirac spectrum. V(B1,B1) = 0 because B1
    # transforms as a U(2) singlet (trivial representation of the unbroken U(2) subgroup
    # of SU(3) under Jensen deformation). By the selection rule, the pairing interaction
    # vanishes for U(2)-singlet self-coupling. The proof uses:
    # (1) Jensen deformation breaks SU(3) -> U(1)_7 x U(2) (SU(3)-specific)
    # (2) B1 carries zero weight under all of su(3) (SU(3)-specific: U(2) singlet in
    #     the specific PW sector of SU(3))
    # (3) Schur's lemma for the vanishing (universal technique)
    "Trap 1: V(B1,B1) = 0": {
        "classification": SU3_SPECIFIC,
        "proof_uses": "Jensen deformation of SU(3) breaks SU(3) -> U(1)_7. B1 is the "
                      "gap-edge mode at the bottom of the (1,0) sector. Its U(2)-singlet "
                      "nature under the SPECIFIC SU(3) branching rule gives V(B1,B1)=0. "
                      "The Schur technique is universal, but B1's quantum numbers are "
                      "SU(3)-specific (they depend on the (1,0) representation of SU(3)).",
        "K_dependence": "Fully SU(3)-specific. For SU(4), the analogous mode would be in the "
                        "fundamental (1,0,0) with different branching rules under A_3 -> U(1) x U(3).",
        "session": "S34"
    },

    # --- Result: [iK_7, D_K] = 0 Jensen symmetry ---
    # K_7 is the 7th Gell-Mann matrix (diagonal in the Cartan subalgebra of su(3)).
    # The Jensen deformation is along a SPECIFIC U(1) direction in the Cartan. [iK_7, D_K] = 0
    # means this U(1) is an EXACT symmetry of the deformed Dirac operator. This is because
    # the Jensen deformation preserves the U(1) generated by K_7 (it deforms the metric
    # in the U(1) direction vs the SU(2) x coset directions).
    # For a general K of rank r, a Jensen-type deformation would break K -> T^r (maximal torus),
    # and the analogous result would be [iH_j, D_K] = 0 for each Cartan generator H_j.
    "[iK_7, D_K] = 0 Jensen symmetry": {
        "classification": GENERALIZABLE,
        "proof_uses": "Jensen deformation preserves a maximal torus action. K_7 generates "
                      "the specific U(1) in the Cartan of su(3). For any compact K of rank r, "
                      "a diagonal deformation (scaling root-space directions independently) "
                      "preserves the Cartan torus T^r, giving [iH_j, D_K] = 0 for all r "
                      "Cartan generators.",
        "K_dependence": "Generalizable to any K. The specific generator K_7 is SU(3)-specific, "
                        "but the STRUCTURE (Cartan torus preserved by diagonal deformation) "
                        "is universal. For SU(4), three Cartan generators would commute with D_K.",
        "session": "S34"
    },

    # --- Result: BCS instability 1D theorem ---
    # Any attractive coupling g > 0 in 1D (the single modulus tau) flows to strong coupling.
    # This is the standard Cooper instability theorem: in a degenerate Fermi system, ANY
    # attractive interaction, no matter how weak, produces a bound state (BCS instability).
    # The proof uses: (1) van Hove singularity producing divergent DOS, (2) the BCS gap
    # equation in the presence of divergent DOS. The van Hove singularity is a consequence
    # of the A_2 catastrophe structure of the B2 branch, which is SU(3)-specific in its
    # details but structurally stable. However, ANY compact K will have van Hove singularities
    # in its Dirac spectrum at generic deformation points.
    "BCS instability 1D theorem": {
        "classification": GENERALIZABLE,
        "proof_uses": "Cooper instability theorem: any g > 0 produces BCS pairing when DOS "
                      "diverges. The van Hove singularity is generic for Dirac operators on "
                      "compact manifolds under deformation (Morse theory on the moduli space "
                      "of metrics -> critical points of eigenvalue branches are generic). "
                      "The SPECIFIC location (tau=0.19) and type (A_2 catastrophe) are "
                      "SU(3)-specific, but EXISTENCE of van Hove singularities is universal.",
        "K_dependence": "Existence of BCS instability: UNIVERSAL (any K has van Hove points). "
                        "Location and strength: SU(3)-specific.",
        "session": "S35"
    },

    # --- Result: Cooper pair K_7 charge ---
    # Cooper pairs carry K_7 charge +/- 1/2. This is because the pairing occurs in the B2
    # branch, whose modes carry K_7 charge +/- 1/4, and the pair has total charge +/- 1/2.
    # The specific charge values come from the weight system of SU(3) representations.
    "Cooper pair K_7 charge": {
        "classification": SU3_SPECIFIC,
        "proof_uses": "B2 modes carry K_7 charge +/- 1/4 in the (1,0) representation of SU(3). "
                      "Cooper pairs (B2, B2*) carry total K_7 charge +/- 1/2. The charge values "
                      "are weights of the fundamental representation of SU(3), determined by "
                      "the A_2 root system.",
        "K_dependence": "Fully SU(3)-specific. For SU(4), the analogous charges would be weights "
                        "of the fundamental of A_3, with different numerical values.",
        "session": "S35"
    },

    # --- Result: Spectral action monotonicity ---
    # V_eff = S_b + F_BCS is monotonically decreasing for ALL tau. This is CONNECTION-INDEPENDENT.
    # Proof structure: (1) ALL eigenvalues lambda_k(tau) decrease monotonically (driven by
    # J_C2(tau) which controls the overall bandwidth). (2) Any spectral functional
    # Tr h(D) with h expressible as Laplace transform of positive measure is monotone.
    # Point (1): The monotonic decrease of eigenvalues under Jensen deformation is a
    # property of the SPECIFIC family of metrics on SU(3). On a general K, eigenvalue
    # monotonicity would depend on the deformation family.
    # Point (2): The Laplace-transform argument is UNIVERSAL for any spectral functional.
    "Spectral action monotonicity": {
        "classification": GENERALIZABLE,
        "proof_uses": "Two ingredients: (A) All lambda_k(tau) of D_K on SU(3) decrease "
                      "monotonically under Jensen deformation (CHECKED NUMERICALLY for SU(3), "
                      "driven by J_C2 coupling decay). (B) Any monotone decreasing spectrum "
                      "gives monotone spectral action for any Laplace-representable cutoff "
                      "(UNIVERSAL functional analysis). Part (A) is SU(3)-specific in detail "
                      "but expected for any K: bandwidth decreases under anisotropic deformation "
                      "because off-diagonal Dirac couplings generically decrease.",
        "K_dependence": "Part (B) UNIVERSAL. Part (A) needs verification per K. Expected to hold "
                        "generically but not proven for arbitrary K.",
        "session": "S37"
    },

    # --- Result: Instanton gas / GPV ---
    # The instanton gas description (S_inst = 0.069, dense gas) and the Giant Pair Vibration
    # identification are specific to the BCS physics at the SU(3) van Hove fold.
    # The GPV frequency (omega = 0.792) and coherence (6.3x) depend on the specific
    # Dirac spectrum and pairing interaction on SU(3).
    "Instanton gas / GPV": {
        "classification": GENERALIZABLE,
        "proof_uses": "BCS instanton physics at a van Hove singularity. The instanton action "
                      "S_inst depends on the barrier height and pairing strength, both computed "
                      "from the SU(3) Dirac spectrum. GPV is a general BCS phenomenon "
                      "(pair addition/removal mode) that occurs at ANY van Hove fold with "
                      "BCS pairing. The EXISTENCE of a GPV is universal; the specific "
                      "S_inst = 0.069 and omega = 0.792 are SU(3)-specific numbers.",
        "K_dependence": "EXISTENCE of instanton gas + GPV: universal for any K with van Hove + BCS. "
                        "Specific action and frequency: SU(3)-specific.",
        "session": "S37-38"
    },

    # --- Result: GGE permanence ---
    # Post-transit state is a Generalized Gibbs Ensemble with conserved Richardson-Gaudin
    # integrals. Integrability is protected by the block-diagonal theorem (universal) and
    # the Richardson-Gaudin structure of the BCS Hamiltonian.
    # The Richardson-Gaudin integrability applies to ANY reduced BCS Hamiltonian in the
    # mean-field sector. The block-diagonal theorem ensures sectors decouple (universal).
    # The specific NUMBER of conserved quantities (8) comes from the SU(3) spectrum at
    # the fold, but the STRUCTURE (RG integrability + block-diag -> GGE) is universal.
    "GGE permanence": {
        "classification": GENERALIZABLE,
        "proof_uses": "Richardson-Gaudin integrability of the BCS Hamiltonian (universal for "
                      "any reduced BCS model with uniform coupling) + block-diagonal theorem "
                      "(UNIVERSAL for any compact K, S22b) => post-transit state is GGE. "
                      "The specific conserved quantities depend on the spectrum (SU(3)-specific "
                      "numbers), but the STRUCTURE of integrability-protected non-thermalization "
                      "is universal.",
        "K_dependence": "Structure UNIVERSAL. Number of conserved integrals and GGE details: "
                        "K-specific.",
        "session": "S38"
    },
}

# ============================================================
# 2. CLOSED MECHANISMS (25 closures from CLAUDE.md + additional)
# ============================================================
# Classify a representative sample covering the main closure categories.

closed_mechanisms = {
    # --- Perturbative closures (Sessions 17-20) ---
    "V_tree minimum (S17a)": {
        "classification": GENERALIZABLE,
        "reason": "Spectral action on round metric has no minimum. Proof: eigenvalue monotonicity "
                  "under deformation. Technique universal, eigenvalue curve K-specific."
    },
    "1-loop Coleman-Weinberg (S18)": {
        "classification": GENERALIZABLE,
        "reason": "CW potential inherits constant F/B ratio from Weyl law. Weyl law is universal "
                  "for any compact Riemannian manifold. F/B value is K-specific."
    },
    "Casimir scalar+vector (S19d)": {
        "classification": GENERALIZABLE,
        "reason": "Casimir energy inherits F/B constant-ratio trap. Weyl law universal."
    },
    "Casimir with TT 2-tensors (S20b)": {
        "classification": GENERALIZABLE,
        "reason": "Constant-ratio trap persists with tensor content. Weyl's law."
    },
    "Seeley-DeWitt a2/a4 (S20a)": {
        "classification": GENERALIZABLE,
        "reason": "Heat kernel coefficients a_2, a_4 are UNIVERSAL functionals of curvature. "
                  "The hierarchy a_4 >> a_2 depends on the specific curvature of K."
    },
    "Spectral back-reaction (S19d)": {
        "classification": GENERALIZABLE,
        "reason": "Back-reaction from spectral determinant. Technique universal."
    },

    # --- BCS closures ---
    "Fermion condensate (S19a)": {
        "classification": UNIVERSAL,
        "reason": "Fermion condensate cannot stabilize modulus: wrong sign. General argument."
    },
    "Pfaffian Z_2 (S17c)": {
        "classification": GENERALIZABLE,
        "reason": "Pfaffian invariant from BDI classification. AZ class depends on symmetries of D_K, "
                  "which may change for different K."
    },
    "Single-field slow-roll (S19b)": {
        "classification": UNIVERSAL,
        "reason": "Single-field slow-roll requires epsilon << 1. Spectral action gradient too steep. "
                  "Universal for any K with SA monotonicity."
    },

    # --- Block-diagonal consequences ---
    "Inter-sector coupled delta_T (S22b)": {
        "classification": UNIVERSAL,
        "reason": "Closed by block-diagonal theorem. Universal for any compact K."
    },
    "Inter-sector coupled V_IR (S22b)": {
        "classification": UNIVERSAL,
        "reason": "Closed by block-diagonal theorem. Universal for any compact K."
    },

    # --- Trap closures ---
    "Higgs-sigma portal (S22c Trap 3)": {
        "classification": SU3_SPECIFIC,
        "reason": "e/(a*c) = 1/16 = 1/dim(spinor). The 16 comes from dim(S) on SU(3) (8D manifold, "
                  "spinor dim = 2^4 = 16). For K of dimension d, spinor dim = 2^{d/2}."
    },
    "Rolling quintessence (S22d)": {
        "classification": GENERALIZABLE,
        "reason": "Clock constraint and settling time. The 232 Gyr settling time is SU(3)-specific "
                  "but the STRUCTURE (SA gradient >> Hubble friction) is generic."
    },
    "DESI dynamical DE (S22d)": {
        "classification": GENERALIZABLE,
        "reason": "Requires rolling tau. Closed because SA gradient too steep. Generic structure."
    },

    # --- Chemical potential closures ---
    "Canonical mu!=0 (S34 MU-35a)": {
        "classification": UNIVERSAL,
        "reason": "PH symmetry forces mu=0 analytically. PH is a property of the Dirac spectrum "
                  "(lambda_k = -lambda_k for every eigenvalue), which holds for ANY compact K with "
                  "spin structure (Dirac spectrum is symmetric about zero)."
    },
    "Grand canonical mu!=0 (S34 GC-35a)": {
        "classification": UNIVERSAL,
        "reason": "Helmholtz F convex at mu=0. Follows from PH symmetry. Universal."
    },

    # --- Spectral action route closures (S36-37) ---
    "Cutoff SA stabilization (S37)": {
        "classification": GENERALIZABLE,
        "reason": "Structural monotonicity theorem: any monotone f inherits monotonicity from "
                  "eigenvalue monotonicity. Part is universal (functional analysis), part needs "
                  "eigenvalue monotonicity verification per K."
    },
    "One-loop RPA self-trapping (S37 F.5)": {
        "classification": GENERALIZABLE,
        "reason": "BdG shift has wrong sign (+12.76 vs E_cond -0.137). The sign mismatch is "
                  "STRUCTURAL: spectral action penalizes pairing. Technique universal."
    },
    "(B1,B3,G1) PMNS triad (S37)": {
        "classification": SU3_SPECIFIC,
        "reason": "Uses specific weight structure of SU(3) representations. All (1,0) weights "
                  "have q_7 != 0. SU(3)-specific quantum numbers."
    },

    # --- Session 38 closures ---
    "CC-through-instanton (S38)": {
        "classification": GENERALIZABLE,
        "reason": "Instanton averaging strengthens F.5 anti-trapping. Universal BCS structure."
    },

    # --- Session 45-46 closures ---
    "Weak order-one Bochniak-Sitarz (S45)": {
        "classification": GENERALIZABLE,
        "reason": "GG/Full = 1.000 exact. Violation is maximally gauge. Technique (checking "
                  "[[D,a],b^o] vs reduced condition) universal. The specific violation magnitude "
                  "(4.000 for (H,H)) is SU(3)-specific but the FAILURE is expected generically."
    },
    "Occupied-state spectral action (S45)": {
        "classification": GENERALIZABLE,
        "reason": "S_occ monotone decreasing. Proof: Delta(tau) monotone -> bandwidth increasing -> "
                  "occupation decreasing. The chain uses BCS + spectral monotonicity. Technique universal."
    },
    "Unexpanded spectral action (S45)": {
        "classification": UNIVERSAL,
        "reason": "For FINITE spectrum, S(L) is EXACTLY its Taylor series for L > lambda_max. "
                  "No non-perturbative content. This is PURE functional analysis, independent of K."
    },
    "BdG twist (S46)": {
        "classification": UNIVERSAL,
        "reason": "A_F acts diagonally in Nambu space. ANY sigma in Aut(A_F) leaves diagonal "
                  "embedding invariant. Twisted first-order reduces to untwisted. ALGEBRAIC, no K."
    },
    "Sigma selection (S45)": {
        "classification": GENERALIZABLE,
        "reason": "4 sigma-selection principles tested, none works. Truncated spectrum artifact. "
                  "The truncation issue is universal (any finite PW truncation)."
    },
}

# ============================================================
# 3. STRUCTURAL WALLS
# ============================================================

structural_walls = {
    "Weyl F/B ratio": {
        "classification": UNIVERSAL,
        "proof_uses": "Weyl's law: N(lambda) ~ C * lambda^{d/2} as lambda -> infinity. "
                      "The constant C depends on volume (which is fixed by volume-preservation). "
                      "The F/B ratio in the UV tail is determined by dim(spinor)/dim(boson) "
                      "which depends only on dim(K). Universal for any compact Riemannian manifold.",
        "K_dependence": "The RATIO value changes with dim(K) but the TRAP (constancy of F/B) is universal."
    },
    "Block-diagonality": {
        "classification": UNIVERSAL,
        "proof_uses": "Peter-Weyl + Schur + left-invariance. Universal for any compact Lie group.",
        "K_dependence": "None."
    },
    "Spectral gap (BDI)": {
        "classification": GENERALIZABLE,
        "proof_uses": "BDI classification requires T^2 = +1 with specific Dirac spectrum symmetry. "
                      "The gap opening is verified for SU(3). For other K, the AZ class may differ.",
        "K_dependence": "AZ class depends on symmetries of D_K, which depend on K."
    },
    "SA monotonicity": {
        "classification": GENERALIZABLE,
        "proof_uses": "Eigenvalue monotonicity (K-specific) + Laplace-transform argument (universal). "
                      "The monotonicity wall stands IF eigenvalues of D_K are monotone under "
                      "the chosen deformation family.",
        "K_dependence": "Functional analysis part universal. Eigenvalue behavior needs per-K verification."
    },
    "PH symmetry (mu=0 forced)": {
        "classification": UNIVERSAL,
        "proof_uses": "Dirac spectrum on any compact spin manifold is symmetric about zero. "
                      "PH symmetry is a consequence of spin structure, not specific to SU(3).",
        "K_dependence": "None. Any compact spin manifold has symmetric Dirac spectrum."
    },
    "Gram matrix PSD (no kinetic tachyons)": {
        "classification": UNIVERSAL,
        "proof_uses": "M^2_{ij} = Tr([D,phi_i]^dag [D,phi_j]) is a Gram matrix, hence PSD. "
                      "Holds for ANY Hermitian D and ANY self-adjoint phi. Pure linear algebra.",
        "K_dependence": "None. Purely algebraic."
    },
    "Taylor exactness for finite spectra": {
        "classification": UNIVERSAL,
        "proof_uses": "For a finite set of eigenvalues, Tr f(D^2/L^2) = sum_k d_k f(lam_k^2/L^2) "
                      "is analytic in 1/L^2 for L > lam_max. The Taylor series is EXACTLY the function. "
                      "This is analysis, independent of K.",
        "K_dependence": "None. Applies to any finite spectral truncation."
    },
    "Occupied cyclic cohomology nondegeneracy": {
        "classification": UNIVERSAL,
        "proof_uses": "HC^0(A_F) = C^3, K_0(A_F) = Z^3. Pairing P^occ = diag(w_i)*P^vac "
                      "with w_i > 0. This is a property of A_F = C+H+M_3(C), independent of K.",
        "K_dependence": "None. Property of the finite algebra A_F."
    },
    "BdG twist obstruction": {
        "classification": UNIVERSAL,
        "proof_uses": "A_F acts diagonally in Nambu space H_BdG = H + H*. Algebraic, no K.",
        "K_dependence": "None."
    },
}

# ============================================================
# 4. ADDITIONAL PERMANENT RESULTS (from MEMORY.md)
# ============================================================

additional_permanent = {
    "B2 fold universality (SECT-33a)": {
        "classification": SU3_SPECIFIC,
        "reason": "B2 is a specific branch in SU(3) PW sectors. Fold at tau~0.19 uses SU(3) spectrum."
    },
    "Lie derivative monotonicity (LIE-33a)": {
        "classification": SU3_SPECIFIC,
        "reason": "f(s) = B(s)/5 monotonically increasing. B(s) is defined on the SU(3) deformation."
    },
    "Strutinsky decomposition (STRUT-33a)": {
        "classification": GENERALIZABLE,
        "reason": "Strutinsky method is universal (nuclear physics technique). Specific percentages "
                  "(B2/B3/B1 = 46/37/17%) are SU(3)-specific."
    },
    "Quantum metric identity (S32)": {
        "classification": GENERALIZABLE,
        "reason": "Off-diagonal RPA = Fubini-Study metric. Quantum metric is universal; "
                  "the specific value 4.24 and the B2 identification are SU(3)-specific."
    },
    "J-protection theorem (S32)": {
        "classification": UNIVERSAL,
        "reason": "[J, D+phi+J*phi*J^{-1}]=0 exactly. Algebraic identity from J properties. "
                  "Holds for any spectral triple satisfying the real structure axiom."
    },
    "Omega^1_D tau-independence (S46)": {
        "classification": GENERALIZABLE,
        "reason": "dim(Omega^1_D) computed for A_F on SU(3). The TECHNIQUE (classifying 1-forms) "
                  "is universal. The specific dimension 342 = 173 + 169 is SU(3)-specific."
    },
    "SA scalar instability (S46)": {
        "classification": UNIVERSAL,
        "reason": "delta^2 Tr f(D^2/L^2) < 0 for ALL scalar phi, ALL monotone f. "
                  "Structural: f'(x) < 0 universally. Pure functional analysis."
    },
    "Connes distance isotropy at tau=0 (S46)": {
        "classification": GENERALIZABLE,
        "reason": "Bi-invariant metric gives isotropic Connes distance. Universal for any K "
                  "at the round point. Specific values are K-dependent."
    },
    "Connes distance fold anisotropy (S46)": {
        "classification": SU3_SPECIFIC,
        "reason": "Anisotropy 1.110 at tau=0.19 fold. Entirely SU(3)-specific numbers."
    },
    "(1,1) adjoint Lipschitz softness (S46)": {
        "classification": SU3_SPECIFIC,
        "reason": "lambda_min^{Lip}(1,1) = 1.1134 at fold. SU(3)-specific mode."
    },
    "alpha_s = n_s^2 - 1 (S50)": {
        "classification": SU3_SPECIFIC,
        "reason": "5 proofs within phase sector, all using SU(3) Dirac spectrum."
    },
    "Commutator antisymmetry theorem (S54)": {
        "classification": UNIVERSAL,
        "reason": "[D, diag(f)] antisymmetric for symmetric D. Linear algebra, any K."
    },
    "Connes distance exponential scaling (S54)": {
        "classification": GENERALIZABLE,
        "reason": "d_D(tau) ~ exp(3.651*tau) on lattice. Scaling form generic, exponent K-specific."
    },
    "61/20 ratio theorem (S44)": {
        "classification": GENERALIZABLE,
        "reason": "a_2^{bos}/a_2^{Dirac} = 61/20. Gilkey coefficients on SU(3). The TECHNIQUE "
                  "(Gilkey on Lie groups) is universal; the ratio depends on dim(K) and curvature."
    },
    "CDM by construction (S44)": {
        "classification": UNIVERSAL,
        "reason": "T^{0i} = 0 algebraic for GGE product states. 5 proofs. Universal."
    },
    "K_7 commutant propagation (S51)": {
        "classification": GENERALIZABLE,
        "reason": "[K_7, D_K]=0 => [K_7, p(D_K)]=0. Universal algebra theorem. K_7 is SU(3)-specific."
    },
    "M_3(C) inner fluctuations zero (S51)": {
        "classification": UNIVERSAL,
        "reason": "All M_3(C) generators give ||A_H||_F = 0. Property of A_F, not K."
    },
}

# ============================================================
# 5. COMPILE COUNTS
# ============================================================

def count_classifications(items_dict, key="classification"):
    """Count how many items fall in each classification category."""
    if key == "classification":
        # Direct classification field
        counts = {UNIVERSAL: 0, GENERALIZABLE: 0, SU3_SPECIFIC: 0}
        for name, info in items_dict.items():
            cls = info.get("classification", info.get("classification"))
            counts[cls] = counts.get(cls, 0) + 1
    else:
        counts = {UNIVERSAL: 0, GENERALIZABLE: 0, SU3_SPECIFIC: 0}
        for name, info in items_dict.items():
            cls = info[key]
            counts[cls] = counts.get(cls, 0) + 1
    return counts

# Main permanent results (12 from task spec)
perm_counts = count_classifications(permanent_results)

# Closed mechanisms (25 sample)
closed_counts = count_classifications(closed_mechanisms)

# Structural walls (9)
wall_counts = count_classifications(structural_walls)

# Additional permanent results (17)
add_counts = count_classifications(additional_permanent)

# Combined totals
all_items = {}
all_items.update(permanent_results)
all_items.update(closed_mechanisms)
all_items.update(structural_walls)
all_items.update(additional_permanent)
total_counts = count_classifications(all_items)

total = sum(total_counts.values())
universal_count = total_counts[UNIVERSAL]
generalizable_count = total_counts[GENERALIZABLE]
su3_specific_count = total_counts[SU3_SPECIFIC]

universal_or_generalizable = universal_count + generalizable_count
fraction_universal_or_gen = universal_or_generalizable / total * 100

print("=" * 72)
print("UNIVERSAL-SURVIVE-59: Classification Summary")
print("=" * 72)

print(f"\n--- Major Permanent Results (12 from task spec) ---")
print(f"  UNIVERSAL:      {perm_counts[UNIVERSAL]}")
print(f"  GENERALIZABLE:  {perm_counts[GENERALIZABLE]}")
print(f"  SU(3)-SPECIFIC: {perm_counts[SU3_SPECIFIC]}")

print(f"\n--- Closed Mechanisms (25 sample) ---")
print(f"  UNIVERSAL:      {closed_counts[UNIVERSAL]}")
print(f"  GENERALIZABLE:  {closed_counts[GENERALIZABLE]}")
print(f"  SU(3)-SPECIFIC: {closed_counts[SU3_SPECIFIC]}")

print(f"\n--- Structural Walls (9) ---")
print(f"  UNIVERSAL:      {wall_counts[UNIVERSAL]}")
print(f"  GENERALIZABLE:  {wall_counts[GENERALIZABLE]}")
print(f"  SU(3)-SPECIFIC: {wall_counts[SU3_SPECIFIC]}")

print(f"\n--- Additional Permanent Results (17) ---")
print(f"  UNIVERSAL:      {add_counts[UNIVERSAL]}")
print(f"  GENERALIZABLE:  {add_counts[GENERALIZABLE]}")
print(f"  SU(3)-SPECIFIC: {add_counts[SU3_SPECIFIC]}")

print(f"\n{'=' * 72}")
print(f"COMBINED TOTALS ({total} items)")
print(f"{'=' * 72}")
print(f"  UNIVERSAL:                 {universal_count:3d}  ({universal_count/total*100:.1f}%)")
print(f"  GENERALIZABLE:             {generalizable_count:3d}  ({generalizable_count/total*100:.1f}%)")
print(f"  SU(3)-SPECIFIC:            {su3_specific_count:3d}  ({su3_specific_count/total*100:.1f}%)")
print(f"  UNIVERSAL + GENERALIZABLE: {universal_or_generalizable:3d}  ({fraction_universal_or_gen:.1f}%)")

print(f"\n--- GATE VERDICT ---")
if fraction_universal_or_gen > 80:
    verdict = "PASS"
    print(f"  UNIVERSAL-SURVIVE-59: PASS ({fraction_universal_or_gen:.1f}% > 80% threshold)")
elif fraction_universal_or_gen >= 50:
    verdict = "INFO"
    print(f"  UNIVERSAL-SURVIVE-59: INFO ({fraction_universal_or_gen:.1f}% in [50%, 80%] range)")
else:
    verdict = "FAIL"
    print(f"  UNIVERSAL-SURVIVE-59: FAIL ({fraction_universal_or_gen:.1f}% < 50% threshold)")

print(f"\n--- Cost of Switching to Alternative K ---")

# Count what needs re-derivation
rederive = []
for name, info in all_items.items():
    cls = info.get("classification")
    if cls == SU3_SPECIFIC:
        rederive.append(name)

print(f"  Results requiring FULL re-derivation for K != SU(3): {len(rederive)}")
for r in rederive:
    print(f"    - {r}")

reverify = []
for name, info in all_items.items():
    cls = info.get("classification")
    if cls == GENERALIZABLE:
        reverify.append(name)

print(f"\n  Results requiring re-verification (constants change): {len(reverify)}")
for r in reverify:
    print(f"    - {r}")

print(f"\n  Results surviving UNCHANGED: {universal_count}")

# ============================================================
# 6. SWITCHING COST ANALYSIS
# ============================================================
print(f"\n{'=' * 72}")
print("SWITCHING COST: SU(3) -> SU(4)")
print("=" * 72)
print("  SU(4): rank 3, dim 15, spinor dim 2^{15/2} -- NOT INTEGER (odd dim)")
print("  SU(4) is 15-dimensional. Spinor dimension = 2^{[15/2]} = 2^7 = 128 (real)")
print("  But 15 is odd -> need Spin^c structure, not Spin. KO-dim analysis changes.")
print("  Jensen family: 2-parameter (rank 3, after volume constraint: 2 free params)")
print("  Peter-Weyl: same structure but representations labeled by (p,q,r) not (p,q)")
print("  Block-diagonal theorem: SURVIVES (universal)")
print("  Van Hove: EXISTS (generically) but location and type need full recomputation")
print("  BCS: theorem SURVIVES if van Hove found. Strength needs recomputation")
print("  MINIMAL COST: Recompute Dirac spectrum on SU(4), find van Hove, verify BCS")
print("  ESTIMATED EFFORT: ~5 sessions (spectrum + BCS + mechanism chain)")

print(f"\n{'=' * 72}")
print("SWITCHING COST: SU(3) -> G_2")
print("=" * 72)
print("  G_2: rank 2, dim 14, spinor dim 2^{14/2} = 2^7 = 128")
print("  14-dimensional even -> Spin structure exists. KO-dim: 14 mod 8 = 6 (SAME!)")
print("  Jensen family: 1-parameter (rank 2, after volume constraint: 1 free param)")
print("  Peter-Weyl: labeled by (p,q) like SU(3) but with G_2 Weyl group (dihedral D_6)")
print("  Block-diagonal theorem: SURVIVES")
print("  ADVANTAGE: KO-dim 6 automatic (14 mod 8 = 6). Same finite spectral triple works.")
print("  DISADVANTAGE: SM quantum numbers may not match (G_2 has 2 fundamentals: 7, 14)")
print("  MINIMAL COST: Recompute Dirac spectrum on G_2, verify SM quantum numbers")
print("  ESTIMATED EFFORT: ~3-4 sessions (spectrum + verification)")

# ============================================================
# 7. SAVE DATA
# ============================================================

# Prepare arrays for npz
categories = ["UNIVERSAL", "GENERALIZABLE", "SU(3)-SPECIFIC"]
perm_arr = np.array([perm_counts[c] for c in [UNIVERSAL, GENERALIZABLE, SU3_SPECIFIC]])
closed_arr = np.array([closed_counts[c] for c in [UNIVERSAL, GENERALIZABLE, SU3_SPECIFIC]])
wall_arr = np.array([wall_counts[c] for c in [UNIVERSAL, GENERALIZABLE, SU3_SPECIFIC]])
add_arr = np.array([add_counts[c] for c in [UNIVERSAL, GENERALIZABLE, SU3_SPECIFIC]])
total_arr = np.array([total_counts[c] for c in [UNIVERSAL, GENERALIZABLE, SU3_SPECIFIC]])

np.savez("computations/session-59/s59_universal_survive.npz",
         categories=np.array(categories),
         permanent_counts=perm_arr,
         closed_counts=closed_arr,
         wall_counts=wall_arr,
         additional_counts=add_arr,
         total_counts=total_arr,
         fraction_universal_or_gen=np.array([fraction_universal_or_gen]),
         verdict=np.array([verdict]),
         n_rederive=np.array([len(rederive)]),
         n_reverify=np.array([len(reverify)]),
         n_unchanged=np.array([universal_count]))

print(f"\nData saved to computations/session-59/s59_universal_survive.npz")
print("DONE.")
