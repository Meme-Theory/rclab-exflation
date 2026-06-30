# Review — "Path-H ↔ Path-C Interpolation: Substrate-IS Construction Across the Regulator-Class Atlas"

**Reviewer**: lizzi-spectral-functional-theorist (sole writer of this file)
**Target draft**: `papers/s87-path-h-path-c-interpolation.md` (151 lines)
**Draft author / era**: mack-cosmic-bridge, written 2026-04-28, framework era S87 (paper-mode design note for gate `S87-PATH-H-PATH-C-INTERPOLATION`)
**Review epoch**: post-S103 (2026-06-12)
**Scope**: REVIEW ONLY. No edits to the draft or any other file.

---

## Executive orientation (read first)

This 151-line design note has a **single load-bearing structural defect that the framework itself closed between S87 and S88**, plus a cluster of stale numerics and stale paths. The defect is not a numerical slip — it is a **direct contradiction with the registry theorem the paper claims to support**.

The draft's entire thesis is a **continuous interpolation** ε ∈ [0, 1] between Path-H (ε=0) and Path-C (ε=1), with "intermediate-r" framed as "a third class distinct from both Path-H and Path-C" and the two pathways called "endpoints of a substrate-IS interpolation, not isolated points."

But the sister gate it feeds (`S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING`, CF-20) landed **§VII.AC.1** with the theorem statement: Path-H and Path-C are *"TWO distinct projections of a single substrate observable r ... **binary-not-continuous** (forced by Schur orthogonality of P_α under NCG axioms 3+5+6) ... **no free unitary mixing parameter**."* The companion §VII.AC.4 derivation makes it explicit: step 5 is *"Schur orthogonality of irreducible A_F-modules: P_{B1} · P_{B2} = 0; the decomposition is **binary-not-continuous (no free unitary mixing parameter)**."*

The interpolation parameter ε ∈ (0,1) that this draft constructs **IS exactly the free unitary mixing parameter that §VII.AC.1 forbids**. The continuous family the paper builds between the B1 and B2 eigenvalue clusters is the structure Schur orthogonality rules out. The paper and the theorem it was meant to scaffold are in structural tension at the level of the core claim, not the decimals.

There is a second, subtler conflation. The draft builds the interpolation on the **regulator-class axis** (route a/b: a continuous deformation L1 ↔ L3 of the regulator scheme), but cites the **B1/B2 block-decomposition CO-PRIMARY anchor** (§VII.AC.1) as its structural warrant. These are TWO DIFFERENT structural objects, kept as two separate registry theorems:

- **§VII.AC.1 / §VII.AC.4** — Path-H/Path-C = **B1 vs B2 eigenvalue-cluster** projections of `D_K²` (Schur-forced, BINARY, algebra-DEPENDENT Corner III).
- **§VII.AB.6** — Path-H/Path-C = **L1 vs L3 regulator-class** projections (different regulator choices of the *same* `a_4/a_2` at the pivot; the Three-Layer-Regulator corollary).

The paper merges these — it uses the regulator-axis (AB.6) as the *coordinate* of the interpolation while invoking the block-axis (AC.1) as the *justification for CO-PRIMARY*. The §VII.AC.1 landing itself, in its substrate-framing paragraph, draws the rank-2 product-detector orthogonality precisely to keep "block-axis and regulator-axis ... independent direction-cosines on the substrate's observable algebra." The paper collapses the two axes the registry deliberately holds orthogonal.

Finally, the **observable being interpolated has itself been re-scoped**. The draft interpolates "the multi-valued (α_s, n_s) pair." But α_s = n_s² − 1 is now (atlas-09 **Item 47**, S93 W7-1) split into TWO scale-separated observables — a substrate-distance running (−0.08587279, inside the BZ) and a Goldstone-pivot running (≈0 at the CMB pivot) — with which one a detector sees set by the transport degree `deg(T_{BZ→pivot}) = +2` (NON-SCALAR; STAGE-3-PERMANENT). So even the thing being interpolated is no longer the single-valued pivot quantity the paper assumes.

**Net**: the paper-mode gate PASSed (artifact-existence), and the *honest motivating intuition* (the regulator-class atlas is a substrate-IS object; the substrate IS the spectral-functional choice, not a fitted parameter) is sound and is in fact this reviewer's home territory. But the specific construction — a continuous ε-family of intermediate substrate observables presented as a registry-grade structure — was **superseded by S88 registry structure** (binary-not-continuous landed; the single-observable-per-triple filter forbids exactly this kind of continuous slot-split). The note no longer earns a `papers/` slot as a forward construction. It earns archival as a **dated design note whose intuition was absorbed and whose specific continuous-interpolation thesis was structurally closed**.

