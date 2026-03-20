# Baptista-Spacetime-Analyst: Project-Wide Findings

Promoted from agent memory — these results affect ALL agents in the project.

## Verified Equation Table

All pass at machine epsilon (~1e-15).

| Eq | Paper | What | Script |
|----|-------|------|--------|
| 2.12 | 14 | hat{Xi} charge conjugation | branching_computation_32dim.py |
| 2.19 | 14 | conjugate rep rho_- | branching_computation_32dim.py |
| 2.62 | 14 | L,R actions on Psi_+ | branching_computation.py |
| 2.65 | 14 | R homo, L not (= order-one constraint) | branching_computation.py |
| 2.66 | 14 | SM particle ID | branching_computation.py |
| 3.61 | 15 | U(2) embedding | branching_computation.py |
| 3.68 | 15 | Jensen scale factors | tier1_dirac_spectrum.py |
| 3.70 | 15 | scalar curvature R(s) | tier1_spectral_action.py |
| 3.72 | 15 | volume preservation | tier1_dirac_spectrum.py |
| 3.80 | 15 | classical V(sigma,s) | tier1_spectral_action.py |
| 3.84 | 15 | gauge boson mass | tier1_spectral_action.py |

## Self-Consistent Freeze-Out Impossibility
- H(t) < c_s/d_mean for ALL R when alpha=0.667
- Exponent: 1/alpha - 1 = 0.5 > 0, so the ratio GROWS with expansion
- Freeze-out is INTERNAL (V_eff minimum / sigma stabilization), NOT dynamical decoupling
- Phase 4a (coupled V_eff ODEs) is ESSENTIAL — Boltzmann sigmoid is phenomenological placeholder

## Three-Level Structure
- **Level 1** (CG / topological / s-independent): determines A_F (algebra). Jensen deformation does NOT affect this.
- **Level 2** (CG values / metric-dependent): determines coupling constants. Depends on s.
- **Level 3** (Dirac spectrum / dynamics): determines masses. Requires D_K eigenvalues at specific s.

## Fock Space Landmine
- KK framework derives single-particle QM (kinematic structure from L^2(K))
- Does NOT derive: multi-particle structure, identical particle statistics, spin-statistics theorem
- This is a KNOWN GAP, not a refutation — comparable to decoherence theory in scope

## D_K Identification
- delta_v from eq 2.65 is NOT D_F — it CONSTRAINS D_F (order-one condition) but does not define it
- D_F = D_K (Dirac operator on internal space K = SU(3))
- D_K anticommutes with Gamma_K by Lichnerowicz theorem (automatic, not tuned)
- D_K commutes with R_{su(3)} for left-invariant metrics (Killing isometries)
- [D_K, L_X] != 0 for non-Killing X — THIS is the chiral fermion mechanism (Paper 17 eq 1.4)

## gamma_F Identification Issue
- gamma_F = diag(+I_16, -I_16) is particle/antiparticle split, NOT internal chirality
- Correct internal chirality grading = Gamma_K (from spin geometry on K)
- KO-dim = 6 SURVIVES with corrected gamma_F (verified computationally)
