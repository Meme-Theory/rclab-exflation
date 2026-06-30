# Session 110 Workshop: connes × mack

**Date**: 2026-06-21
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: connes (connes-ncg-theorist), mack (mack-cosmic-bridge)
**Source Documents**:
- `computations/session-110/s110_gate_verdicts.txt` (W3 mint :52/:56; W4 consumers :86/:90 dimensionful-T, :96/:101 dimensionless-H0)
- `sessions/session-110/session-110-w4-workingpaper.md` (existing CFs CF-S111-CO34B-LRDT-TRANSPORT :556, CF-S111-CF3-H0-RESIDUAL :565; volovik a₀-orthogonality Layer-1 wall :573)
- `sessions/framework/registry/cross-pillar-bridge-corpus.md` (§23 per-observable transport-degree K-counter, SUGGESTION K=2, line 1646; §18 §VII.BA composite-admissibility `deg(B)=d_A`)

**Focus Topics — the adjudication**: Does the per-observable transport-degree theorem (corpus §23, SUGGESTION K=2, currently DIMENSIONLESS-only: n_s scalar / n_T non-scalar / α_s deg=+2) EXTEND to the **DIMENSIONFUL-observable class**? W3 minted `deg(T_{BZ→pivot})=+2 NON-SCALAR` for a *dimensionless* 2nd-derivative observable; two W4 consumers of *different* dimensional class now import that same `+2` with opposite-signed magnitude pathologies — a DIMENSIONFUL temperature (CO34-legB: T_pivot_natural=2.949e-79 K, −82.23 OOM below the [3500,6500] K band) and a DIMENSIONLESS H₀ relief (CF3: fitted 18.37× = 1.17% of budget, NOT substrate-natural; full-homogeneity overshoots ~107 decades). Produce a STRUCTURAL VERDICT on (a) whether `deg(T_{BZ→pivot})` is fixed UNIQUELY by mass dimension (Wodzicki/HKR homogeneity, `deg(B)=d_A` Conjunct-1, §18) or is the SAME `+2` for all dimensional classes; (b) IF per-dimensional-class, DERIVE the admissibility rule and RE-TEST whether CO34-legB and CF3 reach their bands KNOB-FREE; (c) CLASSIFY: §23 K=3 advancement (dimensionful-observable, HIT-distinct on the dimensional-class axis) vs new §VII.BA composite-admissibility entry vs NON-PROMOTION-BY-HELD-NUMBER (dimensionful-slot-collision).

**Steelman assignment** (from the workshop charge, verbatim — the genuine ledger-dissonance both agents adjudicate):
- **connes (Agent A) steelmans DEGREE-BY-DIMENSION**: a dimensionful temperature MUST carry its own non-+2 homogeneity degree; `+2` was inherited from the dimensionless α_s 2nd-derivative sibling (the wrong power). The Wodzicki-trace factor carries `−2s` by uniqueness; an HKR cohomology-class ratio carries `0` — so the dimensional class FIXES the degree.
- **mack (Agent B) steelmans BAND-BINDING**: the substrate-natural degree, whatever its dimensional class, still must LAND the observed band; the −82.23 OOM (T) and ~107-decade (H₀) overshoots constrain whether ANY knob-free substrate-natural degree exists — the held magnitudes may SURVIVE the extension.

**Discipline**: Substitution-chain (`math-scripts.md §"Double-Check Logic Before Compute"`) MANDATORY on the `deg(B)=d_A` homogeneity claim and on EVERY sign / OOM-direction statement. Substrate-first framing (`phononic-framing.md`): the substrate IS the spectral triple; an observable's CMB-pivot image is READ THROUGH the transport map `T_{BZ→pivot}`, not a field propagating in a container. The two single-observable CFs (CF-S111-CO34B-LRDT-TRANSPORT, CF-S111-CF3-H0-RESIDUAL) ALREADY EXIST — do NOT duplicate; this workshop fixes the degree-determination RULE they presuppose.

---

## Round 1 — connes: Opening Analysis

### C1: Is `deg(T_{BZ→pivot})` fixed UNIQUELY by mass dimension? (the `deg(B)=d_A` homogeneity theorem)

**Charge:** Steelman degree-by-dimension from the NCG side. Write the MANDATORY substitution-chain on `deg(B)=d_A` (corpus §18 Conjunct-1; §VII.BA Wodzicki-BCS Bridge Theorem): Wodzicki-trace factor carries `−2s` by uniqueness, HKR cohomology-class ratio carries `0`. Does a substrate-IS observable's transport degree follow uniquely from its mass dimension `d_A`, or is `+2` degree-universal across dimensional classes?

**Finding (degree-by-dimension, steelmanned from the spectral side): the transport degree is NOT a free label — it is the mass dimension of the observable it transports, fixed by Wodzicki uniqueness on the homogeneity axis. `+2` is NOT degree-universal; it is the homogeneity weight of one specific mass-dim-0 amplitude, and importing it onto a mass-dim-1 temperature is a homogeneity-class violation of corpus §18 Conjunct-1.**

This is a substrate-first statement before it is a transport statement. The substrate IS the finite spectral triple `(A_K, H_K, D_K)` (`phononic-framing.md §"IS Space"`); the BZ→pivot image of any observable `O` is read THROUGH the composite bridge map `B = T_{BZ→pivot} ⊙ (HKR ∘ Connes-Karoubi)` (corpus §23.0(1)), not as a field propagating in a container. The degree `deg(B)` is the weight of that map under a uniform spectral rescale `D_K → t·D_K` — and Wodzicki's uniqueness theorem fixes that weight EXACTLY.

**Substitution chain on the `deg(B) = d_A` homogeneity theorem** (`math-scripts.md §"Double-Check Logic Before Compute"`; Sage-verified, `sage_eval` this turn):

```
Claim: "deg(B) is fixed uniquely by the mass dimension d_A of the transported observable."

Step 1 (definitions, canonical sources):
  - Res_W : Ψ(A_K) → ℂ is the UNIQUE (up to scalar) trace on the pseudodifferential
    algebra extending continuously to Ψ(A_K)  [Wodzicki 1984; Connes 1994 book §2.3;
    cited verbatim in §VII.BA Element-1 (registry :20242) and corpus §18.0 Conjunct-1].
  - HKR factor (cohomology-class ratio ρ_FULL = M_FULL/M_BARE) carries degree 0 by the
    orientability axiom + Chern character  [Connes book §III axiom 6, §4; corpus §18.0].
  - d_A := mass dimension of the canonical Level-3 anchor of the bridge (corpus §18.0,
    "canonical Level-3 anchor of homogeneity degree d_A").

Step 2 (substitute the spectral rescale D_K → t·D_K, the ONLY action that probes degree):
  - Res_W(D_K^{-2s}) → Res_W((t·D_K)^{-2s}) = t^{-2s} · Res_W(D_K^{-2s})
        [because D_K^{-2s} is homogeneous of degree −2s and Res_W is a TRACE, scalar-linear]
  - HKR(ρ_FULL) → ρ_FULL  (degree 0; a ratio of equal-degree moments cancels)

Step 3 (simplify to canonical form — read the weight of the composite):
  - deg(Res_W factor) = −2s            [Sage: deg_wodzicki = -2*s, EXACT]
  - deg(HKR factor)   = 0
  - deg(B = Res_W ⊙ HKR) = −2s + 0 = −2s   ← UNIQUELY fixed; no free choice

Step 4 (read off direction / admissibility — corpus §18.0 Conjunct-1):
  - B is admissible iff deg(B) = d_A  (the anchor's mass dimension).
  - −2s is an INDEX-TYPE invariant (non-deformable in moduli, Sage: −4 at s=2, −6 at s=3);
    no pole s>0 has deg→0. The degree is rigid because the trace is UNIQUE.
  Conclusion: deg(B) is fixed UNIQUELY by Wodzicki uniqueness, and admissibility
  REQUIRES it to equal d_A. A mismatch deg(B) ≠ d_A is a homogeneity-class FAIL
  (the T1 forbidden cell, corpus §18.0 table). ∎
```

**Why this forecloses "degree-universal `+2`."** If `deg(B)` were a single value `+2` for ALL observables regardless of dimensional class, then by Step 4 only observables with `d_A = +2` could ever be admissibly transported, and every other observable (n_s with `d_A=0`, a temperature with `d_A=+1`) would be forced into a homogeneity-class FAIL by construction. That is precisely backwards: the framework already transports n_s admissibly with a SCALAR (`deg=0`, registry-canonical, corpus §23 table row 1). So the degree is demonstrably NOT universal — it tracks `d_A`. The `+2` is the homogeneity weight of ONE observable class (the α_s 2nd-derivative sibling, `d_A=0` running but with a TWO-POLE `(a₄/a₂)²` structure giving `deg = 2(s₂−s₄) = +2`, corpus §23.1 instance 2), and it is correct THERE because corpus §23.1 verified `factorization_holds=False` and `deg = 2(s₂−s₄) = +2` matches that observable's own bridge structure. It is the degree OF THAT OBSERVABLE'S MAP, not a universal constant.

**The substrate reading (direction of explanation preserved).** `D_K` eigenvalues → the spectral-moment ratio / residue (the substrate-IS observable) → its transport image under `B` → the CMB-pivot measurement. The degree `−2s` (equivalently `d_A` at admissibility) is upstream of any truncation scheme or lab anchor (corpus §18.1 substrate-framing: "the substrate's own algebraic-trace dimensional structure dictates what its bridge maps CAN be; degree is upstream of the truncation scheme"). The lab band does NOT get to override the degree; the degree is a structural property of `D_K`'s spectrum read through the unique trace. This is the steelman: **degree-by-dimension is not a convention choice, it is Wodzicki uniqueness applied to the transport factor — and uniqueness leaves no room for a universal `+2`.**

### C2: The `+2` inheritance defect — dimensionless-α_s degree carried onto a dimensionful temperature

**Charge:** Trace the cross-wave origin. W3 (S110-CF-CV6B-DS-M4, :52/:56) minted `deg(T_{BZ→pivot})=2 NON-SCALAR` as "amplitude homogeneity d/2=2" for a DIMENSIONLESS spectral-dimension `d_s`. CO34-legB (:86/:90) IMPORTED that same `+2` for a DIMENSIONFUL temperature. Is the import a category error (a degree extracted for a dimensionless 2nd-derivative observable mis-applied to a mass-dimension-1 temperature)? Substitution-chain on the `d/2=2` amplitude-homogeneity claim and on the −82.23 OOM direction.

**Finding: YES — the import is a category error. The `+2 = d/2` minted at W3 is the homogeneity exponent of a DIMENSIONLESS heat-trace amplitude (`d_A = 0`). Applying it to a DIMENSIONFUL temperature (`d_A = +1`) carries the wrong observable's degree onto T. The defect is visible in the verdict file's own provenance trail: the dedup-flag-iii canonical import copied a NUMBER across a dimensional-class boundary that the homogeneity theorem (C1) forbids crossing.**

**The cross-wave trail, read off the verdict file.** W3 line 56 states the mint verbatim: `deg(T_BZ->pivot)=2 NON-SCALAR (amplitude homogeneity d/2=2); reconciles S93 W7-1 deg_T=2.0000 (cross-sector); promoted to canonical_constants (dedup flag iii)`. The observable being transported at W3 is `S110-CF-CV6B-DS-M4` — line 52: `d_s^M4_min=4.0000_d_s^M4_pivot=4.0000`, a windowed **spectral dimension** `d_s = −2 dlnP/dlnσ`. A spectral dimension is DIMENSIONLESS (`d_A = 0`). CO34-legB line 90 then states the import verbatim: `leg B: LRD-T deg(T)=+2 NON-SCALAR transport (IMPORTED canonical_constants.py:716 W3 CF-CV6B, dedup flag iii; matches W3 npz=True)`. CF3 line 99 does the same for H₀: `deg(T_BZ->pivot)=2.0 NON-SCALAR IMPORTED canonical_constants.py:716 (W3 CF-CV6B, dedup flag iii)`. So a SINGLE canonical scalar `deg_T=2.0` minted from a dimensionless observable was imported, by name, into two consumers — one dimensionful (T), one dimensionless (H₀).

**Substitution chain on the `d/2 = 2` amplitude-homogeneity claim** (`math-scripts.md §"Double-Check Logic"`; Sage-verified this turn):

```
Claim: "the +2 minted at W3 is d/2 = 2, the homogeneity exponent of the M4 heat-trace AMPLITUDE."

Step 1 (definitions):
  - P_M(σ) := Tr_{M4} e^{−σ D_M²}  ~ σ^{−d/2}  (leading Weyl heat-trace, d-dim manifold).
    Source: regulator_pin a_2^{ζ} on the M4 summand, W3 line 54.
  - d_s(σ) := −2 d ln P(σ)/d ln σ  (windowed spectral dimension; W3 scheme line 52).
  - M4 base summand: d = 4.

Step 2 (substitute d=4 into the amplitude exponent):
  - P_M4(σ) ~ σ^{−4/2} = σ^{−2}
  - amplitude exponent = −d/2 = −2  ⇒  |exponent| = d/2 = 2.   [Sage: d/2 = 2, EXACT]

Step 3 (read off what the "+2" weights):
  - d_s = −2 d ln(σ^{−2})/d ln σ = −2·(−2) = 4.   [Sage: d_s = 4, EXACT; matches W3 d_s^M4=4.0000]
  - The "+2" is the EXPONENT of the AMPLITUDE P(σ) — a power of a DIMENSIONLESS
    heat-trace ratio sitting INSIDE a DIMENSIONLESS observable d_s.

Step 4 (direction / dimensional-class read):
  - mass-dim of the W3 transported observable d_s = 0.   [Sage CLAIM 3]
  - mass-dim of an LRD photosphere temperature T = +1 (energy, k_B=1).   [Sage CLAIM 3]
  - The degree d_A that B must match (C1 theorem) is the mass dimension of the
    ANCHOR. For d_s, d_A = 0; for T, d_A = +1. These are DIFFERENT cells.
  Conclusion: importing deg=+2 (extracted as the d/2 amplitude exponent of a
  d_A=0 spectral dimension) onto a d_A=+1 temperature crosses a dimensional-class
  boundary. The number "+2" is correct for the W3 observable's own bridge structure
  (the (a₄/a₂)² two-pole reading, corpus §23.1 instance 2 — deg = 2(s₂−s₄) = +2),
  but it is NOT the homogeneity degree of T's transport map. CATEGORY ERROR confirmed. ∎
```

**A subtlety I must flag for rigor (not let slide).** The W3 mint's literal justification — "amplitude homogeneity d/2=2" — and its cross-citation to S93 W7-1's `deg_T=2.0000` (the α_s 2nd-derivative two-pole degree, corpus §23.1) are TWO different routes to the same number `+2`, and BOTH are routes for `d_A = 0` observables. The d/2 route gives `+2` for the M4 spectral dimension; the `(a₄/a₂)²` route gives `+2` for the α_s running. The coincidence that both `d_A=0` observables land on `+2` is exactly what made the import look safe — a "matches W3 npz=True" check passes because the NUMBER matches, while the dimensional-class mismatch (the thing that actually decides admissibility, C1) is never tested. This is a textbook PRU-adjacent slot-collision: a canonical scalar imported by name carries no dimensional-class tag, so the consumer cannot see that `d_A` differs. It is the `regulator-pin-discipline.md §"four-axis orthogonality"` failure mode one axis over — a degree imported across dimensional classes with no dimensional-class pin.

**Substitution chain on the −82.23 OOM direction** (Sage-verified; the magnitude pathology is the OBSERVABLE consequence of the category error):

```
Claim: "deg=+2 drives T_pivot to −82.23 OOM BELOW the [3500,6500] K band; direction right, magnitude wrong."

Step 1: T_bare = 3.545e29 K (substrate/BZ scale, fold-robust 0.69%, inv-7 W2-2).
        Transport kernel |κ| < 1 (T decreases under BZ→pivot; CF3 line 100 clock_coeff<0).
        Natural BZ→pivot separation: sep = 54.04 decades.
Step 2: deg=+2 transport applies the exponent twice: descent = 2 × 54.04 = 108.08 decades.
        [Sage: total bare→pivot descent under deg=+2 = 108.0799 dec; effective deg = 1.99999 ✓]
Step 3: T_pivot = T_bare · 10^(−108.08) = 3.545e29 · 10^(−108.08) ≈ 2.949e−79 K.
        [matches verdict file T_pivot_natural=2.949e-79 K]
Step 4 (direction): band_lo / T_pivot = 3500 / 2.949e−79 ⇒ +82.07 OOM
        [Sage CLAIM 4a; verdict file −82.23 OOM, agreeing to rounding].
  Direction PASS: T_bare DOES come down (kernel<1, sign correct, verdict sign_verdict=PASS).
  Magnitude FAIL: the band needs a descent of only ~25.87 decades (T_bare → band center),
  but deg=+2 forces a 108.08-decade descent — OVERSHOOTING the band by ~82 decades.
  The overshoot is the DIRECT arithmetic consequence of applying the d_A=0 observable's
  degree (+2) to a d_A=+1 observable: the exponent is too large by exactly the factor
  that distinguishes the two dimensional classes. ∎
```

The −82 OOM is not a separate bug; it is what a category error in the transport degree LOOKS like downstream. The W3 mint was sound FOR ITS OBSERVABLE; the W4 import broke it by ignoring `d_A`.

### C3: Per-dimensional-class admissibility rule — derive the degree for a dimensionful T and a dimensionless H₀

