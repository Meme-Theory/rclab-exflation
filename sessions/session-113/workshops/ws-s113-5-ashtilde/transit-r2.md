# WS-S112-5 AS-HTILDE — Round 2 (rebuttal)

**Workshop**: WS-S112-5 AS-HTILDE (S113 EVOI-frontier campaign)
**Author**: transit-dynamics-theorist — Round 2, rebuttal (Reading A pole: TD impulse-quench source)
**Date**: 2026-06-22

**One-line R2 thesis**: lizzi's R1 is the strongest possible Reading B, and her organizing frame — the clean split *floor ← TD (+1 leg) / scale ← H̃ (+2 leg)* — is correct and I adopt it. But she has **mis-assigned which expansion rate carries the impulse-quench scale**: the box-delta `|β_k̂|²` rides on the *fold-transit* conformal rate `aH|_fold = 0.975 M_KK` (the `z''/z` pump barrier), NOT the *horizon-exit* `H̃ = 5.9e-3 M_KK` of UNIFIED-AS-79. These are **two different H's, 165× (2.22 OOM) apart, at two different epochs** — and the `a_0/a_2` SDW/Zubarev functional freedom that lizzi localizes ALL the magnitude-openness to is a property of the *horizon-exit* carrier, which the impulse-quench leg **does not read**. So the impulse-quench source is a substrate-determined scale, not a rider on the open `a_0/a_2` leg.

---

## 0. What lizzi got right (conceded cleanly, up front)

I do not contest the following, and I want to be explicit because two of these were genuine corrections to my R1:

1. **The clean split is the right frame.** lizzi's §6(i) verdict — *floor ← TD (S_IC, +1 power, permanent); scale ← H̃ (+2 power, the question)* — is structurally superior to a winner-take-all framing, and I adopt it. The adjudication is not "TD vs LI for everything"; it is specifically *which leg ORIGINATES the amplitude SCALE*. My R1 conflated "the floor is TD-set" with "the scale is TD-set" in places; that was imprecise. The floor (the inequality `A_s ≥ A_s^{BD}`) is settled-permanent and TD-co-owned; this workshop is about the scale-origin only.

2. **The +2 leg-power is the correct leverage principle.** Within the UNIFIED-AS-79 ledger, H̃ is the unique squared leg (`d ln A_s/d ln H̃ = +2`), carrying 14× the A_s-magnitude leverage of the next scheme leg (Sage-verified both sides, machine-exact). lizzi's §1 is correct: *within that functional*, H̃ sets the scale and everything else rides. I do not dispute the leverage hierarchy of AS79.

3. **I overstated "H̃-free" in R1.** My R1 §1.3 claimed the impulse-quench `|β_k̂|²/(2π²)` contains "no H̃ anywhere." That is too strong, and lizzi's §6(ii) correctly flagged it as the decisive test. The honest statement (§2 below) is more nuanced: the impulse-quench `|β_k̂|²` IS governed by an expansion-rate-like quantity — the fold-epoch conformal rate in the `z''/z` pump barrier — so it is not literally H-independent. I retract the "no H̃ anywhere" overclaim and replace it with the precise epoch-and-functional distinction that actually decides the workshop.

With those conceded, the entire dispute reduces to the single question lizzi herself nominated as decisive (§6(ii)): **does the AS3a impulse-quench normalization inherit the route-unstable horizon-exit H̃ (with its open `a_0/a_2` functional freedom), or is it set by a substrate-determined transit-epoch quantity that does NOT carry that freedom?** I now answer it with the substrate data.

---

## 1. lizzi's strongest move, stated fairly

lizzi's §4 ("Where the threat is genuinely live") and §6(ii) make the one move that could win Reading B even granting everything else. Stated at full strength:

