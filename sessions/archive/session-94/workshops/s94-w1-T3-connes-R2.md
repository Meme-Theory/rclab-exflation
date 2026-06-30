# W-1 Turn 3 — connes-ncg (R2 rebuttal of lizzi + refinement)

**Workshop**: W-1, §VII.AU.OP-PROJ α=−3 discharge status adjudication
**Turn**: T3 (FINAL connes turn — rebut lizzi's T2 + state convergence; lizzi writes the balanced JOINT VERDICT in T4)
**Agent**: connes-ncg-theorist (Reading A; author of W2-3 and T1)
**Opponent**: lizzi-spectral-functional-theorist (Reading B; T2 done; writes T4)
**Adjudication options**: (a) FULL-RECOVERED bare; (b) structural-posit / consistency-confirmed, SCHEMATIC cap preserved; (c) two-layer split; (d) re-tag fine but verdict-line/registry reconciled.

---

## 0. Where this turn lands, stated once and sharply

> I **converge on (c)**, the two-layer split. I do not hold for bare (a), and I withdraw the §VII.3/§VII.7 framing of (a) as "honest as a single tag." lizzi's exponent-vs-observable distinction is correct in its premise and I concede it: `FULL-RECOVERED` as a *single bare registry status* over a slot whose verdict-line carries `LEVEL_CLASS_PIN=SCHEMATIC tier_pin=TIER-2` IS a status-layer class-conflation, and her §III.2 orthogonality-cuts-both-ways argument is a valid proof that `STRUCTURAL-FULL(exponent) ⇏ FULL-RECOVERED(single-tag corridor)` on the binding axis. **I lose that inference, and I say so plainly.**
>
> But the convergence is on (c), NOT on (b), and the distinction is not cosmetic — it is the entire residual disagreement. lizzi's T2 contains one move I must defeat, and it is defeatable from the framework's own canon, not from my preferences: **her claim (§II, §VII) that the corridor has a numerical-`c_continuum` object DISTINCT from the exponent, still SCHEMATIC, which is what `NUMERICAL-DEFERRED` deferred.** That claim is false on the registry record. The corridor's deferred object IS the Level-1 asymptotic exponent itself, certified via the analytic-saturation route — there is no separate numerical anchor hiding behind the word "NUMERICAL." This is decisive for (c)'s *shape*: it means the FULL-RECOVERED layer of (c) is the WHOLE deferred object, and the SCHEMATIC-pending layer is the EVALUATION-ROUTE provenance — not a second, unrecovered physical number. (b) mis-locates the residual; (c) locates it correctly. I show this in §III, and it is the reason I do not accept (b) as the economical contraction lizzi offers.

Everything below: §I concedes precisely and bounds the concession; §II defeats the `c_continuum`-distinct-object claim from the registry record; §III defeats (b)-as-contraction and fixes (c)'s exact two-layer form; §IV addresses her Sage-separability and S91-CLASS=FULL moves head-on; §V is the convergent registry form with verdict-line/`LEVEL_CLASS_PIN` reconciliation made explicit.

---

## I. What I concede, exactly — and the boundary of the concession

I concede, without reservation, the following four of lizzi's moves:

1. **The exponent-vs-observable distinction is real and load-bearing.** There are two substrate-IS objects: the cone exponent `α = −(d−1)` (Level-1, cohomology-class, FI, regulator-invariant) and "the corridor's binding content." `FULL-RECOVERED` as a *bare single tag* predicates over the corridor, and the corridor carries a SCHEMATIC verdict-line. A bare FULL-RECOVERED tag therefore erases the SCHEMATIC class at the highest-leverage (status) layer — exactly the §(iv) class-conflation the rule forbids. **Granted. T1's §VIII "verdict argued: (a) FULL-RECOVERED is honest" is withdrawn as a single-tag claim.**

2. **Orthogonality cuts both ways — my T1 §IV.3 proves lizzi's conclusion, not mine, on the binding axis.** I asserted `SCHEMATIC(provenance) ⊥ STRUCTURAL(exponent)`. lizzi's §III.2/§III.3 correctly turns this around: if the Level axis and the cohomology-class axis are pairwise-independent, then a FULL result on the cohomology-class axis cannot *upgrade* the Level-axis SCHEMATIC reading to FULL. My orthogonality protects the exponent from the SCHEMATIC tag; it equally forbids the exponent's FULL status from propagating onto the binding axis to make a single-tag corridor FULL-RECOVERED. **The implication `STRUCTURAL-FULL(exponent) ⇒ FULL-RECOVERED(single-tag corridor)` is denied by my own orthogonality. I concede this is a clean refutation of bare (a).**

3. **The S91 `CLASS=FULL` provenance is exactly as lizzi states it.** I verified it this turn via the knowledge MCP: `get_constant("alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC")` returns value `−3.0`, **Session S91**, `CLASS=FULL`, deferred object `asymptotic-limit-derivation-DEFERRED-to-CF-S94-W5-3`, provenance added retroactively at S93 W2-3. lizzi is *right* that the exponent value was canonical-FULL three sessions before W2-3 ran, and right that W2-3 therefore did not establish `−3`. My T1 §II.2 already conceded "W2-3 did not establish −3"; lizzi correctly sharpens that into "so the SCHEMATIC tag on the W2-3 line is tagging the DISCHARGE OBJECT (the route-certification), not the exponent." **Granted.**

4. **The Sage window-separability result is correct as arithmetic.** lizzi's T2 §V.1 re-ran my `α(L)` model with `p ∈ {−2.7, −3.0, −3.3}` and showed the in-window slopes shift rigidly with the assumed leading exponent; the `(C₁/L)/(1+C₁/L)` tail is a `p`-independent additive offset; the window [35,100] cannot separate `p=−3` from a nearby `p` because that separation lives only at the never-sampled `L→∞` limit. **Granted as arithmetic.** (I dispute only the inference she draws from it — §IV.2.)

**The boundary of the concession.** I concede everything about the *single-tag* reading of (a). I do NOT concede that the residual is what (b) names it. (b) says the residual is "the corridor's numerical-FULL-extraction of the OBSERVABLE's `c_continuum` anchor, still pending." That phrase smuggles in a *distinct physical number* — a `ρ_FULL(s=3,∞)` continuum amplitude separate from the exponent — and asserts that THAT number is what `NUMERICAL-DEFERRED` deferred. The registry record says otherwise. Defeating that smuggle is the whole of §II–§III, and it is the reason convergence lands on (c), not (b).

---

## II. There is no `c_continuum` object distinct from the exponent — the registry record decides it

lizzi's T2 builds (b)/(c) on a two-object ontology (§I.2, §V, §VII):

- object (1) = the cone exponent `−(d−1)` [conceded recovered], and
- object (2) = "the corridor observable — the residual `R_b(L) = ρ_FULL(s=3,L) − ρ_FULL(s=3,∞)` and its FULL-physical approach … the *amplitude-and-rate* … what a Level-3 anchor pins … the `c_continuum` reference" [claimed still SCHEMATIC, and claimed to be what `NUMERICAL-DEFERRED` deferred].

This is the crux, and it is checkable, not arguable. **What was the §VII.AU.OP-PROJ corridor's deferred object?** I queried the knowledge base this turn. Three registry-PROVEN theorem hits and the corridor gate's own definition return the answer in the framework's own words:

**(i) The corridor's content is the Level-1 asymptotic exponent, verbatim.** The registry theorem text (knowledge MCP, `permanent-results-registry.md`, status PROVEN):

> *"**Reading A — SCHEMATIC convergence-exponent two-pin protocol** (RETAINED): `alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = −3` (**Level-1 asymptotic `L^{−3}` leading[-term]** …)."*

and the asymptotic-anchor row:

> *"**Asymptotic anchor**: `alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = −3` (**Level-1 leading-term universal across Cell I × substrate-distance-1 pole `s=3`** per CM-1995 §III.4)."*

The corridor's content, as the registry records it, is **the Level-1 leading-term exponent** `−3`. It is not "an amplitude-and-rate `c_continuum`." The word "NUMERICAL" in `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED` does not name a second physical number; it names the **route by which the exponent's asymptotic value is read** — the analytic-saturation NUMERICAL evaluation of `α(L)` as `L→∞`, as opposed to a purely axiomatic read-off. lizzi's own T2 §II quotes the constant's provenance correctly — the deferred object is `asymptotic-limit-DERIVATION`, "a statement about an *evaluation route* reaching the limit, not about the limit's value" (her words, §II). **That is exactly my point turned to my purpose: the deferred object is the route to the exponent, not a `c_continuum` distinct from it.** There is no third row in lizzi's own §II table (row 3, "Corridor numerical-FULL-extraction (live Mellin-Barnes at L≥13)") that names a *different observable*; it names a *different evaluation method for the same exponent*.

**(ii) The "amplitude" `c` in `R_b(L) = c·L^{−3}(1+C₁/L)` is a sub-leading fit detail, not the corridor's deferred object.** lizzi conflates "the corridor's binding numerical anchor" with the fit amplitude `c` and the correction `C₁`. But the corridor was registered as a *convergence-rate* corridor — Level-1/Level-2 in the framework's own ladder — whose binding content is the *exponent* (`cross-pillar-bridge-anatomy.md` Level-2 envelope = `L^{−α}` *rate*, not amplitude). The Level-2 envelope's binding content is `α`, not `c`; `c` is a Level-3 amplitude that does not BIND the Level-1 cohomology-class identity. lizzi's §VI.1 even concedes "freezing the spectrum tells you the residual is a fixed analytic function of L" — i.e., the amplitude `c` and correction `C₁` ARE determined by the frozen L≤12 cache (which is why my W2-3 fit recovered `C₁=−3.846` at R²=0.99988 from REAL frozen-cache residual, not synthetic). So even the amplitude is not "deferred-and-unrecovered"; it is *fit from frozen FULL-physical data*. The only thing not done by a live high-L pipeline is the **route**, which is the SCHEMATIC two-pin protocol — and the route is provenance, not a physical observable.

**Consequence.** lizzi's two-object ontology has one object (the exponent) that is recovered, and a second object (`c_continuum`/amplitude-and-rate) that, on the registry record, either (a) IS the exponent (the "rate"), already recovered, or (b) is the amplitude `c`, fit from frozen FULL-physical data, also not an open deferral. There is no surviving third object that is both physical and unrecovered. **What remains SCHEMATIC is the EVALUATION ROUTE, not an observable.** This does not defeat (c) — but it fixes (c)'s shape against (b), as §III now shows.

---

## III. Why (c), not (b): the residual is a ROUTE-provenance layer, not an unrecovered-OBSERVABLE layer

lizzi offers (b) as "the economical correct status" and (c) as "the floor I will accept if connes insists the exponent's recovery be annotated FULL somewhere." I reject the framing that (c) is a concession *to me* about annotating the exponent; (c) is the *correct registry anatomy*, and (b) is structurally wrong because it mislabels the residual. Here is the precise difference, stated as a substitution chain on the registry layers.

### III.1 The two-layer object, named correctly

```
Layer-1 (cohomology-class / exponent):
    object   = α = −(d−1) = −3  (the corridor's REGISTERED content; Level-1 leading-term)
    status   = FULL / PROVEN     (registry-PROVEN, FI, regulator-invariant, L-independent;
                                  canonical-FULL since S91, independent of W2-3)
    binding  = this IS the Level-1/Level-2 convergence-RATE corridor content

Layer-2 (evaluation-route provenance):
    object   = the analytic-saturation NUMERICAL route that reads α off as L→∞
               (the SCHEMATIC two-pin convergence-exponent protocol; rho_FULL_CC_VII_AU_SAT_s3)
    status   = SCHEMATIC tier_pin=TIER-2  (NOT a live full-physical Mellin-Barnes at L≥13)
    binding  = this is a SOURCING/PROVENANCE fact, NOT a physical observable still-deferred
```

### III.2 Why (b) is wrong, in one line

(b) writes a SINGLE row whose status is "structural-posit / consistency-confirmed, SCHEMATIC tier_pin preserved." A single row forces ONE status onto a slot that carries TWO orthogonal statuses (Layer-1 FULL, Layer-2 SCHEMATIC). lizzi's OWN §III.3 orthogonality proof says these axes are independent — so collapsing them into one "consistency-confirmed-SCHEMATIC" tag is the *same axis-collapse error* she (correctly) convicts bare (a) of, committed in the opposite direction: (a) collapses to FULL, (b) collapses to SCHEMATIC. **Both single-tag options collapse two orthogonal axes into one. Only (c) writes both.** This is not me insisting the exponent be "annotated FULL somewhere"; it is the orthogonality theorem lizzi herself proved demanding that two independent axes get two independent status rows.

Moreover, (b)'s label "structural-posit" understates Layer-1. The exponent is not a *posit* (a standing assumption); it is a **registry-PROVEN theorem** (`−(d−1)`, FI, the β_shell FI sibling at the same `d=4` `s*=3` pole — both of us conceded this). Calling a PROVEN cohomology-class identity a "posit" at Layer-1 is itself a status-downgrade that the §(iv) discipline, read symmetrically, forbids: just as SCHEMATIC must not be erased upward, PROVEN must not be erased downward. (c) gives Layer-1 its correct PROVEN/FULL status and Layer-2 its correct SCHEMATIC status. (b) does neither cleanly.

### III.3 The decisive reason (b) cannot be the economical contraction of (c)

A single-row contraction of a two-row orthogonal structure is admissible ONLY when the two rows carry the *same* status (then the contraction loses nothing). Here they carry *opposite* statuses on an axis the framework holds orthogonal. A contraction is therefore lossy by construction — it discards exactly the orthogonality content that is the whole point of the §(iv) Level axis. **(b) is not a lossless contraction of (c); it is a lossy projection onto one axis.** lizzi's §IV offers (b) as "the most economical correct tag." It is economical; it is not correct, because economy that discards an orthogonal axis is the class-conflation pathology, not a remedy for it.

This is why I converge on (c) and decline (b). It is not a split-the-difference; it is the registry-anatomy-faithful reading that lizzi's own orthogonality proof forces.

---

## IV. Rebutting lizzi's two sharpest specific moves

### IV.1 The S91-CLASS=FULL move (her §II) — what it proves and what it does not

lizzi's §II is her strongest section. The fact is verified (§I.3 above). Her inference: "if the exponent was canonical-FULL in S91, the SCHEMATIC tag on the W2-3 line tags the *discharge object* (route-certification), and a status honest to W2-3's deliverable is (b)/(c)." I **agree with the premise and with (c); I reject only the slide to (b)**:

- **What it proves**: the SCHEMATIC tag is NOT tagging the exponent (which is independently FULL since S91). Correct. The SCHEMATIC tag tags the **route**. Correct. This is *precisely* my Layer-2 in §III.1 — the SCHEMATIC class lives on the evaluation-route provenance axis. lizzi has, in her §II, independently derived my Layer-2. We agree the SCHEMATIC tag is real and lives on the route axis.

- **What it does NOT prove**: that the corridor's *content* (the exponent) is anything other than FULL/PROVEN. lizzi's §II says "you cannot discharge a NUMERICAL-DEFERRED corridor by pointing at a theorem already canonical before the discharge gate ran." But that argument, taken to its end, proves the corridor was ALREADY substantively discharged at S91 (the exponent was FULL then) and W2-3 only added the route-certification. That is FINE for (c): Layer-1 was FULL since S91; W2-3 discharged Layer-2's route to it (SCHEMATIC). The corridor's *re-tag* `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → FULL-RECOVERED` is then honest **at Layer-1** (the content, the exponent, is FULL/PROVEN — and was) and requires a **Layer-2 SCHEMATIC-pending annotation** (the route is SCHEMATIC). That is (c), verbatim. lizzi's §II is an argument FOR (c)'s two-layer shape; it is not an argument that Layer-1 is anything less than FULL.

So her §II lands us both on (c). The S91 fact does not push past (c) to (b) — it cannot, because the very fact that the exponent was FULL in S91 is what makes Layer-1's FULL status PROVEN-and-prior, not a "posit."

### IV.2 The Sage-separability move (her §V) — separability is not required for a structurally-fixed exponent

lizzi's §V.1 arithmetic is correct (§I.4). Her inference: "the window cannot pin `p`; the fit supplies `p=−3` as INPUT and certifies consistency; therefore the status is (b) consistency-confirmed, not (a)/FULL-extraction." Here is the decisive reason her inference fails to reach (b), and lands at (c)'s Layer-1-FULL instead:

**Independent pinning of `p` from the window is NOT required, because `p` is supplied a priori by a cohomology-class theorem — and for a structurally-fixed exponent, the fit is correctly a consistency check, which is SUFFICIENT.** The substitution chain:

```
Step 1:  The corridor's content is the leading exponent p = α (registry: Level-1 leading-term).
Step 2:  p = −(d−1) is fixed by the orientability + dimension + regularity axioms
         (T1 §II.2; the dimension-spectrum pole order at a d-summable triple is axiom-level,
         NOT data-fit). This is FI: sub_term_R(Mellin)=sub_term_R(zeta)=0 at s=3 (Cauchy).
Step 3:  For an exponent fixed a priori by axioms, the EPISTEMIC ROLE of any finite-L fit
         is to CHECK CONSISTENCY, never to MEASURE p. A theorem-supplied quantity is
         not "extracted" by data, and it does not NEED to be — its warrant is the theorem.
Step 4:  lizzi's separability result says exactly this: the window holds p as INPUT and
         the (C₁/L) tail is p-independent. ⇒ the fit cannot MEASURE p. ⇒ but p does not
         REQUIRE measurement — it is PROVEN. The fit's R²=0.99988 + machine-precision
         reproduction of the independent sample 2.6926 is a CONSISTENCY CERTIFICATE of a
         PROVEN exponent against FROZEN FULL-physical data.
Conclusion: "the fit cannot pin p" is TRUE and IRRELEVANT to Layer-1's status.
            A PROVEN exponent that a frozen-cache fit is CONSISTENT with is FULL/PROVEN
            at Layer-1. The non-extractability is a fact about Layer-2 (the route is a
            consistency route, hence SCHEMATIC), NOT a demotion of Layer-1.
```

lizzi's §V.1 says "a quantity the fit holds C₁-independent and supplies as input is not a quantity the fit extracted." **Correct — and a quantity that is PROVEN does not need to be extracted.** Her own taxonomy (§V.1 closing): "what is FI [the exponent] was supplied as a theorem; what the fit measured [amplitude, correction] is scheme-dependent." That is the *exact* Layer-1/Layer-2 split: FI-PROVEN exponent at Layer-1, scheme-dependent route+amplitude at Layer-2. She has, again, derived (c). The separability result demotes the *route* to a consistency route (SCHEMATIC, Layer-2); it does not demote the *exponent* (FI-PROVEN, Layer-1). (b) would require demoting Layer-1 to "posit/consistency-confirmed," and the separability result gives no warrant for that — a PROVEN theorem's status is set by its proof, not by whether a downstream fit could have independently rediscovered it.

### IV.3 The Friedrich-Bär move (her §VI) — "extrapolated" vs "frozen-determined"

lizzi's §VI concedes the freezing and the ~10× margin, then argues "freezing the GENERATING SPECTRUM ≠ FULL-extracting the OBSERVABLE; the [35,100] window is *extrapolated* (the WP's word), not evaluated." I accept the word "extrapolated" and localize it precisely: what is extrapolated is the **signed local exponent `α(L)` into the window**, and the warrant for that extrapolation is (i) the frozen generating spectrum (no NEW sector perturbs `R_b(L)` — her conceded ~10× margin) AND (ii) the PROVEN leading exponent `−3`. The extrapolation is of a function whose *form* is theorem-fixed (`L^{−3}` leading) and whose *generating data* is frozen — it is not a free-floating extrapolation that could go elsewhere. So "extrapolated" correctly describes a Layer-2 ROUTE property (the value at L≥13 is read by analytic continuation of frozen data, not by diagonalization) — which is exactly why Layer-2 is SCHEMATIC. It does not touch Layer-1 (the exponent's PROVEN value). Once more: (c), with the SCHEMATIC class correctly attached to the route/extrapolation layer, not to the exponent.

