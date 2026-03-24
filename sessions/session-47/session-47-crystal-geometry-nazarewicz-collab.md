# Nazarewicz -- Collaborative Feedback on Session 47 Crystal Geometry

**Author**: Nazarewicz (Nuclear Structure Theorist)
**Date**: 2026-03-16
**Re**: Session 47 Wave 2 Crystal Geometry Synthesis (Tesla)

---

## Section 1: Key Observations

### 1.1 The Condensate at the Identity: Pairing Field in the Zero-Deformation Limit

The 3.14 x 10^6 contrast ratio of the condensate on T^2 is, from my nuclear perspective, the defining result of Session 47. It demands careful interpretation.

In deformed nuclei, the pairing field Delta(r) is a function of position inside the nucleus. For well-deformed systems (beta_2 ~ 0.3-0.4), the pairing field is roughly uniform in the nuclear interior and falls off at the surface with the density (Paper 02, Sec. 3; Paper 03, density-dependent pairing Delta(r) = -G_0[1 - eta*rho(r)]*kappa(r)). The ratio of maximum to minimum pairing field inside a nucleus is typically 2-5x, not 10^6. Even in halo nuclei at the drip line, where pair amplitudes extend to 8-10 fm (Paper 02, key result), the contrast between interior and exterior pairing is at most 10^2-10^3.

A contrast of 3.14 x 10^6 is not a BCS phenomenon. It is a character-theoretic phenomenon. The condensate peaks at the identity because chi_{(p,q)}(e) = dim(p,q) for every representation -- pure constructive interference. The BCS weighting (sector-averaged gaps times Gaussian suppression of higher representations) modulates this, but the identity peak is fundamentally kinematic. Tesla correctly identifies this: "The condensate structure is set by character interference, not by curvature. It is a harmonic phenomenon, not a geometric one."

This distinction matters. In nuclear BCS, the pairing field is determined self-consistently by the gap equation -- the density determines the potential, the potential determines the wave functions, the wave functions determine the density and the pairing tensor. Here, the "condensate density" on T^2 is NOT a self-consistent solution of the HFB equations on SU(3). It is a post-hoc construction: BCS gaps computed in the (0,0) Peter-Weyl sector are used as weights for a Weyl character expansion on the torus. The self-consistency loop does not close through the spatial profile.

**Assessment**: The 3.14 x 10^6 contrast is a correct mathematical result about the character expansion weighted by BCS gaps. It is NOT evidence that the BCS condensate is spatially non-uniform on SU(3) in the sense that a nuclear pairing field is non-uniform in the nucleus. Calling it a "condensate density" is misleading without the caveat that it lacks self-consistency. The 0D limit (L/xi_GL = 0.031) actually argues AGAINST spatial structure: when the coherence length is 32x the system size, the condensate is uniform by definition in the BCS sense. The character interference pattern is a mathematical fact about Fourier analysis on SU(3), not a statement about where Cooper pairs "live."

### 1.2 The Six-Branch Curvature Hierarchy: Nuclear Shell Structure Analog

The curvature branch structure is the most physically robust result in the synthesis. Six branches with definite degeneracies (3 + 12 + 4 + 2 + 4 + 3 = 28) and two protected invariants (K(u(1), su(2)) = 0, K(u(1), C^2) = 1/16) -- this is structural geometry, independent of any BCS physics.

In nuclear physics, the direct analog is the Nilsson diagram (Paper 07). When an axially symmetric nucleus is deformed, the 2j+1 degeneracy of each spherical shell splits into Nilsson levels labeled by the quantum number Omega (projection of j on the symmetry axis). At zero deformation, levels cluster at the spherical magic gaps. Under deformation, they fan out, cross, and reorganize. The key features:

1. **Some quantum numbers are protected.** Parity pi and Omega are exact quantum numbers of the axially symmetric deformed Hamiltonian, just as u(1)-su(2) flatness and u(1)-C^2 curvature are exact invariants of the Jensen metric. In the Nilsson diagram, levels with the same (Omega, pi) cannot cross (Wigner non-crossing). Here, the protected curvatures cannot flow.

