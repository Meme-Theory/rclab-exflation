# Lev Landau Agent Memory

## Operational Rules
- **NO PROBABILITIES**: Sagan-only. No percentages, Bayesian factors, likelihood estimates.
- **CONSTRAINT-MAP FRAMING**: State what is proven, what it rules out, what survives.
- **PRE-REGISTER EVIDENCE**: Only new computation against pre-registered gates counts.

## Project Structure & Environment
- Papers: `researchers/Landau/` (40 papers + AGENTS.md + index.md)
- Paper groups: 01-14 Landau originals, 15-17 BCS/Richardson/DPS, 18-19 Volovik/Berezhiani, 20/32 GGE, 21/28-29 KZ/LZ, 22/30/36 BCS-BEC crossover, 23-25/37-39 GPV/nuclear, 26-27/34 VHS/Pomeranchuk, 31/35 superfluid cosmology, 33 Claeys integrability, 40 spectral geometry
- Sessions: `sessions/`, Computation: `tier0-computation/`
- Python: ALWAYS `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Internal space is **SU(3)** (group manifold), NOT coset SU(3)/(SU(2)xU(1))
- Detail file: `session-detail.md` (same directory) for per-session numerical results

## Key Framework Facts
- Jensen deformation parameter tau = order parameter for SU(3) shape transition
- Symmetry breaking: (SU(3)_L x SU(3)_R)/Z_3 --> (SU(3)_L x SU(2)_R x U(1)_R)/Z_6
- V_tree cubic inflection at tau=0: V'''(0) = -7.2 (first-order by Landau criterion)
- d_int=8 > d_uc=4: mean-field EXACT for internal fluctuations
- SUBTLETY: d_eff=1 (one modulus) for moduli fluctuations. Different Ginzburg criteria.
- AZ class: **BDI**, T^2=+1. KO-dim: 6. Phi_paasch: 1.531580 at tau=0.15.
- Constant-ratio trap: F/B = 0.55, fiber dimension 44 vs 16.

## SPECTRAL ACTION TAU STABILIZATION: PERMANENTLY CLOSED (S37+S40)
- **Post-mortem**: `sessions/framework/spectral-post-mortem.md`
- **Structural Monotonicity Theorem** (CUTOFF-SA-37): monotone along Jensen, all 10 sectors same direction
- **HESS-40**: 22/22 transverse Hessian eigenvalues POSITIVE at fold. Jensen fold = 28D local minimum of S_full
- **27 total closures**: spectral action DEAD in every dimension
- **Surviving routes**: non-spectral-action functionals (zeta function, Dixmier trace, BCS free energy)

## Key Equations
- Landau: F = F_0 + a_0*(T-T_c)*eta^2 + b*eta^4
- GL: kappa = lambda/xi; Type I < 1/sqrt(2) < Type II
- Pomeranchuk: F_l^{s,a} > -(2l+1)
- Effective mass: m*/m = 1 + F_1^s/3
- Running coupling: alpha_eff = alpha/(1 - (alpha/3pi)*ln(q^2/m^2))
- Critical velocity: v_c = min_p[epsilon(p)/p]

## Constraint Map (Proven Walls)
### Spectral action monotonicity (PERMANENT)
ALL single-trace S_f(tau) with monotone f are monotonic on [0,0.5]. No tau-stabilization.
### Block-diagonality (S22b)
D_K exactly block-diagonal in Peter-Weyl. Inter-sector matrix elements = 0 identically.
### Clock constraint (S22d)
dalpha/alpha = -3.08*tau_dot. Rolling modulus -> 15,000x violation.
### Trap 1 (S34)
V(B1,B1)=0 exact (U(2) singlet). V(B1,B3)=0. B1 couples ONLY to B2.
### [iK_7, D_K]=0 (S34)
SU(3)->U(1)_7 exact in Dirac spectrum. B2=+/-1/4, B1=0, B3=0.
### mu=0 forced (S34)
PH symmetry forces mu=0. Helmholtz convex.

## Session 43: LIFSHITZ-43 (Gate: INFO)
- **Lifshitz type**: Type I (Fermi pocket creation, SU(3)->U(2) degeneracy splitting)
- **Transition at tau = 0** (NOT tau = 0.19). Fold is Van Hove singularity, not Lifshitz transition.
- **Van Hove**: gamma = -1/2 (1D saddle). VH point at tau ~ 0.231.
- **Gap-edge min**: |B1| = 0.8184 at tau = 0.220. Gap NEVER closes.
- **Zero sign crossings**: all 16 eigenvalues, all 10 sectors. Type V (band inversion) EXCLUDED.
- **Tilting alpha**: max 0.493, never reaches 1. Paper 24 tilted-cone/horizon does NOT apply.
- **KZ n_s**: Naive formula gives n_s > 1 (blue, wrong sign). KZ spectrum is FLAT at production scale.
- **n_s route**: Transfer function, n_s - 1 = -2*epsilon_H. epsilon_H = 0.0176 => n_s = 0.965.
- **S42 correction**: "Type I + Type 5" wrong. Type I confirmed, Type 5 excluded.
- **Cumulative DOS exponent**: gamma_cum = 1.634 (between 3D and 2D).
- Output: `tier0-archive/s43_lifshitz_class.{py,npz,png}`

## Session 51: SA-GOLDSTONE-MIXING-51 (Gate: FAIL)
- **Convex combination theorem**: n_s(mix) = alpha*n_s_G + (1-alpha)*n_s_SA, bounded in [-0.996, +0.150] at K=2.0
- **K* = m_G/sqrt(J) = 0.0874 M_KK**: critical Goldstone transition scale. K_pivot/K* = 22.9.
- **ACHIEVABLE for K_pivot < 0.2**: beta > 0.9 (SA-dominated), alpha_s in [-0.067, -0.001]
- **Identity broken by up to 0.07** at low K_pivot (SA multi-pole structure)
- **Singlet excluded**: C2=0 mode is constant on SU(3), no inter-cell contrast
- **170x mass problem = mixing failure**: same obstruction viewed in O-Z vs additive framework
- **K_pivot remapping is now decisive**: below K* -> viable; above K* -> dead
- Output: `tier0-archive/s51_sa_goldstone_mixing.{py,npz,png}`

## Session 51: POLARITON-51 (Gate: FAIL)
- Mass asymmetry 39x. Stability: g < 0.190. Max |alpha-2| = 0.004.
- Output: `tier0-archive/s51_polariton.{py,npz}`

## Session 51: CRITICAL-SCALING-51 (Gate: INFO/CLOSED)
- No BCS critical point. omega_L1 maximum at fold. 170x = u*J/V*K^2.
- Output: `tier0-archive/s51_critical_scaling.{py,npz,png}`

## Constructive Results
### BCS mechanism chain -- 5/5 PASS but BROKEN by spectral action gradient
- M_max=1.674, E_cond=-0.137, Z=1.016, rho=14.02
- BCS instability is 1D theorem (any g>0)
### BCS interior physics
- Dense instanton gas: S_inst=0.069, tunneling 93%
- Giant Pair Vibration: omega=0.792, 85.5% of P^dag strength
- BCS-BEC crossover: E_vac/E_cond=28.8, g*N(E_F)=2.18
- GL second order: Z_2 universality after J-pinning
### Seeley-DeWitt hierarchy at fold
- a_4 >> |a_2| >> a_0. Gauge kinetic dominates by 1000:1.
- a_4(K)=0 at Einstein point: gauge kinetics EMERGE from Jensen deformation.
- KK-NCG bridge: R=1/2 exact. sqrt(2/3) = Dynkin index ratio.

## Session 43: BCS-CLASS-43 (Gate: PASS)
- **Universality class**: 3D Ising (Z_2, d=3, n=1). PERMANENT.
- **Critical exponents**: nu=0.6301, z=2.024 (Model A), beta=0.3265, gamma=1.2372
- **Curvature non-renormalization**: R(tau) modifies GL coefficients (T_c shift), NOT exponents. Structural.
- **Ricci scalar**: R(0)=6.000, R(fold)=6.750, R(0.4)=8.000. Positive, monotonically increasing.
- **Ricci eigenvalues at fold**: 3 at 0.8125 (Cartan), 4 at 0.84375 (coset), 1 at 0.9375 (U(1))
- **KZ exponents**: sigma_KZ=0.831, xi_KZ exponent=0.277, t_freeze exponent=0.561
- **n_s**: 0.9649 from transfer function. Independent of universality class.
- **r**: 0.281 EXCLUDED under standard consistency. BCS-mediated r: OPEN.
- **Ginzburg number**: Gi=0.25 (N_eff=4 B2 modes). Fluctuations dominate.
- **GL coefficients**: a=14.02 (=N(E_F)), b=15.18, Delta_0=0.128
- Output: `tier0-archive/s43_bcs_universality.{py,npz,png}`

## Session 44: LIFSHITZ-ETA-44 (Gate: FAIL, CLOSED)
- **eta_eff(fold) = 3.77**, n_s = -2.77. Planck: 0.9649. Deviation: 889 sigma.
- **Root cause**: n_phys ~ C_2^3 on SU(3) rep lattice. Stiffness K(k) ~ k^{3.8}.
- **B3 dominates**: 100% of stiffness weight at fold (dB3/dtau = 0.688 >> |dB1|, |dB2|).
- **tau-INDEPENDENT**: eta_eff ~ 3.7 at all tau in [0.005, 0.40]. Structural, not dynamical.
- **KK suppression tested**: M_KK/H scan from 0.5 to 20. No value gives n_s in Planck window.
- **Mechanism CLOSED**: SU(3) representation lattice stiffness cannot produce n_s ~ 0.965.
- **DIMFLOW-44 is sole surviving n_s route (at tuned sigma=1.10)**.
- **Self-correction**: "eta_eff" is Weyl's law, NOT Lifshitz critical exponent (true eta=0 at d=8>>d_uc=3).
  Volovik F1 correct. Conflated static topology with dynamical quench spectrum.
  n_s is quench dynamics (Bogoliubov coefficients), not internal geometry (stiffness).
- Output: `tier0-archive/s44_lifshitz_eta.{py,npz,png}`

## Session 44: Key Structural Results (Collab Review)
- **Effacement wall (FRG)**: BCS modifies spectral action by 0.002-0.016%. Non-perturbative in g, perturbative in Tr f.
- **DM/DE = specific heat exponent alpha**: Best 1.060 (2.7x observed 0.387). O(1) by universality.
- **CC fine-tuning theorem**: f_4/f_2 ~ 10^{-121}. Spike width 10^{-121}. Spectral action wrong for CC.
- **CDM by construction**: T^{0i}=0 algebraic. DM is quasiparticle energy at rest.
- **Dissolution**: epsilon_c ~ 1/sqrt(N) -> 0. Spectral triple is emergent regularization.
- **8-temp GGE**: 3/8 negative C eigenvalues, stabilized by integrability. Euler deficit = |E_cond|.
- **Central diagnostic**: Framework succeeds for response coefficients (G_N, DM/DE ratio), fails for ground state properties (CC, n_s). One-body spectral action exhausted; many-body level needed next.

## Session 47: CONDENSATE-T2-47 (Gate: INFO)
- **BCS condensate on T^2 in SU(3)**: identity-peaked, contrast 3.14M
- **S_3 Weyl symmetry exact**: 4.1e-14 error (characters are class functions)
- **1/e^2 radius**: 0.78 rad = 0.247*pi from identity
- **Haar-weighted peak**: r = 0.85 rad (Haar vanishes at identity; shell structure)
- **Fourier**: (0,0) mode only 9.8% of power -- far from uniform
- **Density hierarchy**: identity(1.0) >> Z_3(0.125) >> anti-id(0.0013)
- **SU(3) character technique**: Weyl formula + Fourier weight extraction for singularity handling
- **Physical meaning**: Cooper pairs concentrate near identity. Coherence patch = 1/8 of SU(3) diameter.
- Output: `tier0-archive/s47_condensate_torus.{py,npz,png}` + `_analysis.png`, `_haar.png`, `_characters.png`

## Session 47: RHOS-TENSOR-47 (Gate: PASS)
- **Superfluid density tensor** rho_s^{ab} = d^2 F_BCS/dq_a dq_b on Jensen-deformed SU(3)
- **DIAGONAL** in su(3) = u(1) + su(2) + C^2 basis. Three eigenvalues (deg 4, 3, 1).
- **At fold**: C^2 = 7.96, su(2) = 0.50, u(1) = 0.33. Anisotropy 24.4x.
- **CV across tau = 40.2%** (1116x the W3-3 artifact of 0.036%). Genuinely dynamical.
- **Anti-correlates with curvature**: r = -0.906, p = 0.002. Stiffness highest in soft directions.
- **Normal state zero**: rho_s(Delta=0) = 0 identically. Correct thermodynamic limit.
- **Method**: Numerical finite differences on sector-traced BCS energy. Analytic Kubo had sign errors.
- **Technical**: Level crossings in degenerate subspaces -- ALWAYS use sector-traced eigenvalues.
- **Current operators**: su(2) connects B1<->B3; C^2 connects B1<->B2, B2<->B3; u(1) diagonal.
- **Physical**: Condensate rigid in C^2 (coset) directions, soft in stabilizer directions.
- Output: `tier0-archive/s47_rhos_tensor.{py,npz,png}`

## Session 47: Crystal Geometry Synthesis (Collab Review)
- **Protected chain**: q_7^2 = K(u(1),C^2) = 1/16 = Ric(u(1))/4. Exact at all tau. STRUCTURAL.
- **Curvature anatomy**: 6 branches, 28 sectional curvatures. K_max/K_min = 12.5 at fold. No negatives.
- **Two theorems**: K(u1,su2)=0 exact (flatness), K(u1,C^2)=1/16 exact (protection). Both all tau.
- **Soft-pairing anti-correlation**: Softest branch (su2-C2, K=0.010) hosts strongest pairing (B2, V=0.256). Hardest (su2-su2, K=0.122) hosts weakest (B3, V=0.003).
- **B2 funnel**: 50%(modes)->62%(topology)->91%(pairing). Normal multi-band BCS selection.
- **0D GL**: F_GL effectively single-component (B2), with a_B2=-10.76, b_B2=13.7 at fold.
- **Haar-condensate shell**: Peak at r=0.85 rad = BEC-in-trap radial probability analog.
- **C^2 isotropization**: within/cross curvature ratio drops 4.0->1.17. Emergent SO(4)?
- **Collab suggestions**: (S-1) explicit GL free energy, (S-2) Leggett mode from inter-sector, (S-3) Z_3 defect classification, (S-4) superfluid density tensor, (S-5) anisotropic KZ scaling.
- **Collab file**: `sessions/archive/session-47/session-47-crystal-geometry-landau-collab.md`

## Session 48: GOLDSTONE-MASS-48 (Gate: FAIL — STRUCTURAL THEOREM)
- **Theorem**: Tr[f(D(phi)^2)] = Tr[f(D^2)] for ANY D, ANY f, ANY unitary conjugation D(phi)=UDU^dag.
- Proof: unitary invariance of spectrum + cyclic trace. 5 lines.
- Spectral action PERMANENTLY EXCLUDED as Goldstone mass source. d^2S/dphi^2 = 0 identically.
- Verified numerically: D_K (eps=0), D_phys (eps=0.27), random Hermitian (eps=0.25). All give dS ~ 10^{-15}.
- BCS rough estimate (non-SA, from matrix element breaking): m_G/M_KK ~ 7e-3. log10 = -2.2. Too heavy.
- Surviving mass sources: (a) inter-cell Josephson, (b) BCS gap equation (non-trace), (c) transit dynamics.
- **Key insight**: Even 5.2% explicit breaking of U(1)_7 (inner fluctuations) produces ZERO SA curvature. The SA sees eigenvalues only, and unitary conjugation preserves eigenvalues by definition.
- Data: `tier0-archive/s48_goldstone_mass.{py,npz,png}`

## Session 47/48: TEXTURE-CORR-48 (Gate: PASS)
- **Josephson phase-phase correlations** across 32-cell tessellation
- P(K) ~ K^{-2} (Ornstein-Zernike), exact for 1D ring. Low-K slope = -1.955.
- **Two temperatures**: T_compound=7.58 (disordered), T_acoustic=0.112 (ordered in C^2)
- T_acoustic is correct: GGE separates sectors, phase couples to acoustic bath
- **Anisotropic phase order** at T_acoustic:
  - C^2: T/J=0.120, xi_phase=532 cells (ORDERED, long-range)
  - su(2): T/J=1.90, xi_phase=34 cells (DISORDERED, marginal)
  - u(1): T/J=2.93, xi_phase=22 cells (DISORDERED)
- J = |E_cond| * rho_s * f_overlap: J_C2=0.933, J_su2=0.059, J_u1=0.038 M_KK
- f_overlap = exp(-l_cell/xi_GL) = 0.856 (conservative)
- phi_rms(C^2, acoustic) = 0.566 rad (harmonic valid)
- n_s from phase-gradient coupling: n_s = 1 (HZ), 8.3 sigma from Planck
- Scale: CMB K_pivot = 7.2x tessellation K_max at fabric scale (probes within-cell)
- **Structural theorem**: P(K) = T/(zJ(1-gamma_K)), universal for any Josephson array
- Data: `tier0-archive/s47_texture_corr.{py,npz,png}`

## Session 47: ANISO-DISSIP-47 (Gate: INFO)
- **3 structural theorems**: rho_s anisotropy DECOUPLED from LZ friction
  1. dH/dtau block-diagonal (inter-sector = 0 to 10^{-28})
  2. dH/dtau is order-3 Clifford (gamma_ijk only, orthogonal to J_a = gamma_a)
  3. Schur isotropic Casimir: Tr(T_a^2) = I(p,q) same for all a=1..8
- **Order-3 decomposition**: su2^3 (69.6%), C2-C2-u1 (21.7%), C2-C2-su2 (8.8%)
- **Strict shortfall**: 3.76x (unchanged from S46)
- **Generous screening bound**: 2.22x at fold (Jensen inequality)
- **Best across tau sweep**: 1.85x at tau=0.40
- **Structural conclusion**: n_s gap cannot be closed by direction-weighting
- **C^2 intra-sector norm = 0**: C^2 generators are purely INTER-sector
- Data: `tier0-archive/s47_aniso_dissip.{py,npz,png}`

## Key Data Files (all in `tier0-computation/`)
- S36: `s36_sfull_tau_stabilization.npz`, `s36_mmax_authoritative.npz`
- S41: `s41_spectral_refinement.npz` (16 tau, eigenvalues stored at 7 tau in s36)
- S43: `s43_lifshitz_class.npz` (23 tau, all sectors, alpha, DOS, classification)
- S43: `s43_bcs_universality.npz` (universality class, exponents, curvature, KZ)
- S44: `s44_lifshitz_eta.npz` (eta_eff, n_s, stiffness, tau scan, KK suppression)

## Code Pitfalls
- `.npz` Landau coefficients are 1D arrays. Use `float(np.asarray(d['key']).flat[0])`
- `.npz` 0D scalars: `d['M_8x8']` can be 0-dim. Use `float(np.asarray(d[k]).flat[0])`.
- `s36_mmax_authoritative.npz`: key is 'M_8x8' NOT 'M_max'. Always inspect keys first.
- `d2S_fold` and `dS_fold` in s36 are 1D arrays, not scalars. Pass directly to np.savez.
- Working paper has MULTIPLE `*(Agent writes here)*` placeholders. Use Python for reliable replacement.
- ALWAYS verify post-write that results landed in correct section.
- Riemann tensor sign: Koszul-formula Riemann gives NEGATIVE Ric for compact groups. Fix: negate contraction Ric_ij = -R^k_ikj. Verified at tau=0: R = +6 for SU(3).
- Working paper file modified by other agents between Read and Edit. Use Python open/write for reliable updates.

## Spectrum Structure (0,0) Singlet
- 16 eigenvalues: 3 levels B3 (mult 3), B2 (mult 4), B1 (mult 1) x 2 (PH symmetric)
- B1 gap-edge, non-degenerate, closest to zero
- PH symmetry exact (BDI class)
- N_eff: 32 at tau=0, 240 at any tau>0

## Landau Classification Framework Document
- **Location**: `sessions/framework/landau-classification-of-phonon-exflation.md`
- **Status**: Living document, 509 lines, created S44
- **Content**: Complete CM-to-framework mapping table (35 entries), phase classification, one-body/many-body partition, DM/DE derivation, OCC-SPEC-45 analysis, S45 predictions, limitations
- **Key insight**: Framework succeeds for response coefficients (one-body), fails for ground state properties (many-body). Spectral action = Landau F evaluated at vacuum; OCC-SPEC-45 = F evaluated at physical state.
- **Predictions for S45**: OCC-SPEC non-monotone (min near tau=0.19) -- **WRONG** (S45 W1-R2: FAIL, monotone). KZ n_s too red (FAIL predicted -- confirmed). alpha_eff in [0.2, 0.6]

## Session 45: GL-GGE-STABILITY-45 (Gate: INFO)
- **GGE is a Morse-index-3 saddle of F on the 8-temperature manifold**
- Hessian eigenvalues: [-28.3, -11.5, -6.96, -2.37, -0.20, +1.24, +1.79, +12.6]
- 5 stable (H<0, F concave) + 3 unstable (H>0, F convex) directions
- **Unstable directions**: intra-B2 tilt (B2=99.7%), B1-vs-B2 competing order (B1=79.5%), intra-B3 tilt (B3=99.9%)
- **Interaction dressing**: occupations shifted 69% from free-particle; eps_eff/2E ~ 0.51
- **Correct Hessian**: H_ij = -beta_i * eps_eff_i * G_ij / T_j^2 (NOT C_ij/T_i)
- D^{-1}C variant gives different eigenvalues because eps_eff != 2E
- All unstable directions require changing n_k: INACCESSIBLE by integrability
- Landscape: no secondary minima in |alpha| < 1; F increases monotonically along unstable dirs
- Concave/convex curvature ratio: 3.15 (stable dominates)
- **Physical picture**: GGE is constrained saddle, stabilized by 8 Richardson-Gaudin charges
- Data: `tier0-archive/s45_gl_gge.{py,npz,png}`

## Session 45: OCC-SPEC-45-LANDAU (Gate: FAIL)
- **F_total = F_geo + E_cond is MONOTONE INCREASING** at all 16 tau, all Lambda, all cutoffs
- **Scale separation**: |E_cond|/F_geo ~ 5.5e-7. Variation ratio delta_Econd/delta_Fgeo = 5e-7 (2 million to one)
- **Full-spectrum BCS gives F_BCS > 0**: mu=0, no Fermi sea. ALL modes contribute kinetic cost. Use ED E_cond.
- **Delta(tau) monotone decreasing**: 0.825 (tau=0) to 0.770 (fold). No VH spike.
- **Exp-cutoff F_geo DECREASING**: S37 monotonicity is for Tr|D|, NOT exp(-x). Different cutoff functions give different monotonicity, but all give monotone F_total.
- **VH near-crossing negligible**: 150/101984 states (0.15%). Max enhancement 0.21%.
- **Nb analogy**: E_cond ~ 10^{-9} of cohesive energy. BCS sets T_c, not crystal structure.
- **29th equilibrium closure.** Spectral action tau-stabilization: zero-dimensional constraint surface.
- Data: `tier0-archive/s45_occ_spectral_landau.{py,npz,png}`

## Session 45: LK-RELAX-45 (Gate: FAIL)
- **LK equation**: d(tau)/dt = -(1/tau_0) dS_occ/dtau. Overdamped relaxation on S_occ landscape.
- **tau_0 estimates**: ATDHFB/d2S (5.33e-6), 1/omega_att (0.699, PRIMARY), 1/Gamma_L (4.00)
- **No minimum**: S_occ monotonically decreasing. LK force positive at all tau.
- **Velocity at fold**: v = 2.22e+04 M_KK (838x v_terminal)
- **Transit N_e**: 2.34e-3 (primary), 1.51e-2 (most favorable). Both << 0.1 threshold.
- **No transient trapping**: no inflection points, no dwell maxima near fold
- **Force decomposition**: 93% occupation change + 7% eigenvalue change, SAME SIGN (cooperate, not compete)
- **30th equilibrium closure.** Spectral action dynamical trapping surface: dimension zero.
- Data: `tier0-archive/s45_lk_relax.{py,npz,png}`

## S46: ZUBAREV-DERIVATION-46 (Gate: PASS, but S45 alpha RETRACTED)
- **S45 alpha = 0.410 RETRACTED**: entropy functional mismatch artifact
  - S_GGE = Shannon (-sum n ln n) = 1.612, S_max = FD max (8 ln 2) = 5.545
  - These are DIFFERENT functionals. Mixing them is thermodynamically meaningless.
- **Consistent FD/FD**: alpha = 0.818 (2.1x observed)
- **Zubarev E/P (grand potential)**: alpha = 1.152 (3.0x observed)
- **Keldysh E/sigma (entropy production)**: alpha = 0.698 (1.8x observed)
- **Gate**: Zubarev vs Keldysh discrepancy 39.4% < 50% threshold. PASS.
- **Formula NOT in Zubarev (1974)**: original to framework
- **BdG factor 2**: rho_k = 2*E_k*n_k. Must use E_gibbs(T) = 2*sum E_k/(exp(E_k/T)+1)
- **T_eq = 0.445 M_KK** (with BdG factor), NOT 0.764 (without)
- **DM/DE remains OPEN**: no consistent method reaches alpha = 0.39
- Output: `tier0-archive/s46_zubarev_derivation.{py,npz,png}`

## Critical Entropy Lesson
- Shannon: S = -sum n_k ln(n_k). Max = ln(N) at uniform. For occupations summing to 1.
- Fermi-Dirac: S = -sum[n ln n + (1-n)ln(1-n)]. Max = N*ln(2) at n=1/2.
- The (1-n)ln(1-n) hole entropy term is ESSENTIAL for fermions.
- NEVER mix Shannon numerator with FD denominator. This was the S45 error.

## Session 48: ANISO-OZ-48 (Gate: INFO)
- **O-Z form** P(K)=T/(J K^2 + m^2) on 4x4x2 lattice with J_xy=0.933, J_z=0.059
- **n_s = 0.965 trivially achieved** at m* = 11.87 M_KK = 12.72 J_C2. ONE-PARAMETER family.
- **Running theorem** (STRUCTURAL): alpha_s = -(1 - n_s^2) in continuum O-Z. EXACT.
  - At n_s=0.965: alpha_s = -0.069 (9.6 sigma from Planck)
  - Lattice N=32: alpha_s = -0.038 (4.9 sigma from Planck)
  - N-dependence monotonic: alpha_s -> -0.069 as N -> infinity
- r = 0 (no GW from texture mechanism). Consistent with BICEP.
- Anisotropy angular spread std(n_s) = 0.014 (below observational precision)
- xi_J = 0.067 cells at m*: mass-dominated, phases uncorrelated
- **TENSION**: m=0 gives ordered texture (xi=532 cells), m=m* gives tilt but destroys order
- **alpha_s is a discriminant**: if Planck alpha_s converges to -0.005, O-Z is in 5-10 sigma tension
- Data: `tier0-archive/s48_aniso_oz.{py,npz,png}`

## Session 48: LEGGETT-MODE-48 (Gate: PASS)
- **omega_L1 = 0.0696 M_KK** (lower Leggett, B3 oscillates against B1+B2, 99.9% B3 weight)
- **omega_L2 = 0.1074 M_KK** (upper Leggett, B1 vs B2, 93% B1, 7% B2)
- **2*Delta_B3 = 0.1683 M_KK** (pair-breaking threshold)
- **ratio omega_L1/(2*Delta_B3) = 0.413** -- SHARP resonance, Q = infinity (mean-field)
- **Sharp at ALL tau in [0.05, 0.35]** (ratio 0.40 to 0.44, robust)
- **W2-D estimate WRONG**: 0.284 M_KK was 2-band formula, factor 4.3x too high
- **Correct method**: 3-band generalised eigenvalue problem M v = omega^2 diag(rho) v
- **Josephson hierarchy**: J_12 = 0.0354 >> J_23 = 0.00181 >> J_13 = 0.00047 (K_7 rule)
- **Robust**: PASS for all three V-matrix variants (constrained, branch, raw)
- **Energy hierarchy**: omega_L1 (0.070) < omega_L2 (0.107) < |E_cond| (0.137) < 2*Delta_B3 (0.168)
- Leggett mode is LOWEST collective excitation. 11x softer than pair vibration.
- **Physical**: B3 is "light" sector (rho=0.48, 30x smaller than rho_B2), dominates lower Leggett
- Data: `tier0-archive/s48_leggett_mode.{py,npz,png}`

## Session 49: BRAGG-GOLDSTONE-49 (Gate: INFO)
- **Bragg gap exists but at O(1) M_KK** — 30-60 orders above target [10^{-60}, 10^{-30}]
- **Critical geometry discovery**: w_wall (0.465) > l_cell (0.152). Cells immersed in walls.
  Must use L_Z3 = 1.462 as true lattice period (interior 0.997 + wall 0.465).
- **Z_3 quantization theorem**: Phase jump = 2pi/3 => rho_s(wall)/rho_s(bulk) = cos^2(pi/3) = 1/4
  => impedance ratio eta = 1/2 EXACTLY. Cannot be tuned.
- **Three models tested**: All give m_Bragg in [0.07, 1.35] M_KK.
  Model A (Z_3 phase): 0.269 M_KK. Model B (geodesic tension): 0.071. Model C (elastic): 1.353.
- **3D (4x4x2)**: Same eta=1/2 in both xy and z directions. m_Bragg = 0.269 M_KK everywhere.
- **Disorder**: Gap survives 10% cell-size randomness (200 realizations).
- **Structural exclusion**: Bragg mechanism CANNOT produce hierarchically small mass.
  All parameters (eta, c, a) are O(1) M_KK. Z_3 topological quantization prevents eta -> 1.
- **Next**: Hierarchically small mass requires non-Bragg mechanism (instanton, Friedmann coupling).
- Data: `tier0-archive/s49_bragg_goldstone.{py,npz,png}`

## Session 49: LEGGETT-TRANSIT-49 (Gate: FAIL)
- **Leggett mode CEASES TO EXIST post-transit** (same fate as Goldstone, S38)
- **Sudden limit**: omega_transit/omega_L1 = 12,721. Mode frozen (dt/T_L = 1.25e-5)
- **Phase accumulation**: 7.86e-5 rad during transit. N_osc = 1.25e-5.
- **LZ gamma = 0.01**: Diabatic regime. Leggett state unchanged by sweep.
- **Wrong-sign gap equation**: (1-2n_k) = -0.997 when P_exc=1. Delta_SC = 0 self-consistently.
- **J_ij = 0 post-transit**: No Josephson coupling without condensate. omega_L = 0.
- **9th integral**: Conserved at 4% in adiabatic scenario (O(1/N) = 12.5%).
  Post-transit: trivially conserved (free kinetic energy), NOT independent.
- **Hierarchy**: omega_L1 (0.070) < omega_L2 (0.107) < |E_cond| (0.137) < omega_PV (0.792).
  Leggett is slowest collective mode, most frozen during transit.
- **Adiabatic comparison**: A_L = 0.098 (would oscillate healthily if condensate survived).
- **Symmetry argument (Paper 04)**: Collective mode of ordered phase requires order parameter != 0.
  P_exc = 1 restores full U(1) symmetry. No broken symmetry => no Leggett modes.
- Data: `tier0-archive/s49_leggett_transit.{py,npz,png}`

## Session 49: S49 Collab Review Key Findings
- **alpha_s = n_s^2 - 1 is single-pole O-Z artifact**: Multi-pole Leggett propagator (3 poles: Goldstone, L1, L2) modifies running. Decisive S50 computation: eq. (3) in collab review.
- **Leggett IS the dipolar analog**: J_23 breaks U(1)_7, epsilon = 0.00248, m_G = omega_L1 = 0.070 M_KK (18% from n_s target)
- **Multi-pole propagator formula**: P(K) = sum_alpha w_alpha / (rho_alpha K^2 + m_alpha^2). n_s from d log P / d log K.
- **Fabric GL free energy**: F includes -J_{ss'} |Delta_s||Delta_{s'}| cos(phi_s - phi_{s'}). Leggett = phase sector, not amplitude.
- **32-cell fabric**: 96-mode coupled oscillator (3 phases x 32 cells). Hybridized Goldstone-Leggett mode.
- **Wall-dominated fabric**: w_wall/l_cell = 3. Not "cells with thin walls" but "walls with small patches". Granular limit.
- **HFB V state-independent**: Peter-Weyl representation theory. Backreaction 1.2%. Simpler than nuclear DFT.
- **Multi-T pressure amplifier**: GGE shifts w_0 by 33% toward DESI (spin-charge-like separation).
- **Surviving n_s route**: ONLY multi-pole Leggett propagator. Single-pole O-Z gives alpha_s 6 sigma from Planck.
- **S49 closures**: Bragg gap (Z_3 quantization), Leggett post-transit (Delta=0), CMPP transition (Type II locked), S48 analog horizons (amplitude != phase), cavity-Leggett unification (11.5x mismatch)
- **Collab file**: `sessions/archive/session-49/session-49-landau-collab.md`

## Session 50: LEGGETT-PROPAGATOR-50 (Gate: FAIL — DEGENERACY THEOREM)
- **3-pole = O-Z to 1.5e-7**: Genuine multi-pole effect = 5.8e-9 (8.6e-8 relative)
- **WHY**: Josephson splitting sigma_max = 0.072 M_KK^2, on-site mass m_base^2 = 140.5 M_KK^2
  => poles 99.95% degenerate. Splitting/mass = 5.1e-4.
- **Equal-stiffness theorem**: Same lattice => P(K) = sum_i P_OZ(K; lambda_i). Unit residues.
  Identity holds per pole. Multi-pole correction = sum dw_i/d(ln K)*(n_s_i-1) ~ O(sigma/m^2) ~ 0.
- **Enhancement scan**: Even 4000x Josephson: alpha_s shifts by 0.3%. Need ~195x for 1% shift.
- **Structural cause**: n_s = 0.965 FORCES m_base >> sigma_max. Any mechanism preserving
  n_s = 0.965 will make poles near-degenerate.
- **Tension UNCHANGED**: 8.4 sigma (same as S49 O-Z)
- Pole structure: mu_1=11.854, mu_2=11.854, mu_3=11.857 M_KK
- Data: `tier0-archive/s50_leggett_propagator.{py,npz,png}`
- **Lesson**: Bisection for m_base: use arithmetic mean, bracket from [8,15], verify convergence.
  Geometric mean on steep function converges to wrong limit.

## Session 50: RUNNING-MASS-50 (Gate: FAIL — STRUCTURAL THEOREM)
- **Structural bound**: gamma < 1 - n_s = 0.035 for ANY single-pole propagator P(K) = T/(J K^2 + m(K)^2)
  with power-law running m^2 ~ K^gamma, when n_s = 0.965 (red tilt).
- **Gate required gamma > 1.7**: 49x above structural maximum. ALGEBRAICALLY IMPOSSIBLE.
- **Proof**: u = (1+n_s)/(1-n_s-gamma) must be positive. This forces gamma < 1-n_s.
- **Correction formula**: delta_alpha = gamma*(2-gamma)*u/(1+u)
- **Physical coupling gamma = -6.76e-4** (from 1-loop sunset at lambda = V(B2,B2) = 0.1557)
- **Irony**: At structural max gamma->0.035, delta_alpha->0.0688, which EXACTLY cancels n_s^2-1.
  But this requires u->infinity (pure mass propagator, no kinetic term). Not O-Z.
- **Implication**: alpha_s tension CANNOT be resolved by radiative corrections to mass.
  Must modify propagator STRUCTURE (multi-pole) not mass (running).
- Data: `tier0-archive/s50_running_mass.{py,npz,png}`

## Session 50: ANOMALOUS-DISPERSION-50 (Gate: FAIL — GOLDSTONE THEOREM)
- **Z_3 disorder does NOT produce anomalous dispersion** on 32-cell fabric
- **P_Z3/P_iso flat to 1.7%**: Disorder changes mass, not dispersion form
- **Structural**: Goldstone theorem forces epsilon ~ K^2 for broken U(1). K_pivot at Ka/pi = 0.096.
- **Z_3 is periodic superlattice**, not random disorder. Cannot produce localization.
- **Z_3 bond weakening**: 75% of xy bonds reduced to J_C2/4. In-plane modes softened 4x.
- **Bandwidth compressed**: Z_3 bandwidth = 0.57 * aniso. Van Hove peak shifts to low energy.
- **Mass renormalization**: Z_3 requires m^2 = 38.0 vs iso m^2 = 106.5 (factor 0.36).
- **Lattice artifact WARNING**: 14 K-shells insufficient for alpha_s extraction.
  Retuned propagator gives alpha_s = +0.023 even for KNOWN K^2 (isotropic model).
  Deviation from identity 0.092 in ALL models. Use propagator ratio, not absolute alpha_s.
- **Fifth closure**: After 3-pole (W1-A), running mass (W1-F), eikonal (W1-H), RPA (W2-B)
- Data: `tier0-archive/s50_anomalous_dispersion.{py,npz,png}`

## Session 51: POLARITON-51 (Gate: FAIL — STRUCTURAL)
- **Hopfield 2x2 dynamical matrix**: Goldstone (m_G=0.070) coupled to SA effective mode (C2_eff=7.355)
- **Three physical couplings**: g_geom=9.87e-3, g_BCS=2.00e-3, g_mod=4.40e-5 M_KK^2
- **Stability threshold**: g < sqrt(m_G^2 * C2_eff) = 0.190 M_KK^2 (positive-definiteness)
- **Maximum |alpha-2|**: 0.0038 (26x below gate threshold 0.1). UNREACHABLE in stable regime.
- **Task formula g=(dDelta/dtau)^2*dS/dtau/sqrt(rho_s)=1.36**: DIMENSIONALLY INCONSISTENT. Produces tachyon (7.2x above stability). Not polariton formation — phase instability.
- **Parametric suppression**: (dDelta/dtau / Delta_0)^2 = 1.1e-4. BCS gap is robust to tau modulation.
- **Mass asymmetry**: 39x (sqrt(C2)/m_G). Fundamental obstruction to mode mixing.
- **Self-energy formulation** (multi-pole, 5 Casimir masses): max |alpha-2| = 0.0073. Also fails.
- **Regime**: WEAK coupling (Omega_R/Gamma = 0.015 at best). theta ~ 90 deg (pure Goldstone).
- Data: `tier0-archive/s51_polariton.{py,npz}`

## S50 Collab Review: Goldstone Loopholes Analysis
- **4 CM loopholes examined**: Coulomb (CLOSED, U(1)_7 global), Anderson-Higgs (OPEN if gauged),
  Bose glass (CLOSED, Z_3 periodic), frustrated magnets (CLOSED, counting saturated)
- **Key suggestion**: Anderson-Higgs via gauging U(1)_7 using Connes inner fluctuations.
  Would need g_7 ~ 16, a_2 Seeley-DeWitt computation determines gauge coupling.
- **Polariton model**: Hopfield-type SA-Goldstone avoided crossing (additive, not multiplicative).
  Different from cross-domain resonance lever. Could produce non-K^2 lower branch.
- **Feshbach resonance**: phi crossing (tau=0.2117) as doorway state. Leggett dissolves into
  Dirac continuum at resonance. Transfers geometric info with non-trivial K-dependence.
- **Critical exponent eta**: 3D Ising/XY/Heisenberg all give eta ~ 0.036-0.038, matching 1-n_s = 0.035.
  **S51 RESOLUTION**: At u=56, eta contributes only 1.8% of tilt. Coincidence, not structural.
- **Collab file**: `sessions/archive/session-50/session-50-landau-collab.md`

## Session 51: CRITICAL-SCALING-51 (Gate: INFO — CLOSED)
- **Critical scaling hypothesis for 170x: CLOSED**
- omega_L1(tau) varies only 10.5% across [0.025, 0.40], NEVER approaches zero
- No BCS critical point (1D theorem, Delta never vanishes)
- omega_L1 MAXIMUM near fold, m*/m_L MINIMUM at fold (anti-critical)
- Parabolic peak at tau~0.36 (B3 DOS drives upturn via decreasing inertia)
- eta coincidence: delta(1-n_s) from eta = 0.00064 (1.8% of tilt, negligible at u=56)
- 170x decomposition: u=56.1 (tilt) x J_eff/V_12=4.9 (stiffness) x K^2=3.9 (geometry)
- L1 eigenvector: 99% B3 sector (smallest DOS, largest amplitude)
- Goldstone check: max|lambda_0| = 3.5e-18 (machine zero at all 60 tau points)
- Data: `tier0-archive/s51_critical_scaling.{py,npz,png}`

## PI Directive: Framework-First-Physics (S40)
- STOP gating things already gated. Spectral action is DEAD by theorem.
- Explore what is DIFFERENT. The physics of the atomic is not the physics of the sub-quantum.
- Fails are coastlines, not defeats. Map, don't judge.
