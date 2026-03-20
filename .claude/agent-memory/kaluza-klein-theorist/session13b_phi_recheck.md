# Session 13b: Phi Recheck (compressed)

## Computation Verification: ALL CLEAR
- Structure constants: Jacobi 3e-16, f_abc real, antisymmetric. Killing: B_ab = +3*delta (anti-Hermitian).
- Jensen metric: volume-preserving confirmed. Connection Gamma=ft/2 at s=0.
- Omega: anti-Hermitian at ALL s. Torsion-free: machine eps. SU(2) benchmark: 8.88e-16.

## Key Findings
1. **IVT margin = 0.38%**: (3,0)/(0,0) starts 1.5275, max 1.5374 at s~0.08, crosses phi at s~0.15. Near-miss.
2. **(3,0) UNIQUELY saturates Parthasarathy bound**: Only sector (up to conjugates, p+q<=3) where pred = actual min.
3. **s=ln(phi) is TAUTOLOGY**: For ANY x>1, s=ln(x) gives scale factors x^2, 1/x^2, x. Moreover s=ln(phi)=0.43 != s=0.15.
4. **sigma doesn't select psi_0=0.15**: Both sigma<0 and sigma>0 push psi_0 toward 0.
5. **V_eff has FOURTH parameter (mu)**: psi_0=0.15 needs kappa~212 (unnatural). psi_0=0.43 needs kappa~4.6 (natural but ratio=1.48, below phi).

## Eigenvalue Data (s=0, lambda^2*36)
| Sector | Values | Parthasarathy pred | Match? |
|--------|--------|--------------------|--------|
| (0,0) | {27} | 9 | NO |
| (1,0) | {25,37,49} | 21 | NO |
| (1,1) | {27,45,63,75} | 36 | NO |
| (2,0) | {37,49,61,79} | 39 | NO |
| (2,1) | {49,61,73,91,97,109} | 57 | NO |
| (3,0) | {63,81,93,117} | 63 | YES |
