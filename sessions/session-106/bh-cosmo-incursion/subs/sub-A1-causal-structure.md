# sub-A1 — Causal Structure: UIBH vs the Framework's Acoustic White Hole

**Author**: `schwarzschild-penrose-geometer` (Lead A recursive sub)
**Date**: 2026-06-13
**Mandate**: INDEPENDENT, adversarial causal-structure analysis. PRIMARY = FALSIFICATION, not confirmation.
**Classification of the GR corpus**: GEOMETRIC / laboratory-IN analogs (per `phononic-framing.md`). The substrate is logically prior; but this document's job is to find where the GR constructions are *more precise, more rigorous, or in genuine tension* with the framework's causal claims — and to say so plainly.

**Sources read in full (verified on disk / via reader, not training knowledge)**:
- Gaztañaga, *The Cosmological Constant as Event Horizon*, Symmetry 14, 300 (2022) = arXiv:2202.00641
- Gaztañaga, *How the Big Bang Ends up Inside a Black Hole*, Universe 8, 257 (2022) = arXiv:2204.11608
- Popławski, *Universe in a black hole in Einstein–Cartan gravity*, ApJ 832, 96 (2016) = arXiv:1410.3881
- Popławski, *Black holes in the expanding Universe* (McVittie critique), CQG 42, 065017 (2025) = arXiv:2405.16673
- Framework anchors: S42 BH-cosmology incursion (`sessions/framework/Collabs/blackhole-cosmology-incursion.md`); S85 W6-1 acoustic-white-hole theorem + W6-4 extremal-horizon theorem (`sessions/archive/session-85/session-85-w6-workingpaper.md`); S95-W4-1 white-hole kinematic-consistency gate (`computations/session-95/s95_gate_verdicts.txt`); S96-GEOM-CCC-WEYL.
- Constants (knowledge MCP): `tau_fold=0.19`, `Mach_max=13.75`, `v_term=26.545`, `w0_FW=-0.918`, `a₀^ζ=6440`, `Λ_cc=(2 f_0/f_2)·a_0`.

> **Honesty note on the framework anchor I am auditing**: I (this agent type) authored the S85 W6-4 extremal-horizon theorem and contributed the W6-1 Penrose catalog. I am therefore auditing my own prior work. I have weighted the adversarial reading accordingly and treat the S95 FAIL (below) as the decisive new datum, not the S85 PASS.

---

## 0. Executive summary — the three throughlines and the sharpest tension

**Throughline 1 (causal-orientation inversion).** The UIBH literature puts the observable region inside a **future** event horizon — a BLACK hole, formed by collapse, ingoing, trapping. The framework's cosmogenesis is formalized as a **WHITE** hole — past-type, outgoing-blocked, time-reverse. These are time-reverses of one another. This is a genuine **orientation tension**, not a match. (§1, §a)

**Throughline 2 (boundary vs bulk Λ).** Gaztañaga's Λ is a Gibbons–Hawking–York **boundary** term (codimension-1, on ∂V₄); the framework's Λ is the a₀ zeroth Seeley–DeWitt **bulk** spectral moment (codimension-0, integrated over V₄). These are different differential-geometric objects answering "what kind of thing is Λ." On the specific question *what is Λ*, Gaztañaga is **more rigorous and more predictive** (a parameter-free relation Λ=3/r_S²); the framework is more *fundamental* but currently *less predictive* about the numerical value. (§b)

**The single sharpest tension (FALSIFICATION-grade).** The framework's acoustic-white-hole "pre/post-transit causal disconnection" is **not stable under its own follow-up computation**. The S85 W6-1 theorem (PROVEN) modeled the transit as a *bracketed pair* of acoustic horizons (τ_H± at 0.196858 and below) enclosing a supersonic interior — a clean, two-sided causal cut. But **S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY returned FAIL** with `N_zeros=1; C1_structure=ASYMMETRIC_open_exit; monotone_supersonic_exit=True`. There is only **one** sonic-horizon zero, and the post-transit side is an **open, asymmetric, monotone-supersonic exit** that never re-closes into a subsonic exterior. A white hole needs a past horizon you cannot reach *backward through*; an open one-zero exit does NOT bound a region the way the W6-1 theorem's bracketed pair does. **The framework's "causally disconnected by supersonic flow" claim is, on its own latest evidence, kinematically STRAINED: the disconnection is real and one-directional (Unruh-type), but the bilateral "sealed interior" picture is overstated — exactly the overstatement the S85 wrap-up itself flagged ("The W6-1 plan text overstated the disconnect direction… Unruh is one-directional; the framework inherits that").** Meanwhile the GR models (Gaztañaga, Popławski) make their global causal cut *exactly* — it is a true event horizon with a proven, coordinate-independent definition. **Here the GR literature is more rigorous than the framework about the very claim the framework imports from it.** (§c, §FALSIFICATION)

---

## 1. What kind of horizon is each construction? (the orientation question — §a)

### 1.1 Definitions I will hold everyone to

A horizon claim is only physical if it is coordinate-independent. I use:
- **Future event horizon / black hole**: boundary of the causal past of future null infinity, ∂J⁻(ℐ⁺). Outgoing null congruence has θ ≤ 0 on it; it is the boundary of a **future-trapped** region. Matter crosses **inward**; nothing crosses outward. Formed by collapse.
- **White hole / past horizon**: boundary of the causal future of past null infinity, ∂J⁺(ℐ⁻). It is the time-reverse: matter crosses **outward**; nothing crosses inward; no signal from the exterior can reach **into** the interior's past. A white hole is **anti-trapped**.
- **Acoustic (Unruh) horizon**: surface where flow speed v equals sound speed c_s in the acoustic metric g_ac = Ω²g_M. Surface gravity κ_ac = ½|d(c_s²−v²)/dn|. It is an emergent feature of the *effective* metric; the microscopic theory is regular and continues through it (Volovik, S42 §I.4). A *supersonic-exit* acoustic horizon (flow accelerating outward through c_s) is the acoustic analog of a **white** hole; a *supersonic-entry* one is the analog of a **black** hole.

### 1.2 The corpus, classified

