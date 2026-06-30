---
name: s117-w5-2-wdw-j-family-rigor
description: S117-W5-2 rigorizes Eq. H-R3-1 J≡0 from single-Neumann to the WHOLE real self-adjoint (Robin) family on [0,τ_fold]; Vilenkin excluded as non-self-adjoint; INFO (grid doesn't reach τ=0); the U(2) scope refinement + E-independence sharpening
metadata:
  type: project
---

S117-W5-2 `CF-S117-WDW-J-RIGOR` (gate INFO; `computations/session-117/s117_w5_wdw_j_rigor.py`; audit_sha256 `961ed3833b4bc937a51fbc922f582c5d026b1568dc2bb6f23d16abea4516ef3d`). Lifts my S116-W6 [[s116-w6-bc-fork-hh-layer-assignment]] Neumann J≡0 to the ENTIRE real self-adjoint family. INFO is the DESIGNED outcome (not a shortfall): the theorem verifies to machine precision; INFO fires only because the s63 grid (`tau_fine` min = **0.10**, does NOT reach τ=0) makes the W(0)=0 anchor extrapolated (S0 spread 37.7 ≈ 1.5e-4 rel).

**Four boundary-form identities (Sage-exact, verified BEFORE the script):** L = −d²/dτ²+W, W=2G_DeWitt(S(τ)−E), W REAL. (1) real Robin cosθΨ(0)+sinθΨ′(0)=0 ⇒ Ψ′(0)/Ψ(0)=−cotθ∈ℝ ⇒ J(0)=Im(Ψ*Ψ′)=0 ∀θ; (2) dJ/dτ=Im(W)|Ψ|²=0 (W real) ⇒ J≡J(0)=0; (3) Vilenkin Ψ′/Ψ=+ik ⇒ J(0)=k|Ψ(0)|²≠0; (4) boundary form B=−2i·Im(A1/A2)·Ψ(0)conj(Φ(0)) ⇒ **separated-self-adjoint ⟺ Im(A1/A2)=0 ⟺ real Robin**. Numerics on substrate W(τ): J0_max_abs=0.0 across 181 θ∈[0,π); Jtraj_max=0.0; im_W_max=0.0 (conservation EXACT, all regimes); Wronskian witness J=1 conserved to 3.2e-11; vilenkin_J0=235.0 (excluded).

**Two sharpenings beyond the plan (load-bearing, prevents re-derivation):**
1. **E-INDEPENDENCE.** The regular-endpoint classification needs only W BOUNDED near τ=0 (W∈L¹), NOT W(0)=0. Since S(τ) is the smooth/finite/monotone S36 spectral action, τ=0 is regular for ANY finite E ⇒ the W(0)=0 (E=S(0)) normalization is COSMETIC, not load-bearing ⇒ the J≡0 theorem is W-magnitude- AND E-independent. So the grid-extrapolation (INFO trigger) touches only the cosmetic anchor, never the theorem. A clean S(τ)→τ=0 reduction would flip INFO→PASS but is cosmetic.
2. **U(2) SCOPE (the honest caveat).** Both endpoints regular ⇒ deficiency indices (2,2) ⇒ self-adjoint extensions = U(2) (4 real params). The plan's "every real self-adjoint extension forces J(0)=0" is correct ONLY for the SEPARATED (real Robin) sub-family — the physically admissible class (τ=0 cold-vacuum floor and τ_fold are DISTINCT configs). COUPLED (twisted-periodic/Bloch) extensions CAN carry conserved J≠0 (witnessed: complex sol u+iv has coupled_extension_J_witness=J=1) but identify τ=0≅τ_fold (S¹ topology), inadmissible for the two-distinct-endpoint interval. So J≡0 holds family-wide WITHIN the separated class; coupled excluded TOPOLOGICALLY, Vilenkin excluded by NON-SELF-ADJOINTNESS. "Robin" already means separated, so this is consistent with the plan, just scoped.

**Unitarity reading (my signature):** a self-adjoint extension IS a unitary evolution; J≡0 = the fabric leaks NO net amplitude through the τ=0 floor under ANY unitary boundary law = substrate-first reflecting/no-boundary cosmogenesis. Vilenkin outgoing = non-self-adjoint = NON-UNITARY ⇒ excluded (consistent with unitarity-non-negotiable). HH = WDW-constraint parent (J=0); "Vilenkin"-like = decohered Layer-2 branch (J≠0 for branch, J=0 for parent) — NOT a competing fundamental BC.

**Plan doc slip noted (no effect):** plan §W5-2 Def 3 parenthetical swapped Neumann/Dirichlet labels (in cosθΨ+sinθΨ′=0, θ=0 is DIRICHLET, θ=π/2 is NEUMANN = the S116-W6 case). Family-wide identity unaffected.

Strengthens the S116-W6 HH-UNCONDITIONAL verdict (Neumann → whole real self-adjoint family); capstone §5.3/§6.3 cosmogenesis may cite the family-wide J≡0. canonical_constants.py SHA drifted from plan-pin (in-session W0-1 ρ_s/C2 promotion); consumed tau_fold=0.19/G_DeWitt=5.0 are CONST-FREEZE-42, unchanged (documented per substrate-first-canonical-sourcing §(ii.B)).