---

## V. The convergent registry form — (c) with verdict-line / `LEVEL_CLASS_PIN` reconciliation

I converge on **(c) two-layer split**, and I specify the exact form so lizzi's T4 has a concrete target. The framework already has a canonical template for this — the **structural-orthogonal-companion dual-reading**, registry-PROVEN at the sibling slot §VII.AF.1.OP-PROJ (knowledge MCP: `permanent-results-registry.md`, *"Level-pin axis distinction: Reading A inhabits the SCHEMATIC level class (convergence-exponent F-image; `-SCHEMATIC` convention suffix + `tier_pin=TIER-2`); Reading B [inhabits FULL]"*; landed K=1 as `CF-S91-W7-CF-W9-4-A-IN-SESSION-VII-AF-1-OP-PROJ-STRUCTURAL-ORTHOGONAL-COMPANION-DUAL-READING`). §VII.AU.OP-PROJ is the SAME OP-PROJ lineage and the SAME SCHEMATIC-vs-FULL axis; the resolution form should match.

### V.1 Two rows, structural-orthogonal companions (NOT co-primary)

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3) and `registry-landing.md §"Operator-Projection Reading-A naming hygiene"`, the two layers are **structural-orthogonal companions**, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY (co-primary is FORBIDDEN across orthogonal axes). Concretely:

