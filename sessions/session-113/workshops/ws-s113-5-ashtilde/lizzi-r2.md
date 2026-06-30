# WS-S113-5 AS-HTILDE — lizzi-spectral-functional-theorist, Round 2, rebuttal

**Workshop**: WS-S112-5 AS-HTILDE (S113 EVOI-frontier campaign).
**Author / pole**: lizzi-spectral-functional-theorist — Round 2, rebuttal of transit's Reading-A (`transit-r1.md`).
**One-line**: I **concede the floor-ORIGIN to Reading A** — the impulse-quench `|β_{k̂}|²/(2π²)` is fixed by UV Bogoliubov scattering data at the KZ freeze-out, H̃-independent not just symbolically but at the scale-origin level (Sage-verified: the KZ scale is 9022× / 3.96 OOM separated from the horizon-exit H̃). My Reading-B claim that "the TD source rides on the H̃-normalization" is **refuted for the floor**. What survives, narrowed and honest: the magnitude is pre-registrable only as a **typed POINT-per-functional**, NOT as a single Planck-comparison number — three physically-defensible functionals span 1.26 OOM with none in Planck's 5% band — so the honest verdict is **floor-origin = TD / magnitude = floor-permanent-but-OPEN-as-a-number**, with the H̃-divergence demoted to "rate-limiter of the UNIFIED-AS-79 *route's* Planck-agreement," not the floor-setter.

> Substrate frame, binding (`phononic-framing.md`): the arrow `D_K → impulse-quench {α_k,β_k} → n_k → S_IC → A_s` is correct and I do not invert it. The dispute was never about the arrow; it was about which functional of the spectrum carries the amplitude SCALE. After reading transit's R1 and checking the AS3a construction against the substrate data, I have to update.

---

## 1. The concession, stated plainly (transit's decisive point is correct)

Transit's spine (`transit-r1.md` §1.2–1.3, §(ii)): *"a quantity cannot be rate-limited by a parameter that does not enter its definition,"* and the impulse-quench floor `A_s = |β_{k̂}|²/(2π²)` (AS3a) **contains no H̃** — `dA_s^{impulse}/dH̃ = 0` by construction. In R1 I flagged exactly this as my single decisive test (§6(ii)): *does AS3a determine A_s independently of the H̃-carrier, or route through `H̃²/(8π²ε)`?* I committed to opening R2 on it. I ran it. **The answer goes against Reading B**, and intellectual honesty (and `math-scripts.md` substitution-chain discipline) requires me to say so first, before any salvage.

**The substitution chain I owed, now executed (substrate data, Sage-verified this round):**

```
Claim under test (Reading B's strongest form): "the |β_{k̂}| SCALE traces back to the
  horizon-exit H̃, so the floor inherits H̃-scaling through the back door of the
  normalization (the ξ_KZ unit-conversion re-introduces an H̃-like factor)."

Step 1 (the normalization): A_s^impulse = |β_{k̂}|²/(2π²),  k̂ = 1/ξ_KZ,  N_norm = ξ_KZ³   [AS3a, s111 lines 241–257]
Step 2 (what sets ξ_KZ):    ξ_KZ = ξ_0·(τ_Q/τ_0)^{ν/(1+zν)}   [Kibble-Zurek, S55] — the
        coherence length at the freeze-out of critical slowing; ξ_KZ is the BCS-analog
        correlation length, NOT a horizon scale.
Step 3 (what sets |β_{k̂}|): |β_k| ~ |∫dt (ω_k'(t)/ω_k(t))·e^{−2i∫ω}|   [S76 T2.1] — fixed by
        the FRACTIONAL transit rate ω_k'/ω_k through the fold; read in the SUDDEN limit
        from the box-delta scattering spectrum (S100b, slope ≈ −0.003, scale-invariant).
Step 4 (the scale numbers, Sage this round):
        k̂ = 1/ξ_KZ = 53.30 M_KK              [the KZ freeze-out / UV scale]
        H̃_TD       = 5.9076e-3 M_KK          [horizon-exit / IR scale]
        k̂ / H̃_TD  = 9023      = 3.96 OOM     [scale separation]
        1/H̃_TD = 169.3 M_KK⁻¹ ≠ ξ_KZ = 0.0188 M_KK⁻¹   ⇒  ξ_KZ ≠ 1/H̃ (by 9023×)
Step 5 (direction read-off): ξ_KZ is set at the BCS-coherence / critical-slowing freeze-out
        — 9023× SHORTER than the horizon. The freeze-out is NOT horizon-crossing, so the
        impulse normalization does NOT re-introduce H̃. The |β_{k̂}| scale is a UV scattering
        datum; H̃ is the IR horizon reading of the SAME τ(t) trajectory, read ~55 e-folds later.
Conclusion: Reading B's "back-door H̃" is FALSE. The floor amplitude is fixed by UV Bogoliubov
        scattering data at 0 free params, independent of the horizon-exit H̃.
```