> Even if AS3a computes `A_s = |β_k̂|²/(2π²)` *directly* (a KZ-volume count, not the `H̃²/(8π²ε)·S_IC` form), the **scale of `|β_k̂|²` is itself set by the transit's energy injection**, which is governed by the same `a_0/a_2`-driven H̃(τ) trajectory through the fold. So the impulse-quench number is a *dual expression* of the same GGE-relic amplitude (per `_rollup-as-wall §3` "same floor through two functionals"), and its scale inherits the route-unstable H̃ carrier. The KZ-volume normalization is cosmetic; the physics underneath is the `a_0/a_2`-driven expansion rate, so the magnitude-openness (localized to the `a_0/a_2` functional freedom) propagates into the impulse-quench leg too.

This is genuinely the right place to fight, and if it held, Reading B would win the scale-origin question. It does not hold — but for a precise reason that requires distinguishing two expansion rates lizzi's argument silently identifies.

---

## 2. The rebuttal: there are TWO expansion rates, at two epochs, and the impulse-quench leg reads the wrong one for lizzi's argument

### 2.1 What actually sets the box-delta `|β_k̂|²` (substrate data, not assertion)

I traced the AS3a magnitude source to ground truth. `A_s_FW = 1.5367e-08` is `|β_k̂|²/(2π²)` with `N_norm = ξ_KZ³`, where `|β_k̂|²` is read from the **S100b box-delta sudden-limit Bogoliubov spectrum** (`computations/session-100b/s100b_box_delta_bogoliubov.py`). That spectrum's physical inputs (from the script header + `canonical_constants.py:380`) are:

| Input | Value | What it IS |
|:--|:--|:--|
| Barrier `V_box` | 2.7641 M_KK² (branch-c, η_H-corrected) | `≈ 2(aH)²\|_fold` — the **quasi-dS `z''/z` pump barrier at the FOLD** |
| Conformal rate in barrier | `aH\|_fold = 0.975 M_KK` | the **fold-EPOCH** conformal expansion rate (`a(τ_fold)=1`, S77 Q5.3) |
| Pump weights `Ω_z` | `[z'/z]` jumps `= [+1.287, −1.289] M_KK` | the **conformal-rate JUMP** at the impulsive switch boundaries (Z-pump) |
| Transit window `Δη` | `1.130e-3 M_KK⁻¹` | the **impulsive-transit window** width (fold-conformal clock) |
| `μ_pivot²` | 202.0 M_KK² | the in-barrier mode frequency (74× margin) |
| `ξ_KZ` | `0.01876 M_KK⁻¹` | **Kibble-Zurek coherence length** (critical slowing, ν=1/2, z=1, S89 from T1 atlas + BdG) |

**Every one of these is a fold-transit-epoch quantity.** The barrier is the `z''/z` pump structure during the impulsive transit — which the S77 transit workshop maps explicitly: `z''/z = −111(aH)²` at the fold (pump active) `→ 2(aH)²` at pump shutoff (dS attractor, N~1) `→` tachyonic crossing at N=0.036 (`session-77-sp-transit-workshop.md`). The β_k are produced *during this pump window*, governed by the transit trajectory `a(η)` through the van Hove fold (Mach 13.75, fold curvature), the Z-pump conformal-rate jumps, and the KZ freeze-out length. **None of these is the horizon-exit `a_0/a_2` moment ratio.**

### 2.2 The two H's: `aH|_fold` ≠ H̃, by 165× (2.22 OOM)

This is the crux. lizzi's argument identifies "the H̃(τ) trajectory through the fold" with the carrier that sets the scale. But there are TWO distinct expansion rates here (Sage-verified this round):

```
aH|_fold = 0.975 M_KK     ← FOLD-epoch conformal rate; the box-delta |β_k̂|² barrier rides on THIS
H̃ (UNIFIED-AS-79) = 5.9076e-3 M_KK   ← HORIZON-EXIT rate at N_pivot=55; the carrier lizzi's leverage argument is about
ratio = 165.1×   (2.2178 OOM separation)
```

They are **not the same quantity**. `aH|_fold` is the conformal Hubble *during the transit* (the s64 clock `H_fold = 586.527 M_KK` in fold-normalized units, `a(τ_fold)=1`). `H̃` is the horizon-exit expansion rate 55 e-folds later, the Mukhanov-Sasaki boundary value the *frozen* mode reads off. They differ by 165× because they are evaluated at **different epochs separated by the entire post-fold flow**.

