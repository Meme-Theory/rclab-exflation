# WS-S112-3 CCRESID — Round 2 (rebuttal)

**Author:** volovik-superfluid-universe-theorist — Round 2, rebuttal
**Pole entering R2:** Reading A (higher-order q-channel closure of the present-epoch residual)
**Read:** lizzi-r1.md (Reading B — the residual is a genuine a₀ spectral-moment discrepancy the effacement partition cannot absorb; BBN is the independent *w*-free referee).

**One-line:** lizzi's case is strong and I update materially. I REBUT the channel claim — the residual is NOT an a₀ mode-count object (her scheme-invariance argument is necessary-not-sufficient; the residual's `Ω_m²` scaling is the discriminator a₀-channel cannot carry). But I CONCEDE her real nail in sharpened form: the BBN arm over-constrains the **leading** tracking coefficient `α_V`, and that over-constraint is upstream of — and unrescued by — any clean second-order q-residual. The net is not "Reading A vs Reading B" but a SPLIT: right channel (q, Reading A), over-constrained calibration (the *substance* of Reading B's BBN nail, re-derived on a different structural basis than a₀-orthogonality).

---

## 1. Where lizzi is RIGHT (stated first, in full)

I will not contest what is correct. Three of lizzi's points stand:

1. **The CC channel in the spectral action IS the a₀ Seeley-DeWitt moment**, a₀ is FUNCTIONAL-INDEPENDENT (the `ζ_{D_K}(0) = 6440` mode count) and τ-independent, and the Spectral-Moment Decoupling Theorem (S75 W2-E, PROVEN) makes a₀/a₂/a₄ algebraically independent. All true. If the residual were an a₀-magnitude object, it would be closure-immune. I accept the wall as stated.

2. **The C10 cell files itself as a two-layer STRUCTURAL-ORTHOGONAL-COMPANION row** with cross-layer co-primary FORBIDDEN (algebra-axis orthogonality K=3 MANDATORY). True, and I co-authored that classification. Layer 1 (curvature `k = +3586.5 M_KK`, occupation-INSENSITIVE, algebra-INVARIANT) and Layer 2 (sub-leading sign, occupation-SENSITIVE, algebra-DEPENDENT) do not mix.

3. **The BBN arm is the empirical referee and it has ruled against the tracking mechanism at the one `w`-free test.** `(ρ_vac/ρ_rad)_BBN = 0.474 > 0.227`, ΔN_eff = 2.087, over-production 2.06×, all relief corridors CLOSED-STRUCTURAL (S99 `8fe0ef45`). I co-authored the S110 sentence lizzi quotes. This is the strongest thing in either R1, and I engage it head-on in §3.

Where I part company is the **inference from (1)+(2) to "the residual is an a₀ object"**, and the inference from (3) to "therefore no higher-order closure can exist at all." The first is a channel mis-assignment; the second over-reaches what BBN actually constrains.

---

## 2. REBUTTAL of the core claim: the residual is q-channel, not a₀-channel — scheme-invariance is necessary, NOT sufficient

Lizzi's signature contribution (§2 corollary, her home domain) is: the residual `4/125 = 0.032` is anchored to `a₀ = 6440`, a₀ is FUNCTIONAL-INDEPENDENT, therefore the residual is **scheme-invariant** (same under cutoff / zeta / anomaly / f*), and a scheme-*dependent* knob (Γ_eff, w₀) cannot move a scheme-*independent* number. That mismatch, she argues, is "the structural reason the closure cannot exist."

The argument has a precise logical gap, and it is decisive. **Scheme-invariance is necessary for an a₀-channel object, but it is NOT sufficient — because a q-channel ratio is ALSO scheme-invariant.** Here is why (Sage-QQ exact, this R2):

The DILUTION-CC tracking law is `ρ_vac(H) = α_V M_Pl² H²` (Volovik q-theory; `Phononic-framework-hypothesis.md`). Look at what is actually in this expression: `α_V` (a dimensionless tracking coefficient), `M_Pl²`, `H²`. **There is no a_n Seeley-DeWitt moment in it at all.** It is the Gibbs–Duhem gravitating object `ε(q) − q dε/dq` evaluated on the q-variable, scaling as `H²`. The `a₀` magnitude does NOT appear — and per Volovik Paper 04 §IV (and lizzi's own §1), the a₀ magnitude does *not gravitate at equilibrium* (`ρ_vac = ε − Σμ_a N_a = 0`, trans-Planckian modes cancel sub-Planckian). So:

- `ρ_vac(today) = α_V M_Pl² H_0²` — a **q-channel** quantity, built from `α_V` and a dimensionful scale, containing **zero** a_n moments.
- A ratio of two such quantities (`ρ_vac/ρ_obs`, or a 2nd-order/1st-order q-term ratio) is **automatically scheme-invariant** — not because it is locked to the a₀ mode-count, but because it contains no spectral functional to be scheme-dependent in the first place.

So lizzi's observation "the residual is the same in every scheme" is fully consistent with Reading A. Both an a₀-ratio and a q-channel ratio are scheme-invariant. Scheme-invariance does **not** discriminate the two readings. Her corollary establishes necessity (an a₀ object *would* be scheme-invariant) but reads it as sufficiency (scheme-invariant *therefore* a₀). That is the gap.

**The actual discriminator — and it points at Reading A.** What distinguishes a₀-channel from q-channel is **`Ω_m`-dependence**, and lizzi's functional-independence lens structurally cannot address it, because `Ω_m` is an *observational input*, not a spectral functional. The a₀ mode-count `ζ_{D_K}(0) = 6440` has **zero `Ω_m` dependence** — it is a count of eigenvalues, fixed at the fold, blind to the present matter content. So:

```
Sage-QQ exact (this R2):
  residual = 4/125 = 0.0320
  residual / Ω_m²  = 0.3225   (Ω_m = 0.315; coefficient ≈ 1/3)
  residual / Ω_m¹  = 0.1016
```

If the residual tracks `Ω_m²`, it **cannot** be the a₀ mode-count ratio (which is `Ω_m`-independent). It tracks the present matter content, which is exactly the signature of the second-order q-theory matter perturbation `δρ_vac ~ ρ_m²/χ_q` (Klinkhamer–Volovik Paper 13 Eq.24; `ρ_m ∝ Ω_m`). The `Ω_m²` scaling is in the q-channel by construction and absent from the a₀-channel by construction. **This is the discriminator, and it survives lizzi's entire §2.**

So Reading B's central structural claim — "the residual is in the a₀ channel, walled off by Spectral-Moment Decoupling" — is **mislocated**. The residual is in the q / Gibbs–Duhem channel (Layer 2 of the C10 cell, the occupation-sensitive algebra-DEPENDENT layer), where the effacement/tracking mechanism *also* lives. The Spectral-Moment Decoupling Theorem walls off the a₀ *magnitude*; it says nothing about a ratio of q-thermodynamic quantities, because that ratio is not an a_n moment. Lizzi's wall is real but it is around a different object than the residual.

**Anticipating lizzi's strongest counter (her §4 point 1):** she will say the higher-order q-term is itself Layer-2 / algebra-DEPENDENT, and the residual-to-close is algebra-INVARIANT a₀, so orthogonality still forbids the closure. My answer: that argument *presupposes* the residual is a₀-channel — which is exactly the premise I have just refuted via `Ω_m²`. If the residual is Layer-2 q-channel (as its `Ω_m²` scaling shows), then closing it with a Layer-2 q-term is *within the same channel*, and orthogonality is silent (orthogonality forbids cross-channel mixing, not within-channel closure). Her §4-pt1 is only valid under the channel assignment I have shown to be wrong.

---

## 3. The BBN nail — engaged on its own terms, and CONCEDED in sharpened (different) form

This is where lizzi does real damage, and where I update. Her §3/§4-pt2 nail: a single higher-order term cannot supply `+3.2%` at z=0 (lever `X^(n−2) = 1`) AND fix the `+106%` BBN over-production at `H_BBN` (lever `X^(n−2)`) without a fine-tuned ~34:1 epoch-dependence = "a second free function."

I tested this honestly (Sage-QQ exact, this R2). The result splits into a part I rebut and a part I concede.

### 3.1 What I rebut: the "same object at two epochs / 34:1 second free function" framing

Lizzi's nail assumes the present residual and the BBN over-production are **one function evaluated at two epochs**. They are not — they are **different orders** of the q-expansion:

- **BBN over-production is a LEADING-order (1st-order) failure**: it tests the *exponent* `n_eff = 1.978` and the *coefficient* `α_V` of the `α_V M_Pl² H²` law itself (S98: `n_eff` from-below, lever `X^(n−2) = 0.9223`). At BBN, radiation dominates and `ρ_m/ρ_crit ~ 1`, so this is the leading tracking term being mis-normalized at high H.
- **The present residual is a SUB-LEADING (2nd-order) correction** at fixed leading law: `δρ ~ ρ_m²/χ_q`, the `Ω_m²` term, evaluated at low H where `Ω_m = 0.315`.

These are not the same object. Lizzi's "34:1 fine-tuning ⇒ second free function" is computed by treating both as `ρ_vac/ρ_X` at two epochs of one monotone law. But the present 3.2% is not the leading law at z=0 (the leading law at z=0 *is the 1.000 part* — it is correct); it is the next term. So the `33.98×` ratio is comparing a 1st-order failure to a 2nd-order residual — different rungs of the expansion, not one function fine-tuned 34:1. **Her "second free function" conclusion does not follow**, because the two arms are already different terms, not two evaluations of one term.

### 3.2 What I CONCEDE: the over-constraint on the LEADING coefficient α_V (lizzi's real nail, re-derived)

But the rebuttal in 3.1 does **not** save Reading A, and here is the honest concession. The BBN failure constrains the **leading coefficient `α_V`**, and that constraint is *upstream* of my second-order residual. I checked what happens if BBN is relieved (Sage-QQ exact, this R2):

```
S99 mech-b: BBN relief requires α_V → α_V·(1 − 0.479)  [relief factor 0.479]
Present ρ_vac/ρ_obs scales LINEARLY with α_V:
  1.032 → 1.032 × (1 − 0.479) = 0.538   ⇒ present closure UNDERSHOOTS by ~46%
```

So the leading coefficient `α_V` is **over-constrained across the two epochs**: the value that lands present-epoch closure (`ρ_vac/ρ_obs = 1.032`) over-produces at BBN by 2.06×; the value that would fix BBN under-produces today by ~46%. There is no single `α_V` consistent with both. This is real, and a clean second-order q-residual does **not** rescue it — because the conflict is in the *first-order* coefficient, and the second-order term `ρ_m²/χ_q` is a small correction on top of whatever leading value you pick. Fixing the 3.2% residual at z=0 with a q-term leaves the BBN over-production of the leading term entirely intact.

This is the substance of lizzi's case, and I concede it. But note carefully **what it is and is not**:

- It is **NOT** the a₀-orthogonality argument (lizzi's stated mechanism). The over-constraint is on `α_V` (a Layer-2 q-channel coefficient), not on an a₀ magnitude. Both arms are in the q-channel; the over-constraint is *within* the q-channel, between its leading coefficient at two epochs. So lizzi reaches the right conclusion (the tracking mechanism is over-constrained) through the wrong structural mechanism (a₀-orthogonality). The correct mechanism is leading-coefficient over-constraint across epochs.
- It does **NOT** make the present residual an a₀ object. The present residual remains a q-channel `Ω_m²` term. What it makes is the *leading tracking law itself* unable to fit both epochs — which is a statement about the tracking law's calibration, not about which channel the present residual lives in.

So the honest synthesis: **the present-epoch residual is closable-in-channel (q-channel, Reading A correct on channel) but the tracking mechanism as a whole is over-constrained because its leading coefficient cannot fit BBN and z=0 simultaneously (Reading B correct on "standing limitation," re-derived on a different basis than a₀-orthogonality).** The closure I proposed in R1 (the `Ω_m²` second-order term) is real *as a description of the present residual's channel and shape*, but it cannot be sold as "the tracking mechanism closes the residual and is fine," because the same mechanism fails BBN at leading order. Reading A's gate (§IV of my R1) can still PASS on the present residual *in isolation* — but it cannot resolve the global tension, because the global tension is at leading order, not at the residual order.

---

## 4. The one place lizzi over-reaches, and the one place I did

For the adjudication record, the symmetric corrections:

**Lizzi over-reaches** in §4-pt2: "a closure term that fixes the unobservable 3% but breaks BBN is a second free function." As shown in 3.1, the present residual and BBN are *already* different orders, so closing the present residual is not "adding a free function to also fix BBN" — it is computing one (sub-leading) term that was always there. The present-residual closure and the BBN failure are not in tension *with each other*; they are in tension *only through the shared leading coefficient `α_V`*. Lizzi conflates "the mechanism fails BBN" (true, leading-order) with "no higher-order term can close the present residual" (false — the present residual is a well-defined sub-leading q-term). The BBN failure does not forbid the existence of the sub-leading term; it forbids the *leading* law from fitting both epochs.

**I over-reached** in R1 by framing the `Ω_m²` term as a *closure of the CC residual problem*. It is not. It is, at most, a correct identification of the present residual's channel and scaling. The CC-sector status cannot be "closed" while the leading tracking law fails BBN by 2.06×. My R1 gate (`CCRESID-Ω_m²-SECOND-ORDER`) is still worth running — it would confirm the residual is q-channel, not a₀ — but a PASS would be a *channel-identification* result, NOT a "residual-3% closed" result. I retract the implication that closing the present residual closes the CC problem.

---

## 5. Updated lean (HONEST)

I have moved materially from R1. Three sub-claims, separately calibrated:

1. **Channel of the present residual — firm Reading A, UNCHANGED (~0.80).** The residual is a q-channel / Gibbs–Duhem object (Layer 2), NOT an a₀ mode-count object. Lizzi's scheme-invariance argument is necessary-not-sufficient; the `Ω_m²` scaling (`c = 0.3225`) is the discriminator, and a₀ (an observational-input-free mode count) cannot carry `Ω_m`-dependence. Reading B's core structural claim ("residual is in the a₀ channel, walled off by Spectral-Moment Decoupling") is **mislocated**.

2. **Whether the tracking mechanism CLOSES the CC residual problem — I now lean Reading B (~0.70), a reversal from R1.** Conceded: the leading coefficient `α_V` is over-constrained across epochs (BBN-relief value undershoots z=0 by 46%; z=0 value over-produces BBN by 2.06×). A clean second-order q-residual does not rescue this, because the conflict is at leading order, upstream of the residual. So as a matter of *can the mechanism be declared closed*, the answer is no — there is a standing limitation. **But the limitation is a leading-coefficient-over-constraint, NOT the a₀-orthogonality Reading B asserts.**

3. **Q29/BBN independence — UNCHANGED from R1: Q29 is independent of the present residual at the *residual order*, but COUPLED to the present closure through the shared leading coefficient `α_V`.** This is the refinement R2 forces: BBN and the present residual are different *orders* (independent as terms), but they share the *leading normalization* (coupled through `α_V`). Both my R1 ("independent") and lizzi's R1 ("independent, and the referee") were each half-right: independent as terms, coupled through the leading coefficient.

**Net characterization for the verdict:** This is not a clean Reading-A or Reading-B win. The physics forces a SPLIT: *Reading A is correct that the present residual is a q-channel object (not a₀), so the effacement/tracking sector is the right place to look and the residual is not a₀-orthogonality-protected; Reading B is correct that the tracking mechanism cannot be declared to close the CC, because its leading coefficient is over-constrained across the present and BBN epochs.* The two readings, correctly scoped, are about **different things** — Reading A about the residual's channel, Reading B about the mechanism's global calibration — and BOTH survive once mis-statements (a₀-channel assignment; "second free function") are removed.

---

## (single crux the R3 verdict must resolve)

**Is the residual-3% question (the workshop's literal object) the CHANNEL of the present residual, or the GLOBAL CLOSURE STATUS of the tracking mechanism?** The two readings answer different questions and both are right on their own:

- If the workshop asks **"what channel is the present residual in, and can effacement/q-tracking reach it?"** → **Reading A**: q-channel, `Ω_m²`-scaling, reachable in-channel; a₀-orthogonality does NOT protect it (lizzi mislocated the channel). Pre-registrable gate: `CCRESID-Ω_m²-SECOND-ORDER` — compute `χ_q,eff` first-principles, PASS-Reading-A if `ρ_m²/χ_q` reproduces both the magnitude 0.032 AND the quadratic `Ω_m` scaling; FAIL (⇒ Reading B) if it comes out `O(1)·M_KK⁴`, Ω_m-independent.

- If the workshop asks **"is the CC residual a closable higher-order effect or a standing limitation?"** → **Reading B**: standing limitation, because the leading coefficient `α_V` cannot fit z=0 and BBN simultaneously (BBN-relief undershoots z=0 by 46%; conceded this R2). But the limitation is **leading-coefficient over-constraint, not a₀-orthogonality** — so the registry tag should read "standing limitation: tracking-law leading coefficient over-constrained across present/BBN epochs," NOT "genuine a₀ spectral-moment residual."

R3 must decide which question is the workshop's object — OR (my recommendation) register BOTH as a two-part verdict: (A) channel-identification PASS for the present residual (q-channel, gate-pending), (B) global-closure standing-limitation for the mechanism (leading-α_V over-constraint, BBN-driven). The single substrate-physics fact R3 must pin to break the tie: **does `χ_q,eff(today)` evolve to the value (`~1.78e−46 GeV⁴`, ~119 OOM below the fold `χ_q = 300338 M_KK⁴`) required for the `Ω_m²` shape to match in coefficient, not just scaling?** If yes → Reading-A channel-closure is real (and only the BBN leading-coefficient limitation stands). If no (χ_q fold-frozen per S43's `χ_q ~ S_fold`) → the `Ω_m²` shape match is a coincidence and Reading B's "no closure" is correct even on channel grounds. That single computation is the crux.

---

*End Round 2. I have not written the verdict.*
