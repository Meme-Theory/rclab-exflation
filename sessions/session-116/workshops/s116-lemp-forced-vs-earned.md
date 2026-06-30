# Session 116 Workshop: connes × lizzi

**Date**: 2026-06-28
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: connes (connes-ncg-theorist), lizzi (lizzi-spectral-functional-theorist)
**Source Documents**:
- sessions/session-116/workshops/s116-w8-bridgemap-indep.md
- sessions/session-116/session-116-w8-workingpaper.md
- computations/session-116/s116_gate_verdicts.txt

**Focus Topics** (adversarial test: is the `{APS,CS,BC}` `L_emp` scheme-independence collapse FORCED-by-construction or EARNED-contingent? The landed registry guard `registry:18817` rests on a TWO-PART selection rule (DEGREE selection — solid; PARITY selection — load-bearing, novel, NEVER adversarially tested) minted by same-round parallel agreement between connes (R3A.1) and vdd, both on the NCG/cocycle axis):
1. (a) Does the PARITY selection genuinely FIRE for `Var_a(|v_a(K)|²)` — is the `|v|²`-variance cocycle EVEN under `D_K → −D_K` so it pairs to zero with `β^{odd}`? Derive from the ACTUAL s52 8-mode amplitude set, NOT from "sign-blind `|v|² ≥ 0`" alone. (connes's stated reason is imprecise: `|v_a|² = (1−ξ_a/E_a)/2` DOES reference `sign(ξ_a)`; the rigorous reason needs PH-evenness of the VARIANCE.)
2. (b) Does the conclusion survive `Var(1−X)=Var(X)` PH-evenness ONLY if the s52 8-mode amplitude set `{B2×4, B1, B3×3}` is PH-closed — and is the asymmetric (4+1+3) multiplicity PH-closed? (Unchecked.)
3. (c) DOCUMENTED precedent: corpus §23.0(5) records the S110 W4 catch where `deg_T=2.0` EVEN was wrongly imported onto a `d_A=+1` ODD temperature ("right parity class for the `d_A=0` siblings, WRONG class for T"). A mis-assigned EVEN/sign-blind tag on `Var_a(|v_a|²)` is the same failure mode and would INVERT the verdict (parity FAILS ⇒ `β^{odd}` survives ⇒ collapse EARNED ⇒ the landed registry guard is WRONG ⇒ CF-S117 becomes a genuine three-scheme certification).
4. (d) STRUCTURAL VERDICT: FORCED (degree-0 AND sign-blind, guard stands with the parity rule now rigorously DERIVED from the amplitude set) OR re-classed to EARNED-contingent (route a registry re-tag of the `§A8.1(i)` guard to mack).

NOTE: this is DISTINCT from the already-minted `CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION` (which tests only the path/spectral-flow PRECONDITION — no K-window zero-crossing); this workshop tests the STATIC parity-selection premise at fixed K.

---

## Round 1 — connes: Opening Analysis

### C1: (a) Does the parity selection FIRE for Var_a(|v_a(K)|²)?

**Finding: YES, the parity selection fires — but I CONCEDE that the reason I stated when I minted R3A.1 ("sign-blind `|v|² ≥ 0`") is IMPRECISE and, read literally, FALSE. The rigorous reason is PH-evenness of the VARIANCE (the centered second moment), not sign-blindness of `|v|²` itself. The corrected derivation makes the conclusion STRONGER (unconditional at fixed K), not weaker.**

**The concession, stated plainly (lizzi's (1) is correct).** The Bogoliubov occupation amplitude is

```
(C1.1)  |v_a|² = (1 − ξ_a/E_a)/2,   E_a = √(ξ_a² + Δ_a²),   |u_a|² = (1 + ξ_a/E_a)/2 = 1 − |v_a|².
```

`|v_a|²` manifestly references `sign(ξ_a)` through `ξ_a/E_a`. So "sign-blind `|v|² ≥ 0`" is wrong as a per-mode statement, and the MEAN inherits the defect — under PH it is NOT invariant. Sage (exact, the actual s52 (4,1,3) set):

```
mean(|v|²) = (1/8)B1 + (1/2)B2 + (3/8)B3   →   mean(|u|²) = 1 − [(1/8)B1 + (1/2)B2 + (3/8)B3];   mean_v + mean_u = 1.
```

The first moment maps to `1 − itself`. A premise resting on `|v|²` sign-blindness would leak `β^{odd}` content through the mean (and every uncentered moment). lizzi is right to press this.

**The PH-conjugation substitution chain (the rigorous derivation, from the actual set).** Particle-hole conjugation on the BdG fabric is the Nambu charge conjugation `C = τ_x K` (`C H_BdG C⁻¹ = −H_BdG`, i.e. `D_K → −D_K`):

```
(C1.2)  PH-conjugation substitution chain for the OBSERVABLE Var_a(|v_a|²)

  Step 1 (BdG normalization, UNCONDITIONAL):  |u_a|² + |v_a|² = 1   for every mode a.        [(C1.1)]
  Step 2 (PH action on amplitudes):  C : (u_a, v_a) ↦ (v_a*, u_a*) at E_a ↦ −E_a (ξ_a ↦ −ξ_a)
                                      ⇒ |v_a|² ↦ |u_a|² = 1 − |v_a|².                          [Step 1]
  Step 3 (PH action on the multiset): the 8-mode |v|² multiset {|v_a|²} ↦ {1 − |v_a|²},
                                      multiplicities (4,1,3) PRESERVED (C is a bijection).
  Step 4 (affine-scaling identity):   Var(α + βX) = β² Var(X);  with α = 1, β = −1:
                                      Var_a(1 − |v_a|²) = Var_a(|v_a|²).                        [UNCONDITIONAL]
  Step 5 (PH-parity of the observable): C : Var_a(|v_a|²) ↦ Var_a(|u_a|²) = Var_a(|v_a|²).   PH-EVEN.
```

Sage on the ACTUAL s52 `L_emp` branch values `{B1 = 0 (×1), B2 = 0.7704 (×4), B3 = 0.176 (×3)}` (s90-w5-cf61, s52 ED — the multiset feeding `L_emp = −7.0463`): `Var(|v|²) = Var(|u|²) = 327477/3125000 = 0.10479264` (QQ-exact), residual `0`. The parity is REAL and it is on the actual amplitude set, not a toy.

**Why the centering is the whole story (and the cocycle-level confirmation).** The mechanism is that `Var` is a CENTERED moment. Decompose `|v_a|² = ½ − ½(ξ_a/E_a)`; then `Var_a(|v_a|²) = ¼ Var_a(ξ_a/E_a)`, and `ξ_a/E_a` is the PH-ODD spectral variable (`ξ/E → −ξ/E` under `C`). But `Var(−Y) = Var(Y)`, so the variance of the odd variable is itself even (Sage: `Var(|v|²) = ¼Var(ξ/E)`, both `= 327477/3125000`; `Var(ξ/E) − Var(−ξ/E) = 0`). At the cocycle level this is the same statement: the Mellin trace `Tr_{M_2(ℂ)}(P_BdG · |D_K|^{−2s})` has kernel `|D_K|^{−2s} = (D_K²)^{−s}`, EVEN by construction; the occupied projector `P_BdG = ½(1 − sgn D_K)` carries the sign and maps `P_BdG ↦ 1 − P_BdG` under `C`, so the FIRST moment `Tr(P_BdG|D|^{−2s}) ↦ Tr(|D|^{−2s}) − Tr(P_BdG|D|^{−2s})` (odd-ish, the `|v|² ↦ 1−|v|²` echo), while the CENTERED second cumulant is invariant. The sign lives entirely in the projector's first moment; the variance is built to annihilate it.

**Consequence for the pairing.** A PH-EVEN observable pairs to zero with every `β^{odd}` component of the `{APS, CS, BC}` scheme-difference (the Z₂-graded trace of even × odd vanishes). The PARITY selection of R3A.1 Step 4 therefore FIRES — derived from (C1.1)–(C1.2) on the actual set, not from the sign-blindness hand-wave.

**Q to lizzi (C1):** Do you accept that the load-bearing object is `Var_a` (centered) and that its PH-evenness is the affine identity (C1.2 Step 4) — i.e. that my original "sign-blind `|v|²`" wording was the imprecise shorthand for "centered second moment of the occupation amplitudes," and the conclusion (parity fires) survives the correction unconditionally at fixed K? If you hold that some uncentered or sign-referencing residue survives in the actual `L_emp` parse-tree, name the term.

### C2: (b) PH-evenness of the variance + PH-closure of the (4+1+3) 8-mode set

**Finding: lizzi's (2) contains a TRUE factual sub-point and a FALSE inference. TRUE: the (4+1+3) set is NOT PH-closed. FALSE: that PH-evenness of the variance requires closure. `Var(1−X) = Var(X)` is the affine-scaling identity; it holds for ANY weighted multiset, closed or not. Sage-verified on the exact actual values.**

**The set is genuinely NOT PH-closed (I concede the sub-point — and it is even starker than "asymmetric multiplicity").** On the actual s52 values, the `|v|²` multiset and its PH image are

```
(C2.1)  {|v_a|²}      = { 0.7704 (×4),  0 (×1),  0.176 (×3) }
        C : {|v_a|²}  = {1 − |v|²} = { 0.2296 (×4),  1 (×1),  0.824 (×3) }    [a DIFFERENT multiset]
```

These are not equal as multisets (Sage `PH-CLOSED? = False`). The B1 mode is empty (`|v_B1|² = 0`); under PH it maps to a FULL mode (`|v|² = 1`) which is not in the original set at all — the image lands OUTSIDE the 8-mode set. So if PH-evenness genuinely required the set to map to itself, the premise WOULD fail here.

**But it doesn't require that — and the multiplicities are exactly why it doesn't matter.** `Var(1−X) = Var(X)` follows from `Var(α + βX) = β²Var(X)` with no constraint on the support of `X`. The PH map `C` is a BIJECTION on mode space (each mode has exactly one partner), so it PRESERVES multiplicities: `B2 (×4) ↦ partner (×4)`, `B1 (×1) ↦ partner (×1)`, `B3 (×3) ↦ partner (×3)`. The (4,1,3) weights enter the weighted variance only as the weights `w_a`, and the affine identity holds weight-for-weight:

```
(C2.2)  Var_w(1−X) = Σ w_a (1−x_a)² − (Σ w_a(1−x_a))²
                   = [1 − 2⟨x⟩_w + ⟨x²⟩_w] − [1 − ⟨x⟩_w]²
                   = ⟨x²⟩_w − ⟨x⟩_w²  =  Var_w(X),     for ANY weights {w_a}.
```

Sage on the exact (4,1,3) actual values: `Var(|v|²) = Var(|u|²) = 327477/3125000` — IDENTICAL despite the image (C2.1) being a manifestly different, non-closed multiset.

**The clean distinction lizzi is conflating.** Two different properties:
- "The 8-mode set is PH-closed" — FALSE for (4,1,3), and IRRELEVANT.
- "The variance FUNCTIONAL `Var_a(|v_a|²)` is PH-even" — TRUE, unconditionally, by (C2.2).

The pairing `⟨[P_BdG], β^{odd}⟩` does not see the set; it sees the NUMBER `Var_a(|v_a|²)` (and its K-trajectory). That number is PH-invariant whether or not the modes pair among themselves. Closure would be needed only if one demanded a mode-by-mode PH fixed-point structure — which the secondary-class pairing never asks for.

**Q to lizzi (C2):** The PH-closure worry would bite if `Var_a` were replaced by a functional that is NOT affine-invariant under `X ↦ 1−X` — e.g. a sign-resolved or odd-moment functional (`⟨ξ/E⟩`, a skewness, a signed spectral-flow count). Do you have a reading of the actual `L_emp` parse-tree in which the operative functional is NOT the centered second moment — i.e. in which closure genuinely re-enters? If the functional is `Var`, (C2.2) closes it; if you read a different functional in the s52 → `L_emp` pipeline, that is the real disagreement and we should pin it there, not at closure.

### C3: (c) The corpus §23.0(5) precedent — is this the same EVEN/ODD mis-assignment failure mode?

**Finding: structurally DIFFERENT failure modes — but the §23.0(5) precedent is a VALID methodological discipline, and the corrected C1/C2 derivation is precisely what PASSES it. The precedent indicts the original "sign-blind" hand-wave; it does NOT indict the per-observable variance derivation, and it does NOT invert the verdict.**

**What §23.0(5) / S110 W4 actually caught.** A transport degree `deg_T = 2.0` (EVEN) — correct for the `d_A = 0` morphism-sector siblings — was IMPORTED onto a `d_A = +1` ODD temperature scale leg, where it is the wrong class ("right parity class for the `d_A = 0` siblings, WRONG class for T"). The structural lesson (corpus §23.0(5); my [[s110-w4-transport-degree-parity]] note): the EVEN morphism sector (`−2(s−s′)` Wodzicki ratios, `0` HKR) and the ODD `M_KK^1` scale leg are PARITY-SEPARATED; a parity/degree tag is PER-OBSERVABLE and may not be carried across the `d_A` classes. The failure is a CROSS-SECTOR TAG IMPORT.

**Why `L_emp` is not that failure: it lives genuinely IN the even / `d_A = 0` sector; there is no odd scale leg to mis-tag.**

```
(C3.1)  d_A(L_emp): L_emp = d²/d(ln K)² [ ln Var_a(|v_a(K)|²) ]
        • |v_a|² ∈ [0,1] dimensionless ⇒ Var_a dimensionless ⇒ ln Var_a dimensionless.
        • d/d(ln K) is a LOGARITHMIC (dimensionless) derivative ⇒ d_A(L_emp) = 0.
        ⇒ trivial scale leg M_KK^{d_A} = M_KK^0 = 1.   NO odd M_KK^1 leg exists for L_emp.
```

In the §23 indexing `B = (M_KK^{d_A} scale leg) ⊙ (dimensionless morphism)`, `L_emp` has `d_A = 0`: the transport degree is carried entirely by the dimensionless morphism, which is EVEN. The temperature in §23.0(5) had `d_A = +1` — a genuine `M_KK^1` ODD scale leg. `L_emp` has none. There is no sector across which to import a wrong tag.

**The `d/d(ln K)` operator does not smuggle in an odd leg.** PH conjugation acts on the Nambu / energy structure (`ξ_a → −ξ_a`); `K` is the external momentum/scale the variance is differentiated against. The two act on disjoint factors, so `[C, d/d(ln K)] = 0`: differentiating a PH-even `ln Var_a(K)` in `ln K` yields a PH-even result. The transport leg here is a LOG-derivative (`d_A = 0`), categorically unlike the dimensionful `M_KK^1` temperature leg of §23.0(5).

**The precedent's real force: it forbids the SHORTCUT, which I took and now retract.** §23.0(5)'s lesson is "derive the parity per-observable; never inherit a sibling's tag." My R3 "sign-blind `|v|²`" WAS a sibling-style shortcut — assert evenness from a family heuristic ("magnitude data is even"). The C1/C2 derivation replaces it with a per-observable computation on the actual `{B2×4, B1, B3×3}` set (Sage-exact). That is exactly the discipline §23.0(5) demands — so the precedent, applied correctly, VINDICATES the corrected derivation rather than inverting it. (Indeed, the "magnitude data is even" heuristic is the SAME heuristic that would have wrongly tagged the MEAN occupation as even, which C1 shows is false. So §23.0(5) catches my old reason, and the centered-variance derivation is what survives the catch.)

**The one place the failure mode WOULD bite — and why it doesn't at fixed K.** A §23.0(5)-type inversion needs an odd-`d_A` carrier hiding under the even tag. The only candidate is the dynamical K-trajectory: IF `Var_a(|v_a(K)|²)` developed a non-smooth kink (a projector-rank jump from a K-window zero-mode crossing), the `d/d(ln K)` would couple the magnitude sector to the sign sector AT the crossing and revive `β^{odd}` — an odd contribution wearing the even label. But that is the DYNAMIC precondition, separately carried by CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION (gapped BDI bulk ⇒ no bulk zero modes ⇒ no K-window flow). At FIXED K — the static premise this workshop tests — no such leg exists.

**Q to lizzi (C3):** Do you accept the `d_A(L_emp) = 0` computation (C3.1) — i.e. `L_emp` is a dimensionless log-derivative with the trivial `M_KK^0` scale leg, so there is no odd scale leg onto which an even tag is being mis-imported? If you read a hidden `d_A ≠ 0` carrier in the `s = 4` Mellin / K-window structure (the analog of the `d_A = +1` temperature), name it; otherwise §23.0(5) is a discipline the corrected derivation satisfies, not a matching failure mode.

### C4: (d) connes's pinned position — FORCED via the cocycle parity-selection rule R3A.1

**Pinned position: FORCED for the static parity selection — high confidence, NOT a concession to EARNED. I correct the REASON (variance-centering, not `|v|²` sign-blindness); I do NOT retreat the CONCLUSION. The guard registry:18817 STANDS, with sharpened wording.**

**The argument that the parity half is LOAD-BEARING and FORCED (not a vacuous embellishment on degree-0).** The decisive structural fact is that `L_emp` and the ρ-invariant are BOTH degree-0:

```
(C4.1)  ρ      = η(D_BdG) − dim ker(D_BdG)        — a NUMBER (η-invariant + integer), degree-0.
        L_emp  = d² ln Var_a(|v_a|²)/d(ln K)²      — a NUMBER (log-derivative), degree-0.
```

If degree-0 ALONE forced the `{APS,CS,BC}` collapse, then ρ would ALSO be forced. But S93 W9-3 established ρ's three-scheme agreement is EARNED/contingent (a substantive Reading-A — you had to COMPUTE the ≤ 1e-3 M_KK² agreement; it was not structurally guaranteed). The ONLY structural property distinguishing the two degree-0 objects is PARITY under `D_K → −D_K`:

```
(C4.2)  ρ:      η(−D) = −η(D)  ⇒  ρ is PH-ODD   ⇒  parity selection does NOT fire
                 ⇒  β^{odd} (Dai-τ / spectral-flow) stays LIVE  ⇒  agreement is EARNED/contingent.
        L_emp:  Var_a(1−|v_a|²) = Var_a(|v_a|²)  ⇒  PH-EVEN  ⇒  parity selection FIRES
                 ⇒  β^{odd} annihilated by Z₂ grading  ⇒  agreement is FORCED.
```

So the PARITY selection is not decorative — it is the SOLE discriminator between the forced and earned cases at fixed degree-0. Remove it and you cannot explain why ρ's collapse is contingent while `L_emp`'s is forced. Degree-0 is the half BOTH share; parity is the half that SORTS them. This is the precise content of the R3A.1 two-part rule and the [[secondary-class-collapse-selection-rule]] memory ("degree-0 ALONE insufficient: it leaves the degree-0 odd component — Dai-τ / `dim ker` jump — live").

**Static vs dynamic — the static parity is unconditional; the only residue is dynamic and separately gated.** At FIXED K (the premise this workshop tests, per the skeleton NOTE), `Var_a(|v_a(K)|²)` is PH-even by (C1.2)/(C2.2) — no K-derivative is involved, so the static parity selection fires with NO precondition. The single non-tautological residue is the DYNAMIC smoothness of `Var_a(K)` across the K-window (no spectral flow), which is NOT part of the static parity question — it is the separate CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION (gapped BDI bulk, `Δ_BCS = 0.464 M_KK`). The static fixed-K parity selection is FORCED, full stop.

**The corrected guard wording (what registry:18817 should rest on).** The DEFER tag should read FORCED-by-`(degree-0 ∧ PH-even-VARIANCE)` — NOT FORCED-by-`(degree-0 ∧ sign-blind |v|²)`. The phrase "sign-blind `|v|²`" is the imprecision lizzi correctly flagged; the load-bearing predicate is "`Var_a(|v_a|²)` is PH-even (centered second moment; `Var(1−X) = Var(X)`)." With that substitution the guard is rigorous: the eventual CF-S117 `L_emp` `{APS,CS,BC}` PASS is FORCED-by-construction (degree-0 ∧ PH-even-variance), DISTINCT from and NOT co-equal with S93 W9-3's EARNED ρ-invariant Reading-A. (This is a wording sharpening of the §A8.1(i) guard, not a status change — route to mack via housekeeping if the landed text still reads "sign-blind |v|².")

**The one honest assumption (a scrutiny point, not a path to EARNED).** The chain (C1.2) uses `|u_a|² = 1 − |v_a|²` (BdG normalization) for all 8 modes. For single-mode BdG coherence factors this is unconditional (`|u|² + |v|² = 1` is spinor normalization, robust to detuning ε and gap Δ); the framework's Fermi-surface-lock theorem (`v²(B2[0]) = ½` at ε = 0, S64) confirms the B2 amplitudes ARE genuine BdG `v²`. The lone way it could fail is if the s52 "amplitudes" were composite/hybridized objects breaking simple Nambu doubling (then `|u|² ≠ 1 − |v|²` and PH-evenness becomes contingent — that would be the only honest path to EARNED). I judge this closed by the BdG construction but flag it for lizzi's spectral-functional axis to confirm.

**Verdict:** FORCED (static parity selection); guard STANDS with corrected wording. I do NOT concede a path to EARNED for the static premise; the dynamic residue is separately gated (CF-S117 bulk-gap).

**Q to lizzi (C4):** Two asks. (1) Do you accept the ρ/`L_emp` parity-discriminator argument (C4.1–C4.2) as the proof that the parity half is load-bearing — i.e. that degree-0 alone cannot distinguish the FORCED (`L_emp`) from the EARNED (ρ) case, so parity is doing real work? (2) On your spectral-functional axis: can you confirm the 8 s52 amplitudes are genuine single-mode BdG coherence factors (`|u|² + |v|² = 1` mode-by-mode), closing the one normalization assumption — or do you read a multi-band hybridization in the s52 ED that breaks it?

### C5: Cross-Cutting Observations

**1. The FORCED/EARNED boundary is a PARITY boundary at fixed degree — a substrate-IS statement about orthogonal BdG channels.** The deepest structural content of this adjudication is that `{APS,CS,BC}` collapse is sorted, at degree-0, by which PH channel the observable reads. The substrate fabric's BdG sector has two PH-orthogonal channels (the SIGNED-NAMBU lesson, [[s110-w2-5-ccdark2-mu-discriminator]]): the MAGNITUDE / occupation channel (`|v_a|²`, even under `C`) and the SPECTRAL-ASYMMETRY channel (`η`, `sgn`, signed spectral flow, odd under `C`). `L_emp` is built purely in the even occupation channel; ρ lives in the odd asymmetry channel. The trichotomy's discriminating content `β^{odd}` (Dai-τ, boundary η-asymmetry) lives in the odd channel — structurally invisible to `L_emp`, structurally visible to ρ. FORCED vs EARNED is not a numerical accident; it is which channel the observable couples to.

**2. The variance is the MINIMAL even functional — the first moment already fails.** A sharpening worth registering: PH-evenness is NOT a generic property of "occupation observables." The MEAN occupation `⟨|v_a|²⟩` is PH-ODD-affine (`⟨|v|²⟩ ↦ 1 − ⟨|v|²⟩`, Sage). It is the CENTERING that buys parity — the second CUMULANT is the lowest occupation moment that is PH-even. So R3A.1's forcing is specific to the variance (and higher CENTRAL cumulants), not to "magnitude data" broadly. This is the precise form of the claim, and it is what survives lizzi's (1). It also tells CF-S117 exactly what NOT to test as a forced quantity: any uncentered moment of `|v|²` would NOT be parity-protected.

**3. Methodological: this workshop converts a same-round-minted assertion into a Sage-verified per-observable derivation.** R3A.1 was minted by parallel NCG-axis agreement (connes asserts the parity half, vdd cross-checks from the transgression side, SAME round, both agree) — exactly the configuration the framework flags as NOT independent confirmation (`epistemic-discipline.md` "agreement among agents"). The adversarial test did its job: it found a real imprecision (the "sign-blind `|v|²`" reason), forced the correction (variance-centering), and the corrected claim is STRONGER (unconditional at fixed K, Sage-exact on the actual set). A clean instance of negative adversarial pressure SHARPENING a structural claim rather than breaking it: the CONCLUSION (FORCED) and the GUARD (registry:18817) survive; the REASON is rebuilt.

**4. Substrate framing (GEOMETRIC / PHONONIC).** The `|v_a|²` are the occupation amplitudes of the BdG quasiparticle eigenmodes of `D_K` on the `M_2(ℂ)` child — phononic excitations of the fabric, the 8 SU(3)-singlet-selected modes (BCS shell exactness, S70). `Var_a` is the SPREAD of occupation across those modes; `C = τ_x K` is the fabric's intrinsic particle-hole conjugation. The fabric IS particle-hole symmetric in the gapped bulk; `Var_a(|v_a|²)` reads only the MAGNITUDE of that symmetric occupation structure, never its sign — which is why the secondary-class scheme, whose discriminating content is the SIGNED asymmetry, cannot see `L_emp`. The substrate is logically prior: `L_emp` is a substrate-IS spectral moment whose PH-parity is fixed by the fabric's own `C`, not by any laboratory convention. The direction holds — `Substrate IS the occupation-variance → bridge map → laboratory secondary-class measurement`; the parity selection is a property of the fabric, read off before any scheme is chosen.

---

## Round 1 — lizzi: Response & Cross-Synthesis

### Part 1: Response to connes's Sections

#### Re: C1 — parity selection firing

**Verdict: AGREE — independently Sage-verified. I name NO surviving uncentered residue at the bare-variance level. The MISSED piece is where the scheme-difference actually lives.**

**I verify connes's correction (my own QQ-exact Sage run, not a re-read of his).** On the actual s52 `{B1 = 0 (×1), B2 = 0.7704 (×4), B3 = 0.176 (×3)}`:

```
Var(|v|²) = Var(|u|²) = 327477/3125000 = 0.10479264   (residual 0, QQ-exact)
mean(|v|²) = 282/625,  mean(|u|²) = 343/625,  mean_v + mean_u = 1   (PH-ODD-affine — the mean leaks)
¼·Var(ξ/E) = 327477/3125000 = Var(|v|²)   (the centering decomposition confirmed)
```

C1 is correct on every count: (i) `|v|²` is NOT sign-blind — the per-mode `(1−ξ/E)/2` AND the mean both reference `sign(ξ)`; (ii) the load-bearing object is the CENTERED `Var_a`, whose PH-evenness is the affine identity `Var(1−X)=Var(X)`; (iii) the parity selection genuinely FIRES on the bare 8-mode variance — `Var_a(|v_a|²)` is PH-even, so `⟨Var_a, β^{odd}⟩ = 0` (Z₂-graded trace of even×odd). I hold NO uncentered/sign-referencing residue in the bare-variance parse-tree. connes's "sign-blind |v|²" → "PH-even centered variance" correction is right and STRONGER. Topic-1 at the bare-variance level: **Converged.**

**MISSED (this is the whole disagreement to come).** C1 proves PH-evenness of the BARE, FINITE, CONVERGENT 8-mode variance — call it description (A). But the `{APS,CS,BC}` scheme-difference does NOT live in (A). It lives in the s=4 Mellin-pole REGULARIZATION of the full-spectrum trace `Tr_{M₂(ℂ)}(P_BdG·|D_K|^{−2s})` — description (B), which is DIVERGENT at s=4 (that is why it is a "pole"). The 8-mode set is the BCS-shell-exact FINITE proxy (S70); the secondary-class pairing runs over the full BdG spectrum and is regularized. connes's parity governs (A); the scheme-difference is a property of (B)'s pole-subtraction. The A→B transfer — does PH-evenness of the convergent proxy control the parity of the *divergent-pole scheme-difference*? — is exactly what C1 leaves unproven, and exactly where my regularization axis bites (L1, Re:C4). The parity fires; whether its firing REACHES the scheme-difference is the open question.

#### Re: C2 — PH-evenness / PH-closure

**Verdict: AGREE — connes is right, my assigned closure worry (b) is DEFUSED, I WITHDRAW it. The MISSED piece re-routes "closure" to the object where it IS load-bearing.**

**Concession, plainly.** `Var(1−X)=Var(X)` is the affine-scaling identity `Var(α+βX)=β²Var(X)` and holds weight-for-weight for ANY weighted multiset — closure is irrelevant. My Sage confirms the (4,1,3) set is NOT PH-closed yet the variances are identical:

```
{|v|²}          = { 0.7704 ×4, 0 ×1, 0.176 ×3 }
C:{|v|²}={|u|²}  = { 0.2296 ×4, 1 ×1, 0.824 ×3 }   ⟶  DIFFERENT multiset (PH-CLOSED? = False, Sage)
Var(|v|²) = Var(|u|²) = 327477/3125000              ⟶  EQUAL regardless
```

The pairing sees the NUMBER, not the set. C2's distinction ("the set is PH-closed" FALSE/irrelevant vs "the functional `Var` is PH-even" TRUE) is correct. I have no reading of the s52→`L_emp` pipeline in which the bare-variance-level functional is a non-affine-invariant (odd-moment, skewness, signed spectral-flow count) object that re-imports closure. Topic-2 at the bare-variance level: **Converged**; pressure point (b) withdrawn.

**MISSED — closure IS load-bearing, one object up.** The (4,1,3) set being non-PH-closed means the BdG mode SELECTION is parity-ASYMMETRIC: the empty B1 mode (`|v|²=0`) has its full PH partner (`|v|²=1`) OUTSIDE the 8-mode set entirely (your C2.1). For the FINITE variance this is harmless (the affine identity absorbs it). For the DIVERGENT s=4 trace it is NOT obviously harmless: a parity-asymmetric mode selection means the s=4 pole's regularization TAIL — the modes beyond the 8, which the W8-2 moment actually sums (`M_PV_L14_s4` runs over p+q≤14, thousands of modes, not 8) — is NOT particle-hole symmetric, so a scheme-dependent subtraction of that tail can carry asymmetric content the 8-mode variance cannot see. The real load-bearing closure question is the trace-TAIL's parity + regulator-class behaviour, NOT bare-variance closure. I develop this as L2.

#### Re: C3 — the §23.0(5) precedent

**Verdict: AGREE the `d_A(L_emp)=0` computation; DISAGREE that it disposes of the regulator worry. C3 defuses a scale-leg worry I am NOT raising and leaves my actual worry untouched — and the `d_A=0` fact cuts the OTHER way.**

**I accept C3.1.** `L_emp = d²/d(ln K)²[ln Var_a]` is a dimensionless log-derivative of a dimensionless variance ⇒ `d_A(L_emp)=0`, trivial scale leg `M_KK^0=1`, no odd `M_KK^1` leg. The §23.0(5) failure mode (an EVEN transport degree mis-imported onto a `d_A=+1` ODD temperature SCALE LEG) genuinely does NOT match `L_emp`; there is no odd scale leg to mis-tag. Conceded.

**DISAGREE on sufficiency.** §23.0(5) polices the SCALE LEG `M_KK^{d_A}` — a dimensionful, parity-carrying transport factor. My worry is a DIFFERENT object on a DIFFERENT axis: the UV-REGULATOR COUNTERTERM — a dimensionless, EVEN, regulator-class-keyed local term (the plateau `B(R)`). These are orthogonal axes (`regulator-pin-discipline.md` five-axis table: the Mass-dimension/parity scale-leg axis is explicitly distinct from the UV-regulator axis). `d_A=0` annihilates the odd scale leg but says NOTHING about the even regulator counterterm.

And the sting: `s=4` at `d=8` gives curvature-grade `n = d − 2s = 8 − 8 = 0` (the verdict line's `curvature_grade_n-0`). `d_A=0 ⟺ n=0 ⟺` the **a₀ / cosmological-constant grade** — NOT a clean grade, but the single MOST regulator-class-sensitive Seeley-DeWitt coefficient in the entire spectral action:

```
Direction claim: "n=0 is the grade of MAXIMAL UV-regulator-class spread, not minimal."
  Step 1: S_zeta = ζ_D(0) = a_4        ⟹  a_0 is ABSENT from the zeta spectral action.        [zeta scheme]
  Step 2: S_cutoff = Tr f(D²/Λ²)       ⟹  a_0 enters as the f_0·Λ^d DOMINANT (Λ⁴ at d=4) term.  [cutoff scheme]
  Step 3: spread_R(a_0-grade) ⊇ {0 (zeta), Λ^d-dominant (cutoff)}  ⟹  MAXIMAL across R.         [the CC problem]
  Conclusion: an observable at n=0 sits at the regulator-class spread MAXIMUM, not a clean sector.
```

So C3's `d_A=0` does not certify `L_emp` clean of regulator-class dependence; it LOCATES `L_emp` at the a₀ grade where regulator-class dependence is largest. The right precedent is NOT §23.0(5) (scale-leg parity) but the multiplicative-normalization-cancellation theorem's OWN conclusion (`math-scripts.md`, K=3 MANDATORY): the L_max weight cancels, and the surviving discriminating content is the plateau `B(R)` — **regulator-class-keyed**. That carrier is even, dimensionless, `d_A=0` — and it sits in the exact sector C3 declares safe.

#### Re: C4 — FORCED position

**Verdict: AGREE that parity is load-bearing and the secondary-class forcing holds on its own axis (conceded, with the S90-AQ precedent + the closed normalization). DISAGREE that parity is the SOLE discriminator and that "FORCED" = scheme-robust. Two corrections; the second routes the re-tag.**

**Concession — the secondary-class axis is yours.** C4.1/C4.2 are correct ON THE SECONDARY-CLASS AXIS. Both `ρ` and `L_emp` are degree-0; `ρ` is PH-ODD (`η(−D)=−η(D)`), `L_emp` PH-EVEN. On `{APS,CS,BC}` — three representatives of ONE secondary characteristic class, differing by EXACT-form transgressions = secondary (ODD) data — an odd object (`ρ`) couples to the discriminating `β^{odd}` and must be COMPUTED (S93 W9-3, ≤1e-3 → EARNED); an even object (`L_emp`) annihilates it → FORCED. The framework's own precedent confirms it: `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR` found `delta_scheme = 0.000e+00` with `GV_APS = GV_CS = −1.208158e+08` and `eta = 0` for an EVEN (η=0) observable — Term-1 annihilation in action. So on the secondary-class axis I CONCEDE: `L_emp` is forced-independent of `{APS,CS,BC}` (modulo the divergent-pole subtlety I flag as L3-Q1). And on your "one honest assumption" — single-mode BdG `|u|²+|v|²=1` — I confirm from the spectral-functional side: the s52 amplitudes are genuine single-mode BdG coherence factors (Fermi-surface-lock `v²(B2[0])=½` at ε=0, S64; BCS shell exactness, S70), no multi-band hybridization, so parity is not broken. The normalization assumption is CLOSED — but this closes the parity (odd-axis) question, not the regulator (even-axis) one.

**Correction 1 — "parity is the SOLE discriminator" is FALSE.** It is the sole discriminator on ONE axis. There is a SECOND, parity-orthogonal degree-0 discriminator: the UV-REGULATOR class. The multiplicative-normalization-cancellation theorem's conclusion is not "`L_emp` is scheme-free"; it is "the L_max weight cancels, leaving the plateau `B(R)`, which IS regulator-class-keyed":

```
Claim: "Parity-even ⇏ scheme-independent; the regulator-class index survives the parity selection."
  Step 1: L_emp = [ d²/d(ln K)² ln Tr^{(L)}_R(P_BdG |D_K|^{−2s}) ]|_{s=4, K_horizon}   [Connes-Karoubi pairing value]
  Step 2: Tr^{(L)}_R = w_R(L)·κ_R(K)  ⟹  d²ln(·)/d(lnK)² annihilates w_R(L)
          ⟹ L_emp = d²ln κ_R(K)/d(lnK)² |_{K_horizon} = B(R)     [W8-2 cancellation; L_max drops; B(R) remains]
  Step 3: B(R) is INDEXED by regulator class R ∈ {zeta, Pauli-Villars, Mellin}   [math-scripts.md: "B(R) IS regulator-class-keyed"]
  Step 4: C : |v|² ↦ 1−|v|² leaves κ_R(K) PH-even ⟹ kills β^{odd};
          BUT C is a SPECTRAL involution (D→−D); R is a REGULARIZATION CHOICE ⟹ C acts trivially on the R-index ⟹ parity does NOT collapse R.
  Step 5: ⟹ L_emp = B(R) is regulator-class-keyed in EVERY parity sector.
  Conclusion: parity-even forces {APS,CS,BC}(secondary-class)-independence — NOT {zeta,PV,Mellin}(UV-regulator)-independence. Parity discriminates on ONE axis only.
```

`ρ`-earned vs `L_emp`-forced is real — but it sorts the ODD/secondary axis. It is SILENT on the regulator axis, where BOTH `ρ` and `L_emp` are `B(R)`-keyed.

**Correction 2 — "FORCED" is axis-scoped AND structurally automatic.** `L_emp` is forced-independent of `{APS,CS,BC}` BECAUSE, being PH-even, its η-asymmetry content is ZERO — the three schemes resolve a discriminating content (`β^{odd}`: Dai-τ, boundary-η) that `L_emp` does not carry. That is "forced" in the sense "the test is blind to even objects," not "the observable survived a stringent scheme test." The NON-trivial scheme question for a PH-even, `n=0` (a₀/CC-grade) spectral moment is the UV-regulator class — where `L_emp` is `B(R)`-SD: my §VII.AV `B(R)` finding leaves it regulator-class SD-OPEN (CF: zeta+Mellin vs PV). `registry:18817` certifies the AUTOMATIC (secondary-class, vacuous-for-an-even-object) axis while the LIVE (regulator-class) axis stays open.

**Net:** FORCED on the secondary-class axis (conceded); EARNED/SD-OPEN on the regulator-class axis that governs an `n=0` even moment. The guard needs an **axis-scope re-tag**, not a status flip-to-FORCED-full: "secondary-class `{APS,CS,BC}` FORCED (parity; `L_emp` PH-even, blind to odd content) ∧ UV-regulator `{zeta,PV,Mellin}` NOT-forced — SD-OPEN at n=0, CF-S117." Route the §A8.1(i) wording to mack via housekeeping.

#### Re: C5 — Cross-Cutting

**1 (parity boundary at fixed degree): AGREE on the secondary-class axis; EMERGES a missing third axis.** Your two-PH-orthogonal-channels picture (magnitude/occupation `|v|²` even; spectral-asymmetry `η`,`sgn` odd) is correct and substrate-IS. But it is a picture WITHIN one regulator class. The plateau `B(R)` is regulator-class-keyed in EITHER channel, so the FORCED/EARNED boundary is a parity boundary only AFTER fixing `R`. The full structure is a 2-axis grid `(PH-channel: even/odd) × (regulator-class: zeta/PV/Mellin)`. You mapped column 1 (PH-channel); my §VII.AV `B(R)` SD-OPEN is the row variation (regulator-class). `L_emp` sits at (even, SD-open) — parity-protected on one axis, regulator-exposed on the other.

**2 (variance is the minimal even functional): AGREE, verified.** Sage confirms the mean is PH-ODD-affine (`mean_v+mean_u=1`) and the variance is the lowest PH-even occupation cumulant. Good sharpening — and it cuts both ways: the SAME centered cumulant whose PARITY is protected is the one whose plateau `B(R)` (its K-log-derivative) is REGULATOR-class-keyed. "Minimal even functional" buys odd-axis protection, not regulator-axis protection. CF-S117 must not read parity-protection as regulator-robustness.

**3 (methodological, same-round minting): AGREE strongly — and the cross-axis dispatch earned its keep TWICE.** R3A.1 was minted by same-round NCG-axis agreement (you assert parity; vdd cross-checks from transgression; both on the cocycle axis) — the `epistemic-discipline.md` "agreement among agents" configuration. The adversarial test found TWO things that minting missed: (i) the variance-centering correction (you already conceded, C1); (ii) the AXIS CONFLATION — secondary-class FORCED ≠ regulator-class independence — which BOTH cocycle-axis agents missed precisely because the regulator axis is OFF their axis. That second miss is the structural argument for the cross-axis (spectral-functional) dispatch: a parity theorem on the odd channel cannot certify robustness of an even, `n=0` moment whose live scheme-dependence is the UV-regulator class.

**4 (substrate framing): AGREE, with one addition.** `L_emp` IS the occupation-variance of the BdG eigenmodes of `D_K` on `M₂(ℂ)`; `C=τ_xK` is the fabric's intrinsic PH conjugation; the parity is read off before any scheme — correct, substrate-IS. ADDITION: the REGULATOR CLASS is ALSO a substrate-IS choice — WHICH spectral functional defines the fabric's action (the central question of my program: zeta vs cutoff give different physics from the SAME `D_K`). The fabric's PH-parity is scheme-free; the fabric's spectral-MOMENT VALUE at `n=0` is not — it is the cosmological-constant problem in microcosm. Direction held: substrate IS the occupation-variance; the bridge to the lab secondary-class measurement is parity-protected; the bridge to the lab a₀/CC-grade measurement is regulator-class-keyed.

### Part 2: Original Analysis

#### L1: Spectral-moment / regularization axis — does the Var_a(|v_a|²) cocycle pair to zero with β^{odd}?

**Lead: YES, the `Var_a(|v_a|²)` cocycle pairs to zero with `β^{odd}` (connes right, conceded). But the `{APS,CS,BC}` scheme-difference at the s=4 DIVERGENT pole is not exhausted by `β^{odd}`, and the part the parity selection does NOT reach is the a₀-grade regulator-class spread that `L_emp` is built to be maximally sensitive to.**

Decompose the pairing the guard rests on under the PH-grading:

```
(L1.1)   ⟨ Var_a(|v_a|²), β_{APS,CS,BC} ⟩  =  ⟨ Var_a, β^{odd} ⟩  +  ⟨ Var_a, β^{even} ⟩
                                            =        0           +   ⟨ even, even ⟩
```

- **Term 1, `⟨Var_a, β^{odd}⟩ = 0`:** YES. Z₂-graded trace of even×odd vanishes; conceded; this is connes's entire result. On the STRICT secondary-class axis (three transgression-representatives of one class, where `β ≡ β^{odd}` by construction), Term 1 is the whole story → `{APS,CS,BC}`-FORCED. The `S90-AQ` precedent (`delta_scheme=0`, η=0 even observable) is Term 1 in action.

- **Term 2, `⟨Var_a, β^{even}⟩`:** the leak. To ASSIGN A NUMBER to `L_emp` at the s=4 pole, each scheme must UV-regularize a DIVERGENT trace. The secondary-class representative (`{APS,CS,BC}`) and the UV-regularization (`{zeta,PV,Mellin}`) are ENTANGLED at a pole: APS-1975 ζ-regularizes `η(s)=Σ sgn(λ)|λ|^{−s}`; Bismut-Cheeger heat-kernel/adiabatic-regularizes; Cheeger-Simons uses a Chern-Weil/holonomy representative. These EMBED different UV-regularizations, so the EVALUATED `{APS,CS,BC}` difference INHERITS a UV-regulator difference — an EVEN local (Seeley-DeWitt) counterterm `β^{even}`, which `Var_a` (even) does NOT annihilate.

The substitution chain pinning Term 2 outside the parity selection's reach, and hardest to vanish at this pole:

```
Claim: "Term 2 is not reached by the parity selection, and at n=0 its vanishing is least forced."
  Step 1: pole s=4, d=8  ⟹  curvature-grade n = 8 − 2·4 = 0.                 [verdict line: curvature_grade_n-0]
  Step 2: n=0  ⟺  a_0 Seeley-DeWitt grade (volume / cosmological-constant term).
  Step 3: the {APS,CS,BC} schemes' embedded UV-regularizations can differ at the a_0 grade by a finite local
          counterterm Δa_0^{R,R'} (the ζ-vs-heat-kernel finite-part difference at a divergent pole).
  Step 4: a_0-grade regulator spread is the LARGEST of any grade (zeta: a_0 ABSENT; cutoff: a_0 DOMINANT) — the CC problem.
  Step 5: Δa_0^{R,R'} is built from D_K² (PH-EVEN) ⟹ it is β^{even}, OUTSIDE the parity selection ⟹ ⟨Var_a, β^{even}⟩ is NOT forced to 0.
  Conclusion: parity removes Term 1; Term 2 survives the selection, and at n=0 its vanishing is the LEAST structurally forced (maximal regulator spread).
```

I do NOT claim Term 2 is proven nonzero — I claim parity does not REACH it, so its vanishing is a SEPARATE computation, and `n=0` is the worst place to assume it auto-vanishes (it is the cosmological-constant problem at one pole).

**Quantifying the openness.** `B(R) = R_KW^R(L→∞)` is regulator-class-keyed (`math-scripts.md`; source `s91-w4-w5-1`). The W8-2 PASS (`L_emp_FULL = proxy`, rel `7.3e-11`, `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED`) is **FULL-Pauli-Villars = Casimir-bound proxy, WITHIN PV** — it certifies L_max-invariance inside ONE regulator class; it does NOT span `{zeta, Mellin, PV}`. My §VII.AV `B(R)` finding records that span as regulator-class SD-OPEN (CF: zeta+Mellin vs PV). So Term 2's vanishing is UNTESTED across regulator classes = EARNED.

**Net:** connes's parity argument is a THEOREM about Term 1 (the odd channel) — conceded and Sage-verified. It is SILENT on Term 2 (the even, regulator-inherited, a₀-grade channel), where `L_emp` is built to be maximally sensitive. The `{APS,CS,BC}` collapse is FORCED on the odd half, EARNED on the even half. CF-S117's genuine content is a THREE-regulator certification of `B(R)` at the a₀ grade ({zeta,PV,Mellin}; and, separately, whether the EVALUATED `{APS,CS,BC}` representatives inherit a `β^{even}` — L3-Q1) — not a re-confirmation of the (automatic) odd-channel blindness.

#### L2: PH-closure of the s52 8-mode amplitude set — the load-bearing check

**Lead: connes is RIGHT that closure is irrelevant to the BARE-variance PH-evenness (conceded, Sage-verified). The load-bearing closure check is one object up — the s=4 trace's full-spectrum regularization TAIL — and there the parity-asymmetric mode selection couples to the regulator class.**

1. **Bare-variance closure: settled IRRELEVANT.** Sage QQ: `{B2×4, B1×1, B3×3}` is NOT PH-closed (image `{0.2296×4, 1×1, 0.824×3}` ≠ original), yet `Var(|v|²)=Var(|u|²)=327477/3125000`. Affine identity, weight-for-weight. My assigned pressure point (b) is withdrawn; C2 upheld.

2. **The B1=0 mode exposes a parity-ASYMMETRIC selection.** `|v_{B1}|²=0` (empty); its PH partner `|v|²=1` (full) is OUTSIDE the 8-mode set (your C2.1). So the BCS-shell selection is NOT particle-hole symmetric AS A MODE SET. Harmless for the finite variance; not harmless for the divergent trace.

3. **The trace is NOT 8-mode-saturated.** The W8-2 verdict computes the s=4 moment over the FULL spectrum: `M_PV_L12_s4 = 1321.565`, `M_PV_L14_s4 = 1333.256` (p+q≤14, thousands of modes), `weight_ratio = 1.008846`. The 8-mode variance is the STATE-PROJ FINITE proxy (description A); the secondary-class pairing's actual value (description B) is the regularized full-spectrum trace. The cancellation drops the L_max weight, but the per-regulator-class FINITE remainder `B(R)` is the full-spectrum TAIL's regularized value.

4. **The load-bearing closure question, correctly placed:** is the s=4 DIVERGENT-tail subtraction (i) particle-hole symmetric AND (ii) regulator-class-independent? A parity-asymmetric mode selection (item 2) feeding a regulator-class-keyed tail subtraction (item 3) is precisely the channel through which an EVEN scheme-difference (`β^{even}`, L1 Term 2) enters `L_emp`. The bare-variance parity (connes) does NOT close it — it operates on the finite proxy, not on the divergent tail.

**Net:** closure matters — but at the trace/tail (where parity-asymmetric selection meets regulator-class subtraction), not at the bare 8-mode variance. The bare-variance closure worry (pressure point b) is correctly defused by connes; the trace-tail closure worry is the real one, and it is OPEN (it IS the L1 Term-2 / `B(R)`-SD carry-forward). The honest reading of the skeleton's (b): the multiset closure is a red herring; the operator-tail closure is the live question.

#### L3: Questions for connes

**Q1 (the even counterterm — central).** At the s=4 pole, is the `{APS,CS,BC}` scheme-difference PURELY `β^{odd}`, or does it carry an EVEN local Seeley-DeWitt counterterm `β^{even}` inherited from each scheme's UV-regularization of the divergent trace (APS ζ-reg of `η(s)` vs BC heat-kernel/adiabatic vs CS Chern-Weil)? The secondary INVARIANT being odd (`ρ` is PH-odd) is NOT the same as the pole-REGULARIZATION DIFFERENCE being odd. If you claim PURELY odd, prove the three representatives carry NO scheme-dependent even finite-part at a divergent pole. If it carries `β^{even}`, then `L_emp` (even) sees it (L1.1 Term 2) and the collapse is EARNED.

**Q2 (the a₀ grade).** `L_emp` lives at curvature-grade `n=0` (s=4, d=8) — the a₀ / cosmological-constant grade, where the UV-regulator class produces the LARGEST scheme spread (zeta: a₀ absent; cutoff: a₀ dominant). What FORCES the embedded a₀-grade local term to be scheme-universal across `{APS,CS,BC}` precisely at the grade where regulator schemes diverge MOST? This is the cosmological-constant problem at one pole; I do not see what makes it auto-vanish here, and "degree-0" alone does not (degree-0 is exactly the a₀ grade).

**Q3 (axis scope of registry:18817).** Is the guard's "`{APS,CS,BC}` scheme-independence" the SECONDARY-CLASS axis or the UV-regulator axis? If secondary-class: I concede FORCED, but it is automatic for an even object (no odd content) and must NOT be read as UV-regulator robustness. If it is meant as broad scheme-robustness: it is FALSE — `B(R)` is regulator-class-keyed (§VII.AV SD-OPEN, CF: zeta+Mellin vs PV). Will you accept an axis-scope re-tag that separates "secondary-class FORCED (parity, even-blind)" from "UV-regulator EARNED/SD-OPEN (`B(R)`, n=0)"?

**Q4 (is "SOLE discriminator" defensible given B(R)?).** C4 calls parity "the SOLE discriminator between forced and earned at degree-0." But `B(R)=R_KW^R(L→∞)` is regulator-class-keyed at degree-0 INDEPENDENT of parity (the cancellation theorem's own conclusion). So the regulator class is a SECOND degree-0 discriminator parity does not capture. Do you withdraw "SOLE," or claim `B(R)` is regulator-class-INVARIANT for `L_emp` — contradicting `math-scripts.md`'s plateau conclusion AND my §VII.AV finding? If the latter, that is a computable claim (`B(R)` under zeta vs PV vs Mellin at `K_horizon`); name it as CF-S117's real gate — and note it lands on MY axis (FI/SD regulator classification), not the parity axis.

---

## Round 2 — connes: Follow-up

**Substrate framing held.** The substrate IS the BdG quasiparticle occupation structure of `D_K` on the `M_2(ℂ)` child: `Var_a(|v_a(K)|²)` is the spread of occupation across the 8 SU(3)-singlet-selected phononic modes, and `C = τ_x K` is the fabric's intrinsic particle-hole conjugation. The regulator class `R` is ALSO a substrate-IS choice — WHICH spectral functional defines the fabric's action (lizzi's program). The direction holds: `Substrate IS the occupation-variance → bridge map → laboratory secondary-class / a₀-grade measurement`. The two-axis split below is a split between TWO substrate-IS properties of the same fabric — its PH-parity (scheme-free) and its a₀-grade spectral-moment value (regulator-class-keyed).

### CONVERGENCE

**I accept lizzi's two-axis decomposition, and I concede that my C4 "parity is the SOLE discriminator" was wrong as a GLOBAL claim. The verdict is PARTIAL (two-axis), not FORCED-full.** Four concessions, each forced by lizzi's Re:C4 / L1.

**1. The secondary-class axis `{APS,CS,BC}` and the UV-regulator axis `{zeta,PV,Mellin}` are ORTHOGONAL — and this is the framework's OWN pin, not a new claim.** `regulator-pin-discipline.md §"four-axis orthogonality"` lists the UV-regulator axis (`a_n^{ζ}`, `a_n^{Pauli-Villars}`, `a_n^{Mellin}`) as a distinct row from the secondary-class bridge-map-scheme suffix (`cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"`), whose operational test is explicitly "scheme-spread `Δ_scheme(B) → machine-zero` across {APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger} (**secondary-class axis ONLY, not the orthogonal UV-regulator RD axis**)." lizzi's L1 reads the framework's own orthogonality correctly: my parity argument operates on the secondary-class axis; the UV-regulator axis is a separate pin my argument does not carry.

**2. `math-scripts.md`'s `B(R)` is on the UV-regulator axis, NOT the secondary-class axis.** The multiplicative-normalization-cancellation theorem's `B(R) = L_n[g_R(K)]` is regulator-class-keyed for `R ∈ {Pauli-Villars, zeta, Mellin, lattice, cutoff}` — the UV-regulator atlas, NOT `{APS,CS,BC}`. So there genuinely IS a second degree-0 discriminator (the UV-regulator class) that the parity selection does not touch. lizzi's Re:C4 Correction 1 stands on the merits.

**3. I withdraw "SOLE discriminator" as a GLOBAL claim (answers L3-Q4 in part).** Parity is the sole discriminator of the **secondary-class-axis FORCED/EARNED split** — it is what sorts `L_emp`-forced from `ρ`-earned at fixed degree-0 ON THAT AXIS (C4.1/C4.2 hold, conceded by lizzi). It is NOT the only degree-0 discriminator in existence; the UV-regulator class is a second, parity-orthogonal one. My C4 over-stated the scope: the correct statement is "parity is the sole discriminator of the secondary-class-axis FORCED/EARNED split," not "the sole discriminator at degree-0."

**4. An `{APS,CS,BC}` PASS on `L_emp` is, on the secondary-class axis, structurally automatic for an even object.** lizzi's Re:C4 Correction 2 is right that "FORCED" here means "the secondary-class test is blind to even objects," not "the observable survived a stringent scheme test." I hold (DISSENT below) that this is FORCED-and-structurally-informative rather than "vacuous" — but I concede the operational point: the eventual CF-S117 `{APS,CS,BC}` PASS on `L_emp` certifies the AUTOMATIC odd-channel blindness, and must NOT be read as UV-regulator robustness. The LIVE scheme question for an `n=0` even moment is the UV-regulator class.

### DISSENT

**I hold two NEW positions: (D1) lizzi's L1-Term-2 `β^{even}` is mis-routed onto the secondary-class axis — her own cited precedent forbids it; (D2) the `n=0` / a₀-grade location does NOT amplify the UV-regulator openness for `L_emp` — it is annihilated by the log-derivative, Sage-verified.**

**D1 — the `β^{even}` lives on the UV-regulator axis, NOT the `{APS,CS,BC}` difference; lizzi's S90-AQ precedent proves it.** lizzi's L1 decomposes `⟨Var_a, β_{APS,CS,BC}⟩ = ⟨Var_a, β^{odd}⟩ + ⟨Var_a, β^{even}⟩` and argues the second term leaks because "the `{APS,CS,BC}` schemes embed different UV-regularizations, so the EVALUATED `{APS,CS,BC}` difference INHERITS a UV-regulator difference — an EVEN counterterm." This attributes a `β^{even}` to the **secondary-class difference itself**. But her OWN cited precedent (Re:C4) refutes exactly that attribution:

```
(D1.1)  S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR:
        for an EVEN (η = 0) observable,  delta_scheme = 0.000e+00 EXACTLY,
        GV_APS = GV_CS = −1.208158e+08.
```

`delta_scheme` is the FULL `{APS,CS}` spread paired against the observable — not its odd part only. If the `{APS,CS,BC}` schemes carried an inherited `β^{even}` UV-counterterm, then NO even observable could return `delta_scheme = 0` — the even observable would pair non-trivially with the even counterterm (`⟨even, β^{even}⟩ ≠ 0`). Yet S90-AQ returned `delta_scheme = 0.000e+00` for its even observable. Therefore the `{APS,CS,BC}` difference, paired against an even observable, carries **no surviving even part** — the schemes are three transgression-representatives of ONE secondary class, and their difference is the purely-odd transgression `β^{odd}` (finite secondary invariant; APS-η, Bismut-Cheeger η-form, and the Cheeger-Simons character all represent the same UV-finite class). The `β^{even}` lizzi correctly identifies is REAL, but it is the `{zeta,PV,Mellin}` UV-regulator difference — an ORTHOGONAL axis. The "embedding" intuition (APS is "ζ-named," BC is "heat-kernel-named") conflates the regularization METHOD that NAMES a secondary-class scheme with the UV-regulator AXIS; the framework's four-axis orthogonality + the S90-AQ `delta_scheme = 0` separate them.

**Honest scope-limit on D1 (and a falsifier I pre-register).** S90-AQ may not have run at the `n=0` grade. If the `n=0` grade specifically injects a `β^{even}` into the `{APS,CS,BC}` difference that is absent at other grades, S90-AQ (at a different grade) would not catch it. I therefore do NOT claim D1 closes the `n=0`-specific secondary-class question by precedent alone. The clean closure is a direct compute: **CF-S117 must evaluate `delta_scheme({APS,CS,BC})` for `L_emp` at `n=0` directly.** My FORCED prediction is `delta_scheme → 0` (parity); a `delta_scheme ≠ 0` would vindicate lizzi's secondary-axis `β^{even}` and put a hole in the parity argument. This makes my FORCED claim falsifiable — which is exactly the discipline the adversarial test should produce.

**D2 — the a₀-grade UV-regulator sensitivity is annihilated by `L_emp`; lizzi's "`n=0` is the worst place" holds for the trace, not for `L_emp`.** lizzi's Re:C3 / L1-Step-4 / Q2 argue `n = d − 2s = 8 − 8 = 0` is the a₀ / cosmological-constant grade, where UV-regulator spread is LARGEST (zeta: a₀ absent; cutoff: a₀ dominant). I accept the grade identification (`n=0` IS a₀) and the CC-problem framing for the FULL trace. But `L_emp` is NOT the trace — it is the second K-log-derivative, and the a₀-grade regulator sensitivity is a K-INDEPENDENT (volume / constant) object that the log-derivative annihilates.

```
(D2.1)  Substitution chain — the a₀-grade regulator offset is annihilated by L_emp.

  Step 1:  a₀ Seeley-DeWitt coefficient = volume term ∝ ∫√g dᵈx.  K-INDEPENDENT
           (no curvature, no external scale K in the leading volume term).        [SDW expansion]
  Step 2:  the regulator-class difference at a₀ (zeta: a₀ absent from S_ζ=ζ_D(0)=a_4;
           cutoff: a₀ = f_0·Λᵈ dominant) is a difference in THIS K-independent term.  [lizzi L1 Step 4]
  Step 3:  it enters ln κ_R(K) as a K-independent offset:  ln κ_R(K) = ln κ_0(K) + c_R
           (additive-in-log), or κ_R(K) = e^{c_R}·κ_0(K) (multiplicative prefactor).
  Step 4:  L_emp = d²/d(ln K)² [ln κ_R(K)]
                 = d²/d(ln K)² [ln κ_0(K)] + d²/d(ln K)²[c_R]
                 = d²/d(ln K)² [ln κ_0(K)] + 0.                                    [d/d(lnK) of a const = 0]
  Conclusion:  L_emp(R) − L_emp(0) = 0 for any K-INDEPENDENT regulator offset c_R.
               The a₀-grade volume sensitivity does NOT appear in L_emp.
```

Sage-exact verification (symbolic, this turn): with `u = ln K`, additive `ln κ_R = ln κ_0(u) + c_R` gives `L_emp(R) − L_emp(0) = 0` and `∂/∂c_R L_emp = 0`; multiplicative `κ_R = e^{c_R}κ_0(u)` gives `0` likewise; only a K-DEPENDENT profile `r_R(u)` survives, and then only as `r_R''(u)`. This is not a coincidence — it is the SAME annihilation the multiplicative-normalization-cancellation theorem (`math-scripts.md`, K=3 MANDATORY) applies to `w(L_max)`: a K-independent multiplicative/additive-in-log factor is killed by `d²/d(ln K)²`. The a₀-grade volume offset falls into the identical killed class as the L_max weight.

**Consequence:** `L_emp` is, structurally, the spectral observable MOST PROTECTED against a₀-grade regulator sensitivity — the log-derivative projects out exactly the K-independent (volume / cosmological-constant) part where the a₀ spread is largest. lizzi's "`n=0` is the worst place" is correct for `Tr^{(L)}_R(K)` (the divergent trace, description B) but inverts for `L_emp` (its second K-log-derivative). What survives — and what `B(R)` genuinely keys on — is the **K-DEPENDENT** part of the regulator profile `κ_R(K)` (the `r_R''(u)` term), which is real, untested (§VII.AV SD-OPEN), but a NARROWER and WEAKER target than "the a₀ grade's maximal spread." I do NOT claim this closes the UV-regulator axis; I claim it relocates the openness off the a₀-volume sensitivity and onto the K-dependent kernel profile.

### EMERGENCE

**1. The full structure is a 2×2 orthogonal grid, and `L_emp` occupies one cell of it.**

```
(E.1)               secondary-class axis (PH-parity)        UV-regulator axis (FI/SD)
                    {APS, CS, BC}                            {zeta, PV, Mellin}
  L_emp (even)      FORCED (parity; ⟨even, β^{odd}⟩ = 0)     SD-OPEN at K-dependent κ_R profile
                    [my column — Sage-exact, S90-AQ]         [lizzi's row — §VII.AV, but a₀-offset annihilated, D2]
  ρ    (odd)        EARNED (S93 W9-3, ≤1e-3)                 SD-OPEN (same row)
```

My parity result is the COLUMN (the PH-parity axis sorts FORCED/EARNED); lizzi's `B(R)` is the ROW (the UV-regulator axis is SD-OPEN for both `L_emp` and `ρ`). The two axes are orthogonal — `C = τ_x K` is a SPECTRAL involution (`D_K → −D_K`) and acts TRIVIALLY on the regulator-class index `R` (lizzi's Re:C4 Step 4, conceded), so parity cannot collapse `R` and `R`-variation is not a parity effect. This is the substrate-IS content: the fabric's PH-parity (scheme-free) and the fabric's a₀-grade spectral-moment value (regulator-class-keyed) are two independent substrate properties.

**2. The precise `registry:18817` re-tag: TWO orthogonal pins, NOT a global EARNED demotion.** The guard should read:

> **`{APS,CS,BC}` secondary-class scheme-independence: FORCED** by (degree-0 ∧ PH-even-variance). `Var_a(1−|v_a|²) = Var_a(|v_a|²)` ⇒ PH-EVEN ⇒ `⟨Var_a, β^{odd}⟩ = 0` (S90-AQ precedent: `delta_scheme = 0.000e+00` for even η=0 objects). DISTINCT from S93 W9-3's EARNED `ρ`-invariant Reading-A.
> **∧ UV-regulator `{zeta,PV,Mellin}` `B(R)`: SD-OPEN** (orthogonal axis), at the K-dependent `κ_R(K)` profile only — the a₀-grade volume offset is annihilated by the `d²/d(ln K)²` log-derivative (D2.1, Sage-exact). See §VII.AV; CF-S117.

The two-axis qualification is REQUIRED (degree-0 does NOT close the UV-regulator axis — answering the team-lead's framing question directly: NO, my degree-0 argument does not reach the even UV-regulator axis). But the qualification is two ORTHOGONAL pins, NOT a single muddied "PARTIAL/EARNED" status: the FORCED claim on the secondary-class axis is NOT weakened by the SD-OPEN status on the orthogonal UV-regulator axis. A global "EARNED" demotion would wrongly erase the structural content that explains why `L_emp`'s `{APS,CS,BC}` collapse is forced while `ρ`'s is earned. Route the §A8.1(i) wording to mack via housekeeping (per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` + the capstone-hygiene §A path).

**3. CF-S117 sharpened — TWO orthogonal pre-registered tests, not one.**
- **(i) Secondary-class test:** `delta_scheme({APS,CS,BC})` for `L_emp` at `n=0`. PREDICTED `→ 0` (FORCED; parity). A non-zero result FALSIFIES the parity argument and vindicates lizzi's secondary-axis `β^{even}` (the D1 falsifier). Low expected information — but it closes the `n=0`-specific scope-limit S90-AQ leaves open.
- **(ii) UV-regulator test:** `B(R)` across `{zeta, PV, Mellin}` at `K_horizon`. This is the GENUINE open gate — but its target is the K-DEPENDENT profile of `κ_R(K)`, NOT the a₀-volume offset (D2). It lands on lizzi's FI/SD regulator-classification axis, not the parity axis. The W8-2 PASS (`L_emp_FULL = proxy`, rel 7.3e-11, `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED`) certified FULL-PV = Casimir-proxy WITHIN PV — it does NOT span `{zeta, Mellin}`; that span is the unmet gate.

**4. Extension to the `[[secondary-class-collapse-selection-rule]]` memory.** The rule "degree-0 ∧ sign-blind/magnitude ⇒ FORCED collapse" is now **axis-scoped**: it forces collapse on the SECONDARY-CLASS axis `{APS,CS,BC}` ONLY. A secondary-class FORCED collapse does NOT imply UV-regulator `{zeta,PV,Mellin}` independence — that is a separate FI/SD question at the `B(R)` plateau, on an axis the parity/degree selection does not reach. The selection rule gains a standing caveat: **secondary-class FORCED ⊬ UV-regulator independent.** This is the durable structural output of this workshop (per `output-standards.md §"What Changed"` — a structural change, not a numerical revision).

### QUESTIONS

**Answers to lizzi's L3 Q1–Q4.**

**A1 (Q1 — is the `{APS,CS,BC}` scheme-difference purely `β^{odd}`, or does it carry `β^{even}`?).** Purely `β^{odd}` on the secondary-class axis — proven by YOUR S90-AQ precedent (`delta_scheme = 0.000e+00` EXACTLY for an even observable; D1.1). A surviving inherited `β^{even}` in the `{APS,CS,BC}` difference is incompatible with `delta_scheme = 0` for an even object. The `β^{even}` you correctly identify is the `{zeta,PV,Mellin}` UV-regulator difference — an ORTHOGONAL axis (framework four-axis orthogonality), NOT inherited by `{APS,CS,BC}`. **Scope-limit conceded:** S90-AQ may not be at `n=0`; I therefore do NOT claim PURELY-odd at `n=0` by precedent — I PRE-REGISTER the direct `delta_scheme({APS,CS,BC})` compute at `n=0` as the falsifier (CF-S117 test (i)).

**A2 (Q2 — the a₀ grade: what forces the embedded a₀-grade local term scheme-universal where regulator schemes diverge most?).** Nothing needs to force it — `L_emp` annihilates it. The a₀-grade UV-regulator spread (zeta: a₀ absent; cutoff: a₀ dominant) is the K-INDEPENDENT volume / cosmological-constant term, and `L_emp = d²/d(ln K)²` kills any K-independent regulator offset (D2.1, Sage-exact: additive-in-log `c_R → 0`, multiplicative `e^{c_R} → 0`; only `r_R''(u) ≠ 0` survives). The CC-problem-at-one-pole you invoke lives in the FULL trace `Tr^{(L)}_R(K)`, not in its second K-log-derivative. So "`n=0` is the worst place" is true for the trace and inverts for `L_emp`: the log-derivative is built to project out exactly the a₀-volume sensitivity. The residual openness is the K-DEPENDENT `κ_R(K)` profile — narrower, and the real CF-S117 (ii) target.

**A3 (Q3 — axis scope of `registry:18817`: secondary-class or UV-regulator?).** SECONDARY-CLASS axis. I CONCEDE FORCED there and ACCEPT an axis-scope re-tag — but as TWO orthogonal pins (EMERGENCE 2): "`{APS,CS,BC}` secondary-class FORCED (parity; even-blind)" **∧** "`{zeta,PV,Mellin}` UV-regulator SD-OPEN (`B(R)`, K-dependent profile)". NOT a global flip-to-EARNED: that would erase the FORCED/EARNED structural content (why `L_emp` is forced and `ρ` earned). The guard certifies the secondary-class axis; the UV-regulator axis is a separate, orthogonal pin — route to mack.

**A4 (Q4 — is "SOLE discriminator" defensible given `B(R)`?).** I WITHDRAW "SOLE" globally (CONVERGENCE 3). Parity is the sole discriminator of the **secondary-class-axis FORCED/EARNED split**; the UV-regulator class is a second, parity-orthogonal degree-0 discriminator. I do NOT claim `B(R)` is regulator-INVARIANT for `L_emp` (that would contradict `math-scripts.md`'s plateau conclusion AND your §VII.AV finding). I claim something narrower and NEW: `B(R)`'s regulator-keying lives on the K-DEPENDENT part of `κ_R(K)` (the `r_R''(u)` term), NOT the a₀-volume offset (annihilated, D2). So the CF-S117 gate is the `B(R)` spread across `{zeta,PV,Mellin}` at `K_horizon` restricted to the K-dependent kernel profile — and yes, it lands on YOUR FI/SD regulator-classification axis, not the parity axis. Named as CF-S117 test (ii).

---

## Round 2 — lizzi: Cross-Synthesis

**Substrate framing held.** The substrate IS the BdG occupation-variance `Var_a(|v_a(K)|²)` of the eigenmodes of `D_K` on the `M_2(ℂ)` child, and `C = τ_x K` is the fabric's intrinsic particle-hole conjugation. The regulator class `R` is the OTHER substrate-IS choice — WHICH spectral functional defines the fabric's action (my program: zeta vs cutoff give different physics from the SAME `D_K`). The direction holds: `Substrate IS the occupation-variance → bridge map → laboratory secondary-class / a₀-grade measurement`. The adjudication below separates two substrate-IS properties of the same fabric: its PH-parity (scheme-free) and its a₀-grade spectral-moment value (regulator-class-keyed).

### CONVERGENCE

**The verdict is PARTIAL (two-axis): `{APS,CS,BC}` secondary-class FORCED ∧ `{zeta,PV,Mellin}` UV-regulator SD-OPEN. connes's R2 conceded the two-axis split; I confirm it and add the regularization-axis rigor.** Four convergences.

**1. D1 — I CONCEDE the re-routing of my `β^{even}`. My L1-Term-2 attribution was wrong; connes is right, and his own use of MY S90-AQ precedent is the clean proof.** I attributed an even counterterm `β^{even}` to the `{APS,CS,BC}` *secondary-class difference itself*. But `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR` returned `delta_scheme = 0.000e+00` EXACTLY for an even (η=0) observable, with `GV_APS = GV_CS = −1.208158e+08` — and `delta_scheme` is the FULL `{APS,CS}` spread paired against the observable, not its odd part. If `{APS,CS,BC}` carried an inherited even UV-counterterm, no even observable could return `delta_scheme = 0` (`⟨even, β^{even}⟩ ≠ 0`). It returned 0. Therefore the `{APS,CS,BC}` difference, paired against an even object, is purely `β^{odd}`: the three are transgression-representatives of ONE secondary class (APS-η, Bismut-Cheeger η-form, Cheeger-Simons character all represent the same UV-finite class). **My `β^{even}` is REAL but it lives on the ORTHOGONAL `{zeta,PV,Mellin}` UV-regulator axis, NOT inside `{APS,CS,BC}`.** The "embedding" intuition (APS is "ζ-named") conflated the regularization METHOD that NAMES a secondary scheme with the UV-regulator AXIS — the framework's four-axis orthogonality (`regulator-pin-discipline.md`) separates them. I accept the re-route, with connes's pre-registered **scope-limit**: S90-AQ may not have run at the `n=0` grade, so PURELY-odd at `n=0` is not closed by precedent — the direct `delta_scheme({APS,CS,BC})` at `n=0` is the falsifier (his CF test (i)). I endorse pre-registering it.

**2. The 2×2 orthogonal grid is correct and is the durable structural output.** connes's EMERGENCE-1 grid — column = PH-parity axis `{APS,CS,BC}` (sorts FORCED/EARNED via `C : D_K → −D_K`); row = UV-regulator axis `{zeta,PV,Mellin}` (SD-OPEN for both `L_emp` and `ρ`) — is right. The axes are orthogonal because `C` is a SPECTRAL involution acting trivially on the regulator-class index `R` (my Re:C4 Step 4, conceded both ways). `L_emp` occupies cell `(even, SD-OPEN)`: parity-protected on the secondary-class axis, regulator-exposed on the UV axis.

**3. Parity is load-bearing on the secondary-class axis (C4.1/C4.2).** Degree-0 alone cannot sort `ρ`-earned (PH-ODD, `η(−D)=−η(D)`) from `L_emp`-forced (PH-EVEN); parity does. I conceded this in R1 and hold it. connes's withdrawal of "SOLE discriminator" → "sole discriminator of the *secondary-class-axis* FORCED/EARNED split" is the correct scoping.

**4. The static normalization is CLOSED on my axis.** The 8 s52 amplitudes are genuine single-mode BdG coherence factors (`|u_a|²+|v_a|²=1` mode-by-mode): Fermi-surface-lock `v²(B2[0])=½` at ε=0 (S64) + BCS shell exactness (S70), no multi-band hybridization. So PH-evenness of the variance is not broken by a composite-amplitude failure. connes's "one honest assumption" is discharged.

### DISSENT

**I DISSENT on the MECHANISM of D2 while CONVERGING on its verdict-direction (SD-OPEN). connes's D2 proves the wrong half of the a₀ structure is annihilated; the half that physically carries the cosmological-constant content — the ADDITIVE-IN-TRACE counterterm — is NOT annihilated, and a K-dependent regulator-class residue survives. Sage-exact, this turn.**

**The split connes proved (correct, conceded).** For a regulator difference entering MULTIPLICATIVELY — `κ_R(K) = e^{c_R}·κ_0(K)`, equivalently additive-in-log `ln κ_R = ln κ_0 + c_R` — the log-derivative annihilates it:
```
L_emp(R) − L_emp(0) = d²/d(ln K)²[ln κ_0 + c_R] − d²/d(ln K)²[ln κ_0] = 0.   (Sage-exact: residue ≡ 0)
```
This IS the multiplicative-normalization-cancellation theorem (`math-scripts.md`, K=3 MANDATORY) re-applied to the regulator offset instead of `w(L_max)`. connes is RIGHT for this case, and it is a genuine refinement: the K-INDEPENDENT part of any regulator offset is killed by `L_emp`.

**Where D2.1 Step 3 fails — the a₀ counterterm is ADDITIVE-IN-TRACE, not multiplicative.** The a₀ / cosmological-constant coefficient is the canonical *additive* local counterterm. It enters the spectral action ADDITIVELY: `S = f_0 Λ^d a_0 + f_2 Λ^{d−2} a_2 + …`; zeta scheme `S_ζ = ζ_D(0) = a_4` has a₀ **ABSENT**, cutoff scheme has a₀ = `f_0 Λ^d` **DOMINANT** — the difference is a finite local term *ADDED TO* the trace, not a prefactor *MULTIPLYING* it. So the correct structure is `κ_R(K) = κ_0(K) + Δ_R` (additive-in-trace), which connes's D2.1 Step 3 silently re-wrote as `e^{c_R}κ_0` (multiplicative). The two behave OPPOSITELY under `L_emp`:

```
Substitution chain (Sage-exact, this turn; u = ln K, g = κ_0):

  Step 1: a₀ regulator offset enters the TRACE additively: κ_R(u) = κ_0(u) + Δ_R.   [CC counterterm is additive]
  Step 2: L_emp(R) = d²/du² ln(κ_0(u) + Δ_R).                                         [definition]
  Step 3: L_emp(R) − L_emp(0)
            = ((Δ² + 2Δg)g'² − (Δ²g + Δg²)g'') / (Δ²g² + 2Δg³ + g⁴)                  [Sage simplify_full]
            = Δ·d/du[ −g'/g² ] + O(Δ²)                                                [leading order in Δ]
  Step 4: residue = 0  IFF  Δ=0 (no offset) OR g'=g''=0 (constant base, no K-dependence).
  Conclusion: an ADDITIVE-IN-TRACE a₀ offset is NOT annihilated — a K-dependent, Δ_R-linear residue survives.
```

For the CLEANEST possible base — a pure power law `κ_0 = A·K^α` (zero intrinsic log-curvature, `L_emp(0)=0`) — the a₀ counterterm *induces* `L_emp` out of nothing:
```
L_emp(R) − 0 = A·Δ_R·α²·K^α / (A·K^α + Δ_R)²  →  O(α²) when Δ_R ∼ A·K^α  (the cutoff-dominant, a₀-LARGEST regime).
```

**So my "`n=0` is the worst place" does NOT cleanly invert for `L_emp` — it is TEMPERED, not reversed.** connes is right that the K-INDEPENDENT part of the a₀ spread is projected out (this is exactly why `L_emp` is *more* protected than the bare trace — the log-derivative kills the pure volume term). But the a₀ counterterm is additive-in-trace, and an additive-in-trace constant passes through the *nonlinear* `ln` before the K-derivative, generating a SURVIVING K-dependent residue whose magnitude is set by the log-curvature of the base kernel at `K_horizon` and is `O(1)` precisely in the cutoff-dominant regime where the a₀ spread is largest. The cosmological-constant problem does not vanish at `n=0`; it is *attenuated to its K-dependent shadow* — and that shadow is real, untested, and on my axis.

**Net on D2:** I AGREE the UV-regulator axis is SD-OPEN (convergence on verdict-direction). I DISAGREE that the a₀ offset is cleanly removed and the openness is "narrower/weaker." The additive-in-trace residue keeps the a₀ grade IN the open target. The dissent makes the SD-OPEN *harder* to close, not easier — and it sharpens CF-S117 (ii): the gate must probe the additive-in-trace `Δ_R × (base log-curvature)` interference, not merely a generic K-dependent kernel profile disjoint from a₀.

### EMERGENCE

**1. The spectral-functional refinement of the multiplicative-normalization-cancellation theorem: ANNIHILATES multiplicative (additive-in-log) prefactors; does NOT annihilate additive-in-trace counterterms.** The theorem's three K-counter instances (L_max-truncation weight, τ-moduli weight, Casimir-ceiling weight) are ALL multiplicative `w · g(K)` — all annihilated. The a₀ / CC grade is the canonical ADDITIVE-IN-TRACE case — the complement class. This is a **scope-boundary** on the K=3 MANDATORY theorem, not a new annihilation instance (it is a non-annihilation result). The standing guard it plants: *do not cite the cancellation theorem to claim UV-regulator-independence of an `n=0` even moment* — the W8 WP's "PROXY-REFINEMENT DISCHARGED" (FULL-PV = Casimir proxy, rel 7.33e-11) certifies L_max-invariance WITHIN PV; it does NOT span `{zeta, Mellin}`, and the additive a₀ residue is exactly what a within-PV check cannot see.

**2. The CC problem in microcosm — and why `L_emp` is the right place to see it tamed-but-not-killed.** The cosmological constant IS the additive-in-trace spectral moment whose presence and value are regulator-class-selected (zeta: absent; cutoff: dominant) — the core of my program. `L_emp = d²/d(ln K)²` is the operator that suppresses the K-INDEPENDENT (pure-volume) part of that selection — so `L_emp` is structurally *more* CC-protected than the bare action. But "more protected" ≠ "immune": the additive counterterm survives as its K-dependent shadow. `L_emp` localizes the CC's regulator-sensitivity onto the K-DEPENDENT kernel profile — a genuine, narrowed, but non-empty target. This is the substrate-IS statement: the fabric's PH-parity is scheme-free; the fabric's a₀-grade moment value is not, even after the log-derivative.

**3. The `[[secondary-class-collapse-selection-rule]]` caveat, now Sage-grounded.** The rule "degree-0 ∧ PH-even-variance ⇒ FORCED collapse" forces collapse on the `{APS,CS,BC}` secondary-class axis ONLY. The standing caveat is now mechanically proven, not asserted: **secondary-class FORCED ⊬ UV-regulator independent**, because the additive-in-trace regulator counterterm survives `L_emp` (a K-dependent residue, Sage-exact) on an axis the parity selection cannot reach (`C` acts trivially on `R`). This is the durable structural output (a structural change per `output-standards.md §"What Changed"`).

**Answers to connes's D1/D2.** D1: CONCEDED — `β^{even}` re-routed off `{APS,CS,BC}` (purely odd by S90-AQ) onto `{zeta,PV,Mellin}`; the `n=0`-specific `delta_scheme` direct compute is the right falsifier for the scope-limit. D2: the log-derivative annihilates the K-independent / multiplicative part of the a₀ offset (you are right), but the a₀ counterterm is ADDITIVE-IN-TRACE and its K-dependent residue survives (Sage-exact) — the UV-regulator axis stays SD-OPEN with the a₀ grade INSIDE the target, not relocated off it.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Parity selection firing for Var_a(\|v_a\|²) | C1, Re:C1, L1 | **Converged** | The bare 8-mode variance is PH-EVEN by the affine identity `Var(1−X)=Var(X)` (Sage-QQ `Var(\|v\|²)=Var(\|u\|²)=327477/3125000`, residual 0), so `⟨Var_a, β^{odd}⟩=0`. The rigorous forcing predicate is the CENTERED variance's PH-evenness — NOT "sign-blind `\|v\|²`" (the per-mode `(1−ξ/E)/2` and the MEAN are PH-ODD-affine). connes's correction verified both sides. |
| 2 | PH-closure of the (4+1+3) 8-mode set | C2, Re:C2, L2 | **Converged** | Closure is IRRELEVANT to bare-variance PH-evenness (affine identity holds weight-for-weight on the non-PH-closed `{0.7704×4, 0×1, 0.176×3}` set). Pressure-point (b) WITHDRAWN. The real closure question RELOCATES one object up — to the divergent s=4 trace-tail, where the parity-asymmetric mode selection (`B1`'s `\|v\|²=1` partner outside the 8-set) meets the regulator-class subtraction = the `B(R)` carry-forward. |
| 3 | §23.0(5) precedent — same failure mode? | C3, Re:C3, D2 | **Partial** | `d_A(L_emp)=0` is correct (dimensionless log-derivative; no odd `M_KK^1` scale leg to mis-tag — the §23.0(5) scale-leg failure mode does NOT match). But `d_A=0` does NOT certify regulator-cleanliness: the ADDITIVE-IN-TRACE a₀ counterterm is a DIFFERENT object on the orthogonal UV-regulator axis that §23.0(5) doesn't police and `L_emp` does NOT annihilate (Sage-exact). The governing precedent is the multiplicative-normalization-cancellation theorem's own SCOPE BOUNDARY. |
| 4 | FORCED vs EARNED structural verdict | C4, Re:C4, D1, D2 | **Partial (two-axis)** | Secondary-class `{APS,CS,BC}` **FORCED** (parity; `L_emp` PH-even, blind to `β^{odd}`; S90-AQ `delta_scheme=0` precedent; DISTINCT from `ρ`'s EARNED S93 W9-3) **∧** UV-regulator `{zeta,PV,Mellin}` **SD-OPEN** (`B(R)`; the additive-in-trace a₀ residue survives `L_emp`, §VII.AV, CF-S117 (ii)). Guard re-tag = TWO orthogonal pins, NOT a global EARNED demotion and NOT FORCED-full. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **`B(R)` three-regulator span at `n=0` (the genuine SD-OPEN gate).** Compute `L_emp = d²ln κ_R(K)/d(ln K)²|_{K_horizon}` for `R ∈ {zeta, PV, Mellin}` and report the `{zeta,PV,Mellin}` span. Pre-registered gate: **SD-CONFIRMED** if span > 3 OOM above the W8-2 within-PV floor `7.33e-11 M_KK²`; **FI-PROMOTE** if span < `1e-3 M_KK²` (rel_tol per `L_emp = −7.046336` 7-sig-fig publication precision, Class-8.3). This is CF-S117 test (ii) and lands on the FI/SD regulator-classification axis, NOT the parity axis.

2. **Additive-vs-multiplicative decomposition of `κ_R(K)` at `K_horizon`.** Extract `Δ_R` (the additive a₀-counterterm magnitude, zeta vs PV vs Mellin) and the base log-curvature `d²ln κ_0/d(ln K)²|_{K_horizon}`; verify the surviving SD contribution is the additive residue `Δ_R·d/du[−κ_0'/κ_0²]` (Sage closed form, this workshop), NOT the multiplicative channel. Pre-registered gate: declare **additive-channel-dominant** if `|additive residue| > |multiplicative residue|` at `K_horizon`; the residue is `O(1)` if `Δ_R ∼ κ_0(K_horizon)`, suppressed if `Δ_R ≪ κ_0`.

3. **Direct `delta_scheme({APS,CS,BC})` for `L_emp` PINNED at curvature-grade `n=0`** (the D1 falsifier; refinement of the already-minted CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION — pin its `{APS,CS,BC}` compute to `n=0` specifically, closing the S90-AQ scope-limit which may not have run at `n=0`). Pre-registered gate: `|delta_scheme| < 1e-3 M_KK²` = **FORCED-CONFIRMED** (parity prediction); `> 1e-3` = parity **FALSIFIED**, secondary-axis `β^{even}` vindicated.

4. **Is the a₀ additive residue suppressed at the framework's actual `K_horizon`?** The surviving residue magnitude depends on the base kernel's log-curvature at `K_horizon` (supersonic transit ⇒ strong K-variation ⇒ `O(1)`; slowly-varying ⇒ suppressed). Open: compute `d²ln κ_0/d(ln K)²` at the substrate's actual `K_horizon` to bound whether the SD-OPEN is observationally large or negligible. (Distinct from OQ-1: OQ-1 measures the span; OQ-4 explains its magnitude via the transit profile.)

## Wrap-Up — Workshop Impact Summary

### What Changed

#### (a) Numerical revisions

- `Var_a(|v_a|²) = Var_a(|u_a|²) = 327477/3125000 = 0.10479264` (QQ-exact, residual 0) — connes's parity correction independently Sage-verified; `mean_v = 282/625`, `mean_u = 343/625`, `mean_v + mean_u = 1` (the MEAN is PH-ODD-affine; only the centered variance is PH-even).
- Additive-in-trace residue (Sage `simplify_full`, this turn): `L_emp(R) − L_emp(0) = Δ·d/du[−g'/g²] + O(Δ²)` — the surviving UV-regulator-class spread quantified; `≡ 0` only for `Δ=0` or constant base.
- Pure power-law induced residue (Sage): `AΔα²K^α/(AK^α + Δ)²` — `O(α²)` when `Δ ∼ AK^α` (cutoff-dominant, a₀-largest regime).

#### (b) Structural changes

- "sign-blind `|v|²`" → **"PH-even CENTERED variance" (`Var(1−X)=Var(X)`)** — the rigorous forcing predicate (epistemic type: a per-mode magnitude heuristic replaced by a centered-cumulant parity theorem).
- single-axis "FORCED" → **TWO orthogonal pins**: secondary-class `{APS,CS,BC}` FORCED ∧ UV-regulator `{zeta,PV,Mellin}` SD-OPEN (verdict PARTIAL two-axis — NOT FORCED-full, NOT global-EARNED).
- L1-Term-2 `β^{even}` **RE-ROUTED**: off the `{APS,CS,BC}` secondary-class difference (purely `β^{odd}` by S90-AQ `delta_scheme=0`) onto the orthogonal `{zeta,PV,Mellin}` UV-regulator axis.
- multiplicative-normalization-cancellation theorem gains a **SCOPE-BOUNDARY** (epistemic type promotion: annihilation-theorem → annihilation-theorem-with-declared-complement): annihilates MULTIPLICATIVE / additive-in-log offsets; does NOT annihilate ADDITIVE-IN-TRACE counterterms (the a₀/CC grade).
- `[[secondary-class-collapse-selection-rule]]` gains the Sage-grounded standing caveat: **secondary-class FORCED ⊬ UV-regulator independent.**

### What Holds

- The bare-variance parity selection FIRES (Topic 1, Converged): `⟨Var_a, β^{odd}⟩ = 0`.
- `{APS,CS,BC}` secondary-class scheme-independence is FORCED for `L_emp` (parity; even-blind; S90-AQ `delta_scheme=0` precedent), DISTINCT from S93 W9-3's EARNED `ρ`-invariant Reading-A — the registry MUST NOT record the eventual CF `L_emp` PASS as co-equal with S93 W9-3.
- single-mode BdG normalization `|u|²+|v|²=1` closed (Fermi-surface-lock S64, BCS shell exactness S70) — no hybridization, parity unbroken.
- `d_A(L_emp) = 0` (dimensionless log-derivative; no odd `M_KK^1` scale leg) — the §23.0(5) scale-leg failure mode does NOT match `L_emp`.
- W8-2 `MULTIPLICATIVE-NORMALIZATION-CANCELLATION` (FULL-PV = Casimir proxy, rel 7.33e-11) — WITHIN-PV L_max-invariance holds; certifies ONE regulator class.

### What Breaks or Strains

- The registry §VII.AV (§A8.1(i)) guard at `permanent-results-registry.md:18819` STRAINS: it reads the FORCED as broad scheme-independence and uses the imprecise "sign-blind magnitude-sector" predicate. Both need correction (axis-scope + variance-centering). Routed to mack.
- The a₀-grade UV-regulator axis is genuinely SD-OPEN — NOT closed by D2's multiplicative annihilation (the additive-in-trace a₀ residue survives `L_emp`). The W8 Level-2 "PROXY-REFINEMENT DISCHARGED" (within-PV) must NOT be read as cross-class `{zeta,Mellin,PV}` independence.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

**CF-1 — `B(R)` three-regulator certification at `n=0` (the genuine SD-OPEN gate).**
1. **What**: compute `L_emp = d²ln κ_R(K)/d(ln K)²|_{K_horizon}` for `R ∈ {zeta, PV, Mellin}`; report the `{zeta,PV,Mellin}` span.
2. **Inputs**: the s52 8-mode BdG amplitude trajectory `v_a(K)`; the `K_horizon` anchor; the FULL-PV pipeline `s91_w5_1_full_bdg_pv.npz`; zeta + Mellin regulated traces of `Tr_{M₂(ℂ)}(P_BdG|D_K|^{−2s})` at `s=4` on the L12/L14 caches.
3. **Gate**: SD-CONFIRMED if span > 3 OOM above the W8-2 within-PV floor `7.33e-11 M_KK²`; FI-PROMOTE if span < `1e-3 M_KK²` (rel_tol per the 7-sig-fig publication precision of `L_emp = −7.046336`, Class-8.3).
4. **Effort**: medium (one new script; zeta + Mellin regulated-trace evaluators on the existing caches). **Depends on**: W8-2 FULL-BdG result; `s91_w5_1_full_bdg_pv.npz`.

**CF-2 — additive-vs-multiplicative decomposition of the regulator difference at `K_horizon` (what D2's resolution leaves open).**
1. **What**: extract `Δ_R` (the additive a₀-counterterm magnitude per scheme) and the base log-curvature `d²ln κ_0/d(ln K)²|_{K_horizon}`; verify the surviving SD contribution is the additive residue `Δ_R·d/du[−κ_0'/κ_0²]`, not the multiplicative channel; quantify whether the residue is `O(1)` (`Δ_R ∼ κ_0`) or suppressed (`Δ_R ≪ κ_0`) at the substrate's actual `K_horizon`.
2. **Inputs**: the `κ_R(K)` profiles from CF-1; the Sage additive-residue closed form `(Δ²+2Δg)g'² − (Δ²g+Δg²)g'')/(Δ²g²+2Δg³+g⁴)` (this workshop, EMERGENCE 1).
3. **Gate**: declare additive-channel-dominant if `|additive residue| > |multiplicative residue|` at `K_horizon`; FI if `|residue| < 1e-3 M_KK²`.
4. **Effort**: low (post-processing of CF-1 outputs + the closed-form residue). **Depends on**: CF-1.

*(The already-minted `CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION` is NOT relisted; this workshop's refinement of it — pin its `{APS,CS,BC}` compute to curvature-grade `n=0` as the D1 falsifier — is annotated in the W8 WP at `session-116-w8-workingpaper.md:190`.)*

### Effected In-Session (NON-MATH — completed by the final agent BEFORE TERMINATING)

- [x] **agent-memory (permanent classification)** — recorded the `L_emp` two-axis verdict (secondary-class FORCED ∧ UV-regulator SD-OPEN) + the additive-in-trace-survives scope-boundary as a permanent FI/SD theorem at `.claude/agent-memory/lizzi-spectral-functional-theorist/permanent_theorems.md:22`; index pointer appended at `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md:5`.
- [x] **W8 WP overclaim annotation** — added the two-correction workshop-refinement note (sign-blind → PH-even centered variance; secondary-class-axis-only scope; UV-regulator SD-OPEN caveat; pin `{APS,CS,BC}` compute to `n=0`) at `sessions/session-116/session-116-w8-workingpaper.md:190`.
- [x] **math-scripts.md scope-boundary (additive-in-trace NOT annihilated)** — a `.claude/rules/` edit is harness-blocked for subagents (corpus content routes to `sessions/framework/registry/`). The scope-boundary directive content is recorded in agent-memory (`permanent_theorems.md:22`) + the workshop EMERGENCE 1 derivation; the registry/corpus-facing portion (cross-pillar-bridge-corpus §22 `B(R)` calibration; `mack-cosmic-bridge` sole-writer domain) is routed to mack below. No rule-file diff surfaced for orchestrator application (per the harness directive: the corpus IS the destination).
- [x] **routed-to-mack** — §VII.AV §A8.1(i) guard re-tag at `permanent-results-registry.md:18819`. Precise spec: REPLACE the predicate "structurally FORCED by (degree-0 homogeneity ∧ **sign-blind magnitude-sector construction `Var_a(|v_a|²)`**)" WITH "structurally FORCED by (degree-0 ∧ **PH-EVEN CENTERED VARIANCE: `Var_a(1−|v_a|²)=Var_a(|v_a|²)`** by the affine identity `Var(1−X)=Var(X)`, Sage-QQ `327477/3125000`; S90-AQ `delta_scheme=0.000e+00` precedent for even η=0 objects)"; AND ADD the orthogonal pin "**∧ UV-regulator `{zeta,PV,Mellin}` `B(R)`: SD-OPEN** — the secondary-class FORCED does NOT imply UV-regulator independence; the a₀-grade (n=0) regulator difference is ADDITIVE-IN-TRACE (CC counterterm) and survives the `d²/d(ln K)²` log-derivative (Sage-exact; only multiplicative/additive-in-log offsets are annihilated), §VII.AV B(R), CF-S117 (ii)". Routing: SendMessage(to: "main") sent (mack is sole-writer of §VII.AV registry text + cross-pillar-bridge-corpus §22 per `feedback_mack-bridge-role.md` / capstone-hygiene §A path).

### Closing Line

The fabric's particle-hole parity is scheme-free and forces the `{APS,CS,BC}` collapse; the fabric's a₀-grade spectral-moment value is regulator-class-keyed and survives `L_emp` as a K-dependent residue — `L_emp` is parity-protected on one axis and cosmological-constant-exposed on the other. FORCED on the secondary-class axis; SD-OPEN on the UV-regulator axis. PARTIAL, two orthogonal pins.
