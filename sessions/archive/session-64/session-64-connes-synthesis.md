# Session 64 Synthesis: The CC Walls and the BdG Foundation

**Date**: 2026-04-01
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- sessions/archive/session-64/session-64-results-workingpaper.md
- sessions/archive/session-64/gge-kms-64-content.md
- sessions/archive/session-63/session-63-hawking-quantum-acoustics-workshop.md
- sessions/archive/session-63/session-63-volovik-van-den-dungen-workshop.md

---

## I. Session Outcome

Session 64 mapped the cosmological constant problem to its structural core within the spectral action framework and resolved the tensor-to-scalar ratio. The Master Gate CC-COMBO-64 = FAIL: Path C (transit-as-relaxation along Jensen) is permanently closed by the R(tau) monotonicity theorem (AM-GM proof), and Path B (gravitational integrability-breaking) closes quantitatively at 110 OOM shortfall. The 114-OOM gap is confirmed real, not a category error between the spectral action and Jacobson formalisms. The session's decisive positive result is r = 0.033 (two independent computations), resolving the S62 tension and producing a zero-free-parameter prediction within reach of CMB-S4. From the NCG standpoint, the session establishes three foundational structures: the BdG heat kernel factorization (exact), the generalized KMS compatibility of the GGE with Tomita-Takesaki modular theory (four theorems), and the spectral moment decoupling theorem that structurally separates the CC problem from the area theorem.

---

## II. Key Results

### 1. BDG-KASPAROV-64: Heat Kernel Factorization and Sakharov Decomposition

**Result**: a_2^{BdG}/a_2^{bare} = 0.887; heat kernel factorization K_{BdG}(t) = exp(-Delta^2 t) K_{bare}(t) exact to 2.2e-16. Classification: GEOMETRIC.

The computation of the BdG Seeley-DeWitt coefficient reveals a precise structural decomposition. The BdG spectral triple (A_F, H_{BdG}, D_{BdG}) constructed in S35 has a well-defined heat kernel that factorizes exactly: the BdG heat trace equals the bare heat trace multiplied by a universal gap-dependent exponential. This is an EXACT identity for s-wave BdG pairing, verified to machine epsilon across the full t-range [1e-4, 1.0].

The factorization provides the analytic backbone for understanding how the BCS condensate modifies gravity. The Sakharov mechanism (delta a_2/a_2 = -0.361, from the S63 VdD-Hawking workshop) decomposes into three additive contributions: (A) spectral gap opening (omega^2 -> omega^2 + Delta^2), which accounts for 31.2% of the total; (B) BCS quantum depletion through occupation factors v_k^2, accounting for the bulk; (C) curvature response dDelta/dR. The BdG heat kernel captures ONLY effect (A). This is structurally important: the self-consistent BdG spectral triple must incorporate ground-state information (the occupation weights), not merely the excitation spectrum. The Kasparov product conditions are satisfied at 4/5 (K5 marginal at alpha = 0.566, exceeding the Kato-Rellich 1/2 bound, but gap-protected against spectral flow).

The moment shift identity M_2(BdG) = M_2(bare) + N Delta^2 is verified to 1.8e-16. This confirms that the BdG spectral action at any scale Lambda relates to the bare action by a universal correction computable from Delta alone. The factorization is PERMANENT and survives to all orders in the Seeley-DeWitt expansion.

### 2. GGE-KMS-64: Modular Theory and the Multi-Temperature Structure

**Result**: Four theorems proven -- generalized KMS, 8-fold modular decomposition, Tomita-Takesaki positivity with negative lambda_B2, entropy decomposition. Dense Connes spectrum implies type III_1 in thermodynamic limit. Classification: GEOMETRIC.

The GGE state rho_{GGE} = Z^{-1} exp(-sum_k lambda_k R_k) on the BdG spectral triple satisfies a generalized KMS condition in the multi-strip {z in C^8 : 0 < Im(z_k) < lambda_k}. This follows from two inputs: the mutual commutativity [R_j, R_k] = 0 (Richardson-Gaudin integrability, verified to machine epsilon in S63 and W1-B), and the finite-dimensionality of the Fock space (making all correlation functions entire). The proof is constructive (equations (16)-(18) of the working paper).

