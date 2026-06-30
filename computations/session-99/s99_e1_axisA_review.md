# S99-E1-STAGE2-VERIFY — Axis-A (spectral / NCG-axiomatic) Independent Cross-Review

**Reviewer**: connes-ncg-theorist (Axis-A: spectral / NCG-axiomatic)
**Gate**: S99-E1-STAGE2-VERIFY — Stage-2 cross-axis independent-verify of §VII.BL E1 "Non-LI-Deformation Necessity" joint theorem
**Sources read** (independence-disciplined): the registered §VII.BL E1 STAGE-1-CANDIDATE entry block in `sessions/permanent-results-registry.md` (lines 21027–21104); the axis-A primary npz `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.npz` ONLY; `joint-theorem-promotion.md` §"Stage 2"; the §W3-1 plan block.
**NOT read**: the S98-W3 workshop transcripts, the S98 W3 working-paper sections, `s98_w3_2_baryogen_uniqueness.npz` (axis-B data — withheld to preserve substrate-input orthogonality), any synthesis re-narrating the workshop reading-path. `workshop_transcript_read = false`.
**Verification artifact**: `computations/session-99/s99_e1_axisA_check.py` (5 first-principles checks, all PASS).

## Verdicts

| Clause | Verdict |
|:-------|:--------|
| **Single-axis clause #7** (generation-blindness / ε_LX between-generation corridor) | **PASS** |
| **JOINT clause** (NON-LI-DEFORMATION-NECESSITY, spectral-axis contribution) | **PASS** |

Both verdicts are first-principles, NOT a rubber-stamp: I independently re-derived the multiplicity-scalar obstruction, the Skolem–Noether closure of the twisted escape, and the A_K-module exhaustion that grounds necessity, and I resolved a genuine internal-tension flag (the t=1/t=2 degeneracy) before certifying.

---

## 1. Single-axis clause #7 — generation-blindness corridor (PASS)

The clause asserts that ε_LX between generations = 0.0 (scheme `NCG-INNER-FLUCT-EXTERNAL-NONLI`) is an NCG-inner-fluctuation / external-non-LI structural fact: the Yukawa inner fluctuation does not distinguish generations; the Z₃-triality symmetry of the SU(3) Peter-Weyl multiplicity protects the degeneracy. I verify three things from the spectral side.

### 1.1 The obstruction is NCG-axiomatic, not a D_K-spectrum accident

The Peter-Weyl representation is multiplicity-scalar:

```
π(a) = ⊕_{(p,q)} π_{(p,q)}(a) ⊗ 1_{m(p,q)}                                    (registry line 21048, 21071)
```

An inner fluctuation `A = Σ aᵢ [D_K, bᵢ]` has all `aᵢ, bᵢ ∈ A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`. Because `D_K` is block-diagonal in Peter-Weyl (PROVEN, D_K block-diagonality universality, machine-ε) and `π` is multiplicity-scalar, every commutator `[D_K, b]` — and hence `A` — lies in `⊕_{(p,q)} B(V_{(p,q)}) ⊗ 1_{m(p,q)}`: it acts as a **scalar on each multiplicity factor `ℂ^{m(p,q)}`**. The real-image `ε' JAJ⁻¹` is the opposite-action image of the same algebra and is therefore also multiplicity-scalar. Equivalently (registry line 21080): the Hochschild 1-cochain `a ↦ [D_K, a]` takes values in the multiplicity-scalar subalgebra. **This is module-membership, Morita-invariant — not a spectral coincidence. No re-tuning of `D_K` can detune it.** This grounds clause (a) of the registered table.

### 1.2 Numerical confirmation of the obstruction signature (with a resolved internal-tension flag)

`s98_w3_1` reports `R_cross_loaded = 1.0197042646288914` (registered theorem: 1.01970), `n_distinct = 2`, `gen_mult = [1, 3, 3]`, `gen_lambda0 = [0.81974, 0.83589, 0.83589]`.

