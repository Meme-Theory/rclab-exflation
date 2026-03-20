---
name: flatband-43-result
description: S43 FLATBAND-43 INFO result. B2 is ideal flat band (W=0 exact, U(2) Schur protection). Prior W/Delta~0.9 was WRONG -- actual W/Delta=0. T_c linear in g (Paper 18). Enhancement 11x over conventional BCS. Explains S35 RG-BCS-35 unconditional instability.
type: project
---

FLATBAND-43 (S43): B2 at the fold is an IDEAL flat band, not crossover.

**Key numbers:**
- W_B2 = 0 (exact, 10^{-16}, at ALL 9+9 tau values from two independent sources)
- W/Delta = 0 (prior estimate 0.9 was WRONG -- confused inter-band gap with intra-band bandwidth)
- Delta_flat = g * N * rho / 2 = 1.053 M_KK (linear in g, Paper 18)
- Delta_BCS = 0.094 M_KK (conventional exponential)
- Enhancement: 11.3x
- M_max = 1.385 (Thouless, confirms BCS instability)

**Why:** U(2) = SU(2) x U(1) is the isometry group of the Jensen deformation. C^2 generators carry fundamental rep of U(2). Schur's lemma forces the Dirac operator (which commutes with isometries) to have identical eigenvalues on the 4-dim C^2 spinor subspace. Protection is EXACT and TOPOLOGICAL -- cannot be lifted by any U(2)-preserving perturbation.

**How to apply:**
- S35 RG-BCS-35 (any g>0 -> instability) is now EXPLAINED: flat band eliminates exponential suppression
- S37 S_inst = 0.069 is the collective mode action of the flat-band condensate
- BCS instability is ROBUST, not fine-tuned (linear, not exponential dependence on g)
- Kinematic bandwidth (W=0) is distinct from BCS-channel bandwidth (M spread = 1.64)
- The prior W/Delta ~ 0.9 confused inter-band gap (B2-B1 = 0.026) with intra-band bandwidth

**Data:** `tier0-archive/s43_flat_band.{py,npz,png}`
