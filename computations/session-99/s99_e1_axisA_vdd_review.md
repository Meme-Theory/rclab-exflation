# S99 W3-1 — Stage-2 Axis-A (NCG-axiomatic) Independent Cross-Review of §VII.BL E1

**Reviewer**: van-den-dungen-bridge-theorist (axis-A: spectral / NCG-axiomatic — spectral-triple factorization, almost-commutative manifolds, NCG axioms)
**Gate**: `S99-E1-STAGE2-VERIFY` (re-dispatch of the compromised axis-A leg)
**Date**: 2026-06-01
**Theorem under review**: §VII.BL E1 — "Non-LI-Deformation Necessity" (Generation-Blindness Obstruction), STAGE-1-CANDIDATE

## 0. Re-dispatch reason + reviewer-cleanliness attestation

The S99 W3-1 Stage-2 originally used `connes-ncg-theorist` as the axis-A reviewer. Per `permanent-results-registry.md §VII.BL` provenance, `connes-ncg-theorist` was a **co-author** of the S97 W-2 connes×kk workshop that authored the E1 Stage-0 candidate. This violates `joint-theorem-promotion.md §"Stage 2"` audit item 3 (cross-reviewers must NOT be original workshop authors) and the Axis-B Selection Protocol condition 2 (original-authoring-agent exclusion). The original-author leg is therefore not admissible Stage-2 evidence (workshop-internal agreement is not independent confirmation — `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2).

**Cleanliness attestation (verified, not asserted)**: I (van-den-dungen-bridge-theorist) am a clean axis-A reviewer:
- I am NOT a co-author of the S97 W-2 connes×kk workshop (the registered co-authors are `connes-ncg-theorist` [NCG-axiomatic] + `kaluza-klein-theorist` [representation-theoretic]; the registry-landing author was `kaluza-klein-theorist`).
- My project memory (`MEMORY.md` + bundle files) carries NO E1 / S97-W-2 reading-path. A grep for `S97-W-2`, `connes×kk`, `Non-LI-Deformation`, `generation-blindness` returned ZERO substantive matches; the only hits were incidental substring overlaps inside unrelated SHA-256 hex strings (`...eba91...` etc.). No `reference_*.md` re-citation of the S97 W-2 transcript exists in my memory — I pass the Axis-B Selection Protocol downstream-inheritance reach test.
- I am axis-distinct from the (excluded) original author on the NCG-axiomatic axis in methodology (spectral-triple factorization / Kasparov submersion / almost-commutative manifolds), the clean NCG-axiomatic re-leg.

**Sources read (ONLY these — the independence that IS this gate's evidentiary basis)**:
- (a) The registered §VII.BL E1 STAGE-1-CANDIDATE entry, `sessions/permanent-results-registry.md` (theorem block lines 21027–21104). **NOT the workshop transcript.**
- (b) My axis-A primary npz `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.npz` ONLY (substrate-input orthogonality: I did NOT load `s98_w3_2`, the axis-B primary data).
- (c) `joint-theorem-promotion.md §"Stage 2"` + the §W3-1 block in `sessions/session-plan/session-99-plan-w3.md`.

**Sources I did NOT read** (reading any collapses Stage-2 independence): the S97 W-2 E1 workshop transcript; connes's axis-A outputs (`s99_e1_axisA_verdict.json` / `s99_e1_axisA_review.md`); dirac's axis-B fragment (consumed only by the closeout script, NOT for forming my verdict); any synthesis re-narrating the workshop reading-path.

## 1. Clause assignment (axis-A scope)

Per the §VII.BL clause table (registry lines 21069–21076) and `joint-theorem-promotion.md §"Stage 2"`, my axis-A scope is: the axis-A-authored single-axis clauses (a), (b), (f) PLUS the JOINT clauses (d), (e). The W3-1 plan maps these to the verdict-fragment fields:
- **single_axis_clause = clause_7_generation_blindness** — the ε_LX between-generation generation-blindness corridor (the spectral/Yukawa column #7); covers registry clauses (a) [multiplicity-scalar π], (b) [reality innocent], (f) [order-one residual constraint].
- **joint_clause = joint_nonLI_necessity** — registry JOINT clauses (d) [geometry's natural delivery IS generation-blind] + (e) [unique surviving channel is external non-LI ε_LX]; the NON-LI-DEFORMATION-NECESSITY conjunction.

## 2. First-principles audit — SINGLE-AXIS clause #7 (generation-blindness)

I formed this verdict from the npz structural quantities + an independent Sage derivation of the load-bearing Skolem-Noether fact, BEFORE any cross-reading.

### 2.1 The degeneracy is exact (the obstruction's signature)

`gen_lambda0 = [0.81974111, 0.83589351, 0.83589351]`, `gen_mult = [1, 3, 3]`. The two generation-carrying multiplicity copies (`t=1`, `t=2`) have IDENTICAL lightest |λ| (`gl[1]−gl[2] = −4.44e-16` = machine-ε; the exact identity `spec|_{t=1} = spec|_{t=2}` is structural). A spectrum-only / `A_K`-scalar functional therefore sees:
```
n_distinct = 2  EXACT  (not 3)
R_cross = max(gl)/min(gl) = 1.0197042646  (registry 1.0197042646; INVARIANT at all L_max)
```
This is the EXPECTED signature of a multiplicity-scalar representation, NOT a failure of reality — exactly as the registry's "Reality is INNOCENT (R3-0)" relocation states.

### 2.2 Skolem-Noether multiplicity-blindness — INDEPENDENTLY verified (Sage)

The load-bearing NCG-axiomatic fact (registry clause (a) + the "Twisted-Ω¹ escape PROVEN dead, R3-1" paragraph) is that **every `σ ∈ Aut(A_K)` is multiplicity-scalar**. I verified this from first principles (not by reading the workshop):

- `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` has three simple Wedderburn summands with ℝ-dimensions {1, 4, 18} — **pairwise distinct**, and distinct centers (ℂ, ℝ, ℂ). No two summands are isomorphic ⇒ no outer automorphism can permute summands.
- **Skolem-Noether** (every automorphism of a central-simple algebra over its center is inner) applied per summand ⇒ every `σ ∈ Aut(A_K)` is **block-inner**: `σ(a) = (u₁, u_H a u_H⁻¹, g a g⁻¹)`.
- Under Peter-Weyl `π(a) = ⊕_{(p,q)} π_{(p,q)}(a) ⊗ 1_{m(p,q)}`, a block-inner `σ` maps to `π_{(p,q)}(u) ⊗ 1_{m(p,q)}` — **SCALAR (identity) on the multiplicity leg `ℂ^{m(p,q)}`**.
- The twisted commutator `[D, a]_σ = ⊕ (D_{(p,q)} π_{(p,q)}(a) − π_{(p,q)}(σ(a)) D_{(p,q)}) ⊗ 1_{m(p,q)}` inherits the orbital-block-scalar obstruction VERBATIM.

**This is the one-line death of the twisted-inner escape, and it is squarely in my domain** (almost-commutative manifolds + NCG axioms + the structure of `Aut` on a finite spectral-triple algebra). It holds; I confirm it independently.

### 2.3 Inner-fluctuation impotence + the complement

- `order_one_residual = 0.0` EXACT: the order-one condition `[[D_K, a], Jb*J⁻¹] = 0` (Axiom 5; the surviving 6/7-axiom structure) holds, so the inner-fluctuation orbit stays multiplicity-scalar; `conj_i_order_one = True`.
- The generation-lifting datum must live in the COMPLEMENT `⊕ 1_{V_{(p,q)}} ⊗ M_{m(p,q)}(ℂ)`, orthogonal to `image([D_K, −])`. This complement is **non-empty** precisely because `m(p,q) = 3 > 1` for the generation copies. So `ε_LX` is outside EVERY `A_K`-module (inner, twisted-inner, opposite-action) — a Morita-invariant module-membership statement (the Hochschild 1-cochain `a ↦ [D_K, a]` takes values in the multiplicity-scalar subalgebra), **not** a `D_K`-spectrum accident. No `D_K` re-tuning detunes it.

### 2.4 ε_LX is a legitimate external non-LI fix (consistency)

- `nonscalar_norm = 1843.51 > 0`: `ε_LX` acts non-trivially on the multiplicity index (it IS in the complement).
- `reality_swap_residual = 4.44e-16 ≈ 0`, `eps_LX_hermitian_residual = 0.0`, `reality_ok = True`: `[J, D_K + ε_LX] = 0` is satisfiable block-by-block — reality (W1) preserved.
- Hierarchy delivery (consistency, not the gate criterion): `eps_LX_diag = [0, 168.66, 2849.59]`, `y_derived = [0.82, 169.5, 2850.4]`, `logdist_r1 = logdist_r2 = 0.0`, `sign_correct = True`, `conj_iv_band = True` — `ε_LX` reproduces the target mass ratios on the monotone branch.

**SINGLE-AXIS clause #7 verdict: PASS.** The generation-blindness obstruction is an NCG-axiomatic structural fact (multiplicity-scalar representation, forced by left-invariance + Skolem-Noether), the inner-fluctuation orbit is provably impotent (order-one-respecting and multiplicity-scalar), and the fix `ε_LX` is a reality-compatible external non-LI connection outside every `A_K`-module. Confirmed from first principles on the spectral / NCG-axiomatic axis.

## 3. First-principles audit — JOINT clause: NON-LI-DEFORMATION-NECESSITY

The joint clause asserts the Jensen non-left-invariant deformation is **necessary** for generation-blindness (and, conjoined with the #9 column, that the same non-LI deformation class underlies BOTH generation-blindness AND baryogenesis uniqueness). The NCG-axiomatic contribution is the **obstruction half** (registry clauses (d), (e)):

- **(d)** combining (a) [multiplicity-scalar `π`] + (c) [generations = SU(3) Z₃-triality Peter-Weyl multiplicity, `proven_384`]: the geometry's NATURAL delivery (the multiplicity index) is EXACTLY the generation-blind case. A Yukawa hierarchy cannot be a free output of SU(3)-geometry + inner/twisted fluctuations.
- **(e)** the unique surviving channel is an explicit non-LI `ε_LX` acting non-trivially on the multiplicity index, reality-compatible and order-one-constrained, but OUTSIDE every `A_K`-module.

**Necessity (not merely sufficiency)** follows on the NCG axis from the two-wall schema: homogeneity (W2, left-invariance) is *exactly what forces* the multiplicity-scalar representation (a left-invariant `D_K` commutes with the right-translation generators ⇒ `π` acts on the left-regular factor only ⇒ scalar on `ℂ^{m(p,q)}`). Hence ANY mechanism lifting the degeneracy while preserving reality (W1) MUST break left-invariance on the multiplicity leg — it MUST be a non-LI deformation. There is no `A_K`-internal escape (§2.2 closes inner, twisted-inner, opposite). Non-removability confirmed: `P_nLI = 8.15e+06 > 0` (`‖ε_LX‖²`; `conj_iii_nonremovable = True`).

**The shared design rule** (`shared_design_rule = True`) confirms #7 (Yukawa) and #9 (baryogenesis) share the `{W1 satisfiable} ∧ {W2 mandatory} ∧ {W3 inner-fluctuation impotent}` schema with the common anchor `P_nLI = ε² = 4e-04` (`P_nLI_baryogen_anchor = 0.0004`). From the NCG-axiomatic axis this means: the SAME class of external non-LI deformation is necessary for both intrinsically-rigid matter-sector asymmetries. The genus predicate of the NON-PROMOTION-BY-HELD-NUMBER overlay (STRUCTURE permanent-eligible ∧ NUMBER held ∧ not sideways-re-pinned) holds with the sign-lock differentia (`R_cross` locked to 1 by representation theory; the lab hierarchy magnitude held against substrate-natural extraction because `ε_LX` is an external datum the spectral triple does not encode).

**JOINT clause NON-LI-DEFORMATION-NECESSITY verdict (axis-A): PASS.**

### η_B 2.66× / 0.42-dec refined-suppression drift note (non-blocking)

The §VII.BL #9 anchor reports `η_B = 1.700e-11` (registry line 21082); the W3-2 plan column reports `η_B = 4.517492e-11` (S99 plan-w3 line 22). The ratio `4.517e-11 / 1.700e-11 = 2.66×` = 0.42 decades. This is a **refined-suppression drift** in the #9 baryogenesis MAGNITUDE between the registry snapshot and the S98-W3-2 recomputation — both values sit inside the same `(0, 6e-10)` BBN window, so the column-#9 PASS predicate (`η_B ∈ (0, 6e-10)`) is unaffected. It is **non-blocking** for the joint NECESSITY clause I audit on axis-A: the joint clause is a module-membership / necessity statement (the SAME non-LI deformation class is needed for both frontiers), structurally independent of the precise `η_B` magnitude. The drift lives entirely on the axis-B (substrate/CP) primary data `s98_w3_2`, which by substrate-input orthogonality I did NOT load and do NOT adjudicate; I record it here for the closeout and for the orchestrator's awareness, NOT as a clause finding.

## 4. Axis-A verdict summary

| Clause | Scope | Axis-A verdict | Basis |
|:-------|:------|:---------------|:------|
| #7 generation-blindness (a,b,f) | single-axis | **PASS** | multiplicity-scalar π (Skolem-Noether, Sage-verified); n_distinct=2 EXACT; order_one_residual=0.0; ε_LX non-scalar & reality-compatible, outside every A_K-module |
| NON-LI-NECESSITY (d,e) | JOINT (PASS-AND) | **PASS** | W2 (left-invariance) forces multiplicity-scalar rep ⇒ non-LI deformation NECESSARY; P_nLI>0 non-removable; shared {W1∧W2∧W3} schema with #9, common anchor ε²=4e-04 |

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`): the fabric IS the spectral triple `(A_K, H_K, D_K, J)` on Jensen-deformed SU(3); generations ARE the Peter-Weyl multiplicity of `D_K`'s representation. That representation is multiplicity-scalar BY HOMOGENEITY, so the fabric's own differential calculus (every inner/twisted/opposite form it can build) is BLIND to the generation index. The Yukawa hierarchy is therefore NOT supplied by the fabric's intrinsic geometry; it measures how far the fiber connection is deformed AWAY from homogeneity (the non-LI `ε_LX`) — direction `D_K multiplicity-scalar representation → (W1∧W2 forbid intrinsic hierarchy) → hierarchy ∈ external non-LI ε_LX → measured SM masses`. The substrate is logically prior; the hierarchy is a deformation datum, not a container the masses sit inside.

## 5. Verdict fragment

Written to `computations/session-99/s99_e1_axisA_vdd_verdict.json` (this review's machine-readable companion). Composite PASS-AND closeout (Step 2) consumes this fragment + the EXISTING clean axis-B fragment `s99_e1_axisB_verdict.json` (dirac-antimatter-theorist, a non-author; axis-B is valid and stands). I did NOT read the axis-B fragment for forming THIS verdict — only the closeout consumes it.
