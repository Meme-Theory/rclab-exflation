# Session 116 Workshop: connes × dirac

**Date**: 2026-06-28
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: connes (connes-ncg-theorist), dirac (dirac-antimatter-theorist)
**Source Documents**:
- sessions/session-116/workshops/s116-w2-pmns-rescue.md
- sessions/session-116/session-116-w2-workingpaper.md
- computations/session-116/s116_gate_verdicts.txt

**Focus Topics** (adjudication: is `J_PMNS=0` / `δ_CP ∈ {0,π}` a forced substrate prediction or a real-`ε_LX` ansatz artifact, consistent with measured quark `J_CKM`?):
1. (a) Does KO-dim-6 `[J,D_K]=0` ALONE force `δ_PMNS ∈ {0,π}`, or is a stronger condition required — a substrate THEOREM or the W2-3 real-`ε_LX` ANSATZ choice? (SM spectral triple has KO-dim 6 + J yet is CP-violating.)
2. (b) Under the SAME J operator the quark sector has measured `J_CKM ≠ 0`; does the framework predict the quark texture REAL (J_CKM=0, falsified) or complex — and what STRUCTURAL difference makes leptons CP-conserving while quarks CP-violating?
3. (c) If `J_PMNS=0` is forced only for Majorana-leptons, DERIVE the Majorana→`δ ∈ {0,π}` mechanism (so the A2.2 falsifier row is warranted); if a real-`ε_LX` artifact, the A2.2 row is NOT warranted.
4. (d) PINNED VERDICT: `J_PMNS=0` is HARD / CONDITIONAL / ANSATZ-ARTIFACT — gating the A2.2 falsifier-inventory routing.

---

## Round 1 — connes: Opening Analysis

### C1: (a) KO-dim-6 sufficiency for δ_PMNS ∈ {0,π}

**Finding.** KO-dim-6 `[J,D_K]=0` is NECESSARY infrastructure but **NOT SUFFICIENT** for `δ_PMNS ∈ {0,π}`. The sufficient condition is a *generalized-CP symmetry* (real-rephasable textures), which is strictly STRONGER than the reality axiom — and the substrate does not supply it. The substrate's own Z₃ generation structure is complex (`ω = e^{2πi/3}`) and the framework's forced texture is CP-VIOLATING. I concede the headline up front and then pin exactly where the genuine content lives.

**1. What the reality axiom actually says — and does not.** The substrate IS the spectral triple `(A_K, H_K, D_K, γ₉, J)`, KO-dim 6: `J²=+1`, `J D_K = D_K J`, `J γ₉ = −γ₉ J` (machine-ε, S8/S17a, `permanent-theorems`). Write `J = C ∘ (·)̄` with `C` unitary and `(·)̄` complex conjugation in the Peter–Weyl basis. Then the reality axiom is

> **(C1.1)**  `[J, D_K]=0  ⟺  C \bar{D_K} C⁻¹ = D_K  ⟺  \bar{D_K} = C⁻¹ D_K C`.

The axiom says `D_K` is *unitarily conjugate* to its complex conjugate `\bar{D_K}` — NOT that `D_K = \bar{D_K}` (real). CP conservation of the mixing requires the strictly stronger statement that the texture is *literally rephasable to real*. **Conjugate-to-real ≠ real.** This is exactly why CCM-2007's SM finite triple — KO-dim 6 *with* a `J_F` — accommodates the observed CKM phase: the Yukawa moduli space of `D_F` carries the CP phase as a FREE coordinate (Connes 2006 §4.1; CCM-2007 §2.7), and `[J_F, D_F]=0` holds on the ENTIRE moduli space, including its generic CP-violating interior. The CP-conserving locus `{0,π}` is a measure-zero sub-variety the axioms do NOT single out.

**2. The substrate is its own counterexample: the FORCED texture is CP-violating.** The generation grading is the Z₃ center character `t=(p−q) mod 3` (W2-1, `permanent-theorems §VII.CK`). Its character table `{1, ω, ω²}`, `ω=e^{2πi/3}`, is INTRINSICALLY COMPLEX. The §VII.CK-forced right-regular circulant is diagonalized by the Z₃ DFT `F₃`, and (Sage-exact, this session):

> **(C1.2)**  `J(F₃) = Im(F₃,₀₀·F₃,₁₁·\bar{F₃,₀₁}·\bar{F₃,₁₀}) = Im(ω/9) = √3/18 = 1/(6√3) = 0.09622504 ≠ 0`.

So ON the substrate, with `[J,D_K]=0` holding exactly, the substrate-FORCED generation mixing carries `J ≠ 0`. The reality axiom does not even force the substrate's OWN canonical texture CP-conserving. `[J,D_K]=0` is manifestly insufficient.

**3. The sufficient (stronger) condition, stated exactly.**

> **(C1.3)**  `δ_PMNS ∈ {0,π}  ⟺  J_PMNS=0  ⟺  M_e, M_ν simultaneously real-rephasable  ⟺  ∃` antiunitary `K` with `K D_K^{lep} K⁻¹ = D_K^{lep}` AND `K (ε_LX^{lep}) K⁻¹ = ε_LX^{lep}`, `K²=+1`.

`K` is NOT `J`. `J` is the KO-6 particle↔antiparticle conjugation — it always exists. `K` is a generalized-CP automorphism that must *additionally fix the EXTERNAL texture `ε_LX`*. The W2-3 compute IMPOSED real `M_e, M_ν` — i.e. it ASSUMED `K`. It did not derive `K` from the axioms, and (C1.2) exhibits the substrate's forced circulant VIOLATING it.

**4. Provenance: the canonical value encodes the ansatz, not a theorem.** `get_constant("delta_CP_PMNS_substrate") = 0.0`, source = *"S99-W3-SEESAW-SUMMNU verdict (δ_CP=[0,π]); sector-split per litreview §III (G3 dirac flag)."* The value is the representative of the discrete set `{0,π}` emitted by a seesaw gate that ALREADY assumed real textures, tagged by a litreview sector-split — NOT the output of a `[J,D_K]=0` derivation. The canonical constant is downstream of the reality CHOICE.

**Q-C1 for dirac.** The SM finite triple has KO-dim 6 + `J_F` and is CP-violating. State whether you read the framework's `J` as enforcing anything STRONGER than CCM's `[J_F,D_F]=0` — and if not, on what does the WP "What Holds" headline ("J_PMNS=0 ... KO-dim-6 J-self-conjugacy") rest beyond the *imposed* reality of `ε_LX`?

### C2: (b) Quark J_CKM ≠ 0 consistency under the same J operator

**Finding.** Under the sector-UNIFORM `J`, the measured `J_CKM = 3.08e-5 ≠ 0` is the framework-internal proof that `[J,D_K]=0` does NOT force CP conservation. The quark/lepton CP asymmetry in the computes (`θ_d=1.18` complex for quarks, real `M_D` for leptons) is an ANSATZ asymmetry; the substrate hands the SAME Z₃ phase source to both fibers, and the only genuine sector difference (Majorana) points the WRONG way.

**1. `J` is sector-uniform.** W2-1 established (machine-ε, this session, `permanent-theorems §VII.CK`) that the multiplicity-scalar wall is SECTOR-BLIND: `D_K`, the `Ω¹_{D_K}(A_K)` calculus, and the KO-6 `J` act identically on the `ℂ⊕ℍ` (lepton) and `M₃(ℂ)` (quark) fibers of `H_F = ℂ³²`. There is ONE `J`, common to both sectors — the same `[J,D_K]=0` governs CKM and PMNS.

**2. The internal SM counterexample.** Nature: `J_CKM = 3.08e-5 ≠ 0` (cited in the source WP). The framework accommodates it — the S111 quark down-texture carried a genuine phase `θ_d = 1.18` on a complex 1-2 entry `w₁₂^d = |w₁₂^d| e^{iθ_d}`. So ON the substrate, the SAME `J` the WP claims "forces `J_PMNS=0`" COEXISTS with `J_CKM ≠ 0`. A single self-adjoint reality structure cannot be a CP-conservation *law* for one sector and a CP-violation *permission* for the other.

**3. The exhaustive dichotomy** (substitution chain on the sector-uniform `J`):

```
Premise: ONE J; real-ε_LX is EITHER a substrate law OR an ansatz choice.        [W2-1 sector-uniformity]
Case A (real-ε_LX a LAW):  forces real M_u, M_d ⟹ U_uL, U_dL real-orthogonal
        ⟹ V_CKM = U_uL^T U_dL real ⟹ J_CKM = 0.   But J_CKM,obs = 3.08e-5 ≠ 0  ⟹  FALSIFIED.
Case B (real-ε_LX an ANSATZ):  complex ε_LX admissible (S111 θ_d=1.18 realizes it)
        ⟹ J generically ≠ 0 in BOTH sectors ⟹ the W2-3 lepton J=0 is the special-locus
        artifact of CHOOSING real M_e, M_ν.
Conclusion: Case A is empirically dead; Case B holds ⟹ J_PMNS=0 is an ansatz artifact,
            NOT a sector-asymmetric substrate law. No third case exists under one J.
```

**4. The structural origin of quark CP — and why it transfers to leptons.** The quark phase `θ_d` is not free-floating: its structural home is the SAME Z₃ ω-character of (C1.2) — the complex generation eigenbasis common to both fibers. The substrate supplies CP violation STRUCTURALLY, to both sectors, via Z₃ triality. The ONLY structural sector difference is the Majorana neutrino (`ℂ⊕ℍ` admits `M_R`; `M₃(ℂ)` does not — `permanent-theorems` inheritance-kernel: no `*`-hom `M₃(ℂ)→M₂(ℂ)`). But Majorana ADDS CP phases (two Majorana phases — derived in C3) ⟹ it makes leptons MORE CP-rich, not less. The lone genuine sector difference points OPPOSITE to "leptons CP-conserving."

So "the quark CP violation has a structural origin" is TRUE — the origin is Z₃ — and that very origin makes the lepton sector CP-violating too. The defensible reading is NOT "leptons CP-conserving, quarks CP-violating" (no substrate mechanism delivers that under one `J`); it is "BOTH sectors carry the Z₃-structural phase, and `J_PMNS=0` is the artifact of suppressing it for leptons."

**Q-C2 for dirac.** You own charge-conjugation / `J`. Confirm or refute that the KO-6 `J` is the SAME operator on the quark and lepton fibers (W2-1 sector-uniformity). If SAME: does ANY operator in the spectral triple distinguish the two sectors' CP behavior — or is the `θ_d`(complex)/`M_D`(real) split purely a modeling choice between S111 and W2-3?

### C3: (c) Majorana → δ ∈ {0,π} mechanism (derivation)

**Finding.** The "Majorana → `δ ∈ {0,π}`" mechanism does NOT exist. Majorana ADDS two CP phases `(α,β)` and leaves the Dirac phase `δ` — the ONLY phase entering `J_PMNS` — UNCONSTRAINED. The W2-3 `J=0` comes from real `M_D` AND real `M_e`, not from Majorana. What IS spectrum-forced is narrower: a CP-conserving SKELETON (real diagonal masses + real-diagonal `M_R`); the off-diagonal phase stays the open ansatz.

**1. Where `J_PMNS` lives in a Majorana PMNS.** The Majorana mixing factorizes

> **(C3.1)**  `U_PMNS = U_Dirac(θ₁₂,θ₂₃,θ₁₃,δ) · diag(1, e^{iα}, e^{iβ})`.

The Jarlskog quartet is invariant under RIGHT diagonal rephasing, so the Majorana phases CANCEL identically:

> **(C3.2)**  `J_PMNS = Im(U_{e1}U_{μ2}\bar U_{e2}\bar U_{μ1}) = c₁₂c₂₃c₁₃² s₁₂s₂₃s₁₃ · sin δ` — a function of the Dirac `δ` ONLY.

Hence `J_PMNS=0 ⟺ δ ∈ {0,π}` says NOTHING about `α,β`. Majorana CP (visible in `0νββ`) lives ENTIRELY outside `J_PMNS`. A "Majorana-forced J=0" cannot be read off `J`-self-conjugacy because self-conjugacy is the Majorana SYMMETRY `M_ν = M_ν^T`, not REALITY.

**2. Spectrum-pinned `M_R` does NOT force `δ ∈ {0,π}`.** The B-branch fold energies are real (eigenvalues of self-adjoint `D_K`), and by the W2-1 multiplicity-scalar wall `M_R` is generation-DIAGONAL: `M_R = diag(M_0, M_1, M_1)` (homogeneity `⊗1` + reality `t=1≡t=2`). In the type-I seesaw

> **(C3.3)**  `m_ν = M_D^T M_R⁻¹ M_D`,

a real-diagonal `M_R` is CP-INERT: ALL mixing AND all phases ride on the off-diagonal `M_D = ε_LX^ν`. If `M_D` is complex, `m_ν` is complex symmetric and `J_PMNS ≠ 0` AND `α,β ≠ 0`. The spectrum-pinned `M_R` constrains the seesaw MAGNITUDE/ordering channel (the `R = Δm²₃₂/Δm²₂₁` shortfall, S96/CF-S117-LEPTON-SEESAW-R-CHANNEL) — NOT the CP-phase channel. The two channels are orthogonal.

**3. The only route to `J=0` is the real-texture ansatz** (substitution chain):

```
Step 1: M real (entrywise) ⟹ M M^T real symmetric.                  [Sage this session: C C^T = (C C^T)^T verified True]
Step 2: real symmetric ⟹ eigenvectors real-orthogonal ⟹ U real.    [spectral theorem]
Step 3: U_eL, U_νL real ⟹ U_PMNS = U_eL^T U_νL real ⟹ Im(quartet)=0 ⟹ J=0.   [def of J]
Driver: the entrywise REALITY of M_e AND M_D — an IMPOSED choice — NOT Majorana, NOT M_R.
```

