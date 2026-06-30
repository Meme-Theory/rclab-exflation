# WS-S113-3 CCRESID — lizzi-spectral-functional-theorist, Round 1

**Workshop**: WS-S112-3 CCRESID (Session 113 EVOI-frontier campaign; schedule `sessions/session-112/session-112-workshop-schedule.md` §WS-S112-3)
**Role**: lizzi-spectral-functional-theorist — Round 1, steelman **Reading B** (the residual is a genuine a₀ spectral-moment discrepancy the Volovik effacement partition cannot absorb; the BBN arm is a distinct constraint)
**Pole**: Reading-B (I do not see volovik's Reading-A until R2)

**One-line thesis**: The DILUTION-CC closure is a tracking statement about the *dynamical* vacuum energy density ρ_vac(H) ∝ M_Pl²H²; the residual 3.2 % and the a₀ Seeley-DeWitt zeroth moment that *defines* the cosmological-constant channel are two different spectral functionals of D_K, the former algebra-DEPENDENT (state-pair / occupation) and the latter algebra-INVARIANT (mode-count, FUNCTIONAL-INDEPENDENT, τ-independent) — so no higher-order effacement term, which lives entirely in the dynamical-tracking sector, can reach into the a₀ channel to close the residual; and the S110-hardened BBN arm (2.087× over-production, all relief routes closed) is the independent, *w*-free proof that the tracking mechanism has already exhausted its closure freedom.

---

## 0. What "the residual" actually is (pinning the object before arguing about it)

Three numbers, all canonical, all from the knowledge MCP (queried first per `CLAUDE.md`):

| Object | Value | Provenance | Spectral-functional class |
|:--|:--|:--|:--|
| Present-epoch residual | ρ_vac/ρ_obs − 1 = **4/125 = 0.0320 = +3.2 %** (Sage-QQ exact) | `get_constant rho_vac_over_rho_obs = 1.032`; DILUTION-CC-66 (S66) | a₀-channel ratio (see §2) |
| BBN-epoch realization | (ρ_vac/ρ_rad)_BBN = **0.474049** vs bound 0.227107 ⇒ **2.087× over** | `get_constant rho_vac_over_rho_rad_BBN_below`; S98-MK3-2 audit `1ad846b2` | same a₀ ratio, evaluated at H_BBN |
| BBN over-production / present-residual | **33.98×** (Sage-QQ exact) | derived this R1 | — |

The DILUTION-CC theorem (PROVEN, S66) is exactly and only this: **ρ_vac ~ M_Pl² H²** (Volovik q-theory tracking; `Phononic-framework-hypothesis.md`, CC_OOM = 115.5). It closes the 114-OOM gap to **0.01 OOM** — i.e. to within ρ_vac/ρ_obs = 1.032. The "residual 3 %" is the gap between 1.032 and 1.000. The capstone `project_dilution-cc-priority` records this honestly: "only residual-3% underived."

The contested question is what *kind* of object that 3 % is. Reading A says it is a computable higher-order term of the *tracking* partition (the Γ_eff = 0.99970 effacement mechanism extends to close it). Reading B — my pole — says it is a residual in the **a₀ spectral-moment channel**, structurally walled off from the tracking sector by the Spectral-Moment Decoupling Theorem, so no effacement higher-order term can touch it.

---

## 1. The CC *is* the a₀ zeroth spectral moment — and a₀ is FUNCTIONAL-INDEPENDENT and τ-independent

This is the foundation. In the spectral action the cosmological-constant term is the a₀ Seeley-DeWitt coefficient:

```
S_b(D_K, Λ) = Tr f(D_K²/Λ²) ~ f_4·Λ⁴·a_0(D_K²) + f_2·Λ²·a_2(D_K²) + f_0·a_4(D_K²) + …
              a_0  →  cosmological constant  (vacuum energy, Λ⁴ prefactor)
              a_2  →  Einstein–Hilbert       (Newton's constant)
              a_4  →  Yang–Mills + Higgs
```

(`s86-alpha-s-tension-and-sign-lock.md`; `phononic-framing.md`: "vacuum energy = a₀, a DIFFERENT spectral moment than gravity a₂".)

Two PROVEN structural facts about a₀ are the load-bearing walls of Reading B:

**(a) a₀ is FUNCTIONAL-INDEPENDENT (the mode count).** Canonical `a_0_FW_zeta = 6440.0` is the **dimensionless mode count** — `ζ_{D_K}(0)`, the substrate's total spectral weight (`canonical_constants_provenance_edges`: "substrate dimensionless mode count"; `baseline-findings-s66`: "Mode count (τ-independent)"). The S66 mack-qa workshop states it verbatim: **"a_0 = 6440 is topological and tau-independent (FUNCTIONAL-INDEPENDENT)."** Every spectral functional — cutoff √x, zeta, anomaly-derived, f* — sees the *same* a₀, because it is a count of eigenvalues, not a moment-of-a-weighting. This is the heat-kernel a₀ = ∫√g d⁴x · 1, the volume term; it has no f-dependence at all.

**(b) Spectral-Moment Decoupling Theorem (S75 W2-E, PROVEN; atlas-07 permanent).** The coefficients a₀(τ), a₂(τ), a₄(τ) are **algebraically independent** as functions of the Jensen modulus τ: `P(a_0, a_2, a_4) = 0` has only the trivial solution, the Wronskian is nonzero (`session-75-results-workingpaper`; S75 W2-E PASS, MIGRATED INFO S81 `55a1b9e0`). They are different curvature-polynomial degrees (degree 0, 2, 4) — "algebraically independent, Wronskian nonzero." There is no polynomial relation by which a deformation of one moment induces a deformation of another.

The consequence for the CC: **the a₀ channel cannot be moved by anything that acts on the dynamical sectors.** a₀ is fixed by the eigenvalue *count* at the fold; it is τ-independent (it does not even flow under the Jensen deformation that drives everything else, `dS/dτ = +58,673`); and it is decoupled from a₂/a₄ by an exact theorem. If the residual 3 % is an a₀-channel discrepancy, it is the most rigid object in the framework — a FUNCTIONAL-INDEPENDENT, τ-frozen, algebraically-isolated number.

---

## 2. The decisive structural wall: the tracking mechanism and the a₀ moment are *different spectral functionals*

Now the central argument. The atlas-04 **S3** assumption cell carries the cleanest statement of the wall, in the framework's own words (S37, PROVEN-adjacent):

> "SA penalizes BCS pairing (wrong sign, +12.76 anti-trapping, 93×). **The spectral action is a spectral moment, not a total energy.** The BCS condensation energy is a Fock-space quantity. **These are categorically different functionals.**"

This is the template for Reading B. Translate it to the CC sector:

- The **a₀ moment** is `Σ_k m_k g(λ_k)` with g ≡ 1 — a **spectrum-only, algebra-INVARIANT functional** (Corner I/II of the algebra-axis orthogonality classification, `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, MANDATORY at K=3). It is a property of the bare D_K eigenvalue list.
- The **Volovik tracking vacuum** ρ_vac = ε(q) − μq is a **state-pair / occupation functional** on the q-variable thermodynamics — an **algebra-DEPENDENT** object. The S97 W-1 adjudication (mack+volovik converged) classifies C10 explicitly as a two-layer row with **Layer 2 = "occupation-SENSITIVE … algebra-DEPENDENT"** and Cross-layer co-primary **FORBIDDEN** by the very same algebra-axis orthogonality clause.

The two layers are **STRUCTURALLY ORTHOGONAL** — that is the framework's own settled verdict on C10, not my invention. The S97 W-1 row reads: *"C10 disposition is a STRUCTURAL-ORTHOGONAL-COMPANION two-layer row (S94 W-1 pattern; algebra-axis orthogonality)."*

**Effacement lives entirely in Layer 2.** Γ_eff = 0.99970 is the impedance-mismatch leakage of the *tracking* vacuum (`phononic-framing.md`: "dark energy = impedance-effacement leakage at a₂"; w₀_FW = −0.918 from "Volovik vacuum partition + effacement"). It is an a₂-sector / G_N-normalization phenomenon (the S110 WS-CC-H₀ workshop pins this: the H₀-degeneracy "is the H-sector face of the rank-1 w = M_KK import … an a₂-sector / G_N-normalization question"). A "higher-order effacement term" is, by construction, a higher-order term in the *occupation-sensitive, algebra-DEPENDENT, a₂-coupled tracking* sector.

**Therefore a higher-order effacement term cannot reach the a₀ residual.** To close a residual in the algebra-INVARIANT a₀ mode-count channel, you would need a correction in that channel. The effacement mechanism is structurally in the orthogonal (algebra-DEPENDENT, a₂-coupled) channel. By the algebra-axis orthogonality K=3 MANDATORY clause, no amount of refinement in one channel produces content in the other. **Reading A asks the effacement mechanism to do something its own structural classification forbids.**

### Functional-sensitivity corollary (my domain's signature contribution)

This is where the spectral-functional-pluralism lens sharpens the verdict beyond the existing C10 layering. Ask: *under which spectral functional is the residual 3.2 % computed?*

- The DILUTION-CC ratio ρ_vac/ρ_obs = 1.032 is anchored to the **a₀ = 6440 zeta mode-count** (`get_constant rho_vac_over_rho_obs`: "a_0 Seeley-DeWitt zeroth moment tracks the Volovik H²-scaling vacuum"). Because a₀ is FUNCTIONAL-INDEPENDENT, **the 3.2 % residual is the same in every spectral scheme** — cutoff, zeta, anomaly, f*. There is no functional choice that makes it smaller. Contrast every other CC-sector number, which is maximally SCHEME-DEPENDENT (my permanent record: CC gap 120.5 OOM cutoff / 117.3 OOM zeta; eps_H sign flips; m_H spans 100.5→138.5; `permanent_theorems.md §"SCHEME-DEPENDENT (MAXIMALLY) RESULTS"`). The residual's **functional-independence is the fingerprint of an a₀-channel object**, not a tracking-sector object (tracking-sector quantities like w₀ and Γ_eff are scheme-tunable; the residual is not).
- This is a **FUNCTIONAL-INDEPENDENT / SCHEME-DEPENDENT partition** statement, the canonical output of my methodology: the residual *value* (3.2 %) is FUNCTIONAL-INDEPENDENT (it is locked to the mode-count a₀), while the tracking-sector closure freedom (Γ_eff, w₀) is SCHEME-DEPENDENT (it can be tuned within the tracking functional). A scheme-dependent knob cannot move a scheme-independent number. **That mismatch is the structural reason the closure cannot exist.**

---

## 3. The BBN arm (Q29) is independent — and it is the *w*-free proof that closure freedom is already exhausted

The workshop's second question: is Q29 (BBN-epoch) independent or coupled? **Independent**, and it does the heavy lifting that converts "the closure is structurally hard" into "the closure cannot exist within the tracking mechanism."

**Independence.** The present-epoch residual and the BBN arm are evaluated at two epochs separated by `X = ln(H_BBN/H_0) = 40.2756` (S98). At z = 0 the tracking lever is `X^(n−2) = 1^0 = 1` (sign-INSENSITIVE, 60-bit; C10 cell), so the present residual is blind to the sub-leading anharmonic structure. At BBN the lever is `X^(n−2)` with n_eff = 1.978 from-below — fully sensitive to the same structure. **The two arms probe different moments of the same tracking law**: present-epoch tests the leading H² coefficient; BBN tests the *exponent* n_eff and the sub-leading sign. They cannot both be closed by one knob — closing one re-opens the other unless the *entire* ρ_vac(q) functional is correct to all orders, which is precisely what is in question.

**The exhaustion result (S110-hardened).** Every additional-relief route to the BBN arm has been tested and **FAILED**:

- S98-MK3-2 BBN vacuum fraction: **FAIL** (`1ad846b2`) — relief *direction* confirmed (from-below), magnitude insufficient: 0.474 > 0.227, ΔN_eff = 2.087 > 1.
- S99-W2-BBN-RELIEF: **FAIL** (`8fe0ef45`) — additional-relief corridor **CLOSED STRUCTURAL** (~2.087× over; Q29 atlas-08 status: "CORRIDOR CLOSED (structural)"). Both relief mechanisms quantified and insufficient: mech-a needs an a_n shift ×1.835; mech-b needs α_V relief 0.479 — neither available.
- S99 litrev x C10 vacuum-profile: time-profile ("ρ_vac absent at BBN, built later") **STRUCTURALLY CLOSED for the tracking vacuum**; epoch-dependent α_V ("α_V halves at BBN") **CLOSED**.

The S110 WS-CC-H₀ workshop (volovik × einstein, CONVERGED) then delivers the sentence that, on my reading, *settles this entire CCRESID workshop in Reading B's favour* — and it was co-authored by my Reading-A opponent's own agent:

> **"The H-sector's ONLY w-free falsifiable observable is the BBN ΔN_eff = 2.06× (a₀ ratio ρ_vac/ρ_rad, w cancels; S98 audit 1ad846b2, 0.474 > 0.227, n_BBN ≈ 2) — and it FAILS."** (atlas-04 C10 cell, S110 WS-CC-H₀.)

Read that carefully against Reading A. The *one* place where the tracking mechanism makes a prediction that does **not** hide behind the un-fixed w = M_KK import — the **a₀ ratio** ρ_vac/ρ_rad, where w cancels — is BBN, and there the mechanism **over-produces by 2.06× and fails by >3σ**. The tracking partition is not a mechanism with spare closure capacity that merely needs a higher-order push to mop up a 3 % present-day residual; it is a mechanism whose *only clean, w-free, a₀-channel test* it already **fails by a factor of two**. Asking it to additionally close the present-epoch a₀ residual via a higher-order term is asking more of a mechanism that has already over-spent its budget on the test that actually probes the a₀ channel cleanly.

**Quantitative nail (Sage-QQ exact, this R1).** The BBN over-fraction (2.087 − 1 = 1.087 = +106 %) is **33.98× larger** than the present-epoch residual (3.2 %). If a single higher-order effacement term closed both — Reading A's claim — it would have to simultaneously (i) supply +3.2 % at z = 0 where the lever is exactly 1 and (ii) *remove* +106 % at BBN where the lever is X^(n−2). One additive correction cannot be +3.2 % and −106 % at two epochs of the same monotone tracking law unless its epoch-dependence is fine-tuned to ~34:1 — which is not "a computable higher-order term," it is a second free function. The structure forbids the single-term closure.

---

## 4. Engaging the strongest threat to Reading B (honest steelman of Reading A's best case)

I am required to engage the strongest threat: **a genuine higher-order effacement term that DOES close the residual.** Here is the most dangerous version of Reading A, and where I think it actually lands.

**The threat, stated at full strength.** C10 was *sharpened* at S97 W2-2: the tracking law's scaling exponent "2" is now **substrate-derived** from the spectrum — ρ_vac(q) = ε − q·dε/dq has a q-stationary minimum with curvature **k = +3586.5 M_KK**, computed directly from the 992 D_K eigenfrequencies (T.61), reproducing E_ZP(0) = 81493.046. So the tracking vacuum is *not* an external phenomenological ansatz bolted onto the spectral action — its leading structure is **computed from D_K**, i.e. from the same eigenvalue data that gives a₀. If ρ_vac(q) is a genuine spectral-action object, then its **sub-leading** terms (the C_meas = −0.0219 anharmonic correction, n_eff = 1.978 from-below) are *also* spectral-action objects — and a sufficiently complete computation of ρ_vac(q) to higher order in q might reproduce the missing 3.2 % from first principles. That would be Reading A vindicated: the residual is a computable higher-order term of the (substrate-derived) tracking partition.

**Why I think the threat sharpens Reading B rather than defeating it.** Two reasons, in order of force.

1. **Even if ρ_vac(q) is fully spectral, its higher-order terms live in the q-thermodynamic (Layer-2, occupation-sensitive, algebra-DEPENDENT) functional — not the a₀ mode-count.** The S97 curvature k = +3586.5 is "occupation-INSENSITIVE" *only at leading order* (Layer 1); the C10 cell is explicit that the sub-leading sign C_meas and the BBN realization are "**occupation-SENSITIVE … algebra-DEPENDENT**" (Layer 2). So the higher-order term Reading A needs is, by the framework's own classification, an algebra-DEPENDENT correction. The residual it must close is, by §1, in the algebra-INVARIANT a₀ channel. The orthogonality clause (K=3 MANDATORY) says these do not mix. The substrate-derived sharpening of the *leading* term does not transport to the a₀ channel; it makes the *Layer-2 tracking law* more rigid, which is the opposite of giving it closure freedom. **A more-determined tracking law has *less* room to absorb a residual, not more.**

2. **The BBN arm is the empirical referee, and it has already ruled.** This is decisive and is what tips my honest lean. Reading A's "computable higher-order term" is not a free conjecture — it makes a *prediction* at the one epoch where the a₀ ratio is testable w-free: BBN. If the higher-order completion of ρ_vac(q) supplied the +3.2 % at z = 0, the *same* completion fixes the BBN realization, because it is the same function evaluated at a different H. The framework has computed that BBN realization to the available order and found **2.087× over-production**, with **every relief corridor closed structurally** (S99 CORRIDOR CLOSED). So the higher-order completion, evaluated where it can be checked, does **not** land on the data — it misses by a factor of two in the wrong direction. A closure term that fixes the unobservable 3 % but breaks the observable BBN constraint is not a closure; it is a re-parameterization that fails its only test. **The threat is real in principle but already falsified in practice by Q29.**

So the strongest Reading-A case forces the question onto the BBN arm — and the BBN arm answers it against closure. That is exactly why Q29 is *independent and load-bearing*, not a side-constraint.

**One caveat I will not hide** (it is the seam Reading A will press in R2): the present-epoch residual itself has never been *directly computed* as a failed a₀ higher-order term — it is the *gap to closure* of a tracking law, inferred, not measured against an a₀ first-principles prediction. The DILUTION-CC closure is a magnitude/scaling match (ρ_vac ~ M_Pl²H² to 0.01 OOM), not a derivation of ρ_obs from a₀ to 3 % precision. So Reading B's claim is strictly: *the residual is in a channel (a₀) that the closure mechanism (effacement/tracking, a₂-coupled) cannot structurally reach, and the one place the a₀ channel is cleanly testable (BBN) shows the mechanism has no closure budget.* It is **not** the stronger claim that someone has computed a nonzero a₀ higher-order term equal to 3.2 %. The honest registry tag is therefore a *standing limitation*, not a *refuted closure*.

---

## 5. What the right verdict looks like (pre-registrable)

Reading B's structural verdict, stated for adjudication:

**The residual-3% CC is a standing CC-sector limitation in the a₀ spectral-moment channel, structurally walled off (Spectral-Moment Decoupling Theorem S75 W2-E + algebra-axis orthogonality K=3 MANDATORY) from the Volovik/effacement tracking sector that closes the 114 OOM. No higher-order effacement term — which is by construction an occupation-sensitive, algebra-DEPENDENT, a₂-coupled correction — can reach the algebra-INVARIANT, τ-independent, FUNCTIONAL-INDEPENDENT a₀ channel. Q29 (BBN-epoch) is an INDEPENDENT arm probing a different moment (the exponent n_eff) of the same tracking law; it is the *w*-free a₀-ratio test, and it FAILS at 2.087× over-production with all relief corridors CLOSED-STRUCTURAL (S99), proving the tracking mechanism has no spare closure budget.**

The pre-registrable consequence (a falsifier, in Reading-B's favour, not a closure gate):
- The residual is FUNCTIONAL-INDEPENDENT (locked to a₀ = 6440 mode-count). A pre-registrable gate: compute the residual ρ_vac/ρ_obs under {cutoff, zeta, anomaly, f*}; PASS-Reading-B if the 3.2 % is scheme-invariant to <0.1 % (confirming a₀-channel, closure-immune); the alternative (scheme-dependent residual) would license Reading A by showing the residual is a tracking-sector, hence tunable, object. My prior is strongly that it is scheme-invariant (a₀ is FUNCTIONAL-INDEPENDENT by theorem) — i.e. this gate, if run, confirms Reading B.

---

## (i) Honest current lean

**Reading B, ~0.72.** The structural walls are real and PROVEN (Spectral-Moment Decoupling S75 W2-E; a₀ FUNCTIONAL-INDEPENDENT/τ-independent; algebra-axis orthogonality K=3 MANDATORY; C10's own two-layer ORTHOGONAL-COMPANION classification with cross-layer co-primary FORBIDDEN). The BBN arm is the decisive empirical referee and it has ruled against closure *at the one clean a₀-channel test* (S110 WS-CC-H₀, co-authored by Reading-A's own agent: the only w-free a₀ observable "FAILS"). I hold back from a higher number because of the §4 caveat: the present 3 % has not been computed as an explicit failed a₀ higher-order term, so Reading B is a "channel-orthogonality + exhausted-budget" argument, not a "we computed the residual and it is irreducible" argument — that gap is where a determined Reading A can still operate, and I want to see volovik's best higher-order-term construction before going past 0.72.

## (ii) Single most decisive consideration

**The only w-free, a₀-channel test of the tracking mechanism is BBN, and it fails by 2.06× with every relief corridor closed structurally (S98 `1ad846b2`, S99 `8fe0ef45`).** Present-epoch closure of a₀ would have to come from the same tracking functional that, evaluated where it is cleanly testable, over-produces by a factor of two. A closure term that fixes the unobservable 3 % residual but worsens the observable BBN constraint is not a higher-order closure — it is a second free function. The mechanism has no spare closure budget; the residual is therefore a genuine a₀-channel limitation, not a higher-order effacement effect.
