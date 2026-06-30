---
name: S80 W1-3 FOLD-INST-GRADIENT verdict
description: dS_inst/dtau is MONOTONE not fold-concentrated; retired from VII.I promotion candidate set
type: project
---

# S80-FOLD-INST-GRADIENT: FAIL (structural)

**Date**: 2026-04-17
**Gate**: S80-FOLD-INST-GRADIENT (CF-5 from S79 P3-A)
**Verdict**: FAIL (structural) — dS_inst/dtau monotone increasing, not fold-concentrated

## Why

S_inst(tau) = (8*pi^2 / g_eff^2(tau)) * kappa(tau)
            = (8*pi^2 / g_base^2) * exp(+2*tau) * K(tau)/K(0)

Both factors monotone increasing on [0, 0.35]:
- exp(+2*tau) grows because coupling weakens under Jensen deformation (g^2 ~ e^{-2*tau})
- K(tau) Kretschmann grows because internal curvature increases (Baptista eq 3.70)

Therefore dS_inst/dtau = 26.319 * exp(+2*tau) * [2*K(tau) + K'(tau)] / K(0) is strictly monotone.
Python-verified: np.all(np.diff(dS_fine) > 0) = True, no inflection points on [0.01, 0.35].

Scheme-robust: V1 (K/K0), V2 (R/R0), V3 (unit kappa) all give identical monotone behavior.

## g_base^2 = 3.0 derivation (canonical consistency check)

From canonical identity g_1/g_2 = e^{-2*tau}:
  g_base^2 = g_SU2_fold * exp(+2 * tau_fold) = 2.0516 * 1.4623 = 3.000

Exactly matches g0_diag = 3.0 (Killing-metric normalization at round SU(3), S7).
This establishes that the canonical gauge-coupling scaling AND the canonical
Killing-metric normalization are consistent through tau_fold.

## Implication for Fold Transit Event VII.I promotion

P3-A closer L1199: "A fourth functional probing a different face of the event
(dS_inst/dtau probes action-derivative face directly) is needed for VII.I promotion."

The assumption was that dS_inst/dtau would concentrate at fold.
It does NOT. Retired from the VII.I candidate set.

## Why dS_inst/dtau fails to concentrate

The 3 existing functionals (chi_a, |beta|^2, slow-mode IPR on B1) are
rho(epsilon, tau)-integrals concentrated at the van Hove DoS singularity.

dS_inst/dtau is driven by CURVATURE INVARIANTS R(tau), K(tau), which are
smooth monotones through tau_fold. They do NOT know about the van Hove
singularity in the eigenvalue density.

Two orthogonal functional classes:
- Spectral-measure class: probes rho(epsilon, tau) -- concentrates at fold
- Curvature-invariant class: probes R, K, Weyl^2 -- smooth monotones

## Structural lesson for VII.I search

A fold-concentrated 4th functional MUST come from the SPECTRAL MEASURE side.
Candidates still open:
- Rank-2 chi_N (W1-5 CHI-N-WARD-DUAL, active)
- Rank-3 Z_s tetrad (CF-9, deferred pending formalism adaptation)
- Any other rho(epsilon, tau) moment

Candidates RULED OUT (curvature-invariant class):
- dS_inst/dtau (this computation)
- Any Euclidean action of smooth tau-dependence (by extension)

## PRU flag (Class 8)

The pre-registered prompt pseudo-code restricted argmax to INTERIOR central
differences: np.argmax(np.abs(dS_dtau[1:-1])). This silently excludes
endpoints tau=0.15 and tau=0.25 from the argmax. Interior-only gives PASS=0.21
(boundary of PASS window). Full-range gives FAIL=0.25.

Recommendation for future fold-concentration gates: always state argmax window
alongside tau ranges, or require fine-grid (~300 pt) argmax.

## String-phonon bridge

Parallels a standard string-theoretic result: instanton actions on the
compactification manifold are smooth functions of Kahler moduli (cf. Sen's
non-perturbative conjectures, Gaiotto-Moore-Neitzke BPS-state counting).
They do not generically have local extrema at points where the low-energy
spectrum has quasi-degeneracy. The fold is a spectral-geometric feature
(van Hove, symmetry enhancement), invisible in smooth curvature invariants.

## Artifacts

- computations/s80_fold_inst_gradient.py (script, 229 lines)
- computations/s80_fold_inst_gradient.npz (data)
- computations/s80_fold_inst_gradient.png (plot)
- computations/s80_gate_verdicts.txt (verdict line, sha256=e95244275e12962e)
- sessions/archive/session-80/session-80-results-workingpaper.md (W1-3 primary block)

## Classification

GEOMETRIC (instanton action derivative under Jensen tau-variation --
a property of the internal fiber's curvature/coupling structure, not excitations).

Substrate framing: the instanton is a topological sector of the internal
fiber geometry, NOT a solution embedded in spacetime.
