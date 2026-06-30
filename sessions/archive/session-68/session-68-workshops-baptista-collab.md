# Baptista Spacetime Analyst -- Collaborative Feedback on S68 Workshops

**Author**: Baptista Spacetime Analyst
**Date**: 2026-04-05
**Re**: S68 Workshop Results (Lizzi x Transit, Landau x Transit, Volovik x Mack)

---

## Section 1: Key Observations

The three S68 workshops converge on a single structural picture: the CMB power spectrum is set entirely at the fold by the spectral action curvature, transported without modification by Weinberg's superhorizon conservation theorem (|T|^2 = 1), and dressed by the BCS condensate's squeezed vacuum initial state. From the KK geometry perspective on M4 x SU(3) with Jensen deformation, I identify four structural observations.

**1.1 The "Three Numbers at the Fold" Reduction (Lizzi E1) Has a Fiber-Geometric Origin**

The Lizzi-Transit workshop's central result -- that n_s, A_s, and alpha_s reduce to properties of S(tau) at the fold -- is a consequence of the Riemannian submersion structure pi: P -> M4 with fiber K = SU(3). The spectral action S(tau) is obtained by fiber integration of the Einstein-Hilbert Lagrangian over K (Paper 13, Sec. 2; Paper 15, Sec. 3). Schematically:

(1) S(tau) = integral_K R(g_K(tau)) * vol(g_K(tau))

where g_K(tau) is the Jensen-deformed metric on SU(3) with deformation parameter tau, and R is the scalar curvature. The "three numbers" -- dS/dtau, d^2S/dtau^2, and S itself at tau_fold = 0.190 -- are fiber-integrated curvature invariants of the internal geometry. The reduction to three numbers is the dimensional reduction: the 36-dimensional space of left-invariant metrics on SU(3) collapses to a 1-parameter family (Jensen line), and the spectral action along this line is a smooth function S(tau) whose first two derivatives at the fold determine the CMB observables.

The structural point: the fold tau = 0.190 is the Jensen parameter at which the isometry group of g_K breaks from (SU(3) x SU(3))/Z_3 (bi-invariant metric, tau = 0) to (SU(3) x SU(2) x U(1))/Z_6 (Jensen metric, tau > 0) (Paper 15, Sec. 4). The spectral action S(tau) encodes this symmetry breaking pattern. At the fold, the curvature d^2S/dtau^2 reflects the Hessian of the scalar curvature functional on the moduli space of Jensen metrics -- this is a Lichnerowicz-type quantity (Papers 28-30). The n_s prediction eps_H = 0.02163 is thus a fiber-geometric invariant: the ratio of squared first derivative to the product of the function value and second derivative of the scalar curvature functional along the Jensen deformation.

**1.2 The a_4/a_2 Ratio Bottleneck Is a Spectral Moment Problem, Not a Functional Choice Problem**

Lizzi's Section L4 establishes that the 16.3% BCS correction to a_4/a_2 is functional-independent (both moments are spectral zeta sums of D_K). From the KK geometry side, a_2 and a_4 are the second and fourth Seeley-DeWitt coefficients of the Dirac operator D_K on Jensen-deformed SU(3):

(2) a_{2k} = sum_n |lambda_n|^{-2k}

where {lambda_n} is the Dirac spectrum (Paper 14, Sec. 3; established computationally in S61 with 155,984 eigenvalues at L_max = 10). The ratio a_4/a_2 measures the spectral shape: how the eigenvalue distribution allocates weight between low and high eigenvalues. The BCS dressing shifts this allocation by boosting high eigenvalues preferentially (UV enhancement), explaining the asymmetry delta(a_4)/a_4 = 29.8% > delta(a_2)/a_2 = 11.6%.

The KK threshold corrections (Paper 22; Paper 24, Sec. 3) enter through the sector decomposition of these spectral moments. On the Jensen line, the Peter-Weyl decomposition of D_K decomposes into irreducible representations V_{(p,q)} of SU(3) (Paper 14, Eq. 3.2):