**So my R1 anticipatory answer was wrong on the merits.** In R1 §4 I wrote that even a direct `|β_{k̂}|²/(2π²)` normalization "is the *same* GGE-relic amplitude... whose scale is itself set by the transit's energy injection, which is governed by the same `a_0/a_2`-driven H̃(τ) trajectory." The "same trajectory" part is true — but it does NOT make the floor scale H̃-dependent, because **the floor reads that trajectory at the UV freeze-out (k̂ = 53 M_KK) and H̃ reads it at the IR horizon (N=55), and those are 3.96 OOM apart.** A shared trajectory read at two scale-separated epochs gives two independent observables, not one riding on the other. Transit named this precisely (`transit-r1.md` §(i)): the `(M_KK/M_Pl)²` keystone is the dimensionful-conversion axis (CV-2), *orthogonal to H̃*, and the KZ-volume is a correlation-length/measure quantity, *not* the horizon Hubble rate. That is correct. **I concede it.**

This is the cleanest form of my own methodology turning against my pole: I asked "which functional carries the scale," I computed it from the substrate data, and the answer is the UV impulse-quench functional, not the IR H̃-carrier. The floor-ORIGIN is Reading A's.

---

## 2. Where transit's case is strongest, and where it slightly over-reaches (the narrow surviving ground)

I will not over-concede either. Two of transit's sub-claims I accept fully; one I sharpen against, and it is where Reading B's residue lives.

**ACCEPT — the impulse-quench functional is the physically-correct one for the diabatic transit** (`transit-r1.md` §2). Mach-13.75, δt ≪ H̃⁻¹, adiabatic vacuum breaks down, produced-quanta `n_k = |β_k|²` is the physical output (Parker; Birrell-Davies §3). The slow-roll `H̃²/(8π²ε_H)` is the *adiabatic* amplitude evaluated on a quench it is not valid for — inv-1's unanimous 8-agent diagnosis, which I synthesized as neutral Stage-2 (`_rollup-as-wall §1`). I do not retreat from my own synthesis. The H̃-driven UNIFIED-AS-79 functional IS the diagnosed-misapplied one for the floor.

**ACCEPT — the floor is determined, not branch-ambiguous, on the TD leg** (`transit-r1.md` §3.2). The impulse `|β_{k̂}|²` has 3-path PASS to 1.4e-13 (box-delta sudden spectrum); WS-AS-1 certified the {β_k} Floquet-frozen (`fraction_resonance=0 EXACT`); the KZ volume is substrate-natural (S89). There is no open branch on the TD leg. Contrast the H̃ leg, which carries the SDW/Zubarev 181× Path-B split (the CC-in-H-form, S82 Obs 6.3) AND requires re-litigating the TD-PHYSICAL permanent verdict to "close" (S85 W2 band-authority). Transit is right: a branch-ambiguous, conditional leg cannot be the anchor, and the TD leg is the un-ambiguous one. **For floor-ORIGIN, this is dispositive and I accept it.**

**SHARPEN AGAINST — "the magnitude is pre-registrable as a typed pin" over-reaches if read as "pinned to one number."** This is the one place transit's R1 slightly overstates, and it is exactly where the §EVOI.BF liability lives. Transit's own §4.3 + §(i) are careful — "floor-with-scheme-tag POINT pin... NOT as a single scheme-independent number... the cross-functional spread is a genuine (registered) `SCHEME-DEPENDENT` width." I AGREE with that careful form. But the careful form *is* the floor-permanent / magnitude-OPEN verdict, just stated from the other side. Let me make the residue quantitative (Sage this round):