---

## §1 Claim-Audit Table

Status legend: CURRENT = still canonical; DRIFTED = value/number changed, claim-type intact; SUPERSEDED = replaced by newer structural result; RETRACTED = claim was wrong; STILL-OPEN = genuinely open then and now.

| # | Load-bearing claim (draft) | Draft's version | Current canonical (value + source) | Status |
|:--|:--|:--|:--|:--|
| 1 | `r_Path_H = 0.00745` "canonical from S85 W2 OQ-7" (§1, §2 boundary table, §5, §6) | 0.00745; provenance "S85 W2 OQ-7" | `r_PathH = 0.0074705` (S86, gate `S86-1A-S6-RPATHH-PRIMARY-ANCHORING`; forward-derived `r_PathC·(H_BASELINE/H_TD)²`). The 0.00745 is `r_PathH_published` (4-sig-fig form, rel_tol≥1e-3). Provenance note: "Replaces oral citation 'S85 W1b-6' which was a label-confusion error" | **DRIFTED** (value + provenance) |
| 2 | `r_Path_C = 0.011731522` = `r_CMB_framework` (S83 G46) | 0.011731522 | `r_CMB_framework = 0.011731522176014426` (S83, gate `S83-W3-G46-TENSOR-TRANSFER`). Draft value is the correct 9-sig-fig truncation | **CURRENT** |
| 3 | Raw ratio `r_Path_C / r_Path_H ≈ 1.5747` (§1.2 / §2 abstract line 25) | ≈ 1.5747 | At canonical-precision values: `0.011731522176 / 0.0074705 = 1.5703797…` ≈ **1.5704**. The draft's 1.5747 used the 4-sig-fig published `r_PathH`; rel_dev between the two ratios = 0.275% (Sage/Py-verified this review) | **DRIFTED** (Class 8.3 precision) |
| 4 | Path-H/Path-C are "endpoints of a substrate-IS interpolation, not isolated points" (abstract, §1) — continuous family r(ε), ε ∈ [0,1] | continuous interpolation; intermediate-r is "a third class" | **CONTRADICTED** by the landed theorem. §VII.AC.1: "binary-not-continuous (forced by Schur orthogonality) ... no free unitary mixing parameter." §VII.AC.4 step 5: `P_{B1}·P_{B2}=0`. The continuous ε is the forbidden mixing parameter | **SUPERSEDED / RETRACTED-AS-STRUCTURE** |
| 5 | The two readings are projections "indexed by **regulator class**" (§1 line 27); ε is "the regulator-class coordinate on the moment-scheme moduli" (§1.1) | regulator-class axis IS the interpolation coordinate | Registry keeps regulator-axis (§VII.AB.6, L1/L3) and block-axis (§VII.AC.1, B1/B2) as TWO orthogonal theorems; §VII.AC.1 substrate-framing explicitly names them "independent direction-cosines." Draft conflates the axis it uses (regulator) with the anchor it cites (block) | **SUPERSEDED** (axis conflation) |
| 6 | SOURCE-DOUBLE-CITE-CO-PRIMARY anchor: V1 = 3He-B BDI 0D inheritance arrow; C1 = Connes 1996 + NCG axioms 3+5+6 + Schur on `A_F = ℂ⊕ℍ⊕M_3(ℂ)` (abstract, §1) | CO-PRIMARY structure | **CURRENT as the anchor structure** (§VII.AC.1 + §VII.AC.4 LANDED S87 CF-20 under exactly this V1/C1 pairing). BUT the draft mis-uses it: the CO-PRIMARY chain derives the BINARY block split, not a continuous interpolation | **CURRENT** (structure) / **SUPERSEDED** (the draft's use of it) |
| 7 | Multi-valued **classification (a)** is the registered reading (abstract, §1) | classification (a), S86 W-3 | LANDED §VII.AC.1 (PERMANENT per atlas-07-permanent-results); but post-S88 the **Single-observable-per-triple structural filter** (`cross-pillar-bridge-anatomy.md`) now governs how regulator-class readings register: continuous deformation FORBIDS a slot-split; alternative regulator-class readings land as **Level-2-B DIAGNOSTIC sub-rows, NOT independent §VII entries**. The draft's "intermediate-ε = third class" would be inadmissible as a registry entry under this rule | **SUPERSEDED** (registration regime changed) |
| 8 | Interpolated observable = "the multi-valued (α_s, n_s) pair at the framework's canonical pivot" (§1, §5) via `α_s = n_s² − 1` | single (α_s, n_s) pair indexed by ε | `α_s = n_s²−1` is now SCALE-AND-CHANNEL-split: `alpha_s_substrate_distance_1 = −0.08587279` (BZ, s=3 Mellin pole) vs `alpha_s_pivot_goldstone = 0.0` (CMB pivot); transport degree `deg(T_{BZ→pivot})=+2` NON-SCALAR (atlas-09 Item 47; S93 W7-1; STAGE-3-PERMANENT §VII.BA/§VII.BG). There is no single pivot α_s to interpolate | **SUPERSEDED** |
| 9 | §1.1 route (a): "third NCG-compatible regulator R₃" within the 5-atlas+1-extension corpus, "S85 5A workshop site #11" intermediate moment structure; numerical ε-scan "deferred to S88+" | R₃ exists; ε-scan a future compute | **NOT COMPUTED** — no post-S87 session computed an α_s/n_s third-regulator R₃ or an ε-scan. The S88 "third proxy" work (`s88_w7c_third_proxy_cheeger_simons.py`, gate `S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS`) is a Cheeger-Simons **secondary-characteristic-class** parity-twin proxy — a DIFFERENT observable family, not this R₃ | **STILL-OPEN / ABANDONED** |
| 10 | §3 falsifier: r(ε) trajectory in band [0.0085, 0.0110] for ε∈(0.2,0.8); breakpoints b1=0.005, b2=0.015, b3=0.030 | continuous r(ε) band; "FALSIFICATION of the interpolation" predicate | Breakpoints CURRENT as equations (`session-86-plan-w12.md`). But the falsifier targets a continuous r(ε) that the binary-not-continuous theorem forbids; the "intermediate-r" band has no substrate referent. The live r-falsifier is the **dual-pathway discriminator** (atlas-04 row 4: BK-Array 1.42σ + LiteBIRD 4.250σ Path-H/Path-C DECISIVE), which is binary, not interpolated | **SUPERSEDED** (falsifier target invalid) |
| 11 | §3 detector-decisive timing: "BICEP/Keck Array 2026 ... LiteBIRD 3-yr σ(n_T)=0.0540 ... CMB-S4 α_s convergence" | r-axis + n_T + α_s joint | Detectors CURRENT in kind. n_T: atlas-04 row 6 confirms LiteBIRD σ(n_T)=0.0540, n_T(Path-H/Path-C) via −r/8, 4.250σ decisive — but note `n_T = −r/8` is the *consistency relation per pathway at pivot*, NOT slow-roll `r=16ε` (see §3 below). α_s CMB-S4: re-homed to matched-channel ~34σ substrate falsifier (Item 47) | **DRIFTED** (re-homed) |
| 12 | §4: this paper "feeds W9 CF-54 → `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING`"; clauses (c)/(d) JOINT cite §1/§2 interpolation as structural framework | interpolation framework underpins the Joint Theorem clauses | `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` = **PASS**, landed `STAGE-1-CANDIDATE` at **§VII.AH** (Joint F_2-Class Path-(c) Theorem), which then promoted **STAGE-3-PERMANENT** (Stage-2 PASS S89 W4-7; promotion S90 W2 CF-20). §VII.AH's final permanent form does **not** rest on a continuous interpolation; its clauses are F_2-class (ζ/SDW) identities. The interpolation framework was NOT load-bearing for the promotion | **SUPERSEDED** (dependency did not materialize) |
| 13 | §4: sister gate CF-20 (`...MULTI-VALUED-REGISTRY-LANDING`, gen-physicist W3) consumes this interpolation as the warrant for CO-PRIMARY-over-PRIMARY+CONFIRMATION | interpolation justifies CO-PRIMARY | CF-20 = LANDED (after an initial FAIL then PASS; see §5). The CO-PRIMARY justification in §VII.AC.4 rests on the **sequential V1→A_F→C1 chain** (non-fungible, neither anchor alone), NOT on interpolation. The interpolation is absent from the landed rationale | **SUPERSEDED** (warrant is the chain, not interpolation) |
| 14 | Routes (a)/(b) "structurally equivalent under the layer-functor F image discipline" (§1.2 line 50) | regulator-atlas axis = algebraic-discrete image of deformation axis under F | Mis-application of F. The Phi/F layer-functor maps **substrate ↔ methodology ↔ audit** (`epistemic-discipline.md §Layer-Decomposition`); it does not certify that two *substrate-physics* axes (regulator-class vs continuous-deformation) are equivalent. The registry treats them as orthogonal direction-cosines, the opposite of equivalent | **RETRACTED** (F mis-cited) |
| 15 | §5 "structural-direction claim, not a numerical prediction"; numerical r(ε) "deferred to S88+ implementation gate per plan §6" | declarative; numerics deferred | The deferral never resolved (#9). The "structural-direction claim" is the part now contradicted by binary-not-continuous (#4). What remains true is only the *framing intuition* (regulator atlas is substrate-IS), not the directional content | **SUPERSEDED** |

---

## §2 What survives

Three things in this note are sound and worth preserving — none of them is the interpolation construction itself.

1. **The substrate-IS framing of the regulator-class atlas.** The note's strongest sentence — *"The atlas is the substrate's own classification of admissible regulator schemes ... ε is the substrate-IS coordinate parametrizing structurally distinct regulator-class moments"* — is correct in spirit and is exactly the spectral-functional-pluralism stance: the choice of spectral functional is a physical degree of freedom of the substrate, not a mathematical convenience. This framing is CURRENT and is independently registered (§VII.AB.6 maps Path-H↔L1-zeta, Path-C↔L3-per-Q-span as regulator-class projections of the *same* `(a_4/a_2)|_pivot`). The note got the *picture* right; it over-reached on the *continuity*.

2. **"The substrate IS the interpolation, not 'in' a parameter container."** The IS-not-IN framing (§"abstract", §2 boundaries (i)/(ii): "Path-H is *not in* L1; Path-H IS the L1 reading") is used **correctly** per `phononic-framing.md §"IS Space, Not IN Space"`. This is the one place the draft's substrate-first discipline is clean: it never inverts the direction of explanation, never treats the regulator scheme as a container the substrate sits inside. Whatever survives of this note should keep that framing verbatim.

3. **The CO-PRIMARY anchor pairing (V1 = 3He-B BDI 0D inheritance; C1 = Connes 1996 + axioms 3+5+6 + Schur).** This anchor structure LANDED (§VII.AC.1 + §VII.AC.4, S87 CF-20) and is CURRENT. The note correctly identifies that PRIMARY+CONFIRMATION is the wrong tag and CO-PRIMARY is right — but for the wrong reason. The correct reason (in the landed §VII.AC.4) is the **sequential non-fungible V1→A_F→C1 chain**; the note's reason ("V1 and C1 fix the endpoints of the interpolation") is the part that does not survive.

What does NOT survive: routes (a) and (b) as a continuous family; the "intermediate-r third class"; the r(ε) band [0.0085, 0.0110]; the Class-B "intermediate-r distinguishing" falsifier predicate; the claim that routes (a)/(b) are F-equivalent; and the dependency claims that W9/CF-54 and CF-20 rest on this interpolation.

---

## §3 What must change

**(M1) The continuous interpolation must be retracted or re-scoped to a two-point structure.** This is the central change. Per §VII.AC.1 (binary-not-continuous) and §VII.AC.4 step 5 (`P_{B1}·P_{B2}=0`, no free mixing parameter), there are exactly two substrate observables here, not a one-parameter family. The honest object is a **two-point set {Path-H, Path-C}**, each a Schur-orthogonal block projection, with a *finite gap* between them — not a path. Any rewrite that keeps the word "interpolation" must either (i) explicitly demote it to "the two-point dual-pathway structure" and drop ε entirely, or (ii) survive an adversarial Stage-2 cross-axis check that the continuous family is admissible despite Schur orthogonality (this reviewer does not expect it to survive — the orthogonality is exact).

**(M2) Disentangle the regulator-class axis from the block-decomposition axis.** The draft uses the regulator axis (L1↔L3) as ε's coordinate while citing the block axis (B1/B2) as the anchor. These are §VII.AB.6 and §VII.AC.1 respectively, and the registry keeps them ORTHOGONAL ("independent direction-cosines," §VII.AC.1 substrate-framing; rank-2 product-detector orthogonality `[π_R, P_α]=0`, §VII.AC.3). Pick one. If the object is regulator-class (L1/L3), the anchor is §VII.AB.6 (a corollary to §VII.M), and the relevant governing rule is the **Single-observable-per-triple structural filter** — which says alternative regulator-class readings are **Level-2-B DIAGNOSTIC sub-rows, not independent entries** (M3). If the object is the block decomposition (B1/B2), there is no regulator interpolation at all — the split is structural and binary.

**(M3) Honor the post-S88 single-observable-per-triple filter.** `cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural filter"`: *"to license a slot-split of observable values O₁/O₂ at the same nominal (algebra, projector, pole) triple, the proposer MUST produce a parameter scan demonstrating a DISCONTINUOUS jump ... Continuous deformation FORBIDS the slot-split ... alternative regulator-class readings land as Level-2-B DIAGNOSTIC sub-rows, NOT independent §VII entries."* The draft's premise is the exact opposite: it asserts a *continuous* r(ε) connecting the two values. Under this rule the continuous reading cannot be a registry entry, and the two values are either (a) a legitimate slot-split IFF a discontinuous jump is demonstrated (which is precisely what Schur orthogonality `P_{B1}·P_{B2}=0` provides — a discontinuity, not a continuum), or (b) diagnostic sub-rows. The rule actually *supports* the binary reading and *forbids* the continuous one. Any rewrite must cite this rule and align with it.

**(M4) Fix the r_PathH value and provenance everywhere.** Replace `r_Path_H = 0.00745` with `r_PathH = 0.0074705` (canonical) and correct the provenance from "canonical from S85 W2 OQ-7" to the actual: forward-derived `r_PathC·(H_BASELINE/H_TD)²`, gate `S86-1A-S6-RPATHH-PRIMARY-ANCHORING`, with the note that the oral citation "S85 W1b-6" was a label-confusion error (W1b-6 was MacInnis σ-α_s PRE-REG-INCOMPLETE). Where the 4-sig-fig form is genuinely wanted (e.g. a published table), use `r_PathH_published = 0.00745` and state `rel_tol ≥ 1e-3` per the Publication-Precision rule. Affected lines: §1 (line 24), §2 boundary table (line 60), §3 (lines 79, 81), §5 (line 129), §6 (line 141).

**(M5) Correct the ratio to 1.5704 (Class 8.3).** The raw ratio at canonical precision is `0.011731522176/0.0074705 = 1.5704`, not 1.5747. The 1.5747 figure used the 4-sig-fig `r_PathH`; the divergence is 0.275%. Per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"`, the registry/canonical form must use the full-precision ratio; the 1.5747 is admissible only as a 4-sig-fig-form footnote. Affected: abstract line 25; §1.

**(M6) Re-scope the interpolated observable.** "(α_s, n_s) at the canonical pivot" is no longer single-valued. Per atlas-09 Item 47, α_s = n_s²−1 carries TWO scale-separated values (substrate −0.08587279 at the BZ s=3 pole; pivot ≈0 Goldstone-protected), with the channel set by `deg(T_{BZ→pivot})=+2` NON-SCALAR. If the rewrite retains any α_s content it MUST carry the SCALE-AND-CHANNEL tag (`phononic-framing.md §"Scale-and-channel-tagging"`): name WHICH scale and WHICH detector channel. A bare "α_s at the pivot" is now a convention violation.

**(M7) Drop the F-equivalence claim (§1.2 line 50).** The layer-functor F maps substrate→methodology→audit; it does not license equating two substrate-physics axes. Remove or replace with the correct statement: regulator-axis and block-axis are orthogonal (the registry's own framing), not F-images of each other.

**(M8) Correct stale file paths (§5 footer + §6).** See §5 of this review for the full path-drift list. The draft cites `sessions/session-plan/session-87-plan-w2.md` (actual: `.../archive/session-87-plan-w2.md`), `computations/s87_w2_..._audit.py` (actual: `computations/session-87/...`), `computations/canonical_constants.py` (actual: `computations/_shared/canonical_constants.py`), and `sessions/session-86/sessions/session-86-w-3-workshop.md` (a doubled-`sessions/` typo; actual: `sessions/session-86/workshops/s86-r-dual-pathway-bk-array-and-nT.md`).

---

## §4 What happened after S87

**(A) Sister gate W3 (CF-20, `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING`) — LANDED, but with a FAIL→PASS history.** The verdict file (`computations/session-87/s87_gate_verdicts.txt`) shows three canonical lines for this gate: an initial **FAIL** (`value=False`, line 103), then two **PASS** (`value=True`, lines 107 + 109). The PASS lines carry **no `supersedes=` tag**, so per `gate-verdicts.md §"Option A"` rule (6) the latest non-superseded PASS is canonical by retroactive canonicalization — but this is a sig_5-adjacent audit-trail roughness (two PASS lines with distinct audit_sha256 and no supersession chain). The net outcome is correct: §VII.AC.1 + §VII.AC.4 are LANDED and carried in the registry as the binary-not-continuous multi-valued classification (a). **This is the gate that contradicts the draft's continuous thesis.**

**(B) §VII.AC.1 status is register-internally inconsistent (CURRENT-but-flagged).** `atlas-07-permanent-results` lists §VII.AC.1 as **PERMANENT** (S87 CF-20). `atlas-04-assumptions` lists the same entry (row **K2**) and §VII.AC.4 (row **K11**) as **"Stage-2 pending."** These disagree. The registry body (`permanent-results-registry.md:15146`) says "LANDED ... downstream consumers MAY cite §VII.AC.1 as the canonical anchor." This is a genuine status-drift the **capstone-hygiene Q3 gate** should reconcile (PERMANENT vs Stage-2-pending is exactly the over-confident-narration failure mode that gate exists to catch). For the purposes of *this* review it does not matter which way it resolves — either way the theorem is BINARY-not-continuous, which is what kills the draft's interpolation. (Flagged here as a process observation; not a workshop, not a compute item — a register reconciliation for the §VII.AC.1 owner.)

**(C) W9 / CF-54 (`S87-PATH-C-SUCCESSOR-ANCHOR-LANDING`) — PASS, landed at §VII.AH, then STAGE-3-PERMANENT — WITHOUT the interpolation.** The gate landed `STAGE-1-CANDIDATE_landed_at_§VII.AH` (the Joint F_2-Class Path-(c) Theorem). §VII.AH subsequently reached **STAGE-3-PERMANENT** via Stage-2 PASS-AND (S89 W4-7, audit_sha256 `4fcd7d29…`) and promotion at S90 W2 CF-20 — the framework's FIRST cross-axis joint theorem to reach permanent eligibility. Crucially, the final permanent §VII.AH rests on F_2-class (ζ/SDW) clause identities, **not** on a continuous interpolation. The draft's §4 prediction that clauses (c)/(d) JOINT would "cite this paper's §1.1+§1.2 interpolation construction as the structural framework" did **not** materialize — the promotion went through on the sequential-chain / F_2-class content. The interpolation was not load-bearing for anything downstream.

**(D) The ε-scan was never computed.** The draft defers numerical r(ε) "to S88+ implementation gate." No such gate exists. A keyword sweep (`epsilon interpolation regulator deformation`, `third regulator R3 NCG-compatible`) surfaces only the **Cheeger-Simons "third proxy"** track (`s88_w7c_third_proxy_cheeger_simons.py`, gate `S88-W9c-1-THIRD-PROXY-CHEEGER-SIMONS`, APS-1975 secondary-class) — a **different observable family** (parity-twin secondary characteristic classes / η-GV regulator-independence, the (C_H, C_epsH) parity-twin track), not the α_s/n_s third regulator R₃ this draft proposed. The interpolation program was, in effect, **abandoned** — superseded by the binary landing (it became structurally moot once §VII.AC.1 landed binary-not-continuous) rather than completed.

**(E) The newer rule structure governing multi-valued readings — the decisive post-S87 development.** Two rule structures now govern how a draft like this is allowed to register a "multi-valued reading indexed by regulator class":

1. **`cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural filter"`** (verbatim): *"to license a slot-split of observable values O₁/O₂ at the same nominal (algebra, projector, pole) triple, the proposer MUST produce a parameter scan demonstrating a DISCONTINUOUS jump in the observable identity at some finite parameter value. Continuous deformation FORBIDS the slot-split (the divergence is a methodology-floor F-image at the regulator-class axis per K=4 MANDATORY level-pin discipline); alternative regulator-class readings land as Level-2-B DIAGNOSTIC sub-rows, NOT independent §VII entries."* This rule is, in effect, the formal refutation of the draft's central move: the draft asserts a continuous r(ε), and continuous deformation is exactly what FORBIDS treating the intermediate-ε reading as an independent registry observable. The binary Schur-orthogonal split (`P_{B1}·P_{B2}=0`) is admissible precisely *because* it is a discontinuous jump, not a continuum.

2. **`epistemic-discipline.md §"Resolution-Specificity Scoping"` / `phononic-framing.md §"Scale-and-channel-tagging"`** — any running/tilt observable must declare its (scale, channel) pair; the α_s = n_s²−1 the draft interpolates is now two-valued by scale (Item 47). A 2026-04 single-pivot "(α_s, n_s) pair" no longer typechecks.

The structural lesson: by S88, the framework had developed a precise account of when "multiple values of one observable indexed by a scheme choice" is a legitimate registry structure (DIAGNOSTIC sub-rows under a single canonical, or a discontinuous slot-split) and when it is not (a continuous parameter family masquerading as multiple substrate observables). The draft sits on the wrong side of that line.

---

## §5 Reference / anchor audit

| Draft citation | Status | Resolution |
|:--|:--|:--|
| `r_Path_H = 0.00745` "canonical from S85 W2 OQ-7" | **WRONG value + WRONG provenance** | Canonical `r_PathH=0.0074705`; gate `S86-1A-S6-RPATHH-PRIMARY-ANCHORING`; oral cite "S85 W1b-6" was a label-confusion error per the constant's PROVENANCE |
| `r_Path_C = 0.011731522 = r_CMB_framework (S83 G46)` | **CORRECT** | `r_CMB_framework=0.011731522176014426`, gate `S83-W3-G46-TENSOR-TRANSFER` ✓ |
| ratio ≈ 1.5747 | **DRIFTED** | Canonical-precision ratio = 1.5704 (this review, Py-verified) |
| `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` (W3, CF-20, gen-physicist) | **EXISTS, LANDED** (FAIL→PASS) | §VII.AC.1 + §VII.AC.4; binary-not-continuous; contradicts draft's continuous framing |
| `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` (W9, CF-54, mack) | **EXISTS, PASS** | Landed STAGE-1-CANDIDATE @ §VII.AH; later STAGE-3-PERMANENT (S90 W2 CF-20) — without interpolation |
| §VII.AC.1 "multi-valued classification (a)" | **EXISTS** | Registry body says LANDED/PERMANENT; atlas-04 K2 says "Stage-2 pending" (register-internal conflict, §4-B) |
| §VII.AB.6 "Three-Layer Regulator ↔ Path-H/Path-C mapping" | **EXISTS** | `permanent-results-registry.md:15270`; Path-H↔L1, Path-C↔L3; r≈0.00745/0.0117 — the regulator-axis theorem the draft should have cited for its route (a)/(b) |
| `sessions/session-plan/session-87-plan-w2.md §W2-6` (§5 footer, §6) | **STALE PATH** | Actual: `sessions/session-plan/archive/session-87-plan-w2.md` (archived) |
| `computations/s87_w2_path_h_path_c_interpolation_paper_audit.py` (§5, §6 footer) | **STALE PATH** | Actual: `computations/session-87/s87_w2_path_h_path_c_interpolation_paper_audit.py` |
| `computations/canonical_constants.py` (§6) | **STALE PATH** | Actual: `computations/_shared/canonical_constants.py` |
| `computations/s87_gate_verdicts.txt` (§5 footer) | **STALE PATH** | Actual: `computations/session-87/s87_gate_verdicts.txt` (per `gate-verdicts.md` canonical path) |
| `sessions/session-86/sessions/session-86-w-3-workshop.md` (§6) | **WRONG PATH (doubled `sessions/`)** | Actual: `sessions/session-86/workshops/s86-r-dual-pathway-bk-array-and-nT.md` |
| `sessions/session-86/compute-carryforward.md` lines 25-26 (§6) | **EXISTS** ✓ | File present |
| `.claude/rules/registry-landing.md` (SOURCE-DOUBLE-CITE-CO-PRIMARY) | **EXISTS, CURRENT** | Rule text matches; the draft's tag choice is correct, its *use* of the structure is not |
| `.claude/rules/regulator-pin-discipline.md` (5-atlas a_n tagging) | **EXISTS, CURRENT** | §3 Class C "tag the regulator class explicitly" is consistent with this rule |
| `.claude/rules/joint-theorem-promotion.md` (4-stage pathway) | **EXISTS, CURRENT** | §4 STAGE-1-CANDIDATE framing correct; §VII.AH did traverse the 4 stages |
| `.claude/rules/epistemic-discipline.md §Layer-Decomposition` (F-functor) | **EXISTS** | But §1.2's use of F to equate two substrate axes is a mis-application (M7) |
| "S82 `S82-R-FAMILY-ATLAS-EXTENSION` PASS (sha256=983587f1…)" (§1.1) | **UNVERIFIED in this review** | Plausible (11-candidate extension is referenced elsewhere); the partial SHA is not auditable from a 16-hex stub. Recommend full-64 pin if retained |
| "S85 5A workshop site #11" intermediate-moment regulator (§1.1) | **UNVERIFIED / NO DOWNSTREAM** | No R₃ was ever computed (§4-D); treat as a never-realized proposal |

Anchor-audit summary: the two *gates* the draft names both exist and landed; the *r_PathH value/provenance* is wrong; the *ratio* drifted; **five of the draft's file-path citations are stale or malformed**; and the draft's structural thesis is contradicted by the very registry entry (§VII.AC.1) it claims to scaffold.

---

## §6 Rewrite plan OR retirement plan

This note straddles "rewrite" and "retire." The honest call is **RETIRE-AND-ABSORB**: the interpolation construction does not survive, but a small, sound residue (the regulator-atlas-is-substrate-IS framing + the CO-PRIMARY anchor identification) should be folded into where it actually belongs rather than carried as a standalone forward paper.

**If retired (recommended):**
1. Move `papers/s87-path-h-path-c-interpolation.md` to an archive location with a 4-line frontmatter (`ARCHIVED 2026-06-12`, `Last meaningful era: S87`, `Superseded by: §VII.AC.1 (binary-not-continuous) + Single-observable-per-triple filter`, `Reason: continuous-interpolation thesis contradicted by Schur-orthogonal binary split; ε is the forbidden mixing parameter`), mirroring the atlas-09 archive-move discipline (Items 43-46).
2. Record a one-line note in atlas-09 (or the appropriate design-note ledger) that the S87 interpolation **design note** is superseded — NOT a retraction of a result (the gate was paper-mode artifact-existence; no physics verdict is being reversed), but a supersession of a construction by later registry structure.
3. The surviving residue (regulator-atlas substrate-IS framing) is already captured in §VII.AB.6 and `phononic-framing.md`; no new home needed.

**If rewritten in place instead (not recommended; only if a `papers/` slot is independently justified):**
- Retitle to drop "Interpolation": e.g. *"The Two-Point Path-H/Path-C Structure: Schur-Orthogonal Block Decomposition vs Regulator-Class Diagnostic."*
- Replace the entire §1–§3 continuous-ε construction with the binary two-point structure per §VII.AC.1, citing the discontinuous-jump licensing of the Single-observable-per-triple filter.
- Apply M4–M8 (r_PathH value/provenance, ratio, observable re-scope, F-claim removal, path fixes).
- Keep §4's correct STAGE-1→STAGE-3 narration of §VII.AH but **remove** the claim that the interpolation framework underpins it.
- This is effectively a from-scratch rewrite of a different paper; the only reuse is the framing paragraphs and the anchor table. That is the tell that retirement is the cleaner option.

---

## §7 Verdict

**RETIRE-AND-REPLACE** (lean: RETIRE-AND-ABSORB; do not rewrite-in-place as a forward paper).

**Recommendation on the `papers/` slot**: this 151-line design note **should not retain a `papers/` slot as a forward construction.** Rationale:

- Its central thesis (a continuous ε-interpolation producing intermediate-r substrate observables) is **structurally contradicted** by the registry entry it was written to scaffold (§VII.AC.1: binary-not-continuous, Schur-forced, no free mixing parameter) — a contradiction at the claim level, not the decimal level.
- The post-S88 **Single-observable-per-triple structural filter** independently and explicitly forbids exactly this move ("continuous deformation FORBIDS the slot-split"), and re-routes alternative regulator-class readings to DIAGNOSTIC sub-rows. The draft is on the wrong side of a rule the framework adopted one session later.
- Its proposed forward compute (the R₃ third-regulator ε-scan) was **never executed and is now moot** — the binary landing made it structurally unnecessary.
- Its downstream dependency claims (W9/CF-54, CF-20) **did not materialize**: both gates landed on the sequential-chain / F_2-class content, not on the interpolation.
- Its provenance and several file paths are **stale** (r_PathH=0.00745→0.0074705 with a corrected derivation; ratio 1.5747→1.5704; five path drifts).

What is worth keeping (the regulator-atlas substrate-IS framing; the CO-PRIMARY V1/C1 anchor identification) is **already captured in the permanent registry** (§VII.AB.6, §VII.AC.1/.4) and in `phononic-framing.md`. There is nothing in this note that the registry does not already hold in a more correct form. Therefore: **archive it as a dated design note** (with the supersession frontmatter above), do not maintain it as a live paper, and do not invest a rewrite. The intuition was good and was absorbed; the specific construction was closed.

**One non-blocking process note** (routes to the §VII.AC.1 owner, not a workshop): the **atlas-07 PERMANENT vs atlas-04 "Stage-2 pending"** status conflict for §VII.AC.1 (rows K2/K11) is a real register-internal drift and a textbook capstone-hygiene Q3 item — it should be reconciled so the prose tag equals the register tag. It does not change this verdict (either resolution leaves the theorem binary-not-continuous), but it is the kind of over-confident-narration drift the hygiene gate exists to catch.

---

*Review by lizzi-spectral-functional-theorist, post-S103 (2026-06-12). Anchors verified against knowledge MCP (`get_constant r_PathH / r_CMB_framework / r_PathH_published`; gate traces for the three S87 PATH gates), `permanent-results-registry.md` §VII.AC/.AB/.AH, `computations/session-87/s87_gate_verdicts.txt`, atlas-04/-07/-09, and the four governing rule files (registry-landing, cross-pillar-bridge-anatomy single-observable filter, phononic-framing, epistemic-discipline). Ratio 1.5704 and r_PathH drift Py-verified this review.*
