---
name: dmde-refine-48-result
description: S48 DMDE-REFINE-48 FAIL/INFO/INFO. Z-K gap 39.4% structural (definitional). Euler relation FAILS multi-T GGE. DESI DR2 creates 2.8sigma tension. Pair corrections perturbative (0.84% RPA). Alpha range [0.698, 1.152] vs needed 0.33.
type: project
---

## DMDE-REFINE-48 Results (S48 W5-C)

### Gate: FAIL (GIBBS-DUHEM) / INFO (DESI) / INFO (KELDYSH)

### Sub-1: GIBBS-DUHEM-GGE-48 FAIL

Standard Euler relation (P = sum T_k S_k - E) gives **negative pressure** (-0.115) for multi-T GGE, while grand potential gives P = +1.465. Mismatch = 108%. The Euler relation assumes single T; FAILS for 8-mode GGE.

Three physically distinct alpha values:
- Grand potential (Zubarev): alpha = 1.152
- Euler multi-T: alpha = -14.6 (unphysical, P < 0)
- Keldysh sigma: alpha = 0.698

Keldysh sigma INVARIANT under reference temperature changes (T_harm, T_E-weighted give same result). Multi-T correction does NOT narrow Z-K gap.

Z-K discrepancy: 39.4% (UNCHANGED from S46). Gate < 20% NOT met.

Euler check: sum T_k S_k = 1.573 (not 1.000 -- S45 identity used Shannon entropy, tautological).

### Sub-2: DESI-UPDATED-48 INFO

Framework w_0 band: [-0.465, -0.589] (from alpha [0.698, 1.152])
DESI DR2 (arXiv:2503.14738): w_0 = -0.752 +/- 0.058, w_a = -0.73 +/- 0.28

**No overlap with DESI DR2 2sigma band [-0.868, -0.636].**
Best estimate (Keldysh): w_0 = -0.589, 2.8 sigma from DR2.
w_a = 0 at 2.6 sigma from DR2 (below falsification).

DESI DR2 implies alpha = 0.330, below observed DM/DE = 0.388.
RETRACTED S45 alpha = 0.410 (artifact) was numerically CLOSER to DR2 (0.7sigma) than corrected value.

### Sub-3: KELDYSH-PAIR-48 INFO

Pair corrections to Keldysh alpha:
- RPA self-energy: -0.84% (well-controlled)
- Vertex: +117% (perturbation theory breaks)
- Frequency-dep: +150% (perturbation theory breaks)

V_pair = 0.172, V_RPA = 0.017 (screening ratio 0.097). Bare self-energy 1.61 M_KK exceeds mode energy. Cannot close Z-K gap.

### Key Numbers

| Quantity | Value |
|:---------|:------|
| alpha_Zubarev | 1.152 |
| alpha_Keldysh | 0.698 |
| Z-K discrepancy | 39.4% |
| Euler-GD mismatch | 108% |
| w_0 band | [-0.465, -0.589] |
| DESI DR2 tension | 2.8 sigma |
| w_a tension | 2.6 sigma |
| RPA pair shift | -0.84% |
| alpha_DESI_implied | 0.330 |

### Physical Conclusion

The Z-K discrepancy is DEFINITIONAL: Zubarev (grand potential pressure) vs Keldysh (entropy production rate) define different vacuum energy operators. In 3He-B, the grand potential defines vacuum energy. If same holds here, alpha = 1.15 and w_0 = -0.465 (5.0sigma from DR2).

DM/DE is O(1) by equilibrium theorem (confirmed). The precise coefficient (0.70 vs 0.39 observed) requires identifying which quantity couples to 4D gravity.

**Why:** Closes the multi-T Gibbs-Duhem question from S46. Establishes DESI DR2 tension as new constraint.

**How to apply:** The Z-K spread [0.70, 1.15] is irreducible without specifying the gravitational coupling. DESI DR2 constrains alpha < 0.5 for w_0 consistency. The framework's DM/DE problem is now the same structure as n_s: O(1) by thermodynamics, precise coefficient unknown.
