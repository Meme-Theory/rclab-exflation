---
name: S65 SHELL-L4-65 Results
description: L_max=4 shell Hessian UV convergence test - FAIL (ratio 3.511) but signature preserved
type: project
---

## S65 SHELL-L4-65: L_max=4 Shell Hessian UV Convergence Test

Gate: **FAIL**. ||H^{(4)}||_F / ||H^{(3)}||_F = 3.511 > 2.0 (divergent).

**Why:** The one-loop Hessian sum over PW shells diverges as ||H^(L)||_F ~ 31.65 * L^{3.36}. This is the standard QFT UV divergence for dim(K)=8: density of states ~ L^7, regulator ~ L^{-4}, net ~ L^3.

**How to apply:** The spectral action MUST include the cutoff function f(D^2/Lambda^2) for finiteness. Raw one-loop sums diverge. BUT:

### Key structural results (PERMANENT):
1. **SIGNATURE UV-STABLE**: (36+, 0-) at both L_max=3 and L_max=4. Fold is minimum in ALL directions. Each shell adds positive-definite correction. This is structural: Tr ln(D^2) > 0 for positive eigenvalues.
2. **PER-MODE CONTRIBUTION DECREASING**: 0.1513 -> 0.1270 -> 0.1163 -> 0.1116 -> 0.1092 (L=0..4). Individual modes do not grow. The divergence is purely combinatorial (mode counting).
3. **CONJUGATION SYMMETRY EXACT**: ||H^{(p,q)}|| = ||H^{(q,p)}|| to machine epsilon.
4. **EIGENVALUE AMPLIFICATION UNIFORM**: All 36 eigenvalues scale by 4.97x (range 4.82-5.64) from L3 to L4. No mode becomes preferentially enhanced.

### Quantitative
- L=4 shell: ||H^(4)||_F = 4074.21 (79.9% -> 73.7% of total shifts from L=3 to L=4)
- Shell ratios decreasing: 15.1, 6.91, 4.59, 3.51 — series appears to approach a finite limit
- Min eigenvalue: 31.04 (L3) -> 174.98 (L4), increased by 143.94
- Computation: 637.5s, 5 irreps [(4,0),(0,4),(3,1),(1,3),(2,2)], 1332 Dirac diags

### L=4 per-irrep
| (p,q) | dim | ||H|| |
|---|---|---|
| (4,0) | 15 | 391.19 |
| (0,4) | 15 | 391.19 |
| (3,1) | 24 | 1007.13 |
| (1,3) | 24 | 1007.13 |
| (2,2) | 27 | 1277.57 |

### Implication
Fold stability (signature) is a UV-robust structural result. Quantitative eigenvalues require specifying the spectral action cutoff. L_max=3 truncation gives correct topology but underestimates eigenvalues by ~5x.

Files: `computations/s65_shell_l4_hessian.{py,npz,png}`