| Construction | Horizon type | Orientation | Trapped/anti-trapped | Formed by | Source |
|:--|:--|:--|:--|:--|:--|
| **Gaztañaga BHU** | True future event horizon r_S=r_Λ | **BLACK** (ingoing) | future-trapped ("matter trapped inside r_S", R⁻²) | gravitational collapse 25 Gyr ago | 2202.00641 §2.1; 2204.11608 §3 |
| **Popławski ECSK** | True future event horizon → ER bridge | **BLACK** (ingoing, unidirectional) | future-trapped (Tolman–Bondi interior → singularity, then torsion-bounced) | collapse + torsion bounce | 1410.3881 §1, §"unidirectional" |
| **Framework cosmogenesis** | Acoustic supersonic horizon(s) in g_ac | **WHITE** (outgoing-blocked) | anti-trapped (supersonic *exit*) | first-order phase transition at τ_fold | S85 W6-1; S95-W4-1 |

**The verdict on (a): this is a TENSION (time-reverse), not a match, and not orthogonal.**

Gaztañaga is unambiguous: "matter gets **trapped inside** the event horizon r_S"; "the BH Event Horizon r_S **forbids anything to escape**"; "nothing can come out of a BH" (2204.11608 §3.8; 2202.00641 §3). This is the defining property of a **future** horizon enclosing a **future-trapped** region. Popławski is equally explicit: "matter… **bounce[s] and then expand[s] into a new region of space on the other side of the event horizon**"; "the motion of matter through the event horizon is **unidirectional**" (1410.3881). His interior begins as a *collapsing* Tolman–Bondi region inside a future horizon and is torsion-bounced into expansion.

The framework's S85 W6-1 theorem is, by contrast, an **acoustic white hole**: "future-directed ingoing null curves from the post-fold subsonic exterior **cannot reach** the pre-fold subsonic exterior"; "no past null infinity ℐ⁻ of the post-fold subsonic exterior is reachable from the supersonic interior — the acoustic-analog **white-hole** causal structure." The framework's own modulus docs label τ=0 the "white hole — dynamically repulsive" (S31C, S39). White hole ↔ black hole are time-reverses.

> **Why this matters and is not a quibble.** A black-hole cosmology (Gaztañaga/Popławski) and a white-hole cosmogenesis (framework) make *opposite* statements about the arrow of the causal cut. In the BHU, your past is the collapse and the horizon is in your future (you can never send a signal out). In the framework's acoustic white hole, the disconnection is the other way: the post-fold region cannot send signals *back* into the pre-fold region's past. The framework is, structurally, the **time-reverse** of the UIBH literature's interior. The two pictures cannot both be "the same causal structure" — at most one is the time-reverse of the other, which is the honest reading.

**Strength rating of any claimed (a)-correspondence: WEAK (2/10).** What they genuinely share is only the *topological* fact "observable region sits behind a one-way causal feature." The *orientation* (future-black vs past-white) is opposite, and orientation is the physically load-bearing content. Calling them "the same" inverts a time-direction.

---

## 2. Λ as boundary term vs Λ as bulk spectral moment (§b)

### 2.1 What Gaztañaga actually derives (and it is tight)

From 2202.00641 §2, the on-shell Einstein–Hilbert action for a perfect fluid reduces to a **pure boundary term** via the Raychaudhuri equation:

```
S_on-sh = ∫_V4 dV4 (∇_μ g^μ)/(8πG) = ∮_∂V4 dV_μ g^μ /(8πG) = ⟨ Λ/(4πG) − (ρ+3p) ⟩ V4      [his Eq. 8]
```

Requiring the boundary term to vanish on a region bounded by an event horizon forces

```
Λ = 4πG ⟨ρ + 3p⟩_V4         [Eq. 9]   ⇔   r_Λ = √(3/Λ) = r_S = 2GM,   Λ = 3/r_S²
```

Equivalently (his §2.2), if one does *not* set the boundary term to zero, one must add the **GHY boundary term** S_GHY = (1/8πG)∮_∂V4 d³y √(−h) K, and on a time-like junction at R=r_S with K=−2/r_S this evaluates to S_GHY = −(r_S/G) t, which exactly cancels the Λ-term S_Λ = −r_S³Λt/3G **iff** Λ=3/r_S². His sentence: *"the evolution inside a BH event horizon induces a Λ term in the EFE even when there is no Λ term to start with."*

**This is a codimension-1, on-the-boundary object.** Λ lives on ∂V₄. It is *not* a property of the bulk vacuum; it is the price of having a causal boundary. And it is **parameter-free and predictive**: given that we are inside our own r_S=r_Λ (which the measured acceleration *implies*, via Eq. 11: r* = a∫dt/a ≤ 1/H_Λ = r_Λ), Λ is fixed to 3/r_S² with no tuning. He even gets the coincidence problem for free: ρ_Λ ~ ρ_matter because both are "the matter content inside the boundary."

### 2.2 What the framework's Λ is

From the knowledge base (verified): the framework's cosmological constant is the **a₀ zeroth Seeley–DeWitt coefficient** of the spectral action,

```
Λ_cc = (2 f_0 / f_2) · a_0,     a₀^ζ = 6440  (regulator-pinned, zeta),   w0_FW = −0.918.
```

This is a **codimension-0, bulk** object: a₀ = ∫_M √g · (spectral density) is an *integral over the whole 4-volume*, the zeroth heat-kernel moment Tr e^{−tD²} ~ Σ a_n t^{(n−4)/2}. In the framework's own framing law (`phononic-framing.md`): "Spectral action zeroth moment a_0 — a DIFFERENT spectral moment than gravity (a_2)." Λ is bulk vacuum spectral weight, full stop.

### 2.3 Is "boundary vs bulk" a genuine contradiction about what Λ IS?

**Yes — and it is a clean, differential-geometric contradiction, not a vocabulary clash.** A boundary term ∮_∂V K√h and a bulk term ∫_V a_0 √g are objects of *different codimension*. They are related by Stokes/the divergence theorem only under special conditions; in general one cannot rewrite a GHY boundary integral as a bulk a₀ integral, because GHY is precisely the term whose job is to make the bulk Einstein–Hilbert variational problem well-posed *in the presence of a boundary*. Gaztañaga's Λ exists *because there is a boundary* (no horizon → no Λ → Minkowski, which he explicitly takes as the empty-space limit). The framework's Λ exists *with no boundary at all* — it is the substrate's bulk spectral density at τ_frozen, present whether or not any horizon exists.