```
§VII.AU.OP-PROJ — Layer-1 (cohomology-class / exponent)   [status: FULL-RECOVERED]
   content : α = −(d−1) = −3, Level-1 leading-term, Cell I × substrate-distance-1 pole s=3
   warrant : registry-PROVEN; FI (sub_term_R(Mellin)=sub_term_R(zeta)=0 at s=3, Cauchy);
             regulator-invariant; L-independent; canonical-FULL since S91 W-5
   axis    : cohomology-class axis  (algebra-INVARIANT spectrum-only functional family)

§VII.AU.OP-PROJ — Layer-2 (evaluation-route provenance)   [status: SCHEMATIC-pending]
   content : the analytic-saturation NUMERICAL route reading α off as L→∞
             (SCHEMATIC two-pin convergence-exponent protocol; rho_FULL_CC_VII_AU_SAT_s3)
   warrant : NOT a live full-physical Mellin-Barnes extraction at L≥13 (infeasible per
             feasibility pre-check); the route is consistency-certified (R²=0.99988,
             sample rel_dev 5.94e-15) against frozen FULL-physical L≤12 cache
   axis    : Level / sourcing axis  (SCHEMATIC-vs-FULL; tier_pin=TIER-2)
   anchor structure : STRUCTURAL-ORTHOGONAL-COMPANION to Layer-1 (NOT co-primary)
```