(3) a_{2k} = sum_{(p,q)} dim(V_{(p,q)}) * a_{2k}^{(p,q)}

where a_{2k}^{(p,q)} is the contribution from sector (p,q). The BCS dressing is NOT uniform across sectors -- the S66 result epsilon = -0.13 non-uniformity (Lizzi L4) means the (p,q)-resolved spectral moments shift differently. This sector non-uniformity is the natural resolution of the alpha_s(M_Z) 15.3-sigma tension: the gauge coupling g_3 couples to the color sector's a_4, not to the full fiber a_4. The sector-resolved BCS correction to the color-sector a_4 may differ substantially from the fiber-averaged 29.8%.

**1.3 Off-Jensen Dynamics Lives in the 36-Dimensional Hessian Landscape**

The A_s gap closure budget (Lizzi-Transit T3, Landau Ld4) identifies off-Jensen dynamics as the primary non-BCS channel (0-0.3 OOM). From my S63-S65 computations, the off-Jensen fiber geometry is characterized by the 36-dimensional Hessian of the scalar curvature functional on the space of left-invariant metrics (S63 HESSIAN-CASIMIR-63: all 36 eigenvectors assigned to Ad(U(2)) irreps). The 10 Hessian eigenvalue clusters decompose under Ad(U(2)) into representations {1, 1, 4, 3, 6, 3, 4, 8, 1, 5}, with the softest mode being the U(1) breathing direction (#30, eigenvalue amplitude -0.71) mixed with C^2-su(2) mixing (#35, amplitude +0.56) (S66 HESSIAN-CUTOFF-66).

The off-Jensen correction to A_s enters through the spectral action evaluated on metrics NEAR the Jensen line:

(4) S(tau, h^a) = S(tau, 0) + (1/2) H_{ab} h^a h^b + ...

where h^a are the 35 off-Jensen deformations (tau itself being the Jensen direction) and H_{ab} is the Hessian. The S64 result (R-saddle: 8 positive + 27 negative eigenvalues at tree level) shows the Jensen line is a SADDLE of the scalar curvature functional. One-loop corrections flip all eigenvalues positive (S62), but the eigenvalue magnitudes determine the Gaussian fluctuation amplitude of off-Jensen modes, which feeds into the multifield delta-N through additional field-space directions.

**1.4 The Kibble-Zurek Resolution (Landau Ld2) Validates the Adiabatic BCS Assumption**

Landau's three-timescale hierarchy -- 1/omega_tach ~ 10^{-3}/M_KK << tau_relax ~ 2/M_KK << dt_transit ~ 663/M_KK -- resolves the D-T2 concern from the Lizzi-Transit workshop. From the fiber geometry perspective, this hierarchy means the internal geometry g_K(tau) evolves SLOWLY compared to the BCS relaxation time on the fiber. The BCS condensate at each tau tracks the ground state of the pairing Hamiltonian on (K, g_K(tau)). The spectrum of D_K(tau) reorganizes at the fold, but the reorganization is adiabatic with respect to the Cooper pair dynamics. The KZ correlation length hat{xi} = 7.7 lattice spacings producing O(3) Josephson vortex defects on CG(24) provides a physical origin for the GGE Leggett modes -- this is a novel connection between fiber geometry and dark matter content.

---

## Section 2: Assessment of Key Findings

**2.1 The phi_eff Squeeze Phase: Geometrically Interpretable**

The BCS squeeze parameter r_k = arctanh(v_k/u_k) (Landau Ld1.9) has a direct fiber-geometric interpretation. The coherence factors u_k, v_k are determined by the eigenvalues of D_K relative to the chemical potential:

(5) v_k^2 = (1/2)(1 - epsilon_k / E_k), where E_k = sqrt(epsilon_k^2 + Delta^2)

The epsilon_k are eigenvalues of D_K on the Jensen-deformed SU(3), computed via Peter-Weyl decomposition (Paper 14). The chemical potential mu sits at the BCS-BEC crossover (mu/E_F = 0.55, S61). The squeeze is thus a SPECTRAL property of D_K(tau_fold): it is determined by the distribution of D_K eigenvalues relative to mu at the fold. No free parameter enters.

The Landau-Transit reconciled squeeze range r_eff = 0.28-0.50 (Transit Re:Ld1, Table) maps to a power spectrum enhancement of 1.16-1.54 (0.065-0.19 OOM). This is geometrically constrained by the finite number of BCS bands (8 at half-filling), producing the hard upper bound 2<N_pair> + 1 = 9 (Landau Ld4.5). The effective squeeze depends on the variance-weighted distribution of eigenvalues relative to the gap edge -- a quantity determinable entirely from the D_K spectrum.

**2.2 The eps_H Cancellation Theorem: Fiber-Geometric Origin**

The eps_H cancellation theorem (Lizzi L3, Eq. 4-5) -- that S(tau) -> (1+f)S(tau) with f constant leaves eps_H invariant -- has a clean fiber-geometric origin. The spectral action S(tau) is a fiber integral (Eq. 1). A tau-independent multiplicative factor (1+f) amounts to a uniform rescaling of the integration measure on K. In the Riemannian submersion formalism (O'Neill), this is equivalent to a conformal rescaling of the fiber metric g_K -> (1+f)^{2/d} g_K at fixed tau, where d = dim(K) = 8. Such a conformal rescaling changes the volume and total curvature but not the ratios of curvature derivatives -- precisely what eps_H measures.

The protection breaks when the rescaling is tau-dependent. In the BCS case, Delta(tau) varies with tau, producing a subleading non-uniform correction. The measured residual delta(eps_H)/eps_H = -1.12% (W1-D) quantifies this breaking. The geometric interpretation: the BCS dressing is approximately a fiber-conformal transformation (uniform spectral weight shift), but the tau-dependence of the gap introduces an anisotropic distortion of the fiber spectrum that breaks conformality at the 1% level.

**2.3 The w_a = 0 Triple Lock and Fiber Geometry**

Volovik's three-fold protection of w_a = 0 (V2: GGE integrability, Josephson lock, frozen texture) has a fiber-geometric underpinning. The frozen texture means tau is frozen at tau_fold = 0.190 post-transit. Since the fiber metric g_K(tau) is determined by tau, the internal geometry is STATIC post-transit. All quantities derived from g_K -- including the BCS spectrum, the GGE occupation numbers, and the Volovik two-fluid partition -- are time-independent. The w_a = 0 prediction is thus a consequence of the post-transit fiber rigidity: g_K(tau_fold) is the permanent internal geometry of the universe, and all dark sector properties inherit its constancy.

---

## Section 3: Collaborative Suggestions

This is my primary contribution. Three specific computations from the KK geometry toolkit address the central open problems identified across the workshops.

**3.1 Sector-Resolved BCS Correction to a_4 (Resolves alpha_s 15.3-sigma Tension)**

The alpha_s(M_Z) tension traces to the BCS correction delta(a_4)/a_4 = 29.8% applied uniformly across all Peter-Weyl sectors. The gauge coupling g_3 couples only to the COLOR sector -- the SU(3)_color factor in (SU(3) x SU(2) x U(1))/Z_6. In the Peter-Weyl decomposition (Eq. 3), the color sector corresponds to specific (p,q) representations that transform nontrivially under the SU(3)_color factor of the isometry group (Paper 15, Sec. 4-5).

The computation: resolve the BCS spectral weight redistribution per Peter-Weyl sector. The D_K spectrum at each (p,q) level is known (S61, 28 irreps at L_eff = 6). The BCS dressing modifies eigenvalues within each sector according to the gap equation with sector-specific pairing matrix elements. The sector-resolved correction delta(a_4^{color})/a_4^{color} may differ significantly from the fiber-averaged 29.8%.

From Paper 22 (KK threshold corrections on warped backgrounds, Sec. 3): the one-loop threshold correction to g_3^{-2} depends on the Dynkin index T(V_{(p,q)}) of each representation in the color sector. The S64 KK-THRESHOLD-64 computation established that the correct formula is T/(8pi^2) per sector (Formula C). The sector-resolved BCS correction enters as a modification of these Dynkin-weighted contributions.

**3.2 Off-Jensen Spectral Action Computation Along Hessian Soft Modes**

The A_s gap requires 0.49-0.61 OOM from non-BCS sources (Landau Ld4). The primary candidate is off-Jensen dynamics: fluctuations of the fiber metric in directions transverse to the Jensen line. The Hessian computation (S63-S66) provides the infrastructure.

The computation: evaluate S(tau, h^a) at the fold for displacements along the 5 softest Hessian directions (the U(1) breathing mode, the C^2-su(2) mixing mode, and the three C^2 coset directions identified in S65 YUKAWA-TEXTURE-65). The off-Jensen spectral action provides additional field-space directions for the multifield delta-N formula:

(6) A_s(off-Jensen) = (H^2/8pi^2) * sum_I (dN/dphi_I)^2 * sigma_I^2

where the sum now includes both the Jensen direction (tau) and the off-Jensen directions (h^a). The off-Jensen variance sigma_a^2 = H^2/(2*m_a^2), where m_a^2 = H_{aa} (Hessian eigenvalue along direction a). The softest mode has lambda_soft = -15.08 at tree level, flipping to positive at one-loop (S62). The one-loop eigenvalue determines the off-Jensen contribution to A_s.

This computation directly uses the 3-parameter Yukawa family from S66 (3-PARAM-YUKAWA-66), which breaks U(2) symmetry and splits the C^2 directions into 2+2. The deformation parameters L3A, L3B of that family are precisely the off-Jensen directions that matter for A_s.

**3.3 Fiber Volume Factor in the Non-BD Enhancement**

The Landau-Transit reconciliation of the non-BD squeeze (r_eff = 0.28-0.50, enhancement 0.065-0.19 OOM) identifies the variance-weighted position of optical-branch modes as the dominant uncertainty. This uncertainty is resolvable by computing the spectral density of D_K eigenvalues near the gap edge at the fold.

The computation: from the Peter-Weyl decomposition of D_K at tau_fold, extract the cumulative spectral density N(lambda) near the gap edge (|lambda| within Delta of the chemical potential). The van Hove singularity at the fold concentrates spectral weight here -- the density of states diverges as (lambda - lambda_fold)^{-1/2} for a fold singularity. The variance weights w_I in Landau's Eq. (Ld1.16) are proportional to (dN/dphi_I)^2 * sigma_I^2, and the latter depends on the spectral density through sigma_I^2 ~ 1/(d^2 E_I/dk^2) (inverse effective mass). Modes at the van Hove singularity have diverging sigma^2 (flat band, zero effective mass), which would enhance the Leggett-branch contribution and increase r_eff toward the upper end of the range.

The D_K spectrum data from S61 (5704 positive eigenvalues at L_eff = 6) contains this information. It requires computing the eigenvalue density near the gap edge and weighting by the tau-derivative of each eigenvalue (the coupling to the deformation parameter).

---

## Section 4: Connections to Framework

**4.1 Fiber Integration as the Bridge Between KK Geometry and Spectral Action**

The spectral action S(tau) = Tr f(D_K^2/Lambda^2) is the fiber-integrated Einstein-Hilbert action in the KK reduction on SU(3) (Paper 13, Sec. 2; Paper 19). Every spectral moment a_{2k} is a fiber-integrated curvature invariant. The "three numbers at the fold" -- S, dS/dtau, d^2S/dtau^2 -- are the zeroth, first, and second derivatives of this fiber integral along the Jensen deformation. The CMB observables are determined by the geometry of the fiber moduli space at a single point (tau_fold), transported to observation by |T|^2 = 1.

This means the entire CMB prediction chain passes through a single geometric object: the scalar curvature functional on the space of left-invariant metrics on SU(3), restricted to the Jensen line, evaluated at the fold. The 0.755 OOM A_s gap is a quantitative discrepancy in the evaluation of this functional, not a structural failure.

**4.2 The S65 Yukawa Theorem Constrains Off-Jensen A_s Corrections**

The S65 PERMANENT THEOREM 2 (C^2 coset degeneracy on Jensen line: all 4 non-Killing directions give identical Yukawa coupling) constrains the off-Jensen corrections available for A_s. On the Jensen line, the 4 C^2 directions are degenerate and contribute identically to the multifield delta-N. Breaking this degeneracy requires moving off the Jensen line into the 3-parameter family (S66), which splits C^2 -> 2+2. The maximum Yukawa hierarchy achievable is 21.5 at L3A/L3B = 10 (S66 3-PARAM-YUKAWA-66), corresponding to a substantial breaking of the C^2 degeneracy.

This degeneracy breaking has direct consequences for A_s: the 2+2 splitting gives two pairs of off-Jensen directions with different effective masses, and the lighter pair contributes more to the multifield variance. The S65 theorem guarantees that ON the Jensen line, the off-Jensen contribution to A_s is 4-fold degenerate (single effective mass for all C^2 directions). Moving off-Jensen lifts this degeneracy and generically INCREASES the total multifield variance.

**4.3 KK Threshold Corrections Are the Rate-Limiting Computation for m_H**

The m_H worsening from 127.5 to 137.4 GeV under BCS dressing (Lizzi L4) traces to the a_4/a_2 shift. The KK threshold corrections (S62-S64) provide a known counter-term. The S63 result delta(1/g_3^2) = 2.353 (Gaussian-cutoff, L = 6) represents a correction to the UV boundary condition of the gauge coupling. The same threshold mechanism applies to the Higgs quartic coupling lambda(M_KK), which is proportional to a_4/(a_2^2 * f_0) in the Chamseddine-Connes-Marcolli route (Lizzi Eq. 6). The KK threshold correction to lambda(M_KK) has not been computed but is accessible with the existing Peter-Weyl infrastructure. The sector-resolved computation (Suggestion 3.1) provides both the alpha_s correction and the m_H correction from a single computation.

---

## Section 5: Open Questions

**OQ-1: Does the Sector-Resolved BCS Correction Reduce or Amplify the a_4 Shift?**

The fiber-averaged BCS correction delta(a_4)/a_4 = 29.8% is the mean over all (p,q) sectors weighted by dim(V_{(p,q)}). If the color sector sits near the gap edge (where the BCS correction is maximal), the sector-resolved correction could EXCEED 29.8%, worsening the alpha_s tension. If the color sector sits far from the gap edge, the correction is reduced. The answer depends on the spectral placement of color-sector eigenvalues relative to the chemical potential -- a computable quantity from the D_K spectrum.

**OQ-2: How Does the Off-Jensen Hessian Eigenvalue Spectrum Change Under BCS Dressing?**

The S63 Hessian computation used the bare (undressed) D_K spectrum. The BCS dressing shifts eigenvalues by O(10-30%), which will modify the Hessian eigenvalues. The one-loop stabilization (all 36 eigenvalues flip positive, S62) depends on the relative magnitudes of tree-level and one-loop contributions. If BCS dressing shifts the tree-level Hessian by 30%, the one-loop stabilization margin (H_1loop/|H_tree| ~ 3.5) could change significantly. The Lambda_crit = 5.033 M_KK (S66) may shift under BCS dressing.

**OQ-3: What Determines the Off-Jensen Transit Trajectory?**

The transit follows the spectral action gradient dS/dtau in the Jensen direction. But the full gradient nabla S in the 36-dimensional moduli space has components in off-Jensen directions. If these off-Jensen gradient components are nonzero at the fold, the physical transit trajectory deviates from the Jensen line, sampling off-Jensen metrics during the transit. The transit-scale A_s depends on the actual trajectory, not just the Jensen-line value. The off-Jensen gradient at the fold has not been computed; it requires evaluating dS/dh^a at (tau_fold, h^a = 0).

**OQ-4: Can the Normalization Mismatch (Transit Re:Ld4, Factor 12.9) Be a Convention Issue?**

The Transit agent identifies a factor 12.9 discrepancy between the direct amplitude chain and the delta-N chain (Re:Ld4). This discrepancy is 1.11 OOM -- larger than the current A_s gap (0.755 OOM). If the direct chain is correct, the framework may OVERPREDICT A_s. This normalization must be resolved before the gap closure budget is meaningful.

**OQ-5: Does the Volovik CC Tracking Relation Depend on the Fiber Geometry?**

Mack's Q-M3 asks whether epsilon(q) in the Gibbs-Duhem subtraction (Volovik V1.1) depends on the spectral action a_0 coefficient. From the KK perspective, a_0 = 6440 is the topological mode count of D_K (tau-independent, S66). The vacuum energy density epsilon(q) in the substrate picture is the spectral action S(tau) evaluated at the post-transit vacuum. The Gibbs-Duhem subtraction removes the extensive part, leaving a correction proportional to H^2 (Paper 25, Sec. V). The fiber geometry enters through S(tau_fold) and a_2(tau_fold), both of which are fixed post-transit. The tracking relation rho_vac ~ H^2 is thus fiber-geometry-dependent in its normalization (through S and a_2) but structurally robust (the tracking mechanism is topological, depending on the positive compressibility chi > 0, which is guaranteed by the Hessian structure).

---

## Section 6: Computation Suggestions Summary

| # | Computation | Input Data | Output | Pre-Registered Gate | Priority |
|:--|:-----------|:-----------|:-------|:-------------------|:---------|
| B1 | Sector-resolved BCS correction to a_4^{color} | D_K spectrum (S61), BCS gap Delta = 0.52, PW sectors at L=6 | delta(a_4^{color})/a_4^{color}, revised alpha_s(M_Z) | alpha_s(M_Z) in [0.110, 0.126] (2-sigma Planck) | HIGH |
| B2 | Off-Jensen spectral action along 5 softest Hessian modes | S63 Hessian eigenvectors, S(tau) at fold, 3-param family | sigma_a^2 per off-Jensen direction, delta(A_s) from multifield | Combined BCS + off-Jensen closes >= 0.5 OOM of 0.755 gap | HIGH |
| B3 | Van Hove spectral density near gap edge | D_K eigenvalues at tau_fold (S61 data), BCS coherence factors | Variance weights w_I for Leggett/optical branches, r_eff | r_eff in [0.28, 0.50] (Landau-Transit reconciled range) | MEDIUM |
| B4 | KK threshold correction to Higgs quartic lambda(M_KK) | PW Dynkin indices (S64), sector-resolved a_4, f_0 | m_H(corrected), comparison with 125.1 GeV | m_H in [120, 135] GeV | MEDIUM |
| B5 | Off-Jensen gradient nabla_a S at the fold | S(tau, h^a) numerical evaluation, Hessian infrastructure | Off-Jensen gradient components, transit trajectory deviation | nabla_a S / nabla_tau S < 0.1 (Jensen line is the actual trajectory) | LOW |
| B6 | BCS-dressed Hessian eigenvalue spectrum | BCS-corrected D_K spectrum, Hessian recomputation | Revised 36 eigenvalues, Lambda_crit(BCS), stabilization margin | All 36 eigenvalues remain positive at Lambda = 2.048 M_KK | LOW |

---

## Closing Assessment

The three S68 workshops establish a clear structural picture from the fiber geometry perspective. The CMB observables are fiber-integrated curvature invariants of Jensen-deformed SU(3), frozen at the fold and transported without modification to observation. The BCS condensate on the fiber provides a squeezed vacuum initial state (non-BD enhancement 0.07-0.19 OOM) and mean-field dressing (+0.046 OOM), both determined by the D_K spectrum with no free parameters. The combined BCS contribution (0.15-0.27 OOM) closes at most 36% of the A_s gap. The remainder must come from off-Jensen fiber geometry -- fluctuations in the 35 directions transverse to the Jensen line in the 36-dimensional moduli space of left-invariant metrics on SU(3).

The a_4/a_2 ratio bottleneck (Lizzi L4) and the alpha_s tension (15.3 sigma) are the most consequential open problems from the KK geometry perspective. Both trace to the sector structure of the Peter-Weyl decomposition and the non-uniform BCS dressing across (p,q) sectors. The sector-resolved computation (B1) is the highest-priority computation I can contribute, because it addresses both tensions from a single fiber-geometric calculation.

The Volovik w_a = 0 prediction is structurally grounded in the post-transit rigidity of the fiber metric g_K(tau_fold). The DESI DR3 test is the framework's most decisive near-term confrontation, and the sensitivity analysis (dw_0/dGamma ~ 14, Volovik R2) identifies the Meissner fraction as the dominant systematic. From the fiber geometry side, the Meissner fraction is determined by the superfluid density D_s(GGE), which is computed from the BCS Hamiltonian on the Jensen-deformed fiber. The 992-mode computation would provide the definitive value.

The workshops collectively demonstrate that the A_s gap is a PRECISION problem in fiber geometry, not a structural failure. The gap decomposes cleanly into three sectors: BCS condensate (bounded at 0.27 OOM), off-Jensen geometry (estimated 0-0.3 OOM), and a possible normalization convention (the unresolved factor 12.9 from W1-A). The rate-limiting computation is B2 (off-Jensen spectral action), which requires evaluating S(tau, h^a) at the fold -- a computation within reach of the existing Hessian infrastructure from S63-S66.

---

## Wrap-Up

### What Changed

- **The A_s gap decomposed into a precision budget.** Before S68, the 0.755 OOM shortfall was a monolithic deficit. The three workshops dissected it into BCS condensate (0.15-0.27 OOM, bounded), off-Jensen fiber geometry (0-0.3 OOM, computable), and a normalization ambiguity (the factor 12.9 from W1-A, unresolved). The gap is no longer a single unknown -- it is three independent contributions, each addressable by a distinct computation on the D_K spectrum.
- **The a_4/a_2 ratio bottleneck replaced the CC problem as the sharpest tension.** The Lizzi-Transit workshop established that the BCS-dressed m_H worsens from 127.5 to 137.4 GeV through a 29.8% shift in a_4. Combined with the alpha_s 15.3-sigma tension, the sector structure of the Peter-Weyl decomposition under BCS dressing is now the central open problem in the KK geometry program -- surpassing the cosmological constant (structurally closed at a_0/a_2 = 6/R, S65) in urgency.
- **Off-Jensen dynamics entered the quantitative picture.** The Hessian infrastructure from S63-S66 was previously a structural result (eigenvalue clusters assigned to Ad(U(2)) irreps). The workshops connected it to a specific observable: off-Jensen fluctuations contribute to A_s through the multifield delta-N formula, with the 5 softest Hessian modes setting the scale.

### What Holds

- **The eps_H cancellation theorem is structurally exact.** The BCS dressing is approximately fiber-conformal (uniform spectral weight shift), breaking conformality only through the tau-dependence of Delta. The measured 1.12% residual (W1-D) is a quantitative correction, not a structural threat. The n_s = 0.9567 prediction survives BCS dressing with sub-percent modification.
- **The post-transit fiber rigidity protects w_a = 0.** The Jensen parameter tau freezes at tau_fold = 0.190 after the transit. The fiber metric g_K(tau_fold) is static, and all dark sector quantities (GGE occupation numbers, Volovik two-fluid partition, BCS spectrum) inherit this constancy. Volovik's triple lock (GGE integrability, Josephson lock, frozen texture) is grounded in the geometry of the internal space.
- **The "three numbers at the fold" reduction to fiber-integrated curvature invariants.** S, dS/dtau, d^2S/dtau^2 at tau_fold are the complete input for CMB observables. This is a consequence of the Riemannian submersion structure and |T|^2 = 1 superhorizon conservation. No workshop finding challenged this chain.

### What Breaks or Strains

- **The factor 12.9 normalization mismatch (W1-A, Transit Re:Ld4) is unresolved and potentially load-bearing.** At 1.11 OOM, this discrepancy exceeds the A_s gap itself. If the direct amplitude chain is correct, the framework may overshoot A_s rather than undershoot it. The entire gap closure budget is meaningless until this normalization is resolved. This is not a convention choice -- it is a factor that must be tracked through the fiber integration measure and the delta-N prefactor.
- **The BCS-dressed m_H worsening (127.5 to 137.4 GeV) moves in the wrong direction.** The bare KK threshold prediction (S63-S66) was already 5.4% above the observed 125.1 GeV. The BCS dressing adds another 7.8%, opening the total discrepancy to 9.8%. The sector-resolved KK threshold correction (B1) and the Higgs quartic correction (B4) must compensate, but neither has been computed. If the sector-resolved corrections also worsen m_H, the Higgs mass becomes a genuine tension.
- **The one-loop stabilization margin under BCS dressing is untested.** The S62 result (all 36 Hessian eigenvalues flip positive at one-loop, margin H_1loop/|H_tree| = 3.5) used the bare D_K spectrum. A 30% BCS shift to the tree-level Hessian could reduce this margin to O(1). The physical cutoff Lambda = 2.048 M_KK sits 2.5x below Lambda_crit = 5.033 M_KK (S66), but both numbers may shift. If any eigenvalue goes negative under BCS dressing, the Jensen fold ceases to be a minimum of S_eff, and the transit dynamics must be reconsidered.

### Carry-Forward Computations

1. **B1: Sector-resolved BCS correction to a_4^{color}.** Needs: D_K spectrum (S61, 5704 eigenvalues), BCS gap Delta = 0.52, Peter-Weyl sector decomposition at L = 6 (28 irreps). Feeds: alpha_s(M_Z) gate [0.110, 0.126] and m_H gate [120, 135] GeV. Estimated effort: 1 computation script, medium complexity (sector labeling infrastructure exists from S64).

2. **B2: Off-Jensen spectral action along 5 softest Hessian modes.** Needs: S63 Hessian eigenvectors, spectral action S(tau) at the fold, 3-parameter family from S66. Feeds: A_s gap closure gate (combined BCS + off-Jensen closes >= 0.5 OOM of 0.755 gap). Estimated effort: 1 computation script, high complexity (requires numerical evaluation of S(tau, h^a) at fold in 5 directions).

3. **B3: Van Hove spectral density near the BCS gap edge.** Needs: D_K eigenvalues at tau_fold (S61 data), BCS coherence factors u_k, v_k. Feeds: squeeze parameter r_eff gate [0.28, 0.50] (Landau-Transit reconciled range). Estimated effort: 1 computation script, low complexity (spectral density extraction from existing eigenvalue data).

4. **B4: KK threshold correction to Higgs quartic lambda(M_KK).** Needs: Peter-Weyl Dynkin indices (S64), sector-resolved a_4 from B1, spectral action coefficient f_0. Feeds: m_H gate [120, 135] GeV. Estimated effort: 1 computation script, medium complexity (depends on B1 output).

5. **B5: Off-Jensen gradient nabla_a S at the fold.** Needs: S(tau, h^a) numerical evaluation (same infrastructure as B2), Hessian eigenvectors. Feeds: transit trajectory gate (nabla_a S / nabla_tau S < 0.1, confirming Jensen line is the physical trajectory). Estimated effort: low marginal effort if B2 is completed first (gradient is a byproduct of the same evaluation).

6. **B6: BCS-dressed Hessian eigenvalue spectrum.** Needs: BCS-corrected D_K spectrum, full Hessian recomputation (36x36 matrix). Feeds: stabilization gate (all 36 eigenvalues positive at Lambda = 2.048 M_KK under BCS dressing). Estimated effort: 1 computation script, high complexity (full Hessian recomputation with modified spectrum).

### Closing Line

The sector-resolved Peter-Weyl decomposition under BCS dressing (B1) is the single computation that simultaneously addresses the two sharpest tensions -- alpha_s at 15.3 sigma and m_H worsening to 137.4 GeV -- and its answer determines whether the KK threshold program converges to observation or exposes a structural mismatch between the fiber geometry and the Standard Model.
