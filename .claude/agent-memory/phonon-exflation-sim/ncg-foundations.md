# NCG Foundations (Sessions 7-12, 16)

## Session 7: Branching (branching_computation.py)
- End_{U(2)}(Delta_8) = C + M_2(C) + M_3(R) + R (real dim 20)
- Two methods agree (Schur + null-space). 17 checks at machine epsilon.
- Y eigenvalues: {-3, -1.5, 0, 1.5, 3}. C_2: {-2, -0.75, 0}.
- Casimir: j(j+1) = -c2_val (anti-Hermitian convention).

## Session 8: J-Compatible Commutant (branching_computation_32dim.py)
- J = Xi o conj, Xi = (0, -G5; -G5, 0). J^2=+I. KO-dim=6.
- G5 sign: row-dependent vs column-only = ISOMORPHIC algebras (proven).
- R_{u(2)} is ONLY gauge giving center=5, factors=3 (matches A_F).
- But dim=128 >> 24. Order-zero fails for all choices.

## Session 10: Explicit A_F (branching_computation_phase2b.py, ~1624 lines)
- Order-one subalgebra under any Yukawa D_F = dim 20 (NOT 24).
- Eigenvalue gap: 10^15. Constrained eigenvalues: 20/3 and 40/3.
- Wedderburn: C(2) + M_3(C)(18). Center=4. Semisimple.
- H (quaternions) missing: requires column mixing (right mult).
- A_F extraction requires FULL bimodule L.X.R, not commutant alone.

## Chirality Resolution (Session 11)
- gamma_PROD = gamma_PA * gamma_CHI solves catch-22.
- KO-dim=6 preserved. {D,gF}=0 and order-one both satisfied for block-diag D_F.
- Barrett classification: valid spectral triple guaranteed.
- Scripts: session11_chirality_exploration.py, session11_gamma_product.py

## V_eff / CW Analysis (Sessions 14-18) -- Constraint CW-1
- Full CW with ALL modes: monotonically increasing from tau=0.
- 52,556 bosonic vs 439,488 fermionic DOF at pq<=6. Fermions 8.4:1.
- Zeta-regularized V_zeta also monotonically increasing.
- phi^{3/2} = 1.8954 (appears in CW formula).
- Baptista 4-boson: V_eff min at tau=0.3-0.6, but phi at tau=0.15. INCOMPATIBLE.

## Performance Notes
- _irrep_cache is s-INDEPENDENT (no need to clear between s-values)
- eigvalsh(1j * D_pi) gives ~10x speedup over eigvals(D_pi) for Hermitian Dirac
- ~8.7s/point at pq<=6. Freudenthal BFS can infinite-loop: use hardcoded branching table.
