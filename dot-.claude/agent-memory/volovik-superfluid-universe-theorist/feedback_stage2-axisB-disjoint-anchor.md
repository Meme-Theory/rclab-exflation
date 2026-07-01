---
name: feedback-stage2-axisB-disjoint-anchor
description: As Stage-2 Axis-B cross-reviewer, verify transport numbers via a DISJOINT anchor + a separate corroborating gate, not by transcribing the registry's own published value
metadata:
  type: feedback
---

When serving as the Axis-B (transport/superfluid) independent cross-reviewer in a joint-theorem Stage-2 verify (`joint-theorem-promotion.md §"Two-Agent Independent-Verify"`), a clause is only INDEPENDENTLY verified if the number is reproduced from a source OTHER than the registry block being audited.

**Why**: copying `Δ_scheme = 0` (or any number) out of the registry entry into my own Sage check is transcription, not re-derivation — it cannot catch a registry error and gives a false sense of independence. The substrate-input-orthogonality clause makes PASS-AND structurally independent ONLY if the data is disjoint.

**How to apply (the pattern that worked at S95 W1-1 §VII.BG)**:
1. Load a transport-side orthogonal `.npz` DISJOINT from the Axis-A reviewer's anchor (e.g. for a χ-image-inheritance bridge, use `s88_w3b_chi_inheritance_kde_complete.npz` (per-summand χ-image norms: M3→0, C/H→√2) and `s88_w4c_az_inheritance_cartesian_confirm.npz` (rank_ker_chi=2, ker_cocycles=[phi_67,phi_88]) — NOT the producing gate's own a_4-residue npz).
2. Corroborate the headline scalar via a SEPARATE gate in a different session (e.g. `Δ_scheme=0` independently in `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR`, `S86-W-11-ETA-GV-JOINT-PROBE`, `S88-W7-LF-D`). A separate-session reproduction is the real independence signal.
3. Supply the SUBSTRATE-PHYSICS structural reason from my own domain — for secondary-class scheme-independence on a 3He-B child, η-defect=0 is FORCED by BDI parity-blindness (W17 PROVEN wall), so APS/Cheeger-Simons/Bismut-Cheeger collapse bit-identically. That is the substrate-side content only the transport reviewer is positioned to assert.
4. A separate-gate FAIL verdict (S90-AQ FAILed) does NOT invalidate the NUMBER it reports when the FAIL is a Class-(c) PIN-DRIFT (η-threshold testing a hypothesis Bulletin #2 already disproved); the (η=0, GV≠0) signature is the canonical content regardless. Read the verdict's structural meaning, not just its PASS/FAIL tag.

**S115 W2-1 instance (commutant / crossed-product class, NOT transport-κ).** Axis-B blind verify of §VII.CK Door D4 (B_leg PASS, JOINT PASS). The disjoint-anchor discipline applied to a structural (not numerical-transport) clause: instead of transcribing the registry's `7.25e-17` residual, I re-derived the EXACT structural zero `[L_{X_a}, R_{Y_b}]=0` over all 64 su(3)×su(3) pairs (Sage ℚ[i]) — the residual is recovered as its float shadow, not the source. The triality selection rule `0 ≢ ±1 (mod 3)` (Sage ℤ/3) is the second disjoint exact check. My own-domain substrate reason (step 3 of this rule): SU(3)_R is the residual internal symmetry of the group-manifold "condensate" — exactly the ³He residual-order-parameter symmetry `SO(3)_{L−S}` whose generators are isometries of the condensate manifold but whose BdG-quasiparticle coupling lives in the COMMUTANT of the single-particle operator, coupled in via the symmetry group acting on the Nambu spinors. The NCG analog: right translation commutes with the left-invariant D_K by group-associativity ⇒ `Y_R ∈ (A_K^{left})'`, coupling only via `A_K ⋊ SU(3)_R` (Kasparov external product). REUSABLE CONVENTION-TRANSLATION: residual order-parameter symmetry (right-acting on the OP manifold) ↔ right-regular commutant; the "external-as-a-coupling ≠ field-in-a-container" distinction IS the superfluid distinction between a residual symmetry's group-action coupling vs a hand-added background field. This is the substrate-side content only the transport/superfluid reviewer is positioned to assert.

Related: [[feedback_r1-overconfidence-test-before-claim]] (run the exact test WITHIN dispatch, do not defer).
