# Tier 0 Branching Result (compressed)

## Result: End_{U(2)_LR}(Psi+) = C + M_2(C) + M_3(R) + R (dim_C=20). NOT A_F.
- No H factor (Y!=0 doublets are complex, not pseudoreal)
- M_3(R) not M_3(C) (Y=0 singlets are real type)
- Full gauge commutant (L_{u2}+R_{su3}) = C^6 (commutative)

## Branching Table (L+R u(2) on 16-dim Psi+)
| Y | j | dim | mult | Factor |
|---|---|-----|------|--------|
| +/-3.0 | 0 | 1 | 1 | C |
| +/-1.5 | 1/2 | 2 | 2 | M_2(C) |
| 0 | 0 | 1 | 3 | M_3(R) |
| 0 | 1 | 3 | 1 | R |

## Resolution: A_F is NOT the commutant
- A_F is the algebra; gauge group = U(A_F). Correct question: does A acting on Delta_8 exist with axioms?
- J converts: M_2(C)->H (reality), M_3(R)->M_3(C) (complexification from particle+antiparticle)
- Script: `tier0-computation/branching_computation.py`