lizzi's §2 is precisely correct *about H̃*: the Mukhanov-Sasaki freezing reads off the horizon-exit H̃, and that H̃ carries the `a_0/a_2` functional freedom. **But the impulse-quench `|β_k̂|²` is not a horizon-exit-frozen amplitude — it is a transit-window production amplitude.** The β_k are produced *at the fold* by the pump barrier, then *frozen and conserved* as relics (89/89 frozen-superhorizon, Z_norm=1, AS3a regime resolution). The quantity in its barrier is `aH|_fold`, not the horizon-exit H̃.

### 2.3 The decisive consequence: the `a_0/a_2` openness does NOT propagate into the impulse-quench leg

lizzi localizes the entire magnitude-openness to one place (her §2, §3, §6): the **181× SDW/Zubarev split in `a_0/a_2`** (= 2.26 OOM), the CC-sector functional freedom inside the horizon-exit H̃. Her §3 step 3 is explicit: *"the amplitude scale inherits the latter [the a_0/a_2 functional choice]."* This is the engine of her "magnitude-OPEN" conclusion.

Here is the rebuttal in one line: **that 181× `a_0/a_2` freedom is a property of the horizon-exit H̃ carrier, and the impulse-quench leg does not read the horizon-exit H̃ — it reads `aH|_fold` and the `z''/z` pump.** So the openness lizzi correctly identifies in the UNIFIED-AS-79 leg **does not propagate into the impulse-quench leg**:

```
Substitution chain (Reading A rebuttal):
Step 1: H̃² = (16/3π)·(a_0/a_2)·M_KK⁴/M_Pl²        [lizzi §2; the a_0/a_2 functional freedom lives HERE]
Step 2: the 181× SDW/Zubarev split is a split in (a_0/a_2) at the HORIZON-EXIT epoch [lizzi §3 step 3]
Step 3: box-delta |β_k̂|² depends on {V_box ≈ 2(aH|_fold)², Ω_z=[z'/z]|_fold, Δη, μ_pivot², ξ_KZ}  [§2.1, substrate data]
Step 4: NONE of the Step-3 inputs is (a_0/a_2) at horizon-exit; aH|_fold is the FOLD-epoch transit rate (165× ≠ H̃)
Step 5: therefore d|β_k̂|²/d(a_0/a_2 horizon-exit functional choice) = 0 — the impulse-quench scale does NOT
        inherit the 181× SDW/Zubarev openness
Conclusion: the magnitude-openness lizzi localizes to the a_0/a_2 carrier is ABSENT from the impulse-quench leg.
            The impulse-quench scale is set by the fold-transit pump + KZ freeze-out — substrate-determined.
```

This is *not* the weak "H̃-free" claim I overstated in R1. It is the precise claim: the impulse-quench `|β_k̂|²` is governed by a fold-epoch expansion rate (so it is not H-independent), but that rate (`aH|_fold`) is a **different functional at a different epoch** from the horizon-exit `a_0/a_2`-driven H̃ — and the route-instability lizzi attributes to the magnitude lives entirely in the latter.

### 2.4 Why the "dual expression / same floor through two functionals" reply fails here

lizzi's anticipatory defense (§4 last bullet) is that AS79's `H̃²/(8π²ε)·S_IC` and AS3a's `|β_k̂|²/(2π²)` are dual expressions of one observable, so the impulse-quench scale "is itself set by the `a_0/a_2`-driven H̃(τ)." Two responses:

- **They are dual expressions of the same FLOOR, not the same SCALE-origin.** The `_rollup-as-wall §3` net I co-authored says the two are "the same sign-locked floor seen through different functionals." That is a statement about the *floor inequality* (both give `A_s ≥ A_s^{BD}`), which is exactly the +1-leg object lizzi correctly assigns to TD. It is NOT a statement that the two functionals read the same horizon-exit H̃ for the scale. The rollup's whole point is that the magnitude is *functional-dependent* — i.e., the two functionals give *different scales* — which is the opposite of "the impulse-quench scale is the H̃ scale."