The Tomita-Takesaki modular operator for the GGE decomposes:

    Delta_{GGE} = prod_{k=1}^{8} exp(-lambda_k (R_k^L - R_k^R))

into 8 commuting factors, each generating an independent modular flow. The TOTAL modular automorphism group sigma_t^{GGE} is the product of 8 independent sector flows, each satisfying its own sector KMS condition at inverse temperature lambda_k. The negative Lagrange multiplier lambda_B2 = -0.053 poses no obstruction: the modular operator eigenvalues Delta_{nm} = p_n/p_m are ratios of strictly positive numbers (the exponential function is positive regardless of the sign of its argument). The B2 sector's negative temperature indicates population inversion -- the condensate mode B2[0] is over-occupied relative to the infinite-temperature state -- but this is a physical feature, not a mathematical pathology.

The modular flow has 8 fundamental frequencies omega_k = lambda_k/(2 pi) that are generically rationally independent. The Connes spectrum (Arveson spectrum) Sp(sigma^{GGE}) = {sum n_k lambda_k : n_k in Z} is therefore a dense subgroup of R. In the thermodynamic limit (L_max -> infinity), this would give a type III_1 factor -- the unique hyperfinite factor classified by Connes in 1973 (Paper 04), with full Connes invariant S(M) = R_+. This is precisely the von Neumann algebra type arising in QFT via the Haag-Hugenholtz-Winnink theorem for KMS states.

The von Neumann entropy of the GGE decomposes as S_{GGE} = sum_k S_k, where each sector entropy S_k = lambda_k <R_k> + ln Z_k is expressible as a spectral-action-type functional in the sense of Paper 15 (Chamseddine-Connes-van Suijlekom 2019). This provides 8 independent entropy-spectral action channels, each governed by its own Lagrange multiplier.

The Connes cocycle connecting different GGE states with Lagrange multipliers {lambda_k} and {lambda_k'} is u_t = exp(it sum_k (lambda_k' - lambda_k) R_k), confirming the Connes Radon-Nikodym theorem (Paper 04, Chapter V). The three distinct times coexisting on the spectral triple -- modular (sigma_t^{GGE}), cosmological (tau-flow), and Unruh (vacuum modular flow) -- are related by cocycles, not in conflict.

### 3. S[D_{sc}] > 0 Structural Theorem and the Post-Jensen Landscape

**Result**: R(tau) strictly monotonically increasing for all tau > 0 (AM-GM proof); fold is R-saddle with signature (8+, 27-) in 35D volume-preserving subspace; a_2 decreases off-Jensen but a_0/a_2 INCREASES. Classification: GEOMETRIC.

The proof that dR/dtau >= 0 on volume-preserving Jensen-deformed SU(3) is exact:

    dR/dtau = exp(-4 tau) - 2 exp(-tau) + exp(2 tau) >= 0