The S42 incursion already tested the bridge between these and found it does **not** close cleanly: Volovik/Hawking showed that treating the GHY/horizon term as the source of the observed Λ ("P_ext = P_GHY ~ κ/8πG") gives the **wrong scaling** (∝1/M_BH; fine-tunes M_BH; II.6: "the hierarchy survives as a hierarchy in the function f"). That is the framework's own internal finding that Gaztañaga's boundary-Λ does *not* map onto the framework's bulk-a₀-Λ by a thermodynamic matching.

### 2.4 Which is more rigorous / predictive about Λ?

I split this honestly:

| Axis | Winner | Why |
|:--|:--|:--|
| **What kind of object Λ is (fundamentality)** | Framework | a₀ is derived from the spectral triple with zero geometric free parameters; it is not contingent on the existence of a boundary. Λ-as-boundary is contingent — remove the horizon and it vanishes. |
| **Predictivity of the numerical value of Λ** | **Gaztañaga** | Λ=3/r_S² is parameter-free *given* we are inside r_Λ, and the coincidence ρ_Λ~ρ_m falls out. The framework's a₀=6440 fixes a *bare* spectral value but the route to the *observed* 10⁻¹²² requires q-theory self-tuning + GGE residual (S42), which is NOT yet a closed numerical prediction (CC-QTHEORY-43 was pre-registered, predicted FAIL). |
| **Rigor of the global-structure claim** | **Gaztañaga** | His "Λ = causal boundary" is a theorem about ∂J⁻(ℐ⁺) with the Israel junction explicitly satisfied (no surface terms). The framework's "Λ is a bulk moment" is rigorous as spectral geometry but says nothing about global causal structure — it does not, by itself, predict that we are inside any horizon. |

**Verdict on (b): genuine contradiction about the *nature* of Λ (boundary vs bulk). Gaztañaga is more rigorous and more predictive about Λ-the-number and Λ-the-causal-object; the framework is more fundamental about Λ-the-thing.** This is a place where the GR construction *exceeds* the framework on its own turf (predicting the value/meaning of Λ), and I flag it as such.

**Strength rating of a boundary↔bulk correspondence: VERY WEAK (1.5/10).** They are different-codimension objects; the S42 matching gives the wrong scaling. Treating them as "the same Λ seen two ways" is not supported.

---

## 3. Torsion bounce vs supersonic phase-transition white hole (§c) — the core falsification

### 3.1 The three global causal structures, stated precisely

**(i) Popławski ECSK (1410.3881).** Tolman–Bondi cold collapse inside a parent's **future** event horizon. Each comoving point "locally evolves toward the singularity as an independent, spatially homogeneous, isotropic universe." ECSK torsion (spin–spin repulsion ~ −κ²·n_F²/density) halts collapse at finite (sub-Planck) density → bounce → expanding **closed** FLRW. The horizon becomes an **Einstein–Rosen bridge** to the parent. The arrow of time is *defined* by the **unidirectional** matter flux through the horizon (his §"unidirectional", Eq. 43: dS/dt > 0 entropic + horizon-flux). Key for my Weyl mandate: **"For the FLRW metric, the Weyl tensor vanishes"** — the bounced interior is conformally flat.

**(ii) Gaztañaga BHU (2202.00641, 2204.11608).** A homogeneous dust cloud of M≈5×10²² M_⊙ free-falls, crosses its own r_S 25 Gyr ago (forming a true future horizon), continues to collapse to nuclear saturation, and **bounces** (Pauli/neutron-degeneracy, supernova-like) into the hot Big Bang. Interior = FLRW (2Φ=−r²H²); exterior = Schwarzschild (2Φ=−r_S/r); glued by **Israel junction at R=[r_H² r_S]^{1/3}** with *no surface terms*. The frame-duality (FLRW comoving ↔ quasi-static Schwarzschild) is a **Lorentz contraction** relabeling, *not* a maximal extension. He never invokes a white hole or a Kruskal/Penrose maximal extension; the cut is a single future horizon. Expansion freezes as a→1 because "nothing can come out of a BH."

**(iii) Framework acoustic white hole (S85 W6-1).** On the 2D modulus-time slice, the acoustic (Painlevé–Gullstrand) metric is
```
g_ac = −(c_s²(τ) − v²(τ)) dt² − 2 v(τ) dt dτ + dτ²,   v = v_term = 26.545,  c_s(τ_fold)=1.9305,  Mach=13.75.
```
S85 W6-1 modeled c_s(τ)=v_term·[1/Mach_max + A·tanh²((τ−τ_fold)/δ_h)], giving **two** sonic horizons τ_H± (roots of v=c_s) bracketing a supersonic interior, with a one-directional disconnect: the supersonic interior cannot reach ℐ⁻ of the post-fold subsonic exterior (Unruh-type). SEPARATELY, the dump τ=0.19 is an **extremal Killing horizon** in the *modulus* metric ds²=−V dt²+dτ²/V with V=V₀(τ−τ_dump)²: κ=0, T_H=0 (S85 W6-4, which I authored).

### 3.2 The κ=0 problem (the prompt's pointed sub-question)

The prompt asks: *does an acoustic white hole at κ=0 actually disconnect pre/post, given κ=0 means T_H=0 and a degenerate/marginally-trapped surface?*

This requires care, because the framework has **two distinct horizons at τ≈0.19** living in **two different effective metrics**, and conflating them is an error I want to head off:

- The **acoustic** horizons τ_H± live in g_ac (the *acoustic* metric). At τ_fold, Mach=13.75≫1; the sonic horizons have **nonzero** κ_ac (the W6-1 disconnect is driven by v−c_s ≠ 0 derivative; the related BCS sonic horizon has κ_BCS=4.019). The disconnect is a *kinematic* statement about null modes of g_ac.
- The **extremal** horizon Σ_dump lives in the *modulus* metric (the Schwarzschild-like ds²=−V dt²+dτ²/V), and there κ=0, T_H=0.

So the κ=0 result is **not** the surface gravity of the acoustic white hole; it is the surface gravity of the *modulus-space* horizon at the freeze-out. The framework's own W6-4 working paper says exactly this ("κ_BCS is the surface gravity of a SONIC horizon… κ(τ_dump)=0 is the surface gravity of the MODULUS-SPACE canonical horizon… the two horizons coexist").

