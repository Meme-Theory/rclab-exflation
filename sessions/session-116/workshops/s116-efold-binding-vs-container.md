# Session 116 Workshop: volovik × mack

**Date**: 2026-06-28
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: volovik (volovik-superfluid-universe-theorist), mack (mack-cosmic-bridge)
**Source Documents**:
- sessions/session-116/workshops/s116-w6-bc-fork.md
- sessions/session-116/session-116-w6-workingpaper.md
- computations/session-116/s116_gate_verdicts.txt

**Upstream verdict to fold in**: S-4 (ATFORM-transfer solo) landed **Wave-6 = HH-UNCONDITIONAL** (the BC-layer residual CF-S117-Q45 is MOOTED). So the BC-layer e-fold residual `N_e_BC=0.1734` is closed; if an e-fold gap is a real liability, it lives at the ACOUSTIC layer (`N_e_acoustic≈2.92`).

**Focus Topics** (adjudication: is `N_e ≥ 3.1` a substrate-binding requirement on EXFLATION, or a container-thinking inflation yardstick the acoustic white hole supersedes? Wave-6 tests `N_e_BC` against `N_E_THRESHOLD=3.1` and reports `gap_to_3.1=2.9266` routed "to TRANSIT-PS-67 regardless"; neither agent questioned whether exflation NEEDS 3.1 e-folds):
1. (a) Does the acoustic white hole solve the HORIZON problem WITHOUT an e-fold count — and does that argument extend to FLATNESS (`Ω_k→0`), or is flatness a separate, still-e-fold-shaped requirement? (The workshop's 3.1 CONFLATES horizon and flatness — decompose them.)
2. (b) Is `N_e` a substrate-IS observable or a container import under `phononic-framing.md §"IS Space, Not IN Space"`?
3. (c) VERDICT: is `gap_to_3.1=2.9266` a REAL liability (→ TRANSIT-PS-67 must supply ≥3.1; gap unclosed at BOTH the BC layer 0.1734 AND the acoustic layer 2.92) or a DISSOLVED category error (→ retire the 3.1 target as inflation-imported; mint a `phononic-framing.md` IS-not-IN calibration entry)?

NOTE: the W4 modulus e-fold `N ∝ (1+δ)` uncertainty (δ open, `CF-S117-MODULUS-A4-GRADIENT`) is a SEPARATE mechanism from the WDW-BC/acoustic `N_e` — do NOT conflate.

---

## Round 1 — volovik: Opening Analysis

### V1: (a) Horizon vs flatness — does the acoustic white hole need an e-fold count?

**Key finding.** The horizon problem is solved in exflation by the acoustic white hole — a *kinematic* causal disconnection set by the Mach condition `|v|=c`, with NO expansion factor anywhere in the mechanism (PROVEN S85; Volovik `09_2005` hydraulic-jump white hole, `27_2003` Painlevé-Gullstrand 3He-A). Flatness is also not e-fold-shaped, but by a *different* route: the substrate carries no pre-geometric spatial-curvature degree of freedom for e-folds to dilute. When the two are decomposed, NEITHER lands on an e-fold count — and the workshop's `N_e ≥ 3.1` silently conflates them into a single inflation-internal number.

**The root — the transit is a global-modulus event, not a spatial process.** Inflation's horizon problem exists because the pre-inflationary universe is a *spatial* configuration: `O(1)` patches across the sky are causally disconnected, and the ~60 e-folds exist to have brought them into causal contact BEFORE stretching them apart. The substrate's pre-transit state is not a spatial configuration at all — it is the undeformed round SU(3) fiber at the single global Jensen modulus `τ=0`. inv11's WDW operator is built on exactly this: Ψ(τ) is a *minisuperspace* wavefunction over ONE global `τ` (`session-116-w6-workingpaper.md`: "Ψ(τ) is the substrate's OWN amplitude over its OWN Jensen-deformation moduli `{(A_K,H_K,D_K(τ)):τ}`"), not a field `τ(x)` with spatial gradients.

```
Substitution chain — why the CMB is uniform (substrate-IS, no e-folds):
  Step 1: pre-transit state = (M4 × SU(3))|_{τ=0}, the SAME round fiber over every M4 point
          (single global modulus, inv11 minisuperspace).
  Step 2: transit = τ: 0 → τ_fold=0.19, a GLOBAL modulus evolution (one τ for the whole
          substrate), NOT a spatially-propagating front.
  Step 3: ⇒ the post-transit fiber configuration is identical over every emergent-space point
          BY CONSTRUCTION (inherited homogeneity); there is no "bring patches into contact" step.
  Read-off: observed CMB uniformity is INHERITED from the substrate's global-modulus homogeneity,
            not MANUFACTURED by e-folds. The job 60 e-folds do in inflation (smooth a pre-existing
            spatial inhomogeneity) has no referent here — there is no spatial inhomogeneity to smooth.
```

**What the acoustic white hole then does — the causal-SEALING question, also e-fold-free.** There is a *separate*, genuine causal question: why are pre-fold (trans-Planckian, `τ<τ_fold`) and post-fold (observable) physics causally SEALED, so the round-SU(3) "before" does not leak into the post-fold light cone? This is the acoustic-white-hole question, PROVEN at S85: "acoustic white hole causal-disconnect FORMALIZED — single-asymmetric-open / one-directional (white-hole/Unruh) disconnect" (`Phononic-framework-hypothesis.md`). The mechanism is Volovik's: in the hydraulic-jump white hole (`09_2005`) the interior flows radially OUTWARD with `v>c`, and relativistic ripplons "cannot propagate into the interior region" — the horizon at the Mach surface `|v|=c` seals interior from exterior. The PG 3He-A construction (`27_2003`) puts the horizon at `|v(r_h)|=c` with `T_H = ħ|v'(r_h)|/2π` (Eq.12).

```
Substitution chain — the horizon condition carries no N:
  Def 1: white-hole horizon condition (Volovik 09/27): |v(r_h)| = c  (the Mach-1 surface of the
         substrate's OWN flow — ACOUSTIC, not a GR metric horizon).
  Def 2: substrate transit Mach number = 13.75 ≫ 1 (constraint-mega-matrix; tau_fold=0.190)
         ⇒ supersonic ⇒ the sealing surface EXISTS.
  Def 3: Hawking/sealing strength = |v'(r_h)| (the flow GRADIENT at the Mach surface; Volovik Eq.12).
  Read-off: the causal-sealing condition is set by (v/c) and its gradient — the MACH NUMBER and the
            fold SHARPNESS. The e-fold count N = ∫H dt appears in NEITHER |v|=c NOR |v'(r_h)|.
            The horizon solution is N-independent BY CONSTRUCTION.
```

This is not analogy but a controlled realization in the *same universality class*: Rolley–Guthmann–Pettersen–Chevallier observed the stationary critical ripplon inside the 4He hydraulic-jump white-hole interior (`09_2005`). Causal sealing of a horizon WITHOUT any expansion factor is an experimental fact — a superfluid does not "inflate" to seal its white-hole interior; it flows supersonically.

**Flatness — the harder half, decomposed honestly.** I will not pretend flatness is as cleanly disposed of as horizon. In inflation flatness IS e-fold-shaped: `Ω_k − 1 = k/(aH)²`, and exponential growth of `aH` drives `|Ω_k−1| → 0`, needing ~60 e-folds from a generic `O(1)` start. The question is whether the substrate carries the *thing* that equation dilutes — a free spatial-curvature datum `k`. It does not, on the same global-modulus ground: the emergent 3-geometry is generated by the `a_2` Seeley-DeWitt coefficient of the spectral action (`phononic-framing.md`: "the 4D metric g_M emerges from the a_2 Seeley-DeWitt coefficient"), and its spatial sections inherit the substrate's global-modulus homogeneity. There is no pre-geometric Cauchy surface carrying an adjustable `k` to be ironed out — `k` is not an initial datum, it is whatever the `a_2` geometry produces. So flatness is not "a few e-folds short"; the e-fold-dilution mechanism is *inapplicable* — it dilutes a degree of freedom the substrate does not carry.

But here is my honest concession to mack: this RELOCATES flatness rather than trivially dissolving it. The substrate-native flatness question is *"does the `a_2` emergent geometry come out spatially flat (`k=0`) by construction?"* — a spectral-geometry computation, genuinely open, worth a gate. It is categorically NOT *"did `N_e` reach 3.1?"*. So flatness exits the e-fold axis too, but it lands on `a_2`-emergent-geometry, not on a vanishing gap. **The decomposition the workshop's 3.1 suppressed: horizon → acoustic white hole (Mach, PROVEN S85); flatness → `a_2` emergent-geometry (open, spectral); neither → e-folds.**

### V2: (b) Is N_e a substrate-IS observable or a container import?

**Key finding.** The answer is layered, and the layering IS Reading B. `N_e^geom = ln(a_f/a_i) = 0.1734` is a Layer-3 container observable (the log of the EMERGENT FRW scale factor on `g_M`). `N_e^acoustic = ∫ H_acoustic dt = 2.8913` is genuinely substrate-IS (built from the Volovik two-fluid variables `ρ(τ), c_s(τ)`). But the THRESHOLD `3.1` is a pure container import — defined on the inflationary FRW container, not derivable from the substrate. The category error is NOT in `N_e^acoustic`; it is in the COMPARISON `N_e^acoustic ≥ 3.1`, which lays an inflation ruler against a substrate-IS quantity.

**The three objects, separated under `phononic-framing.md §"IS Space, Not IN Space"`.**

*(1) `N_e^geom = 0.1734` — the most container-like.* This is `ln(a_final/a_initial)`, the logarithm of the emergent metric scale factor. Under the IS-not-IN mandate `a(t)` is NOT fundamental: it is the emergent description of how spectral weight redistributes (`phononic-framing.md`: "Space is an emergent description of how the fabric's spectral weight distributes itself"; table row "Space expands → Spectral complexity grows inside each point — the eigenvalue spectrum reorganizes"). `N_e^geom` is a Layer-3 *measured-on-`g_M`* diagnostic. It is the right number to compare against inflation ONLY IF the substrate's cosmogenesis IS metric stretching — which `phononic-framing.md` forbids by name.

*(2) `N_e^acoustic = 2.8913` — genuinely substrate-IS; I concede this openly.* It is NOT a container import. S53 Eq.15B (machine-ε exact, Sage-confirmed) decomposes it:

```
  N_e^acoustic = N_e^geom + ½ ln(ρ_f/ρ_i) − ½ ln(c_sf/c_si)     [S53 Eq.15B]
               = 0.1734    + [substrate density rise]  − [substrate sound-speed change]
               = 2.8913    (enhancement 2.8913 / 0.1734 = 16.7× over the bare geom count)
```

Every term beyond `N_e^geom` is built from `ρ(τ)` (superfluid number density) and `c_s(τ)` (acoustic speed) evolving along the transit — exactly the two hydrodynamic variables of Volovik's Landau-Khalatnikov two-fluid model (`01_2001` §II: "two hydrodynamic variables: particle number density `n(r,t)` and superfluid velocity `v_s`"; the acoustic-metric conformal factor is `mn/c`, Eq.13). `N_e^acoustic` is the log-growth of that conformal factor — a substrate-IS, Level-2 moduli-deformation quantity. So the substrate DOES carry a legitimate, microscopically-grounded expansion observable. Reading B does not deny this — denying it would itself be a framing error (treating the substrate's own hydrodynamic growth as illegitimate because it doesn't look like metric stretching).

*(3) The threshold `3.1` — pure container import.* `N_E_THRESHOLD = 3.1` is the plan's "external cosmological horizon/flatness requirement at K_pivot" (`session-116-w6-workingpaper.md` Def 6, tagged `# (local)`, "external horizon/flatness target"). It is a reduced image of inflation's ~50–60 e-fold budget — the e-fold count inflation needs to solve horizon+flatness+scale on the FRW container, carried over to the substrate's compressed transit timeline. It is NOT computed from `D_K`, `ρ(τ)`, `c_s(τ)`, or any substrate datum. Under `substrate-first-canonical-sourcing.md §(i)`, a number that REPLACES a substrate computation with an external-framework target is precisely a CANONICAL external-paper citation — forbidden as a binding pin (admissible only as a methodological cross-check).

**Substitution chain — isolating the category error:**

```
  Substrate-IS content:  "the acoustic conformal factor mn/c grows by e^{2.8913} across the transit
                          (S53; from ρ(τ), c_s(τ))."                        ← Layer-2 substrate-IS, TRUE.
  Container import:       "...and this must EXCEED e^{3.1} to solve horizon/flatness."
                                                                            ← Layer-3 inflation target, IMPORTED.
  Comparison gate:        N_e^acoustic ≥ 3.1  ⇒  2.8913 ≥ 3.1  ⇒  FAIL by 0.2087.
  Read-off: the FAIL pits a substrate-IS quantity (2.8913, real) against a container yardstick
            (3.1, imported). The substrate did not fail to PRODUCE something — it produced 2.8913;
            an inflation ruler was laid against it. The "gap" is the offset between a substrate
            observable and a container target — a category mismatch, not a substrate deficit.
```

So `N_e` is BOTH: the substrate HAS an expansion observable (`N_e^acoustic` — do not demote it) AND the gate carries a container-import threshold (`3.1` — do not bind to it). The IS-not-IN mandate is satisfied by KEEPING `N_e^acoustic` as the substrate observable and RETIRING `3.1` as the gate — not by denying that the substrate's acoustic conformal factor grows.

### V3: (c) The container-import reading (Reading B) — 3.1 is an inflation yardstick exflation does not inherit

**Key finding.** `3.1` (the reduced image of inflation's ~60 e-folds) bundles THREE distinct inflation jobs — horizon, flatness, and stretch-fluctuations-across-the-horizon. Exflation discharges each by a different, substrate-native mechanism, NONE of which counts e-folds. The bundle therefore does not transfer: `gap_to_3.1` is a DISSOLVED category error on the e-fold framing. The one genuinely non-vacuous piece inside the bundle — the power spectrum must span the observed k-range — RELOCATES to TRANSIT-PS-67 as a spectral-bandwidth requirement, not an e-fold count.

**Unbundling the 60-(→3.1)-e-fold yardstick.** Inflation's e-fold budget is a single number doing three jobs:

| Inflation job | Inflation mechanism (needs N_e) | Exflation mechanism (no N_e) | Status |
|:--|:--|:--|:--|
| Horizon (sky uniform across disconnected patches) | stretch one causal patch past the horizon | inherited global-modulus homogeneity + acoustic white-hole sealing (Mach 13.75) | PROVEN S85 |
| Flatness (`Ω_k→0`) | dilute pre-existing `k` by `e^{−2N}` | no pre-geometric `k`; `a_2` emergent geometry | open (spectral), NOT e-fold |
| Scale-range (broadband near-scale-invariant `P(k)`) | stretch sub-horizon quantum modes to CMB scales over ~10 e-folds | GGE acoustic spectrum supplies the k-range directly (TRANSIT-PS-67) | CRITICAL gate, substrate-native |

Each row replaces "e-folds" with a substrate mechanism. The third row is load-bearing for observation: in inflation the OBSERVED CMB power spectrum is quantum modes stretched across the horizon, so `N_e` must be large enough to cover the observed k-decades. In exflation the CMB is NOT stretched vacuum modes — it is "the acoustic signature of the GGE relic" (`phononic-framing.md`), "the interference pattern of post-transit GGE acoustic excitations." The observed k-range is supplied by the Bogoliubov spectrum through the fold — precisely what TRANSIT-PS-67 computes (`baseline-findings-s66`: "Full Bogoliubov power spectrum through fold"; PASS: `α_s(k_CMB) < 0.015`).

```
Substitution chain — why the scale-range job needs no e-fold count:
  Def 1 (inflation): observed P(k) over k ∈ [k_min, k_max] = vacuum modes that exited the horizon
         between e-fold N(k_max) and N(k_min) ⇒ need ΔN ≳ ln(k_max/k_min) ≈ the observed k-decades.
  Def 2 (exflation): observed P(k) = |β(k)|² Bogoliubov occupation of GGE acoustic modes produced
         AT the fold (TRANSIT-PS-67), with k-dependence set by the fold's Mach number and sharpness,
         NOT by horizon-exit timing.
  Step 3: the GGE spectrum's bandwidth is a property of the SUDDEN transit kinematics (S70: WKB
         inapplicable, sudden approximation mandatory) — β(k) is nonzero over the band the impulsive
         fold excites, INDEPENDENT of any ∫H dt.
  Read-off: the k-range is delivered by β(k) bandwidth, not by an e-fold count. "N_e ≥ 3.1" is
            inflation's ENCODING of the scale-range job; exflation's encoding is "TRANSIT-PS-67 spans
            the observed k-decades." Same observational target, different — and non-fungible — variable.
```

**Verdict on `gap_to_3.1`.** The BC-layer gap `2.9266` is already mooted (S-4 ATFORM solo: Wave-6 HH-UNCONDITIONAL ⇒ `N_e_BC=0.1734` is the settled BC value, and the BC layer was never where the count lives — it routes to TRANSIT-PS-67). The acoustic-layer gap is `3.1 − 2.8913 = 0.2087` (≈ 6.7%). My Reading-B verdict: NEITHER gap is a "real liability" in the e-fold sense, because `3.1` is not a substrate-binding target. A 6.7%-short comparison against the WRONG yardstick is still the wrong yardstick — the smallness of `0.21` is not evidence the substrate "almost made it," it is a coincidence of the scaling that produced `3.1`. **The gap DISSOLVES as a horizon/flatness liability.**

**What I do NOT dissolve — the honest residual, and the convergence seed for mack.** One piece of the bundle is real and survives: the OBSERVED universe's power spectrum spans a definite, finite range of comoving scales (the several decades in `k` that Planck CMB + DESI/LSS cover), and SOMETHING must produce a spectrum that broad with the right tilt. That requirement does not vanish — but it is NOT "`N_e ≥ 3.1`". It is a BANDWIDTH requirement on TRANSIT-PS-67's GGE acoustic spectrum, and TRANSIT-PS-67 is ALREADY the framework's gate for it (`α_s, A_s, n_s(k)`; CRITICAL). So even the real core relocates onto an existing substrate-native gate; it does not survive AS an e-fold count.

Reading B's verdict is therefore not "there is no observational obligation" — it is: **retire `3.1` as a substrate-binding e-fold gate; route its one real obligation (scale-range) to TRANSIT-PS-67, its horizon obligation to the acoustic white hole (PROVEN S85), and its flatness obligation to `a_2` emergent-geometry. None of the three is `N_e`.**

**Recommendation.** Mint a `phononic-framing.md` IS-not-IN calibration entry: *"`N_e ≥ 3.1` (e-fold count) is a container import; the substrate discharges horizon / flatness / scale-range by acoustic-white-hole sealing / `a_2`-emergent-geometry / TRANSIT-PS-67 bandwidth respectively — `N_e` is a Layer-3 translation diagnostic, never a substrate-binding gate."* Retire `N_E_THRESHOLD=3.1` from the gate ledger; keep `N_e^acoustic=2.8913` as a substrate-IS observable with NO inflation threshold attached.

### V4: Cross-Cutting Observations

**1. Pre-empting mack's strongest Reading-A move (observational viability).** mack's best case is not "the substrate must literally inflate" — it is: the OBSERVED universe is (i) causally coherent across the sky, (ii) spatially flat to `Ω_k ≈ 0` (Planck `|Ω_k| ≲ few×10⁻³`), (iii) carries a near-scale-invariant broadband `P(k)`. These are binding FACTS regardless of mechanism, and SOMETHING in the substrate must deliver each. I concede the facts are binding. Reading B is precisely that the SUBSTRATE-NATIVE ENCODING of these three facts is NOT a single e-fold number — it is three separate substrate gates (acoustic white hole / `a_2` geometry / TRANSIT-PS-67). The disagreement left for R2 is narrow: mack will want to KEEP `3.1` as a convenient translated cross-check ("if the substrate mechanisms work, they should ADD UP to ≳3.1 e-folds of effective expansion"); I argue keeping the number invites exactly the category error the workshop just exhibited — testing `N_e^acoustic ≥ 3.1` and reading the `0.21` shortfall as a substrate liability rather than a ruler mismatch.

**2. The vacuum-energy-test consistency check (standing methodology).** The SAME microscopic structure that nullifies the CC also supplies the expansion observable — not a coincidence, and it constrains the reading. Volovik `01_2001` §II.G: the two-fluid hydrodynamics `(ρ, v_s)` gives `ε_vac(equilibrium) = −P_vac = 0` for the self-sustaining vacuum (the substrate's CC-nullification, inherited by the framework's q-theory path). The acoustic metric (Eq.13, conformal factor `mn/c`) comes from the SAME `(ρ, c_s)` variables. So `N_e^acoustic` (log-growth of `mn/c`) and the CC-nullification are two readings of ONE two-fluid structure. A framework whose vacuum energy is microscopically computable (and zero in equilibrium) does not separately OWE an "e-fold count" as a fundamental input — the expansion observable is a DERIVED diagnostic of the two-fluid transit, the same transit whose equilibrium endpoint nullifies Λ. Importing an external `3.1` as a binding requirement treats a derived diagnostic as if it were an independent fundamental knob — the inverse of the substrate-first direction.

**3. Laboratory grounding (the test my methodology always applies).** The horizon solution is not merely modeled — it is realized in a controlled superfluid. Rolley–Guthmann–Pettersen–Chevallier (`09_2005`) observed the white-hole interior of the 4He circular hydraulic jump with the stationary critical ripplon (Miles instability) inside the ergoregion; Volovik's 3He-A PG construction (`27_2003`) gives the cleaner horizon, `T_H = ħ|v'(r_h)|/2π`. In NONE of these does causal disconnection involve an expansion factor — the horizon is sealed by `|v|>c`. If a benchtop superfluid seals a horizon with zero e-folds, then an e-fold count is demonstrably NOT a necessary condition for horizon-sealing in this universality class. This is the laboratory face of the V1 claim, and the hardest single point for Reading A to absorb: the substrate is in the same universality class as a system where the horizon-problem analog is solved WITHOUT inflation.

**4. Scope boundary (what I am NOT claiming).** I am not claiming the substrate's cosmology is observationally complete. TRANSIT-PS-67 is a CRITICAL OPEN gate (the Bogoliubov spectrum must actually deliver the observed `α_s, A_s, n_s` across the k-range — real, unfinished work). `a_2`-emergent-flatness is an open spectral computation. I claim ONLY that the e-fold count `N_e ≥ 3.1` is the wrong instrument for ALL of these — a container ruler whose three obligations relocate to three substrate gates. Retiring `3.1` does not weaken the framework's observational obligations; it routes them to the gates that can actually compute them.

**Questions for mack:**

- **Q-V1 (name the spatial degree of freedom).** Inflation needs ~60 e-folds because the pre-inflationary universe is a SPATIAL configuration with `O(1)` curvature and causally-disconnected patches. The substrate's pre-transit state is ONE global Jensen modulus `τ=0` (inv11 minisuperspace — a single `τ`, not a field `τ(x)`). Name the SPATIAL inhomogeneity or curvature degree of freedom in the substrate that `3.1` e-folds would be needed to iron out. If the modulus is global (no spatial d.o.f.), what spatial problem is `3.1` solving?

- **Q-V2 (what does 3.1 constrain that TRANSIT-PS-67 doesn't?).** TRANSIT-PS-67 is already the gate for `α_s, A_s, n_s(k)` across the observed k-range (PASS: `α_s < 0.015`). Exhibit an OBSERVABLE that `N_e ≥ 3.1` constrains but TRANSIT-PS-67's spectral bandwidth does not. If there is none, `3.1` is redundant against an existing substrate gate; if there is one, name it and we have a genuine binding requirement to localize.

- **Q-V3 (is N necessary, or only inflation-sufficient?).** A controlled superfluid (Rolley et al. 4He hydraulic jump; 3He-A PG black hole) seals a horizon with ZERO expansion factor (`|v|>c`; Volovik `09`/`27`). On what grounds is an e-fold count a NECESSARY condition for the substrate's horizon solution, rather than merely the SUFFICIENT condition inflation happens to use? If a lab system in the same universality class does it without e-folds, the necessity claim needs an independent argument.

---

## Round 1 — mack: Response & Cross-Synthesis

### Part 1: Response to volovik's Sections

#### Re: V1 — horizon vs flatness

**AGREE on horizon — with one observational caveat.** V1's decomposition is the cleanest move in the opening, and I accept it on horizon. The pre-transit state is ONE global Jensen modulus τ=0 (inv11 minisuperspace), not a field τ(x) with spatial gradients, so post-transit homogeneity is inherited by construction — there is no "bring causally-disconnected patches into contact" job, and the e-fold count ∫H dt enters neither the Mach sealing condition |v|=c nor the gradient |v'(r_h)|. The horizon FACT — CMB uniform to ΔT/T ~ 10⁻⁵ across the full sky (Planck) — is met by inherited homogeneity + acoustic sealing, not by stretching. This is substrate dynamics (the supersonic Mach-13.75 transit is c-uncoupled — not a c-bounded propagation). The caveat I must enter as the observational voice: *inherited homogeneity is an initial-condition POSIT, not a dynamical generation.* It is the substrate's exact analog of inflation's most-criticized assumption — the smooth starting patch (Penrose's phase-space-measure argument; Ijjas–Steinhardt–Loeb). The substrate's version is structurally CHEAPER (a single global modulus carries no spatial d.o.f. to be inhomogeneous, so there is strictly less to assume), but it is the same epistemic move: assumed, not derived. Horizon is e-fold-free; it is not assumption-free.

**DISAGREE on flatness — the relocation is an IOU resting on a conflation.** V1 concedes flatness "RELOCATES rather than trivially dissolves" and routes it to "does the a_2 emergent geometry come out flat (k=0) by construction." Two problems. (1) An open computation is not a discharge (developed in M1). (2) The relocation leans on a conflation: V1 says the emergent spatial sections "inherit the substrate's global-modulus homogeneity," as if homogeneity supplies flatness. It does not. **Homogeneity ≠ flatness.** A homogeneous FRW 3-geometry can be a 3-sphere (k=+1) or hyperbolic (k=−1) — both maximally symmetric, both homogeneous, neither flat. The spatial-curvature datum k ∈ {−1,0,+1} survives homogeneity as a SEPARATE invariant. So inheriting homogeneity from the global modulus gives V1 NO head start on k=0; the a_2 geometry must select k=0 *specifically*, over k=±1, and homogeneity is silent on which.

```
Substitution chain — why 3.1 is the wrong flatness instrument either way (Sage-verified):
  Def 1: flatness measure  |Ω_k − 1| ∝ (aH)^{-2}                        [FRW constraint].
  Def 2: during an accelerating phase a∝e^N (H≈const) ⇒ (aH)^{-2} ∝ e^{-2N}
         ⇒ N e-folds suppress |Ω_k−1| by e^{-2N}.
  Step 3 (substrate acoustic budget N_e_acoustic=2.8913): e^{-2·2.8913} = 3.08×10^{-3}  (−2.51 OOM).
  Step 4 (inflationary dilution, for reference): flatten a generic O(1) start AND survive ~50–60 e-folds
         of post-fold re-growth to today's |Ω_k|≲0.005 ⇒ N≳60 ⇒ e^{-120} = 7.67×10^{-53}  (−52.1 OOM).
  Read-off: 2.89 e-folds give ~2.5 OOM of suppression — a ~49.6 OOM SHORTFALL against the ~52 OOM
            dilution-flatness would need. Flatness CANNOT rest on the acoustic transit budget (2.89 ≪ 60).
            It rests EITHER on a_2-flat-by-construction (0 e-folds; OPEN) OR on the post-fold expansion
            history (S100a: median q=−0.866, mostly-accelerating — a candidate dilution channel, not yet
            connected to an Ω_k prediction). In NEITHER case is "3.1" the flatness instrument: flatness
            needs 0 (a_2-flat) or ≫3.1 (dilution). gap_to_3.1 carries ZERO flatness content.
```

**MISSED — the observational referent of 3.1 itself.** V1 reads "N_e ≥ 3.1" as inflation's conflated horizon+flatness number. But 3.1 is NOT the inflationary horizon+flatness budget (that is ~50–60), nor cleanly the scale-range budget (ln of the observed k-decades ≈ 9.2; see Re:V3). 3.1 matches no standard observational threshold. The under-derivation cuts toward Reading A: the real thresholds are mostly HARDER than 3.1, discharged only by the substrate's open non-dilution mechanisms.

**EMERGES.** The decomposition is right to SEPARATE horizon from flatness (converged), but the separation exposes an asymmetry V1 underplays: horizon is genuinely e-fold-free (substrate dynamics), while flatness is e-fold-IRRELEVANT in a *different* sense — the acoustic e-folds are the wrong order of magnitude either way, and flatness exits the 3.1 axis onto an OPEN gate (a_2 k-selection). An open gate is a deferred liability, not a dissolved one.

#### Re: V2 — N_e substrate-IS vs container

**AGREE on the three-object decomposition.** `N_e^acoustic = 2.8913/2.9202` is genuinely substrate-IS — built from ρ(τ), c_s(τ) along the transit (S53 Eq.15B), the same two-fluid variables as the Landau–Khalatnikov hydrodynamics; I do not demote it. `N_e^geom = 0.1734 = ln(a_f/a_i)` is the most container-like (the log of the emergent FRW scale factor). The separation is clean and accepted. With the upstream **S-4 = HH-UNCONDITIONAL** closing the BC layer, `N_e^geom = 0.1734` is settled and BC-invariant; the live e-fold question is entirely at the acoustic layer and beyond.

**DISAGREE — and this is the load-bearing correction: substrate-first-canonical-sourcing is MISAPPLIED to 3.1.** V2(3) invokes `substrate-first-canonical-sourcing.md §(i)` to forbid 3.1 as a "CANONICAL external-paper citation." That rule governs the PROVENANCE of NUMERICAL PINS consumed by substrate COMPUTATIONS — you may not import an external paper's number as a substrate constant standing in for a computation you never performed. **An observational constraint is not a pin of that kind. It is the external datum the substrate is TESTED AGAINST.** Planck's |Ω_k| ≲ 0.005, the observed k-window, n_s = 0.9649 ± 0.0042 — these are SUPPOSED to be external; "facing the data" is exactly that. If the framework could reclassify every observational bound as a "forbidden container import," it would be unfalsifiable by construction — the precise failure mode `epistemic-discipline.md` exists to prevent. So §(i) does not license retiring an observational requirement; it licenses re-sourcing a substrate PIN. 3.1 is a (badly-encoded) proxy for an observational requirement, not a substrate pin — the rule does not reach it.

The sharp form: "3.1 is not computed from D_K, ρ(τ), c_s(τ)" is TRUE and IRRELEVANT to whether the obligation binds. *Observational constraints are never computed from D_K — they are measured.* The test is whether the substrate's PREDICTION (a_2 flatness; the transported GGE bandwidth) meets the external requirement. Retiring the proxy does not retire the requirement.

**MISSED — mechanism-laden encoding vs mechanism-independent fact.** V2 is RIGHT about something it doesn't quite isolate: "N_e ≥ 3.1" *qua e-fold count* is mechanism-laden — it is inflation's ENCODING of the obligations, not the obligations themselves. The mechanism-independent FACTS are Ω_k, the k-window, n_s — and THOSE bind. I concede the literal e-fold-count gate is the wrong instrument (a mechanism import). The missed step: conceding the encoding is wrong does not concede the facts dissolve — it relocates them to substrate-native gates that must DISCHARGE the facts, and those gates (a_2, TRANSIT-PS-67) are open.

**EMERGES.** The right registry move is not V2's "retire N_e ≥ 3.1, keep N_e^acoustic as an observable with no threshold." It is: retire the e-fold-COUNT encoding, and REPLACE it with the precise observational obligations on the named substrate gates — an Ω_k prediction from a_2 (vs Planck 0.0007 ± 0.0019) and window-wide tilt from TRANSIT-PS-67 (vs n_s 0.9649 ± 0.0042 across ~4 k-decades). That keeps the falsifier surface intact while dropping the mechanism-laden number. "Retire 3.1 with nothing in its place" silently discharges an open liability — the failure mode I most want to block.

#### Re: V3 — container-import reading

**AGREE on the unbundling and the scale-range relocation in PRINCIPLE.** V3's three-job table (horizon / flatness / scale-range) is the right anatomy, and the third row is the observationally load-bearing one. I accept that the observed CMB is the GGE relic acoustic signature (`phononic-framing.md`), not stretched vacuum modes, and that the k-range is therefore set by the GGE Bogoliubov spectrum β(k), not by horizon-exit timing. In PRINCIPLE the scale-range obligation relocates to TRANSIT-PS-67's bandwidth. Accepted as the right address.

**DISAGREE — the relocation is asserted, not discharged; α_s < 0.015 does not certify it.** V3 cites TRANSIT-PS-67's PASS (α_s(k_CMB) < 0.015) as if the scale-range job is done. It is not. **α_s < 0.015 is a PIVOT-LOCAL running** — the curvature of ln P(k) AT k_pivot, a measure-zero point. It says nothing about whether the spectrum holds near-scale-invariant tilt across the FULL observed window. A spectrum can have small running at the pivot and still curve away within one or two decades.

```
Substitution chain — the bandwidth obligation TRANSIT-PS-67 actually owes (Sage-verified):
  Def 1: observed P(k) spans k ∈ [~10^{-4}, ~1] Mpc^{-1} (CMB ℓ∈[2,2500] + LSS/Lyα) ≈ 4 decades.
  Def 2: dynamic range in e-fold-equivalent = ln(k_max/k_min) = ln(10^4) = 4 ln10 = 9.21.
  Def 3 (the transport): β(k) is produced at the transit scale (f_transit≈8.55×10^{37} Hz) and imaged
         to the CMB pivot 54.04 decades down by T_{BZ→pivot} (deg(T_{BZ→pivot})=+2 for the tilt;
         S116-W1-AS-CF3 / canonical).
  Step 4: the obligation is that |β(k)|², AFTER T_{BZ→pivot}, holds n_s = 0.9649 ± 0.0042 across ALL
         9.21 e-folds of the observed window — NOT merely d²lnP/dlnk² < 0.015 at the single pivot.
  Read-off: pivot-local α_s < 0.015 is NECESSARY on a measure-zero point; window-wide near-scale-
            invariance over 9.21 e-folds of k is the SUFFICIENT condition observation demands, and it
            is a SEPARATE, undischarged demonstration. The scale-range obligation relocates to an OPEN
            computation, not to a closed PASS.
```

**MISSED — N_e^acoustic is the wrong observable for scale-range, so gap_to_3.1 is doubly mis-specified.** V3 correctly says the k-range is a β(k) BANDWIDTH, not an ∫H dt. But the workshop's gate compares `N_e^acoustic` (a TEMPORAL expansion measure — the log-growth of the acoustic conformal factor mn/c) to 3.1 (a putative scale-range threshold). Scale-range lives in β(k)'s k-EXTENT, not in N_e^acoustic's value. So `gap_to_3.1 = 3.1 − 2.8913 = 0.2087` is meaningless TWICE: 3.1 is a mechanism-laden proxy AND N_e^acoustic is not the scale-range quantity. This supports retiring the `N_e^acoustic ≥ 3.1` COMPARISON — but it TRANSFERS the obligation to "β(k)-bandwidth, transported, ≥ 9.21 e-folds of k at the observed tilt," which is TRANSIT-PS-67's open burden.

**DISSENT on the verdict — the 6.7% is FALSELY reassuring.** V3 concludes the gap "DISSOLVES" and the 6.7% acoustic shortfall is "a coincidence of the scaling that produced 3.1." I AGREE the 6.7% is not meaningful — but for the OPPOSITE conclusion. The smallness of 0.21 is not evidence the substrate "almost made it" (V3 right); but neither is it evidence the substrate is fine. Once the obligations are properly specified, the true gap can be far WORSE than 6.7%: window-wide bandwidth over 9.21 e-folds of k is a much stronger demand than "N_e^acoustic within 7% of 3.1," and a_2 flatness is binary (k=0 or broken). I take V3's "the gap size is meaningless" and turn it: the meaninglessness means the liability is UNBOUNDED above by 6.7%, not dissolved below it.

#### Re: V4 — Cross-Cutting

**AGREE on V4.1 — the three facts are binding; the framing is right.** V4 concedes causal coherence, flatness (|Ω_k| ≲ 0.005), and broadband near-scale-invariant P(k) are binding facts regardless of mechanism, and that the substrate-native encoding is three gates, not one e-fold number. This is the core of our convergence. Where we diverge is narrow, and I state it sharply: conceding the facts are binding while routing them to OPEN gates means the framework's observational viability is, RIGHT NOW, ESTABLISHED on horizon and UNESTABLISHED on flatness and scale-range. The honest scorecard is 1-of-3 discharged, 2-of-3 deferred — a standing liability, not a dissolved one.

**DISAGREE on V4.3 — the lab grounding answers the conceded question, not the disputed ones.** The Rolley–Guthmann–Pettersen–Chevallier 4He hydraulic-jump white hole sealing a horizon with zero e-folds (and the 3He-A PG construction, T_H = ħ|v'(r_h)|/2π) is a genuine demonstration that an e-fold count is not NECESSARY for horizon-sealing in this universality class. I accept it fully. But it is a HORIZON demonstration, and horizon is the piece I concede. A benchtop superfluid white hole seals causal contact; it does NOT exhibit a flat emergent 3-geometry, nor a broadband near-scale-invariant fluctuation spectrum spanning 4 decades of k. V4.3 has zero purchase on the two obligations actually in dispute (flatness, scale-range). It is the strongest possible answer to a question that isn't the live one.

**MISSED on V4.2 — "derived diagnostic" SHARPENS Reading A, it does not soften it.** V4.2 argues N_e^acoustic is a DERIVED diagnostic of the same two-fluid structure that nullifies the CC, so importing 3.1 "treats a derived diagnostic as an independent fundamental knob." But *derived ≠ exempt from observational test.* The CMB temperature is derived; it still must match 2.725 K. A derived quantity with NO free knob is a HARDER test, not a softer one: if the rigid prediction undershoots what observation needs (via whatever channel), the framework is FALSIFIED, not "in need of more e-folds." The parameter-free character cuts FOR Reading A — the obligations bind MORE tightly because there is no knob to absorb a shortfall. (One regime caveat: the CC-nullification is an EQUILIBRIUM statement, ε_vac = −P_vac = 0; N_e^acoustic is a DIABATIC-TRANSIT quantity — the Ordered Veil never thermalizes, S95. They share (ρ, c_s) but evaluate them in different regimes — equilibrium endpoint vs impulsive transit — so "two readings of ONE structure" is really "two regimes of one structure," and the consistency is looser than V4.2 implies.)

**EMERGES.** V4.4 (scope) and I agree completely: TRANSIT-PS-67 and a_2-flatness are open. The disagreement is purely about what "open" entails. V4 reads "open gate" as "the obligation relocated successfully, 3.1 retired." I read "open gate" as "the obligation is binding and UNDISCHARGED; the liability stands until the gate closes favorably." Both of us want 3.1-the-e-fold-count retired; only I insist its observational content be transferred, not deleted.

### Part 2: Original Analysis

#### M1: The binding-requirement reading (Reading A) — observational viability needs scale-range + flatness

Reading A's strong form is NOT "the substrate must inflate" — volovik rightly pre-empted that (V4.1). It is: the OBSERVED universe is (i) causally coherent, (ii) spatially flat to |Ω_k| ≲ 0.005, (iii) carries a broadband near-scale-invariant P(k) over ~4 decades of k with n_s = 0.9649 ± 0.0042 — three mechanism-independent facts the substrate must deliver by SOME substrate-native mechanism. "N_e ≥ 3.1" is a crude, mechanism-laden proxy for the bundle; retiring the proxy is fine, but the obligations it stands for are binding, and the substrate's named mechanisms for them are open. So the gap is real — not as a literal e-fold shortfall, but as an undischarged observational obligation.

**The observational scorecard (what 3.1 actually proxies):**

| Obligation | Current datum (Planck 2018) | Substrate mechanism | Status |
|:--|:--|:--|:--|
| Horizon (sky causally coherent) | full-sky ΔT/T ~ 10⁻⁵ | global-modulus homogeneity + acoustic white-hole sealing (Mach 13.75) | **LARGELY DISCHARGED** (e-fold-free); caveat: homogeneity is an IC posit |
| Flatness (Ω_k → 0) | Ω_k = 0.0007 ± 0.0019 (CMB+BAO); \|Ω_k\| ≲ 0.005 | a_2 Seeley–DeWitt emergent 3-geometry must give k=0 (not k=±1) | **OPEN** — uncomputed; homogeneity ≠ flatness |
| Scale-range + tilt | P(k) over k ∈ [10⁻⁴,1] Mpc⁻¹ (~9.21 e-folds of k); n_s = 0.9649 ± 0.0042 | GGE β(k) bandwidth, transported 54.04 dec by T_{BZ→pivot} | **OPEN** — α_s<0.015 is pivot-local; window-wide unshown |

**Decompose 3.1.** It is neither the inflationary horizon+flatness budget (~50–60) nor the scale-span budget (~9.21). It has no recognizable observational referent — an under-derived threshold, and the workshop's own note flags that neither prior agent questioned its provenance. The under-derivation FAVORS Reading A: the precise obligations are mostly HARDER than 3.1 (dilution-flatness needs ≫3.1 if a_2 isn't flat — a ~49.6 OOM shortfall on the acoustic budget, Re:V1; scale-span needs ~9.21 e-folds of k), discharged only by the substrate's open non-dilution mechanisms.

**What 3.1 buys: nothing precise. What the OBLIGATIONS buy: falsifiability.** Each obligation is a sharp, parameter-free test the substrate either passes or fails — and that is the registry content worth KEEPING when 3.1 is retired. The Reading-A claim is therefore not "N_e^acoustic must reach 3.1" (a weak claim — N_e^acoustic is the wrong observable and 3.1 the wrong threshold). It is: the gap is a real liability because two of three observational obligations are undischarged, and the framework cannot retire the liability by relabeling — only by closing the a_2 and TRANSIT-PS-67 gates favorably. "Dissolved category error" is the wrong verdict; "real liability, wrong encoding, transfer don't delete" is the right one.

#### M2: What TRANSIT-PS-67 must deliver if 3.1 is binding (the standing-liability tag)

**The precise observational obligation.** TRANSIT-PS-67 must deliver |β(k)|² (the GGE acoustic power spectrum) such that, after T_{BZ→pivot} (54.04 decades, deg +2), the CMB-pivot P(k):

- (i) **spans** k ∈ [10⁻⁴, 1] Mpc⁻¹ — the 9.21-e-fold BANDWIDTH of the observed window (CMB ℓ∈[2,2500] + LSS/Lyα);
- (ii) **holds n_s = 0.9649 ± 0.0042 ACROSS that window** — window-wide near-scale-invariance, not pivot-local;
- (iii) **keeps α_s within bounds across the window** — the pivot-local PASS (α_s < 0.015) is necessary, not sufficient;
- (iv) **amplitude A_s ≈ 2.1×10⁻⁹** — though A_s magnitude is itself SCHEME-DEPENDENT in the framework (S116-W1: squeeze A_s = 1.5367×10⁻⁸, OOM band [+0.196, +1.527] vs Planck), so the amplitude is a live, unsettled axis, not a clean PASS.

**Does the acoustic bandwidth meet it?** The sudden/impulsive quench (S70: WKB inapplicable, sudden approximation mandatory) produces a broadband Bogoliubov spectrum — |β(k)|² ~ O(1) below a cutoff set by the fold sharpness, falling above. The OPEN question is whether the band over which |β(k)|² has near-scale-invariant SHAPE spans 9.21 e-folds of k AFTER transport. The framework has the pivot-local result (α_s < 0.015); it does NOT yet have the window-wide demonstration. The obligation is undischarged.

**The standing-liability tag (precise re-location).** Replace "N_e^acoustic ≥ 3.1" with:

> **β(k)-bandwidth, transported through T_{BZ→pivot}, ≥ 9.21 e-folds of k at n_s = 0.9649 ± 0.0042 window-wide.**

This is the SAME observational target V3 names — stated as the falsifiable quantity TRANSIT-PS-67 actually computes — and it is OPEN. Critically, `N_e^acoustic = 2.89` is NOT this quantity: it is a temporal conformal-factor growth (log of mn/c), not a spectral bandwidth. So the workshop's `gap_to_3.1` at the acoustic layer (~0.21) is not even measuring the right thing. M2's contribution is to RE-LOCATE the liability onto the quantity TRANSIT-PS-67 genuinely owes — the gap is real but currently mis-located by the gate.

**Falsifier-surface note (discipline).** IF this framing is adopted, the scale-range obligation becomes a §7 / `falsifier-master-inventory.md` entry (TRANSIT-PS-67 window-wide bandwidth + tilt vs Planck), and the flatness obligation a second entry (a_2 Ω_k prediction vs Planck 0.0007 ± 0.0019). I FLAG these for the Wave-6 synthesis designated writer; I do NOT effect them in this workshop turn — the §7 / inventory surface is `mack-cosmic-bridge` sole-writer domain reached via a separate landing, never a workshop edit (AMRI / `feedback_mack-bridge-role.md`).

#### M3: Questions for volovik

**Q-M1 (homogeneity ≠ flatness — name the k-selector).** A homogeneous emergent 3-geometry can be a 3-sphere (k=+1) or hyperbolic (k=−1), both maximally symmetric. Your V1 routes flatness to "a_2 inherits global-modulus homogeneity," but homogeneity does not fix k. What in the a_2 Seeley–DeWitt geometry SPECIFICALLY selects k=0 over k=±1? Until that is computed, on what observational ground is flatness "relocated" rather than "deferred"? Planck binds Ω_k = 0.0007 ± 0.0019; the substrate currently predicts *nothing* for Ω_k.

**Q-M2 (window-wide vs pivot-local — exhibit the bandwidth).** TRANSIT-PS-67's α_s < 0.015 is a pivot-local running. Exhibit that the GGE β(k) bandwidth, after T_{BZ→pivot} (54.04 decades), holds n_s = 0.9649 ± 0.0042 across the FULL observed window (~9.21 e-folds of k from CMB to LSS), not just at the pivot. If the band curves away within 1–2 decades, the scale-range obligation fails regardless of the pivot α_s. Does the framework have the window-wide demonstration, or only the pivot-local one?

**Q-M3 (dissolved or deferred — and is it falsifiable?).** You route horizon → acoustic-WH (discharged), flatness → a_2 (open), scale-range → TRANSIT-PS-67 (open) — 2-of-3 open. If a_2 gives k=±1, OR TRANSIT-PS-67's transported band fails to span the observed k-decades at the observed tilt, **is the framework FALSIFIED?** If YES, the obligations are binding (Reading A) — just not in the "3.1 e-fold" encoding — and "dissolved category error" is the wrong verdict; "real liability, wrong encoding, transfer don't delete" is right. If NO (nothing could falsify them), then the deeper problem surfaces: the framework's flatness / scale-range claims are not observational claims at all. Which is it? — because that binary, not the value of N_e^acoustic, is what decides Reading A vs Reading B.

---

## Round 2 — volovik: Follow-up

### CONVERGENCE

mack's three load-bearing corrections (Re:V1 flatness, Re:V2 the sourcing-rule, Re:V3 scale-range) land, and I move on all three. I separate what I concede (here) from what survives on corrected ground (DISSENT).

**(1) homogeneity ≠ flatness — conceded; flatness is OPEN, deferred not dissolved (Re:V1, Q-M1).** mack is right that a homogeneous FRW 3-geometry can be a 3-sphere (k=+1) or hyperbolic (k=−1) — both maximally symmetric, both homogeneous, neither flat. The curvature datum k survives homogeneity as a SEPARATE invariant, so my V1 "the emergent spatial sections inherit the global-modulus homogeneity" buys NO head-start on k=0 in a generic-FRW reading. I withdraw any implication that homogeneity *alone* discharges flatness. And I accept the sharper epistemics: my V1 already said flatness "RELOCATES rather than dissolves," and mack's Re:V1 correctly tightens "relocate to an open gate" = a DEFERRED liability, not a discharge. Flatness is a genuine open substrate-geometry obligation. (What it relocates ONTO — and why the relocation is not a bare IOU — is DISSENT (1).)

**(2) substrate-first-canonical-sourcing §(i) was the wrong rule — withdrawn (Re:V2).** This is a methodology call in my own translator's domain, and mack's correction is correct. `substrate-first-canonical-sourcing.md §(i)` governs the PROVENANCE of a numerical PIN a substrate computation CONSUMES — its operational test is literally "a canonical citation REPLACES the substrate-first computation." An observational threshold is not a pin of that kind; it is the external datum the framework is TESTED AGAINST, and "facing the data" requires exactly such external numbers. Reclassifying every observational bound as a "forbidden container import" would make the framework unfalsifiable by construction — the failure mode `epistemic-discipline.md` exists to block. I withdraw the §(i) citation against `3.1`. (The substantive non-transfer claim survives on a different, corrected ground — DISSENT (2): `3.1` is not an observational datum either.)

**(3) pivot-local α_s does NOT discharge scale-range — conceded (Re:V3, Q-M2).** I cited TRANSIT-PS-67's α_s(k_CMB) < 0.015 as if the scale-range job were done. mack is right it is not: α_s < 0.015 is the curvature of ln P(k) at a single pivot — a measure-zero point — and says nothing about whether near-scale-invariance holds across the full observed window. I verified the gate's live status against the registry: TRANSIT-PS-67 is OPEN (CRITICAL) — "full Bogoliubov power spectrum through fold … power spectrum computation pending" (constraint-mega-matrix); the framework holds the pivot result (α_s; n_s anchored 0.9561 framework / 0.9590 sqrt-cutoff) but NOT the window-wide demonstration. Window-wide near-scale-invariance over ln(10⁴)=9.21 e-folds of k, AFTER the 54.04-decade transport, is a separate, undischarged computation. Conceded.

**(4) the scorecard, and "transfer, don't delete."** I accept mack's honest scorecard: horizon DISCHARGED (acoustic white hole, PROVEN S85, lab-realized); flatness and scale-range OPEN — 1-of-3 discharged, 2-of-3 deferred. The right verdict for the OBLIGATIONS is mack's "real liability, wrong encoding, transfer don't delete," NOT my "dissolved category error." My "dissolved" is correct for the e-fold COUNT `3.1` specifically (DISSENT (2)) and WRONG for the observational obligations it proxied — those are real and mostly undischarged. I retract "dissolved" as the verdict on the obligations.

**(5) parameter-free = harder test — adopted (Re:V4.2 MISSED).** mack turned my V4.2 cleanly: a DERIVED, no-knob prediction is a HARDER test, not a softer one — if it undershoots what observation needs, the framework is falsified, with no knob to absorb the shortfall. I agree, and I will USE it (EMERGENCE): the substrate's flatness and tilt predictions are parameter-free, which makes retiring `3.1` TIGHTEN the falsifier surface, not loosen it — the direct answer to the unfalsifiability worry. (I accept the regime caveat too: the CC-nullification is an EQUILIBRIUM statement, N_e^acoustic a DIABATIC-TRANSIT one — "two regimes of one two-fluid structure," not "two readings of one," as mack sharpened.)

### DISSENT

New evidence only, on two points.

**(1) The k-selector mack demanded (Q-M1, Re:V1) EXISTS — and it is substrate-physics, not generic-FRW. homogeneity is silent on k for a GENERIC FRW metric; the substrate's emergent metric is not generic — it is ACOUSTIC, and acoustic metrics carry no free k.** This is the new content. mack's 3-sphere counterexample is a GR configuration; the live question is whether the substrate's emergent geometry is a generic GR metric (free k ∈ {−1,0,+1}) or an acoustic/Painlevé-Gullstrand metric (no free k). In Volovik's superfluid-vacuum universality class the effective metric for the low-energy quasiparticles is ALWAYS of acoustic/PG type — and that form has EXACTLY flat spatial sections by construction:

```
Substitution chain — the acoustic metric is flat-sliced (k=0) BY CONSTRUCTION:
  Def 1: emergent metric in the superfluid-vacuum universality class = acoustic / Painlevé-Gullstrand form,
         ds² = (ρ/c)[ −(c²−v²) dt² + 2 v·dx dt + dx² ]      [Volovik 01_2001 conformal factor mn/c;
                                                              27_2003 Eq.(1) PG; the "river model"].
  Def 2: cosmological (homogeneous, isotropic) specialization ⇒ v = Hubble flow, ρ, c spatially uniform
         ⇒ ds² = −dt² + a²(t) dx²   (spatially-flat FRW); spatial slice = a²(t) δ_ij.
  Step 3: a²(t) δ_ij at fixed t = (constant) × δ_ij = the flat Euclidean 3-metric ⇒ R^{(3)} ≡ 0 ⇒ k = 0.
          (PG black-hole form: the spatial slice dr² + r²dΩ² is likewise flat Euclidean 3-space, for ANY v(r).)
  Step 4: the conformal factor ρ/c is spatially HOMOGENEOUS (global-modulus inheritance, V1) ⇒ it rescales,
          but does not curve, the (already flat) slices.
  Read-off: the acoustic metric carries no free k ∈ {−1,0,+1}; its preferred (comoving) foliation is flat-sliced,
            and the "curvature" lives entirely in v and a(t). A homogeneous 3-sphere (k=+1) is a GR configuration
            the acoustic construction does NOT produce.
```

So homogeneity ≠ flatness for a GENERIC FRW (mack is right), but for an acoustic metric there is no free k to be silent about — the universality class produces flat-sliced metrics. The k-selector is therefore "is the a_2 Seeley-DeWitt geometry of acoustic/PG form (does it admit the flat-sliced preferred foliation)?" — sharp and computable, with a substrate-physics PRIOR pointing to k=0 (the superfluid-vacuum universality class produces acoustic metrics; cf. 01_2001 acoustic metric from the two-fluid (ρ, c_s); 02_2023). This is NOT "homogeneity gives flatness" (refuted) and NOT a bare uncomputed IOU ("is a_2 flat?"). It is a structural relocation: flatness → "is a_2 acoustic-form?", with the answer expected k=0 from the universality class. I CONVERGE with mack that this is OPEN (the a_2 computation has not confirmed acoustic-form); I DISSENT from "homogeneity is silent on k" — for the substrate's universality class, the natural foliation is flat-sliced by construction.

**(2) `3.1` does not transfer — on the CORRECTED ground that it is neither a substrate pin (my withdrawn §(i)) NOR an observational datum (mack's framing), but a competing-mechanism internal intermediate.** mack's Re:V2 reads `3.1` as "the external datum the substrate is tested against." It is not — and this is where I still disagree, with new structure. Planck does not measure "N_e ≥ 3.1"; no instrument does. `3.1` is the e-fold count INFLATION's specific DILUTION mechanism needs to discharge horizon+flatness on the FRW container — a number internal to a competing framework's machinery, NOT a measured quantity. The OBSERVATIONAL data (Ω_k = 0.0007 ± 0.0019; n_s = 0.9649 ± 0.0042; the k-window) bind regardless of mechanism (CONVERGENCE (4)); `3.1` is inflation's ENCODING of how to meet them by dilution. Exflation meets the SAME observational obligations by mechanisms that do not count e-folds (acoustic sealing / acoustic-PG flat-slicing / GGE bandwidth), so `3.1`-the-count does not transfer — and retiring it retires NO falsifier, because the falsifiers are the observational obligations (Ω_k, n_s, k-window), which I keep. mack's unfalsifiability worry is answered not by retaining `3.1` but by retaining the real falsifiers it badly proxied.

### EMERGENCE

**The A/B/C taxonomy that dissolves the apparent disagreement.** The workshop's confusion is that `3.1` was treated as one of two things when it is a third:

| Category | What it is | Governing rule | `3.1`? | The obligations? |
|:--|:--|:--|:--|:--|
| **(A) substrate pin** | a number a substrate computation CONSUMES | `substrate-first-canonical-sourcing.md §(i)` | NO (my V2 error) | — |
| **(B) observational datum** | the external number the framework is TESTED against | falsification (`epistemic-discipline.md`) | NO (mack's framing) | YES — Ω_k, n_s, k-window BIND |
| **(C) competing-mechanism intermediate** | a number internal to inflation's dilution machinery | none — it does not transfer | YES — `3.1` lives here | — |

My V2 mis-filed `3.1` as (A); mack's Re:V2 mis-filed it as (B). It is (C). Once filed correctly the apparent disagreement dissolves: the (B) obligations bind and are KEPT (mack's core point, conceded); the (C) number `3.1` is retired as non-transferring (my point, on corrected ground); and `substrate-first-canonical-sourcing.md §(i)` (A) governs neither. The sharp distinction the workshop needed: "the OBSERVABLE the data demands" (flatness Ω_k, window-wide tilt) is category (B) and BINDS; "the MECHANISM `3.1` encodes" (e-fold dilution) is category (C) and does NOT transfer.

**The three-way obligation split — converged, with substrate-physics content added to each open gate:**

| (B) Obligation | Substrate mechanism (no e-folds) | Status | Substrate-physics prior |
|:--|:--|:--|:--|
| Horizon (sky causally coherent) | inherited global-modulus homogeneity + acoustic white-hole sealing (Mach 13.75) | **DISCHARGED** (PROVEN S85; lab-realized 09_2005) | — |
| Flatness (Ω_k = 0.0007 ± 0.0019) | a_2 geometry acoustic/PG-form ⇒ flat-sliced ⇒ k=0 by construction | **OPEN** gate "is a_2 acoustic-form?" | → k=0 (universality class produces acoustic metrics, 27_2003/01_2001) |
| Scale-range + tilt (n_s = 0.9649 ± 0.0042 over 9.21 e-folds of k) | GGE β(k) bandwidth, transported 54.04 dec (deg +2) | **OPEN (CRITICAL)** TRANSIT-PS-67 window-wide | → wide band (deep-sudden Mach-13.75 quench is near-scale-free; running = finite-sharpness correction) |

The convergence with mack is the STRUCTURE (transfer don't delete; 2-of-3 open; binding falsifiers). My contribution as the substrate-physics translator is the third column: each open gate has a directional substrate-physics prior grounded in the superfluid-vacuum corpus, so "open" here means "open with a prior + a sharp falsifier," not "open and unknown."

**Parameter-free sharpness — the falsifiability answer (adopting Re:V4.2).** Each substrate obligation is a NO-KNOB prediction. The acoustic-PG route predicts Ω_k = 0 EXACTLY (k=0 by construction — no curvature knob); the sudden-quench route fixes the window-wide tilt from fold kinematics (Mach number + sharpness — no slow-roll potential to tune). A parameter-free prediction binds MORE tightly than inflation's tunable version: if a_2 comes out non-acoustic (k≠0), OR the transported band fails to span 9.21 e-folds at the observed tilt, the framework is FALSIFIED with no knob to absorb it. So retiring `3.1` TIGHTENS the falsifier surface. The structural change: `3.1`-the-e-fold-count (category C, retired) → two parameter-free substrate falsifiers (Ω_k from a_2; window-wide tilt from TRANSIT-PS-67).

**Two falsifier-surface candidates (flagged for mack as §7 sole writer — NOT effected here, per AMRI / `feedback_mack-bridge-role.md`):** (i) a_2 acoustic-form ⇒ Ω_k = 0 vs Planck 0.0007 ± 0.0019; (ii) TRANSIT-PS-67 window-wide tilt over 9.21 e-folds of transported k vs n_s 0.9649 ± 0.0042. Both are the substrate-native replacements for the retired `3.1` gate.

### QUESTIONS

**A-M1 (the k-selector — answered).** The k-selector is the acoustic/Painlevé-Gullstrand structure of the emergent metric, NOT homogeneity. The PG form (Volovik 27_2003 Eq.1) has exactly flat spatial slices (dr² + r²dΩ², R^{(3)}≡0, k=0) for ANY flow v(r) — the "curvature" is the flow, the spatial sections are flat by construction (DISSENT (1)). So homogeneity is silent on k for a generic FRW (you are right), but the substrate's emergent metric is acoustic, and acoustic metrics carry no free k. The flatness gate is therefore "is the a_2 geometry acoustic/PG-form (does it admit the flat-sliced preferred foliation)?" — with a substrate-physics prior → k=0 from the universality class. OPEN (the a_2 computation must confirm acoustic-form), but a sharp, parameter-free Ω_k = 0 prediction, not a bare "is it flat."

**A-M2 (window-wide vs pivot-local — answered: the framework has only the pivot result).** No — the framework does NOT have the window-wide demonstration, only pivot-local α_s < 0.015 (registry: TRANSIT-PS-67 OPEN/CRITICAL, "power spectrum computation pending"). I concede this fully. What I can supply is the substrate-physics prior and the precise computable quantity: a SUDDEN (impulsive) quench has no internal scale except the fold sharpness, so the deep-sudden (Mach 13.75) Bogoliubov spectrum |β(k)|² is near-scale-FREE over a wide band; the DEPARTURES from scale-invariance (the running) are FINITE-SHARPNESS corrections, parametrically suppressed in the deep-sudden limit. The transport T_{BZ→pivot} (deg +2) is a power-law rescaling of k, which PRESERVES bandwidth in log-k. So the obligation reduces to a computable quantity — the near-scale-free bandwidth of the sudden-quench spectrum, transported — expected wide for Mach 13.75 but NOT yet demonstrated to span 9.21 e-folds. That demonstration is TRANSIT-PS-67's genuine open burden.

**A-M3 (dissolved or deferred — and falsifiable? answered: DEFERRED and FALSIFIABLE).** Deferred, and yes falsifiable. If the a_2 geometry comes out non-acoustic (k≠0), OR TRANSIT-PS-67's transported band fails to span 9.21 e-folds at n_s = 0.9649 ± 0.0042, the framework is FALSIFIED — these are parameter-free predictions with no knob (EMERGENCE). So the obligations are binding (your Reading A), in the substrate-native encoding (NOT the `3.1`-e-fold encoding). The precise verdict: the e-fold-COUNT `3.1` is a dissolved category error (category C, non-transferring); the observational OBLIGATIONS it proxied are real, deferred, falsifiable liabilities. "Real liability, wrong encoding, transfer don't delete" is the converged verdict — for the obligations; "dissolved" survives only for the number `3.1`.

**Questions back to mack (for your R2 cross-synthesis):**

- **Q-V4 (does the acoustic-PG k-selector reframe the flatness gate to your satisfaction?).** I have replaced "homogeneity gives flatness" (refuted) with "the acoustic/PG metric is flat-sliced by construction; the open gate is whether a_2 is acoustic-form" — a parameter-free Ω_k = 0 prediction vs Planck 0.0007 ± 0.0019. Does that satisfy your Q-M1 falsifiability requirement (a sharp k-selector + a binding Ω_k test), or do you read "is a_2 acoustic-form?" as itself too soft a gate (i.e., does the acoustic-form question admit a non-flat answer that would still be called "acoustic," leaving k under-determined)?

- **Q-V5 (do we converge on the verdict?).** I propose the pinned verdict: gap_to_3.1 is a DISSOLVED category error AS AN E-FOLD COUNT (category C, `3.1` non-transferring) AND a REAL, DEFERRED, FALSIFIABLE liability AS AN OBLIGATION (flatness → a_2-Ω_k OPEN; scale-range → TRANSIT-PS-67 window-wide OPEN; horizon DISCHARGED). The number `3.1` is retired; its two undischarged obligations relocate to two parameter-free substrate gates. Do you accept that joint phrasing — "dissolved as the count, real as the obligations" — as the workshop verdict, or do you want the liability tagged more strongly (e.g., the scorecard 2-of-3-open carried as the headline rather than the retirement of `3.1`)?

---

## Round 2 — mack: Cross-Synthesis

### CONVERGENCE

volovik's R2 conceded my three load-bearing corrections (Re:V1 homogeneity≠flatness; Re:V2 the §(i) misapplication; Re:V3 pivot-local α_s ≠ scale-range) and returned new structure. I accept the new structure on four points; the disagreement that remains is narrow and productive (DISSENT).

**(1) The A/B/C taxonomy resolves the apparent binary — adopted.** volovik's EMERGENCE table is the right anatomy, and it dissolves the R1 standoff (his "dissolved" vs my "real liability") cleanly. `3.1` is neither a substrate pin (category A, `substrate-first-canonical-sourcing.md §(i)` — his withdrawn V2 error) NOR an observational datum (category B — my Re:V2 reading); it is a **category-C competing-mechanism intermediate** — the e-fold count INFLATION's dilution machinery needs to discharge horizon+flatness on the FRW container. No instrument measures `N_e ≥ 3.1`; Planck measures `Ω_k`, `n_s`, the k-window. Once `3.1` is filed as (C), my "transfer, don't delete" and his "dissolved as the count, real as the obligations" are the SAME verdict: the (B) obligations BIND and are KEPT; the (C) number does NOT transfer and is retired. Converged.

**(2) The scorecard — 1-of-3 discharged, 2-of-3 deferred — adopted verbatim.** Horizon DISCHARGED (acoustic white-hole sealing, PROVEN S85, lab-realized Rolley et al. `09_2005`); flatness and scale-range OPEN. volovik accepted my honest scorecard and retracted "dissolved" as the verdict on the obligations. Converged.

**(3) parameter-free = harder test ⇒ retiring `3.1` TIGHTENS the falsifier surface — this is the answer to my own unfalsifiability worry.** I raised the worry (Re:V2: reclassifying observational bounds as "container imports" would make the framework unfalsifiable). volovik answers it correctly with my own Re:V4.2 turn: each substrate obligation is a NO-KNOB prediction (Ω_k = 0 EXACT from acoustic-form; window-wide tilt from fold kinematics, no slow-roll potential to tune). A parameter-free prediction binds MORE tightly — if it undershoots what observation needs, the framework is FALSIFIED with no knob to absorb the shortfall. Retiring `3.1` removes a vacuous comparison and exposes two sharp falsifiers. The unfalsifiability worry is answered not by KEEPING `3.1` but by keeping the real falsifiers it badly proxied. Converged — and this is the single most important load-bearing agreement of the workshop.

**(4) the regime caveat is mutual.** volovik accepted my Re:V4.2 sharpening: the CC-nullification (`ε_vac = −P_vac = 0`) is an EQUILIBRIUM statement; `N_e^acoustic` is a DIABATIC-TRANSIT one (the Ordered Veil never thermalizes, S95). "Two regimes of one two-fluid structure," not "two readings of one." Converged.

### DISSENT

New structure only, on volovik's two posed questions.

**(1) Answering Q-V4 — the acoustic-PG k-selector is RIGHT, but the gate "is a_2 acoustic-form?" is, AS LITERALLY STATED, too soft; Q-V4's own worry is vindicated, and the fix is a TWO-part gate.** volovik asks directly whether I read "is a_2 acoustic-form?" as too soft — "does the acoustic-form question admit a non-flat answer that would still be called acoustic, leaving k under-determined?" My answer: **YES, as literally stated it does** — and the reason is a precise one his substitution chain (DISSENT (1), lines 303–316) passes over at Step 3.

```
Substitution chain — acoustic-form ⇒ conformally-flat (NOT flat); the k=0 selector is uniform ρ/c:
  Claim: "g_ij^(3) acoustic ⇒ Ω²(x)δ_ij = CONFORMALLY flat; conformal-flatness ALONE does not select
          k=0 (all three k∈{−1,0,+1} are conformally flat); the k=0 selector is Ω = ρ/c SPATIALLY CONSTANT."

  Step 1: acoustic/PG slice at fixed t (Volovik 01_2001 Eq.13 conformal factor mn/c; 27_2003 Eq.1 PG):
          g_ij^(3) = (ρ/c) δ_ij = Ω²(x) δ_ij,   Ω² ≡ ρ/c.                  [conformally flat by construction]
  Step 2: 3D conformal-flatness ⟺ Cotton tensor C_ijk ≡ 0. Every constant-curvature 3-space (k=−1,0,+1)
          is maximally symmetric ⇒ C_ijk ≡ 0 ⇒ ALL THREE are conformally flat. The round 3-sphere (k=+1)
          in stereographic coords IS of acoustic form: g = [4/(1+|x|²)²] δ_ij = Ω²(x)δ_ij, Ω = 2/(1+|x|²).
  Step 3: ⇒ "g_ij^(3) = Ω²(x)δ_ij" is satisfied by S³ (k=+1) and H³ (k=−1) too — via a SPATIALLY-VARYING Ω.
          Acoustic-form ALONE does NOT exclude k=±1. (This is the soft spot Q-V4 worried about — it is real.)
  Step 4: scalar curvature of a conformally-flat 3-metric (standard, exact):
          R^(3) = −Ω^{−2}( 4∇²lnΩ + 2|∇lnΩ|² )   [flat-space ∇², |∇|²].
          Ω = const  ⇒ ∇²lnΩ = 0, |∇lnΩ|² = 0  ⇒ R^(3) = 0  ⇒ k = 0.
          Ω = (1 + (k/4)|x|²)^{−1} (varying) ⇒ R^(3) = 6k ≠ 0  ⇒ k = ±1.
  Read-off: within the acoustic (conformally-flat) class, the k=0 SELECTOR is Ω = ρ/c SPATIALLY CONSTANT —
            a UNIFORM conformal factor in the preferred (lab-Cartesian / Painlevé) foliation — NOT "acoustic-form"
            per se. The homogeneity that does the work is uniformity of the PHYSICAL density field ρ/c in the
            privileged coordinates, a STRONGER datum than the geometric (isometry-transitive) homogeneity my
            3-sphere counterexample addressed. volovik's Step 3 "a²(t)δ_ij = (const)×δ_ij ⇒ k=0" SMUGGLES IN the
            constant conformal factor under the label "acoustic-form"; the constancy is the separate uniform-ρ/c input.
  Conclusion: the gate is TWO-part. (a) a_2 emergent metric is acoustic/PG-form (admits a substrate-rest-frame
            preferred foliation whose slices are Ω²δ_ij). (b) the a_2 conformal prefactor ρ/c is spatially UNIFORM
            in that foliation under the homogeneous global-modulus (τ uniform) state. (a)∧(b) ⇒ k=0 EXACT ⇒ Ω_k=0;
            (a)∧¬(b) ⇒ conformally-flat-but-CURVED ⇒ k≠0 ⇒ Ω_k≠0 ⇒ FALSIFIED vs Planck 0.0007 ± 0.0019.
```

So I CONVERGE with volovik on the CONCLUSION (k=0 is the expected substrate-physics answer, and flatness is the right address — the a_2 emergent geometry, not an e-fold count) and on the relocation. I DISSENT on the DERIVATION: "acoustic-form" is conformal-flatness, which is exactly as silent on k as generic homogeneity was (his own concession (1)) — both S³ and H³ are conformally flat. What earns k=0 is the conjunction with a uniform conformal factor in the substrate's preferred foliation. This is not a demotion of his argument; it is the upgrade that makes it a SHARP, parameter-free falsifier instead of a soft one. One scope note I add as the observational voice: k=0 is foliation-dependent, and the acoustic/PG construction supplies a *physically distinguished* foliation (the superfluid rest frame = the substrate's absolute Painlevé time). That is a virtue — the foliation is the substrate's own, not chosen to produce k=0 — but it must be stated, because if the a_2 geometry did NOT single out a preferred rest frame, the "k=0" claim would lose its anchor. The two-part gate folds this in: (a) includes "admits the substrate-rest-frame preferred foliation."

**(2) Answering Q-V5 — I accept the joint verdict, with ONE headline refinement (the scorecard, not the retirement, is the durable output).** volovik proposes "dissolved as the count, real-deferred-falsifiable as the obligations." I accept this as the workshop verdict; it IS "transfer don't delete." My one refinement is on EMPHASIS, per `output-standards.md` (structural changes are SUBORDINATE-to nothing; numerical/encoding revisions are subordinate to them): the durable, structural output is the SCORECARD re-anchored onto two parameter-free substrate falsifiers (1 discharged / 2 open-no-knob). The retirement of the *number* `3.1` is the enabling ENCODING revision that makes those two entries no-knob — it is the means, not the headline. So on the §7 falsifier surface I carry the **scorecard 2-of-3-open as the headline**, with "3.1 retired as category-C" as the move that sharpens the two open entries. A reader who headlines "dissolved category error" will under-weight two undischarged, binding liabilities; a reader who headlines "1-of-3 discharged, 2-of-3 open and now parameter-free" reads the framework's current standing correctly. This is the stronger-tagging volovik offered me in Q-V5, and I take it — not by re-opening the verdict, but by ordering the surface.

**Residual on scale-range (mild, on completeness not direction).** volovik's A-M2 deep-sudden near-scale-free prior (the Mach-13.75 quench has no internal scale but the fold sharpness, so |β(k)|² is near-scale-free over a wide band; running = finite-sharpness correction) is a substrate-physics PRIOR, not a result — and it carries TWO undischarged sub-conditions, not one: (i) the finite-sharpness running must be shown *sufficiently suppressed* over the full 9.21 e-folds of k after the deg-+2 transport, not merely small at the pivot; and (ii) it must be reconciled with the LIVE amplitude-scheme axis — the squeeze `A_s = 1.5367×10⁻⁸` is OOM `+0.864`, band `[+0.196, +1.527]` vs Planck, magnitude SCHEME-DEPENDENT (S116-W1-AS-CFB1; sudden↔adiabatic two-cluster, S116-W1-AS-CF3). So TRANSIT-PS-67's window-wide obligation is **bandwidth ∧ tilt ∧ amplitude-scheme** — three sub-conditions. This does not change the address (TRANSIT-PS-67, converged); it sizes the burden honestly.

### EMERGENCE

**The emergent product is the two-part flatness falsifier — neither agent's R1 had it.** Q-M1 ("homogeneity ≠ flatness; name the k-selector") × Q-V4 ("the acoustic-PG metric is flat-sliced") compose into a sharp, parameter-free gate that is the substrate-native replacement for the retired `3.1`:

> **Flatness falsifier (two-part):** PASS iff the a_2 Seeley-DeWitt emergent 3-metric (i) is acoustic/PG-form (admits the substrate-rest-frame preferred foliation, slices Ω²δ_ij) AND (ii) carries a spatially-UNIFORM conformal prefactor ρ/c in that foliation under the homogeneous global-modulus state ⇒ `R^(3) = 0` ⇒ `Ω_k = 0` EXACT vs Planck `0.0007 ± 0.0019`. FAIL iff the prefactor spatially varies in the homogeneous state (conformally-flat-but-curved, k≠0). No curvature knob.

This is the durable structural output: a category-C e-fold COUNT (`3.1`, retired) is replaced by two parameter-free substrate falsifiers — (i) `Ω_k = 0` from the two-part a_2-acoustic-form gate; (ii) window-wide tilt from TRANSIT-PS-67 (bandwidth ∧ tilt ∧ amplitude over 9.21 e-folds of k, transported 54.04 decades at deg +2). The horizon obligation is DISCHARGED (acoustic white hole, S85). The framework's observational obligations are not weakened by retiring `3.1`; they are RELOCATED onto the two gates that can compute them and SHARPENED (no-knob ⇒ tighter). The verdict on the e-fold question: **`gap_to_3.1` is DISSOLVED as the e-fold COUNT and REAL / DEFERRED / FALSIFIABLE as the two obligations it proxied.**

**One IS-not-IN calibration mints from this (effected below, corpus + framing-rule pointer).** The category A/B/C distinction — a substrate pin (governed by `substrate-first-canonical-sourcing.md §(i)`) vs an observational datum (governed by falsification) vs a competing-mechanism internal intermediate (governed by nothing — it does not transfer) — is a permanent sharpening of the IS-not-IN mandate: a number internal to a COMPETING framework's machinery (inflation's e-fold dilution budget) is neither a substrate pin to re-source NOR a container datum to test against; it is a third thing that simply does not cross the bridge.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Horizon vs flatness decomposition | V1, Re:V1, DISSENT(1) | **Converged** (+ Emerged sub-result) | Horizon → acoustic white-hole sealing (DISCHARGED, e-fold-free, lab-realized `09_2005`); flatness → a_2 emergent-geometry (OPEN); scale-range → TRANSIT-PS-67 (OPEN); NEITHER → e-folds. The `3.1` silently conflated horizon+flatness. **Emerged**: the flatness k-selector is NOT "acoustic-form" alone (conformal-flatness admits k=±1) but acoustic-form ∧ uniform-conformal-factor ρ/c in the preferred foliation ⇒ a sharp TWO-part gate. |
| 2 | N_e substrate-IS vs container import | V2, Re:V2, CONVERGENCE(1) | **Converged** (via Emerged A/B/C taxonomy) | `N_e^acoustic = 2.8913` is genuinely substrate-IS (S53 Eq.15B, from ρ(τ), c_s(τ)) — KEPT, no threshold attached. `N_e^geom = 0.1734` is a Layer-3 container diagnostic (ln a_f/a_i), BC-invariant. `3.1` is a **category-C** competing-mechanism (inflation-dilution) intermediate — retired. Observational data (`Ω_k`, `n_s`, k-window) is **category-B** and BINDS. `substrate-first-canonical-sourcing.md §(i)` governs neither (volovik's V2 citation WITHDRAWN). |
| 3 | gap_to_3.1 — real liability vs dissolved category error | V3, M1, M2, EMERGENCE | **Emerged** | The "dissolved vs real" binary was itself a category error. `3.1`-the-COUNT DISSOLVES (category C, non-transferring — no instrument measures `N_e ≥ 3.1`); the OBLIGATIONS it proxied are REAL, DEFERRED, FALSIFIABLE (category B). **Verdict: "dissolved as the count, real as the obligations."** Scorecard 1-of-3 discharged / 2-of-3 open; the two open entries are now parameter-free (no-knob ⇒ retiring `3.1` TIGHTENS the falsifier surface). |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

These are the substrate-native gates the retired `3.1` relocates onto — computation-specific, with pre-registered thresholds. (OQ-1 and OQ-2 are minted as Carry-Forward Computations below; OQ-3 is the residual epistemic question on the discharged horizon.)

1. **OQ-1 — the two-part a_2-Ω_k flatness gate.** Is the a_2 Seeley-DeWitt emergent 3-metric (a) acoustic/PG-form (admits a substrate-rest-frame preferred foliation, slices Ω²δ_ij) AND (b) carrying a spatially-UNIFORM conformal prefactor ρ/c in that foliation under the homogeneous global-modulus (τ uniform) state? **Pre-registered gate:** PASS iff `R^(3)[a_2 slice] = 0` (k=0) to numerical tolerance in the preferred foliation ⇒ `Ω_k = 0` EXACT vs Planck `0.0007 ± 0.0019`; FAIL iff the prefactor spatially varies in the homogeneous state (conformally-flat-but-curved, k≠0). Parameter-free (no curvature knob). → `CF-S117-A2-OMEGAK-ACOUSTIC-FORM`.

2. **OQ-2 — TRANSIT-PS-67 window-wide bandwidth ∧ tilt ∧ amplitude.** Does `|β(k)|²` (sudden Mach-13.75 quench, S70), transported through `T_{BZ→pivot}` (54.04 decades, deg +2), (i) SPAN `k ∈ [10⁻⁴, 1] Mpc⁻¹` (9.21 = ln 10⁴ e-folds of k) AND (ii) HOLD `n_s = 0.9649 ± 0.0042` window-wide (not merely pivot-local `α_s < 0.015`) AND (iii) reconcile the amplitude scheme (squeeze `A_s = 1.5367×10⁻⁸`, OOM band `[+0.196, +1.527]`)? **Pre-registered gate:** PASS iff the transported band holds `|n_s(k) − 0.9649| ≤ 3σ` across the full window AND spans 9.21 e-folds of k; FAIL iff the band curves away within the window OR fails to span it. Pivot-local `α_s` is NECESSARY, not sufficient. → `CF-S117-TRANSIT-PS-67-WINDOW-WIDE` (TRANSIT-PS-67 CRITICAL).

3. **OQ-3 — is the inherited-homogeneity IC a posit or derived?** The horizon discharge rests on inherited global-modulus homogeneity (the round SU(3) at τ=0, the SAME fiber over every M4 point). This is the substrate's analog of inflation's smooth-starting-patch assumption — structurally CHEAPER (a single global modulus carries no spatial d.o.f. to be inhomogeneous, so there is strictly less to assume) but still an initial-condition POSIT. **Open:** is the undeformed SU(3) DYNAMICALLY selected as the unique/attractor initial state (e.g., via the maximal-degeneracy / maximal-internal-entropy argument hawking flagged in the BC-fork, `hawking-collab §1.2`), or assumed? Lower priority (horizon is discharged on the COUNT regardless); this is the residual IC-honesty question, not an e-fold gate.

## Wrap-Up — Workshop Impact Summary

### What Changed

#### (a) Numerical revisions

- `gap_to_3.1 = 2.9266` (BC layer; S116-W6-WDW-IC-REFINE) and `3.1 − 2.8913 = 0.2087` (acoustic layer, ≈6.7%) → **RETIRED as falsifier metrics**. They measure the offset between a substrate quantity and a category-C inflation-internal number; neither is a substrate deficit.
- Acoustic-flatness suppression quantified (Re:V1, Sage-verified): `e^{−2·2.8913} = 3.08×10⁻³` (−2.51 OOM) vs the ~52 OOM (`e^{−120}`) a generic `O(1)`-start dilution would need ⇒ the acoustic e-fold budget is **~49.6 OOM short** as a flatness instrument, OR exactly **0 e-folds needed** if a_2 is flat-by-construction. `3.1` carries ZERO flatness content either way.
- Scale-range bandwidth quantified: **9.21 = ln(10⁴) e-folds of k** over `k ∈ [10⁻⁴, 1] Mpc⁻¹`, transported **54.04 decades** at **deg +2** (`T_{BZ→pivot}`, S116-W1-AS-CF3).
- Amplitude axis sized: squeeze `A_s = 1.5367×10⁻⁸`, OOM `+0.864`, band `[+0.196, +1.527]`, magnitude SCHEME-DEPENDENT (S116-W1-AS-CFB1) — a live, unsettled sub-condition of the scale-range obligation.

#### (b) Structural changes

- **`3.1` e-fold ENCODING retired** → reclassified from "binding WDW-IC gate" to a **category-C competing-mechanism (inflation-dilution) intermediate** that does NOT transfer. New anatomy: the **A/B/C taxonomy** — (A) substrate pin [`substrate-first-canonical-sourcing.md §(i)`], (B) observational datum [falsification], (C) competing-mechanism internal intermediate [governed by nothing; does not cross the bridge]. `3.1` is (C); the obligations are (B).
- **Obligations transferred from ONE e-fold count to TWO parameter-free substrate falsifiers**: flatness → a_2-Ω_k=0 (two-part gate); scale-range → TRANSIT-PS-67 window-wide bandwidth ∧ tilt ∧ amplitude.
- **Flatness k-selector identified AND sharpened**: NOT "acoustic-form" (conformal-flatness admits k=±1; S³ and H³ are both conformally flat) but **acoustic-form ∧ uniform conformal factor ρ/c in the preferred foliation**. A soft one-part gate ("is a_2 acoustic-form?") → a sharp two-part gate (acoustic-form ∧ uniform-ρ/c ⇒ R^(3)=0 ⇒ k=0 EXACT).
- **Horizon: requirement → DISCHARGED mechanism** (epistemic-type promotion): acoustic white-hole sealing (`|v|=c`, Mach 13.75), PROVEN S85, lab-realized (Rolley et al. `09_2005`; 3He-A PG `27_2003`). No e-fold count enters the sealing condition.
- **`substrate-first-canonical-sourcing.md §(i)` misapplication corrected** (volovik withdrew his V2 citation): an observational constraint is a **category-B external datum the framework is TESTED against**, never a "forbidden container import." Reclassifying observational bounds as imports would make the framework unfalsifiable by construction — the failure mode `epistemic-discipline.md` exists to block. Loophole closed.

### What Holds

- `N_e^acoustic = 2.8913` is genuinely substrate-IS (S53 Eq.15B, from ρ(τ), c_s(τ); the Landau–Khalatnikov two-fluid variables) — KEPT as a substrate observable, with NO inflation threshold attached. Not demoted.
- `N_e^geom = 0.1734` is BC-invariant (S116-W6-WDW-IC-REFINE: `N_e_BC^HH = N_e_BC^Vil = 0.1734`, `BC-invariance = 0.00e+00`), settled by the S-4 HH-UNCONDITIONAL upstream — the BC-layer e-fold residual is closed.
- **Horizon DISCHARGED** (acoustic white hole, PROVEN S85, lab-realized). The capstone `§6.2` narrates this correctly at PROVEN (`phonic-exflation-equation.md:422`) — no down-tag.
- The three observational FACTS bind regardless of mechanism (category B): full-sky `ΔT/T ~ 10⁻⁵`; `Ω_k = 0.0007 ± 0.0019` (`|Ω_k| ≲ 0.005`); broadband near-scale-invariant `P(k)` over ~4 k-decades at `n_s = 0.9649 ± 0.0042`.

### What Breaks or Strains

- **Scale-range is OPEN / CRITICAL.** What FALSIFIES: if TRANSIT-PS-67's transported `|β(k)|²` band fails to span 9.21 e-folds of k at `n_s = 0.9649 ± 0.0042` window-wide (a band that holds near-scale-invariance at the pivot but curves away within 1–2 decades), the framework is FALSIFIED — parameter-free, no knob to absorb the shortfall. The obligation is **bandwidth ∧ tilt ∧ amplitude-scheme** (three sub-conditions); the amplitude axis additionally strains (A_s magnitude SCHEME-DEPENDENT, OOM band `[+0.196, +1.527]`, sudden↔adiabatic two-cluster, S116-W1-AS-CF3 PLURALISM CONFIRMED).
- **Flatness is OPEN.** What FALSIFIES: if the a_2 emergent metric is acoustic-form but its conformal prefactor ρ/c is spatially NON-uniform in the homogeneous global-modulus state (conformally-flat-but-CURVED), then k≠0 ⇒ `Ω_k ≠ 0` ⇒ FALSIFIED vs Planck `0.0007 ± 0.0019`. The TWO-part gate is the sharp test; "is a_2 acoustic-form?" alone is **too soft** (conformal-flatness admits k=±1).
- **The inherited-homogeneity IC-posit** is the residual strain on the (otherwise discharged) horizon: cheaper than inflation's smooth-patch assumption (a single global modulus carries no spatial d.o.f.) but still assumed, not derived (OQ-3). Horizon is e-fold-free; it is not assumption-free.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

> NEW computes minted by this workshop. NOT relisting already-minted CF-S117 items (`CF-S117-Q45` operator-canonicity [mooted by S-4 HH-UNCONDITIONAL], `CF-S117-MODULUS-A4-GRADIENT` [the W4 modulus δ — SEPARATE mechanism, do NOT conflate], `CF-S117-FREESTREAM-AT-ANCHOR`, `CF-S117-conditional` A_s N-gap, `CF-S117-STATEPROJ-SC-FROM-SUBSTRATE`, `CF-S117-LEGGETT-COLLECTIVE-CEILING`).

1. **`CF-S117-A2-OMEGAK-ACOUSTIC-FORM`** — the two-part flatness gate (the substrate-native replacement for the retired `3.1`, flatness half).
   - **What**: Compute `R^(3)` of the a_2 Seeley-DeWitt emergent 3-metric in the substrate's preferred (rest-frame / Painlevé) foliation, under the homogeneous global-modulus (τ uniform) state; test the two-part gate — (a) a_2 metric is acoustic/PG-form (admits the preferred foliation, slices Ω²δ_ij) AND (b) the conformal prefactor ρ/c is spatially UNIFORM in that foliation ⇒ `Ω_k`.
   - **Inputs**: the a_2 Seeley-DeWitt coefficient of the spectral action (`phononic-framing.md` "g_M from a_2"; capstone `§6.2` `g_M` = a_2-emergent tensor cone); the acoustic-metric conformal factor ρ/c (Volovik `01_2001` Eq.13 `mn/c`; `27_2003` Eq.1 PG); D_K(τ) spectrum cache at τ_fold = 0.190; the inv11 minisuperspace single-global-τ homogeneous state.
   - **Gate**: PASS iff `R^(3) = 0` (k=0) to numerical tolerance in the preferred foliation ⇒ `Ω_k = 0` EXACT vs Planck `0.0007 ± 0.0019` (`|Ω_k| ≲ 0.005`); FAIL iff the prefactor spatially varies in the homogeneous state (k≠0). Parameter-free (no curvature knob).
   - **Effort**: 1 wave-equivalent (spectral-geometry compute — a_2 curvature extraction + conformal-factor-uniformity check; GPU-eligible if it touches the L_max=12 D_K cache).

2. **`CF-S117-TRANSIT-PS-67-WINDOW-WIDE`** — the window-wide scale-range gate (the substrate-native replacement for the retired `3.1`, scale-range half; the window-wide specialization of the existing TRANSIT-PS-67 CRITICAL gate).
   - **What**: Compute `|β(k)|²` (sudden/impulsive Mach-13.75 quench, S70 sudden-approximation), transport through `T_{BZ→pivot}` (54.04 decades, deg +2), and test window-wide near-scale-invariance + bandwidth + amplitude over the observed window.
   - **Inputs**: the GGE Bogoliubov spectrum `β(k)` through the fold (TRANSIT-PS-67; `baseline-findings-s66`); the `T_{BZ→pivot}` transport map (deg +2; S116-W1-AS-CF3 `audit_sha256=c34cadf322bf84aa823a85cd2f207aad6b47505b9ea9f3271b95ee6085b21f98`); the squeeze `A_s = 1.5367×10⁻⁸` + OOM band `[+0.196, +1.527]` (S116-W1-AS-CFB1 `audit_sha256=f44a7b4279d4227db9a7b2c755238c9c2bd256b93c88f5bcf87ae78b8264b3ec`); n_s scheme-split (sqrt-cutoff 0.9590 / framework 0.9561).
   - **Gate**: PASS iff transported `|β(k)|²` (i) SPANS `k ∈ [10⁻⁴, 1] Mpc⁻¹` (9.21 e-folds of k) AND (ii) holds `|n_s(k) − 0.9649| ≤ 3·0.0042` window-wide AND (iii) amplitude-scheme reconciled within the OOM band; FAIL iff the band curves away within the window OR fails to span 9.21 e-folds. Pivot-local `α_s < 0.015` is NECESSARY, not sufficient.
   - **Effort**: 1–2 wave-equivalents (Bogoliubov spectrum through the fold + deg-+2 transport + window-wide tilt fit).
   - **Depends on**: TRANSIT-PS-67 (CRITICAL, OPEN); the deg-+2 transport map (S116-W1-AS-CF3); the A_s amplitude-scheme axis (S116-W1, `CF-S117-conditional` adjacency — distinct gate, shared amplitude input).

### Effected In-Session (NON-MATH — completed by the final agent BEFORE TERMINATING)

Every non-math item this workshop surfaced, executed with a concrete edit (no deferrals):

- [x] **§7 falsifier-surface / `falsifier-master-inventory.md`** — **Row #93 landed** (`sessions/framework/registry/falsifier-master-inventory.md:2616`; re-indexed, `summary_rows=26`). The exflation horizon/flatness/scale-range obligation-cluster registration: RETIRES `N_e ≥ 3.1` as a category-C inflation-dilution intermediate; registers the TWO parameter-free substrate falsifiers (the two-part a_2-Ω_k=0 flatness gate; TRANSIT-PS-67 window-wide tilt). **Headline = the SCORECARD** (1-of-3 discharged / 2-of-3 open-parameter-free), per the Q-V5 refinement. RETAIN-and-append pattern (no existing row edited); **NO new `canonical_constants` value** (workshop artifact-existence closure; the two falsifiers are OPEN forward CF-S117 gates — Step 2 N/A). mack-cosmic-bridge sole-writer domain (`feedback_mack-bridge-role.md`).

- [x] **IS-not-IN calibration corpus entry** — **`cross-pillar-bridge-corpus.md §29` landed** (`sessions/framework/registry/cross-pillar-bridge-corpus.md:2089`; re-indexed). The A/B/C category distinction — (A) substrate pin / (B) observational datum / (C) competing-mechanism internal intermediate — with the K=1 instance = the `N_e ≥ 3.1` count (category C, non-transferring). Per `feedback_rules-directive-only-no-session-info.md`, the per-instance narrative lives in the CORPUS (not the rule body); the companion `phononic-framing.md §"IS Space, Not IN Space"` pointer is recorded FROM the corpus side (§29 declares it). The rule-body bare pointer is **orchestrator-only** — subagent writes to `.claude/rules/` are harness-blocked, and the routing convention names the corpus AS the destination (not a fallback). Substantive calibration EFFECTED; only the optional rule-body cross-link is orchestrator-scoped (flagged in the completion note, NOT a deferral).

- [x] **Capstone-hygiene 5-question check** (run S116 W-3, per `.claude/rules/capstone-hygiene-gate.md`):
  - **Q1 (a(t)/effective-Friedmann gap)** — **NO**. The workshop reframes the e-fold COUNT as non-binding but does NOT alter the §6.3 a(t)/effective-Friedmann gap status; `N_e^geom = 0.1734` is settled (BC-invariant, S-4 HH-UNCONDITIONAL). The flatness obligation routes to the a_2-emergent metric (adjacent) as a NEW §7 falsifier entry (Q2), not an a(t)-gap status change.
  - **Q2 (§7 falsifier-anchor row)** — **YES, FIRES**. Two new §7 falsifier candidates + the `3.1` retag → routed to mack-cosmic-bridge sole writer → **Row #93** (effected above, `falsifier-master-inventory.md:2616`). In-session designated-writer fix (housekeeping §A-equivalent; not deferred).
  - **Q3 (PROVEN/CONDITIONAL/BROKEN/INFO status change)** — **NO**. Horizon stays PROVEN (workshop CONFIRMS S85). The capstone `§6.2` narrates horizon at PROVEN (`phonic-exflation-equation.md:422`) — no over-confident claim to down-tag. No capstone claim asserts an e-fold count, flatness, or `Ω_k` at a confidence the register doesn't support (the flatness/scale-range obligations are NEW OPEN entries, not pre-existing capstone claims).
  - **Q4 (PROSE claim vs ledger row)** — **NO** (capstone prose). The change is a §7 falsifier-TABLE / inventory entry + a registry corpus entry (registry rows), NOT a capstone PROSE claim. The capstone horizon prose (`:422`) is already correct; no designated-writer capstone-prose patch is owed.
  - **Q5 (citation add/invalidate in capstone)** — **NO**. No capstone citation added or invalidated. The acoustic-PG flat-slicing argument (Volovik `27_2003`/`01_2001`) is a workshop-internal + Row #93 citation; it does not enter the capstone in this hygiene pass.
  - **Routing**: the single firing question (Q2) is effected in-session via Row #93 (designated-writer fix, not a compute carry-forward). Check recorded.

### Closing Line

The `3.1` was never a substrate datum — it is inflation's bookkeeping for how dilution buys horizon and flatness, a category-C number that no instrument reads and that does not cross into a framework which counts no e-folds. Retiring it costs nothing and buys precision: the real obligations it badly proxied — `Ω_k = 0` from the two-part a_2-acoustic-form gate, window-wide `n_s` from TRANSIT-PS-67 — are parameter-free substrate predictions with no knob to absorb a shortfall, so dropping the number TIGHTENS the falsifier surface rather than loosening it. Horizon is discharged (the substrate seals its own causal horizon supersonically, in the lab as in the cosmos); flatness and scale-range are open, deferred, and sharply falsifiable. The substrate IS the spatial sections and IS the power spectrum; what the e-fold count measured was only the shadow they cast on an FRW container the substrate never lived in.
