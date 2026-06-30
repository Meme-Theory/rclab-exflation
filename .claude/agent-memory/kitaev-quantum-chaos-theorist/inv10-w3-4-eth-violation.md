---
name: inv10-w3-4-eth-violation
description: INV10-W3-4 ETH-violation result — fabric beta_fabric=0.181 (eigenstate-level Ordered Veil, NEW eigenvector-axis diagnostic), cell-vs-fabric discriminator INFO
metadata:
  type: project
---

INV10-W3-4 (investigation-10 Wave 3, kitaev): ETH-violation / eigenstate-fluctuation size-scaling on the D_K spectrum. VERDICT **INFO** (sign=PASS, mag=INFO, regime=VALID). audit_sha256 `cd7ee706d47abf3c160f5d75fd3abaaafd472f8e0493c5a4642adc5bb4964d9f`. Script `computations/investigation-10/inv10_w3_eth_violation.py`.

**Why:** First EIGENVECTOR-axis integrability diagnostic in the framework — all my prior chaos functionals (⟨r⟩, OTOC, SFF, Krylov) probe eigenVALUES. ETH (Srednicki 1994): diagonal matrix element fluctuation Δ_A∝e^{-S/2}=D^{-1/2} for chaotic; integrable systems VIOLATE (Δ_A→const). β:=−d ln Δ_A/d ln D; ETH=0.5, violation→0.

**How to apply:** Cite β_fabric=0.181 as the eigenstate-level POSITIVE statement of the Ordered Veil (the fabric's eigenstates ARE non-thermal), complementary to and independent of the level-spacing results and the transit-freeze R_therm=5252. Do NOT claim the cell-vs-fabric eigenstate discriminator is resolved — it is NOT (Δβ inverted).

## Numbers (β = −d ln Δ_A / d ln D; ETH self-averaging = 0.5; →0 = max violation)
- **β_fabric = 0.181** (r²=0.956), primary operator A1 = i·γ⁰γ¹ spinor bilinear ⊗ 𝟙_rep on D_K eigenVECTORS, fixed-energy windows, D=432→11424. Δ_A flat ~0.30–0.57 across 26× D → CLEAN ETH-VIOLATION = eigenstate-level Ordered Veil ESTABLISHED for the fabric.
- β_A2 = 0.470 (L12, sector-(3,3) Peter-Weyl membership; energy-CORRELATED superposition channel, reads ETH-like); β_A2_L14 = 0.193 (deeper truncation, target (7,7), violation-leaning, consistent with A1).
- **β_cell = 0.032** (r²=1.0), s38 256-dim BCS (INTEG-39 object), number-conserving DOS-weighted occupation operator, rising-half D=28→56. Also flat.
- **Δβ = β_cell − β_fabric = −0.150** (need ≥+0.15) → discriminator INVERTED, FAILS. |β_A1−β_A2|=0.29>0.20 → operator-dependent ETH. Both INFO clauses fired.

## Load-bearing operator-design facts (verified in-session; reusable)
- The CHAOS-2/OTOC pair operator Δ=Σ_k √ρ_k P_k changes N_pair by ±1 ⇒ A=(Δ+Δ†)/√2 is IDENTICALLY ZERO within any fixed-N_pair sector (max|A_within|=0.000e+00). A diagonal-ETH test needs a NUMBER-CONSERVING operator. Use n_k-occupation (DOS-weighted) for the cell.
- Peter-Weyl sector membership is ENERGY-CORRELATED (each (p,q) at |λ|~√C₂) — a target sector must overlap the bulk window band or the fixed-energy-window std is identically 0. NOT a clean ETH probe; it reads the Berry-Tabor superposition structure, not eigenstate-thermality. Use the Clifford spinor bilinear (orthogonal to (p,q) energy labeling) as the PRIMARY fabric ETH operator.
- The L12 cache (`s84_spectrum_cache_L12_tau019.npz`) stores `abs_evals` ONLY (no eigenvectors). For matrix elements, re-diagonalize each block via `dirac_spectrum.collect_spectrum_with_eigenvectors(s, gens, f_abc, gammas, max_pq_sum)` (returns per-sector 'evals'+'evecs'+'D_pi'). p+q≤6 builds in ~6s on GPU; eigenvectors at p+q≥13 infeasible (GT-builder timeout) — L14 cross-check uses A2 on eigenVALUES only.

## Interpretation (what survives, what doesn't)
- SURVIVES: fabric ETH-violation (β=0.181, confirmed L14 β=0.193) = positive eigenstate-level Ordered Veil, an axis ORTHOGONAL to my level-spacing/SFF results. λ_L=0, no MSS issue. Kill authority NOT triggered.
- DOES NOT survive: cell-vs-fabric eigenstate-level thermalization CONTRAST. Single cell D=28–70 is too small for ETH self-averaging to set in (Brody-β=0.633 is a SPACING property; ETH self-averaging is a Hilbert-size limit) AND the occupation op is near-conserved for the 13%-non-separable near-integrable cell. The cell/fabric thermalization distinction lives in DYNAMICS (t_therm≈6 M_KK⁻¹ single-cell vs diabatic transit-freeze), NOT at the eigenstate level. C2 SHARPENED, not resolved.

## Carry-forward (genuine future work)
Larger-cell / many-cell ETH: the cell-side eigenstate-level thermalization claim needs D ≳ 10³ (a multi-cell BCS or a deeper single-cell construction) for ETH self-averaging to be testable; only then can the cell-vs-fabric β discriminator resolve. Inputs: a >256-dim chaotic-cell Hamiltonian + number-conserving local op. Gate: β_cell ≥ 0.4 at D≳10³ (cell approaches ETH) AND β_cell − β_fabric ≥ 0.15.

Links: [[integrability_hierarchy]] (add as eigenvector-axis row), [[methodology_and_data]] (operator-design + re-diagonalization lessons).
