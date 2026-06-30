# WS-S112-1 KPIVOT — Round 1

**mack-cosmic-bridge — Round 1, steelman Reading B (external calibration)**

**One-line thesis:** K_pivot is NOT a substrate-derived bridge image; it is the framework's *second* protected dimensionful import — and the rank-1 normalization-non-universality wall (§VII.BS, N₃=0, STAGE-3-PERMANENT `d309efb4`) forbids a second independent dimensional handle, so K_pivot either reduces to M_KK by a substrate-computed *dimensionless* ratio R (inheriting M_KK's just-closed PERMANENT-external fate, S112 `3fa9be16`) or it is a genuine second handle the substrate cannot supply. The transport-degree machinery Reading A invokes lives in the *even morphism sector* and is parity-barred (§23.0(5)) from acting on the *odd `M_KK¹` scale-leg* where any dimensionful pivot must sit. Either way, the dimensionful number K_pivot is external.

---

## 0. What the registers actually say (queried first, per epistemic-discipline)

Before steelmanning, the canonical state — because three of these facts decide the workshop and two of them are traps:

| Object | Register status | Source (verified this session) |
|:--|:--|:--|
| **C2 `K_pivot = 2.0 M_KK`** | `BROKEN-WITH-LIVE-RESEARCH-PATHWAY` — "Never rigorously derived. SA-Goldstone mixing FAILS at K=2.0 (convex-combination theorem, S51)." | atlas-04 C2 (knowledge.db theorem entry, sourced S51) |
| **`deg_T_BZ_pivot = 2.0`** | canonical constant, "DERIVED ONCE on the M4 base"; S110 `S110-CF-CV6B-DS-M4`; the d_s spectral-dimension homogeneity exponent | `get_constant(deg_T_BZ_pivot)`; canonical_constants.py:716 |
| **§VII.BS Normalization-Non-Universality** | STAGE-3-PERMANENT, audit `d309efb4`; clause (a) rank-1 covariance ("one scale → \|Corr\|=1; two scales → rank 2"), clause (b) N₃=0 → single-cutoff count | `trace_entity(normalization-non-universality)`; permanent-results-registry §VII.BS |
| **`CF-S112-MKK-SUBSTRATE-ANCHOR`** | FAIL `3fa9be16` — M_KK magnitude is a **CLOSED-PERMANENT external-import boundary** (self-referential-unit no-go; lattice-QCD scale-setting analog) | atlas-04 C1 (S112 freshness, line 13); evoi-framework §5 |
| **§23.0(5) parity selection rule** | SUGGESTION K=2; `d_A=0` ⇒ even morphism sector (transport works); `d_A=odd` ⇒ sign-locked `M_KK¹` scale leg, no even morphism can correct it | cross-pillar-bridge-corpus §23.0(5), S110 W4 connes×mack |
| **`BF_spine_vs_incumbent_ceiling = 31.62`** | canonical; incumbent-discrimination "structurally ceilinged at very-strong (31.62), unliftable by adding observables; EVOI concentrated entirely in the M_KK-derivation" | `get_constant`; S101 BF-spine workshop |

**TRAP 1 (the one that decides the workshop):** the `deg(T)=2.0` that EXISTS and is DERIVED is the homogeneity exponent of a **dimensionless** observable (the M4 heat-trace spectral dimension d_s; `d_A=0`). It is NOT a map that lands a dimensionful K* at 0.087 M_KK. Reading A's strongest move is to point at this derived `deg(T)` and say "the transport degree is computable." It is — but for the wrong dimensional class. §23.0(5) makes this precise and I build my whole case on it (§3).

**TRAP 2:** the C2 cell records a **three-way K-anchor distinction** (S110 W0 HK-DS, line 11): `K_pivot≈2.0` (SEED, BROKEN) / `K_star=1.3130` (lab) / **`K*=0.087` (SA-Goldstone)**; only `k_pivot_planck=0.05 Mpc⁻¹` is canonical. The "intermediate K* = 0.087 where n_s=0.965 works" has **"no physical mechanism"** placing it there (C2 row). The physical e-fold mapping gives `K = 4.3e-57 M_KK` (flat, n_s=1). So even the *number* Reading A would need to derive is not 2.0 — it is the empirically-back-solved 0.0435·M_KK, and that one has no derivation at all.

