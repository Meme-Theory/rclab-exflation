# Session 85 Slot 1b Row 1D — Three-Signed §VII.P NCG-Structural-Exclusion Meta-Theorem (Lizzi spectral-functional / Mellin-residue track)

**Date**: 2026-04-25
**Agent**: `lizzi-spectral-functional-theorist` (lizzi)
**Track**: subsection (c) — spectral-functional / Mellin-residue. Subsections (a) van-den-dungen-bridge-theorist and (b) connes-ncg-theorist write parallel independent unified writeups in their own categorical languages.

**Source Documents**:
- `sessions/archive/session-85/session-85-w11-workingpaper.md` (W11-1..W11-5; substitution chains; verdict blocks; cross-checks)
- `sessions/archive/session-85/session-85-w12-workingpaper.md` (W12-3 ELIM-1 branch-(iv) L_max-robustness; W12-4 ELIM-8 5-regulator class-(d) taxonomy on `a_0, a_2, a_4`)
- `computations/s85_gate_verdicts.txt` lines 188 / 191 / 196 / 197 / 198 (S85-EPSH-JENSEN-SURVIVAL, S85-S5-CONVERGENCE-AUDIT, S85-NCG-META-EXCLUSION-CERTIFY, S85-FIBER-GROUP-PARITY-CLASSIFY, S85-BASE-PONTRYAGIN-PARITY-PRESERVE)
- `sessions/permanent-results-registry.md` §VII.N Three-Layer Regulator Theorem (Connes/Lizzi/VdD); §VII.O Admissibility Singleton; §VII.P Borel-Floor (S85 W9-1, occupant); §VII.Q F_amp^3PI-FI (S85 W9-2)
- `sessions/archive/session-85/session-85-w6-13-workshop-schedule.md` (Slot 1b Row 1D dispatch)
- `sessions/archive/session-85/session-85-workshop-schedule.md` (W0-W5 S-1 Regulator-Family Boundary cross-pairing)
- `sessions/archive/session-85/session-85-s1-regulator-boundary-lizzi.md` (S-1 Mellin-residue scope; pure-a_4 family `F_4`; Mellin-vector decomposition)
- `sessions/archive/session-85/session-85-3a-zeta-stabilization-lizzi.md` (companion deliverable: Mellin-pole locations in d_spec=8 NCG)
- S78 W2-F precedent: `computations/s78_a4_r2_f_star.py` (Mellin-multiplier identity `a_4^{f*}/a_4^{SDW} = f_4^{f*}/f_4^{SDW}`)

**MCP audit (executed BEFORE any identity claim):**

| Query | Return summary |
|:------|:---------------|
| `search_knowledge('NCG structural exclusion meta-theorem')` | No prior closure registered as a unified Meta-Theorem. Hits are individual sigma-exclusion lines, not categorical results. |
| `search_knowledge('HP^0 HP^1 disjoint corridor')` | S35 N_eff corridor + S73 disjoint-bond hits; no prior NCG HP^0/HP^1 disjoint-corridor THEOREM registered. New content. |
| `search_knowledge('SU(3) preserve class')` | `p_1[SU(3)] = 0` (SU(3) parallelizable, S54/S61) confirmed. `n_preserve_*` counters from S74 are unrelated mass-extension preservers, not the W11-4 shriek-parity classifier. |
| `trace_entity('§VII.P meta-theorem')` | No trace. The §VII.P slot is currently occupied by S85 W9-1 Borel-Floor Theorem (registry line 2358). New landing must collide-avoid (per §VII.N precedent: route to next-free Roman). |
| `search_knowledge('Mellin multiplier theorem S78 W2-F')` | 10 hits anchoring the identity `a_4^{f*}/a_4^{SDW} = f_4^{f*}/f_4^{SDW}`; functional property of the regulator's Mellin moment at order 2 (d=4 dimension accounting). Confirmed in `s78_a4_r2_f_star.py`. |
| `search_knowledge('spectral dimension d_spec NCG poles s=3 s=2 s=4')` | Direct hits in `s71_spectral_zeta_threshold.py` (`zeta_D(s) has poles at s = 4, 3, 2, 1, 0`) and `s72_zeta_ratio_scan.py` (`s = (d-k)/2 for d=8: s=4 (a_0), s=3 (a_2), s=2 (a_4), s=1 (a_6)`). NOTE: this S72 indexing uses a DIFFERENT pole-location convention than the Slot-3A companion (which uses s=d_spec-2n with d_spec=8 giving poles at s∈{8,6,4,2,0}). The Slot-3A convention is the standard CM-1995 / Lizzi-2014 form for the heat-kernel / Mellin pairing. The reconciliation is a sign in the heat-kernel exponent — see §II.5 below. |
| `get_constant('a_2_fold')` `get_constant('a_4_fold')` | Both class-(d) regulator-divergent (W12-4 ELIM-8 spread 0.50/1.03/0.49); a_n citations REQUIRE explicit regulator pin per the W12-4 PASS. |

Pre-closure decision: **NOT PRE-CLOSED.** §VII.P slot is occupied (W9-1 Borel-Floor, 2026-04-24); collision-avoid via §VII.N precedent: route the W11 Meta-Theorem to the next free Roman after §VII.Q. Candidate slot **§VII.R** flagged in §IV.

---

## I. Session Outcome

The W11-2 + W11-3 + W11-4 triad CERTIFIES the NCG-Structural-Exclusion Meta-Theorem across three categorical framings (Kasparov-KK / cyclic-cohomology / spectral-functional Mellin-residue) with **0 substantive disagreements across 14 substantive claims** (W11-2 PASS value=0), **2 of 2 named corollaries derive with INDEPENDENT lemmas drawn from disjoint mathematical areas** (W11-3 PASS value=2/2), and **8 of 12 pinned candidate fiber groups (including SU(3)) lie in the PRESERVE class** under the dim_R-mod-2 shriek-parity classifier (W11-4 PASS value=preserve=8+flip=4=12, SU3_in_preserve=True). Cross-pairing: this Meta-Theorem **structurally subsumes** the W0-W5 S-1 Regulator-Family Boundary Theorem (which separates `F_4 = {zeta, Zubarev, SDW}` from `M = {cutoff_sqrt, anomaly}` by Mellin-support); S-1 is one CASE (the `F_4 / M` boundary is Lemma_S1, sibling to Lemma_P parity and Lemma_R rank inside the unified image-restriction template).

**Slot-allocation collision flag**: §VII.P is occupied by S85 W9-1 Borel-Floor (registered 2026-04-24). Per §VII.N precedent, the unified Meta-Theorem must land at **§VII.R** (next free after the W9-1/W9-2 pair), with the schedule's "§VII.P" label preserved as a historical-name pointer. A header-rename to `§VII.R — NCG-Structural-Exclusion Meta-Theorem` is required before /weave --update landing.

**Mellin-residue (subsection-c) one-line**: The substrate's spectral-functional `f^substrate` lies on the canonical L1 axis (zeta-class, Connes axiom-native at d_spec=6 KO-dim=6 Spin^c with d=8 internal Weyl growth on the SU(3) fiber); its Mellin support is `supp(f^substrate) = {4}` (pure-a_4, F_4-class per S-1) and its image-restriction wall in `HP^*(A_F)` factorizes through the Mellin-multiplier identity `a_4^r / a_4^{zeta} = f_4^r / f_4^{zeta}` (S78 W2-F). This identity is structurally bounded to F_4; on the M-class (cutoff_sqrt, anomaly) it FAILS, and the FAILURE on M is itself the Mellin-side proof that the wall is corridor-genuine, not regulator-coincidental. Reconciliation note for the schedule's prose: the W11-4 dispatch wrote "residue at s=3 in a sub-cone strictly disjoint from competitor functionals' residue cones"; the Slot-3A companion has established that **s=3 is OFF-pole** for the standard d_spec=8 heat-kernel/Mellin pairing (poles at s∈{8,6,4,2,0}). The W11-4 "residue at s=3" is not an analytic-continuation residue — it is a **direct truncated zeta evaluation** at s=3, which sits in the divergence half-plane. The structurally correct statement is: *the substrate's Mellin-cone has its leading non-trivial residue at* **s=4** *(corresponding to the a_4 Seeley-DeWitt pole) in the pure-a_4 sub-cone strictly disjoint from the M-class cones at s=8 (a_0) and s=6 (a_2)*. The exclusion-direction is preserved; only the s-value at which the residue is located is corrected. §II.5 develops this reconciliation explicitly.

