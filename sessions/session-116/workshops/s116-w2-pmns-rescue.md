# S116-W2-PMNS-RESCUE — Lepton shape-leg: ε_LX rescue vs §VII.CK wall

**Date**: 2026-06-27
**Gate**: `S116-W2-PMNS-RESCUE` (gate_type: workshop, Wave 2, Session 116)
**Format**: 2-agent adversarial adjudication, 3 rounds, sequential turns on this shared document
**Agents**: `connes-ncg-theorist` (NCG homogeneity/commutant wall — argues **WALLED**) vs `neutrino-detection-specialist` (PMNS sector-asymmetry phenomenology — argues **ε_LX-RESCUABLE**)
**Closure**: artifact-existence (NO verdict line, per `wave-classification.md §M1`). Must end with R1/R2/R3 filled + `## Structural Verdict` (one pinned position: Track A ε_LX-rescuable OR Track B walled, + the ε_LX epistemic-status sub-verdict + sub-(a)/(b)/(c)) + `## Wrap-Up`.

## Adjudication Question

> The S115 INTERNAL forced `A_K⋊SU(3)_R` circulant lepton texture WASHED OUT — tri-maximal `|U_ij|²=1/3`, `J=1/(6√3)=0.0962` locked by rephasing invariance (a coset-diagonal `U_L` leaves `J` invariant; `J_scan_spread=8.3e-17`), `dev=1.92 ≫ band`, `J_obs=0.0329`. The registry D4-disposition tags lepton-PMNS as **RESONANT-CONDITIONAL** (~2.9× from observed, on the ℂ⊕ℍ charged-lepton-vs-neutrino sector-asymmetry) vs quark-CKM **FALSIFIED** (~3124×) — leptons are ~1000× closer.
>
> **THE FORK**: Does the EXTERNAL ε_LX multiplicity-bundle charge-class (the §VII.BL/§VII.CK external SHAPE handle, the ONLY surviving internal-wall escape) **RESCUE** the lepton shape leg — i.e., does the ℂ⊕ℍ sector-asymmetry supply a genuine substrate texture handle that breaks the tri-maximal degeneracy and lands PMNS in the observed band (a DERIVATION, like the quark down-texture S111-W3-1) — OR is the lepton sector **PERMANENTLY WALLED** by the SAME §VII.CK multiplicity-scalar theorem that walls the quark sector (the 2.9× a symmetric-limit coincidence)?
>
>   (a) Is the ℂ⊕ℍ charged-lepton/neutrino sector-asymmetry a genuine substrate DOF that distinguishes leptons from quarks for the PMNS texture, or is it §VII.BL-blind — a fiber-charge distinction (which 16-dim SM rep, not which generation) the multiplicity-bundle ε_LX cannot see (the same blindness that HELD the quark same-gen J-conjugacy)?
>   (b) Does admitting ε_LX count as a "rescue/derivation," or is it an EXTERNAL input with the same external-as-a-coupling status as the §VII.CK D4 crossed product (a coupling, not a derivation)?
>   (c) Given the quark precedent's mass-vs-mixing tension (S111-W3-1: `V_us=0.3107` overshoots 0.225 by 38% precisely BECAUSE the texture magnitudes that break the mass log-gap force too large a 1-2 rotation), does the lepton ε_LX texture face the SAME tension (PMNS angles/J overshoot when the charged-lepton masses fit), or does the sector-asymmetry RELIEVE it (the extra ℂ⊕ℍ freedom decouples mass-fitting from mixing-fitting)?

## Competing Positions (each first-principles-backed; the workshop derives which is correct)

- **connes-ncg-theorist (NCG homogeneity/commutant wall) — WALLED.** The §VII.CK + §VII.BL multiplicity-scalar theorem walls the lepton sector INTERNALLY exactly as it walls the quark sector. The bare `D_K` is generation-blind (generation = Z₃-triality multiplicity index); the forced circulant is washed out by rephasing invariance; the ONLY shape handle is the EXTERNAL ε_LX. Admitting ε_LX is not a "derivation" — it is an external charge-class (external-as-a-coupling, same status as the D4 crossed product). PMNS is "walled" in the SAME structural sense as CKM; the 2.9× residual is the wall, not a near-miss. Sector-asymmetry (a) is a FIBER-CHARGE distinction the multiplicity-bundle ε_LX is §VII.BL-blind to.
- **neutrino-detection-specialist (PMNS sector-asymmetry phenomenology) — ε_LX-RESCUABLE.** The lepton sector's ℂ⊕ℍ charged-lepton-vs-neutrino asymmetry is a genuine substrate DOF the M₃(ℂ)-shared quark sector LACKS (the quark negative control gave `U_mix=identity` precisely because both chiralities share the M₃(ℂ) leg). That asymmetry lets a NON-coset-diagonal `U_eL` break the tri-maximal lock where the quark sector cannot — the registry's own "RESONANT-CONDITIONAL ~2.9×" tag encodes this. The ε_LX texture on the asymmetric lepton sector is a substrate-derived PMNS texture, not a fit; the 2.9× is a near-miss the external SHAPE handle closes.

**Numeric stakes**: `J_obs=0.0329` (NuFIT 5.2 NO band [0.0086, 0.0331]); `J_forced=1/(6√3)=0.0962` (locked); lepton residual ~2.9× vs quark ~3124×; quark precedent `V_us=0.3107` vs PDG 0.225 (38% overshoot, `mass_grp=5/6` with slot-6 the sole FAIL).

**Adjudication rule**: the workshop produces a STRUCTURAL VERDICT (one pinned position) on whether the lepton shape leg is **(A) ε_LX-RESCUABLE** (a substrate handle quarks lack) or **(B) WALLED** like the quark sector — AND on the epistemic status of ε_LX (derivation vs external coupling). The verdict FRAMES the interpretation of the W2-3 compute number (in-band under Track A = derivation; in-band under Track B = external fit). The two agents must GENUINELY diverge across R1/R2/R3.

**Substrate framing**: PMNS mixing IS the representation-theoretic content of `D_K` — generation = SU(3) Peter-Weyl Z₃-triality multiplicity. The lepton mass/mixing texture is a feature of the EXTERNAL non-left-invariant ε_LX on the multiplicity-bundle complement of the `[D_K,−]` image (§VII.BL), NOT of the bare (generation-blind) `D_K` spectrum. Direction of explanation flows from `D_K` outward; the lab PMNS angles are the emergent image, never the starting point.

**Sources** (read all before writing):
1. `sessions/permanent-results-registry.md §VII.CK` (D4-disposition: lepton-PMNS RESONANT-CONDITIONAL ~2.9×; quark-CKM FALSIFIED ~3124×)
2. `computations/session-115/s115_gate_verdicts.txt` (S115-LEPTON-PMNS-FORCED-TEXTURE: FAIL — internal forced circulant washed out, J locked to 1/(6√3))
3. `computations/session-115/s115_lepton_pmns_forced_texture.py` (the rephasing-invariance decider)
4. `computations/session-111/s111_gate_verdicts.txt` (S111-CF-YUK-FULLFLAVOR: PASS — quark ε_LX precedent, mass_grp=5/6, V_us=0.3107 overshoots 0.225 by 38%)
5. Rank-1 Yukawa (S62, proven_2186: J_12/J_23=19.52 algebraically constant, rank-deficient per-generation)
6. R_S96_matter_hierarchy (the hierarchy anchor)
7. the §VII.BL ε_LX external-class note (multiplicity-bundle SHAPE/MAGNITUDE channel; S98-W3-1 existence-PROVEN; §VII.BL STAGE-3-PERMANENT generation-blindness)

---

## Round 1 — Opening Positions (steelman your assigned side)

### R1 · connes-ncg-theorist — WALLED steelman

**Thesis.** PMNS is walled INTERNALLY by the §VII.CK + §VII.BL multiplicity-scalar theorem in the *identical structural sense* as CKM. The lepton sector is not "~1000× closer to a derivation"; it is exactly as far from one. The substrate is generation-blind by **homogeneity**; the generation-texture handle lives in the **commutant** of the algebra that builds every internal functional; and the ℂ⊕ℍ sector-asymmetry — though a genuine fiber feature — is *provably inert on the Jarlskog* (S115, `J_scan_spread = 8.3e-17`). The 2.9× residual IS the wall measured in the J-ratio, not a near-miss. It is small only because the observed PMNS happens to sit near a Z₃-symmetric attractor of the multiplicity-scalar structure — a coincidence of where the data lands, not a property the substrate derives.

#### 1. The homogeneity wall (why `D_K` is generation-blind, quarks and leptons alike)

The substrate IS the spectral triple `(A_K, H_K, D_K, γ₉, J)` on Jensen-deformed SU(3), `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`. Peter–Weyl factorizes the Hilbert space (§VII.BL `proven_384`):

> **(1)**  `H_K = ⊕_{(p,q)} V_{(p,q)} ⊗ ℂ^{m(p,q)} ⊗ ℂ¹⁶`,   generation leg = `ℂ^{m(p,q)}`, generation index = `t = (p−q) mod 3`.

`A_K` acts by the LEFT-regular representation on the carrier `V_{(p,q)}` and by the SM fiber action on `ℂ¹⁶`; it is the **identity** on the multiplicity leg:

> **(2)**  `π_L(a) = ⊕_{(p,q)} π_{(p,q)}(a) ⊗ 1_{m(p,q)} ⊗ ρ_{fiber}(a)`,   `a ∈ A_K`.

`D_K` is the LEFT-INVARIANT (homogeneous) Dirac operator, so it commutes with the entire right-regular SU(3)_R, hence `D_K = ⊕ D_{(p,q)} ⊗ 1_{m(p,q)}` — **multiplicity-scalar** on the generation leg. This is §VII.BL STAGE-3-PERMANENT: every `A_K`-built form (inner fluctuation `A = Σ aᵢ[D_K,bᵢ]`, real image `ε'JAJ⁻¹`, twisted-inner `Ω¹_σ`) is `⊗1` on `ℂ^{m(p,q)}` and therefore **cannot lift the generation degeneracy**. The twisted escape is DEAD by Skolem–Noether: the three simple summands `{ℂ, ℍ, M₃(ℂ)}` have ℝ-dimensions `{1,4,18}`, pairwise non-isomorphic with distinct centers, so every `σ ∈ Aut(A_K)` is block-inner ⇒ `Aut(A_K)` is multiplicity-blind. **This wall is sector-blind: it is a statement about the LEFT-regular action of `A_K`, which is shared verbatim by the lepton (`ℂ⊕ℍ`) and quark (`M₃(ℂ)`) fibers.**

#### 2. The commutant wall (why the handle is external, not "inside `A_K` with more effort")

The generation-texture handle must be NON-scalar on `ℂ^{m(p,q)}`. But the differential calculus that builds every internal functional is confined to the carrier:

> **(3)**  `Ω¹_{D_K}(A_K) = span{ a[D_K,b] : a,b ∈ A_K } ⊆ ⊕_{(p,q)} B(V_{(p,q)}) ⊗ 1_{m(p,q)}`.

The multiplicity leg `ℂ^{m(p,q)}` is precisely the **commutant** of `A_K`'s left-regular action (it carries the conjugate right-regular SU(3)_R — S114 W3-1 Peter–Weyl fact). The closing theorem (§VII.CK D4, the commutant identity, `A_F`-INDEPENDENT): *no algebra's own differential calculus reaches its commutant non-scalarly.* The residual `‖Y_R − P_{Ω¹}(Y_R)‖/‖Y_R‖ = 1.000000 EXACT` (S114 W3-1, all three triality classes) is the numerical shadow. To reach the generation leg you must ENLARGE the algebra by the crossed product `A_K ⋊ SU(3)_R` ≡ the Kasparov external product — i.e. **admit an external coupling**. Reality `[J, D_K + ε_LX] = 0` (BDI, `J² = +1`) keeps `ε_LX` admissible and order-one is SILENT on the generation texture (index-disjointness — `A_K` acts as identity on the multiplicity index, Connes 2006 §5.2), so the substrate *permits* `ε_LX` but the axioms fix NONE of its values. This is the §VII.BL reframe verbatim: the hierarchy "is necessarily a threshold/transit/localization effect — NOT a tree number," "OUTSIDE every `A_K`-module."

#### 3. The two symmetric attractors — the 2.9× vs 3124× crux

What the substrate DOES force, it forces by symmetry. The right-regular Z₃ circulant `C = c₀I + c₁P + c₂P²` is diagonalized by the DFT `F₃` *for ANY couplings* `c_a` (coefficient-INDEPENDENT, S115):

> **(4)**  `U_R = F₃`,  `|U_{R,ij}|² = 1/3` (tri-maximal),  `J = 1/(6√3) = 0.0962250`.

The two fibers land on the two Z₃-symmetric fixed points of the multiplicity-scalar structure:

> **(5a)**  Quark, `M₃(ℂ)`-shared chiralities → TWO circulants → `U_mix = F₃†F₃ = 1` → `J = 0` (identity attractor; `‖U_mix − 1‖_F = 5.2e-16`).
> **(5b)**  Lepton, `ℂ⊕ℍ` asymmetric → coset-diagonal `U_L` → `U_mix = U_L†F₃` → tri-maximal, `J = 0.0962` (DFT attractor).

**Neither is in band.** And the lepton attractor is LOCKED there: a coset-diagonal `U_L = diag(e^{iα_k})` left-multiplies each row of `U_R` by a pure phase, and the Jarlskog quartet `U₀₀U₁₁Ū₀₁Ū₁₀` carries each generation index once unconjugated and once conjugated, so the row phases cancel EXACTLY:

> **(6)**  `J(U_L† U_R) = J(U_R) = 1/(6√3)`  ∀ `α`   (`J_scan_spread = 8.3e-17`, machine-exact).

So the ℂ⊕ℍ sector-asymmetry, *even though it is structurally present*, is **J-inert**: it buys a coset-diagonal `U_L`, and a coset-diagonal `U_L` cannot move `J` off the maximal value by a single part in 10¹⁶.

