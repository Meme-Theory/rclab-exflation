# Foundations Detail (Sessions 3-11)

## CG Algebra and Fiber Integration (Session 6)
- Baptista's Haar integrals (Paper 14, eqs 2.25, 2.37) ARE CG selection rules
- integral_K h v h^T vol_K = 0: integration selects SINGLET, closes OCTET
- Jensen deformation preserves CG selection rules (vol_{g_s} = vol_{g_0}, metric-independent)
- R: su(3)->End(M_{4x4}) IS a homomorphism; L|_{u(2)} IS; L: su(3) is NOT (v_11 term = Higgs)
- Three-level structure: (1) CG rules->A_F [invariant], (2) CG values->couplings [s-dep], (3) Dirac spectrum->masses [s-dep]

## Phase 1: Psi_+ = C^16 (Session 7)
- eq 2.62 (L_v, R_v actions): PASS at machine epsilon
- eq 2.65 (L+R homomorphism, L failure on C^2): PASS -- failure = Higgs
- End_{U(2)_{L+R}}(Delta_8) = C + M_2(C) + M_3(R) + R (mismatches resolved in Phase 2)

## Phase 2: Full 32-dim H_F with J (Session 8)
- **KO-dim = 6 mod 8** from (epsilon, epsilon', epsilon'') = (+1, +1, -1) -- parameter-free
- J^2 = +I, J commutes with gauge, J*gamma = -gamma*J -- all at machine epsilon
- J-compatible commutant: dim 80 (order-zero needed to select A_F)

## R_{u(2)} Gauge Justification (Session 9)
- R_{u(2)} uniquely gives center=5, factors=3 matching A_F
- R_{u(2)} = opposite algebra action A_F^o = J*A_F*J^{-1} (NCG derivation)

## s-Independence
- ALL Phase 1-2 inputs are algebraic/metric-independent
- Gauge structure topologically fixed for all Jensen parameters s

## Chirality Resolution: D_K = D_F (Sessions 10-11)
- **Catch-22**: Block-diagonal D_F passes order-one but COMMUTES with gamma_F (wrong chirality); off-diagonal anticommutes but FAILS order-one
- **Resolution** (5/5 unanimous): delta_v (eq 2.65) is CONSTRAINT, not D_F. True D_F = D_K on (SU(3), g_s)
- D_K anticommutes with Gamma_K (Lichnerowicz) -> chirality automatic
- D_K commutes with R_{su(3)} (Killing isometries) -> order-one automatic
- gamma_F = diag(+I_16, -I_16) is particle/antiparticle, NOT internal chirality. Correct gamma_F = Gamma_K.
- Three generations: G = (SU(3)xSU(3))/Z_3, center Z_3xZ_3. Second Z_3 -> 3 generations (Paper 18 App E).

## QM Emergence (Sessions 4-5)
- L^2(K, S_K) provides Hilbert space for single-particle internal DOF
- Born rule DEFENSIBLE (Gleason's theorem, dim >= 3)
- Bell classification OPEN (bipartite CHSH from K x K uncomputed)
- **Fock space LANDMINE**: L^2(K) = single particle only, no derivation of identical particles

## GPE Simulation (Session 3)
- D/H = 2.737e-5 vs observed 2.527e-5 (8% match) at 1024x1024
- Self-consistent freeze-out FAILS: H(t) < c_s/d_mean for ALL R up to 13.8
- Phase 4a: coupled ODEs from eqs 3.79-3.80 (sigma, psi fields)

## Key Equations (Foundations)
| Eq | Paper | Role |
|----|-------|------|
| 2.25, 2.37 | 14 | Fiber integration = CG selection rules |
| 2.62 | 14 | L_v, R_v actions on Psi_+ |
| 2.65 | 14 | L-failure = Higgs = order-one CONSTRAINT |
| 3.8 | 17 | D_P decomposition: D_K provides mass term |
| 1.4 | 17 | [D_K, L_X] = chiral fermion mechanism |
| 7.5 | 18 | Dim-reduced Dirac: M = <phi, D_K phi> = D_F |
| App E | 18 | Z_3 x Z_3 -> three generations |
