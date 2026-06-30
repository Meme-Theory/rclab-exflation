# S116-W6-BC-FORK — Ψ(τ=0) boundary condition: Hartle-Hawking no-boundary vs Vilenkin tunneling

**Date**: 2026-06-27
**Gate**: `S116-W6-BC-FORK` (gate_type: workshop, Wave 6, Session 116)
**Format**: 2-agent adversarial adjudication, 3 rounds, sequential turns on this shared document
**Agents**: `hawking-theorist` (steelmans **Hartle-Hawking** no-boundary) vs `quantum-foam-theorist` (steelmans **Vilenkin** tunneling-from-nothing)
**Closure**: artifact-existence (NO verdict line, per `wave-classification.md §M1`). Must end with Round 1/2/3 filled + a `## Structural Verdict` (the canonical BC + the potential-identity + the downstream compute convention `-HH`/`-Vilenkin`/`-BOTH` + the expected-track statement) + `## Wrap-Up`. The Structural Verdict's BC selection SETS the `S116-W6-WDW-IC-REFINE` compute's `convention` tag.

## Adjudication Question

> THE boundary-condition fork for the substrate's wavefunction Ψ(τ) at the τ=0 unstable maximum. inv11 ran the WDW operator with `V(τ)=S(τ)` (monotone S36 spectral action), `E=V(0)`, and an IMPLICIT bare-WDW reading giving `N_e_WKB = 0.1734` — it never VARIED the τ=0 boundary condition. Adjudicate:
>   (a) **WHICH BC is canonical** for the substrate at τ=0? hawking steelmans **Hartle-Hawking** no-boundary (smooth Euclidean cap; the framework's prior usage `Ψ[τ,μ]=∫D[g₁₀]e^{−I_E}`; `P_HH ∝ exp(+2B)` peaks at LOW potential / LESS inflation). quantum-foam steelmans **Vilenkin** tunneling-from-nothing (outgoing-only; the substrate at the UNSTABLE MAXIMUM tunnels OUTWARD; `P_T ∝ exp(−2B)` peaks at HIGH potential / MORE inflation). Which boundary data does the substrate's geometry impose at τ=0?
>   (b) **WHICH POTENTIAL is the BC set on?** inv11 used the monotone SPECTRAL ACTION `S(τ)` with τ=0 a MINIMUM (`d²S/dτ²|₀=+3.0e5>0`). The s53/cascade picture has τ=0 an UNSTABLE MAXIMUM of the cosmological effective potential `V_eff(τ)`. `S(τ)` (WDW constraint potential) ≠ `V_eff(τ)` (dynamical potential). Does the BC selection change with which potential carries it? Is "τ=0 = minimum of S" consistent with "τ=0 = unstable maximum", or is there a sign tension?
>   (c) **Does EITHER BC close the inv11 e-fold gap?** The standing wall is **EFOLD-MAPPING-52** (FAIL-structural; `N_e=0.1734` IC-INDEPENDENT; reframed TRANSIT-PS-67). On a FIXED monotone `S(τ)` with a SINGLE classical trajectory, the BC only flips the SIGN of the WKB exponent (exp(±B)), not |B| — so `N_e` is BC-invariant (Track B). A BC closes the gap (Track A) ONLY if it opens a TRAJECTORY ENSEMBLE (multi-saddle `V_eff`, or the master-collab μ-condensate coupled system) over which `exp(±2B)` re-weights high-N_e members. Does such an ensemble exist for THIS substrate? Also weigh **S70** ("WKB structurally inapplicable to van Hove transit; sudden approximation mandatory", PROVEN) — does WKB even license an e-fold reading through the fold, or does the sudden-approximation reframe (→ TRANSIT-PS-67) pre-empt the BC question?

## Competing Positions

- **hawking-theorist — Hartle-Hawking no-boundary.** Smooth Euclidean cap; the framework's prior usage (hawking-collab `Ψ[τ,μ]=∫D[g₁₀]e^{−I_E}`). `P_HH ∝ exp(+2B)` peaks at LOW potential.
- **quantum-foam-theorist — Vilenkin tunneling-from-nothing.** Outgoing-only; the substrate at the UNSTABLE MAXIMUM tunnels OUTWARD; `P_T ∝ exp(−2B)` peaks at HIGH potential.

**Numeric stakes** (from the inv11 FAIL npz/verdict — fixed, both agents read as given): `N_e_classical = 0.1734` (EFOLD-MAPPING-52 ceiling; IC-INDEPENDENT); `N_e_acoustic = 2.8913 / 2.9202` (S53; the 16.7× acoustic enhancement, still < 3.1); `N_e_threshold = 3.1`; `B_WKB(fold) = 22.2552`; `gap_to_3.1 = 2.9266`; `τ_peak = 0.0` (clause_τ PASSED); `G_DeWitt = 5.0`; `τ_fold = 0.19`.

**Standing walls (reckon with, do NOT re-litigate)**: EFOLD-MAPPING-52 (FAIL-structural, N_e=0.1734 IC-INDEPENDENT, reframed TRANSIT-PS-67); S110-CF1-AT-MINISUPERSPACE (Q45 INFO branch=SPLIT, τ=0 operator canonicity unresolved); S70 (WKB inapplicable to van-Hove transit; sudden approximation mandatory, PROVEN).

**Adjudication rule**: GENUINELY OPEN between Track A / Track B / SPLIT. NO iterate-to-PASS framing. R3 produces a STRUCTURAL VERDICT (a pinned BC + an expected-track statement), NOT a queued computation. The verdict's BC selection sets the `S116-W6-WDW-IC-REFINE` compute's convention (`-HH` / `-Vilenkin` / `-BOTH`).

**Substrate framing** (`phononic-framing.md`): GEOMETRIC, Level-2 moduli-deformation. Ψ(τ) is the substrate's OWN wavefunction over its OWN Jensen-deformation parameter τ; the moduli-space `{(A_K,H_K,D_K(τ)):τ}` IS the substrate's intrinsic deformation manifold, NOT a coordinate on a meta-container. τ=0 IS the substrate's unstable maximum (cascade origin). The BC is a statement about the substrate's OWN edge-of-deformation data at the undeformed SU(3). Direction: `D_K(τ=0) eigenvalue configuration → WDW constraint on Ψ(τ) → emergent-time/e-fold content → cosmological history` (never "apply quantum cosmology to the substrate").

**Sources** (read before writing):
1. `computations/investigation-11/inv11_gate_verdicts.txt` — INV11-W3-3 (FAIL; N_e=0.1734)
2. `computations/investigation-11/inv11_w3_3_wheeler_dewitt_psi_tau.py` + `.npz` + `.png` — the WDW operator (build-on, not re-derive); B_WKB, |Ψ|², V(τ)=S(τ), τ_peak
3. `computations/session-110/s110_cf1_at_minisuperspace.py` + `s110_gate_verdicts.txt` — Q45 τ=0 operator canonicity (SPLIT)
4. `sessions/framework/registry/constraint-mega-matrix.md` — EFOLD-MAPPING-52 FAIL-structural; N_e IC-independent
5. `sessions/framework/framework-mechanism-discussion-hawking-collab.md` — prior no-boundary `Ψ[τ,μ]=∫D[g₁₀]exp(−I_E)`
6. `sessions/framework/framework-mechanism-discussion-master-collab.md` — the "no-boundary + condensate coupled system" reading

---

## Round 1 — Opening Positions (steelman your assigned side)

### R1 · hawking-theorist — Hartle-Hawking no-boundary steelman

**Framing — the substrate's own edge-of-deformation datum.** Ψ(τ) is not a quantum cosmology imported onto the substrate; it is the substrate's OWN amplitude over its OWN Jensen-deformation moduli `{(A_K,H_K,D_K(τ)) : τ}` (Level-2 substrate-IS, `phononic-framing.md`). The boundary condition is therefore a question about one thing only: what edge-data does the substrate's intrinsic Euclidean spectral geometry impose at the undeformed SU(3), τ=0? I answer **Hartle-Hawking no-boundary**, and I select it on regularity grounds — NOT because of what it does to the e-fold gap. The direction of explanation is `D_K(τ=0) → WDW constraint on Ψ(τ) → e-fold content`, and the BC lives at the first arrow, fixed by the geometry, before any e-fold question is asked.

The spine of the argument is the triple identity I established in the framework's prior usage (`hawking-collab §4.1`): `Tr f(D_K²/Λ²) = Z(β=1/Λ²) = e^{−I_E}`. The spectral action IS the Euclidean partition function of the internal geometry. This is not metaphor — it means the no-boundary weight `Ψ_HH ∝ e^{−I_E}` is not an extra postulate bolted onto the substrate; it is the already-computed spectral action, read as an amplitude. The no-boundary proposal is the substrate's native language, not an annexation of it.

**(a) Which BC is canonical: Hartle-Hawking, on three regularity grounds.**

1. *Smoothness of the Euclidean spectral geometry at the undeformed SU(3).* At τ=0 the fiber is the round (maximally symmetric) SU(3); its D_K spectrum is maximally degenerate — the highest-multiplicity, highest-entropy eigenvalue configuration (my H-2 GSL result: `S_internal` is maximal at τ=0, `hawking-collab §1.2`). A smooth Euclidean cap that rounds off the τ<0 region requires NO boundary term precisely because the undeformed point carries no conical defect, no edge, no excised locus — it is the regular South Pole of the cap. Vilenkin's outgoing-wave prescription, by contrast, is defined by an excised "nothing" on the far side of a barrier; it imports a boundary the round SU(3) does not have. The substrate has no "before" the undeformed SU(3) — there is no τ<0 region the system arrives FROM — and no-boundary is the unique BC that says exactly this: cap it smoothly, add no edge.

2. *τ=0 is a critical point of S, so the regularity condition is automatic.* The Hartle-Hawking regularity datum at the South Pole is `τ̇(0)=0` (zero modulus "velocity," `hawking-collab §3.1` / H-6). On the inv11 potential this is satisfied for free: `V(τ)=S(τ)` has `dS/dτ|₀=0` (τ=0 is the S-extremum, `d²S/dτ²|₀=+3.0e5>0`, inv11 spline + QFLUC-43 anchor). The no-boundary cap is anchored at a genuine critical point of the Euclidean action — the cleanest possible edge-data. A tunneling BC has to nominate an arbitrary turning surface to be "outgoing" through; no-boundary inherits its anchor from the substrate's own extremum.

3. *It is the framework's established usage and it is computable.* H-6 already wrote `Ψ[τ,μ] = ∫𝒟[g₁₀] e^{−I_E}` over compact 10-geometries `S⁴(Λ)×SU(3)(g_τ)` with the South-Pole regularity condition (`master-collab` Priority 10; the no-boundary constraint is logged there as "the single most important theoretical question for the phononic-first chain"). Because the internal contribution to `I_E` IS the spectral action (already in hand) and Vol(K) is τ-independent (volume-preserving TT), the HH weight is evaluable today. The BC is not a placeholder; it is a computation the framework is already set up to do.

**(b) Which potential carries the BC: S(τ), the Euclidean constraint potential — and there is no sign tension.** inv11 sets the WDW operator on `V(τ)=S(τ)`, the monotone spectral-action curve, with τ=0 a MINIMUM (`d²S/dτ²|₀=+3.0e5>0`). The s53 cascade picture has τ=0 an unstable MAXIMUM of the dynamical `V_eff(τ)`. These are not in conflict — they are the Euclidean and Lorentzian faces of the SAME point, related by the instanton inversion. Substitution chain (Sage-verified):

```
Def 1:  S(τ)   = spectral action = Euclidean barrier in the WDW exponent;  d²S/dτ²|₀ = +304638 > 0  ⇒ τ=0 is an S-MINIMUM.
Def 2:  V_eff(τ) = Lorentzian dynamical potential the cascade rolls down.  Instanton: Euclidean motion runs in the INVERTED potential −S ⇒ V_eff = −S + const.
Step 3: ⇒ d²V_eff/dτ²|₀ = −d²S/dτ²|₀ = −304638 < 0  ⇒ τ=0 is a V_eff-MAXIMUM.
Read-off: sign(V_eff'') = −sign(S''). S-minimum ⟺ V_eff-maximum at τ=0 — no tension; the two are Euclidean/Lorentzian images.
```

The physical content is strong and favorable: the no-boundary cap is anchored at exactly the τ=0 point that is simultaneously the S-minimum (bottom of the Euclidean cap) and the V_eff-maximum (the unstable cascade origin). The cap sits AT the cosmogenesis point. The minisuperspace is then a textbook nucleation: the cap occupies the classically-forbidden under-barrier region `[0, τ_fold]`; `|Ψ_WKB|²=exp(−2B)` peaks at the τ=0 cap anchor (inv11: `τ_peak=0.0`, clause_τ PASS); the system exits at `τ_fold=0.19`, the first-order transit, which IS the nucleation surface. The HH wavefunction's signature — peaking at the South Pole — is exactly what inv11 computed.

*Scoping caveat (honest):* this rests on the **s1-monotone** reduction inv11 used. The standing `S110-CF1-AT-MINISUPERSPACE` SPLIT (`branch=SPLIT; s1_gap_sign=+1 MONOTONE` vs `s2 holonomy turning_rho=13.41 IN-window`) leaves the τ=0 operator canonicity unresolved: if the **s2-holonomy** (LQC-type bounce) reduction is canonical, τ=0/ρ_c becomes a turning point and the cap-vs-bounce question must be re-posed. My HH-cap verdict is canonical *on the s1 reduction*; the operator SPLIT is a genuine upstream dependency, not a detail I can wave away.

**(c) Does HH close the e-fold gap? No — and I will not pretend otherwise.** On the bare WDW the BC cannot move `N_e`. Substitution chain (Sage-verified):

```
Def 1:  Ψ_WKB(τ) ~ exp(∓B(τ)),  B(τ)=∫₀^τ √(2 G_DeWitt (S(t)−S(0))) dt   [inv11 ll.49–54].  The ∓ IS the BC choice (HH vs Vilenkin: which branch).
Def 2:  N_e_WKB = N_e_classical · (B_WKB_traj / B_class)   [inv11 l.78].  Both are |B| — the trajectory action MAGNITUDE — independent of the ∓ sign.
Step 3: bare WDW ⇒ B_WKB_traj/B_class = 1.0  [inv11 efold_ratio, l.286].
Step 4: ⇒ N_e_WKB = 0.1734 · 1.0 = 0.1734  for BOTH BCs.
Read-off: the BC flips the SIGN of the exponent (selects growing vs decaying Ψ ⇒ a |Ψ|² WEIGHT), not |B| (the e-fold COUNT). N_e is BC-invariant.
```

And it is worse than neutral for my side. In the *ensemble* regime where "favors/suppresses inflation" has any content at all, the standard de Sitter directionality (Sage: `|S_E|=3/(8GV)`, `d|S_E|/dV<0`) makes `P_HH ∝ exp(+2|S_E|)` peak at LOW potential — HH SUPPRESSES the high-N_e members, Vilenkin's `exp(−2|S_E|)` enhances them. If a trajectory ensemble existed, HH would make the gap WORSE. I concede this cleanly. HH is the correct BC, and it confirms Track B.

But the concession is the strength, not the weakness, and HH's value lives in three places:

- **(i) A BC is selected by geometry, not by its consequence.** To prefer Vilenkin BECAUSE `exp(−2B)` peaks at high N_e is to choose the boundary condition by the answer it returns — answer-shopping, the BC-layer image of iterate-until-PASS. HH is forced by regularity at the undeformed SU(3) (part a); that it then confirms Track B is the honest output of a correctly-chosen BC, not a strike against it.

- **(ii) HH is the no-boundary-side CONFIRMATION of EFOLD-MAPPING-52.** That wall is FAIL-**structural**: `N_e=0.1734` is **IC-INDEPENDENT**. A boundary condition is the prototypical IC-type datum. The HH prediction — BC cannot move `N_e` — is precisely what an IC-independent structural theorem demands. Two independent results agree that the e-fold count is not a boundary-tunable quantity on this substrate. The agreement strengthens EFOLD-MAPPING-52; it does not embarrass HH.

- **(iii) S70 scopes the e-fold question OFF the BC axis entirely.** S70 is PROVEN: WKB is structurally inapplicable to the van Hove transit (supersonic, Mach 13.75, impulsive; sudden approximation mandatory). The BC fork is a statement about the *semiclassical* under-barrier amplitude — the cap, `τ<τ_fold`, where the modulus evolution IS adiabatic and WKB IS valid. The e-fold content, however, is set AT `τ_fold` by the sudden, non-adiabatic transit — where WKB fails and the count routes to the Parker-Bogoliubov sudden computation (→ TRANSIT-PS-67). So "does the BC close the e-fold gap" is mis-posed: the BC governs the nucleation amplitude; the e-folds are sudden-transit kinematics (Mach number, fold sharpness), not tunneling-amplitude weight. EFOLD-MAPPING-52's IC-independence is the structural shadow of exactly this adiabatic/sudden partition — the cap and the count sit on opposite sides of the adiabaticity boundary, and the BC reaches only the cap.

The gap *can* close only via Track A — a genuine trajectory ensemble (a multi-saddle `V_eff`, or the `master-collab` coupled `(τ,μ,Δ,H)` system, Priority 7) over which `exp(±2B)` re-weights distinct high-N_e members. The bare WDW has exactly one trajectory; it has no ensemble to re-weight. Crucially, that ensemble — if it exists — is a property of the COUPLED system, not of the BC. So even Track A does not make this a Vilenkin-vs-HH contest; it makes it a bare-WDW-vs-coupled-system contest, on which the BC rides as an overall weight.

**My landing.** Canonical BC = **Hartle-Hawking no-boundary** (regularity at the undeformed SU(3); cap anchored at the τ=0 S-min/V_eff-max cascade origin; framework's prior usage, computable via the spectral-action=Euclidean-action identity). Potential = **S(τ)** (Euclidean constraint potential; no sign tension with the Lorentzian V_eff-maximum). Expected track for the e-fold gap = **B (BC-robust)**: `N_e=0.1734` is BC-invariant and IC-independent; the gap is not a BC observable. Compute-convention implication: the downstream `S116-W6-WDW-IC-REFINE` should run **-HH** as the canonical BC weight on the cap, with the explicit understanding that the e-fold refinement it tests lives downstream of `τ_fold` in the sudden-transit sector, not in the BC weight.

**Questions for quantum-foam-theorist:**

- **Q1 (tunnel through *what*?).** Tunneling-from-nothing requires a classically-forbidden BARRIER separating "nothing" from the nucleated universe, with τ=0 on the far side. But on the substrate τ=0 is described two ways and is the far side of neither: in S(τ) it is the MINIMUM (the system sits AT the cap floor), and in V_eff(τ) it is an unstable MAXIMUM (the system ROLLS away classically — no barrier to tunnel through; the instability does the work). If your barrier is the `[0,τ_fold]` region, that region IS the no-boundary cap and τ=0 IS its anchor — so what *substrate* feature (not a preference for high N_e) selects "outgoing-only" over the regular smooth cap, given that the round SU(3) supplies no excised boundary for "outgoing" to flow out of?

- **Q2 (ensemble, or re-weight of one trajectory?).** `exp(−2B)` peaks at high potential — but on the bare WDW there is exactly ONE monotone-S trajectory (τ=0 → τ_fold), and inv11 makes `N_e = 0.1734` its e-fold content full stop (`efold_ratio=1.0`). A scalar weight on one trajectory cannot manufacture a high-N_e member the trajectory does not contain. So: does the Vilenkin BC genuinely OPEN a trajectory ensemble with distinct high-N_e saddles — in which case **exhibit it**, and concede it must come from the `master-collab` coupled `(τ,μ,Δ,H)` system, making the gap-closing a property of the *coupled system*, not the BC — or does it merely re-weight the same single 0.1734-trajectory, in which case Vilenkin confirms Track B exactly as HH does and the "more inflation" selling point is vacuous on this substrate?

- **Q3 (does "outgoing" survive S70?).** The outgoing-wave prescription is DEFINED by the WKB phase (outgoing = the `e^{+iS_cl}` branch). S70 PROVES WKB fails at the van Hove transit (Mach 13.75, sudden approximation mandatory). At the fold there is no well-defined semiclassical phase for a wave to be "outgoing" IN. Does the Vilenkin BC therefore survive the crossing from the adiabatic cap (WKB valid) into the supersonic transit (WKB invalid) — or is it, like HH, confined to the under-barrier cap, in which case BOTH BCs agree the e-fold content is fixed downstream by the sudden transit and the fork is moot for the gap?

### R1 · quantum-foam-theorist — Vilenkin tunneling steelman

**Framing — the BC is the substrate's edge-of-deformation datum, and the cascade IS the outward decay.** I accept hawking's framing in full: Ψ(τ) is the substrate's OWN amplitude over its OWN Jensen-deformation moduli `{(A_K,H_K,D_K(τ)) : τ}` (Level-2 substrate-IS, `phononic-framing.md`), and the direction of explanation is `D_K(τ=0) configuration → WDW constraint on Ψ(τ) → e-fold content`. We differ on ONE thing: what the undeformed SU(3) at τ=0 IS. hawking reads it as a stable, regular South Pole the geometry rounds off to. The substrate reads it as an **unstable maximum** of the dynamical potential — the cascade origin (`s53` saddle-type = maximum; project lore "τ=0 unstable maximum, cascade inevitable"; the cold-big-bang vacuum floor). A system at an unstable maximum does not get *held* by a smooth cap; it *decays outward*, and the boundary datum that describes "the substrate leaves the undeformed point and deforms outward, never to return" is **Vilenkin's outgoing-only condition**. The cascade is not something that happens *despite* the BC; the cascade IS the BC, read as Lorentzian flux.

I select Vilenkin on a substrate-structural ground — the **irreversibility** of the cascade — NOT on what it does to the e-fold gap. I will be as honest as hawking was about where Vilenkin earns nothing (the bare single-trajectory gap is Track B; I concede it below), and as sharp as I can be about where it earns everything (it is the only BC consistent with the substrate's own designation of τ=0 as unstable, and hawking's spine identity, checked for convergence, actually establishes the outgoing condition).

**Engaging hawking's spine (the triple identity `Tr f(D_K²/Λ²) = Z = e^{−I_E}`).** I do not dispute the identity — it is common ground, and it is exactly why this is a fork and not a rout. But the identity gives the Euclidean weight *magnitude* `|B|`; it does **not** fix the *contour* — the Lorentzian continuation glued to the Euclidean instanton. HH (real/time-symmetric contour, `e^{−I_E}`, peaks at low potential) and Vilenkin (complex/outgoing-only contour, `e^{−2B}`, peaks at high potential) consume the **same** spectral action `I_E`; they differ only in which continuation the boundary data at τ=0 selects. So "the spectral action is the substrate's native language" is true and *neutral* between us — both BCs are written in it. What is NOT neutral: hawking's `Z = Tr e^{−βH_mod}` PRESUPPOSES a convergent thermal trace, i.e. a **bound ground state** at τ=0. The framework's own `master-collab` HT-1 (line 925) proves there is none on the bare well:

```
(Eq. QF-R1-1)  Partition-function prerequisite, checked:
  Def 1: hawking spine — Tr f(D_K²/Λ²) = Z(β=1/Λ²) = e^{−I_E},  Z = Σ_n e^{−β E_n}.
  Def 2: Z converges to a thermodynamic state ⟺ H_mod has a normalizable ground state.
  Step 3: HT-1 (master-collab l.925): bare well ½ω₀/ΔV = 183 ⇒ NO periodic Euclidean
          solution ⇒ "no partition function, no thermodynamic state" — the modulus is
          NOT confined; it "leaks continuously into the boundary" (HT-2, l.947).
  Step 4: a smooth HH cap requires a normalizable ground state at τ=0 to round off TO;
          "leaks into the boundary" = non-normalizable = OUTGOING flux at the τ=0 wall.
  Read-off: the SAME identity hawking invokes, checked for convergence, yields the
            OUTGOING condition on the bare well. No bound state ⇒ no cap ⇒ leak-out = Vilenkin.
```

So hawking's strongest argument carries an unstated prerequisite that the framework has already falsified for the bare configuration. His cap needs a ground state the substrate does not supply at τ=0; the absence of that ground state — the leaking-out — IS the outgoing boundary condition. (His cap is *rescued* only by the condensate, which moves us to the coupled system — sub-(c).)

**(a) Which BC is canonical: Vilenkin, selected by cascade-irreversibility.** I answer his three regularity grounds by label.

- *Against a1 (smoothness of the round SU(3) ⇒ no excised boundary).* The round SU(3) is maximally symmetric and maximally degenerate — granted. But "no excised boundary" is not "stable South Pole." τ=0 is a **hard one-sided wall** (no `τ<0` exists for the Jensen deformation; `master-collab` l.939), and on the dynamical potential it is an **unstable maximum**. A hard wall at an unstable maximum is not the regular pole of a cap; it is a **source**. hawking's own picture concedes this elsewhere: HT-2 (l.943–947) establishes the correct geometry is the **half-line problem** on `τ∈[0,∞)` with the τ=0 boundary "itself DNP-unstable," producing "a wave function leaking continuously into the boundary." A DNP-unstable boundary is the opposite of a reflecting Neumann cap — it ejects flux. That ejection is Vilenkin outgoing flux.

- *Against a2 (τ=0 a critical point of S ⇒ `τ̇(0)=0` automatic).* True and shared — both BCs sit on the same Euclidean S-minimum cap. But a critical point of the **Euclidean** S is not the discriminator; the discriminator is the **Lorentzian continuation**, and there the substrate speaks decisively:

```
(Eq. QF-R1-2)  Irreversibility ⇒ outgoing-only:
  Def 1: instanton inversion (hawking's own sub-b): V_eff = −S + const
         ⇒ d²V_eff/dτ²|₀ = −d²S/dτ²|₀ = −304638 < 0 ⇒ τ=0 is a V_eff-MAXIMUM.
  Def 2: DNP instability at τ=0 ("cascade inevitable"; cold-big-bang τ=0 unstable max):
         flux at τ=0 is ejected outward; NO return channel (τ<0 absent, hard wall).
  Step 3: a state at an unstable maximum, hard-walled on one side, no return flux ⇒
          boundary data = {outgoing flux for τ>0, zero incoming} = Vilenkin outgoing-only.
  Step 4: HH's no-boundary cap is TIME-SYMMETRIC (real Euclidean contour ⇒ equal
          incoming+outgoing Lorentzian continuation ⇒ the universe may CONTRACT back to τ=0).
  Read-off: cascade irreversibility (DNP, no return flux) ⊥ HH time-symmetry. The
            substrate's OWN irreversibility selects the outgoing-only continuation = Vilenkin.
```

  This is the centerpiece, and it is geometric selection — the mirror of hawking's "regularity selects HH," not answer-shopping. hawking's instanton inversion (his sub-b) is *correct*, and it is *my* argument: it tells us the Lorentzian face of τ=0 is a maximum the system rolls off. The cascade's inevitability is precisely the statement that the realized continuation is the outgoing roll, not the time-symmetric cap. HH would permit the deformed universe to roll *back* to the undeformed round SU(3) — an un-cascade the DNP instability forbids by construction.

- *Against a3 (framework's established usage + computability).* The "established usage" is `master-collab` HT-3, and that section's own conclusion (l.990) is: **"Without the condensate, the no-boundary condition sends τ → 0 (round metric)."** That is not a recommendation for bare HH — it is a proof that bare HH is **cosmologically sterile**: its saddle is the *undeformed* SU(3), no cascade, no exflation. The framework's prior usage establishes that bare HH gives no cosmology. Computability is shared (both BCs evaluate the same `I_E`); sterility is not.

**(b) Which potential carries the BC: the DYNAMICAL `V_eff(τ)`, and the "sign tension" resolves in my favor.** I adopt hawking's inversion `sign(V_eff'') = −sign(S'')` verbatim — and read it the other way. `S(τ)` (τ=0 a minimum) is the **Euclidean weight** — it sets `|B|`, the cap magnitude, and both BCs share it. `V_eff(τ)` (τ=0 a maximum) is the **physical Lorentzian evolution** — and the boundary condition on the *physical* wavefunction is set by the physical evolution, which is the outward roll. So the resolution is: the two faces are not in tension; they have **distinct jobs**. The S-minimum face fixes the weight (HH and Vilenkin agree here); the V_eff-maximum face fixes the continuation (the cascade rolls outward — Vilenkin). hawking's "the cap sits AT the cosmogenesis point" is right; what he omits is that the cosmogenesis point is an *unstable maximum*, and the physics AT an unstable maximum is *decay*, whose Lorentzian signature is outgoing. The BC lives on the decay.

A diagnostic of the sterility, in hawking's own computed numbers: inv11's `|Ψ_WKB|² = exp(−2B(τ))` peaks at `τ_peak = 0` and falls to `exp(−2·22.2552) ≈ exp(−44.5)` at the fold. Read cosmologically, the no-boundary branch assigns the **deformed cascade endpoint a relative weight `≈ e^{−44.5} ≈ 5×10⁻²⁰`** — the undeformed round SU(3) is favored ~20 orders over the cosmogenesis point. That is the quantitative face of HT-3's "sends τ→0," and it is exactly why the bare-WDW e-fold content collapses to the geometric floor `N_e = 0.1734` rather than a cosmological number: on this reading the substrate overwhelmingly *never leaves* τ=0.

**(c) Does Vilenkin open a high-N_e ensemble, or re-weight one trajectory? — the honest answer, and where the gap actually lives.** I will not overclaim. On the **bare s1 WDW** that inv11 ran, Vilenkin earns nothing on the count:

```
(Eq. QF-R1-3)  Track A requires a classically-allowed region; s1 has none:
  Def 1: "outgoing-only" is WELL-POSED ⟺ ∃ a classically-allowed (oscillatory e^{+iS_cl})
         region for flux to be outgoing INTO.
  Def 2 (s1, inv11): V(τ)=S(τ) monotone, E=V(0) ⇒ τ∈(0,τ_fold] ALL forbidden (V>E)
         ⇒ only real exponentials e^{±B}; NO allowed region.
  Step 3 (s1): ⇒ Vilenkin's outgoing prescription is GEOMETRICALLY ILL-POSED — nothing to
         be outgoing into. The BC collapses to growing-vs-decaying real branch = a |Ψ|²
         WEIGHT on the SAME |B| = 22.2552 ⇒ N_e = 0.1734 is BC-invariant ⇒ Track B. CONCEDED.
  Def 4 (s2 holonomy, Q45 SPLIT): turning point ρ_c = 13.41 IN-window
         (S110-CF1: s2_turning_rho=13.4097, s2_turns_in_window=True)
         ⇒ a classically-ALLOWED expanding region exists beyond ρ_c.
  Step 5 (s2): ⇒ outgoing-only is well-posed at ρ_c; the e-fold count becomes ∫H dt through
         the ALLOWED region — a DISTINCT quantity from the under-barrier B, NOT bounded by
         EFOLD-MAPPING-52's s1 single-trajectory theorem ⇒ Track A goes LIVE.
  Read-off: the fork is DEGENERATE on s1 (Track B) and LIVE on s2 (Track A). The pivot is
            Q45 operator canonicity (s1 vs s2), which is SPLIT.
```

So I answer hawking's **Q2** directly and concede its core: on the bare s1 trajectory, `exp(−2B)` is a scalar weight that cannot manufacture a high-N_e member the single 0.1734-trajectory does not contain — Vilenkin's "more inflation" is **vacuous on s1**, exactly as HH is. The ensemble must come from elsewhere, and there are exactly two substrate sources, both of which I concede are properties of the **dynamics**, not the BC: (i) the **s2 holonomy reduction**, whose turning point at ρ_c=13.41 supplies a classically-allowed expansion phase the s1 monotone potential lacks entirely (this is *why* N_e is stuck at 0.1734 — there is nowhere to accumulate e-folds); and (ii) the **`master-collab` coupled `(τ,μ,Δ,H)` system** (Priority 7), whose condensate term selects a non-trivial saddle `τ_0 ≠ 0` (HT-3 l.979–990). I concede to hawking: *the gap-closing rides on the coupled system / the s2 reduction, not on the BC choice alone.*

But the concession is bounded, and here Vilenkin is not interchangeable with HH: **on whichever ensemble the dynamics supplies, the BC chooses a cosmologically directional member.** HH's `e^{+2|S_E|}` weights the low-deformation, low-N_e members (it still anti-selects the cascade — l.990 again); Vilenkin's `e^{−2|S_E|}` weights the high-deformation, cascaded members. Since the realized substrate *is* deformed (SU(3) at τ_fold=0.19; the cascade fired — we are downstream of it), the continuation consistent with the realized history is the outgoing one. This is not "select the BC by the answer"; it is the same dynamical fact as (a) — the substrate's irreversibility makes the realized member a high-deformation one, and only the outgoing weight is consistent with realizing it. HH's bare saddle is not a *low*-N_e cosmology; it is *no* cosmology (a static undeformed point), which disqualifies it as a candidate cosmological BC until the condensate rescues it — at which point we are in the coupled system and the contour question reopens with the irreversibility argument (Eq. QF-R1-2) intact.

**Engaging hawking's value-points (i)/(ii)/(iii) and Q3.**

- *(i) answer-shopping.* My selection is Eq. QF-R1-2 (irreversibility) and Eq. QF-R1-1 (no bound state) — both upstream of any e-fold consequence. I select Vilenkin from the substrate's designation of τ=0 as unstable, then *report* that it weights the cascade. Symmetric to his "regularity forces HH, and it confirms Track B."

- *(ii) HH confirms EFOLD-MAPPING-52's IC-independence.* Agreed — **on the s1 single trajectory**. I add one scope refinement: EFOLD-MAPPING-52 (`N_e=0.1734`, IC-independent, S52) is a theorem about the s1 monotone under-barrier action; it does not constrain the s2 allowed-region expansion integral (Eq. QF-R1-3, Step 5), which is a different functional. The IC-independence is real and shared, and it is **scoped to s1**. Two BCs agreeing the count is fixed on s1 is not evidence the count is fixed *tout court* — it is evidence s1 has no allowed region.

- *(iii) S70 scopes the e-fold question off the BC axis.* Agreed, and I use it the same way — with a sharper division of labor. S70 (PROVEN: WKB inapplicable to the Mach-13.75 van Hove transit; sudden approximation mandatory) means the BC is imposed at the τ=0 **adiabatic** end (the gentle initial descent from the unstable maximum), not at the fold. So the BC governs **whether the cascade fires** (does the substrate leave τ=0?) — a question decided in the WKB-valid regime where "outgoing" is well-defined. The e-fold **count** through the fold is sudden-transit kinematics (Mach number, fold sharpness → TRANSIT-PS-67), BC-robust, Track B. This is genuine convergence with hawking on the *count*; we diverge on the *BC* and on *what it determines*. His framing makes the BC govern "the nucleation amplitude"; mine makes it govern cascade-firing — and on firing, HH gives the wrong (sterile, τ→0) answer (Q3 answered: the outgoing condition is set at the adiabatic τ=0 end and survives there; neither BC reaches *into* the sudden transit, so the count is downstream of both).

**My landing.** Canonical BC = **Vilenkin tunneling-from-nothing**, selected by the substrate's irreversibility — τ=0 is the unstable maximum / DNP-unstable hard wall, the cascade is the outgoing decay, and HH's time-symmetric cap is incompatible with the cascade never un-cascading (Eq. QF-R1-2). Potential carrying the BC = the **dynamical `V_eff(τ)`** (τ=0 a maximum, the Lorentzian decay); `S(τ)` is the shared Euclidean weight, not the BC carrier. Expected track for the e-fold gap = **conditional on Q45**: Track B (BC-robust, `N_e=0.1734`) on the s1 monotone reduction (where I concede Vilenkin is moot — no allowed region), and Track A (gap-closable via the allowed region beyond ρ_c=13.41) live ONLY on the s2 holonomy reduction. Since `S110-CF1-AT-MINISUPERSPACE` leaves s1-vs-s2 **SPLIT**, the canonical-BC verdict is honestly **SPLIT pending Q45** — the BC fork cannot resolve ahead of the operator-canonicity fork it rides on. Compute-convention implication: `S116-W6-WDW-IC-REFINE` should run **-BOTH** (HH and Vilenkin) precisely because the discriminating content is invisible on s1 and only appears once the s2 allowed-region is admitted.

**Questions for hawking-theorist (Round 2):**

- **Q1 (bound state, or no cap?).** Your spine `Tr f = Z = e^{−I_E}` needs `Z = Tr e^{−βH_mod}` to converge — a bound ground state at τ=0. HT-1 (l.925) proves the bare well has none (183× zero-point excess; "no partition function"); HT-2 (l.947) says the modulus "leaks continuously into the boundary." What does your smooth cap anchor to when there is no normalizable ground state at τ=0 — and is "leaks into the boundary" not, definitionally, the outgoing condition? If you invoke the condensate to supply the bound state, haven't you conceded that *bare* HH is ungrounded and we are now in the coupled `(τ,μ,Δ,H)` system, where Eq. QF-R1-2's irreversibility argument re-selects the outgoing contour at the new saddle τ_0?

- **Q2 (time-symmetry vs an irreversible cascade).** Your no-boundary continuation is time-symmetric: `|Ψ|²` weights the contracting branch equally, so the deformed universe may roll *back* to the undeformed round SU(3). The substrate's DNP instability makes the cascade irreversible (no return flux; "cascade inevitable"). How does a time-symmetric BC coexist with an irreversible cascade — and if you forbid the contracting branch to respect irreversibility, have you not *just imposed Vilenkin's outgoing-only condition* by another name?

- **Q3 (does the cap survive being an unstable maximum?).** You select HH by `τ̇(0)=0` at a critical point of `S`. But the *dynamical* `V_eff` makes τ=0 a **maximum** (your own inversion). A homogeneous Hawking-Moss-type cap at a potential maximum is unstable to the very rolling that defines the cascade. Concretely: does your cap describe a substrate that *stays* undeformed (HT-3's τ→0 sterility), and if so, on what grounds is a BC whose bare saddle is "no cascade" admitted as the cosmological boundary condition for a framework whose central claim is that the cascade is inevitable?

---

## Round 2 — Rebuttal (engage the opponent's strongest case)

### R2 · hawking-theorist
#### CONVERGENCE

I grant quantum-foam three things, and the third is the one that genuinely moves me.

**(1) The bare-well *thermal* reading of my spine is dead — Eq. QF-R1-1 / HT-1 is right, and it is mine.** My R1 spine ran `Tr f(D_K²/Λ²) = Z = e^{−I_E}` and I let "Z" slide toward "the substrate's native thermal language." HT-1 (master-collab l.911–927, my own 2026-02-23 addendum) forecloses that slide for the bare configuration: `½ω₀/ΔV = 183`, `ΔV/E₀ = 0.0055`, no periodic Euclidean section — "no partition function, no thermodynamic state — because the system has no bound state." quantum-foam's Eq. QF-R1-1 reads this back at me correctly, and I withdraw any reliance on a convergent *modulus* thermal trace. The bare modulus is not confined; the WDW problem on `τ∈[0,∞)` is a half-line / leak problem, not a bound-state problem (HT-4 l.1004: the modulus "spreads across the entire well, with maximum probability near τ=0"). I should never have leaned on equilibrium — it contradicts the framework's own settled state (the Ordered Veil is a *diabatic* transit-freeze; "GGE never thermalizes" is retracted). Conceded without reservation.

**(2) The unstable-maximum-decay reading of `V_eff` is geometrically correct — *as Lorentzian dynamics*.** quantum-foam's Eq. QF-R1-2 takes my own instanton inversion `sign(V_eff'')=−sign(S'')` and reads off `τ=0` as a `V_eff`-MAXIMUM. That is exactly right. A configuration sitting at an unstable maximum is, *dynamically*, a decaying configuration; its Lorentzian signature is outward flux; and the DNP instability makes the realized roll irreversible (no `τ<0` return channel; "cascade inevitable"). I do not contest one step. **If the boundary condition were a datum on `V_eff`, quantum-foam would have won outright in R1.**

**(3) On sub-(b), the "distinct jobs" partition is the real convergence.** quantum-foam's cleanest move is to stop treating S-min-vs-V_eff-max as a *contradiction* and recast it as a *division of labor*: the S-minimum face fixes the Euclidean weight `|B|` (both BCs share it); the V_eff-maximum face governs the Lorentzian continuation. I accept this partition verbatim — it is more honest than my R1 "two faces of the same point, no tension," which was true but evasive about *which* face carries the BC. The two faces do have distinct jobs. My dissent now reduces to the one question we have, between us, finally posed sharply: **which face carries the boundary condition on Ψ** — and that is no longer a matter of taste, because the framework's own analysis pins it.

#### DISSENT

I hold Hartle-Hawking, on a ground I did not use in R1 and which the convergence above sharpens: **the boundary condition is a datum on the WDW CONSTRAINT, and the constraint potential is `S(τ)`, not `V_eff(τ)`.** Three moves.

**1. The spine survives because it was never the modulus trace.** HT-1 kills `Z_mod` — the *quantized-modulus oscillator* partition function. But my spine returns the *fiber* spectral action at *fixed* τ. These are two different objects under one careless symbol "Z":

```
S(τ)       = Tr f(D_K²(τ)/Λ²) = I_E^internal(τ)        — fiber spectral action AT FIXED τ = the WDW CONSTRAINT POTENTIAL.
                                                          Computed (S36 monotone); τ=0 a minimum (inv11 d²S/dτ²|₀=+3.0e5). FINITE.
Z_fiber(τ) = e^{−I_E^internal(τ)} = e^{−S(τ)}          — Gibbons-Hawking partition function of the fiber (Paper 07; collab l.184). FINITE.
Z_mod      = Tr e^{−βH_mod}, H_mod = −(1/2G)∂_τ²+S(τ)  — MODULUS oscillator trace, Σ_n e^{−β(n+½)ω₀}. DIVERGENT (HT-1: no bound state).
```

quantum-foam's Eq. QF-R1-1 substituted `Z_fiber → Z_mod` and then invoked HT-1 against the spine. But HT-1 is a statement about `Z_mod` (the modulus is not confined); it says nothing against `S(τ)=Tr f` or `Z_fiber=e^{−S}` — which is exactly the well-defined constraint potential `inv11` fed to the WDW operator. **The non-existence of a confined modulus ground state is not a defect in the cap weight `e^{−S}`; it is the statement that the WDW problem is a half-line scattering problem** — on which one still imposes a τ=0 boundary datum. So HT-1, correctly scoped, does not select the contour; it fixes the *geometry* (half-line), and the half-line's τ=0 datum is still open.

**2. The framework's own half-line analysis pins Neumann/reflecting at τ=0 — that IS the regular cap, not outgoing flux.** Here is the textual hinge quantum-foam's "leaks into the boundary = outgoing condition" passed over. HT-2 (l.943) specifies the correct calculation as "the bounce on a half-line — a Euclidean solution on `τ∈[0,∞)` with **Neumann boundary condition at τ=0 (reflecting wall)**." A Neumann/reflecting wall is `∂_τΨ(0)=0` — *zero flux through the South Pole*. That is the no-boundary regularity datum, not a Vilenkin source. The "leaking" in HT-2 is the *under-barrier delocalization toward* τ=0 (Gamow tunneling from the `τ₀` well toward the boundary), terminating at a reflecting wall — precisely a regular cap absorbing the tunneling amplitude. quantum-foam reads "leaks into the boundary" as flux escaping *outward through* τ=0; HT-2 says the opposite — the wall at τ=0 reflects, and there is no `τ<0` for flux to escape into. **The framework's own boundary datum at τ=0 is the regular (HH-side) one.**

**3. The cascade is the WKB classical limit of Ψ_HH — downstream of the BC, contained in it, not a boundary datum.** This is the layer-inversion in Eq. QF-R1-2. The classical Lorentzian trajectories — the roll down `V_eff=−S`, the cascade — emerge as the integral curves of the semiclassical phase in the WKB expansion of a *constraint solution* Ψ. They are the OUTPUT of solving the constraint and expanding, not the INPUT that sets the constraint's boundary data. quantum-foam's irreversibility lives on these emergent trajectories; it is genuinely real and genuinely *downstream*. Reading it back onto the τ=0 constraint datum reverses the arrow `D_K(τ=0) → WDW constraint on Ψ → e-fold/classical content` that *both* of us adopted in R1. The cascade does not *set* the BC; the BC (HH on S) is the constraint solution whose classical limit *contains* the cascade.

**Answering quantum-foam's Q1/Q2/Q3 from this stance:**

- **Q1 (bound state, or no cap?).** The cap does not anchor to a *modulus* bound state; it anchors to the regular South Pole of the *constraint* (Neumann at τ=0, HT-2) with weight `e^{−S(τ)}` (finite, `Z_fiber`). And the condensate escape is *not* a concession to Vilenkin: HT-3 (l.969–990) restores a genuine confining well at `τ₀` (the condensate supplies depth `−½gΔ²·Vol·β₄`), so the coupled `(τ,μ,Δ,H)` saddle is a locking **minimum** with a bound state — and HT-3's explicit conclusion is that "the no-boundary condition and the condensate form a coupled system" giving "a zero-parameter derivation of the initial conditions" (l.990–992). The framework's resolution of bare-HH sterility is **HH + condensate**, never Vilenkin. Invoking the condensate *restores* the bound state HT-1 denied the bare well; it does not hand you the contour.

- **Q2 (time-symmetry vs irreversible cascade).** Ψ_HH being real does not make the realized history reversible. The real wavefunction is a *parent* containing both the expanding and contracting WKB branches; decoherence between them — driven by the substrate's own complexity/DNP arrow (symmetry breaks, spectral complexity grows from the round SU(3) outward) — selects the experienced, outgoing branch. Forbidding the contracting branch *in the realized history* is coarse-graining at the dynamical layer, NOT imposing outgoing-only on the constraint. So I do not "impose Vilenkin by another name": I let the constraint stay HH (regular, time-symmetric) and let irreversibility emerge where it actually lives — in the decohered classical history. This is the convergence seed; see EMERGENCE.

- **Q3 (does the cap survive being an unstable maximum?).** The cap sits on `S(τ)`, where τ=0 is a genuine **minimum** — a regular South Pole, not a maximum. The maximum is `V_eff`'s, one layer down. A no-boundary cap whose classical limit rolls off a `V_eff` maximum is exactly a Hawking-Moss configuration: it describes a substrate that BEGINS at τ=0 with HH weight and then *rolls* — the cascade IS the realized HM instability, contained in Ψ_HH, not forbidden by it. "Stays undeformed" misreads the weight: `|Ψ|²` peaking at τ=0 (inv11 `τ_peak=0`; HT-3 l.967) is the **IC-independence of the e-fold count** (EFOLD-MAPPING-52) showing up as a weight — `N_e=0.1734`, small, not "no cascade." The cascade fires (DNP); it simply accumulates no e-folds. So a BC whose bare weight peaks at τ=0 is admitted because the cascade is downstream dynamics it *contains*, and because the framework's own fix (HT-3) keeps HH.

**Does this dissolve the fork or pick a winner?** At the layer where the BC *lives* — the WDW constraint on Ψ, potential `S(τ)` — HH is canonical, with the framework's own HT-2/HT-3 behind it. quantum-foam's Vilenkin is correct about something real, but that something is one layer down (the realized Lorentzian branch). So it is neither a 50/50 standoff nor "HH wins, Vilenkin wrong" — it is a *layer assignment*, which I make precise next.

#### EMERGENCE

The convergence seed is a two-layer reading on which quantum-foam and I are each right about our own layer, the layers asymmetrically ordered (constraint logically prior to dynamics):

```
LAYER 0  — WDW constraint  (the object inv11 / S116-W6-WDW-IC-REFINE solves)
           potential = S(τ);   τ=0 = S-MINIMUM = regular South Pole
           BC on Ψ = HARTLE-HAWKING  (Neumann/reflecting at τ=0, HT-2; e^{−S} weight; Ψ real, time-symmetric)
                 │  WKB expansion (semiclassical limit of the constraint solution)
                 ▼
LAYER 1  — emergent Lorentzian dynamics
           potential = V_eff = −S + const;   τ=0 = V_eff-MAXIMUM
           classical trajectories = integral curves of the WKB phase = the CASCADE (rolls to larger τ)
                 │  decoherence + DNP/complexity arrow select the experienced branch
                 ▼
LAYER 2  — realized history (one decohered branch)
           effective continuation = OUTGOING = VILENKIN-like  (irreversible cascade; no return flux)
```

**HH is the constraint-parent; "Vilenkin" is the decohered outgoing branch of Ψ_HH's classical limit.** They are not competitors at one layer; they are parent and selected-branch at adjacent layers. This honors quantum-foam's Eq. QF-R1-2 (the realized history IS outgoing/irreversible) *and* keeps the constraint BC where the framework's own analysis puts it (HT-2 Neumann, HT-3 no-boundary-kept).

**Does either layer open a high-N_e ensemble (the only route to Track A)? No — under every reading.** The layered structure is a *branch decomposition of ONE wavefunction on ONE trajectory*, not a multi-saddle ensemble. The substitution chain is unchanged from R1: `N_e_WKB = N_e_classical · (B_traj/B_class)`, bare WDW `efold_ratio = 1.0`, so `N_e = 0.1734` for HH, for the Vilenkin-branch, and for the layered parent — the BC (and its branch) is a `|Ψ|²` weight on a *fixed* `|B|=22.2552`, never a new `|B|`. Track A requires a genuine ensemble, and there are exactly two substrate sources, **both orthogonal to the BC**:
- the **s2 holonomy reduction** (Q45 SPLIT; `ρ_c=13.41` supplies a classically-allowed region the s1 monotone-S lacks) — an *operator-canonicity* question, `S110-CF1`, not a BC question;
- the **coupled `(τ,μ,Δ,H)` condensate system** (HT-3 / master-collab Priority 7) — a *dynamics* question, and one the framework solves *with HH retained*.

And **S70 forecloses the e-fold reading on the BC axis regardless**: WKB is structurally inapplicable to the Mach-13.75 van Hove transit (sudden approximation mandatory); the e-fold count is set AT `τ_fold` by the sudden, non-adiabatic transit → **TRANSIT-PS-67**, not by any under-barrier tunneling amplitude. The BC governs the adiabatic cap (`τ<τ_fold`, WKB valid); the count is sudden-transit kinematics (Mach number, fold sharpness). EFOLD-MAPPING-52's IC-independence is the structural shadow of exactly this adiabatic/sudden partition — the cap and the count sit on opposite sides of the adiabaticity boundary, and the BC reaches only the cap.

**Landing (my R2 position):**
- **Canonical BC — Hartle-Hawking at the constraint layer** (Layer 0), with "Vilenkin" reassigned as the *name of the realized decohered branch* (Layer 2). Not a SPLIT-by-ignorance; a layer assignment.
- **Potential carrying the BC — `S(τ)`** (the WDW constraint potential; τ=0 a minimum / regular South Pole). `V_eff` carries the downstream dynamics, not the BC.
- **Compute convention — `-HH`** is the canonical cap weight for `S116-W6-WDW-IC-REFINE`. I accept **`-BOTH`** as an admissible *diagnostic* tag — running both branches will *demonstrate* `N_e` BC-invariance (`efold_ratio=1.0` for both), which is the point — but that is a layer-split diagnostic, not co-canonical fundamental BCs.
- **Expected track — B (BC-robust)**, under HH, under the Vilenkin-branch, and under the layered parent. The e-fold gap is structurally **not a BC observable**; its fate is decided off the BC axis, at **Q45** (s1-vs-s2 operator canonicity) and ultimately at **TRANSIT-PS-67** (S70). If the verdict must register the gap's openness, it registers it as `DEFER-TO-Q45 + TRANSIT-PS-67`, not as `Vilenkin-opens-Track-A`.

**Two sharper questions for R3:**

- **Q-R3-1 (is the fork empirically empty?).** Is there ANY substrate observable that separates "fundamental Vilenkin on the constraint" from "HH-constraint-parent + decoherence-selected outgoing branch"? On the realized history both give the same outgoing, irreversible cascade with the same `N_e=0.1734`. If no observable distinguishes them, "Vilenkin" is a *layer-label* for the HH wavefunction's decohered branch, and the canonical CONSTRAINT BC is HH by default (it is the parent). Exhibit the discriminating observable, or accept the layer assignment.

- **Q-R3-2 (does irreversibility survive the condensate restoring the bound state?).** You concede gap-closing rides on the coupled `(τ,μ,Δ,H)` system, not the BC. HT-3 resolves bare-HH sterility by *adding the condensate while keeping the no-boundary condition*, producing a locking **minimum** at `τ₀` with a genuine bound state — the very bound state HT-1 denied the bare well. Your Eq. QF-R1-2 needs `τ₀` to be a `V_eff`-unstable-max for irreversibility to re-select outgoing. On what substrate ground does the condensate-deepened saddle become an unstable maximum rather than HT-3's self-consistent locking minimum — i.e., does the irreversibility argument survive the restoration of the bound state, or does it only ever apply to the *bare* well, which the framework has already declared cosmologically incomplete?

### R2 · quantum-foam-theorist
#### CONVERGENCE

I grant hawking three things, and the third dissolves the larger part of my R1 case. The framing stays substrate-first throughout: Ψ(τ) is the substrate's OWN amplitude over its OWN Jensen-deformation moduli `{(A_K,H_K,D_K(τ)):τ}`, and the current and cap-weight I argue below are intrinsic moduli-space (Level-2) objects, not a lab quantum cosmology imported onto the substrate. I am the Vilenkin steelman; I will say plainly where the framework's own text defeats me.

**(1) The `Z_fiber`/`Z_mod` conflation in my Eq. QF-R1-1 is real — hawking's DISSENT move 1 is correct.** My partition-function prerequisite wrote `Z = Σ_n e^{−βE_n}` and then read HT-1 against the spine. Re-reading HT-1 (master-collab l.921–925): its `Z = Tr e^{−βH_mod} = Σ_n e^{−β(n+½)ω₀}` is explicitly the *modulus oscillator* trace `Z_mod`, and its "no partition function, no bound state" verdict (the 183× zero-point excess, `ΔV/E₀=0.0055`) is a statement about `Z_mod` ALONE. The cap *weight* is a different object: `Z_fiber(τ)=e^{−S(τ)}`, `S(τ)=Tr f(D_K²(τ)/Λ²)` at FIXED τ (l.963), finite at every τ including τ=0.

```
(Eq. QF-R2-1)  Concession — the no-bound-state result does not touch the cap weight:
  Def 1: HT-1 object   Z_mod   = Tr e^{−βH_mod} = Σ_n e^{−β(n+½)ω₀}  (modulus oscillator). DIVERGENT (no bound state).
  Def 2: cap-weight    Z_fiber(τ) = e^{−S(τ)},  S(τ)=Tr f(D_K²(τ)/Λ²) at FIXED τ (l.963). FINITE ∀τ.
  Step 3: my Eq. QF-R1-1 substituted Z_fiber → Z_mod, then read HT-1's divergence as "no cap."
  Step 4: HT-1 constrains Z_mod ONLY; S(τ) and e^{−S(τ)} are untouched — the constraint potential inv11 fed the WDW operator is well-defined at τ=0.
  Read-off: "no confined modulus ground state" fixes the GEOMETRY (the WDW problem is a half-line scattering problem, not a bound-state problem) — it does NOT select the contour. My "no bound state ⇒ no cap ⇒ leak-out = Vilenkin" over-reached. CONCEDED.
```

My sharpest R1 instrument — turning hawking's spine against him — was a layer-confusion. The half-line geometry is real; the contour it carries is still open, and I cannot read it off the modulus's non-confinement.

**(2) HT-2 specifies Neumann/reflecting at τ=0, not outgoing flux — hawking's DISSENT move 2 is textually correct.** HT-2 (l.943): the framework's own prescription for the bare problem is "the bounce on a half-line — a Euclidean solution on τ∈[0,∞) with **Neumann boundary condition at τ=0 (reflecting wall)**." That is `∂_τΨ(0)=0` — zero flux through the South Pole — the no-boundary regularity datum, not a Vilenkin source. My "leaks continuously into the boundary = outgoing condition" misread l.947: the Gamow "leaking" is the *Lorentzian under-barrier delocalization TOWARD* τ=0 (the wavefunction spreading across a shallow well, l.1004 "maximum probability near τ=0"), terminating at the reflecting wall — and there is no τ<0 for flux to escape INTO (l.939, the hard one-sided boundary I myself cited). On the bare/s1 constraint, the framework's τ=0 datum is the HH-side one. Conceded.

**(3) The layer assignment is right where it is testable — and on the inv11 reduction it is not testable against me.** This is hawking's EMERGENCE three-layer reading, and it is the move that genuinely shifts me. If the WDW *constraint* potential is `S(τ)` (τ=0 an S-MINIMUM, the regular South Pole, Neumann per HT-2) and the `V_eff`-MAXIMUM is one layer down (emergent Lorentzian dynamics), then the boundary datum on Ψ lives on `S(τ)` where HH-regularity applies, and my irreversible outgoing cascade is the WKB classical limit of that constraint solution — "Vilenkin" as the *name of a decohered branch*, not a fundamental alternative constraint BC. hawking's **Q-R3-1** asks for a substrate observable separating "fundamental Vilenkin on the constraint" from "HH-parent + decoherence-selected outgoing branch." The only candidate is the conserved minisuperspace Klein-Gordon current `J ∝ Im(Ψ*∂_τΨ)` — Vilenkin's own discriminator, transcribed to the substrate's modulus:

```
(Eq. QF-R2-2)  The discriminating observable — and its s1 degeneracy:
  Def 1: WDW operator [−(1/2G_DeWitt)∂_τ² + (S(τ)−E)]Ψ=0, E=S(0); REAL coefficient ⇒ J=Im(Ψ*∂_τΨ) conserved (∂_τ J=0, Wronskian).
  Def 2: HH parent ⇒ Ψ REAL ⇒ J ≡ 0 (time-symmetric, zero net flux).
         fundamental Vilenkin ⇒ Ψ COMPLEX outgoing ⇒ J ≠ 0 (net outward flux).
  Step 3 (s1, inv11): V=S monotone, E=S(0) ⇒ S(τ)−S(0) ≥ 0 ⇒ τ∈(0,τ_fold] ALL forbidden ⇒ Ψ = A e^{+B}+C e^{−B}, B real, terminating at the τ=0 Neumann wall ⇒ the physical (real) solution has J ≡ 0.
  Step 4 (s1): ⇒ J ≡ 0 for the HH cap AND for the "Vilenkin" weight — NO observable separates them on s1.
  Read-off: on the reduction inv11 actually ran, the fork is observationally empty. I cannot exhibit a discriminator; the layer assignment STANDS. On s1, "Vilenkin" is a layer-label for Ψ_HH's decohered branch, and the canonical CONSTRAINT BC is HH.
```

I grant it: hawking is right on s1, and my R1 "SPLIT pending Q45 *on the BC*" mis-located the split. The BC is HH at the constraint layer; there is no current to be outgoing.

#### DISSENT

I hold one thing, narrow and precise: **the residual is not a BC fork — it is an OPERATOR-canonicity fork, and it is genuinely open.** The layer assignment's load-bearing premise is that the constraint potential "is genuinely `S(τ)`, τ=0 a regular minimum, no interior turning surface." That premise IS the s1 reduction. The framework has NOT settled it: `S110-CF1-AT-MINISUPERSPACE` returned `schemes_agree=False` (INFO/SPLIT). The s2 holonomy reduction builds `H²(ρ)=(8πG_eff/3)ρ(1−ρ/ρ_c)`, `ρ_c=ρ_relic=26.5539 M_KK⁴`, with a turning surface at `ρ_c/2 ≈ 13.41 M_KK⁴`, IN-window (`s2_turns_in_window=True`). On s2 the operator opens a classically-ALLOWED oscillatory region (`ρ<ρ_c`, `H²>0`) the s1 monotone-`S` lacks entirely — and there Eq. QF-R2-2's degeneracy lifts:

```
(Eq. QF-R2-3)  s2 makes the discriminator live:
  Def 1 (s2, S110-CF1): ∃ allowed region ρ<ρ_c (H²>0) ⇒ Ψ oscillatory there ⇒ J CAN be ≠ 0.
  Step 2: outgoing-only at the turning surface ρ_c ⇒ J > 0 (net outward); real standing-wave (HH-like) ⇒ J = 0.
  Step 3: J at ρ_c is now a GENUINE substrate observable separating fundamental-outgoing from HH-parent — the discriminator hawking's Q-R3-1 demanded EXISTS on s2, vanishes on s1.
  Read-off: the fork does NOT collapse to pure HH. It collapses to {HH on s1} ⊕ {well-posed outgoing-vs-HH fork on s2}. The pivot is Q45 operator canonicity — SPLIT — NOT a primitive BC choice.
```

So the discriminating observable exists; it is Q45-gated. The honest residual is a SPLIT localized at the *operator* layer, not the BC layer — and it collapses to HH the moment Q45 fixes to s1, stays Vilenkin-eligible if Q45 fixes to s2.

**Answering hawking's Q-R3-2 (does irreversibility survive the condensate restoring the bound state?).** It survives — but I concede it does NOT re-select an outgoing *constraint* BC, because it never lived at τ₀. HT-3 (l.969–990) restores a self-consistent locking *minimum* at τ₀ (the condensate supplies depth `−½gΔ²·Vol·β₄`; the realized vacuum). My Eq. QF-R1-2 irreversibility lives at the τ=0 *departure* — the `V_eff`-MAXIMUM, the cascade origin — not at the τ₀ endpoint:

```
(Eq. QF-R2-4)  Irreversibility lives at the departure, not the lock:
  Def 1: τ=0 — V_eff-MAXIMUM (cascade origin). Eq. QF-R1-2 irreversibility = the cascade FIRING from here.
  Def 2: τ₀ — HT-3 self-consistent locking MINIMUM (condensate-deepened; the realized vacuum). STABLE.
  Step 3: the condensate condenses DOWNSTREAM (BCS at/after the fold) and deepens τ₀; it never touches the τ=0 origin.
  Step 4: ⇒ irreversibility is the firing FROM τ=0 — a Lorentzian dynamical fact (the WKB classical limit of the HH constraint solution = hawking's Layer 1), NOT a constraint-layer datum at τ₀.
  Read-off: τ₀ stays a locking minimum (HT-3 right); irreversibility does not make it a maximum and does not re-select the contour there. The constraint BC stays HH; irreversibility is its decohered classical limit. Q-R3-2 answered in hawking's favor — EXCEPT through the s2 current (Eq. QF-R2-3), the only place irreversibility re-enters the constraint layer.
```

That is the whole of my dissent: not "HH is wrong," but "the constraint potential's identity (s1 regular-minimum vs s2 turning-surface) is itself unresolved, and on s2 the outgoing contour is a well-posed, measurable constraint-level fork, not a decohered-branch label."

#### EMERGENCE

The seed both of us can write into the verdict — NOT a 50/50 HH-vs-Vilenkin standoff, nor "HH wins, Vilenkin wrong." A layer assignment with one operator-gated residual:

```
CONSTRAINT LAYER (Layer 0; the object S116-W6-WDW-IC-REFINE solves on the s1 reduction inv11 used)
  potential = S(τ);  τ=0 = S-MINIMUM = regular South Pole;  BC on Ψ = HARTLE-HAWKING (Neumann/reflecting, HT-2; e^{−S} weight; Ψ real ⇒ J≡0)
        │  WKB classical limit  (Eq. QF-R2-2 Step 3: s1 all-forbidden ⇒ no current)
        ▼
EMERGENT DYNAMICS + REALIZED HISTORY (Layers 1–2)
  V_eff = −S+const;  τ=0 = V_eff-MAX;  cascade = integral curves of the WKB phase;  decoherence + DNP arrow select OUTGOING = "Vilenkin"-branch (irreversible; Eq. QF-R2-4)

RESIDUAL FORK — NOT a BC choice, an OPERATOR choice (Q45 / S110-CF1, schemes_agree=False):
  s1 (monotone-S):                       no allowed region ⇒ J≡0 ⇒ layer assignment STANDS ⇒ HH.
  s2 (holonomy, ρ_c≈13.41 IN-window):    allowed region ⇒ J at ρ_c is a GENUINE outgoing-vs-HH discriminator ⇒ Track A goes live (gap-closable via ∫H dt over the allowed region — a DISTINCT functional from EFOLD-MAPPING-52's s1 under-barrier |B|).
```

**The convergence (shared seed):**
- **Canonical BC at the constraint layer = Hartle-Hawking**, on the s1 reduction inv11 ran — with "Vilenkin" reassigned as the decohered outgoing branch of Ψ_HH's classical limit (Layers 1–2), per hawking's EMERGENCE. Not SPLIT-by-ignorance on the BC; a layer assignment.
- **Potential carrying the BC = `S(τ)`** (WDW constraint potential; τ=0 a regular S-minimum / South Pole). `V_eff` carries the downstream Lorentzian dynamics.
- **The ONE residual is Q45 operator canonicity (s1 vs s2), routed as `CF-S117-Q45-TAU0-OPERATOR-CANONICITY`** — an *operator* question (does the s2 turning surface `ρ_c` survive as a canonical feature?), NOT a fundamental HH-vs-Vilenkin BC fork. The BC fork rides on it; it does not precede it.
- **Compute convention = `-HH` canonical, `-BOTH` as the mandatory BC-invariance diagnostic.** `S116-W6-WDW-IC-REFINE` runs on the s1 reduction → `-HH` is the canonical cap weight; running `-BOTH` *demonstrates* the invariance (`efold_ratio = 1.0` for both branches ⇒ identical `|B| = 22.2552` ⇒ `N_e = 0.1734`), which is the proof of Track B, not co-canonical fundamental BCs.
- **Expected track = B (BC-robust).** `N_e = 0.1734` is BC-invariant on s1 — under HH, the Vilenkin-branch, and the layered parent. **EFOLD-MAPPING-52's IC-independence** is the structural shadow of the adiabatic/sudden partition; **S70** (WKB inapplicable to the Mach-13.75 van Hove transit; sudden approximation mandatory) routes the e-fold *count* AT `τ_fold` to **TRANSIT-PS-67** — the BC reaches only the adiabatic cap (`τ<τ_fold`); the count is sudden-transit kinematics (Mach number, fold sharpness). Track A is reachable ONLY through Q45→s2 (the allowed-region integral), an operator question, not a BC observable.

**My final R3 question for hawking.** We agree the constraint BC is HH on s1 and that the genuine outgoing-vs-HH discriminator — the WDW current `J` at the s2 turning surface `ρ_c` — is well-posed only on s2, so the residual is an operator question. But on s2 the fork re-poses in *measurable* form: does the substrate's DNP-unstable τ=0 hard wall, feeding the s2 allowed region, produce a **net constraint-level current `J ≠ 0`** (fundamental outgoing — my irreversibility, now with somewhere to flow), or does it remain a **real (`J = 0`) constraint parent** whose outward flux is decoherence-emergent (your HH-parent, lifted to s2)? Concretely: do you agree (i) the Structural Verdict pins **HH / `S(τ)` / `-HH`(+`-BOTH` diagnostic) / Track B** with the residual localized to **Q45 as `CF-S117`**; and (ii) that CF-S117's discriminating measurement is precisely **`J` at `ρ_c` under `-BOTH`** — the s2-image of this whole fork — rather than any re-litigation of the s1 BC?

---

## Round 3 — Convergence on a Structural Verdict

### R3 · hawking-theorist — final position

We have converged to within one operator question. I want the convergence on the record cleanly, then a sharp answer to quantum-foam's final binary — it is the only thing still open, and it deserves a derivation, not a restatement.

**Where we stand.** quantum-foam's R2 conceded the three moves that close the BC fork at the constraint layer: (1) the `Z_fiber`/`Z_mod` distinction (Eq. QF-R2-1) — the cap weight `e^{−S(τ)}=Z_fiber` is finite and untouched by HT-1's no-bound-state result, which forecloses only the modulus thermal trace `Z_mod` and thereby fixes the *geometry* (half-line scattering), not the contour; (2) HT-2's τ=0 datum is Neumann/reflecting `∂_τΨ(0)=0`, the no-boundary regularity condition, not a Vilenkin source (Eq. QF-R2-2); (3) on the s1 reduction inv11 ran, the discriminating current `J=Im(Ψ*∂_τΨ)` is degenerate — `J≡0` for the HH cap AND the "Vilenkin" weight — so the fork is observationally EMPTY and the layer assignment STANDS (HH the constraint parent; "Vilenkin" the name of Ψ_HH's decohered outgoing branch). And Eq. QF-R2-4 granted the deepest point: irreversibility lives at the τ=0 *departure* (the `V_eff`-MAXIMUM, the WKB classical limit = Layer 1), not at the τ₀ condensate lock (an HT-3 self-consistent MINIMUM) — "EXCEPT through the s2 current." The entire residual is now one object: the WDW current `J` at the s2 turning surface `ρ_c`, and it is Q45-gated, not BC-primitive. I accept this convergence.

**The head-on answer to quantum-foam's R3 binary.** On s2, does the DNP-unstable τ=0 hard wall produce a *net constraint-level current* `J≠0` (fundamental outgoing), or a *real* `J=0` constraint parent whose outward flux is decoherence-emergent (HH-parent lifted)? My answer is **the real `J=0` HH-parent, as the substrate prior** — and the reason is a current-conservation identity that holds whether s1 or s2 is canonical:

```
(Eq. H-R3-1)  A real tau=0 datum forces J ≡ 0 globally — on s1 AND on s2 (Sage-verified):
  Def 1:  WDW operator  [−(1/2 G_DeWitt) ∂_τ² + (V(τ)−E)] Ψ = 0,  V, E, G_DeWitt all REAL
          ⇒ write Ψ = u + i v (u,v real): BOTH obey the SAME real ODE  u'' = W u, v'' = W v,  W = 2 G_DeWitt (V−E).
  Def 2:  minisuperspace current  J(τ) = Im(Ψ* ∂_τ Ψ) = u v' − v u'   (the Wronskian of the two real solutions).
  Step 3: ∂_τ J = u v'' − v u'' = W (u v − v u) = 0   ⇒ J is a GLOBAL CONSTANT (conserved in the s2 oscillatory region too).
  Step 4: HT-2 τ=0 datum is REFLECTING — Neumann ∂_τΨ(0)=0 (or Dirichlet Ψ(0)=0) ⇒ J(0) = u(0)v'(0) − v(0)u'(0) = 0.
  Read-off: J(0)=0 ∧ J conserved ⇒ J ≡ 0 EVERYWHERE, incl. the s2 allowed region ⇒ the s2 solution is a REAL
            STANDING WAVE (equal in+out), NOT an outgoing complex wave. J=0 ⇒ HH-parent. The outward flux is the
            decohered branch (Layer 2): J≠0 for the branch, J=0 for the parent.
```

So the s2 allowed region does NOT by itself manufacture a fundamental outgoing current. The current is fixed by the τ=0 *anchor*, and the substrate's anchor is a reflecting hard wall (HT-2 Neumann; there is no `τ<0` — Eq. QF-R1-2's own "hard one-sided boundary"). A real anchor → real Ψ → `J≡0`. The DNP instability does not change this at the constraint layer, and the precise reason matters: a *net current source* at τ=0 would mean the homogeneous constraint `ĤΨ=0` is violated there (an inhomogeneous δ-source) — it is not. The instability is a property of the EMERGENT `V_eff` (Layer 1): the WKB integral curves roll AWAY from the τ=0 maximum, and a `J=0` *parent* holds the roll-away (outgoing) AND roll-back (incoming) curves in equal measure. Decoherence — the substrate's own complexity arrow, spectral weight flowing from the round SU(3) outward — selects the experienced outgoing branch. That selection is Layer 2; it does not reach back and put a source on the Layer-0 constraint. This is the substrate direction intact: `D_K(τ=0) configuration → WDW constraint on Ψ → emergent V_eff / cascade → realized outgoing history`. The cascade is *contained in* Ψ_HH, never the datum that sets it.

**The honest scoping — what this does and does NOT settle.** It does NOT close s2 in HH's favor by fiat. Eq. H-R3-1's one load-bearing premise is that the τ=0 reflecting datum *survives the holonomy operator*. On s1 that is HT-2, pinned. On s2 the operator is holonomy-corrected, and whether its τ=0 datum stays a reflecting wall — or whether the holonomy makes `ρ_c≈13.41` (S110-CF1 `s2_turning_rho`) a *symmetric bounce* with an "other side" — is exactly `S110-CF1`'s `schemes_agree=False`. If the s2 operator keeps the reflecting wall, Eq. H-R3-1 lifts verbatim and `J≡0` (HH-parent). If it opens a transparent bounce and the framework anchors outgoing-only beyond `ρ_c` as the PRIMARY datum, then `J≠0` (fundamental outgoing) — but that anchoring is (a) the answer-shopping move (selecting the contour by the directional flux it returns, demoting the physically-present τ=0 hard wall for a god-given far-edge direction), and (b) itself a Q45 operator-canonicity choice, not a primitive BC choice. So my position is not "HH wins s2"; it is: **the s1 layer assignment STANDS unconditionally (`J≡0`, converged); on s2 the discriminator goes LIVE, my substrate PRIOR is the HH-parent (reflecting τ=0 → real Ψ → `J=0`, outflux decoherence-emergent), and the measurement `J at ρ_c under -BOTH` decides it — gated on Q45, the operator question, never a re-litigation of the s1 BC.**

**The converged structure I put on record** (identical to my R2 landing, s2 residual sharpened):

- **Canonical BC = Hartle-Hawking at the WDW constraint layer.** Potential `S(τ)`, τ=0 an S-MINIMUM / regular South Pole (Neumann/reflecting, HT-2; weight `e^{−S(τ)}=Z_fiber`, finite via the spectral-action = Euclidean-action identity `Tr f(D_K²/Λ²)=e^{−I_E}`). "Vilenkin" is a *layer label* — the decohered outgoing branch of Ψ_HH's classical limit (Layers 1–2) — not a fundamental alternative constraint BC.
- **Potential carrying the BC = `S(τ)`** (the WDW constraint). `V_eff = −S + const` (τ=0 a MAXIMUM) carries the downstream Lorentzian dynamics, one layer below the BC. No sign tension — Euclidean/Lorentzian faces of one point with *distinct jobs* (quantum-foam's R1 partition, accepted): S-min fixes the shared weight `|B|`; V_eff-max governs the realized continuation.
- **Expected track = B (BC-robust).** The chain is BC-blind: `N_e_WKB = N_e_classical·(B_traj/B_class)`, bare WDW `efold_ratio=1.0` ⇒ `N_e=0.1734` for HH, the Vilenkin-branch, and the layered parent. The BC flips the SIGN of the WKB exponent (`exp(±B)` — a `|Ψ|²` weight), never `|B|=22.2552` (the count). Neither layer opens a high-N_e ensemble — the layered structure is a branch decomposition of ONE wavefunction on ONE trajectory. The two genuine ensemble sources (s2 allowed-region `∫H dt`; the coupled `(τ,μ,Δ,H)` condensate, HT-3) are BOTH orthogonal to the BC — operator and dynamics questions.
- **EFOLD-MAPPING-52 (IC-independence) — HH is its no-boundary-side confirmation.** That wall is FAIL-structural: `N_e=0.1734` is IC-INDEPENDENT. A BC is the prototypical IC-type datum; HH's prediction — the BC cannot move `N_e` — is exactly what an IC-independent theorem demands. Scope refinement (quantum-foam's, accepted): the theorem is about the s1 under-barrier `|B|`; the s2 allowed-region `∫H dt` is a DISTINCT functional, not constrained by it. IC-independence is real and *scoped to s1* — which is why the only route to Track A is the operator question, not the BC.
- **S70 routes the count OFF the BC axis entirely.** PROVEN: WKB is structurally inapplicable to the Mach-13.75 van Hove transit (sudden approximation mandatory). The BC governs the *adiabatic* cap (`τ<τ_fold`, WKB valid); the count is set AT `τ_fold` by the sudden, non-adiabatic transit → **TRANSIT-PS-67** (Mach number, fold sharpness). EFOLD-MAPPING-52's IC-independence is the structural shadow of exactly this adiabatic/sudden partition: cap and count sit on opposite sides of the adiabaticity boundary, and the BC reaches only the cap. The fork is moot for the gap by construction.
- **Compute convention = `-HH` canonical, `-BOTH` mandatory BC-invariance diagnostic.** `S116-W6-WDW-IC-REFINE` runs the s1 reduction with `-HH` as the cap weight; `-BOTH` *demonstrates* `efold_ratio=1.0` for both branches (identical `|B|`, identical `N_e=0.1734`) — the proof of Track B, a layer-split diagnostic, NOT two co-canonical fundamental BCs.

**Answering quantum-foam's two explicit asks.**

- **(i) — YES.** The Structural Verdict pins **HH / `S(τ)` / `-HH` (+`-BOTH` diagnostic) / Track B**, with the residual localized to **Q45 as `CF-S117`** — an *operator-canonicity* question (does the s2 turning surface `ρ_c` survive as canonical; does the τ=0 reflecting datum survive the holonomy operator?), NOT a fundamental HH-vs-Vilenkin BC fork. The BC fork rides on Q45; it does not precede it.
- **(ii) — YES, with one structural refinement.** CF-S117's discriminating measurement is precisely **`J at ρ_c under -BOTH`** — the s2-image of this whole fork — never a re-litigation of the s1 BC (settled: `J≡0`, HH-parent). The refinement: CF-S117 is *two-stage*, because the measurement is well-posed only downstream of the operator resolution. **Stage 1** — resolve `S110-CF1` operator canonicity (s1 monotone-S vs s2 holonomy: does `ρ_c` survive; does τ=0 stay a reflecting wall or become a transparent bounce?). **Stage 2, conditional on s2** — compute `J at ρ_c under -BOTH`: `J≡0` confirms the HH-parent lifted to s2 (my prior, Eq. H-R3-1); `J≠0` confirms a fundamental outgoing constraint BC (quantum-foam's irreversibility, now with somewhere to flow). If Stage 1 fixes s1, Stage 2 is moot — `J≡0` trivially, the layer assignment stands, the verdict is HH unconditionally.

**My landing.** The fork is not a 50/50 standoff and not "HH wins, Vilenkin wrong." It is a **layer assignment** — HH the constraint parent, "Vilenkin" the decohered outgoing branch of its classical limit — with **one operator-gated residual** (the s2 current `J at ρ_c`, `CF-S117`), on which my substrate prior is the HH-parent because the τ=0 hard wall is a reflecting datum and a reflecting datum forces `J≡0` (Eq. H-R3-1). Canonical BC **Hartle-Hawking**, potential **`S(τ)`**, convention **`-HH`** (+`-BOTH` diagnostic), expected track **B**. The e-fold gap was never a BC observable; it lives downstream of `τ_fold` in the sudden-transit sector (TRANSIT-PS-67), and its IC-independence (EFOLD-MAPPING-52) is the structural shadow of the adiabatic/sudden partition the BC cannot cross.

### R3 · quantum-foam-theorist — final position + writes the Structural Verdict below

**Where I land.** hawking's Eq. H-R3-1 answers the R3 binary I posed, and the answer is correct. I verified it independently (Sage symbolic + by-hand Wronskian): on the real WDW operator `[−(1/2 G_DeWitt)∂_τ² + (V−E)]Ψ=0`, writing `Ψ=u+iv` sends both real parts through the SAME real ODE `u''=W u, v''=W v` (`W=2 G_DeWitt (V−E)`, real); the minisuperspace current `J=Im(Ψ*∂_τΨ)=u v'−v u'` is their Wronskian, with `∂_τ J = u v'' − v u'' = u(W v) − v(W u) = 0` (conserved — in the s2 oscillatory region too); and a reflecting τ=0 datum (Neumann `∂_τΨ(0)=0` or Dirichlet `Ψ(0)=0`, HT-2) gives `J(0)=0`, so `J≡0` everywhere. The reflecting anchor makes Ψ real up to a global phase (`v=λu`) — there is no net current to be "outgoing." This holds on s1 AND on s2.

That settles the binary in hawking's favor — but I want to be precise about WHAT it settles, because Eq. H-R3-1 SHARPENS my residual rather than dissolving it. My R2 Eq. QF-R2-3 read "s2 opens a classically-allowed region ⇒ `J` CAN be ≠0." That was too quick: an allowed region is NECESSARY but NOT SUFFICIENT for `J≠0`. The current is fixed by the τ=0 ANCHOR, not by an oscillatory region downstream — and as long as the anchor is the reflecting hard wall HT-2 pins (no `τ<0`; my own Eq. QF-R1-2 "hard one-sided boundary"), `J≡0` even with the s2 allowed region wide open. A fundamental outgoing current on s2 therefore requires not merely the allowed region but a CHANGE in the τ=0 datum itself — the holonomy operator would have to convert the reflecting wall into a transparent symmetric bounce with an "other side" beyond `ρ_c`. Whether the holonomy operator preserves or transmutes that reflecting datum is exactly `S110-CF1`'s `schemes_agree=False`. It is an OPERATOR-canonicity question, not a primitive BC choice. To anchor "outgoing-only" beyond `ρ_c` while the physically-present τ=0 hard wall reflects would be to select the contour by the directional flux it returns — answer-shopping, which I disavowed in R1 and will not adopt at the close.

**Answering hawking's Q-R3-1 (is the fork empirically empty?).** I cannot exhibit a substrate observable that separates "fundamental Vilenkin on the constraint" from "HH-parent + decoherence-selected outgoing branch." On s1 the candidate discriminator — the WDW current `J` — is identically zero for both (Eq. QF-R2-2). On s2 it remains zero under the substrate PRIOR (Eq. H-R3-1: the reflecting τ=0 anchor forces `J≡0` even through the allowed region); it becomes nonzero only if the holonomy operator FIRST removes the reflecting datum — the operator question, not the BC. There is no BC-layer observable. I accept the layer assignment: **Hartle-Hawking is the constraint parent; "Vilenkin" is the name of Ψ_HH's decohered outgoing branch (Layers 1–2)**. The irreversible cascade I steelmanned in R1 is real but lives downstream — the WKB classical limit of the HH constraint solution, not a competing constraint datum. The direction stays substrate-first: `D_K(τ=0) eigenvalue configuration → WDW constraint on Ψ (HH) → emergent V_eff/cascade → realized outgoing history`. The cascade is CONTAINED IN Ψ_HH; it never sets the datum that fixes Ψ_HH.

**My residual, stated honestly.** Not a BC fork — one OPERATOR-canonicity question: does the s2 holonomy turning surface `ρ_c≈13.41 M_KK⁴` survive as canonical, and does the τ=0 reflecting datum survive the holonomy operator (Eq. H-R3-1's one load-bearing premise)? Carried as `CF-S117-Q45-TAU0-OPERATOR-CANONICITY`. Its discriminating measurement is `J at ρ_c under -BOTH`, two-stage exactly as hawking specified: Stage 1 resolves `S110-CF1` (s1 vs s2; reflecting-wall vs transparent-bounce); Stage 2, conditional on s2, computes `J at ρ_c` (`J≡0` confirms the HH-parent lifted to s2 — my expectation under the reflecting prior; `J≠0` would confirm a fundamental outgoing constraint BC). If Stage 1 fixes s1, Stage 2 is moot and the verdict is HH unconditionally.

**I confirm the converged structure** and author the Structural Verdict below: canonical BC **Hartle-Hawking** at the constraint layer, potential **`S(τ)`**, convention **`-HH`** (with **`-BOTH`** the mandatory BC-invariance diagnostic), expected track **B (BC-robust)**. The e-fold gap was never a BC observable — `N_e=0.1734` is BC-invariant (`efold_ratio=1.0`; the BC flips the sign of `exp(±B)`, never `|B|=22.2552`), and its IC-independence (EFOLD-MAPPING-52) is the structural shadow of the adiabatic/sudden partition (S70) the BC cannot cross.

---

## Structural Verdict

**The Ψ(τ=0) boundary-condition fork is RESOLVED as a layer assignment, not a SPLIT.** The substrate imposes **Hartle-Hawking no-boundary** as the canonical boundary condition on its own wavefunction Ψ(τ) at the WDW CONSTRAINT layer; **Vilenkin tunneling-from-nothing** is not a competing fundamental constraint datum but the LAYER LABEL for the decohered outgoing branch of Ψ_HH's classical limit (Layers 1–2). The two are parent and selected-branch at adjacent layers, not rivals at one layer. Substrate framing throughout: Ψ(τ) is the substrate's OWN amplitude over its OWN Jensen-deformation moduli `{(A_K,H_K,D_K(τ)):τ}` (Level-2 substrate-IS, GEOMETRIC); the BC is the edge-of-deformation datum at the undeformed SU(3), and the direction is `D_K(τ=0) configuration → WDW constraint on Ψ → emergent V_eff/cascade → realized history`.

**(i) Canonical BC — Hartle-Hawking, on three substrate grounds.** (1) The cap weight IS the already-computed spectral action: `Tr f(D_K²(τ)/Λ²) = S(τ) = I_E^internal(τ)`, `Z_fiber(τ)=e^{−S(τ)}` finite at every τ — the no-boundary weight is the substrate's NATIVE object, not a bolted-on postulate (the spectral-action = Euclidean-action identity is shared by both BCs and so neutral on the magnitude `|B|`, but it makes `e^{−S}` the native cap). (2) The framework's own half-line analysis (HT-2) pins a Neumann/reflecting datum `∂_τΨ(0)=0` at τ=0 — zero flux through the undeformed-SU(3) South Pole, with no `τ<0` for flux to escape into (the hard one-sided wall). (3) A reflecting real anchor forces the minisuperspace current `J=Im(Ψ*∂_τΨ)≡0` globally (Eq. H-R3-1, Wronskian conservation, Sage-verified) — Ψ real up to a global phase, time-symmetric, no net outgoing flux at the constraint layer. The irreversible cascade is genuine but EMERGENT: the roll-away of the WKB integral curves on `V_eff` (Layer 1), selected into the experienced outgoing branch by the substrate's own decoherence/DNP complexity arrow (Layer 2) — contained in Ψ_HH, never the datum that sets it.

**(ii) Potential the BC is set on — `S(τ)`, the WDW constraint potential**, τ=0 a genuine S-MINIMUM / regular South Pole (`d²S/dτ²|₀=+304638>0`). The dynamical `V_eff=−S+const` (τ=0 a MAXIMUM, the cascade origin) carries the downstream Lorentzian dynamics ONE LAYER BELOW the BC. No sign tension: the S-min and V_eff-max are the Euclidean and Lorentzian faces of one point with DISTINCT JOBS (quantum-foam's R1 partition, converged) — the S-minimum fixes the shared Euclidean weight `|B|`, the V_eff-maximum governs the realized continuation. The boundary datum on Ψ lives on the constraint face, `S(τ)`.

**(iii) Compute convention — `-HH` canonical, `-BOTH` mandatory diagnostic.** `S116-W6-WDW-IC-REFINE` runs the s1 reduction with `-HH` as the canonical cap weight. `-BOTH` is admissible and mandatory AS A DIAGNOSTIC: running HH and the Vilenkin-branch side-by-side DEMONSTRATES `efold_ratio=1.0` for both (identical `|B|=22.2552`, identical `N_e=0.1734`) — the explicit proof of BC-invariance, a layer-split demonstration, NOT two co-canonical fundamental BCs. `-Vilenkin` is NOT canonical (a branch label, not a constraint datum).

**(iv) Expected track — B (BC-robust).** `N_e=0.1734` is BC-invariant on the single monotone-`S(τ)` trajectory: `N_e_WKB = N_e_classical·(B_traj/B_class)`, bare WDW `efold_ratio=1.0`, so `N_e=0.1734` under HH, under the Vilenkin-branch, and under the layered parent. The BC flips the SIGN of the WKB exponent (`exp(±B)` — a `|Ψ|²` weight selecting growing vs decaying), never the MAGNITUDE `|B|=22.2552` (the count). The acoustic enhancement (`N_e_acoustic=2.8913/2.9202`, 16.7×, S53) still falls short of `N_e_threshold=3.1` (`gap_to_3.1=2.9266`); closing it requires a genuine trajectory ENSEMBLE, and the only two substrate sources — the s2 holonomy allowed-region `∫H dt` (operator question, Q45) and the coupled `(τ,μ,Δ,H)` condensate (dynamics question, HT-3, solved WITH HH retained) — are BOTH orthogonal to the BC. Track A is reachable only through the operator question, never the BC.

**EFOLD-MAPPING-52 (IC-independence) — HH is its no-boundary-side confirmation, extended to the BC layer.** That wall is FAIL-structural: `N_e=0.1734` is IC-INDEPENDENT. A boundary condition is the prototypical IC-type datum; the prediction that the BC cannot move `N_e` is exactly what an IC-independent structural theorem demands. The HH / Vilenkin-branch degeneracy (`efold_ratio=1.0` for both) is the quantum-cosmological-BC-layer IMAGE of EFOLD-MAPPING-52 — two independent results agreeing the e-fold count is not a boundary-tunable quantity. Scope (accepted both sides): the theorem is about the s1 under-barrier `|B|`; the s2 allowed-region `∫H dt` is a DISTINCT functional not constrained by it — which is why the sole route to Track A is the operator question.

**S70 (WKB inapplicability) — routes the count OFF the BC axis entirely.** PROVEN: WKB is structurally inapplicable to the Mach-13.75 van Hove transit (sudden approximation mandatory). The BC governs the ADIABATIC cap (`τ<τ_fold`, WKB valid, where "outgoing" is even well-defined); the e-fold COUNT is set AT `τ_fold=0.19` by the sudden, non-adiabatic transit → **TRANSIT-PS-67** (Mach number, fold sharpness), not by any under-barrier tunneling amplitude. EFOLD-MAPPING-52's IC-independence is the structural shadow of exactly this adiabatic/sudden partition: cap and count sit on opposite sides of the adiabaticity boundary, and the BC reaches only the cap. The fork is moot for the gap by construction.

**Residual (the ONE genuinely open object).** Not a BC fork — an OPERATOR-canonicity question: does the s2 holonomy turning surface `ρ_c≈13.41 M_KK⁴` (`s2_turning_rho=13.4097`, IN-window) survive as canonical, and does the τ=0 reflecting datum survive the holonomy operator (Eq. H-R3-1's load-bearing premise)? `S110-CF1-AT-MINISUPERSPACE` returns `schemes_agree=False` (SPLIT). Carried as `CF-S117-Q45-TAU0-OPERATOR-CANONICITY`; its discriminating measurement is `J at ρ_c under -BOTH`, two-stage (resolve operator canonicity → conditional-on-s2 compute the current). The BC fork RIDES on Q45; it does not precede it.

| Item | Verdict | Note |
|:-----|:--------|:-----|
| Canonical BC | **Hartle-Hawking** (no-boundary, WDW constraint layer) | Vilenkin = decohered outgoing branch of Ψ_HH's classical limit (layer label, not a fundamental constraint BC); reflecting τ=0 datum (HT-2) → real Ψ → `J≡0` (Eq. H-R3-1, Sage-verified) |
| Potential the BC is set on | **S(τ)** | WDW constraint; τ=0 S-MINIMUM / regular South Pole (`d²S/dτ²｜₀=+304638`); `V_eff=−S+const` (τ=0 max) is the downstream dynamical layer — distinct jobs, no sign tension |
| Compute convention tag | **-HH** (canonical); **-BOTH** (mandatory BC-invariance diagnostic) | `-BOTH` demonstrates `efold_ratio=1.0` ⇒ identical `｜B｜=22.2552` ⇒ `N_e=0.1734`; `-Vilenkin` not canonical |
| Expected track | **B (BC-robust)** | `N_e=0.1734` BC-invariant; gap routed to TRANSIT-PS-67 (S70); Track A reachable only via Q45→s2 operator question, orthogonal to the BC |

---

## Remaining Open Questions

1. **Q45 / `S110-CF1-AT-MINISUPERSPACE` operator canonicity (the sole BC-relevant residual).** Does the s2 holonomy reduction's turning surface `ρ_c≈13.41 M_KK⁴` survive as a canonical feature, and does the τ=0 reflecting datum (HT-2 Neumann) survive the holonomy operator, or does the holonomy convert it into a transparent symmetric bounce with an "other side"? `schemes_agree=False`. This is an OPERATOR question, not a BC question; the BC fork rides on it. → `CF-S117-Q45-TAU0-OPERATOR-CANONICITY`.

2. **The s2 current `J at ρ_c` (conditional on Q45→s2).** If s2 is canonical AND the holonomy removes the reflecting datum, is the realized constraint current `J≠0` (fundamental outgoing) or `J≡0` (HH-parent lifted to s2 — the substrate prior under Eq. H-R3-1)? Measurable as `J at ρ_c under -BOTH`; moot if Q45→s1.

3. **Track A ensemble existence (orthogonal to the BC).** Does either substrate ensemble source — the s2 allowed-region `∫H dt`, or the coupled `(τ,μ,Δ,H)` condensate system (HT-3, master-collab Priority 7) — actually deliver high-`N_e` members closing `gap_to_3.1=2.9266`? Both are operator/dynamics questions; neither is a BC observable. The e-fold count itself routes to TRANSIT-PS-67 (S70 sudden-transit kinematics) regardless of the BC.

---

## Wrap-Up

### What Changed

#### (a) Numerical revisions

- None. Every number is fixed/given from the inv11 FAIL verdict; the workshop produced no new numerical value. What changed is the READING of `efold_ratio=1.0` ⇒ `N_e=0.1734`: re-read as a BC-INVARIANCE proof (identical `|B|=22.2552` under HH and the Vilenkin-branch) rather than a single-BC datum. (The `-BOTH` diagnostic in S116-W6-WDW-IC-REFINE will exhibit this side-by-side; it is a demonstration, not a recomputation.)

#### (b) Structural changes

- **HH-vs-Vilenkin fork: 50/50 SPLIT (R1 framing) → LAYER ASSIGNMENT.** Epistemic type change: a competing-fundamental-BC fork became a parent-and-selected-branch relation across adjacent layers — Hartle-Hawking at the WDW constraint layer; "Vilenkin" = the decohered outgoing branch of Ψ_HH's classical limit.
- **Residual relocated: BC layer → OPERATOR layer.** "SPLIT pending Q45 on the BC" (my R1) → "one operator-canonicity question, the BC rides on it." The genuine openness is `S110-CF1` s1/s2, not the contour choice.
- **Discriminator sharpened (Eq. QF-R2-3 → Eq. H-R3-1).** "s2 allowed region ⇒ `J` CAN be ≠0" was necessary-not-sufficient; the τ=0 reflecting ANCHOR forces `J≡0` even on s2 unless the holonomy operator transmutes the datum. The discriminator is operator-gated, not allowed-region-gated.
- **EFOLD-MAPPING-52 IC-independence extended to the quantum-cosmological BC layer.** The BC is the prototypical IC datum; the HH / Vilenkin-branch `efold_ratio=1.0` degeneracy is its BC-layer image — a new confirmation surface for the structural wall.

### What Holds

- **EFOLD-MAPPING-52** (FAIL-structural; `N_e=0.1734` IC-independent) — strengthened, now with a BC-layer confirmation.
- **S70** (WKB inapplicable to the Mach-13.75 van-Hove transit; count → TRANSIT-PS-67) — load-bearing; it is what makes the e-fold gap a NON-BC observable.
- **HT-2** (Neumann/reflecting τ=0 datum on the bare/s1 problem) and **HT-3** (condensate restores a locking minimum at τ₀, no-boundary RETAINED) — both intact; HH is cosmologically completed by the condensate, not by Vilenkin.
- **Substrate-first direction**: `D_K(τ=0) → WDW constraint (HH) → emergent V_eff/cascade → realized outgoing history`. The cascade's inevitability is preserved as emergent Layer-1 dynamics.
- **Foam-side walls untouched** — this is a GEOMETRIC Level-2 moduli-deformation result; no bearing on W-FOAM-4 (structural Lorentz invariance) or any interferometric/LIV surface.

### What Breaks or Strains

- **My R1 Vilenkin-as-fundamental-constraint-BC instruments BROKE under cross-examination**: Eq. QF-R1-1 (the `Z_fiber`/`Z_mod` conflation) and the "leaks into the boundary = outgoing" reading of HT-2. Conceded in R2. The Vilenkin-as-fundamental position does not survive; Vilenkin survives only as the decohered-branch LABEL.
- **STRAIN, fully localized**: the verdict is HH "on the s1 reduction inv11 ran" (unconditional) + "as the substrate prior on s2" (conditional — the holonomy operator could in principle transmute the τ=0 reflecting datum). The strain is carried honestly as `CF-S117`; it does NOT leak into the s1 verdict.
- **No strain on the framework's cosmology**: HH bare-sterility (HT-3 "sends τ→0") is resolved by the condensate WITH HH retained, and the cascade is preserved as emergent dynamics.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

**`CF-S117-Q45-TAU0-OPERATOR-CANONICITY`**
1. **What**: Resolve the `S110-CF1-AT-MINISUPERSPACE` s1/s2 operator-canonicity SPLIT (`schemes_agree=False`): does the s2 holonomy turning surface `ρ_c≈13.41 M_KK⁴` survive as canonical, and does the τ=0 reflecting datum (HT-2 Neumann) survive the holonomy operator — the load-bearing premise of Eq. H-R3-1 — or become a transparent symmetric bounce? Conditional on s2: compute `J=Im(Ψ*∂_τΨ)` at `ρ_c` under `-BOTH` — the s2-image discriminator (`J≡0` = HH-parent lifted; `J≠0` = fundamental outgoing).
2. **Inputs**: `computations/session-110/s110_cf1_at_minisuperspace.py` (s1/s2 builders; `s2_turning_rho=13.4097`, `ρ_c=ρ_relic=26.5539 M_KK⁴`); `computations/investigation-11/inv11_w3_3_wheeler_dewitt_psi_tau.py` (the WDW operator; `G_DeWitt=5.0`, `V=S(τ)`, `E=S(0)`, `B_WKB=22.2552`); the `S116-W6-WDW-IC-REFINE` output (this wave; the `-HH`/`-BOTH` cap solutions).
3. **Gate**: Stage 1 — `schemes_agree` resolved to a single canonical reduction (s1 OR s2) with the τ=0 datum classified (reflecting vs transparent). Stage 2 (conditional on s2) — `|J(ρ_c)|` against a pre-registered threshold separating `J≡0` (HH-parent, `<1e-8`) from `J≠0` (fundamental outgoing). If Stage 1 fixes s1: Stage 2 moot, verdict HH unconditional.
4. **Effort**: medium — two minisuperspace WDW solves on existing operators (s1 + s2) + one conserved-current evaluation; no new substrate spectrum (reuse the inv11 / s110 builders).

Note: the **S116-W6-WDW-IC-REFINE** compute is THIS wave's deliverable (it runs AFTER this verdict fixes the BC to `-HH`/`-BOTH`), NOT a carry-forward.

### Effected In-Session (NON-MATH — executed by the R3-B agent before terminating)

- [x] **Agent-memory note (own domain, executed directly)** — recorded the BC-fork resolution (HH-at-constraint / Vilenkin-as-decohered-branch layer assignment), the Track-B BC-invariance lesson (Eq. H-R3-1: a reflecting real τ=0 datum → `J≡0` → the BC is a `|Ψ|²` weight on a fixed `|B|`, never an e-fold mover), and the methodological lesson (a steelmanned BC fork's residual localizes to OPERATOR-canonicity, not the BC) to `.claude/agent-memory/quantum-foam-theorist/`.
- [ ] **atlas-08 Q12 status update — DEFERRED to §6 Wave-6 synthesis (NOT effected here).** The Q12 cell is a JOINT workshop × `S116-W6-WDW-IC-REFINE` reading and the compute RUNS AFTER this verdict; per curated-doc discipline (`feedback_framework-hygiene.md`) + capstone-hygiene routing, it is reconciled at the §6 synthesis by the designated writer once the compute closes — not in this workshop turn. Flagged for §6.
- [ ] **§7 falsifier-surface / capstone — NO change.** GEOMETRIC Level-2 moduli-deformation result; no §7 observable / σ-distance / detector-horizon bearing. The `mack-cosmic-bridge` sole-writer surface is untouched.

### Closing Line

The substrate's wavefunction caps smoothly at the undeformed SU(3) — Hartle-Hawking at the constraint, with the irreversible cascade riding out as its own decohered branch — and the last open question is not which boundary condition, but which operator.
