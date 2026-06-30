---
name: S56 Fabric Neutrino Assessment
description: S56 fabric partition function results evaluated for neutrino sector impact -- mu-shift, adiabatic gap, N_eff, PMNS unchanged
type: project
---

## S56 Neutrino-Relevant Results

**Why:** S56 computed the 32-cell fabric partition function Z_fabric. Three results have neutrino sector implications.

**How to apply:** The PMNS constraint surface is topologically unchanged by S56. The mu-shift breaks PH but in the wrong space for PMNS. Normal ordering and NNI texture remain the strongest predictions.

### W1-4: MU-SHIFT-56 = PASS
- mu_eff = -0.201 M_KK at fold (from non-bipartite graph topology + Casimir disorder)
- S34 mu=0 theorem does NOT extend to coupled fabric
- Effect on R: WORSENS (B3 gets largest fractional shift 17.4%, compresses eigenvalue hierarchy)
- R moves further from 33.8, not closer
- PH-breaking is in TB Hamiltonian space, not in Dirac operator eigenspace

### W3-6: GGE-FABRIC-56 = INFO (Adiabatic Protection)
- 2-cell Josephson gap = 13.04 M_KK (35x single-cell BCS gap 0.370 M_KK)
- P_exc = 6.6e-4 (nearly perfect adiabatic following)
- Eigenvalue structure survives transit intact on fabric
- No scrambling of B1/B2/B3 branch labels

### W0-2: NEFF-56 = FLAGGED
- Fabric N_eff = 41.5 at fold (internal thermodynamic modes, NOT cosmological N_eff)
- BA phonon frequencies 0.2-1.4 M_KK, frozen out at BBN T ~ 1 MeV by 100+ orders
- Does not contribute to cosmological N_eff = 3.044
- F_BA/F_Josephson = 0.8% -- below BBN sensitivity

### Additional S56 Findings
- Fabric integrability preserved (W1-2: <r>=0.367, Poisson). R-G conserved quantities survive inter-cell coupling
- Mass variation (W3-8): ALL 32 modes dE_k/dtau < 0 at fold. Universal spectral drainage
- BKT ordering maintained (W0-4): T_GH/T_BKT < 0.17 everywhere. No topological defects
- Fabric after transit: uniform, ordered, defect-free superfluid. Neutrino propagation sees constant potential (no MSW-like effect from fabric)

### PMNS Status Post-S56 (UNCHANGED from S52)
- Normal ordering: STRUCTURAL PASS
- NNI texture: STRUCTURAL PASS
- sin^2(theta_13) achievable at off-Jensen eps=0.0918 (Level 4)
- sin^2(theta_12), sin^2(theta_23): LEVEL 5, structurally blocked
- Full 3x3 PMNS: requires beyond-singlet or non-left-invariant mechanism
- mu-shift does not open new route

### Potential Opening (SPECULATIVE, not computed)
- Fabric graph topology breaks PH symmetry (proven). Could it also break U(2) within spinor module?
- 32-cell fabric spectrum has different symmetry group than single-cell Dirac spectrum
- If U(2) broken at fabric level, eigenspace overlaps could become non-trivial
- NOT computed. Flagged for future session.

## Collab File
- `sessions/archive/session-56/session-56-neutrino-collab.md`