**Charge:** IF degree is per-dimensional-class, DERIVE the rule that fixes a dimensionful temperature's transport degree (mass dimension 1) and a dimensionless relief's degree (`ΔH₀/H₀`, dimension 0). Connect to the 54.04-decade BZ→pivot separation and the band-required ratios (T needs a 12.93-decade ratio; H₀ needs [0.08,0.10]). State the substitution-chain for each derived degree.

**The admissibility rule (derived).** Combining C1 (Wodzicki uniqueness fixes `deg(B)`) with the framework's universal dimensional bookkeeping `Q = R · M_KK^m` (MEMORY; every dimensionful quantity is a dimensionless substrate ratio `R` times an integer power of the sole external pin `M_KK`):

> **DIMENSIONAL-CLASS ADMISSIBILITY RULE.** For a substrate-IS observable `O` with mass dimension `d_A`, the admissible transport degree is `deg(B) = d_A` (C1). The transport factor decomposes as `B = (M_KK-carrying scale leg)^{d_A} ⊙ (dimensionless structural morphism)`. Concretely:
> - **`d_A = 0` (dimensionless: n_s, α_s, d_s, ΔH₀/H₀):** the `M_KK^{d_A} = M_KK^0 = 1` scale leg is TRIVIAL. The transport degree is carried ENTIRELY by the dimensionless structural morphism — `scalar` (T2-VACUOUS, n_s-like, substrate=pivot) if `factorization_holds=True`, or a `substrate-natural NON-SCALAR` (n_T-like, α_s-like, substrate≠pivot) if the windowed shape is L_max-dependent. The `+2` of α_s lives HERE: it is the morphism degree `2(s₂−s₄)` of a TWO-POLE ratio, NOT a unit conversion.
> - **`d_A = 1` (dimensionful, energy/temperature: T, H, E):** the `M_KK^1` scale leg is NON-TRIVIAL and CARRIES the 54.04-decade BZ→pivot unit conversion. The dimensionless structural morphism is a SEPARATE factor. The transport degree of the DIMENSIONFUL channel is `+1` in the `M_KK` unit-conversion leg (the bridge that turns a substrate-scale energy into a pivot-scale energy), times whatever dimensionless re-weighting the structural morphism adds.

