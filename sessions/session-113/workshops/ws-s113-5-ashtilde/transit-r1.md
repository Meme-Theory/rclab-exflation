# WS-S112-5 AS-HTILDE — Round 1 (Reading A: TD impulse-quench source)

**Workshop**: WS-S112-5 AS-HTILDE (Session 113 EVOI-frontier campaign; spec `sessions/session-112/session-112-workshop-schedule.md` lines 66–75)
**Author**: transit-dynamics-theorist — Round 1, steelman Reading A (TD impulse-quench Bogoliubov source sets the A_s amplitude floor)
**Date**: 2026-06-22

**One-line thesis**: The A_s amplitude floor is set by the impulse-quench Bogoliubov source `A_s = |β_{k̂}|²/(2π²)` (AS3a, 1.5367e-08), which contains **no H̃** — and a quantity cannot be "rate-limited" by a parameter that does not appear in its definition; the LI H̃-divergence is the rate-limiter of a *different, slow-roll functional* (UNIFIED-AS-79) that inv-1's six-route survey already diagnosed as the WRONG functional for an impulsive quench, so the H̃-divergence is sub-dominant — it is a property of the LI leg, not the floor.

---

## 0. Substrate-first frame (binding throughout)

A_s is NOT an inflaton normalization in an expanding container. It is the squeezing modulus of the post-transit GGE-relic acoustic state — the amplitude of the interference pattern of the relic Bogoliubov excitations of the D_K eigenvalue spectrum after the supersonic transit (Mach 13.75) through the van Hove fold at τ_fold. The arrow is fixed and unidirectional:

```
D_K eigenvalues → impulse-quench Bogoliubov {α_k, β_k} of the fold transit
   → produced occupation n_k = |β_k|² ≥ 0 → squeezing modulus S_IC = 1 + 2 n_k
   → relic power-spectrum amplitude A_s                                          (TR1-0)
```

The adjudication question — "which leg sets the floor, TD-source or LI-H̃-divergence?" — is a question about **which functional of the D_K spectrum the floor IS**. My Reading A: the floor is the impulse-quench Bogoliubov amplitude evaluated on the locked, Floquet-frozen {β_k}; the LI H̃-divergence is internal to a parallel, slow-roll-style functional and rides as a sub-dominant correction, not as the rate-limiter.

I want to be scrupulous about scope at the outset, because the prior record (WS-AS-1, S110) already settled an *adjacent* axis and it would be a category error to re-fight it:

- **The FLOOR `A_s ≥ A_s^{BD}` (`S_IC = 1 + 2n_k ≥ 1`, `proven_1097`) is PERMANENT and FUNCTIONAL-INDEPENDENT** on three orthogonal axes (reference-state inv-12 W1-2 / families-index η-form inv-12 W2-5 / dynamical-Bogoliubov inv-5+inv-6). That is NOT what this workshop adjudicates and I do not re-litigate it. (`sessions/session-110/workshops/ws-as-1.md` §"What Holds".)
- **WS-AS-1 already adjudicated the MAGNITUDE's *epistemic type*** (physical-d.o.f. vs truncation-soft band) and converged to **(A) physical degree of freedom** — the magnitude-bearing observable is the *intensive* UNIFIED-AS-79 pivot coth `A_s = A_s^{BD}·coth(Δ_pivot/2T_pivot)` at ONE mode, NO band-sum. (I was Reading B there and conceded the band-count leg on the merits.)

**WS-S112-5 is a THIRD axis, distinct from both:** not "is the magnitude real" (WS-AS-1, settled (A)) and not "is the floor permanent" (settled, 3 axes), but **"which leg FIXES the amplitude scale — the TD impulse-quench source or the LI H̃-divergence?"** This is a question of *magnitude-origin*, and it turns on a structural fact neither prior workshop foregrounded: the two legs are **two different functionals of the same spectrum**, and only one of them contains H̃.

---

## 1. The decisive structural fact: the two legs are different functionals, and the TD source is H̃-free

This is the spine of Reading A. I establish it first because everything else follows from it.

### 1.1 The LI leg (UNIFIED-AS-79): H̃ IS the lever

The H̃-divergence "rate-limiter" lives entirely inside the UNIFIED-AS-79 five-factor ledger (`computations/investigation-12/inv12_w3_5_cf21_htilde_reconcile.py`, S82 W1-2 canonical):

