# WS-S112-3 CCRESID — R3 Structural Verdict (open)

**Workshop:** WS-S112-3 CCRESID (Session 113 EVOI-frontier campaign)
**Round-files:** `volovik-r1.md`, `lizzi-r1.md`, `volovik-r2.md`, `lizzi-r2.md` (all on disk, all read)
**Verdict author:** volovik-superfluid-universe-theorist (R3 convergence, written NEUTRALLY — this verdict does NOT favor the Reading-A pole the author held in R1/R2; where the physics favors Reading B, it says so).

**Adjudication question (verbatim from the schedule):** Is the residual-3% CC a higher-order effacement effect (with a pre-registrable closure gate) or a genuine a₀ residual? Is Q29 (BBN-epoch) independent or coupled?

**One-line verdict:** The two readings converged onto a clean two-part structure — **Reading A wins the CHANNEL sub-question** (the residual is a q-departure / Gibbs–Duhem object, NOT an a₀-magnitude offset; lizzi conceded this in R2), and **Reading B wins the CLOSABILITY sub-question** (the proposed closure is the S43 `ρ_m²/χ_q` route, requiring a 118.7-OOM run-down of an intensive, spectrum-fixed compressibility against a settled τ-nearly-constant argument; no working closure normalization was exhibited). The physics forces a **SYNTHESIS resolving to a CONDITIONAL standing-limitation verdict** with a registered falsifier. **Q29 (BBN) is INDEPENDENT in epoch but DIAGNOSTIC of the shared q-expansion**, and as such bears against closability.

---

## 1. Each agent's FINAL lean (from R2, stated faithfully)

### volovik (Reading-A pole) — final lean: a SPLIT
- **Channel of the present residual — firm Reading A (~0.80).** The residual is a q-channel / Gibbs–Duhem object (Layer 2 of the C10 cell), NOT an a₀ mode-count object. Argument: scheme-invariance is necessary-not-sufficient (the tracking law `α_V M_Pl²H²` contains no a_n moment, so a q-channel ratio is *also* scheme-invariant); the discriminator is `Ω_m`-dependence, which the a₀ mode-count cannot carry.
- **Whether the mechanism CLOSES the CC residual — reversed to Reading B (~0.70).** Conceded in R2 §3.2: the leading coefficient `α_V` is over-constrained across epochs (BBN-relief value undershoots z=0 by ~46%; z=0 value over-produces BBN by 2.06×). A second-order q-residual does not rescue a *leading-order* conflict. Explicitly retracted the R1 implication that closing the present residual closes the CC problem.
- **Q29:** independent as a *term* (different order), but coupled to present closure *through the shared leading coefficient* `α_V`.
- **Self-correction on record:** the R1 `Ω_m²` "fingerprint" was over-sold; a PASS of the proposed gate is *channel-identification*, not "residual closed."

### lizzi (Reading-B pole) — final lean: Reading B, ~0.75, scope-refined
- **Channel location — concedes Reading A (~0.85 on this sub-point).** R2 §1: "volovik wins the channel-location sub-question: the residual is a q-departure object, not an a₀-magnitude offset." Withdrew the implication that a₀-orthogonality alone settles closability.
- **Closability — Reading B firms to ~0.78.** Three R2 arguments: (i) the `ρ_m²/χ_q` mechanism is *verbatim* the S43 A.3.1 dead end, needing a 118.7-OOM χ_q run-down against the τ-nearly-constant (`χ_q ~ S_fold`, ΔS/S=2.2%) structural argument; (ii) the `Ω_m²` fingerprint is a two-parameter fit to one datum with zero discriminating power; (iii) the **order-of-expansion trap** — BBN is the *leading* term of the *same* `ρ_vac(q)` expansion and overshoots by 2.06×, so the *next-order* term cannot be trusted to 3%.
- **Q29:** independent in epoch, but **diagnostic** of the q-expansion's reliability — bears against closability more than volovik allows.
- **Concession trigger NOT met:** volovik exhibited a *channel* + an *uncomputed, structurally-adverse normalization*, not a *demonstrated* higher-order closure term.

**Convergence achieved:** Both agents END agreeing on (a) the channel (q-departure, Reading A), (b) that the dispute reduces to whether `χ_q(a)` runs, (c) that Q29 is independent-in-epoch. They split only on the *force* of Q29 and the *closability* prior.

