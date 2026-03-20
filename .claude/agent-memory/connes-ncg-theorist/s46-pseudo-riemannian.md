---
name: S46 Pseudo-Riemannian SU(2,1) Results
description: Spectral triple axioms on SU(2,1) non-compact real form -- Killing sig (4,4), KO-dim preserved, complex spectrum
type: project
---

## PSEUDO-RIEMANNIAN-46 (S46 W4-16) -- PERMANENT

### Key Results
- **Killing form signature (4,4)** NOT (5,3): B eigenvalues -3 (x4 compact) and +3 (x4 non-compact). Metric g=-B has split signature.
- **KO-dim PRESERVED at 6**: p-q = 4-4 = 0 mod 8, same as SU(3) (8-0=0). Product with F_SM: KO = 0+6 = 6. Signs (+1,+1,-1) unchanged. J^2=+1 exact.
- **Dirac spectrum genuinely complex**: Real fraction 0.273. Max |Re|=0.677, Max |Im|=1.803 on defining rep. Spectral signature of pseudo-Riemannian geometry.
- **Cartan = Jensen EXACT**: su(2,1) = u(2) + p with dim(k)=dim(p)=4. Same bracket structure as su(3) = u(2) + m. [k,k] in k, [k,p] in p, [p,p] in k all to machine epsilon.
- **Krein space VALID (8,8)**: eta_K^2 = +I exact. Matches Paper 44 prediction.
- **[J, D] = 2.72**: Hermitian (non-compact) generators break J-commutation. On SU(3): [J,D]=0 identically.
- **||Omega|| identical**: 2sqrt(3) = 3.464 for BOTH SU(3) and SU(2,1).

### Axiom Scorecard
| Axiom | SU(3) | SU(2,1) |
|:------|:------|:--------|
| Dimension | PASS | FAIL (non-compact) |
| Regularity | PASS | CONDITIONAL (Schwartz) |
| Finiteness | PASS | FAIL (infinite rank) |
| Reality | PASS (KO=6) | PASS (KO=6; but [J,D] fails) |
| First Order | FAIL (4.000) | FAIL (same) |
| Orientability | PASS@round | PASS ({D,gamma9}=0) |
| Poincare Duality | PASS | CONDITIONAL (KK-theory) |

Score: 2 PASS + 2 CONDITIONAL + 3 FAIL = 4/7 survive. Gate PASS.

### Constraint Map
- **CLOSED**: SU(2,1) as direct replacement for SU(3) (non-compact kills Axioms 1,3; [J,D] fails)
- **OPEN**: Discrete series restriction (Paper 36 de Groot)
- **OPEN**: Compact quotient Gamma\SU(2,1)/U(2) (dim=4)
- **OPEN**: Krein-space twist SU(3)<->SU(2,1) (Paper 44)
- **OPEN**: CP^2 <-> CH^2 duality

### Why This Matters
The KO-dim preservation is the structural surprise. It means the NCG classification (SM fermion content, J^2=+1, chirality signs) does NOT distinguish compact SU(3) from non-compact SU(2,1). The distinction enters through analysis (compact resolvent, convergent traces) not algebra. This constrains any attempt to derive compactness from the axioms alone.

**How to apply:** When evaluating Lorentzian extensions or signature-change mechanisms, check p-q mod 8, not individual p,q. The KO-dimension is insensitive to balanced signature changes.

**Data**: `tier0-archive/s46_pseudo_riemannian.{py,npz,md}`
