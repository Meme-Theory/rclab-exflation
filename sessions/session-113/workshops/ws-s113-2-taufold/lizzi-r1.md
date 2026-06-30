# WS-S113-2 TAUFOLD — Round 1

**Workshop**: WS-S112-2 TAUFOLD (Session 113 EVOI-frontier campaign; schedule `sessions/session-112/session-112-workshop-schedule.md` lines 33–42)
**Author**: `lizzi-spectral-functional-theorist` — Round 1, steelman **Reading B** (τ_fold is an irreducible empirical modulus the action cannot select)
**Opponent**: `transit-dynamics-theorist`, holding Reading A (a dynamical mechanism-chain selects τ_fold). Not yet seen.

**One-line thesis**: The spectral action selects a modulus *if and only if* that modulus is an interior stationary point of the action; t=1/2 is one (`u′(1/2)=0`, grade-by-grade, f-independent), τ_fold structurally is NOT (the action is strictly monotone in τ — `dS/dτ=+58,673>0`, 9,600/9,600, for ALL f) — so τ_fold is not action-selectable in any spectral functional, and the honest move is to accept it as one empirical input, completing the dimensional-input set alongside the M_KK magnitude (which S112 W1 just closed as a permanent external import).

---

## 0. The question, stated as a spectral-functional question

The tension is usually phrased "one modulus the action closes (t), one it does not (τ_fold) — is the τ_fold non-closure permanent?" My domain owns the first half of that sentence: *what does it mean for "the action" to "close" a modulus, and is that verb functional-dependent?*

The spectral action is a one-real-parameter family, not a single object:

```
S_f(D_K) = Tr f(D_K²/Λ²),    f ∈ {cutoff f(x)=√x, exp(−x), …},   zeta:  S_ζ = ζ_{D_K}(0) = a_4,   anomaly-derived: f_0 forced = 1/2
```

My standing methodology (arXiv:1412.4669; 1103.0478; 1001.2036): a prediction is **structural** iff it survives every choice of f, and **scheme-dependent** iff it changes with f. The cosmological constant is the canonical scheme-dependent quantity — a_0 enters S_cutoff but is *absent* from S_ζ = a_4. So before I can say "the action closes/doesn't close τ_fold," I must check whether that statement is f-independent. **It is** — and that is the spine of the Reading-B case. Both the t-closure and the τ_fold non-closure are functional-INDEPENDENT structural facts, so no change of spectral functional can convert τ_fold non-selection into selection.

---

## 1. WHY the action closes t=1/2 — and the verb is "extremize"

The S101 W1-1 result `S101-TAU0-OPERATOR-CANONICITY` PASS (audit `194b2b3c`; EVOI row 4b) is precise about the mechanism. The substrate framing of that gate (session-101-plan-w1.md lines 339–351) reads, verbatim:

> "at genesis the substrate's own action functional closes the residual modulus: **dS/dσ = 0 exactly at the gravity AND Yang-Mills grades for every τ, grade-by-grade and hence f-independently**. … This is the framework's first CLOSED operator modulus (vs τ_fold, which the action does NOT close — S95 pair)."

Decompose what "closes" means here. The Lai-Teh operator-fan opens a one-parameter `t` direction at the bi-invariant point (the Olmos-Reggiani five-fold degeneration locus). The spectral action, graded into its torsion weights A_6/A_4/A_2 (twist-powers of the torsion weight `u(t)`), is **stationary** at t=1/2:

- `u′(1/2) = 0` — Sage-symbolic, computed not narrated (the S101 PASS criterion L2: `dA_k/dt|_{t=1/2}=0` for k∈{6,4,2} as EXACT symbolic zeros).
- Verified this round (Sage, `u(t)=t(1−t)` the symmetric bi-invariant torsion weight): `u′(t)=−2t+1`, root `t=1/2` (INTERIOR), `u″(1/2)=−2≠0` → a *genuine extremum*, not an inflection.
- The stationarity is at the **gravity AND Yang-Mills grades simultaneously**, **grade-by-grade**, and therefore **f-independent** (S101 regulator_pin note: "FI at the stationarity-identity level: the two-grade stationarity is grade-by-grade and hence f-independent — no cutoff-function moments consumed in the PASS conjunction").

So the operation by which the action "closes" t is **extremization**: the action has an interior critical point in the t-direction, and the substrate's own action picks it out. This is exactly the operation a spectral action is *built to perform* — `S_f` is a functional whose stationary points are the physical configurations. When an interior stationary point exists, every reasonable f finds the same one (the stationarity is a grade-by-grade algebraic identity, not a moment-weighted competition).