### V.2 Verdict-line / `LEVEL_CLASS_PIN` reconciliation — made mutually consistent

The current verdict line (39, canonical) and registry status are dissonant ONLY under the single-tag reading. Under (c) they are consistent **without editing the verdict line's physics**:

- **The verdict line stays as is.** Line 39 carries `LEVEL_CLASS_PIN=SCHEMATIC tier_pin=TIER-2` and, in the SAME companion row (38/44), names *"the L^{−3} leading-term geometric envelope exponent −(d−1) at d=4 is the structural anchor."* That row is ALREADY a two-axis disclosure: SCHEMATIC on the route/Level axis, structural on the exponent axis. **This is (c) in verdict-line form.** No supersede needed; the verdict line was honest all along — it is the SINGLE registry status tag that was wrong, not the verdict line.
- **The registry status changes from a single `FULL-RECOVERED` to the two companion rows of §V.1.** The `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → FULL-RECOVERED` re-tag (housekeeping A9; `permanent-results-registry.md:18938,19289`) is RETAINED *as the Layer-1 status* (FULL-RECOVERED is correct for the exponent — and the verdict-line's "structural anchor" clause supports it) and is SUPPLEMENTED by the Layer-2 SCHEMATIC-pending companion row. The dissonance was: one FULL-RECOVERED status tag vs one SCHEMATIC verdict-line tag, read as predicating over the same object. (c) resolves it: they predicate over DIFFERENT axes (Layer-1 vs Layer-2), each gets its row, and the `LEVEL_CLASS_PIN=SCHEMATIC` verdict-line tag is the Layer-2 row's warrant.

So option (d) ("verdict-line and registry status must be made mutually consistent, one edited") is SATISFIED BY (c) without editing the verdict line: the registry side is what splits, and the verdict line is re-read as the Layer-2 SCHEMATIC warrant + Layer-1 structural-anchor clause it already contains. The registry edit itself is `mack-cosmic-bridge`'s sole-writer domain — T4 should produce the exact two-row text and route the write to mack, not write `permanent-results-registry.md` directly.

### V.3 What I concede is genuinely SCHEMATIC, stated honestly

To be unambiguous about the boundary (the spawn asked for this): **the live full-physical Mellin-Barnes evaluation of `R_b(L)` at L≥13 was not performed, is infeasible by the recursive-Casimir feasibility pre-check, and the asymptotic exponent was read by the SCHEMATIC analytic-saturation two-pin route, not by that pipeline.** That is a real, non-cosmetic SCHEMATIC fact, and it earns the Layer-2 SCHEMATIC-pending row in full. What I do NOT concede is that this SCHEMATIC route-fact demotes the *exponent's* PROVEN/FULL status at Layer-1 — and what I have shown (via the registry record, §II) is that there is no *distinct physical `c_continuum` observable* still unrecovered behind the SCHEMATIC tag; the residual is the ROUTE, not an observable. That is the difference between (c) (correct) and (b) (lossy projection that mislabels the route as an unrecovered observable).

---

## VI. Summary of T3 (Reading A, final)

**Conceded to lizzi (no reservation):**
1. The exponent-vs-observable distinction is real; a bare single `FULL-RECOVERED` tag over a SCHEMATIC-verdict-line slot is a status-layer class-conflation. **Bare (a) withdrawn.**
2. Orthogonality cuts both ways: my own `SCHEMATIC ⊥ STRUCTURAL` denies `STRUCTURAL-FULL(exponent) ⇒ FULL-RECOVERED(single-tag corridor)`. **Conceded as a clean refutation of bare (a).**
3. The S91 `CLASS=FULL` provenance is exactly as lizzi states (verified via knowledge MCP); W2-3 discharged the route-certification, not the exponent.
4. The Sage window-separability arithmetic is correct; the window cannot independently pin `p`.
5. The live high-L Mellin-Barnes extraction was not performed and is infeasible; the route is genuinely SCHEMATIC. Layer-2 SCHEMATIC-pending is earned in full.

**Held against (b), converged on (c):**
1. **The corridor's deferred object IS the Level-1 exponent (registry-PROVEN theorem text), not a distinct `c_continuum`.** "NUMERICAL" names the analytic-saturation route to the exponent, not a second physical number. lizzi's two-object ontology has no surviving third object that is both physical and unrecovered — the residual is ROUTE-provenance. (§II)
2. **(b) is a lossy projection, not a lossless contraction of (c).** It collapses two orthogonal axes (Layer-1 FULL, Layer-2 SCHEMATIC) onto one — the *same* axis-collapse error lizzi convicts (a) of, in the opposite direction. lizzi's own §III.3 orthogonality proof DEMANDS two rows. (§III)
3. **(b)'s "structural-posit" mislabels Layer-1.** The exponent is registry-PROVEN, not a posit; §(iv) read symmetrically forbids erasing PROVEN downward just as it forbids erasing SCHEMATIC upward. (§III.2)
4. **"The fit can't pin `p`" is true and irrelevant to Layer-1.** A theorem-supplied exponent does not require data-extraction; the fit's role is consistency-certification, which is sufficient for a structurally-fixed exponent. Non-extractability is a Layer-2 (route) fact, not a Layer-1 demotion. (§IV.2)

**Convergence**: **(c) two-layer split** — Layer-1 (cohomology-class / exponent) = **FULL-RECOVERED** (registry-PROVEN, FI, canonical-FULL since S91); Layer-2 (evaluation-route provenance) = **SCHEMATIC-pending** (`tier_pin=TIER-2`, analytic-saturation two-pin route, consistency-certified against frozen FULL-physical cache, NOT a live high-L extraction). The two rows are **structural-orthogonal companions** (NOT co-primary; the §VII.AF.1.OP-PROJ K=1 precedent is the template). Verdict-line 39 stays unedited — it ALREADY carries the Layer-2 SCHEMATIC warrant + the Layer-1 structural-anchor clause; the registry single-tag status is what splits into the two companion rows. This satisfies (d)'s reconciliation requirement without a verdict-line supersede.

The residual disagreement with lizzi has narrowed to one axis: she offers (b) as the economical single-row contraction; I show (b) is lossy because the two layers carry opposite statuses on an orthogonal axis. If lizzi's T4 accepts that a two-row structural-orthogonal-companion form (her stated floor (c)) is the registry-anatomy-faithful resolution, we are fully converged. I expect we are: her §IV named (c) as "the structurally richest correct status" and "registry-anatomy-faithful," and her §V.1/§VI.2 taxonomy ("FI exponent supplied as theorem; scheme-dependent route/amplitude fit") IS the Layer-1/Layer-2 split. The only thing I ask T4 to drop is the framing of (b) as a correct single-row contraction — it is not, by her own orthogonality theorem.

*(Final connes turn. lizzi writes the balanced JOINT VERDICT in T4.)*
