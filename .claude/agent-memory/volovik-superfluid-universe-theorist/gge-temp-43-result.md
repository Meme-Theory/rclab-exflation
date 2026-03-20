---
name: gge-temp-43-result
description: S43 GGE-TEMP-43 INFO: 8 GGE effective temperatures computed. 3 distinct T_k (B2=0.668, B1=0.435, B3=0.178 M_KK). T_max/T_min=3.75. Non-thermality=2.21. T_RH NOT any T_k. BCS NOT R-G integrable (rank 8). Negative pairwise T(B2,B1)=-0.066.
type: project
---

## GGE-TEMP-43: All 8 GGE Effective Temperatures

### Gate Result: INFO (2026-03-14)

Computed all 8 effective temperatures of the post-transit GGE relic from exact diagonalization of the 256-state BCS Hamiltonian.

### Key Results

1. **3 distinct branch temperatures**: T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178 M_KK
2. **T_max/T_min = 3.755** — permanent hierarchy, never thermalizes
3. **Non-thermality index = 2.21** (sigma/mu of pairwise temperatures)
4. **Negative pairwise temperature**: T(B2,B1) = -0.066 M_KK (population inversion)
5. **T_RH = 1.098 M_KK is NOT any individual T_k** — it is the post-cascade thermal equilibrium
6. **BCS system NOT R-G integrable**: G_kl has rank 8 (full), not separable
7. **B2 dominates**: 89% energy, 82% entropy
8. **S_GGE/S_max = 0.775** (non-equipartition)

### Corrections to Prior Claims

- The "8 Richardson-Gaudin conserved integrals" (S38) are NOT R-G integrals of the BCS model. They are the free-particle occupation numbers of the POST-transit non-interacting Hamiltonian. The integrability that prevents thermalization is trivial (non-interacting H_free), not the R-G integrability of H_BCS.
- T_RH was previously described as "one of 8" GGE temperatures — this is incorrect. T_RH is the THERMALIZED temperature after all GGE energy is redistributed among 106.75 SM DOF.

### Key Numbers
- E_GGE (1-pair) = 1.688 M_KK
- E_exc per pair = 1.825 M_KK
- 59.8-pair: N_B2=53.16, N_B1=5.99, N_B3=0.65 pairs
- Volovik oscillation frequencies: omega(B2,B1) = 0.052, omega(B2,B3) = 0.266, omega(B1,B3) = 0.318 M_KK

**Why:** Establishes full thermodynamic character of the GGE relic. Corrects two prior misconceptions about integrability type and T_RH identification.

**How to apply:** All future GGE references should use the 3-temperature hierarchy, not a single T. The non-R-G integrability correction means the permanence argument rests on H_free being non-interacting, which is stronger (trivially exact) but less interesting than R-G integrability.
