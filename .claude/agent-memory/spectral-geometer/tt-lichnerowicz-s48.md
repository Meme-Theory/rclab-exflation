---
name: TT Lichnerowicz S48
description: Complete TT 2-tensor Lichnerowicz spectrum on Jensen-deformed SU(3), transversality theorem, sector classification
type: project
---

## TT-LICH-48 Computation Details

### Gate: PASS (all positive, hard/soft confirmed)

### Method
- Lichnerowicz operator Delta_L h_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}
- In (0,0) singlet sector: -nabla^2 = 0 (Casimir = 0), so Delta_L is PURELY ALGEBRAIC
- Constructed symmetric 2-tensor basis (36 modes), projected to TT subspace via SVD of constraint matrix
- Constraint matrix = 1 trace row + 8 divergence rows. SVD determines rank.

### Transversality Theorem (NEW RESULT)
- tau=0: ALL 8 div constraints trivial (Gamma totally antisym on bi-inv). rank=1, n_TT=35
- tau>0: 4 C^2 div constraints activate (fourfold degenerate SV ~ 0.196*tau). rank=5, n_TT=31
- 4 u(2) div constraints remain trivial at ALL tau (Jensen preserves U(2))
- The 4 modes that exit TT at tau=0+ are pure C^2 divergence modes

### Bi-Invariant Eigenvalues (tau=0)
- lambda = 1/3 (deg 27): all sectors mixed
- lambda = 3/4 (deg 8): all sectors mixed
- Trace = 15.0 exactly

### 8-Branch Spectrum at Fold (tau=0.19)
1. 0.32166 (deg 5) HARD pure su(2)
2. 0.32523 (deg 3) C2-C2 (C2=0.69, U1=0.31)
3. 0.34168 (deg 1) U1-mixed
4. 0.34219 (deg 6) C2 pure
5. 0.34494 (deg 8) SOFT pure su(2)-C2
6. 0.34677 (deg 4) U1-mixed
7. 0.62661 (deg 3) U1-mixed (outlier)
8. 0.93867 (deg 1) HARD mixed (outlier)

### Cross-Checks
- S20b no-tachyon: CONFIRMED at 9 tau values
- Trace: Tr(L_TT) = sum(evals) to 1.5e-16
- Self-adjoint: sym error 5e-17
- R(0)=2.0 (err 7e-16), R(0.19)=2.01814 (matches S46)
- Ricci eigenvalues: {0.230x4, 0.250x1, 0.283x3} (matches S46)

**Why:** Foundation for spin-2 mode stability on internal manifold. Required before any graviton spectrum claim.
**How to apply:** When analyzing metric perturbations, the 31-mode TT spectrum with 8-branch structure is the complete singlet-sector input. The lambda_min local maximum near fold connects to van Hove/BCS physics.
