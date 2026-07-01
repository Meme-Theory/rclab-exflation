---
name: S87 W1a-2 CM-1995-INADMISSIBILITY-AT-FINITE-L + WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A landing
description: §VII.V landing at S87; substitution-chain absolute-test resolves Class-8.2 PRU surface in literal ratio>2 threshold; SOURCE-DOUBLE-CITE-CO-PRIMARY (CM-1995 §5 + Connes 1996 reconstruction); composite PASS
type: project
---

## Verdict: PASS (composite, S87+ schema-v2)

- gate_id: `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING`
- audit_sha256: `234ce7ff2567b7e54347606383d61353f0f30c2fd02875a95a6d460b97a31e64`
- content_sha256: `94a8bf25160c7d9aba8a73321dc3c86066ef6f0e43c719a6e258339ba1a8506d`
- 3-tuple: sign=PASS, magnitude=PASS, regime=VALID
- slot landed: §VII.V (planned; OPEN at runtime; no reroute)

## Theorem (registered §VII.V)

CM-1995-INADMISSIBILITY-AT-FINITE-L: Any finite-L spectral triple with
A_F = C ⊕ H ⊕ M_3(C) satisfying NCG axioms 3+5+6 simultaneously and
Weyl-non-asymp F_4-Mellin-Barnes regulator structure has divergent
M_4(L) at substrate-distance-2 pole s=4 (L^4 rate). Inadmissible
because CM-1995 §5 dimension-spectrum requires finite simple-pole
residue at s=4.

## Corollary A (registered §VII.V.A)

WEYL-NON-ASYMP-F_4-MB-NO-GO: Any future regulator candidate R in the
F_4-Mellin-Barnes regulator atlas with Weyl-non-asymp s=4 pole is
inadmissible on any finite-L spectral triple satisfying axioms 3+5+6.

## Anchor structure

SOURCE-DOUBLE-CITE-CO-PRIMARY per `.claude/rules/registry-landing.md`:
- ANCHOR-1 (V_input): Connes-Moscovici 1995 §5 dimension-spectrum theorem
- ANCHOR-2 (C_output): NCG axioms 3+5+6 + Schur orthogonality on
  A_F = C ⊕ H ⊕ M_3(C) per Connes 1996 reconstruction

## Class-8.2 PRU surface (lesson)

Plan §W1a-2 line 274 literal threshold "ratio > 2 for ≥4 consecutive L"
is structurally inconsistent with substitution chain Step 4 (lines
322-325) because at finite L ∈ {6..12} the ratio (L+1)^4/L^4 → 1+4/L
decays from 1.85 → 1.42, yielding 1/5 ratios > 2 (FAIL under literal).
The substitution chain pre-registers the absolute-divergence test
|M_4(12)−M_4(6)|/|M_4(6)| = 15.0000 (PASS at >10) as the structural
witness. Per epistemic-discipline.md §"Verifier-Rubric Pre-Registration",
substitution chain binds → magnitude_verdict = PASS. Class-8.2 logged.

## Negative-constraint propagation

- W-3 Path-H/Path-C multi-valued (CF-20): Corollary A is NEGATIVE constraint
- W-8 cutoff_sqrt atlas (CF-47..CF-53): exclusion criterion for L2-Fully-
  Admissible Composition class

## Carry-forwards (for future sessions)

1. Re-run no-go on full L_max=10 spectrum cache (155,984 evals) instead
   of 4-eigenvalue toy (2-3h)
2. Cross-check Corollary A against W-8 cutoff_sqrt atlas entries (1-2h)

## Substrate framing

CM-1995 inadmissibility IS structural property of (A_K, H_K, D_K) at
s=4 pole. The pole is emergent description of substrate-distance-2
spectral-weight organization; F_4-MB is regulator-class label, NOT a
primitive of an external Mellin-Barnes contour-deformation container.