**The t-closure is a FUNCTIONAL-INDEPENDENT structural selection. The action selects t=1/2 because an interior critical point EXISTS.**

---

## 2. WHY the action structurally CANNOT select τ_fold — the verb is "monotone-flow"

Now the τ-direction. Here the canonical result is the **Structural Monotonicity Theorem** (S37; baseline-findings-s66 W4; atlas-07 A2/W7):

> `⟨λ²⟩(τ)` increases **monotonically** under the volume-preserving Jensen deformation on SU(3). For **any monotone cutoff f**, `S_f(τ)` inherits monotonicity **sector-by-sector**. **ALL** monotone f, **ALL** Λ, **ALL** 10 sectors. **9,600/9,600 checks.** `dS/dτ = +58,673` at the fold.

And the decisive register consequence — atlas-04 assumption **S1**, "SA stabilizes tau at the fold", carries status **DISSOLVED**:

> "Structural monotonicity theorem: S_f(τ) monotonic for ALL smooth monotone cutoffs, ALL Lambda, ALL tau, ALL 10 sectors. 9,600/9,600 checks. **The question was reframed**: transit paradigm replaces static trapping."

This is not "we looked for a minimum and didn't find one yet." It is "a minimum **cannot exist**, because the function is provably strictly monotone." A strictly monotone function has **no interior stationary point** — verified this round (Sage): `dS/dτ=+58,673>0` ⇒ `dS/dτ=0` has the empty solution set on τ∈(0,∞).

The structural reason this is the *right* answer (and not a defect to be fixed) traces to atlas-04 **S3**: "**SA is a spectral moment, not a total energy.**" The spectral action's τ-content is `Tr f(D_K²/Λ²)` — a sum of cutoff-weighted eigenvalue moments. As the Jensen deformation stretches the spectrum, every monotone-weighted moment grows. There is nothing in a moment-sum to turn it around: a well requires a competition between a term that grows and a term that shrinks under τ, and the spectral action — being a single monotone functional of a monotonically-stretching spectrum — has only the growing term. (This is the same lesson as F.5 / atlas-04 S3: the SA even *penalizes* BCS pairing with the wrong sign, +12.76 anti-trapping — it is the wrong *kind* of functional to host a vacuum-selecting well; the condensation energy is a Fock-space quantity, categorically different.)

**The τ_fold non-closure is a FUNCTIONAL-INDEPENDENT structural fact. The action cannot select τ_fold because an interior critical point is ABSENT — for every monotone f.**

---

## 3. The asymmetry, stated cleanly (the heart of Reading B)

| | t-modulus | τ_fold-modulus |
|:--|:--|:--|
| Action's behavior in this direction | interior **stationary point** (`u′(1/2)=0`, `u″≠0`) | strictly **monotone** (`dS/dτ=+58,673>0`) |
| Selection operation | **extremize** → critical point FOUND | **flow** → no critical point to find |
| Functional dependence | f-INDEPENDENT (grade-by-grade identity) | f-INDEPENDENT (monotone for ALL f, 9,600/9,600) |
| Register status | RESOLVED (S101 W1-1, audit `194b2b3c`) | DISSOLVED (atlas-04 S1) — *question ill-posed* |
| What the action supplies | a **well** (a point) | a **slope** (a direction) |

The two are not "the action closed one and we haven't worked hard enough on the other." They are **two qualitatively different geometries of the same action in two different modulus directions**, both established to machine precision, both f-independent. A spectral action can only *select* where it has a stationary point. It has one in t; it provably has none in τ. **This exhausts the action's selective power over τ_fold — there is no further functional to try, because the absence is functional-independent.**

This is the most important thing my domain contributes: someone could reasonably hope that the τ_fold non-selection is an artifact of the cutoff choice (maybe S_ζ = a_4 has a well where S_cutoff does not?). It does not. Monotonicity holds for ALL monotone f, sector-by-sector; the zeta functional is built from the same monotonically-stretching moments. **The CC problem taught us a_0 is scheme-dependent; the τ_fold problem teaches us the *opposite* — the non-selection is scheme-robust.** You cannot regularize your way to a τ_fold selector.

---

## 4. The strongest threat — a dynamical attractor that lands on 0.190 with zero parameters — and why it relabels rather than selects

I must engage Reading A's best case honestly, not strawman it. The S95 FAILs (`T-STAR-ONELOOP-ORIGIN` FAIL, `NO-WELL-ONE-LOOP` PASS) closed the **equilibrium / variational** selectors — the one-loop effective potential and the fixed-point search. Reading A's live move is: the substrate is *non-equilibrium* (the whole transit paradigm), so τ is selected **dynamically** — a relaxation/transit mechanism-chain drives τ → 0.190 as an **attractor**, not as a potential minimum. If a substrate-fixed dynamical system flows to 0.190 with zero free parameters, that *would* be a genuine substrate selection and Reading B would lose. So I take it at full strength.

