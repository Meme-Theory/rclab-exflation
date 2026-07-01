---
name: substrate-not-c-limited
description: The substrate itself (fold transit, Jensen evolution, instanton dynamics) is NOT bounded by c. Only propagation ACROSS the substrate through emergent g_M is bounded, and the cap there is c_Gold ~ 0.915 M_KK set by finite lambda_max in D_K.
type: project
---

## Two regimes of speed in the phonon-exflation framework

**Regime 1: Propagation ACROSS the substrate.** Phononic branches (Goldstone, Leggett, B2, B3, Higgs) carry signals on the emergent 4D metric g_M. These modes ARE moving through something (the 4D acoustic metric projected from the fabric's spectral density). Their group velocities are bounded above by c_Gold = 0.915 M_KK = the fastest throughput the substrate can accommodate as a coherent phonon branch. Deeper reason: D_K has finite lambda_max (155,984 eigenvalues at L_max=10), so dispersive slopes omega(k) cannot exceed M_KK * (a finite constant). c_Gold IS the M_KK-level throughput ceiling. This is a STRUCTURAL cap, not an imported GR postulate.

**Regime 2: Substrate dynamics.** Fold transit (tau from tau_fold to 0), Jensen parameter evolution, classical instanton trajectories, spectral-action gradient flow, the fabric-level reorganization itself -- these are NOT bounded by c at all. They aren't moving THROUGH something; they ARE the substrate reorganizing. The Mach number 13.75 is c_transit / c_Gold where c_transit is a substrate-level speed (fabric dynamics), NOT a phononic signal speed in any 4D inertial frame. The transit is supersonic in the Goldstone frame precisely because it's a substrate-level motion, not a phonon propagating across the substrate.

## User's metaphor (canonical)

"c is the frame rate; the substrate is the film."

- The phonon branches live INSIDE the film. They see the frame rate as their speed-of-light.
- Editing the film is not bound by frame rate. The substrate edits itself during transit, and that editing speed has no c bound.

## Application to W4-L (S74 dispersion analysis)

W4-L tests ell_gap = (m_gap/c_s) * chi_recomb for gap-dominated branches and finds FAIL by 56 OOM. The FAIL is correct, but the reason must be stated as:

CORRECT: "c_s ~ 10^56 c_Gold exceeds substrate propagation throughput by 56 OOM. The ell_gap formula tests a PROPAGATION mode (phononic branch dispersion across emergent g_M), so the M_KK throughput bound applies. The bound is structural because D_K has finite lambda_max, not because of GR Lorentz invariance."

WRONG: "c_s > c violates causality in any causal framework." -- This imports GR Lorentz invariance into a substrate-throughput argument. Phononic branches are bounded by c_Gold not because of Lorentz invariance but because the finite spectral content of D_K limits how fast any coherent mode can propagate.

## Why this distinction matters

Fold transit has Mach 13.75. If we interpreted that as "13.75x faster than light," we would be violating causality by a framework-internal contradiction. The resolution: Mach = c_transit / c_Gold where c_transit is substrate-dynamics (Regime 2, not c-bound) and c_Gold is the phonon throughput ceiling (Regime 1, IS the c of the emergent 4D metric). The transit is fast not because it violates causality but because causality applies only within the emergent metric, and the transit happens at a level prior to that emergent metric.

## Application rule for dispersion computations

When testing whether a dispersion relation omega(k) is physical within the framework:
- Compute v_g(k) = d omega / d k.
- If v_g(k) > c_Gold anywhere, the mode is not a coherent phonon branch on the emergent 4D metric. (Regime 1 bound violated.)
- But this is NOT a causal violation -- it simply means the proposed "branch" isn't something the substrate can accommodate as propagation across g_M. It might still exist as substrate-level dynamics (Regime 2), where the c_Gold bound doesn't apply.
- Never phrase FAIL results as "violates causality." Say instead: "exceeds M_KK throughput ceiling" or "cannot be accommodated as a propagation branch on the emergent metric."

## Provenance
User correction to S74 qa-vdd workshop R2, 2026-04-11. Q1 of Round 1 used the wrong framing ("within any causal framework this is impossible" for c_s > 10^56 c_light). The FAIL conclusion stands; the argument has been restated per this distinction in the R2 CONVERGENCE section.
