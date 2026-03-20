# Landau Session Detail (overflow from MEMORY.md)

## Session 29Bb Detailed Results (2026-02-28)

### 29B-3: BCS Gap with Bogoliubov Occupation (P-29c FIRES)
- BEC-side gap equation: Delta_n = -sum_m V_{nm} * Delta_m * (1+2*B_m) / (2*E_m)
- Gap EXISTS WITHOUT Bogoliubov injection. Delta_vac/lmin = 0.092 at (3,0) tau=0.50. Enhancement only 1.02x.
- UT-5 thermal Goldilocks RESOLVED: window is entire B_k >= 0 quadrant. Not narrow.
- B_k is ANTI-THERMAL (peaks at band top, not gap edge). T_eff ~ 3-5 >> T_c ~ 0.08.
- (0,0) singlet anomalous: gap only at tau=0.20. V(gap,gap)=0 selection rule forces off-diagonal chain.
- Data: `tier0-archive/s29b_bogoliubov_bcs.{npz,py,txt,png}`

### 29B-4: Jensen 5D Transverse Hessian (B-29d FIRES -- saddle)
- 2/4 transverse eigenvalues negative: E1=-511,430 (T2 cross-block), E2=-16,066 (T1 breathing)
- 2/4 positive: E3=+219 (T4 C^2 aniso), E4=+1,758 (T3 su(2) aniso)
- EXACT block-diagonality: U(2)-invariant (T1,T2) decouples from U(2)-breaking (T3,T4) at 10^{-8}
- Pomeranchuk instability in moduli space: BCS condensate favors lower lambda_min than Jensen provides.
- True minimum in U(2)-invariant 2D family. 1D Jensen ODE needs promotion to 2D.
- Data: `tier0-archive/s29b_jensen_transverse.{npz,py,txt,png}`

### 29B-5: Full 1-Loop Josephson Coupling (P-29e FIRES)
- J_max/Delta = 1.17, J_1loop/Delta = 4.52 at tau=0.35 (BCS minimum)
- STRONG Josephson regime (stronger than MgB2 ~ 0.3-0.5 or iron pnictides ~ 0.1-1.0)
- CG enhancement: singlet channel in (3,0) x (0,3) provides representation-theoretic coupling
- d_eff >= 2 CONFIRMED at ALL tau in [0, 0.50]. Mermin-Wagner does NOT apply.
- Data: `tier0-archive/s29b_josephson_coupling.{npz,py,txt,png}`

### 29Ba Results (inherited)
- B-29a PASS: 3-sector F_BCS = -17.22, 172x above threshold. Stabilization UV-safe.
- P-29b conditional: sin^2(theta_13) = 0.027 at tau=0.50. Theta_23 fails (14 vs 49 deg).

## Session 29 Full Summary (2026-02-28)
- ALL 7 priority computations executed. 17 total across 5 sub-sessions.
- Gaussian correction: Gi=0.36 singlet, 0.014-0.028 multi-sector. F_1loop/F_MF=0.125-0.130. Amplitude mode gapped.
- V_eff monotone after BCS: Spectral action slope overwhelms F_BCS at ALL tau. L-9 sole trapping.
- Trapping margin: 20% sensitivity (mu_eff >= 1.2*lambda_min required). Principal vulnerability.
- BCS without injection: Delta_vac/lmin=0.092. KC-1 enhancement only 1-2%. UT-5 resolved.
- Weinberg angle: sin^2(theta_W) moves toward 0.231 along T2 direction. P-30w pre-registered.
- Observational: k=9.4e23, f_peak=1.3e12 Hz. Both structurally inaccessible.
- S29 collab: `sessions/archive/session-29/session-29-landau-collab.md`

## Session 32 Detailed Results (2026-03-03 to 2026-03-06)

### Session 32 Core (2026-03-03)
- RPA-32b PASS: d^2(sum|lam|)/dtau^2 = 20.43, 38x above threshold. Wall 4 circumvented.
- W-32b PASS: rho_wall = 12.5-21.6, 1.9-3.2x above BCS threshold. Wall 3 bypassed at boundaries.
- Key vulnerability: Wall width (K_grad) uncomputed; smooth walls suppress van Hove LDOS.
- Key vulnerability: V_pair * rho_wall ~ 1.2-2.0, marginal for wall-BCS gap equation.
- S32 collab: `sessions/archive/session-32/session-32-landau-collab.md`
- S32 data: `s32a_*.npz`, `s32b_*.npz`, `s32c_*.npz`

