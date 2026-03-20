---
name: spectral-flow-ns-47-result
description: S47 SPECTRAL-FLOW-NS-47 INFO. Adiabatic BdG spectral flow gives n_s=-2.51 (827 sigma). alpha=2.63 (steep blue). BCS flow k-independent within sector, geometric flow has wrong slope. 11th n_s route closed. Same eigenvalue-span obstruction as all prior routes. No topological protection (N_3=0). 3He-A chiral anomaly inapplicable.
type: project
---

## SPECTRAL-FLOW-NS-47 Result (Session 47 W4-3)

### Gate: INFO (2026-03-16)

Spectral flow IS k-dependent (alpha != 0) but n_s far outside [0.93, 0.99].

### Key Numbers
- alpha (uniform gap, 992 modes): 2.63
- alpha (3-sector gap, 992 modes): 3.51
- alpha (3-sector, at fold): -17.84 (unstable, 3-point fit)
- n_s (adiabatic occupation): -2.51 (827 sigma from Planck)
- n_s (sudden quench): -5.17 (1470 sigma)
- Flow decomposition at fold:
  - B1: 98.9% geometric, 1.1% BCS
  - B2: 13.8% geometric, 86.2% BCS (but BCS is k-INDEPENDENT)
  - B3: 100.0% geometric, 0.0% BCS
- Flow rates: B3 (+0.672) >> B1 (-0.064) >> B2 (-0.002), ratio 275:1
- Total flow: 784 up, 208 down, net +576 (Dirac eigenvalues, not BdG)
- Van Hove at omega=2.05: 6.0x mean flow rate (reinforces blue tilt)

### Three Structural Obstructions
1. BCS flow k-INDEPENDENT within each sector (flat band B2: 496 identical modes)
2. Geometric flow steep (alpha ~2.6) because high-energy modes more sensitive to metric deformation
3. No topological protection (N_3 = 0, BDI class, gap open at all tau)

### 3He-A Comparison
- 3He-A chiral anomaly (Paper 09): requires Fermi points (N_3 = +/-2), produces NET CURRENT not spectrum
- Framework BDI: N_3 = 0, no Fermi points, flow along gap edge, no zero crossings
- The anomaly mechanism is structurally inapplicable, not just quantitatively wrong

### n_s Route Closure Count: 11
All share same root cause: eigenvalue span 2.5x across KK tower with approximately uniform BCS gap forces steep power law regardless of readout mechanism.

### Remaining Open Paths
1. Texture spectrum on fabric (inter-cell coupling, no session has attempted)
2. Topological defect correlations (outside Bogoliubov paradigm)
3. k-dependent Delta(k) (blocked by flat band + Schur's lemma in singlet)

**Why:** Definitively demonstrates that adiabatic spectral flow inherits the SAME obstruction as pair creation. The spectral index is a property of the SPECTRUM (KK tower), not the PROCESS (pair creation vs spectral flow vs LZ). No single-cell mechanism can produce n_s.

**How to apply:** Future n_s attempts MUST use fabric-level physics (texture spectrum, defect correlations) or non-Bogoliubov physics. All single-cell, single-particle readout mechanisms are exhausted.

Files: s47_spectral_flow_ns.py, s47_spectral_flow_ns.npz, s47_spectral_flow_ns.png
