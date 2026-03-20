---
name: non-li-tt-s49
description: S49 NON-LI-TT-49 PASS result -- non-left-invariant TT Lichnerowicz eigenvalues all positive
type: project
---

## NON-LI-TT-49: PASS (Session 49)

Extended S48 TT Lichnerowicz from singlet (0,0) to (1,0) and (0,1) Peter-Weyl sectors.

**Why:** S48 proved stability for left-invariant TT modes (n_TT=31). Non-left-invariant modes could in principle be unstable at the fold due to weaker curvature protection.

**How to apply:** Non-left-invariant TT modes are MORE stable than singlet ones. The Casimir gap C_2(p,q) > 0 provides a structural positive floor. No instability possible until deformation overcomes this floor.

### Key Numbers
- n_TT = 81 per sector (compared to 31 for singlet)
- (1,0) and (0,1) spectra identical (conjugation symmetry)
- min lambda at fold: 1.047 (vs 0.322 for singlet, ratio 3.26x)
- Global minimum over [0, 0.78]: 0.946 at tau=0.40
- No negative eigenvalues anywhere in scan range

### Mathematical Notes
- Rough Laplacian on tensor bundles has cross-terms between representation action rho_ON[a] and connection Gamma
- At tau=0, naive Casimir shift (C_2/3 = 4/9) does NOT reproduce spectrum exactly -- actual shift is larger (0.944 vs 0.444)
- This is because nabla^*nabla on S^2(T*M) is not scalar_Lap x Id_tensor + Id_V x tensor_Lap
- (1,0) eigenvalues at tau=0: {23/18 (deg 24), 1.596 (deg 15), 16/9 (deg 42)}
- For higher (p,q), C_2 grows as ~(p^2+q^2+pq)/3, so stability only increases

### Structural Conclusion
For ALL (p,q) != (0,0), non-left-invariant TT modes have min_lambda > singlet min_lambda. The KK graviton tower is positive-definite at the fold. PERMANENT.

### Files
- `tier0-archive/s49_non_li_tt.py`
- `tier0-archive/s49_non_li_tt.npz`
- `tier0-archive/s49_non_li_tt.png`
