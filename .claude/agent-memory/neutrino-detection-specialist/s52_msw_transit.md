---
name: S52 MSW Transit Results
description: MSW-TRANSIT-52 gate results — level crossing during transit, Landau-Zener non-adiabatic, R unmodified, ordering transition from inverted to normal
type: project
---

## MSW-TRANSIT-52 Gate: INFO

**Why:** During modulus transit (tau: 0 -> 0.19), the B1 and B2 sector eigenvalues cross at tau = 0.107. This is the geometric analog of the MSW resonance. The Landau-Zener analysis determines whether the transit modifies neutrino mass predictions.

**How to apply:** R = dm2_31/dm2_21 is a property of the Dirac operator at the frozen tau, not of the transit history. MSW-like dynamics cannot fix the R shortfall. However, the transit dynamically CREATES the normal ordering from an initially inverted configuration — this strengthens the normal ordering prediction.

## Key Numerical Results

- B1-B2 level crossing at tau = 0.1067 (interpolated from s44 data)
- Initial ordering (tau=0): B2 < B1 = B3 (INVERTED for B1-B2)
- Final ordering (tau=0.19): B1 < B2 < B3 (NORMAL)
- gamma_LZ = 0.000929 (STRONGLY NON-ADIABATIC, gamma << 1)
- P_diabatic = 0.9985 (states jump through crossing)
- V(B1,B2) = 0.077 M_KK, avoided crossing gap = 0.154 M_KK
- Sweep rate dtau/dt = 168.1 M_KK (from v_terminal = 26.545, dt_transit = 0.00113)
- Effective B1-B2 mixing at fold: sin^2(theta_m) = 0.552 (matter angle, not vacuum)
- R at fold = 3.37 (10x below NuFit target 33.8)
- R unmodified by MSW dynamics (eigenvalue property, not state property)

## Structural Findings

1. Normal ordering is DYNAMICAL: created by B1-B2 crossing during transit, not an initial condition
2. B1 and B3 degenerate at tau=0, split without coupling (V_13 = 0, NNI exact)
3. Crossing is non-adiabatic (gamma = 0.001): too-fast transit prevents adiabatic following
4. B2-G1 minimum gap = 0.136 at fold (no near-degeneracy in [0, 0.19] range)
5. Scale bridge unresolved: eigenvalues O(1)*M_KK, physical masses < 0.45 eV

## Files

- `computations/s52_msw_transit.py` (main script)
- `computations/s52_msw_transit.npz` (all numerical data)
- `computations/s52_msw_transit.png` (6-panel plot)
- `computations/s52_msw_transit_output.txt` (full output log)
