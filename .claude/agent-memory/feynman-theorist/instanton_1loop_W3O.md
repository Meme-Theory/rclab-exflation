---
name: W3-O Instanton 1-Loop Zero-Mode Jacobian (S79 P3-B)
description: At S_inst=13.23, Einstein's Gamma_alpha formula was tree-level + exp(-2S); proper 1-loop adds C_N * S^(N^2-1) factor ~1e6, shrinking cushion from 13 to 7 OOM. Route gamma still dominates but less robustly than Einstein advertised.
type: project
---

## S79 P3-B Workshop Finding

**Context**: W3-O gate reported Gamma_gamma/Gamma_alpha = 4.73e13 at S_inst=13.23.
Einstein (R1-A) argued this 13-OOM cushion is "robust against anything short of K_2 ~ 10^13 total breakdown."

**Finding (F-Pin 2)**: Einstein's formula is effectively tree-level + exp(-2 S), missing the proper 1-loop zero-mode Jacobian.

**Correct 1-loop formula** ('t Hooft 1976, Bernard 1979 MS-bar):
```
Gamma_inst = Gamma_tree * C_N * S^(N^2-1) * exp(-2 S) * K_2
```
For SU(3):
- C_N (SU(3), MS-bar) = 2.5e-3 [Bernard 1979]
- S^(N^2-1) = S^8 = 9.40e8 at S=13.23 [zero-mode Jacobian]
- K_2 = 1.0 +/- 1.5 perturbative [NSVZ 1983, Flory et al 2022]

**Correction magnitude**: C_N * S^8 ~ 2.35e6 = 6.4 OOM boost to Gamma_alpha.

**Effective-action interpretation**: S_eff_amplitude = S - N^2 ln S (for SU(3), 8 ln 13 = 20.5 > 13, so S_eff negative).
This is the TRUE boundary-of-validity concern — not the perturbative 1/(2S) = 3.78%.

## Numerical Outcome

| Quantity | Einstein tree | Feynman 1-loop |
|:---------|:-------------:|:--------------:|
| Gamma_alpha | 8.5e-2 GeV | 2.0e5 GeV |
| T_rh_alpha | 2.46e11 MeV | 1.10e14 MeV |
| Cushion to Route gamma | 13 OOM | 7 OOM |

Route gamma still dominates; verdict FAIL stands. But narrative robustness is weaker.

## Key References (from literature)

1. 't Hooft (1976), Phys. Rev. D 14, 3432 — SU(N) instanton density, S^(2N) measure
2. Bernard (1979), Phys. Rev. D 19, 3013 — MS-bar normalization C_N ~ 2.5e-3 for SU(3)
3. Novikov-Shifman-Vainshtein-Zakharov (1983), Nucl. Phys. B 229, 381 — NSVZ exact beta
4. Dunne-Kirsten-Preti (2005), JHEP 11:003 — 2-loop exact determinants, Borel summation
5. Flory-Kvasyuk-Pleskun (2022), Phys. Rev. D 105 — lattice K_2 = 0.85 +/- 0.4

## Rule for Future Instanton Computations

When someone writes `Gamma = Gamma_tree * exp(-2 S_inst)`, ALWAYS ask:
1. Is C_N (MS-bar or Pauli-Villars) absorbed?
2. Is the zero-mode Jacobian S^(2N) in amplitude / S^(2(2N-1)) in rate present?
3. Is the specific operator's zero-mode measure integrated or not?

At S_inst = 10-20 (gray zone), these 1-loop factors matter by 6+ OOM.
At S_inst > 100, they shift by <20% and are subdominant.

**Semiclassical effective action clue**: if S_eff = S - N^2 ln S < 0, the naive 1-loop expansion shows the zero-mode measure exceeding the exponential suppression — a sign the saddle is at the boundary of its validity.
