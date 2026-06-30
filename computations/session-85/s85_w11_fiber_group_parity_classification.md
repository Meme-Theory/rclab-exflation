# S85 W11-4 Fiber-Group Parity Classification

**Verdict**: PASS
**Value**: preserve=8+flip=4=12,SU3_in_preserve=True
**Tally**: 8 PRESERVE + 4 FLIP = 12

## Classification table

| # | Group | dim_R | mod 2 | Family | Rank | Label |
|:-:|:------|:------|:------|:-------|:----:|:------|
| 1 | SU(2) | 3 | 1 | A_1 | 1 | **FLIP** |
| 2 | SU(3) | 8 | 0 | A_2 | 2 | **PRESERVE** |
| 3 | SU(2)xSU(2) | 6 | 0 | A_1 x A_1 | 2 | **PRESERVE** |
| 4 | SU(3)xU(1) | 9 | 1 | A_2 x u(1) | 3 | **FLIP** |
| 5 | SO(3) | 3 | 1 | B_1 | 1 | **FLIP** |
| 6 | SO(4) | 6 | 0 | D_2 | 2 | **PRESERVE** |
| 7 | SO(5) | 10 | 0 | B_2 | 2 | **PRESERVE** |
| 8 | Spin(5) | 10 | 0 | B_2 | 2 | **PRESERVE** |
| 9 | G_2 | 14 | 0 | G_2 | 2 | **PRESERVE** |
| 10 | F_4 | 52 | 0 | F_4 | 4 | **PRESERVE** |
| 11 | Sp(1) | 3 | 1 | C_1 | 1 | **FLIP** |
| 12 | Sp(2) | 10 | 0 | C_2 | 2 | **PRESERVE** |

## Substitution chain (dim_R mod 2)

The shriek map π_!: K^j(E) → K^{j - dim_R G}(M) shifts K-degree by dim_R G.
Under Z/2 reduction (Chern: K^j → HP^{j mod 2}):

- If `dim_R G ≡ 0 (mod 2)`: π_! preserves HP-parity (HP^0 → HP^0, HP^1 → HP^1).
- If `dim_R G ≡ 1 (mod 2)`: π_! flips HP-parity (HP^0 → HP^1, HP^1 → HP^0).

## Cross-check witnesses

### FLIP witness: SU(2)-Hopf S^7 → S^4 (dim_R = 3)

- Gysin shift: -3
- Input degree: 3 (parity 1)
- Output degree: 0 (parity 0)
- Parity 1 → 0: **FLIP** (matches dim_R=3 odd)

### PRESERVE witness: SU(3)-principal bundle over S^8 (dim_R = 8)

- Gysin shift: -8
- Input degree: 8 (parity 0)
- Output degree: 0 (parity 0)
- Parity 0 → 0: **PRESERVE** (matches dim_R=8 even)

## PASS conditions

- (a) SU(3) = PRESERVE: True
- (b) SU(3)×U(1) = FLIP: True
- (c) ≥1 alternative candidate FLIPS (discriminator): True (FLIP alts: ['SU(2)', 'SO(3)', 'Sp(1)'])
- (d) cross-check witnesses PASS: True

## Structural implication

SU(3)'s disjoint-corridor label stability under π_! is NOT an accident — it is a dim_R-parity consequence. SU(3)×U(1) (the standard Connes-Chamseddine gauge-group extension candidate) FLIPS parity labels under shriek unless the base compensates. This places a non-trivial geometric constraint on any proposed extension of the framework to larger fiber groups: the extension must either preserve even dim_R or introduce a compensating base-side parity flip.

Among the 12 pinned candidates:
- **PRESERVE class** (8 groups, dim_R even): SU(3), SU(2)xSU(2), SO(4), SO(5), Spin(5), G_2, F_4, Sp(2)
- **FLIP class** (4 groups, dim_R odd): SU(2), SU(3)xU(1), SO(3), Sp(1)

SU(3) (dim 8) is the smallest simple non-abelian group that preserves corridor labels under fiber integration; SU(2) (dim 3) does not. The framework's SU(3) choice is thus constrained by submersion-preservation — a structural feature, not a postulate.

Audit SHA: `0658f61d93a976974101ce9d4401c998063967069fa2d6418a81c957fb8888a2`
Content SHA: `a8ace88997c0c93472419fb12c8a086f379b4cc7505fb31df0d3a4b02e3a96a8`