### Session 32 W4 R2 (Landau x QA workshop, 2026-03-06)
- Turing KILLED: Delta is slaved (no gradient energy). System is single-field (tau). LK relaxation.
- Reverse critical slowing: tau_LK -> 0 at dump point. BCS singularity steepens potential.
- Dissipation: B3 provides damping (99.6% RPA weight). B2 does NOT dissipate (flat, no transport).
- Spinodal at swallowtail: At eta=0.04592, nucleation barrier B_3D=0. SPINODAL DECOMPOSITION.
- GL coefficients: Delta_jump=0.114 (weak) to 0.24 (BEC). L/E_kin=1.21 (weak) to 2.5 (BEC). Marginal at weak, comfortable at BEC.
- Ginzburg: Gi~0.005. Mean-field reliable (comparable MgB2, 60-200x below MATBG).
- M_max stress-test: Van Hove survives BCS (coherence peak reinforces). Flat-band M_max/M_crit~1-2 is TYPICAL.
- kappa_wall = 3.6: Deeply Type II. Negative surface energy. Walls PROLIFERATE. Honeycomb Z_3 network.

#### CT Structural Theorems (Session 32 W4 R2)
- CT-1: Swallowtail trapping + Peotta-Torma D_s=2*g_B2 share root in g_B2=4.24.
- CT-2: sqrt(v_B1*v_B2)=0.026=shell gap. Algebraic identity for 2-band fold.
- CT-3: xi_BCS(0.55) < w_wall(2.0) < l_imp(4.4). Local BCS. Clean limit.
- CT-4: Fabry-Perot enhances M_max: 0.92->1.44 (band-edge valid).
- CT-5: Displacive transition, not order-disorder. First-order nucleation at band-edge phase boundary.
- CT-6: Z_wall=1/pi. Universal finite impedance at fold. DOS divergence and v->0 cancel.
- CT-7: B2 = symmetry-protected BIC. Bound state in B3 continuum. Trap 4 = Schur protection. Infinite Q.
- CT-8: Andreev self-confinement. R_BCS~1.0. BCS gap = perfect mirror for B2.
- Pattern formation: DISPLACIVE with first-order nucleation. Swallowtail -> spinodal.
- Vulnerabilities: V normalization (0.08 vs 0.31), LANDAU-SECTOR test, self-consistent CHFB.

## Session 33 W3 R2: Domain Wall BCS (2026-03-06)
- Landau critical velocity: v_c set by B3. v_c = 1.51 (tau=0.15), 1.42 (0.20), 1.35 (0.25). Monotonically decreasing.
- Pomeranchuk at walls: B2 ph coupling REPULSIVE. f_0 = +30 (bulk), +0.6-2.1 (walls). Session 22c f_0=-4.687 was cross-sector.
- BCS exactly single-band: V(B_i, B_j) = 0 to machine precision (Trap 4). Only Delta_B2 > 0.
- phi_paasch NOT a BCS attractor in singlet: Dressed ratio at Delta_B2=0.128 is 1.044, not 1.532. Needs Delta=0.93 (unphysical).
- USER CORRECTION: phi_paasch correlations in BCS context are likely just correlations. phi is spectral geometry; BCS is many-body. Need self-consistency mechanism.
- GL free energy: F = a(tau)|Delta|^2 + b|Delta|^4 + c|Delta|^3*cos(3*theta), c=0.007 (L-9). First-order. U(1)->Z_3.
- Phase boundary: First-order BCS (latent heat trapping), NOT Landau critical velocity.
- Wall 10x subsonic (v_tau/v_c = 0.098). Two-layer protection: geometric + BCS.
- E_kin = 0.0095-0.0245 from KK modulus equation. B3 Cherenkov unchanged by BCS (Trap 5: Delta_B3=0).
- Berry RETRACTED phi_paasch attractor. Z_3 domain wall topology from cos(3*theta).
- CRITICAL AMBIGUITY: V_pair vs V_ph distinction. L_BCS estimates used V_ph off-diagonal (0.09-0.63); BCS needs V_pair.
- **TRAP-1 gate**: Solve 2x2 real BdG for B2 at wall. Gate: Delta_wall > 0 AND L_BCS > 0.0095.
- **K-1e may need revisiting**: Session 23a used diagonal coupling only. Off-diagonal (CG-allowed) may change verdict.
- **ANDREEV-Z3 gate**: Solve 1D BdG for B2 at Z_3 wall with 2pi/3 phase twist. Prereq: TRAP-1.