A first-principles cross-reviewer must not rubber-stamp `n_distinct = 2`. My initial test used bit-exact `gen_lambda0[1] == gen_lambda0[2]` and it returned **False** — flagging a potential gap. Investigation resolved it decisively:

- `gen_lambda0[2] − gen_lambda0[1] = 4.440892e-16` (absolute), relative `5.31e-16`.
- The float64 dense-Hermitian eigensolve floor at the `λ ≈ 0.84` scale is `eps·λ ≈ 1.86e-16`; the observed split is **2.39 × that floor ≈ 2 ULP**.
- `n_distinct = 2` is **stable from tolerance 1e-9 all the way to 1e-15**.

So t=1 and t=2 ARE degenerate as a **representation-class identity** (Z₃-triality charge-conjugation pairs `t=1, t=2`), realized numerically to machine precision; the 4.44e-16 difference is pure diagonalization round-off, NOT a physical splitting. **The theorem's Level-1 claim ("`R_cross = 1` by Skolem–Noether + Peter-Weyl, regulator-invariant, holds at every `L_max`") is vindicated.** The correct operational degeneracy test is `n_distinct = 2` at any physically-meaningful tolerance (which the npz uses), not bit-exact equality.

### 1.3 The corridor value = 0.0 is the log-distance of the EXTERNAL fix (not "ε_LX = 0")

The verdict-line headline `value = 0.0` could be naively misread as "ε_LX vanishes" — which would re-assert the obstruction, not the fix. The npz disambiguates: `value == max_logdist == logdist_r1 == logdist_r2 == 0.0`, and `r1_derived = r1_target = 206.768`, `r2_derived = r2_target = 16.817`. So the headline 0.0 is the **log-distance residual between the ε_LX-derived inter-generation ratios and their PDG targets** — i.e. once the external non-LI ε_LX is admitted, it reproduces the hierarchy EXACTLY (zero residual). The ε_LX itself is a genuine non-`A_K`-module object (§1.4 below, CHECK 3), nonzero on the multiplicity index. This reading is load-bearing and confirmed.

### 1.4 ε_LX is a genuine external non-LI object (four conjuncts)

The registered corollary (registry line 21043) demands ε_LX break W2 while preserving W1, order-one-compatible, non-gauge-removable. `s98_w3_1` satisfies all four:

| Conjunct | Quantity | Value | Reading |
|:---------|:---------|:------|:--------|
| **W2-break** | `nonscalar_norm` | 1843.51 (> 0) | ε_LX acts non-trivially on the multiplicity index — outside the multiplicity-scalar image |
| **W1 reality** | `reality_swap_residual`, `eps_LX_hermitian_residual` | 4.44e-16, 0.0 | `[J, D_K + ε_LX] = 0` satisfiable; reality preserved |
| **order-one** | `order_one_residual` | 0.0 (< 1e-10 floor) | order-one compatible (Axiom 5) |
| **non-removable** | `P_nLI` | 8.15e6 (> 0) | not gauge-removable |

**Single-axis clause #7 verdict: PASS.** The inner-fluctuation orbit is generation-blind (obstruction, §1.1–1.2); the corridor value=0.0 is the external non-LI fix's exact-reproduction residual (§1.3); and the ε_LX is a bona-fide non-`A_K`-module object (§1.4). All provenance tags (`NCG-INNER-FLUCT-EXTERNAL-NONLI`, `a_4^{Mellin}` poleconv-A-double s=2/n=4, τ=0.19, L_max=12) match the named theorem object (CHECK 4).

---

## 2. JOINT clause — NON-LI-DEFORMATION-NECESSITY (spectral axis, PASS)

The JOINT clause (registered clauses (d)+(e), lines 21074–21075; W3-1 plan-block line 109) asserts the non-LI Jensen deformation is **NECESSARY** for generation-blindness — geometry's natural delivery IS generation-blind (d), and the unique surviving channel is the external non-LI ε_LX (e) — and that this same non-LI deformation underlies BOTH generation-blindness AND baryogenesis uniqueness. As the Axis-A reviewer I audit the spectral-axis contribution to necessity, with adversarial scrutiny of exhaustiveness.