---

## 2. The crux the disagreement turned on

> **Does the q-channel compressibility `χ_q = d²ε/dq²` run by ~119 OOM between the fold and today, or is it τ-nearly-constant / fold-frozen?**

This is the single point both agents independently identified as decisive (volovik R2 §"crux"; lizzi R2 §ii). It is the ONLY remaining disagreement after the channel was conceded. The numbers (Sage-QQ exact, R3 re-verified):

```
χ_q(fold)            = 300,338 M_KK⁴ = 9.148e+72 GeV⁴    (TWOFLUID-W-43-V2, S43)
χ_q(today) NEEDED    = 1.780e−46 GeV⁴                     (for ρ_m,today²/χ_q = 0.032·ρ_obs)
RUN-DOWN required    = 118.7 OOM
```

- **If `χ_q` runs the 118.7 OOM** → the present residual's magnitude (not just its scaling) is reproduced by the second-order q-term → Reading A's closure is real (and only the separate BBN leading-coefficient limitation stands).
- **If `χ_q` is fold-frozen** (S43: `χ_q ~ S_fold`, ΔS/S = 2.2% τ-spread; S99 "the dead end has a normal vector" PROVEN on this corridor) → the magnitude cannot match, the `Ω_m²` shape-match is coincidental, and the residual is a standing limitation even on channel-internal grounds → Reading B.

The crux is a **computable substrate quantity** that has not been computed: the `χ_q(a)` scaling. S43 explicitly left it "a computable quantity that has NOT been computed" (`s43_cc_113_workshop.md:489`), while arguing structurally that it points the wrong way.

---

## 3. STRUCTURAL VERDICT — what the physics ACTUALLY FORCES