---

## 1. The structural parallel to the just-closed M_KK no-go (the spine of Reading B)

S112 W1 just closed the single largest gap on the C1 axis. The shape of that closure is the template for K_pivot.

**What S112 proved.** `CF-S112-MKK-SUBSTRATE-ANCHOR` (FAIL `3fa9be16`) attempted to fix the *magnitude* of M_KK from substrate data via two substrate-natural anchors (Δ_BCS·M_KK and √(a₂^ζ/48π²)·M_KK). Both **reduced to M_KK·(pure number)** because the substrate's spectral data are *dimensionless in M_KK units*. This is the self-referential-unit-system no-go: you cannot bootstrap the unit you measure everything in *out of* quantities already expressed in that unit. The lattice-QCD scale-setting analog is exact — you set `a` (lattice spacing) by ONE external input (a measured hadron mass); everything else is then a dimensionless ratio. The substrate determines the conformal class + all dimensionless dynamical shapes from **zero continuous parameters**; exactly ONE dimensionful scale is imported.

**Why this is a wall, not a gap.** §VII.BS clause (a) (the rank-1 covariance theorem, JOINT volovik+phonon-first, Sage-proven) states it cleanly: *one scale → an all-ones-up-to-sign log-Jacobian column → |Corr|=1 (rank 1); two scales → rank 2.* Clause (b): N₃=0 → BDI single-cutoff COUNT. The topological cause is N₃=0/BDI (S44). **The substrate is entitled to exactly ONE imported dimensionful scale**, the way GR is entitled to exactly one (G, or equivalently the meter). This is not a deficiency to be repaired by more cleverness; it is a feature of a background-independent spectral geometry (the S110 WS-CC-H₀ "constructive-O3" reading: the rank-1 `w = M_KK` is the framework's G-analog).

**The transfer to K_pivot.** Now ask: what *kind* of object is K_pivot? It is a **dimensionful wavenumber** — units of Mpc⁻¹, or equivalently `R · M_KK` for some number R (in natural units, `K_pivot = 2.0 M_KK` literally writes it as `R=2.0` times the one external scale). Two exhaustive cases:

- **Case A — K_pivot is `R · M_KK` with R a substrate-computed dimensionless ratio.** Then K_pivot is NOT an independent handle; it inherits M_KK's fate *exactly*. The moment M_KK is fixed (externally, permanently, per S112), K_pivot is fixed *too* — but only because M_KK was. There is no *additional* substrate content fixing the pivot beyond what already fixed M_KK. **K_pivot is external because M_KK is external.** This is the benign case for Reading A's "it's derived" claim *only if R itself is derived* — and §2 shows R is precisely the thing that is NOT derived (R=2.0 gives n_s=1; the working R=0.0435 has no mechanism).

- **Case B — K_pivot carries dimensional content NOT reducible to M_KK** (i.e., a genuinely second physical scale entering the CMB-pivot map — a comoving horizon scale, a transit-epoch sound-horizon, an absolute e-fold count). Then K_pivot is a **second independent dimensional handle**. By §VII.BS clause (a), a second scale forces the covariance rank from 1 to 2 — **directly contradicting the STAGE-3-PERMANENT N₃=0 rank-1 theorem.** This case is *foreclosed by a permanent wall.*

**Either branch lands on Reading B.** In Case A the dimensionful pivot is external (it is M_KK in disguise, and M_KK is permanently external). In Case B the dimensionful pivot is forbidden as substrate-derived (it would be a second handle the rank-1 theorem prohibits). The substrate fixes the *dimensionless ratio* R if and only if a mechanism exists; it never fixes the *dimensionful* K_pivot independently. That is the definition of an irreducible external calibration for the dimensionful pivot.

---

## 2. The number itself is not derived — the C2 "live pathway" has been searched and is empty

Reading A needs a substrate-natural mechanism that lands the *working* pivot. The register says, flatly, there is none. I make the three numbers explicit because they are the falsification of "live pathway = derivable":

```
Mechanism                         →  K (in M_KK)     →  n_s          status
-------------------------------------------------------------------------------
Tessellation (BZ, K=2 M_KK)       →  2.0             →  ~1 (flat)    BROKEN: SA-Goldstone
                                                                      mixing FAILS at K=2.0
                                                                      (convex-comb. thm, S51)
Physical e-fold mapping           →  4.3e-57         →  1 (flat)     no spectral tilt at all
SA-Goldstone working point K*     →  0.0435 (=0.087  →  0.965 ✓      "No physical mechanism
                                     /2.0)               (margin       places K at the
                                                          0.2 e-fold)  intermediate K*"  (C2)
```

The structure here is the *opposite* of a derivation. The two scales the substrate *can* point at (the BZ tessellation scale K=2 and the physical e-fold scale K=4.3e-57) both give a **flat spectrum** (n_s=1), which is *ruled out* by Planck at enormous significance. The ONE value that reproduces n_s=0.965 (K*=0.0435·M_KK) is reached by **back-solving from the answer** — it is an empirical fit to Planck, fenced off from any substrate mechanism by 54+ decades on one side and a failed convex-combination theorem on the other. This is the textbook signature of an external calibration: the dimensionful anchor is whatever observation requires, and no first-principles computation reaches it.

This is *also* why C3 (n_s) is tagged `BROKEN-WITH-α_s-IDENTITY-PROMOTION`: the substrate-internal result that survived is the **dimensionless** identity α_s = n_s²−1 (a relation between two *tilts*, both `d_A=0`), promoted STAGE-3-PERMANENT (§VII.X.1). The substrate gives you the *shape relation* between dimensionless tilts; it does not give you the *scale* at which to read them off. That is the same rank-1 dimensionless/dimensionful split as M_KK, one register row over.

---

## 3. The strongest threat to my pole, met head-on: the parity selection rule

Reading A's best weapon is the one genuinely-derived transport degree: `deg_T_BZ_pivot = 2.0`, minted S110 W3 on the M4 base, "DERIVED ONCE." If the substrate computes a transport degree across the 54-decade BZ→pivot gap, why can't that *same* degree carry the pivot scale itself? I have to defeat this on the math, not by assertion. The §23.0(5) parity selection rule (S110 W4 connes×mack, the workshop *immediately downstream* of the `deg_T=2.0` mint, which exists *precisely because* an agent tried to import that degree onto a dimensionful observable and it was caught) does exactly that:

**The composite bridge map factors by dimensional class:**
```
B = (M_KK^{d_A} scale leg)  ⊙  (dimensionless structural morphism)
                                with admissibility deg(B) = d_A  (§18.0 Conjunct-1, Wodzicki-unique)
```

- **`d_A = 0` (dimensionless: n_s, α_s, n_T, d_s, ΔH₀/H₀):** scale leg is `M_KK⁰ = 1` (trivial); the entire transport degree lives in the **dimensionless morphism**, which is **EVEN** (a same-class Wodzicki two-pole ratio has `deg = −2(s−s') ∈ {…,−4,−2,0,+2,…}`; an HKR cohomology-class ratio has `deg = 0`). The `deg_T=2.0` that EXISTS is exactly this: `+2 = +d/2` of the M4 heat-trace amplitude, a *morphism degree* of a *dimensionless* d_s. **This is why the framework's transport successes (n_s scalar, n_T non-scalar, α_s `deg=+2`) all sit at even degree.**

- **`d_A = +1` (dimensionful: T, H, E — and K_pivot, a wavenumber):** scale leg is `M_KK¹` — non-trivial, ODD, and it is what carries the 54.04-decade unit conversion. **The only ODD-degree carrier is the bare `M_KK¹` scale leg.** No even-degree morphism can act on it. The two halves of `Q = R·M_KK^m` are **parity-separated**: the even morphism sector and the odd scale-leg sector never meet.

**The consequence for K_pivot is direct.** K_pivot is a wavenumber: `[K_pivot] = energy¹ = d_A = +1`. By the parity selection rule it is forced onto the **sign-locked `M_KK¹` scale leg** — the *same* leg M_KK itself occupies, the *same* leg S112 just closed as PERMANENT-external, the *same* leg that holds 93.875% of the H₀ relief (the `d_A=+1` parity-inadmissible fraction, `CF-S112-H0-BAND-CLOSURE` `f5a8498d`, capping H₀ relief at 6.125%). **The `deg_T=2.0` morphism degree literally cannot reach K_pivot — it is the wrong parity class.** Reading A's derived transport degree transports *dimensionless tilts*; it is structurally barred from transporting the *dimensionful pivot*. The W3→W4 "category error" the §23.0(5) workshop diagnosed (importing the EVEN `deg_T=2.0` onto a `d_A=+1` ODD temperature) is *exactly* the error Reading A must make to claim K_pivot is a `deg(T)` image. It was caught for LRD-T; it is the same error for K_pivot.

This is the heart of my case and it is a **theorem-shaped** argument, not an "it hasn't been done" argument: the parity mismatch is structural (even morphism ⊥ odd scale leg), the way the κ-sign ∧ Wodzicki-parity joint foreclosure (§VII.CF, STAGE-1-CANDIDATE) is a theorem and not the observation that the exhibited transport happens to have |κ|<1.

---

## 4. Is K_pivot a SECOND dimensional handle, or M_KK-reducible? — the discriminating question

Section 1 split the cases; here I sharpen which one the physics actually selects, because the answer changes *which kind* of external the pivot is (and that matters for §5).

**The multiplicative-normalization cancellation theorem (`math-scripts.md`, MANDATORY K=3) is the tell.** A dimensionless log-derivative observable `O = L_n[f] = d^n ln f / d(ln K)^n` is *identically invariant* under any multiplicative scale factor `w`: `L_n[w·g(K)] = L_n[g(K)]`. The transport degree machinery operates *on exactly these log-derivative observables* (d_s, α_s, n_s are all log-derivatives of power spectra). **A machine that is by-construction blind to multiplicative scale factors cannot output a multiplicative scale factor.** `deg(T)` annihilates `w`; it cannot produce K_pivot, which *is* (a piece of) `w`. This is the cleanest statement of why the dimensionless transport cannot fix the dimensionful pivot: they are orthogonal by the cancellation invariant.

So the substrate-natural content of the BZ→pivot bridge is *entirely* the dimensionless morphism (the tilt-transport: how n_s, α_s, n_T map from BZ scale to pivot scale). The pivot *scale* K* itself is the multiplicative `w`-piece that the morphism cancels. **K_pivot is M_KK-reducible in the trivial sense (`K_pivot = R·M_KK`) but R is the un-derived piece** — and a non-trivial, *independently-physical* R (Case B) would be a second handle the rank-1 theorem forbids. The framework is caught in a vice:

- If R = 2.0 (BZ tessellation, the only substrate-natural candidate) → n_s = 1, **observationally dead.**
- If R = 0.0435 (the working value) → **no mechanism**, it is a fit to Planck.
- If R is "some other substrate scale" providing genuine new dimensional content → **rank-2 violation of §VII.BS** (PERMANENT).

There is no fourth option. The dimensionful pivot is external because (i) the only substrate machinery that crosses the gap is dimensionless-only (parity + cancellation invariant), and (ii) any genuinely-new dimensional content is rank-2-forbidden. **K_pivot is the second protected dimensionful import** — protected the same way M_KK is, by the same N₃=0 rank-1 wall.

**Honest caveat on "second."** Strictly, §VII.BS rank-1 says there is exactly ONE *independent* import. So K_pivot is not a *second independent* handle that coexists with M_KK (that would be the rank-2 violation). The precise statement is: **K_pivot's dimensionful content is M_KK (Case A), and only its dimensionless ratio R is "new" — but R is not substrate-derived, it is observation-set.** So K_pivot contributes *no new derivable substrate content*; it is M_KK (permanently external) times an empirically-fitted R. "Second protected import" is the right intuition; "M_KK-times-a-fit, with the fit irreducibly external" is the exact statement. I flag this so Round 2 doesn't catch me overclaiming a literal rank-2 — the wall I'm leaning on is rank-1 itself, used the other way: rank-1 *permits no second handle*, so the pivot must be M_KK-reducible, so its dimensionful part is M_KK (external), and its dimensionless part R is the unfit-able residual.

---

## 5. Does external K_pivot SHARPEN the incumbent-discrimination ceiling? — yes, and it's quantitative

The incumbent-discrimination ceiling (`BF_spine_vs_incumbent_ceiling = 31.62 = 10^1.5`, S101 BF-spine workshop) is already known to be "unliftable by adding observables; EVOI concentrated entirely in the M_KK-derivation." If K_pivot is a *second* protected external import, this is not just consistent with the ceiling — it **explains and reinforces** it:

- **The ceiling exists because the substrate's dimensionful predictive content is rank-1.** A framework with only ONE derivable dimensionful scale (and that one *also* external, post-S112) can never reach DECISIVE Bayes factors against ΛCDM, because ΛCDM also has free dimensionful scales and the framework cannot out-predict it on *any* dimensionful anchor — only on dimensionless ratios (α_s = n_s²−1 etc.). The m_H-only BF ceiling (b_mH=1.5) is the residue of the *one* place a dimensionless mass-ratio gave near-free predictive power.

- **K_pivot being external removes the one observable that could have lifted the ceiling.** If the CMB pivot scale *were* substrate-derived, then the *absolute* CMB power-spectrum scale (not just its tilt) would be a free-parameter-zero prediction — a genuinely new dimensionful anchor, potentially worth orders of magnitude in BF against an incumbent that fits the pivot freely. Reading B says that observable does not exist: the pivot scale is fit, not predicted. So the second protected import **closes the last door** to lifting the discrimination ceiling. The EVOI being "concentrated entirely in M_KK-derivation" is precisely the statement that the *dimensionful* sector has exactly one lever — and S112 showed that lever is external too.

This is a genuine sharpening: it upgrades the ceiling from an *empirical* observation ("we keep hitting 31.62") to a *structural* one ("rank-1 dimensionful content ⇒ no dimensionful anchor can beat the incumbent; the two dimensionful scales the framework touches, M_KK and K_pivot, are BOTH external"). It also relocates K_pivot's status in the EVOI table: it is **not** a high-leverage open gate (a derivation that would move the needle); it is a *second instance of the M_KK-class permanent-external boundary*, and like M_KK's magnitude sub-residual (retired to evoi-framework §5 post-S112), it should be retired from the "derivable" column to the "permanently-external" column — sharpening A1 (open-channel-ledger) from "the single largest *gap*" to "a second instance of the rank-1 dimensional-import *boundary*."

---

## 6. Substrate-first framing check (so the verdict doesn't drift into container-thinking)

Reading B is *not* "the substrate is incomplete and needs an external crutch." The substrate-IS framing is preserved and is in fact *stronger* under Reading B:

The substrate IS the D_K eigenvalue spectrum on Jensen-deformed SU(3). That spectrum determines — from zero continuous parameters — the conformal class and **every dimensionless observable**: the tilt relations (α_s = n_s²−1), the GGE relic shapes, the coupling ratios (g₁/g₂ = e^{−2τ}), the dimensionless transport degrees (n_T non-scalar, α_s `deg=+2`). What the spectrum does *not* do — *cannot* do, by N₃=0 rank-1 — is set the ONE dimensionful unit those dimensionless quantities are read off in. That unit (M_KK) is imported once, the way GR imports the meter. K_pivot is dimensionful, so its *dimensionful part* is that same single import; its *dimensionless part* (R) is the only thing "new," and the substrate does not derive R either (no mechanism lands the working value).

The direction of explanation is intact: substrate → dimensionless physics (derived) → dimensionful readout (one external unit). Reading A inverts this by treating a dimensionful pivot scale as a *substrate output*, which would require the substrate to fix two dimensionful scales (M_KK and K_pivot) independently — container-thinking at the dimensional-class level, and rank-2-forbidden. The IS-not-IN discipline at the *sourcing layer* (substrate-first-canonical-sourcing.md) says exactly this: the substrate sources dimensionless content; dimensionful pins are the one external calibration, never multiplied.

---

## (i) Honest current lean

**I lean FOR my assigned pole (Reading B), and the lean is strong — but with one scoping correction to the naive "second independent handle" framing, and one genuine residual risk I cannot fully close in R1.**

The structural case is, to my reading, close to decisive: the parity selection rule (§23.0(5)) shows the derived transport degree is even-morphism-class and **cannot** act on the odd `M_KK¹` scale leg where a dimensionful pivot must live; the multiplicative-normalization cancellation theorem shows the dimensionless transport machinery is **by construction** blind to (and incapable of outputting) the multiplicative scale K_pivot; and the rank-1 §VII.BS theorem (STAGE-3-PERMANENT) forbids the only escape (a genuinely new second dimensional handle). The empirical record (C2: BZ-scale and e-fold-scale both give n_s=1; working K* has "no mechanism") is exactly the fingerprint of an external calibration. And it is the *same shape* as the M_KK no-go S112 just closed permanently.

**Scoping correction I am volunteering against my own pole:** the cleanest statement is NOT "K_pivot is a second *independent* handle" (that would be a literal rank-2 structure, which §VII.BS forbids and which I should not claim). It is "K_pivot's dimensionful content reduces to the *one* external import M_KK, and its dimensionless ratio R is observation-set, not substrate-derived." The pivot contributes no new *derivable* substrate content. That is still squarely Reading B (the dimensionful pivot is external), but it is the *defensible* version.

**The residual risk to my pole** (the thing Round 2 should press, and the thing I'd press if I held Reading A): the parity rule is **SUGGESTION at K=2**, not a STAGE-3 theorem, and the κ-sign∧Wodzicki-parity foreclosure (§VII.CF) is **STAGE-1-CANDIDATE** with its Stage-2 cross-check (`CF-S111-KSIGN-PARITY-STAGE2`) outstanding. If there exists a substrate-natural bridge map that is *not* a same-class Wodzicki ratio and *not* an HKR cohomology-class ratio — i.e., a morphism that legitimately carries ODD degree — then the parity wall has a hole and a `d_A=+1` pivot *could* be reached dimensionlessly. I do not believe such a morphism exists (the §23.0(5) enumeration of substrate-natural morphisms is even-only), but its *exhaustiveness* is not STAGE-3-proven. That is the single crack.

## (ii) The single most decisive consideration the verdict will turn on

**Whether K_pivot's mass dimension `d_A = +1` (it is a wavenumber) forces it onto the odd `M_KK¹` scale leg, OR whether there exists a substrate-natural ODD-degree morphism that can transport a dimensionful scale dimensionlessly.**

Everything reduces to this. If the parity selection rule's morphism-sector-is-even enumeration is *exhaustive* (no substrate-natural odd-degree morphism), then K_pivot is parity-locked to the `M_KK¹` scale leg, inherits M_KK's PERMANENT-external fate (S112), and Reading B wins — K_pivot is an irreducible external calibration, the second instance of the rank-1 dimensional-import boundary, and it sharpens the incumbent-discrimination ceiling into a structural statement. If, on the contrary, an odd-degree substrate-natural morphism exists (the K=2 SUGGESTION status of §23.0(5) leaves this formally open), then Reading A has a live channel and the verdict moves toward "substrate-derived bridge image." 

The workshop should therefore put its weight on the **exhaustiveness of the substrate-natural morphism enumeration in §23.0(5)** — promoting (or breaking) the parity selection rule from SUGGESTION K=2 toward a theorem is the decisive computation. My strong prior, from the dimensional-class analysis and the just-closed M_KK structural parallel, is that the enumeration holds and K_pivot is external — but the verdict turns on closing that one gap, not on any of the (already decisive-looking) empirical or rank-1 arguments.