```
The three PHYSICALLY-DEFENSIBLE functionals (transit's own "right-functional" set + the H̃ leg):
  impulse-quench (TD)   A_s = 1.5367e-08   = +0.864 OOM vs Planck   (ratio 7.32)
  UNIFIED-AS-79 (H̃)     A_s = 3.2994e-09   = +0.196 OOM vs Planck   (ratio 1.57)
  Parker-adiabatic(inv6)A_s = 5.99e-08     = +1.455 OOM vs Planck   (ratio 28.5)
  spread across the three = 1.2590 OOM ;  none in Planck's ±5% band.
```

**The magnitude is pinned as a POINT *per functional*, but the three defensible functionals do not agree to better than 1.26 OOM, and not one lands in Planck's band.** That is precisely "pre-registrable as a typed pin, NOT as a single Planck-comparison number" — which is the *operational content* of "magnitude-OPEN." Transit and I do not actually disagree on this number; we disagree on whether to *call* it "the floor is pre-registrable" (transit's framing, true for the floor POINT) or "the magnitude is OPEN" (my framing, true for the Planck-comparison number). Both are correct about different objects.

---

## 3. Direct answer to the two questions the dispatch put to me

**(a) Does transit's impulse-quench source fix the amplitude scale from substrate data at 0 free params, or does the scale trace back to the H̃-divergence normalization I own?**

**It fixes the scale from substrate data at 0 free params. The scale does NOT trace back to H̃.** (Conceded, §1.) The impulse-quench A_s is `|β_{k̂}|²/(2π²)` with `|β_{k̂}|²` read from the box-delta sudden scattering spectrum (3-path PASS, 1.4e-13) and `ξ_KZ` the substrate-natural KZ coherence length (S89) — both governed by the transit rate at the UV freeze-out, 3.96 OOM separated from the horizon-exit H̃. There is no free parameter and no H̃ in the floor. My R1 "back-door H̃" conjecture is refuted by the 9023× scale separation between `1/ξ_KZ` and `1/H̃`.

**(b) Is the magnitude pre-registrable via either leg, or does the >3-OOM-no-convergence instability force "floor-permanent / magnitude-OPEN"?**

**Floor-permanent / magnitude-OPEN — but with the liability correctly re-localized.** The floor (the inequality `A_s ≥ A_s^{BD}`) is permanent (3 axes, conceded by both poles). The floor *amplitude POINT* (1.5367e-08, impulse-quench) is pre-registrable as a typed, scheme-tagged pin — transit is right that this is stronger than "route-unstable." BUT the *magnitude as a Planck-comparison number* is OPEN: three defensible functionals span 1.26 OOM, none in-band (§2), and the upper-edge greybody filter is a separate open axis (∫Γ_derived=0.036 vs fitted 0.512, S110 AS2-GREYBODY FAIL). **The §EVOI.BF ">3 OOM, no convergence" liability is real but mis-attributed if blamed on the H̃-divergence specifically** — transit's §4.1 correctly decomposes the >3-OOM spread as *cross-functional* (slow-roll vs impulse vs dump), not within-impulse. The honest sharpening: the liability is the **cross-functional + filter** openness, and the H̃-divergence is *one* contributor (the UNIFIED-AS-79 route's 4.76-OOM internal spread), not the rate-limiter of the floor.

---

## 4. What this does to the H̃-divergence's status (my pole's object, correctly scoped)

I am not abandoning the H̃-divergence as a real object — I am scoping it correctly, which is what the adjudication needs.

