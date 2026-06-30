---
name: S64 LOCAL-ENTANGLE-64 Results
description: Local entanglement entropy of GGE on CG(24) via Peschel method — bipartite structure, area law, near-maximal S_ent
type: project
---

## Gate: LOCAL-ENTANGLE-64 (INFO)

**S_ent(normal, max-cut) = 55.72 nats, S_ent(BCS) = 54.99 nats**

### CG(24) Graph Structure
- 24 vertices, 72 edges, regular degree 6, diameter 3
- CG(24) IS BIPARTITE: A_4 (even permutations) vs odd permutations
- Adjacency spectrum symmetric: {+6(x1), +2(x9), 0(x4), -2(x9), -6(x1)}
- Max-cut = 72 = ALL edges (bipartite partition = even/odd)
- Min-cut = 24 edges (Fiedler partition)

### Entanglement Results
- Max-cut (bipartite): S = 55.72 nats (84% of theoretical maximum 8*12*ln2 = 66.5)
- Fiedler partition: S = 32.38 nats
- Min-cut partition: S = 29.27 nats
- S(A) = S(B) = 55.72 (symmetry by vertex-transitivity restricted to bipartite class)
- S(AB) = 0.72 nats (total GGE thermal entropy)
- Mutual information I(A:B) = 110.72 nats (massive spatial correlation)

### Area Law (R^2 = 0.926)
- S = 0.483 * n_cut + 19.07 nats
- Entropy per cut edge: 0.483 nats/edge
- Topological entanglement entropy: gamma = 19.07 nats
- Pearson r = 0.962

### Physical Mechanism
- Josephson hybridization creates BIMODAL occupation distribution per band
- beta * J_eff ~ 23: bandwidth >> GGE temperature
- Each band: ~10 modes at n~1, ~10-14 modes at n~0, 4 intermediate (zero-energy sector)
- On bipartite graph, all non-degenerate eigenstates have w_A = w_B = 0.5 exactly
- Near-maximal entanglement because occupied modes are perfectly delocalized across cut
- Per-band S ~ 6.93-7.06 nats (each band near-maximally entangled independently)

### CC Connection
- S_BH per bond = 4*pi*a_2 = 34,886
- S_ent/S_BH = 2.2e-5 per bond (entanglement far below BH scale)
- rho_ent ~ 5.9 M_KK^4: log10(rho_ent/rho_obs) = 114.8 (same CC gap)
- S64 W1-B: 94.6% of rho_ZP outside Gaudin span
- Entanglement entropy is LARGE but does not suppress CC

### Structural Insight
- "Genuine" entanglement (S_ent - S_thermal_uniform) = -9.49 nats
- NEGATIVE: k-dependent occupations REDUCE entropy below uniform case
- This is because bimodal n~{0,1} is purer than intermediate n
- The large S_ent is NOT anomalous quantum correlation but rather
  the consequence of tracing out half the degrees of freedom of
  a state with strongly k-dependent occupations
- The mutual information I(A:B) = 110.7 nats quantifies the true
  spatial correlation content

### Files
- `computations/s64_local_entangle.{py,npz,png}`