Here is why, from the spectral-action side, it does not escape the modulus problem — it **relocates** it:

**(a) A monotone potential gives an attractor only at a boundary, never at an interior 0.190.**
The only τ-potential the substrate supplies is the spectral action, and it is monotone. Gradient-type relaxation `τ̇ = −(1/γ) dS/dτ` with `dS/dτ>0` everywhere drives τ monotonically toward the *boundary* of moduli space (the round point τ=0 backward, or τ→∞ / the next degeneration locus forward) — it cannot have a fixed point at an interior value like 0.190, because a gradient flow's fixed points ARE the potential's stationary points, and there are none. The S110 WS-CLOCKLOC closure makes this concrete and *register-permanent*: the substrate-natural evolution equation is `τ̈ = −3Hτ̇ − (1/5)dV/dτ` with `dS/dτ=+58,673` **one-signed** (`S111-CF-CLOCKLOC1-CED` PASS, audit `7ac41f0397a1c64b`; CLOCKLOC2 monotone τ̇-corridor, `n_zero_corr=0`). A one-signed driving term on a monotone corridor does not manufacture an interior attractor.

**(b) So a transit endpoint at 0.190 must be set by a terminating condition imported from OUTSIDE the action.**
For the transit to *freeze* at τ=0.190 rather than run through it, something must stop the flow there — a freeze-out time, an impedance-matched transit endpoint, a quench timescale, an initial τ from which the impulsive transit lands at 0.190. Each of these is a perfectly good piece of physics, but each is an **initial/boundary datum**, not an output of the action. The attractor "basin" still has to be entered, and the stopping condition still has to be calibrated. **Reading A does not delete the free number; it changes its *type*** — from "a potential minimum the action selects" to "a transit initial/boundary condition the dynamics propagates." A boundary condition that must be externally set is exactly an empirical input. (This is the same structural move as `α_s`/Yukawa "selection" that turned out to be `O = w·Ô` with one un-fixed `w` — the rank-1 Normalization-Non-Universality theorem, §VII.BS STAGE-3-PERMANENT: the substrate fixes all the dimensionless *shape*, imports one dimensional *scale*. τ_fold is the modulus-space analog: the substrate fixes the transit *trajectory shape*, the endpoint *value* is imported.)

**(c) The burden of proof for Reading A is a pre-registrable, zero-parameter attractor — and it must produce 0.190 without using 0.190.**
This is the honest discriminator. For Reading A to WIN (not merely to be possible), it must exhibit a dynamical system whose coefficients are ALL substrate-fixed (no τ_fold-dependent input, no hand-tuned freeze-out time, no calibrated quench rate) and whose attractor is `τ* = 0.190 ± tolerance`. If any coefficient must be set to make the attractor land on 0.190, the mechanism has *relabeled* τ_fold as that coefficient, and Reading B stands. The pre-registrable gate is therefore: **build the substrate-natural relaxation ODE from `D_K`-data alone (the spectral-action slope + the WS-CLOCKLOC `(C,E,D)`-triple, zero continuous params), integrate it, and check whether `τ→0.190` emerges or whether 0.190 had to be injected as the stopping/initial datum.** My prediction (functional-independent): the dimensionless trajectory *shape* will be substrate-fixed and beautiful, and the *value* 0.190 will be traceable to an imported initial/boundary condition — a FAIL on the "zero-parameter attractor" criterion that confirms Reading B, exactly as the analogous a(t) program resolved (S101 W-2: dimensionless content derived, one dimensional scale imported).

---

## 5. The positive Reading-B deliverable — τ_fold is empirical, parallel to M_KK, and S112 just made that parallel exact

Reading B is not a counsel of despair; it is a **completion**. The framework's honest dimensional-input set is small and now nearly closed:

- **M_KK magnitude** — `CF-S112-MKK-SUBSTRATE-ANCHOR` FAIL (audit `3fa9be16…`), the keystone gate that RAN and FAILed *as the pre-registered permanent boundary*: both substrate-natural anchors reduce to `M_KK·(pure number)` because the substrate's spectral data are **dimensionless in M_KK units** (the self-referential-unit-system no-go; lattice-QCD scale-setting analog). The M_KK-magnitude leg is now a **CLOSED-PERMANENT external-import boundary** (atlas-04 C1; EVOI Tier-1 #1 sub-residual retired to §5; "irreducibly external, not a refinable approximation").
- **τ_fold value** — the modulus-space analog of exactly the same fact. The substrate's spectral data fix every *dimensionless ratio* and every *shape*; they do not fix this one *dimensionful-modulus location*, because the action that would select it is monotone (no interior stationary point), f-independently.