### 2.1 Necessity by exhaustion of A_K-modules (the spectral-axis core)

Necessity is an **exhaustion** claim: I verify that every operator constructible from the spectral-triple data `(A_K, H_K, D_K, J)` is built from a closed list of primitives, all multiplicity-scalar:

1. **Inner fluctuations** `A = Σ aᵢ[D_K, bᵢ]` — multiplicity-scalar (§1.1).
2. **Real-image** `ε' JAJ⁻¹` — opposite-action image of the same algebra, multiplicity-scalar.
3. **Twisted-inner** `Ω¹_σ` for any `σ ∈ Aut(A_K)` — **dead by Skolem–Noether** (§2.2).
4. **SU(3)-equivariant geometric deformation** (Casimir-function τ) — the only metric freedom on a homogeneous space; block-diagonal, multiplicity-scalar.

The differential calculus `Ω¹_{D_K}(A_K)` is *generated* by `a₀[D_K, a₁]`; there is no fifth class of `A_K`-intrinsic object. Therefore the Hochschild 1-cochain `[D_K, −]` has its image strictly inside the multiplicity-scalar subalgebra `⊕ B(V_{(p,q)}) ⊗ 1_{m(p,q)}`, and the generation-lifting datum MUST live in the orthogonal complement `⊕ 1_{V_{(p,q)}} ⊗ M_{m(p,q)}(ℂ)` (registry line 21080) — which is non-left-invariant (external) by construction. **This is necessity from first principles ("the complement is unreachable by the cochain"), NOT an empirical "we tried things and they failed."**

### 2.2 The twisted escape is genuinely closed (independent Skolem–Noether check)

The most plausible escape from the obstruction is a twisted inner module `Ω¹_σ`. I verified independently that it is dead: `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` has simple summands of dimensions 1, 2, 3 — **all distinct, no isomorphic pair to permute**. By Wedderburn + Skolem–Noether, every `σ ∈ Aut(A_K)` is therefore inner on each simple summand: `σ(a) = u a u*` per block. Hence `π(σ(a)) = π_{(p,q)}(u) π_{(p,q)}(a) π_{(p,q)}(u)* ⊗ 1_{m(p,q)}` — still multiplicity-scalar — and the twisted commutator `[D, a]_σ = ⊕ (D_{(p,q)} π_{(p,q)}(a) − π_{(p,q)}(σ(a)) D_{(p,q)}) ⊗ 1_{m(p,q)}` inherits the orbital-block-scalar obstruction verbatim. **`Aut(A_K)` is multiplicity-blind.** The one-line death holds; I find no gap in it.

### 2.3 Reality is INNOCENT (the obstruction is W2, not W1)

A spectral-axis reviewer must confirm the obstruction is correctly located. The registered theorem (line 21037) relocates it from `[J, D_K] = 0` (reality) to the multiplicity-scalar representation (homogeneity). I confirm: reality is satisfied BY CONSTRUCTION for every inner fluctuation (J-protection `[J, A + ε'JAJ⁻¹] = 0` EXACT) and block-by-block for ε_LX (`reality_swap_residual = 4.44e-16`, `eps_LX_hermitian_residual = 0`, CHECK 3). So `[J, D_K + ε_LX] = 0` is satisfiable; the KO-dim-6 factorization `J = J_K ⊗ J_F` (0+6=6, PROVEN) is never sacrificed. The gate FAIL signature (`R_cross = 1.01970`, `n_distinct = 2`) is the EXPECTED signature of a multiplicity-scalar representation, not a reality failure. This grounds clause (b).

### 2.4 The BOTH-frontiers conjunction — what the spectral axis can and cannot certify

The JOINT clause's full statement (plan-block line 109) is that the non-LI deformation underlies BOTH generation-blindness AND baryogenesis uniqueness *simultaneously*. From the spectral axis:

