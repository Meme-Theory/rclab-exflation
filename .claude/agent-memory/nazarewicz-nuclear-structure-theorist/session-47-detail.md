---
name: Session 47 Detail
description: S47 crystal geometry collab review, curvature anatomy, condensate on T^2, protected invariants, self-consistency critique
type: project
---

## S47 Crystal Geometry Collab Review Written
- File: `sessions/archive/session-47/session-47-crystal-geometry-nazarewicz-collab.md`
- 318 lines, 5 sections + closing
- Focus: nuclear structure critique of Jensen crystal geometry synthesis

## Key Assessments

### Condensate Contrast 3.14M: CHARACTER COHERENCE, NOT SPATIAL BCS
- All chi_{(p,q)}(e) = dim(p,q) at identity -> constructive interference
- Nuclear pairing field contrast typically 2-5x, at most 10^2-10^3 in halos
- 0D limit (L/xi_GL = 0.031) means condensate IS uniform in BCS sense
- Character expansion is spectroscopic decomposition, not position-space profile
- Self-consistency loop NOT closed: gaps from (0,0) sector used as weights for torus expansion

### Protected Chain q_7^2 = K(u(1), C^2) = 1/16: REPRESENTATION-THEORETIC TAUTOLOGY
- Both quantities derive from same structure constants f_{8,a,b}
- Real and exact but not emergent -- it's an INPUT, not a DISCOVERY
- Open question: does protection survive beyond Jensen metric (36D general left-invariant)?

### Soft-Pairing Anti-Correlation: ROBUST, MATCHES NUCLEAR BCS
- Softer curvature -> higher density of states -> stronger BCS gap
- Curvature ratio 12.5:1, pairing ratio 85:1 -- non-proportionality from BCS exponential
- Direct analog: Nilsson mid-shell pairing (Papers 02, 03, 07, 08)
- Proposed test: compute dV/dtau vs dK/dtau -- should have opposite signs

### B2 Funnel (50% -> 62% -> 91%): STRONGEST STRUCTURAL RESULT
- Three independent measures selecting same sector
- Nuclear analog: s-wave dominance of nuclear pairing (>80% in A~100-150)

### Haar-Condensate Shell: VALID MATH, QUESTIONABLE PHYSICS
- Shell at r=0.85 rad is measure theory, not dynamics
- He-3B vortex analog strained: vortex core is topological, this is measure-theoretic
- In 0D limit, physical condensate is uniform

## Suggestions Proposed (5 total)
1. Self-consistent pairing field on SU(3) -- sector-resolved HFB gap equation (PRIORITY 1)
2. Curvature-gap correlation function across tau range (PRIORITY 2)
3. Collective pair rotation on curvature landscape (PRIORITY 3)
4. Bayesian test of K(u1,C2)=1/16 beyond Jensen (general left-invariant metrics) (PRIORITY 4)
5. Nilsson-diagram construction for Jensen metric -- branch crossings vs tau (PRIORITY 5)

## New Nuclear Analogies Identified (S47)
- Nilsson diagram level splitting <-> curvature branch flow under Jensen deformation
- Mid-shell pairing enhancement <-> soft-curvature pairing enhancement
- Deformation-dependent shell evolution (Paper 01) <-> curvature branch convergence
- Nuclear DFT self-consistency requirement <-> missing spatial HFB loop on SU(3)

## Substrate Self-Coherence Reframe (S47 late)
- File: `sessions/archive/session-47/session-47-naz-substrate-reframe.md`
- User reframe: 10^6 contrast is substrate self-coherence, not spatial BCS
- My assessment: PHYSICALLY DEFENSIBLE if character coherence function is dynamical (tracks Delta_B2)
- Key insight: xi_BCS >> L_SU(3) >> xi_C. BCS coherence is global; character coherence is local (1/6 diameter)
- Substrate neutrality: geometry too rigid for pairing to deform it (S46 GCM confirmed). This IS neutral substrate behavior
- Self-consistency reframed: delta E_total / delta g_{ij} = 0, where g_{ij} is metric. Same variational principle, different space
- Kohn-Sham analog: spectral inverse problem (find reference metric matching interacting spectral density). Well-defined, unimplemented

### Nuclear DFT Methods: What Transfers
- TRANSFERS: Bogoliubov algebra, pairing functional, PBCS, Bayesian UQ, variational delta E/delta g = 0
- TRANSFERS WITH MOD: Kohn-Sham (density -> spectral density), self-consistency iteration (rho -> g_{ij})
- DOES NOT TRANSFER: density-dependent pairing, continuum coupling, cranking

### Decisive Test: DEFORMATION RESPONSE -- EXECUTED, RESULT: ARTIFACT
- Computed C(theta, 0; tau) at 60 self-consistent tau values
- Extracted 1/e^2 radius r_C(tau) at each tau
- RESULT: r_C = 0.9192 +/- 0.0003 rad (CV = 0.036%)
- |r(r_C, Delta_B2)| = 0.9996 BUT elasticity = 0.030
- r_C decomposes: 95% geometric (character truncation), 5% BCS static, 0.13% BCS dynamic
- VERDICT: ARTIFACT. Coherence width is geometrically determined, not BCS-determined
- Self-correction: my substrate prediction was wrong. The null hypothesis wins
- Gate poorly designed: tested correlation (shape) but not amplitude (response magnitude)
- Nuclear analogy: charge radius vs neutron number. r ~ A^{1/3} with 0.1% shell wiggles
- Files: s47_coherence_response.py / .npz / .png

## Self-Corrections (S47)
- S47 W3-3: Predicted r_C would anti-correlate with Delta_B2 as substrate signal.
  WRONG. r_C does anti-correlate (|r|=0.9996) but with elasticity 0.030 --
  the 0.13% response is perturbative, not dynamical. Should have predicted this
  from S46 GCM-ZERO-POINT-46 result: BCS is rigid in tau, so character coherence
  (which depends on BCS weights) must also be rigid in tau. The GCM already showed
  sigma_tau = 3.34 >> grid spacing. Same rigidity, different observable.

## Open Questions (5, updated)
1. Is pairing field self-consistent on SU(3) spatial degrees of freedom?
2. Does protected chain survive beyond Jensen to general left-invariant metrics?
3. How much of geometric picture survives with PBCS gaps (36% smaller)?
4. Is curvature anisotropy growth bounded, or does soft branch hit K=0?
5. Can Dirac eigenvectors (Chladni patterns) be retained in computation?