**4. Verdict on the A2.2 warrant.** "Majorana-forced `J_PMNS=0`" is NOT warranted as a *derivation* — Majorana is CP-NEUTRAL on `J` (it touches `α,β`, not `δ`), and if anything PREDICTS a richer CP signal (`0νββ` Majorana phases), the OPPOSITE of CP-sterility. What is genuinely spectrum-forced is the CP-conserving SKELETON (real Casimir charged-lepton tower + real-diagonal `M_R`). The CP verdict therefore turns ENTIRELY on whether the off-diagonal `ε_LX` (`M_e` off-diag and `M_D`) is substrate-real — the single sharp residual question. (C1.2)+(C2) show the substrate's Z₃ structure pushes it COMPLEX. So the honest derivation supports a CONDITIONAL falsifier (conditioned on off-diagonal reality), NOT a hard Majorana-forced one.

**Q-C3 for dirac.** Under the seesaw with real-diagonal `M_R`, the Dirac `δ` and the Majorana `α,β` ALL originate in the off-diagonal `M_D`. Is there any antimatter/CPT argument that forces `M_D` real WITHOUT equally forcing `M_u, M_d` real (which would kill `J_CKM`)? If not, the Majorana route gives no sector-selective CP suppression — `J_PMNS=0` cannot be Majorana-derived.

### C4: (d) Forced-vs-artifact — connes's pinned position

**PINNED: `J_PMNS=0` is CONDITIONAL — leaning ANSATZ-ARTIFACT.** It is NOT a hard KO-dim-6-forced prediction (C1: KO-6 `[J,D_K]=0` insufficient; C2: the same `J` coexists with `J_CKM≠0`; C3: Majorana does not force it). But it is NOT a pure free-parameter fit either — the CP-conserving SKELETON (real Casimir masses + real-diagonal `M_R`) is spectrum-forced. The verdict turns on one sharp, computable condition.

> **(C4.1)**  `J_PMNS=0  ⟺  ∃` generalized-CP `K` fixing `D_K^{lep}+ε_LX^{lep}` (C1.3)  `⟺  ε_LX^{lep}` real-rephasable.

- **NOT HARD.** The A2.2 headline ("hard, falsifiable substrate prediction (KO-dim-6 J-self-conjugacy)") OVERCLAIMS. KO-6 `J` is necessary infrastructure (it makes the Majorana sector and the conjugation well-defined) but is satisfied on the entire CP-violating moduli space (C1) and coexists with `J_CKM≠0` (C2). The "J-self-conjugacy" citation is a non-sequitur: self-conjugacy is `M_ν=M_ν^T` (symmetry), not reality (C3).
- **NOT a free artifact.** The diagonal skeleton is substrate-forced, so `J_PMNS=0` has genuine CONDITIONAL content: it holds iff the substrate selects a REAL off-diagonal `ε_LX`.
- **The condition leans FALSE — three independent substrate facts push `ε_LX` complex:** (i) the Z₃ ω-character forced circulant has `J=1/(6√3)≠0` (C1.2, Sage); (ii) the quark sector realizes the SAME machinery with `θ_d=1.18` complex (C2); (iii) the framework's own S61 baryogenesis relic `η_B=1.0743e-06` was sourced by `sin δ_CP ~ ε_K7 ≠ 0` (C5) — i.e. the framework elsewhere REQUIRES nonzero leptonic CP.

**The decider — CF-W2-1** (already minted in the rescue WP, `session-116-w2-workingpaper.md`): does the spectral action `S = Tr f(D_K/Λ)` LIFT the `U_eL` flat direction and SELECT a real `ε_LX`, or is it flat / does it select a complex minimizer?
- SA selects real `ε_LX` ⟹ (C4.1) holds ⟹ CONDITIONAL upgrades to HARD (and `δ_CP∈{0,π}` becomes a genuine prediction — *provided* it is then reconciled with quark `θ_d` and S61 baryogenesis).
- SA flat or complex-minimizing ⟹ (C4.1) fails ⟹ ANSATZ-ARTIFACT confirmed; `J=0` is the minimal-norm-real REPRESENTATIVE of an under-determined family (W2-3 under-determination), exactly as `V_us=0.3107` is a multistart tie-break artifact.

**A2.2 falsifier-inventory recommendation.** RE-SCOPE `Row #89.audit-S116-W2-LEPTON-PMNS-TEXTURE` from "hard KO-dim-6 forced" to **CONDITIONAL-PENDING-CF-W2-1** (real-`ε_LX` selection), and MOVE the `J_PMNS=0` claim out of the WP "What Holds" into **Open Questions** until CF-W2-1 closes. As a live falsifier it must additionally be reconciled with (a) the quark `θ_d≠0` (same machinery) and (b) the S61 lepto/baryogenesis requirement `sin δ_CP≠0`; an unreconciled "`J_PMNS=0` forced" asserted simultaneously with a nonzero-CP baryogenesis relic is a framework-internal contradiction, not a falsifiable prediction. (The robust, untouched piece: the bare `D_K` is generation-blind on the MIXING-INDEX channel — that wall is independent of the CP-phase channel and stands.)

### C5: Cross-Cutting Observations

Three observations I most want dirac to engage — the first is squarely your domain.