The structural parallel is not loose analogy — it is the **same N₃=0 / single-dimensional-handle wall** (S44; the rank-1 NNU topological cause) showing up in two places: once as the one mass scale the substrate cannot self-set (M_KK), once as the one modulus location the substrate cannot self-select (τ_fold). S112 W1 *just* certified the first as permanent-external via a clean no-go. **Reading B says: τ_fold is the second member of the same permanent-external set, and the honest capstone move is to narrate it as one empirical input — `τ_fold = 0.190`, matched from the DESI/ACT/CMB epoch (EMPIRICAL-τ_fold RETENTION, the ACTIVE default-fallback open channel, session-84-w8) — exactly as M_KK is narrated.** Input count: 3 master gears (dimensionless) + 2 external dimensional imports (M_KK scale, τ_fold modulus location). That is a *result*, not a gap: a precise, falsifiable statement of where the substrate's self-determination ends.

This also *sharpens* the framework rather than weakening it, in the §EVOI.BF sense: a pinned "τ_fold is empirical, like M_KK" honesty statement is the methodology-floor analog of the anti-rescue fence — it refuses to convention-shop a selector into existence, and it concentrates the framework's zero-parameter claims where they are real (the dimensionless shapes) instead of overclaiming a modulus selection the action provably cannot deliver.

---

## 6. The one place Reading B could lose (intellectual honesty)

I will not pretend the door is bolted. Reading B loses if Reading A produces **(i)** a substrate-fixed dynamical system **(ii)** with zero free/calibrated coefficients **(iii)** whose attractor is 0.190 **(iv)** where 0.190 is genuinely an *output*, not an injected stopping/initial datum. The monotonicity theorem forbids this for *gradient* dynamics on the *spectral action*, but it does NOT forbid it for a *non-gradient* dynamical system whose fixed point comes from a balance of terms NONE of which is the spectral-action slope — e.g., a transit where a Hubble-friction term `−3Hτ̇` balances a substrate-fixed source at a specific τ. That balance *could* in principle pin an interior τ* from substrate data alone. My structural prediction is that when that balance is written out (WS-CLOCKLOC `(C,E,D)`-triple, which IS non-gradient: `τ̈ = −3Hτ̇ − (1/5)dV/dτ`), the friction coefficient or the H-normalization will carry the same un-fixed dimensional scale (M_KK / the clock normalization `γ = dt/dτ = 29.7532`, S101 W4 `S101-W1-QEQ-RELIC-ODDFLOOR`) — relabeling, not selecting. But that is a *prediction*, and the pre-registrable gate in §4(c) is precisely the test that would adjudicate it. If that gate returns a zero-parameter 0.190, I concede.

---

## 7. (i) Honest current lean · (ii) single most decisive consideration

**(i) Current lean — Reading B, with ~0.8 confidence.** The decisive evidence is already on the books and is functional-independent: the spectral action is *provably strictly monotone* in τ (9,600/9,600, ALL f, ALL Λ, ALL sectors; atlas-04 S1 = DISSOLVED), so it has no interior stationary point in the τ-direction, so it cannot *select* τ_fold by the only operation a spectral action performs (extremization) — and this is true for every spectral functional, so no scheme change rescues it. The remaining ~0.2 is the genuine non-gradient-attractor threat of §6, which is not yet closed by computation. The asymmetry with t=1/2 is not a puzzle: t IS an interior critical point, τ_fold is NOT, both f-independently — the action selects exactly the moduli where it is stationary, and τ_fold is not one of them.

**(ii) Single most decisive consideration:** *Selection by an action means stationarity; the spectral action's τ-direction is strictly monotone (no stationary point) for every spectral functional, so τ_fold-selection is not merely unachieved but structurally absent in a functional-independent way.* The contrast with t=1/2 (`u′(1/2)=0`, an interior extremum the action DOES find) shows the framework's selector working exactly where it can and silent exactly where it cannot. The dynamical-selection route does not change this — it moves the unfixed number from "a missing potential minimum" to "an imported transit boundary condition," which is the definition of an empirical input. Therefore the honest, structural-confidence-maximizing verdict is: **τ_fold is an irreducible empirical modulus, the second member (with M_KK) of the framework's permanent external-dimensional-import set** — unless Reading A produces a pre-registered zero-parameter non-gradient attractor that outputs 0.190 without injecting it.

---

*End of Round 1 (lizzi-spectral-functional-theorist). No verdict written; opponent section not authored.*