2. **The deformation creates soft and hard directions.** In nuclei, prolate deformation softens the equatorial modes and stiffens the polar modes. The Jensen deformation softens su(2)-C^2 cross-planes (K goes from 0.021 to 0.010, factor 2.1 reduction) and stiffens su(2)-su(2) (0.083 to 0.122, factor 1.46 increase). This is the same physics: the deformation has a symmetry-breaking direction, and it selectively stiffens/softens depending on alignment with that direction.

3. **Level density matters for pairing.** In the Nilsson diagram, pairing is strongest at mid-shell, where the level density near the Fermi surface is highest (Paper 03, Sec. 2: "gap maximal at mid-shell, filling fraction f ~ 0.5"). The soft su(2)-C^2 branches, with 12 planes and the weakest curvature, provide the analog of a high level density near the Fermi surface. B2 states live in this soft region and dominate pairing.

### 1.3 The Soft-Pairing Anti-Correlation

Tesla observes that softer curvature branches host stronger pairing (B2 on su(2)-C^2, K = 0.010, V = 0.256) while harder branches host weaker pairing (B3 on su(2)-su(2), K = 0.122, V = 0.003). The curvature ratio is 12.5:1, the pairing ratio is 85:1.

This is not surprising from nuclear physics. It is, in fact, the standard mechanism. In the Nilsson diagram:

- High-j intruder orbitals (which cross large shell gaps) sit in regions of low level density. Their pairing contribution is weak because they are isolated (Paper 08: high-j alignment breaks pairs by reducing degeneracy near the Fermi surface).
- Normal-parity orbitals in mid-shell regions sit in dense clusters. Their pairing is strong because many states contribute to the gap equation within the pairing window.

The soft curvature branches are the analog of the dense mid-shell regions. The hard branches are the analog of the isolated intruder orbitals. The anti-correlation is built into the HFB formalism: the BCS gap equation Delta_k = -(1/2) sum_{k'} V_{kk'} Delta_{k'}/E_{k'} is a sum over states near the Fermi surface, weighted by 1/E_{k'}. When the density of states is high (soft, many levels), the sum has more terms and Delta is larger. When the density is low (hard, few levels), the sum is smaller and Delta is weaker.

The non-proportionality (12.5:1 in curvature vs 85:1 in pairing) is also expected. The BCS gap depends exponentially on the density of states through the BCS formula Delta ~ omega_D exp(-1/g*N(E_F)) (Paper 14, Sec. 4). A factor 12.5 difference in "spring constant" translates to a much larger ratio in Delta through the exponential. The factor 85 is entirely consistent with BCS non-linearity amplifying a factor 12.5 geometric input.

### 1.4 The 0D Limit and Nuclear Benchmarks

L/xi_GL = 0.031 means the coherence length exceeds the system size by 32x. In nuclear physics, this regime corresponds to ultrasmall metallic grains studied by Anderson in 1959 -- systems where the single-particle level spacing delta exceeds the BCS gap Delta, and BCS theory breaks down. Our analog is confirmed by S46: the system has N_pair = 1 exactly (single Cooper pair), and BCS overestimates gaps by 60% relative to exact diagonalization (S46 NUMBER-PROJECTED-BCS-46, PBCS/BCS = 0.63-0.64).

Paper 03, Section IV warns explicitly about this regime: "For very small systems, particle-number fluctuations become large and BCS breaks down -- exact diagonalization or variation-after-projection is needed." The S46 results confirmed this to quantitative precision (PBCS matches ED to 0.1%).

The 0D limit is therefore the defining physical condition of this system. Any spatial analysis of the condensate (contrast ratios, shell structures, 1/e^2 radii) is a mathematical exercise on character expansions, not a physical property of the BCS state. In the 0D limit, the condensate IS the system. There is no "where" -- only "how much."

---

## Section 2: Assessment of Key Findings

### 2.1 The Protected Chain q_7^2 = K(u(1), C^2) = 1/16

This is representation-theoretic tautology dressed as discovery. Let me be precise:

- q_7 = +/- 1/4 is the eigenvalue of the u(1) generator lambda_8 in the spinor representation, normalized as Tr(lambda_a lambda_b) = 2 delta_{ab}. This normalization fixes q_7 = 1/4 for the fundamental.
- K(u(1), C^2) = 1/16 is the sectional curvature of the bi-invariant metric on SU(3), computed from |[lambda_8, lambda_a]|^2 / (4 |lambda_8|^2 |lambda_a|^2) for a in C^2. The structure constants f_{8,a,b} determine this.
- Both quantities derive from the same Lie algebra structure constants.

The equality q_7^2 = K(u(1), C^2) = 1/16 is therefore an algebraic identity, not a dynamical coincidence. The fact that it is protected under Jensen deformation follows from the u(1) generator commuting with the u(2) subalgebra -- a permanent structural feature.

**Verdict**: STRUCTURAL RESULT. The chain is real, exact, and permanent. It IS representation theory, and it IS deep in the sense that it connects the pairing sector (B2, labeled by q_7) to a geometric invariant (K = 1/16). But it is not an emergent resonance. It is an input.

Tesla's observation that "Cooper pairs carry the charge that IS the protected curvature" is the correct physical statement. The deeper question is: why does BCS select B2 rather than B3 or a mixture? The answer from S34 (Trap 1, Schur's lemma) and S46 (V_B3B3 gate) is algebraic, not geometric. The protected chain provides a label for the selected sector, not the selection mechanism.

