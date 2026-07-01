---
name: Permanent Theorems and Verified NCG Structures
description: All machine-epsilon verified NCG axioms, permanent structural theorems, and key identities -- the core mathematical inventory
type: reference
---

## Verified NCG Structures

### Axiom Status (12D product triple M^4 x SU(3) x F_SM)
- **6/7 axioms PASS**. Only Axiom 5 (order-one) FAILS at 4.000 (H,H).
- Weak order-one (Bochniak-Sitarz): FAILS MAXIMALLY (S45). GG/Full=1.000 exact.
- Surviving order-one routes: CCS quadratic, Pati-Salam, twisted triples.

### KO-Dimension
- KO-dim(F_SM) = 6: (eps,eps',eps'')=(+1,+1,-1), J^2=+1. Machine epsilon (S8).
- KO-dim(SU(3)) = 0 (d=8 mod 8=0, NOT 6). J^2=+1, [J,gamma_9]=0. JD=-DJ from B_- (S65).
- KO-dim(M^4 x SU(3)) = 4. d=8 uniquely degenerate: B+/B- same KO. J_tot^2=-1. eps''=+1. PERMANENT (S66).
- KO mismatch (product=4 vs finite=6) is PERMANENT. SA unaffected; fermionic sector affected.

### Core Identities
- H_F = C^32: SM quantum numbers correct (S7).
- [J, D_K(s)] = 0 identically (S17a). CPT hardwired.
- Order-zero: PASSES for A_F. Uniquely selects SM algebra from commutant (S31).
- Order-one violation hierarchy: (H,H)=4.0, (C,H)=2.83, (C,C)=2.0 (S9-10, S28c). CONTEXT: this is the BAPTISTA A_F on the Cliff(R^8) SPINOR space of the PRODUCT triple M^4 x SU(3) x F_SM (s22c), a representation MISMATCH (Baptista basis != Cliff spinor basis), NOT the CCM finite bimodule. DISTINCT from the N2 finite-bimodule result below.

### N2 o-map H-extraction (S116 W5-2, S116-W5-BIMODULE-H PASS) -- atlas-04 N2 CONDITIONAL->VERIFIED
- On the CCM finite bimodule (A_LR=C+H_L+H_R+M_3(C), H_F=C^32, KO-6 J [J^2=+1, JD=DJ, Jg=-gJ all machine-0], D_F=Yukawa(S)+Majorana(T)), the ORDER-ONE condition [[D_F,pi(a)],pi^o(b^o)]=0 (o-map pi^o(b^o)=J pi(b)* J^-1) extracts A_F = C+H+M_3(C), dim_R=24, a VERIFIED *-subalgebra (closure resid 2.2e-15), order-one residual 1.665e-29 over all 24^2 pairs. order-zero [pi(a),pi^o(b^o)]=0 machine-0. Here order-one WORKS (contrast the spinor-rep mismatch above) -- the proper finite bimodule, not the product-triple-on-spinors.
- H = H_L (LEFT quaternions survive); H_R BROKEN (its diagonal tied to the C factor by the Majorana M_R: nu_R<->nu_R^c; no independent H_R summand). The famous CCM 28->24 reduction.
- LEFT-ONLY COMMUTANT {a:[D_F,pi(a)]=0} = C+M_3(C), dim_R=20 (M_3 color-blind + one U(1) = a C<->H_R-diag tie the Majorana makes compatible). H does NOT lie in the commutant (Yukawa S mixes SU(2)_L doublet). DEFICIT 24-20=4 = dim_R(H) is the order-1-but-not-order-0 summand the J-twisted o-map supplies. [SIGN] deficit=+4>0.
- H = {M in M_2(C): eps Mbar eps^-1 = M}, eps=i*sigma_2: dim_R=4 quaternion real form, basis {I,i*sx,i*sy,i*sz}, e_a^2=-I, {e_a,e_b}=0, Hamilton e1e2=-e3 -- SAGE-EXACT over Q(i).
- tau-INVARIANT: reads D_F BLOCK PATTERN not magnitudes (rescale x2.7 -> identical dim-24 closure, subspace_dist 4.2e-15). tau_fold=0.19 is CANONICAL-IMPORT-BINDING anchor only.
- METHOD LESSON (reusable): the greedy order-one fixed-point iteration is OVER-STRICT -- it strips ALL of H_R in pass 0 (incl. the H_R-diagonal needed for the C<->H_R-diag tie), then drops the now-untied pure-C, returning 22 not 24. The RIGOROUS maximal order-one subalgebra = closure span(commutant(20) + H_L(4)) = 24, verified by DIRECT all-pairs order-one + *-subalgebra closure. When a fixed-point greedily removes a whole factor, check whether a cross-factor TIE (here C<->H_R-diag) lives in the removed span.

## Spectral Action & Monotonicity Theorems

- **SA monotonicity**: V_eff = S_b + F_BCS monotonically decreasing ALL tau. Connection-independent. SD exact 40+ digits (S28). No smooth minimum.
- **Taylor expansion exactness** (S45): S(L)=sum d_k f(lam_k^2/L^2) IS its Taylor series for L>lam_max. No non-perturbative content. CC hierarchy impossible without f fine-tuning.
- **SA scalar instability** (S46): delta^2 Tr f(D^2/L^2) < 0 ALL scalar phi, ALL monotone f, ALL tau. Structural: f'(x)<0.
- **Nonlocal SA worsens CC** (S65): All damping f increase a_0/a_2.
- **U(2) preservation** (S65): All 28 off-diagonal SA gradient components=0 at U(2)-invariant metrics.
- **SA-ON-OMEGA-TAU saddle** (S46): 2D landscape SADDLE at fold. H_2d=(-0.639,+2.337). Transit is 1D.
- **Spectral entropy**: Monotone DECREASING all tau, all beta. Fold invisible to entropy.

## CC Theorems (ALL geometric routes CLOSED)

- **a_0/a_2 = C_Q/R universal** (S65): For ANY left-invariant metric on SU(3), CC ratio depends ONLY on R. 36D->1D.
- **Volume cancellation** (S65): Q(x)=C_Q/R(x), fiber volume cancels identically.
- **Jensen-mean shift negligible** (S65): Best delta_Q/Q ~ 8.6e-3*eps^2. Negligible for 120 OOM gap.
- **a_0/a_2 trap** (S64): VP a_2 decrease INCREASES a_0/a_2. CC worsens off-Jensen.
- **R(tau) monotonicity on Jensen** (S64): dR/dtau >= 0 by AM-GM. a_2 diverges exponentially.
- **Odd SDW a_3=0** (S65): Three proofs. Theta-vacuum CC CLOSED.
- **Lambda_SA = Lambda_J** (S64): SA fixes Jacobson integration constant. 114-OOM gap real.
- **S[D_sc]>0 structural theorem** (S63): CC cannot vanish at self-consistent fixed point.
- **Vortex CC bound** (S65): max |delta log10(a_0/a_2)| = 0.05 OOM.

## J-Protection & Spectral Pairing

- **J-protection**: [J, D+phi+J*phi*J^{-1}]=0 exactly. Spectral pairing survives ALL inner fluctuations.
- **B/F spectral asymmetry = 0** (S65): No B/F decomposition on pure Riemannian triple.
- **eta(s)=0 identically** (S61): |eta/zeta|<87*eps_mach. J-symmetry forces +/- pairing.
- **Poincare duality** (S61): mu_CCM=[[0,1,1],[1,0,1],[1,1,0]], det=2. Non-degenerate.

## Fold & Jensen Geometry

- **Jensen saddle**: Hessian block-diag. U(2)-inv negative, U(2)-breaking positive.
- **B2 fold universality** (S33a): Eigenvalue min at tau~0.19 GLOBAL across all PW sectors. delta_tau=0.004.
- **Lie derivative monotonicity** (S33a): f(s)=B(s)/5 monotonically increasing all s>0.
- **R-saddle at fold** (S64): Signature (8+,27-) in 35D VP subspace. Round metric is R-maximum.
- **Anti-Jensen direction** (S64): Steepest R-decrease = expand SU(2), shrink C^2+U(1).
- **Connes distance isotropy at tau=0** (S46): d_F directions agree to 0.02%. At fold: anisotropy=1.110.
- **(1,1) adjoint Lipschitz softness** (S46): lambda_min^{Lip}=1.1134 at fold. SOFTEST sector.
- **Spectral moment decoupling** (S64): CC and NEC are independent spectral channels.

## Selection Rules & Coupling

- **Trap 1** (S34a): V(B1,B1)=0 EXACTLY all tau, all 8 generators. U(2) singlet.
- **B1 coupling**: V(B1,B3)=0 exact. V(B1,B2)>0 from C^2 ONLY (100%).
- **Trap 4**: V_eff(B_i,B_j)=0 (Schur). Broken by phi.
- **Trap 5**: V_ph(real reps)=0 (J-reality). Proof incomplete (gamma_9 issue). Numerical solid.
- **Strutinsky** (S33a): B2/B3/B1 = 46/37/17% of RPA curvature.

## Omega^1_D & Inner Fluctuations

- **Omega^1_D tau-independent** (S46): dim=342=173 linear + 169 quadratic at ALL tau.
- **Gram matrix PSD** (S46): Kinetic mass is Gram matrix. No kinetic tachyons for any Hermitian D.
- **Mixed grading** (S46): gamma_9 does NOT separate gauge/scalar. Continuous eigenvalues.
- **M_3(C) inner fluctuations ZERO** (S51): Only C+H sector generates nonzero fluctuations.
- **K_7 commutant propagation** (S51): [K_7,D_K]=0 => [K_7,p(D_K)]=0 for any analytic p.
- **PS gauge module PASS** (S63): All 9 PS generators in enlarged Omega^1_D(A_PS). 8/9 outside SM space.

## BdG & BCS Theorems

- **BdG both KILL gates PASS** (S35): Delta=C2*Delta^T*C2, [gamma_9,Delta]=0. KO-dim 6 preserved.
- **BdG twist obstruction** (S46): A_F diagonal in Nambu space. Twisted first-order reduces to untwisted. CLOSED.
- **Chirality non-cancellation** (S64): {gamma_9,dD_K/dtau}=0 => chiral pairs ADD.
- **Quadratic chiral trace zero** (S65): Tr(gamma_9 dD dD)=0 identically.
- **Fermi-surface lock** (S64): v^2(B2[0])=1/2 identically when eps=0.
- **J pins Goldstone** (S35): Real structure forces Delta_0 in R. U(1)->Z_2.
- **Heat kernel factorization** (S64): K_BdG(t)=exp(-Delta^2 t)*K_bare(t) to 2.2e-16.
- **Occupied-state cyclic cohomology** (S45): HC^0=C^3, K_0=Z^3. Nondegeneracy preserved. Index=0.

## Heat Kernel & Spectral Geometry

- **Gilkey identity** (S61): a_2/a_0=(5/12)*R exact to 1.33e-14%.
- **61/20 ratio theorem** (S44): a_2^bos/a_2^Dirac=61/20 exact, tau-independent.
- **Level spacing = Poisson** (S61): Per-sector <r>=0.469. Integrable, not GOE.
- **Weil positivity** (S61): Trivially satisfied for finite truncation (entire zeta). Vacuous.
- **BCS shell exactness** (S70): 8/992 truncation EXACT by representation theory (SU(3) singlet selection rule).
- **c_s^2 = 0** (S70): Product spectral triple factorization. D_K depends on g_K, not dg_K.

## Connes Distance

- **Lattice metric verified** (S54): d(i,i)=0, d(i,j)>0, symmetry, triangle (0 violations all tau). TRUE METRIC.
- **Exponential scaling** (S54): <d_D>=1.014*exp(3.651*tau). a(fold)/a(0)=2.117.
- **Commutator antisymmetry** (S54): [D,diag(f)] antisymmetric for symmetric D. Schur SDP required.
- **D_BCS monotone** (S55): d_BCS increasing all tau (46th closure). d_BCS/d_D~0.053, nearly constant.

## Inheritance-Kernel Universality (condensate sector)
- **chi annihilates whole M_3(C)** (S88 W3a): chi: C+H+M_3(C) -> M_2(C) (BdG corner). No nonzero *-hom M_3(C)->M_2(C) (simple algebra embeds injectively; needs dim>=3>2), so ker(chi)=M_3(C) ENTIRELY (center AND non-center). Color-singlet forcing V(q+,q-)=0 (D-2, S34/35) is the STRONGEST form: surviving condensate is color-singlet by kernel ANNIHILATION, not a mere selection rule. Cooper pairs carry K_7=+/-1/2.
- **Abelian-only EXTENDS to rank-4 Pati-Salam** (S97 W5-2, S97-Q10-1-PS-CONDENSATE PASS): A_K^PS = C + M_2(C)_L + M_2(C)_R + M_4(C). The (15)-adjoint of su(4) (rank 15, all traceless/non-central, verified machine-eps) is the canonical SU(4)->SU(3)_cxU(1)_{B-L} breaking channel -- non-abelian at the GROUP level. BUT iota^PS sends M_4(C)->0 ENTIRELY (rep-dim lemma: condensate target dim 2 < 4), so the (15)-adjoint is in ker(iota_*^PS); no non-abelian M_4(C) class survives inheritance. D-2 GENERALIZES; W3 abelian-only is ALGEBRA-INDEPENDENT within the AF-Wedderburn class.
- **General mechanism**: the color-singlet-forcing is a representation-theoretic UNIVERSAL: rank(condensate target = BdG corner) < rank(color summand) => the color summand is annihilated by ANY *-homomorphism. NOT an A_K accident. Verdict GENUINELY OPEN before compute (the inheritance question is distinct from bare SU(4) breaking group-theory); the dim-comparison closes it. The N-ality(adjoint)=0 grading (SU(4) triality analog t_4=(#boxes) mod 4) is a CONSISTENCY cross-check, not the forcing. Morphism-choice-INVARIANT (both LR-symmetric and left-only iota^PS annihilate M_4(C)) => no INFO/PRU on the M_4 sub-question. Strengthens registry §VII.AZ.OP-PROJ M_3(C)-Kernel Universality (Track A) on a SECOND higher-rank algebra. Q10 unaffected (stays closed); W3 scope does NOT narrow.

## §VII.CK D4 corrigendum -- center-character vs coset-shift (S116 W2-1, S116-W2-CK-STAGE2-VERIFY PASS)
- **t(R_X)=0 for ALL 8 su(3)_R generators** (2 Cartan + 6 root = adjoint (1,1); t(p,q)=(p-q) mod 3, t(1,1)=0). Machine-exact: zeta=omega*I_3 conjugation residual max||zeta X zeta^-1 - X||=8.06e-17; Sage-QQbar EXACT (zeta X zeta^-1 == X in Q(omega) for every gen). Nontrivial-grading contrast: fundamental vector t=1 (so t=0 is a real result, not a tautology).
- **LESSON (reusable for any adjoint-type-operator exclusion)**: a Z_3 center-character SELECTION RULE CANNOT exclude R_{E_alpha} from Omega^1_{D_K}(A_K), because t(R_{E_alpha})=0 EQUALS the t=0 of every A_K one-form -- the rule cannot distinguish them. The registry's "t(O)=+-1 != 0" was a MISLABEL: the +-1 is the COSET-SHIFT grading (how the root op permutes generation-SLOT triality {1,0,0}: off-diag diff +-1, 2==-1 mod 3), NOT the operator's center character. Two DIFFERENT gradings.
- **Single reconciled mechanism = commutant/Skolem-Noether LEG-MEMBERSHIP** (A_F-INDEPENDENT, L_max-INVARIANT): Peter-Weyl H=(+)V_pi(x)V_pi^*; Omega^1_{D_K}(A_K) subset of (+)B(V_(p,q))(x)1 (scalar on the mult/right leg). R_{E_alpha}=1(x)E_alpha^*, E_alpha^* traceless root op => NON-scalar on mult leg => in COMMUTANT (+)1(x)B(V^*), NOT (+)B(V)(x)1. Residual ||O-Pi_{B(V)(x)1}(O)||/||O||=1.000000 EXACT for R_{E_alpha} (extends W3-1 Cartan Y_R residual=1.0 to the off-diag root handle); L (left-reg) residual=0; [L,R]=0 machine-zero. SAME multiplicity-scalar wall as §VII.BL MAGNITUDE + §VII.CK D3. D4-external CLOSED-EXTERNAL-AS-A-COUPLING PRESERVED; genus {A_K-built U Casimir-graded U gamma9-traced U right-regular} COMPLETE for A_K-INTERNAL couplings. Corrigendum ready for mack; UNCONDITIONAL flip owed to DISJOINT-pair (lizzi x volovik) blind re-verify (connes EXCLUDED as adjudication author).

## Key Structural Identities
- Kosmann != inner fluctuations: K_a is 2nd order in Clifford, [D,f]=cl(df) is 1st order. BCS kernel is ADDITIONAL Lie group input beyond spectral triple.
- Modulus kinetic energy: E_kinetic ~ 57,480 at fold. Stiff-fluid (w=1) redshifts as a^{-6}.
- Vulnerability hierarchy: Turing 300x > RPA 38x(333x@D_phys) > W-32b 1.9-3.2x (under phi).

## Key Constants & Equations

- SA: S_b = Tr f(D^2/Lambda^2) ~ 2f_4 Lambda^4 a_0 + 2f_2 Lambda^2 a_2 + f_0 a_4
- GUT: g_1^2 = g_2^2 = (5/3)g_3^2 at Lambda (Paper 07/10)
- KK: g_1/g_2 = e^{-2s} (S17a). Weinberg: sin^2(theta_W) = 1/(1+e^{4s}).
- Classification: A = M_a(H)+M_{2a}(C), a=2 -> PS -> SM (Paper 12)
- KO-dim 6: AZ class BDI (T^2=+1), NOT DIII.
- gamma_F = gamma_PA x gamma_CHI (S11). D_can = M_Lie (S27).
- Connes papers: 07=spectral action, 10(CCM 2007)=SM coefficients, 14=survey, 15=entropy, 16=finite-density.
