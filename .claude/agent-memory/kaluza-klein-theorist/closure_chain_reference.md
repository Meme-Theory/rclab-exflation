# V_eff Closure Chain Reference (Sessions 13-20b, compressed)

## Classical V_eff (Session 13)
- V(phi,sigma) = eq 3.80, m^2(phi,sigma) = eq 3.84, V_eff = eq 3.87
- sigma_0 monotonically decreasing in r = kappa_eff/A. Unique minimum for r>0.
- phi direction UNBOUNDED (rescaling instability). Needs separate stabilization.
- 4 parameters: kappa, mu, Lambda, sigma_0

## CW Closure (Session 18)
- 714 scalar + 1456 vector eigenvalues per s-value. No negative eigenvalues.
- CW monotonically decreasing. Fermion-dominated (F/B = 8.4:1).

## False Vacuum Double-Counting (Session 19a)
- F_spectral IS dV_CW/dtau in different notation. "Force balance" reduces to -2*dV_CW/dtau = 0.
- True self-consistency requires D_total = D_K + D_F where D_F depends on eigenvectors.

## Casimir Closure (Session 19d)
- R(tau) = |E_fermion|/E_boson = 9.92 at tau=0. Varies only 1.83% over [0,2].
- DOF ratio: 439,488 fermionic / 52,556 bosonic = 8.36. Combined with <|lam|> ratio: 8.36 x 1.19 = 9.92.
- KEY LESSON: On compact manifolds, fermion/boson DOF ratio dominates ALL polynomial weightings.
- Data bug: kk1_bosonic_spectrum.npz stores mult = dim(p,q)^2 (WRONG). Code API returns dim(p,q) (CORRECT).

## TT Lichnerowicz Closure (Session 20b)
- 741,652 TT DOF at tau=0. All eigenvalues POSITIVE (min mu=1.0).
- E_total = E_boson - E_fermion > 0 at ALL tau. Monotonically increasing. No minimum.
- R = F/B = 0.558 BOSON-DOMINATED (TT flips ratio). Varies only 1.8%.
- CORRECTION: Rough Laplacian on constant tensors is NOT zero (connection terms).
- At tau=0: rough_lap eigenvalues 0.25 (adjoint) and 2/3 (complement). TOTAL m^2 = 1.0 for all 35 modes.
- Koiso-Besse instability is CONFORMAL, not TT. SU(3) is TT-STABLE.
- mps=5 vs mps=6: 68% absolute E_TT difference. R ratio stable (1.8%).

## Cumulative Closure List (all perturbative)
1. V_tree minimum (17a SP-4)
2. 1-loop CW (Session 18) — fermion-dominated, monotone
3. Casimir scalar+vector (19d D-1) — R=9.9 constant
4. Casimir WITH TT (20b) — R=0.55 constant, monotone positive
5. Fermion condensate (19a S-4) — spectral gap > 0
6. Seeley-DeWitt a_2/a_4 (20a SD-1)
7. ALL perturbative spectral mechanisms exhausted. NP physics required.