**Now the adversarial point.** κ=0 / T_H=0 at the modulus horizon means it is **extremal** = **marginally trapped** (degenerate double root V=V′=0). An extremal horizon is a *degenerate* causal boundary: in the classical Reissner–Nordström/Kerr extremal limit, the surface gravity vanishes, the Hawking temperature vanishes, and the horizon recedes to infinite proper/affine distance along the relevant null generators (the throat becomes infinitely long; cf. the extremal-RN "infinite throat"). **An extremal horizon is therefore the *weakest* kind of causal disconnector**: zero temperature, zero generative power, and — crucially for a *white* hole — zero outgoing flux (T_H=0 means no white-hole emission). The framework's own W6-4 reading: "Σ_dump is thermodynamically null… no Hawking-like radiation channel." A white hole with **zero** emission temperature is, thermodynamically, *not emitting* — which is in tension with the intuitive "white hole spews stuff out" picture but consistent with "frozen, silent boundary."

**This is the honest synthesis of the κ=0 sub-question:**
1. The κ=0 modulus horizon does NOT by itself "causally disconnect pre/post" — it is a *freeze-out marker* (a critical point of the spectral action, dS/dτ=0), thermodynamically silent, marginally trapped. It is the framework's analog of an *extremal* (degenerate) horizon, the **least** dynamically active kind.
2. The *causal disconnection* claim rests entirely on the **acoustic** horizons (nonzero κ_ac, Mach≫1), NOT on the κ=0 modulus horizon.
3. Therefore the prompt's worry is well-founded: **if one reads the disconnection as coming from the κ=0 extremal horizon, the claim collapses** (an extremal/marginal surface with T_H=0 is a degenerate disconnector). The disconnection only survives if it is the *acoustic* (supersonic) horizons doing the work — which moves us to §3.3, where the S95 FAIL bites.

### 3.3 The S95 FAIL: the supersonic disconnect is asymmetric and open

This is the decisive datum. **S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY: FAIL**, with verdict value:
```
N_zeros=1; C1_structure=ASYMMETRIC_open_exit; tau0=0.112443; kappa0=-18.442205;
sign_entry_d_disc=-36.884410; graze_min_abs=1.936988e-03; disc_far_max=-1.936988e-03;
monotone_supersonic_exit=True
```
Reading this against the S85 W6-1 theorem:

- **S85 W6-1 (PROVEN)** claimed a *bracketed pair* τ_H± (two zeros of v−c_s) enclosing a finite supersonic interior — a two-sided sonic cut, like a finite supersonic nozzle region.
- **S95 W4-1 (FAIL)** finds **N_zeros = 1**: a *single* sonic crossing at τ₀=0.1124, with κ₀=−18.44 (note: **negative** surface gravity), and the post-crossing branch is `monotone_supersonic_exit=True` with `C1_structure=ASYMMETRIC_open_exit`. In plain terms: the flow crosses the sound speed **once** and then stays supersonic monotonically — there is **no second horizon re-closing the region into a subsonic exterior on the far side.**

**Why this is a falsification-grade tension with the framework's causal claim:**
- A clean *white-hole* disconnect (the W6-1 picture) needs the supersonic interior to be **bounded** so that "the post-fold subsonic exterior's ℐ⁻ is unreachable from the interior" is a statement about a *bounded* interior with a well-defined past horizon. With only one zero and an open monotone-supersonic exit, the "interior" is **half-open**: the far side never returns subsonic. The two-horizon bracketing the W6-1 theorem relied on (via the engineered tanh² profile reaching back above c_s) is **not** what the S95 kinematics produce.
- The negative κ₀ and the ASYMMETRIC label say the entry and exit are *not* mirror images — the structure is not the symmetric bracketed pair but a single asymmetric transition. The S85 wrap-up itself confessed: *"The W6-1 plan text overstated the disconnect direction… Unruh is one-directional; the framework inherits that."* S95 sharpens this from "one-directional" to "**one-zero, open exit**."

**So the framework's "pre/post causally disconnected by supersonic flow (Mach 13.75)" claim, audited against its own latest gate, is:**
- **TRUE in the weak sense**: there *is* a one-directional Unruh-type disconnect (signals from post-fold cannot propagate backward through the single supersonic crossing into the pre-fold past). This part survives.
- **OVERSTATED in the strong sense**: there is NOT a clean bounded supersonic interior bracketed by a horizon *pair*; the exit is open and asymmetric. The framework cannot claim a *sealed* causally-disconnected interior the way Gaztañaga and Popławski claim a sealed black-hole interior.

### 3.4 Consistency with the global causal structure the GR models require

Gaztañaga and Popławski both require, and rigorously have, a **bona fide future event horizon** — a global, coordinate-independent, two-sided causal boundary (∂J⁻(ℐ⁺)), with the Israel junction (Gaztañaga) or the ER-bridge throat (Popławski) supplying the exact matching. Their interiors are genuinely sealed: outgoing θ≤0 everywhere inside, no signal escapes, ever.

The framework's acoustic structure is, by contrast, an **emergent kinematic** feature of g_ac that (per Volovik, S42 §I.4, the framework's own theorist) is "**NOT a thermodynamic boundary**… the superfluid continues beyond the horizon… the horizon is an emergent feature of the effective metric, **not a wall**." And per S95, it is a *single asymmetric* sonic crossing, not a sealed interior.

**Verdict on (c): the framework's "causally disconnected by supersonic flow" is STRAINED — consistent only in the weak/one-directional sense, and STRICTLY WEAKER than the global event-horizon disconnection the GR models prove.** The GR models make a precise, global, two-sided causal cut. The framework makes a kinematic, one-directional, single-crossing, emergent (non-wall) cut that its own S95 gate shows is asymmetric and open. **This is the central place where the framework hand-waves a causal claim that the GR models make precise.**

**Strength rating of a torsion-bounce ↔ supersonic-white-hole correspondence: WEAK (3/10).** Both replace a singularity with finite-density physics (torsion repulsion vs BCS quench) — that *mechanism-level* parallel is real (see §3.5). But the *causal structures* are different in kind (sealed future-horizon interior + ER bridge vs emergent one-directional open acoustic crossing) AND opposite in orientation (black vs white).

### 3.5 What DOES genuinely transfer (so I am not only negative)