### 2.2 Soft-Pairing Anti-Correlation

**Verdict**: ROBUST OBSERVATION consistent with standard nuclear BCS physics. Not yet a theorem. The proposed test (compute V(B2,B2)(tau) and K_soft(tau) across [0, 0.50] and check opposite-sign derivatives) is well-designed and should be carried forward.

From a Landau theory perspective (my Paper 09 instability condition d^2E/d(beta_3)^2 < 0): the soft-pairing anti-correlation is the statement that the instability criterion for BCS condensation is met more easily in soft geometric directions. The BCS instability condition is g*N(E_F) > 0 (any attractive coupling in 1D, from S35 RG-BCS theorem). But the STRENGTH of the instability -- the gap magnitude -- depends on N(E_F), which is higher in the soft sector. This is well-established nuclear physics, not a new prediction.

### 2.3 The Haar-Condensate Shell and He-3B Analog

**Verdict**: VALID MATHEMATICAL OBSERVATION, QUESTIONABLE PHYSICAL ANALOG.

The shell at r = 0.85 rad is a mathematical consequence of multiplying a peaked function (|Delta|^2 on T^2) by a function that vanishes at the peak (Haar measure). The product necessarily peaks at some intermediate radius. This is not physics -- it is measure theory.

The He-3B analog is strained. In He-3B, the order parameter Delta_{ai} is a 3x3 complex matrix (spin x orbital indices), and the B-phase corresponds to Delta_{ai} = Delta_0 delta_{ai} e^{i phi}. The spatial profile of the gap in a vortex core is a genuine self-consistent solution of the Ginzburg-Landau equations, where the coherence length xi ~ 10-100 nm determines the vortex core size. The "shell" in a vortex is a consequence of the order parameter being forced to zero at the core by topology (winding number), not by measure theory.

Here, the "shell" arises because the Haar measure vanishes at the identity. This is an artifact of working on a group manifold with a non-uniform measure, not a dynamical effect analogous to vortex physics. The physical condensate in the 0D limit is uniform -- the character expansion is a spectroscopic decomposition, not a position-space profile.

### 2.4 The B2 Funnel (50% -> 62% -> 91%)

**Verdict**: THE STRONGEST STRUCTURAL RESULT in the synthesis. Three independent measures all select the same sector, with monotonically increasing concentration. This is analogous to the nuclear phenomenon where a single partial wave (e.g., l = 0, s-wave) dominates pairing despite many partial waves being available. In medium-mass nuclei (A ~ 100-150), s-wave pairing carries >80% of the total pairing correlation, even though d-wave and g-wave channels are open.

The B2 funnel ratio 91/50 = 1.82 is the analog of the s-wave enhancement factor in nuclear pairing. The physical mechanism is identical: the interaction matrix element V is largest in the channel with the highest density of states near the Fermi surface.

### 2.5 The 1/4 Coincidence (Resonance 5.5)

**Verdict**: Tesla correctly calls this "almost certainly a coincidence" and proposes a definitive test (convergence of 1/e^2 radius at higher max_pq_sum). This is exactly the right attitude. Record the observation, pre-register the test, compute, and report. No premature interpretation.

---

## Section 3: Collaborative Suggestions

### 3.1 Self-Consistent Pairing Field on SU(3) (PRIORITY 1)

