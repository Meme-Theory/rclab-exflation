---
name: elast-z-43-result
description: ELAST-Z-43 computation results. Elasticity tetrad derivation of Z(tau). 8 independent elastic constants. Chain rule correction explains factor 2.09. C2 block U(2) not SO(4).
type: project
---

## ELAST-Z-43: Elasticity Tetrad Derivation of Z(tau)

### Key Numbers at Fold (tau = 0.190)

| Quantity | Value |
|:---------|------:|
| Z_Hessian (C * n * n) | 665,810 |
| d2S/dtau2 (S42 direct) | 317,863 |
| Z_spectral (S42) | 74,731 |
| G_DeWitt (analytic) | 5.0 |
| Z_Hessian / d2S | 2.094 |
| Z_Hessian / G_DeWitt | 133,162 |
| Chain rule correction | -347,948 |
| K_bulk | 11,606 |

### 8 Independent Elastic Constants

| Constant | Value | Notes |
|:---------|------:|:------|
| C_self_su2 = C[0000] | 166,341 | Self-stiffness, su(2) |
| C_cross_su2 = C[0011] | -9,337 | Cross within su(2) |
| C_self_C2 = C[3333] | 104,174 | Self-stiffness, C^2 |
| C_cross_C2 = C[3344] | -5,028 | Cross within complex pair |
| C_u1u1 = C[7777] | 87,324 | u(1) self |
| C_su2_C2 = C[0033] | -3,840 | su(2)-C^2 cross-block |
| C_su2_u1 = C[0077] | -2,907 | su(2)-u(1) cross-block |
| C_C2_u1 = C[3377] | -4,282 | C^2-u(1) cross-block |

### Structural Findings

1. **C^2 block has U(2) symmetry, NOT SO(4)**: C[3344]/C[3355] = 0.794. The complex structure of C^2 = R^4 under U(2) distinguishes within-pair from cross-pair coupling. This is the FIRST computation to detect this symmetry reduction in the elastic response.

2. **Zener anisotropy = 1.000 within each block**: The internal crystal is isotropic within su(2) and within C^2, but anisotropic BETWEEN blocks. Hexagonal-like elastic symmetry.

3. **Chain rule correction (factor 2.09)**: Z_Hessian = C*n*n overestimates d2S/dtau2 by 2.09x because the Jensen parametrization L_I = e^{c_I*tau} is exponential. d2h/dtau2 = c_I^2/2 != 0 generates a first-order correction that partially cancels the Hessian. The correction is -347,948 (52% of Hessian). Stable across tau (2.02-2.16).

4. **Self-stiffness positive, cross-coupling negative**: C_self/C_cross ~ -18 (su2), -21 (C2). This is the elastic signature of volume preservation: swelling in one direction requires compensating shrinkage.

5. **TAU-DYN reinforced**: Z_Hessian = 665,810 is larger than Z_spectral = 74,731, making the dynamical shortfall WORSE.

### Downstream

- The 8 elastic constants are the microscopic input for any off-Jensen perturbation analysis
- The C^2 U(2) symmetry finding constrains allowed off-Jensen deformation directions
- Spectral amplification factor Z/G = 133,162 is the density of spectral states sensitive to geometry

**Why:** Completes the Volovik elasticity tetrad identification for the framework. Provides the microscopic elastic modulus tensor from the known Hamiltonian (Dirac on SU(3)).

**How to apply:** When evaluating spatial modulation of tau (domain walls, fabric texture), use the full 8-constant C tensor, not the block-averaged version. The C^2 U(2) symmetry means off-Jensen perturbations within C^2 split into two classes.
