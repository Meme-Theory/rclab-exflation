---
name: S64 QUANTUM-METRIC-64 Result
description: Peotta-Torma D_s test FAIL -- three structural zeros kill single-particle Drude weight; Josephson f-sum rule is correct route
type: project
---

## S64 QUANTUM-METRIC-64 Results (Wave 6)

Gate: **FAIL**. D_s(PT) = 0.000 vs D_s(Josephson) = 6.283 M_KK^2.

### Three structural zeros

1. **Quantum metric g_nn = 0**: Inter-cell pair hopping T = E_J * I_8 (proportional to identity in mode space). This is exact in the single-pair sector: S^+_2 S^-_1 preserves the mode index. Consequence: Bloch eigenvectors are k-independent, so the quantum geometric tensor vanishes identically.

2. **Band curvature d^2E/dgamma^2 = 0**: Pair band energies are E_n(gamma) = E_n^(0) + E_J * gamma (linear in adjacency eigenvalue). Linear dispersion has zero second derivative.

3. **CG(24) bipartite pure gauge**: Every edge connects an even to an odd permutation. Any uniform Peierls phase can be absorbed by c_i -> c_i * exp(i*q*parity_i). Eigenvalues are q-independent.

### Why D_s(Josephson) = 2*E_J*S_+ survives

The Josephson stiffness is the **f-sum rule** for the pair kinetic energy:
- D_s = -<K_pair>/N where K_pair = 2*E_J*S_+*cos(phi)
- Requires only S_+(1) = 0.936 (exact diag), ODLRO = 0.989, E_J = 3.397
- NO quasiparticle properties enter. Robust against W3-C Q < 1.

### Physical regime

- E_J / Delta_BCS = 73.2 (extreme strong-coupling Josephson regime)
- Band 0 bandwidth = 40.8 M_KK >> intra-cell pair gap = 0.046 M_KK
- Pairs completely delocalized across cells
- Superfluid weight is a collective phase property, not a band-structure quantity

### S63 correction

S63 QUANTUM-METRIC-63 reported a tautological PASS by setting D_s(PT) = D_s(fold)*ODLRO "by construction." The actual D_s(PT) = 0.

**Why:** CG(24) bipartite graph + mode-preserving pair hop = structurally zero Peotta-Torma D_s. This is permanent.

**How to apply:** The Peotta-Torma single-particle route is inapplicable to the CG(24) Josephson array. Always use the f-sum rule D_s = 2*E_J*S_+ for superfluid weight. Any future D_s calculation must use the Josephson phase stiffness, not the Drude weight.

Files: `computations/s64_quantum_metric.{py,npz,png}`