Now the crux. The substrate is generation-blind, so it can only produce Z₃-symmetric mixing — the DFT eigenbasis (5b) or its degenerate collapse (5a). The residuals are simply the distance from these symmetric attractors to the data:

- Observed CKM `J = 3.08e-5` is **tiny** (small mixing) ⇒ the tri-maximal attractor overshoots by `3124×`, and the actual identity attractor undershoots to `0`. BOTH symmetric limits badly miss.
- Observed PMNS `J = 0.0329` is **large** (near-maximal mixing) ⇒ the tri-maximal attractor sits only `2.92×` away.

The `2.9×`-vs-`3124×` gap is *entirely* explained by WHERE the data sits relative to the symmetric fixed points — small-mixing CKM is far from a symmetric attractor, large-mixing PMNS is near one. **It is not evidence that leptons carry a derivation handle quarks lack.** The "RESONANT-CONDITIONAL ~2.9×" tag is the substrate landing on a symmetric attractor that the near-maximal PMNS happens to be close to in the single coarse Jarlskog number.

And the "closeness" is a J-only artifact. The forced tri-maximal texture has `|U_e3|² = 1/3 = 0.3333`, while observed `sin²θ₁₃ = 0.02203` (NuFIT 5.2 NO, the S115 anchor) — a **15.1× overshoot on θ₁₃** hidden underneath the 2.9× J-ratio. The substrate-forced symmetric texture is NOT close to PMNS in detail; it matches `sin²θ₁₂ ≈ 1/3` by luck and fails `θ₁₃` by an order of magnitude. The single-number 2.9× is the precisely the kind of buried-choice near-miss that must not be headlined as a positive.

#### Sub-(a) — ℂ⊕ℍ sector-asymmetry: §VII.BL-blind FIBER-charge, not a generation DOF

The ℂ⊕ℍ vs M₃(ℂ) distinction lives on the SM-rep fiber `ℂ¹⁶` of (1) — it labels WHICH of the 16 SM fermions (lepton doublet/singlet vs colour triplet), i.e. WHICH 16-dim rep. The generation index lives on the *orthogonal* multiplicity leg `ℂ^{m(p,q)}`. These are different tensor legs. This is exactly the §VII.CK D3 **LABELING-B vs LABELING-A** distinction: every `A_K`-built cocycle "distinguishes SECTORS (LABELING-B, registry-foreclosed) but NOT the `t`-generations (LABELING-A, the operative index)." The sector-asymmetry is a LABELING-B (fiber) feature — the very thing §VII.CK proves is foreclosed as a generation handle.

The proof that this blindness is the SAME one that HELD the quarks: in S111 the up↔down fiber-charge distinction (both in `M₃(ℂ)`) supplied NOT a per-generation texture but a single overall scale `Λ_d/Λ_u = 0.02523`. A fiber-charge difference buys an overall coupling/scale, never the per-generation circulant-breaking texture. By identical structure the ℂ⊕ℍ-vs-neutrino fiber difference can supply at most an overall lepton coupling `g_R` — and (6) proves the only thing it actually contributes to the mixing (a coset-diagonal `U_L`) is J-inert. **Verdict: §VII.BL-blind fiber-charge.**

#### Sub-(b) — admitting `ε_LX` is external-as-a-coupling, NOT a derivation

§VII.CK D4 already tags the only surviving corridor `CLOSED-EXTERNAL-AS-A-COUPLING`: the crossed product `A_K ⋊ SU(3)_R` "holds only an overall coupling `g_R` with the texture/phase FORCED around it." The ONE structurally-forced thing — the Z₃-circulant texture (4) — is what WASHED OUT (S115 FAIL). Everything beyond it is fitted: S111's `{ρ₁₃ᵈ = 0.595, ρ₂₃ᵈ = 0.181, |w₁₂ᵈ| = 0.0238, θ_d = 1.18}` are four external parameters per sector plus a scale, reality-compatible and order-one-admissible but *value-unfixed by the axioms*; slot-5 `m_s/m_d` is logged honestly as "a DIRECT FIT TARGET not a prediction." This is the standard-Connes situation: Connes 2006 §4.1 makes the Yukawas FREE finite-geometry parameters; the framework's `D_K ≡ D_F` promotion PROMISED to derive them from SU(3)-spectral data, and §VII.BL is the THEOREM that the promotion FAILS for the texture. **The decisive parity: the epistemic status of `ε_LX` is a property of the MACHINERY (a non-LI multiplicity-bundle deformation outside `Ω¹_{D_K}(A_K)`), not of which fiber it is applied to.** The registry already reads the quark `ε_LX` as external (quark-CKM FALSIFIED, the one pure prediction `V_us` FAILED). The identical machinery cannot be a "fit" for quarks and a "derivation" for leptons. **Verdict: external coupling.**

#### Sub-(c) — the lepton texture SHARES the quark mass-vs-mixing tension (and the "relief" is more external input)

S111's tension is structural: "the texture magnitudes (`ρ·|w| ~ 0.02`) needed to break the mass log-gap locks are LARGER than the gen1/gen2 light-eigenvalue diagonal gap ⇒ overpredict the Cabibbo 1-2 rotation by 38%. Masses fit ⇒ mixing overshoots." The SAME off-diagonal `ε_LX` entries that de-degenerate the masses (breaking the Casimir lock `ln(m_s/m_d)/ln(m_b/m_s) = 9/5`) ALSO generate the rotation — they are the same matrix elements, not independently dialable.

The lepton sector inherits this *with the overshoot in the same direction*. The bare circulant already overshoots `J` by 2.9× (5b). By (6), pulling `J` DOWN into band requires a NON-coset-diagonal `U_eL` — i.e. an off-diagonal-in-generation charged-lepton `ε_LX`. But an off-diagonal charged-lepton `ε_LX` generates BOTH the charged-lepton mass splittings AND the `U_eL` rotation that enters `PMNS = U_eL† U_ν` — coupled exactly as in the quark case. Fitting `m_e : m_μ : m_τ` (a ~3477× span) thus pins `U_eL`, which generically does NOT land `J` in band. The neutrino side will claim the ℂ⊕ℍ asymmetry DECOUPLES mass-fitting from mixing — but decoupling is purchased by giving the charged-lepton and neutrino sectors SEPARATE `ε_LX`'s (more external parameters), which is the S111 forward question verbatim ("does a SEPARATE `ε_LX` sector ... bring `V_us` into band"). Adding free parameters to relieve a tension is the OPPOSITE of a derivation. **Verdict: shared (overshoot); any relief strengthens the external-coupling reading.**

#### Questions for neutrino-detection-specialist (answer in Turn B)

**Q1 (name the operator).** By (6), the ℂ⊕ℍ asymmetry can break tri-maximality only through a non-coset-diagonal `U_eL`, i.e. an off-diagonal-in-generation charged-lepton `ε_LX` on the multiplicity leg — the SAME deformation §VII.BL proves is outside every `A_K`-module. Name a single operator that is INTERNAL (inside `Ω¹_{D_K}(A_K)`, or otherwise `A_K`-derivable) for the lepton sector but EXTERNAL for the quark sector. If you cannot, in what sense is the lepton handle structurally different from the quark handle rather than the identical external coupling applied to a different fiber?

**Q2 (fix θ₁₃, not just J).** The forced tri-maximal texture overshoots `sin²θ₁₃` by 15× (`1/3` vs `0.02203`) while sitting 2.9× from `J_obs`. Demonstrate that the ℂ⊕ℍ asymmetry lands `θ₁₃` AND `θ₁₂` AND `J` in band *simultaneously* using NO more free parameters than the quark sector's `{ρ, |w|, θ, Λ}`. If it requires more parameters, distinguish that from the standard free-Yukawa fit (Connes 2006 §4.1).

**Q3 (escape the coupling).** For quarks, `V_us` overshoots 0.225 by 38% because the mass-gap-breaking texture and the Cabibbo rotation are the same off-diagonal entries. The bare lepton circulant already overshoots `J` by 2.9× in the same direction. Show that the charged-lepton mass texture required to fit `m_e:m_μ:m_τ` does NOT inherit the identical mass-vs-mixing coupling — and if your decoupling relies on a separate neutrino `ε_LX`, justify why that is not simply additional external input (which would confirm, not refute, the WALLED reading).

### R1 · neutrino-detection-specialist — ε_LX-RESCUABLE steelman

**Thesis.** The lepton shape-leg is ε_LX-RESCUABLE — not because the bare `D_K` carries a generation handle (it does not; I grant §VII.BL in full), but because the S115 wash-out is a property of the **coset-diagonal ansatz** imposed on the internal forced circulant, NOT a J-inertness theorem for the external `ε_LX` on the asymmetric sector. The single number connes's §3 leans on, `J_scan_spread = 8.3e-17`, was produced by scanning 25 coset-**diagonal** phase matrices `U_L = diag(e^{iα_k})` (`s115_lepton_pmns_forced_texture.py` lines 252–262). By rephasing invariance `J` is flat across diagonal phases *by a textbook identity*, so that scan verifies rephasing invariance and probes **nothing** about the off-diagonal `U_eL` that the asymmetric `ε_LX` actually produces. Connes's own eq (6) restricts to coset-diagonal `U_L`; connes's own Q1 *concedes* the operative move is a non-coset-diagonal `U_eL`. The 2.9× is the symmetric **starting point** of a deformation the framework's own S96 compute already showed **moves** — not a wall. And the `ℂ⊕ℍ` asymmetry the `M₃(ℂ)`-shared quark sector lacks is a genuine substrate DOF with a concrete physical name: the charged leptons are **Dirac** (in `ℂ⊕ℍ`) while the neutrinos are **Majorana** (seesaw, `M_R` supplied by the B-branch `D_K` fold energies — no free scale). That asymmetry removes exactly the alignment constraint that collapses connes's quark negative control to `U_mix = F₃†F₃ = 1`.

#### 1. What I grant (homogeneity wall, bare wash-out, θ₁₃ overshoot)

I concede connes's §1 **homogeneity wall in full and without reservation**, and this costs the rescuable side nothing:

- The bare `D_K` is multiplicity-scalar, generation-blind, sector-blind. §VII.BL is STAGE-3-PERMANENT; I do not contest it. The generation texture is **not** in the bare spectrum. The generation index is the `Z₃`-triality `t = (p−q) mod 3` on the multiplicity leg, and `D_K = ⊕ D_{(p,q)} ⊗ 1_{m(p,q)}` is `⊗1` there. Agreed, verbatim.
- The forced `A_K⋊SU(3)_R` right-regular circulant lands on the tri-maximal DFT attractor (`|U_ij|² = 1/3`, `J = 1/(6√3) = 0.0962250` Sage-exact `= √3/18`) and washes out under a coset-diagonal `U_L`. `dev = 1.924773`, FAIL. Agreed.
- In the **exact** tri-maximal symmetric limit, `sin²θ₁₃ = 1/3 = 0.3333` overshoots the measured `0.02203` (NuFIT 5.2 NO, the S115 anchor) by **15.13×** (Sage-exact `(1/3)/0.02203`). The bare symmetric attractor is **not** the observed PMNS in detail — `θ₁₃` is the *smallest* PMNS angle, nowhere near maximal. Granted, and it is connes's strongest single number.

Every one of these three concessions is a statement about (i) the **bare spectrum** or (ii) the **symmetric attractor**. None is a statement about the deformed `ε_LX`. The rescue lives in the deformation *away* from the attractor — precisely the object S115 never tested.

#### 2. The J-inert claim is an artifact of the coset-diagonal ansatz — DEMONSTRATED

This is my decisive disagreement with connes's §3. His eq (6) is correct as a *restricted* statement: a coset-diagonal `U_L = diag(e^{iα_k})` left-multiplies each row of `U_R` by a pure phase, the moduli `|U_mix,ij| = |U_R,ij|` are unchanged, and `J` cancels by the rephasing identity. But that is the **entire** content of `J_scan_spread = 8.3e-17`. The S115 scan (lines 252–262) draws 25 random **diagonal** phase vectors and confirms a rephasing identity. It is structurally incapable of moving `J`, because it never applies an off-diagonal `U_eL`.

Substitution chain (the moduli, not just the phases):

```
Claim: J is inert under coset-diagonal U_L ONLY; a non-coset-diagonal (off-diagonal-in-generation)
       U_eL — the actual ε_LX deformation — moves J off 1/(6√3).
Step 1 (def):   U_mix = U_eL† U_R ,  U_R = F₃ tri-maximal,  |U_R,ij|² = 1/3.        [s115 lines 229–245]
Step 2 (coset-diag): U_L = diag(e^{iα_k}) ⟹ (U_L† U_R)_{ij} = e^{−iα_i}(U_R)_{ij}
                ⟹ |U_mix,ij| = |U_R,ij| UNCHANGED ⟹ J invariant.                    [s115 J_scan; rephasing identity]
Step 3 (off-diag):   U_eL with ≥1 off-diagonal entry ⟹ (U_eL† U_R)_{ij} = Σ_k (U_eL†)_{ik}(U_R)_{kj}
                is a SUM of ≥2 tri-maximal entries with relative phases
                ⟹ |U_mix,ij| ≠ 1/3 generically ⟹ J moves.
Conclusion:     S115 tested only Step-2 configurations. The "wash-out" is a Step-2 property,
                NOT a property of ε_LX.
```

I verified Step 3 by **direct Sage computation** (one real 1-2 generation rotation `U_eL = R₁₂(b)`, the simplest off-diagonal deformation):

| `U_eL` | `J(U_eL† F₃)` | `|U_mix,00|²` |
|:-------|:--------------|:--------------|
| identity (bare) | `0.0962250` | `0.3333` |
| coset-diag `diag(e^{iα})`, ∀α | `0.0962250` (flat, machine ε) | `0.3333` |
| `R₁₂(b=0.2)` | `0.08863` | `0.2035` |
| `R₁₂(b=0.5)` | `0.05199` | `0.0528` |
| `R₁₂(b=0.9)` | `−0.02186` | `0.0087` |

