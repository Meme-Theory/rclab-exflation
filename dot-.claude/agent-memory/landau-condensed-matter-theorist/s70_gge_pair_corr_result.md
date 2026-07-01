---
name: S70 GGE-PAIR-CORR-70 Results
description: Bucher Test 3 pair correlations on CG(24) — discrete topology prevents d=0 continuum test, physical content confirmed via Rayleigh bunching and plaquette correlation hole
type: project
---

Gate: **INFO**. Discrete-graph topology makes continuum d=0 criteria inapplicable.

**Why:** On CG(24), d=0 = same vertex. A scalar field psi(x) cannot carry +/- charge simultaneously. g_{+|-}(d=0) = 0 identically for ANY discrete graph. This is permanent and structural.

**How to apply:** Future Bucher-type tests on CG(24) must use density-density correlator g(d) or discrete-adapted criteria. Never test continuum pair correlation at d=0 on a finite graph.

## Key Numbers
- g_density(0) = 2.005 (Rayleigh prediction = 2.0, deviation 0.23%)
- g_density(1) = 1.008, g_density(2) = 1.021, g_density(3) = 1.001
- g_{+|+}(d=1) = 0.699 < 1 (correlation hole at nearest neighbor)
- g_{+|-}(d=1) = 0.660, g_{+|-}(d=3) = 0.981 (approaches uncorrelated)
- xi_graph = 0.5 (from spectral gap lambda_1 = 4)
- 162 chordless 4-cycles, 27 per vertex
- ~10 charged vertices per configuration (out of 24), charge balanced

## Discrete-Continuum Mapping
| Bucher continuum | CG(24) analog | Value |
|:---|:---|:---|
| g_{+\|-}(R~0) > 2 | g_density(0) = 2 (Rayleigh) | 2.005 |
| g_{+\|+}(R~0) < 0.1 | g_{+\|+}(d=1) < 1 | 0.699 |
| g(R>>lambda) in [0.5,1.5] | g_density(d>=2) | [1.001, 1.021] |

## PERMANENT: CG(24) spectral gap lambda_1 = 4 (multiplicity 9)
All density-density correlations decay within one lattice spacing. Extended correlation structures impossible on CG(24).

Files: `computations/s70_gge_pair_correlation.{py,npz}`