The category error of C2 is now precise: importing `+2` onto T conflated the **dimensionless morphism degree** (where `+2` legitimately lives for α_s) with the **dimensionful scale-leg degree** (where T's own degree of `+1` lives). They are different factors of `B`.

**Substitution chain — derived degree for a dimensionful temperature T** (`d_A = +1`):

```
Claim: "T's admissible transport degree is +1 in the M_KK scale leg, NOT +2."

Step 1 (definitions):
  - T_substrate = R_T · M_KK^1   (Q = R·M_KK^m with m=1; T is energy, k_B=1).
  - T_pivot = the pivot-scale temperature, an energy at the 4D/CMB scale.
  - sep = log10(M_KK / k_4D) = 54.04 decades (the BZ→pivot unit-conversion span).
Step 2 (substitute — what carries the dimension):
  - The unit conversion M_KK → k_4D is the d_A=1 scale leg: it acts ONCE
    (deg=+1) on the single power M_KK^1 in T = R_T·M_KK^1.
  - T_pivot = R_T · k_4D^1 · (dimensionless morphism), i.e. the SAME R_T re-expressed
    at the pivot energy unit.
Step 3 (simplify — the descent from the scale leg alone):
  - descent from the d_A=1 scale leg = +1 × 54.04 = 54.04 decades, NOT 108.08.
  - T_pivot(deg=+1) ≈ 3.545e29 · 10^(−54.04) ≈ 3.5e−25 K  (scale-leg only).
Step 4 (read off):
  - deg=+1 still OVERSHOOTS: band needs ~25.87 decades of descent (Sage CLAIM 4a),
    deg=+1 gives 54.04 decades. So even the dimensionally-CORRECT integer degree (+1)
    does not land the band — it overshoots by ~28 decades.
  Conclusion: T's admissible degree is +1 (its mass dimension), which is STRICTLY
  better than the imported +2 (108→54 dec, halving the overshoot) but STILL does
  not reach the band knob-free. The dimensionally-correct degree SHARPENS the
  diagnosis without curing the magnitude. ∎
```

**The decisive Sage result — no integer degree lands the T band.** I computed the effective degree that WOULD land the band center:

```
band-landing descent needed = log10(T_bare / band_center) = 25.871 decades   [Sage, exact RealField]
effective deg to land band   = 25.871 / 54.04 = 0.4787...                      [Sage]
```

The band-landing degree is **`0.4787`, a fractional non-integer power** — distinct from `+2` (full homogeneity, the W3 import), `+1` (T's mass dimension, the dimensionally-correct integer), and `0` (scalar). The charge's "12.93-decade ratio" is exactly `25.87 / 2` — the per-application descent that deg=+2 applies TWICE; reading it as a single required ratio is itself a residue of the deg=+2 framing. **No substrate-natural integer degree lands the LRD-T band.** Degree-by-dimension fixes the degree at `+1` and proves the band is unreachable by ANY admissible integer transport — which is a sharper, more useful negative than "the import was wrong."

**Substitution chain — derived degree for the dimensionless H₀ relief** (`d_A = 0`):

```
Claim: "ΔH₀/H₀ has d_A=0, so its admissible degree is carried entirely by the dimensionless
        morphism (scalar OR substrate-natural non-scalar) — NOT the +2 amplitude exponent."

Step 1 (definitions):
  - ΔH₀/H₀: a RATIO of two energies (H_pivot, H_BZ), mass-dim = [H]−[H] = 0.   [Sage CLAIM 3]
  - Q = R·M_KK^0 = R: a pure dimensionless substrate ratio. The M_KK scale leg is M_KK^0 = 1.
Step 2 (substitute — the d_A=0 transport):
  - The scale leg contributes M_KK^0 = 1 (TRIVIAL); it cannot move ΔH₀/H₀ across decades.
  - The transport degree is whatever the dimensionless structural morphism is:
      reading (1) scalar (deg=0):     ΔH₀/H₀ = 0.0049  (CF3 line 101) → below [0.08,0.10] band.
      reading (3) fitted 18.367× = 7500000/408331 (Sage-exact) → lands band but NOT substrate-natural.
Step 3 (the +2-full-homogeneity reading is DIMENSIONALLY INADMISSIBLE for a d_A=0 ratio):
  - reading (2) full homog deg=2 × 54.04 = 108.08 decades → 10^108 overshoot (CF3 line 101).
  - But a d_A=0 ratio CANNOT carry a 54.04-decade unit conversion at ALL — there is no
    M_KK power to convert. Applying the 54.04-decade span to a dimensionless ratio is the
    SAME category error as C2, in the opposite magnitude direction: instead of overshooting
    DOWN (T), it overshoots UP (H₀ by 107 decades). [Sage CLAIM 4b: 2*sep = 108.08]
Step 4 (read off):
  - The dimensionally-correct transport for ΔH₀/H₀ is a deg=0 (or substrate-natural non-scalar)
    dimensionless morphism that does NOT invoke the 54.04-decade separation. That morphism is
    the a₂ focusing-clock relief, which natively yields 0.0049 (scalar reading) — BELOW the band.
  Conclusion: H₀'s admissible transport is dimensionless-morphism-only; the +2 import is
  inadmissible (it imports a unit-conversion span a dimensionless ratio cannot carry). The
  substrate-natural relief is 0.0049, which is a genuine PARTIAL relief but does NOT close
  the ~9% tension. The fitted 18.367× is the knob CF3 correctly flags as not substrate-natural. ∎
```

**Convergent structural conclusion across both consumers.** Once the dimensional-class admissibility rule is applied, BOTH magnitudes stay HELD — but for the SAME structural reason, which is the volovik a₀-orthogonality Layer-1 wall (workingpaper:573): *"neither moment pins a dimensionful H₀; a dimensionless ratio cannot close a dimensional gap."* For T (`d_A=1`): the dimensionless substrate ratio `R_T` is fixed, and the ONLY thing that could move it across the 54.04-decade gap is the `M_KK^1` scale leg — which gives deg=+1, overshooting the band by ~28 decades, with no integer degree landing it (Sage: 0.4787 needed). For H₀ (`d_A=0`): there is no scale leg at all, so the relief is bounded by the dimensionless morphism (0.0049), and reaching [0.08,0.10] requires the fitted knob. **The dimensional-class rule does not rescue either band; it explains WHY neither is reachable knob-free — the held magnitudes survive the dimensionally-correct extension.** This is the precise point where my degree-by-dimension steelman and mack's band-binding steelman CONVERGE rather than conflict: degree-by-dimension fixes the degree; band-binding then verifies the fixed degree still does not land — and it doesn't.

### C4: Cross-Cutting — classification + how the verdict sharpens CF-S111-CO34B-LRDT-TRANSPORT and CF-S111-CF3-H0-RESIDUAL

**Charge:** Pre-state the connes-side classification: §23 K=3 advancement on the dimensional-class axis (Hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv`), new §VII.BA composite-admissibility entry, or NON-PROMOTION-BY-HELD-NUMBER (dimensionful-slot-collision). State concretely how the degree-determination RULE sharpens each existing single-observable CF (do NOT re-author them). Pose specific questions for mack.

**Connes-side classification (pre-stated; mack adjudicates the band-binding leg in M1/M2).** The outcome is NOT a single bucket — it is a TWO-LAYER landing, because the workshop straddles a methodology layer (the degree-determination RULE) and a substrate-physics layer (the held magnitudes). Per the multi-layer output-slot decomposition (`agent-standards.md §"HIGH-DENSITY WORKSHOP TEMPLATE"`), I read it as:

**(Layer 1 — methodology) §23 K=3 ADVANCEMENT on the dimensional-class axis.** The dimensionful-observable transport degree (`d_A = +1`, the `M_KK`-scale-leg degree, distinct from the `d_A=0` morphism degree) is a structurally-distinct calibration instance for the §23 per-observable transport-degree K-counter. Evaluate the Hybrid Independence Test `(i ∨ ii ∨ iii) ∧ iv` (corpus §3; `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`) against the existing §23 instances (n_T, α_s — BOTH `d_A=0`):

```
(i)  distinct substrate-IS observable?  YES — a dimensionful temperature/Hubble (d_A=1),
     vs n_T (d_A=0 tensor tilt) and α_s (d_A=0 scalar running). DISTINCT on the
     DIMENSIONAL-CLASS axis — the new axis this workshop opens. PASS.
(ii) distinct laboratory-IN pillar?  T → LRD photosphere (Pillar II CMB-adjacent / JWST);
     H₀ → late-time expansion. Not required to fire (i alone suffices). 
(iii) distinct bridge-map class?  SAME composite class T_{BZ→pivot} ⊙ (HKR∘CK); does not fire.
(iv) independent algebraic envelope?  YES — the d_A=1 scale-leg degree (+1, M_KK unit
     conversion) is NOT a numerical refinement of the d_A=0 morphism degree (+2). The
     factorization is structurally different: scale-leg vs structural-morphism. PASS.

HIT predicate (i ∧ iv) FIRES ⇒ K=3 advancement candidate VALID on the dimensional-class axis.
```

This is the genuine K=3 instance the §23 status line has been waiting for (corpus §23 line 1685: "K=3 advancement candidate: deg(T_{BZ→pivot}) for r ... or α_t" — those are BOTH `d_A=0`; the DIMENSIONFUL class is a STRONGER distinctness, on a new axis, and I argue it is the better K=3 occupant because it forces the K-counter to recognize that the transport-degree theorem is dimensional-class-INDEXED, not just observable-indexed). **The K=3 advancement, IF it lands, promotes §23 SUGGESTION → MANDATORY.** mack adjudicates whether the band-binding evidence supports calling it an advancement vs a non-promotion.

**(Layer 2 — substrate-physics) NON-PROMOTION-BY-HELD-NUMBER, differentia = dimensionful-slot-collision.** The magnitudes (T_pivot, ΔH₀/H₀) are HELD. Per the Non-Promotion-by-Held-Number Meta-Taxonomy (`cross-pillar-bridge-anatomy.md §"Non-Promotion-by-Held-Number Meta-Taxonomy"`; corpus §26), test the genus predicate:

```
P1 (theorem-STRUCTURE permanent/proven): YES — the dimensional-class admissibility RULE
   (C3) is the proven structure; deg(B)=d_A is Wodzicki-unique (C1).
P2 (a NUMBER is HELD against substrate-natural extraction): YES — T_pivot∈[3500,6500]K and
   ΔH₀/H₀∈[0.08,0.10] are NOT reachable knob-free (Sage: T needs effective deg 0.4787, a
   non-integer; H₀ needs the fitted 18.367×).
P3 (the held NUMBER is NOT sideways-re-pinned to a methodology-floor F-image): YES — we do
   NOT re-pin T_pivot to the fitted knob and call it substrate-natural. It stays HELD.
Genus P1∧P2∧P3 HOLDS ⇒ NON-PROMOTION-BY-HELD-NUMBER.

Differentia: DIMENSIONFUL-SLOT-COLLISION (the SAME differentia as Member A, n_PBH, corpus §26).
  The dimensionful magnitude (T's energy scale) and the transport-degree slot share ONE
  multiplicative M_KK^{d_A} structure: fixing the degree (+1) fixes the scale leg, and the
  scale leg IS the dimensionful magnitude's carrier. You cannot promote the magnitude without
  promoting the degree, and the degree (+1) overshoots. This is the dimensionful-slot-collision
  signature: the dimension prefactor and the transport span share one slot.
```

This is a companion instance to Member A (n_PBH) on the SAME differentia — by the corpus §26 ENRICH precedent (the K_csub_R note, corpus §26 "S95 W1-2 companion instance"), **a structurally-distinct firing of an EXISTING differentiator ENRICHES the corpus WITHOUT advancing the §26 K-counter** (§26 stays K=1; the new content is the §23 dimensional-class K=3 on the orthogonal methodology axis). The two layers are orthogonal per the algebra-axis orthogonality / Layer-Decomposition `F(observable)` vs `F(rule)` split — the §23 advancement is a METHODOLOGY-layer event; the held magnitude is a SUBSTRATE-PHYSICS-layer event. No conflation.

**Why NOT a new §VII.BA composite-admissibility entry.** §VII.BA (corpus §18, `deg(B)=d_A`) is the PARENT framework this workshop INVOKES, not a new entry it creates. The dimensional-class rule is the §18 Conjunct-1 homogeneity axis SPECIALIZED to the dimensionful class — it lands as a §23 cross-link / corpus extension citing §18, not as a fresh §VII.BA slot. (If mack's band-binding analysis surfaces a genuinely new composite bridge map with its own 5-anatomy, that would be a separate §VII slot — but the degree-RULE itself is a §23 K-counter event.)

**How the verdict SHARPENS the two existing single-observable CFs (do NOT re-author):**

- **`CF-S111-CO34B-LRDT-TRANSPORT` (workingpaper:556).** Its "What" field asks: *"Derive the substrate-natural transport DEGREE/kernel proper to the temperature channel ... and re-test T_pivot ∈ [3500,6500] K."* This workshop's degree-RULE SHARPENS that CF in two ways: (1) the substrate-natural degree IS NOW DERIVED — `d_A = +1`, the `M_KK^1` scale-leg degree, NOT a free search; the CF's compute should pin deg=+1 a priori and verify, not scan. (2) The Sage result pre-states the CF's likely OUTCOME: even deg=+1 overshoots (54.04 vs 25.87 decades needed), and NO integer degree lands the band (effective deg 0.4787 is non-integer) — so the CF's gate (`T_pivot ∈ [3500,6500] K via a substrate-natural non-fitted degree`) is expected to return HELD/INFO, and the CF should pre-register that the substrate-natural-degree PASS criterion may be structurally unreachable, routing to dimensionful-slot-collision rather than to a fitted knob. NOTE to the CF, not a re-authoring: the gate should test "is there a substrate-natural NON-SCALAR dimensionless morphism ON TOP of the deg=+1 scale leg that supplies the residual ~28-decade descent" — that is the only remaining substrate-natural channel, and it is the genuine open compute.

- **`CF-S111-CF3-H0-RESIDUAL` (workingpaper:565).** Its "What" field asks for *"the residual relief from the a₀-orthogonal channel ... test whether the substrate closes the FULL ΔH₀/H₀ ∈ [0.08,0.10] with zero fitted knobs."* The degree-RULE SHARPENS it: ΔH₀/H₀ is `d_A=0`, so its transport CANNOT invoke the 54.04-decade scale leg at all (the +2 full-homogeneity reading is dimensionally INADMISSIBLE — it imports a unit-conversion span a dimensionless ratio cannot carry). The CF's residual-relief search is therefore CONSTRAINED to dimensionless-morphism channels (the a₂ focusing-clock at 0.0049, plus any a₀-orthogonal dimensionless RELATION) — consistent with the volovik a₀-orthogonality scope note (workingpaper:573): the a₀ draw is a dimensionless-Ô RELATION refinement, NOT a dimensionful budget. This CONFIRMS the CF's existing scope-restriction and adds the degree-theoretic REASON: a `d_A=0` observable has no scale leg, so "drawing a dimensionful relief from a₀" is forbidden by the SAME homogeneity theorem (C1) that forbids the T import. The CF stays a dimensionless-relation gate; its PASS criterion (substrate-derived dimensionless relation predicting the shift once `w=M_KK` is fixed by one observation) is the correct one, and the workshop pins WHY.

**Questions for mack (engage your band-binding steelman — this is the counter-position I must test):**

- **Q-C-1 (the band-binding crux).** I claim degree-by-dimension fixes T's degree at `+1` and that NO integer degree lands the LRD-T band (Sage: effective deg 0.4787, non-integer). Your band-binding steelman says the substrate-natural degree, WHATEVER its class, must land the band — and the held magnitudes "may SURVIVE the extension." Do you AGREE the magnitudes survive (i.e., the band is NOT reached knob-free), making this a NON-PROMOTION-BY-HELD-NUMBER? Or do you see a substrate-natural NON-SCALAR dimensionless morphism (on top of the deg=+1 scale leg) that supplies the residual ~28-decade descent for T and lands [3500,6500] K — a channel my degree-only analysis does not foreclose?

- **Q-C-2 (the non-integer effective degree).** The band-landing effective degree for T is `0.4787` — fractional. In NCG, transport degrees from index-type invariants (`−2s`, Wodzicki) are INTEGER/half-integer-rigid (corpus §18.0: `d_τ(s)=−2s` index-rigid, non-deformable). A fractional `0.4787` is NOT an index-type degree. Does that, from your cosmological-bridge side, independently confirm that NO substrate-natural transport lands the band (because substrate-natural degrees are quantized and `0.4787` is not in the lattice) — i.e., is the non-integrality of the required degree ITSELF the falsifier-surface content?

- **Q-C-3 (falsifier-surface, your sole-writer domain).** If the dimensional-class rule holds and the magnitudes stay HELD, what is the falsifier-master-inventory consequence? My read: the LRD-T channel and the H₀-relief channel become PREDICTIONS that the substrate-natural degree does NOT reach the observed band — a DIMENSIONFUL-SLOT-COLLISION held-number, NOT a falsification (the structure is permanent, the number is held). Does that match how you'd land the row, or does the band-miss rise to a genuine tension worth flagging on the §7 surface?

- **Q-C-4 (K=3 vs companion-enrich).** I argue the DIMENSIONFUL transport-degree is a §23 K=3 advancement (HIT (i)∧(iv) fires on the dimensional-class axis) — promoting §23 to MANDATORY — while the held magnitude is a §26 companion-enrich (NO §26 advance). Do you concur the methodology advancement (§23 K=3) and the substrate-physics non-promotion (§26 enrich) are the correct ORTHOGONAL two-layer landing, or would you fold them differently (e.g., hold §23 at K=2 because the dimensional-class instance "fails to land" and only a LANDED band counts as a calibration instance)? This is the sharpest methodology question: does a transport-degree instance that correctly FIXES the degree but whose magnitude stays HELD still count as a §23 calibration instance, or must the band be reached for the K-counter to advance?

---

## Round 1 — mack: Response & Cross-Synthesis

### Part 1: Response to connes's Sections

#### Re: C1 — degree fixed by mass dimension

**AGREE** — on the homogeneity theorem `deg(B) = d_A` and its uniqueness, with one cosmological-bridge sharpening and one scope-flag I must hold against over-reach.

The substitution chain in C1 is sound and I reproduce its Step-3 spine from the corpus directly: corpus §18.0 Conjunct-1 states the Wodzicki-trace factor carries `−2s ≠ 0` (unique trace on Ψ(A_K), Connes 1994 §2.3) and the HKR factor carries `0` (orientability axiom + Chern character), so `deg(B = Res_W ⊙ HKR) = −2s`, and admissibility *requires* `deg(B) = d_A`. The corpus §18.0 five-formulation table makes the same point structurally: **T2** (`N·Res_W`, scalar `N`) is FORBIDDEN/VACUOUS precisely because a scalar of any degree "cancels in the ratio" — the §W2-3 binding-invariant "no scalar of any degree closes the gap". So a uniform `+2` across all dimensional classes is exactly the T2 pathology dressed as a transport degree: it would degree-match by fiat and carry no `L_max`-dependence to actually move the observable. connes is right that the degree is NOT a free label.

**The cosmological-bridge sharpening (what my domain adds to C1).** connes argues degree-by-dimension from Wodzicki uniqueness alone. From the observational side there is an *independent* confirmation that the framework already transports a `d_A=0` observable with a SCALAR and a `d_A=0` observable with a NON-SCALAR — and the discriminator is empirical `L_max`-flow, not just dimensional bookkeeping. The §23 K=2 table (corpus :1681-1683) is the witness: **n_s** transports SCALAR (substrate 0.9561 = pivot 0.9561, the flagship CMB success); **α_s** transports NON-SCALAR `+2` because the `w(L_max)·κ(k)` factorization returned `factorization_holds=False` with `ratio_rel_spread=1.81` (the s=3 transfer-trace shape is genuinely `L_max`-dependent). So `+2` is not even universal *within* the `d_A=0` class — n_s (first-derivative, `d_A=0`) is scalar and α_s (second-derivative, `d_A=0`) is `+2`. This *strengthens* connes's C1: the degree tracks not just `d_A` but the observable's specific bridge structure (derivative order, pole count). A single canonical scalar `deg_T=2.0` imported by name is structurally blind to BOTH axes (dimensional class AND pole-count), which is why the W3→W4 import looked safe and was not.

**SCOPE-FLAG I must hold (rigor, not dissent).** C1's claim "deg(B) is fixed uniquely by Wodzicki uniqueness" is exact for the *Res_W ⊙ HKR* composite (the §18 / §VII.BA object). But the W3 mint did NOT derive its `+2` from a Wodzicki trace — it derived it from `d/2 = 2`, the amplitude-homogeneity exponent of an M4 heat-trace `P_M4(σ) ~ σ^{−2}` (verdict line 54-56, `regulator_pin=a_2^{ζ}`). That is a DIFFERENT degree-determination route than the `−2s` Wodzicki factor (which would give `−4` at s=2, `−6` at s=3, never `+2`). So when C1 says "−2s is index-rigid, no pole s>0 has deg→0," it is correct for the *Wodzicki* leg but does not by itself foreclose the *heat-trace-amplitude* `+d/2` route — those are two distinct homogeneity-degree generators living on the same spectral triple. This matters for C2/C3: the `+2` is a legitimately-derived degree FOR ITS OBSERVABLE (the M4 `d_s`), just on a route (`+d/2`) orthogonal to the Wodzicki route C1 analyzes. The category error is real, but it is "right degree, wrong observable's route," not "the degree was never derivable." I flag this so the verdict does not over-claim that `+2` is non-physical — it is physical for `d_s`, and that is exactly why a name-only canonical import propagated it undetected.

**Answer to the C1-implicit question.** Degree-by-dimension holds. The transport degree is fixed by the transported observable's own homogeneity structure (Wodzicki `−2s` for trace-ratio composites; `+d/2` for heat-trace amplitudes), and `+2` is one specific observable's weight, not a universal constant. I converge with connes here — the dissent, if any, lives downstream in whether the *band* survives (M1), not in whether the *degree* is dimensional-class-indexed (it is).

#### Re: C2 — the `+2` inheritance defect

**AGREE** that the import is a category error, with the verdict-file provenance trail exactly as C2 reads it (line 56 mint "amplitude homogeneity d/2=2"; line 90 import "IMPORTED canonical_constants.py:716 W3 CF-CV6B, dedup flag iii"; line 99 the same for H₀). The dedup-flag-iii canonical promotion copied a single scalar `deg_T=2.0` across a dimensional-class boundary. I confirm connes's −82.23 OOM substitution chain against my own Sage RealField(120) run:

```
T_bare = 3.545e29 K; sep = 54.04 dec; deg=2 ⇒ descent = 2×54.04 = 108.08 dec
T_pivot(deg=2) = 2.9486e-79 K   [Sage; verdict file 2.949e-79 ✓]
band_lo/T_pivot = 82.07 OOM      [Sage; verdict file 82.23 — agree to the T_bare rounding]
```

Direction PASS (kernel<1, T comes down), magnitude FAIL (overshoots the band by ~82 decades). I agree with the C2 conclusion.

**MISSED — the LRD photosphere observational context that fixes what the band actually IS.** C2 treats `[3500,6500] K` as a given band. From my domain it is worth stating WHY that band, because it sharpens the falsifier-surface stakes (M2). The [3500,6500] K window is the JWST Little-Red-Dot rest-frame photosphere temperature inferred from the Balmer-break + red optical / blue UV "V-shaped" SED — the regime where the LRD population's atmospheres sit (cool, dense, near the H⁻ opacity floor and the ~3500 K Hayashi-track boundary; the ~6500 K upper edge is where the Balmer break weakens). It is an OBSERVED band with real error structure, not a free target. That is the cosmological-bridge weight of T: unlike α_s (where the "band" is a Planck datum the substrate value relocates OFF via scale-mismatch, corpus §23.1), the LRD-T band is a *direct* astrophysical measurement of a photosphere, so a substrate-natural overshoot of −82 (or even −28) decades is a clean, hard miss against data — not a relocatable scale-mismatch. This is exactly why the held magnitude here is more consequential than the α_s case: there is no "substrate-sensitivity channel" to relocate T to. T_bare = 3.545e29 K *is* the substrate scale, and the band is at the 4D/pivot scale; the transport has to physically land it.

**MISSED — the dimensional-class pin is the precise missing axis (and it is a known axis-family).** C2 calls the defect "PRU-adjacent slot-collision … a degree imported across dimensional classes with no dimensional-class pin." I sharpen: this is the `regulator-pin-discipline.md §"four-axis orthogonality (UV-regulator × Level × Binding × MACHINERY-SCOPE)"` failure mode on a FIFTH axis the table does not yet carry — a **transported-observable mass-dimension pin**. The four existing axes (UV-regulator `a_n^{ζ}` vs `a_n^{Pauli-Villars}`; Level FULL vs SCHEMATIC; Binding canonical-import vs substrate-natural; MACHINERY-SCOPE cache-projection vs full-leaf-foliation) each close a silent class-conflation. The W3→W4 import is a silent class-conflation on `d_A` (the transported observable's mass dimension): `deg_T=2.0` carries no `d_A` tag, so the consumer cannot see that the source observable (`d_s`, `d_A=0`) and the target observable (T, `d_A=+1`) live in different dimensional cells. The `matches W3 npz=True` check passes on the NUMBER and is blind to `d_A` — the four-axis pathology one axis over. (I record this as an orchestrator-reserved rule-mirror hand-off in the Effected-In-Session block, since `.claude/rules/` is subagent-edit-denied.)

**EMERGES — the coincidence that made the import undetectable is itself substrate content.** Both `d_A=0` routes (the M4 `+d/2` heat-trace amplitude AND the α_s `(a₄/a₂)²` two-pole `2(s₂−s₄)`, corpus §23.1 instance 2) land on `+2`; connes flags this in C2's "subtlety." The cross-domain reading: this is not an accident — BOTH are `d_A=0` SECOND-order objects, and `+2` is the generic non-scalar degree for a `d_A=0` second-derivative / two-pole / `d=4` heat-trace object. A FIRST-derivative `d_A=0` object (n_s) is scalar; a SECOND-derivative `d_A=0` object is `+2`. So the "safe-looking match" is a real structural regularity (second-order `d_A=0` observables share `+2`), and the bug is that a `d_A=+1` FIRST-order temperature was force-fit into that regularity by a name-only import. The emergence: the `+2` collision is a *correct* fact about `d_A=0` second-order observables, mis-applied to a `d_A=+1` first-order one — which is why M1's band test is the right adjudicator, not a degree re-derivation. The degree `+2` was right for `d_s`; the live question is whether T's OWN admissible degree lands T's band, and (M1) it does not.

#### Re: C3 — per-dimensional-class admissibility rule

**AGREE** with the DIMENSIONAL-CLASS ADMISSIBILITY RULE as derived (the `B = (M_KK-scale leg)^{d_A} ⊙ (dimensionless morphism)` decomposition; `d_A=0` ⇒ trivial scale leg + morphism-only; `d_A=1` ⇒ non-trivial `M_KK^1` scale leg carrying the 54.04-decade conversion). The factor-separation cleanly diagnoses C2's error: `+2` lived in the dimensionless-morphism slot (where it belongs for α_s) and was conflated with the scale-leg slot (where T's `+1` lives). I reproduce connes's H₀ chain: `ΔH₀/H₀` is `[H]−[H] = d_A=0`, so its transport CANNOT invoke the 54.04-decade scale leg, the `+2` full-homogeneity reading is dimensionally inadmissible, and the relief is bounded by the dimensionless morphism (0.0049, scalar a₂-clock). All agreed.

**DISAGREE — sharply — on the SIGN of the residual, and this is the band-binding crux (Q-C-1).** connes's C3 closes with "T's admissible degree is +1 … STILL does not reach the band — it overshoots by ~28 decades," and the workshop charge asks me to test whether a "substrate-natural NON-SCALAR dimensionless morphism … supplies the residual ~28-decade **descent**." **The residual is not a descent — it is an ASCENT.** I ran the integer-degree images at RealField(120):

```
[Sage] band geo-center = 4769.70 K; descent needed (T_bare → band) = 25.871 dec
  deg=0 (scalar):   T image log10 = +29.550  ⇒ residual_to_band = +25.871 dec  (too HOT,  must DESCEND)
  deg=1 (d_A,M_KK): T image log10 = −24.490  ⇒ residual_to_band = −28.169 dec  (too COLD, must ASCEND)
  deg=2 (imported): T image log10 = −78.530  ⇒ residual_to_band = −82.209 dec  (way too COLD)
  eff deg to land band center = 25.871 / 54.04 = 0.47874   (SUB-SCALAR: 0 < 0.4787 < 1)
```

The structural fact connes's "overshoot by ~28 decades" phrasing buries: **the band sits SANDWICHED strictly between the deg=0 image (+25.87 dec too hot) and the deg=1 image (−28.17 dec too cold).** The band-landing degree `0.4787` is *sub-scalar* — between 0 and 1 — not above 1. So the residual a morphism would have to supply on top of the deg=+1 scale leg is a **+28.17-decade ASCENT** (the scale leg overshoots DOWNWARD; the morphism must reverse it part-way back UP). The charge's "residual ~28-decade descent" has the sign inverted.

This MATTERS for Q-C-1, and it tightens connes's negative rather than loosening it. The transport kernel is `|κ| < 1` (that is the entire reason T comes down at all — it is the `sign_verdict=PASS` in the verdict file, line 88: "kernel<1 ⇒ T decreases"). A morphism that *ascends* would need `|κ| > 1` on its leg — the OPPOSITE sign from the one that makes the sign-verdict PASS. So the only substrate-natural channel connes left open in Q-C-1 (a non-scalar morphism on top of deg=+1) is **sign-foreclosed**: to land the band from the deg=+1 image, the morphism must push T back UP, but the substrate transport that the framework actually exhibits pushes T DOWN. You cannot have a `|κ|<1` scale leg AND a `|κ|>1` morphism on the SAME substrate-natural transport without a sign reversal that is not substrate-natural — it would be a fitted dial, the exact knob CF3/CO34 flag they lack.

**There IS one substrate-natural channel that survives this sign argument — and it points to deg=0, not deg=+1.** The band-landing degree `0.4787` is between deg=0 and deg=+1, i.e. it can be reached EITHER as (deg=+1 scale leg − a +28-dec ascent morphism) OR as (deg=0 scalar + a +25.87-dec DESCENT morphism). The second decomposition is sign-consistent with `|κ|<1` (a descent morphism on top of a no-op scale leg). But deg=0 is the dimensionally WRONG scale leg for a `d_A=+1` temperature (it is the H₀-class leg). So the band is reachable by a sign-consistent morphism ONLY at the dimensionally-inadmissible scale leg, and dimensionally-admissibly (deg=+1) ONLY by a sign-INCONSISTENT ascent morphism. **Either way the substrate-natural transport cannot land it: dimensional admissibility and sign-consistency are mutually exclusive for the LRD-T band.** That is a strictly sharper foreclosure than "no integer degree lands it" — it is "no substrate-natural transport (integer or morphism) simultaneously satisfies `deg(B)=d_A` AND `|κ|<1`." This is my band-binding steelman's verdict: I tested the open channel connes flagged and it is closed, for a reason his degree-only analysis did not surface (the sign of `κ`, which is a cosmological-bridge / transport-physics fact, not an NCG homogeneity fact).

**MISSED — the H₀ fence is quantitatively tighter than C3 states, and it cuts both ways.** C3 says the scalar relief 0.0049 is "a genuine PARTIAL relief but does NOT close the ~9% tension." Precisely: `[Sage] 0.0049 / 0.08 = 6.125%` — the substrate delivers exactly 6.1% of the shift needed to reach the band floor, requiring an 18.367× fitted multiplier (Sage-exact `7500000/408331`) which is `1.17%` of the full-homogeneity 108.08-decade budget. So the fence is: substrate-natural = 6% of the way there (far below), full-homogeneity = 10^107 past it (absurdly above), and the fitted knob lands in a 1.17%-of-budget needle between them. The cosmological-bridge reading: this is NOT the H₀-tension-resolving relief the timescape framing hoped for — 6% of a ~9% tension leaves ~8.4% unrelieved. But it is ALSO not zero: the a₂ focusing-clock genuinely moves H₀ in the right direction (`clock_coeff=−3.08 < 0 ⇒ voids clock faster ⇒ positive relief`, verdict line 100, sign PASS). So H₀ is a sign-PASS / magnitude-HELD partial, with the held fraction (~94% of the needed shift) being the honest number for the §7 surface.

**EMERGES — the volovik a₀-orthogonality wall and my κ-sign wall are the SAME wall, seen from two pillars.** The volovik Layer-1 wall (workingpaper:573): "neither moment pins a dimensionful H₀; a dimensionless ratio cannot close a dimensional gap." My κ-sign result is the *dimensionful* (T) analog: a dimensionful temperature's scale leg is forced to `deg=+1` (it DOES carry the gap, unlike H₀), but the sign of the carry (`|κ|<1`, downward) overshoots and cannot be reversed substrate-naturally. So: for H₀ (`d_A=0`) the wall is "no scale leg exists to carry a dimensionful relief" (volovik); for T (`d_A=+1`) the wall is "the scale leg exists and is sign-locked downward, overshooting the band" (mine). Both are the same structural statement — **the substrate's dimensional bookkeeping `Q = R·M_KK^m` rigidly fixes BOTH whether a scale leg exists (via `m`) AND its sign-direction (via `|κ|<1`), and neither degree of freedom is a free dial.** The two consumers fail for the two complementary halves of one `Q = R·M_KK^m` rigidity.

#### Re: C4 — classification + CF sharpening

**AGREE on the TWO-LAYER landing shape** (methodology layer §23 + substrate-physics layer §26, orthogonal per the `F(observable)` vs `F(rule)` Layer-Decomposition split). connes is right that this is not a single bucket. I AGREE the held magnitude is **NON-PROMOTION-BY-HELD-NUMBER, differentia = dimensionful-slot-collision**, companion to Member A (n_PBH) — and I confirm the genus predicate against corpus §26: P1 (the dimensional-class admissibility RULE is the proven structure) ∧ P2 (T_pivot and ΔH₀/H₀ not reachable knob-free) ∧ P3 (not sideways-re-pinned to the fitted knob). I also AGREE this is a §26 **ENRICH, NOT a K-counter advance** — corpus §26's "S95 W1-2 companion instance" precedent (K_csub_R) is explicit: a structurally-distinct firing of an EXISTING differentiator (dimensionful-slot-collision) enriches the corpus WITHOUT advancing the §26 K-counter. So §26 stays K=1. Agreed on Layer 2.

**DISAGREE — the §23 K=3 advancement is NOT clean, and connes's own cited corpus line forecloses it as he framed it.** This is the sharpest methodology dissent and it is Q-C-4. connes argues (C4) the DIMENSIONFUL transport-degree is the §23 K=3 instance, promoting §23 SUGGESTION → MANDATORY, with HIT `(i)∧(iv)` firing on the dimensional-class axis. I read the corpus differently, and the corpus text is on my side. The §23 status line (corpus :1685) and the K=2 distinctness paragraph (corpus :1731) BOTH say the K=3 advancement candidate is **a NEW OBSERVABLE — `r` (tensor-to-scalar) or `α_t` (tensor running)** — and corpus :1731 explicitly *retracts* a "K=2→K=3" narration as imprecise: *"resolving α_s's degree CONFIRMS instance 2 … it does NOT add a 3rd distinct observable … the W7-1/transit 'K=2→K=3' narration is imprecise."* The §23 K-counter advances on **a third structurally-distinct observable whose transport degree is independently extracted**, not on re-classifying the dimensional CLASS of the determination rule.

Here is the substantive problem with connes's HIT evaluation. He fires axis-(i) on "distinct on the DIMENSIONAL-CLASS axis." But the §23 K-counter's axis-(i) is **"distinct substrate-IS observable"** (corpus §3 / §23 :1731: "distinct substrate-IS observable: tensor tilt vs scalar running"). T (a temperature) IS a distinct observable from n_T and α_s — so axis-(i) plausibly fires on the OBSERVABLE, not on the dimensional class. The deeper issue is axis-(iv), **independent algebraic envelope**: the §23 instances are *transport-degree EXTRACTIONS via the `w(L_max)·κ(k)` factorization* (n_T proven non-scalar; α_s `factorization_holds=False`, deg=+2 Sage-locked). But for T, **no transport-degree was extracted** — the `+2` was IMPORTED (dedup-flag-iii, name-only), then the workshop DERIVED `+1` from `d_A` bookkeeping, NOT from a `w(L_max)·κ(k)` factorization on a T-channel npz. There is no T-channel factorization gate. So the §23 "instance" for T is a degree-DETERMINATION-by-dimensional-rule, not a degree-EXTRACTION-by-factorization — a structurally DIFFERENT KIND of evidence than the two existing instances. That is exactly the kind of "instance" the corpus §23 :1731 retraction was guarding against (confirming/re-classifying an existing structure ≠ adding a distinct extraction).

**My classification (the band-binding-informed verdict).** The dimensional-class admissibility RULE is real and is a genuine methodology output — but its correct home is **a corpus §18 / §23.0 DIRECTIVE EXTENSION (the per-observable transport-degree theorem is dimensional-class-INDEXED: `d_A=0` morphism-degree vs `d_A=1` scale-leg-degree), landing as a §23.0 sub-clause + a §18 cross-link**, NOT a §23 K-counter advancement to MANDATORY. Reasons: (1) the corpus explicitly reserves §23 K=3 for a new observable with an independent factorization-extracted degree (r / α_t); (2) T's degree was rule-derived not factorization-extracted, so it confirms/extends the THEOREM rather than adding a distinct transport-extraction instance; (3) and — the band-binding kicker — **the instance does not LAND** (Re:C3: dimensional-admissibility and sign-consistency are mutually exclusive for the T band). On connes's own Q-C-4 framing ("must the band be LANDED for the K-counter to advance?"), my answer is: for a K-counter whose calibration instances are *transport-degree determinations*, landing the band is NOT required (n_T's BLUE +0.4676 doesn't "land" any CMB band either — it's a prediction inaccessible to LiteBIRD by 540×, corpus :1729). BUT the instance must be a genuine *independent degree extraction*, and T's is not — it is a rule-application. So the foreclosure is on the EXTRACTION-distinctness axis, not the band-landing axis. **§23 stays SUGGESTION at K=2**; the dimensional-class rule lands as a directive extension (methodology content preserved, K-counter honesty preserved).

This is a genuine dissent from connes's C4 Layer-1, and it is the workshop's load-bearing methodology adjudication: connes reads the dimensional-class instance as the long-awaited §23 K=3 (→ MANDATORY); I read the corpus as reserving K=3 for an independently-extracted new-observable degree (r/α_t), making the dimensional-class instance a THEOREM-INDEXING directive extension at K=2. The two readings differ on what "calibration instance" means for the §23 K-counter — extraction-distinctness (mine, corpus-grounded) vs determination-distinctness (connes's). I hold the corpus-grounded reading.

**AGREE on "why NOT a new §VII.BA entry"** — §VII.BA / §18 is the parent framework invoked, not a new slot. The dimensional-class rule is the §18 Conjunct-1 homogeneity axis specialized to `d_A=1`; it lands as a §18/§23 corpus cross-link, not a fresh §VII.BA. Agreed.

**CF sharpening — I CONCUR with connes's two sharpenings and ADD the κ-sign pre-registration to each (this is the genuinely-new compute content):**

- **`CF-S111-CO34B-LRDT-TRANSPORT` (workingpaper:556).** connes's sharpening (pin deg=+1 a priori, verify, don't scan; pre-register HELD/INFO) is correct. I ADD: the CF MUST pre-register that the only remaining substrate-natural channel — a non-scalar morphism on top of deg=+1 — requires a **`|κ|>1` (ASCENDING) morphism** (Re:C3 Sage: residual = +28.17-dec ascent, NOT descent), which is sign-INCONSISTENT with the `|κ|<1` transport that gives the sign-PASS. So the CF's gate should test the **κ-sign-consistency predicate**: "is there a substrate-natural transport with `deg(B)=d_A=+1` AND `|κ|>1` on the morphism leg?" — and pre-register that this is expected FALSE (dimensional-admissibility ⊥ sign-consistency for the T band). The CF's real open compute is whether ANY substrate-natural object supplies an ascending morphism without a fitted dial; my analysis says no, but it is a falsifiable pre-registration, not a foregone conclusion. The CF's "What" field ("is T carried by a different power than running/tilt?") is answered: yes, `+1` not `+2` — but `+1` still misses, on the sign axis.

- **`CF-S111-CF3-H0-RESIDUAL` (workingpaper:565).** connes's sharpening (constrain to dimensionless-morphism channels; the `d_A=0` ratio has no scale leg; confirms the volovik a₀-orthogonality scope note) is correct and I CONFIRM it against the volovik audit (workingpaper:573): the a₀-draw is a dimensionless-Ô RELATION refinement, NOT a dimensionful budget. I ADD the quantitative fence: the substrate-natural scalar delivers `6.125% = 0.0049/0.08` of the needed shift (Sage-exact), so the CF's PASS criterion (full close to [0.08,0.10] knob-free) is expected to return INFO/HELD with ~94% of the shift unrelieved — the CF should pre-register the partial-relief fraction as the honest outcome and route the residual to dimensionless-slot (NOT dimensionful-slot — H₀ has no scale leg). The gate restatement under the volovik scope (a substrate-derived dimensionless RELATION that predicts ΔH₀/H₀ once `w=M_KK` is fixed by one observation) is the correct PASS criterion; this workshop pins WHY (no scale leg + the 6.125% fence).

### Part 2: Original Analysis

#### M1: Band-binding test — does ANY knob-free substrate-natural degree land [3500,6500] K (T) and [0.08,0.10] (H₀)?

**Charge:** Steelman band-binding. For the dimensionally-correct degree connes derives (or for the family of candidate degrees), RE-TEST: does the LRD photosphere temperature reach [3500,6500] K (band needs a 12.93-decade ratio; natural separation is 54.04 decades) and does the H₀ relief reach [0.08,0.10] — KNOB-FREE? Or do the magnitudes stay HELD even under the dimensionally-correct degree? Substitution-chain on every OOM-direction claim.

**Verdict of the band-binding steelman: NO substrate-natural transport lands either band — but the foreclosure is STRUCTURALLY RICHER than "the magnitudes are held." For T the obstruction is a SANDWICH + a κ-SIGN lock; for H₀ it is the absent scale leg + a 6.125% fence. I tested the channel connes left open in Q-C-1 and it is closed, for a transport-physics reason (the sign of κ) his degree-only analysis did not reach.**

**T (LRD photosphere temperature) — the SANDWICH structure (Sage RealField(120), independent of connes's run).**

I re-derived every integer-degree image and the band-landing effective degree from scratch:

```
[Sage] T_bare = 3.545e29 K; sep = 54.04 dec; band [3500,6500] K, geo-center 4769.70 K
  descent needed (T_bare → band center) = 25.871 dec   (to band_hi 6500: 25.737; to band_lo 3500: 26.006)
  band WIDTH = log10(6500/3500) = 0.269 dec   (the band is NARROW — 0.27 decades)

  deg=0 (scalar, dimensionally WRONG for d_A=1):  T_img log10 = +29.550 ⇒ +25.871 dec ABOVE band (too HOT)
  deg=1 (d_A, M_KK scale leg, dimensionally RIGHT): T_img log10 = −24.490 ⇒ −28.169 dec BELOW band (too COLD)
  deg=2 (imported, WRONG observable's degree):    T_img log10 = −78.530 ⇒ −82.209 dec BELOW band

  eff deg to land band center = 25.871 / 54.04 = 0.47874   ⇒  SUB-SCALAR: 0 < 0.4787 < 1
```

**Substitution chain — direction of every claim:**

```
Claim 1: "the band is SANDWICHED between the deg=0 and deg=1 images."
  Step 1: deg=0 image = T_bare (no transport) at log10 = +29.55 (BZ scale).
  Step 2: deg=1 image = T_bare·10^(−54.04) at log10 = −24.49.
  Step 3: band center log10 = +3.679 (4769.70 K).
  Step 4: +29.55 > +3.679 > −24.49  ⇒  band is strictly BETWEEN the two integer images. ∎
  ⇒ the band-landing degree 0.4787 is SUB-SCALAR (between 0 and 1), NOT super-scalar.

Claim 2: "the residual on top of deg=+1 is an ASCENT, not a descent."
  Step 1: deg=+1 image at log10 = −24.49 (band center at +3.679).
  Step 2: residual = (band − image) = +3.679 − (−24.49) = +28.17 dec.   [sign: image is BELOW band ⇒ must go UP]
  Step 3: [Sage] residual_to_band(deg=1) = −28.169 (in the "descent-needed" sign convention) ⇒ a NEGATIVE descent = ASCENT.
  Step 4: a morphism supplying +28.17 dec of ASCENT requires |κ_morphism| > 1.   [ascent ⇔ multiply UP ⇔ kernel>1] ∎

Claim 3: "an ascending morphism is sign-inconsistent with the substrate transport."
  Step 1: the substrate transport that makes T come down has |κ| < 1 (verdict line 88: "kernel<1 ⇒ T decreases"; sign_verdict=PASS).
  Step 2: an ascending morphism on the SAME transport needs |κ_morphism| > 1 (Claim 2 Step 4).
  Step 3: |κ|<1 (scale leg) ∧ |κ|>1 (morphism) on one substrate-natural transport ⇒ a sign reversal between legs.
  Step 4: a within-transport sign reversal is a FITTED dial (it is not forced by any substrate structure; it is exactly
          the "fitted ratio NOT substrate-natural" CO34/CF3 flag). ⇒ NO substrate-natural ascending morphism. ∎
```

**The mutual-exclusivity theorem (the band-binding steelman's actual result).** Decompose the band-landing degree 0.4787 two ways:
- **(A) deg=+1 scale leg − 0.5213·sep ascent morphism** = 0.4787·sep. Dimensionally ADMISSIBLE (`deg(B)=d_A=1`) but sign-INCONSISTENT (the −0.5213 leg is an ascent, `|κ|>1`).
- **(B) deg=0 scalar + 0.4787·sep descent morphism** = 0.4787·sep. Sign-CONSISTENT (descent, `|κ|<1`) but dimensionally INADMISSIBLE (deg=0 is the `d_A=0` H₀-class leg, wrong for a `d_A=1` temperature).

```
[Sage] decomposition (A): morphism on top of deg=1 = (0.47874 − 1)·54.04 = −28.169 dec  (ASCENT; |κ|>1)
[Sage] decomposition (B): morphism on top of deg=0 = (0.47874 − 0)·54.04 = +25.871 dec  (DESCENT; |κ|<1)
```

**Conclusion (T):** dimensional admissibility (`deg(B)=d_A`) and sign-consistency (`|κ|<1`, the transport the framework exhibits) are **MUTUALLY EXCLUSIVE for the LRD-T band**. No substrate-natural transport — integer degree OR non-scalar morphism — satisfies both. The channel connes flagged open in Q-C-1 (a non-scalar morphism on top of deg=+1) is foreclosed on the κ-sign axis, which is a transport-physics fact orthogonal to the homogeneity-degree axis his analysis covered. **The magnitude is HELD, and the foreclosure is stronger than "no integer degree lands it": it is "no `deg(B)=d_A`-admissible AND `|κ|<1`-consistent transport lands it."**

**H₀ relief — the absent-scale-leg + 6.125% fence (Sage-exact).**

```
[Sage] scalar a₂-clock relief ΔH₀/H₀ = 0.0049 (verdict line 100, clock_coeff=−3.08<0 ⇒ POSITIVE relief, sign PASS)
  band [0.08, 0.10]; center 0.09
  shortfall to band_lo:    0.08 / 0.0049 = 16.327×   (need 16.3× more)
  shortfall to band_center: 0.09 / 0.0049 = 18.367×   = Sage-exact 7500000/408331 (the fitted ratio, verdict line 101)
  substrate delivers FRACTION of needed shift:  0.0049 / 0.08 = 6.125%
  fitted knob as % of full-homog budget:  log10(18.367) / 108.08 = 1.264/108.08 = 1.17%
```

**Substitution chain (H₀ direction):**
```
Claim: "the substrate-natural H₀ relief is 6.125% of the needed shift; the band requires a fitted knob."
  Step 1: ΔH₀/H₀ is d_A=0 (ratio of two energies) ⇒ no M_KK scale leg (the +2 full-homog reading is inadmissible).
  Step 2: the ONLY substrate-natural transport is the dimensionless morphism = the a₂ focusing-clock = 0.0049.
  Step 3: 0.0049 / 0.08 = 0.06125 ⇒ 6.125% of the way to the band floor.
  Step 4: closing to 0.09 needs ×18.367 (Sage-exact 7500000/408331) — a fitted multiplier, 1.17% of the
          full-homog budget; NOT substrate-natural (natural_in_band=False). ∎
```

**Conclusion (H₀):** the relief is sign-PASS (clock moves H₀ the right way) / magnitude-HELD — substrate delivers 6.125% of a ~9% tension, leaving ~94% unrelieved. The fence: substrate-natural is far BELOW (6%), full-homogeneity is 10^107 ABOVE, the fitted knob threads a 1.17%-of-budget needle. **The magnitude is HELD.**

**Both bands HELD — and the held-ness has a unified structural origin (the band-binding steelman converges with connes's degree-by-dimension, but on a transport-physics floor he did not reach).** For H₀ (`d_A=0`): no scale leg exists, so the relief is capped at the dimensionless morphism (6.125%). For T (`d_A=+1`): the scale leg exists and is sign-locked downward (`|κ|<1`), overshooting; reversing it is a fitted dial. **The `Q = R·M_KK^m` dimensional bookkeeping rigidly fixes BOTH the existence of a scale leg (via `m`) AND its sign-direction (via `|κ|<1`), and neither is a free dial — that is the single wall both consumers hit, from the two complementary `d_A` halves.** This is my band-binding verdict: the magnitudes SURVIVE the dimensionally-correct extension as HELD numbers, exactly as connes's C3 convergence predicted — but the T foreclosure rests on the κ-sign lock (a cosmological-bridge / transport fact), not merely on the non-integrality of 0.4787 (an NCG fact). The two analyses converge on HELD; they reach it on orthogonal axes, which is why the joint workshop is stronger than either alone.

#### M2: Held magnitudes & NON-PROMOTION-BY-HELD-NUMBER — dimensionful-slot-collision differentia + falsifier-surface consequences

**Charge:** Apply the Non-Promotion-by-Held-Number Meta-Taxonomy (`cross-pillar-bridge-anatomy.md`): if NO substrate-natural degree lands either band, which differentia fires — dimensionful-slot-collision, undischarged-magnitude-bound, or sign-lock? Cross-check against the volovik a₀-orthogonality Layer-1 wall (workingpaper:573, "a dimensionless ratio cannot close a dimensional gap"). State the falsifier-surface / falsifier-master-inventory consequence (mack is sole writer of that surface).

**The two consumers fire DIFFERENT differentiae — and this is a genuine refinement of connes's C4 (which folded both into dimensionful-slot-collision).** The Non-Promotion-by-Held-Number genus (corpus §26: P1 STRUCTURE-permanent ∧ P2 NUMBER-held ∧ P3 not-sideways-re-pinned) holds for BOTH, but the 3-way differentia (dimensionful-slot-collision / undischarged-magnitude-bound / sign-lock) splits them:

**T (LRD-T) — fires TWO differentiae, dominantly sign-lock (a NEW reading vs connes's C4):**

```
P1 (STRUCTURE permanent): YES — the dimensional-class admissibility RULE (deg(B)=d_A, Wodzicki-unique) is proven.
P2 (NUMBER held):         YES — T_pivot ∈ [3500,6500] K not reachable knob-free (M1: mutual-exclusivity theorem).
P3 (not sideways-re-pinned): YES — T_pivot stays HELD, not re-pinned to a fitted dial.
Genus HOLDS.

Differentia — connes (C4) says dimensionful-slot-collision (same as Member A n_PBH). I REFINE:
  • dimensionful-slot-collision FIRES (corpus §26 Member A signature): the dimension prefactor (T's M_KK^1
    energy scale) and the transport-degree slot share ONE multiplicative M_KK^{d_A} structure — fixing deg=+1
    fixes the scale leg, and the scale leg IS the dimensionful magnitude's carrier. ✓ (connes is right this fires.)
  • BUT sign-lock ALSO FIRES, and it is the DECISIVE one (corpus §26 Member C signature): the substrate
    transport is sign-locked to |κ|<1 (DOWNWARD). Landing the band requires a |κ|>1 (UPWARD) morphism on the
    dimensionally-admissible deg=+1 leg (M1 Claim 2-3). The sign of the morphism's κ is locked by the same
    |κ|<1 transport-physics that gives sign_verdict=PASS — it cannot be reversed without a fitted dial. The band
    is unreachable not (only) because the dimension prefactor and divergence share a slot, but because the
    DIRECTION of the only admissible transport is fixed AGAINST the band.
```

So T is a **dual-differentia instance: dimensionful-slot-collision ∧ sign-lock**, with sign-lock dominant. This is structurally distinct from Member A (n_PBH), which is dimensionful-slot-collision ONLY (a power-law-divergent cardinality channel, no κ-sign content). The sign-lock here is NOT the corpus §26 Member C sign-lock (which is a combinatorial-fraction surrogate `R_surr=2f−1` with no cohomology content) — it is a *transport-κ* sign-lock, a NEW sub-species of the sign-lock differentia on the transport-physics axis. **This is a candidate §26 K-counter consideration** (a structurally-distinct firing — transport-κ sign-lock vs combinatorial-fraction sign-lock), which I flag for connes in M3: does a transport-κ sign-lock advance §26, or ENRICH the sign-lock differentia? My lean is ENRICH (per the §26 K_csub_R precedent: a distinct firing of an EXISTING differentiator enriches without advancing), keeping §26 at K=1 — but the κ-sign sub-species is novel enough to be worth the explicit M3 question.

**H₀ — fires dimensionful-slot-collision's COMPLEMENT (the absent-scale-leg case):**

```
P1∧P2∧P3: YES (STRUCTURE = a₀-orthogonality + dimensional-class rule; NUMBER = ΔH₀/H₀ held at 6.125%; not re-pinned).
Differentia: this is the VOLOVIK a₀-orthogonality Layer-1 wall directly (workingpaper:573): "a dimensionless ratio
  cannot close a dimensional gap." H₀ is d_A=0 ⇒ NO scale leg exists. The held-ness is NOT slot-collision (there is
  no dimensionful slot to collide with) — it is the ABSENCE of a dimensionful carrier. The relief is capped at the
  dimensionless morphism (6.125%). This is the dimensionful-slot-collision differentia's complement: collision says
  "the dimension and the divergence SHARE one slot"; absent-scale-leg says "there is NO dimensionful slot at all."
```

**Cross-check against the volovik Layer-1 wall (workingpaper:573): CONFIRMED, and the two consumers are the two HALVES of it.** The volovik wall states the H₀ (`d_A=0`) case exactly: "neither moment pins a dimensionful H₀; a dimensionless ratio cannot close a dimensional gap." The T (`d_A=+1`) case is the *dimensionful* complement the volovik wall did not need to state (because H₀ is dimensionless): a dimensionful T DOES have a scale leg, but the scale leg is sign-locked and overshoots. So the workshop ADDS the dimensionful half to the volovik Layer-1 wall: **`Q=R·M_KK^m` forbids closing the gap from EITHER side — `m=0` (no carrier, H₀) OR `m=1` (sign-locked carrier, T).** I will record this as the falsifier-surface synthesis.

**Falsifier-master-inventory consequence (I am SOLE WRITER; this round I ANALYZE the row — the edit is Round 2 Turn B).**

The row I would land is an **INVERTED-falsifier / held-prediction sub-row** on the LRD-T + H₀-relief surface, NOT a tension flag. Reasoning for the §7-surface tag:

- **It is a PREDICTION, not a falsification.** The structure (dimensional-class admissibility + κ-sign lock + a₀-orthogonality) is PERMANENT; the NUMBERS (T_pivot, ΔH₀/H₀) are HELD. Per `feedback_reporting-framing.md` and the corpus §26 NON-PROMOTION discipline, a held-number under a permanent structure is a prediction that the substrate-natural transport does NOT reach the observed band — it does not falsify the framework, it bounds what the framework natively predicts.
- **The T row is the more consequential one** (Re:C2 MISSED): the LRD-T band is a DIRECT astrophysical photosphere measurement (no relocatable substrate-sensitivity channel, unlike α_s). So the substrate prediction is concretely: *the LRD photosphere temperature is NOT reproduced by a knob-free substrate-natural transport of T_bare; a substrate-natural transport that satisfies `deg(B)=d_A=+1` is sign-locked to overshoot the band by ~28 decades.* This is a clean, falsifiable, INVERTED prediction (the framework predicts the substrate-natural channel CANNOT produce the LRD-T band — if a future derivation FOUND a knob-free transport landing it, THAT would contradict the κ-sign-lock theorem). The falsifier content is the κ-sign-lock theorem itself.
- **The H₀ row** is a sign-PASS / magnitude-HELD partial: substrate delivers 6.125% of the ~9% tension. The §7 surface tag is "partial relief, ~94% held; NOT the H₀-tension resolution" — honest about both the genuine directional relief AND the held remainder. This connects to the standing WS-CC-H0 interlock (my MEMORY: H₀=67.40 anchor-degeneracy, the shared rank-1 `w=M_KK` import) — the a₂-clock relief is a₀-ORTHOGONAL (does not consume the a₀ CC budget, verdict line 103), so it is a genuine independent partial, not a re-counting of the CC channel.
- **Row STRUCTURE**: audit-pin sub-rows (the 1.dovekie pattern, my MEMORY S110 W4b precedent — additive sub-rows, NO existing row rewritten), citing the W3 mint SHA (`f60cff36…`, S110-CF-CV6B-DS-M4) AND the two W4 consumer SHAs (`2a654897…` CO34-legB, `7bfda02a…` CF3-H0) AND this workshop's verdict. The values live in the registry (AMRI — NOT in agent memory). I pre-state the row content here for connes's Round-2 cross-check; I land it in Round 2 Turn B after convergence/dissent settles the §23-vs-directive-extension classification (which determines whether the row cites a §23 K=3 instance or a §23.0 directive extension — my M1/Re:C4 reading is the latter).

**Net M2 verdict:** NON-PROMOTION-BY-HELD-NUMBER, genus confirmed for both consumers; T fires dimensionful-slot-collision ∧ **sign-lock (transport-κ, dominant, a refinement of connes's single-differentia C4 reading)**; H₀ fires the absent-scale-leg complement of dimensionful-slot-collision (= the volovik Layer-1 wall directly). §26 stays K=1 (ENRICH, both consumers). Falsifier-surface: INVERTED held-prediction sub-rows (T: κ-sign-lock theorem as the falsifier content; H₀: 6.125% partial relief, ~94% held), landed Round 2 Turn B.

#### M3: Questions for connes

**Q-M-1 (the κ-sign foreclosure — does it survive your NCG read of the morphism?).** My band-binding result (M1) is that the residual on top of deg=+1 is a +28-decade ASCENT requiring `|κ_morphism|>1`, which is sign-inconsistent with the `|κ|<1` transport that gives sign_verdict=PASS — so the channel you left open in Q-C-1 is foreclosed on the κ-sign axis. From the NCG side: is there ANY substrate-natural structural morphism (an HKR cohomology-class ratio, a K_0-pairing, a same-class pole ratio per your §18 T3/T4|_{s≠s'}/T5) that can carry `|κ|>1` (amplitude GROWTH across scales) while remaining substrate-natural — or is amplitude-growth itself non-substrate-natural for a transport factor (which would make the κ-sign foreclosure a theorem, not just an observation)? Concretely: can a T4|_{s≠s'} ratio `Res_W(s)/Res_W(s')` with `s'<s` produce `|κ|>1`, and would that be admissible for a `d_A=+1` anchor?

**Q-M-2 (the §23 K-counter classification — extraction-distinctness vs determination-distinctness).** I read corpus §23 (:1685, :1731) as RESERVING K=3 for a new observable whose transport degree is independently EXTRACTED via `w(L_max)·κ(k)` factorization (r / α_t), and the dimensional-class instance as a degree-DETERMINATION-by-rule (no T-channel factorization gate exists) — so it lands as a §23.0/§18 DIRECTIVE EXTENSION at K=2, NOT a K=3 advancement to MANDATORY. You (C4) read it as the long-awaited K=3 on the dimensional-class axis (→ MANDATORY). The corpus :1731 explicitly retracted a prior "K=2→K=3" narration as imprecise on exactly this distinction (confirming an existing structure ≠ adding a distinct extraction). Do you concede the dimensional-class instance is a THEOREM-INDEXING directive extension (extraction-distinctness not met), or do you hold that determination-by-dimensional-rule is itself a sufficient new calibration instance? This is the workshop's load-bearing methodology adjudication and we must converge or dissent explicitly.

**Q-M-3 (transport-κ sign-lock — §26 advance or ENRICH?).** I find T fires a NEW sub-species of the sign-lock differentia (transport-κ sign-lock, distinct from the corpus §26 Member C combinatorial-fraction sign-lock). My lean is ENRICH (§26 stays K=1, per the K_csub_R "distinct firing of existing differentiator" precedent). But the transport-κ sign-lock is on a different axis (transport-physics) than Member C's surrogate-combinatorics. Does it advance §26 to K=2 (distinct firing sub-test on the 3-way discriminator) or ENRICH the sign-lock member (no advance)? I want your read before I land the falsifier row, since it sets whether the row cites a §26 ENRICH or a §26 K=2.

**Q-M-4 (the dimensional-class RULE's home — §18 cross-link vs §23.0 sub-clause vs both).** We agree the dimensional-class admissibility rule (`d_A=0` morphism-degree vs `d_A=1` scale-leg-degree) is a real methodology output and NOT a new §VII.BA slot. Where does it LAND? My read: a §23.0 sub-clause (extending the per-observable transport-degree theorem to be dimensional-class-indexed) WITH a §18 Conjunct-1 cross-link (it is the homogeneity axis specialized to `d_A=1`). Do you concur, or do you see it as primarily a §18 extension (since `deg(B)=d_A` is the §18 object) with a §23 pointer? This sets the Effected-In-Session landing target.

---

## Round 2 — connes: Follow-up

### CONVERGENCE

Three things changed from Round 1. The first is the largest and I lead with it.

**(1) I ACCEPT the κ-sign mutual-exclusivity theorem (Re:C3 + M1), and I UPGRADE it from "observation" to "theorem" on the NCG side — answering Q-M-1 in mack's favor and then strengthening it.** In C3/Q-C-1 I left ONE channel open: a substrate-natural NON-SCALAR dimensionless morphism on top of the `deg=+1` scale leg, supplying the residual descent. I described that residual as a "~28-decade descent." mack's RealField(120) sandwich (Re:C3) corrects the SIGN: the `deg=+1` image sits at log10 = −24.49, the band center at +3.679, so the residual is a **+28.17-decade ASCENT**, requiring `|κ_morphism| > 1` — the opposite sign from the `|κ|<1` transport that yields `sign_verdict=PASS`. mack is right that my Q-C-1 channel is sign-foreclosed, and the sign of κ is a transport-physics fact my degree-only homogeneity analysis did not reach. **What changed in my position: the band-landing degree 0.4787 is SUB-scalar (0 < 0.4787 < 1), not super-scalar; I had the residual's sign inverted, and the corrected sign closes the channel I thought I had left open.** I concede this cleanly.

I do not merely concede — I close the residual loophole mack flagged for me. Q-M-1 asks whether ANY substrate-natural NCG morphism (HKR ratio, K₀-pairing, same-class pole ratio `T4|_{s≠s'}` per §18) can carry `|κ|>1` (amplitude GROWTH) for a `d_A=+1` anchor. The answer is **NO, and it is a theorem from Wodzicki index-rigidity** (full chain in QUESTIONS, Q-M-1). Two independent NCG obstructions:

- A same-class Wodzicki ratio `Res_W(s)/Res_W(s')` has homogeneity degree `−2(s−s')` (Sage-exact this round). Under the physical substrate→pivot rescale `t = M_KK/k_4D = 10^54.04 > 1`, every such factor with `s'<s` gives `|κ| = 10^(−108.08) ≪ 1` — DECAY. To force `|κ|>1` you need `s'>s`, which is the SAME ratio relabeled (numerator/denominator swap); there is no substrate-natural asymmetry selecting the growth orientation.
- The deeper obstruction is **parity**: a `d_A=+1` temperature needs `deg(B) = +1` (a SINGLE `M_KK` power, ODD), but a two-pole Wodzicki ratio delivers only EVEN degrees `{…,−4,−2,0,+2,…}`. A two-pole morphism cannot even MATCH `d_A=+1`, let alone supply the `|κ|>1` ascent on the `+1` leg.

So the κ-sign foreclosure mack found from the transport side is reinforced by an orthogonal NCG-side foreclosure (Wodzicki degree-rigidity + integer-parity). **Amplitude-growth `|κ|>1` is non-substrate-natural for a transport factor; the κ-sign mutual-exclusivity is a THEOREM.** This is genuine cross-pollination: mack's transport-κ axis and my Wodzicki-rigidity axis foreclose the SAME open channel independently, which is strictly stronger than either alone (it is a PASS-AND across two structurally-distinct axes, in the joint-theorem-promotion sense).

**(2) I ACCEPT mack's dual-differentia refinement (Re:C4 + M2): T fires dimensionful-slot-collision ∧ sign-lock, with sign-lock DOMINANT.** My C4 folded T into a single differentia (dimensionful-slot-collision, companion to Member A n_PBH). mack is right that this UNDER-reads it: the decisive obstruction is not that the dimension prefactor and the transport span share one `M_KK^{d_A}` slot (that fires, but it is the weaker leg) — it is that the DIRECTION of the only admissible transport (`|κ|<1`, downward) is locked AGAINST the band, and reversing it is a fitted dial. Member A (n_PBH) is dimensionful-slot-collision ONLY (a power-law-divergent cardinality channel, no κ-sign content); T carries an additional, dominant sign-lock that n_PBH does not. I withdraw my single-differentia C4 reading in favor of mack's dual `dimensionful-slot-collision ∧ sign-lock (transport-κ)`. The Wodzicki-parity result in (1) is what makes the sign-lock irreversible substrate-naturally, so I am not merely agreeing — I am supplying the NCG mechanism for why the sign cannot be reversed.

**(3) I ACCEPT the LRD-T direct-measurement context (Re:C2 MISSED) as load-bearing for the falsifier-surface tag.** I treated `[3500,6500] K` as a given band. mack's domain correctly weights it: it is a DIRECT JWST photosphere measurement (Balmer-break + V-shaped SED; ~3500 K Hayashi boundary, ~6500 K Balmer-break weakening), with NO relocatable substrate-sensitivity channel — unlike α_s, where the substrate value relocates OFF the Planck pivot to a CMB-S4/CMB-HD channel. This changes the EPISTEMIC TYPE of the held number (per `output-standards.md §"Numerical vs Structural"`): T's held magnitude is a hard miss against direct data, not a relocatable scale-mismatch, so the falsifier-surface row is the more consequential of the two. I had not internalized that the absence of a relocation channel is what makes T's held-ness falsifier-grade. This is mack's sole-writer domain and I defer to his framing of the §7 stakes.

### DISSENT

**On the §23 K=3 classification (Q-M-2) — I CONCEDE. mack has the corpus text, and on re-reading :1731 against the actual evidence-KIND for T, my C4 Layer-1 was wrong.** This is the workshop's load-bearing methodology adjudication, so I give the resolved verdict in full, with the reasoning that moved me — not a bare concession.

My C4 claimed the dimensionful transport-degree is the long-awaited §23 K=3 instance, HIT `(i)∧(iv)` firing on the dimensional-class axis, promoting §23 SUGGESTION → MANDATORY. mack reads the corpus as reserving K=3 for a NEW OBSERVABLE whose transport degree is independently EXTRACTED via the `w(L_max)·κ(k)` factorization (r / α_t), and cites :1731's explicit retraction of a prior "K=2→K=3" narration. I re-read :1731 verbatim and tested my own HIT evaluation against it. mack is right, for three reasons that compound:

**(a) The corpus axis-(iv) is EXTRACTION-distinctness, and T fails it.** Corpus :1731 states the n_T/α_s instances are distinct on axis-(iv) by "independent transport-factor-degree EXTRACTION — n_T proven non-scalar via the LiteBIRD discrimination; α_s's degree now RESOLVED NON-SCALAR `+2` via the S93 W7-1 two-pole … triad." Both existing instances have a transport degree *extracted from a compute on that observable's own channel* (the `w(L_max)·κ(k)` factorization — `factorization_holds=False` for α_s, a windowed-trace-shape computation). For T, **no transport degree was extracted**: the `+2` was IMPORTED by name (dedup-flag-iii), and this workshop then DERIVED `+1` from `d_A` bookkeeping (`Q = R·M_KK^m` mass-dimension counting). There is no T-channel factorization gate. So T's degree is determination-by-rule, not extraction-by-factorization. On the corpus's OWN axis-(iv) definition, T is not axis-(iv)-distinct — it is a rule-application of the existing theorem, exactly the evidence-KIND :1731 guards against ("confirming an existing structure ≠ adding a distinct extraction"). My C4 axis-(iv) — "the d_A=1 scale-leg degree is not a numerical refinement of the d_A=0 morphism degree" — re-read the axis as *determination*-distinctness (a different degree-VALUE via a different bookkeeping), which is not what the corpus means by it.

**(b) :1731 already retracted exactly this move.** The line reads: "resolving α_s's degree CONFIRMS instance 2 … it does NOT add a 3rd distinct observable … the W7-1/transit 'K=2→K=3' narration is imprecise (α_s IS instance 2, not a 3rd instance)." That is the precedent: re-classifying or re-determining the degree of an object the theorem already covers does NOT advance the K-counter. The dimensional-class rule re-determines (via `d_A`) the degree that the per-observable theorem already governs — it is a THEOREM-INDEXING refinement (the theorem is now dimensional-class-indexed), which is structurally the same KIND of event as the α_s degree-resolution that :1731 explicitly held at K=2. To call T a K=3 advancement while :1731 holds α_s's full degree-resolution at K=2 would be inconsistent — α_s's resolution was a HARDER, factorization-grounded result and it did not advance the counter.

**(c) The band-binding kicker is real but it is NOT my reason for conceding.** mack adds that the instance "does not LAND" (the κ-sign mutual-exclusivity). I want to be precise here so the verdict is clean: I do NOT concede on band-landing grounds, and I AGREE with mack's own caveat that band-landing is not the K-counter criterion (n_T's BLUE `+0.4676` does not land any CMB band either, yet it is a settled K-instance — corpus :1729). The decisive reason is (a)+(b): EXTRACTION-distinctness is the corpus criterion, and T's degree was not extracted. Band-landing is downstream colour, not the gate. I flag this to keep the concession grounded in the right axis — if I conceded "because it doesn't land," that would mis-state the K-counter criterion and could be mis-cited later.

**Resolved verdict on Q-M-2: §23 stays SUGGESTION at K=2.** The dimensional-class admissibility rule is a real methodology output, but its correct home is a **§23.0 DIRECTIVE EXTENSION** (the per-observable transport-degree theorem is now dimensional-class-INDEXED: `d_A=0` → morphism-degree; `d_A=1` → `M_KK`-scale-leg-degree) **WITH a §18 Conjunct-1 cross-link** (it is the homogeneity axis specialized to `d_A=1`) — NOT a §23 K-counter advancement to MANDATORY. This concedes mack's extraction-distinctness reading over my determination-distinctness reading, on the merits, with :1731 as the controlling text. The K-counter honesty is preserved; the methodology content (the rule) is preserved as a directive extension; nothing is lost except my over-claim of MANDATORY promotion.

**Where I still hold a sharpening (not a dissent — a precision on mack's M2).** mack reads the §23 K=3 candidate slot as still reserved for r / α_t. I AGREE, with one addition that should be recorded so the slot is not mis-occupied later: the dimensional-class directive extension is now a PRECONDITION on any future r / α_t K=3 instance — a future r-channel transport-degree extraction MUST declare its `d_A` (r and α_t are both `d_A=0`, so they extract a MORPHISM degree, and the extraction gate must verify it is a morphism-degree not a scale-leg-degree). This is not a dissent from mack; it sharpens the K=3 slot's pre-registration so the dimensional-class axis is checked at extraction time. I flag it for the Effected-In-Session §23.0 directive-extension text.

### EMERGENCE

**E1 — The two consumers are the EVEN/ODD parity halves of one `Q = R·M_KK^m` wall, and the parity is the deep structure.** mack's M2 already gave the unified reading: H₀ (`m=0`, no scale leg) and T (`m=1`, sign-locked scale leg) are the two complementary halves of the `Q = R·M_KK^m` rigidity. The Wodzicki-parity result (CONVERGENCE 1) sharpens WHY the halves are complementary and not bridgeable: a temperature's admissible degree is `+1` (ODD), but every substrate-natural NCG morphism that could supply a corrective re-weighting (Wodzicki two-pole ratio, HKR cohomology-class ratio) carries an EVEN degree (`−2(s−s')`, or `0` for HKR). So the morphism sector and the scale-leg sector live in DIFFERENT PARITY CLASSES. A `d_A=0` observable (H₀, n_s, α_s) is transported entirely within the EVEN sector (scalar `0` or morphism `+2`) — which is why the framework's `d_A=0` successes (n_s scalar; α_s `+2`) all sit at even degree. A `d_A=+1` observable needs the ODD sector, which only the bare `M_KK^1` scale leg provides — and that leg is sign-locked. **The substrate cannot lend an even-degree morphism to fix an odd-degree scale-leg's overshoot: the parity mismatch is the structural reason the two `Q=R·M_KK^m` halves never meet.** This is new content from the cross-pollination — neither the volovik a₀-orthogonality wall (which is stated for `d_A=0` only) nor mack's transport-κ sign-lock (stated for magnitude/direction) carried the parity observation; it emerges only when the Wodzicki degree-rigidity (NCG axis) is laid against the `d_A` dimensional bookkeeping (cosmological-bridge axis).

**E2 — "scalar-looking match" detection should pin BOTH `d_A` AND degree-PARITY.** mack (Re:C2 EMERGES) noted the `+2` collision is a real regularity: second-order `d_A=0` objects (M4 `d/2` heat-trace; α_s `(a₄/a₂)²` two-pole) generically share `+2`, and the bug was force-fitting a `d_A=+1` first-order T into it by name-only import. E1 adds the cleaner detector: the import was undetectable because `deg_T=2.0` is EVEN and EVEN-ness is shared across the entire `d_A=0` morphism sector — the number "looks right" precisely because it is in the wrong parity class for T but the right one for the `d_A=0` siblings. A dimensional-class pin that recorded `(d_A, degree-parity)` together would have flagged the import at consumption: T (`d_A=+1`, needs ODD) ≠ `deg_T=2.0` (EVEN). I record this as a sharpening of mack's proposed fifth axis (the transported-observable mass-dimension pin, Re:C2): the pin should carry `(d_A, deg, parity-class)`, not `d_A` alone, because parity is the invariant that the name-only import silently crossed.

**E3 — A clean falsifier-surface statement of the T held-prediction, in substrate-first form.** Combining mack's direct-measurement framing (CONVERGENCE 3) with the parity theorem (E1): the substrate's prediction is not "T overshoots" but the structurally sharper *the LRD photosphere temperature cannot be produced by ANY substrate-natural transport of `T_bare`, because the only admissible (ODD, `d_A=+1`) transport is the sign-locked `M_KK^1` scale leg, and every even-degree morphism that could correct its overshoot is in the wrong parity class to act on it.* Direction of explanation preserved (`phononic-framing.md`): `D_K` eigenvalues → `T_bare` substrate-scale temperature → read THROUGH the `deg=+1` scale leg → overshoots the JWST band; the substrate IS `T_bare`, the band is its pivot image, and the transport is read-through not field-propagation. The falsifier content (mack's sole-writer domain) is the conjunction `κ-sign-lock theorem ∧ Wodzicki-parity theorem` — if a future derivation found a knob-free transport landing `[3500,6500] K`, it would have to break ONE of the two, and naming WHICH it breaks is the falsifier-surface test.

### QUESTIONS

**Answer to Q-M-1 (does the κ-sign foreclosure survive my NCG read of the morphism? — YES, as a theorem).** Full substitution chain, Sage-verified this round:

```
Claim: "No substrate-natural NCG morphism can carry |κ|>1 (amplitude growth) for a d_A=+1 anchor;
        amplitude-growth is non-substrate-natural for a transport factor."

Step 1 (definitions):
  - A substrate-natural transport morphism on (A_K,H_K,D_K) is built from the unique Wodzicki trace
    Res_W (Connes 1994 §2.3) and/or HKR cohomology-class ratios (orientability axiom + Chern character).
  - Under the physical substrate→pivot readout, the spectral rescale is D_K → t·D_K with
    t = M_KK/k_4D = 10^{+54.04} > 1  (UV substrate scale / IR pivot scale; this is the ONE rescale
    that probes degree, and its DIRECTION is fixed by the substrate-IS framing: the observable lives at M_KK).
  - |κ| := magnitude of the transport factor under this rescale.

Step 2 (substitute — same-class Wodzicki two-pole ratio, the §18 T4|_{s≠s'} candidate):
  - Res_W(D_K^{-2s}) → t^{-2s}·Res_W(D_K^{-2s})   [homogeneity degree −2s; Res_W a TRACE, scalar-linear]
  - ratio R(s,s') = Res_W(s)/Res_W(s') → t^{-2(s-s')}·R(s,s')
  - deg(R) = −2(s−s')                            [Sage: ratio homogeneity degree = -2*s + 2*sp, EXACT]

Step 3 (simplify — read |κ| for s'<s under t>1):
  - s=3, s'=2: deg = −2 ⇒ |κ| = (10^54.04)^{−2} = 10^{−108.08} ≪ 1   [Sage]
  - s=4, s'=3: deg = −2 ⇒ |κ| = 10^{−108.08} ≪ 1                      [Sage]
  - to get |κ|>1 needs deg>0 ⇒ s'>s ⇒ the SAME ratio with numerator/denominator swapped
    (no substrate-natural asymmetry selects which pole is numerator; the anchor does not supply one).

Step 4 (read off — TWO independent obstructions to |κ|>1 on a d_A=+1 leg):
  (4a) DIRECTION: every same-class ratio with a fixed pole ordering gives |κ|<1 under t>1 (Step 3).
       Amplitude GROWTH (|κ|>1) is not produced by a unique-trace morphism in the physical direction.
  (4b) PARITY: a d_A=+1 anchor requires deg(B)=+1 (a single M_KK power, ODD). A Wodzicki two-pole
       ratio gives deg = −2(s−s') ∈ {…,−4,−2,0,+2,…} (EVEN, integer poles); HKR gives 0 (EVEN).
       So no Wodzicki/HKR morphism can even MATCH d_A=+1 — parity mismatch — let alone supply |κ|>1.
  Conclusion: amplitude-growth |κ|>1 is non-substrate-natural for a transport factor, AND no
  substrate-natural morphism reaches the ODD degree a temperature needs. The κ-sign foreclosure is a
  THEOREM (Wodzicki degree-rigidity + integer-parity), not merely the observation that the framework's
  exhibited transport happens to have |κ|<1. ∎
```

Direct answer to the concrete sub-question mack posed: a `T4|_{s≠s'}` ratio `Res_W(s)/Res_W(s')` with `s'<s` produces `|κ| = 10^{−108.08} ≪ 1` (DECAY, not growth), and it is **not** admissible for a `d_A=+1` anchor — its degree is EVEN (`−2(s−s')`), parity-incompatible with the ODD `+1` a temperature needs. So the channel I left open in Q-C-1 is doubly closed (sign AND parity). The κ-sign mutual-exclusivity is a theorem.

**Answer to Q-M-2 (extraction-distinctness vs determination-distinctness — I CONCEDE).** Resolved in DISSENT above: §23 stays SUGGESTION at K=2. mack's extraction-distinctness reading is correct and corpus :1731 is the controlling text — T's degree was rule-DERIVED from `d_A` bookkeeping, not factorization-EXTRACTED on a T-channel gate (none exists), so it is a §23.0/§18 DIRECTIVE EXTENSION at K=2, NOT a K=3 advancement to MANDATORY. The dimensional-class rule lands as a §23.0 directive extension (dimensional-class-indexed transport-degree theorem) + a §18 Conjunct-1 cross-link. I do not hold determination-by-rule as a sufficient calibration instance; the corpus reserves the K-counter for independent degree EXTRACTIONS (r / α_t). This is the clear resolved verdict mack needs for the Workshop Verdict + Wrap-Up.

**Answer to Q-M-3 (transport-κ sign-lock — §26 advance or ENRICH? — ENRICH; §26 stays K=1).** I concur with mack's lean, and the Wodzicki-parity result (Q-M-1) gives the structural reason it is ENRICH and not a K=2 advance:

The corpus §26 differentia is a 3-WAY discriminator (dimensionful-slot-collision / undischarged-magnitude-bound / sign-lock). mack's transport-κ sign-lock and Member C's combinatorial-fraction sign-lock (`R_surr = 2f−1`) are BOTH instances of the SAME differentia member (sign-lock) — they differ in the AXIS that locks the sign (transport-κ direction vs surrogate-combinatorics), not in WHICH of the three differentiae fires. Per the §26 ENRICH precedent (the K_csub_R "S95 W1-2 companion instance": a structurally-distinct firing of an EXISTING differentiator enriches the corpus WITHOUT advancing the §26 K-counter), a second sub-species of the sign-lock member ENRICHES sign-lock, it does not add a fourth differentia or advance the 3-way discriminator. **§26 stays K=1.** The transport-κ sign-lock is recorded as a NEW SUB-SPECIES of the sign-lock differentia (the first one with cohomology/transport content — Member C's is a pure combinatorial surrogate with no cohomology, corpus §26), worth an explicit corpus annotation under the sign-lock member, but NOT a K-counter event. So the falsifier row mack lands cites a §26 ENRICH (sign-lock sub-species), not a §26 K=2. This is consistent with my Q-M-2 concession: BOTH layers stay at their current K (methodology §23 at K=2 directive-extension; substrate-physics §26 at K=1 enrich) — the workshop's structural output is two directive/corpus extensions, zero K-counter advancements. That is the honest two-layer landing.

**Answer to Q-M-4 (the dimensional-class rule's home — §23.0 sub-clause + §18 cross-link; I CONCUR).** Your read is correct and I adopt it as the Effected-In-Session landing target: the dimensional-class admissibility rule lands PRIMARILY as a **§23.0 sub-clause** (it extends the per-observable transport-degree theorem to be dimensional-class-indexed — `d_A=0` ⇒ morphism-degree carried by the dimensionless structural morphism; `d_A=1` ⇒ scale-leg-degree carried by the `M_KK^1` unit-conversion leg), WITH a **§18 Conjunct-1 cross-link** (it is the `deg(B)=d_A` homogeneity axis specialized to the dimensionful class — §18 is the parent object, §23 is the per-observable specialization the rule directly extends). Rationale for §23.0-primary over §18-primary: the rule's OPERATIVE content is the per-observable transport-degree determination (a §23 object — "which degree does THIS observable's transport carry"), and §18's `deg(B)=d_A` is the homogeneity THEOREM it invokes, not the per-observable bookkeeping it extends. So §23.0 is the home, §18 is the cited parent. The verbatim directive-extension text + the orchestrator-reserved parent-rule mirror (the `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"` per-observable transport-degree cross-link, which is subagent-edit-denied) should be recorded in your Effected-In-Session block as an orchestrator-reserved hand-off line — do not attempt the `.claude/rules/` edit; flag it for the orchestrator.

**Final sharpening for mack's closing synthesis (one item).** When you land the falsifier row and the §23.0 directive extension, please record the PARITY observation (EMERGENCE E1/E2) explicitly — that the morphism sector is EVEN-degree and the dimensionful scale leg is ODD-degree, so the two `Q=R·M_KK^m` halves are parity-separated. It is the single most reusable structural output of this workshop (it predicts that EVERY future `d_A=odd` observable will hit the same wall, not just T), and it is the precise content that makes the proposed fifth pin axis a `(d_A, deg, parity)` pin rather than a `d_A`-only pin. If you concur it belongs on the §7 surface as the falsifier-content generator (the conjunction `κ-sign-lock ∧ Wodzicki-parity` is what a future knob-free LRD-T transport would have to break), that closes my open items.

---

## Round 2 — mack: Cross-Synthesis

### CONVERGENCE

This is the final turn, and we have converged on every load-bearing question. I record the convergence precisely, because the SHAPE of the agreement — two independent axes foreclosing the SAME channel — is the workshop's strongest output, stronger than either of us reached alone.

**(1) The κ-sign foreclosure is now a THEOREM, by a PASS-AND across two structurally-independent axes.** In Round 1 I closed the channel connes left open in Q-C-1 (a non-scalar morphism on top of the `deg=+1` scale leg) on the **transport-κ axis**: the residual is a `+28.17`-decade ASCENT (not a descent — the sign connes had inverted), which needs `|κ_morphism|>1`, sign-inconsistent with the `|κ|<1` transport that yields `sign_verdict=PASS`. connes's Round-2 CONVERGENCE-1 ACCEPTS that correction AND reinforces it on the **Wodzicki-rigidity axis**: a same-class two-pole ratio `Res_W(s)/Res_W(s')` carries degree `−2(s−s')`, which under the physical rescale `t = M_KK/k_4D = 10^{+54.04} > 1` gives `|κ| = 10^{−108.08} ≪ 1` for any fixed pole ordering — DECAY, never the growth the band needs. I re-verified this independently (Sage, this round): `log₁₀|κ|(deg=−2) = −108.08` exactly. So the open channel is **doubly closed**: my transport-κ sign-lock and his Wodzicki degree-rigidity foreclose `|κ|>1` from two orthogonal directions. Per `joint-theorem-promotion.md`, two axes converging WITHOUT shared derivation path is genuine independent confirmation — the κ-sign mutual-exclusivity is a theorem, not an observation.

**(2) I ACCEPT connes's PARITY sharpening as the deepest structural content — it answers WHY the two axes cannot be bridged.** This is the item I did NOT have in Round 1 and it is the cleanest result of the cross-pollination. connes's Q-M-1 chain establishes a SECOND, parity-based obstruction independent of the magnitude/direction one: a `d_A=+1` temperature needs `deg(B)=+1` — a single `M_KK` power, **ODD** — but every substrate-natural NCG morphism that could re-weight the overshoot carries an **EVEN** degree (`−2(s−s')` for a Wodzicki two-pole ratio; `0` for an HKR cohomology-class ratio). I verified the parity arithmetic (Sage, this round): every Wodzicki ratio degree `{−2, −2, −6, …}` is EVEN; HKR is `0` (EVEN); none equals `+1`. So the morphism sector and the scale-leg sector live in **different parity classes**. A morphism cannot even MATCH `d_A=+1`, let alone supply the `|κ|>1` ascent on it. This is strictly stronger than the κ-sign argument alone: even if amplitude growth WERE available, parity would forbid the morphism from acting on the odd-degree scale leg. **The two `Q=R·M_KK^m` halves never meet because they are parity-separated.**

**(3) I ACCEPT the dual-differentia, with sign-lock dominant, now mechanistically grounded.** connes withdraws his single-differentia C4 reading (dimensionful-slot-collision only, companion to Member A n_PBH) in favor of my dual `dimensionful-slot-collision ∧ sign-lock (transport-κ)`. His Wodzicki-parity result (CONVERGENCE-1) is what makes the sign-lock IRREVERSIBLE substrate-naturally — it supplies the NCG mechanism for the lock I diagnosed from the transport side. So the two of us now hold the same dual-differentia reading from both ends: I have the transport-κ direction-lock, he has the parity reason it cannot be undone. Member A (n_PBH) is dimensionful-slot-collision ONLY (no κ-sign content); T carries the additional dominant sign-lock — structurally distinct, hence a genuine ENRICH of the sign-lock differentia (not a re-listing of Member A).

**(4) I ACCEPT connes's full CONCESSION on the §23 K=3 classification (Q-M-2) — §23 stays SUGGESTION at K=2.** This was the workshop's load-bearing methodology dissent in Round 1 (his C4 read it as the long-awaited K=3 → MANDATORY; I read the corpus as reserving K=3 for an independently-EXTRACTED new observable r/α_t). connes re-read corpus :1731 against the actual evidence-KIND for T and CONCEDED on the merits, with the decisive reason being the corpus's own axis-(iv) = EXTRACTION-distinctness: T's `+1` was rule-DERIVED from `d_A=Q·M_KK^m` bookkeeping, NOT factorization-EXTRACTED on a T-channel `w(L_max)·κ(k)` gate (none exists), exactly the move :1731 retracted ("confirming an existing structure ≠ adding a distinct extraction"). I note and endorse his precision that he does NOT concede on band-landing grounds — n_T's BLUE `+0.4676` doesn't land any CMB band either yet is a settled K-instance (corpus :1729), so band-landing is downstream colour, not the K-counter gate. The foreclosure is on EXTRACTION-distinctness, period. The dimensional-class rule lands as a **§23.0 DIRECTIVE EXTENSION** (the per-observable transport-degree theorem is now dimensional-class-INDEXED) + a **§18 Conjunct-1 cross-link**, NOT a K-counter advancement.

**(5) I ACCEPT connes's §26-ENRICH concurrence (Q-M-3) and §23.0-home concurrence (Q-M-4).** Transport-κ sign-lock ENRICHES the sign-lock differentia (§26 stays K=1) — both he and I reach this via the corpus §26 K_csub_R "S95 W1-2 companion instance" precedent (a structurally-distinct firing of an EXISTING differentiator enriches without advancing the counter). And the rule's home is §23.0-primary + §18-cross-link (the operative content is per-observable transport-degree determination, a §23 object; `deg(B)=d_A` is the §18 theorem it invokes). Both concurrences are exactly where I landed in M3/Re:C4; I adopt them as the Effected-In-Session landing targets.

### DISSENT

**I have NO residual dissent. We have fully converged.** I record this explicitly rather than manufacture a disagreement, per the discipline that "no dissent" is an honest output when it is true (`Investigating-Workshops.md §"No workshops"` analog: padding with a fabricated tension would be the violation).

Two precisions, each a sharpening of a converged point, not a dissent:

**(P1) The H₀ fence has a Sage-exact form the verdict file rounds — and I pin the exact one.** I re-derived the H₀ figures at exact QQ this round. The substrate-natural relief delivers `49/800 = 6.125%` EXACT of the band-floor shift (not a rounded `~6%`). The band-CENTER shortfall is `900/49 = 18.3673×` EXACT; the verdict file's fitted ratio `7500000/408331 = 18.3675×` is a near-equal fitted-budget representation that agrees to 4 sig figs but is NOT the bare band-center shortfall — when I land the falsifier row I cite `900/49` as the exact band-center shortfall and tag `7500000/408331` as the verdict-file fitted-budget form. The fitted knob is `1.1695%` of the full-homogeneity budget (the verdict file's `1.17%`). This is a `feedback_omega-gw-roundfigure-fidelity`-class precision: cite the Sage-exact rational, relegate the round figure to a tagged annotation. It does not change any conclusion (the magnitude is HELD either way); it makes the §7 row exact.

**(P2) The parity observation belongs on the §7 falsifier surface as the falsifier-content GENERATOR, and I will land it there.** connes's final-sharpening request (the closing item of his Round 2) is that I record the parity result on the §7 surface explicitly. I CONCUR and go further: the falsifier content of the T held-prediction is the **conjunction** `κ-sign-lock ∧ Wodzicki-parity` — a future knob-free LRD-T transport landing `[3500,6500] K` would have to break ONE of the two, and naming WHICH it breaks is the falsifier-surface test. That conjunction, not either factor alone, is what I land as the inverted-prediction's falsifier content.

### EMERGENCE

**E-M-1 — "Every `d_A=odd` substrate observable is unreachable knob-free" is a falsifier-surface CLASS, not two isolated rows.** This is the new cross-domain insight, and it is the single most reusable thing the workshop produced. Combine the parity theorem (E1, connes) with the dimensional-class admissibility rule (C3, joint): the morphism sector is EVEN-degree (closed under `−2(s−s')` Wodzicki ratios and `0` HKR), and the only ODD-degree carrier is the bare `M_KK^1` scale leg — which is sign-locked. So for ANY substrate-IS observable `O` with ODD mass dimension `d_A ∈ {±1, ±3, …}`, the transport is forced onto the sign-locked odd scale leg, with no even-degree morphism able to act on it (parity mismatch). T (`d_A=+1`, a temperature/energy) is merely the FIRST instance. The prediction generalizes: **the LRD photosphere temperature, and every other odd-mass-dimension substrate observable, is NOT reachable by a knob-free substrate-natural transport** — they are sign-locked at their own scale leg. This converts two rows (LRD-T, H₀) into a structural CLASS with a parity selection rule: `d_A` EVEN ⇒ transport stays in the even morphism sector (the framework's `d_A=0` successes n_s/α_s/d_s live here, which is exactly why they work); `d_A` ODD ⇒ forced onto the sign-locked scale leg (held). H₀ is the `d_A=0` edge case of this — even mass dimension, but the morphism degree is bounded (6.125%) because it is a SECOND-derivative-free ratio with no large-amplitude morphism available. The falsifier-surface statement of the class: *a future derivation that lands ANY odd-`d_A` substrate observable in its observed band knob-free would break the parity selection rule — that is the class-level falsifier, of which the LRD-T κ-sign∧parity conjunction is the inaugural concrete test.*

**E-M-2 — the `+2` import was undetectable because EVEN-ness is shared across the entire `d_A=0` morphism sector — confirming the fifth pin axis must be `(d_A, deg, parity)`.** In Round 1 (Re:C2 EMERGES) I noted the `+2` collision is a real regularity: second-order `d_A=0` objects (M4 `d/2` heat-trace amplitude; α_s `(a₄/a₂)²` two-pole) generically share `+2`. connes's E2 gives the cleaner detector reason: `deg_T=2.0` is EVEN, and EVEN-ness is shared across the whole `d_A=0` morphism sector, so the number "looks right" precisely because it sits in the right parity class for the `d_A=0` siblings but the WRONG one for T (which needs ODD). A name-only canonical import carries no parity tag, so the consumer's `matches W3 npz=True` check passes on the NUMBER and is blind to the parity-class crossing. The fix I proposed in Round 1 (a transported-observable mass-dimension pin, the fifth axis beyond `regulator-pin-discipline.md`'s four) is sharpened by connes's E2: the pin must carry `(d_A, deg, parity-class)`, NOT `d_A` alone, because PARITY is the invariant the name-only import silently crossed. I record this as an orchestrator-reserved rule-mirror hand-off (the `regulator-pin-discipline.md` four-axis table is subagent-edit-denied), with the parity-class field as the operative new content.

**E-M-3 — the volovik a₀-orthogonality wall and the κ-sign∧parity wall are ONE wall with two parity faces.** The volovik Layer-1 wall (workingpaper:573) states the `d_A=0` case: "neither moment pins a dimensionful H₀; a dimensionless ratio cannot close a dimensional gap." The workshop ADDS the dimensionful (`d_A=+1`) complement: a temperature DOES have a scale leg (unlike H₀), but the leg is ODD-parity and sign-locked, and no EVEN-parity morphism can correct it. So the unified statement is: **`Q=R·M_KK^m` forbids closing the gap from EITHER parity side — `m` EVEN with no large morphism (H₀, the volovik wall) OR `m` ODD with a sign-locked, parity-isolated scale leg (T, the workshop's addition).** The two consumers are the EVEN and ODD parity halves of one rigidity wall. This is the synthesis I land on the §7 surface: the volovik a₀-orthogonality wall is the EVEN face; the κ-sign∧parity theorem is the ODD face; together they are the parity-complete `Q=R·M_KK^m` dimensional-necessity wall.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | `deg(T_{BZ→pivot})` fixed uniquely by mass dimension (`deg(B)=d_A`)? | C1, Re:C1 | **Converged** | `deg(B)=−2s` Wodzicki-unique ⇒ admissibility REQUIRES `deg(B)=d_A`; a universal `+2` is the T2-VACUOUS scalar pathology. Degree is dimensional-class-indexed, NOT a free label. |
| 2 | The `+2` inheritance defect (dimensionless-α_s degree → dimensionful T) | C2, Re:C2 | **Converged** | A single canonical scalar `deg_T=2.0` (the `d_A=0` M4 `d/2` amplitude exponent) was name-imported (dedup-flag-iii) onto a `d_A=+1` temperature — a category error visible in the −82.23 OOM overshoot; the LRD-T band is a DIRECT JWST photosphere measurement (no relocation channel), making T's held-ness falsifier-grade. |
| 3 | Per-dimensional-class admissibility rule (degree for T vs H₀) | C3, Re:C3, M1 | **Converged** | `B = (M_KK scale leg)^{d_A} ⊙ (dimensionless morphism)`: `d_A=0` ⇒ trivial scale leg, morphism-only (H₀); `d_A=1` ⇒ non-trivial `M_KK^1` leg carrying the 54.04-dec conversion (T). `+2` lived in the morphism slot, conflated with the scale-leg slot. |
| 4 | Band-binding: does any knob-free substrate-natural degree land T-band and H₀-band? | M1, CONVERGENCE | **Converged** (NO) | **Mutual-exclusivity theorem**: for T, dimensional admissibility (`deg(B)=d_A=+1`) and sign-consistency (`|κ|<1`) are MUTUALLY EXCLUSIVE — the band-landing eff deg `0.4787` is sub-scalar, the deg=+1 residual is a `+28.17`-dec ASCENT needing `|κ|>1` (sign-foreclosed). For H₀, no scale leg exists; relief capped at `49/800=6.125%`. BOTH HELD. |
| 5 | Classification (§23 K=3 / §VII.BA entry / NON-PROMOTION-BY-HELD-NUMBER) | C4, M2, DISSENT→CONCEDED | **Converged** | TWO-LAYER landing: **(methodology) §23 stays K=2** — dimensional-class rule is a §23.0 DIRECTIVE EXTENSION (T's degree rule-DERIVED not factorization-EXTRACTED ⇒ fails axis-(iv); corpus :1731 controlling) + §18 cross-link; **(substrate-physics) §26 stays K=1** — NON-PROMOTION-BY-HELD-NUMBER, T fires dimensionful-slot-collision ∧ sign-lock (ENRICH). Zero K-counter advancements. |
| 6 | Falsifier-surface / held-magnitude consequence | M2, EMERGENCE | **Emerged** | INVERTED held-prediction sub-rows: T falsifier-content = `κ-sign-lock ∧ Wodzicki-parity` (PASS-AND across two axes); H₀ = sign-PASS/magnitude-HELD, 6.125% partial, a₀-orthogonal, ~94% held. **EMERGES**: "every `d_A=odd` observable is unreachable knob-free" is a falsifier-surface CLASS (parity selection rule), not two isolated rows. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **OQ-1 (the only genuine open compute) — is there a substrate-natural object that supplies an ascending `|κ|>1` morphism for T without a fitted dial?** The κ-sign∧parity theorem says NO (amplitude growth is non-substrate-natural for a transport factor; the only odd-degree carrier is the sign-locked scale leg). This is FALSIFIABLE: `CF-S111-CO34B-LRDT-TRANSPORT` should pin `deg=+1` a priori and pre-register the κ-sign-consistency predicate ("∃ substrate-natural transport with `deg(B)=d_A=+1` AND `|κ|>1` morphism leg?"), expected FALSE. A future derivation FINDING one would break the theorem. → carry-forward NOTE on the existing CF (do NOT duplicate).

2. **OQ-2 — does the parity selection rule (E-M-1) hold at higher odd `d_A`?** The theorem is proven for `d_A=+1` (T). Does every odd-mass-dimension substrate observable (`d_A ∈ {±1, ±3, …}`) hit the same sign-locked-odd-scale-leg wall? This is a structural CLASS prediction; a second odd-`d_A` instance (e.g. an energy-density-class observable) would either confirm the class or expose a parity-evading channel. → future-session structural gate (not this workshop's deliverable; registered as the class-level falsifier on the §7 surface).

3. **OQ-3 — does the `κ-sign-lock ∧ Wodzicki-parity` joint theorem survive a Stage-2 two-agent NON-AUTHOR cross-check?** Registered STAGE-1-CANDIDATE this workshop (see Effected-In-Session item 5). The Stage-2 verifiers must NOT be connes or mack (per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection"`: axis-distinctness + original-author exclusion). → the math CF below.

4. **OQ-4 (H₀ residual) — is there a substrate-derived dimensionless RELATION that predicts `ΔH₀/H₀` once `w=M_KK` is fixed by one observation?** The a₂ focusing-clock delivers `49/800=6.125%` of the band-floor shift; the remaining `~94%` is HELD and cannot come from a dimensionful a₀ draw (the parity-EVEN / no-scale-leg side of the wall). The OPEN question is whether a dimensionless `a₀⊥a₂` relation closes it — `CF-S111-CF3-H0-RESIDUAL`'s correct gate, constrained to dimensionless-morphism channels. → carry-forward NOTE on the existing CF (do NOT duplicate). This interlocks with the standing CF-S111-MKK-RG-INVARIANCE (whether `w=M_KK` is a virtue or a defect).

## Wrap-Up — Workshop Impact Summary

### What Changed

#### (a) Numerical revisions

- `band-landing eff deg for T = 0.4787` (Sage RealField(200), SUB-SCALAR `0 < 0.4787 < 1`) — corrects the Round-1 charge's implicit "super-scalar morphism on top of deg=+1" framing.
- `deg=+1 residual = −28.17 dec` in the descent convention = a `+28.17`-dec ASCENT (sign INVERTED from connes's C3 "~28-decade descent").
- `H₀ relief = 49/800 = 6.125%` EXACT of the band-floor shift (was the round `~6%` / `0.49%` mis-statement of the per-cent-of-floor figure).
- `H₀ band-center shortfall = 900/49 = 18.3673×` EXACT; the verdict-file `7500000/408331 = 18.3675×` is a near-equal fitted-budget representation (4-sig-fig agreement, NOT the bare shortfall) — Sage-exact form pinned for the falsifier row per `feedback_omega-gw-roundfigure-fidelity`.
- `fitted knob = 1.1695%` of the full-homogeneity 108.08-dec budget (verdict file `1.17%`).
- `|κ|(deg=−2 morphism) = 10^{−108.08}` (Sage) — confirms every fixed-pole-ordering Wodzicki ratio DECAYS, foreclosing `|κ|>1`.

#### (b) Structural changes

- **κ-sign foreclosure: observation → THEOREM** (PASS-AND across two independent axes: transport-κ sign-lock [mack] ∧ Wodzicki degree-rigidity + integer-parity [connes]). The Q-C-1 open channel (non-scalar morphism on deg=+1) is DOUBLY closed.
- **Parity selection rule discovered**: the morphism sector is EVEN-degree (`−2(s−s')` Wodzicki ratios, `0` HKR); the only ODD-degree carrier is the sign-locked `M_KK^1` scale leg. A `d_A=+1` (ODD) observable cannot be re-weighted by any EVEN-degree morphism — the two `Q=R·M_KK^m` halves are parity-separated.
- **Two isolated rows (LRD-T, H₀) → a falsifier-surface CLASS**: "every `d_A=odd` substrate observable is unreachable knob-free" (parity selection rule; E-M-1). Type promotion from per-observable held-number to a structural class with a selection rule.
- **T differentia: single → dual** — `dimensionful-slot-collision` (connes C4, single) → `dimensionful-slot-collision ∧ sign-lock (transport-κ)` with sign-lock DOMINANT (a NEW sub-species of the §26 sign-lock differentia, first with cohomology/transport content vs Member C's combinatorial surrogate `R_surr=2f−1`).
- **§23 K=3 classification: contested → CONCEDED at K=2** — the dimensional-class instance is a THEOREM-INDEXING directive extension (extraction-distinctness NOT met; T's degree rule-derived not factorization-extracted), NOT a K-counter advancement. The dimensional-class rule lands as a §23.0 sub-clause + §18 cross-link.
- **The volovik a₀-orthogonality wall and the κ-sign∧parity wall unified as ONE parity-complete wall** (EVEN face = volovik `d_A=0`; ODD face = workshop `d_A=+1`).

### What Holds

- **`deg(B) = d_A` (Wodzicki uniqueness)** — PERMANENT; corpus §18.0 Conjunct-1. The transport degree is the mass dimension of the transported observable, fixed by the unique trace on Ψ(A_K); no universal `+2`.
- **The §VII.BA five-formulation taxonomy** (T1–T5; corpus §18) — unchanged; this workshop INVOKES it (the dimensional-class rule is the Conjunct-1 homogeneity axis specialized to `d_A=1`), does not modify it.
- **The framework's `d_A=0` transport successes** — n_s scalar (substrate=pivot, flagship), α_s `+2` non-scalar (corpus §23.1 instance 2), n_T non-scalar (instance 1) — all sit in the EVEN morphism sector, which is exactly WHY they transport admissibly. The parity rule EXPLAINS the existing successes, it does not strain them.
- **`Q = R·M_KK^m` dimensional bookkeeping** (rank-1 `w=M_KK` import; `permanent-results-registry.md §VII.BS`, STAGE-3-PERMANENT) — the wall both consumers hit is a CONSEQUENCE of it, not a new assumption.
- **The W3 `+2` mint** — CORRECT for its own observable (M4 spectral dimension `d_s`, `d_A=0`, `d/2=2` amplitude exponent). The defect is the W4 IMPORT across the dimensional-class boundary, not the mint.

### What Breaks or Strains

- **The dedup-flag-iii name-only canonical import of `deg_T=2.0`** — STRAINED (it crossed a parity class silently; `matches W3 npz=True` checked the NUMBER, blind to `d_A` and parity). Mitigation is the proposed `(d_A, deg, parity)` fifth pin axis (orchestrator-reserved rule-mirror; Effected item 6).
- **The LRD-T substrate-natural transport** — BREAKS against direct data: no `deg(B)=d_A`-admissible AND `|κ|<1`-consistent transport lands `[3500,6500] K`. This is a clean HELD prediction (the structure is permanent, the number held), NOT a framework falsification — but it is the more consequential of the two consumers because the LRD-T band is a DIRECT JWST photosphere measurement with no relocation channel (unlike α_s).
- **The H₀-tension "resolution" reading** — STRAINS: the a₂ focusing-clock is a genuine sign-PASS partial (6.125% of the shift, correct direction) but leaves `~94%` HELD; it is NOT the timescape-style full H₀-tension resolution. Honest framing: directional relief real, magnitude held, a₀-orthogonal (does not consume the CC budget).
- **Nothing in the permanent registry breaks.** Both held magnitudes are NON-PROMOTION-BY-HELD-NUMBER under permanent structures; no PROVEN/PERMANENT claim is down-tagged.

### Carry-Forward Computations (MATH ONLY — propagate to S111)

**Discriminator (4-field test)**: an item belongs HERE iff it satisfies ALL FOUR fields (what / inputs / gate / effort). If ANY field cannot be filled, move it to "Effected In-Session" and EXECUTE it now. The single-observable CFs CF-S111-CO34B-LRDT-TRANSPORT and CF-S111-CF3-H0-RESIDUAL ALREADY EXIST in the W4 working paper — do NOT duplicate them; if this workshop's degree-rule changes their gate or inputs, state the sharpening as a note, not a new CF.

#### NOTES on the two existing single-observable CFs (sharpenings, NOT new CFs)

- **`CF-S111-CO34B-LRDT-TRANSPORT` (workingpaper:556) — SHARPENED, not re-authored.** This workshop's degree-RULE answers the CF's "What" field: T's substrate-natural degree IS DERIVED as `d_A=+1` (the `M_KK^1` scale leg), NOT a free search — the CF should **pin deg=+1 a priori and verify, not scan**. The Sage result pre-states the likely outcome (deg=+1 overshoots; eff deg `0.4787` is non-integer AND sub-scalar; the deg=+1 residual is a `+28.17`-dec ASCENT requiring `|κ|>1`). The CF MUST **pre-register the κ-sign-consistency predicate**: "∃ a substrate-natural transport with `deg(B)=d_A=+1` AND a `|κ|>1` morphism leg?" — expected **FALSE** by the κ-sign∧parity theorem. The CF's real open compute (OQ-1) is whether ANY substrate-natural object supplies an ascending morphism without a fitted dial; the theorem says no, but it is a falsifiable pre-registration. Gate routes to **dimensionful-slot-collision ∧ sign-lock (HELD/INFO)**, NOT a fitted knob.

- **`CF-S111-CF3-H0-RESIDUAL` (workingpaper:565) — SHARPENED, not re-authored.** The degree-RULE CONSTRAINS the CF: `ΔH₀/H₀` is `d_A=0`, so its transport CANNOT invoke the 54.04-dec scale leg (the `+2` full-homogeneity reading is dimensionally INADMISSIBLE — confirms the volovik a₀-orthogonality scope note, workingpaper:573). The residual-relief search is restricted to **dimensionless-morphism channels** (the a₂ focusing-clock at `6.125%`, plus any `a₀⊥a₂` dimensionless RELATION). The CF should **pre-register the partial-relief fraction `49/800=6.125%` as the honest outcome** (~94% held) and route the residual to **dimensionless-slot** (NOT dimensionful-slot — H₀ has no scale leg). Correct PASS criterion: a substrate-derived dimensionless RELATION predicting the shift once `w=M_KK` is fixed by one observation (OQ-4). Interlocks with CF-S111-MKK-RG-INVARIANCE.

#### NEW math CF (the one genuine 4-field future computation this workshop registers)

##### CF-S111-KSIGN-PARITY-STAGE2 — Stage-2 two-agent NON-AUTHOR cross-check of the `κ-sign-lock ∧ Wodzicki-parity` joint theorem

| Field | Spec |
|:--|:--|
| **What** | Stage-2 two-agent parallel independent-verify of the STAGE-1-CANDIDATE `κ-sign-lock ∧ Wodzicki-parity` joint theorem (registered this workshop; see Effected item 5). Axis-A (NCG/spectral) cross-reviewer audits the Wodzicki degree-rigidity + integer-parity clause; Axis-B (transport/cosmological-bridge) cross-reviewer audits the transport-κ sign-lock clause; the JOINT clause (the conjunction forecloses ALL substrate-natural ascending morphisms for a `d_A=+1` anchor) is PASS-AND'd across both. Both operate WITHOUT prior workshop context (read only the registered Stage-1 entry, NOT this workshop file). |
| **Inputs** | the registered STAGE-1-CANDIDATE entry in `permanent-results-registry.md` (joint-clause flags); `s110_gate_verdicts.txt` W3 mint `f60cff36…` + W4 consumers `2a654897…`/`7bfda02a…`; corpus §18.0 Conjunct-1 (`deg(B)=d_A`, Wodzicki); the Sage substitution chains (Q-M-1 connes; M1 mack). |
| **Gate** | BOTH cross-reviewers PASS their single-axis clauses AND the JOINT conjunction PASSes independently in BOTH verdicts (logical AND) ⇒ STAGE-3-PERMANENT. ANY clause FAIL ⇒ stays STAGE-1-CANDIDATE, FAILing clause routed to remediation. |
| **Effort** | ~1 wave (2 parallel cross-reviewers; NON-AUTHORS — must NOT be connes or mack per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`; candidate axis-A = `lizzi-spectral-functional-theorist` or `van-den-dungen-bridge-theorist`; candidate axis-B = `transit-dynamics-theorist` or `volovik-superfluid-universe-theorist`). |
| **Depends on** | the STAGE-1-CANDIDATE registration (Effected item 5, this workshop); the §23.0 directive extension (Effected item 1) for the dimensional-class context. |

### Effected In-Session (NON-MATH — executed by mack BEFORE TERMINATING)

**MANDATORY — NON-NEGOTIABLE.** Every non-math item executed NOW with concrete file edits; each box ticked with file:line + sha-short/anchor. corpus/registry/inventory edits are REVIEWED PATCHES, not bulk appends (`feedback_framework-hygiene.md`).

- [x] **1. corpus §23.0 DIRECTIVE EXTENSION** — `sessions/framework/registry/cross-pillar-bridge-corpus.md` §23.0, new subsection **§23.0(5)** appended after the ORCHESTRATOR-RESERVED block (before §23.1). Records: the per-observable transport-degree theorem is now DIMENSIONAL-CLASS-INDEXED (`d_A=0` ⇒ morphism-degree carried by the dimensionless structural morphism; `d_A=1` ⇒ scale-leg-degree carried by the `M_KK^1` unit-conversion leg); the §18 Conjunct-1 cross-link; the PARITY sharpening (EVEN morphism sector vs ODD scale leg; the two `Q=R·M_KK^m` halves parity-separated; every `d_A=odd` observable hits the same wall); the `(d_A, deg, parity)` fifth-pin sharpening. **§23 STAYS SUGGESTION K=2 — NO K-counter advance** (directive extension, not a calibration instance; K=3 slot remains reserved for an independently-EXTRACTED new-observable degree r/α_t, now with a `d_A`-declaration precondition). Cites this workshop + the three verdict SHAs (`f60cff36…`/`2a654897…`/`7bfda02a…`). LANDED at `cross-pillar-bridge-corpus.md` §23.0(5) (anchor `### §23.0(5)`).

- [x] **2. §26 sign-lock sub-species annotation** — same corpus, §26, new paragraph **"S110 W4 CO34/CF3 companion instance (ENRICH the sign-lock differentia; NO §26 K-counter advance)"** appended after the §26 S95-W1-2 companion paragraph (line ~1933). Records transport-κ sign-lock as a NEW SUB-SPECIES of the sign-lock differentia (Member C), the first with cohomology/transport content vs Member C's combinatorial surrogate `R_surr=2f−1`. **§26 STAYS K=1 (ENRICH, not advance)**. LANDED at `cross-pillar-bridge-corpus.md` §26 (paragraph anchor "S110 W4 CO34/CF3 companion instance").

- [x] **3. falsifier-master-inventory.md rows** (mack SOLE WRITER per `feedback_mack-bridge-role.md`) — two additive audit sub-rows appended (NO existing row rewritten), race-safe single-shot `open("a")`: **Row #88.audit-S110-CO34-LRDT-TRANSPORT-PARITY** (T: INVERTED held-prediction; falsifier content = `κ-sign-lock ∧ Wodzicki-parity`; LRD-T band a DIRECT JWST photosphere measurement, no relocation channel ⇒ held-ness falsifier-grade; the parity-CLASS prediction) + **Row #81.audit-S110-CF3-H0-RESIDUAL-PARTIAL** (H₀: sign-PASS/magnitude-HELD; substrate delivers `49/800=6.125%` of the ~9% tension, ~94% held, a₀-orthogonal). Cite the three verdict SHAs + this workshop. Values live in the inventory (AMRI). LANDED at `falsifier-master-inventory.md` lines (appended at EOF, anchors `### Row #88.audit-S110-CO34-LRDT-TRANSPORT-PARITY` + `### Row #81.audit-S110-CF3-H0-RESIDUAL-PARTIAL`).

- [x] **4. §7 capstone falsifier surface** (mack sole-writer domain) — NO capstone PROSE edit. This is a NEW held-prediction (NON-PROMOTION, not a status change to any existing capstone claim), so the capstone-hygiene status-sync is satisfied WITHOUT a prose edit: no existing §7 row's PROVEN/CONDITIONAL/BROKEN/INFO status changes. The held-prediction lands on the `falsifier-master-inventory.md` surface (item 3) which IS the §7 falsifier/observable surface's registry home (`capstone-hygiene-gate.md` Q2 routing: §7 falsifier-TABLE → `mack-cosmic-bridge` + `falsifier-master-inventory.md`). Recorded explicitly here that the 5-question capstone-hygiene gate Q2 (§7 falsifier-anchor row) routes to the inventory rows of item 3, and Q3 (status change) is NO (new prediction, not a re-tag). No `phonic-exflation-equation.md` edit warranted.

- [x] **5. STAGE-1-CANDIDATE registration** — `sessions/permanent-results-registry.md`, new slot **§VII.CF** (runtime-verified next-free over §VII.CA–CE; CF/CG both free, CF taken) appended, `κ-sign-lock ∧ Wodzicki-parity` joint theorem, STAGE-1-CANDIDATE, joint-clause flags (clause (a) mack-side transport-κ; clause (b) connes-side Wodzicki-parity; clause (c) JOINT conjunction). Queues its Stage-2 two-agent NON-AUTHOR cross-check as `CF-S111-KSIGN-PARITY-STAGE2` (the math CF above; verifiers MUST NOT be mack/connes). LANDED at `permanent-results-registry.md` (anchor `### §VII.CF`).

- [x] **6. ORCHESTRATOR-RESERVED hand-off line** (recorded, NOT executed — `.claude/rules/` is subagent-edit-denied):
  - **(6a)** `.claude/rules/cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"` — the existing "Per-observable transport-degree scale-separation" cross-link sub-clause should gain a DIMENSIONAL-CLASS-INDEXED sentence (`d_A=0` ⇒ morphism-degree; `d_A=1` ⇒ `M_KK^1` scale-leg-degree) + a pointer to corpus §23.0(5). Verbatim mirror text is in corpus §23.0(5).
  - **(6b)** `.claude/rules/regulator-pin-discipline.md §"four-axis orthogonality (UV-regulator × Level × Binding × MACHINERY-SCOPE)"` — add a FIFTH axis row: **transported-observable mass-dimension/parity pin** `(d_A, deg, parity-class)`, closing the silent dimensional-class/parity conflation the W3→W4 name-only import crossed. Pin form: a `convention=…-DA-<n>-PARITY-<even|odd>` suffix on transport-degree consumers. Substrate analog: the §23.0(5) parity selection rule. Verbatim mirror text staged in corpus §23.0(5).
  - The orchestrator lands (6a)+(6b) post-workshop; mack does NOT attempt the `.claude/rules/` edits.

### Closing Line

The LRD photosphere temperature is unreachable not because the substrate transports it wrongly but because the only admissible transport for an odd-mass-dimension observable is the sign-locked `M_KK^1` scale leg, and every even-degree morphism that could correct its overshoot is in the wrong parity class to touch it — so `κ-sign-lock ∧ Wodzicki-parity` is the falsifier content, and "every `d_A=odd` substrate observable is unreachable knob-free" is the falsifier CLASS it inaugurates.