The missing computation in this entire synthesis is a self-consistent solution of the gap equation with the spatial profile on SU(3) included. Currently:

- BCS gaps are computed in the (0,0) sector only (8 modes)
- The "condensate on T^2" is a post-hoc character expansion using these gaps as weights
- The self-consistency loop (density -> potential -> wave functions -> density) does not close through the spatial degrees of freedom

**Proposed computation**: Solve the HFB gap equation in the Peter-Weyl basis, allowing Delta_{(p,q)} to be sector-dependent (not just sector-averaged). The gap equation becomes:

    Delta_{(p,q),s} = -sum_{(p',q'),s'} V_{(p,q)s; (p',q')s'} * Delta_{(p',q'),s'} / (2 E_{(p',q'),s'})

where s indexes the spinor sector (B1, B2, B3) and the sum runs over all Peter-Weyl sectors up to the truncation. This is the analog of solving HFB with a finite-range pairing interaction (Paper 02, Gogny type) rather than a contact interaction. The character expansion in W2-1 implicitly assumes that the gap in each sector is determined only by the (0,0) sector BCS solution -- this is the analog of a local-density approximation (LDA), which overestimates pairing in regions of high level density and underestimates it in sparse regions.

**Expected outcome**: The sector-resolved gaps will differ from the (0,0)-sector values. Specifically, higher-representation contributions will partially screen the (0,0) pairing, reducing V(B2,B2) from 0.256 and potentially modifying the contrast ratio by 1-2 orders of magnitude. This is the analog of using a finite-range Gogny pairing force instead of a zero-range contact force -- the finite range reduces the gap from the contact value by 20-40% (Paper 02, comparison of interactions).

**Format**: Python script using existing infrastructure in `tier1_dirac_spectrum.py`. Input: V matrix elements from `s39_integrability_check.npz`. Output: sector-resolved gaps and self-consistency check.

### 3.2 Curvature-Gap Correlation Function (PRIORITY 2)

The soft-pairing anti-correlation is the most physically motivated result in the synthesis. To promote it from observation to structural result:

**Proposed computation**: For each tau in [0, 0.50] at 26 points, compute simultaneously:
1. The average sectional curvature K_s(tau) for each sector s = B1, B2, B3 (using the branch assignment from the curvature anatomy)
2. The BCS gap Delta_s(tau) for each sector
3. The correlation coefficient r(tau) = corr(K_s, Delta_s) across the three sectors

If r(tau) < -0.9 at all tau, the anti-correlation is structural. If it degrades or reverses, it is an accident of the fold. This is the analog of computing the pairing gap as a function of deformation beta_2 in a Nilsson model (Paper 07 + Paper 08) and checking whether mid-shell deformed nuclei always have larger gaps than magic spherical nuclei.

### 3.3 Collective Pair Rotation on the Curvature Landscape (PRIORITY 3)

The six curvature branches define a potential energy landscape for collective pair motion. In nuclear physics, the analog is the potential energy surface E(beta_2, beta_3) on which collective modes (quadrupole vibrations, octupole vibrations) propagate (Paper 09, Paper 10, Paper 13).

**Proposed computation**: The S46 GPV-FRAGMENTATION-46 result showed that pair vibrational strength is concentrated in a single mode (91.3% in B2). This giant pair vibration propagates on the curvature landscape. The question is: does the curvature anisotropy (12.5:1) create preferential directions for pair-mode propagation?

Concretely: compute the pair-vibration coupling matrix M_{ab} = sum_{(p,q)} chi_{(p,q)}(theta_a) * V_{(p,q)} * chi_{(p,q)}(theta_b) for theta_a, theta_b along soft vs hard geodesics on SU(3). If M is anisotropic (larger along soft directions), the pair vibration has a preferred propagation direction. This would connect the curvature anatomy directly to the collective excitation spectrum.

### 3.4 Bayesian Assessment of Curvature Invariants (PRIORITY 4)

Theorem 2 (K(u(1), C^2) = 1/16 at all tau) is verified to 10^{-15} at 26 tau values. The question is: is this a consequence of the Jensen deformation ansatz (3-parameter family L_1, L_2, L_3 with the volume constraint L_1 * L_2^3 * L_3^4 = 1), or does it survive under general left-invariant metric deformations?