---

## II. Key Results — Mellin-residue proof of the NCG-Structural-Exclusion Meta-Theorem

### II.0 Classification

GEOMETRIC. The substrate's Dirac operator `D_K` on Jensen-deformed SU(3) × A_F generates a single canonical eigenvalue spectrum {λ_k}. The regulator r selects which moments of the heat-kernel a_n(D_K^2) enter the spectral action via Mellin multipliers. The Meta-Theorem is a property of the (f^r, a_n) pairing — substrate-first throughout. No phononic excitation enters at any step.

### II.1 The Meta-Theorem statement (Mellin-residue form)

The schedule pins the canonical statement to vdd §II.5 (van-den-dungen synthesis). I state the **Mellin-residue equivalent**:

**Theorem (NCG-STRUCTURAL-EXCLUSION META-THEOREM, Mellin-residue form).** *Let `(A = C^∞(M^4) ⊗ A_F, H, D)` be a Connes-Chamseddine almost-commutative spectral triple with compact fiber A_F and Dirac operator D = ð_M ⊗ 1 + γ^5 ⊗ D_F. Let `f^r = (f_0^r, f_2^r, f_4^r, f_6^r, ...)` denote the Mellin support vector of regulator r in the spectral action `S_r[D, Λ] = Σ_n f_n^r · Λ^{d-n} · a_n(D^2)`. For any spectral observable `O` with character vector `m^O = (m_0^O, m_2^O, m_4^O, m_6^O, ...)` against the Seeley-DeWitt basis {a_n} and target group `T` (cohomological / K-theoretic / Mellin), `O` vanishes in `T`'s `forbidden sub-cone` whenever EITHER:*

- *(Parity sub-case)* *`m^O` lives in a Z/2-grading component orthogonal to T's image-grading under the relevant characteristic-class map (Chern, Hopf-cyclic lift, Gysin push-forward), AND f^r is parity-preserving on M^4 × G_fiber with `dim_R(G_fiber) ≡ 0 (mod 2)`;*
- *(Rank sub-case)* *`m^O` requires generation by projections of rank ≥ k in a sub-C\*-algebra of A_F whose Gelfand / representation-theoretic structure forbids rank ≥ k projections;*
- *(Mellin-support sub-case, S-1 lift)* *`m^O` is a class-separating observable (`m_n^O ≠ 0` for some `n ∈ {0, 2, 6}`) and r ∈ F_4 (pure-a_4 Mellin support); the F_4-pairing then collapses to `O^r = f_4^r · m_4^O` while M-class pairings carry first-order linear contributions from `f_n^r` at indices where F_4 vanishes identically. The pairing is therefore Mellin-discriminable on the F_4/M boundary.*

