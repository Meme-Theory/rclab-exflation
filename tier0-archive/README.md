# Tier 0 Discriminator: Branching Delta_8|_{U(2)}

## What This Computes

This script computes the branching of the Spin(8) internal spinor representation
Delta_8 (Baptista's 16-dimensional Psi_+) under U(2), and determines the
commutant algebra End_{U(2)}(Delta_8). The goal is to check whether this
commutant equals Connes' finite algebra A_F = C + H + M_3(C).

## How to Run

```bash
python branching_computation.py
```

Requirements: Python 3.8+, numpy, scipy. No SageMath needed.

## What to Expect

The script runs through 12 analysis parts:

1. **Parts 1-2**: Constructs the su(3) basis, U(2) embedding, and L/R action matrices
2. **Part 3**: Validates the construction (anti-Hermiticity, homomorphism checks, traces)
3. **Part 4**: Decomposes Delta_8 under U(2) via simultaneous diagonalization of Y and C_2
4. **Part 5**: Cross-checks decomposition using T_3 weight diagrams
5. **Part 6**: Determines representation types (real/complex/quaternionic) and reads off commutant
6. **Part 7**: Independent check via direct null-space computation
7. **Part 8**: Identifies each basis vector with SM fermion particles
8. **Part 9**: Analyzes L and R actions separately
9. **Part 10**: Computes commutant under full SM gauge group (L on u(2) + R on su(3))
10. **Part 11**: Full decomposition under separate L|_{u(2)} x R|_{su(3)}
11. **Part 12**: Synthesis and interpretation

## Key Result

The branching Delta_8|_{U(2)} (via L+R combined action) gives:

| Y (hypercharge) | j (isospin) | dim(irrep) | mult | Type |
|---|---|---|---|---|
| +/-3.0 | 0 | 1 | 1 | Complex |
| +/-1.5 | 1/2 | 2 | 2 | Complex |
| 0.0 | 0 | 1 | 3 | Real |
| 0.0 | 1 | 3 | 1 | Real |

**Commutant**: End_{U(2)}(Delta_8) = C + M_2(C) + M_3(R) + R

**This is NOT A_F = C + H + M_3(C)**

However, the result is physically correct (SM quantum numbers match exactly)
and the commutant is a semisimple algebra with a structure reminiscent of A_F.
Three key differences: no quaternionic H factor, M_3(R) instead of M_3(C),
and an extra R factor.

## Why This Matters

The full SM gauge commutant (Part 10) has dimension 6 (= C^6, one factor per
fermion type), which is commutative. The L+R commutant is larger (dim 20) but
still not A_F. The NCG framework requires including the antiparticle sector
Psi_- and the real structure J (charge conjugation) to potentially obtain A_F.

## Next Steps

1. Include the full [Psi_+ | Psi_-] space (32 dimensions) with charge conjugation J
2. Determine if J converts the types (M_2(C) -> H, M_3(R) -> M_3(C))
3. Reformulate: instead of computing End_G(V), find an algebra A acting on V
   whose unitary group generates the correct gauge transformations

## References

- Baptista arXiv:2105.02901v1 (fermion construction, eq 2.62, 2.65, 2.66)
- Baptista arXiv:2306.01049 (2024, U(2) embedding, eq 3.57-3.62)
- Connes-Chamseddine-Marcolli arXiv:0706.3688 (A_F definition)