A **single** off-diagonal parameter sweeps `J` straight through the observed band `[0.0086, 0.0331]` — `J_obs = 0.0329` lands between `b = 0.5` and `b = 0.9`, and the moduli depart tri-maximal in lockstep. So `J` is **not** inert under the asymmetric `ε_LX`; it is inert only under the coset-diagonal `U_L` that S115 happened to scan. The "machine-exact lock" is the lock of the *symmetric endpoint*, exhibited and then mistaken for the whole orbit.

And the framework's **own** compute already demonstrated the motion. `S96-MATTER-PMNS-3X3` (INFO, audit `29d70247…`) turned on a KK-modified **non-left-invariant** `L_X` — the same external non-LI class as `ε_LX` — on the lepton sector and found the B2 Schur wall **LIFTS**: `sin²θ₁₂` and `sin²θ₂₃` open **monotonically from exactly 0**, with the Jensen side-condition `‖[iK₇, M_lep]‖ = 0` preserved at *every* scan point (`ε_LX ∈ [0, 0.10]`, step 0.005). At `ε_LX = 0.05`: `sin²θ₁₂ = 0.7908`, `sin²θ₂₃ = 0.3322`, `sin²θ₁₃ = 0.0330`. The angles **move under the external handle**. That is the live contradiction with connes's "J-inert" reading: S115's coset-diagonal scan finds inertness because it is a diagonal scan; S96's off-diagonal `L_X` finds motion because it is the off-diagonal deformation. Same external class, opposite verdict — because the wash-out is a property of the *symmetric configuration*, not of `ε_LX`.

**Honest residual (I flag it, per my discipline):** S96 also found that *no single* `ε_LX` lands all four NuFIT bands simultaneously, and that `R = Δm²₃₂/Δm²₂₁` is the binding shortfall (peak `R = 6.87` vs NuFIT floor `[17, 66]`). So I am **not** claiming the rescue is closed. I am claiming the *angles* are a live, moving, side-condition-respecting derivation corridor — and the open question is `R` and simultaneity, **not** a wall on the mixing. The W2-3 compute is the discriminator, and it tests a deformation, not the symmetric endpoint S115 already foreclosed.

#### 3. The ℂ⊕ℍ asymmetry is a genuine substrate DOF: Dirac-charged / Majorana-neutrino

Engaging the **commutant wall** (connes §2): I grant that the generation handle lives in the commutant of `A_K`'s left-action and that reaching it requires a non-LI `ε_LX` **outside** `Ω¹_{D_K}(A_K)`. "External to `A_K`'s differential calculus" — granted in the precise NCG sense. But "external to `Ω¹_{D_K}(A_K)`" is **not** the same as "a free fit." S96's `L_X` is outside `Ω¹` *and* constrained (the `q₇`-neutral side-condition holds at every point). External-in-the-NCG-sense ≠ value-unconstrained.

The substantive asymmetry quarks lack is not a generation index on `ℂ⊕ℍ` (connes is right that the bare `D_K` is blind to the fiber label). It is the **reality structure**: the `ℂ⊕ℍ` charged-lepton sector is **Dirac**, while the neutrino sector is **Majorana** — the framework's seesaw, with the heavy scale `M_R` supplied by the B-branch `D_K` fold energies (not a free seesaw scale), the Majorana texture forced by KO-dim-6 `J`-self-conjugacy, `δ_CP ∈ {0, π}` `J`-forced, and the Dirac normalization oscillation-anchored. Normal ordering itself is read off the B-branch eigenvalue crossing at `τ = 0.107`. **None of this exists in the quark sector**, where up and down are both Dirac in a *shared* `M₃(ℂ)` leg. That shared leg is exactly the structure that drives connes's negative control to identity: both quark chiralities get the **same** forced eigenbasis `F₃`, so `U_mix = F₃†F₃ = 1` (`‖U_mix − I‖_F = 5.2e-16`). The `ℂ⊕ℍ` split removes the shared-leg alignment, so `U_eL` (charged, Dirac) and `U_ν` (seesaw, Majorana) are **not** forced onto a common eigenbasis. The asymmetry is a genuine, computed, substrate reality-structure difference — and it is precisely the feature the quark negative control demonstrates the quarks do not have.

#### 4. The two attractors select the right structure per sector; bare numbers are starting points

Connes's §3 says the `2.9×`-vs-`3124×` gap is "entirely explained by where the data sits relative to the symmetric fixed points." I agree with the *arithmetic* and read it the opposite way. The quark `M₃(ℂ)`-shared structure selects the **identity** attractor (`J = 0`, small mixing) — and CKM **is** small (`J = 3.08e-5`). The lepton `ℂ⊕ℍ`-asymmetric structure selects the **DFT** attractor (tri-maximal, large mixing) — and PMNS **is** large (`J = 0.0329`, near-maximal `θ₂₃`, large `θ₁₂`). One mechanism — which attractor each sector's leg-structure selects — gets the **qualitative** structure of *both* mixing matrices right: quark mixing small and hierarchical, lepton mixing large and near-anarchic. That is the single most striking flavor fact, and the substrate reproduces it from leg-structure alone. Connes calls this a coincidence of "where the data lands"; I call it the substrate selecting the correct attractor per sector.

And the bare numbers are **starting points, not walls** — the quark precedent proves it. Connes tags quark-CKM "FALSIFIED ~3124×," but that `3124×` is the *bare, undeformed* tri-maximal vs CKM. `S111-CF-YUK-FULLFLAVOR` (PASS) **deformed** it: with a down-sector texture `{ρ₁₃ᵈ=0.5955, ρ₂₃ᵈ=0.1814, |w₁₂ᵈ|=0.0238, θ_d=1.18}` it landed `mass_grp = 5/6` (five mass observables derived from one scale `Λ_d/Λ_u = 0.02523`), with **only** the one pure-mixing prediction `V_us = 0.3107` overshooting (38% high). A bare `3124×` deformed to a 5/6 derivation. The lepton bare number is `2.9×` — three orders of magnitude closer to begin with — and the deformation machinery (S52/S96) has *already* matched `sin²θ₁₃` (S52: `→ 0.02225` at C²-split 0.0918) and lifted `θ₁₂/θ₂₃` from zero. Comparing the lepton **bare** `2.9×` to the quark **bare** `3124×` and calling both "walls" ignores that the quark bare number was not the final word.

#### Sub-(a) — ℂ⊕ℍ sector-asymmetry: genuine substrate DOF (via reality-structure, not fiber-label)

**Genuine substrate DOF.** Connes is correct that `ℂ⊕ℍ` vs `M₃(ℂ)` is a LABELING-B fiber-charge and that the bare `D_K` is blind to it *as a generation index*. But the asymmetry's physical content is the **Dirac/Majorana reality-structure split** (`ℂ⊕ℍ` charged sector Dirac; neutrino sector Majorana via KO-dim-6 `J`-self-conjugacy), which is a genuine, derived substrate feature — it is *why* the framework predicts Majorana neutrinos and Dirac charged leptons, with `M_R` spectrum-supplied. It changes the boundary conditions on `ε_LX` (the seesaw inverts the texture; `M_R` is pinned by the spectrum) and it removes the shared-leg alignment that collapses the quark negative control to identity. It is not a generation index on the fiber (connes right); it is a substrate reality-structure DOF the quark sector structurally lacks.

#### Sub-(b) — admitting ε_LX: external-in-the-NCG-sense, but a constrained substrate deformation, closer to derivation than to a free fit

The dichotomy "derivation vs external-as-a-coupling" is a false binary; the operative axis is **free vs constrained**. I grant `ε_LX` is outside `Ω¹_{D_K}(A_K)` (the NCG "external" sense). But the lepton `ε_LX` is *more* constrained than the quark `ε_LX`: the Majorana scale `M_R` is supplied by the B-branch fold energies (not free), `δ_CP ∈ {0, π}` is forced, `Σm_ν` is oscillation-anchored, and the S96 `L_X` carries `q₇`-neutrality as a hard side-condition. The quark `ε_LX` carries 4 free texture parameters per sector `{ρ, |w|, θ, Λ}`. So admitting the lepton `ε_LX` is admitting a *more*-constrained deformation than the quark one the registry already reads as a partial derivation (5/6). Verdict: external-in-the-NCG-sense, but a constrained substrate deformation — closer to derivation than connes's "external coupling" tag allows.

#### Sub-(c) — mass-vs-mixing tension: RELIEVED structurally (Dirac/Majorana split), not by extra free parameters

The quark `V_us` overshoots 38% because `U_CKM = U_uL† U_dL` with **both** textures Dirac in `M₃(ℂ)` — the same off-diagonals that break the mass log-gap also rotate. The lepton sector breaks this coupling **structurally**: `PMNS = U_eL† U_ν`, where `U_eL` is the Dirac charged-lepton diagonalization (it does the `m_e:m_μ:m_τ` mass-fitting, a 3477× span) but `U_ν` is the **seesaw** diagonalization of the Majorana matrix (it does the large mixing), and the seesaw **inverts** the texture (light masses `∝ M_D²/M_R`). The large PMNS angles are dominated by the `M_R` texture — spectrum-supplied — not by the charged-lepton Dirac off-diagonals. So fitting the charged-lepton masses pins `U_eL` but leaves the large angles to `U_ν`, a *separately and more tightly* constrained object — **not** an additional free `ε_LX`. The relief is the Dirac/Majorana split, which is spectrum-constrained, not a parameter you dial. Verdict: RELIEVED, and the relief tightens rather than loosens the parameter budget.

#### Answers to connes's Q1 / Q2 / Q3

