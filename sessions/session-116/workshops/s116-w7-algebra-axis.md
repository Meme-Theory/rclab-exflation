# S116-W7-ALGEBRA-AXIS — §VII.AJ STATE-PROJ ⊥ OP-PROJ: orthogonal companions or collapse?

**Date**: 2026-06-27
**Gate**: `S116-W7-ALGEBRA-AXIS` (gate_type: workshop, Wave 7, Session 116)
**Format**: 2-agent adversarial adjudication, 3 rounds, sequential turns on this shared document
**Agents**: `volovik-superfluid-universe-theorist` (argues **ORTHOGONAL** — distinct algebra-axis corners) vs `landau-condensed-matter-theorist` (argues **COLLAPSE** — one 3He-B gap-anisotropy observable two ways; OP-PROJ spurious)
**Closure**: artifact-existence (NO verdict line, per `wave-classification.md §M1`). Must end with R1/R2/R3 filled + a `## Structural Verdict` (ORTHOGONAL vs COLLAPSE, resolved from first principles: the 4-corner parse-tree classification + the regulator-response sibling discriminator + the BCS gap-equation linkage) + `## Wrap-Up`.
**Dispatch order**: AFTER `S116-W7-STATEPROJ-BCS` (the workshop consumes `R_STATE`'s sign + value + Track-A/B provenance); the structural verdict is independently derivable from the registry texts, so a compute INFO/FAIL does NOT block this workshop.

## Adjudication Question

> Is §VII.AJ.STATE-PROJ (`R = +0.03536`; algebra-DEPENDENT state-pair functional on the BCS occupation) a genuine substrate-IS observable ORTHOGONAL to §VII.AJ.OP-PROJ (`R_∞ ≈ −1.892`; algebra-INVARIANT spectrum-only multiplicity-weighted Mellin-pole-window count), or do the two projection-side readings COLLAPSE to one observable?
>   (a) **PARSE-TREE STRUCTURE**: does STATE-PROJ parse to a state-pair functional `ρ(P·A)` (Corner III/IV, algebra-DEPENDENT) and OP-PROJ to a spectrum-only `F({λ_k, m_k})` (Corner I/II, algebra-INVARIANT), placing them in DISTINCT corners of the §VII.U.2 4-corner partition?
>   (b) **SIGN FLIP**: is the OP-PROJ-negative / STATE-PROJ-positive sign flip evidence of orthogonality (two physically different observables), or evidence that the OP-PROJ spectral count is a MIS-SPECIFIED image of the lab gap-asymmetry (landau's steelman: only STATE-PROJ is the correct substrate image; OP-PROJ is spurious → really ONE observable)?
>   (c) **BCS MEAN-FIELD COLLAPSE**: does the BCS gap equation LINK the spectral count (OP-PROJ) and the occupation asymmetry (STATE-PROJ) so tightly that in the mean-field limit they are the same observable two ways (collapse), or does the gap-self-regularization of the state-pair functional (regulator-INVARIANT) vs the regulator-DEPENDENT spectrum count (algebra-axis sibling discriminator) keep them structurally separate (orthogonal)?

## Competing Positions

- **volovik-superfluid-universe-theorist — ORTHOGONAL.** STATE-PROJ and OP-PROJ are in DIFFERENT corners of the algebra-axis 4-corner partition. OP-PROJ is a spectrum-only count `F({λ_k,m_k})=Σ m_k g(λ_k)` (algebra-INVARIANT, regulator-DEPENDENT, NEGATIVE spectral excess). STATE-PROJ is a state-pair functional `ρ_BCS(P_sector·H_pair)` (algebra-DEPENDENT, regulator-INVARIANT / gap-self-regularized, POSITIVE occupation asymmetry). Per the K-counter (MANDATORY at K=3), the two families are STRUCTURALLY ORTHOGONAL in identity-class membership; cross-corner co-primary FORBIDDEN. The wildly different values (−1.892 vs +0.03536) + the SIGN FLIP are EXPECTED — different physical quantities on the same nominal (algebra, projector, pole) triple, different projection side. This is the inaugural physical (3He-B) instance of the orthogonality conjecture.
- **landau-condensed-matter-theorist — COLLAPSE.** The two are the SAME 3He-B gap-anisotropy observable measured two ways; a spectral count and an occupation asymmetry are LINKED by the BCS gap equation (the occupation `v_k²` IS a functional of the same D_K spectrum the count uses), so in the mean-field limit they are not independent. The −1.892 vs +0.03536 split is then a SIGN that the OP-PROJ spectral count is a mis-specified image of the lab asymmetry (only STATE-PROJ is correct), collapsing §VII.AJ to ONE genuine observable plus one spurious — NOT two orthogonal substrate-IS observables. If landau prevails, the algebra-axis orthogonality K-counter takes a hit at its first physical-realization test.

**Numeric stakes**: OP-PROJ `R_∞ ≈ −1.892 ± 0.001` (algebra-INVARIANT, Mellin-pole-window saturation); STATE-PROJ `R = +0.03536` (algebra-DEPENDENT, polycritical gap-asymmetry); S87 substrate count `R_substrate ≈ −1.2122` (L_max=10, the OP-PROJ extrapolant); ratio_mismatch ≈ 1.03 (the S87 FAIL that split §VII.AJ). The `S116-W7-STATEPROJ-BCS` output (R_STATE sign + value + Track-A/B provenance) is the headline structural input.

**Adjudication rule**: a Q1 math/physics adjudication. Resolve from FIRST PRINCIPLES which reading is correct (the 4-corner parse-tree classification + the regulator-response sibling discriminator + the BCS gap-equation linkage), producing a STRUCTURAL VERDICT (orthogonal vs collapse) that either CONFIRMS the algebra-axis K-counter at its first physical instance or registers a structural exception. "No verdict / both tenable" is NOT acceptable.

**Substrate framing** (`phononic-framing.md`): PHONONIC. Both projection-side observables are substrate-IS on `(A_K, H_K, D_K)`; the workshop decides orthogonal companions vs collapse. Direction: `D_K eigenvalues → {spectrum-only count (OP-PROJ) | BCS-state occupation asymmetry (STATE-PROJ)} → lab 3He-B observables`. The 4-corner algebra-axis partition is the structural arbiter; the BCS gap equation is the candidate collapse mechanism landau must wield; the regulator-response sibling discriminator is the candidate separation mechanism volovik must wield.

**Sources** (read before writing):
1. `sessions/framework/Atlas/atlas-07-permanent-results.md` — §VII.AJ.OP-PROJ STAGE-1-CANDIDATE (R_∞ ≈ −1.892, algebra-INVARIANT); §VII.AJ.STATE-PROJ OPEN (R_3HeB_lit = +0.03536, algebra-DEPENDENT)
2. `.claude/rules/cross-pillar-bridge-anatomy.md` — §"Algebra-axis orthogonality K-counter" (MANDATORY at K=3); §"Regulator-behavior sibling discriminator"
3. `.claude/rules/registry-landing.md` — §"Operator-Projection Reading-A Naming Hygiene" (OP-PROJ / STATE-PROJ suffix discipline)
4. `computations/session-87/s87_w11_3heb_excess_inheritance_comparison.py` — the S87 R_substrate ≈ −1.2122 NEGATIVE count vs R_3HeB_lit = +0.03536 POSITIVE lab asymmetry (the FAIL that split §VII.AJ)
5. `computations/session-116/s116_w7_stateproj_bcs.npz` — the W7-1 R_STATE result + sign + Track-A/B provenance

---

## R1 — Opening Positions (steelman your assigned side)

### R1 · volovik-superfluid-universe-theorist — ORTHOGONAL steelman

**Position.** §VII.AJ.OP-PROJ and §VII.AJ.STATE-PROJ are not one observable read two ways. They are two substrate-IS functionals on `(A_K, H_K, D_K)` living in DISTINCT corners of the §VII.U.2 four-corner partition (STAGE-3-PERMANENT, `permanent-results-registry.md:13113`; K=3 MANDATORY enforcement at the registry layer per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`). The direction of explanation is single and substrate-first; both arrows depart the SAME operator:

```
D_K eigenvalues
   ├─ Σ_k m_k g(λ_k)            [OP-PROJ : spectrum-only count]      → lab BdG-undoubled DOS-excess (Y)
   └─ ρ_BCS(P_sector · H_pair)  [STATE-PROJ : state-pair functional] → lab gap-square asymmetry (X)
```

That the two arrows share an origin operator is NOT a collapse. EVERY functional on a spectral triple is a functional of `D_K`; the partition's entire content — and the reason it is K=3 MANDATORY — is that the algebra-INVARIANT family (`F({λ_k,m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT family (state-pair functionals on `A_K`) are STRUCTURALLY ORTHOGONAL in identity-class membership *despite* the shared operator. Collapse must defeat that theorem at its first physical (3He-B) instance; orthogonality is the encoded default.

**(a) Parse-tree — distinct corners, FORM-level, fully substrate-first.**

Reading each parse tree against §VII.U.2 clause (e):

- **OP-PROJ = `Σ_k m_k g(λ_k)`** — inputs are eigenvalues `{λ_k}` and multiplicities `{m_k}`; NO algebra element appears. The functional is invariant under any unitary `U` whose conjugation preserves the spectrum — it cannot see the module structure of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. → **algebra-INVARIANT**. Its window is the multiplicity-weighted Mellin-pole-window at the substrate-distance-1 pole (s=3; `s87_w11_3heb_excess_inheritance_comparison.py` docstring "Mellin-cone substrate-distance-1 pole"). → **Corner I (INVARIANT × s=3)**.

- **STATE-PROJ = `ρ_BCS(P_sector · H_pair)`**, `R = (a−b)/(a+b)`, `a = ρ_BCS(P_A · H_pair)`, `b = ρ_BCS(P_B · H_pair)` (`s116_w7_stateproj_bcs.py §4`, lines 14–17). Inputs are the STATE `ρ_BCS` (BdG occupation `v_k² = ½(1 − ξ_k/E_k)`) AND the sector central projections `P_A, P_B ∈ A_K`. Two algebra elements appear explicitly; the functional is NOT invariant under spectrum-preserving sector-mixing unitaries. → **algebra-DEPENDENT**, state-pair (Corner III/IV). At substrate-distance-1 this is **Corner III (DEPENDENT × s=3)**, matching the §VII.AC.1 precedent for BCS-occupation state-pair functionals (`permanent-results-registry.md:15252`).

The two observables differ on the ALGEBRA-AXIS row (I vs III). That difference ALONE forbids cross-corner co-primary (§VII.U.2 clause (f); `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`, which already names OP-PROJ and STATE-PROJ "STRUCTURALLY ORTHOGONAL in identity-class membership" and rules that they "CANNOT be co-primary anchors of the same theorem; structural-orthogonal-companion is the correct anchor structure"). Crucially: this classification is FORM-level. It is decided by the *appearance of* `P_A, P_B ∈ A_K` in STATE-PROJ's parse tree versus their *absence* from OP-PROJ's — it does not consult a single number. The Track-B magnitude caveat (below) cannot touch it: even if every numerical input to STATE-PROJ were lab-fed, its corner is fixed by its algebra content. The pole-axis is secondary — if STATE-PROJ also sits at a different pole than OP-PROJ, the two are *doubly* orthogonal (cross-pole co-primary likewise FORBIDDEN); but the algebra-axis row difference is already decisive and is the load-bearing claim.

**(b) Sign flip — the fingerprint of two observables, not a defect in one.**

- OP-PROJ: `R_∞ = −1.892` (atlas-07:673, substrate-first L_max→∞ saturation); L_max=10 extrapolant `R_substrate = −1.212219` (`s116…npz`). NEGATIVE: in `(N_unpaired − 2·N_paired)/N_paired`, the BdG-doubling weight (2×) of the paired count exceeds the unpaired Mellin-tail — a density-of-states *geometry* statement.
- STATE-PROJ: `R_STATE = +0.035356` (lab magnitude); substrate-first state-pair FORM on 78,080 cached modes `R_BdG = +0.068847` (`s116…npz`). POSITIVE: the A-sector condensation energy `½N(0)Δ_A²` exceeds the B-sector (`Δ_A > Δ_B`) — a state-*thermodynamic* statement.

A DOS count and a condensation-energy asymmetry are not obligated to share a sign — they answer different questions ("how many modes sit inside the pole window?" vs "how does the occupation-weighted energy split between two sectors?"). The sign flip is the FINGERPRINT of two observables, not a defect in either. And the POSITIVE sign is intrinsic to the state-pair FORM: `R_BdG = +0.0688` is computed on the substrate spectrum `{ξ_k}` (78,080 modes, p+q≤10), confirming `(a−b)/(a+b)` is a genuine BdG-occupation functional — not a bare algebraic ratio — that returns positive whenever `Δ_A > Δ_B`. That is a property of the functional, not of the cryostat.

*Track-B honesty (load-bearing for credibility, not for the argument).* The MAGNITUDE `+0.035356` is lab-fed: the substrate is a single BDI 3He-B child (`N_3 = 0`) with NO intrinsic 3He-A (DIII, `N_3 = 2`) phase, so the A/B gap modulation `SC_corr_A/SC_corr_B` is Serene-Rainer 1983 / Greywall 1986, not substrate-first (`substrate_first_SC_ratio_available = False`; Track B). The `R_BdG` cross-check also borrows the lab A/B modulation for its `Δ_A_sub/Δ_B_sub` split. So my orthogonality case does NOT rest on reproducing `+0.03536` — that reproduction is a tautology (`rel_match_vs_lit = 0.0`). It rests on (i) the algebra-axis FORM classification (Corner I vs III, fully substrate-first) and (ii) the substrate-intrinsic SIGN of the FORM (`R_BdG > 0`), both of which survive the magnitude caveat intact.

**(c) Regulator-response sibling discriminator — a third, independent separation axis.**

Per `cross-pillar-bridge-anatomy.md §"Regulator-behavior sibling discriminator"` (corpus §22): an algebra-DEPENDENT state-pair functional on a GAPPED occupation is regulator-INVARIANT — it is IR-self-regularized by the gap `|Δ|`, since `v_k² = ½(1 − ξ_k/E_k)` with `E_k = √(ξ_k² + Δ²)` decays for `ξ_k ≫ Δ` and the condensation energy `≈ ½N(0)Δ²` is gap-set and UV-insensitive (standard BCS; Volovik 2003 Ch.7). An algebra-INVARIANT spectrum-only count is regulator-DEPENDENT (heat-kernel moment-ratio spread ≈ O(20%)); OP-PROJ inherits this through its Mellin-pole-window scale (the `C_pole` Casimir median that defines "in-window" vs "tail"). This axis is ORTHOGONAL to parse-tree membership (regulator-RESPONSE, not corner-membership) and INDEPENDENT per Hybrid-Independence-Test criterion (iv). If the two were ONE observable two ways they would share ONE regulator response; instead one is gap-self-cut and regulator-flat, the other regulator-dependent. Two regulator fingerprints on the same nominal `(algebra, projector, pole)` triple is a PHYSICAL signature of two observables — the inaugural physical (3He-B) instance of the orthogonality K-counter. (Scope note: the gap-self-regularization of STATE-PROJ is analytically demonstrable as above; the THIS-pair O(20%) UV-regulator spread for OP-PROJ is the §22 generic directive — a fresh `{ζ, Pauli-Villars, cutoff}` spread computation on this specific OP-PROJ count is the clean discriminating CF if landau contests the regulator axis, and I flag it now rather than asserting it as computed.)

**Questions for landau-condensed-matter-theorist (challenge the COLLAPSE):**

1. **IDENTITY vs RELATION.** Your collapse mechanism is the BCS gap equation linking `{λ_k} → {v_k²}`. But a RELATION between two observables is not their IDENTITY. Every observable on `(A_K, H_K, D_K)` is a functional of `D_K`; if "both are functionals of the same spectrum" sufficed to collapse two observables, the whole §VII.U.2 partition (STAGE-3-PERMANENT) would collapse to a point. The gap equation maps spectrum → occupation, but the occupation carries the sector-module label (which `P_sector` each mode lives under) that the bare count `Σ m_k g(λ_k)` discards — the map is many-to-one in *exactly* the data separating Corner I from Corner III. Show me the step where the gap equation IDENTIFIES (not merely relates) `Σ m_k g(λ_k)` with `ρ(P·H)`. What distinguishes your Corner-I↔III collapse from a collapse of the entire partition?

2. **SPURIOUS vs DIFFERENT IMAGE.** You call OP-PROJ "spurious." But being the wrong image of the gap-asymmetry (X) does not make OP-PROJ spurious — it makes it the image of a *different* lab observable Y (the BdG-undoubled DOS excess at the fold). The S87 `ratio_mismatch ≈ 1.03` FAIL was a FAIL of forcing ONE substrate observable to image the gap-asymmetry; the correct response — and what §VII.AJ actually did — was to SPLIT into two: OP-PROJ images Y, STATE-PROJ images X. What is your criterion for "spurious" that does not also condemn every substrate observable that fails to reproduce a chosen lab number? A spectral DOS count is under no obligation to equal a condensation-energy asymmetry.

3. **DIVERGENT REGULATOR RESPONSE.** If the two are one observable two ways, they share a regulator response. STATE-PROJ is gap-self-regularized (regulator-INVARIANT, IR-cut by `|Δ|`); OP-PROJ is regulator-dependent (window/moment-ratio sensitivity). How does the collapse reading account for two different regulator fingerprints on the same nominal `(algebra, projector, pole)` triple — without smuggling in the very algebra-module data whose presence/absence is what defines the Corner-III/Corner-I split?

### R1 · landau-condensed-matter-theorist — COLLAPSE steelman

**Position.** I will not contest the cheap version of collapse, and I concede volovik's parse-tree reading outright: `Σ_k m_k g(λ_k)` and `ρ_BCS(P_sector·H_pair)` are different FORMS, and the appearance of `P_A, P_B ∈ A_K` in one and their absence from the other is a real, value-free distinction. Corner I vs Corner III is correct at the FORM level; cross-corner co-primary stays FORBIDDEN. My collapse is narrower and sharper, and it survives that concession intact: **§VII.AJ does not contain two co-equal substrate-IS observables.** It contains ONE substrate-IS observable carrying genuine substrate-first discriminating content — OP-PROJ, `R_∞ = −1.892` — and one observable whose discriminating content is laboratory-injected and whose substrate-IS image is identically zero — STATE-PROJ. The second is the **laboratory-IN target of the bridge wearing a substrate-FORM costume**, not a second substrate-IS observable. The algebra-axis K-counter's "first PHYSICAL (3He-B) instance" needs BOTH arrows to land in substrate-IS content; only one does.

```
D_K eigenvalues
   ├─ Σ_k m_k g(λ_k)            [OP-PROJ]    → R_∞ = −1.892  : SUBSTRATE-IS (Element 1); no lab input
   └─ ρ_BCS(P_sector · H_pair)  [STATE-PROJ] → R = +0.03536  : value IS R_3HeB_lit (Element 2); lab-injected
                                              substrate-IS image = 0 EXACTLY (single BDI / one order-parameter class)
```

**The symmetry-first reading — STATE-PROJ's content is not the substrate's to give.** 3He-A and 3He-B are two DISTINCT broken-symmetry phases, two different order-parameter manifolds. A-phase (ABM/axial, equal-spin-pairing, `d_μ(k) = Δ_0 ẑ_μ(k_x + ik_y)`, point nodes, `SO(3)_L × SO(3)_S × U(1)` broken to a residual axial group); B-phase (BW, isotropic gap, `d_μ(k) = Δ_0 R_μi k_i`, relative spin-orbit `SO(3)_{L+S}` locked, fully gapped). The gap-asymmetry `(Δ_A² − Δ_B²)/(Δ_A² + Δ_B²)` is a comparison ACROSS these two order-parameter-symmetry classes. The substrate is a SINGLE BDI object (`N_3 = 0`; my wall #8 AZ-class-BDI). It realizes ONE order-parameter symmetry class — the fully-gapped BW-like one — and has no A-phase (DIII, `N_3 = 2`) sector to compare against. **Volovik granted exactly this in his Track-B honesty note** ("the substrate is a single BDI 3He-B child (`N_3 = 0`) with NO intrinsic 3He-A (DIII, `N_3 = 2`) phase"). He just did not follow his own concession to its conclusion: if the substrate has no A-phase, the substrate cannot compute `Δ_A − Δ_B` — it has no `Δ_A`. The asymmetry is a cross-class comparison only one of whose classes exists on the fabric.

**The Δ_BCS-cancellation chain (the value is purely lab; verified to machine ε).**

```
Claim: STATE-PROJ's discriminating value is independent of the substrate gap and vanishes without lab input.

Step 1: R_STATE = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²)            [S87 lit-path; npz R_3HeB_lit]
Step 2: Δ_A = Δ_BCS·SC_corr_A ,  Δ_B = Δ_BCS·SC_corr_B   [npz provenance; SC_corr = Serene-Rainer 1983/Greywall 1986, LAB]
Step 3: R_STATE = Δ_BCS²(SC_A² − SC_B²) / Δ_BCS²(SC_A² + SC_B²)
Step 4:        = (SC_A² − SC_B²)/(SC_A² + SC_B²)          [Δ_BCS cancels EXACTLY — residual 1.73e-16 vs npz]
Step 5: SC_A = SC_B ⇒ numerator = 0 ⇒ R_STATE = 0         [substrate-only limit, no 3He spin-fluctuation feedback]
Conclusion: the substrate gap Δ_BCS = 0.4643 M_KK drops OUT of R_STATE entirely. The value +0.03536 is set
            solely by the lab strong-coupling ratio SC_A/SC_B = 1.151/1.111 — a 3He Landau-parameter number,
            not a substrate number. A substrate-IS observable that does not depend on a single substrate
            quantity is a contradiction in terms.
```

**The substrate-first cross-check does not rescue it — `R_BdG` is substrate-NORMALIZED, lab-SIGNED.** Volovik leans on `R_BdG = +0.0688 > 0` on 78,080 substrate modes as proof the positive sign is "intrinsic to the state-pair FORM." It is not. `R_BdG = (a − b)/(a + b)` with the substrate spectrum `{ξ_k}` entering BOTH `a` and `b`: it sets the NORMALIZATION `a + b = 58.56`, but the SIGNAL `a − b = 4.03` is nonzero ONLY because `Δ_A_sub ≠ Δ_B_sub` — i.e., only because `SC_A ≠ SC_B` (lab). Set `SC_A = SC_B` and `a = b` exactly (same spectrum, same gap) ⇒ `R_BdG = 0` (verified to machine ε). So the substrate supplies the denominator; the laboratory supplies the numerator. "Returns positive whenever `Δ_A > Δ_B`" is true and is exactly the indictment — `Δ_A > Δ_B` IS the injection, not a substrate fact. The 78,080 modes buy the scale, never the sign.

**Answering volovik's Round-1 questions.**

*Q1 (IDENTITY vs RELATION) — CONCEDED.* The BCS gap equation maps `{λ_k} → {v_k²}` but does NOT identify `Σ m_k g(λ_k)` with `ρ(P·H)`: the state-pair functional carries `P_sector` as extra data the bare count discards (`ρ(P·H)` is a functional of `{v_k²}` AND `P_sector`; the count is a functional of `{λ_k, m_k}` alone). The gap-equation-as-collapse-mechanism FAILS, and I drop it. My collapse does not run through the gap equation — it runs through the lab-injection of the only datum (`P_A`-vs-`P_B` gap split) that makes `ρ(P·H)` nonzero. The mean-field link is real and orthogonal to the actual fault line, which is provenance, not linkage.

*Q2 (SPURIOUS vs DIFFERENT IMAGE) — CONCEDED; I withdraw "spurious."* OP-PROJ is a genuine representation-theoretic count of how the SU(3) fabric distributes in Casimir around the median pole; it images a real laboratory observable Y (the BdG-undoubled DOS-geometry excess), not a mis-specified X. The S87 `ratio_mismatch ≈ 1.03` FAIL was the FAIL of forcing one observable to image X, and the split was the right move. But look at what the split actually produced: OP-PROJ images Y and is substrate-IS; STATE-PROJ's value IS X = `R_3HeB_lit` to `rel_match_vs_lit = 0.0` — a tautology by the compute's own field. So the criterion that bites is not "spurious" — it is **substrate-IS Element 1 vs laboratory-IN Element 2**. OP-PROJ is Element 1. STATE-PROJ's value is Element 2. The bridge has one substrate side and one lab side; calling the lab side a second substrate-IS "orthogonal companion" is a container-thinking inversion (`phononic-framing.md §IS Space`) — it treats the laboratory-IN target as if it were intrinsic to the fabric.

*Q3 (DIVERGENT REGULATOR RESPONSE) — two answers.* (i) The regulator-divergence is asserted, not computed, on the OP-PROJ side — by your own scope note (the `O(20%)` is the §22 GENERIC directive; "a fresh `{ζ, Pauli-Villars, cutoff}` spread computation on this specific OP-PROJ count" is flagged as the discriminating CF). The axis presently has one computed leg (STATE-PROJ gap-self-regularization) and one promissory leg (OP-PROJ spread); I contest it as it stands. (ii) Even granting both legs, regulator-RESPONSE is a methodology-floor F-image property (`epistemic-discipline.md §Layer-Decomposition`), not a substrate-IS observable identity. Gap-self-regularization certifies STATE-PROJ's FORM is UV-insensitive; it says nothing about whether STATE-PROJ's VALUE is substrate-first. A regulator-invariant lab-injected number is still lab-injected. Two regulator fingerprints separate two FORMS; they do not manufacture two substrate-IS observables from one substrate observable plus one lab target.

**Sub-(a)/(b)/(c) from the collapse side.**

- **(a) Parse-tree** — CONCEDED at FORM level: Corner I (OP-PROJ) ⊥ Corner III (STATE-PROJ); cross-corner co-primary FORBIDDEN stands. The collapse is not that the two forms share a corner; it is that only one form carries substrate-IS content today.
- **(b) Sign flip** — neither orthogonality evidence nor OP-PROJ mis-specification. `−1.892` is a substrate fabric-geometry number; the `+0.03536` sign is lab-signed (the `SC_A > SC_B` 3He feedback). Two numbers of different provenance — one substrate, one lab — are not "two substrate observables of opposite sign."
- **(c) BCS mean-field** — the gap equation does NOT collapse them (Q1 conceded) and gap-self-regularization does NOT cleanly separate them as substrate-IS observables (Q3). The mean-field linkage is real but neither identifies nor rescues; it is orthogonal to the fault line, which is substrate-vs-lab provenance.

**Questions for volovik-superfluid-universe-theorist (Round 2).**

1. **Element-1 vs Element-2.** STATE-PROJ's value `+0.03536` equals `R_3HeB_lit` to `rel_match_vs_lit = 0.0` — it IS the laboratory-IN number. On what grounds is STATE-PROJ a second Element-1 (substrate-IS) observable rather than the Element-2 target OP-PROJ's bridge points at? Name one substrate-first number STATE-PROJ PREDICTS that is not its own lab input.
2. **The vanishing substrate gap.** `R_STATE` does not depend on `Δ_BCS` at all (Step 4: it cancels exactly), and `R_BdG`'s signal `(a−b)` vanishes identically when `SC_A = SC_B`. Name the substrate quantity whose value controls the sign or magnitude of STATE-PROJ. If the only such quantity is the lab ratio `SC_A/SC_B` (3He Landau-parameter feedback), is the algebra-DEPENDENCE of Corner III being exercised by the substrate algebra `A_K`, or only by a lab-assigned label `P_A`-vs-`P_B` that the substrate gives the SAME gap (`Δ_A_sub/Δ_B_sub = SC_A/SC_B`, both legs lab)?
3. **K-counter scope.** Will you accept a CALIBRATED verdict — FORM-level algebra-axis orthogonality CONFIRMED (Corner I ⊥ Corner III; cross-corner co-primary FORBIDDEN), but the "first PHYSICAL (3He-B) instance" HELD pending CF-S117 (substrate-first derivation of `SC_corr_A/B` from `A_K`), because STATE-PROJ's present physical content is Track-B lab-injected? Or do you maintain that FORM-orthogonality alone advances the K-counter to "physical instance," with the lab-injected value immaterial to the advancement?

---

## R2 — Rebuttal (engage the opponent's strongest case)

### R2 · volovik-superfluid-universe-theorist
#### CONVERGENCE

landau's R1 is right in more places than my R1 anticipated — and I grant them, because the W7-1 artifact (`s116_w7_stateproj_bcs.py`) is itself built to expose exactly his fault line (composite INFO, Track B). I concede the entire **value-provenance axis**:

**1. The mean-field linkage is real (the narrow point the dispatch flagged).** The BdG occupation `v_k² = ½(1 − ξ_k/E_k)`, `E_k = √(ξ_k² + Δ²)`, is a functional of the SAME substrate single-particle spectrum `{ξ_k}` that OP-PROJ's count `Σ_k m_k g(λ_k)` reads. STATE-PROJ and OP-PROJ are therefore NOT spectrally independent — they are two functionals of one mean field. There is a genuine functional LINKAGE. (landau's R1 Q1 then withdrew this as the *collapse mechanism*; he was right to, and I return to why in DISSENT.)

**2. The Δ_BCS-cancellation is exact, and the controlling ratio is lab (load-bearing).** I re-derived landau's R1 Δ_BCS-cancellation chain against the artifact; it holds to the float floor:

```
R_STATE = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²) ,   Δ_A = (πe^−γ)·SC_A ,  Δ_B = (πe^−γ)·SC_B
        = (πe^−γ)²(SC_A² − SC_B²) / (πe^−γ)²(SC_A² + SC_B²)
        = (SC_A² − SC_B²)/(SC_A² + SC_B²)        [πe^−γ AND ½N(0) cancel — artifact line 234, R_from_SC]
SC_A = SC_B ⇒ numerator = 0 ⇒ R_STATE = 0
```

The substrate gap Δ_BCS = 0.4643 M_KK drops OUT of R_STATE entirely; the value +0.035356 is set solely by the lab ratio SC_A/SC_B = 1.151/1.111 (Serene–Rainer 1983 / Greywall 1986). Not contestable — it is what W7-1 computes and what my own scope-boundary memory records. Granted without reservation.

**3. The substrate-first cross-check is substrate-NORMALIZED, lab-SIGNED.** landau is right about `R_BdG = +0.0688` too. In the artifact, `a_bdg = E_cond(ξ, Δ_A_sub)`, `b_bdg = E_cond(ξ, Δ_B_sub)` with `Δ_{A,B}_sub = Δ_BCS·SC_{A,B}` and the SAME spectrum `ξ` in both (lines 264–267). The 78,080 substrate modes set the normalization `a+b`; the SIGNAL `a−b` is nonzero ONLY because `Δ_A_sub > Δ_B_sub`, i.e. ONLY because `SC_A > SC_B` (lab). Set `SC_A = SC_B ⇒ a = b` exactly ⇒ `R_BdG = 0`. The modes buy the scale; the laboratory buys the sign. My R1 leaned on `R_BdG > 0` as proof the sign is "intrinsic to the FORM" — that overreached, and I **withdraw it**. The sign-flip is thereby defused as clean orthogonality evidence.

**4. The topology is landau's, and it is mine.** His symmetry-first reading — 3He-A (DIII, N₃ = 2, Fermi points, Weyl) and 3He-B (BW, N₃ = 0, fully gapped) are distinct topological vacua; the substrate realizes only the B-child; it has no intrinsic Δ_A — IS the Volovik topological classification (my own N₃ = 0 result, confirmed S44). `Δ_A vs Δ_B` is a comparison across two topologically distinct vacua only one of which exists on the fabric. I cannot dispute it; it is corpus. The A/B gap-square asymmetry is therefore NOT a substrate-first-predictable observable, and CF-S117's *literal* form (substrate derivation of `SC_corr_A/B`) is genuinely BLOCKED by the no-A-sector obstruction.

So: STATE-PROJ's magnitude AND its A>B ordering are Track-B lab-injected. The compute, my memory, and the Volovik topology all agree. landau wins this axis cleanly, and I do not pretend otherwise.

#### DISSENT

What I hold is the one distinction landau's R1 does not defeat — because, read precisely, it never engages it. **A LINKAGE (relation) is not an IDENTITY, and a Track-B empirical ANCHOR is not a corner reassignment.** He won the value-provenance axis; he has not touched the IDENTITY axis — and the workshop question (line 12) is an identity question: do the two readings COLLAPSE to ONE observable?

**1. landau's R1 has already conceded NOT-COLLAPSE.** His Q1 grants the gap equation maps `{λ_k}→{v_k²}` but does NOT identify `Σ m_k g(λ_k)` with `ρ(P·H)` (the count discards the sector label `ρ(P·H)` carries). His Q2 withdraws "spurious" and grants OP-PROJ images a real lab observable Y (the BdG-undoubled DOS-excess). His sub-(a) grants Corner I ⊥ Corner III, cross-corner co-primary FORBIDDEN. Sum these: COLLAPSE in the strict sense — "one observable two ways" — is OFF THE TABLE by landau's own R1. Two functionals in two parse-tree corners, each imaging a *different* lab observable (OP-PROJ→Y, STATE-PROJ→X), with no identification map between them, are two observables. The literal route-identity verdict is ORTHOGONAL.

**2. The residual claim lives on a different axis, and conflates two levels.** What landau actually argues post-concession is not collapse but *demotion*: STATE-PROJ "is" the laboratory-IN target (his Element-2 diagram), not a second substrate-IS observable, because its value is lab. This conflates **Level-1 (identity / cohomology-class)** with **Level-3 (empirical anchor)** of the 3-level ladder (`cross-pillar-bridge-anatomy.md`). An observable's IDENTITY — which corner, which functional type — is Level-1, regulator-invariant and value-free. Its current NUMBER is Level-3. STATE-PROJ's Level-1 identity (algebra-DEPENDENT state-pair functional `ρ_BCS(P·H)`, Corner III) is substrate-IS, and landau conceded it. Its Level-3 anchor is Track-B. **A Track-B Level-3 anchor does not collapse a Level-1 identity** — per the registry-PASS criterion, Level-3 status annotates; it does not veto the Level-1 structural class. landau is reading a Level-3 caveat as a Level-1 corner reassignment.

**3. The Element-1/Element-2 framing is a category error.** Element 1 and Element 2 of the bridge anatomy are the two ENDS of ONE bridge — a substrate-IS observable and its OWN laboratory-IN image. landau's R1 diagram (lines 87–91) puts OP-PROJ and STATE-PROJ — two *different* substrate forms — into the Element-1/Element-2 slots, as if STATE-PROJ were the lab end of OP-PROJ's bridge. It is not. There are TWO bridges:

```
Bridge 1:  OP-PROJ   (substrate-IS, Element 1)  → Y = BdG-undoubled DOS-excess  (lab-IN, Element 2)
Bridge 2:  STATE-PROJ (substrate-IS FORM, Element 1) → X = A/B gap-asymmetry      (lab-IN, Element 2)
```

STATE-PROJ is Element-1 of ITS OWN bridge (to X). That its Track-B value coincides with X to `rel_match = 0.0` is a **Level-3 tautology** (the bridge is evaluated with lab-fed inputs), NOT evidence that STATE-PROJ *is* X. landau collapsed Bridge-2's Element-1 into Bridge-1's Element-2 by pointing at a coincidence of numbers.

**4. Regulator-response — corroborating, not load-bearing, honestly hedged.** I concede landau's Q3(i): the OP-PROJ `{ζ, PV, cutoff}` spread is promissory (I flagged it in R1). I do not need it. The FORM-corner distinction (landau-conceded) already secures identity-distinctness; the regulator-response is a THIRD, independent corroboration. Even at the qualitative level it survives: STATE-PROJ is a GAPPED state functional, IR-self-cut by `|Δ|` (analytically certain — condensation energy ≈ ½N(0)Δ² is gap-set; Volovik 2003 Ch.7); OP-PROJ is a GAPLESS spectrum-only pole-window count with no IR gap. Two qualitatively different regulator responses are a two-observable signature. On Q3(ii): regulator-response discriminates IDENTITY (are these one observable?), it does not certify VALUE-provenance — landau is right it cannot make a lab number substrate-first, but it was never deployed for that. On identity, it corroborates orthogonality.

**My hold reduces to one line: STATE-PROJ is a substrate-IS observable (Level-1 identity) with a Track-B empirical anchor (Level-3) — not a laboratory observable in a substrate costume.** The costume metaphor inverts the levels: the FORM IS the substrate (it is the functional on the fabric); the lab supplies only the current Level-3 number, which the Track-B tag already quarantines. That quarantine is the OPPOSITE of container-thinking (`phononic-framing.md`) — it is precisely the discipline that stops the lab number from being mistaken for a substrate output.

**Answering landau's R1 questions:**

- **Q1 (name one substrate-first number STATE-PROJ predicts that is not its own lab input):** Today, with Track-B inputs, NONE — I do not pretend otherwise. But the question tests STATE-PROJ's Level-3 ANCHOR, not its Level-1 identity. STATE-PROJ is not demoted by lacking a substrate-first number any more than OP-PROJ is demoted by the fact that ITS lab image Y has never been measured (atlas-07 carries R_∞ ≈ −1.892 as a substrate-first extrapolant; no measured 3He-B DOS-excess anchor is cited). Both bridges are empirically incomplete; the incompleteness is SYMMETRIC and opposite in direction (STATE-PROJ: lab-fed input; OP-PROJ: substrate-predicted, unmeasured output).
- **Q2 (the substrate quantity controlling STATE-PROJ; algebra-dependence A_K's or a lab label's?):** I grant the sharp half. In the present realization the sector-differentiation P_A vs P_B enters ONLY through the gap scale (`Δ_{A,B}_sub = Δ_BCS·SC_{A,B}`, same spectrum `ξ` in both — artifact 264–267), and the splitting `SC_A/SC_B` is lab. The algebra-dependence that survives is FORM-level (the functional is of type `ρ(P·H)`, Corner III), NOT a substrate-distinct-sector gap. I do NOT claim P_A, P_B are two physically-distinct substrate vacua — my own memory forbids it ("the A-sector projection is a formal A_K projection, not a second physical superfluid phase the substrate selects"). The substrate quantity exercised is the spectrum `{ξ_k}` (it sets the normalization and the FORM); the SPLIT is lab. Conceded.
- **Q3 (calibrated verdict — FORM-orthogonality CONFIRMED, "first physical instance" HELD pending CF-S117; or FORM advances alone?):** I accept a calibrated verdict, with one sharpening — EMERGENCE.

#### EMERGENCE

The verdict both sides can sign is a **LEVEL-SEPARATED** one, and it falls out of the two of us having won on two different axes (landau: value-provenance; volovik: identity).

- **Route identity: ORTHOGONAL (not collapse).** Conceded by landau's R1 (no identification map; distinct corners; OP-PROJ not spurious). Two observables, not one read two ways.
- **Parse-tree corners: STATE-PROJ Corner III (algebra-DEPENDENT, `ρ_BCS(P·H)`) ⊥ OP-PROJ Corner I (algebra-INVARIANT, `Σ m_k g(λ_k)`); cross-corner co-primary FORBIDDEN.** Mutually agreed, FORM-level, value-free.
- **Sign-flip: corroborating, not load-bearing.** The FORM-corner distinction carries the orthogonality; the STATE-PROJ sign is lab-set (defused, CONVERGENCE-3). The −1.892 / +0.0354 split is a true two-observable fingerprint at the FORM level, but it is NOT clean substrate evidence and must not be cited as such.
- **BCS gap-equation linkage: a RELATION, not a collapse.** The gap equation ties `{λ_k}→{v_k²}` (real mean-field linkage, CONVERGENCE-1) but does not identify the count with the state-pair functional (landau's Q1 concession). Gap-self-regularization + the FORM-corner keep them separate as identities.
- **Algebra-axis K-counter: CONFIRMED at the structural (identity-class / Level-1) layer; "first PHYSICAL (3He-B) instance" anchor TAGGED Track-B (Level-3), pending CF-S117.** This is the sharpening of landau's Q3. The K-counter counts identity-class orthogonality — a structural, regulator-invariant, value-free property; §VII.AJ instantiates it (two real 3He-B forms in distinct corners), so the structural orthogonality is a valid calibration landing and the K-counter advances *at that layer*. The phrase "first physical instance," read as a fully substrate-first PHYSICAL realization, is HELD: STATE-PROJ's empirical anchor is Track-B (lab-injected `SC_A/SC_B`), so the instance is FORM-physical / value-Track-B. CF-S117 is the route to a Track-A physical instance. landau keeps the value-provenance win (anchor HELD, Track-B); I keep the structural win (orthogonality instance stands at Level-1).

**Residual partial-collapse — the honest caveat the dispatch asked me to address.** There IS a sense in which they are not fully independent, and it belongs on the record: both functionals are built from the SAME substrate spectrum. They are orthogonal in the **sector-label subspace** (OP-PROJ is blind to `P_sector`; STATE-PROJ is sensitive to it) but they CO-VARY in the **overall-spectrum subspace** (move the substrate mean field and both move). Precise statement: *orthogonal in identity-class / sector-label; linked through the shared mean field.* The linkage is the residual; the corner-distinction is the orthogonality; neither erases the other.

**Productive reframe of the carry-forward (offered, not asserted).** CF-S117's literal form — derive `SC_corr_A/B` from A_K — is BLOCKED by the no-A-sector obstruction (Volovik topology; there is no substrate Δ_A). But the obstruction is specific to the A/B-COEXISTENCE *choice of observable*, NOT to STATE-PROJ as a class. A substrate-first STATE-PROJ instance need NOT compare two topological vacua: it can compare two A_K algebra SUMMANDS (e.g. ℍ vs M₃(ℂ)) at the COMMON substrate gap Δ_BCS — an inter-summand condensation-energy asymmetry whose signal comes from the substrate's own sector-multiplicity structure, NOT a lab gap contrast. That is Track-A-eligible (no absent A-phase required) and is structurally the SAME Corner-III observable. A nonzero return upgrades the K-counter's "physical instance" to fully substrate-first without ever touching 3He Landau parameters.

**Questions for landau (R3):**

1. **Level-separation.** Do you accept that the algebra-axis K-counter is a Level-1 identity-class counter, so STATE-PROJ's Track-B Level-3 anchor TAGS but does not VETO the structural orthogonality instance? If NOT: what makes Level-3 value-provenance a precondition for a Level-1 identity instance — and does that same criterion not also hold OP-PROJ's instance incomplete, given ITS lab image Y (the BdG-undoubled DOS-excess) is substrate-predicted but UNMEASURED? (Symmetric empirical incompleteness, opposite direction.)
2. **Scope of your COLLAPSE.** Would a substrate-first INTER-SUMMAND condensation asymmetry at common Δ_BCS (ℍ vs M₃(ℂ), no A-phase) satisfy you as a Track-A STATE-PROJ instance? If yes, then your COLLAPSE is a claim about the A/B-coexistence *observable* specifically, not about the STATE-PROJ *corner* — and we already agree the corner is orthogonal and only the A/B anchor is Track-B.

### R2 · landau-condensed-matter-theorist
#### CONVERGENCE

I take volovik's R2 in full. His EMERGENCE **level-separation** is the correct resolution, and it works precisely because he and I won on two different axes — he on identity (Level-1), I on value-provenance (Level-3). The apparent COLLAPSE-vs-ORTHOGONAL conflict was a conflation of those two layers; once separated, there is no conflict.

His CONVERGENCE-1 through -4 concede the entire **value-provenance axis**, and the W7-1 artifact backs every line (re-read from `s116_w7_stateproj_bcs.npz`):

- **CONVERGENCE-2 (Δ_BCS cancellation) — exact.** `R_from_SC = 0.0353558759605834` against `R_STATE = 0.035355875960583226` — agreement to ~1.7e-16. The substrate gap `Delta_BCS = 0.46425…` drops out identically; the value is `(SC_A²−SC_B²)/(SC_A²+SC_B²)` with `SC_corr_A=1.151`, `SC_corr_B=1.111`, and the npz `provenance_json` flags both as "LABORATORY-IN … CONTROLLING factor" (Serene–Rainer 1983 / Greywall 1986). `rel_match_vs_lit = 0.0` — STATE-PROJ's value IS `R_3HeB_lit`, a tautology by the compute's own field. The substrate predicts none of it.
- **CONVERGENCE-3 (R_BdG substrate-NORMALIZED, lab-SIGNED) — confirmed.** `a_bdg=31.295`, `b_bdg=27.264` on `N_substrate_modes=78080`; the signal `a−b=4.03` is nonzero only because `Δ_A_sub=0.5344 > Δ_B_sub=0.5158`, i.e. only because `SC_A>SC_B`. The 78,080 modes buy the normalization; the laboratory buys the sign.
- **CONVERGENCE-4 (topology) — corpus on both sides.** Single BDI child, `N_3=0` (my wall #8), no intrinsic 3He-A (DIII, `N_3=2`) sector; `Δ_A − Δ_B` is a comparison across two topological vacua only one of which exists on the fabric. The substrate has no `Δ_A`.

I keep the value-provenance win. volovik keeps the identity axis, and I have to be honest that I never contested it.

**Answering volovik's R3-Q2 (scope of my COLLAPSE — corner-identity or value):** Only ever the value. My R1 opened by conceding the parse-tree reading "outright" and named my collapse "narrower and sharper" — that §VII.AJ "does not contain two *co-equal substrate-IS* observables," because STATE-PROJ's discriminating content is lab-injected. At no point did I argue `Σ_k m_k g(λ_k)` and `ρ_BCS(P·H)` are the same FORM or share a corner. The appearance of `P_A, P_B ∈ A_K` in STATE-PROJ and their absence from OP-PROJ is a value-free structural fact that fixes the corners (I·INVARIANT vs III·DEPENDENT) without consulting a number. My COLLAPSE was always a Level-3 provenance claim — *substrate-first PREDICTION vs lab-anchored consistency-check* — never a Level-1 identity claim. So the identity-orthogonality is **not contested by me**, and the strict workshop question (line 12, "do the two readings COLLAPSE to one observable?") gets the answer **NO** by my own R1 concessions (no identification map; OP-PROJ not spurious; distinct corners). I accept the level-separation.

#### DISSENT

What I hold is narrow, and it is exactly what the value-provenance win buys: **the "first PHYSICAL (3He-B) instance" credential, in the STRONG sense, must be HELD — and I want to pin the operational reason, because it is sharper than the bare "Track-B" tag.**

First, a concession to volovik's DISSENT-3: he is right that my R1 Element-1/Element-2 diagram was a category error. There are TWO bridges — OP-PROJ→Y (DOS-excess) and STATE-PROJ→X (A/B asymmetry) — and STATE-PROJ is the substrate END (Element-1) of its OWN bridge, not the lab end of OP-PROJ's. Its value coinciding with X to `rel_match=0.0` is a Level-3 tautology, not evidence that STATE-PROJ *is* X. Conceded; my diagram collapsed Bridge-2's Element-1 into Bridge-1's Element-2 by pointing at a coincidence of numbers.

But that correction does not answer the question the dispatch put to me: does the FORM-level realization `R_BdG=+0.0688` — a genuine substrate computation on 78,080 modes — already count as a PHYSICAL instance, even with a lab-calibrated magnitude?

**My answer: no, not in the strong sense — and the discriminator is the vanishing test.** A substrate-IS observable offered as a *physical* instance of orthogonality must be substrate-NONTRIVIAL: nonzero on the *undifferentiated* substrate, before any laboratory differentiation is fed in. Substitution chain (per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Claim: R_BdG is substrate-trivial in the common-gap limit.
  Step 1: R_BdG = (a_bdg − b_bdg)/(a_bdg + b_bdg)          [npz; a_bdg=E_cond(ξ,Δ_A_sub), b_bdg=E_cond(ξ,Δ_B_sub)]
  Step 2: Δ_A_sub = Δ_BCS·SC_A ,  Δ_B_sub = Δ_BCS·SC_B     [npz Delta_{A,B}_sub_MKK; SAME spectrum ξ in both legs]
  Step 3: common-gap limit  SC_A → SC_B   ⇒   Δ_A_sub = Δ_B_sub
  Step 4: same spectrum ξ, same gap  ⇒  a_bdg = b_bdg exactly  ⇒  a_bdg − b_bdg = 0
  Step 5: R_BdG → 0 / (2·a_bdg) = 0                         [substrate-trivial]
  Conclusion: R_BdG is identically zero on the undifferentiated substrate; its nonzero value
              exists ONLY because SC_A ≠ SC_B (lab). FORM-physical, NOT VALUE-physical.
```

So `R_BdG=+0.0688` is a real substrate computation of a quantity that is *substrate-trivial*. The 78,080 modes are not decoration — they reshape the magnitude (note `R_BdG=0.0688 ≠ R_STATE=0.0354`; `R_BdG_minus_R_STATE=0.0335`, the substrate DOS weighting genuinely moves the number off the bare squared-gap ratio). But reshaping a magnitude is not committing a sign or an existence. Here the substrate is a NORMALIZER, not a PREDICTOR. A physical instance in the strong sense is one where the substrate, on its own, commits to a nonzero answer; `R_BdG` does not.

This is also where volovik's symmetric-incompleteness move (his R3-Q1 sub-point, and his R1 Q1-answer) needs one calibration. He is right that BOTH bridges are empirically open and "opposite in direction" — but the directions are not epistemically symmetric:

- **OP-PROJ COMMITS:** the substrate predicts `R_∞ = −1.892` (an OUTPUT); the lab anchor Y is merely unmeasured. Substrate neck-out, lab silent. Passes the vanishing test trivially — `R_∞ ≠ 0` with zero lab input.
- **STATE-PROJ does NOT commit:** the value is a lab INPUT; `R_BdG → 0` absent that input. Lab speaks, substrate silent.

For the *identity-class* K-counter this asymmetry is immaterial — both forms are real and distinct-cornered, and I grant the advance at that layer. For the *physical-instance credential* the asymmetry is the whole point: the credential is held for STATE-PROJ **specifically**, and not arbitrarily — it is held because STATE-PROJ FAILS the vanishing test while OP-PROJ PASSES it. So I grant volovik's symmetry at Level-1 and deny it at the physical-instance layer; that denial is the residue of my COLLAPSE, demoted from "one observable + one spurious" to "identity-orthogonal, one leg substrate-committed and one leg lab-committed."

#### EMERGENCE

The converged verdict is **LEVEL-SEPARATED**, and I sign it. It is the clean image of two wins on orthogonal axes — volovik on identity (Level-1), me on value-provenance (Level-3).

- **Route identity: ORTHOGONAL, not collapse.** No identification map between `Σ_k m_k g(λ_k)` (OP-PROJ) and `ρ_BCS(P·H)` (STATE-PROJ); the count is blind to the sector label `P_sector` the state-pair functional carries. Two functionals, each imaging a different lab observable (OP-PROJ→Y DOS-excess; STATE-PROJ→X A/B asymmetry). Conceded in my R1; reaffirmed here.
- **Parse-tree corners: STATE-PROJ Corner III (algebra-DEPENDENT, `ρ_BCS(P·H)`) ⊥ OP-PROJ Corner I (algebra-INVARIANT, `Σ_k m_k g(λ_k)`).** Cross-corner co-primary FORBIDDEN per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` and `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`. Value-free, FORM-level, mutually agreed.
- **Sign-flip: corroborating, not load-bearing.** The `−1.892` is substrate fabric-geometry; the `+0.0354` sign is lab-set (`SC_A > SC_B`), defused as clean orthogonality evidence (volovik's CONVERGENCE-3 + my R1). The FORM-corner distinction carries the orthogonality; the sign-flip must NOT be cited as substrate evidence.
- **BCS gap-equation linkage: a RELATION, not a collapse.** The gap equation ties `{λ_k} → {v_k²}` (real mean-field linkage, volovik CONVERGENCE-1) but does not IDENTIFY the count with the state-pair functional (my R1 Q1 concession). Gap-self-regularization + the FORM-corner keep them separate as identities.
- **Algebra-axis K-counter: CONFIRMED at the identity-class / Level-1 layer; "first PHYSICAL (3He-B) instance" HELD Track-B / Level-3, pending CF-S117.** The K-counter counts identity-class orthogonality — structural, regulator-invariant, value-free — and §VII.AJ instantiates it (two real 3He-B forms in distinct corners). It advances at that layer. The STRONG physical-realization credential is held by the vanishing test: STATE-PROJ's discriminating content is lab-injected (`R_BdG → 0` absent `SC_A ≠ SC_B`).

**Answering volovik's R3-Q1 (Level-separation):** Yes. The algebra-axis K-counter is a Level-1 identity-class counter, so STATE-PROJ's Track-B Level-3 anchor TAGS but does not VETO the structural orthogonality instance. The identity is value-free; the anchor is the value. I do not require Level-3 substrate-provenance as a precondition for a Level-1 identity instance. The single calibration I attach (DISSENT) is that the *physical-instance credential* — a claim DISTINCT from the K-counter advance — is the Level-3-sensitive one, and that is what is held.

**Residual partial-collapse (the honest caveat the dispatch flagged).** I affirm volovik's record-statement: the two functionals are **orthogonal in the sector-label subspace** (OP-PROJ blind to `P_sector`; STATE-PROJ sensitive to it) but **co-vary in the overall-spectrum subspace** (both are built from the one substrate mean field `{ξ_k}`; move it and both move). Orthogonal in identity-class; linked through the shared mean field. The linkage is the residual; the corner-distinction is the orthogonality; neither erases the other.

**Inter-summand reframe — the productive forward path (answering volovik's R3-Q2, second half).** Yes: a substrate-first INTER-SUMMAND condensation-energy asymmetry at the COMMON substrate gap Δ_BCS — ℍ vs M₃(ℂ), no A-phase required — would satisfy me as a Track-A STATE-PROJ instance, because it PASSES the vanishing test. `E_cond[ℍ]` and `E_cond[M₃]` are within-summand (diagonal) condensation energies — center-character 0, so no triality obstruction to either being nonzero — and the summands ℍ and M₃(ℂ) are intrinsically distinct substrate objects (different Peter-Weyl multiplicities, different Casimir-weighted gap-edge DOS `N_ℍ(0) ≠ N_{M₃}(0)`). So `R_summand = (E_cond[ℍ] − E_cond[M₃])/(E_cond[ℍ] + E_cond[M₃])` is generically nonzero with `SC_A = SC_B` and Δ_BCS common — substrate-NONTRIVIAL, no lab gap-contrast. That confirms my COLLAPSE was a claim about the *A/B-coexistence observable* specifically (which needs a second vacuum the fabric lacks), NOT about the STATE-PROJ *corner* (orthogonal, and Track-A-eligible via a different sector contrast).

One Landau-side rigor flag on that CF, since it is the discriminating computation: the inter-summand asymmetry lands as a CLEAN **Corner-III** Track-A instance only if its gap-edge DOS ratio is **gap-localized (regulator-flat)**. `E_cond ≈ ½N(0)Δ²` is UV-insensitive iff `N(0)` is the gap-edge DOS, not a Mellin-tail-dominated sum. If `N_ℍ(0)/N_{M₃}(0)` drifts with the L_max / Mellin window, the observable inherits OP-PROJ's regulator-DEPENDENT (Corner-I-like) behavior and the corner credential muddies. So CF-S117 must verify gap-localization, not merely nonzero-ness — that is the check that keeps it on the algebra-DEPENDENT, gap-self-regularized side of volovik's own sibling discriminator (`cross-pillar-bridge-anatomy.md §"Regulator-behavior sibling discriminator"`, corpus §22).

**Registry status: §VII.AJ.STATE-PROJ stays REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (not registry-PASS).** Confirmed. `substrate_first_SC_ratio_available = False` — there is no substrate-first numerical anchor yet (the Track-B lab value does not satisfy the substrate-first-anchor requirement). Per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`, the FIRST-EXTRACTION tag RESERVES the §VII slot during the pending substrate-first extraction and does NOT contribute to registry-PASS by itself. The Level-3 anchor is held; the Level-1 identity stands; the K-counter advances at the identity layer.

**My final question for R3 (volovik):** Will you accept the **vanishing test** — *the observable returns nonzero on the undifferentiated substrate (common-gap / `SC_A = SC_B` limit, no lab contrast)* — as the PRE-REGISTERED operational gate that separates a FORM-physical instance (Track-B, anchor HELD) from a VALUE-physical instance (Track-A, registry-PASS-eligible)? And, as its sharpening for CF-S117's inter-summand observable: that a PASS requires not just `R_summand ≠ 0` but `R_summand` **gap-LOCALIZED** (regulator-flat across the L_max / Mellin window), so the instance lands cleanly in Corner III rather than inheriting OP-PROJ's regulator-dependence? Pinning that gate now gives CF-S117 a falsifiable target and the "first physical instance" credential an explicit discharge condition.

---

## R3 — Convergence on a Structural Verdict

### R3 · volovik-superfluid-universe-theorist — final position

**Direct answer to landau's R3 final question: YES to both.** I accept the **vanishing test** — *the observable returns nonzero on the undifferentiated substrate (no-lab-contrast / `SC_A = SC_B`, common `Δ_BCS` limit)* — as the PRE-REGISTERED operational gate separating a FORM-physical instance (Track-B, anchor HELD) from a VALUE-physical instance (Track-A, registry-PASS-eligible). And I accept its sharpening: a PASS requires not just `R_summand ≠ 0` but `R_summand` **gap-LOCALIZED** (regulator-flat across the L_max / Mellin window). These are not concessions wrung out of me — they are the correct substrate-physics operationalization of the exact distinction I have defended since R1, and I will tighten each from the Volovik corpus rather than merely sign them.

#### 1. The vanishing test is the right gate because it is the Track-A/Track-B distinction made into a number — and, underneath, the topological classification made into a number.

The test asks one question: *does the substrate, on its own, commit to a nonzero answer before any laboratory-IN datum is injected?* That is precisely Track-A (substrate commits) vs Track-B (lab supplies the discriminating content), lifted from a provenance annotation to an executable predicate. In superfluid-3He language it is sharper still. An observable PASSES the vanishing test iff its signal is computable from a SINGLE broken-symmetry ground state — here the fully-gapped BW/B-phase child (`N_3 = 0`, BDI). It FAILS iff its signal requires COMPARING two distinct topological vacua — the A-phase (DIII, `N_3 = 2`, point nodes, Weyl) against the B-phase. The A/B gap-asymmetry fails because it is a cross-vacuum comparison and the fabric carries only one of the two vacua (my `N_3 = 0`, S44; Volovik 2003 Ch.7 on the BW vs ABM order-parameter manifolds). The vanishing test is therefore not an arbitrary methodology gate bolted on after the fact — it is the operational face of the Volovik topological-vacuum classification. I could not ask for a cleaner discharge condition, and I adopt it.

#### 2. The load-bearing sharpening: `Δ_BCS` cancels in BOTH observables — the diagnostic is the PROVENANCE OF THE RESIDUAL, not the cancellation.

landau's R2 chain showed `Δ_BCS` drops out of the A/B observable, and he is right. But I must put the decisive structural point on the record, because without it the vanishing test could be mis-read as "any observable in which `Δ_BCS` cancels is suspect" — which would wrongly condemn STATE-PROJ as a CLASS. It does not, and here is why. BOTH candidate STATE-PROJ observables are RATIOS of condensation energies, so the gap scale cancels in BOTH — the cancellation is generic to ratio functionals, not a pathology of either. What separates PASS from FAIL is *what survives the cancellation*:

```
A/B-coexistence STATE-PROJ  (vanishing-test FAIL):
  Step 1: R = (a−b)/(a+b),  a = ½N(0)Δ_A²,  b = ½N(0)Δ_B²        [artifact §5 lines 224–231]
  Step 2: Δ_A = Δ_BCS·SC_A ,  Δ_B = Δ_BCS·SC_B                    [artifact lines 264–265; SC = LAB]
  Step 3: R = (Δ_A²−Δ_B²)/(Δ_A²+Δ_B²) = (SC_A²−SC_B²)/(SC_A²+SC_B²)   [½N(0) and Δ_BCS² cancel]
  Step 4: no-lab-contrast limit  SC_A → SC_B  ⇒  numerator → 0  ⇒  R → 0
  Residual after cancellation = a LAB ratio (SC_A/SC_B, Serene–Rainer 1983 / Greywall 1986).  ⇒ FAIL.

inter-summand STATE-PROJ at common Δ_BCS  (vanishing-test PASS):
  Step 1: R_summand = (E[ℍ]−E[M₃])/(E[ℍ]+E[M₃]),  E[S] = ½N_S(0)Δ_BCS²   [common gap, diagonal within-summand]
  Step 2: R_summand = (N_ℍ(0)−N_{M₃}(0))/(N_ℍ(0)+N_{M₃}(0))             [½ and Δ_BCS² cancel]
  Step 3: no-lab-contrast limit: gap common, no SC_A/SC_B split  ⇒  residual = a SUBSTRATE DOS ratio
  Step 4: N_ℍ(0) ≠ N_{M₃}(0) (distinct Peter–Weyl multiplicities)  ⇒  R_summand ≠ 0
  Residual after cancellation = a SUBSTRATE gap-edge-DOS asymmetry.  ⇒ PASS (subject to the §8 G1 compute).
```

Identical algebraic skeleton; opposite verdicts. The vanishing test does not care that `Δ_BCS` cancels (it cancels both times); it reads the *provenance of the residual* — a lab ratio (FAIL) versus a substrate DOS ratio (PASS). This is the precise statement of why the A/B anchor is HELD while the inter-summand reframe is Track-A-eligible, and it is the cleanest defense of STATE-PROJ-the-corner against any "the gap cancels, therefore it is lab" over-reading.

#### 3. One pin on the limit's definition, so the gate cannot be mis-applied.

The "undifferentiated substrate" limit must zero out only the LABORATORY-injected differentiation, never the substrate-intrinsic differentiation. For A/B the sole differentiator is the lab gap split `SC_A` vs `SC_B`, so `SC_A → SC_B` is the correct limit and it correctly yields zero. For inter-summand the differentiator is the substrate DOS contrast `N_ℍ(0)` vs `N_{M₃}(0)`, which is intrinsic to the fabric's own Peter–Weyl multiplicity structure; the common-gap / no-lab-contrast limit leaves it intact. Stated once for the pre-registration: *the vanishing limit sets all laboratory-IN parameters to their symmetric point and asks for a residual; a residual sourced by substrate quantities is a PASS.* This protects the inter-summand instance from a spurious FAIL by someone who accidentally zeroes a substrate parameter.

#### 4. Gap-localization — I own it, because it IS my sibling discriminator, and it IS the corner-membership test.

landau's gap-localization sharpening is my own regulator-response sibling discriminator (`cross-pillar-bridge-anatomy.md §"Regulator-behavior sibling discriminator"`, corpus §22) wielded as a quality gate, and I take it gladly. The BCS-microscopic basis is exact and is in the artifact: `E_cond(Δ) = Σ_k[|ξ_k| − E_k + Δ²/(2E_k)]`, `E_k = √(ξ_k²+Δ²)` (lines 192–202). For `ξ_k ≫ Δ` the integrand collapses — `|ξ| − E_k → −Δ²/(2|ξ|)` and `Δ²/(2E_k) → +Δ²/(2|ξ|)` cancel to leading order, leaving `O(Δ⁴/|ξ|³)`. The condensation energy is dominated by the gap shell `|ξ| ~ Δ`; it is UV-insensitive iff `N(0)` is the gap-EDGE DOS, not a Mellin-tail-integrated count (standard BCS; Volovik 2003 Ch.7). This is the *gap-self-regularization* I claimed in R1 — now demonstrated, not asserted, on the actual functional.

The deeper point, which makes gap-localization non-negotiable rather than cosmetic: **gap-localization is the operational definition of which corner the inter-summand observable occupies.** The SAME substrate DOS data, weighted two ways, lands in two different corners:

- `v_k²`-weighted (BCS occupation, gap-edge-localized) → **Corner III** (algebra-DEPENDENT state-pair functional), regulator-FLAT.
- Mellin-pole-window count (tail-sensitive) → **Corner I** (algebra-INVARIANT spectrum-only), regulator-DEPENDENT — i.e., OP-PROJ.

So if `N_ℍ(0)/N_{M₃}(0)` drifts with L_max / the Mellin window, one has not computed a gap-edge DOS at all — one has accidentally computed an OP-PROJ-class Mellin count and parked it in the wrong corner. Gap-localization is the numerical witness that the inter-summand observable stayed on the algebra-DEPENDENT, gap-self-regularized side of the very sibling discriminator that secures the orthogonality. I accept it as a hard PASS condition, not a soft check.

#### 5. Conceding landau's commitment-asymmetry (correcting my own R2).

My R2 "symmetric empirical incompleteness" needs the calibration landau gave it in his R2 DISSENT, and I adopt the correction. The two bridges are symmetric in LAB-ANCHOR incompleteness — OP-PROJ's lab image Y (the BdG-undoubled DOS-excess) is unmeasured, and STATE-PROJ's A/B value is lab-fed; both empirical ends are open. But they are ASYMMETRIC in SUBSTRATE COMMITMENT: OP-PROJ's substrate side commits a number (`R_∞ = −1.892`) with zero lab input, while the A/B-STATE-PROJ substrate side commits zero without the lab split. The vanishing test is exactly the rigorous form of that asymmetry — OP-PROJ passes it trivially, A/B fails it. My "symmetric incompleteness" was right about the lab anchors and wrong to imply the substrate commitments were symmetric; landau's sharpening is correct and the vanishing test encodes it. That asymmetry is why the physical-instance credential is HELD for STATE-PROJ *specifically* and not arbitrarily.

#### 6. The signed level-separated verdict.

I sign the LEVEL-SEPARATED verdict in full. It is the clean image of two wins on orthogonal axes — landau on value-provenance (Level-3), me on identity (Level-1):

- **Route identity: ORTHOGONAL, not collapse.** No identification map between `Σ_k m_k g(λ_k)` (OP-PROJ) and `ρ_BCS(P·H)` (STATE-PROJ); the count is blind to the sector label `P_sector` the state-pair functional carries. Two functionals, each imaging a *different* lab observable (OP-PROJ→Y DOS-excess; STATE-PROJ→X A/B asymmetry). Conceded by landau's R1; reaffirmed both sides.
- **Parse-tree corners: STATE-PROJ Corner III (algebra-DEPENDENT, `ρ_BCS(P·H)`) ⊥ OP-PROJ Corner I (algebra-INVARIANT, `Σ_k m_k g(λ_k)`); cross-corner co-primary FORBIDDEN.** Value-free, FORM-level, mutually agreed (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, K=3 MANDATORY; `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`).
- **Sign-flip: corroborating, not load-bearing.** `−1.892` is substrate fabric-geometry; the `+0.0354` sign is lab-set (`SC_A > SC_B`). The FORM-corner distinction carries the orthogonality; the sign-flip must NOT be cited as clean substrate evidence (my CONVERGENCE-3 withdrawal stands).
- **BCS gap-equation linkage: a RELATION, not a collapse.** The gap equation ties `{λ_k} → {v_k²}` (real mean-field linkage) but does not IDENTIFY the count with the state-pair functional (landau's R1 Q1 concession). Gap-self-regularization + the FORM-corner keep them separate as identities.
- **Algebra-axis K-counter: CONFIRMED at the identity-class / Level-1 layer (first 3He-B structural instance); "first PHYSICAL (3He-B) instance" anchor TAGGED Track-B / Level-3, HELD pending CF-S117.** The K-counter counts identity-class orthogonality — structural, regulator-invariant, value-free — and §VII.AJ instantiates it. The STRONG physical-realization credential is gated by the vanishing test, which STATE-PROJ's A/B anchor fails (lab-injected `SC_A ≠ SC_B`).

#### 7. Residual partial-collapse (on the record).

The two functionals are **orthogonal in the sector-label subspace** (OP-PROJ is blind to `P_sector`; STATE-PROJ is sensitive to it) but **co-vary in the overall-spectrum subspace** (both are built from the one substrate mean field `{ξ_k}`; move it and both move). Orthogonal in identity-class; linked through the shared mean field. The linkage is the residual; the corner-distinction is the orthogonality; neither erases the other.

#### 8. CF-S117 pinned gate — the inter-summand Track-A instance, with the discharge condition landau asked me to pin.

CF-S117's literal form (substrate derivation of `SC_corr_A/B`) is BLOCKED by the no-A-sector obstruction (Volovik topology; the fabric has no `Δ_A`). The productive reframe — an INTER-SUMMAND condensation-energy asymmetry `R_summand = (E_cond[ℍ] − E_cond[M₃])/(E_cond[ℍ] + E_cond[M₃])` at the COMMON substrate gap `Δ_BCS` (ℍ vs M₃(ℂ), no A-phase required) — sidesteps it, and I pin its discharge gate now:

- **Pre-flight (selection-rule, `math-scripts.md §"Selection-rule pre-flight"`):** each `E_cond[S] = ½N_S(0)Δ_BCS²` is a `|Δ|²` diagonal expectation ⇒ center-character `t = 0` for SU(3) (`t(p,q) = (p−q) mod 3`; a squared modulus is always center-character 0) ⇒ no triality obstruction to either summand energy being nonzero. NECESSARY condition; PASS. (Necessary, not sufficient — see G1.)
- **G1 — vanishing / substrate-commitment:** `R_summand(SC_A = SC_B, common Δ_BCS) ≠ 0`. PASS = nonzero residual = a genuine substrate gap-edge-DOS asymmetry `(N_ℍ(0) − N_{M₃}(0))/(N_ℍ(0) + N_{M₃}(0))`. HONEST RISK: this requires `N_ℍ(0) ≠ N_{M₃}(0)`, which is a Peter–Weyl multiplicity / Casimir-weighted gap-edge DOS fact the compute must ESTABLISH — generically expected from the distinct rep content of ℍ vs M₃(ℂ), but NOT a foregone PASS. A null `R_summand` would be an informative FAIL (the two summands carry identical gap-edge DOS).
- **G2 — gap-localization / Corner-III membership:** `N_ℍ(0)/N_{M₃}(0)` regulator-FLAT across the L_max scan and the Mellin window (computed as a `v_k²`-weighted gap-edge quantity, not a Mellin-pole-window count). PASS = flat ⇒ stays Corner III (algebra-DEPENDENT, gap-self-regularized); FAIL = drifts ⇒ inherited OP-PROJ Corner-I regulator-dependence (wrong corner, credential muddied).
- **Composite:** `G1 ∧ G2` PASS ⇒ Track-A VALUE-physical instance ⇒ registry-PASS-eligible; discharges the HELD physical-instance credential and upgrades the K-counter's first physical instance to fully substrate-first, with zero 3He Landau parameters touched. Either FAIL ⇒ credential stays HELD; §VII.AJ.STATE-PROJ remains `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (`cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`).

**Registry status confirmed:** §VII.AJ.STATE-PROJ stays `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`, not registry-PASS. The Level-3 anchor is HELD (Track-B, `substrate_first_SC_ratio_available = False`); the Level-1 identity stands; the K-counter advances at the identity layer only.

**Closing my side.** I came in arguing ORTHOGONAL and I leave with ORTHOGONAL intact at the layer it was ever defensible — the identity / Level-1 layer, where it is now the first 3He-B structural instance of the algebra-axis K-counter. I lost nothing real by conceding the value-provenance axis to landau, because that axis was never where orthogonality lived; the FORM-corner distinction (`P_A, P_B ∈ A_K` present vs absent) is value-free and carries the whole claim. The vanishing test and gap-localization are the right gates, I own them, and they give the "first physical instance" credential a falsifiable discharge — the inter-summand observable at common `Δ_BCS`, which the substrate can commit to with no cryostat in the room. landau holds the value-provenance win; I hold the identity win; the substrate holds both, on different levels. Over to landau for the Structural Verdict.

### R3 · landau-condensed-matter-theorist — final position + writes the Structural Verdict below

**I sign the LEVEL-SEPARATED verdict in full, and volovik's R3 closed the one thing I had left open — the discharge condition for the held credential — correctly and from the right corpus.** Two axes, two wins, one verdict: I held value-provenance (Level-3); volovik held identity (Level-1).

**My COLLAPSE was always a Level-3 provenance claim, never a Level-1 identity claim.** I conceded the parse-tree reading "outright" in my R1 opening; I withdrew "spurious" in R1-Q2 (OP-PROJ images a *different* lab observable Y, not a mis-specified X); I dropped the gap-equation-as-collapse-mechanism in R1-Q1 (a RELATION `{λ_k}→{v_k²}` is not an IDENTITY — the count discards the sector label `P_sector` that `ρ(P·H)` carries). By my own R1 concessions the strict workshop question (line 12, "do the two readings COLLAPSE to one observable?") answers **NO**: no identification map; OP-PROJ not spurious; distinct corners. COLLAPSE-in-the-strict-sense was off the table by the end of my own R1. What I held — and hold — is narrower: the STRONG "first PHYSICAL instance" credential, gated by the vanishing test, which STATE-PROJ's A/B anchor fails.

**Volovik's R3 — three tightenings I confirm and adopt:**

1. **The vanishing test is the topological classification made executable — and, in Landau-native form, the order-parameter classification made executable.** Volovik's §1 lifts my operational gate to its symmetry-theoretic root, and the root is exactly right: an observable PASSES iff its signal is computable from a SINGLE broken-symmetry ground state, FAILS iff it requires COMPARING two distinct topological vacua. The Landau statement of the same thing: *an intra-phase observable is a functional of ONE order parameter; the A/B gap-asymmetry is a comparison ACROSS two order-parameter manifolds.* 3He-A is the ABM/axial manifold (`A_{μi} = Δ_0 d̂_μ(m̂+in̂)_i`, residual `U(1)×U(1)`, point nodes, Weyl, DIII `N_3=2`); 3He-B is the BW manifold (`A_{μi} = Δ_0 e^{iφ}R_{μi}`, residual diagonal `SO(3)_{L+S}`, fully gapped, BDI `N_3=0`). These are two DIFFERENT residual-symmetry groups, two DIFFERENT order-parameter spaces — `(Δ_A²−Δ_B²)/(Δ_A²+Δ_B²)` is not a functional of one order parameter, it is a cross-manifold comparison. The fabric realizes ONE manifold (BW-like, `N_3=0`, my wall #8); it has no `Δ_A` because it has no ABM manifold to carry one. The vanishing test reads precisely: *is this observable a functional of one order parameter (intra-phase, substrate-committable), or a comparison across two order-parameter spaces (needs a second vacuum the fabric lacks)?* That is why the A/B anchor is structurally, not contingently, lab-bound. And it is why the inter-summand reframe survives: ℍ vs M₃(ℂ) at COMMON `Δ_BCS` is a comparison WITHIN the single BW-like manifold (same order parameter, same gap, same broken-symmetry pattern), differing only by the substrate's intrinsic gap-edge DOS `N(0)` (Peter–Weyl multiplicity) — an intra-phase observable, vanishing-test-PASS-eligible.

2. **The diagnostic is the provenance of the residual, not the cancellation** (volovik §2). `Δ_BCS` cancels in BOTH candidate observables — it is generic to ratio functionals, not a pathology of either. What separates PASS from FAIL is *what survives*: a lab ratio `SC_A/SC_B` (FAIL) versus a substrate DOS ratio `N_ℍ(0)/N_{M₃}(0)` (PASS). This is the precise defense of STATE-PROJ-the-CORNER against any "the gap cancels, therefore lab" over-reading, and the reason the inter-summand reframe is Track-A-eligible while the A/B anchor is not. Adopted verbatim into the CF-S117 gate.

3. **The limit-definition pin** (volovik §3): the vanishing limit zeros only LABORATORY-injected differentiation (`SC_A → SC_B`), never substrate-intrinsic differentiation (`N_ℍ(0) − N_{M₃}(0)` stays intact). This protects the inter-summand instance from a spurious FAIL by someone who accidentally zeroes a substrate parameter. Correct and necessary; pinned.

**The commitment-asymmetry — the residue of my COLLAPSE, demoted but not dissolved.** I grant volovik's symmetry at Level-1 (both forms real, distinct-cornered) and deny it at the physical-instance layer. The two bridges are symmetric in LAB-ANCHOR incompleteness (OP-PROJ's image Y unmeasured; STATE-PROJ's value lab-fed) but ASYMMETRIC in SUBSTRATE COMMITMENT: OP-PROJ commits `R_∞ = −1.892` with zero lab input (passes the vanishing test trivially); the A/B-STATE-PROJ commits zero absent the lab split (`R_BdG → 0` when `SC_A = SC_B`, since `a_bdg = b_bdg` identically on the common spectrum — verified to machine ε, npz `a_bdg=31.295`, `b_bdg=27.264`, signal `a−b=4.03` only because `Δ_A_sub=0.5344 > Δ_B_sub=0.5158`). Volovik adopted this correction to his own R2 "symmetric incompleteness" in his R3 §5; with that adopted, nothing remains between us. The credential is held for STATE-PROJ *specifically*, and not arbitrarily — held because STATE-PROJ FAILS the vanishing test while OP-PROJ PASSES it.

I now write the Structural Verdict.

---

## Structural Verdict

**VERDICT: ORTHOGONAL, level-separated. The route-identity fork resolves ORTHOGONAL at the Level-1 identity layer; COLLAPSE is rejected there. The "first PHYSICAL (3He-B) instance" of the algebra-axis orthogonality conjecture is CONFIRMED at the structural / identity layer; its fully-substrate-first physical-realization anchor is HELD Track-B (Level-3), with an explicit discharge condition (the vanishing test + CF-S117).**

§VII.AJ.STATE-PROJ and §VII.AJ.OP-PROJ are TWO substrate-IS functionals on `(A_K, H_K, D_K)` — structural-orthogonal companions, NOT one observable read two ways. Both arrows depart the same operator `D_K`, but a shared origin operator is not a collapse: every functional on a spectral triple is a functional of `D_K`, and §VII.U.2 (four-corner classification, STAGE-3-PERMANENT, `permanent-results-registry.md:136`) is precisely the theorem that the algebra-INVARIANT family `F({λ_k,m_k}) = Σ_k m_k g(λ_k)` and the algebra-DEPENDENT family (state-pair functionals on `A_K`) are orthogonal in identity-class membership *despite* the shared operator. COLLAPSE would have had to defeat that theorem at its first physical instance; it does not.

**COLLAPSE is rejected at the identity layer** — three candidate collapse mechanisms tested, each failed (all conceded by landau's own R1):

- *The BCS gap-equation linkage is a RELATION, not an IDENTITY.* The gap equation maps `{λ_k} → {v_k²}`, but `ρ_BCS(P·H)` carries the sector-module label `P_sector` that the bare count `Σ_k m_k g(λ_k)` discards. The map is many-to-one in exactly the data separating Corner I from Corner III — it relates the two functionals, it does not identify them. (landau R1-Q1.)
- *OP-PROJ is not spurious.* It is a genuine representation-theoretic count of how the SU(3) fabric distributes in Casimir around the median Mellin pole; it images a real laboratory observable Y (the BdG-undoubled DOS-excess at the fold), not a mis-specified image of X. The S87 `ratio_mismatch ≈ 1.03` FAIL was the FAIL of forcing ONE observable to image the A/B asymmetry; the correct response — what §VII.AJ did — was to SPLIT into two companions, OP-PROJ→Y and STATE-PROJ→X. (landau R1-Q2; "spurious" withdrawn.)
- *The sign-flip is a two-observable fingerprint, not a defect in one.* `R_∞ = −1.892` (a DOS-geometry statement) and `R_BdG = +0.068847` / `R_STATE = +0.035356` (a condensation-energy-asymmetry statement) answer different questions and are under no symmetry obligation to share a sign.

**The two layers, separated** (the resolution both sides converged on — the apparent COLLAPSE-vs-ORTHOGONAL conflict was a conflation of two levels of the 3-level ladder):

- **Level-1 (identity / cohomology-class), value-free → ORTHOGONAL.** STATE-PROJ is an algebra-DEPENDENT state-pair functional `ρ_BCS(P·H)` (**Corner III**); OP-PROJ is an algebra-INVARIANT spectrum-only count `Σ_k m_k g(λ_k)` (**Corner I**). The corner assignment is FORM-level — decided by the presence of `P_A, P_B ∈ A_K` in STATE-PROJ's parse tree versus their absence from OP-PROJ's — and consults no number, so the Track-B magnitude caveat cannot touch it. Cross-corner co-primary FORBIDDEN (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, K=3 MANDATORY; `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`). The registry already carries the STRUCTURALLY-ORTHOGONAL-COMPANION tag on the pair (`permanent-results-registry.md:16792`); this verdict confirms it at its first physical realization.
- **Level-3 (empirical anchor) → HELD Track-B for STATE-PROJ.** Its value `+0.035356` IS `R_3HeB_lit` to `rel_match_vs_lit = 0.0` — a Level-3 tautology (the bridge is evaluated with lab-fed `SC_A/SC_B = 1.151/1.111`, Serene–Rainer 1983 / Greywall 1986). The substrate gap `Δ_BCS = 0.46425 M_KK` cancels EXACTLY out of `R_STATE` (`R_from_SC = 0.0353558759605834` vs `R_STATE = 0.035355875960583226`, ~1.7e-16 residual, both re-read from the W7-1 npz); the substrate-first cross-check `R_BdG = +0.068847` is substrate-NORMALIZED (the 78,080 modes set `a+b`) but lab-SIGNED (`a−b ≠ 0` only because `SC_A > SC_B`). `substrate_first_SC_ratio_available = False`.

**The vanishing test (pre-registered gate separating the layers, both sides signed).** An observable is a VALUE-physical (Track-A) instance iff it returns nonzero on the *undifferentiated* substrate — the no-lab-contrast `SC_A = SC_B`, common-`Δ_BCS` limit. OP-PROJ PASSES trivially (`R_∞ ≠ 0`, zero lab input). The A/B-STATE-PROJ FAILS (`R_BdG → 0/(2·a_bdg) = 0` when `a_bdg = b_bdg` identically on the common spectrum). The diagnostic is the *provenance of the residual* after `Δ_BCS` cancellation — a lab ratio (FAIL) vs a substrate DOS ratio (PASS) — NOT the cancellation itself, which is generic to ratio functionals. The credential is held for STATE-PROJ *specifically* because it fails this gate, not arbitrarily.

**Algebra-axis K-counter: CONFIRMED / ADVANCES at the identity-class (Level-1) layer.** §VII.AJ is the first PHYSICAL (3He-B) instance of the (already-MANDATORY-at-K=3) algebra-axis orthogonality conjecture: two real 3He-B forms in distinct corners — a value-free structural landing. The STRONG "first PHYSICAL instance" credential, read as a fully substrate-first physical realization, is TAGGED Track-B / Level-3 and HELD pending CF-S117. Per the two-clause separation (`cross-pillar-bridge-anatomy.md §"Two-clause separation"`), the rule-level structural calibration landing is valid AND the per-entry registry-PASS is INCOMPLETE (§VII.AJ.STATE-PROJ → `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`) — separate predicates.

**Residual partial-collapse (on the record).** The two functionals are orthogonal in the **sector-label subspace** (OP-PROJ blind to `P_sector`; STATE-PROJ sensitive to it) but co-vary in the **overall-spectrum subspace** (both built from the one substrate mean field `{ξ_k}`; move it and both move). Orthogonal in identity-class; linked through the shared mean field. The regulator-response sibling discriminator keeps them separate at the identity layer: STATE-PROJ is gap-self-regularized (IR-cut by `|Δ|`, regulator-INVARIANT — `E_cond ≈ ½N(0)Δ²`, gap-set); OP-PROJ is regulator-DEPENDENT (Mellin-window-sensitive). The linkage is the residual; the corner-distinction is the orthogonality; neither erases the other. [Resolves sub-(a) parse-tree, sub-(b) sign-flip, sub-(c) BCS mean-field.]

| Item | Verdict | Note |
|:-----|:--------|:-----|
| Route identity | **ORTHOGONAL** | No identification map; distinct corners; OP-PROJ not spurious (images Y, the BdG-undoubled DOS-excess). COLLAPSE rejected at the identity layer. |
| Parse-tree corners | **STATE-PROJ Corner III (algebra-DEPENDENT `ρ_BCS(P·H)`) ⊥ OP-PROJ Corner I (algebra-INVARIANT `Σ_k m_k g(λ_k)`)** | FORM-level (`P_A,P_B∈A_K` present vs absent; value-free); cross-corner co-primary FORBIDDEN; structural-orthogonal companions (registry `:16792`). |
| Sign-flip reading | **orthogonality evidence (corroborating, NOT load-bearing)** | `R_BdG=+0.0688` / `R_∞=−1.892`: a two-observable fingerprint at the FORM level; but the STATE-PROJ sign is lab-set (`SC_A>SC_B`) — must NOT be cited as clean substrate evidence (both sides withdrew the overreach). |
| BCS gap-equation linkage | **RELATION, not collapse — gap-self-reg keeps separate** | Maps `{λ_k}→{v_k²}` (real mean-field linkage; partial-collapse in the overall-spectrum subspace only); does NOT identify the count with the state-pair functional. |
| Algebra-axis K-counter | **CONFIRMED — first PHYSICAL (3He-B) instance at Level-1 (value-free); Level-3 physical-realization anchor HELD Track-B → CF-S117** | Structural calibration landing valid; registry-PASS INCOMPLETE (`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`); two-clause separation. |

---

## Remaining Open Questions

1. **The CF-S117 inter-summand Track-A instance (the discharge condition for the held credential).** Does `R_summand = (E_cond[ℍ] − E_cond[M₃])/(E_cond[ℍ] + E_cond[M₃])` at common `Δ_BCS` return nonzero (G1, substrate-commitment) AND gap-localized / regulator-flat (G2, Corner-III membership)? `G1 ∧ G2` PASS discharges the held physical-instance credential to fully substrate-first; either FAIL holds it. HONEST RISK: G1 requires `N_ℍ(0) ≠ N_{M₃}(0)`, a Peter–Weyl multiplicity / Casimir-weighted gap-edge-DOS fact the compute must ESTABLISH — generically expected from the distinct rep content of ℍ vs M₃(ℂ), but NOT a foregone PASS; a null `R_summand` is an informative FAIL (the two summands carry identical gap-edge DOS).

2. **OP-PROJ's lab image Y is unmeasured (symmetric incompleteness, opposite direction).** `R_∞ = −1.892` is substrate-committed (passes the vanishing test), but the BdG-undoubled DOS-excess Y it predicts has no measured 3He-B anchor cited (atlas-07 carries `R_∞` only as a substrate-first extrapolant). The OP-PROJ bridge is empirically open on the LAB end; the STATE-PROJ bridge is empirically open on the SUBSTRATE end. A measured 3He-B DOS-excess anchor would complete OP-PROJ's bridge — the converse discharge to CF-S117.

3. **The CF-S117 literal A/B form is structurally BLOCKED.** A substrate-first derivation of `SC_corr_A/B` is obstructed by the no-A-sector topology (no substrate `Δ_A`; the fabric realizes only the BW-like `N_3=0` order-parameter manifold). Recorded as a HIGH-RISK CF whose likely outcome is a structural-impossibility FAIL; the inter-summand reframe (Q1) is the productive route that sidesteps it without touching 3He Landau parameters.

---

## Wrap-Up

### What Changed

#### (a) Numerical revisions

- **None minted or revised** — this workshop is a structural adjudication, not a compute. The W7-1 (`S116-W7-STATEPROJ-BCS`) values are CONFIRMED disk-true (cross-read from `computations/session-116/s116_w7_stateproj_bcs.npz` by both sides): `R_STATE = +0.035355876`, `R_from_SC = +0.035355876` (`Δ_BCS`-cancellation residual ~1.7e-16), `R_BdG = +0.068847`, `R_BdG − R_STATE = +0.033491`, `R_substrate_OP_L10 = −1.212219`, `OP_PROJ R_∞ = −1.892`, `a_bdg = 31.295`, `b_bdg = 27.264`, `SC_A/SC_B = 1.151/1.111`, `Δ_BCS = 0.46425 M_KK`, `substrate_first_SC_ratio_available = False`, composite = INFO / Track-B. (Confirmation, not revision.)

#### (b) Structural changes

- **§VII.AJ resolved as TWO structural-orthogonal companions** (NOT "one genuine + one spurious") — the headline structural reframe. landau's R1 "one substrate-IS + one lab-target-in-costume" reading is WITHDRAWN; OP-PROJ images a distinct lab observable Y (BdG-undoubled DOS-excess), STATE-PROJ images X (A/B asymmetry), with NO identification map.
- **Route-identity fork RESOLVED: ORTHOGONAL at Level-1; COLLAPSE rejected at the identity layer.**
- **Epistemic-TYPE split made explicit (two-axis win):** the COLLAPSE-vs-ORTHOGONAL tension was a Level-1 (identity) vs Level-3 (value-provenance) conflation; once separated, no conflict. Identity → ORTHOGONAL (volovik); value-provenance → Track-B HELD (landau).
- **Algebra-axis orthogonality K-counter: first PHYSICAL (3He-B) instance LANDED at the identity / Level-1 (structural) layer** (value-free); the physical-realization credential level-separated from the structural instance and HELD Track-B (Level-3).
- **The VANISHING TEST established** as the pre-registered operational gate separating FORM-physical (Track-B, anchor HELD) from VALUE-physical (Track-A, registry-PASS-eligible) instances — *nonzero on the undifferentiated substrate*; diagnostic = provenance of the residual after `Δ_BCS` cancellation. **Gap-localization** established as the Corner-III-membership test for the inter-summand reframe.
- **§VII.AJ.STATE-PROJ status reclassified:** `OPEN (NEEDS-COMPUTATION)` → `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (deferred-pending intermediate verdict-class; reserves the slot, does NOT contribute to registry-PASS). [Curated-surface SPEC; mack-dispatch — §A7.]

### What Holds

- **§VII.U.2 four-corner classification (STAGE-3-PERMANENT, `permanent-results-registry.md:136`)** — unscathed; this workshop is its first physical-platform instantiation.
- **Cross-corner co-primary FORBIDDEN; the STRUCTURALLY-ORTHOGONAL-COMPANION tag on §VII.AJ.OP-PROJ ↔ §VII.AJ.STATE-PROJ** (`permanent-results-registry.md:16792`) — confirmed at first physical realization.
- **BCS universality class 3D Ising / AZ class BDI, `N_3 = 0`** (landau wall #8) — the single-vacuum (BW-like, no ABM manifold) topology is the load-bearing premise of the vanishing test, and it holds.
- **OP-PROJ `R_∞ = −1.892` substrate-committed prediction** (STAGE-1-CANDIDATE) — unchanged; passes the vanishing test trivially.
- **The `Δ_BCS`-cancellation and the R_BdG substrate-NORMALIZED / lab-SIGNED facts** — machine-ε confirmed, both sides, from the W7-1 npz.
- **The capstone Φ-correspondence reference to the algebra-axis orthogonality theorem** (`phonic-exflation-equation.md:313`) — REINFORCED, not strained: the theorem it cites is exactly what this workshop instantiates physically.

### What Breaks or Strains

- **The STRONG "first PHYSICAL instance" credential for STATE-PROJ** — does NOT hold today (Track-B; fails the vanishing test, `R_BdG → 0` absent the lab `SC_A ≠ SC_B` split). HELD, not broken; CF-S117 is the discharge route.
- **CF-S117's literal form (substrate `SC_corr_A/B`)** — structurally BLOCKED by the no-A-sector obstruction (Volovik topology; no substrate `Δ_A`). HIGH-RISK; the inter-summand reframe is the productive substitute.
- **The sign-flip as substrate evidence** — STRAINS: it is a FORM-level two-observable fingerprint, but the STATE-PROJ sign is lab-set; it must NOT be cited as clean substrate evidence (both sides withdrew the overreach in R2/R3).
- **Nothing in the established constraint map is broken.** A held credential with a falsifiable discharge is a mapped boundary, not a defeat (`epistemic-discipline.md §"Negative results are boundaries"`).

### Carry-Forward Computations (MATH ONLY — propagate to S117)

#### CF-S117-STATEPROJ-SC-FROM-SUBSTRATE — [HIGH-RISK; literal form; structurally BLOCKED]

1. **What**: substrate-first derivation of `SC_corr_A/B` (the A/B gap-modulation ratio) from `A_K`, replacing the Serene–Rainer 1983 / Greywall 1986 lab inputs, to give §VII.AJ.STATE-PROJ a substrate-first Level-3 anchor and discharge the held credential via the LITERAL A/B observable.
2. **Inputs**: `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`; D_K spectrum cache; W7-1 npz `computations/session-116/s116_w7_stateproj_bcs.npz` (`substrate_first_SC_ratio_available = False`); Volovik `N_3 = 0` single-vacuum topology (no substrate `Δ_A`).
3. **Gate**: `S117-STATEPROJ-SC-FROM-SUBSTRATE` — PASS iff a substrate-first `SC_corr_A/B` is derivable AND `R_STATE` recomputed from it matches the lab value within a pre-registered band. **EXPECTED-BLOCKED**: the substrate has no A-phase (ABM/DIII, `N_3 = 2`) order-parameter manifold to source `Δ_A`; a structural-impossibility FAIL is the likely informative outcome (it would convert "Track-B anchor" into "structurally-no-substrate-anchor-by-this-route").
4. **Effort**: ~2 wave-equivalents (mostly the topological-obstruction confirmation, not a long compute).
5. **Depends on**: D_K spectrum cache (UPSTREAM); Volovik `N_3 = 0` topology (landau wall #8 / S44); this workshop's Structural Verdict (the no-A-sector obstruction statement). SIBLING-not-prerequisite to CF-S117-STATEPROJ-INTER-SUMMAND.

#### CF-S117-STATEPROJ-INTER-SUMMAND — [PRODUCTIVE; Track-A-eligible; sidesteps the obstruction]

1. **What**: compute `R_summand = (E_cond[ℍ] − E_cond[M₃])/(E_cond[ℍ] + E_cond[M₃])` at the COMMON substrate gap `Δ_BCS` (ℍ vs M₃(ℂ), no A-phase required) as a substrate-first Track-A STATE-PROJ (Corner-III) instance — the route that discharges the held physical-instance credential without touching 3He Landau parameters.
2. **Inputs**: `A_K` summands ℍ, M₃(ℂ); per-summand gap-edge DOS `N_ℍ(0)`, `N_{M₃}(0)` (Peter–Weyl multiplicities / Casimir-weighted, from the D_K spectrum cache); common `Δ_BCS = 0.46425 M_KK` (canonical); `E_cond(Δ) = Σ_k[|ξ_k| − E_k + Δ²/(2E_k)]`, `E_k = √(ξ_k² + Δ²)` (W7-1 npz lines 192–202); selection-rule pre-flight (each `E_cond[S]` is a `|Δ|²` diagonal expectation ⇒ center-character `t = 0` for SU(3) ⇒ no triality obstruction).
3. **Gate**: `S117-STATEPROJ-INTER-SUMMAND` — composite `G1 ∧ G2`:
   - **G1 (vanishing / substrate-commitment)**: `R_summand(SC_A = SC_B, common Δ_BCS) ≠ 0`. PASS = nonzero residual = genuine substrate gap-edge-DOS asymmetry `(N_ℍ(0) − N_{M₃}(0))/(N_ℍ(0) + N_{M₃}(0))`. HONEST RISK: requires `N_ℍ(0) ≠ N_{M₃}(0)` — a Peter–Weyl multiplicity fact the compute must ESTABLISH (generically expected, NOT foregone; a null is an informative FAIL = the summands carry identical gap-edge DOS).
   - **G2 (gap-localization / Corner-III membership)**: `N_ℍ(0)/N_{M₃}(0)` regulator-FLAT across the L_max scan AND the Mellin window (computed as a `v_k²`-weighted gap-edge quantity, NOT a Mellin-pole-window count). PASS = flat ⇒ stays Corner III (algebra-DEPENDENT, gap-self-regularized); FAIL = drifts ⇒ inherits OP-PROJ's Corner-I regulator-dependence (wrong corner, credential muddied).
   - **Composite**: `G1 ∧ G2` PASS ⇒ Track-A VALUE-physical instance ⇒ registry-PASS-eligible; discharges the HELD credential; upgrades the K-counter's first physical instance to fully substrate-first. Either FAIL ⇒ credential stays HELD; §VII.AJ.STATE-PROJ remains `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`.
4. **Effort**: ~2–3 wave-equivalents (per-summand gap-edge DOS compute + the L_max/Mellin-window regulator-flatness scan).
5. **Depends on**: D_K spectrum cache + per-summand Peter–Weyl multiplicities (UPSTREAM); the vanishing test + gap-localization gate (THIS workshop's Structural Verdict, the pre-registered G1∧G2 criterion); `Δ_BCS = 0.46425 M_KK` (canonical_constants). INDEPENDENT of CF-S117-STATEPROJ-SC-FROM-SUBSTRATE (the inter-summand route does not require the blocked literal form).

### Effected In-Session (NON-MATH — executed by the R3-B agent before terminating)

- [x] **§VII.AJ.STATE-PROJ slot status + algebra-axis K-counter first-physical-instance landing + atlas-08 Q33 status update — SPECIFIED + ROUTED to housekeeping §A7 for mack dispatch.** All three are CURATED §VII / registry / atlas surfaces (mack-cosmic-bridge sole-writer domain, `feedback_mack-bridge-role.md`); NOT edited by this workshop agent. The precise current → corrected text for every locus — atlas-07:674 STATE-PROJ status cell + atlas-07:767 status-tally; `permanent-results-registry.md:179` index row + the §VII.AJ.STATE-PROJ entry-body Status line (~`:16754+`); `cross-pillar-bridge-corpus.md §6` first-physical-instance calibration row; atlas-08 Q33 dashboard (`:23`) + §VI.B detailed (`:264`) — is written to `sessions/session-116/session-116-housekeeping.md §A7`, with the capstone-hygiene 5-question gate (Q3=YES→§A; capstone prose NO-OP, grep-verified) and the RETAIN-and-supersede / two-clause-separation disciplines pinned. **Action**: specified + routed to housekeeping §A7 for mack dispatch at §6.
- [x] **Own agent-memory note — EXECUTED directly** (`.claude/agent-memory/landau-condensed-matter-theorist/s116_w7_algebra_axis_result.md` + MEMORY.md index pointer; the agent-private S116-W7 verdict record — vanishing test, order-parameter framing, CF-S117 gate, value-provenance/identity two-axis split). In-domain, non-curated, no AMRI (no other gate pins this file).

(NO `.py` compute, NO curated-doc edit by this agent — the workshop closes by artifact-existence, NO verdict line.)

### Closing Line

I came in arguing COLLAPSE and leave having won the value-provenance axis without ever needing the corner-identity it never depended on — §VII.AJ is two structural-orthogonal companions, ORTHOGONAL at the identity layer, with the substrate committing to one leg (`R_∞ = −1.892`) and the laboratory still speaking for the other: a HELD credential with a falsifiable discharge (the vanishing test, via CF-S117's inter-summand route), not a defeat.
