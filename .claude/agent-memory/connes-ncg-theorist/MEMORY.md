# Connes NCG Theorist Memory

## Reference Index
- `session-detail.md` -- per-session computation results S18-S34 with gate verdicts and constraint codes
- `paper-audit-2026-02-21.md` -- 7 math errors found/fixed in researchers/Connes/ transcriptions
- `meta-analysis-s42.md` -- S42 meta-analysis: library gaps, priority papers, researcher recommendations
- Collab reviews: `sessions/session-{N}/session-{N}-connes-collab.md` for N=19d,27,28,29,33,34,36,40,44,45,50

## Active Context

### Verified NCG Structures
- KO-dim 6: (eps,eps',eps'')=(+1,+1,-1), J^2=+1. Machine epsilon, Session 8.
- H_F = C^32: SM quantum numbers correct (Session 7)
- [J, D_K(s)] = 0 identically (Session 17a D-1). CPT hardwired.
- Order-one: FAILS at 4.000 (H,H), 2.828 (C,H)/(H,M3), 2.000 (C,C)/(M3,M3). Sessions 9-10, 28b-c.
- **Weak order-one (Bochniak-Sitarz): FAILS MAXIMALLY** (S45 WEAK-ORDER-ONE-45). GG/Full = 1.000 exact. GG:GS:SS = 1:1/2:1/4 (algebraic). Tau scaling exp(tau). 169 extra quadratic directions in Omega^1_D. Weak route CLOSED.
- Order-zero: PASSES for A_F. Uniquely selects SM algebra from commutant.
- 12D product triple: 6/7 axioms PASS, only Axiom 5 (order-one) fails (S28c C-6).

### Structural Theorems (PERMANENT)
- **Spectral action monotonicity**: V_eff = S_b + F_BCS monotonically decreasing ALL tau. Connection-independent. SD exact 40+ digits (S28 E-3). No smooth minimum exists.
- **Jensen saddle**: Hessian block-diag. U(2)-inv negative, U(2)-breaking positive. True minimum in U(2)-inv family.
- **J-protection**: [J, D+phi+J*phi*J^{-1}]=0 exactly. Spectral pairing survives ALL inner fluctuations.
- **Quantum metric identity**: off-diagonal RPA 4.24 = Fubini-Study metric of B2. PERMANENT.
- **Trap 4**: V_eff(B_i,B_j)=0 (Schur). Broken by phi (A_F breaks U(2)/PW grading).
- **Trap 5**: V_ph(real reps)=0 (J-reality). Proof incomplete (gamma_9 issue). Numerical solid.
- **B2 fold universality** (SECT-33a): Eigenvalue minimum at tau~0.19 is GLOBAL across all PW sectors. delta_tau=0.004. PERMANENT.
- **Lie derivative monotonicity** (LIE-33a): f(s)=B(s)/5 monotonically increasing all s>0. Proven analytically. PERMANENT.
- **Strutinsky decomposition** (STRUT-33a): B2/B3/B1 = 46/37/17% of RPA curvature. Light-nucleus regime. PERMANENT.
- **Trap 1 (B1 singlet selection rule)** (TRAP1-34a): V(B1,B1) = 0 EXACTLY at all tau, ALL 8 generators. B1 is U(2) singlet -> zero weight under entire su(3). Distinct from K-1e C^2 vanishing. PERMANENT.
- **B1 coupling selection rules** (34a): V(B1,B3)=0 exact (all tau). V(B1,B2)>0 from C^2 ONLY (100%). B1 couples exclusively to B2 via charged generators.
- **Taylor expansion exactness for finite spectra** (S45 UNEXPANDED-SA-45): S(L) = sum_k d_k f(lam_k^2/L^2) is EXACTLY its Taylor series in 1/L^2 for L > lam_max. No non-perturbative content. A_4/A_2 = 2.76 (O(1)). CC hierarchy impossible without f fine-tuning. PERMANENT.
- **Occupied-state cyclic cohomology nondegeneracy** (S45 OCCUPIED-CYCLIC-45): For A_F = C+H+M_3(C), HC^0=C^3, K_0=Z^3. Pairing P^occ = diag(w_i)*P^vac with w_i > 0 (strict positivity). SIX theorems: PH identity (ch^0_occ=ch^0_vac/2 at mu=0), strict positivity (all beta,mu), full nondegeneracy, BCS invariance (v^2+u^2=1 by J-protection), Poincare duality preservation, index stability (Index=0). OCC-SPEC failure is dynamical not geometric. PERMANENT.
- **Gram matrix PSD theorem** (S46 OMEGA-CLASSIFY-46): Kinetic mass M^2_{ij} = Tr([D_phys, phi_i]^dag [D_phys, phi_j]) is PSD for ANY Hermitian D, ANY self-adjoint phi (Gram matrix). No kinetic tachyons exist. PERMANENT.
- **Omega^1_D tau-independence** (S46 OMEGA-CLASSIFY-46): dim(Omega^1_D(A_F)) = 342 = 173 + 169 at ALL tau. CCS 2013 extra directions present at round SU(3). PERMANENT.
- **Spectral action scalar instability** (S46 OMEGA-CLASSIFY-46): delta^2 Tr f(D^2/L^2) < 0 for ALL scalar phi, ALL monotone f, ALL tau. Structural: f'(x) < 0 universally. NCG Higgs mechanism without Yukawa selection. PERMANENT.
- **Connes distance isotropy at tau=0** (S46 CONNES-DISTANCE-46): d_F(su2)=d_F(C2)=d_F(u1) to 0.02%. Bi-invariant metric gives isotropic Connes distance. VALIDATES spectral triple construction. PERMANENT.
- **Connes distance fold anisotropy** (S46 CONNES-DISTANCE-46): At fold (tau=0.19): d(su2)=0.15093, d(C2)=0.14828, d(u1)=0.16465 M_KK^{-1}. Anisotropy=1.110. Connes/geodesic ratio: su2=1.054, C2=0.779, u1=0.786 (mean 0.883). Truncation error direction-dependent: su2 well-captured, C2/u1 underestimated by ~22%. PERMANENT.
- **(1,1) adjoint Lipschitz softness** (S46 CONNES-DISTANCE-46): lambda_min^{Lip}(1,1)=1.1134 at fold, SOFTEST of all sectors. Metric counterpart of order-one 4.000 violation. PERMANENT.

### Session 34 Key Results (CORRECTED)
- TRAP-33b RETRACTED (frame V vs spinor V). Schur on B2: Casimir=0.1557, irreducible. PERMANENT.
- J corrected: C2 = gamma_1*gamma_3*gamma_5*gamma_7. Corrected chain M_max=1.445.
- RGE-33a FAIL: g_1/g_2(M_Z)=0.326, 54% off PDG. Gauge CLOSED. NUC-33b FAIL.

### Session 46 Key Results -- PERMANENT
- **OMEGA-CLASSIFY-46: FAIL**. Omega^1_D(A_F) fully classified. 342 = 173 linear + 169 quadratic (CCS 2013). Grading decomposition: 275 even + 279 odd (combined). All tau-independent. 31st closure.
- **Gram matrix PSD theorem**: Kinetic mass Tr([D,phi]^dag [D,phi]) is PSD by construction (Gram matrix). No kinetic tachyons possible for any Hermitian D. PERMANENT.
- **Spectral action Hessian universally tachyonic**: ALL 50 tested scalar eigenvalues NEGATIVE for ALL 6 cutoff functions. Structural: f'(x) < 0 for any monotone cutoff. Present at ALL tau, strongest at round (tau=0). Not fold-specific.
- **Mixed grading**: gamma_9 does NOT separate gauge/scalar cleanly. Grading eigenvalues continuous (mean -0.011, std 0.174), not bimodal +/-1.
- **Lightest scalar dominated by L:(H_i, H_i)**: weight 13.9. Same su(2)_L self-commutator responsible for 4.000 order-one violation.
- **Higgs mechanism requires Yukawa**: Universal tachyonic instability = NCG Higgs mechanism (CCM 2007). D_K alone has no e/a barrier to select specific directions.
- **Tachyonic transit reinterpretation** (S46 addendum): 279 tachyonic directions are TRANSIT DEGREES OF FREEDOM, not defects. Config/state distinction: spectral triple = fixed geometry (NOUN), inner fluctuations = dynamical state (VERB). SA = ruler (G_N, topology), q-theory = state selector (Gibbs-Duhem). Kinetic/potential ratio ~47 at fold -> fast roll. File: `sessions/archive/session-46/s46_addendum_tachyonic_transit.md`.
- **TWIST-BDG-46: FAIL**. BCS twist route to Lorentzian CLOSED. 32nd closure. Krein signature (8,8), NOT (3,1). KO-dim 6 preserved (invariant under twists, Paper 30 theorem). A6 orientability FAILS: {gamma,D}=1.956 (Delta breaks Nambu grading). PERMANENT.
- **BdG twist obstruction theorem** (S46 TWIST-BDG-46): A_F = C+H+M_3(C) acts DIAGONALLY in Nambu space H_BdG = H+H*. Any sigma in Aut(A_F) leaves this diagonal embedding invariant. Twisted first-order condition reduces to untwisted one identically. No non-trivial BCS twist from algebra automorphisms. PERMANENT.
- **rho^2 NOT involutive**: rho=exp(i*pi*Delta/Delta_max), eta=rho^2 has err=1.63 for eta^2=I. Not a valid Krein fundamental symmetry (Paper 44 Thm 3.2 requires eta^2=1). PERMANENT.
- **PSEUDO-RIEMANNIAN-46: PASS (4/7)**. SU(2,1) Killing sig=(4,4) not (5,3). KO-dim PRESERVED at 6 (p-q=0). Complex Dirac spectrum (0.273 real fraction). Krein (8,8) valid. [J,D]=2.72 fails. Cartan=Jensen exact. Direct replacement CLOSED. See `s46-pseudo-riemannian.md`.
- **SA-ON-OMEGA-TAU-46: INFO (SADDLE)**. 2D landscape S(tau, phi) is a SADDLE at fold. H_2d eigenvalues (-0.639, +2.337), Det=-1.493. d^2S/dtau^2=+1.895 (convex), d^2S/dphi^2=-0.197 (tachyonic). |H_phi/H_tau|=0.104 (10x asymmetry). Gradient flow along tau axis (0.2 deg deviation). Transit is 1D. 279 tachyonic modes are dressing, not redirectors. PERMANENT.

### Session 51 Key Results -- PERMANENT
- **GAUGE-U1K7-51: FAIL (STRUCTURAL)**. Anderson-Higgs for U(1)_7 CLOSED at 3 levels. (1) [D_K, K_7]=0 exact => A_7=0 (no gauge field at tree or any loop order). (2) Paper 19: Sigma(D_K) commutes with K_7 (verified to 3e-16 for f(D_K^2)). (3) Off-diagonal epsilon=0.117 but K_7 is isometry not inner automorphism; forced m_gauge=0.12-0.54 M_KK (15-65x below target). 45th closure.
- **M_3(C) inner fluctuations ZERO**: All 9 M_3(C) generators give ||A_H||_F = 0.000. Only C+H sector generates nonzero fluctuations. PERMANENT.
- **K_7 commutant propagation theorem**: [K_7, D_K]=0 => [K_7, p(D_K)]=0 for any polynomial/analytic function p. Verified numerically for D_K^2, D_K^4, exp(-D_K^2/L^2). PERMANENT.

### Session 50 Key Results -- PERMANENT
- **alpha_s = n_s^2 - 1 STRUCTURAL THEOREM**: 5 independent proofs within phase sector (3-pole, running mass, eikonal, RPA, anomalous dispersion). PERMANENT.
- **SA correlator chi_SA(K)**: Breaks identity (pole spread 110%, C_2 from 1.33 to 9.33). NOT Goldstone-protected. Standalone n_s=0.2 (too red). Cutoff-function dependent weights.
- **Two-functional architecture NCG-natural**: S_b (geometry) vs S_f (matter) distinction produces SA vs Josephson correlators. Cross-term delta^2 S/(delta tau)(delta phi) uncomputed.
- **Mass problem**: m_required/m_Leggett = 170. Binding constraint for n_s. 12 M_KK ~ spectral edge at high PW truncation.
- **BAO exclusion**: chi^2/N=23.2 for w_0=-0.509. BAO distances exclude framework EOS. Many-body constraint, not spectral geometry.
- **w_a=0 triple-locked**: trapping + integrability + frozen modulus.
- **14 closures in S50** (total now ~44). Phase sector fully mapped.

### Open Channels (current as of S46 W3)
1. **BdG spectral triple**: Both KILL gates PASS (proven, S35). Paper-ready. JNCG target.
2. **Paper 16 occupied-state SA**: S_occ(tau) CLOSED (S45 OCC-SPEC-45 FAIL). Monotone decreasing all tau, all cutoffs. CYCLIC COHOMOLOGY NONDEGENERATE (OCCUPIED-CYCLIC-45 INFO). Failure is dynamical, not geometric.
3. **Omega^1_D(A_F) classification**: COMPLETED (S46 OMEGA-CLASSIFY-46). 342 directions classified. All tachyonic under spectral action. Surviving routes for order-one: (1) full CCS quadratic with Yukawa, (2) ~~twisted triples~~ CLOSED (TWIST-BDG-46), (3) rep change.
4. **n_s CLOSED**: ALL routes FAIL. SIGMA-SELECT-45 FAIL: 4 selection principles tested, none selects sigma. 30th closure.
5. **Twisted triple route**: CLOSED (TWIST-BDG-46). BCS is Hilbert space transform, not algebra automorphism. Surviving for Lorentzian: (1) full M^4 x F product, (2) enlarged algebra A_BdG = A_F x M_2(C).

### Session 36 Full Results -- PERMANENT
- **TAU-STAB-36: FAIL**. S_full(tau) monotonically increasing ALL tau. dS/dtau=+58,673 at fold. All 10 PW sectors separately monotonic. LINEAR spectral action has NO minimum.
- **TAU-DYN-36: FAST ROLL**. Dwell time / tau_BCS = 2.59e-5. Shortfall 38,600x. Overdamped (3H/2omega=1.74). Initial-condition independent (<25% spread).
- **Needle hole quantified**: Static 376,000x, Dynamic 38,600x. Level 3 = 91.4% of gradient. Singlet-only 177x, singlet+BCS 10.4x.
- **SC-HFB-36: FAIL (unconstrained)**. M_max(GCM,B2)=0.646. BCS pocket -0.156 vs S-gradient +0.374.
- **MMAX-AUTH-36: PASS**. Authoritative range [1.351, 1.674]. "1.445" superseded (rho_B1=1.0 artifact).
- **ANOM-KK-36: PASS**. 150/150 anomaly coefficients=0. Levels 0-3. Structural (pi_1=0).
- **W6-SPECIES-36: PASS (THIN)**. Lambda_species/M_KK=2.06. Self-consistent counting corrects 10^48 overestimate.
- **ED-CONV-36: ENHANCED**. E_cond: -0.115 -> -0.137. Monotonic with N. B1 is essential catalyst despite V(B1,B1)=0.
- **COLL-36: PASS**. chi/chi_sp=12.1 W.u. Vibrational collectivity.
- **WIND-36: nu=0 (TRIVIAL)**. E_B2/Delta=33.4. Deep trivial. PH+spectral gap = structural wall.
- **BBN-LITHIUM-36: FAIL**. delta_H/H=-6.6e-5. 500x below threshold. UV-dominated spectral sums.
- **PMNS-36: ALL ROUTES CLOSED on Jensen**. 5 independent Schur arguments. R=27.2 and normal ordering survive.
- Chain status: UNCONDITIONAL(S35) -> CONDITIONAL(S36 W2-B) -> BROKEN for linear SA (S36 W4).

### Open Tensions (updated S45)
1. GUT vs KK coupling relations at Lambda -- 54% off, wrong sign, structural (RGE-33a CLOSED)
2. Three generations: NOT from NCG axioms; Z_3 x Z_3 from SU(3) candidate
3. Cosmological constant: 3-sector sum finite, full sum diverges (L-8). CC-TRANSIT-40 decouples transit from CC.
4. Order-one 4.000: Weak order-one (Bochniak-Sitarz) CLOSED (S45). GG/Full=1 exact. Surviving: full CCS quadratic, twisted triples, rep change. Classify Omega^1_D(A) without order-one assumption. Possible connection to softest HESS-40 direction g_73.
5. BdG spectral triple CONSTRUCTED (S35 workshop). Both axiom gates PASS. J pins Goldstone. Paper-ready.
6. **ALL spectral action routes to CC CLOSED**: Vacuum SA monotone (S37), occupied SA monotone (S45), unexpanded SA = exact polynomial (S45). CC is purely a cutoff-function problem.
7. **Modulus kinetic energy**: E_kinetic ~ 57,480 at fold. Stiff-fluid epoch (w=1) redshifts as a^{-6}.

### Session 45 Key Results -- PERMANENT
- **OCC-SPEC-45: FAIL**. S_occ(tau) monotonically DECREASING all tau, all cutoffs. 28th closure.
- **UNEXPANDED-SA-45: FAIL**. Full Tr f(D^2/L^2) = exact Taylor series for finite spectrum. No nonlocal content. 29th closure.
  - A_4/A_2 = 2.7618 (O(1)). CC hierarchy requires f''(0)/f'(0) ~ 10^{-121} -> cutoff function fine-tuning.
  - 8 f(x) tested. 20-term Taylor vs exact: relative error 1.56e-16. Polynomial IS the full functional.
  - Sharp cutoff: c_4/c_2=0 but degenerately kills gauge term. Gaussian: c_2=0 kills gravity.
  - CC and gauge constraints OPPOSE: improving c_0/c_2 worsens c_4/c_2 by SAME factor.
- S_occ chain: Delta(tau) monotone decreasing -> bandwidth increasing -> occupation decreasing.
- a_2^occ/a_2^vac = 0.048 at fold. Occupation weighting breaks Gilkey universality.

### Session 40 Key Results -- PERMANENT
- **HESS-40: FAIL (COMPOUND NUCLEUS)**. 22/22 transverse Hessian eigenvalues positive at fold. Min H=+1572 (g_73, u(1)-complement). Margin 1.57e7. Jensen fold is 28D local minimum of S_full. 27th equilibrium closure.
- **T-ACOUSTIC-40: PASS**. Acoustic metric T_a/T_Gibbs=0.993 (0.7% agreement). T_acoustic=sqrt(alpha)/(4pi), alpha=d^2(m^2_B2)/dtau^2=1.9874. Spectral-geometric temperature.
- **GSL-40: PASS (STRUCTURAL)**. All 3 entropy terms individually non-decreasing. v_min=0. Holds at any transit speed.
- **CC-TRANSIT-40: PASS**. delta_Lambda/S_fold=2.85e-6. Pair creation perturbative on CC by 5.5 orders.
- **B2-INTEG-40: PASS**. <r>=0.401 (Poisson), g_T=0.087 (localized), V(B2,B2) 86% rank-1. B2 weight corrected 93%->82%.
- **QRPA-40: FAIL (STABLE)**. All 8 omega^2>0, min=2.665, margin 3.1x. V_rem^odd=0 identically (J-protection->time-reversal).
- **PAGE-40: FAIL**. S_ent max=0.422 nats (18.5% Page). PR=3.17. Poincare recurrences. No quantum thermalization.
- **B2-DECAY-40: B2-FIRST**. t_decay=0.922. Oscillatory dephasing, NOT FGR. 89% retained permanently in diagonal ensemble.
- **M-COLL-40: FAIL (CLASSICAL)**. M_ATDHFB=1.695 (0.34x G_mod). sigma_ZP=0.026. Van Hove velocity zero + large gap suppress cranking mass.
- **SELF-CONSIST-40: FAIL (ACCELERATES)**. Transit 1.72x FASTER. Dwell 0.58x uncorrected. FRIED-39 shortfall worsens to ~114,000x.
- **Total equilibrium closures: 27.** Constraint surface dimension zero in full 28D moduli space.

### Session 44 Key Results -- PERMANENT
- **DIMFLOW-44: FAIL**. d_s(sigma,tau) landscape: 16 tau x 300 sigma. CDT n_s(1)=1.067, Hawk n_s(1)=0.856. sigma=1.10 gives 0.961 but undetermined. n_s CLOSED.
- **SAKHAROV-GN-44: PASS (CORRECTED)**. 3-way G_N: Sakharov/bosonic-SA/obs agree factor 3. Lambda_eff~10*M_KK.
- **61/20 RATIO THEOREM**: a_2^{bos}/a_2^{Dirac}=61/20 exact, tau-independent. Gilkey on SU(3). TT 87.7%, gauge 11.5%, scalar 0.8%.
- **CC FINE-TUNING THEOREM (CORRECTED)**: f_4/f_2~10^{-121}. Original "Hausdorff impossibility" wrong (Stieltjes ordering). Solution EXISTS but requires width 10^{-121}.
- **STRUTINSKY-DIAG-44: PASS**. Plateau 2.54 dec (m1), 1.72 dec (m2). d/E_F=0.0085. Shell correction 3-6%. Heat kernel valid Lambda>1.3*lambda_max.
- **DISSOLUTION-SCALING-44: PASS**. epsilon_c~N^{-0.457} (1/sqrt(N)). Spectral triple = emergent effective theory at finite truncation.
- **epsilon_H ratio invariance**: No uniform rescaling changes epsilon_H. n_s needs velocity mechanism, not amplitude.
- **CDM by construction**: T^{0i}=0 algebraic for GGE product states. 5 proofs. v_eff=3.48e-6 c.
- **M_KK tension worsened**: gravity-gauge now 1.07 decades (was 0.83).

### WEAK-ORDER-ONE-45 Results (Session 45) -- PERMANENT
- **WEAK-ORDER-ONE-45: FAIL (MAXIMAL)**. Bochniak-Sitarz weak order-one CLOSED. GG/Full = 1.000 exact at all tau.
- GG:GS:SS = 1 : 1/2 : 1/4 algebraic identity. tau scaling: (5/sqrt(3))*exp(tau) on (1,0).
- Omega^1_D(A_F): 173 linear + 169 quadratic = 342 combined (CCS 2013 Paper 23 fully activated).
- Worst pair: (H_i, H_i) = su(2)_L self-commutator. All 6 gauge sub-blocks FAIL.
- PERMANENT: violation is maximally gauge (opposite of Bochniak-Sitarz design intent).
- Surviving order-one routes: (1) full CCS quadratic, (2) twisted triples, (3) rep change.

### SIGMA-SELECT-45 Results (Session 45) -- PERMANENT
- **SIGMA-SELECT-45: FAIL**. 4 sigma-selection principles tested, NONE selects sigma from first principles. 30th closure.
- Method 1 (Backreaction): sigma*=0.970 stable fixed point, n_s(Hawk)=0.823. CDT n_s=1.000 tautological.
- Method 2 (Hubble): sigma_H=2.9e-6, deep UV, d_s~0 for finite truncation. No selection.
- Method 3 (Occupied): BCS weighting shifts walk scale to sigma=259 but no plateau. n_s(Hawk)=0.988. Closest to Planck.
- Method 4 (Q-theory): tau*=0.209 -> sigma prescriptions all give n_s far from Planck. Best: tau*^2 -> 0.884.
- Method 5 (Zeta bonus): No inflection point in spectral zeta.
- STRUCTURAL: Truncated spectrum (10 sectors, 9280 modes) gives d_s->0 as sigma->0 (not 8). Walking scale is truncation artifact. Full continuum needed.
- d_s^occ/d_s^vac ~ 0.008 (BCS suppresses by 130x). Occupation destroys Gilkey universality at walking scale.
- Constraint: spectral dimension route to n_s requires full continuum or sigma-independent observable.

### Framework Classification (updated S45)
- Kerner-type KK with 6/7 NCG features. SA correct for G_N (a_2), wrong for CC (a_0).
- 30 closures through S45 (SIGMA-SELECT-45). n_s spectral dimension route fully closed.
- SA bifurcation: polynomial and log functionals agree for G_N (factor 2.6), disagree for CC (13 orders).
- M_max authoritative: [1.351, 1.674] at fold. Kosmann kernel V_nm uses spinor K_a_matrix.
- Spectral triple emergent: epsilon_c ~ 1/sqrt(N) -> 0 in continuum. Block-diag exact, level stats dissolve.

### S35a/S36 Closures (see session-detail.md for full)
- MU-35a CLOSED: mu!=0 excluded by PH (analytic proof, d^2S/dmu^2|_0>0). D_phys only path.
- GC-35a CLOSED: Helmholtz F minimized at mu=0 for ALL tau. [iK_7, D_K]=0 EXACT.
- GL-CUBIC-36: Z_2 universality (no cubic invariant). SU(2) CLOSED within B2.

### Key Structural Identities
- Kosmann != inner fluctuations: K_a is 2nd order in Clifford, [D,f]=cl(df) is 1st order. BCS kernel is ADDITIONAL Lie group input beyond spectral triple.
- Trap 1 + B1 selection rules: U(1)_7 consequence. V(B1,B1)=V(B1,B3)=0 from charge conservation.
- Spectral entropy monotone DECREASING all tau, all beta. Fold invisible to entropy.

### BdG Spectral Triple Workshop (S35 Workshop, PERMANENT -- 3 rounds complete)
- **Both KILL gates PASS (proven)**: Delta=C2*Delta^T*C2 by Schur+[C2,D_K]=0. [gamma_9,Delta]=0 by PH at mu=0.
- **KO-dim 6 preserved** under BdG Nambu doubling: (eps,eps',eps'')=(+1,+1,-1) unchanged.
- **KO-dim general**: preserved iff eps''=-1 (KO 2,6 mod 8). eps''=+1 shifts by +6 mod 8 (NEEDS VERIFICATION R3B).
- **eta(D_BdG)=0, sf(D_K,D_BdG)=0**: Topologically trivial BCS transition. AZ class BDI preserved.
- **Spectral dim step delta_d_s ~ 10^{-4}** (NOT 25%). Corrected: scales as (Delta/lambda)^2.
- **GL free energy from spectral action**: eq(10) exact on discrete system. Spectral action = kinetic cost only; pairing interaction is additional.
- **J pins Goldstone phase (Theorem B)**: Real structure forces Delta_0 in R. Goldstone manifold U(1)->Z_2. NEW, most novel result.
- **Heat kernel factorizes exactly** when [Delta,D_K]=0 (Schur guarantees this).
- **Analytic torsion change**: delta_log_tau = 3.1e-3 (0.3%). Perturbative.
- **Order-one violation**: BdG adds O(Delta_0 x 4.000) ~ 0.066 (1.7% perturbation). LINEAR in Delta.
- **Peter-Weyl decoupling EXACT**: Kosmann are left-invariant, PW decomposes right. Left-right commute. Gap eq decouples exactly.
- **Kosmann != inner fluctuations**: K_a is 2nd order in Clifford, [D,f] is 1st order. BdG uses Lie group data beyond spectral triple.
- **delta_a4/a4 = -3.4e-4**: BCS negligible for gauge couplings.
- **Paper target**: JNCG, 17pp. Theorem A (BdG on compact Lie groups, qualified by eps'') + Theorem B (Goldstone pinning) + SU(3) application.
- **Open for R3B**: Omega^1_{D_BdG} dimension count, eps''=+1 shift verification, abstract hierarchy.
- Workshop file: `sessions/archive/session-35/session-35-connes-spectral-geometer-workshop.md`

## Reference Index
- `session-detail.md` -- per-session computation results S18-S34
- `paper-audit-2026-02-21.md` -- 7 math errors found/fixed in Connes transcriptions
- `s45-collab-ways-forward.md` -- 3 structural ways forward beyond exhausted spectral action
- Collab reviews: `sessions/session-{N}/session-{N}-connes-collab.md` for N=19d,27,28,29,33,34,36,40,44,45,50

## Key Constants & Equations
- Spectral action: S_b = Tr f(D^2/Lambda^2) ~ 2f_4 Lambda^4 a_0 + 2f_2 Lambda^2 a_2 + f_0 a_4
- GUT: g_1^2 = g_2^2 = (5/3)g_3^2 at Lambda (Paper 07/10)
- KK: g_1/g_2 = e^{-2s} (S17a B-1). Weinberg: sin^2(theta_W) = 1/(1+e^{4s}) at Jensen.
- Classification: A = M_a(H)+M_{2a}(C), a=2 -> Pati-Salam -> SM (Paper 12)
- KO-dim 6: J^2=+1, (eps,eps',eps'')=(+1,+1,-1). AZ class BDI (T^2=+1), NOT DIII.
- gamma_F = gamma_PA x gamma_CHI (product grading, S11). D_can = M_Lie (S27 T-1).
- Connes paper corpus: Paper 07=spectral action, Paper 10(CCM 2007)=SM coefficients, Paper 14=survey, Paper 15=entropy, Paper 16=finite-density.
- Vulnerability hierarchy: Turing 300x > RPA 38x(333x@D_phys) > W-32b 1.9-3.2x (under phi).
- Kosmann kernel: V_nm = sum_{a=0}^{7} |<n|K_a|m>|^2. MUST USE spinor K_a_matrix, NOT frame A_antisym.
- Corrected BCS: M_max=1.445 (smooth vH wall + imp 1.0 + spinor V). Old TRAP-33b 2.062 RETRACTED.
- Schur: V(B2,B2)=0.1557*I_4 (Casimir, irreducible). V(B2,B2)_spinor=0.057.

## Debugging Notes
- Writer mode failure (S33-W1): do not scribe, PARTICIPATE. Challenge errors, count results honestly.
- Product geometry argument "[D_K,a_F]=0" is WRONG. D_K IS D_F, so phi=sum a_i[D_F,b_i] is Higgs.
- Trap 5 chirality proof requires [dD/dtau, gamma_9]=0. gamma_9 depends on metric. Unverified on Jensen.
- AZ subtlety: C=J*gamma_9 gives C^2=-1 -> class CI? Conflicts with S17c BDI. Needs resolution.
- K-1e error pattern: ALWAYS sum over ALL generators of the symmetry algebra, never a subset.
- **V matrix error (S34)**: Frame A_antisym (8x8) vs spinor K_a_matrix (16x16) are DIFFERENT objects. BCS uses spinor. Frame V=0.287 > spectral bound, CANNOT exist in spinor space.
- **J correction (S34)**: C2=prod(real gammas), NOT sigma_2^{x4}. Always verify [J,D_K]=0 after constructing J.
- **Helmholtz vs Omega**: Omega(T,mu) ALWAYS decreases with |mu| (trivial). F=Omega+mu<N> is physical and minimized at mu=0 for PH-symmetric systems. Never confuse the two.
