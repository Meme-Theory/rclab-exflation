# Chirality Resolution (Session 11)

## The Catch-22
- Block-diagonal D_F: [D_F, gamma_F]=0 (WRONG, NCG requires anticommutation)
- Off-diagonal D_F: {D_F, gamma_F}=0 (correct) but ad hoc operators failed order-one

## Resolution: Lichnerowicz Theorem
- On any even-dim Riemannian spin manifold (M^{2n}, g), {D, gamma}=0 automatically
- SU(3) is 8-dim (n=4). D_K anticommutes with gamma_K^(9) = gamma_F
- D_K is NECESSARILY off-diagonal in Psi_+/Psi_- decomposition
- Proof: <psi_n|D_K|psi_m> = -<psi_n|D_K|psi_m> => 0 for same-chirality states

## gamma_PROD Correction
- gamma_PA = particle/antiparticle grading, gamma_CHI = internal chirality
- gamma_PROD = gamma_PA * gamma_CHI = correct grading for NCG
- KO-dim 6 PRESERVED; block-diagonal Connes Yukawa ANTICOMMUTES with gamma_PROD

## Key: Order-One Is gamma_F-Independent
- [[D, pi(a)], J pi(b*) J^{-1}] depends on D, pi(a), J but NOT gamma_F
- Changing gamma_F fixes chirality, zero effect on order-one
- The 4/9 {C,H} failures are SEPARATE from chirality

## -2y Structural Factor (Persists)
- [[D, C_Im], o(C_Im)] on nu_R->nu_L = -2y (exact, nonzero for any y!=0)
- Resolution requires actual D_K matrix elements from geometry