- **"Set by the H̃(τ) trajectory" is true but vacuous for lizzi's argument.** Yes — everything in the post-fold cosmology is "set by the `a(τ)` trajectory" in the trivial sense that the trajectory determines all epochs. But the *route-instability* is not a property of the trajectory; it is a property of the **horizon-exit `a_0/a_2` functional choice** (the 181× SDW/Zubarev split). The impulse-quench leg samples the trajectory *at the fold* (where the pump barrier is `aH|_fold`-set), not *at horizon-exit* (where `a_0/a_2` is read). The trajectory is shared; the *functional that carries the openness* is not. lizzi needs the impulse-quench leg to inherit the `a_0/a_2` freedom specifically — and it samples a different epoch where that freedom does not enter.

---

## 3. The corrected sub-verdict map (lizzi's table, repaired at one row)

lizzi's §5 table is right except for the assignment of the SCALE carrier. The repair:

| Object | Power in AS79 | Owner | Status |
|:--|:--|:--|:--|
| FLOOR inequality `A_s ≥ A_s^{BD}` (S_IC ≥ 1) | +1 | **TD impulse-quench source** | PERMANENT, 3 axes — agreed |
| Amplitude SCALE *in the UNIFIED-AS-79 functional* | +2 (H̃) | LI H̃-divergence | route-unstable, 4.76 OOM, OPEN — agreed *for that functional* |
| Amplitude SCALE *in the impulse-quench functional* | — | **TD: fold-transit pump (`aH\|_fold`, `z''/z`, Ω_z) + ξ_KZ** | **substrate-determined; does NOT read the `a_0/a_2` openness** |
| Functional freedom `a_0/a_2` (181× SDW/Zub) | — | LI horizon-exit H̃ carrier | OPEN — but **confined to the UNIFIED-AS-79 leg**, not the impulse-quench leg |
| Magnitude number `A_s_FW=1.537e-08` | — | S111 AS3a | epistemic-type POINT (AS3b PASS: per-charge GGE NO-SHIFT) |

**The repaired claim**: there is no single "the SCALE carrier." There are TWO scales from TWO functionals — the UNIFIED-AS-79 scale (H̃-carried, horizon-exit, route-unstable via `a_0/a_2`) and the impulse-quench scale (fold-transit-pump-carried, substrate-determined). lizzi's §5 row 4 ("functional selection OPEN") is the openness of the *UNIFIED-AS-79* leg; it is not an openness of the impulse-quench leg, which reads a different epoch's rate.

---

## 4. Honest re-engagement with §EVOI.BF "route-unstable / >3 OOM, no convergence" and the floor-vs-magnitude split

I committed in R1 to engaging this honestly, and lizzi's R1 sharpens it, so I re-engage at the new precision.

### 4.1 The two-layer split is correct, and I affirm it

lizzi and I now agree on the two-layer structure, and it IS the right verdict shape:
- **FLOOR** (`A_s ≥ A_s^{BD}`, `S_IC ≥ 1`): PERMANENT, FUNCTIONAL-INDEPENDENT, 3-axis-confirmed. TD-owned. Not in dispute.
- **Upper-edge / MAGNITUDE scale**: scheme-dependent across *functionals*, with two distinct openness sources — (b-i) the choice of spectral functional (cutoff/zeta/impulse-quench/UNIFIED-AS-79), and (b-ii) within the UNIFIED-AS-79 functional, the `a_0/a_2` horizon-exit freedom.

Where I now diverge from lizzi: she reads (b-ii) as the *dominant* and *universal* openness ("the magnitude is open because the carrier's functional weighting is unpinned"). My §2 shows (b-ii) is **confined to the UNIFIED-AS-79 leg**. The impulse-quench leg's openness is (b-i)-type only (it is *one* functional choice), and *within* that functional its scale is substrate-determined (fold-pump + KZ), not `a_0/a_2`-soft.

### 4.2 So is the honest verdict "TD sets it, pre-registrable" or "floor-permanent / magnitude-OPEN"?

Neither, exactly — and this is where I update my lean honestly. The precise verdict is a **THIRD position** that both R1 poles were circling:

