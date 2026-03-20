# Session 22b: D_K Block-Diagonality + Bugs

## D_K Block-Diagonality (PROVEN)
- EXACTLY block-diagonal in Peter-Weyl for ALL tau.
- Mechanism: (L_g)^{jk} symmetric, [gamma_j,gamma_k] antisymmetric -> contraction=0. Tr(L_g)=0 (vol-preserving).
- Off-diagonal max|elem| = 0.00e+00. PB-1 through PB-4 trivially identity.

## PA-1 Eigenvector Extraction
- Script: `s22b_eigenvector_extraction.py`, data: `s22b_eigenvectors.npz` (23.8 MB)
- 1232 modes/tau, 10 sectors (p+q<=3), 9 tau. Uses eigh on H_pi = 1j*D_pi.

## Bugs (avoid repeating)
- **dT_b2 sign**: must use -prefactor (s21c convention), not +prefactor
- **Dict lookup coverage**: always verify dict keys match data coverage (p+q<=6, 28 sectors)
- **Freudenthal BFS**: infinite loop possible; use hardcoded branching table from s21c

## Key Numbers
- delta_T(0.30, pq<=3)=6.39; delta_T(0.30, pq<=6)=1080.71 (matches s21c)
- UV tail: sectors p+q=4,5,6 carry 99.4% of signal (169.2x ratio)