by AM-GM applied to exp(-4 tau) + exp(2 tau) >= 2 exp(-tau), with equality only at tau = 0 (where R'''(0) = 18 > 0, a third-order inflection). This is the S63 CC-PATH-E-63 structural theorem realized: the spectral action along Jensen DIVERGES. S(tau_fold)/S_floor = 1.117 at the fold; at tau = 10, S/S_floor exceeds 10^{15}.

The HESSIAN-DESCENT-64 computation reveals the 36D structure beyond Jensen. The R-Hessian restricted to the 35D volume-preserving tangent space at the fold has signature (8+, 27-). The round metric is a LOCAL MAXIMUM of R (d^2R/da^2 = -2, d^2R/db^2 = -8). The steepest R-descent is ANTI-JENSEN: expand SU(2), shrink CP^2 and U(1), the geometric opposite of the Jensen deformation. Along this direction, R decreases from 2.018 to 0.578 over 2000 gradient steps.

The critical structural finding: this does NOT help with the CC. Since a_2 = C * R * Vol with C > 0 and Vol constant (volume-preserving), decreasing a_2 via the anti-Jensen direction INCREASES the ratio a_0/a_2 (because a_0 is constant under volume-preserving deformations). The physical CC = rho_{vac} proportional to a_0/a_2 therefore WORSENS. This is the a_0/a_2 trap: any volume-preserving direction that decreases a_2 automatically increases the CC.

Escape requires either breaking volume preservation (allowing a_0 to change) or accessing the spectral action through a channel not captured by the Seeley-DeWitt expansion. The S45 UNEXPANDED-SA-45 theorem (the Taylor expansion is exact for finite spectra) constrains the latter route to infinite-volume or infinite-L_max effects.

### 4. Shell Hessian UV Sensitivity

**Result**: First zero crossing at step 2 (removing (2,1) irrep); L=3 shell = 79.9% of one-loop Hessian Frobenius norm; all 36 eigenvalues negative after removing L=3 shell. Classification: GEOMETRIC.

The FRG shell-by-shell decimation of the one-loop Hessian reveals that the fold's stability is a UV-dominated phenomenon. The tree-level spectral action makes the fold a local MAXIMUM in all 36 moduli directions. The one-loop correction from Tr ln(D_K^2) provides positive contributions that flip the sign, but these contributions are concentrated in the highest Peter-Weyl shell: the L=3 irreps ((1,2), (2,1), (0,3), (3,0)) contribute 79.9% of the total one-loop Frobenius norm.

From the NCG perspective, this is structurally significant. The spectral action Tr f(D^2/Lambda^2) receives contributions from ALL eigenvalues of D. The one-loop effective action adds a functional-determinant correction whose Hessian decomposes additively by Peter-Weyl irrep. The UV dominance means the spectral action landscape -- whether the fold is a minimum or maximum of the effective action -- depends on the highest PW modes included. At L_max = 2 (removing L=3), the fold becomes a maximum; at L_max = 3, it is a minimum.

The conjugate pairs (p,q) and (q,p) contribute identically to the Hessian (CPT symmetry: [J, D_K(tau)] = 0, Session 17a D-1), verified to machine precision. The per-shell Frobenius norm scales approximately as ||H_{1-loop}^{(L)}||_F ~ L^{2.5}, suggesting convergence, but L_max = 4 verification is needed.

This result constrains the framework's effective-theory interpretation: the spectral triple at L_max = 10 is the physical object (DISSOLUTION-SCALING-44: epsilon_c ~ N^{-0.457}), not a truncation of an underlying continuum. The fold stability is a property of the full discrete spectrum, and removing UV modes changes the qualitative physics.

### 5. The Self-Consistent BdG Spectral Triple as Foundation

**Result**: BdG spectral triple satisfies 4/5 Kasparov conditions; factorization K_{BdG}(t) = exp(-Delta^2 t) K_{bare}(t) exact; GGE-KMS compatible with Tomita-Takesaki. Classification: GEOMETRIC.

The BdG spectral triple (A_F, H_{BdG}, D_{BdG}) from S35 (both KILL gates PASS) now has a complete operator-algebraic characterization. The first-quantized spectral triple satisfies the Kasparov product conditions with K5 marginal but gap-protected. The heat kernel factorization provides the analytic connection between the BdG and bare spectral actions at all scales. The second-quantized GGE state on the Fock space over H_{BdG} satisfies the generalized KMS condition with 8 independent sector temperatures, fully compatible with the Tomita-Takesaki modular theory that is central to Connes' classification program.

The BdG spectral triple captures 31.2% of the Sakharov gravitational coupling reduction through the spectral gap contribution. The remaining 69% requires the BCS ground state structure -- specifically the occupation factors v_k^2 and dDelta/dR. This means the SELF-CONSISTENT BdG spectral triple (incorporating the ground state as input, not just the excitation spectrum) is the correct mathematical object for the framework's gravitational sector. The self-consistent construction was pre-registered in CC-PATH-E-63 and remains the highest-priority open computation.

### 6. VAB Rank = 5 and Three-Generation Structure

**Result**: Second variation V_{AB} of one-loop spectral action has rank = 5 non-singlet C_2(U(2)) sectors; structural room for 3 fermion generations. Classification: PARTICLE.

The 36D moduli tangent space T_{g_{fold}} Met(SU(3)) decomposes under Ad(U(2)) into 6 irreducible sectors classified by the quadratic Casimir C_2(U(2)). The commutation [V_{AB}, C_2(U(2))] = 0 (to the finite-difference precision 3.6e-3) forces V_{AB} to block-diagonalize. All 5 non-singlet sectors have full rank with non-degenerate eigenvalue spectra. Within the C_2 = -1.50 sector (dim 8), the eigenvalues split into two sub-clusters {57.45 x 4} and {155.32 x 4}, providing hierarchical mass-matrix structure.

From the NCG standpoint, three generations are NOT a consequence of the axioms alone -- they are an additional datum. The Z_3 x Z_3 grading of SU(3) is a candidate origin (S34), but this remains conjectural. The VAB rank = 5 result establishes that the spectral action's moduli structure has sufficient dimensionality (5 independent Yukawa texture directions) to accommodate 3 generations with hierarchical masses. Whether the specific SU(3) fiber geometry SELECTS 3 generations from these 5 directions requires computing the chiral asymmetry matrix C_{alpha,beta} (Paper 17, Baptista 2025, Proposition 5.1).

### 7. Spectral Moment Decoupling: CC and Area Theorem Are Siblings, Not Parent-Child

**Result**: CC monotonicity (F_{-1} = sum d_n/omega_n) and NEC (F_{+1} = sum d_n omega_n n_n) operate through different spectral channels. A construction exists breaking CC monotonicity while preserving NEC. Classification: GEOMETRIC.

The spectral moment decoupling theorem is PERMANENT: it holds for any spectral triple (A, H, D) with discrete spectrum generating Einstein gravity through a_2, independent of KO-dimension, real structure, and fiber geometry.

The hierarchy topology established in the S63 Hawking-QA workshop is refined:

    Level 0 --> Level 1 --> Level 2 --X--> Level 3
    (substrate)  (BCS)     (CC/a_0)        (NEC/a_2, a_4)

Levels 0-1-2 are rigidly linked (BCS Coherence Suppression Theorem, shared-spectrum theorem). The Level 2 -> Level 3 connection is FLEXIBLE: they share an algebraic ancestor (spectral positivity at Level 0) but operate through algebraically independent spectral moments. The proof by construction uses distinct B/F spectra to break CC monotonicity (dE_{ZP}/dq changes sign) while preserving the NEC (sum of positive terms remains positive).

This is a PERMISSION result: the CC problem can be solved without breaking gravity. The surviving theoretical path requires giving bosonic and fermionic sectors effectively DIFFERENT spectra. Whether the almost-commutative geometry's grading structure (gamma_5 vs J) produces such a split is the decisive unresolved question.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S-ASYMPTOTIC-64 | FAIL (permanent) | dR/dtau >= 0 by AM-GM; a_2(10)/a_2(fold) = 1.2e8 |
| R-G-CHARGE-DECOMPOSITION-64 | PASS | 7/8 charges broken > 0.01 threshold; 110 OOM shortfall |
| SA-VERSUS-JACOBSON-64 | FAIL (permanent) | Lambda_SA = Lambda_J; 114-OOM gap confirmed real |
| HESSIAN-DESCENT-64 | PASS (with trap) | R-Hessian (8+, 27-); a_2 decreases off-Jensen but a_0/a_2 increases |
| BDG-KASPAROV-64 | INFO | a_2^{BdG}/a_2^{bare} = 0.887; factorization exact |
| TENSOR-BURST-64 | PASS | r = 0.033 < 0.036 (BICEP/Keck) |
| SHELL-HESSIAN-64 | FAIL | Zero crossing at step 2; L=3 = 79.9% of H_{1-loop} |
| GGE-KMS-64 | INFO | 4 theorems proven; type III_1 limit; 8-fold modular |
| TENSOR-SCALAR-64 | PASS | r = 0.0333; independent KK verification (0.25% agreement with W3-A) |
| NS-FINAL-64 | PASS | n_s = 0.9557 +/- 0.0036; 2.2 sigma from Planck |
| VAB-RANK-64 | PASS | rank = 5 >= 3; 36/36 positive eigenvalues |
| SPECTRAL-MONO-LINK-64 | FAIL (permanent) | CC and NEC decouple at Level 2->3 |
| LINEWIDTH-HIERARCHY-64 | FAIL | Gamma_B2 > Gamma_B1 > Gamma_B3 (reversed) |
| SKYRMION-BARYON-64 | FAIL | M_skyrm = 10^{22} GeV (22 OOM above proton) |

---

## IV. Structural Implications

### NCG Axiom Status After S64

The 12D product spectral triple (M^4 x SU(3), H, D) maintains its S28c standing: 6/7 NCG axioms PASS, with only Axiom 5 (order-one condition) failing at ||[[D,a],b^o]|| = 4.000 for (H,H) pairs. The S45 weak order-one route (Bochniak-Sitarz) remains CLOSED (GG/Full = 1.000 exact). No new axiom-level developments in S64.

The BdG spectral triple gains substantial new structure:
- Heat kernel factorization EXACT (permanent)
- GGE-KMS compatible with Tomita-Takesaki (4 theorems proven)
- Kasparov conditions 4/5 (K5 marginal, gap-protected)
- Both KILL gates continue to PASS (S35, verified)

### The CC Constraint Surface

S64 closes 5 additional CC mechanisms, bringing the total to at least 14 CC closures. The constraint surface is now:

**Permanently closed:**
- Jensen relaxation (R-monotonicity, AM-GM)
- Category error (Lambda_SA = Lambda_J, structural proof)
- Volume-preserving off-Jensen (a_0/a_2 trap)
- Jacobson multi-T (T_Unruh is kinematic, 3 arguments)
- 12D Jacobson-Kasparov (Lambda_eff = (1/8)R_K, wrong sign)
- Shared-spectrum B/F cancellation (S63 maximum theorem)
- All perturbative monotone spectral functionals (S19 exhaustion)

**Structurally permitted but uncomputed:**
- Volume-breaking deformations (a_0 changes when Vol changes)
- Distinct B/F spectra (spectral moment decoupling permits this)
- Nonlocal spectral action (beyond SDW expansion, requires L_max -> infinity)
- Self-consistent BdG spectral action (D_{BdG} captures 31% of Sakharov)

### What the Spectral Action Tells Us and What It Does Not

The spectral action Tr f(D^2/Lambda^2) is UNIVERSAL: it depends only on the spectral triple, not on additional input. Session 64 demonstrates both the power and the limitation of this universality.

Power: the spectral index n_s = 0.9557 is a SHAPE INVARIANT of the spectral action profile, cutoff-independent (verified across 5 families, spread 0.0012). The tensor ratio r = 0.033 follows from the H2 theorem, which is a geometric property of volume-preserving deformations in DeWitt superspace. Both observational predictions emerge from the spectral triple and its axioms alone.

Limitation: the CC is controlled by a_0/a_2, a RATIO of spectral moments. The spectral action computes both moments from the same D_K eigenvalues. The a_0 moment counts modes (= 6440), the a_2 moment weights modes by inverse-squared eigenvalues (= 2776.17 M_KK^{-2}). Their ratio is O(1) in M_KK units, giving Lambda_SA ~ M_KK^2 ~ 10^{114} Lambda_obs. No manipulation within the standard spectral action framework changes this by more than O(1) factors. The CC problem requires either modifying D_K itself (Level 0 intervention) or accessing physics beyond the spectral action.

### The Modular Structure as Mathematical Home

The GGE-KMS-64 result provides the natural mathematical home for the framework's post-transit state. In Connes' classification of von Neumann algebras, the GGE modular flow has dense Connes spectrum, approaching type III_1 in the thermodynamic limit. This is the algebra type of quantum field theory (Haag-Hugenholtz-Winnink). The framework's post-transit physics -- 8 independent thermodynamic sectors with mode-dependent temperatures, including population inversion in B2 -- fits naturally within the operator-algebraic structure that Connes classified in 1973.

The three coexisting time evolutions on the spectral triple (modular, cosmological, Unruh) are related by the Connes cocycle, not in conflict. This cocycle structure (Radon-Nikodym theorem, Paper 04 Chapter V) is the precise mathematical statement of how the GGE's multi-temperature structure interacts with the emergent spacetime geometry.

---

## V. Forward Projection

### Highest Priority: BCS-DRESSED-SA (S65 Core)

The single most consequential uncomputed quantity is the BCS-dressed spectral action profile S^{BCS}(tau). The BDG-KASPAROV-64 factorization provides the analytic framework; what remains is computing eps_H^{BCS} = (S'^{BCS})^2 / (2 S^{BCS} S''^{BCS}) at 5-7 tau values. This controls:
- n_s correction: estimated +0.0014 toward Planck (reducing 2.2-sigma tension)
- Fold Hessian: does BCS dressing preserve the one-loop positive-definiteness?
- Sakharov gravitational coupling: completing the 31% -> 100% chain

Pre-registered: |delta(eps_H)/eps_H| > 0.01.

### CC Surviving Paths (NCG Perspective)

The spectral moment decoupling theorem opens a specific theoretical direction: can the almost-commutative geometry's grading structure produce effectively distinct B/F spectra for the CC-relevant inverse moment F_{-1}? The bosonic and fermionic sectors share D_K but differ in their gamma_5 and J gradings. If this structural difference produces an effective spectrum split at the a_0 level, the CC monotonicity can be broken without violating the NEC. This is the most NCG-native surviving path.

Volume-breaking deformations (relaxing det(g_K) = const) allow a_0 to change. The a_0/a_2 trap holds only for volume-preserving directions. Whether a dynamical mechanism exists to simultaneously decrease a_0 and increase a_2 in the full 36D moduli space is untested.

### Modular Theory Computation

The GGE-KMS structure suggests a computation: the modular Hamiltonian K = -ln(rho_{GGE}) = sum_k lambda_k R_k generates the canonical time evolution. Does the modular flow of the spectral action -- sigma_t^{GGE}(Tr f(D^2/Lambda^2)) -- produce a dynamical CC relaxation? The modular flow acts on the algebra, not on the spectral triple directly, but the spectral action is a trace on the algebra and therefore a modular invariant. Whether the modular dynamics produces non-trivial evolution of the CC-relevant spectral moments is an open structural question that connects the GGE-KMS result to the CC problem.

### L_max Convergence

The shell Hessian UV-sensitivity demands L_max = 4 verification. The per-shell Frobenius norm scales as L^{2.5}; at L = 4, the 8 new irreps would add approximately 2.6x the L=3 contribution if the scaling continues. This would either further stabilize the fold (supporting the spectral triple as an emergent effective theory) or reveal an asymptotic instability requiring UV completion.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | BdG heat kernel factorization exact | GEOMETRIC | PERMANENT | K_{BdG}(t) = exp(-Delta^2 t) K_{bare}(t); captures 31% of Sakharov |
| 2 | Generalized KMS (4 theorems) | GEOMETRIC | PERMANENT | GGE compatible with Tomita-Takesaki; 8-fold modular; type III_1 limit |
| 3 | R(tau) monotonicity on Jensen | GEOMETRIC | PERMANENT | Path C CLOSED; AM-GM proof exact |
| 4 | R-saddle at fold (8+, 27-) | GEOMETRIC | PERMANENT | 27 descent directions for a_2; anti-Jensen = expand SU(2) |
| 5 | a_0/a_2 trap | GEOMETRIC | PERMANENT | Off-Jensen a_2 decrease WORSENS CC |
| 6 | Lambda_SA = Lambda_J | GEOMETRIC | PERMANENT | 114-OOM gap is real, not category error |
| 7 | Spectral moment decoupling | GEOMETRIC | PERMANENT | CC and NEC operate through independent spectral channels |
| 8 | Shell Hessian UV dominance | GEOMETRIC | INFO | L=3 = 79.9% of one-loop; fold stability UV-dependent |
| 9 | r = 0.033 (two independent) | GEOMETRIC | PASS | H2 theorem kills first-order; second-order below BICEP/Keck |
| 10 | n_s = 0.9557 +/- 0.0036 | GEOMETRIC | PASS | 2.2 sigma from Planck; one-loop corrected; BCS uncomputed |
| 11 | VAB rank = 5 | PARTICLE | PASS | Structural room for 3 generations in 5 non-singlet sectors |
| 12 | Fermi-surface lock v^2(B2[0]) = 1/2 | GEOMETRIC | PERMANENT | Condensate occupation immune to energy-shift perturbations |
| 13 | Mukhanov-Sasaki inapplicable | GEOMETRIC | PERMANENT | N_e = 7.75, eta_H = 0.96; modes never freeze |
| 14 | All 5 baryogenesis channels CLOSED | PARTICLE | CLOSED | Fiber skyrmions at 10^{22} GeV; remaining: UV completion or 4D effective |
| 15 | Chirality: no tensor cancellation | GEOMETRIC | PERMANENT | {gamma_9, dD_K/dtau} = 0; antisym x antisym = sym |
