# Spectral Geometer Agent Memory

## Project Structure
- Research papers: `researchers/Spectral-Geometry/` (35 papers, fully indexed 2026-03-14)
- Index: `researchers/Spectral-Geometry/INDEX.md` (416 lines, 8 topic groups, 35 entries)
- Tier0 computations: `tier0-computation/` (all .py/.npz/.png files)
- Sessions: `sessions/session-NN/` for results, `sessions/session-plan/` for prompts
- Python venv: `phonon-exflation-sim/.venv312/Scripts/python.exe`

## Library Status (Post-S43 Index Rebuild, 2026-03-14)
- All 21 priority papers from S42 meta-analysis NOW PRESENT (15-35)
- Index covers: Gilkey (5), Berger (3), Mueller (3), Lott (1), Connes (3), applied HK (5), rigidity (3), NCG physics (7), CDT (2), propagator (1), bounds (1)
- KEY NEW PAPER: Arias-Marco 2025 (#31) -- natural reductivity INAUDIBLE (structural tension with rigidity results)
- See `meta-analysis-gaps.md` for historical gap analysis (now resolved)

## Key Spectral Results (Post-Session 47)
- **PI-SECTOR-47 PASS**: 13 pi-phases: B1=1(PW=15), B2=9(PW=81), B3=3(PW=35). See `pi-sector-s47.md`
- **[iK_7, D_K] = 0 is (0,0)-ONLY**: Higher PW sectors have ||[I⊗iK7,DK]||/||DK||=7.5% for (0,1). Spinor sectors MIX in entangled eigenstates.
- **TRAP-33b RETRACTED**: Frame V=0.287 was wrong vector space. Spinor V(B2,B2)=0.057
- **Schur on B2**: Casimir=0.1557, irreducible. V basis-independent (10k U(4) + optimization)
- **V(B1,B1) = 0 exact**: U(2) singlet selection rule. All 8 generators, all tau. PERMANENT
- **[iK_7, D_K] = 0**: SU(3)->U(1)_7 exact at ALL tau IN (0,0) SECTOR. B2=+/-1/4, B1=0, B3=0
- **J corrected**: C2 = gamma_1*gamma_3*gamma_5*gamma_7 (product of real gammas)
- **Van Hove**: rho_smooth=14.02/mode (2.6x over step 5.40). v_min=0.012
- **mu=0 forced**: Both canonical (PH) and grand canonical (Helmholtz convex). PERMANENT
- **D_phys fold survives**: d2=1.226 at phi=gap (STABILIZED vs bare 1.176)
- **Kosmann enhanced under D_phys**: V(B2,B2)=0.086 at phi=gap (+50% over bare 0.057)
- **RPA enhanced**: d2S=180.09 at phi=gap (333x margin, up from 38x bare)

## Key Eigenvalue Data (SU(3) Jensen-deformed)
- B1 (trivial, 1-fold): lambda = 0.819 at tau=0.20
- B2 (U(2) fund, 4-fold): lambda = 0.845 at tau=0.20, minimum at tau=0.190158
- B3 (SU(2) adj, 3-fold): lambda = 0.978 at tau=0.20
- Shell gap B2-B1 = 0.026, B3-B2 = 0.133 at tau=0.20
- phi_paasch = m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15

## Proven Structural Results
- KO-dim = 6, SM quantum numbers from Psi_+ = C^16
- [J, D_K(tau)] = 0 -- CPT hardwired (J = C2 = prod real gammas)
- D_K block-diagonal in Peter-Weyl sectors (W2)
- Trap 1: V(B1,B1) = 0 exact (U(2) singlet selection rule)
- Trap 4: inter-branch decoupling on U(2) submanifold (Schur)
- Trap 5: M_ph purely imaginary for all branches (anti-Hermiticity theorem)
- A_2 catastrophe classification of B2 fold, destruction bound 0.42
- Schur on B2: Casimir=0.1557, V basis-independent within degenerate subspace
- [iK_7, D_K] = 0 at all tau: SU(3)->U(1)_7 exact symmetry breaking
- PH x U(1)_7 = full symmetry algebra of D_K for tau > 0

## Mechanism Chain Status (Post-40)
- Chain: UNCONDITIONAL(S35) -> BROKEN at tau-stabilization (S36-S40)
- Structural Monotonicity Theorem: <lambda^2>(tau) monotonic => S_f(tau) monotonic for any monotone f
- **HESS-40: 22/22 transverse positive**, min H=+1572 (g_73), margin 1.57e7. Jensen fold = 28D local min of S_full
- Hessian hierarchy: diagonal u(2) H~20000, complement H~14000, off-diag u(1)-complement H~1572
- Condition number 12.87 (well-conditioned)
- **27 total equilibrium closures**: spectral action cannot stabilize tau in ANY direction
- FRIED-39 shortfall worsens to ~114,000x with M_ATDHFB=1.695 (SELF-CONSIST-40)

## BdG Spectral Triple (S35, R3 COMPLETE)
- C3/C4 PASS, eta=0, spectral flow=0, Goldstone pinning by J (most novel), KO-dim convention issue OPEN
- Publishable JNCG: first BdG spectral triple on compact Lie group. Lichnerowicz bound RETRACTED.

## Session 37/40/45 Key Results (compressed)
- **CUTOFF-SA-37: FAIL**. S_f(tau) monotonic ALL cutoffs. da_6/dtau = -1058 dominates. CLOSED.
- **T-ACOUSTIC-40 PASS**, B2-INTEG-40 PASS, QRPA-40 FAIL(STABLE), GSL-40 PASS, CC-TRANSIT-40 PASS
- **Analytic torsion CLOSED**: T~10^{20301} is truncation artifact. Singlet T=0.147 (physical, O(1)).

## Heat Kernel Validity Tiers (HEAT-KERNEL-AUDIT-45, UPDATED S46)
- See `heat-kernel-audit-s45.md` for full classification
- **Tier 1 (exact)**: spectral action, heat trace, spectral zeta moments
- **Tier 2 RECLASSIFIED (S46)**: "spectral a_2" = zeta_D(1) is NOT the SD coefficient a_2
  - SD a_2 = (4pi)^{-4} * (20R/3) * Vol = 0.728 (geometric, exact)
  - zeta_D(1) = sum d_k/lambda_k^2 = 2776.17 (spectral sum, pole at s=1 for d=8)
  - Ratio = 3812 (structural, not truncation error)
  - M_KK extraction uses zeta_D(1) correctly; the formula implicitly accounts for this
- **Tier 3 (artifact)**: d_s in UV, analytic torsion, anything needing zeta poles
- d_s -> 0 as sigma -> 0 (not 8). Correct dim probe: Weyl counting d_Weyl = 6.81

## Uncomputed Priority Gates (Post-45 Collab Review)
1. ~~Analytic torsion T(tau)~~: CLOSED (artifact of truncation)
2. ~~Truncated torsion~~: COMPUTED S45. T_singlet = 0.147
3. epsilon'' sign convention: re-run Sessions 7-8 with corrected C2
4. Spectral rigidity of fold: is Jensen SU(3) at tau=0.190 spectrally rigid?
5. **Spectral zeta at nonzero s**: zeta(s,tau) for s>4 suppresses UV, may reveal fold structure (Tier 1)
6. **Eta invariant under transverse deformation** (g_73 direction)
7. ~~BdG spectral dimension~~: CLOSED (artifact per audit)
8. ~~Lichnerowicz bound check~~: COMPUTED S46. lambda_1=0.820 >= sqrt(2R/7)=0.759. SATISFIED, 8% margin.
9. **Van Hove on other Lie groups**: SU(4), Sp(2), G_2 -- does fold exist?
10. ~~Independent geometric a_2~~: COMPUTED S46. a_2^{SD}=0.728 vs zeta_D(1)=2776.17. Different objects (factor 3812).
11. **Q-THEORY-T3T5-46**: T3-T5 crossing at tau=0.19104 may lock q-theory crossing (tau*=0.209) to fold
12. ~~Spectral current j(lambda,tau)~~: COMPUTED S46. alpha_j=4.03 (FAIL). alpha_v=0.62 (INFO). UV-dominated.
13. **max_pq_sum=6**: test d_Weyl convergence, M_KK tension, moment ratios
14. **Connes distance on truncated Jensen SU(3)**: finite crystal metric geometry
15. ~~Spectral form factor K(t)~~: COMPUTED S46. Poisson class (HIGH). No ramp. <r>=0.439. t_H=748

## S45 Collab Review: Ways Forward (8 identified)
- See `sessions/archive/session-45/session-45-quicklook-spectral-collab.md`
- Finite crystal is noncommutative geometry in its own right, not truncated manifold
- Connes distance, spectral form factor, eigenvalue current are correct tools
- Continuum limit restores zeta poles, asymptotic SD, genuine torsion -- last open door for CC hierarchy
- T3-T5 crossing (tau=0.19104) may lock q-theory to fold via BCS gap feedback

## Normalization Conventions
- Seeley-DeWitt: a_k with (4*pi)^{-d/2} prefactor, d=8 for SU(3)
- Spinor rank: 2^4 = 16 for 8-dimensional SU(3)
- Volume-preserving Jensen deformation (TT constraint)
- Kosmann pairing: V_nm = sum_{a=0..7} |<n|K_a|m>|^2 (SPINOR basis, not frame)
- K_a = (1/8) sum_{rs} A^a_{rs} gamma_r gamma_s (Kosmann from frame structure constants)
- Connes 15/16: finite-density spectral action exists (van Suijlekom, JNCG 2022)

## Session 36 Results
- **W6-SPECIES-36 PASS (THIN)**: Lambda_sp/M_KK = 2.06 (d=4) or 8.06 (d=8) at fold
- C_Weyl = 42.80 at fold. Converged by L_max=4. d_eff = 8.1 confirms Weyl law
- **GL-CUBIC-36**: Second order. U(1)_7 charges +/-1/2 forbid cubic GL. Z_2 universality
- **ANOM-KK-36**: 150/150 anomaly coefficients = 0 exactly. Structural (pi_1(SU(3))=0)
- **COLL-36**: Vibrational chi/chi_sp = 12.1 W.u. Moderate multi-mode coherence
- **ED-CONV-36**: E_cond enhanced -0.115 -> -0.137. B1 is proximity catalyst
- **INTER-SECTOR-PMNS-36**: All PMNS routes CLOSED on Jensen (Schur's lemma, 5 proofs)
- **WIND-36**: BDI winding nu=0. E_B2/Delta=33.4. Deep trivial. Edge modes CLOSED
- **BBN-LITHIUM-36**: delta_H/H = -6.6e-5 (500x below threshold). UV dominance structural
- **TAU-STAB-36**: S_full monotonic. Level 3 = 91.4% of gradient. Fold invisible to linear sum
- **TAU-DYN-36**: Overdamped. 38,600x shortfall. BCS back-reaction negligible (6.7e-7)
- **CRITICAL INSIGHT (S36)**: Linear sum reads a_0 (volume). Fold lives in a_2/a_4 (curvature). Cutoff shifts weighting from a_0 to a_2/a_4.
- **S37 RESOLUTION**: The shift from a_0 to a_2/a_4 does NOT help. a_2(tau) and a_4(tau) are themselves monotonic. The a_6 term (da_6/dtau = -1058) dominates and ensures all smooth cutoffs give monotonically DECREASING S_f. The "needle hole" is CLOSED.

## Session 46 Results (A2-GEOMETRIC-46)
- **R(tau=0.19) = 2.018**: verified to machine epsilon (analytic vs Riemann tensor)
- **a_2^{SD} = 0.728**: exact geometric Seeley-DeWitt coefficient
- **zeta_D(1) = 2776.17**: spectral sum, structurally different from a_2^{SD}
- Ratio 3812 is structural (pole at s=1 for d=8), not truncation error
- **Lichnerowicz SATISFIED**: lambda_1 = 0.820, bound = 0.759, ratio = 1.080
- Ricci eigenvalues at fold: {0.230 x4, 0.250 x1, 0.283 x3}
- |Ric|^2 = 0.514, Kretschner = 0.535, |Weyl|^2 = 0.386
- a_2^{SD} variation tau=0->fold: 0.91% (tracks R linearly, Vol constant)
- Gate: INFO (structural finding, not pass/fail applicable)
- Files: s46_geometric_a2.py/.npz/.png

## Session 46 Results (SPECTRAL-FLOW-NS-46)
- **SPECTRAL-FLOW-NS-46: FAIL**. alpha_j = 4.03 +/- 0.34 (Casimir k). Outside [0.5, 2.0].
- **alpha decomposition**: alpha_j = alpha_N(1.53) + alpha_d(1.88) + alpha_v(0.62) = 4.03
- alpha_v (velocity only) = 0.62 +/- 0.08 (R^2=0.956). INFO range [0.5, 2.0]
- Eigenvalue-k proxy: alpha_ev = 6.49 (inflated by eigenvalue-wavenumber conflation)
- 992/992 modes matched to fine-scan eigenvalue trajectories (4th-order forward diff, h=0.005)
- v > 0: 712 modes, v < 0: 280 modes. Net flow expanding. 34.5% cancellation
- Near-VH modes: 12 (1.2%), carrying 0.002% of spectral current. VH suppression 794x
- B3 carries 99.95% of total spectral current
- **Velocity-weighted Bogoliubov**: n_s correction delta = -1.18 (right direction, insufficient)
- **STRUCTURAL**: spectral current is UV-dominated (Weyl + dimension + velocity all reinforce)
- Any observable that SUMS over modes inherits Weyl counting alpha >> 1
- Pair creation controlled by BLOCK membership (B1/B2/B3), not Casimir k (confirms W2-2)
- Files: s46_spectral_flow_ns.py/.npz/.png

## Session 46 Results (SPECTRAL-FORM-FACTOR-46)
- **SPECTRAL-FORM-FACTOR-46: INFO**. Universality class: POISSON (HIGH confidence)
- K(t) shows NO ramp (R^2=0.0002). Smoothed K sits at 1/N from dip onward
- <r> = 0.439 (Poisson 0.386, GOE 0.531). Closer to Poisson. S38 CHAOS-1 discrepancy resolved (degeneracy dilution)
- Sigma^2(L) sub-Poisson (GOE-like): arithmetical spectrum from Peter-Weyl structure
- t_H(system, unfolded) = 747.7; t_H(raw) = 203.6
- K_plateau/(1/N) = 1.04 (Poisson confirmed)
- Consistent with block-diagonal theorem, integrability, [iK_7,D_K]=0
- SFF EXCLUDES quantum chaos in single-particle Dirac spectrum. PERMANENT
- Files: s46_spectral_form_factor.py/.npz/.png

## Session 48-49 TT Lichnerowicz Results
- **TT-LICH-48: PASS**. 31 singlet TT modes, ALL positive. See `tt-lichnerowicz-s48.md`
- **NON-LI-TT-49: PASS**. 81 TT modes per (1,0)/(0,1) sector, ALL positive [0, 0.78]. See `non-li-tt-s49.md`
- Casimir gap C_2(p,q)/3 provides structural positive floor for non-singlet modes
- Non-LI modes 3.26x MORE stable than singlet at fold (min 1.047 vs 0.322)
- KK graviton tower positive-definite at fold. PERMANENT

## Session 51 Results (CUTOFF-CONV-51)
- **CUTOFF-CONV-51: FAIL**. SA correlator sector weights NOT cutoff-universal at Lambda=3
- Smooth cutoffs (Gaussian, Poly, SmComp): dim2=64 [(1,1)] has 55.7% rel. variation (FAIL threshold 50%)
- dim2=225 (dominant, >50% weight): STABLE at 4.7%. dim2=100: INFO at 17.2%
- Sharp cutoff pathological: projects 100% weight to single sector near Lambda
- alpha_eff = 0.860 +/- 0.02 (4.7% variation across smooth cutoffs) -- STABLE
- Identity deviation = 0.066 +/- 0.011 (33% variation) -- NOT STABLE
- S50 alpha_eff=1.21 was for P_G*eta_SA product, not standalone SA correlator (alpha=0.86)
- **STRUCTURAL**: chi_SA involves f'(x), not f-moments. Cutoff non-universality is permanent.
- Lambda->infinity converges (all cutoffs agree), but finite Lambda introduces shape dependence
- dim2=225 MIXES (2,1)+(1,2) [C2=5.33] with (4,0)+(0,4) [C2=9.33] -- S50 bug
- Files: s51_cutoff_conv.py/.npz/.png

## Detailed Notes
- See `spectral-results.md` for computation details
- See `tt-lichnerowicz-s48.md` for S48 TT analysis
- See `non-li-tt-s49.md` for S49 non-left-invariant extension
