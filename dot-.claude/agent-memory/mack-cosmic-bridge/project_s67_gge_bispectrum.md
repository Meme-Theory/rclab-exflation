---
name: S67 GGE Bispectrum
description: S67 GGE-BISPECTRUM-67 INFO: f_NL=0.853 (equil, c_BLV=0.485), 0.129 (folded, GGE diagonal), 0.56 (multi-branch), total=1.03. Folded shape unique discriminant. Pre-registered 1.12 was arithmetic error.
type: project
---

## S67 GGE-BISPECTRUM-67 Results

### Gate: INFO

The pre-registered f_NL^{equil} ~ 1.12 was an arithmetic error: used (85/324)/c_s^2 instead of (85/324)(1/c_s^2 - 1). Correct value: **0.853**.

### Three Channels

| Channel | f_NL | Shape | Status |
|:--------|:-----|:------|:-------|
| Equilateral (c_s < 1) | 0.853 | Equilateral triangles | FUNCTIONAL-INDEPENDENT |
| GGE diagonal (Poisson) | 0.129 | FOLDED triangles (unique!) | FUNCTIONAL-INDEPENDENT |
| Multi-branch (sudden) | 0.56 | Squeezed triangles | SCHEME-DEPENDENT |
| **Total (quadrature)** | **1.03** | Combined | Mixed |

### Key Results
- f_NL^{equil} = (85/324)(1-c_s^2)/c_s^2 = 0.853 with c_s = c_BLV = 0.485
- Folded bispectrum (k_1+k_2=k_3) from pair momentum conservation -- no inflation model produces this
- 50x above Maldacena consistency relation (0.017) -- expected for c_s < 1
- Consistent with all Planck bounds (f_NL^{equil} = -26 +/- 47)
- NOT detectable by CMB-S4 (sigma=5 for equilateral, SNR=0.17)
- NLO correction from M_3 operator: 1.31 -- comparable to leading order. EFT-MATCHING needed.
- Shape correlations: equil-folded cosine = 0.003 (orthogonal, distinguishable)

### Observational Constraints
- Planck f_NL^{equil} = -26 +/- 47: framework at 0.6 sigma
- Planck f_NL^{folded} = -20 +/- 290: framework at 0.07 sigma
- CMB-S4 sigma(f_NL^{equil}) = 5: insufficient for detection
- Need next-gen survey sigma ~ 0.1 for folded shape

### How to apply
- Quote f_NL^{equil} = 0.853, NOT 1.12 (the pre-registration error)
- The folded shape is THE unique discriminant for Bogoliubov pair creation
- The equilateral channel is functional-independent (from c_BLV)
- NLO correction makes sign determination critical: EFT-MATCHING-67 resolves
- Multi-branch channel depends on acoustic/Leggett partition (scheme-dependent)
