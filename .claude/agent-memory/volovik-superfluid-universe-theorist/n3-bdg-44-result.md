---
name: n3-bdg-44-result
description: S44 N3-BDG-44 FAIL. N_3 topological invariant is structurally inapplicable to 0D BCS on SU(3). System is 3He-B class not 3He-A. No Fermi points. Vacuum energy unprotected. q-theory is correct path.
type: project
---

## N3-BDG-44 Result: FAIL

### Gate
N3-BDG-44: FAIL. No Fermi points exist in the BdG spectrum. N_3 = 0 (structurally inapplicable).

### Key Numbers
- min|E_BdG| at fold = 0.8297 (gapped, no zero modes)
- N_3 = 0 (N/A): requires 3 continuous momenta, system is 0D discrete
- N_1 = 0: PH cancellation at all nodes
- eta (spectral asymmetry) = 0: PH-enforced, not topological
- Pfaffian Z_2 = -1: nontrivial but does NOT protect vacuum energy
- n_paired/n_total = 5/8 (5 gapped by BCS, 3 unpaired at xi_3=0.978)
- E_vac(BdG) - E_vac(normal) = +0.029 (nonzero, unprotected)

### Five Independent Arguments for N_3 = 0
1. Dimensionality (fatal): N_3 needs 3D continuous BZ; system has discrete (p,q) in Z^2
2. Codimension: unpaired nodes are co-dim 2 (lines), not co-dim 3 (points)
3. Paired levels fully gapped: det(H_2x2) < 0 everywhere
4. PH cancellation: N_1 = 0 at every node
5. No level crossings: B2 ordering xi_1 < xi_2 < xi_3 preserved for all tau

### Universality Class
Framework BCS on SU(3) = 3He-B (fully gapped, BDI), NOT 3He-A (Fermi point, N_3=+/-2).
Hawking's S43 prediction (FAIL: flat band is Fermi surface) CONFIRMED.

### Downstream
- Paper 04 vacuum energy cancellation inapplicable
- N3-TOPOLOGICAL constraint: CLOSED
- Correct CC path: q-theory (Papers 15-16) + generalized Gibbs-Duhem (CC-GGE-GIBBS-44)
- Pfaffian Z_2=-1 protects gap topology, not vacuum energy

**Why:** Definitively closes the N_3 Fermi-point channel for CC suppression. Self-correction: my S43 CC Workshop R1 proposal was wrong about BdG creating conical nodes. The obstruction is dimensional, not dynamical.
**How to apply:** Do not propose Fermi-point mechanisms for this system. Focus on q-theory and equilibrium-theorem extensions for GGE vacuum energy.