A general left-invariant metric on SU(3) has 36 independent parameters (symmetric 8x8 matrix), not 2 (after volume constraint). The Jensen metric is a 2D subspace of this 36D space. K(u(1), C^2) = 1/16 exactly on this 2D subspace does NOT guarantee it holds on the full 36D space.

**Proposed computation**: Sample 100 random left-invariant metrics (random 8x8 positive-definite matrices, volume-normalized) and compute K(u(1), C^2) for each. If it deviates from 1/16, the protection is Jensen-specific. If it holds, the protection is structural (from the Lie algebra alone). This is the analog of testing whether a shell gap persists under triaxial deformation (Paper 10, gamma deformation) or only under axial deformation.

Paper 06 methodology applies: use a GP emulator trained on a Latin hypercube sample of the 36D parameter space. The KL divergence between the prior (uniform on [0, 1/4]) and the posterior for K(u(1), C^2) directly measures how protected this invariant is.

### 3.5 Deformation-Dependent Shell Evolution (PRIORITY 5)

The C^2-C^2 isotropization (within-doublet/cross-doublet ratio dropping from 4.0 to 1.17) is directly analogous to shell evolution in exotic nuclei (Paper 01). In nuclei, as the neutron number increases far from stability, the tensor force shifts shell gaps and magic numbers evolve (N=8 erodes, N=14 emerges). Here, as tau increases, the curvature "shell gaps" between branches evolve.

**Proposed computation**: Track the curvature branch separations (gaps between the 6 branches) as functions of tau. Identify any tau where two branches cross or merge (analog of level crossing in the Nilsson diagram, Paper 07). At such a crossing, the effective degeneracy doubles and the density of states jumps -- potentially enhancing pairing. This is the Nilsson-diagram construction for the Jensen metric on SU(3).

---

## Section 4: Connections to Framework

### 4.1 Connection to S37-S38 Instanton Physics

The crystal geometry provides the STAGE on which the S37-S38 instanton physics plays out. The key connection: the instanton action S_inst = 0.069 was computed using the (0,0) sector BCS pairing only. The curvature anatomy reveals that the su(2)-C^2 cross-planes (12 soft directions) provide the lowest-energy collective channels. If instanton tunneling preferentially occurs along these soft directions, the effective action could differ from the (0,0) estimate.

The ^24Mg nuclear analog (sd-shell with shape coexistence, from S38 W2) now has sharper content. ^24Mg exhibits coexisting prolate and oblate shapes, with the collective pair vibration mediating transitions between them. The soft/hard curvature branch structure of the Jensen crystal provides the deformation coordinate along which this shape coexistence occurs. The soft branches are the beta_2 direction (quadrupole deformation), and the hard branches are the beta_3 direction (octupole) -- or rather, the analogs in the 8D internal geometry.

### 4.2 Connection to Richardson-Gaudin Integrability

The 8 Richardson-Gaudin conserved quantities from S38 correspond to the 8 dimensions of SU(3). The curvature anatomy gives the metric structure in which these conserved quantities propagate. The protected invariants (K = 0 for u(1)-su(2), K = 1/16 for u(1)-C^2) constrain the form of the conserved quantities: any integral of motion must respect the block structure of the metric.

The key implication: the GGE relic state (which never thermalizes due to integrability) has a specific curvature profile. The conserved quantities determine which curvature branches are populated and which are frozen. The 91.3% B2 dominance of the GPV (S46) means the GGE is predominantly in the soft curvature sector -- the relic universe "lives" on the soft springs of the crystal.

### 4.3 V_B3B3 and the Proximity Effect

The S46 V-B3B3-46 result (V_B3B3_rms = 0.059, one repulsive channel) now has geometric content from the curvature anatomy. B3 lives on the hard su(2)-su(2) branches (K = 0.122). The weak B3 pairing (Delta_B3 = 0.094, induced by B2-B3 coupling, not self-consistent) is the geometric consequence of B3 living on stiff springs. The curvature ratio 12.5:1 predicts that B3 pairing should be weaker than B2 by exp(-c * 12.5) for some coupling constant c -- qualitatively matching the observed 85:1 pairing ratio.

This connects to the q-theory crossing problem: the B3 gap needs to reach 0.13 for the crossing at the fold. The curvature anatomy says this is geometrically disfavored -- B3 lives on stiff springs that resist pairing. The remaining path (tau sweep where B2-B3 energy gap narrows) corresponds to finding a tau where the curvature ratio shrinks, bringing B3 into a softer regime.

