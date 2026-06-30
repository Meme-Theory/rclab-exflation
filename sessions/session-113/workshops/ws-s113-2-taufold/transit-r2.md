# WS-S113-2 TAUFOLD — Round 2

**Workshop**: WS-S112-2 TAUFOLD (τ_fold dynamical selection vs empirical input), EVOI Tier-2 #4.
**Author**: transit-dynamics-theorist — Round 2, rebuttal (Reading A, responding to lizzi's Reading-B R1).
**One-line thesis**: Lizzi's monotonicity theorem is correct, f-independent, and **answers the wrong question** — it proves the action has no τ-*well*, but "selection ≡ action-stationarity" is an *equilibrium* premise smuggled into a *transit* framework; the substrate's actual τ_fold selector is the van Hove cusp uniqueness theorem (S85-W10, PERMANENT, **co-authored by lizzi**), which is parameter-free and is NOT an action extremum — exactly the category lizzi's definition excludes by fiat. The honest residual is narrower than "τ_fold is empirical like M_KK": it is "does the cusp pin 0.190 specifically, or only the 0.221 DOS-region?"

---

## 0. What I concede to lizzi, up front (no strawman)

Lizzi's R1 is a strong, disciplined case and three of its load-bearing claims are simply correct. I grant them without reservation:

1. **The spectral action is strictly monotone in τ, f-independently** (Structural Monotonicity Theorem, S37; atlas-04 S1 = DISSOLVED; 9,600/9,600 across all monotone f, all Λ, all 10 sectors; `dS/dτ = +58,673 > 0`). This is exactly the S85 NO-WELL fact, and it holds for *every* spectral functional, including S_ζ = a_4. **You cannot regularize your way to a τ_fold well.** I agreed in R1 §1; I re-affirm it.

2. **A gradient flow on S(τ) cannot have an interior fixed point at 0.190.** `τ̇ = −(1/γ)dS/dτ` with `dS/dτ > 0` everywhere drives τ monotonically to a *boundary*, never to an interior value. Lizzi §4(a) is correct, and the WS-CLOCKLOC `S111-CF-CLOCKLOC1-CED` PASS (one-signed `dS/dτ` corridor, `n_zero_corr = 0`) makes it register-permanent. **The gradient-attractor version of Reading A is dead.** I already conceded this in R1 §6 Threat 1 (my own S112 EOM integration shows the modulus launches *from* τ_fold and settles at τ_final ≈ 0.184, not at 0.190).

3. **The §4(c)/§6 discriminator is fair and I accept it as the operative test.** For Reading A to *win*, it must exhibit a substrate-fixed dynamical structure that produces 0.190 *without injecting 0.190*. If any coefficient must be tuned to land on 0.190, the mechanism relabeled rather than selected. Correct framing of the burden.

So I am NOT contesting lizzi's spectral-functional theorem. I am contesting the **definition of "selection"** lizzi builds the whole case on, and I am introducing the selector lizzi's R1 never engages.

---

## 1. The hidden premise: lizzi's argument is "selection ≡ action-stationarity" — an EQUILIBRIUM definition

Lizzi's R1 reduces, structurally, to a syllogism (lizzi §3, §7-ii, verbatim "Selection by an action means stationarity"):

```
P1 (definition):  A modulus is "selected" ⟺ it sits at an interior stationary point of the action.
P2 (theorem):     The spectral action is strictly monotone in τ ⇒ no interior τ-stationary point.
C  (conclusion):  τ_fold is not selected ⇒ τ_fold is an empirical input.
```

P2 is the monotonicity theorem — true, f-independent, conceded. **The entire weight of Reading B rests on P1.** And P1 is an *equilibrium* statement: "the physical configuration is the one that extremizes the action." That is the variational principle of an equilibrium field theory.

But the framework's standing paradigm — the one the knowledge base repeats as a permanent result — is the **opposite**: *"transit physics, not equilibrium; instanton gas, not potential well"* (MEMORY, PARADIGM line; theorem `proven_2249`: "Mechanism chain UNCONDITIONAL. Paradigm shift to transit."). In a transit / quench theory, the selected parameter is **not** an action extremum. It is the **critical point the dynamical flow is forced to cross** — and the critical point of a quench is a *spectral singularity*, not a stationary point of an action.

Concretely: in a thermal quench, the order parameter freezes defects at T_c. T_c is *selected by the spectrum* (it is the thermodynamic singularity where the susceptibility diverges) — and the system **does not sit at T_c**; it crosses it and ends at T ≠ T_c. Nobody calls T_c "an empirical input" because the final state is at T ≠ T_c. T_c is a *parameter-free spectral feature* that the dynamics crosses. **τ_fold = 0.190 is the substrate's T_c, and the van Hove cusp is the spectral singularity.**

So lizzi's P1 is not a neutral definition of "selection" — it is the *equilibrium* notion, and applying it to a transit modulus is the category error. The correct question is not "is τ_fold an action stationary point?" (no — and S85 *proves* it is non-stationary) but "is τ_fold a parameter-free spectral feature the transit is forced to cross?" (yes — S85-W10, PERMANENT).

---

## 2. The selector lizzi's R1 never engages — and lizzi CO-AUTHORED it

Here is the structural gap in Reading B. Lizzi's R1 treats "an action stationary point" as the *only* possible substrate selector, shows there is none in the τ-direction, and concludes "no selector exists." But there is a **second, registered, PERMANENT** substrate selector that is NOT an action extremum:

> **S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM** (PASS, value='promoted', L_max=10; atlas-07 **§VII.M.W10-3**, status **PERMANENT**, authors **"connes + lizzi"**): ρ(λ=0; τ) has a **unique** van Hove cusp at τ_fold = 0.190 on the Jensen-SU(3) × A_F triple (cubic-BC Γ₆, mesh a=12), with the transit-identifier `dS/dτ|_fold = +58,672.80 ≠ 0` locking it **non-stationary**.

This is a **parameter-free spectral-geometric selector** of τ_fold. It is on the books as PERMANENT. And lizzi is a **co-author of it**. Yet lizzi's R1 does not cite it once — the word "van Hove" appears in lizzi's R1 only inside the `dS/dτ = +58,673` monotonicity citation, never as the *cusp uniqueness selector*. Reading B's "no selector exists" is therefore not "we searched and found none"; it is "we defined selection so the existing selector doesn't count."

**Why the cusp is a genuine selector and not an injected condition:**

- The cusp **location is forced by the SU(3) representation content** under the Jensen deformation — it is where the bottom-band eigenvalue λ→0 reorganizes, which is fixed by the cubic-BC Γ₆ corner at mesh a=12. There is **no continuous tunable knob** that slides the cusp; the Jensen deformation has no free parameter that moves it. (Contrast a hand-set freeze-out time, which *is* a free coefficient.)
- It is **unique** in the modulus range — the theorem's verb. Not "a cusp"; "the unique cusp." So it is not one choice among a family; it is *the* spectral singularity.
- It is **over-determined**: Γ₆ (cubic-BC corner) + Γ₅′ (right-convexity, `d²S/dτ² = +317,862 > 0`) + transit-identifier (`dS/dτ ≠ 0`) all co-localize it.

The cusp is to the transit what T_c is to the quench: a parameter-free spectral feature the dynamics crosses. Lizzi's monotonicity theorem does not touch it — which I now prove rigorously.

---

## 3. Sage-verified: a monotone action and a van Hove cusp are LOGICALLY INDEPENDENT (they live on different functionals)

Lizzi §2 argues the action's τ-monotonicity is "the right answer, not a defect" because "a moment-sum has only a growing term." Correct — *for the action*. But the cusp does not live in S(τ); it lives in ρ(λ; τ), a **different functional**. I verified the independence symbolically (Sage MCP):

```
Toy band-edge eigenvalue λ₁(τ) = √|τ − τc|  (the generic van Hove square-root edge):
  dλ/dτ = 1/(2√(τ−τc))  →  +∞  as τ → τc⁺
  ⇒ DOS ρ(0) ~ 1/|dλ/dτ|  DIVERGES at τc          [van Hove cusp]

Same mode's action contribution  S_mode = f(λ²) = exp(−|τ−τc|):
  dS_mode/dτ = −exp(−(τ−τc))  =  FINITE at τc       [no divergence; smooth]

CONCLUSION (Sage): the DOS derivative diverges (cusp) while dS/dτ stays finite.
A monotone S(τ) does NOT preclude a van Hove cusp in ρ. Different functionals.
```

This is the rigorous core of the rebuttal. **Lizzi's monotonicity theorem operates on `S(τ) = Tr f(D_K²/Λ²)` — a smooth moment-sum. The cusp operates on `ρ(λ; τ) = Σᵢ δ(λ − λᵢ(τ))` — the density.** The density's τ-derivative diverges one-sidedly (the van Hove singularity) precisely where the action's τ-derivative stays smooth and positive. So:

- Lizzi §2 proves: **S(τ) has no interior stationary point.** ✓ TRUE.
- Lizzi concludes: **the substrate has no τ_fold selector.** ✗ NON SEQUITUR — the selector is in ρ, not S, and the two are functionally independent (Sage-proven).

The monotonicity of S(τ) is not just *compatible* with the cusp; it is the *transit-identifier itself* — `dS/dτ ≠ 0` is precisely what locks the cusp as non-stationary (S85-W10 Step 5). Lizzi's strongest theorem is, read correctly, **a premise of the cusp-selection argument, not a refutation of it.** The substrate is *pushed through* the cusp (monotone S) rather than *held at* it (which would need a well) — that is the transit, and the monotonicity is what drives it.

---

## 4. The M_KK parallel is false at the selector level — and lizzi's own framing slips on it

Lizzi's positive deliverable (§5) is "τ_fold is the second member, with M_KK, of the permanent external-dimensional-import set; same N₃=0 / single-dimensional-handle wall." This is the move I think the physics most clearly forbids, and lizzi's own §5 wording reveals the seam:

> lizzi §5, line 99 (verbatim): *"they do not fix this one **dimensionful-modulus location**."*

**τ_fold is not dimensionful.** τ is the Jensen deformation parameter — a *pure number* labelling a point in moduli space (the deformation interpolates SU(3) away from the round metric; τ=0 is round, τ_fold=0.190 is the cusp). The N₃=0 single-dimensional-handle wall (S44; the rank-1 Normalization-Non-Universality cause) is a statement about **dimensionful scales** — it says the substrate's spectral data are dimensionless *in M_KK units*, so one overall scale must be imported. That wall has *nothing to grip* on a dimensionless modulus coordinate. A pure number fixed by a combinatorial spectral condition (the Γ₆ corner) is categorically not an instance of "the one mass scale the substrate cannot self-set."

| | M_KK | τ_fold |
|:--|:--|:--|
| Type | **dimensionful** scale (units of mass) | **dimensionless** modulus coordinate (pure number) |
| The N₃=0 wall applies? | **YES** — it IS the single dimensional handle | **NO** — the wall is about dimensionful scales |
| Substrate selector | none (genuinely no handle) | **van Hove cusp uniqueness (S85-W10, PERMANENT)** |
| S112 W1 closure relevance | direct (M_KK IS the closed import) | none — different object |

The `α_s = w·Ô` / rank-1 NNU analogy lizzi invokes (§4b) is likewise a *dimensionful-scale* (w) factoring off a dimensionless shape. τ_fold is not a scale `w` multiplying a shape — it is itself a point in the dimensionless modulus space, and it has a selector. So Reading B's "τ_fold is the second M_KK" rests on miscategorizing a dimensionless cusp-selected modulus as a dimensionful unselected scale. **M_KK has no selector; τ_fold has a PERMANENT one.** That is the asymmetry that breaks the parallel.

---

## 5. Engaging lizzi's §4(b)/§6 honestly — and conceding the genuine residual

Now the part where lizzi is strongest and where I must move my position. Lizzi §4(b): even granting all of the above, for the transit to *land at / cross at* 0.190 rather than some other τ, **a terminating/initiating condition must select where on the trajectory the cusp-crossing sits**, and that condition might carry an imported scale. Lizzi §6 sharpens it: the non-gradient EOM `τ̈ = −3Hτ̇ − (1/5)dV/dτ` could pin an interior τ* from a *balance* of terms, but lizzi predicts the friction/H-normalization (the clock `γ = dt/dτ = 29.7532`, S101 W4) carries the same un-fixed scale — relabeling, not selecting.

This is a real and sharp point, and it converges with the residual I flagged in R1 §6 Threat 3 — **the 0.190-vs-0.221 mismatch**:

- The **DOS-cusp gate** `S85-VAN-HOVE-CUSP-THEOREM` (L_max=8, Baptista-sign) returned the cusp *peak* at **τ = 0.221 and FAILED**.
- The **transit-identifier gate** `S85-W10` (L_max=10) PASSED at **0.190**, where 0.190 sits "on the **rising flank**" of the cusp (my S111-CF-TAUCUSP memory: rel_dev = 0.162609 non-stationarity).

So the honest situation is: **the cusp uniqueness theorem pins a cusp *region* (peak ≈ 0.221), and the precise value 0.190 is the *flank-crossing point* where the transit-identifier `dS/dτ` does additional work.** Lizzi's §4(b) question — "what selects *where on the flank*?" — is exactly the open hinge. If the flank-crossing point 0.190 is L_max-robust and forced by the `dS/dτ ≠ 0` non-stationarity condition (parameter-free), Reading A holds. If only the 0.221 *peak* is L_max-stable and 0.190 is the value matched to the DESI/ACT epoch (the `EMPIRICAL-τ_fold RETENTION` channel, which I confirm is the ACTIVE default fallback: "3 master gears + 1 empirical τ"), then the cusp under-determines 0.190 and lizzi's residual stands *for the precise value*.

**I therefore move my position to a sharper, narrower claim than R1:** Reading A does NOT win "τ_fold is wholly dynamically selected." It wins, *if* the gate passes, "**τ_fold is a van-Hove-selected, transit-crossed structural constant** — the substrate's spectral singularity (the cusp), parameter-free at the *region* level (PROVEN), with the precise flank-value 0.190 pending the L_max-robustness gate." And the thing Reading B genuinely has not earned is the full "τ_fold is empirical like M_KK" — because the cusp selector exists and is PERMANENT, which M_KK has nothing analogous to.

---

## 6. The pre-registrable gate, sharpened to adjudicate lizzi's §4(c) directly

Lizzi and I now agree on the *form* of the decisive test; we disagree on its *predicted outcome*. I pre-register the version that tests the cusp-selection claim against lizzi's "injected datum" prediction:

**Gate A1′ — Cusp-flank L_max-robustness gate** `[VERIFY]` (sharpened from R1 Gate A1):

- **Claim**: the transit-crossing point — the τ where ρ(λ=0;τ) has its van Hove cusp AND `dS/dτ ≠ 0` flank-crossing — is τ = 0.190 ± 0.5%, **L_max-stable across {8, 10, 12}**, with NO τ_fold-dependent input.
- **Inputs**: L12 master spectrum cache (`s84_spectrum_cache_L12_tau019.npz`); `dirac_spectrum.collect_spectrum` rebuild on a τ-grid bracketing [0.18, 0.23]; `dS_fold`, `d2S_fold` canonical anchors. **No injected 0.190** — the grid brackets the region and the cusp-finder + transit-identifier locate the value.
- **PASS** (Reading A wins, in its corrected form): τ_cusp-crossing = 0.190 ± 0.5% stable across L_max, traceable to the Γ₆-corner + `dS/dτ ≠ 0` flank condition (parameter-free). ⇒ τ_fold is a van-Hove-selected structural constant; the `EMPIRICAL-τ_fold RETENTION` default fallback is retired.
- **FAIL** (Reading B wins, *for the precise value*): only the 0.221 peak is L_max-stable; 0.190 requires the DESI/ACT epoch match as the stopping/initial datum ⇒ τ_fold's *region* is cusp-selected but its *precise value* is the imported flank-point — i.e., lizzi's "relabel, don't select" holds *at the 16% level*.

Note what this gate does NOT do: it does not chase a gradient-attractor (lizzi correctly killed that) and it does not require the modulus EOM to settle at 0.190 (it doesn't — it settles at 0.184). It tests the *spectral-geometric* selection (the cusp-crossing), which is the only version of Reading A that survives lizzi's R1 — and which is genuinely distinct from the equilibrium selectors S95 closed.

---

## 7. Updated lean (moved from R1) + the single crux for R3

**Updated lean: ~58% Reading A in its corrected (van-Hove-selected, transit-crossed) form / ~42% Reading B *for the precise value* — moved from R1's 70/30 toward lizzi.**

Why I moved toward lizzi: lizzi's §4(b)/§6 + the 0.221-vs-0.190 flank gap are a stronger, more specific threat than I credited in R1. The cusp uniqueness theorem cleanly defeats lizzi's *general* "no selector exists" claim (the cusp IS a selector, PERMANENT, lizzi co-authored it, and Sage confirms it is functionally independent of the monotonicity theorem) — so Reading B's headline "τ_fold is empirical like M_KK" is **not earned** (M_KK has no selector; the parallel is mis-categorized; τ is dimensionless). But lizzi's *narrow* residual — that the precise 0.190 (vs the 0.221 peak) leans on a flank-crossing condition whose L_max-robustness is unproven — is live and unrefuted, and it is the same residual I flagged in R1. So the contest has narrowed from "selected vs empirical" to "**is the precise flank-value 0.190 parameter-free-and-L_max-robust, or is the 16% peak-to-flank offset an imported datum?**"

Why I did not move further: the equivalence "selection ≡ action-stationarity" that anchors all of Reading B is an equilibrium premise the framework's transit paradigm rejects, and the van Hove cusp is a real, PERMANENT, parameter-free selector of a *different kind* — so "the action provably cannot select τ_fold" is true but does not entail "the substrate cannot select τ_fold," because the substrate selects through the spectral singularity (ρ), not the action (S). Lizzi's strongest theorem is, correctly read, the transit-identifier that locks the cusp — a premise of my case, not a refutation.

**The single crux the R3 verdict must resolve:**

> Granting (a) the cusp uniqueness theorem IS a parameter-free substrate selector distinct from action-stationarity [Reading A's win], and (b) the gradient-attractor is dead and the modulus does not settle at 0.190 [Reading B's win]: **does the van Hove cusp select the precise value 0.190 in an L_max-robust, parameter-free way (the `dS/dτ ≠ 0` flank-crossing at 0.190), or does it select only the cusp *region* (peak ≈ 0.221, L_max=8) while the precise 0.190 is the flank-point imported from the DESI/ACT epoch?** Gate A1′ is the adjudicator. If PASS → τ_fold is a van-Hove-selected structural constant (Reading A, corrected). If FAIL → τ_fold's region is substrate-selected but its precise value is empirically pinned at the ~16% level (a *hybrid* — closer to Reading B than to "wholly selected," but strictly stronger than lizzi's "empirical like M_KK," because M_KK has no cusp-region selector at all).

---

*End of Round 2 (transit-dynamics-theorist). No verdict written; opponent section not authored.*
