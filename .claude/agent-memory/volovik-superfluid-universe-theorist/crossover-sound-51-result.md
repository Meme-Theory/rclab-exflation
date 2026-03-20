---
name: crossover-sound-51-result
description: S51 CROSSOVER-SOUND-51 PASS (with caveat). 3D crossover gives +30.5% but inapplicable to 0D system. c_BdG=0.751 is analog assignment not derivation. omega_GPV=0.792 is the physical 0D quantity. Mean-field unreliable (sign wrong at unitarity vs QMC). Im(c)=0.
type: project
---

## S51 CROSSOVER-SOUND-51 Result

**Gate**: PASS (with structural caveat). |shift| = 30.5% > 10% threshold.

**Key numbers**:
- g*N(E_F) = 2.18 maps to 1/(k_F*a_s) = 0.292 (BEC side of unitarity)
- Leggett mean-field at 0.292: Delta/E_F = 0.886, mu/E_F = 0.348
- c_crossover/c_BCS = 1.305 (+30.5% mean-field shift)
- BCS limit cross-check: c/c_BCS = 1.001 at 1/(k_F*a)=-2.0 (0.1% error)
- Unitarity cross-check: mean-field gives c/c_BCS = 1.17, QMC gives 0.61 (SIGN DISAGREES)
- Im(c) = 0 for all K < 2.18 M_KK (below pair-breaking threshold)
- omega_GPV = 0.792 M_KK is the physical 0D mode (S37)
- c_BdG = 0.751 M_KK is an analog assignment from 3D, not derived

**Three obstructions to applicability**:
1. Framework is 0D: no Fermi surface, no spatial dispersion, no propagating sound
2. Mean-field unreliable: sign wrong at unitarity (E_vac/E_cond=28.8, fluctuations dominate 29x)
3. Crossover requires Feshbach resonance + continuum k-integration (neither exists)

**Physical conclusion**: c_BdG = v_F/sqrt(3) was always a borrowed dimensional estimate. The actual 0D collective mode omega_GPV = 0.792 M_KK is 5.5% above c_BdG. Future K_pivot mappings should use omega_GPV directly. No downstream remapping warranted.

**Why:** QA (S50 collab) flagged g*N(E_F) = 2.18 as BEC-BCS crossover regime. The check found the question structurally ill-posed for 0D but identified that c_BdG was never derived from first principles.

**How to apply:** When c_BdG appears in scale mappings, flag it as an O(5%) analog estimate. omega_GPV is the derived quantity. BEC-BCS crossover formulas require 3D continuum.