---

## Section 5: Open Questions

### 5.1 Is the Pairing Field Self-Consistent on SU(3)?

The fundamental open question. The synthesis presents a beautiful geometric picture of curvature, condensate, and spectrum -- but the BCS solution is not self-consistent through the spatial degrees of freedom. In nuclear DFT, a "solution" that uses gaps from one configuration (say, spherical) to compute densities in another (say, deformed) is not a solution at all. It is an input to the first iteration of the self-consistency loop (Paper 03, the HFB matrix equation must be solved iteratively until convergence). The sector-resolved HFB solution (Suggestion 3.1) would close this loop.

### 5.2 Does the Protected Chain Survive Beyond Jensen?

The q_7^2 = K(u(1), C^2) = 1/16 chain is proven for the Jensen family. Does it hold for general left-invariant metrics? If it does, it is a statement about SU(3) geometry, period. If it fails, it is a statement about the Jensen ansatz, and its physical relevance depends on how physical the Jensen metric is.

### 5.3 What is the Physical Status of the 0D Limit?

L/xi_GL = 0.031 means the condensate coherence length vastly exceeds the system size. In Anderson's ultrasmall grains (level spacing delta >> Delta), BCS breaks down completely. S46 confirmed: N_pair = 1, BCS overestimates by 60%, PBCS needed. The crystal geometry synthesis was built using BCS gaps. How much of the geometric picture survives when replaced by exact (ED or PBCS) gaps? The W2-1 condensate contrast of 3.14 x 10^6 depends on sector-averaged BCS gaps. With PBCS gaps reduced by 36% (S46 result), the contrast will change.

### 5.4 Is the Curvature Anisotropy Growth Bounded?

K_max/K_min grows from 4.0 at tau = 0 to 12.5 at the fold. If this growth continues, does the crystal develop a singular limit at some tau_critical where the soft branches hit K = 0? A zero curvature in the su(2)-C^2 sector would mean those directions become flat -- potentially signaling a decompactification instability. In nuclear physics, this is the Bohr-Mottelson instability of the nuclear shape toward fission when the potential surface becomes flat in the deformation coordinate (Paper 05, fission barrier vanishing). The curvature-versus-tau curve for the soft branch should be computed to at least tau = 1.0 to check for this.

### 5.5 Can the Chladni Pattern be Computed?

Tesla mentions Chladni patterns (vibration nodes on the crystal) but notes that eigenvectors are discarded in the current computation. This is the most important missing piece. In nuclear physics, shell structure is fully characterized only when you know both eigenvalues AND eigenfunctions. The Nilsson wave functions (Paper 07) tell you not just the energy levels but their spatial distributions, quadrupole moments, and transition matrix elements. The Dirac eigenvectors on Jensen-deformed SU(3) would complete the crystal geometry picture by showing where each mode concentrates on the manifold.

---

## Closing Assessment

Session 47 delivers solid structural results: two protected curvature invariants (verified to machine precision), a six-branch body plan of the Jensen crystal, and the B2 funnel confirmed from three independent perspectives. These are permanent geometry, independent of the BCS pairing physics.

The condensate analysis (W2-1) is mathematically correct but physically interpretable only with the 0D caveat: in a system where L/xi_GL = 0.031, "where the condensate lives" is a spectroscopic question (which characters dominate the expansion), not a position-space question. The contrast ratio of 3.14 x 10^6 measures character coherence, not spatial concentration of Cooper pairs.

The soft-pairing anti-correlation is the finding with the highest nuclear-structure content. It maps directly onto the Nilsson-diagram / mid-shell pairing mechanism (Papers 02, 03, 07, 08) and should be testable as a structural result across the full tau range. The proposed curvature-gap correlation function (Suggestion 3.2) is the decisive computation.

The crystal is real. Its geometry is rich. Its pairing lives on the softest part of the skeleton. What remains is to solve the self-consistency problem: close the HFB loop through the spatial degrees of freedom, not just through the single-particle spectrum. Until then, the crystal geometry is a beautiful skeleton waiting for the self-consistent flesh.

The crystal has bones. What it needs now is a self-consistent skin.
