---
name: schwinger-36-result
description: S43 SCHWINGER-36-43 INFO. Factor-36 was formula error (3 wrong ingredients in S42 PG formula). S38 BCS formula confirmed: S_Schwinger = 0.070 matches S_inst = 0.069 to 1.8%. PG analog inapplicable to 0D BCS.
type: project
---

SCHWINGER-36-43 = INFO (formula error, not physics)

The S42 Volovik review used a PG horizon formula with three wrong ingredients:
1. E_cond = 0.115 instead of Delta_0 = 0.770 (factor 44.9 in squared energy)
2. kappa_eff * c_fabric = 22,533 instead of v_terminal = 26.5
3. c_fabric in denominator (irrelevant for 0D system)

Correct formula (S38): S_Schwinger = pi * Delta_0^2 / |v_terminal| = 0.0702
S_inst = 0.069. Match: 1.8%.

**Why:** The PG horizon analog (Paper 29) requires a horizon (v_flow = c_s), spatial extent, and a sound speed. The BCS sector has none: it is 0D (L/xi = 0.031), Parker creation (no horizon), and the sweep rate is v_terminal = V'/(3HG) = 26.5. The gradient stiffness Z and c_fabric govern spatial fabric variations (nabla tau)^2, which vanish for homogeneous evolution.

**How to apply:** When mapping Volovik analogs to the framework, distinguish SPATIAL analogs (fabric: Z, c_fabric, kappa_eff) from TEMPORAL analogs (BCS transit: v_terminal, Delta_0, S_inst). The PG horizon formula applies to fabric spatial gradients. The BCS Schwinger formula applies to the temporal modulus sweep. Never mix the two.

Key numbers: S_Schwinger_BCS = 0.0702, S_Schwinger_PG = 1.84e-6, S_inst = 0.069.
Output: tier0-archive/s43_schwinger_factor36.{py,npz,png}