```
A_s^{UNIFIED} = (H̃²/8π²) · (1/ε_H) · F_amp_slot · (1/c_sub) · f_conv · S_IC          (TR1-1)
```

The five legs `{ε_H, F_amp_slot, c_sub, f_conv, S_IC}` are H̃-INDEPENDENT (branch-shared), so `A_s^{UNIFIED} ∝ H̃²` exactly, and `d ln A_s / d ln H̃ = +2` (CC3, machine-ε). The inv-12 W3-5 script states the rate-limiter logic in its own words (lines 265–266):

> "the fixed legs are H̃-INDEPENDENT; the H̃ divergence passes UNCOMPENSATED into A_s as H̃² (CC3 = +2). **This is why CF21 IS the A_s rate-limiter.**"

I do not dispute that statement **within its functional**. Inside UNIFIED-AS-79, H̃ is the lever, and the TD-vs-LI branch ambiguity (5.9076e-3 vs 2.46411e-5) maps to a 4.76-OOM A_s-space spread. I Sage-verified the exact relationship (this turn):

```
H̃-space TD/LI gap   = log10(5.9076e-3 / 2.46411e-5) = +2.3798 OOM   (atlas "2.38")
A_s-space TD/LI gap  = log10(A_s(H_TD) / A_s(H_LI))   = +4.7595 OOM   (atlas-04 stale "4.56" → live 4.76)
CC3 check:  2 × 2.3798 = 4.7595   (diff = 0.00e+00, machine-exact)
```