**VERDICT: SYNTHESIS → CONDITIONAL STANDING-LIMITATION (Reading B holds the workshop's literal object; Reading A holds the channel sub-result).**

The workshop's literal object — "is the residual-3% a *closable* higher-order effacement effect or a *genuine standing limitation*?" — resolves to **standing limitation, conditional on the S43 χ_q-nearly-constant argument**, for three first-principles reasons, with the channel-win for Reading A preserved as a sub-result:

### 3.1 Reading A's channel claim is CORRECT and survives (first-principles)
The residual is a q-departure / Gibbs–Duhem object, not an a₀-magnitude offset. First-principles reason: the a₀ magnitude `ζ_{D_K}(0) = 6440` does **not gravitate at equilibrium** (Volovik Paper 04 §IV: `ρ_vac = ε − Σμ_a N_a = 0`, trans-Planckian/sub-Planckian cancellation); what gravitates is `ρ_vac = ε(q) − q dε/dq`, a *different functional of the spectrum* than the bare a₀ count. The Spectral-Moment Decoupling Theorem (S75 W2-E) walls off the a₀ *magnitude*, not a ratio of q-thermodynamic quantities — that ratio carries no a_n moment. lizzi conceded this explicitly in R2 §1 (the table distinguishing the a₀-magnitude row from the q-departure row). **So Reading B's R1 framing ("genuine a₀ spectral-moment residual the effacement cannot absorb") is mislocated: the residual is not in the a₀-magnitude channel, and a₀-orthogonality does not protect it.** This sub-result is settled FOR Reading A.

### 3.2 But channel-location does NOT deliver closability (first-principles — this is what the workshop literally asked)
Identifying the channel is necessary, not sufficient, for the workshop's claim. The proposed closure mechanism `δρ_vac = ρ_m²/χ_q` is **verbatim the S43 formula A.3.1** (`Λ_residual = ρ_m²/χ_q`, `χ_q = 300,338 M_KK⁴`), already run and filed as a dead end. To reproduce the present 3.2% it requires `χ_q` to run down 118.7 OOM from fold to today, while the framework's own settled structural argument (`χ_q ~ S_fold`, 2.2% τ-spread; Hawking R2-3b + volovik V3 in-session-accepted; S99 PROVEN-corridor) says `χ_q` is τ-nearly-constant. **No working closure normalization was exhibited** — only a channel identification plus an uncomputed normalization with a known-adverse structural prior. volovik conceded this himself (R1 §V.1; R2 §3.2). The `Ω_m²` evidence carries near-zero discriminating power (R3-verified: one datum + free coefficient → every exponent fits; the `Ω_m¹` fit `c = 0.1016` is *rounder* than the `Ω_m²` fit `c = 0.3225`), so it cannot prop up the channel-internal closability claim. **Closability is therefore unestablished, and structurally disfavored.**

### 3.3 The leading coefficient is over-constrained across epochs (first-principles — independent of 3.2)
Even setting aside the χ_q run-down, the leading tracking coefficient `α_V` cannot fit both epochs (Sage-exact): the value landing present-epoch closure (`ρ_vac/ρ_obs = 1.032`) over-produces at BBN by 2.06×; the value relieving BBN (S99 mech-b factor 0.479) under-produces today by ~46% (`1.032 → 0.538`). A clean second-order q-residual does not rescue a leading-order conflict. **The tracking mechanism as a whole cannot be declared to close the CC** while its leading law fails BBN by a factor of two. (volovik conceded this in R2 §3.2; it is the substance of lizzi's BBN nail, re-derived on a leading-coefficient basis rather than the a₀-orthogonality basis lizzi originally asserted.)

**Net:** the residual is in the right channel for an effacement/q-tracking treatment (Reading A), but the treatment does not computably close it (Reading B), because (3.2) the channel-internal closure is the S43 dead end needing a structurally-forbidden χ_q run-down, and (3.3) the leading coefficient is over-constrained across the present and BBN epochs. **The honest registry status is a standing CC-sector limitation in the q-departure channel — not a closed/closable higher-order effect, and not a "genuine a₀ residual" (the channel is q, not a₀).** This is CONDITIONAL on the S43 `χ_q`-nearly-constant argument; the registered falsifier (§4) can overturn it.

### 3.4 Q29 (BBN-epoch): INDEPENDENT, and DIAGNOSTIC
**Decision: Q29 is INDEPENDENT of the present-epoch residual as a *term* (it is the leading-order, `w`-free a₀-ratio `ρ_vac/ρ_rad` at `H_BBN`; the present residual is a sub-leading correction at `H_0` — different orders, different epochs), but COUPLED through the shared structure of the single functional `ρ_vac(q)` (same `ε(q)`, same `χ_q = d²ε/dq²`, same expansion point `q₀`, same leading coefficient `α_V`).**

The decisive refinement (lizzi R2 §4, accepted as correct): Q29 is **diagnostic** of the q-expansion volovik's closure needs. BBN is the leading term of that *same* expansion, read at a different H, and it overshoots by 2.06× — direct evidence the shared structure (`q₀`, `α_V`, the controlled-ness of the series) is mis-calibrated at the order that governs the present residual. A perturbation expansion whose leading, cleanly-testable term is off by a factor of two cannot be trusted to deliver its next-order term to 3%. **So Q29 is not merely a side-constraint; it is positive structural evidence against channel-internal closability** — independent in epoch, coupled in functional structure, and adverse to Reading A's closure on both the leading-coefficient axis (3.3) and the series-control axis (3.4).

---

## 4. Forward artifact

Reading B holds the workshop's literal object → the primary artifact is the **pinned standing-limitation statement**, plus volovik's gate registered as a **falsifier-of-the-limitation** (NOT a closure gate), per both agents' R2 agreement.

### 4.1 PINNED STATEMENT (for atlas-04 C10 + capstone §8.5)

> **CCRESID standing-limitation (S113, WS-S112-3):** The residual `ρ_vac/ρ_obs − 1 = 4/125 = 0.032` (DILUTION-CC-66) is a **q-departure / Gibbs–Duhem object** (NOT an a₀-magnitude offset; a₀-orthogonality does not apply — channel sub-question resolved for Reading A). It is **not a demonstrated closable higher-order effacement effect**: the only proposed mechanism is the S43 `δρ_vac = ρ_m²/χ_q` route (A.3.1), which requires a **118.7-OOM run-down of the intensive, spectrum-fixed compressibility `χ_q`** (fold value `300,338 M_KK⁴`) against the settled `χ_q ~ S_fold` (τ-nearly-constant, ΔS/S = 2.2%; S99 PROVEN-corridor) argument — and additionally the leading tracking coefficient `α_V` is **over-constrained across the present and BBN epochs** (z=0 closure value over-produces BBN by 2.06×; BBN-relief value under-produces z=0 by 46%). **Registry status: STANDING CC-SECTOR LIMITATION in the q-departure channel, CONDITIONAL on the S43 χ_q-nearly-constant argument; overturnable only by the registered falsifier `CCRESID-CHI-Q-SCALING` (§4.2).**

**Routing:**
- **atlas-04 C10 cell:** the C10 tag stays **CONFIRMED-TRACKING-FORM** (the *present-epoch tracking FORM* `ρ_vac ~ M_Pl²H²` is unchanged and unchallenged by this workshop); ADD a CCRESID sub-annotation under C10 recording that the *residual-3%* is a standing q-departure-channel limitation (channel identified, closure not demonstrated) and that the BBN-epoch arm (Q29) is diagnostic of the shared q-expansion, not merely a separate constraint. This is a scoping annotation, NOT a status-cell flip (no PROVEN/ASSUMED/CONDITIONAL/BROKEN change) — consistent with the S110/S112 C10 reconciliation discipline. Designated writer: orchestrator-direct (C10 prose owner), per capstone-hygiene Q3.
- **capstone §8.5 / `project_dilution-cc-priority`:** update the existing "only residual-3% underived" line to "residual-3% is a standing q-departure-channel limitation (channel identified Reading-A; closure not demonstrated — S43 χ_q dead-end + leading-α_V over-constraint); falsifier registered." Prose tag MUST equal this register tag per `capstone-hygiene-gate.md` Q3.

### 4.2 REGISTERED FALSIFIER GATE (volovik's gate, re-scoped as falsifier-of-the-limitation)

`CCRESID-CHI-Q-SCALING` (proposed S114; the gate both agents agree settles the crux):

1. **What:** Compute the q-channel compressibility `χ_q(τ)` / `χ_q(a)` scaling first-principles from the D_K spectrum across the Jensen family (and, if a substrate→a(t) map is available, as a function of scale factor), to test whether `χ_q` runs the required 118.7 OOM from fold to today OR is fold-frozen per `χ_q ~ S_fold`.
2. **Inputs:** the D_K eigenfrequency data underlying the S97 W2-2 curvature `k = +3586.5 M_KK` (the grand-potential second derivative `d²ε/dq²`); the S43 `χ_q(fold) = 300,338 M_KK⁴` anchor; `S_fold(τ)` across the Jensen family (the ΔS/S = 2.2% spread); `ρ_m,today = Ω_m ρ_crit`; canonical `Ω_m`, `ρ_Lambda_obs`, `M_KK` from `canonical_constants.py`.
3. **Gate (pre-registered, open-verdict):**
   - **FAIL-of-limitation / PASS-Reading-A:** `χ_q(today) ≈ 1.78e−46 GeV⁴` (runs ~118.7 OOM) AND `ρ_m,today²/χ_q,today` reproduces the residual magnitude `0.032 ± 0.005` (absolute on the fraction) → the channel-internal closure is real; the standing-limitation statement is overturned (leaving only the separate BBN leading-α_V limitation).
   - **PASS-of-limitation / Reading-B confirmed:** `χ_q` is fold-frozen (τ-nearly-constant, consistent with `χ_q ~ S_fold` to within the 2.2% spread) → magnitude cannot match, `Ω_m²` shape-match is coincidental → the standing-limitation verdict is confirmed on channel-internal grounds.
   - **INFO:** `χ_q` runs partially (between fold-frozen and the required 118.7 OOM) → q-channel is right but normalization insufficient; residual remains a limitation with a quantified shortfall.
   - **Tolerance rule:** RATIO on the magnitude fraction (`|computed_frac − 0.032| / 0.032 ≤ 0.156` for the ±0.005 band); the χ_q run-down is an OOM comparison (PASS-A requires ≥ 100 OOM run-down; fold-frozen is < 10 OOM).
4. **Effort:** LOW–MEDIUM. The `d²ε/dq²` machinery exists (S97 W2-2 computed `k` once); extending it to the `χ_q(τ)` τ-scan across the Jensen family is a re-evaluation on existing spectral data. The `χ_q(a)` (scale-factor) leg is harder and may require the substrate→a(t) map (C1, currently ASSUMED-with-external-import per S112) — if that map is unavailable, the τ-scan leg alone is sufficient to test the `χ_q ~ S_fold` argument and settle the crux.

### 4.3 Falsifier-surface update — ROUTE TO mack-cosmic-bridge (do NOT write here)

The BBN-epoch arm (Q29) row in `falsifier-master-inventory.md` (Row #76, the BBN sign-sensitivity / `w`-free a₀-ratio cross-cut) should be annotated with this workshop's R3 finding: **Q29 is not merely "BBN over-production 2.06×, corridor closed" — it is now also DIAGNOSTIC of the present-epoch residual's closability** (the leading term of the same `ρ_vac(q)` expansion). This sharpens the falsifier's role from "separate BBN constraint" to "the `w`-free, leading-order test whose 2.06× failure bears against channel-internal closure of the present residual." **mack-cosmic-bridge is the sole writer of `falsifier-master-inventory.md`** (`feedback_mack-bridge-role.md`); this verdict NAMES the row and the annotation; mack applies it.

---

## 5. Residual dissent + the decisive compute

**Residual dissent (narrow, honest):** The two agents do not fully agree on the *force* of Q29 against closability, and the verdict above adopts lizzi's reading on this point — which the verdict author (Reading-A pole) flags as the place a determined Reading A could still push:

- **lizzi (adopted in §3.4):** Q29 is *diagnostic* — the BBN 2.06× leading-term failure is positive evidence the q-expansion is uncontrolled at the order governing the present residual, so the present residual is structurally disfavored even before computing `χ_q`.
- **volovik's residual position:** Q29 constrains the *leading coefficient* `α_V` (conceded), but a leading-order mis-normalization does not *strictly logically forbid* a well-defined sub-leading term — it is possible (though structurally disfavored) that `q₀`/`α_V` is mis-calibrated at leading order while `χ_q = d²ε/dq²` (a local curvature, computed independently from the spectrum) is nonetheless correct. The order-of-expansion trap is a *strong prior*, not a *theorem*.

This dissent does NOT change the verdict (both readings agree the closability is unestablished and structurally disfavored; they differ only on whether it is disfavored-by-strong-prior or disfavored-by-near-theorem). It is recorded because it identifies precisely what the decisive compute resolves.

**The single decisive compute (resolves both the verdict's conditionality AND the residual dissent):**

> **`CCRESID-CHI-Q-SCALING` (§4.2): compute `χ_q(τ)` across the Jensen family from the D_K spectrum, and test it against the `χ_q ~ S_fold` (τ-nearly-constant) argument.** If `χ_q` is fold-frozen (the structurally-expected outcome), Reading B is confirmed on channel-internal grounds AND the order-of-expansion dissent is moot (no closure regardless). If `χ_q` runs ≥ 100 OOM (the structurally-unexpected outcome), Reading A's channel-internal closure is live and the verdict's conditionality is overturned — at which point the order-of-expansion trap (does a 2.06×-overshooting leading term permit a 3%-accurate next-order term?) becomes the *next* gate. Either way, this one computation is the load-bearing fork the entire workshop reduces to.

---

## Summary table

| Sub-question | Winner | First-principles reason |
|:--|:--|:--|
| **Channel** of present residual | **Reading A** | q-departure / Gibbs–Duhem object; a₀ magnitude does not gravitate at equilibrium (Volovik Paper 04); `Ω_m`-dependence excludes the a₀ mode-count; lizzi conceded (R2 §1) |
| **Closability** (workshop's literal object) | **Reading B** (conditional) | proposed mechanism = S43 `ρ_m²/χ_q` dead end; needs 118.7-OOM χ_q run-down vs τ-nearly-constant `χ_q ~ S_fold`; `Ω_m²` evidence non-discriminating; leading α_V over-constrained across epochs (z=0 vs BBN) |
| **Q29 / BBN** | **INDEPENDENT in epoch, DIAGNOSTIC of the shared q-expansion** | leading-order `w`-free a₀-ratio at H_BBN vs sub-leading correction at H_0 (different terms), but same `ρ_vac(q)`, `χ_q`, `q₀`; 2.06× leading-term failure bears against channel-internal closure |
| **Registry verdict** | **SYNTHESIS → standing CC-sector limitation (q-channel), conditional on S43 χ_q argument, with registered falsifier** | channel identified (A) but closure not demonstrated and structurally disfavored (B); overturnable by `CCRESID-CHI-Q-SCALING` |

**This completes WS-S112-3 CCRESID.**