## Framework Paasch-Potential Review (2026-03-06)
- Collab: `sessions/framework/framework-paasch-potential-landau-collab.md`
- Poschl-Teller well SHALLOW: lambda_PT ~ 0.008-0.14 at estimated wall params. AT MOST 1 bound state.
- Correct CM analog is ANDREEV bound states, not Poschl-Teller.
- 45-deg / 120-deg incommensurability: n*pi/4 = m*2pi/3 has no integer solutions.
- B2 counting problem: 4-fold B2 multiplet must generate 6 Paasch sequences. Mismatch 6/4 = 1.5.
- L_wall/xi_BCS = kappa analog: Type I/II for walls. phi_paasch~1.53 would be "Type II wall."
- Wall coarsening problem: Without stabilization, Z_3 wall network coarsens to single domain.
- Z_3 Potts: Delfino-Mussardo m2/m1 = 2*cos(pi/5) = 1.618 (golden ratio in Potts too).
- Spectral function diagnostic: A(x,E) at wall center for QP character.

## CM Analogs Reference (Session 30)
- Multi-band BCS: MgB2, iron pnictides
- Semiconductor BCS: SrTiO3, TBG
- Pomeranchuk: He-3
- AZ class BDI: InSb/Al wires
- First-order BCS: CeCoIn5
- Leggett mode: MgB2

## Session 28 Fusion Cross-Synthesis Detail
- F-1: V_total = S_spectral(tau) + F_BCS(tau, Delta(tau)). Min in 2D even if 1D projection monotone.
- F-2: J-even triple function. CPT + d_eff guarantor. J maps (3,0)->(0,3).
- F-3: Q-factor ~100-130 (underdamped). First-order L-9 provides single-pass capture.
- F-4: Pomeranchuk-van Hove mutual reinforcement. f_0=-300 + zero critical coupling.
- F-5: Semiconductor self-doping analog. Gap=band gap, Parker=doping, BCS=superconductivity.
- F-6: 3-sector L-8 resolution. Only (3,0)/(0,3)/(0,0) load-bearing.
- F-7: Cooper pairs spatially global but sector-localized.
- F-8: J-symmetry guarantees Josephson coupling for conjugate sectors.
- CDL bounce RESOLVED: V_total has no saddle beyond BCS min.

## Session 34 Detail (2026-03-06)

### Bug Corrections
1. J operator: B=sigma_2^{x4} WRONG. C2=gamma_1*gamma_3*gamma_5*gamma_7 CORRECT. J D_K J^{-1}=+D_K to eps.
2. V matrix: A_antisym (frame, 8x8) V_max=0.287. K_a_matrix (spinor, 16x16) V_max=0.057. Factor 5x error.
3. Wall DOS: Step rho=5.40. Smooth van Hove rho=14.02 (2.6x). v_min=0.012 cutoff, v_crit=0.085.

### Gate Results
- DPHYS-34a-1 PASS: Fold survives to phi=0.17 (1.28x gate). d2 increases 1.176->1.226 (stabilization).
- TRAP1-34a CONFIRMED: V(B1,B1)=0 exact. U(2) singlet selection rule. Permanent.
- DPHYS-34a-2 PASS: V(B2,B2) enhanced 0.057->0.086 (+50%) at phi=gap. Off-diagonal only.
- RPA-34a CONSISTENT: d2S=180.09 at phi=gap (333x margin, up from 38x bare).
- DPHYS-34a-3 FAIL: M_max=0.899 all walls (step DOS). Superseded by VH-IMP-35a.
- VH-IMP-35a PASS: M_max=1.445 (smooth wall, imp=1.0, spinor V).
- BMF-35a FAIL at N_eff=4: 35% suppression. Corridor N_eff>5.5.
- MU-35a CLOSED: PH forces mu=0.
- GC-35a CLOSED: Helmholtz F convex at mu=0.