**The 4.76-OOM "rate-limiter" gap is exactly 2× the H̃-space gap.** It is the CC3 *image* of an ambiguity in the H̃ branch — a property of the `H̃²/8π²` prefactor of the slow-roll functional. (My memory's shorthand "4.76 = 2×c_sub" is loose: 2×c_sub = 4.476 ≠ 4.76; the correct identity is 2×2.38 = the doubled H̃-gap. I correct that here per `math-scripts.md` mnemonic-vs-exact discipline.)

### 1.2 The TD leg (impulse-quench Bogoliubov): H̃ does not appear

The impulse-quench source (AS3a, `computations/session-111/s111_cf_as3a_impulse_quench.py`, methodology §(1)) is a *completely different functional*:

```
A_s^{impulse} = |β_{k̂}|² / (2π²),   N_norm = ξ_KZ³ (Kibble-Zurek coherence VOLUME),   k̂ = 1/ξ_KZ = 53.30 M_KK   (TR1-2)
```

`|β_{k̂}|²` is read from the S100b box-delta SUDDEN-limit Bogoliubov spectrum (the proper impulse-quench *scattering* spectrum, 3-code-path PASS to 1.4e-13) by near-flat UV-tail extrapolation (slope ≈ −0.003, the scale-invariant sudden signature). This reproduces `A_s = 1.5367e-08` (+0.8644 OOM vs Planck).

**There is no H̃ anywhere in (TR1-2).** Not in the Bogoliubov coefficient `β_{k̂}` (which is fixed by the transit profile through the fold — the time-dependent ω_k(t), not by a horizon-exit Hubble rate), not in the KZ-volume normalization `ξ_KZ³` (a substrate correlation length at the freeze-out of critical slowing), not in the `2π²` (a measure factor). I verified the consequence directly (this turn):

```
d A_s^{impulse} / d H̃ = 0   by construction   (H̃ is not an argument of TR1-2)
contrast:  d ln A_s^{UNIFIED} / d ln H̃ = +2   (the CC3 lever)
```

### 1.3 The conclusion that decides the workshop

> **A quantity cannot be rate-limited by a parameter that does not enter its definition.**

The H̃-divergence is the rate-limiter of `A_s^{UNIFIED}` (TR1-1), where H̃ is the lever. It is structurally *unable* to be the rate-limiter of `A_s^{impulse}` (TR1-2), where H̃ is absent. Reading B's claim — "the LI H̃-divergence fixes the amplitude scale and the TD source rides on it" — requires the TD source to *inherit* the H̃-scaling. It does not: the impulse-quench A_s is a frozen-occupation Bogoliubov normalization, not a slow-roll `H̃²/ε_H` prefactor.

I checked whether the two could secretly be the same number reached two ways (which would rescue Reading B). They are not: the H̃ that UNIFIED-AS-79 would need to *equal* the impulse number 1.5367e-08 is `H̃ = 1.27e-2` — a *third*, different value (ratio 2.16 above H_TD = 5.9076e-3). The impulse-quench floor and the H̃-driven UNIFIED value are **independent functionals that happen to land within ~0.67 OOM of each other** (+0.864 vs +0.196), not one quantity riding on the other.

**Reading A, sharply stated:** the floor is set by the substrate's Bogoliubov scattering data {β_k} through the impulse-quench functional (TR1-2). The H̃-divergence is sub-dominant *to the floor* precisely because it lives in a different (slow-roll) functional whose use on an impulsive quench is the methodological error inv-1 diagnosed (§2). H̃ is a property of the LI leg; the floor is a property of the TD leg.

---

## 2. Why the impulse-quench functional is the *right* one (and the LI/H̃ functional is the diagnosed-wrong one)

Reading A is not merely "the TD number exists." It is "the TD functional is the physically correct one for an impulsive transit, so its amplitude IS the floor; the LI functional (where H̃ matters) is the one inv-1 flagged as misapplied." This is a substrate-physics claim about regime, and it is exactly my domain.

### 2.1 The regime: supersonic transit is diabatic, not slow-roll

The fold transit is Mach 13.75, impulsive (δt ≪ H̃⁻¹). In the diabatic/sudden limit the adiabatic vacuum breaks down and real excitations are produced with occupations set by the **Bogoliubov coefficients**, not by a thermal or slow-roll equilibrium amplitude. This is the founding insight of non-equilibrium QFT in time-dependent backgrounds (Parker; Birrell-Davies §3): when the background changes faster than the system's internal response time, the produced-quanta spectrum `n_k = |β_k|²` is the physical output. The slow-roll Mukhanov-Sasaki `H̃²/(8π²ε_H)` prefactor is the *adiabatic* (quasi-static) amplitude — valid when `ω'/ω² ≪ 1`, which is precisely the limit the supersonic transit violates.

**So the LI/UNIFIED functional (TR1-1) is the slow-roll amplitude evaluated on a quench it is not valid for.** That is not my editorializing — it is inv-1's unanimous six-vantage diagnosis.

### 2.2 inv-1's root-cause diagnosis (8 agents, unanimous)

The CV-1 convergence rollup (`sessions/investigation/_rollup-as-wall.md` §1, synthesized by lizzi as neutral Stage-2) records that the framework's A_s survey (gen-physicist, kaluza-klein, spectral-geometer, landau, transit-dynamics, quantum-acoustics, hawking, feynman) diagnosed a single root cause:

> "an equilibrium free-energy functional applied to a sudden (impulsive) quench. The prescribed fix was unanimous across vantages — a **Bogoliubov |β_k|² / Parker-Bogoliubov power spectrum with adiabatic regularization, not slow-roll 1/ε_H**."

The 2-layer decomposition the six routes converged to (rollup §3) is exactly Reading A's structure:

| inv-1 corpus figure | What it actually is | Functional |
|:---|:---|:---|
| −3.02 / −3.15 OOM (under, S66/S83) | the **slow-roll / equilibrium-functional** route (`1/ε_H`) — the WRONG functional | LI / UNIFIED-AS-79 (H̃-driven) |
| +0.86 → +1.455 OOM (over) | the **impulse-quench Bogoliubov \|β_k\|²** route — the RIGHT functional | TD / impulse-quench (H̃-free) |
| +9.5 OOM | naive aggregate-occupation dump `n_pairs/2π²` — a normalization artifact | (discarded) |
| 4.56 OOM (atlas figure) | a **STALE H̃-space figure** (W3-5 corrects to 4.76 = 2×2.38 via CC3) | LI H̃-branch internal |

The decisive observation for WS-S112-5: **the H̃-divergence appears in this table ONLY in the bottom row — and that row is the LI functional's internal branch-ambiguity, NOT a magnitude source.** The +0.86 OOM floor (Reading A's leg) is on the impulse-quench row, which carries no H̃. The H̃-divergence is a feature of the leg inv-1 told us not to use.

### 2.3 Two independent impulse-quench routes agree, sign-definite, H̃-free

Reading A's floor is not a single number — it is the convergent output of two independent non-equilibrium calculations (rollup §2 "Cross-route consolidation"):

- **inv-5 W2-1**: `+0.86 OOM` (A_s = 1.54e-8), ξ̂³ KZ-volume normalization.
- **inv-6 W2-2**: `+1.455 OOM` (A_s = 5.99e-8), Parker-Bogoliubov P_ζ(k) + adiabatic counterterm; the adiabatic regularization moved A_s DOWN 1.695 OOM from the bare +3.15, **sign-definite-negative correction**.

Both land sub-2-OOM over-production, sign-definite-positive, **neither containing H̃ as a lever**. inv-6 is especially telling: it started from the bare slow-roll over-estimate and the *adiabatic counterterm* (the non-equilibrium correction) brought it toward the floor — i.e., the physics that fixes the amplitude is the Bogoliubov/adiabatic machinery, not an H̃ choice. That two structurally distinct non-equilibrium routes converge to a narrow band is the signature of a *physical* amplitude, not a parameter-driven one.

---

## 3. The LI H̃-divergence is itself unresolved and conditional — it cannot be the anchor

Even granting (for argument) that one wanted the H̃ functional to set the scale, the H̃-divergence is **not a settled rate-limiter** — it is an open, conditional branch choice that the S85 band-authority workshop showed requires re-litigating a permanent-results verdict. A leg that is itself unresolved cannot be the anchor that fixes the floor.

### 3.1 The H̃-divergence resolution requires demoting the TD-PHYSICAL verdict

The S85 W2 band-authority workshop (`sessions/archive/session-85/workshops/s85-w2-as-band-authority.md`, transit × mack) traced the 57% UNIFIED-AS-79 surplus to the H̃ TD-vs-baseline divergence and found (mack, R1 Re:T3):

> "The honest framing: the surplus is **mechanism-CONDITIONAL**. It closes IF and ONLY IF the BASELINE H̃ derivation supersedes the TD verdict. That's not a knob to turn at S86 plan-write; it's a permanent-results-registry change. We should not call it 'closable' without flagging that the closure requires re-litigating the TD-PHYSICAL verdict from S80."

And the S80 H-TILDE-DIVERGENCE-CHASE returned **TD-PHYSICAL as a *conditional* verdict, not a closure** (S85 T4 cache-provenance table). The three candidate H̃ values (TD 5.9076e-3, LI 2.46411e-5, baseline-centre 4.714e-3) are not three measurements of one quantity — the baseline-centre is the **CC3-inverted value that makes A_s PASS by construction** (inv-12 W3-5 §5(c)), i.e. a consistency *target*, not an independent derivation. The LI endpoint is FAIL-GT15 (−4.56 OOM, ruled out). So within the H̃ functional the "rate-limiter" is a still-open branch question.

### 3.2 Reading B's leg is rate-limited; Reading A's leg is determined

This is the asymmetry that decides magnitude-origin:

- **LI/H̃ leg**: the amplitude is `∝ H̃²`, and *which* H̃ is canonical is an unresolved branch choice pending a permanent-results re-litigation (S85/S80). The leg is **rate-limited by H̃** — that is exactly Reading B's framing, and it is correct *for that leg*.
- **TD/impulse-quench leg**: the amplitude is `|β_{k̂}|²/(2π²)`, fixed by the box-delta sudden scattering spectrum (3-path PASS to 1.4e-13) and the KZ coherence volume. There is **no branch ambiguity and no H̃** — the substrate Bogoliubov data determines it. WS-AS-1 (S110) certified the {β_k} are Floquet-frozen (DEAD-by-depth, `fraction_resonance = 0 EXACT`), so the occupations are a locked, conserved Bogoliubov output, not a re-pumping artifact.

The leg that *determines* the floor is the one whose value is fixed by substrate data with no open branch. That is the TD leg. The H̃-divergence is the open question of the *other* leg — it rate-limits the LI route's agreement with Planck, but it does not set the floor, because the floor is the impulse-quench amplitude, which H̃ does not touch.

---

## 4. Honest engagement with the strongest threat: §EVOI.BF "A_s route-unstable / >3 OOM, no convergence"

I will not strawman the threat to Reading A. The §EVOI.BF Bayesian re-anchor (`sessions/evoi-framework.md` line 43) lists, among the observational liabilities that moved the BF cohort DOWN:

> "A_s floor route-unstable (>3 OOM, no convergence)"

Taken at face value, this looks fatal to "the TD source pins the floor": if the routes span >3 OOM with no convergence, how can any single leg be said to *set* the amplitude? Three honest responses, in increasing force:

### 4.1 The ">3 OOM, no convergence" is the inv-1 *entering* incoherence, which the six routes RESOLVED

The ">3 OOM" spread is the inv-1 corpus figure (3.02/3.15/4.56/9.5 OOM, sign-flipping). The CV-1 rollup §3 verdict is explicit: this was a **category error in the register prose** — "those are not four measurements of one quantity that disagree, they are the SAME sign-locked floor evaluated under different spectral functionals." The six routes did not leave it unconverged; they *decomposed* it: the under-production figures are the slow-roll functional, the over-production figures are the impulse-quench functional, the +9.5 is the discarded dump, the 4.56 is the stale H̃-space figure. **The spread is across functionals, not within the impulse-quench functional.** Within the impulse-quench functional, inv-5 (+0.86) and inv-6 (+1.455) converge to a sub-2-OOM band — a ~0.6-OOM spread, not >3.

So §EVOI.BF's "route-unstable" is honest about the *register's historical incoherence* and correctly flags A_s as a live liability — but it is a statement about the cross-functional spread, not a refutation of "the impulse-quench leg sets the floor." Reading A's claim is precisely the resolution of that instability: *pick the physically-correct functional (impulse-quench), and the floor is determined* (+0.86 OOM), with the residual cross-route width being the diagnosed-wrong slow-roll functional you should not be averaging in.

### 4.2 What IS still open is the upper-edge FILTER, and that is a DIFFERENT axis

There remains a genuinely open A_s question, and intellectual honesty requires naming it: the **exit greybody filter** (∫Γ_derived = 0.036 vs fitted 0.512, 14× short; inv-4 W1-4 AND inv-12 W3-4, two independent machineries; S110 AS2-GREYBODY FAIL). But this is the *upper-edge* axis — "is the produced amplitude attenuated on exit?" — **not** the magnitude-origin axis this workshop adjudicates. WS-AS-1's closing line and the S110 AS2 FAIL both scope it as a distinct leg (CF-AS-2), and the floor was certified **permanent** (3 axes) *independently of* the filter. The filter being open does not make the H̃-divergence the floor-setter; it makes the *upper edge* open while the floor (set by the impulse-quench source) stands.

### 4.3 The honest status: the floor IS pre-registrable *as a floor-with-scheme-tag*; the magnitude is a typed pin, not a free band

This is the part where I must be careful not to over-claim. The S111 AS3a verdict pinned `A_s_FW = 1.5367e-08` with the epistemic type set **AS3b-CONDITIONAL** (POINT if AS3b FB-temp PASS / BAND if FAIL). WS-AS-1 register-*predicted* AS3b PASS (the per-charge GGE Lagrange multiplier `λ_k = −ln(n_k/(1−n_k))` is per-mode, so a new high-Casimir sector adds a new `λ_{k'}`, not a shift to `λ_pivot`) ⇒ POINT. So the defensible reading is:

> The A_s amplitude floor is **pre-registrable as a POINT-per-functional with a scheme-tag** (impulse-quench, +0.86 OOM, conditional on the AS3b FB-temp PASS the register predicts), against Planck A_s = 2.1e-9 at OOM-distance +0.864 — and the H̃-divergence is recorded as the *LI leg's* internal branch question, sub-dominant to and structurally separate from the floor.

It is **not** "floor-only / magnitude-free." The magnitude is a typed, scheme-tagged pin (1.5367e-08), with a `SCHEME-DEPENDENT` tag on the cross-functional spread and a `FUNCTIONAL-INDEPENDENT/PERMANENT` sub-annotation on the floor inequality. That is a stronger, more honest status than "route-unstable" — it says *the routes resolved once the wrong functional was removed; the floor is the impulse-quench amplitude; the residual openness is (b-i) functional-choice freedom + (b-ii) the upper-edge filter, neither of which is the H̃-divergence.*

---

## 5. Summary of the Reading A case

1. **Two functionals, one H̃-free.** UNIFIED-AS-79 (TR1-1) has H̃ as its lever (CC3 = +2); the impulse-quench source (TR1-2) `A_s = |β_{k̂}|²/(2π²)` has no H̃. Sage-verified: `dA_s^{impulse}/dH̃ = 0`.
2. **The 4.76-OOM "rate-limiter" is internal to the LI leg.** It is exactly 2× the H̃-space branch-gap (machine-exact), i.e. the CC3 image of an ambiguity in the slow-roll `H̃²/8π²` prefactor — a property of the LI functional, not an amplitude source for the floor.
3. **The impulse-quench functional is the physically-correct one** for a Mach-13.75 diabatic transit (Parker/Birrell-Davies); inv-1's 8-agent survey unanimously diagnosed the H̃-driven slow-roll functional as the *misapplied* one. The H̃-divergence is a feature of the leg we were told not to use for the floor.
4. **Two independent non-equilibrium routes (inv-5, inv-6) converge** to a sub-2-OOM, sign-definite floor, H̃-free, with inv-6's adiabatic counterterm doing the work that fixes the amplitude.
5. **The LI H̃-divergence is itself unresolved/conditional** (S85: closing it requires re-litigating the TD-PHYSICAL permanent verdict; the baseline-centre is a CC3-inverted PASS *target*, not a derivation). A conditional, branch-ambiguous leg cannot be the anchor.
6. **The §EVOI.BF ">3 OOM, no convergence"** is the cross-functional spread (the inv-1 entering incoherence), RESOLVED by the six routes into a functional decomposition; within the impulse-quench functional the spread is ~0.6 OOM. The still-open A_s leg is the upper-edge *filter* (different axis), not the H̃-divergence.

**Net Reading A:** the floor is set by the TD impulse-quench Bogoliubov source; the LI H̃-divergence is sub-dominant — it rate-limits the *LI route's* match to Planck but is structurally absent from the floor's definition.

---

## (i) Honest current lean

**Lean: Reading A, with high confidence on the structural core and a scoped caveat on "pre-registrable."**

My confidence is high that the *magnitude-origin* of the **floor** is the TD impulse-quench source, not the LI H̃-divergence — this is forced, not preferred, by the fact that the floor's defining functional (TR1-2) contains no H̃ while the H̃-divergence is wholly internal to the parallel UNIFIED-AS-79 functional (TR1-1). A parameter absent from a quantity's definition cannot rate-limit it. The inv-1 root-cause diagnosis (slow-roll = wrong functional) and the WS-AS-1 (A)-verdict (the magnitude-bearing observable is the intensive pivot coth, not an H̃²/ε_H prefactor) both point the same way.

Where I hold back: "the magnitude is **pre-registrable**" is true as a *floor-with-scheme-tag POINT pin* (1.5367e-08, +0.86 OOM, conditional on the register-predicted AS3b FB-temp PASS), but NOT as a single scheme-independent number — the cross-functional spread is a genuine (registered) `SCHEME-DEPENDENT` width, and the upper-edge greybody filter (a separate axis) remains open. So the honest verdict shape is "**floor-permanent + magnitude pre-registrable-as-a-typed-pin, set by the TD source; H̃-divergence sub-dominant and LI-internal**" — not "magnitude fully pre-registrable as one Planck-comparison number."

I expect Reading B (lizzi) to press that the H̃ *normalization* is logically prior — that even the impulse-quench `|β_{k̂}|²` must be expressed in physical (M_Pl) units via a conversion that re-introduces an H̃-/scale-like factor, so the H̃-divergence re-enters through the back door of the normalization. My pre-emptive response (to be sharpened in R2): the impulse-quench normalization is the **KZ coherence volume ξ_KZ³** and the measure `2π²`, both substrate correlation-length / measure quantities at freeze-out — NOT the horizon-exit Hubble rate H̃; the M_KK→M_Pl unit conversion is the `(M_KK/M_Pl)²` keystone factor (CV-2), which is *orthogonal to H̃* (it is the dimensionful-prefactor axis, rank-1 PROVEN §VII.BS, inv-3 W2-3's decomposition). The functional-pluralism cross-link (CV-1↔CV-4) is real, but the spread it generates is across *spectral functionals* (cutoff/zeta/impulse-quench/near-floor-DOS), not across H̃ values.

## (ii) Single most decisive consideration

**`dA_s^{impulse}/dH̃ = 0` (Sage-verified) versus `d ln A_s^{UNIFIED}/d ln H̃ = +2` (CC3).**

The impulse-quench source — the leg that produces the +0.86-OOM floor — does not contain H̃. The H̃-divergence is the rate-limiter of a *different* functional (UNIFIED-AS-79), and its entire 4.76-OOM A_s-space footprint is the machine-exact CC3 doubling of an H̃-branch ambiguity internal to that functional. Reading B requires the floor to *inherit* H̃-scaling; the construction shows it does not. The single fact that settles "which leg sets the floor" is that **only one of the two legs has H̃ in it, and it is not the one that sets the floor.**