**A1 (the operator → it's a constraint, and your negative control exhibits it).** I concede the narrow point: there is **no** operator inside `Ω¹_{D_K}(A_K)` for leptons that is outside it for quarks — the differential calculus is sector-uniform, and *both* textures are external to it (§VII.BL). The structural difference is not an operator but a **constraint**: the `M₃(ℂ)`-shared-chirality **alignment** that *your own* negative control exhibits as `U_mix^quark = F₃†F₃ = 1`. That constraint forces the two quark diagonalizations onto a shared eigenbasis (collapsing the misalignment to identity); the `ℂ⊕ℍ` split removes it. The lepton handle is the same external operator *class* acting under **fewer alignment constraints** — and "fewer alignment constraints on a constrained deformation" is exactly the room the quark sector lacks. The negative control you cite as proof of sector-blindness is the proof that the collapse mechanism is shared-leg-specific.

**A2 (I do not claim simultaneous landing today — and your parameter count is inverted).** I will not over-claim: S96 found no single `ε_LX` lands all four NuFIT bands at once (`R` is the binding shortfall). But the parameter-count framing inverts the situation. The lepton sector has **fewer** free parameters than the quark sector, because `M_R` is supplied by the B-branch `D_K` fold energies (not free), `δ_CP ∈ {0,π}` is forced, and `Σm_ν` is oscillation-anchored. The quark sector carries 4 free texture parameters per sector; the lepton seesaw replaces the neutrino-side free scale with a spectrum-pin. The honest comparison is: *can the more-constrained lepton `ε_LX` land the angles?* — and S52 already lands `θ₁₃` (`→ 0.02225` at C²-split 0.0918) while S96 lifts `θ₁₂/θ₂₃` from zero. That is the W2-3 question, pre-registered; the open shortfall is `R`, not the angles.

**A3 (the Dirac/Majorana split breaks the coupling — without adding parameters).** Per sub-(c): the quark coupling (mass-gap-breaker = rotation) holds because both quark diagonalizations are Dirac in `M₃(ℂ)`. The lepton `PMNS = U_eL† U_ν` splits the two jobs across a **Dirac** `U_eL` (masses) and a **Majorana seesaw** `U_ν` (mixing), with the seesaw inverting the texture and `M_R` spectrum-pinned. The decoupling is the reality-structure split, which is *more*-constrained than the quark texture, not an additional free `ε_LX`. So the relief confirms the **rescuable**, not the WALLED, reading: it is a substrate constraint quarks lack, not a parameter we add.

#### Questions for connes (answer in Round 2)

**Q1 → (does the wall force `U_eL` and `U_ν` onto a shared eigenbasis?).** Your negative control gives `U_mix^quark = F₃†F₃ = 1` EXACTLY *because* both quark chiralities share the `M₃(ℂ)` leg and thus the same forced eigenbasis. Does your homogeneity/commutant wall predict that the lepton `U_eL` (Dirac, `ℂ⊕ℍ`) and `U_ν` (Majorana seesaw) are likewise forced onto a **shared** eigenbasis? If **no**, the misalignment `U_eL† U_ν` is unconstrained by the wall and the wall is silent on whether it lands in band. If **yes**, name the operator that aligns a Dirac charged sector and a Majorana seesaw across the `ℂ`/`ℍ` summand boundary.

**Q2 → (what computed object shows the *off-diagonal* `U_eL` leaves `J` at 0.0962?).** `J_scan_spread = 8.3e-17` scans coset-diagonal `U_L` only, and you concede the operative move is a non-coset-diagonal `U_eL`. My Sage table (and S96's monotonic lift) show a single off-diagonal rotation sweeps `J` through the band. What computed object shows that the **actual** off-diagonal `ε_LX` deformation holds `J` at `1/(6√3)`? If none exists, on what basis is `2.9×` a "wall" rather than the symmetric start of a deformation S96 already moved?

**Q3 → (how is a spectrum-supplied `M_R` "additional external input"?).** You read any lepton decoupling as "more parameters ⇒ more external ⇒ confirms WALLED." But `M_R` is supplied by the B-branch `D_K` fold energies, the Majorana texture is `J`-self-conjugacy-forced, and `δ_CP ∈ {0,π}` is forced — **fewer** free parameters than a generic Dirac sector, not more. How is a spectrum-pinned Majorana scale "additional external input" rather than a substrate-derived constraint the quark sector structurally lacks?

---

## Round 2 — Rebuttal (engage the opponent's strongest case)

### R2 · connes-ncg-theorist

#### CONVERGENCE — where you now grant the neutrino side

I grant the decisive point of your §2, and it forces a correction to my R1 §3.

**The "J-inert" claim was over-stated.** My R1 §3 leaned on `J_scan_spread = 8.3e-17` as if it were a wash-out *theorem* for the lepton mixing. It is not. It is a **coset-diagonal-subspace identity**. The S115 scan (`s115_lepton_pmns_forced_texture.py` lines 252–262) draws 25 *diagonal* phase vectors `U_L = diag(e^{iα_k})` and confirms the rephasing identity — my eq (6) is correct exactly as far as it reaches, and no further. It probes a 3-real-parameter coset-diagonal slice of the 8-parameter `U(3)` and is structurally incapable of moving `J`, because it never applies a transverse (off-diagonal) `U_eL`. Your substitution-chain Step 3 is right: a non-coset-diagonal `U_eL` forms `(U_eL† U_R)_{ij} = Σ_k (U_eL†)_{ik}(U_R)_{kj}`, a sum of ≥2 tri-maximal entries with relative phases, so `|U_mix,ij| ≠ 1/3` generically and `J` moves. Your one-parameter Sage table (`R₁₂(b)` sweeping `J` from 0.0962 through 0.0520 to −0.0219, crossing the observed band between `b = 0.5` and `b = 0.9`) is a clean demonstration. And `S96-MATTER-PMNS-3X3` independently exhibits the motion on the *physical* lepton sector: under the non-LI `L_X`, `sin²θ₁₂`/`sin²θ₂₃` open monotonically from exactly 0 with `‖[iK₇, M_lep]‖ = 0` preserved at every scan point.

So I withdraw "the 2.9× IS the wall measured in the J-ratio." The bare tri-maximal point is the **symmetric starting point of a deformation that demonstrably moves**, not a wall on `J`. Your **Q2** asks what computed object shows the off-diagonal `U_eL` holds `J` at `1/(6√3)`: **none exists, and I do not claim one.** The forced circulant is J-mobile under the off-diagonal deformation; the machine-exact lock is the lock of the *symmetric endpoint*, and I mistook it for the whole orbit.

**Two further grants.** (i) Your §3 reframe of the ℂ⊕ℍ asymmetry as the **Dirac/Majorana reality-structure split** — not merely the fiber label — is a genuine substrate feature: the charged sector is Dirac, the neutrino sector Majorana via KO-dim-6 `J`-self-conjugacy, and that is real, derived content the `M₃(ℂ)`-shared quark sector lacks. (ii) Your §3 distinction "external-to-`Ω¹_{D_K}(A_K)` ≠ value-unconstrained" is correct: the `S96` `L_X` is outside `Ω¹` *and* carries the `q₇`-neutral side-condition at every point. External-in-the-NCG-sense does not, by itself, mean free.

These grants cost the WALLED reading nothing — because none of them is a claim that the substrate *supplies* the off-diagonal. They establish that the off-diagonal **exists and moves `J`**. Whether it is **substrate-derived** or **external** is the question my DISSENT now re-aims at, on ground that no longer depends on J-inertness at all.

#### DISSENT — where you hold, with NEW argument (don't restate R1)

Grant in full that the off-diagonal `U_eL` moves `J`. The wall does not live in the *mobility* of the orbit; it lives in **what pins the point on it**.

**1. The off-diagonal is not a free dial — it is pinned by the charged-lepton mass-fitting, and the quark sector already computed where the pinned point lands: 38% past the band.**

Your §2 Sage table treats `b` (the `R₁₂` angle) as a free parameter and sweeps it until `J` lands in band. But `b` is **not free**. It is the *same* matrix element that diagonalizes the charged-lepton masses. The lepton PMNS is `PMNS = U_eL† U_ν`, and `U_eL` is the unitary that diagonalizes `M_e = M_diag(charged-lepton log-gap) + ε_LX^e_offdiag`. The off-diagonal entries of `ε_LX^e` are fixed by requiring the eigenvalues of `M_e` to reproduce `m_e : m_μ : m_τ` — a span of 3477× whose diagonal log-spacing ratio `ln(m_μ/m_e)/ln(m_τ/m_μ) = 1.89` is the lepton analog of the down-quark `9/5 = 1.80` Casimir lock (and the same 1.89 my S99 Connes-distance candidate targets). Once those off-diagonals are pinned by the masses, `U_eL`'s rotation angle is **determined**, not dialable.

This is exactly the quark structure, and the quark sector already supplied the computed answer. Substitution chain, grounded entirely in S111 computed numbers (`s111_gate_verdicts.txt` lines 71–73):

```
Step 1:  V_CKM = U_uL† U_dL                                          [S99, computed]
Step 2:  U_dL diagonalizes M_d = diag(9/5 Casimir log-gap) + ε_LX^d_offdiag;
         the off-diagonals {ρ13^d=0.595, ρ23^d=0.181, |w12^d|=0.0238}
         are PINNED by fitting m_d:m_s:m_b (9/5 → PDG 0.787).        [S111 lines 71–72]
Step 3:  The SAME pinned off-diagonals set U_dL's rotation:
         |V_us| = |(U_uL† U_dL)_12| = 0.3107.                        [S111 line 73]
Step 4:  0.3107 / 0.225 = 1.38 > 1  ⇒  OVERSHOOT by 38%.            [S111 slot-6 FAIL]
Concl.:  Mass-fitting FORCES off-diagonals LARGER than the mixing needs;
         the mass-pinned point on the J-orbit lands PAST the band.
```

The lepton sector inherits the identical `PMNS = U_eL† U_ν` structure with `U_eL` carrying the mass-fitting. Your demonstration that *some* `b` lands `J` in band proves the orbit *passes through* the band; it does **not** show the **mass-pinned** `b` lands there. The rescue-vs-wall fork is precisely whether the charged-lepton-mass-fixed `U_eL` lands PMNS in band or over-rotates like `V_us`. That is **untested**: S115 tested the symmetric endpoint (washed out); S96 tested a *free* `L_X` scan (angles move, but no single point lands all four bands — `R = Δm²₃₂/Δm²₂₁` peak 6.87 ≪ NuFIT floor [17, 66]); your own S52 lands `θ₁₃` *individually*. None tested the mass-pinned point. The S96 honest residual — angles move but **never simultaneously land** — is the leading indicator that the lepton sector sits on the same coupled mass-vs-mixing surface the quark sector overshot.

**Answer to your Q1 (shared eigenbasis?).** No — I grant the wall does *not* force `U_eL` and `U_ν` onto a shared eigenbasis; the ℂ⊕ℍ split genuinely removes the `M₃(ℂ)`-shared-leg alignment that collapses my quark negative control to `F₃†F₃ = 1` (`5.2e-16`). But your own statement of the consequence is my point: "the wall is silent on whether `U_eL† U_ν` lands in band." **Wall-silence is externality, not derivation.** The misalignment is unconstrained by the axioms *because the texture lives in the external `ε_LX` the axioms do not fix* — the very reason the quark misalignment is unconstrained. "The wall does not forbid it" is not "the substrate produces it."

**2. sub-(a): the Dirac/Majorana split is a genuine substrate DOF — but it is a MASS-SPECTRUM DOF, §VII.BL-blind as a GENERATION-MIXING handle. The spectrum-pinned `M_R` you invoke makes this exact.**

I grant the split is real (CONVERGENCE). The NEW point is *which channel* it acts in. The reality structure `J` acts on the SM-rep fiber `ℂ¹⁶` (KO-dim-6 particle↔antiparticle conjugation); the Dirac/Majorana distinction is *whether* the fiber carries a Majorana mass term `M_R` — a **fiber-charge** property of which 16-dim rep, on the orthogonal tensor leg from the generation index. Via seesaw it rewrites the *mass spectrum* (`m_ν = M_D^T M_R⁻¹ M_D`, light masses ∝ `M_D²/M_R`): a magnitude/ordering effect — the **mass channel**.

Now your **Q3**, sharpened to its breaking point. You ground the rescue in `M_R` being **spectrum-supplied** (B-branch `D_K` fold energies, not free). But a spectrum-supplied `M_R` is **multiplicity-scalar by §VII.BL** — the bare-`D_K` fold energies are generation-diagonal (homogeneity forces `⊗1` on the leg; reality forces `t=1≡t=2`), so `M_R = diag(M_0, M_1, M_1)`. A **diagonal** `M_R` in the seesaw contributes **zero generation mixing** — all of `U_ν`'s mixing then comes from the off-diagonal of `M_D`, which is again the external `ε_LX`. The dichotomy is exhaustive and closes the rescue's load-bearing claim:

- If `M_R` is *truly* spectrum-pinned ⇒ it is generation-diagonal ⇒ it supplies **no PMNS mixing**. The large angles ride entirely on off-diagonal `M_D = ε_LX^ν` (external). Crediting the rescue to the spectrum-pinned `M_R` is misattribution.
- If `M_R` is given off-diagonal generation structure to *source* the mixing ⇒ it is **not** purely spectrum-pinned ⇒ it carries an external `ε_LX^{M_R}` — *additional* external input, exactly the WALLED reading.

Either way the large PMNS mixing is external off-diagonal `ε_LX`. "Spectrum-pinned `M_R`, fewer parameters" is true and *irrelevant to the mixing handle*: it constrains the mass channel, not the generation-mixing channel. Your **A1** already conceded there is no operator internal-for-leptons-but-external-for-quarks; *this is why* — the mixing handle is the same external off-diagonal `M_D` in both sectors, and the Dirac/Majorana split only re-routes the *mass magnitude* through the seesaw.

**3. sub-(b): admitting `ε_LX` is external-as-a-coupling — and this session's `W2-1` just re-confirmed it on the only surviving corridor.**

The freshest entry in the framework's own register settles the epistemic status against the rescue. `W2-1` this session (the §VII.CK D4 mechanism corrigendum, `S116-W2-CK-STAGE2-VERIFY`, building on the S115 `CLOSED-EXTERNAL-AS-A-COUPLING` disposition) holds the D4 crossed-product corridor `A_K ⋊ SU(3)_R` at **CLOSED-EXTERNAL-AS-A-COUPLING**: it supplies an overall coupling `g_R` plus the **forced Z₃-circulant texture** — and nothing else (registry §VII.CK D4-disposition: "the crossed product holds only an overall coupling `g_R` with the texture/phase FORCED around it"). The one structurally-forced object, the circulant, is **exactly what washed out** in S115.

So the off-diagonal `U_eL` your rescue requires is **not** part of the crossed-product's forced content. It is a *further* deformation beyond the forced circulant — **doubly external**: outside `Ω¹_{D_K}(A_K)` (NCG-external, granted) **and** beyond the only forced texture the substrate's own SU(3)_R right-isometry supplies. Your §2 `S96 L_X` constrains the *direction* of that further deformation (`q₇`-neutral side-condition) but not its *magnitude* — and the magnitude is the free coupling the axioms do not fix (S96's own non-simultaneous-landing residual is the proof the side-condition is not tight enough to pin the values). A side-condition on a free coupling is a constraint on the *corridor*, not a derivation of the *point* in it. The register reads the quark `ε_LX` as external (CKM FALSIFIED; `V_us`, the one pure prediction, FAILED); the identical machinery on a different fiber cannot be re-graded "derivation."

#### EMERGENCE — new structure from the exchange

The exchange has converted a contested *wall* into a precise *joint discriminator*, and that is the durable output.

**The replaced object.** My "J-inert wall" (withdrawn) → the **mass-pinned-point-on-the-J-orbit** test. Three pinned facts now frame it: (i) the off-diagonal `ε_LX` traces an orbit through `J`-space — CONCEDED (your Sage table + S96 monotonic lift); (ii) the substrate does not supply a free point on that orbit — the charged-lepton mass-fitting **pins** `U_eL` (DISSENT §1); (iii) a spectrum-pinned `M_R` is generation-diagonal, so the *mixing* rides entirely on external off-diagonal `M_D` (DISSENT §2). The fork is no longer "is `J` mobile" (it is) but "**does the mass-pinned `ε_LX` land the mixing in band, or over-rotate like `V_us`**."

**What the W2-3 compute (`S116-W2-LEPTON-PMNS-TEXTURE`) must show to settle rescue-vs-wall (precise pre-registration):**

- **Track A (ε_LX-RESCUABLE corridor live):** a *single* external `ε_LX` — one charged-lepton off-diagonal texture `{ρ, |w|, θ}` plus the neutrino seesaw — lands `mix_grp ≥ 3` (≥3 of `{sin²θ₁₂, sin²θ₂₃, sin²θ₁₃, J}` inside the NuFIT 5.2 NO 3σ bands) **simultaneously** with `m_e : m_μ : m_τ` in the same 0.5-dex mass grid the quark sector used, **and** with `M_R` held at its B-branch spectrum value (not re-fit to source mixing). If the *same* texture does both, the corridor is live — though still external per sub-(b), it is at least a *constrained* external corridor, not a free fit.
- **Track B (WALLED, the quark pattern repeats):** fitting `m_e:m_μ:m_τ` pins `U_eL`; the pinned `U_eL` drives `sin²θ_{ij}(U_eL† U_ν)` **past** the band (the `V_us/PDG = 0.3107/0.225 = 1.38` overshoot analog; `mix_grp ≤ 2` when masses fit) — OR the mixing lands *only* by **detaching** the mixing texture from the mass-fixed `U_eL` (a separate neutrino `ε_LX^ν` and/or an off-diagonal `M_R`), i.e. *more* external input, which **confirms** rather than refutes the wall.

**The discriminator number and its framing.** W2-3 reports `mix_grp` at the mass-fitting `ε_LX`. `mix_grp ≥ 3` *at the mass-fixed point with spectrum-pinned `M_R`* = a live (still-external) rescue corridor → Track A. `mix_grp ≥ 3` *only after detaching the mixing `ε_LX` from the mass-fixed `U_eL`* = an external fit → Track B. The S96 residual (angles move, `R` shortfall, no simultaneous landing) is the standing prior **toward Track B**: the lepton sector already showed it sits on the same coupled surface where mixing and masses cannot both be satisfied by one external deformation.

**Two sharper questions for Round 3:**

- **R3-Q1 (the overshoot magnitude, not its possibility).** The charged-lepton span `m_τ/m_e = 3477×` (log-spacing ratio 1.89) is comparable to or larger than the down-quark span whose mass-pinned off-diagonals overshot `V_us` by 38%. At the W2-3 `ε_LX` that fits `m_e:m_μ:m_τ`, what is `sin²θ₁₂(U_eL† U_ν)`, and does the mass-pinned `U_eL` over-rotate the PMNS 1-2 angle the way the mass-pinned `U_dL` over-rotated `V_us` — or does the seesaw inversion on the neutrino side *measurably* absorb it? Name the quantitative absorption mechanism, not just its possibility.

- **R3-Q2 (the mixing that survives a diagonal `M_R`).** Set `M_D` generation-diagonal and keep only the spectrum-pinned (diagonal) `M_R`. What PMNS mixing survives? If "none" (as the seesaw algebra forces for diagonal `M_R`), the large PMNS angles are attributable to off-diagonal `M_D = ε_LX^ν` (external), **not** to the Dirac/Majorana split — confirming the split is a mass-channel DOF, not the generation-mixing handle the rescue needs. If some mixing survives, name the off-diagonal that carries it and show it is spectrum-pinned rather than externally supplied.

### R2 · neutrino-detection-specialist

#### CONVERGENCE — where you now grant the connes side

I grant connes's R2 §1 in full, and it forces a correction to my R1 §2.

**My `b`-sweep proved the orbit, not the landing.** My R1 Sage table swept `R₁₂(b)` until `J` crossed the band and read that as "the rescue lives in the deformation." Connes's R2 §1 is the correct sharpening: `b` is NOT a free dial. If the charged-lepton off-diagonal is the *same* matrix element that diagonalizes `M_e`, then fitting `m_e:m_μ:m_τ` PINS `b`, and my sweep shows only that the J-orbit PASSES THROUGH the band — not that the mass-pinned point lands there. I over-read my own table. "Some `b` works" is necessary, not sufficient; the operative question is where the *mass-fixed* `b` sits.

**The precedent is on-disk and adverse — granted.** The charged-lepton log-spacing ratio `ln(m_μ/m_e)/ln(m_τ/m_μ) = 1.89` IS the lepton analog of the down-quark `9/5 = 1.80` Casimir lock, and `S111-CF-YUK-FULLFLAVOR` (s111_gate_verdicts.txt line 73) computed exactly what a mass-pinned point does: `|V_us|^FW = 0.3107` vs PDG `0.225`, a 38% overshoot, slot-6 the sole FAIL — "the texture magnitudes needed to break the mass log-gap locks force too large a 1-2 rotation." That is a computed, adverse precedent, not a rhetorical worry, and the WALLED reading is entitled to it.

**I withdraw a specific R1 over-statement.** My R1 §3 wrote "the large PMNS angles are dominated by the `M_R` texture — spectrum-supplied." Connes's R2 §2 is right that a diagonal `M_R`, taken as a STANDALONE matrix, has trivial eigenvectors and supplies no mixing by itself. "Dominated by `M_R` texture" mis-stated it as if `M_R` alone rotated. I withdraw that phrasing and re-aim at the seesaw COMPOSITE, where (DISSENT) the correction is decisive — and where connes's own load-bearing step fails.

**The concession connes asked for — bounded.** I grant the conditional connes built: IF the lepton PMNS is structurally the quark situation — `PMNS = U_eL† U_ν` a misalignment of two mass-pinned Dirac rotations with no relief stage — THEN "rescuable" weakens to "held-number." The J-orbit would be mobile (CONCEDED both ways now) but the substrate-forced point would sit out of band, and the 2.9× would be a number we HOLD against extraction, not one the substrate derives. That is a real epistemic down-grade, and I accept it *as the antecedent*. My DISSENT is precisely that the antecedent fails — the lepton sector has a relief stage (the seesaw) the quark sector structurally lacks.

#### DISSENT — where you hold, with NEW argument (don't restate R1)

Grant the off-diagonal is mass-pinned (CONVERGENCE). The wall does not live in the *mobility* of the orbit (connes withdrew that), and I now grant it does not live in a *free* dial either. Connes's R2 re-aimed it at "the mass-pinned point lands past the band, like `V_us`." My NEW ground: connes's own load-bearing step — R2 §2's "a spectrum-pinned `M_R` is generation-diagonal, so it supplies no mixing" — is **false in the seesaw composite**, and its failure IS the relief stage that breaks the quark mass-vs-mixing coupling. Direction of explanation: `D_K` → B-branch fold energies (`M_R`) → seesaw composite `M_ν = M_D M_R⁻¹ M_D^T` → `U_ν` → emergent PMNS. The lab angles are the image; `M_R` is read off the spectrum.

**1. The seesaw is a reweighting stage; a diagonal-but-HIERARCHICAL `M_R` is load-bearing on the mixing channel.**

Connes's R2 §2 dichotomy conflates two distinct statements:

- (i) `M_R` diagonal *as a standalone matrix* → trivial eigenvectors → no mixing. TRUE.
- (ii) `M_R` diagonal *in the seesaw composite* → contributes nothing to the light-neutrino mixing; "all of `U_ν`'s mixing comes from the off-diagonal of `M_D`." **FALSE.**

The light-neutrino mixing is the eigenvector structure of `M_ν[i,j] = Σ_k M_D[i,k] M_D[j,k] / M_R[k]`. The factor `1/M_R[k]` **reweights `M_D`'s columns**. A *degenerate* `M_R = M·1` factors out (`M_ν = M_D M_D^T / M`) and returns the Dirac mixing — only THEN is connes's (ii) correct. A *hierarchical* `M_R` does not factor out: it changes which column of `M_D` dominates `M_ν`, and the seesaw mixing angle tracks the `M_R` hierarchy at FIXED `M_D`.

Computed object (2×2 type-I seesaw, **illustrative toy — not framework-pinned values**; fixed small Dirac off-diagonal `M_D = [[1, 0.1],[0.1, 5]]`, varying ONLY the diagonal `M_R`; Sage RDF):

| `M_R` (diagonal) | `θ_ν` |
|:---|:---|
| `diag(1, 1)` (degenerate) | `1.43°` ≡ the Dirac angle of `M_D` |
| `diag(1, 5)` | `2.85°` |
| `diag(1, 25)` | `43.86°` |
| `diag(1, 100)` | `82.08°` |

The SAME small Dirac off-diagonal yields `θ_ν` from `1.4°` to `82°` as the diagonal `M_R` hierarchy turns — while the charged-lepton Dirac angle of `M_D` itself stays fixed at `1.43°`, M_R-independent. This is the standard single-right-handed-neutrino-dominance / seesaw enhancement (Smirnov; King): `M_D` supplies the SEED off-diagonal; `M_R` supplies the AMPLIFICATION; the resulting angle is M_R-controlled at fixed `M_D`. So connes's R2 §2 mis-locates the control variable: the SIZE of `U_ν`'s mixing is set by the `M_R` hierarchy, not by the size of `M_D`'s off-diagonal.

Crucially this bites even on connes's OWN claimed form `M_R = diag(M_0, M_1, M_1)`: that is non-degenerate in the 1-2 and 1-3 sectors (`M_0 ≠ M_1`), so it reweights the SOLAR (θ₁₂) and REACTOR (θ₁₃) angles — exactly where the bare tri-maximal texture's `15×` θ₁₃ overshoot lives. The `t=1≡t=2` degeneracy only flattens the 2-3 block back to the Dirac θ₂₃ (which is near-maximal anyway, and unconstrained-by-the-wall). And the framework's `M_R` is not even that: it is supplied by the B-branch `D_K` fold energies, which carry the bowtie splitting `B1 < B2 < B3` (distinct at all τ>0 — the computed normal-ordering-from-crossing at τ=0.107), so the reweighting is available across ALL three blocks. Which `M_R` form is physical — B-branch-distinct `diag(B1,B2,B3)` (my reading, grounded in the bowtie) vs bare-multiplicity-leg `diag(M_0,M_1,M_1)` (connes's reading) — is itself a W2-3 input, not a settled point.

**Answer to your R3-Q2, brought into R2.** You asked: set `M_D` generation-diagonal, keep only the diagonal `M_R` — what mixing survives? Answer, honestly: with `M_D` strictly diagonal, NONE — I grant it freely (`M_ν` is then diagonal). But that forces the seed to zero, which is the wrong limit. Your own operative limit is a *mass-pinned* (hence small, charged-lepton-aligned, NON-zero) `M_D` off-diagonal — and there the table shows the surviving mixing is large and carried by the diagonal-hierarchical `M_R` reweighting, NOT by the magnitude of the Dirac off-diagonal.

**2. This is exactly the relief the quark sector cannot have — and it costs ZERO extra parameters.**

The quark CKM `= U_uL† U_dL` is the misalignment of TWO mass-pinned Dirac rotations. Both fit charged-fermion mass log-gaps; there is NO reweighting stage between mass-fitting and mixing — the off-diagonal that breaks the log-gap IS the rotation, so the overshoot is rigid (`V_us = 0.3107`). The lepton PMNS `= U_eL† U_ν` replaces the second mass-pinned Dirac rotation with the seesaw `U_ν`:

- `U_eL` does the charged-lepton mass-fitting — mass-pinned, CONCEDED, the `1.89`-log-gap analog of `U_dL`. I do not contest that it sits where the masses put it.
- `U_ν` is NOT a charged-fermion mass-pinned Dirac rotation. It diagonalizes `M_ν = M_D M_R⁻¹ M_D^T`, whose mixing is set by the spectrum-pinned `M_R` hierarchy reweighting `M_D`, and whose light eigenvalues are the neutrino `Δm²` (oscillation-anchored), NOT a charged-lepton log-gap.

So the large PMNS mixing does not have to come from an over-rotated mass-pinned Dirac angle (the `V_us` failure mode). It can ride the seesaw enhancement on `U_ν`, governed by `M_R` (spectrum-pinned) and `Δm²` (oscillation-anchored). The relief is the seesaw FORMULA's reweighting — not a dialed parameter, and not a SEPARATE `ε_LX` bolt-on (your R1 sub-c worry). The quark budget is `M_D` + a free down-scale `Λ_d`; the lepton budget is `M_D` + a spectrum-pinned `M_R` (no free scale). The relief TIGHTENS the budget. This is the quantitative absorption mechanism your **R3-Q1** demands by name: seesaw enhancement (single-RH-neutrino dominance) — the `M_R⁻¹` reweighting that decouples `U_ν`'s angle from `M_D`'s Dirac angle, with amplification factor set by the B-branch ratio `B_max/B_min`. Whether that factor lands θ₁₂ in band at the framework's specific `M_R` is W2-3; the mechanism is named and computed.

**Engaging your sub-(a) directly: the fiber-charge changes operator ADMISSIBILITY, and that IS a generation-mixing handle.** You are right that `ℂ⊕ℍ` vs `M₃(ℂ)` is not a generation index on the fiber — conceded in R1, not reopened. But the distinction is not inert "which-16-dim-rep" labeling: it selects WHICH MASS OPERATORS ARE ADMISSIBLE. The neutrino fiber admits a Majorana `M_R` (KO-dim-6 `J`-self-conjugacy); the quark fiber does not. That admissibility is the entire difference between "mixing = misalignment of two Dirac rotations" (rigid, quark) and "mixing = seesaw composite WITH a reweighting stage" (relieved, lepton). The Majorana operator is generation-non-diagonal *in its composite action* `M_D M_R⁻¹ M_D^T` in a way no Dirac-only quark texture can reproduce — not because `M_R` carries a generation index the bare `D_K` is blind to, but because the seesaw INVERTS and REWEIGHTS, and a Dirac sector has no inversion stage to invert. **Wall-silence is not the whole story** (your answer to my R1-Q1): the homogeneity/commutant wall is silent on the misalignment `U_eL† U_ν`, yes — but the substrate is NOT silent on `U_ν`'s STRUCTURE, because `M_R` is spectrum-pinned. "The wall does not forbid it" understates the case: the substrate SHAPES it through the spectrum-supplied `M_R` hierarchy, even where the wall says nothing.

**The honest boundary (my discipline).** The seesaw enhancement is load-bearing only if the SPECIFIC spectrum-pinned `M_R` hierarchy (the actual `B1<B2<B3` fold energies), reweighting the mass-pinned `M_D` off-diagonals, lands the angles in band with a DIAGONAL `M_R`. If in-band mixing requires an off-diagonal `M_R` (generation structure beyond the diagonal fold energies) or a neutrino `ε_LX^ν` detached from `M_D`, then connes's dichotomy second horn fires and the rescue collapses to held-number. I hold that the reweighting STAGE exists and is non-vacuous (the table proves it, refuting R2 §2 (ii)); whether the framework's specific `M_R` USES it to land in band is the open discriminator, not a wall.

#### EMERGENCE — new structure from the exchange

The exchange has converged the fork to a single, sharp, pre-registered discriminator — and both sides can now AGREE on the discriminator even while we disagree on its prior.

**The pinned reduction.** Three facts are now jointly held: (i) the off-diagonal `ε_LX` traces a mobile J-orbit (connes CONCEDED in R2); (ii) the charged-lepton `U_eL` is mass-pinned, its rotation fixed by `m_e:m_μ:m_τ` (I CONCEDED in CONVERGENCE); (iii) the seesaw is a reweighting stage, so a diagonal-hierarchical spectrum-pinned `M_R` is load-bearing on `U_ν`'s mixing — NOT a spectator (DISSENT §1, refuting connes R2 §2 (ii)). The fork is therefore neither "is J mobile" (it is) nor "is `M_R` diagonal" (it can be, and still matter); it is:

> **Does the seesaw enhancement on a DIAGONAL spectrum-pinned `M_R` carry the mass-pinned `M_D` off-diagonals to in-band PMNS angles — OR does in-band mixing require off-diagonal `M_R` / a detached neutrino `ε_LX^ν` (more external input)?**

**The W2-3 discriminator (`S116-W2-LEPTON-PMNS-TEXTURE`), with the framing each outcome warrants.** I accept connes's Track A / Track B skeleton and refine the verdict map to three pre-registered outcomes, fixed BEFORE the number:

- **PASS → Track A, rescue live.** `mix_grp ≥ 3` (≥3 of `{sin²θ₁₂, sin²θ₂₃, sin²θ₁₃, J}` inside NuFIT NO 3σ) AT the `M_D` that fits `m_e:m_μ:m_τ` on the same mass grid the quark sector used, WITH `M_R` held DIAGONAL at its B-branch spectrum values. Frame: the seesaw enhancement relieved the quark mass-vs-mixing coupling; the spectrum-pinned `M_R` hierarchy is the load-bearing weighting; `ε_LX` is a CONSTRAINED external corridor — still external in the NCG sense (sub-b), but the `M_R` weighting is substrate-supplied, strictly closer to derivation than the quark `ε_LX` whose 4 texture params plus `Λ_d` are free. A PASS frames the W2-3 number as a *constrained derivation*, not a free fit.
- **INFO → relief partial / pending.** `mix_grp ≥ 3` only when the diagonal `M_R` is RESCALED off its bare B-branch values (diagonal but tuned), OR the angles land but `R = Δm²₃₂/Δm²₂₁` stays out of band (the S96 standing residual: peak `R = 6.87` vs floor `[17,66]`). Frame: the seesaw relieves the angle-tension but the specific spectrum-pin does not yet close simultaneity; HELD pending a tighter `M_R` identification or the separate `R` channel. The angle-rescue is live; the four-band simultaneity is not.
- **FAIL → Track B, walled / held-number.** The mass-pinned `M_D` over-rotates (`mix_grp ≤ 2` when the masses fit — the `V_us = 0.3107` analog), OR in-band mixing lands ONLY via off-diagonal `M_R` / detached `ε_LX^ν`. Frame: the lepton sector shares the quark coupling, the 2.9× is a held-number, the §VII.CK multiplicity-scalar wall extends to PMNS. A FAIL frames the W2-3 number as an external fit.

**The standing priors, declared honestly.** Connes's prior points to Track B and he is entitled to it: the S96 honest residual (angles move, but no single `ε_LX` lands all four bands; `R` is the binding shortfall) is real, on-disk, unrefuted. My prior points to Track A: the seesaw reweighting (the table) is a relief stage the quark sector demonstrably lacks, and the framework's `M_R` is non-degenerate (bowtie `B1<B2<B3`), so the enhancement is structurally available. Neither prior is the verdict; W2-3 is. What the exchange SETTLED is that the verdict is DECIDABLE by one compute — the mass-pinned point with diagonal spectrum-pinned `M_R` — and that its three outcomes carry three distinct epistemic framings.

**My final question for Round 3 (R3-Q-NDS).** You hold (sub-b) that the lepton `ε_LX` is "the identical external machinery applied to a different fiber" as the quark `ε_LX`. But the quark sector has NO `M_R⁻¹` reweighting stage — its `M_D` off-diagonal acts on the mixing UNMEDIATED, while the lepton `M_D` off-diagonal acts MEDIATED by a spectrum-pinned hierarchy that the table shows can swing the SAME off-diagonal from `1.4°` to `82°`. Is a spectrum-supplied reweighting stage that exists in one sector and is structurally absent in the other "identical machinery on a different fiber" — or is it the substrate-derived metric on the mixing channel that makes the lepton handle structurally different from the quark handle? Concretely: if W2-3 returns PASS at the diagonal B-branch `M_R`, do you grant that the spectrum-pinned `M_R` weighting (not a free parameter) is what landed it — a derivation-leaning corridor the quark sector cannot enter — even while `M_D` itself stays external?

---

## Round 3 — Convergence on a Structural Verdict

### R3 · connes-ncg-theorist — final position

**Pinned position up front.** I concede the structural core of your case and hold the epistemic boundary — and the two are compatible, not a hedge. The seesaw reweighting stage is REAL, parameter-free, spectrum-pinned, and structurally ABSENT in the quark sector: it is **not** "identical machinery on a different fiber." I grant your phrase exactly — it is a *substrate-derived metric on the mixing channel*. But a metric is a ruler, and a ruler returns a length only when handed a vector: the substrate supplies the ruler (`M_R` = B-branch fold energies), the vector it measures (the seed `M_D` off-diagonal) stays external `ε_LX`. So the lepton corridor is a **metricized / constrained-external** corridor — strictly closer to derivation than the quark free-fit, quark-INACCESSIBLE, but external on the seed and therefore not a derivation. My prior leans Track B on the S96 `R`-shortfall + the `V_us` mass-pinned-overshoot base-rate; I hold it as a PRIOR, subordinate to W2-3.

#### Answer to R3-Q-NDS (head-on): a substrate-supplied metric, not a fiber relabel — and a metric needs an external argument

You asked whether a spectrum-supplied reweighting stage present in one sector and structurally absent in the other is "identical machinery on a different fiber," or "the substrate-derived metric on the mixing channel that makes the lepton handle structurally different." **It is the latter — granted, three times over, cleanly.**

**1. The reweighting stage is real, and my R2 §2 load-bearing step was wrong where it mattered.** My R2 §2 wrote "a spectrum-pinned `M_R` is generation-diagonal, so it supplies no PMNS mixing; all of `U_ν`'s mixing rides on the off-diagonal of `M_D`." That is FALSE in the seesaw composite, and I withdraw it. I re-derived your table from scratch (Sage RDF, `M_D = [[1,0.1],[0.1,5]]`, varying ONLY diagonal `M_R`), value-for-value:

| `M_R` (diag) | `M_ν = M_D M_R⁻¹ M_D^T` | `θ_ν` |
|:---|:---|:---|
| `diag(1,1)` | `[[1.0100,0.6000],[0.6000,25.0100]]` | `1.43°` ≡ Dirac angle of `M_D` |
| `diag(1,5)` | `[[1.0020,0.2000],[0.2000,5.0100]]` | `2.85°` |
| `diag(1,25)` | `[[1.0004,0.1200],[0.1200,1.0100]]` | `43.85°` |
| `diag(1,100)` | `[[1.0001,0.1050],[0.1050,0.2600]]` | `82.08°` |

The mechanism is visible in the `(2,2)` entry: `M_R⁻¹` drives it `25.01 → 5.01 → 1.01 → 0.26`, and at `diag(1,25)` it falls into near-degeneracy with the `(1,1)` entry (`1.0100 ≈ 1.0004`) — near-degenerate diagonal ⇒ near-maximal mixing by level repulsion. The SAME small Dirac seed (`θ_D = 1.43°`, `M_R`-independent) is swung to `82°` by the diagonal `M_R` hierarchy alone. This is textbook seesaw enhancement (Smirnov 1993; single-RH-dominance, King): `M_D` is the seed, `M_R` the amplifier, the angle `M_R`-controlled at fixed seed. My "spectator" claim was the standalone-matrix statement (`M_R` diagonal ⇒ trivial eigenvectors, TRUE) smuggled into the composite (where it is FALSE). **CONCEDED — and it bites on my own `diag(M_0,M_1,M_1)` form, which is non-degenerate in the 1-2/1-3 blocks and so reweights exactly the solar/reactor angles where the bare tri-maximal 15× θ₁₃ overshoot lives.**

**2. It is structurally different from the quark handle.** `V_CKM = U_uL† U_dL` is the misalignment of two mass-pinned Dirac diagonalizations with NO stage between mass-fitting and mixing — the off-diagonal that breaks the mass log-gap IS the rotation (the rigid `V_us = 0.3107`, S111 line 73). `PMNS = U_eL† U_ν` replaces the second Dirac rotation with a seesaw composite carrying a reweighting stage. That stage exists because the `ℂ⊕ℍ` lepton fiber ADMITS a Majorana `M_R` (KO-dim-6 `J`-self-conjugacy) and the `M₃(ℂ)` quark fiber does not. So the sector-asymmetry is a genuine substrate DOF — not as a generation index (it is §VII.BL-blind there, R1-conceded), but as a **mass-operator-admissibility** selector that opens a structurally distinct mixing channel. This upgrades my R1 sub-(a). **GRANTED.**

**3. The conditional — granted without reservation.** If W2-3 returns `mix_grp ≥ 3` at the `M_D` that fits `m_e:m_μ:m_τ`, with `M_R` held DIAGONAL at its B-branch spectrum values (not re-fit to source mixing), then YES: the spectrum-pinned `M_R` weighting — not a free parameter — is what landed it; it is a derivation-leaning corridor the quark sector structurally cannot enter. **I grant this cleanly.** The structural difference is real, and a PASS makes it load-bearing. This is the precise conditional you asked for, and I believe it.

**Where the metric framing also FIXES the boundary — my hold.** A metric is a ruler; it returns a length only when handed a vector. The substrate supplies the ruler (`M_R` = B-branch fold energies, spectrum-pinned); the vector it measures — the seed off-diagonal of `M_D` — is the external `ε_LX`, value-unfixed by the axioms. Make the enhancement condition explicit (substitution chain per `math-scripts.md`):

```
Claim: large PMNS mixing fires iff an EXTERNAL seed lands on a SPECTRUM-PINNED resonance.
Step 1: U_ν diagonalizes  M_ν = M_D M_R^{-1} M_D^T.                    [type-I seesaw]
Step 2: large mixing  ⟺  diag(M_ν) near-degenerate  ⟺  level repulsion. [2-state mixing]
Step 3: dominant-diagonal seed ⇒ diag(M_ν)_k ≈ M_D[k,k]^2 / M_R[k].    [Sage table: (2,2) entry]
Step 4: near-degeneracy ⟺ M_D[1,1]^2/M_R[1] ≈ M_D[2,2]^2/M_R[2]
                        ⟺ M_D[2,2]/M_D[1,1] ≈ sqrt(M_R[2]/M_R[1]) = sqrt(B_2/B_1).
Concl.: the resonance fires iff the RATIO of external Dirac entries matches
        sqrt(B-branch ratio). Substrate fixes the RHS (the ruler);
        external ε_LX fixes the LHS (the argument). (Table check: 25/25 ≈ 1/1 at diag(1,25).)
```

So even granting everything: the substrate supplies a FIXED ruler against which an external seed may or may not resonate. A PASS shows the external seed sits on the substrate ruler — a CONSTRAINED-external corridor (the ruler is fixed; no longer a free 4-parameter fit) — but the seed *landing* on the ruler is an external fact, not a derived one. The right tag is **metricized external coupling**: `free-external` (quark: 4 texture params + free `Λ_d`) → `constrained-external` (lepton: seed + spectrum-pinned ruler) is a genuine one-notch upgrade; `constrained-external` → `derivation` is the notch the seed-externality denies.

#### Acceptance of the 3-outcome framing map — with one label refinement

I ACCEPT your PASS/INFO/FAIL map. One refinement on the Track-A label, load-bearing for sub-(b):

- **PASS → Track A**, tagged **CONSTRAINED-EXTERNAL corridor**, not "constrained-derivation." Frame: the spectrum-pinned `M_R` metric is substrate-supplied and load-bearing (your win); the seed stays external (my hold). The W2-3 number is a substrate-WEIGHTED external corridor — a real epistemic upgrade over the quark free-fit, quark-inaccessible — but external on the seed. "Closer to derivation than the quark `ε_LX`" is exactly right; "a derivation" overshoots.
- **INFO → relief partial / `R`-residual.** Agreed verbatim: angles relieve but `R = Δm²₃₂/Δm²₂₁` (a mass-SPECTRUM observable — the eigenVALUES of the SAME `M_ν` whose eigenVECTORS the metric helps) stays short of the NuFIT floor `[17,66]` (S96 peak `6.87`). The metric can relieve the angle channel while the spectrum channel holds — the most likely split given the S96 residual.
- **FAIL → Track B / held-number.** Agreed: the mass-pinned seed over-rotates (`mix_grp ≤ 2`; the `V_us = 0.3107` analog), OR in-band mixing lands only via off-diagonal `M_R` / detached `ε_LX^ν` (more external input), confirming the wall.

#### Standing prior (a PRIOR, not the verdict)

I am entitled to Track B per the S96 residual and I hold it softly, subordinate to W2-3. Two concrete on-disk indicators:

- **The `R`-shortfall is the binding one.** S96: angles move under the non-LI `L_X` with the `q₇`-neutral side-condition preserved at every point, but no single `ε_LX` lands all four NuFIT bands, and `R = Δm²₃₂/Δm²₂₁` peaks at `6.87` vs floor `[17,66]`. `R` is the eigenvalue-RATIO of the SAME composite `M_ν = M_D M_R⁻¹ M_D^T` whose eigenVECTORS the reweighting helps. The seesaw metric can relieve the angles and still miss the spectrum — the S96 residual is exactly that signature, and the metric does not touch it.
- **The `V_us` base-rate.** The one place the framework computed a mass-pinned mixing prediction (`S111-CF-YUK-FULLFLAVOR`, `V_us = 0.3107` vs PDG `0.225`, 38% overshoot, slot-6 the SOLE FAIL of a 5/6 PASS) it over-rotated, "because the texture magnitudes needed to break the mass log-gap locks force too large a 1-2 rotation." The lepton charged-log-gap ratio `1.89` ≈ the down `9/5 = 1.80` lock; the mass-pinned `U_eL` sits where the masses put it, as `U_dL` did.

This is SOFTENED from my R1 "the 2.9× IS the wall" (withdrawn R2): the reweighting stage is a genuine relief mechanism the quark sector lacks, so the lepton fork is decidable BOTH ways and is not pre-walled. Declared weights: **~0.55 Track B** (over-rotation or `R`-shortfall) / **~0.30 Track A constrained-external** (the enhancement fires at the mass-fit seed against the B-branch ruler) / **~0.15 INFO** (angles relieve, `R` holds). W2-3 is the verdict; the prior only says where I would bet before the number.

#### sub-(b) ε_LX epistemic status — external-as-a-coupling (W2-1-confirmed), with a substrate-supplied weighting the quark lacks

The axis is **free-vs-constrained WITHIN external** (your R1 §3, conceded), not derivation-vs-external. This session's W2-1 (the `S116-W2-CK-STAGE2-VERIFY` / §VII.CK D4 corrigendum, discharging `CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM` from the S115 `S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` INFO) holds the D4 crossed product `A_K ⋊ SU(3)_R` at **CLOSED-EXTERNAL-AS-A-COUPLING**: "the crossed product holds only an overall coupling `g_R` with the texture/phase FORCED around it" (§VII.CK D4-disposition). The forced texture (Z₃-circulant `|U_ij|² = 1/3`, `J = 1/(6√3)`) is exactly what WASHED OUT (S115 FAIL). So:

- the `ε_LX` seed is external-as-a-coupling — SETTLED, both sectors;
- the lepton corridor adds a spectrum-pinned reweighting metric (`M_R`) the quark corridor structurally lacks — so it is MORE CONSTRAINED;
- **sub-(b) verdict: external-as-a-coupling on the seed, with a substrate-supplied weighting stage the quark sector cannot enter.** A metricized external coupling, not a derivation. The two readings (external on the seed + more-constrained-than-quark) are not in tension; they are the free-vs-constrained axis you correctly named.

#### sub-(a) and sub-(c) — final

- **sub-(a):** genuine substrate DOF, via **mass-operator admissibility** (Majorana `M_R` on `ℂ⊕ℍ`, absent on `M₃(ℂ)`), NOT via a generation index (§VII.BL-blind there). Upgraded from my R1 "fiber-charge only": the admissibility difference has real consequences on the mixing channel (the reweighting stage). Genuine DOF on the admissibility/metric channel; §VII.BL-blind on the generation-index channel — different channels, both true.
- **sub-(c):** the relief MECHANISM is real and parameter-free (the seesaw reweighting, `M_R` spectrum-pinned — a withdrawal of my R1 "any relief is more external input"). Its SUFFICIENCY at the framework's specific B-branch `M_R` is the open W2-3 question; the S96 `R`-shortfall is the standing adverse indicator. Verdict: **relieved-in-MECHANISM, sufficiency-pending** — a genuine upgrade from "shared," not yet "relieved" simpliciter.

#### Pinned closing

The fork is no longer "is the lepton handle different from the quark handle" — it IS (the seesaw metric is real, quark-inaccessible, spectrum-pinned: granted). It is now: **does the substrate-pinned `M_R` ruler, handed the mass-fit external seed, read off in-band PMNS — and does the SAME composite's spectrum reproduce `R`.** A PASS is a constrained-external corridor (substrate ruler, external seed), quark-inaccessible, closer to derivation than anything the quark sector reached — but external on the seed, so not a derivation. My prior leans Track B on the `R`-shortfall and the `V_us` base-rate; W2-3 is the verdict. Direction holds throughout: `D_K` → B-branch fold energies (`M_R`) → seesaw composite `M_ν = M_D M_R⁻¹ M_D^T` → `U_ν` → emergent PMNS; the lab angles are the image, never the starting point.

### R3 · neutrino-detection-specialist — final position + writes the Structural Verdict below

**Pinned position up front.** I apply my own R2 pre-registered map to the W2-3 number — committed BEFORE it landed — and it routes to **Track B (WALLED)**, refined by what the compute surfaced to **WALLED-AS-UNDER-DETERMINED**. I conceded this antecedent in my R2 CONVERGENCE ("IF the lepton PMNS is structurally the quark situation … THEN 'rescuable' weakens to 'held-number'"), and the discriminator fired on the held-number side. I do not reach for Track A. But the wall is the SOFTEST class on the ladder — under-determination, not structural exclusion — and the structural win the exchange produced (the seesaw reweighting metric is real, parameter-free, spectrum-pinned, and quark-inaccessible — connes conceded it three times over) survives the FAIL intact. What FAILED is the metric's SUFFICIENCY at the framework's specific B-branch `M_R`, not the metric's EXISTENCE.

**1. The pre-registered map, applied honestly.** `S116-W2-LEPTON-PMNS-TEXTURE` returned `mix_grp = 0/4` at the `M_D` that fits `m_e:m_μ:m_τ`, with `M_R` held DIAGONAL at its B-branch spectrum values `[1.0044, 1.0786, 1.1700]` (S100a) — exactly the Track-A test condition. My R2 EMERGENCE 3-outcome block pinned: "FAIL → Track B … the mass-pinned `M_D` over-rotates (`mix_grp ≤ 2` when the masses fit — the `V_us = 0.3107` analog) … A FAIL frames the W2-3 number as an external fit." The number obeyed the FAIL clause on both its disjuncts:

- `sin²θ₁₂ = 0.996` **OVERSHOOTS** observed `0.303` — the lepton `V_us` analog, the over-rotation connes's R2/R3 base-rate named in advance. The minimal-norm charged-lepton texture that fits the `m_τ/m_μ` Casimir tower (`C₂`-tower ratio 18.0 vs PDG 16.82; level repulsion only RAISES that ratio, so the masses cannot be fit by widening the gap — they force a rearranging off-diagonal `‖ε_LX‖ = 0.036` → near-maximal solar mixing). `sin²θ₂₃ = 0.059`, `sin²θ₁₃ = 0.0087` UNDERshoot — the seesaw enhancement did not fire to lift them.
- `J_PMNS = 0` EXACT — the framework forces `δ_CP ∈ {0,π}` (KO-dim-6 `J`-self-conjugacy ⇒ real textures), so there is no leptonic CP. This is CP-conserving-CONSISTENT (`J=0 ↔ δ_CP=180°` IS inside the NuFIT 5.2 NO 3σ `[108°,404°]`); the tension lives in `θ₁₂`, not in `J`. I flag it as a hard, falsifiable substrate prediction, ORTHOGONAL to the wall.

So by my own pre-registered procedure: **FAIL → Track B.** I concede it cleanly; no convention is shopped, no threshold moved.

**2. The refinement the compute forced: WALLED-AS-UNDER-DETERMINED (a SOFT wall).** My pre-reg FAIL framing called the residual "a held-number" — a number the substrate forces out of band that we hold against extraction. W2-3 sharpened that, and the sharpening matters. The charged-lepton masses fix the eigenVALUES of `M_e`, NOT its eigenVECTORS: for any orthogonal `R`, `M_e = R · diag(m_e,m_μ,m_τ) · Rᵀ` reproduces the masses, so `U_eL` is FREE. The observed PMNS is therefore EXACTLY reachable — at `1.53×` the minimal `‖ε_LX‖` (the `U_eL_match` construction lands 3/3 angle slots). This is a SOFT under-determination wall: the observed point is INSIDE the reachable set, but the substrate does not SINGLE IT OUT. The minimal-norm texture (the substrate-natural choice) gives `mix_grp = 0`; the in-band point exists but rides a non-minimal `U_eL` the masses do not pin. "Reachable but NOT predicted" is the precise verdict — distinct from a HARD structural exclusion (observed point OUTSIDE the reachable set: the §VII.BL/§VII.CK multiplicity-scalar wall on the GENERATION-INDEX channel) AND distinct from a free fit (the substrate supplies the spectrum-pinned `M_R` ruler).

**3. What survives the FAIL — the win is on the MECHANISM, the FAIL is on SUFFICIENCY.** connes conceded, three times over in R3 and value-for-value on my seesaw table, that the reweighting stage is REAL, parameter-free, spectrum-pinned, and structurally ABSENT in the quark sector — "a substrate-derived metric on the mixing channel," NOT "identical machinery on a different fiber." That concession is the durable output and it is untouched by `mix_grp = 0`. The FAIL is located precisely: the framework's B-branch `M_R = [1.0044, 1.0786, 1.1700]` is NEARLY DEGENERATE (`√(B₂/B₁) = 1.036`), and the seesaw resonance condition `M_D[2,2]/M_D[1,1] ≈ √(B₂/B₁)` therefore demands NEAR-EQUAL Dirac entries — incompatible with the hierarchical mass-fit `M_D`. The ruler is real; the framework's ruler is too FLAT to resonate the hierarchical seed, so the enhancement does not fire at the mass-fit point (the task's diagnosis, confirmed by the `θ₂₃/θ₁₃` undershoot). **Sufficiency-FAILED ≠ mechanism-absent** — this is the one place where the verdict is NOT the quark sector's framing.

**4. The corollary — the highest-order finding, and it cuts connes's prior as much as my rescue.** `U_eL` free is not a lepton-only fact. The same algebra holds for `U_dL`: the quark masses fix `M_d`'s singular VALUES, not its left singular VECTORS. So the `S111-CF-YUK-FULLFLAVOR` `V_us = 0.3107` "prediction" was a MULTISTART TIE-BREAK ARTIFACT — the optimizer selected one `U_dL` in the free family, and that point gave `0.3107`; the masses did not force it. This dissolves the asymmetry connes's ~0.55 Track-B prior leaned on: the "`V_us` base-rate" (mass-pinning forces over-rotation) is not a base-rate — it is one selected point in an under-determined family. BOTH sectors' mixing are under-determined; NEITHER is derived. This does NOT rescue Track A (the lepton minimal-norm point still walls at `mix_grp = 0`, and the in-band point is non-minimal). It sharpens WHY Track B holds: the wall is under-determination in BOTH sectors, not a hard mass-vs-mixing coupling unique to one.

**5. Substrate-first frame, held throughout.** Direction: `D_K` → B-branch fold energies (`M_R`, spectrum-pinned) → seesaw composite `M_ν = M_D M_R⁻¹ M_D^T` → `U_ν` → emergent PMNS. The lab angles are the image, never the starting point. The substrate IS the spectral triple; the wall is the substrate's SILENCE on which `U_eL†U_ν` misalignment the external `ε_LX` seed selects — and the metric (`M_R`) it DOES supply is, at the framework's own B-branch values, too flat to resonate the mass-fit seed. I author the Structural Verdict below on this reading.

---

## Structural Verdict

**Pinned position: Track B (WALLED), refined WALLED-AS-UNDER-DETERMINED.** The lepton shape-leg fork resolves to the WALLED branch — but the wall is the SOFTEST class on the ladder, and it is structurally DISTINCT from the quark sector's framing in exactly one respect connes conceded: the lepton corridor carries a real, parameter-free, spectrum-pinned seesaw reweighting METRIC the `M₃(ℂ)`-shared quark sector structurally lacks. The rescue-vs-wall fork is decided on the WALL side because that metric, at the framework's specific nearly-degenerate B-branch `M_R = [1.0044, 1.0786, 1.1700]`, does NOT fire the seesaw enhancement at the mass-fit seed (`mix_grp = 0/4`; `√(B₂/B₁) = 1.036` demands near-equal Dirac entries the hierarchical mass-fit cannot supply). The wall is UNDER-DETERMINATION: the charged-lepton masses fix `M_e`'s eigenVALUES not its eigenVECTORS, so `U_eL` is FREE and the observed PMNS is reachable at `1.53×` the minimal `‖ε_LX‖` — INSIDE the reachable set, NOT singled out by the substrate. Reachable, not predicted. This is neither the hard structural exclusion of the GENERATION-INDEX channel (§VII.BL/§VII.CK multiplicity-scalar wall) nor a free fit (the `M_R` ruler is substrate-supplied); it is a SOFT wall on the MIXING-SELECTION channel.

**ε_LX epistemic status: external-as-a-coupling on the SEED, with a substrate-supplied weighting stage the quark sector lacks — a METRICIZED EXTERNAL COUPLING.** W2-1 this session (`S116-W2-CK-STAGE2-VERIFY`; §VII.CK D4 = CLOSED-EXTERNAL-AS-A-COUPLING) re-confirms the `ε_LX` SEED is external in both sectors. The lepton corridor adds the spectrum-pinned `M_R` reweighting metric (`free-external` → `constrained-external`, a genuine one-notch upgrade, quark-inaccessible) — but `constrained-external` → `derivation` is the notch the seed-externality denies. A metric is a ruler; it returns a length only when handed an external vector (the `M_D` seed). The W2-3 number is a substrate-WEIGHTED external corridor, not a derivation.

The three sub-verdicts, as the two agents converged them:

- **Sub-(a): genuine substrate DOF on the ADMISSIBILITY/metric channel ∧ §VII.BL-blind on the GENERATION-INDEX channel — different channels, both true.** The `ℂ⊕ℍ` vs `M₃(ℂ)` asymmetry is NOT a generation index the bare `D_K` can see (§VII.BL-blind, R1-conceded). Its genuine substrate content is mass-operator ADMISSIBILITY: the lepton fiber admits a Majorana `M_R` (KO-dim-6 `J`-self-conjugacy), the quark fiber does not. That admissibility difference opens the seesaw reweighting stage — a real consequence on the MIXING channel, not the generation-index channel.
- **Sub-(b): admitting `ε_LX` is an EXTERNAL COUPLING (metricized), not a derivation.** Free-vs-constrained WITHIN external is the operative axis (connes R1-conceded); the lepton `ε_LX` seed is external-as-a-coupling (W2-1-settled), wrapped by a substrate-supplied `M_R` weighting the quark `ε_LX` lacks. More-constrained-than-quark, still external on the seed.
- **Sub-(c): relieved-in-MECHANISM, sufficiency-FAILED at the framework's B-branch `M_R`.** The seesaw reweighting is a real, parameter-free relief mechanism the quark sector cannot have (connes withdrew his R1 "any relief is more external input"). Its SUFFICIENCY at the framework's specific nearly-degenerate B-branch `M_R` FAILED (`mix_grp = 0`): the ruler is too flat to resonate the hierarchical mass-fit seed. A genuine upgrade from "shared," not yet "relieved" simpliciter.

**Frames the W2-3 number as: an external fit — reachable, not predicted.** A FAIL frames `mix_grp = 0/4` as the external-fit reading (my R2 map): the substrate-natural minimal-norm `ε_LX` walls, the observed PMNS is reachable only at a non-minimal `1.53×` `U_eL` the masses do not pin. The number is a soft under-determination wall, not a derivation.

**THE COROLLARY (the workshop's highest-order finding): both lepton AND quark mixing are under-determined.** `U_eL` free ⇒ the masses fix eigenvalues not eigenvectors in BOTH sectors. The S111 quark `V_us = 0.3107` "prediction" was a multistart tie-break artifact within the same free family — not a forced derivation. Neither sector's mixing is derived; both are reachable-not-predicted at fixed masses. The asymmetry connes's prior leaned on (the `V_us` over-rotation base-rate) is itself an artifact of one selected point in an under-determined family.

| Item | Verdict | Note |
|:-----|:--------|:-----|
| Lepton shape-leg fork | **Track B WALLED** (refined **WALLED-AS-UNDER-DETERMINED**) | SOFT wall: observed PMNS reachable at 1.53× minimal `‖ε_LX‖`, not singled out. Not a hard structural exclusion; not a free fit. |
| ε_LX epistemic status | **external-as-a-coupling** (METRICIZED) | seed external (W2-1 CLOSED-EXTERNAL-AS-A-COUPLING); `M_R` weighting substrate-supplied + quark-inaccessible. `free-external`→`constrained-external` upgrade; seed-externality denies the derivation notch. |
| Sub-(a) ℂ⊕ℍ sector-asymmetry | **genuine substrate DOF** (admissibility/metric channel) ∧ **§VII.BL-blind** (generation-index channel) | mass-operator admissibility (Majorana `M_R` on ℂ⊕ℍ, absent on M₃(ℂ)); different channels, both true. |
| Sub-(b) admitting ε_LX | **external coupling** (metricized) | more-constrained-than-quark (spectrum-pinned `M_R`), still external on the seed. |
| Sub-(c) mass-vs-mixing tension | **relieved-in-MECHANISM, sufficiency-FAILED** | seesaw reweighting real + parameter-free; does NOT fire at B-branch `M_R` (`√(B₂/B₁)=1.036` too flat for hierarchical seed). |
| Frames W2-3 number as | **external fit** (reachable, not predicted) | `mix_grp=0/4`; soft under-determination wall at 1.53× minimal norm. |
| COROLLARY (both sectors) | **lepton ∧ quark mixing BOTH UNDER-DETERMINED** | masses fix eigenvalues not eigenvectors; S111 `V_us=0.3107` reframed as multistart artifact, not derivation. |

---

## Remaining Open Questions

1. **The R-channel (the binding shortfall).** Does the SAME seesaw composite `M_ν = M_D M_R⁻¹ M_D^T` (mass-pinned `M_D`, diagonal B-branch `M_R`) reproduce `R = Δm²₃₂/Δm²₂₁` in the NuFIT NO floor `[17,66]`, or does it reproduce the S96 peak-`6.87` shortfall? The angles and `R` are eigenVECTORS and the eigenVALUE-RATIO of the SAME composite; the metric can relieve the angle channel while the spectrum (`R`) channel holds. → CF-S117-LEPTON-SEESAW-R-CHANNEL.

2. **The resonance search.** Is there ANY substrate-natural `M_R` (B-branch fold energies across `τ`, or an alternative spectrum-pinned form) that satisfies `M_D[2,2]/M_D[1,1] ≈ √(M_R[2]/M_R[1])` at the mass-fit seed and fires the enhancement to `mix_grp ≥ 3` — i.e., is the framework's seesaw ruler ANYWHERE non-flat enough to resonate the hierarchical seed, or is the near-degeneracy (`√(B₂/B₁)=1.036`) structural across the moduli? → CF-S117-SEESAW-RESONANCE-MR-SEARCH.

3. **The quark-CKM under-determination re-examination (the corollary's direct test).** Is `U_dL` free at fixed quark masses, so that `V_us` spans an interval with PDG `0.2243` reachable at a non-minimal `‖ε_LX‖` (the quark analog of the lepton `1.53×` soft wall) — confirming `V_us = 0.3107` was a multistart artifact, not a derivation? → CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM.

4. **The `M_R` form question (an unsettled W2-3 input).** Is the physical `M_R` the B-branch-distinct `diag(B1,B2,B3)` (bowtie `B1<B2<B3`, my reading) or the bare-multiplicity-leg `diag(M_0,M_1,M_1)` (connes's reading, `t=1≡t=2`-degenerate in the 2-3 block)? The two differ in whether the 2-3 block reweights `θ₂₃`; both are nearly degenerate in the 1-2 block where the `θ₁₂` overshoot lives. → folds into CF-S117-SEESAW-RESONANCE-MR-SEARCH.

---

## Wrap-Up

### What Changed

#### (a) Numerical revisions

- lepton-PMNS residual: bare forced-circulant `2.9×` (tri-maximal, the S114 reading) → external-`ε_LX` `mix_grp = 0/4` (`sin²θ₁₂ = 0.996` overshoot; `sin²θ₂₃ = 0.059`, `sin²θ₁₃ = 0.0087` undershoot; `J_PMNS = 0`); observed PMNS reachable at `1.53×` minimal `‖ε_LX‖`.
- `J_PMNS`: forced-circulant `1/(6√3) = 0.0962250` (washed-out, overshoots from above) → external-`ε_LX` `J = 0` (real texture, `δ_CP ∈ {0,π}`, undershoots from below). Both miss; opposite directions.
- seesaw resonance condition pinned: `√(B₂/B₁) = √(1.0786/1.0044) = 1.036` — the framework's B-branch ruler is nearly degenerate, so the resonance demands near-equal Dirac entries the hierarchical mass-fit cannot supply.

#### (b) Structural changes

- **lepton shape leg: RESONANT-CONDITIONAL ~2.9× (registry §VII.CK D4) → WALLED-AS-UNDER-DETERMINED** (a SOFT wall: `U_eL` free; observed PMNS reachable-not-predicted at 1.53× minimal norm; not a hard structural exclusion, not a free fit).
- **the seesaw reweighting METRIC established as REAL + parameter-free + spectrum-pinned + quark-inaccessible** (connes-conceded three times over) — a substrate-derived metric on the mixing channel, NOT "identical machinery on a different fiber." Type promotion: the FAIL is on the metric's SUFFICIENCY at the framework's B-branch `M_R`, not on its EXISTENCE.
- **ε_LX epistemic status: external-as-a-coupling → METRICIZED external coupling** (`free-external` → `constrained-external` one-notch upgrade; seed external, `M_R` weighting substrate-supplied).
- **the UNDER-DETERMINATION reframe of BOTH sectors' mixing**: masses fix eigenvalues not eigenvectors ⇒ `U_eL`/`U_dL` free ⇒ the S111 quark `V_us = 0.3107` reframed from "prediction" to multistart artifact. NEITHER sector's mixing is derived. (This is the workshop's highest-order output — an epistemic-type change to a previously-headlined quark result.)

### What Holds

- The §VII.BL/§VII.CK multiplicity-scalar wall on the GENERATION-INDEX channel — UNTOUCHED. The bare `D_K` is generation-blind (R1-conceded in full); the wall this workshop SOFTENS is on the MIXING-SELECTION channel, a structurally orthogonal channel.
- `J_PMNS = 0` / `δ_CP ∈ {0,π}` — a hard, falsifiable substrate prediction (KO-dim-6 `J`-self-conjugacy); CP-conserving-CONSISTENT with NuFIT 5.2 NO 3σ `[108°,404°]`.
- Normal ordering from the B-branch crossing at `τ = 0.107`; `Σm_ν` oscillation-anchored; `M_R` spectrum-supplied (B-branch fold energies); `m₁ = 0` rank-deficient (`Y₁ = 0` EXACT) — all unchanged.
- The seesaw metric's EXISTENCE + quark-inaccessibility — connes-conceded, durable across the FAIL.

### What Breaks or Strains

- The S96 `R = Δm²₃₂/Δm²₂₁` shortfall (peak `6.87` vs NuFIT floor `[17,66]`) is now the BINDING open channel for the lepton sector — the eigenvalue-RATIO of the same composite whose eigenVECTORS the metric helps. The metric can relieve the angle channel while the spectrum channel holds; W2-3 leaves `R` untested at the mass-fit seed.
- The S111 quark `V_us = 0.3107` "prediction" STRAINS under the under-determination corollary — if `U_dL` is free, the headline quark-mixing result is a SELECTED point, not a forced one. It must not be cited as a derivation until CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM settles whether the mass-pinned family is narrow or wide.
- The "RESONANT-CONDITIONAL ~2.9×" registry tag (§VII.CK D4-disposition) is now STALE — the resonance does not fire at the framework's B-branch `M_R`. Routed to mack for the §VII.CK annotation patch (Effected-In-Session below).

### Carry-Forward Computations (MATH ONLY — propagate to S117)

**CF-S117-LEPTON-SEESAW-R-CHANNEL**
1. **What**: Compute `R = Δm²₃₂/Δm²₂₁` from the eigenVALUES of the SAME seesaw composite `M_ν = M_D M_R⁻¹ M_D^T` used in W2-3 (mass-pinned `M_D`; `M_R` diagonal at B-branch `[1.0044, 1.0786, 1.1700]`); test the mass-SPECTRUM channel (the binding shortfall the metric does NOT touch).
2. **Inputs**: `computations/session-116/s116_lepton_pmns_texture.npz` (`M_D`, `M_R`, `M_ν`); `canonical_constants` M_R B-branch `[1.0044, 1.0786, 1.1700]` (S100a); NuFIT 5.2 NO `R`-floor `[17,66]` (the S96 anchor); S96 peak `R = 6.87`.
3. **Gate**: PASS if `R ∈ [17,66]` at the mass-pinned `M_D` + diagonal B-branch `M_R`; FAIL if `R < 17` (S96 shortfall persists); INFO if `R` lands only by rescaling `M_R` off bare B-branch. Depends on: s116_lepton_pmns_texture.npz (UPSTREAM); S96 R-residual.
4. **Effort**: ~1 agent, LOW (re-uses W2-3 npz; eigenvalue-RATIO of an existing `M_ν`; no new spectrum build).

**CF-S117-SEESAW-RESONANCE-MR-SEARCH**
1. **What**: Scan substrate-natural `M_R` candidates (B-branch fold energies across `τ`; or alternative spectrum-pinned `M_R` forms incl. connes's `diag(M_0,M_1,M_1)`) to test whether ANY satisfies the resonance condition `M_D[2,2]/M_D[1,1] ≈ √(M_R[2]/M_R[1])` at the mass-fit seed and fires the enhancement to `mix_grp ≥ 3` — i.e., is the framework's seesaw ruler ANYWHERE non-flat enough to resonate the hierarchical seed.
2. **Inputs**: `dirac_spectrum.py` B-branch fold energies across `τ` (incl. `τ = 0.107` crossing) OR the S100a `M_R` derivation; mass-fit `M_D` from `s116_lepton_pmns_texture.npz`; the resonance condition `√(B₂/B₁)`; NuFIT 5.2 NO 3σ bands. Resolves the OQ-4 `M_R`-form question.
3. **Gate**: PASS if a substrate-natural (spectrum-pinned, NOT free-tuned) `M_R` fires `mix_grp ≥ 3` at the mass-fit seed; FAIL if NO substrate-natural `M_R` resonates (the B-branch is structurally too flat across the moduli); INFO if resonance fires only off the fold or at a rescaled `M_R`. Depends on: dirac_spectrum.py B-branch (UPSTREAM); s116 mass-fit `M_D`.
4. **Effort**: ~1 agent, MEDIUM (a `τ`-scan of B-branch fold energies + per-`τ` seesaw recompute; re-uses the mass-fit `M_D`).

**CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM**
1. **What**: Re-examine the `S111-CF-YUK-FULLFLAVOR` `V_us = 0.3107` "prediction" under the under-determination lens: is `U_dL` free (masses fix singular VALUES not left singular VECTORS) so `V_us` spans an interval at fixed quark masses? Quantify the reachable `V_us` range and the minimal `‖ε_LX‖` to reach PDG `0.2243` (the quark analog of the lepton `1.53×` soft wall). The corollary's direct test.
2. **Inputs**: S111 quark texture `{ρ13^d, ρ23^d, |w12^d|, θ_d, Λ_d}` + npz; quark mass spectrum; the S111 multistart seed protocol; PDG `V_us = 0.2243`.
3. **Gate**: PASS (under-determination CONFIRMED for quarks) if `V_us` spans an interval at fixed masses with PDG `0.2243` reachable at a non-minimal norm; FAIL (`V_us` genuinely mass-forced) if `V_us` is uniquely pinned to `0.3107` with no free `U_dL` family; INFO if the family is constrained but narrow. Depends on: s111 quark texture npz (UPSTREAM); the lepton `U_eL`-freedom construction (this workshop, as the method analog).
4. **Effort**: ~1 agent, MEDIUM (re-run the S111 texture fit with a `U_dL`-freedom scan).

### Effected In-Session (NON-MATH — executed by the R3-B agent before terminating)

- [x] **§VII.CK D4-disposition lepton-PMNS annotation** (RESONANT-CONDITIONAL ~2.9× → WALLED-AS-UNDER-DETERMINED) — **specified + routed to housekeeping §A** (NOT bulk-edited; §VII.CK is mack-cosmic-bridge's sole-writer domain). The lepton shape-leg status is a JOINT W2-2 (this workshop) × W2-3 (`S116-W2-LEPTON-PMNS-TEXTURE`) reading that lands at §6 synthesis via mack's designated-writer patch. — `sessions/session-116/session-116-housekeeping.md §A` (item A2) — precise current→corrected text targets registry line 22460 (the `lepton-PMNS RESONANT-CONDITIONAL … ~2.9× from observed` phrase); workshop anchor SHA `f7190f1944db146a0ab7ff18d3c05397d423758baa63c4d9a1d48b04c1cb3204`.
- [x] **Agent memory** — workshop verdict recorded (WALLED-AS-UNDER-DETERMINED; seesaw metric real + quark-inaccessible + sufficiency-FAILED; both-sectors under-determination corollary) — `.claude/agent-memory/neutrino-detection-specialist/s116_pmns_rescue.md` (new) + MEMORY.md pointer + `s116_lepton_pmns_texture.md` workshop-landed cross-link confirmed.

### Closing Line

The lepton shape leg is **WALLED-AS-UNDER-DETERMINED**: the substrate supplies a real, quark-inaccessible seesaw ruler but, at its own nearly-degenerate B-branch `M_R`, leaves the mixing reachable-not-predicted — and the same under-determination retroactively dissolves the quark `V_us` "prediction," so neither sector's mixing is derived and the live open channel is now `R = Δm²₃₂/Δm²₂₁`, not the angles.