Three structural parallels survive adversarial scrutiny, and I rate them:
- **Singularity avoidance by finite-density physics** (STRENGTH MODERATE, 6/10): Popławski's ECSK torsion bounce, Gaztañaga's neutron-degeneracy bounce, and the framework's first-order BCS phase transition at τ_fold all replace the t=0 curvature singularity with sub-Planck, finite-density physics. The framework's S42/S85 "no singularity; phase transition" is *structurally* the same move as a bounce — though the framework insists it is a *quench*, not a *bounce* (no contracting pre-phase in the physical universe; the contraction is in modulus-time, see Throughline-3 caveat below). All three respect Penrose-1965-style avoidance only by violating the relevant energy/regularity condition at the bounce (torsion → effective NEC violation; BCS → the framework's DNP/NEC-boundary at τ_NEC=1.382).
- **Weyl-curvature behavior at genesis** (STRENGTH MODERATE, 6/10): Popławski notes "**for the FLRW metric the Weyl tensor vanishes**" — his bounced interior is conformally flat (C=0). The framework's genesis τ=0 is the **WCH minimum**: |C|²(0)=5/14 minimal, round metric, "conformally flat by construction" on the spatial slice (S44, S96). **Both put minimal/zero Weyl at the beginning and let it grow** — the framework's S96-GEOM-CCC-WEYL proves d|C|²/dτ>0 (monotone from 5/14). This is a *real* shared structure: both are Penrose-Weyl-curvature-hypothesis–compliant (low Weyl at the start, Weyl grows with clumping/complexity). I rate this the **strongest genuine correspondence in the whole comparison**. (Caveat: the framework's |C|² is *not exactly zero* at genesis — Type O is impossible by SU(3) structure constants — whereas Popławski's FLRW Weyl is *exactly* zero. So even here the framework is "minimal-Weyl" not "zero-Weyl.")
- **One-directional time arrow** (STRENGTH MODERATE-WEAK, 4/10): Popławski's arrow = unidirectional flux through the future horizon (entropic, dS/dt>0). The framework's arrow = the irreversible diabatic transit-freeze (R_therm=5252, S_ent→0, "the Ordered Veil") — entropy is produced and the transit does not reverse. Both are entropic/irreversible-flux arrows. But Popławski's is tied to a *global event horizon*; the framework's is tied to a *non-equilibrium quench*. Same flavor (irreversible flux), different substrate.

---

## 4. Penrose diagrams (§d)

ASCII conformal diagrams. Null rays at 45°. I label i⁺/i⁻/i⁰, ℐ⁺/ℐ⁻, horizons, singularities, and shade trapped/anti-trapped/frozen regions. (Canonical TikZ versions belong in `sessions/framework/Phononic-Penrose-Diagrams.md`; these ASCII sketches are the adversarial comparison.)

### 4.1 (i) Popławski UIBH with Einstein–Rosen bridge (1410.3881)

This is the maximally-extended Schwarzschild-like diagram with the *future-interior* singularity replaced by a torsion bounce that opens into a new closed FLRW universe. (Two-sided ER bridge; child = the bounced future interior.)

```
              i⁺(parent)              i⁺(parent')
                \                       /
                 \   ℐ⁺(parent)        /  ℐ⁺(parent')
                  \                   /
          PARENT   \                 /  PARENT'
         exterior   \   FUTURE      /   (other ER sheet)
          (our       \  INTERIOR   /
           cosmos)   i⁰----X======X----i⁰
                      \   //######\\   /      X===X  = future event horizon
                       \ //########\\ /              (ingoing; matter crosses IN only)
                        \/##########\/        ######  = future-trapped region (θ_out<0)
              ====•BOUNCE•============         •BOUNCE• = torsion bounce replaces singularity
                 // (ECSK torsion;  \\                    (NOT a spacelike sing.; spacelike
                //  Weyl C=0 here)   \\                    bounce hypersurface)
               //   CHILD FLRW        \\
              //    (closed, expanding) \\      CHILD universe = NEW region "on the
        i⁻---X========================X---i⁻    other side of the horizon" (ER bridge)
              \    ℐ⁻(parent)        /
               \                    /
                i⁻(parent)      i⁻(parent')
```
Global structure: the child universe is the **future interior** of the parent's black hole; its past boundary is the parent's **future** event horizon (the ER-bridge throat, "outermost trapped surface" asymptotically = the horizon). Matter flux is **unidirectional inward** across that horizon — this *is* the time arrow. The child's own future may itself host black holes → recursion. The bounce hypersurface is where torsion makes the effective NEC fail.

### 4.2 (ii) Gaztañaga BHU (FLRW-inside-Schwarzschild, Israel junction at R=[r_H² r_S]^{1/3})

Single future horizon; collapse → bounce → frozen expansion. No white hole, no maximal extension. The diagram is a *finite causal diamond* glued to a Schwarzschild exterior.

```
            i⁺                         schematic — single future event horizon r_S=r_Λ
             \                         FLRW interior (R<r_H, blue) embedded in SW exterior
       ℐ⁺     \                        glued at R=[r_H² r_S]^{1/3} (Israel, no surface terms)
               \
        SW       \   r_S = r_Λ  (FUTURE event horizon; "nothing comes out")
      exterior    \ ____________
      (empty,      X            \         X = future horizon (formed 25 Gyr ago by collapse)
       Birkhoff    |\\\\\\\\\\\\\ \
       → SW)       | \  FROZEN   \ \       \\\\\ = super-horizon FROZEN shell  r_H<r<R
                   |  \ (yellow)  \ \              (re-enters during expansion → "no inflation
        i⁰---------|---\__________\_\--- ...        needed"; seeds structure)
                   |    [ FLRW    ]  |
                   |    [ interior]  |       [FLRW interior], R<r_H, causal (blue)
                   |    [ R<r_H   ]  |       expansion FREEZES as a→1 (Λ boundary halts it)
                   |   •••BOUNCE•••  |       •BOUNCE• = neutron-degeneracy bounce (Pauli);
                   |   (mathematical |               replaces the t=0 math singularity
                   |    sing. at t=0 |
                   |    is bounced)  |
       ℐ⁻         /  \••••••••••••/  \
             \   /    \ COLLAPSE  /    \        COLLAPSE phase (H<0): dust free-falls
              \ /      \ (H<0)   /      \                       in, crosses r_S
            i⁻          \_______/        i⁰
```
Global structure: a **future** event horizon r_S=r_Λ (Gaztañaga's whole point — Λ *is* this horizon). The observable FLRW is a **finite causal diamond** inside r_H, itself inside r_S. The collapse (H<0) → bounce → expansion (H>0) all happen **inside** the future horizon. Λ-as-GHY-boundary lives on the time-like junction ∂V₄ at R=r_S. **No white hole, no past horizon, no Kruskal extension.**

### 4.3 (iii) Framework acoustic white hole — TWO honest versions

**(iii-a) As the S85 W6-1 theorem CLAIMED it (bracketed supersonic interior, one-directional disconnect):**
```
   POST-FOLD              SUPERSONIC            PRE-FOLD
   subsonic exterior      interior (Mach>1)     subsonic exterior
   (physical universe)    anti-trapped          (high-τ "primordial")
        |                  /##########\               |
        |   τ_H+ (sonic)  /############\  τ_H- (sonic) |
   .....|----X-----------/##############\-----------X--|.....   X = acoustic horizon (v=c_s)
        |    ^           |  v > c_s      |           ^  |        ###### = supersonic ergoregion
        |    |  ingoing  |  (frozen-in   |  ingoing  |  |
        |    |  null     |   flow)       |  null     |  |        ONE-DIRECTIONAL disconnect:
        |    |  STALLS   |               |  reaches  |  |        post-fold ℐ⁻ unreachable from
        |   τ_H+ from    |               |  pre-fold |  |        interior (Unruh-type WHITE hole)
        |   above        |               |           |  |
       τ=0.197         τ_fold=0.19     (interior)  τ_H-
```

**(iii-b) As the S95 W4-1 gate ACTUALLY found it (FAIL: single asymmetric crossing, open exit):**
```
   POST-FOLD                                   PRE-FOLD
   subsonic exterior      SUPERSONIC (monotone, OPEN)        ...continues supersonic...
        |                  /#######################################▶
        |   τ₀ (the ONLY  /   v > c_s   (monotone_supersonic_exit=True)
   .....|----X-----------/##########################################▶   NO second horizon.
        |    ^           |  κ₀ = −18.44 (negative)                       Exit never re-closes
        |    | one-      |  C1_structure = ASYMMETRIC_open_exit          to a subsonic exterior.
        |    | directional|                                             ⇒ interior is HALF-OPEN,
        |    | disconnect |  N_zeros = 1  (not a bracketed pair!)           not a sealed white-hole
        |   survives     |                                                  interior.
       τ=...           τ₀=0.1124
```

**(iii-c) Separately, the modulus-space extremal horizon (S85 W6-4, the κ=0 surface):**
```
      ds² = −V(τ)dt² + dτ²/V(τ),   V = V₀(τ − τ_dump)²    (Schwarzschild-LIKE in modulus time)

           t                       Σ_dump : τ = τ_dump = 0.19
           |                       DEGENERATE (extremal) horizon:
           |        //             κ = ½|V′| = 0,  T_H = κ/2π = 0
           |       //              double root V = V′ = 0  ⇒  marginally trapped
   --------+------//----------- τ   "thermodynamically null" — silent, zero-emission.
           |     // (degenerate    This is NOT the disconnector; it is the freeze-out marker
           |    //   null line)     (critical point of the spectral action, dS/dτ=0).
```

**The diagrammatic punchline (where they share structure, where the framework hand-waves):**
- **Shared global structure**: all three have a *region behind a one-way feature* and a *finite-density replacement of the singularity*. Gaztañaga's frozen-shell (yellow) and the framework's pre-fold "primordial" region play *analogous* roles (causally-disconnected reservoir that seeds/precedes the observable region).
- **Where the GR models are precise and the framework is not**: Gaztañaga's X and Popławski's X are **true event horizons** — global, two-sided, coordinate-independent, with exact junctions (Israel / ER throat). The framework's X in (iii-a) was an engineered *bracketed pair*; the *actual* kinematics (iii-b) give a **single asymmetric open crossing**. The framework's diagram (iii-a) that the catalog shows is **not what its own S95 computation produces**. That gap — between the drawn bracketed white-hole interior and the computed open asymmetric crossing — is the framework's hand-wave.
- **Orientation**: Gaztañaga/Popławski horizons are **future** (ingoing); the framework's is **past/white** (outgoing-blocked). Time-reverses.

---

## 5. FALSIFICATION subsection (mandate-critical)

### 5.1 Tensions and contradictions I FOUND

**F1 — [SHARPEST] The framework's own follow-up gate (S95) contradicts the clean white-hole interior its S85 theorem drew.**
S85 W6-1 (PROVEN) → bracketed pair of sonic horizons enclosing a sealed supersonic interior. S95-W4-1 (**FAIL**) → `N_zeros=1, C1_structure=ASYMMETRIC_open_exit, monotone_supersonic_exit=True`. There is only one sonic crossing and the exit is open. **The "sealed, causally-disconnected interior" is not supported by the framework's latest kinematics; only a one-directional Unruh-type disconnect survives.** This is internal to the framework and is the single most important finding of this analysis. It is also a place where the GR models (true two-sided event horizons) are **strictly more rigorous** than the framework about the causal cut.

**F2 — Orientation inversion (black vs white).** UIBH = future event horizon, ingoing, future-trapped, formed by collapse. Framework = white hole, outgoing-blocked, anti-trapped, formed by phase transition. These are **time-reverses**. Any claim that the framework "is a kind of universe-inside-a-black-hole" inverts the arrow. The honest statement: the framework is the *time-reverse* of the UIBH interior. (This also means the framework should NOT borrow Gaztañaga/Popławski's "we are inside a black hole" rhetoric — it is inside a *white* hole, which is the opposite causal object.)

**F3 — Λ-as-boundary vs Λ-as-bulk-moment is a genuine differential-geometric contradiction, and the GR side wins on predictivity.** Gaztañaga's Λ=3/r_S² is parameter-free and gets the coincidence problem for free; the framework's a₀=6440 is a *bare* bulk value whose route to 10⁻¹²² is not a closed numerical prediction (CC-QTHEORY-43 predicted FAIL). The S42 incursion's own attempt to bridge boundary↔bulk via GHY-as-P_ext gave the **wrong scaling**. **GR (Gaztañaga) exceeds the framework here.**

**F4 — The κ=0 extremal horizon is the WRONG object to hang causal disconnection on.** κ=0/T_H=0 ⇒ marginally trapped, degenerate, thermodynamically silent, zero-emission. If the framework's disconnection were attributed to the κ=0 modulus horizon, the claim would collapse (an extremal horizon is the weakest disconnector and emits nothing — odd for a "white hole" that is supposed to be the time-reverse of an absorber). The disconnection must rest on the *acoustic* (Mach≫1) horizons — which is precisely where F1 bites.

**F5 — The framework's white hole is "not a wall" by its own theorist; the GR horizons ARE walls.** Volovik (S42 §I.4): the acoustic horizon "is NOT a thermodynamic boundary; the superfluid continues beyond the horizon; the microscopic theory is the same on both sides; the horizon is an emergent feature, not a wall." Gaztañaga/Popławski horizons are genuine global causal boundaries. So the framework's "causal disconnection" is **emergent and observer/mode-dependent**, while the GR models' is **absolute**. The framework cannot claim the same *strength* of disconnection.

**F6 — Bounce vs quench: the framework lacks the contracting pre-phase the GR bounces have.** Popławski and Gaztañaga both have a genuine *contracting* FLRW phase (H<0) that bounces to H>0 — a temporal bounce in physical spacetime. The framework's "transit" is a *quench in modulus-time τ* (a first-order phase transition), and the physical universe does **not** have a pre-fold contracting phase in cosmic time t — the contraction is along τ, not t. So the framework's analog to a "bounce" is structurally a *quench*, and mapping it to a temporal bounce is a category slip the framework itself warns against (`phononic-framing.md`: "supersonic transit… not a torsion bounce, not a potential well"). I flag that the *prompt's* framing "phase-transition white hole, NOT a torsion bounce" is correct and the framework is internally consistent here — but it means the bounce↔transit correspondence is weaker than it looks.

### 5.2 Tensions I SEARCHED FOR and did NOT find (negative results — these strengthen the framework)

**N1 — I looked for a hard contradiction between the framework's Weyl-at-genesis and Popławski's Weyl=0, and did NOT find one.** Both put minimal/zero Weyl at the start and grow it. Popławski: FLRW ⇒ C=0 exactly. Framework: |C|²(0)=5/14 minimal, monotone-increasing (S96-GEOM-CCC-WEYL PASS, d|C|²/dτ>0). The only daylight is "exactly zero" (Popławski) vs "minimal but nonzero" (framework, Type O impossible by SU(3) structure constants). This is a **genuine shared structure** (Penrose Weyl-curvature hypothesis compliance), not a tension. Strength 6/10 — the strongest real correspondence in the comparison.

**N2 — I looked for a contradiction in the singularity-avoidance mechanism and found only a parallel.** All three avoid the t=0 (or τ→∞) curvature singularity by finite-density physics (torsion / neutron degeneracy / BCS quench). No contradiction; a real mechanism-level parallel. I did NOT find that the framework's avoidance is *less* rigorous — the framework's DNP-instability/NEC-boundary (τ_NEC=1.382) is as well-defined as torsion's effective-NEC violation. (Note: the framework's 12D singularity censor, MEMORY.md, shows K12~e^{4τ}→∞ at τ→∞ is *censored* behind the τ=0.19 barrier — structurally analogous to cosmic censorship hiding the GR singularity behind the horizon. This is a *match*, not a tension.)

**N3 — I checked whether Gaztañaga's frame-duality (FLRW↔Schwarzschild) secretly introduces a white hole or a maximal extension that would match the framework. It does NOT.** It is a Lorentz-contraction relabeling of a single causal diamond; no past horizon appears. So the framework cannot claim Gaztañaga as a black-hole *and* white-hole structure. (This rules out a cheap "they're secretly the same" reconciliation.)

**N4 — I checked whether the framework's recursion (child-in-parent, S42) could match Popławski's ER-bridge recursion closely enough to be "the same multiverse." It does NOT cleanly.** The S42 incursion's *own* verdict is that the recursive fixed point gives Λ*=0 (the BH embedding adds no new CC mechanism), and the "faucet" correction is ~10⁻¹⁹ negligible. So while both have recursion, the framework's recursion is *decorative* for the CC (Volovik/Hawking: "adds nothing"), whereas Popławski's recursion is *load-bearing* (it is his multiverse + arrow-of-time + information-paradox resolution). This is a place where Popławski's construction is *more structurally committed* — but not a contradiction, since the framework explicitly declines the recursion as a CC mechanism.

### 5.3 Where the framework EXCEEDS the GR literature (for balance)

**E1 — The framework derives its causal structure from a spectral triple with zero geometric free parameters; the GR models posit theirs.** Gaztañaga posits "we are inside our own r_S"; Popławski posits ECSK torsion. The framework's acoustic metric *emerges* from D_K eigenvalues via the a₂ Seeley–DeWitt coefficient (c_s set by spectral stiffness d²S/dτ²). The framework's causal structure is *derived*, the GR models' is *assumed* — even if the framework's derived structure (F1) is then weaker than claimed.

**E2 — The framework has a microscopic theory through the horizon; the GR models do not.** Volovik's point (which is a *strength* here): the framework knows what happens "beyond" the acoustic horizon (the substrate continues, BCS Hamiltonian on both sides). Gaztañaga/Popławski must posit quantum-gravity / torsion physics at the bounce that they cannot compute from first principles (Gaztañaga: "cold nuclear matter at neutron density is a major unsolved problem"; Popławski: spin-fluid approximation). The framework's bounce-analog (BCS quench) is *computed* (59.8 GGE pairs, S_ent=0, P_exc=1.000).

**E3 — The framework's "horizon is not a wall" is arguably more physical.** Real event horizons being absolute one-way membranes leads to the information paradox. The framework's emergent, non-wall acoustic horizon (and S_ent=0 product state) sidesteps it structurally (S42 §II.12-14: no entanglement across the transit ⇒ no monogamy violation ⇒ no firewall). This is a *conceptual* advantage, though it is the same property (F5) that *weakens* the causal-disconnection claim. The framework can have absolute-disconnection OR no-information-paradox, not both — and it has chosen the latter.

### 5.4 Net falsification verdict

The framework's cosmogenesis is **NOT falsified** by this corpus, but **one of its causal claims is materially overstated and one GR competitor is more predictive about Λ**:
- The "pre/post causally disconnected by supersonic flow" claim survives only in the **weak, one-directional, emergent** sense (F1, F5). The strong "sealed white-hole interior" reading is contradicted by the framework's own S95 FAIL. **Recommend the framework down-tag "causal disconnection" to "one-directional Unruh-type acoustic disconnection (single asymmetric crossing per S95; NOT a sealed interior)"** in the capstone and `phononic-framing.md` LCDM-translation table.
- Λ-as-bulk-moment is more fundamental but **less predictive** than Gaztañaga's Λ-as-boundary (F3, E1). The framework should stop implying its CC story is more complete than the GR-side; on the *number*, it is not (yet).
- The orientation is **white**, not black (F2) — the framework should not borrow UIBH "inside a black hole" language.
- The genuine, defensible correspondences are **Weyl-at-genesis** (N1, 6/10) and **singularity-avoidance/censorship** (N2, 6/10), not the causal-disconnection or the Λ identifications.

---

## 6. Correspondence strength table (my ratings, with reasons)

| # | Claimed correspondence | Strength /10 | Reason |
|:--|:--|:--:|:--|
| C-a | UIBH interior ≈ framework cosmogenesis (same causal structure) | **2** | Orientation opposite (future-black vs past-white); they are time-reverses, not the same. |
| C-b | Λ-as-GHY-boundary ≈ Λ-as-a₀-bulk-moment | **1.5** | Different codimension; S42 bridge gives wrong scaling; GR more predictive. |
| C-c | Torsion bounce ≈ supersonic phase-transition white hole | **3** | Singularity-avoidance parallel real; causal structures different in kind + orientation. |
| C-d1 | UIBH event horizon ≈ framework acoustic horizon | **3** | Both one-way features, but GR=absolute global wall, framework=emergent non-wall, single asymmetric crossing (S95). |
| C-d2 | UIBH event horizon ≈ framework κ=0 modulus horizon | **2** | κ=0 is extremal/marginal/silent — wrong object for disconnection. |
| **C-W** | **Weyl-curvature hypothesis: low/zero Weyl at genesis, grows** | **6** | Popławski FLRW C=0; framework WCH-min |C|²=5/14 monotone-increasing. **Strongest real match.** |
| C-S | Singularity avoided + censored behind a one-way feature | **6** | All three; framework 12D censor ≈ cosmic censorship. Real structural parallel. |
| C-T | One-directional entropic time arrow | **4** | Both irreversible-flux; GR tied to event horizon, framework to quench. |
| C-R | Recursive child-in-parent multiverse | **3** | Both have recursion; framework's is decorative for CC (S42), Popławski's load-bearing. |

---

## 7. Carry-forwards (4-field, for the synthesis/`/rclab-plan`)

**CF-A1-1 — Re-examine the W6-1 acoustic-white-hole theorem against the S95 FAIL.**
- *What*: Reconcile S85 W6-1 (bracketed pair, PROVEN) with S95-W4-1 (single asymmetric open exit, FAIL). Determine whether the W6-1 tanh² c_s(τ) profile is physically justified or was an artifact that manufactured the second horizon. Re-derive c_s(τ) from the actual a₂(τ) spectral stiffness and count zeros of v−c_s.
- *Inputs*: S85 W6-1 script `s85_w6_acoustic_white_hole_formal.py`; S95 `s95_w4_1_white_hole_kinematic_consistency.py`; c_s(τ) from a₂(τ) Seeley–DeWitt.
- *Gate*: PASS iff N_zeros and disconnect-direction are consistent across both scripts under the *same* c_s(τ); pre-register N_zeros∈{1,2} criterion. If N_zeros=1 confirmed, the white-hole "sealed interior" claim is down-tagged (capstone + phononic-framing.md).
- *Effort*: 1 compute gate (sp + transit-dynamics).

**CF-A1-2 — Down-tag "causal disconnection" language in the capstone + phononic-framing.md.**
- *What*: Change the LCDM-translation entry "Horizon problem solved by acoustic white hole" to specify *one-directional Unruh-type* disconnection (single asymmetric crossing), not a sealed interior. Reconcile with the S85 wrap-up's own "overstated the disconnect direction" lesson.
- *Inputs*: `phononic-framing.md` LCDM table; capstone §6/§7; S85 W6 wrap-up §"W6-1 plan text overstated"; S95 verdict.
- *Gate*: capstone-hygiene Q3 (status change) + Q4 (prose claim). Designated writer patch.
- *Effort*: in-session prose fix (orchestrator-direct, no compute).

**CF-A1-3 — Formalize the Weyl-curvature-hypothesis correspondence (the one strong match).**
- *What*: Register the Popławski-FLRW-C=0 ↔ framework-WCH-|C|²=5/14-monotone correspondence as a cross-framework structural parallel (GEOMETRIC class). Note the "exactly zero vs minimal-nonzero" distinction (Type O impossible by SU(3) structure constants).
- *Inputs*: Popławski 1410.3881 §"FLRW Weyl vanishes"; S96-GEOM-CCC-WEYL; MEMORY.md WCH entries.
- *Gate*: structural-theorem registration (not a numerical gate); cross-pillar-bridge-anatomy 5-anatomy if it rises to a bridge.
- *Effort*: 1 registry landing (sp + connes).

---

## 8. Provenance / verification

- File written to `sessions/bh-cosmo-incursion/subs/sub-A1-causal-structure.md` (verified on disk, §below).
- All paper claims sourced from the fetched PDFs/HTML (read_arxiv_paper), not training knowledge, per `feedback_research-corpus.md`. Gaztañaga 2202.00641 read in full; 2204.11608 + 1410.3881 extracted via python on saved reader output; 2405.16673 read in full.
- Framework anchors sourced from knowledge MCP + on-disk session files (S42 incursion, S85 W6 WP, S95 verdict file, S96 gate).
- Constants verified via `get_constant`: tau_fold=0.19, Mach_max=13.75, v_term=26.545, w0_FW=−0.918, a₀^ζ=6440.
- **Adversarial-mandate compliance**: §5 contains explicit tensions (F1–F6), explicit not-found tensions (N1–N4), and explicit framework-exceeding findings (E1–E3). Every correspondence in §6 carries a numerical strength rating with reason. The sharpest tension (F1) is internal-to-framework and is reported against my own prior authorship (S85 W6-4).