> **FLOOR-PERMANENT (TD-owned, 3 axes). MAGNITUDE = a SCHEME-TAGGED POINT, set by the TD impulse-quench fold-transit source (not the horizon-exit H̃ carrier), pre-registrable AS A TYPED PIN (`A_s_FW = 1.5367e-08`, +0.864 OOM, scheme=IMPULSE-QUENCH-BOGOLIUBOV, epistemic-type POINT per AS3b) — but NOT pre-registrable as a single scheme-INDEPENDENT number, because the cross-FUNCTIONAL spread (b-i) is a genuine registered `SCHEME-DEPENDENT` width.**

This is "TD sets the scale-origin" AND "magnitude carries a scheme-tag" simultaneously. It is *not* "floor-only / magnitude fully open" (lizzi over-reaches: the impulse-quench scale is substrate-determined, not `a_0/a_2`-open), and it is *not* "magnitude fully pre-registrable as a Planck-comparison number" (my R1 over-reached: the cross-functional width is real).

### 4.3 What §EVOI.BF's ">3 OOM, no convergence" actually refers to — and why it does NOT make H̃ the scale-origin

The ">3 OOM, no convergence" is the **cross-FUNCTIONAL spread** (the inv-1 entering incoherence: −3.02 slow-roll / +0.86 impulse-quench / +6.008 near-floor-DOS / +9.5 dump). It is honest and live as an observational-liability flag. But it is a statement about *which functional you pick*, **not** evidence that H̃ originates the scale. In fact §2 shows the opposite: the impulse-quench functional's scale is the LEAST H̃-dependent of the routes (it reads the fold-transit rate, not the horizon-exit `a_0/a_2`), and it is the one inv-1's 8-agent survey diagnosed as the physically-correct functional for an impulsive quench. The ">3 OOM" is the spread *across* functionals including the diagnosed-WRONG slow-roll one; it is not the spread *within* the correct (impulse-quench) functional, which is sub-2-OOM.

So §EVOI.BF "route-unstable" sharpens to: *the cross-functional spread is real and A_s is a live observational liability — but the scale-ORIGIN within the physically-correct functional is the TD fold-transit source, substrate-determined, and the horizon-exit H̃ `a_0/a_2` openness is confined to the slow-roll (UNIFIED-AS-79) leg that inv-1 told us not to use for the floor.*

---

## 5. Summary of the R2 rebuttal

1. **Conceded** (genuine ground): the clean split frame (floor +1 / scale +2) is right; the +2 leg-power leverage hierarchy of UNIFIED-AS-79 is right; my R1 "no H̃ anywhere" was an overclaim.
2. **The crux lizzi nominated** (is AS3a H̃-independent or H̃-routed?) resolves via the substrate data: the box-delta `|β_k̂|²` rides on the **fold-transit** conformal rate `aH|_fold = 0.975 M_KK` (the `z''/z` pump barrier) + Z-pump jumps + ξ_KZ — **NOT** the horizon-exit `H̃ = 5.9e-3 M_KK`. Two different H's, 165× / 2.22 OOM apart, at two different epochs.
3. **The decisive structural fact**: the 181× SDW/Zubarev `a_0/a_2` functional freedom — the engine of lizzi's "magnitude-OPEN" conclusion — is a property of the **horizon-exit H̃ carrier**, which the impulse-quench leg **does not read**. The openness is confined to the UNIFIED-AS-79 leg; it does not propagate into the impulse-quench scale. `d|β_k̂|²/d(a_0/a_2 horizon-exit) = 0`.
4. **"Dual expression" reply fails**: the two functionals are dual expressions of the same FLOOR (the +1 object), not the same scale; "set by the `a(τ)` trajectory" is true but vacuous because the route-instability lives in the horizon-exit functional choice, which the impulse-quench leg samples at a different epoch.
5. **The repaired verdict**: floor-permanent (TD); magnitude = scheme-tagged POINT set by the TD fold-transit source, pre-registrable as a typed pin but not as a scheme-independent number; §EVOI.BF ">3 OOM" is the cross-functional spread (including the diagnosed-wrong slow-roll leg), not evidence for H̃-as-scale-origin.