- **Generation-blindness necessity**: fully certified above (§2.1–2.3).
- **Shared two-wall schema**: the registered entry shows both frontiers (#7 Yukawa, #9 baryogenesis) share `{W1 satisfiable} ∧ {W2 mandatory} ∧ {W3 inner-fluctuation impotent}` (registry line 21082; table 21086–21093). The spectral-column npz carries the shared anchor `P_nLI_baryogen_anchor = 4.0000e-04` and `shared_design_rule = True` (CHECK 5). I confirm the schema and anchor are present and consistent on the spectral side.
- **Baryogenesis-side substantiation** (`η_B ∈ (0, 6e-10)`, `φ_CP` forced π/2, the φ₈₈-Cartan δA): this lives in `s98_w3_2`, which I **deliberately did NOT load** to preserve substrate-input orthogonality. It is the Axis-B reviewer's audit domain.

**The division is correct and protocol-mandated.** I certify the spectral-axis half of the JOINT clause (generation-blindness necessity + the shared design-rule schema + the shared anchor value). The full BOTH-frontiers conjunction is PASS-AND-complete only when my spectral-axis verdict is combined at closeout with the Axis-B reviewer's independent baryogenesis verdict (logical AND, per `joint-theorem-promotion.md` §"Stage 2"). The substrate-input-orthogonality predicate is SATISFIED: `s98_w3_1` (ε_LX, spectral) feeds exactly this reviewer; `s98_w3_2` (baryogenesis, substrate) feeds exactly the Axis-B reviewer — disjoint inputs.

**JOINT clause spectral-axis verdict: PASS.**

---

## 3. Adversarial cross-review notes (recorded honestly; not FAIL triggers)

1. **t=1/t=2 degeneracy flag — RESOLVED.** My CHECK 1 initially FAILed on a bit-exact `==` degeneracy test. Resolution: the 4.44e-16 split is 2.39 ULP — pure dense-Hermitian-eigensolve round-off on a structurally-exact representation-class degeneracy (`n_distinct = 2` stable 1e-9→1e-15). The correct test is tolerance-based, and it PASSES. This is the kind of internal tension a first-principles cross-review exists to catch; it does not undermine the theorem — it confirms the Level-1 "regulator-invariant `R_cross = 1`" claim is realized to machine precision.

2. **JOINT-clause completeness depends on the AND.** The full "non-LI underlies BOTH frontiers" conjunction is complete only under PASS-AND with Axis-B. My fragment certifies the spectral half. This is by design (substrate-input orthogonality), not a sufficiency gap.

3. **Level-2 NON-BINDING is correctly classified.** The envelope is structurally-exact (`R_cross = 1` identically; no `c_continuum`). The entry is correctly tagged an INTRA-PILLAR OBSTRUCTION + NON-PROMOTION-BY-HELD-NUMBER overlay with the sign-lock differentia, NOT a 5-anatomy convergence bridge — so it clears the HARD-HALT auditor by classification (registry line 21033). I find this classification sound: the bridge map is a cokernel/obstruction map, not an HKR/Connes–Karoubi continuum pairing.

4. **No spectral-axis sufficiency gap found.** The exhaustion of `A_K`-modules is complete (inner, real-image, twisted-inner via Skolem–Noether, SU(3)-equivariant geometric); the complement is unreachable by the Hochschild cochain; reality is preserved. The spectral-side necessity argument is airtight.

## 4. Summary

From the spectral / NCG-axiomatic axis, operating WITHOUT the S98-W3 workshop transcript and reading only the registered §VII.BL E1 entry + `s98_w3_1`:

- **Single-axis clause #7 (generation-blindness corridor): PASS.**
- **JOINT clause (NON-LI-DEFORMATION-NECESSITY, spectral contribution): PASS.**

The independent agreement is structural, not shared-context: my route is the multiplicity-scalar Peter-Weyl representation + Skolem–Noether `Aut(A_K)`-multiplicity-blindness + Hochschild-cochain complement-unreachability — derived from the registered entry alone. The composite S99-E1-STAGE2-VERIFY verdict and the PASS-AND collapse with Axis-B are the closeout's responsibility, not mine.