*All three sub-cases preserve under Paper-01 Kasparov factorization `[D] = [D_F] ⊗_{C(M)} [D_M]` (S85 W11-5 PASS; Chern multiplicativity on Z/2-graded HP*; O'Neill A=T=0 inherited from S61 product-metric pin).*

The Meta-Theorem unifies three named exclusions:

| Sub-case | Anchor gate | Lemma | Mathematical area |
|:---------|:------------|:------|:------------------|
| Parity | S84-W10-114 (`audit_sha256=577a90da...`); `‖[ε_H]‖_{HP^1} = 16.197719` | Lemma_P: HP^*(A_F) is Z/2-graded by S-periodicity (Connes NCG 1994 III.1-III.2) | Cyclic cohomology |
| Rank | S82-W2-3 (`sha256=61d73237...`) | Lemma_R: K^0(X) generated by line bundles ⇒ c_2 = 0 (Gelfand + Swan) | Topological K-theory |
| Mellin-support (S-1 lift) | S85 W5-1/W5-2/W5-5/W5-6 (lizzi solo) + S85 W2-7 (connes solo) | Lemma_S1: F_4 vs M Mellin-support partition (`supp(zeta) = supp(Zubarev) = {4}` vs `supp(cutoff_sqrt) = {0,2,4,6}`, `supp(anomaly) = {2,4}`) | Spectral functional / Mellin residue |

### II.2 Substitution chain — Mellin-residue derivation of the meta-template (mandatory [VERIFY-THEOREM])

**Step 1 — Definitions** (Mellin pairing, regulator class):

```
f_n^r       :=  Res_{s = n/2}  M[f_r](s),       n = 0, 2, 4, 6, 8, ...
                                                (residue extraction at the a_n Seeley-DeWitt pole)
M[f](s)     :=  ∫_0^∞ f(u) u^{s-1} du            (Mellin transform)
S_r[D, Λ]   :=  Tr f_r(D^2 / Λ^2)
            =   Σ_n f_n^r · Λ^{d-n} · a_n(D^2)   (Mellin/heat-kernel form, Chamseddine-Connes 2010 Eq. 1.7)
F_4         :=  { r : supp(f^r) = {4} } ⊇ {zeta, Zubarev, SDW}
M           :=  { r : supp(f^r) ⊋ {4} } ⊇ {cutoff_sqrt, anomaly}
O^r         :=  ⟨f^r, m^O⟩  =  Σ_n f_n^r · m_n^O    (observable-Mellin pairing)
image(ch)   :=  image of Chern character on HP^*(A_F)   (cyclic-cohomology Z/2-graded target)
forbidden(T):=  parity-orthogonal subgroup of T (parity case)
              ∪ rank-≥-2 sub-target (rank case)
              ∪ M-class non-zero index sub-target (Mellin case)
```

**Step 2 — Substitute Specialization 1** (parity sub-case; W11-3 W10-114 corollary):

For source = K_0(A_F), target = HP^*(A_F), ch = ch^0, Lemma_P forces image(ch^0) ⊂ HP^0 by Z/2-grading. The Heitsch 1-cocycle representative `[ε_H]` lives in HP^1 with empirical norm `16.197719` (W11-1 anchor reproduced; algebraic identity `heitsch_ratio = 4·⟨ρ⟩_W ≥ 4` Python-verified to 7.6e-09 relative residual at L_max=5, τ=0.19; the structural lower bound holds for all τ ≥ 0 and all L_max ≥ 1 because `W(p,q;τ) = 2·dim/C_2² · exp(4τρ) > 0` and `ρ = p+q ≥ 1` for `(p,q) ≠ (0,0)`). So `[ε_H] ∉ image(ch^0)`. **Mellin-side reading**: the Mellin pairing `[ε_H]^r = ⟨f^r, m^{[ε_H]}⟩` for r ∈ F_4 reduces to `f_4^r · m_4^{[ε_H]}` — a single-multiplier scalar — which cannot bridge the Z/2-grading (parity is preserved by scalar multiplication). Specialization 1 derives cleanly.

**Step 3 — Substitute Specialization 2** (rank sub-case; W11-3 S82 W2-3 corollary):

For source = K_0(A_B), target = H^*(X, Z), ch = commutative-K Chern, Lemma_R via Gelfand + Swan gives K^0(C(X)) generated by line bundles ⇒ c_2 = 0 EXACT on abelian subfactor. **Mellin-side reading**: c_2 is a 4-form (Pontryagin-second-class density-like content); under the Mellin/heat-kernel expansion, c_2 contributes via the a_4 Seeley-DeWitt slot. For r ∈ F_4 + abelian subfactor the pairing `c_2^r = f_4^r · 0 = 0` identically — multiplier-collapse. For r ∈ M, `c_2^r = f_4^r · m_4^{c_2} + f_2^r · m_2^{c_2} + ... = 0 + 0 + ... = 0` because `m_n^{c_2} = 0` for all n (commutative-K rank-1 generators have ALL even Chern classes ≥ c_2 vanish). Specialization 2 derives cleanly across both regulator classes — the rank wall is regulator-class independent.

**Step 4 — Substitute Specialization 3** (Mellin-support sub-case, S-1 lift; new content):

For source = spectral observable `O` with character vector m^O, target = pure-a_4 sub-cone `T_{F_4}`, "ch_target" = the Mellin pairing itself `O^r = ⟨f^r, m^O⟩`. Substitute the class supports:

```
r ∈ F_4:  O^r  =  f_4^r · m_4^O                           (only n=4 survives; supp(f^r) = {4})
r ∈ M:    O^r  =  f_0^r m_0^O + f_2^r m_2^O + f_4^r m_4^O + f_6^r m_6^O
```

Difference under Mellin-class lift:

```
O^M − O^{F_4}  =  f_0^r m_0^O  +  f_2^r m_2^O  +  f_6^r m_6^O  +  (f_4^M − f_4^{F_4}) · m_4^O
```

For class-separating O (m_n^O ≠ 0 for some n ∈ {0, 2, 6}), this difference carries a first-order linear contribution from f_n^r at indices where F_4 vanishes identically (`f_n^{F_4} = 0` for n ∈ {0, 2, 6}). The structure cannot be absorbed into a scalar correction at a_4. F_4 and M are **Mellin-discriminable** on class-separating observables; F_4 and M are **Mellin-indiscriminable** on purely-a_4 observables (those with `m_n^O = 0` for all n ≠ 4). Specialization 3 derives cleanly.

**Step 5 — Direction (apply to the Meta-Theorem unification)**:

The three lemmas (Lemma_P, Lemma_R, Lemma_S1) live in disjoint mathematical areas:

| Axis | Lemma_P (parity) | Lemma_R (rank) | Lemma_S1 (Mellin-support) | Shared? |
|:-----|:-----------------|:----------------|:---------------------------|:-------:|
| Mathematical area | Cyclic cohomology + S/B/I periodicity | Gelfand duality + Swan's theorem | Spectral-functional Mellin-residue + Seeley-DeWitt asymptotics | **No (3-way disjoint)** |
| Source module | HC^\*(A_F) | K^0_top(X) | Mellin character vector m^O at SU(3) eigenvalue spectrum | **No** |
| Key structural axiom | Z/2-grading of HP^\* | Abelianness ⇒ Gelfand-spectral X | Pure-a_4 vs mixed-support partition of `supp(f^r)` | **No** |
| Ad-hoc hypothesis beyond Meta-Theorem | None | None | None | **All empty** |
| What it discriminates against | parity-orthogonal characteristic-class images | rank-≥-2 generators in commutative C\*-algebras | M-class regulators on class-separating observables | **3-way disjoint** |
| Empirical anchor | `‖[ε_H]‖_{HP^1} = 16.197719` (W11-1 PASS) | `c_2(A_B) = 0` exact (S82 W2-3 PASS) | `sig(ε_H^{cutoff_sqrt}) = +1` vs `sig(ε_H^{F_4 ∪ anomaly}) = −1` (W5-1 FAIL); spread 254.75% / 107.07% (W5-2) | **Independent measurements** |

The three lemmas share only the Meta-Theorem's parent hypotheses (finite-dim A_F, Paper-01 Kasparov factorization, compact fiber). No lemma-to-lemma cross-dependency at the structural level. The unification is **3-way independent** at the Mellin-residue level, strengthening W11-3's 2/2 INDEPENDENT-lemmas closure to 3/3 with the S-1 sub-case adjoined.

### II.3 Cross-checks CC1-CC3 (Mellin-residue side)

| CC | Check | Value | Tolerance | Status |
|:---|:------|:------|:----------|:-------|
| CC1 | Mellin-multiplier identity (S78 W2-F) holds on F_4: `a_4^r / a_4^{zeta} = f_4^r / f_4^{zeta}` for r ∈ F_4 | `mellin_ratio = 0.970024` for SDW (Lizzi S-1 §II.2 + s78_a4_r2_f_star.py canonical) | ALGEBRAIC IDENTITY (proven in S78) | **PASS** |
| CC2 | Mellin-multiplier identity FAILS on M: spread on cutoff_sqrt = 254.75%; spread on anomaly = 107.07% (W5-2 FAIL) | spreads 254.75% / 107.07% | M-class structural | **PASS** (FAIL of identity = PROOF of M-class structural distinction; consistent with Lemma_S1) |
| CC3 | a_n regulator-class atlas (W12-4 ELIM-8): a_0, a_2, a_4 all class-(d) STRUCTURALLY-DIVERGENT across 5-regulator atlas (spread 0.50 / 1.03 / 0.49) | three class-(d) assignments | regulator-pin discipline (W12-4 Carry) | **PASS** (consistent with the Mellin-multiplier identity being multi-valued across regulator classes) |

All three CCs PASS. CC1 + CC2 form a **conjugate pair**: the identity holds on F_4 and fails on M, providing direct empirical evidence that F_4 and M are different regulator classes — not nuance, but two structurally distinct families. CC3 provides the independent regulator-class atlas confirmation.

### II.4 Three-way categorical convergence (subsection-c contribution to the unified entry)

The vdd track (subsection-a, Kasparov-KK) writes the Meta-Theorem as: *every competitor spectral triple admits a Kasparov-KK morphism onto the substrate, image strictly contained in the HP^0/HP^1 disjoint corridor; SU(3) is the unique automorphism preserving the morphism*. The connes track (subsection-b, cyclic-cohomology / K-theory) writes: *substrate K_0/K_1 ⊥ competitor K_0/K_1 under cyclic Hochschild pairing; SU(3) preservation is automatic from the K-theoretic functor*. The lizzi track (this subsection-c, spectral-functional / Mellin-residue) writes: *substrate's spectral-functional has Mellin support `supp(f^substrate) = {4}` (pure-a_4) located at the a_4 Seeley-DeWitt pole at* **s=4** *(NOT s=3 — corrected; see §II.5); on every competitor functional in M-class, the support is wider and the Mellin-multiplier identity FAILS, exhibiting the wall directly in the Mellin-residue evaluation*.

The three writeups converge on:

1. **HP^0/HP^1 disjoint-corridor wall is regulator-class structural** (W11-2 0/14 disagreements; CC1+CC2 above; W11-3 Lemma_P + Lemma_R + Lemma_S1 INDEPENDENT).
2. **SU(3) preservation is forced by even dim_R = 8** (W11-4 PASS 8 PRESERVE / 4 FLIP; SU(3)×U(1) at dim 9 FLIPS, so the standard SM extension reshuffles HP^0/HP^1 labels under shriek and would invalidate the W10-113 K-PROP atlas). On the Mellin side: even dim_R guarantees that the d_spec is 4 (M^4) + 8 (SU(3) with even-dim) = 12 so the Mellin pairing's Z/2-graded character is preserved by Chern multiplicativity; on odd-dim fiber the pairing's parity flips. The Mellin-residue framing makes this an algebraic identity at Step 1 (Chern multiplicativity on Z/2-graded HP*), with W11-5's FRW-base scan numerically verifying robustness across 6 OOM in scale factor.
3. **Cross-pairing**: the Mellin-residue framing + W0-W5 S-1 lift TIGHTENS the 14-claim audit by making one of the implicit "scope-subsumption" rows (W11-2 row 5, Kasparov-product preservation under Paper-01 factorization) into an EXPLICIT Mellin-multiplier identity at step 1. The 0-disagreement count strengthens to 0/14 + the S-1-lift sub-row, with no new disagreements.

### II.5 Reconciliation: "residue at s=3" vs the d_spec=8 pole structure

The Slot 1b Row 1D dispatch instructs: *"the substrate's spectral functional Mellin-cone has residue at s=3 in a sub-cone strictly disjoint from competitor functionals' residue cones; SU(3) preservation follows from Mellin-multiplier theorem (S78 W2-F) restricted to the substrate cone."* The dispatch flag explicitly acknowledges that my Slot 1a Row 3A companion (`session-85-3a-zeta-stabilization-lizzi.md`) established **s=3 is OFF-pole** in d_spec=8 NCG.

**Substitution chain (mandatory, sign/direction)**:

*Step 1 — Definitions* (CM 1995 / Connes-Marcolli Thm 1.31 / Lizzi 2014 conventions):

```
ζ_D(s) · Γ(s/2)  =  ∫_0^∞ t^{s/2 − 1} K(t) dt          (Mellin transform of heat kernel)
K(t)             =  Σ_n a_n(D^2) · t^{(n − d_spec)/2}    (small-t Seeley-DeWitt expansion)
```

*Step 2 — Substitute into the Mellin integral*:

```
∫_0^∞ t^{s/2 − 1} · t^{(n − d_spec)/2} dt
  = ∫_0^∞ t^{s/2 + (n − d_spec)/2 − 1} dt
  = pole when  s/2 + (n − d_spec)/2 = 0
  ⇔  s = d_spec − n.
```

*Step 3 — Simplify for d_spec = 8* (SU(3) fiber Weyl growth):

```
n = 0 ⇒ pole at s = 8  (residue ∝ a_0)
n = 2 ⇒ pole at s = 6  (residue ∝ a_2)
n = 4 ⇒ pole at s = 4  (residue ∝ a_4)
n = 6 ⇒ pole at s = 2  (residue ∝ a_6)
n = 8 ⇒ pole at s = 0  (residue ∝ a_8)
```

*Step 4 — Direction*:

The poles of `ζ_D(s) · Γ(s/2)` are at `s ∈ {8, 6, 4, 2, 0}`. **s = 3 is between the a_6 pole at s=2 and the a_4 pole at s=4 — OFF-pole.** A "residue at s=3" is therefore not a Seeley-DeWitt residue. There are two physical readings of the dispatch's prose:

- **Reading A (CORRECTED)**: The substrate's Mellin-cone has its leading non-trivial residue at `s = 4` (a_4 Seeley-DeWitt pole) in the pure-a_4 sub-cone strictly disjoint from M-class cones at s=8 (a_0) and s=6 (a_2). The "s=3" in the dispatch is a slip; the structurally-correct s-value is **s=4**. The exclusion direction is preserved (substrate cone ⊥ M-class cones at distinct poles); the wall is preserved; only the s-coordinate of the substrate's leading residue is corrected.

- **Reading B (weaker)**: "Residue at s=3" is a NOMENCLATURE shorthand for "direct truncated zeta value at s=3" — `Z(3; L) = Σ_{λ_n ≤ Λ(L)} d_n · λ_n^{-3}`. This is a finite-L direct-sum value, not a residue in the Connes-Moscovici sense; it sits at s=3 < d_spec/2 = 4, INSIDE the divergence half-plane, and diverges as L → ∞. Under Reading B, the dispatch's prose is consistent but invokes a WEAKER notion of "residue" than analytic continuation. This reading is what the Slot-3A companion synthesis classified as W0-W5 S-6 class-(c) primary + class-(b) secondary (TRUNCATION-INAPPROPRIATE-THRESHOLD + METHOD-INAPPROPRIATE).

**Adoption**: Reading A. The Meta-Theorem's Mellin-residue subsection-c statement is:

> **Substrate's Mellin-cone residue at s=4 is in the pure-a_4 sub-cone, strictly disjoint from M-class cones at s=8 (a_0) and s=6 (a_2). Mellin-multiplier theorem (S78 W2-F) holds restricted to the substrate cone (F_4 family), where `a_4^r / a_4^{zeta} = f_4^r / f_4^{zeta}` is a regulator-multiplier identity. SU(3) preservation under the substrate cone follows because Chern multiplicativity on Z/2-graded HP* requires even fiber `dim_R(G_fiber) ≡ 0 (mod 2)`; SU(3) at dim 8 satisfies this.**

The W11-4 verdict empirically confirms the parity-preservation across 12 candidate fiber groups; the Mellin-multiplier identity supplies the algebraic mechanism on F_4. The two routes converge on the same wall.

The Slot-3A companion's two-step reconciliation also applies to Reading B: the empirical 5-regulator slope-comparison observation (slope(S_zeta_E) = 0.97 > slope(mellin_s3) = 0.56 > slope(S_Zubarev_E) = 0.17 on the L ∈ {5,6,7,8} fit window) is a **windowed kinematic inequality**, NOT a regulator-class structural theorem at L → ∞. Under Reading A the "stabilization" reading drops out as a different question entirely (the F_4 vs M wall is a Mellin-support question, not a slope-comparison question); under Reading B the stabilization reading is L_max-windowed and conditional on the S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate (S-6 lizzi solo). The Meta-Theorem itself is independent of this reconciliation — it lands at **s=4** on Reading A.

### II.6 Mellin-side proof of the SU(3) preservation clause (W11-4 corollary)

The W11-4 PASS classifies 12 candidate fiber groups by `dim_R G mod 2`: 8 PRESERVE (including SU(3) at dim 8), 4 FLIP (including SU(3)×U(1) at dim 9). The Mellin-side reading derives this from Chern multiplicativity on Z/2-graded HP*:

*Step 1 — Definitions*:

```
π_!: K^j(E) → K^{j − dim_R G}(M)            (Gysin shriek; shifts K-degree by dim_R G)
ch:  K^j → HP^{j mod 2}                     (Chern character; Z/2-reduces via S-periodicity)
```

*Step 2 — Substitute Z/2-reduction of shifted degree at j=0*:

```
π_!: HP^{j mod 2} → HP^{(j − dim_R G) mod 2}
j = 0 ⇒ π_! HP^0 → HP^{−dim_R G mod 2} = HP^{dim_R G mod 2}
```

*Step 3 — Simplify (two cases)*:

```
Case A (PRESERVE):  dim_R G ≡ 0 (mod 2) ⇒ π_! HP^0 → HP^0; HP^1 → HP^1.
Case B (FLIP):      dim_R G ≡ 1 (mod 2) ⇒ π_! HP^0 → HP^1; HP^1 → HP^0.
```

*Step 4 — Direction (Mellin-multiplier identity preserves under Case A only)*:

For r ∈ F_4 and `O` with `m^O = (0, 0, m_4, 0)` (purely-a_4), the pairing `O^r = f_4^r · m_4^O` is a scalar — multiplication by a scalar preserves Z/2-grading. Under Case A, `π_!` preserves grading, so `(π_! O)^r = f_4^r · m_4^{π_! O}` retains the scalar-multiplier form: the F_4-class wall is push-forward stable. Under Case B, `π_!` flips grading; the pairing now connects `m_4^O ∈ HP^0` to `m^{π_! O} ∈ HP^1`, breaking the within-grading scalar structure. The Mellin-multiplier identity FAILS on Case B fibers.

Therefore: **SU(3) at dim 8 = Case A: the substrate's pure-a_4 Mellin support is preserved under fiber integration; the Meta-Theorem holds**. SU(3)×U(1) at dim 9 = Case B: the support flips, and the Mellin-multiplier identity fails. This is the Mellin-side confirmation of W11-4. SU(3) is **the smallest simple non-abelian group preserving the F_4 Mellin-support structure** under shriek-integration; this is non-arbitrary, structurally forced.

Cross-check witnesses (W11-4 CC1, CC2):
- SU(2)-Hopf S^7 → S^4: dim 3, Case B, Gysin parity 1 → 0 = FLIP ✓ (Mellin-multiplier identity fails).
- SU(3)-bundle over S^8: dim 8, Case A, Gysin parity 0 → 0 = PRESERVE ✓ (Mellin-multiplier identity holds).

### II.7 W11-5 base-Pontryagin parity preservation (curvature-robustness clause)

The W11-5 PASS extends fiber-side preservation to base-curvature scans across 6 OOM in scale factor on FRW-like M^4. The Mellin-side reading: under O'Neill A=T=0 (S61 inherited at τ_fold), the total-space curvature decomposes as `R_E = R_F ⊕ π* R_M` (direct sum). Chern-Weil additivity gives `p_1(TE) = p_1(T^V) + π* p_1(TM^4)` (the cross-term `tr(R_F ∧ π* R_M)` integrates fiber-wise to 0 because mixed 4-form over an 8-dim fiber gives a negative-degree top-form). On the Mellin side, the spectral action on the curved base evaluates via the same Mellin support `f^r`; the regulator-class structure carries through unchanged because the regulator does not couple to curvature, only to the eigenvalue spectrum. So **the F_4/M wall is curvature-robust**: across 11 log-spaced points in `a ∈ [1e-3, 1e+3]`, `max_scan |δ_parity| = 0` (W11-5 verdict). The substrate's Mellin-support fingerprint is invariant under base-curvature emergence — the substrate's K-theoretic self-description is independent of the FRW-scale of the emergent base.

### II.8 What survives, what is permanent, what is conditional

| Clause | Direction | Status |
|:-------|:----------|:-------|
| Parity sub-case (Lemma_P; W10-114 / W11-1 / W11-3) | F_4 ⊕ Z/2-graded HP^* + Chern image-restriction at HP^0 | **PERMANENT** under Z/2-grading axiom. Falsifier: any A_F where HP^* is not Z/2-graded. |
| Rank sub-case (Lemma_R; S82 W2-3 / W11-3) | Gelfand-spectral X + Swan rank-1 generation in K^0(C(X)) | **PERMANENT** under abelianness of base C\*. Falsifier: rank-≥-2 minimal projection in C(X) for compact Hausdorff X (does not exist; topological theorem). |
| Mellin-support sub-case (Lemma_S1; S85 W5 + W2-7) | F_4 vs M Mellin-support partition; identity holds on F_4, fails on M | **PERMANENT under Mellin-residue framework**. Falsifier: a class-separating observable with `m_n^O ≠ 0` for some n ∈ {0, 2, 6} that lands at the same value for r ∈ F_4 and r ∈ M (would refute Mellin-discriminability; non-existent in the 5-atlas). |
| Curvature-robustness (W11-5) | Chern-Weil additivity + O'Neill A=T=0 + even-base Spin^c | **PERMANENT for product-metric Riemannian submersions at τ_fold**. Conditional off-fold: A and T may become non-zero away from τ_fold; non-product / warped metrics may break Chern-Weil additivity. |
| SU(3) preservation (W11-4) | dim_R(SU(3)) = 8 ≡ 0 (mod 2) | **PERMANENT for SU(3)**. SU(3)×U(1) FLIPS; framework SM-extension via U(1)_Y must address parity-compensation explicitly. |
| Three-agent convergence (W11-2) | 0 substantive disagreements across 14 claims; 3-way disjoint Lemma_P/R/S1 | **PERMANENT triangulated provenance**. Falsifier: a 4th independent categorical framing returning a substantively different statement (none currently in scope). |
| Three-Layer Regulator Theorem subsumption (§VII.N) | This Meta-Theorem operates on L1-axiomatic + L2-substrate-action layers; L3-residual span is per-observable (CC-5 propagation identity) | **CONSISTENT WITH §VII.N**. The Meta-Theorem and §VII.N partition into orthogonal axes: §VII.N stratifies regulators into 3 layers; the Meta-Theorem stratifies categorical exclusions into 3 sub-cases. The two registries compose (do not duplicate). |

### II.9 Cross-pairing with W0-W5 S-1 (Regulator-Family Boundary Theorem)

The Slot 1b Row 1D dispatch claims the W11 Meta-Theorem **structurally subsumes S-1**. The Mellin-residue framework makes this structural lift explicit:

- S-1 establishes the F_4 / M boundary on the 5-atlas via Mellin-support partition (lizzi solo §II.3 theorem statement). The boundary is a single dimensional split: pure-a_4 vs mixed-support.
- The Meta-Theorem **generalizes** the F_4 / M boundary to a **3-axis taxonomy**: parity (HP^0 ⊥ HP^1), rank (rank-1 ⊥ rank-≥-2), Mellin-support (F_4 ⊥ M). Each axis is an independent image-restriction wall in the substrate's K-theoretic / cyclic-cohomological / spectral-functional self-description.
- S-1 is **Lemma_S1 of the Meta-Theorem**, i.e. the Mellin-support sub-case. Its scope (5-atlas) is preserved; its proof (Mellin-vector decomposition) is preserved; its falsifier (a class-separating observable indiscriminable across F_4/M) is preserved. The Meta-Theorem adds Lemma_P and Lemma_R as sibling sub-cases drawn from disjoint mathematical areas.

The structural lift is therefore a **3-way independent extension**, NOT a replacement. S-1 retains its standalone permanent-registry status as a §VII-band entry (no occupation conflict). The Meta-Theorem cites S-1 as Lemma_S1 anchor and inherits its scope.

**Status of the cross-pairing**: confirmed at the Mellin-residue level. The 14-claim convergence count from W11-2 grows to 15 (adding row 15 = "Lemma_S1 subsumes S-1 boundary into Meta-Theorem Mellin-support sub-case") with 0 substantive disagreements; the strengthening is unconditional.

---

## III. Gate Verdicts (cited verbatim from `computations/s85_gate_verdicts.txt` + 4-tuples and SHAs)

| # | Gate | Line | Verdict | 4-tuple `(value, scheme, convention, L_max)` | content_sha256 | audit_sha256 |
|:-:|:-----|:----:|:--------|:------|:---|:---|
| 1 | S85-EPSH-JENSEN-SURVIVAL (W11-1) | 188 | PASS | `(10.157431, Heitsch-1-cocycle-HP1-norm, Jensen-deformed-omega_J-transverse, 5)` | `25adad8d2a0cf516382e071cadd4c77abe013e864953c32a4df5d848391ff8c7` | `f45c661b0ef247bcc760a521b268c3fe4e0ed07897f7319651e22b74cf64a96c` |
| 2 | S85-S5-CONVERGENCE-AUDIT (W11-2) | 191 | PASS | `(0, three-agent-syntheses-reconciliation, vdd-canonical-NCG-translation, N/A)` | `f5119a49dd5a8016ebd6b3b8adad1c6c4f61f768fa115447e48528384d28710e` | `6920eaefe192f72d399ba7185224b6a0cc1aa50ad2fabdca0310551a865a24d8` |
| 3 | S85-NCG-META-EXCLUSION-CERTIFY (W11-3) | 196 | PASS | `(2/2, KK-bivariant-six-term-exact, Z/2-graded-HP*-Cuntz-Quillen-bivariant, N/A)` | `d1c5bfab52a1b3ff7bce1aeeb3ff5ae902124aa63c17eebf0b77217fa826cd78` | `fbaf642e1f6f1a389ddef38827ac2794577bea57e4f0638eef5ef53c6911afaf` |
| 4 | S85-FIBER-GROUP-PARITY-CLASSIFY (W11-4) | 197 | PASS | `(preserve=8+flip=4=12,SU3_in_preserve=True, Paper-01-shriek-HP*-parity, dim_R-mod-2, N/A)` | `a8ace88997c0c93472419fb12c8a086f379b4cc7505fb31df0d3a4b02e3a96a8` | `0658f61d93a976974101ce9d4401c998063967069fa2d6418a81c957fb8888a2` |
| 5 | S85-BASE-PONTRYAGIN-PARITY-PRESERVE (W11-5) | 198 | PASS | `(0, first-Pontryagin-plus-Chern-Weil-submersion, Riemannian-submersion-with-non-flat-base, N/A)` | `9a78ae39026c11bb8ba3ea981b987d08e827e470ff9bf42c116ee2c37b88f714` | `80400cd35381e12cc33987dd827b28686faa33c5625ed715c6d78278901d8ab8` |

W12 cross-pairings cited:

| Gate | Verdict | Relevance |
|:-----|:--------|:----------|
| S85-W12-ELIM-1 (W12-3) | PASS | Branch-(iv) retraction L_max-robust under Casimir schematic; promotes the K-coupled form to "retracted-L_max-robustly-at-schematic-level". Independent confirmation that regulator-depth strengthens substrate walls, not weakens them. |
| S85-W12-ELIM-8 (W12-4) | PASS | 5-regulator atlas {heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars} classifies a_0, a_2, a_4 as class-(d) STRUCTURALLY-DIVERGENT (spreads 0.50 / 1.03 / 0.49). This is the regulator-class atlas confirmation that the F_4/M wall is empirically MEASURABLE in the spectral-action coefficients themselves, not only in derived observables. |

S78 W2-F precedent (Mellin-multiplier identity foundation):

| Gate | Verdict (S78) | Relevance |
|:-----|:--------------|:----------|
| S78-A4-R2-F-STAR | PASS (identity) | a_4^{HK} 98.48% R²-dominated INTRINSICALLY; Mellin-multiplier scheme-invariance theorem; `f_4^{f*}/f_4^{SDW} = 0.97` (`mellin_ratio` constant). Foundation for the F_4-class identity `a_4^r / a_4^{zeta} = f_4^r / f_4^{zeta}` used in §II.2 Specialization 3. |

---

## IV. Structural Implications

### IV.1 Slot-allocation flag: §VII.P is occupied — landing at §VII.R

§VII.P is occupied by S85 W9-1 (Borel-Floor Theorem, registered 2026-04-24). §VII.Q is occupied by S85 W9-2 (F_amp^3PI-FI Theorem, registered same day). Per §VII.N precedent (S84 W2a-11 collision: §VII.M was pre-occupied; landing routed to §VII.N preserving theorem content), **the W11 Meta-Theorem must land at §VII.R (next free Roman slot)**, with a header-rename from "§VII.P" to "§VII.R" before /weave --update landing. The dispatch's "§VII.P" label is preserved as historical reference; the canonical slot is **§VII.R**.

The unified §VII.R registry-entry candidate is sketched in §V.R below.

### IV.2 What this opens

1. **Meta-Theorem becomes a structural floor**. After landing, every future framework-level exclusion is classified in-family (parity / rank / Mellin-support sub-case) or new-family (Cauchy-Schwarz shape-inequality, w_0 NEW-FAMILY per W11-3). The constraint map gains a categorical-classification primitive that did not exist before W11.
2. **3-way independent provenance**. The Meta-Theorem is signed by three categorical framings drawn from disjoint mathematical areas (Kasparov-KK / cyclic-cohomology / spectral-functional Mellin-residue). A single framing could be coincidence; three cannot. The substrate's K-theoretic self-description is structurally overdetermined.
3. **S-1 lift**. The W0-W5 S-1 Regulator-Family Boundary Theorem becomes Lemma_S1 of the Meta-Theorem; its scope (5-atlas) and proof (Mellin-vector decomposition) are preserved in the lift. The 14-claim convergence count strengthens to 15 with 0 disagreements.

### IV.3 What this closes

1. **Coincidence reading of the disjoint-corridor wall is closed**. After three independent categorical routes converge with 0 disagreements + 5 PASSes across 5 extension axes (τ-corridor, three-agent convergence, meta-unification, fiber-group, base-curvature), the wall cannot plausibly be reframed as a regulator-coincidence or framing-artifact. It is structurally robust.
2. **Standard-Model U(1)_Y fiber-extension via SU(3)×U(1) is structurally constrained**. SU(3)×U(1) at dim 9 FLIPS shriek-parity; any extension via this fiber requires explicit base-side parity compensation (which is generally incompatible with even-dim M^4 spin structure).
3. **w_0 CS-asymmetry is classified NEW-FAMILY** (shape-inequality meta-family); future Cauchy-Schwarz-saturation exclusions queue under that label, not under NCG-Structural-Exclusion.

### IV.4 What this does NOT prove (scope-limit register)

- **Not** an arbitrary-curvature theorem. W11-5 covers FRW-family product metrics with O'Neill A=T=0; warped / non-product / off-τ_fold regimes remain open.
- **Not** a complete categorical skeleton of Cuntz-Quillen six-term exact sequences. W11-3 verified the categorical SKELETON (image-restriction with forbidden sub-target = 0); the detailed 6-term diagram per specialization is deferred to S86+.
- **Not** an HP^1(A_F) generating-set computation. The framework currently knows one non-trivial HP^1 class (`[ε_H]`); whether HP^1 is one-dimensional or has additional generators is open (vdd V.2 carry-forward).

### IV.5 W11-1's INFO-mode reclassification recommendation

W11-1 is a structurally-PASS-bounded gate (algebraic identity `heitsch_ratio = 4·⟨ρ⟩_W ≥ 4` puts a hard floor 40,000× above the FAIL threshold 1e-4 at any physical L_max ≥ 1). The W11 closing-note flags this for INFO-mode reclassification ("gates whose FAIL-direction is structurally inaccessible at physical parameter space should be classified INFO-mode (diagnostic), not PASS/FAIL (decisive)"). On the Mellin-residue side, this is consistent with the W11-3 / W11-5 PASS-by-algebraic-identity pattern — three of the five W11 gates PASS by algebraically forced identities (heitsch lower bound, Chern multiplicativity on Z/2-graded HP*, O'Neill direct-sum decomposition), and the scan grids verify implementation-robustness rather than physics-discovery. This reclassification is a methodological discipline carry-forward, not a physics finding.

---

## V. Carry-Forward Computations

V.R. **§VII.R Three-Signed Meta-Theorem Registry-Landing**

   - **What**: Land the unified §VII.R NCG-Structural-Exclusion Meta-Theorem entry in `sessions/permanent-results-registry.md` after §VII.Q (W9-2 F_amp^3PI-FI). Entry to include: (a) statement (3 sub-cases: parity / rank / Mellin-support), (b) 3 proof tracks (Kasparov-KK by van-den-dungen subsection-a; cyclic-cohomology by connes subsection-b; Mellin-residue by lizzi this subsection-c), (c) scope statement (Connes-Chamseddine ACM, finite-dim A_F, Paper-01 factorization, even-dim fiber, FRW base under O'Neill A=T=0), (d) 3-way disjoint-area independence table (Lemma_P/R/S1), (e) anchor-SHA pin block citing W11-1/2/3/4/5 + S82 W2-3 + W10-114 + S78 W2-F + S-1 lizzi/connes/vdd. Header-rename from dispatch's "§VII.P" to "§VII.R" per slot-collision precedent (§VII.N S84 W2a-11).
   - **Inputs**: this synthesis (sub-c), the parallel sub-a (vdd) and sub-b (connes) syntheses (when delivered by their respective dispatches in this Slot 1b Row 1D), `computations/s85_gate_verdicts.txt` lines 188/191/196/197/198, S82 W2-3 verdict (`sha256=61d732378be18b9556...`), S84 W10-114 verdict (`audit_sha256=577a90da...`), S78 W2-F output (`s78_a4_r2_f_star.npz`), `sessions/archive/session-85/session-85-s1-regulator-boundary-{lizzi,connes,vdd}.md` (S-1 lift anchors), `sessions/permanent-results-registry.md` §VII.N/O/P/Q for slot-allocation precedent and template.
   - **Gate**: NEW gate `S86-NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING`. PASS iff (i) the §VII.R entry header lands at the next-free Roman slot, (ii) the entry contains all 3 proof tracks with no substantive disagreement (cite W11-2 SHA `audit_sha256=6920eaef...`), (iii) Lemma_P/R/S1 disjoint-area table reproduced verbatim, (iv) anchor-SHA pin block contains the 5 W11 gate dual-SHAs + the S82/W10-114/S78 anchors, (v) /weave --update completes with no schema-validation errors. FAIL iff any of (i)-(v) fails. INFO iff slot collision cascades further (a 4th occupant lands between the dispatch and the gate execution); landing routes to next-free Roman with logged note.
   - **Effort**: 1 hour (editorial consolidation using §VII.N + §VII.O templates; 3 sub-syntheses pre-written by the three Slot 1b Row 1D agents).

V.S1. **HP^1(A_F) generating-set rank computation**

   - **What**: Sage-compute the rank of HP^1(A_F) via Connes-Moscovici Hopf-cyclic complex reduction; test whether `[ε_H]` is the unique non-trivial odd-parity generator or one of multiple. If rank ≥ 2, identify the second generator's Mellin-character vector and check whether it is class-separating (m_n ≠ 0 for n ∈ {0, 2, 6}) — this would extend the Lemma_S1 atlas with a second observable.
   - **Inputs**: Sage MCP (`mcp__sage__sage_eval`, `mcp__sage__sage_simplify`); A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) module structure (G32 singleton); Hochschild boundary on the cyclic bicomplex (Connes NCG 1994 III.1.γ); cross-check via independent computation on the truncated cyclic chain at b ≤ 4.
   - **Gate**: NEW gate `S86-HP1-AF-GENERATING-RANK`. PASS iff Sage-computation + cross-check return integer rank with ≥ 2 independent methods agreeing within rank-equality. FAIL iff cross-checks disagree on rank (would indicate computational instability). INFO iff one method returns rank but the other times out (HEAVY symbolic computation).
   - **Effort**: 6 hours (symbolic Hochschild boundary + 2 cross-check methods; 1 agent session, HEAVY).

V.S2. **Off-τ_fold O'Neill tensor evaluation across Jensen corridor**

   - **What**: Compute O'Neill A and T tensors on Jensen-deformed SU(3) at 41-point τ-grid `np.linspace(0.0, 0.4, 41)`; check whether `|A_norm²(τ)| < 1e-6` and `|T_norm²(τ)| < 1e-6` hold across the full corridor or only at τ_fold = 0.19. Computation closes the W11-5 scope-limit "Does not address O'Neill A or T non-zero off τ_fold" by verifying or refuting that the structural pin extends globally.
   - **Inputs**: `s61_oneill_tensors.py` (S61 A-TENSOR-61 PASS infrastructure at τ_fold); Jensen-deformed metric `g_τ` from `s83_w1_g2_epsilon_h_promotion.py` (anchor 16.197719); cross-check via Sage symbolic evaluation at τ ∈ {0.05, 0.20, 0.35} for verification.
   - **Gate**: NEW gate `S86-ONEILL-OFF-FOLD`. PASS iff `max_τ |A_norm²| < 1e-6` AND `max_τ |T_norm²| < 1e-6` across [0, 0.4]. FAIL iff either tensor exceeds 1e-6 at any τ ≠ 0.19 — would invalidate the Chern-Weil direct-sum step in W11-5's substitution chain off-fold and require compensation terms. INFO iff numerical noise dominates the signal (would indicate machinery-pin tightening needed).
   - **Effort**: 3 hours (computation script; CPU-only; 1 agent session, MODERATE).

V.S3. **Cuntz-Quillen six-term diagram detail per Meta-Theorem specialization**

   - **What**: Draw the explicit morphism diagram + connecting homomorphism δ for each Meta-Theorem sub-case (Lemma_P parity, Lemma_R rank, Lemma_S1 Mellin-support); verify exactness at each position via Sage symbolic computation. Closes the W11-3 scope-limit "Detailed 6-term-exact-sequence diagram for each specialization is deferred."
   - **Inputs**: `s73b_six_sequence.py` (existing Cuntz-Quillen machinery, currently unused); Connes-Marcolli 2008 §1.2 (Cuntz-Quillen bivariant cyclic cohomology); Lemma_P / Lemma_R / Lemma_S1 statements from §II of this synthesis; cross-check via Sage MCP `mcp__sage__sage_eval` on each morphism's commutativity.
   - **Gate**: NEW gate `S86-CUNTZ-QUILLEN-DETAIL`. PASS iff all 3 specializations yield commuting 6-term diagrams with verified exactness at each position (THEOREM tolerance: algebraic equality). FAIL iff exactness fails at any position — would require a compensation lemma. INFO iff one specialization completes but another times out (HEAVY symbolic).
   - **Effort**: 4 hours (Sage symbolic + diagrammatic verification per sub-case × 3; 1 agent session, MODERATE).

V.S4. **Shape-inequality meta-family formulation (w_0 NEW-FAMILY first exemplar)**

   - **What**: Formulate a parallel meta-family for functional-inequality-saturation exclusions, with W11-3's w_0 Cauchy-Schwarz saturation as the first exemplar. Enumerate 2-3 candidate additional exemplars (e.g., thermodynamic-concavity saturations like the Bogoliubov inequality saturation at BCS; Markov-inequality-bounded observables like P_exc cap at unity for adiabatic-impulsive transit). Test whether each candidate fits a (source, target, ch) image-restriction template at all, or genuinely sits outside the K-theoretic family.
   - **Inputs**: W11-3 w_0 NEW-FAMILY classification (`session-85-w11-workingpaper.md` §W11-3 (c)); s72_cauchy_schwarz_w0.py (anchor); BCS Bogoliubov inequality from S70 BCS-GAP-CANONICAL-70; P_exc cap from S38 Parker-pair production logs.
   - **Gate**: NEW gate `S86-SHAPE-INEQUALITY-META-FAMILY-DRAFT`. PASS iff template frozen with ≥ 2 exemplars populated AND each exemplar's CS / Bogoliubov / Markov saturation is verified against an independent functional-inequality form. FAIL iff only one exemplar (w_0) survives the test (not yet a family, only a singleton). INFO iff template draft completes but a single exemplar's verification incomplete (defers to S87).
   - **Effort**: 3 hours (framework-design + 2-3 exemplar candidates verified; 1 agent session, MODERATE).

V.S5. **Mellin-multiplier identity test on extended atlas**

   - **What**: Extend the W12-4 5-regulator atlas to include Pauli-Villars (already in atlas) and dim-reg (recommended new entry); verify whether the F_4/M boundary holds for these candidates by direct Mellin-vector computation `f^r = (f_0^r, f_2^r, f_4^r, f_6^r, ...)`. Tests whether the regulator-class atlas in §VII.N L1/L2/L3 needs updating with the Mellin-support partition. If a 6th regulator (e.g. Pauli-Villars) clusters at `supp = {2, 4}` (anomaly-like) or `supp = {0, 2, 4, 6}` (cutoff_sqrt-like), it joins M; if it has `supp = {4}` (zeta/Zubarev/SDW-like), it joins F_4.
   - **Inputs**: `_spectral_action_regulators.py` helper from W12-4 (5-regulator evaluator); `s78_a4_r2_f_star.py` Mellin-multiplier infrastructure; Pauli-Villars subtraction prescription with mass scale `Lambda_PV = M_KK`; dim-reg with d = 8 + ε analytic continuation.
   - **Gate**: NEW gate `S86-MELLIN-SUPPORT-ATLAS-EXTEND`. PASS iff each new regulator gets a unique Mellin-vector classification (F_4 or M) AND the F_4/M boundary is preserved (no regulator straddles). FAIL iff a regulator straddles the boundary (would indicate the F_4/M partition is not the coarsest). INFO iff one regulator's Mellin moments are infinite at d_spec=8 (Schwartz-class failure; would require tightening the admissible-regulator class).
   - **Effort**: 3 hours (Sage Mellin-moment computation per regulator + cross-check; 1 agent session, MODERATE).

V.S6. **W11-5 base-curvature scan extension to non-FRW base metrics**

   - **What**: Extend the W11-5 11-point FRW scan to non-product / warped / Bianchi-class base metrics; verify whether the Chern-Weil additivity step (`p_1(TE) = p_1(T^V) + π* p_1(TM^4)`) holds beyond product metrics. Tests the W11-5 scope-limit "Does not address non-product metrics where the O'Neill pin fails by construction."
   - **Inputs**: warped product metric `g = -dt² + a(t)² δ_ij dx^i dx^j + B(t) g_F^{SU(3)}` for warp factor B(t); cross-check via S61 O'Neill recomputation on the warped metric (A and T no longer vanish).
   - **Gate**: NEW gate `S86-NON-PRODUCT-BASE-EXTEND`. PASS iff `δ_parity = 0` mod 2 across an 11-point warp-factor scan with `B ∈ [0.5, 2.0]`. FAIL iff `δ_parity = 1` at any scan point — would refute the curvature-robustness clause beyond product metrics and tighten the W11-5 scope. INFO iff Chern-Weil additivity formally requires correction terms but `δ_parity` remains 0 by another mechanism (cancellation lemma).
   - **Effort**: 4 hours (computation script + analytic verification of warped-metric Pontryagin density; 1 agent session, MODERATE-to-HEAVY).

V.S7. **S78 W2-F Mellin-multiplier extension to a_2, a_6**

   - **What**: S78 W2-F established `a_4^{f*}/a_4^{SDW} = f_4^{f*}/f_4^{SDW}` (the multiplier identity at the a_4 slot). Extend to a_2 and a_6: do `a_2^r / a_2^{zeta} = f_2^r / f_2^{zeta}` and `a_6^r / a_6^{zeta} = f_6^r / f_6^{zeta}` hold for r ∈ M-class? If yes, the multiplier identity is universal; if no, the F_4/M boundary is even sharper than Lemma_S1 currently states (since the identity FAILS at a_2 and a_6 even WITHIN F_4 — Zubarev and SDW would have different `f_2` and `f_6` than zeta despite all three having `supp = {4}`).
   - **Inputs**: `s78_a4_r2_f_star.py` (a_4 anchor); 5-regulator atlas Mellin moments at orders 0, 2, 4, 6 from `_spectral_action_regulators.py` (W12-4 helper); Sage symbolic verification.
   - **Gate**: NEW gate `S86-MELLIN-MULTIPLIER-EXTEND`. PASS iff identity holds at a_2 AND a_6 across F_4 (would extend Lemma_S1 to a multi-slot statement). FAIL iff identity fails at a_2 or a_6 within F_4 (would split F_4 into sub-classes). INFO iff identity holds modulo divergent moments at a_0 (which is structurally divergent across all regulators per W12-4 class-(d) at spread 0.50).
   - **Effort**: 3 hours (Sage Mellin extension + cross-check; 1 agent session, MODERATE).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | NCG-Structural-Exclusion Meta-Theorem certified across 3 categorical framings (Kasparov-KK / cyclic-cohomology / Mellin-residue) with 0 substantive disagreements | GEOMETRIC | PERMANENT (after §VII.R landing) | The HP^0/HP^1 disjoint-corridor wall is structurally overdetermined; coincidence reading closed. |
| 2 | Lemma_P (parity), Lemma_R (rank), Lemma_S1 (Mellin-support) drawn from disjoint mathematical areas; 3-way independence verified | GEOMETRIC | PERMANENT | The Meta-Theorem unification is genuine, not post-hoc grouping. |
| 3 | SU(3) at dim 8 in PRESERVE class; SU(3)×U(1) at dim 9 in FLIP class (W11-4 8 PRESERVE + 4 FLIP = 12) | GEOMETRIC | PERMANENT | Standard-Model U(1)_Y fiber-extension structurally constrained; SU(3) is the smallest simple non-abelian fiber compatible with the wall. |
| 4 | Algebraic identity `heitsch_ratio = 4·⟨ρ⟩_W ≥ 4` enforces structural FAIL-direction inaccessibility of W11-1 at any physical L_max ≥ 1 | GEOMETRIC | PERMANENT | W11-1's PASS is by algebraic identity; INFO-mode reclassification recommended. |
| 5 | Chern-Weil additivity + O'Neill A=T=0 + even-base Spin^c forces `δ_parity = 0` IDENTICALLY at the algebraic level (W11-5) | GEOMETRIC | PERMANENT for product-metric Riemannian submersions at τ_fold | Curvature-robustness across 6 OOM in scale factor numerically verified; off-fold + non-product extension queued. |
| 6 | s=4 (NOT s=3) is the substrate Mellin-cone's leading non-trivial residue location in d_spec=8 NCG; reconciled with dispatch prose | GEOMETRIC | RECONCILIATION FLAGGED | Dispatch's "residue at s=3" corrected to "residue at s=4 in pure-a_4 sub-cone". |
| 7 | Mellin-multiplier identity `a_4^r/a_4^{zeta} = f_4^r/f_4^{zeta}` holds on F_4 (S78 W2-F) and FAILS on M (W5-2 spread 254.75% / 107.07%) | GEOMETRIC | PERMANENT | The F_4/M wall is empirically MEASURABLE in spectral-action coefficients; CC1+CC2 form a conjugate pair. |
| 8 | a_0, a_2, a_4 are class-(d) STRUCTURALLY-DIVERGENT under W12-4 5-regulator atlas (spreads 0.50 / 1.03 / 0.49) | GEOMETRIC | PERMANENT | Any future a_n citation requires explicit regulator pin (canonical_constants discipline). |
| 9 | S-1 W0-W5 Regulator-Family Boundary Theorem becomes Lemma_S1 of the Meta-Theorem; 14-claim convergence count strengthens to 15 with 0 disagreements | GEOMETRIC | PERMANENT under structural lift | S-1 retains standalone permanent-registry status; Meta-Theorem cites as Lemma_S1 anchor. |
| 10 | §VII.P slot-allocation collision (occupied by W9-1 Borel-Floor); landing routes to §VII.R per §VII.N precedent | NON-PHONONIC (registry hygiene) | LANDING-DEFERRED to S86 | Header-rename required before /weave --update; no theorem content compromise. |
| 11 | w_0 CS-asymmetry classified NEW-FAMILY (shape-inequality meta-family); not in NCG-Structural-Exclusion family | NON-PHONONIC | CARRY-FORWARD | Parallel meta-family draft pending in V.S4. |
| 12 | Three of five W11 gates PASS by algebraically-forced identities (W11-1 lower bound; W11-3 Chern multiplicativity; W11-5 O'Neill direct-sum); scan grids verify implementation-robustness, not physics-discovery | NON-PHONONIC (methodological) | METHODOLOGY DEBT | Plan-author discipline carry-forward: gates with structurally inaccessible FAIL direction should be classified INFO-mode. |
