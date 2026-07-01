---
name: S84 W5-59 A_s Branch-B floor result
description: S84 W5-59 INFO — A_s_floor_B = 1.10e-13 R5-applied (4.28 OOM below Planck); raw = 5.74e-14 (4.56 OOM). Prompt 5.09e-13 = mantissa typo for 5.09e-14; 4.6 OOM anchor correct.
type: project
---

# S84 W5-59 — A_s Branch-B floor + OOM audit

- **Gate**: S84-FLOOR-CONDITIONED-ON-BRANCH
- **Verdict**: INFO
- **Key values**:
  - A_s_B_raw = 5.7403e-14 (UNIFIED-AS-79 Branch-B L_max=5, machine-precision match to S82-UNIFIED-AS-79-FULL-B)
  - A_s_floor_B = 1.1033e-13 (R5-applied = raw × K_R5=1.922)
  - OOM_R5 = 4.2795 below Planck
  - OOM_raw = 4.5633 below Planck
  - OOM_prompt_direct = 3.6155 (direct eval of 5.09e-13)
  - closure sha256: `023beabd278c5dd21fccdddc8d93407ad8acd8c6c44ce09816d1ff87e91b92e5`

**Why**: S84 W5-59 required resolving prompt self-inconsistency where value 5.09e-13 and "4.6 OOM below Planck" cannot both be true (direct eval gives 3.62 OOM, not 4.6). The raw Branch-B A_s matches 4.6 OOM to 0.037 OOM error; the prompt value is a mantissa-exponent typo (10⁻¹³ → 10⁻¹⁴). S83 Volovik synthesis L223 derivation contains matching exponent typo (2.65e-13 should be 2.65e-15).

**How to apply**: Downstream consumers of A_s_floor_5conv (W5-60 canonical_constants promotion, W5-63 K-floor reachability) should use 1.1033e-13 (R5-applied value) as the canonical floor. Raw 5.74e-14 is the pre-K anchor. Branch-B is NOT a Planck-match candidate — structural positivity wall 4.3–4.6 OOM below Planck.

## Structural consequence

Branch-B floor is a positivity WALL, not a Planck-reach path. Planck-match is forced to Branch-A path exclusively. This reinforces S83 W1-G1 Branch-A/B inequivalence and explains why S83 G51 w_0 regulator FAIL is sub-leading to the 4+ OOM Branch-B/Branch-A split.
