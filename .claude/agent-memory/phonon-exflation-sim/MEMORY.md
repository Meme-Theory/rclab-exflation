# Phonon-Exflation Simulation Specialist Memory

## Active Context

### Project Structure
- **Root**: `C:\sandbox\Ainulindale Exflation\`
- **Tier0 scripts**: `tier0-computation/` (all NCG spectral computations)
- **GPE sim**: `phonon-exflation-sim/src/` (dormant since Session 14)
- **Python**: `phonon-exflation-sim/.venv312/Scripts/python.exe` (ALWAYS use this)

### Core Scripts
- `tier1_dirac_spectrum.py` (~1600 lines): Peter-Weyl Dirac, D_K, D_F, eigenvectors, Lie derivatives
- `tier1_spectral_action.py` (~1550 lines): 14 modules, spectral action, Seeley-DeWitt

### Structurally Proven (machine epsilon)
- KO-dim = 6 (S7-8). SM quantum numbers from Psi_+ = C^16 (S7).
- [J, D_K(tau)] = 0 identically -- CPT hardwired (S17a)
- g1/g2 = e^{-2tau} structural identity (S17a B-1)
- D_K block-diagonal in Peter-Weyl for ANY left-invariant metric on compact Lie group (S22b)
- phi_paasch: m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 (S12)
- Constant-ratio trap: F/B = 0.55 full spectrum (S21a)
- Riemann 147/147 (S20a). TT no tachyons (S20b). Volume-preserving TT (S12).
- AZ class BDI, T^2=+1 (S17c). 67/67 Baptista geometry (S17b).
- D_F chirally graded, anti-Hermitian, D_F(tau=0)=0 exactly (S30Aa)

### Key Closures
- CW-1: CW monotonically increasing (S18). V_spec monotone VSPEC-1 (S24a).
- BCS-1: mu=0 subcritical, M_max=0.08-0.15 (S23a/26). V(gap,gap)=0 exactly (selection rule).
- L-1: Thermal F(tau;T) monotone at ALL T (S28a). FR-1: settling time >> age (S22d).
- BA-31-fr: Freund-Rubin monotone (S31Aa). Wall 4 on full 2D U(2) surface (S30Ba).
- B-30min: No interior V_total minimum. V_spec/F_BCS ~ 8000 (S30Ba).
- B-29f: Z_2 = +1 (TRIVIAL) at ALL tau. Topological route exhausted (S30Ab).
- phi-Weinberg anti-correlation: STRUCTURAL, Delta_tau ~ 0.4, no eps bridges (S30Bb).

### Active Landscape (Sessions 29-32)
- Formula B: sin^2 = 3*L2/(L1+3*L2). SM contour at tau~0.575.
- Candidate 1 (tau=0.18, eps=-0.135): phi=1.521, DOS=62, sin2_B=0.585
- Candidate 2 (tau=0.575, eps=-0.005): sin2_B=0.231, phi=1.323 FAIL
- Branch structure: B1(1)+B2(4)+B3(3). B2 perfectly 4-fold degenerate.
- s23a eigval ordering: cols 0-2=-B3, 3-6=-B2, 7=-B1, 8=+B1, 9-12=+B2, 13-15=+B3
- J_perp = 1/3 exactly (Schur orthogonality, S29Aa)
- t_BCS = 1.3e-41s. Gi=0.36. Mean-field reliable (S29Ab).
- N_max convergence: phi_30 and lambda_min identical at N_max=3,4,5,6.

### Session 33a Results (Task #5)
- W3-33a gate: PASS. 1288 exact mass ratios scanned across 17 theory categories.
- Closest match: 2*cos(2*pi/9) = 1.532089, deviation 0.033% from phi_paasch. A_8 Toda m4/m2.
- sqrt(7/3) = 1.52753 also within 2% (0.26%), triggering W_3-specific PASS.
- 118 matches within 5%, 39 within 2%. phi_paasch sits in a dense region of Toda ratios.
- Key insight: 2*cos(2*pi/9) is degree-3 algebraic over Q, same as rank of SU(3).
- Output: `tier0-archive/s33a_w3_kink_masses.{py,npz}`

## Reference Index
- `ncg-foundations.md` -- Sessions 7-12,16: KO-dim, branching, chirality, CW, performance
- `session22b_lessons.md` -- D_K block-diag proof, eigenvectors, bugs, UV tail
- `session23a_bcs.md` -- BCS gap eq, V(gap,gap)=0, Kosmann formula, mu=0 closure
- `session26-bcs.md` -- Multi-mode BCS, [V,J]!=0 structural, no tau lock
- `session27-torsion-gate.md` -- T-1 PASS, canonical connection, gap weakening
- `sessions-28-29-detail.md` -- KC-1, L-1, L-7, L-3, L-9, S-3, K-29a-d, B-29a/d, P-29c/e
- Constraint map: `.claude/agent-memory/constraint-map.md` (project-level)

## Key Constants & Equations
- D is anti-Hermitian. R=+2 for g=-Killing=3*I. Killing sign: use |B| not -B.
- Ricci: Ric_{ac} = R^b_{bac}. R(0)=+2.0, Ric=+1/4*I.
- sqrt(7/3)=1.52753, 0.26% of phi_paasch=1.531580. Algebraic invariant of bi-invariant SU(3).
- K_a = (1/8) sum_{r,s} [Gamma[s,r,a]-Gamma[r,s,a]] * gamma_r*gamma_s (ANTISYMMETRIC)
- L_{e_a} = rho_ON(e_a) x I + I x (omega_a + K_a). omega_a = (1/4)Gamma[b,a,c]*gamma_b*gamma_c.
- Pfaffian: Pf(total) = Pf(0,0)*[Pf(0,1)]^2*[Pf(0,2)]^2*Pf(1,1). Conjugate pairs squared out.
- V_nm formula: V_nm = -sum_{a=3..6} |<n|K_a|m>|^2
- sin^2(theta_W) Formula B: 3*L2/(L1+3*L2) (Paper 14 eq 2.85-2.93)
- N_max=6: 28 sectors, 11424 eigenvalues, ~14s/point. Largest: (3,3)=1024x1024.
- D/H = 2.737e-5 (GPE, N=1024): tau_Q=50, tau_exp=2.0, alpha=0.667, gamma0=0.1, R_freeze=3.0

## Debugging Notes
- **Signed sums**: For Dirac with particle-hole symmetry, NEVER use unsigned sums. ALWAYS weight by sign(lambda_k) for spectral action. sum_{k!=n} |V_kn|^2/(lk-ln) = 0 is IDENTITY (S32b).
- **Freudenthal BFS**: Can infinite-loop. Use hardcoded branching table from s21c.
- **eigh pitfall**: Add absolute floor eta=max(eta_frac*lmin, 1e-15). tau=0 fully degenerate.
- **Dict coverage**: Always verify dict keys match data coverage (28 sectors at pq<=6).
- **G5 != gamma9**: G5=diag from gamma_5 cols. gamma9=Spin(8) chirality. Different operators.
- **Xi_ext construction**: Each sector pairs with OWN charge conjugate, NOT contragredient sector.
- **build_cliff8()**: Correct function name in tier1_dirac_spectrum.py (not clifford_generators).
- **_irrep_cache**: s-INDEPENDENT. No need to clear between s-values.