### Corrected Chain (all mean-field PASS)
I-1(3.2-9.6x) -> RPA-32b(333x@D_phys) -> U-32a(D=16-3435) -> W-32b(1.9-3.2x) -> BCS(M_max=1.445)

### Permanent Structural Results
- [iK_7, D_K]=0 at all tau. SU(3)->U(1)_7 exact. B2=+/-1/4, B1=0, B3=0.
- Schur on B2: Casimir=0.1557, irreducible. V basis-independent.
- Trap 1: V(B1,B1)=0 exact (representation-theoretic identity).

### Impedance
- T_branch=0.998, T_diag=0.362. CT-4's R=0.64 is intra-B2 rotation, not scattering.
- Physical impedance ~1.0. Cross-branch leakage <10^{-28}.

### N_eff Corridor
N_eff=inf: M_eff=1.272(PASS). N_eff=8: ~1.15(PASS). N_eff=5.5: ~1.01(MARGINAL). N_eff=4: 0.938(FAIL).
Cross-channel: V(B1,B2)=0.080, V(B3,B2)=0.022. Multi-band Thouless needed.

### Proposed Next Computations
1. Multi-band 3x3 Thouless matrix eigenvalue (resolves N_eff) -- DONE Session 35, PASS
2. Josephson re-evaluation with spinor V
3. Ginzburg number for wall BCS
4. QP residue Z map across fold
5. Pomeranchuk f_0 at van Hove with diverging DOS

## Session 35 Detail: NEFF-THOULESS-35 (2026-03-07)

### Computation
Multi-band Thouless eigenvalue: 3x3 (branch), 5x5 (B2+B1), 8x8 (all positive modes).
Spinor Kosmann basis (K_a_matrix, not A_antisym). Smooth-wall van Hove DOS for B2.

### Numerical Results
- M_max(8x8, smooth) = 1.6740 -- PASS (67% above threshold)
- M_max(3x3, smooth) = 1.6740
- M_max(5x5, smooth) = 1.6701
- M_max(8x8, step) = 0.7852 -- FAIL at step DOS
- M_max(3x3, step) = 0.7852
- M_max(5x5, step) = 0.7824
- Enhancement 8x8/5x5 = 1.002x
- Participation ratio PR = 6.36
- N_eff_min for BMF = 2.48

### Branch DOS (per mode, with ms factor 1.046)
- rho_B1_eff = 3.94 (step, no fold)
- rho_B2_eff = 14.67 (van Hove smooth)
- rho_B3_eff = 0.48 (step, fast dispersion)

### V matrix (spinor basis, phi=0, tau=0.20)
- V(B1,B1) = 3.4e-29 (Trap 1, exact zero)
- V(B1,B2) max = 0.0799
- V(B1,B3) = 5.8e-30 (NEW selection rule, exact zero)
- V(B2,B2) offdiag max = 0.0572
- V(B2,B3) max = 0.0265
- V(B3,B3) offdiag max = 0.0738

### Eigenvector of dominant Thouless eigenvalue
- B1: 24.6% weight
- B2: 59.4% weight (4 modes)
- B3: 16.1% weight (3 modes)

### Key Physics
1. Van Hove DOS is the SOLE driver: smooth/step ratio = 2.13x, consistent across all matrix sizes
2. Cross-channel couplings are negligible (0.2% enhancement)
3. B1 at gap edge (xi=0) does NOT cause regulator sensitivity because V(B1,B1)=0
4. V(B1,B3) = 0 is a new representation-theoretic selection rule
5. N_eff corridor is WIDE: need only N_eff > 2.48, have PR = 6.36

### Data files
- `tier0-archive/s35_thouless_multiband.{py,npz,png}`
