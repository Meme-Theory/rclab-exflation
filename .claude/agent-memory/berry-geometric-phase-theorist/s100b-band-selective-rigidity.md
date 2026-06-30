---
name: s100b-band-selective-rigidity
description: S100b W6-2 — band-selective Schur rigidity of the (0,0)-block D_K eigenbundle on the U(2)-invariant TT surface; J/PH chirality lock; corner B1/B2 crossing anatomy
metadata:
  type: project
---

# S100b-NONABELIAN-METRIC-FRACTION (W6-2) — structural findings

**Verdict**: FAIL [FAIL-a-JPH-protected-B2-carries-CKH], sign=PASS/mag=FAIL/regime=VALID.
audit=4a03497c43a97335... Artifacts: `computations/session-100b/s100b_nonabelian_metric_fraction.{py,npz,png}`; WP §W6-2 of `sessions/session-100b/session-100b-w6-workingpaper.md`. UNTRUSTED-UPSTREAM caveat carried (LC t=1/2 lineage; canonicity open, numerics control-verified).

**Why**: the gate tested Chen–Karki–Hosur non-additivity (Tr R ≠ Σ per-band Abelian QM) on the lowest D_K multiplet over the (τ,μ) U(2)-invariant surface; the answer reshapes how ANY future quantum-geometry gate on this base must be designed.

**How to apply** (load-bearing for future modulus-space QGT work):

1. **Signed (0,0)-block layout** (PH/chiral-symmetric at every node): [−B3×3 | −B2×4 | −B1 | +B1 | +B2×4 | +B3×3]. The "deg-2 lowest multiplet" is the J/PH pair (−|λ|min, +|λ|min) — TWO 1-dim eigenspaces, NOT a 2-dim eigenspace. eigh's |λ|-argsort order flips randomly on the pair (ties): use signed-ascending col order (cols 7,8) for deterministic tracking.
2. **Band-selective Schur rigidity**: pair(B1±) and B3± bundles are FROZEN over the whole surface (max‖ΔP‖_F ~ 1e-14 — multiplicity/direction-locked isotypic slots; dH|u⟩ = dλ|u⟩ pointwise ⇒ QGT ≡ 0, CKH 0/0-vacuous). B2± quadruplets genuinely MOVE (‖ΔP‖ = 0.228; defect-excluded I_NA(B2) = 2.59e-2). The flat optical multiplet is the ONLY geometric carrier on the U(2)-invariant base.
3. **Chirality lock**: γ₉ (normalized Cl(8) gamma product) anticommutes with H exactly; |⟨u₊|γ₉|u₋⟩| = 1.000000000. Cross-WZ ⟨u₊|dH|u₋⟩: γ₉ forces imaginary-only, J reality kills the rest — median |A^WZ| = 1.3e-17 (99.96% nodes < 1e-12). Double protection.
4. **B2 complement-QGT is Schur-scalar** (∝ 1₄ to ~1e-13): on a U(2)-invariant base the invariant complement metric CANNOT discriminate Abelian vs non-Abelian band structure (symmetry-forced isotropic). Discrimination needs isotropy-BREAKING deformations (outside the U(2)-invariant 3-param family) — the natural forward gate.
5. **Corner trap**: B1/B2 cross in |λ| at the (0.10,+0.10) window corner (symmetry-ALLOWED, different isotropy characters, von Neumann–Wigner). Sorted/signed tracking jumps there → exact-rational FD spikes (4/Δ² etc.) that carried 100.00% of the pinned I_NA = 1.5; single π-plaquette gives spurious C_FHS = −0.5 (NOT topology; 2499/2500 plaquettes zero; S96's argsort fell below the det-link guard so it read 9.78e-15). ALWAYS map gap12 and report defect-excluded companions.
6. **Evaluator rule**: use the projector identity Tr_band Q_ab = Tr[(d_aP)(1−P)(d_bP)] (exact lemma; basis/phase-free). The largest-|component| real-positive phase pin has π-jumps (argmax switches) — raw state-FD is polluted; rank-1 projectors per member are immune. Per-band decomposition inside an EXACTLY degenerate eigenspace is not even FD-stable (pinned-frame I_Ab(B2) = 5.8e3 = artifact) — the sharpened CKH point.
7. **Sign-margin floor**: for trapezoid-cancellation numerators use the canonical 1e-14 relative floor (epistemic-discipline.md Class 8.3 item 4), never 1e-15 (measured floor on 2601 nodes was exactly 20·eps).

Relation: extends [[dimensional-reduction-reframe]] (metric-rich content lives in su(3)/Kosmann directions, NOT the metric-moduli base for B1/B3) and the L0–L7 triviality chain (Chern stays 0; the −0.5 reading is a tracking artifact class to watch for).