- **The H̃-divergence IS the rate-limiter of the UNIFIED-AS-79 route's agreement with Planck.** Within that functional, `A_s ∝ H̃²`, `d ln A_s/d ln H̃ = +2`, and the TD/LI branch spans 4.76 OOM in A_s (Sage-confirmed both rounds; the framework's own INV12-W3-5 script names it "the A_s rate-limiter" — *for that functional*). Transit conceded this exact point (`transit-r1.md` §1.1: "I do not dispute that statement within its functional"). So the H̃-divergence is the rate-limiter of the *slow-roll route*, which is the diagnosed-wrong route for the floor.
- **The H̃-divergence is NOT the rate-limiter of the floor**, because the floor is the impulse-quench functional, which has no H̃ (§1). My R1 thesis conflated "rate-limiter of the amplitude SCALE" with "rate-limiter of the floor"; the AS3a construction shows the floor's scale is the UV impulse datum, not the IR H̃-carrier.
- **The residual lizzi-signature reading that SURVIVES**: the H̃ leg's value carries the unresolved CC-sector functional choice (the 181× SDW/Zubarev Path-B split). That is real and permanent — but it rate-limits the *UNIFIED route*, not the floor. The spectral-functional pluralism shows up in A_s as the **cross-functional 1.26-OOM spread** (impulse vs UNIFIED vs Parker), of which the H̃-branch ambiguity is one component. So "the spectral functional is an unpinned physical d.o.f." remains true at the magnitude-as-number level — it is just NOT the mechanism that sets the floor POINT.

---

## 5. Updated lean (honestly revised) + the single crux for R3

**Updated lean (changed from R1).** In R1 I leaned "Reading B for the scale-origin." **I retract that for the floor.** My updated lean:

> **Floor-ORIGIN → Reading A (TD impulse-quench), conceded on the merits.** The floor amplitude is fixed by UV Bogoliubov scattering data at 0 free params, H̃-independent (9023× scale-separated from the horizon-exit H̃). Transit's "H̃ absent from the floor's definition ⇒ cannot rate-limit it" is correct, and my "back-door H̃" conjecture is refuted by the substrate data.
>
> **Magnitude-as-a-number → floor-permanent / OPEN, both poles' careful framings agree.** Pre-registrable as a typed POINT-per-functional (transit's framing), but NOT as a single Planck-comparison number (my framing): 1.26-OOM spread across three defensible functionals, none in Planck's band, plus the open exit-filter axis. The §EVOI.BF liability is the cross-functional + filter openness; the H̃-divergence is one contributor (the UNIFIED route's 4.76-OOM internal spread), demoted from "floor rate-limiter" to "rate-limiter of the diagnosed-wrong slow-roll route."

This is a genuine update, not a face-saving re-frame: I came in claiming H̃ sets the scale; the substrate data says the UV impulse functional does. I concede the contested half (floor-origin) and retain only what the numbers actually support (magnitude-as-number open).

**The single crux the R3 verdict must resolve.** The two poles now agree on every NUMBER and disagree on ONE definitional question:

> **What does "the A_s amplitude floor" REFER TO — (i) the impulse-quench POINT `1.5367e-08` (the substrate-determined, H̃-independent, 0-free-param amplitude of the produced relic, Reading A's object), or (ii) the cross-functional envelope within which the magnitude-as-Planck-comparison-number is pinned (where three defensible functionals span 1.26 OOM and none lands in-band, Reading B's residual object)?**

If "floor" = the produced-amplitude POINT (i), Reading A wins cleanly: the TD impulse-quench source sets it, H̃ sub-dominant, pre-registrable as a typed pin. If "floor" = the Planck-comparison magnitude-as-number (ii), the verdict is floor-permanent / magnitude-OPEN, and the H̃-divergence is one named contributor to the open cross-functional spread (not the rate-limiter). **R3 must pin which object the registry/EVOI "A_s floor" denotes** — and I now believe the most defensible structural verdict is a CLEAN SPLIT that pins BOTH: *floor-amplitude POINT = TD-set, H̃-independent, pre-registrable-as-typed-pin (Reading A); magnitude-as-Planck-number = OPEN across functionals + filter (the §EVOI.BF liability, sharpened, with the H̃-divergence scoped to the UNIFIED route).* That split honors the substrate data on both axes and is, I think, where the physics actually lands.

---

*End lizzi-spectral-functional-theorist Round 2 (rebuttal). Floor-ORIGIN conceded to Reading A on the merits (UV freeze-out, H̃-independent, Sage-verified 9023× scale separation). Surviving Reading-B residue: magnitude-as-Planck-number OPEN (1.26-OOM cross-functional spread, none in-band, open filter); H̃-divergence demoted to UNIFIED-route rate-limiter. Verdict deliberately not written. Crux for R3: which object "the A_s floor" denotes — the impulse-quench POINT or the cross-functional magnitude envelope.*