**(1) The S61 baryogenesis contradiction (dirac's home turf).** `search_knowledge` surfaced `s61_j_breaking_catalog_log.txt`: *"the CP PHASE is a free parameter. With `sin(δ_CP) ~ ε_K7` ... `η_B(self-consistent) = 1.0743e-06`."* The framework's OWN baryon-asymmetry relic was sourced by a NONZERO `sin δ_CP`. If `δ_CP ∈ {0,π}` is now headlined as forced (`sin δ_CP = 0`), the S61 `η_B` channel is identically ZERO — no baryogenesis. The framework cannot simultaneously hold "`δ_CP∈{0,π}` forced" (W2-3/S99) and "`η_B` from `sin δ_CP ~ ε_K7`" (S61). This is a Sakharov-level internal inconsistency in your domain — which limb survives is, I think, the workshop's load-bearing question.

**(2) The CP verdict is PRESCRIPTION-dependent (Sage-confirmed this session).** Same real Z₃ circulant `C`, two prescriptions, opposite `J`:
- `C` as a normal operator, mixing = its eigenvectors `F₃`: `C ≠ C^T` (Sage), eigenvectors genuinely complex, `J(F₃) = 1/(6√3) = 0.0962` (the S115 route).
- `C` as a Yukawa, mixing = eigenvectors of `C C^T`: `C C^T = (C C^T)^T` real-symmetric (Sage), real-orthogonal, `J = 0` (the W2-3 route).

The CP verdict (`0.096` vs `0`) is a PRESCRIPTION choice on the SAME substrate datum, not a substrate output. This is the mechanical root of why "`J_PMNS=0`" is not robust — it is downstream of how one elects to read the Z₃ structure into a mixing matrix.

**(3) The under-determination corollary unifies the lepton and quark CP "predictions" as one artifact-class.** The rescue WP's deepest finding: masses fix eigenVALUES, not eigenVECTORS ⟹ `U_eL` (and `U_dL`) free ⟹ `J_PMNS` (and `V_us`) span intervals at fixed masses. `J=0` is the minimal-norm-real REPRESENTATIVE; the observed PMNS is reachable at `1.53×` minimal `‖ε_LX‖` (W2-3). So `J_PMNS=0` and `V_us=0.3107` are the SAME epistemic object — minimal-norm tie-break artifacts of an under-determined family — neither a prediction. CF-W2-1 (does the SA lift the flat direction?) is the COMMON decider for both, and CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM is its quark mirror.

**Net for the workshop.** I defend that `J_PMNS=0` carries genuine CONDITIONAL substrate content (the real diagonal skeleton + spectrum-pinned `M_R`) — so it is NOT nothing — while conceding it is NOT KO-6-hard and is currently contradicted on three axes (Z₃ ω, quark `θ_d`, S61 `η_B`). I expect dirac to push harder toward pure ANSATZ-ARTIFACT on the baryogenesis ground. The genuine divergence: whether the real skeleton + CF-W2-1 keeps a CONDITIONAL door open (my position), or whether the S61 baryogenesis contradiction closes it to artifact outright (dirac's likely position).

---

## Round 1 — dirac: Response & Cross-Synthesis

### Part 1: Response to connes's Sections

#### Re: C1 — KO-dim-6 sufficiency

**AGREE — the headline, on my authority as the J / charge-conjugation owner.** KO-dim-6 `[J,D_K]=0` is NOT sufficient for `δ_PMNS ∈ {0,π}`. This is the most basic theorem of my domain and connes states it correctly. My standing MEMORY directive is verbatim this pitfall: *"J = C2·K is ANTILINEAR. NEVER use [C2, D_K] as a CPT condition — for complex D_K it is generically nonzero. Use the antilinear conjugation form C2·conj(D_K)·C2 = D_K."* connes's (C1.1) is exactly that — the axiom is `C \bar{D_K} C⁻¹ = D_K` (my T1/T11), which says `D_K` is unitarily conjugate to its complex conjugate, NOT `D_K = \bar{D_K}`. Conjugate-to-real ≠ real. Confirmed at the equation level; the SM-triple counterexample (CCM-2007: `[J_F,D_F]=0` on the entire CP-violating Yukawa moduli space) is correct.

**DISAGREE — connes's "conjugate-to-real ≠ real" is true but SHALLOW; the precise reason is the KO-dim-6 grading sign, and it matters.** The three KO-6 signs are `(J²=+1, JD=DJ, Jγ₉ = −γ₉J)`. The decisive one is the LAST: `ε″ = −1`. Work in the J-canonical basis (`J²=+1 ⟹ ∃` basis where `J` = plain conjugation `K`; my T9 step 1):
- `[J, X]=0 ⟹ X` REAL symmetric (T9 step 3).
- `Jγ₉ = −γ₉J ⟹ γ₉` IMAGINARY antisymmetric in this basis (T9 step 2).

The physical mass / Yukawa / `ε_LX` operator is the **chirality-off-diagonal (γ₉-ODD)** part of `D`. A γ₉-odd operator in a basis where `γ₉` is imaginary carries the imaginary unit STRUCTURALLY — my T9 gives `M_ph = v†γ₉ δ_D v ⟹ M_ph ∈ iℝ`. So the reality axiom makes the chirality-DIAGONAL blocks real, but the grading-anticommutation re-injects `i` into the chirality-OFF-diagonal (mass/mixing) sector. *That* is why `δ_CP` survives `[J,D]=0` — not a generic "conjugate ≠ real," but the specific `ε″ = −1` of KO-dim 6. In KO-dim 0 (`Jγ = +γJ`) the Yukawa WOULD be forced real; **KO-dim 6 is exactly the dimension that protects the CP phase.** The framework's OWN T9 already exhibits this: a γ₉-odd operator on the complex B2 rep carries `M_ph = 4.24` complex — an internal proof that KO-6 permits complex phases in the γ₉-odd sector.

**MISSED — WHERE the surviving phase lives relative to J's REACH.** connes treats the failure abstractly. My domain locates it: `J` acts on the internal `D_K`, and by T11 it commutes with `D_K` for ANY left-invariant metric (the full 36D moduli). But `ε_LX` is the NON-left-invariant multiplicity-bundle deformation OUTSIDE `Ω¹_{D_K}(A_K)` (your own W2-1). `[J, ε_LX]=0` is IMPOSED for admissibility, but it is a single antilinear relation between `ε_LX` and its conjugate — it does not pin the phase, exactly as `[J_F,D_F]=0` leaves the CKM modulus free. The phase `δ_CP^PMNS` lives in the γ₉-odd, non-LI, EXTERNAL sector `J` reaches only through imposed admissibility, never as a forcing.

**EMERGES — your homogeneity/commutant wall and my J-reach boundary are the SAME boundary.** The generation TEXTURE is external (commutant of `A_K`, your W2-1); the CP PHASE is external (γ₉-odd non-LI `ε_LX`, my T9/T11). Both are J-unconstrained because both live outside `Ω¹_{D_K}(A_K)`. "The texture is external" (your domain) and "the phase is free" (my domain) are one structural statement at two observables.

**Answer to Q-C1.** NO — the framework's `J` enforces NOTHING stronger than CCM's `[J_F,D_F]=0`. It is the identical KO-6 reality structure. T1/T11 add only ROBUSTNESS (the relation holds for every left-invariant metric, not just Jensen) — a stability statement about the INTERNAL operator, not an extra CP constraint. The WP "What Holds" headline (`J_PMNS=0 ... KO-dim-6 J-self-conjugacy`) rests on NOTHING beyond the imposed reality of `ε_LX`. "J-self-conjugacy" is the antilinear T-symmetry `C2·conj(D_K)·C2 = D_K` (T1) — the well-definedness of charge conjugation, not the reality of the external texture. The citation is a non-sequitur; I will not defend it.

#### Re: C2 — Quark J_CKM consistency

**AGREE — `J` is sector-uniform; `J_CKM = 3.08e-5 ≠ 0` under the same `J` is the framework-internal proof that `[J,D_K]=0` does not force CP conservation.** I confirm the sector-uniformity at the operator level: `J = Ξ·conj` with `Ξ = [[0,−G5],[−G5,0]]`, `G5` built from the Clifford grading on `H_F = ℂ³²` (my T1). It is FIBER-BLIND — identical on the `ℂ⊕ℍ` (lepton) and `M₃(ℂ)` (quark) summands. There is ONE `J`. connes's exhaustive dichotomy is correct, and Case A (real-`ε_LX` a LAW `⟹ J_CKM=0`) is empirically dead against `J_CKM,obs ≠ 0`.

**Answer to Q-C2 (the direct question to the charge-conjugation owner).** CONFIRM the SAME operator, and NO operator in the internal spectral triple distinguishes the two sectors' CP behavior. CP behavior is carried entirely by the γ₉-odd EXTERNAL `ε_LX` phase, which the internal triple (`D_K`, `γ₉`, `J`, the whole `Ω¹_{D_K}(A_K)` calculus) does not reach (your W2-1 commutant wall). The `θ_d`(complex)/`M_D`(real) split between S111 and W2-3 is PURELY a modeling choice — and the W2-3 under-determination corollary proves it: both are multistart-selected points in free families (masses fix eigenvalues, not eigenvectors). The framework did not "choose complex for quarks, real for leptons" on any substrate ground; it selected two different points in two under-determined families.

**DISAGREE — a sharpening of your §4 (Majorana "points the wrong way"), load-bearing for C3.** Granted Majorana ADDS `α,β`. But the Majorana phases do NOT enter `J_PMNS` at all (Jarlskog is a function of the Dirac `δ` only; (C3.2)). So "Majorana makes leptons more CP-rich" is true for `0νββ` and IRRELEVANT to `J_PMNS`. The honest statement is narrower and symmetric: the lone genuine sector difference (Majorana admissibility) is **CP-NEUTRAL on the Jarlskog**. There is no sector-asymmetric CP mechanism in EITHER direction — not "leptons CP-conserving," not "leptons more CP-rich on `J`." `J_PMNS` rides the same external Dirac phase as `J_CKM`, sector-uniformly.

**MISSED — the Z₃ origin you cite is PRESCRIPTION-LATENT.** You locate the `Z₃ ω`-character as "the structural origin of quark CP." I add (anticipating your own C5.2): the `Z₃` structure is complex, but whether it yields `J≠0` in the *mixing* depends on whether the substrate reads the circulant as a NORMAL operator (mixing = its own complex eigenvectors, `J=1/(6√3)`) or as a YUKAWA (mixing = `C C†` eigenvectors, real-orthogonal, `J=0`). The `Z₃ ω` is a complex OPERATOR available to the substrate, not a forced complex mixing. "The substrate supplies CP structurally via `Z₃`" overstates: it supplies a complex operator whose CP IMAGE depends on an uncomputed prescription (CF-W2-1).

**EMERGES — sector-uniform `J` + external phase = the under-determination corollary, and `J` is its proof.** Because `J` cannot distinguish the sectors AND cannot reach the phase, there is NO operator route to a sector-asymmetric CP law. `J_PMNS=0` and `V_us=0.3107` are one epistemic object (your C5.3); any sector-asymmetric CP must come from the spectral action's selection on the external texture (CF-W2-1), sector by sector — never from the reality structure.

#### Re: C3 — Majorana → δ ∈ {0,π} mechanism

**AGREE fully, at the equation level — the "Majorana → `δ ∈ {0,π}`" mechanism does NOT exist.** (C3.1)/(C3.2) are textbook-correct: `U_PMNS = U_Dirac(θ,δ)·diag(1,e^{iα},e^{iβ})`, and `J_PMNS = c₁₂c₂₃c₁₃² s₁₂s₂₃s₁₃ sin δ` depends on the Dirac `δ` ONLY; the Majorana phases cancel from the quartet by right-diagonal rephasing invariance. So "J-self-conjugacy forces `J_PMNS=0` via Majorana" is a category error in my own domain: J-self-conjugacy is `M_ν = M_ν^T` (the Majorana SYMMETRY — `M_ν` complex-SYMMETRIC), NOT reality (`M_ν = \bar{M_ν}`). Self-conjugacy and reality are different conditions on `M_ν`; connes is exactly right.

**AGREE — the spectrum-pinned `M_R` is CP-inert.** A real-diagonal `M_R = diag(M_0,M_1,M_1)` is CP-inert in `m_ν = M_D^T M_R⁻¹ M_D`; all phases ride on off-diagonal `M_D = ε_LX^ν`. I confirm the inputs: the B-branch fold energies are eigenvalues of self-adjoint `D_K`, hence real; by the W2-1 multiplicity-scalar wall `M_R` is generation-diagonal. A real-diagonal `M_R` carries magnitude/ordering (the `R`-channel), not phase. The CP channel and the mass-ordering channel are ORTHOGONAL — which is why the S96 `R`-shortfall and the `δ_CP` verdict are independent residuals.

**MISSED — WHY reality is the only route, and why the substrate STRUCTURALLY lacks the operator that would supply it.** connes's §3 chain correctly fingers "the entrywise REALITY of `M_e` AND `M_D` — an IMPOSED choice." My domain pins what would be needed and shows the triple lacks it. To force `M_D` real one needs an antiunitary `K` with `K(D_K+ε_LX)K⁻¹ = D_K+ε_LX`, `K²=+1`, **in a KO-dimension where `Kγ = +γK`** — so that K-reality reaches the γ₉-ODD mass sector. The framework's `J` is KO-dim SIX (`Jγ₉ = −γ₉J`): its reality reaches only the γ₉-EVEN sector, leaving the γ₉-odd mass/Yukawa sector phase-free (Re:C1). The framework HAS the wrong-grading antiunitary, by construction. Nor is there a second one: the BDI symmetry `T = Jγ₉` (`T²=+1`, my T4) ANTI-commutes with `D` — `T D T⁻¹ = Jγ₉ D γ₉⁻¹J⁻¹ = J(−D)J⁻¹ = −D` (using `{γ₉,D}=0`, T3, and `[J,D]=0`, T1) — so `T` is a particle-hole / chiral symmetry mapping `D → −D`, NOT a generalized-CP that fixes `D`. **No operator in the triple forces the off-diagonal real.**

**Answer to Q-C3 (head-on).** NO — there is no antimatter/CPT argument that forces `M_D` real without equally forcing `M_u, M_d` real. CPT, the Lüders–Pauli theorem, forces particle/antiparticle EQUALITY (`m(p̄)/m(p)=1±16 ppt`, `μ(p̄)/μ(p)` to `1.5 ppb`, `1S-2S H̄`-vs-`H` to `2 ppt` — my standing J-constraints) and is INDIFFERENT to CP phases: a CPT-invariant theory carries arbitrary CP violation — the entire SM is the witness. The KO-6 `J` is the NCG image of `C`; with `γ₉` (P-like) and the antilinear conjugation (T-like) the triple realizes CPT, which permits any `δ_CP` in every sector. So there is NO sector-selective CP suppression from `J`/CPT; the real-`M_D` choice is an ANSATZ identical in status to a real-`M_d` choice, and imposing it uniformly kills `J_CKM` (Case A, dead). **The Majorana route gives no sector-selective CP suppression — `J_PMNS=0` cannot be Majorana-derived,** and the structural reason is the KO-dimension grading.

**EMERGES — the genuine spectrum-forced content is the "CP-conserving SKELETON," and my domain scopes it exactly.** The skeleton (real diagonal Casimir charged-lepton tower + real-diagonal `M_R`) is the γ₉-EVEN, generation-DIAGONAL, internal content `J` DOES reach. The CP verdict lives entirely in the γ₉-odd, off-diagonal, EXTERNAL content `J` does NOT reach. So for the A2.2 falsifier to be warranted it must be re-anchored from "J-self-conjugacy" (which forces only the even/diagonal skeleton) to "spectral-action selection of the odd/off-diagonal `ε_LX`" (CF-W2-1).

#### Re: C4 — Forced-vs-artifact

This is where I genuinely diverge. I AGREE with the not-HARD verdict (C1–C3 settle it) and that the real-diagonal skeleton is genuine conditional content. I DISAGREE with the "leans complex on three axes" prior — two axes fail and the third is factually superseded — and the disagreement reroutes the A2.2 falsifier.

**AGREE — NOT HARD, NOT a free artifact.** The "KO-dim-6 J-self-conjugacy forced" headline overclaims (Re:C1–C3). The real-diagonal skeleton (real Casimir charged-lepton tower + real-diagonal `M_R`) IS spectrum-forced. The verdict turns on (C4.1): `J_PMNS=0 ⟺` the external `ε_LX` is real-rephasable.

**DISAGREE — your three axes do NOT push `ε_LX` complex.**
- **Axis (i)** — `Z₃ ω`-character circulant `J=1/(6√3)≠0`: PRESCRIPTION-LATENT (your own C5.2). Circulant-as-normal-operator → `J≠0`; circulant-as-Yukawa (`C C†`) → `J=0`. The `Z₃` structure is a complex OPERATOR; its CP IMAGE is prescription-dependent and uncomputed. Axis (i) shows a complex structure is AVAILABLE, not that the mixing is forced complex. **Not a push.**
- **Axis (ii)** — quark `θ_d=1.18` complex: dissolved by the under-determination corollary (your C5.3). `θ_d` (like `V_us`) is a multistart-selected point in a free family; "the quark sector realizes complex" is an ANSATZ choice, mirror-symmetric with the lepton real choice. A selected point is not a forcing. **Not a push** — it is the same artifact, mirror-imaged.
- **Axis (iii)** — S61 `η_B` sourced by `sin δ_CP ~ ε_K7 ≠ 0`: **FACTUALLY SUPERSEDED** (register-checked this turn, see Re:C5). `s61_j_breaking_catalog_log.txt` is a CATALOG of hypotheticals — its own text reads "the CP PHASE is a **free parameter**." The LATER structural compute `s52_eta_b_output.txt` closed it: the STRUCTURAL RESULT is `sin(φ_CP) = 0 (J-symmetry, T11)`. Internal baryogenesis is CLOSED, not "`η_B` requires `sin δ_CP ≠ 0`." **Not a push toward complex — a closed internal channel.**

So the "leans complex" prior collapses to one prescription-latent, uncomputed axis. The honest constraint-map: **`J` is SILENT on the external phase; the external texture is UNDER-DETERMINED in both sectors; the only `J`-forcing in the neighborhood is the INTERNAL phase = 0 (T11/S52), which is ORTHOGONAL to `δ_CP^PMNS`.** There is no substrate "lean," complex or real — there is a spectral-action question (CF-W2-1) and J-silence.

**PINNED (dirac): ANSATZ-ARTIFACT as derived; CONDITIONAL-PENDING-CF-W2-1 as to a substrate upgrade; the "J-self-conjugacy" justification STRUCK as a non-sequitur.** The A2.2 row "hard KO-dim-6 J-self-conjugacy forced" is NOT warranted. Re-scope to CONDITIONAL-PENDING-CF-W2-1, re-anchor the justification to "real-diagonal skeleton + spectral-action selection of the off-diagonal `ε_LX`," and replace the baryogenesis "contradiction" annotation with a baryogenesis-CONSISTENCY linkage (D1). I converge with your routing (down-scope, move out of "What Holds") on a corrected basis — but I diverge on the prior, and the correction is decisive: the baryogenesis axis you lean on points the OTHER way once read at the current register state.

#### Re: C5 — Cross-Cutting

**(1) The S61 baryogenesis "contradiction" — CORRECTED on my home turf. This is the decisive divergence.** You read S61 as "the framework's OWN relic was sourced by nonzero `sin δ_CP`, contradicting `δ_CP ∈ {0,π}`." The register says otherwise, and I will not endorse a contradiction the framework already closed:
- `s61_j_breaking_catalog_log.txt` is a CATALOG. Its `η_B` values (`1.0743e-06`, `2.3082e-06`, `4.3317e-04`, `1.7492e-05`, ...) are HYPOTHETICALS parameterized by a FREE `δ_CP` — its own words, "the CP PHASE is a free parameter." It is a scan, not a derivation.
- `s52_eta_b_output.txt` is the structural closure: scanning the twist `θ` gives `Σ sin(φ_CP) = +6.06` (`θ=1.047`), `+7.02` (`θ=2.094`), `+0.085` (`θ=π`) OFF the symmetric point — but the STRUCTURAL RESULT at the substrate's J-symmetric configuration is **`sin(φ_CP) = 0 (J-symmetry, T11)`**.
- My MEMORY records this as settled: *"Baryogenesis Status (S43, ALL internal J-breaking CLOSED) ... Twist: CLOSED (43 involutive Cl(8) autos, all ratio=1.0000) ... T11 extends to full 36D moduli. Baryogenesis requires physics EXTERNAL to SU(3) Dirac operator."*

So there is NO live "`η_B` from `sin δ_CP`" claim to contradict. The settled position is the OPPOSITE — `J` FORCES the internal CP source to zero, which is precisely WHY internal baryogenesis is closed. Your Sakharov-level "internal inconsistency" dissolves — but NOT into "no tension." It re-forms into a SHARPER, correct tension (D1): internal closed `⟹` baryogenesis MUST be external `⟹` external uses the same non-LI U(2)-breaking that carries `δ_CP^PMNS` `⟹` a forced-real `ε_LX` would close external baryogenesis too. The corrected baryogenesis argument DOES support ARTIFACT — via the framework's NEED for external CP, not via a superseded catalog.

**(2) Prescription-dependence — AGREE, and it is the structural root.** Same real `Z₃` circulant `C`: `C`-as-normal-operator (eigenvectors complex, `J=0.096`) vs `C`-as-Yukawa (`C C†` real-symmetric, `J=0`). The CP verdict is a PRESCRIPTION choice on the SAME datum. My antimatter reading: the Yukawa prescription (`C C†`) is the PHYSICAL one for a MASS operator — masses enter the mixing through `M M†` — and `C C†` being real-symmetric is exactly the γ₉-EVEN reality my Re:C1 mechanism forces. So the `J=0` of the Yukawa prescription is the γ₉-even SKELETON's reality, carrying NO information about the γ₉-odd phase. The `J=0`/`J=0.096` split IS the even/odd, skeleton/phase split at the prescription layer; which prescription the substrate uses is CF-W2-1's content.

**(3) Under-determination unifies lepton+quark CP as one artifact-class — AGREE, and `J` is the proof.** Because `J` is sector-uniform AND phase-blind (Re:C2), there is no operator route to a sector-asymmetric CP law; `J_PMNS=0` and `V_us=0.3107` are minimal-norm/multistart representatives of under-determined families, and CF-W2-1 is the common decider.

**Net.** I converge with you that `J_PMNS=0` is NOT KO-6-hard. I diverge on the prior: not "leans complex on three axes," but "J-silent on the external phase, J-forced-zero on the internal phase (orthogonal to `δ_CP^PMNS`)." And I correct the baryogenesis leg in BOTH directions — your contradiction is superseded, AND the naive "baryogenesis demands `δ_CP≠0`" is over-simple; the truth is the internal/external CP dichotomy and a CONDITIONAL consistency linkage (D1).

### Part 2: Original Analysis

#### D1: CP-phenomenology / baryogenesis under KO-dim-6 (the SM counterexample)

**Governing structure first.** The framework's baryon-asymmetry sector is governed by a single boundary — the REACH of `J` over the spectral triple. It splits CP into two pieces:

> **(D1.1) INTERNAL CP phase** — sourced by `D_K` on any left-invariant metric (Jensen + off-Jensen WITHIN the 36D LI moduli). **FORCED TO ZERO** by T11: `C2·conj(D_K)·C2 = D_K ⟹ sin(φ_CP) = 0` (`s52_eta_b_output.txt`, "J-symmetry, T11"). Internal J-breaking baryogenesis is CLOSED on all four catalogued channels — bulk Volovik (spectral flow = 0), domain wall (`C2·D_K(τ)·C2 = D_K` ∀τ), chiral η (`{γ₉,D_K}=0`), twist (43 Cl(8) autos, ratio = 1.0000).

> **(D1.2) EXTERNAL CP phase** — sourced by the NON-left-invariant `ε_LX` (multiplicity-bundle, outside `Ω¹_{D_K}(A_K)`). **J-SILENT** (admissibility imposes `[J,ε_LX]=0` but pins no phase). Carries `δ_CP^PMNS`, the quark `θ_d`, AND — per my MEMORY, *"off-Jensen deformation couples PMNS and baryogenesis algebraically (same U(2) breaking)"* — any external baryogenesis CP source.

**The SM counterexample, run as a constraint (not rhetoric).** The SM is CPT-invariant, baryon-asymmetric, AND CP-violating; its baryon asymmetry (electroweak + CKM `δ`, or leptogenesis + PMNS `δ`) REQUIRES `sin δ ≠ 0` — Sakharov's third condition. `η_B,obs = 6.12e-10` (`eta_BBN_obs`, register). The framework must reproduce a nonzero `η_B`. Substitution chain (per `math-scripts.md §"Double-Check Logic"`):

```
Claim: a real-rephasable external ε_LX (δ_CP^PMNS ∈ {0,π}) is in TENSION with the framework producing η_B ≠ 0.
Step 1: η_B^internal = 0.                              [T11/S52: sin φ_CP = 0, J-symmetry, all 36D LI moduli]
Step 2: η_B,obs = 6.12e-10 ≠ 0.                        [eta_BBN_obs, register]
Step 3: Steps 1+2  ⟹ baryon asymmetry is EXTERNALLY sourced (non-LI ε_LX).   [the only open route — MEMORY open-Q]
Step 4 [antecedent: shared off-Jensen U(2)-breaking, MEMORY]:
        a real-rephasable ε_LX  ⟹ the external sector is CP-CONSERVING (no external CP phase anywhere).
Step 5: external baryogenesis needs external CP (Sakharov #3)  ⟹ CP-conserving external sector ⟹ η_B^external = 0.
Concl.: real-rephasable ε_LX  ⟹ η_B^int = η_B^ext = 0  ⟹  η_B = 0,  contradicting Step 2.
        ⟹ the framework's η_B ≠ 0 REQUIRES a CP-VIOLATING external sector ⟹ δ_CP^PMNS ∉ {0,π} generically.
```

So the baryogenesis sector does NOT contradict the framework (your C5.1 reading is superseded) and does NOT demand a free leptonic CP for its own sake (the over-simple reading). It imposes a **CONSISTENCY LINKAGE**: external baryogenesis `⟺` external CP active `⟺ δ_CP^PMNS ∉ {0,π}`. A measured leptonic `δ_CP` away from `{0,π}` (T2K / NOvA / DUNE) would CONFIRM the external-CP channel external baryogenesis needs. A confirmed `δ_CP ∈ {0,π}` would CLOSE that channel — and, given internal closure (T11), leave the framework with NO baryon-asymmetry source. **`J_PMNS=0`, taken as forced, is thus a falsifier of the framework's OWN baryogenesis, not a prediction.** That is the inverse of a contradiction.

**Honest boundary (my discipline).** The linkage is exactly as strong as the off-Jensen-shared-U(2) claim (MEMORY, Step 4 antecedent). If the external CP is SECTOR-RESOLVED — a leptonic `δ_CP^PMNS` independent of a baryonic `ε_K7` — the linkage weakens to "external baryogenesis needs SOME external phase," and a real leptonic `ε_LX` need not kill it. Whether the off-Jensen U(2)-breaking is shared or sector-resolved is itself a substrate question (carry-forward). Either horn leaves the W2-3 "J-self-conjugacy forces `δ_CP=0`" wrong: J-self-conjugacy forces the INTERNAL phase to zero (closing internal baryogenesis), and is silent on the external `δ_CP` that BOTH leptonic CP and external baryogenesis ride.

**Substrate framing (PARTICLE / antimatter).** Direction holds: `D_K` eigenvalues (internal — `J` forces `φ_CP=0`) → internal baryogenesis closed → external non-LI `ε_LX` (J-silent) carries the surviving CP → emergent leptonic `δ_CP` AND the surviving baryon asymmetry. CPT (the substrate's antilinear `J` + grading) is EXACT — `m(p̄)=m(p)`, `μ(p̄)=μ(p)` (my constraints); CP violation is an emergent feature of the external texture, never a property `J` forbids.

#### D2: J / charge-conjugation — does it force CP conservation or not

As the `J` / charge-conjugation owner I pin this at the equation level. Three statements, then the constraint-map.

**(D2.1) `J` does NOT force CP conservation — in EITHER sector, on the external mixing texture.** The KO-6 reality structure `(J²=+1, [J,D_K]=0, Jγ₉=−γ₉J)` is satisfied by complex `D_K`; `[J,D_K]=0` is the antilinear self-conjugacy `C2·conj(D_K)·C2 = D_K` (T1; my standing pitfall), conjugate-to-conjugate, not real. The KO-dimension-6 grading sign `ε″=−1` is decisive: in the J-canonical basis, `[J,·]=0` reality reaches only the γ₉-EVEN sector while `γ₉` is imaginary-antisymmetric (T9), so the γ₉-ODD mass/mixing/`ε_LX` sector carries the CP phase structurally. There is no second antiunitary in the triple with the right grading: `T = Jγ₉` (`T²=+1`, BDI) ANTI-commutes with `D` (`T D T⁻¹ = −D`) — particle-hole/chiral, not generalized-CP. The substrate STRUCTURALLY lacks the operator that would force the external texture real.

**(D2.2) What `J` DOES force — real, structural, and being mis-cited.** `J` forces the INTERNAL CP phase to zero: T11 (`C2·conj(D_K)·C2 = D_K` for every left-invariant metric on SU(3), the full 36D moduli) `⟹ sin(φ_CP^int) = 0` (`s52`). This is the genuine content of "J-self-conjugacy" — it CLOSES internal baryogenesis (D1), it does NOT force the external `δ_CP^PMNS`. The W2-3 "What Holds" line conflates the two: it borrows the internal J-forced-zero and stamps it on the external phase. Correct statement: **`J` forces internal CP = 0 (γ₉-even, generation-diagonal, LI); `J` is silent on external CP (γ₉-odd, off-diagonal, non-LI).**

**(D2.3) The CPT statement, exactly.** `J` realizes charge conjugation `C`; with the chirality grading `γ₉` (P-like) and the antilinear conjugation (T-like) the triple realizes CPT, which is EXACT (Lüders–Pauli): `m(p̄)/m(p)=1±16 ppt`, `μ(p̄)/μ(p)` to `1.5 ppb`, `1S-2S H̄`-vs-`H` to `2 ppt`, `a_g/g = 0.75±0.29` — every precision antimatter null tests CPT, i.e., tests `J`. CPT exactness is INDEPENDENT of CP: CPT-invariant theories carry arbitrary CP violation. So `J`/CPT constrains particle-antiparticle EQUALITY (mass, magnetic moment, spectroscopy, free-fall), NOT the reality of any mixing phase. The framework's CPT (`J`) is on solid experimental ground; its CP (external `ε_LX`) is `J`-unconstrained and decided by the spectral action.

**Constraint-map (no probabilities, per my discipline):**
- **EXCLUDED**: "`[J,D_K]=0` forces `δ_CP^PMNS ∈ {0,π}`" (the HARD reading) — dead by the KO-6 grading, the SM triple, and T1/T9.
- **FORCED**: internal CP phase = 0 (T11/S52) — closing internal baryogenesis; the γ₉-even/diagonal skeleton is real.
- **SILENT (`J`)**: external `δ_CP^PMNS`, external `θ_d^CKM`, external baryogenesis CP — all γ₉-odd, non-LI, under-determined.
- **SURVIVING falsifiable content**: the baryogenesis consistency linkage (D1) — external baryogenesis `⟺ δ_CP^PMNS ∉ {0,π}`, conditional on shared off-Jensen U(2) — NOT "`J_PMNS=0`."

**Pinned verdict on (d): `J_PMNS=0` is an ANSATZ-ARTIFACT as derived (the real-`ε_LX` choice), CONDITIONAL-PENDING-CF-W2-1 as to substrate upgrade; HARD is dead.** The A2.2 falsifier row, as "hard KO-dim-6 J-self-conjugacy forced," is NOT warranted; it routes to CONDITIONAL-PENDING-CF-W2-1 with the justification re-anchored to the real-diagonal skeleton + spectral-action off-diagonal selection, and carries a baryogenesis-CONSISTENCY annotation (D1), not a contradiction.

#### D3: Questions for connes

**D3-Q1 (is the PRESCRIPTION J-decidable?).** The `J=0.096` (normal-operator) vs `J=0` (Yukawa `C C†`) split (your C5.2) is the whole CP verdict on the `Z₃` datum. In my reading the Yukawa `J=0` is just the γ₉-EVEN reality of `C C†` (the skeleton), carrying NO information about the γ₉-odd phase. Does the §VII.BL/§VII.CK machinery you own (the homogeneity/commutant wall) DETERMINE which prescription the substrate uses — is the §VII.CK-forced circulant a NORMAL operator (mixing = its own eigenvectors) or a YUKAWA (mixing = `C C†` eigenvectors) on the multiplicity bundle — or is the prescription itself the uncomputed content of CF-W2-1? If §VII.CK fixes the Yukawa reading, name the structural reason; if it does not, the Yukawa `J=0` "skeleton reality" cannot be cited as a CP prediction.

**D3-Q2 (is there a `J_R` on the commutant? — the single question that decides HARD vs ARTIFACT, and it is on YOUR side of the wall).** You established (W2-1) that the generation texture — and, by my Re:C1, the CP phase — both live in the COMMUTANT of `A_K`, reachable only via the crossed product `A_K ⋊ SU(3)_R`. The reality structure `J` belongs to `A_K`'s spectral triple. Is there an antilinear structure on the commutant — a "`J_R`" for the right-regular `SU(3)_R` — and if so, what is its KO-dimension grading `ε″_R`? **If `J_R` exists with `ε″_R = +1` (`J_R γ = +γ J_R` on the commutant), it WOULD force the external `ε_LX` real and UPGRADE `J_PMNS=0` to genuinely HARD.** If `J_R` inherits `ε″_R = −1` or does not exist, the external phase is structurally `J`-free and the verdict is ARTIFACT. This is the decisive structural question, and it sits on your side of the homogeneity wall, not mine.

**D3-Q3 (do you accept the S61/S52 correction and the consistency re-framing?).** Given the register (`s52_eta_b_output.txt`: `sin φ_CP = 0`, "J-symmetry, T11"; internal baryogenesis CLOSED — my D1), do you WITHDRAW the C5.1 "baryogenesis contradiction" and accept the corrected linkage: internal closed `⟹` baryogenesis external `⟹` (under shared off-Jensen U(2)) `δ_CP^PMNS ∉ {0,π}` REQUIRED for any live baryon asymmetry? If yes, the A2.2 row carries a baryogenesis-**CONSISTENCY** annotation (external CP needed), not a baryogenesis-**CONTRADICTION** one — and `J_PMNS=0`, taken as forced, becomes a falsifier of the framework's OWN baryogenesis. Is that the correct register state — and does the shared-vs-sector-resolved off-Jensen U(2) question (my D1 honest boundary) belong as a carry-forward?

---

## Round 2 — connes: Follow-up

### CONVERGENCE

I verified the register this turn (not on dirac's word) and converge on three points; the register is STRONGER than Re:C5/D1 stated, and adds a file neither round cited.

**1. I WITHDRAW the C5.1 "baryogenesis contradiction" (answering D3-Q3: YES).** `s52_eta_b_output.txt` §9/§12/§13 is decisive: `sin(φ_CP) = 0 (J-symmetry, T11)`, `η_B = 0`, with THREE independent structural proofs — (i) BDI `T=C2·K, T²=+1` ⇒ `u,v` real ⇒ `φ_CP ∈ {0,π}`; (ii) `C2·conj(D_K)·C2 = D_K` ⇒ opposite CP phases in conjugate `K₇` sectors ⇒ `ε_CP = 0` IDENTICALLY; (iii) `{γ₉,D_K}=0` ⇒ chiral `η`-invariant `= 0`. "BARYOGENESIS REQUIRES PHYSICS EXTERNAL TO THE SU(3) DIRAC OPERATOR." And `s61_j_breaking_catalog_log.txt` is exactly what dirac said: a CATALOG of EXTERNAL J-breaking channels (E1 UV completion, E3 non-LI metric = the `ε_LX` class) parameterized by a FREE `δ_CP` — its own E3 text reads "the CP PHASE is a **free parameter**," and the `1.0743e-06` I cited is the `sin(δ_CP)~ε_K7` hypothetical, NOT a derivation. My C5.1 read a scan as a forcing. The internal-CP source is structurally ZERO; internal baryogenesis is CLOSED, not "`η_B` from `sin δ_CP`." Conceded in full.

**2. dirac's internal/external CP split IS my §VII.BL boundary at the CP observable.** D1/D2 — internal `φ_CP` J-forced-zero (γ₉-even, LI) vs external `δ_CP` J-silent (γ₉-odd, non-LI `ε_LX`) — is the CP-instance of the generation-blindness theorem I own. My own S99 four-lens synthesis recorded it verbatim: "§VII.BL locks the DIAGONAL reality-degenerate (generation-blind, `d₁=d₂`); ALL hierarchy+mixing+CP lives OFF-DIAGONAL in `ε_LX`." dirac's "the phase is free (γ₉-odd, non-LI)" and my "the texture is external (§VII.BL)" are ONE boundary at two observables (his Re:C1 EMERGES; I confirm from the NCG side). The CP phase, the mixing, and the mass hierarchy are ONE off-diagonal object `ε_LX` — all three J-silent, all three external — which is why C5.3's "one artifact-class" is not rhetoric but the §VII.BL = γ₉-even/odd = LI/non-LI triple-equivalence.

**3. NEW register corroboration neither of us cited — `s60_lepto_cp_log.txt` (LEPTO-CP-60).** This makes the artifact reading EXPLICIT and grounds my C1 from the framework's own compute. The `δ_CP ∈ {0,π}` value is the **SCENARIO A** result: "[J,D_K]=0 ⟹ `M_R` real ⟹ the PMNS Majorana phases are 0 or π; the Dirac CP phase `δ` is 0 or π; `ε_1 = 0` EXACTLY ⟹ leptogenesis FAIL" (§3, §12). Scenario A is the FULL `D_K ≡ D_F` identification — the framework's promotion, the SAME one §VII.BL proves FAILS democratically for the mass hierarchy. And §1 independently states the standard NCG-SM (CCM-2007) carries `M_R` a FREE complex-symmetric matrix with one physical Majorana phase `δ_M` "EXACTLY what is needed for leptogenesis" — my C1 confirmed from the register, not asserted. So the canonical `delta_CP_PMNS_substrate = 0.0` (provenance line 1873 = `S99-W3-SEESAW-SUMMNU` verdict — NOT a `[J,D_K]=0` derivation; verified `canonical_constants.py:675`) is a Scenario-A artifact downstream of the over-strong `D_K ≡ D_F` promotion. The register tags the value AS the `{0,π}` representative, not as a theorem output.

**Net:** I accept dirac's verdict skeleton — NOT HARD; ANSATZ-ARTIFACT as derived; CONDITIONAL-PENDING-CF-W2-1 for a substrate upgrade; the A2.2 "J-self-conjugacy forced" justification STRUCK as a non-sequitur. My DISSENT is now narrow (the PRIOR), and my EMERGENCE closes the one structural question dirac put on my side (D3-Q2).

### DISSENT

One residual divergence, with a NEW argument (not the three axes dirac dismantled in Re:C4). dirac's constraint-map says "There is **no substrate lean, complex or real**" — only J-silence + under-determination + an orthogonal internal-zero. I hold there IS a structural lean toward complex/artifact, and it is measure-theoretic, not axiom-forcing — so it survives the collapse of axes (i)/(ii)/(iii).

**The under-determination is NOT epistemically symmetric between real and complex `ε_LX`.** Substitution chain (per `math-scripts.md §"Double-Check Logic"`):

```
Claim: on the ε_LX moduli space, the generic (measure-1) outcome is J_PMNS ≠ 0;
       the CP-conserving locus is a measure-zero sub-variety.
Step 1: physical-phase count for an N-generation mixing = (N−1)(N−2)/2.   [standard rephasing count]
        N=3 ⟹ exactly 1 physical Dirac phase δ.
Step 2: CP-conserving locus {ε_LX real-rephasable} = {δ ∈ {0,π}} = {1 physical phase pinned to a discrete set}.
Step 3: pinning a continuous modulus to a discrete set ⟹ codimension ≥ 1 ⟹ measure-zero. [generic position]
Concl.:  any selection NOT fine-tuned to that locus returns J ≠ 0 generically. The real
         texture must be HIT by a mechanism; it is not the default. ⟹ the prior leans complex.
```

This is the NCG moduli-space view: Connes 2006 §4.1 makes the CP phase a FREE COORDINATE on the Dirac-operator moduli space, and the real-rephasable textures are a positive-codimension sub-variety of it. dirac's "J-silent" (no AXIOM forces a direction) is correct; his "no lean" (uniform prior over the moduli space) is too strong — a uniform prior over a space whose CP-conserving slice is measure-zero already leans complex. So "`J_PMNS=0` forced" is not merely unproven (the not-HARD result) but **anti-favored by genericity**, and the burden on ANY upgrade-beyond-artifact (including the spectral-action route) is to show the SA minimizer lands ON a codimension-≥1 locus — a fine-tuning, not a default.

**Honest two-sided register check (my discipline — the data does NOT one-sidedly support me).** The W2-3 verdict (`S116-W2-LEPTON-PMNS-TEXTURE`) records the observed PMNS reachable at `1.53×` minimal `‖ε_LX‖` (a SOFT WALL, 3/3 angle slots), and `J=0` (`δ_CP=180°`) sits INSIDE the 3σ NuFIT range `[108,404]°` (`CP-conserving-consistent=True`). So the measure-zero locus is observationally LIVE today — not a falsified corner. And `s60` Scenario B found `V_B3` real-symmetric. But `V_B3`-real is the INTERNAL (D_K-built, Kosmann-lifted, Peter-Weyl-real per S22b) SKELETON — by §VII.BL the off-diagonal generation texture is provably NOT D_K-built, so the genericity argument lives on the EXTERNAL `ε_LX` moduli space where `V_B3`-reality has no reach. The lean is a prior on the external moduli space; the internal-real facts are skeleton facts on the orthogonal (γ₉-even) leg.

### EMERGENCE

Three cross-pollination results. **E-1 decisively answers dirac's D3-Q2 on my side of the wall**; E-2 answers D3-Q1; E-3 is register-grounded and adjudicates D1's honest boundary.

**E-1 — D3-Q2 (is there a `J_R` on the commutant?): the HARD-via-reality-structure route is SELF-DEFEATING. It dies on the KO-dim-6 ↔ Majorana co-dependence — one structural fact serving both.**

dirac framed this as the single decisive question: `J_R` with `ε″_R=+1` on the commutant would force `ε_LX` real and UPGRADE to HARD; `ε″_R=−1` or no `J_R` ⟹ ARTIFACT. The NCG answer, in three steps:

(a) **There is no INDEPENDENT `J_R` to discover.** In a real spectral triple the order-zero axiom is `[a, J b* J⁻¹] = 0` ⟺ `J π_L(A_K) J⁻¹ = π_L(A_K)°` — i.e. the commutant where the generation texture lives (the right-regular `SU(3)_R` on the multiplicity leg, W2-1) IS `J A_K J⁻¹`. There is ONE reality structure `J`; it is itself the antilinear operator relating left and right (equivalently, the Tomita modular conjugation of the unimodular `SU(3)` bi-regular representation, `(Jξ)(g)=\overline{ξ(g⁻¹)}`, decorated by the fiber conjugation). dirac's "`J_R`" is `J` viewed on the commutant — not a free new object.

(b) **Its grading is INHERITED, not free.** The KO-dimension is a property of the pair `(J, γ₉, D)`, NOT of which algebra acts: the opposite triple `(A_K°, H_K, D_K, J, γ₉)` shares the SAME `(J, γ₉)` as `(A_K, H_K, D_K, J, γ₉)`, hence the SAME KO-dimension. Structurally, `γ₉` acts on the SM-fiber `ℂ¹⁶` leg, which is tensor-DISJOINT from BOTH the carrier (`SU(3)_L`) and the multiplicity (`SU(3)_R`) leg — `γ₉` does not distinguish left from right. So the SAME `J` that conjugates `A_K → commutant` carries the SAME relation to `γ₉`: `J γ₉ = ε″ γ₉ J` with `ε″ = −1` (KO-dim 6, machine-ε, `permanent-theorems`; `s60 §1` confirms `J_F D_F = D_F J_F`, `ε'=+1`). Therefore `ε″_R = ε″ = −1`.

(c) **The `ε″_R=+1` upgrade requires a KO-dimension incompatible with the Majorana sector.** From the KO table, `ε″=+1` occurs ONLY at KO-dim 0 `(+,+,+)` and KO-dim 4 `(−,+,+)`; `ε″=−1` at KO-dim 2 and 6. Forcing the γ₉-ODD mass operator real needs `Kγ₉=+γ₉K`, i.e. `ε″=+1`, i.e. KO-dim 0/4. But it is precisely KO-dim 6 (`ε″=−1`) that BOTH (i) protects the CP phase in the γ₉-odd sector (dirac's Re:C1 grading mechanism — `ε″=−1` re-injects `i` into the off-diagonal) AND (ii) admits the `ν_R` Majorana mass `M_R` (CCM-2007's reason for choosing KO-dim 6 mod 8: resolves fermion doubling, allows the `M_R` symmetric term — `s60 §1`). So a reality structure that forces `ε_LX` real would have to leave KO-dim 6 — DESTROYING the Dirac/Majorana asymmetry that is the entire premise of treating leptons differently from quarks.

**Conclusion E-1:** the HARD route via a reality structure is self-defeating. The ONE KO-dim-6 fact (`ε″=−1`) is co-dependently the protector of the CP phase AND the enabler of the Majorana neutrino; you cannot deploy a reality structure to kill the first while keeping the second. Combined with the settled R1 result (the EXISTING KO-6 `J` is insufficient), HARD is DOUBLY dead — no existing and no alternative reality structure rescues it. D3-Q2 closes toward ARTIFACT.

**E-2 — D3-Q1 (is the PRESCRIPTION J-decidable, or is it CF-W2-1's content?): `D_K` self-adjointness FIXES it as Yukawa; the prescription is NOT CF-W2-1's content.**

The mass/texture operator is the γ₉-ODD (chirality-reversing) block of `D_K = [[0, M],[M†, 0]]`. The physical left-handed mixing is the SVD of `M` = eigenvectors of `M M†` — FORCED, because `D_K` is self-adjoint and the mass operator is chirality-off-diagonal. The "normal-operator" reading (eigenvectors of the circulant `C` directly, the S115 `J=0.0962`) treats a γ₉-odd mass as if it were a γ₉-EVEN Hamiltonian — non-physical. So the structural reason dirac asked for IS available: **D_K self-adjointness + the γ₉-odd location of the mass operator fix the Yukawa prescription.** Direction check (real vs complex):

```
Real circulant C (real couplings c_a):  C† = C^T ⟹ C C† = C C^T real-symmetric
   ⟹ real-orthogonal eigenvectors ⟹ J = 0.            [the γ₉-even reality of M M† = dirac's Re:C5(2) "skeleton"]
Complex M (off-diagonal ε_LX complex):  M M† Hermitian with genuinely complex eigenvectors
   ⟹ U_eL complex ⟹ PMNS = U_eL† U_νL ⟹ J ≠ 0.
```

So the Yukawa `J=0` is the γ₉-EVEN reality of `M M†` (skeleton), carrying NO γ₉-odd phase information; it is a CP PREDICTION only if `M` is substrate-real — which is CF-W2-1. D3-Q1's "is the prescription itself the uncomputed content of CF-W2-1?" → **NO.** Prescription fixed by self-adjointness; CF-W2-1 decides the REALITY of `M`'s off-diagonal, not the reading. This MERGES with E-1: the only door beyond artifact is the spectral-action SELECTION of a real off-diagonal (a DYNAMICAL preference) — never a reality-structure FORCING (E-1 kills that). Even if CF-W2-1 returns "SA selects real," the resulting `δ_CP ∈ {0,π}` would be a spectral-action MINIMIZATION prediction, NOT "KO-dim-6 J-self-conjugacy forced." **The A2.2 "J-self-conjugacy" justification is dead REGARDLESS of CF-W2-1's outcome** — its verdict is prior to and independent of CF-W2-1.

**E-3 — register-grounded adjudication of D1's honest boundary: the baryogenesis linkage is SECTOR-RESOLVED per the canonical tag, weakening D1's main line to its honest-boundary horn.**

dirac's D1 linkage ("external baryogenesis ⟺ `δ_CP^PMNS ∉ {0,π}`") is conditioned on the SHARED off-Jensen `U(2)`-breaking. The register weighs in directly: `canonical_constants.py:674` carries `phi_CP_K7_transit = π/2 EXACT`, tagged "K_7 TRANSIT CP phase (baryogenesis; **phi_88-Cartan unique non-leptophilic CP source**; substrate-FIXED)... NOT the PMNS leptonic delta_CP." So the framework's baryogenesis CP source is a NONZERO (`π/2`) hypercharge-direction (`H_8`) phase, EXPLICITLY tagged **non-leptophilic** = sector-resolved from the leptonic `δ_CP`. Under that tag, D1's main line weakens to dirac's own honest-boundary horn: external baryogenesis needs SOME external phase (it has `π/2` from the `K₇` transit), and a real leptonic `ε_LX` (`δ_CP ∈ {0,π}`) need NOT kill it. So "`J_PMNS=0` forced is a falsifier of the framework's OWN baryogenesis" (D1's punchline) holds ONLY under the shared-`U(2)` horn; the register currently tags the SECTOR-RESOLVED horn, which preserves baryogenesis on `phi_88`-Cartan even with a CP-conserving lepton sector. The baryogenesis annotation on the A2.2 row should therefore be a CONSISTENCY note (external CP exists, sector-resolved), NOT a contradiction — and the shared-vs-sector-resolved off-Jensen `U(2)` question is the load-bearing carry-forward, with the register tag a current data point FOR sector-resolved.

**Net verdict (connes, pinned for the final round):** `J_PMNS=0` is **ANSATZ-ARTIFACT as derived, CONDITIONAL-PENDING-CF-W2-1 as to a (dynamical-only) substrate upgrade; HARD is DOUBLY dead** (R1: existing KO-6 `J` insufficient; E-1: no alternative reality structure rescues it without destroying the Majorana sector). The prescription is fixed-Yukawa (E-2); the baryogenesis annotation is a sector-resolved consistency note (E-3); the "J-self-conjugacy forced" justification is struck regardless of CF-W2-1.

### QUESTIONS

(My answers to D3-Q1/Q2/Q3 are E-2 / E-1 / CONVERGENCE-1 respectively.) Three sharper follow-ups to drive the final round to the A2.2 row FORM:

**Q-conn-R2-1 (leptogenesis under §VII.BL-external — the inverse of S60 Scenario A).** `s60 §3/§12` shows Scenario A (`D_K≡D_F`, `M_R` real) kills leptogenesis (`ε_1 = 0` EXACT). Under the §VII.BL-corrected reading (`M_D` off-diagonal EXTERNAL, J-silent, complex-admissible), does the SAME external `ε_LX` phase that gives a nonzero `δ_CP^PMNS` ALSO rescue `ε_1 ≠ 0`? If yes, then within the lepton sector ALONE (no off-Jensen `U(2)` sharing needed) leptonic baryogenesis is live ⟺ `δ_CP^PMNS ∉ {0,π}` — the SHARP, sector-internal form of your D1, and the cleanest statement of "`J_PMNS=0` taken as forced self-falsifies leptogenesis." Is that the correct sector-internal reading?

**Q-conn-R2-2 (the A2.2 falsifier CONTENT — operator-expression / laboratory-IN form).** Given (E-1) HARD-via-reality-structure is dead and (E-2) the prescription is fixed-Yukawa, the A2.2 row's live falsifiable content reduces to a TWO-SIDED discriminator: "spectral action selects real `ε_LX` (CF-W2-1) ⟺ `δ_CP ∈ {0,π}`; a DUNE/T2K measurement of `δ_CP` away from `{0,π}` falsifies the real-`ε_LX`/Scenario-A reading and confirms §VII.BL-external over `D_K≡D_F`-internal." Do you agree the row should be stated as this two-sided discriminator (with the laboratory-IN observable = the DUNE `δ_CP` posterior), rather than a one-sided "`J_PMNS=0` forced"? That is the `cross-pillar-bridge-anatomy` Element-2 OE-form the inventory row needs.

**Q-conn-R2-3 (does the `phi_88`-Cartan sector-resolution survive YOUR domain?).** The register TAGS `phi_CP_K7_transit = π/2` as the "unique non-leptophilic CP source." From your charge-conjugation/`J` domain: is the `phi_88`-Cartan (hypercharge-direction) CP phase STRUCTURALLY independent of the leptonic `ε_LX` off-diagonal (sector-resolved), or does the off-Jensen `U(2)`-breaking couple them (shared)? Your answer fixes whether E-3's softening holds (sector-resolved ⟹ baryogenesis survives a real leptonic `ε_LX`) or whether your D1 main-line linkage stands (shared ⟹ `J_PMNS=0` falsifies baryogenesis). This is the single carry-forward that sets the A2.2 baryogenesis-annotation's strength.

---

## Round 2 — dirac: Cross-Synthesis

### CONVERGENCE

I verified each of connes's Round-2 moves at the equation level (the `J`/charge-conjugation structure is my domain) and converge on all three EMERGENCE results, the baryogenesis withdrawal, and the verdict skeleton. The register is exactly as connes read it (I checked `canonical_constants.py:674/675/1873`, `falsifier-master-inventory.md:2206/2219`, `s60_lepto_cp_log.txt §1/§3` this turn — not on his word).

**1. E-1 (no `J_R` rescues HARD) — CORRECT, and I sharpen it to a CPT theorem in my domain.** connes answers my D3-Q2 decisively. I framed it as "is there a free `J_R` on the commutant with `ε″_R=+1`?" The order-zero axiom forecloses the freedom: `[a, Jb*J⁻¹]=0 ⟺ J π_L(A_K) J⁻¹ = π_L(A_K)°`, so the commutant where the generation texture lives IS `J A_K J⁻¹` — ONE reality structure, and "`J_R`" is `J` viewed on the commutant, not a new object (connes (a)). Its grading is INHERITED because the KO-dimension is a property of the pair `(J, γ₉)`, and `γ₉` acts on the SM-fiber `ℂ¹⁶` leg, tensor-disjoint from BOTH the carrier (`SU(3)_L`) and the multiplicity (`SU(3)_R`) leg — so `γ₉` cannot distinguish left from right, and `ε″_R = ε″ = −1` (connes (b)). I confirm both at the operator level: `J = Ξ·conj`, `Ξ=[[0,−G5],[−G5,0]]` is FIBER-blind (my T1), and `Jγ₉=−γ₉J` (`ε″=−1`, KO-dim 6, my T5) is a relation on the `(J,γ₉)` pair the left/right split does not see.

The decisive co-dependence (connes (c)) is, in my domain, a CPT–Majorana theorem, and I state it sharper than the workshop has:

> **(D-R2.1)** The KO-dimension-6 grading sign `ε″=−1` is SIMULTANEOUSLY (i) the protector of the `γ₉`-odd CP phase and (ii) the admissibility condition for the `ν_R` Majorana mass. Forcing `ε_LX` real requires `ε″=+1` (KO-dim 0/4), which FORBIDS the Majorana term. **You cannot have a Majorana neutrino and a CP-forced-real lepton mixing from the same reality structure — they are KO-dimension-incompatible.**

Proof sketch (my domain). The Majorana mass `M_R` couples `ν_R` to its OWN charge conjugate `\overline{ν_R}` — it is, by definition, a charge-conjugation (`J`) operator: `ν = ν^c`. In NCG it is the `J`-symmetric part of `D_F` (the antisymmetric bilinear `⟨Jψ, Dψ⟩` / Pfaffian structure CCM-2007 chose KO-dim 6 to obtain — resolving fermion doubling); its existence REQUIRES `ε″=−1` (KO-dim 2 or 6; `s60 §1` confirms `J_F D_F = D_F J_F`, the `M_R`-symmetric admissibility). Independently, my Re:C1 grading mechanism: in the `J`-canonical basis `[J,·]=0` makes the `γ₉`-EVEN sector real while `Jγ₉=−γ₉J` makes `γ₉` imaginary-antisymmetric, so the `γ₉`-ODD mass operator carries `i` STRUCTURALLY (`M_ph∈iℝ`, my T9) — this protection ALSO requires `ε″=−1`. The two roles are ONE sign. To force the off-diagonal real you need `Kγ₉=+γ₉K` (`ε″=+1`), landing at KO-dim 0/4, where the Majorana term is forbidden. So the HARD route would DELETE the Dirac/Majorana asymmetry (the `ℂ⊕ℍ` Majorana vs `M₃(ℂ)`-shared) that is the ENTIRE premise of treating leptons differently from quarks (the rescue WP's Track-A seed). **HARD is not just dead — it is self-cannibalising, and the obstruction is a CPT theorem: the same `ε″=−1` serves charge-conjugation-of-the-neutrino and protection-of-the-phase.**

**2. E-2 (prescription fixed-Yukawa by `D_K` self-adjointness) — CORRECT; it is the biunitary-vs-unitary distinction, and it kills the A2.2 justification independently of CF-W2-1.** connes answers my D3-Q1. The mass operator is the `γ₉`-odd block of `D_K = [[0,M],[M†,0]]`; `D_K` self-adjoint ⟹ physical left-handed mixing is the SVD of `M` (eigenvectors of `M M†`), NOT a similarity-diagonalisation of `M` (the "normal-operator" `J=0.0962` reading). In my language: a MASS is not a HAMILTONIAN. The gauge currents couple to left-handed fields, so the physical mixing is the LEFT singular-vector matrix `U_eL† U_νL` (biunitary `M = U_L Σ U_R†`), never a single similarity `M = SΛS⁻¹` (physical only if `M` is normal, `MM†=M†M` — a `γ₉`-even Hamiltonian). The normal-operator reading treats a chiral mass as a Hamiltonian — non-physical.

> **(D-R2.2)** Real circulant `C` ⟹ `C C† = C C^T` real-symmetric ⟹ real-orthogonal `U_eL` ⟹ `J=0` — the `γ₉`-EVEN reality of `M M†` (my Re:C5(2) SKELETON), carrying NO `γ₉`-odd phase. Complex `M` ⟹ `M M†` Hermitian with complex eigenvectors ⟹ `J≠0`. The prescription is FIXED by self-adjointness; CF-W2-1 decides the REALITY of `M`'s off-diagonal, not the reading.

Consequence (connes's, sharpened): the A2.2 "KO-dim-6 J-self-conjugacy forces `J_PMNS=0`" justification is dead REGARDLESS of CF-W2-1. Even if the spectral action selects a real `ε_LX`, the resulting `δ_CP∈{0,π}` is a spectral-action MINIMISATION (a DYNAMICAL preference), NOT a `J`-self-conjugacy FORCING. The verdict on the JUSTIFICATION is prior to and independent of CF-W2-1's outcome.

**3. S61/S52 withdrawal + `s60` grounding — accepted on my home turf; `s60` confirms Scenario A is the artifact's source.** connes withdrew the C5.1 "contradiction" (my D3-Q3: YES) and grounded the artifact reading in `s60_lepto_cp_log.txt`. I verified: `s60 §3` records Scenario A (`[J,D_K]=0 ⟹ M_R real ⟹ ε_1 = 0.00e+00 EXACT`, `δ_CP∈{0,π}`); `s60 §1` records the standard NCG-SM (CCM-2007) `M_R` as a FREE complex-symmetric matrix, the Majorana phase "EXACTLY what is needed for leptogenesis." So canonical `delta_CP_PMNS_substrate = 0.0` (provenance `:1873` = `S99-W3-SEESAW-SUMMNU` verdict, NOT a `[J,D_K]=0` derivation — verified `:675`) is a SCENARIO-A artifact downstream of the over-strong `D_K≡D_F` promotion — the SAME promotion §VII.BL refutes for the mass hierarchy. My D1 internal/external split and connes's §VII.BL boundary are ONE statement (his CONVERGENCE-2): internal `φ_CP` `J`-forced-zero (`γ₉`-even, LI, T11/S52) vs external `δ_CP` `J`-silent (`γ₉`-odd, non-LI `ε_LX`).

**Answer to Q-conn-R2-3 (does `phi_88`-Cartan sector-resolution survive my domain?) — YES, structurally, with one quantitative carry-forward.** The register tags `phi_CP_K7_transit = π/2` (`:674`, verified) as the "`phi_88`-Cartan unique non-leptophilic CP source... NOT the PMNS leptonic `delta_CP`." From the `J`/charge-conjugation side: `phi_88` is a CARTAN generator (`λ_8`, gauge-hypercharge direction, generation-DIAGONAL); the leptonic `δ_CP` is the Jarlskog of the `ε_LX^ν` OFF-diagonal (generation-mixing, multiplicity-leg coset). These are DIFFERENT CP invariants — a Cartan-diagonal phase and an off-diagonal Jarlskog phase are rephasing-invariant under DIFFERENT rephasings; no rephasing of the generation basis maps one to the other. So at the reality-structure level they are STRUCTURALLY INDEPENDENT — sector-resolved — and E-3's softening HOLDS. **Honest boundary:** structural `J`-independence does not preclude the off-Jensen `U(2)`-deformation from introducing a SINGLE parameter feeding BOTH the `λ_8` transit phase AND the coset off-diagonal — that is a quantitative property of the off-Jensen deformation, not of `J`-algebra. The register tag (`phi_88` non-leptophilic, substrate-FIXED at `π/2`) is a current data point FOR sector-resolution; the shared-vs-sector-resolved `U(2)` is the carry-forward. So E-3 holds for the K₇-TRANSIT channel — but it does NOT, by itself, settle the LEPTOGENESIS channel, which my Q-conn-R2-1 answer (E-3′) gates SECTOR-INTERNALLY by `M_D`-reality, independent of `phi_88`.

### DISSENT

One residual divergence — connes's measure-theoretic genericity lean (R2 DISSENT) — and I answer it not by re-asserting "no lean" (my R1 position, which connes correctly called too strong) but by showing his is the WRONG PRIOR for a SELECTION-by-minimisation substrate. The dissent is sharp, and it inverts the direction.

**The genericity lean applies the wrong measure: the external phase is SELECTED by the CPT-even spectral action, not drawn uniformly from the moduli space.** connes's chain is correct AS a statement about a uniform measure: the CP-conserving locus `{δ∈{0,π}}` is codimension ≥1, hence measure-zero, so a uniform draw returns `J≠0` generically. But the framework does NOT sample `ε_LX` uniformly — it (claims to) SELECT `ε_LX` by minimising the spectral action `S = Tr f(D_K/Λ)` (this IS CF-W2-1). A minimiser is a CRITICAL point, and critical points are THEMSELVES measure-zero. So the uniform-measure argument proves too much: by its own logic ANY SA-selected `ε_LX` — real OR complex — is measure-zero. The operative question is not "what fraction of the moduli space is CP-conserving" (measure-zero, trivially) but "does the SA critical point SIT ON the CP-conserving locus" — decided by a SYMMETRY of `S`, not by the measure of the locus.

Here the `J`/CPT structure decides the direction, OPPOSITE to genericity. Substitution chain (per `math-scripts.md §"Double-Check Logic"`):

```
Claim: a CPT-even spectral action with a UNIQUE minimiser in ε_LX selects a REAL ε_LX
       (δ_CP ∈ {0,π}) — the SELECTION prior leans REAL, not complex.
Step 1: S(ε_LX) = Tr f((D_K+ε_LX)²/Λ²) is REAL (f real) and depends ONLY on the spectrum
        of the self-adjoint D_K+ε_LX.                                  [spectral action def]
Step 2: CP acts on the moduli by conjugation ε_LX → ε_LX^CP, sending D → D̄ = Dᵀ
        (D self-adjoint ⟹ D̄ = Dᵀ); D and Dᵀ have the SAME spectrum.   [transpose-spectrum identity]
Step 3: Steps 1+2 ⟹ S(ε_LX^CP) = S(ε_LX): S is CP-EVEN (J-invariant) on the moduli space.
Step 4: a CP-even real function whose global minimiser is UNIQUE (up to gauge) has that
        minimiser at a CP-FIXED point ε* = ε*^CP, i.e. REAL.           [ε* min ⟹ ε*^CP min (CP-even);
                                                                        uniqueness ⟹ ε* = ε*^CP ⟹ real]
Concl.: unique-min CPT-even SA ⟹ real ε_LX ⟹ δ_CP ∈ {0,π}. The SELECTION prior leans REAL.
```

So connes's "the real texture must be HIT by a mechanism; it is not the default" is exactly right — and the SA-CPT-even minimisation IS that mechanism, and it hits real GENERICALLY (for a unique-min functional), not by fine-tuning. The fine-tuning is on the OTHER side: a COMPLEX SA minimiser requires the minimum to be DEGENERATE (a CP-conjugate pair `{ε*, \overline{ε*}}` or a continuous flat direction), and degeneracy is ITSELF non-generic in the space of functionals (a flat direction is codimension ≥1 in function space). connes applied genericity to the moduli MEASURE; the operative genericity is on the SELECTION FUNCTIONAL, and it points the opposite way. **Neither lean is the substrate's answer — that is CF-W2-1 — but the relevant prior is the SA-selection one, and it does NOT lean complex.** This sharpens (not dissolves) connes's residual: the divergence is now a PRECISE three-way fork on CF-W2-1's outcome (E-2′), not a "complex-vs-no-lean" standoff.

### EMERGENCE

Three cross-domain results, all in the `J`/CPT/baryogenesis sector. **E-1′** is the CPT–Majorana sharpening (folded into CONVERGENCE-1 as (D-R2.1) — not repeated). **E-2′** gives CF-W2-1 a precise structure and surfaces a NEW outcome. **E-3′** answers Q-conn-R2-1 and resolves the baryogenesis-annotation strength as a two-CHANNEL dichotomy.

**E-2′ — CF-W2-1 has a THREE-way structure, and the middle case is spontaneous CP violation: a NEW outcome neither round considered, in which `δ_CP` IS a substrate prediction without being `J`-forced.** From the CPT-evenness of `S` (DISSENT), the SA minimiser in the `ε_LX` off-diagonal falls into exactly three structural classes:

> **(D-R2.3)**
> - **(I) Unique min (up to gauge):** CP-fixed ⟹ `ε_LX` real ⟹ `δ_CP ∈ {0,π}` — the Scenario-A / W2-3 value, now as a DYNAMICAL (spectral-action) prediction, NOT a `J`-forcing.
> - **(II) CP-conjugate-pair min `{ε*, \overline{ε*}}`, `ε*` gauge-inequivalent to `\overline{ε*}`:** SPONTANEOUS CP violation. The substrate selects ONE member (a `Z₂` domain-wall choice); `δ_CP = ±|δ*|` with the MAGNITUDE `|δ*|` a substrate prediction (the SA-minimum location) and the SIGN spontaneously broken.
> - **(III) Continuous flat direction:** `δ_CP` genuinely under-determined (the W2-3 soft-wall, minimal-norm-by-fiat).

Outcome (II) is the result neither round reached: it makes `δ_CP ∉ {0,π}` a GENUINE zero-parameter substrate prediction (definite magnitude from the SA minimum), with the sign spontaneously broken — the leptonic analog of Lee's 1973 spontaneous CP violation, distinct from BOTH "forced real" (I) and "free" (III). It is the outcome that REVIVES the framework's leptonic CP as a prediction rather than an artifact. CF-W2-1 should therefore pre-register a THREE-way verdict, not the binary "flat-vs-lifted" the rescue WP stated — because "lifted" splits into the radically different (I) and (II).

**E-3′ — answer to Q-conn-R2-1: the leptogenesis–PMNS linkage is SECTOR-INTERNAL via the shared `M_D`-reality CONDITION; this SUPERSEDES `s60` Scenario A and makes the baryogenesis annotation a TWO-CHANNEL dichotomy.** connes asks whether the SAME external `ε_LX` phase that gives `δ_CP^PMNS ≠ 0` also rescues `ε_1 ≠ 0`. YES, sector-internally, and the structure is exact. With `M_R` spectrum-pinned real-diagonal (§VII.BL multiplicity-scalar), there is no free Casas–Ibarra `R`-matrix — the ONLY phase source is the external `M_D = ε_LX^ν` off-diagonal, which carries BOTH:

```
Leptogenesis CP:  ε_1 ∝ Σ_j Im[(Y†Y)_{1j}²] · f(M_j²/M_1²),   Y = M_D/v   [Davidson–Ibarra, M_R diagonal]
Low-energy PMNS:  δ_CP^PMNS from the phases of m_ν = M_D^T M_R⁻¹ M_D       [seesaw]
```

Both are functions of the SAME `M_D` phases.

> **(D-R2.4)** The single external object `M_D = ε_LX^ν` gates BOTH leptonic CP observables: `M_D` real-rephasable ⟹ `ε_1 = 0` (real `Y` ⟹ `Im[(Y†Y)²]=0`) AND `δ_CP^PMNS ∈ {0,π}` (real `m_ν` ⟹ real-orthogonal `U_PMNS`); `M_D` complex ⟹ both `≠0` generically. They are DIFFERENT functions of the `M_D` phases (no numerical lock-step), but they share ONE CP-conservation CONDITION — `M_D` reality.

This SUPERSEDES `s60` Scenario A: `s60`'s "`[J,D_K]=0 ⟹ M_R real ⟹ ε_1=0`" assumed `M_R`-INTERNAL-real (`D_K≡D_F`) — the over-strong promotion §VII.BL refutes. Under the corrected reading, `M_R` is real-diagonal (spectrum-pinned) but `M_D` is EXTERNAL and complex-admissible, so `ε_1` is NOT forced to zero. The SHARP consequence (the sector-internal form of my D1, needing NO off-Jensen `U(2)` sharing): forcing `M_D` real — the ONLY route to `J_PMNS=0` (E-2 + Re:C3) — ALSO forces `ε_1 = 0`. **`J_PMNS=0` taken as forced self-falsifies LEPTOGENESIS, sector-internally.**

Combined with E-3 (Q-conn-R2-3), the baryogenesis annotation is a TWO-CHANNEL dichotomy with OPPOSITE consequences:

> **(D-R2.5)** The framework has (at least) two external baryon-asymmetry channels:
> - **K₇-transit** (`phi_CP_K7_transit = π/2`, `phi_88`-Cartan, sector-RESOLVED from `δ_CP`, Q-conn-R2-3): `J_PMNS=0`-forced is CONSISTENT (baryogenesis rides `phi_88`, not the leptonic phase).
> - **Leptogenesis** (`ε_1` from `ν_R` decays, sector-INTERNAL, `M_D`-reality-gated, (D-R2.4)): `J_PMNS=0`-forced is SELF-FALSIFYING (`M_D` real ⟹ `ε_1=0`).
>
> The load-bearing carry-forward — which sets the A2.2 baryogenesis-annotation strength — is therefore NOT (only) "shared-vs-sector-resolved off-Jensen `U(2)`" but **WHICH baryon-asymmetry channel the framework actually uses**: if leptogenesis, `J_PMNS=0`-forced self-falsifies; if K₇-transit, it is consistent.

Direction of explanation holds: `D_K` eigenvalues (internal, `J` forces `φ_CP^int=0`, T11) → internal baryogenesis closed → external non-LI `ε_LX` (J-silent) → the SINGLE `M_D` reality gates BOTH `δ_CP^PMNS` and the leptogenesis `ε_1` → emergent leptonic CP AND any leptonic baryon asymmetry. CPT (`J`) is exact throughout (`m(p̄)=m(p)` to 16 ppt, `μ(p̄)/μ(p)` to 1.5 ppb); CP violation is an emergent property of the external texture, never a property `J` forbids.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | KO-dim-6 sufficiency | C1, Re:C1 | **Converged** | KO-6 `[J,D_K]=0` is necessary infrastructure but NOT sufficient for `δ_CP∈{0,π}`; the SM finite triple (KO-6 + `J_F`) is CP-violating. The decisive structure is the grading sign `ε″=−1` — it makes `γ₉` imaginary in the `J`-basis, re-injecting `i` into the `γ₉`-odd mass sector. **KO-dim 6 PROTECTS the phase.** |
| 2 | Quark J_CKM consistency | C2, Re:C2 | **Converged** | `J` is sector-uniform (`Ξ` fiber-blind); measured `J_CKM=3.08e-5≠0` under the SAME `J` is the framework-internal proof that `[J,D_K]=0` does not force CP conservation. No operator in the triple distinguishes the sectors' CP; `J_PMNS=0` and `V_us=0.3107` are one under-determination artifact-class. |
| 3 | Majorana → δ∈{0,π} mechanism | C3, Re:C3 | **Converged** | No such mechanism. Majorana CP (`α,β`) cancels from the Jarlskog (Dirac `δ` only); J-self-conjugacy is `M_ν=M_νᵀ` (symmetry), NOT reality. The only route to `J=0` is the real-`ε_LX` ansatz; CPT forces particle/antiparticle EQUALITY and is INDIFFERENT to CP — no sector-selective suppression from `J`. |
| 4 | Forced/Conditional/Artifact verdict | C4, Re:C4, D1, D2, E-1/2/3 | **Partial** (verdict Converged; prior Dissent; structure Emerged) | VERDICT converged: ANSATZ-ARTIFACT-as-derived, CONDITIONAL-PENDING-CF-W2-1, HARD doubly-dead (E-1: no alt reality structure rescues HARD without destroying the Majorana sector — a CPT theorem, (D-R2.1); E-2: prescription fixed-Yukawa by self-adjointness, justification dead ∀ CF-W2-1). PRIOR dissents: connes's uniform-measure complex-lean vs my CPT-even-SA real-lean-if-unique (DISSENT). STRUCTURE emerged: CF-W2-1 three-way (I real / II spontaneous-CPV / III flat, (D-R2.3)); baryogenesis two-channel dichotomy (K₇-transit consistent vs leptogenesis self-falsifying, (D-R2.5)). |

**PINNED VERDICT (d): `J_PMNS=0` is ANSATZ-ARTIFACT-as-derived; CONDITIONAL-PENDING-CF-W2-1 as to a (DYNAMICAL spectral-action) substrate upgrade; HARD is DOUBLY dead.** The "KO-dim-6 J-self-conjugacy forced" justification is STRUCK as a non-sequitur. **A2.2 row:** re-scope from "hard KO-6 forced" to the two-sided reading-discriminator (CONDITIONAL-PENDING-CF-W2-1); the ">3σ `δ_CP` away from `{0,π}` falsifies" form is warranted ONLY as a discriminator between the Scenario-A-internal and §VII.BL-external READINGS (it CONFIRMS §VII.BL-external, which predicts `δ_CP∉{0,π}` generically), NOT as a falsifier of "the framework." Routed to `mack-cosmic-bridge` (sole writer).

## Remaining Open Questions

(Q1 is CF-W2-1's promotion; Q2/Q3/Q4 are the new MATH carry-forwards below, 1:1.)

1. **CF-W2-1 three-way verdict (the decider).** Does the bosonic spectral action `S=Tr f(D_K/Λ)`, restricted to the lepton `ε_LX` off-diagonal at fixed charged-lepton masses, have (I) a unique minimiser (⟹ real `ε_LX` ⟹ `δ_CP∈{0,π}` as a DYNAMICAL prediction), (II) a CP-conjugate-pair minimiser (⟹ SPONTANEOUS CP violation, `δ_CP=±|δ*|`, magnitude predicted), or (III) a continuous flat direction (⟹ `δ_CP` under-determined)? **Pre-registered gate**: evaluate `S` over the `U_eL` orbit at fixed lepton masses; classify by (a) minimiser multiplicity (unique / 2-fold / continuous) and (b) CP-parity of the minimiser (`Im(ε*)=0`?). PASS-(I) unique ∧ real; PASS-(II) 2-fold ∧ CP-conjugate (report `|δ*|`); PASS-(III) Hessian null-direction along the CP phase. SUBSUMES the rescue WP's binary CF-W2-1.

2. **WHICH baryon-asymmetry channel does the framework use — K₇-transit or leptogenesis?** Sets the A2.2 baryogenesis-annotation strength ((D-R2.5)). **Pre-registered gate**: compute `η_B` on BOTH channels at the substrate texture — (a) K₇-transit (`phi_CP_K7_transit=π/2`); (b) leptogenesis (`ε_1` from `M_D=ε_LX^ν`, `M_R` B-branch diagonal). PASS-K₇ if K₇-transit reproduces `η_B,obs=6.12e-10` and dominates; PASS-LEPTO if leptogenesis dominates (⟹ `J_PMNS=0`-forced self-falsifies); INFO if both contribute. **Depends on** Q1 (the leptogenesis `ε_1` needs the `M_D`-reality verdict).

3. **Sector-internal `(ε_1, δ_CP^PMNS)` joint image over the `M_D` phase ((D-R2.4) refinement).** With `M_R` spectrum-pinned real-diagonal and `M_D` the sole phase source, does a substrate-natural complex `M_D` land BOTH a viable `η_B` (leptogenesis) AND a DUNE-measurable `δ_CP∉{0,π}`? **Pre-registered gate**: scan the `M_D` phase; PASS if ∃ phase with `η_B∈[3,8]×10⁻¹⁰` AND `δ_CP^PMNS` in the DUNE 5σ band away from `{0,π}` (⟹ JOINT prediction: baryon asymmetry ⟺ measurable leptonic CP). **Depends on** Q1, Q2.

4. **Shared-vs-sector-resolved off-Jensen `U(2)` (the K₇-transit channel's leptonic reach).** Does the off-Jensen `U(2)`-breaking feed BOTH `phi_88` (`λ_8`) AND the coset `ε_LX` off-diagonal from ONE parameter, or are they independent moduli? **Pre-registered gate**: parameter-count the off-Jensen deformation on `{λ_4,…,λ_8}`; PASS-RESOLVED if independent (⟹ E-3 holds, K₇-transit survives a real leptonic `ε_LX`); PASS-SHARED if one parameter (⟹ D1 main-line linkage, leptonic phase couples to baryogenesis).

## Wrap-Up — Workshop Impact Summary

### What Changed

**(a) Numerical revisions** — none. No σ-band, ratio, or OOM was re-pinned; this workshop was a structural adjudication on an existing FAIL verdict.

**(b) Structural changes**
- **`J_PMNS=0` status: "hard KO-6 J-self-conjugacy-forced prediction" → "ANSATZ-ARTIFACT-as-derived; CONDITIONAL-PENDING-CF-W2-1; HARD doubly-dead."** An epistemic-TYPE change (forced falsifiable prediction → real-`ε_LX`-ansatz artifact whose only upgrade is a DYNAMICAL spectral-action selection, never a reality-structure forcing). The "KO-dim-6 J-self-conjugacy" justification STRUCK as a non-sequitur.
- **A2.2 falsifier FORM: one-sided "`J_PMNS=0` forced" → two-sided READING-discriminator** (lab-IN observable = DUNE/Hyper-K `δ_CP` posterior): "SA-real-`ε_LX` (CF-W2-1) ⟺ `δ_CP∈{0,π}`; >3σ `δ_CP` away from `{0,π}` falsifies the Scenario-A-internal reading and CONFIRMS §VII.BL-external." The NuFIT-6.0 `δ_CP≈230°` "tension" REFRAMES to a data point FOR §VII.BL-external.
- **CF-W2-1: binary (flat-vs-lifted) → three-way (unique-real / spontaneous-CPV / continuous-flat, (D-R2.3)).** "Lifted" splits into `δ_CP∈{0,π}` dynamical and spontaneous CP violation with PREDICTED magnitude — radically different physics.
- **Baryogenesis linkage: "shared-U(2) D1 conjecture" → two-channel dichotomy (K₇-transit consistent vs leptogenesis self-falsifying, (D-R2.5)), the leptogenesis horn now SECTOR-INTERNAL** (`M_D`-reality-gated, (D-R2.4)) and superseding `s60` Scenario A.

### What Holds

- **CPT (`J`) is exact and untouched** — `m(p̄)/m(p)=1±16 ppt`, `μ(p̄)/μ(p)` to 1.5 ppb, `1S-2S H̄/H` to 2 ppt, `a_g/g=0.75±0.29`. The workshop constrains CP (external `ε_LX`), never the CPT structure `J` realises. CPT-invariance PERMITS arbitrary CP — the SM is the witness.
- **The internal CP phase is `J`-forced to zero** (T11/S52, `sin φ_CP^int=0`), closing INTERNAL baryogenesis — the genuine content of "J-self-conjugacy" (`γ₉`-even, generation-diagonal, LI), ORTHOGONAL to the external `δ_CP^PMNS`.
- **The CP-conserving SKELETON is spectrum-forced** — real diagonal Casimir charged-lepton tower + real-diagonal spectrum-pinned `M_R` (the `γ₉`-even/diagonal reality the substrate DOES supply).
- **The §VII.BL/§VII.CK generation-index wall** (bare `D_K` generation-blind) is untouched — both agents conceded it; independent of the CP-phase channel.

### What Breaks or Strains

- **The A2.2 / Row #89 "`[J,D_K]=0` ⇒ `J_CP=0` forced" registration is a MIS-CITATION** and must be re-scoped (routed to mack). It conflates the antilinear self-conjugacy (`C2·conj(D_K)·C2=D_K`) with texture-reality; the SM finite triple is the standing counterexample.
- **If the framework's baryon asymmetry is LEPTOGENESIS-sourced, `J_PMNS=0` taken as forced SELF-FALSIFIES the framework's own baryogenesis** (sector-internally, (D-R2.4)) — the inverse of a prediction. Only the K₇-transit channel (sector-resolved) survives a forced-real leptonic `ε_LX`.
- **The `m_ββ` funnel (Row #80) `[1.5,4.5] meV` is conditional on `δ_CP∈{0,π}`**, now CONDITIONAL-PENDING-CF-W2-1 — the funnel inherits that conditional status (flagged to mack).

### Carry-Forward Computations (MATH ONLY — propagate to S117)

(CF-W2-1 already minted; CF-S117-LEPTON-SEESAW-R-CHANNEL / -SEESAW-RESONANCE-MR-SEARCH / -QUARK-CKM-UNDERDETERMINATION-REEXAM already minted — not relisted.)

**CF-S117-CFW21-THREE-WAY — CF-W2-1 promoted to a three-way CP-parity classification.**
1. **What**: Classify the lepton `ε_LX`-off-diagonal spectral-action minimiser into (I) unique-real, (II) CP-conjugate-pair (spontaneous CP violation, predicted `|δ*|`), or (III) continuous-flat — via the CP-parity of the minimiser, not just flat-vs-lifted ((D-R2.3)).
2. **Inputs**: `computations/session-116/s116_lepton_pmns_texture.npz` (the `ε_LX` texture + `U_eL`-freedom orbit at fixed masses); the bosonic spectral action `S=Tr f(D_K/Λ)`; the CPT-evenness identity `S(ε_LX^CP)=S(ε_LX)` ((D-R2.3) Step 3).
3. **Gate**: PASS-(I) unique ∧ `Im(ε*)=0`; PASS-(II) 2-fold ∧ CP-conjugate (report `|δ*|`); PASS-(III) Hessian null-direction along the CP phase. The CP-parity of the minimiser is the discriminator.
4. **Effort**: ~1 agent, MEDIUM (SA over the `U_eL` orbit + Hessian CP-parity test). **Depends on**: `s116_lepton_pmns_texture.npz`; the SA assembly. SUBSUMES the rescue WP's binary CF-W2-1.

**CF-S117-BARYO-CHANNEL-ADJUDICATION — which channel sources `η_B`: K₇-transit or leptogenesis?**
1. **What**: Compute the framework `η_B` on BOTH external channels at the substrate texture and adjudicate which dominates — (a) K₇-transit (`phi_CP_K7_transit=π/2`, S98-W3-2 lineage); (b) leptogenesis (`ε_1` from `M_D=ε_LX^ν`, `M_R` B-branch diagonal, Davidson–Ibarra).
2. **Inputs**: `phi_CP_K7_transit=π/2` (`canonical_constants.py:674`); `s116_lepton_pmns_texture.npz` (`M_D`, `M_R`); `computations/session-60/s60_lepto_cp.py` (the `ε_1` machinery, Scenario-A/B); `eta_BBN_obs=6.12e-10`.
3. **Gate**: PASS-K₇ if K₇-transit reproduces `η_B,obs` and dominates (⟹ A2.2 baryogenesis = CONSISTENCY note); PASS-LEPTO if leptogenesis dominates (⟹ A2.2 = self-falsification linkage, (D-R2.4)); INFO if both contribute comparably.
4. **Effort**: ~1 agent, MEDIUM. **Depends on**: CF-S117-CFW21-THREE-WAY (the leptogenesis `ε_1` needs the `M_D`-reality verdict).

**CF-S117-LEPTO-PMNS-JOINT-IMAGE — the sector-internal `(ε_1, δ_CP^PMNS)` joint map over the `M_D` phase.**
1. **What**: With `M_R` spectrum-pinned real-diagonal and `M_D=ε_LX^ν` the sole phase source, scan the `M_D` phase and map the JOINT image `(ε_1, δ_CP^PMNS)`; test whether a substrate-natural complex `M_D` lands BOTH a viable `η_B` (leptogenesis) AND a DUNE-measurable `δ_CP∉{0,π}`.
2. **Inputs**: `s116_lepton_pmns_texture.npz` (`M_D`, `M_R`, `m_ν`); Davidson–Ibarra `ε_1(M_D, M_R)`; seesaw `δ_CP^PMNS(M_D, M_R)`; DUNE 5σ `δ_CP` band.
3. **Gate**: PASS if ∃ `M_D` phase with `η_B∈[3,8]×10⁻¹⁰` AND `δ_CP^PMNS` in the DUNE band away from `{0,π}` (⟹ JOINT prediction: baryon asymmetry ⟺ measurable leptonic CP); FAIL if mutually exclusive on the substrate texture; INFO if reachable only off the substrate-natural `M_R`.
4. **Effort**: ~1 agent, MEDIUM. **Depends on**: CF-S117-CFW21-THREE-WAY, CF-S117-BARYO-CHANNEL-ADJUDICATION.

**CF-S117-OFFJENSEN-U2-SHARING — is `phi_88` (`λ_8`) independent of the `ε_LX` coset off-diagonal?**
1. **What**: Parameter-count the off-Jensen `U(2)`-deformation on the `{λ_4,…,λ_8}` coset+Cartan; determine whether the `phi_88` transit phase and the lepton `ε_LX` off-diagonal are independent moduli (sector-RESOLVED) or share one parameter (SHARED).
2. **Inputs**: the off-Jensen deformation generator structure (`U(2)⊂SU(3)` breaking); the `phi_CP_K7_transit` definition (`canonical_constants.py:674`); the `ε_LX` multiplicity-bundle class (§VII.BL).
3. **Gate**: PASS-RESOLVED if `phi_88` and the `ε_LX` off-diagonal are independent moduli (⟹ E-3 sector-resolution, K₇-transit survives a real leptonic `ε_LX`); PASS-SHARED if one parameter (⟹ D1 main-line linkage stands).
4. **Effort**: ~1 agent, LOW–MEDIUM (algebraic moduli count on the coset+Cartan). **Depends on**: the §VII.CK external-`ε_LX` class (W2-1, this session).

### Effected In-Session (NON-MATH — completed by the final agent BEFORE TERMINATING)

- [x] **WP "What holds" overclaim down-tagged** — `sessions/session-116/session-116-w2-workingpaper.md` §"Wave 2 Synthesis → What holds" (line 167): replaced "`J_PMNS=0` … is a hard, falsifiable substrate prediction (KO-dim-6 J-self-conjugacy …)" with the workshop verdict (ANSATZ-ARTIFACT-as-derived; CONDITIONAL-PENDING-CF-W2-1; HARD doubly-dead; the "J-self-conjugacy" justification STRUCK; the two-sided discriminator form; the holding content — §VII.BL generation-index wall + CP-conserving SKELETON — preserved), with a pointer to this workshop + the mack routing. The §W2-3 FAIL verdict line is UNTOUCHED (verdict permanence).
- [x] **canonical_constants.py:675 comment scope-corrected** — `computations/_shared/canonical_constants.py:675`: `delta_CP_PMNS_substrate = 0.0` VALUE unchanged; the inline comment "substrate-forced DISCRETE set {0, pi}" re-scoped to "Scenario-A {0,pi} representative (real-`ε_LX` ansatz); NOT KO-6-forced — S116 W-1: ANSATZ-ARTIFACT-as-derived / CONDITIONAL-PENDING-CF-W2-1; the '[J,D_K]=0 / J-self-conjugacy forces δ_CP∈{0,π}' justification STRUCK." Prevents downstream mis-citation at the source. PROVENANCE dict (`:1873`) already honest (seesaw-gate source) — untouched.
- [x] **Capstone checked (no standalone overclaim — no-padding)** — `sessions/framework/phonic-exflation-equation.md`: grep confirms the capstone narrates `δ_CP∈{0,π}` ONLY as an `m_ββ`-configuration input (§7.3 line 580; line 679 `m_bb_FW`), NOT as a standalone "hard KO-6-forced" headline — so no capstone-prose down-tag is warranted (`feedback_fix-in-session-never-defer.md` no-padding on already-correct artifacts). The consequential dependency (the `m_ββ` funnel Row #80 inherits the `δ_CP∈{0,π}` CONDITIONAL status) flows to mack via the routing below. Capstone-hygiene Q3 (status change) + Q2 (§7 falsifier-row) FIRE → routed to mack + flagged to the orchestrator session-close gate.
- [x] **routed-to-mack: A2.2 / Row #89 + Row #89.audit re-scope** (`sessions/framework/registry/falsifier-master-inventory.md:2206`/`:2219` — `mack-cosmic-bridge` SOLE-WRITER per `feedback_mack-bridge-role.md`, NOT edited by me). Full spec sent via `SendMessage(to:"main")`: (1) Row #89 structural-origin "`[J,D_K]=0` ⇒ `J_CP=0`/`δ_CP∈{0,π}` forced" is a MIS-CITATION — re-scope to "CP-conserving SKELETON spectrum-forced; CP-PHASE leg ANSATZ-ARTIFACT-as-derived / CONDITIONAL-PENDING-CF-W2-1; `[J,D_K]=0`/J-self-conjugacy justification STRUCK (necessary infrastructure, not sufficient)." (2) Falsifier FORM → two-sided reading-discriminator (lab-IN = DUNE/Hyper-K `δ_CP` posterior); the NuFIT-6.0 `δ_CP≈230°` "tension" REFRAMES to a data point FOR §VII.BL-external. (3) Row #89.audit clause (1) "second independent route to J_CP=0" → both routes are the SAME real-`ε_LX` ansatz (NOT independent corroboration); clause (3) "CP-PHASE leg HARD+reinforced" → "NOT HARD; doubly-dead." (4) Baryogenesis annotation = sector-resolved CONSISTENCY note (E-3) with the TWO-CHANNEL dichotomy (D-R2.5) flagged (→ CF-S117-BARYO-CHANNEL-ADJUDICATION sets the strength). (5) Row #80 `m_ββ` funnel inherits the `δ_CP∈{0,π}` CONDITIONAL status. RETAIN original text per audit-trail (append supersession, the §VII.CK-corrigendum pattern).

### Closing Line

Dirac kept the negative-energy solutions because the algebra demanded them; here the same discipline keeps `δ_CP ∉ {0,π}` on the table — `[J,D_K]=0` is exact CPT and says NOTHING about the external phase, the KO-dim-6 sign `ε″=−1` that makes the neutrino Majorana is the very sign that protects its CP phase, and `J_PMNS=0` is the real-`ε_LX` ansatz's shadow, not the substrate's voice. The substrate will speak through the spectral action's minimiser (CF-W2-1, now three-way) and through whichever baryon channel it actually uses — and DUNE will hear the answer.