---

## (i) Updated lean (honest)

**I have moved, and I say so plainly.** My R1 lean was "Reading A, high confidence, the TD source sets the floor and H̃ is sub-dominant," with "no H̃ anywhere" as the spine. lizzi correctly broke that spine: the impulse-quench `|β_k̂|²` is not literally H-free (it rides on `aH|_fold`). I retract the overclaim.

My updated lean is **Reading A on the SCALE-ORIGIN question, but at the refined claim that survives lizzi's challenge**: the TD impulse-quench source sets the amplitude scale **within the physically-correct functional**, because it reads the *fold-transit* expansion rate (substrate-determined: pump barrier + Z-pump + KZ freeze-out), NOT the *horizon-exit* H̃ carrier whose `a_0/a_2` functional freedom is the open leg. lizzi's clean-split frame is right; her *assignment of the scale carrier to the horizon-exit H̃* is wrong for the impulse-quench leg — that leg reads `aH|_fold`, 165× away, where the SDW/Zubarev openness does not live.

On pre-registrability I have converged toward lizzi's caution but not all the way: **floor-permanent + magnitude pre-registrable as a TYPED, scheme-tagged POINT (not a scheme-independent number).** I concede the cross-functional width (b-i) is a real registered `SCHEME-DEPENDENT` tag — that is honest and I will not pretend the magnitude is a clean Planck-comparison prediction. But I do NOT concede lizzi's stronger "magnitude fully OPEN via `a_0/a_2`," because that openness is confined to the leg the impulse-quench source does not use.

Net: **floor ← TD (permanent); scale-origin ← TD fold-transit source (substrate-determined, NOT the horizon-exit H̃); magnitude pin ← typed POINT with a cross-functional scheme-tag; the `a_0/a_2` route-instability ← confined to the UNIFIED-AS-79 leg, NOT the rate-limiter of the impulse-quench scale.**

## (ii) The single crux the R3 verdict must resolve

**Is the box-delta `|β_k̂|²` fold-transit barrier (`aH|_fold = 0.975 M_KK`, the `z''/z` pump) a DIFFERENT functional/epoch from the horizon-exit `a_0/a_2`-driven H̃ — so the 181× SDW/Zubarev openness does NOT propagate into the impulse-quench scale (Reading A) — or is `aH|_fold` ITSELF a reading of the same `a_0/a_2` spectral-moment ratio (just at the fold epoch), so the impulse-quench scale inherits the SAME functional freedom and the openness is universal (Reading B)?**

This is the one fact that flips the verdict, and it is now sharply decidable (it is no longer "H̃-routed yes/no" — that was R1's blunt form). The refined question: **does `aH|_fold = 0.975 M_KK` carry the `a_0/a_2` SDW/Zubarev functional split, or is it fixed by the transit trajectory `a(η)` independently of which regularization weights `a_0` and `a_2`?**

- If `aH|_fold` is transit-trajectory-fixed (a kinematic property of the fold passage, set by Mach number + fold curvature, regulator-invariant) → the impulse-quench scale is substrate-determined, the `a_0/a_2` openness is confined to the horizon-exit leg → **Reading A wins the scale-origin** (magnitude = substrate-determined typed pin).
- If `aH|_fold` is itself an `a_0/a_2` spectral-moment reading at the fold epoch (so the 181× SDW/Zubarev split propagates to the fold barrier and into `|β_k̂|²`) → the impulse-quench scale inherits the functional freedom → **Reading B wins** (magnitude-OPEN, universal across functionals).

R3 must compute (or pin from the existing s64-clock / H_fold provenance) whether `aH|_fold` carries the SDW/Zubarev `a_0/a_2` split. My prediction (to be tested, not assumed): `aH|_fold` is the s64-clock transit rate (`H_fold = 586.527 M_KK` in fold-normalized units), fixed by the fold-passage kinematics, and is NOT recomputed through the horizon-exit `a_0/a_2` regularization choice — so the SDW/Zubarev openness does not reach it, and Reading A holds for the scale-origin. But that pin is the workshop's decisive deliverable, and I do not pre-judge the verdict.
