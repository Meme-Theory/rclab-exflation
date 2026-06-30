# Independent Review — *The Phonon-Exflation Equation*

**Reviewer:** mack-cosmic-bridge (particle-physics / astrophysics interface; observational cosmology)
**Source under review:** `sessions/framework/phonic-exflation-equation.md` (capstone synthesis, §0–§9 + verification ledger)
**Date:** 2026-05-26
**Scope of authority:** I review the document where it touches **observation** — §6.3 (the FRW gap), §7 (where the equation meets data), §8.3 (derived scales that anchor data comparisons), and the cross-cutting question of *what these numbers entitle the framework to claim against Planck/DESI/BICEP/LISA*. I do **not** re-adjudicate gate verdicts or PROVEN/CLOSED statuses — those are authoritative per the spawn contract. I verify that the document uses observational results with fidelity, translates conventions correctly, and does not over-state what the data show.

---

## §1 — Summary of what I checked and where I land

I read the document in full and cross-checked its load-bearing observational anchors against my canonical constraint set (`sessions/framework/registry/mack-observational-constraints.md`) and the knowledge MCP. **The document is, by the standards of this field, unusually honest about the boundary between what the substrate delivers and what it borrows.** The single most consequential thing it does right is §6.3: it states, without softening, that there is no substrate-derived FRW scale factor `a(t)`, and it does not let the "space does not expand" reframe smuggle that obligation off the books. That is exactly the discipline I would demand, and it is rarer than it should be.

My review surfaces **one substantive fidelity correction** (the §7.1 dark-energy comparison anchor is mislabeled relative to its own σ-figure and to the canonical DESI release I hold), **three places where the data-facing language slightly out-runs the data**, and **a set of verbiage recommendations** that sharpen the observational sections without weakening any result. None of this touches a gate verdict. All of it is about how the substrate's spectral outputs are *positioned against detectors*.

The structural assessment, stated as geometry rather than verdict: the framework occupies a region of the constraint surface that is **simultaneously falsifiable and non-degenerate**. Its most exposed coordinate is `wₐ = 0` (a structural four-fold lock, not a fitted value), and the document correctly identifies DESI DR3 as the near-term cliff-edge rather than burying it under the LISA headline. That ordering — DESI DR3 as the dangerous test, LISA as the spectacular one — is the correct read of the observational landscape.

---

## §2 — The one fidelity correction that must be made (§7.1, dark-energy row)

This is the only item I would call a **defect**, and it is a labeling/sourcing defect, not a physics error.

The §7.1 table gives the `w₀` comparison anchor as:

> DES-Dovekie+DR2+P/ACT/SPT: `−0.803 ± 0.054` → "LIVE; 2.13σ / 0.73σ"

and the `wₐ` anchor as:

> DESI+Dovekie: `−0.72 ± 0.21` → "3.43σ — the live wager".

Two problems, in increasing order of severity.

**(a) The compilation label and the canonical release disagree, and the document does not flag the choice.** My canonical DESI anchor (DR2, `mack-observational-constraints.md`) is `w₀ = −0.752 ± 0.057`, `wₐ = −0.73 ± 0.25`. The document's `w₀ = −0.803 ± 0.054` is a *different, tighter* compilation (a DES-Dovekie + multi-probe combination). That is a legitimate choice — newer joint compilations exist and are tighter — but **the framing law and the project's own epistemic discipline require that an observational anchor declare its provenance when it departs from the canonical registry value.** Right now a reader cannot tell whether `−0.803 ± 0.054` is DESI DR2, a DESI DR2 + external combination, or a forecast. Per the spawn rules ("cite sources precisely — paper numbers, file paths"), this anchor needs a one-line provenance tag. This is the same discipline the document applies impeccably to its *own* numbers (every framework value carries a regulator tag and an E-number); the comparison anchors deserve the same.

**(b) The σ-arithmetic on the `w₀` row does not reconcile with a single anchor, and this is load-bearing.** The row reports "2.13σ / 0.73σ" for the two branches against `−0.803 ± 0.054`. Let me write the substitution chain explicitly, because a σ-distance is exactly the kind of directional claim the math-scripts discipline says I must not eyeball:

```
Branch (canonical):  w0_FW       = −0.918
Branch (iv):         w0_FW_R842  = −0.842454
Anchor:              w0_obs      = −0.803 ± 0.054   (σ_obs = 0.054, as printed)

σ_canonical = |w0_FW − w0_obs| / σ_obs
            = |−0.918 − (−0.803)| / 0.054
            = 0.115 / 0.054
            = 2.13σ        ✓  (matches the "2.13σ" printed for the canonical branch)

σ_branch_iv = |w0_FW_R842 − w0_obs| / σ_obs
            = |−0.842454 − (−0.803)| / 0.054
            = 0.039454 / 0.054
            = 0.73σ        ✓  (matches the "0.73σ" printed for branch iv)
```

So the **arithmetic is internally correct** against the printed anchor `−0.803 ± 0.054` — good. But the *label* on that anchor ("DES-Dovekie+DR2+P/ACT/SPT") is then inconsistent with the **wₐ** anchor on the very next line, which is labeled "DESI+Dovekie: `−0.72 ± 0.21`". A `w₀`–`wₐ` pair must come from the **same fit** — they are jointly constrained with a strong negative correlation (`ρ ≈ −0.85` in the DESI DR2 era), and you cannot quote `w₀` from one compilation and `wₐ` from another and then read either σ-distance as a real tension. **The two rows must cite a single joint `(w₀, wₐ)` posterior.** As written, the document risks the exact error my memory flags as a recurring failure pattern: treating marginal one-parameter distances as if they were the joint constraint.

**Recommended fix (verbiage):** replace the two anchor cells with a single sourced joint citation, e.g.

> `w₀` anchor: `−0.803 ± 0.054` *(DESI DR2 + DES-SN5YR + CMB joint; ρ(w₀,wₐ) ≈ −0.85)*
> `wₐ` anchor: `−0.72 ± 0.21` *(same fit)*
> **and** add a footnote: *"σ-distances are 1-parameter marginals; the binding test is the 2D `(w₀, wₐ)` posterior — see Falsifier #1 / `R_842` rectangle."*

This is consistent with the document's own §7.2, which correctly frames DESI DR3 as a *rectangle* falsifier (`R_842`) — a 2D object. §7.1 should not quietly collapse that to two independent 1D σ-distances.

> **Note on what I did NOT touch.** I am not disputing that `wₐ = 0` is at ~3σ and advancing — the knowledge base confirms `wₐ = 0` is PROVEN/STRUCTURAL (four-fold lock, S58) and the registry shows the tension live (baseline-findings-s66 records 2.9σ at DR2; the document's 3.43σ reflects the tighter combined anchor). Both are consistent: a tighter anchor on a structurally-fixed prediction *should* push the σ-distance up. The framework value is not moving; the data is tightening around a fixed prediction. That is the honest and dangerous situation, and the document says so. My correction is purely that the *two rows must be sourced to one fit*.

---

## §3 — Three places the data-facing language slightly out-runs the data

These are not errors. They are calibration issues — the language is ~10–20% stronger than the constraint warrants. Each is a one-clause fix.

### 3.1 σ₈ — "VIABLE (in the tension gap)" is right; the implicit suggestion of resolution is not

The document gives `σ₈ = 0.799` (zero-free-parameter), Planck `0.829`, lensing `~0.76`, status "VIABLE (in tension gap)." This is a genuinely strong line and I want to protect it — landing *between* the two ends of the S₈ tension from zero free parameters is a real structural fact, not a fit. **But the phrase "in the tension gap" can be read as "the framework resolves S₈," which it does not.** The substrate prediction sits at `0.799`; that is `2.1σ` low of Planck primary (`0.829 ± 0.014`) and `~1σ` high of the weak-lensing central value. It is *consistent with the existence of the tension* and *compatible with both ends within their spreads* — it does not adjudicate between them.

Substitution chain (so the directional claim is explicit):

```
σ8_FW    = 0.799
σ8_Planck = 0.829 ± 0.014   ⇒  (0.829 − 0.799)/0.014 = 2.14σ  below Planck primary
σ8_lensing ≈ 0.76 (±~0.02)  ⇒  (0.799 − 0.76)/0.02  ≈ 1.95σ  above lensing central
```

So the framework value is **not** comfortably consistent with either anchor at <1σ; it is ~2σ from *both*, sitting in between. The honest statement is: *"the framework's `σ₈ = 0.799` falls between the CMB-primary and weak-lensing determinations, ~2σ from each — compatible with the tension being real, but not (yet) a resolution of it."* That is still a strong, zero-parameter result. **Recommended verbiage:** change "VIABLE (in the tension gap)" to "VIABLE — sits ~2σ between CMB-primary (0.829) and lensing (~0.76); compatible with the S₈ tension, not a resolution of it."

### 3.2 Ω_DM h² — the "0.7σ" is excellent, but the dark-matter *identity* claim needs its exclusion stated as a constraint, not a footnote

The Leggett-only `Ω_DM h² = 0.120` against Planck `0.1186 ± 0.0020` is `0.7σ` — a flat PASS, and from zero free parameters it is one of the strongest single lines in the document. I have nothing to correct in the number. What I want sharpened is the *logical structure* around it, because it is doing more work than it looks.

The document notes parenthetically that "the full-DM route over-closes at 260σ; only the Leggett-only channel passes." **That 260σ exclusion is not a footnote — it is one of the framework's sharpest internal falsifiers, and it should be reported as a constraint in the §7.3 scorecard, not buried in §7.1 prose.** Here is why it matters observationally: a framework that predicts the relic abundance from geometry could, in principle, have predicted *any* abundance. The fact that the full graph-gapped Goldstone spectrum over-produces by 260σ and *only* the Leggett-channel projection lands at 0.7σ means the framework is **not** free to slide its DM prediction to match data — the geometry forces a specific channel, and that channel happens to work. That is a much stronger Bayesian statement than "0.7σ PASS," and the document under-sells it by keeping the exclusion in parentheses.

I also want to register, in my role as the DM-phenomenology bridge, that the **`σ/m = 0` exactly** line (DM self-interaction, structural, from `N_pair = 1`) is the cleanest observational signature in the whole table. The Bullet-cluster bound is `σ/m < 1.25 cm²/g`; a *structurally exact zero* (CPT-neutral, non-annihilating, integrability-protected GGE quasiparticle) is qualitatively distinct from the WIMP/SIDM landscape, where `σ/m` is a tuned parameter. **Recommended verbiage (§7.1 substrate-readings paragraph):** promote both the 260σ over-closure and the structural `σ/m = 0` to a single sentence: *"The geometry does not permit the DM abundance to be tuned — the full Goldstone spectrum over-produces by 260σ, and only the Leggett-channel projection lands at 0.7σ; that same channel forces `σ/m = 0` exactly (vs Bullet `< 1.25 cm²/g`), a structural zero distinct from any tuned-cross-section dark-matter model."*

### 3.3 The α_s row — the resolution is correct, but "RESOLVED" risks being read as "confirmed"

I checked this one against the knowledge base directly because it is the row my memory flags as most-misread (the QCD `α_s(M_Z)` vs inflationary `dn_s/d ln k` symbol overload). The S93 W7-1 gate is confirmed: `deg(T_{BZ→pivot}) = +2` (non-scalar), `α_s_substrate = −0.08587279`, `α_s_pivot = 0.0`, `factorization_holds = False`, formulation T4-non-scalar. The physics is exactly as the document states: there are **two scale-separated observables**, the `−12σ` was the scalar-transport leaf (now falsified), and on the matched channel the pivot image sits at `+0.67σ`.

This is a correct and genuinely elegant resolution — a tension *relocated to its correct detector channel*. **My only caution is on the status word.** "RESOLVED" is true in the sense that the *apparent 12σ tension is resolved* (it was a channel mismatch). But it could be misread as "the α_s prediction is confirmed at +0.67σ," which over-claims: the pivot image at +0.67σ is *consistent*, and the substrate-distance value `−0.0859` is *not yet measured at all* — it relocates to a ~34σ-reach CMB-S4/CMB-HD falsifier (2030–2035). So the honest status is **"tension resolved as a channel artifact; pivot image consistent (+0.67σ); substrate-distance value awaits CMB-S4."** That is a future test, not a present confirmation.

**Recommended verbiage:** change the status cell from "**RESOLVED** (S93 W7-1)" to "**RESOLVED-AS-CHANNEL-ARTIFACT** (S93 W7-1); pivot +0.67σ consistent; substrate value `−0.0859` → CMB-S4 falsifier." The box prose below the table already says this well; the *table cell* should not compress it to a word that reads like a checkmark.

> **Convention-fidelity note (this is my standing watch-item).** The document is careful to keep the two `α_s` observables scale-and-channel-tagged, per `phononic-framing.md §"Scale-and-channel-tagging"`. I confirm the tagging is correct here. The one thing I will keep watching across future documents: the QCD `α_s(M_Z)` (strong coupling) must *never* drift into the same symbol as this `dn_s/d ln k` running. The S50–51 identity `α_s = n_s² − 1` is topological-scheme-only and is a *different* α_s again. This document does not conflate them — but the symbol is overloaded three ways across the corpus, and any reader arriving from particle physics will assume "α_s" means the strong coupling. A one-line glossary footnote ("`α_s` here = scalar spectral-index running `dn_s/d ln k`, NOT the QCD strong coupling") would prevent a predictable misread.

---

## §4 — Where the document gets the observational framing exactly right (protect these)

I want to be explicit about what should *not* change, because in my experience these are the parts a future editor is tempted to soften, and softening them would be a mistake.

### 4.1 §6.3 — the FRW gap, stated without softening

This is the best paragraph in the document from my vantage. The framework does not have a derived `a(t)`; C1 postulates `τ = cosmic time`; C2 (`K_pivot`) is BROKEN-WITH-LIVE-PATHWAY; T6 (Friedmann–BCS locking) is BROKEN; and the document says all of this in plain language. Critically, it does **not** let the substrate-first reframe ("space does not expand; spectral complexity grows") be used as an excuse to *not owe* an effective Friedmann map. The sentence —

> "'Friedmann is the wrong question' is right about the *fundamental* level and wrong about the *effective* level; both must be said"

— is exactly the discipline I would enforce. The framework borrows the container-observer's FRW `H(t)` for *every* late-time observable (`w₀`, `wₐ`, `σ₈`, the CC tracking). It is therefore not entitled to wave away the Friedmann obligation by appeal to emergence. The document knows this. **Do not let any future pass weaken this paragraph.** If anything, I would make the borrowing even more visible in §7 (see §5 below).

### 4.2 §7.3 — no aggregate metric, and the joint-probability framing

The scorecard correctly refuses a PASS/FAIL ratio and instead makes the **joint** statement: the probability of one random geometry reproducing the relic abundance AND the CC scale AND `σ₈` AND `m_H` simultaneously is the *product* of the individual improbabilities. This is the right Bayesian framing, and it is the framing my memory and the project's evoi-prioritization rule both demand. A single 0.7σ PASS is weak evidence; four independent zero-parameter near-landings across a wide prior range is a large likelihood ratio. The document states this correctly. (See §6 below for the one tightening I would make to keep it honest.)

### 4.3 The LISA / DESI DR3 ordering

§7.3 headlines LISA's CGWB discriminator (acoustic class 11 OOM above LISA-PLS vs Companion-null `8.299×10⁻⁵⁸`, SNR ~10¹³) but then explicitly elevates **DESI DR3 (2026) as the more urgent and more dangerous near-term test**. This is the correct observational triage. LISA (~2034) is the spectacular, unique-to-this-equation test (LCDM has no fold, no white hole, no GGE relic, hence makes no prediction in the acoustic band — a clean discriminator). But DESI DR3 is the near-term cliff-edge for the most exposed prediction (`wₐ = 0`). A framework review that led with the 10¹³-SNR headline and buried the 2026 cliff-edge would be doing PR, not physics. This document does the opposite. Protect that ordering.

---

## §5 — One structural recommendation: make the "borrowed H(t)" visible in the §7.1 table itself

This is my main *constructive* recommendation, and it follows directly from §6.3 being right.

§6.3 admits — correctly — that `w₀`, `wₐ`, `σ₈`, and the CC closure all **consume an external FRW `H(t)`** as input (caveat C10). The CC closure row is explicitly flagged "doubly conditional" in the §7.1 substrate-readings paragraph. **But the §7.1 *table* does not carry that conditionality in its Status column.** A reader scanning the table sees "CC closure | PASS (DILUTION-CC-66)" and "w₀ | LIVE" without the flag that *both of these are evaluated inside a borrowed expansion history the framework does not yet derive*.

This is not a request to weaken the results — the `ρ_vac/ρ_obs = 1.032` closure is a genuine PASS *given* an external `H(t)`, and the document says so in prose. It is a request to make the table **self-consistent with §6.3**: any observable that is read against (or fed into) the borrowed FRW `H(t)` should carry a visible marker in the Status column. Concretely:

**Recommended verbiage (§7.1 table):** add a dagger marker to every row that consumes the external `H(t)` — `w₀†`, `wₐ†`, `σ₈†`, `CC closure†` — with one footnote: *"† Evaluated using the container-observer's FRW `H(t)` as external input (caveat C10); not yet a from-`D_K` derivation of the expansion history — see §6.3. The spectral *value* is from `D_K`; the *cosmological evaluation* borrows `H(t)`."*

The reason this matters to me specifically: in observational cosmology, the single most common way a model launders an unearned result is by quietly adopting the ΛCDM expansion history to convert its prediction into an observable, then reporting the comparison as if the whole chain were derived. The document is **not** doing that — §6.3 is scrupulous — but the §7.1 table, read in isolation (which is how tables get read), does not show the seam. The dagger closes the gap between the table and the caveat. It costs four daggers and one footnote and makes the document bulletproof against the "you borrowed ΛCDM" objection that a referee *will* raise.

A subtler version of the same point: the `r = 0.033` row and the `n_s` row are read at the **CMB pivot** `k = 0.05 Mpc⁻¹`, which is 54.04 decades in `k` from the transit scale. The document handles this correctly elsewhere (the n_T convention trap — transit-scale `n_T = +0.4676` is a GEOMETRIC FLOOR, not a LiteBIRD-comparable quantity; the CMB-transferred `n_T = −3.024×10⁻³` is the detector-matched value). I would add a one-line reminder in the §7.1 caption that **`n_s`, `r`, and `α_s` are quoted at the CMB pivot via the transport map, not at the substrate/BZ scale** — same discipline as the α_s box, applied table-wide. This prevents a reader from comparing a substrate-scale spectral output directly to a Planck pivot-scale measurement (a 54-decade category error the framework has explicitly closed but the table does not re-state).

---

## §6 — One honesty-tightening on the joint-probability argument (§7.3)

The joint-probability framing (§4.2 above) is correct, but it has a known failure mode I am obligated to flag, because the project's own epistemic-discipline rule forbids citing it loosely.

The §7.3 sentence says the joint statement is "the *product* of the individual improbabilities." **The product rule is only valid for *independent* observables.** Some of the four cited (relic abundance, CC scale, σ₈, m_H) are *not* fully independent — in particular, `σ₈` (structure growth via `a₂`) and `Ω_DM h²` (Leggett gap via `a₂`) **both descend from the same `a₂` channel**, so their improbabilities do not multiply cleanly; there is a shared geometric origin that correlates them. Multiplying them as if independent over-states the joint likelihood ratio.

This does not break the argument — m_H (a₄/fiber), the CC scale (a₀), and the a₂-channel observables *are* drawn from genuinely distinct spectral moments (the Spectral-Moment Decoupling Theorem, S75 W2-E, certifies a₀/a₂/a₄ are algebraically independent with non-vanishing Wronskian, which is precisely the license for treating *cross-moment* observables as independent). So the *cross-layer* product (a₀ × a₂ × a₄) is defensible. The within-layer pair (Ω_DM and σ₈, both a₂) is not.

**Recommended verbiage:** change "the *product* of the individual improbabilities" to "the product of the improbabilities **across distinct spectral-moment layers** (a₀ × a₂ × a₄ — independent by the Decoupling Theorem); within a single layer (e.g. Ω_DM and σ₈, both a₂-channel) the observables share a geometric origin and must not be multiplied as independent." This *strengthens* the argument by tying the independence claim to the certified Wronskian theorem the document already proved in §4.2 — it makes the joint-probability statement rest on a theorem rather than an assumption. The Decoupling Theorem is the perfect tool here and the document should use it for exactly this.

---

## §7 — Minor / verbiage-level notes (no physics impact)

1. **§7.1 `n_s` row — "SCHEME-DEPENDENT (0.9561 / 0.9590 / 0.9595)".** Correct and honest. The Planck anchor `0.9649 ± 0.0042` is right (my canonical). The three values span `1.4–2.1σ`. I would add the σ-distance *per value* so the reader sees that even the most favorable scheme (`0.9595`, `√x`) is `1.29σ` low, not a flat hit:
   `(0.9649 − 0.9595)/0.0042 = 1.29σ`; `(0.9649 − 0.9590)/0.0042 = 1.40σ`; `(0.9649 − 0.9561)/0.0042 = 2.10σ`. The document's "1.4–2.1σ" is right; printing the favorable end (1.29σ, slightly *below* the stated range floor of 1.4σ — recheck which value the 1.4 refers to) would let the reader see the spread isn't "PASS vs FAIL" but "marginal-but-correct-sign across the board, contingent on the unsolved functional selection." **Recheck:** the stated range "1.4–2.1σ" omits the `0.9595` value's `1.29σ`; either the range floor should be `1.3σ` or `0.9595` is being excluded from the cited range — clarify.

2. **§7.1 m_H row.** "127.5–131.8 GeV (KK threshold)" vs PDG `125.25 ± 0.17`. The defensible-headline framing (band, route-dependent; zeta route 138.5 excluded; μ_BC 188 GeV is an ACCOMMODATION not a prediction) is exactly the right honesty. One numerical note: the band floor `127.5` is `~13σ` above PDG in *PDG's* error bar (`(127.5 − 125.25)/0.17 ≈ 13σ`) — but that is the wrong comparison, because the framework band has its own ~2% theory width that dwarfs the 0.17 GeV experimental error. **State the comparison in the framework's error budget, not PDG's:** "consistent at the ~2% level given KK-threshold theory uncertainty; PDG's 0.17 GeV precision is not the relevant comparator until the route is pinned." Otherwise a referee will (wrongly) compute a 13σ tension against a band that isn't claiming 0.17 GeV precision.

3. **§7.2 Falsifier #2 (r / n_T).** "Path-H vs Path-C discriminator (4.25σ via `n_T = −r/8`)." Good — this is a real, near-term, B-mode discriminator. Confirm the `n_T = −r/8` consistency relation is the *framework's* transferred-to-CMB relation (it is — the slow-roll `n_T = −r/8` is INAPPLICABLE at the transit scale per the five-argument result, but the CMB-transferred tensor sector recovers a slow-roll-like consistency, per S66 TENSOR-TRANSFER). A reader could mistake `n_T = −r/8` for the standard single-field consistency relation; add "(the CMB-transferred tensor consistency, S66 — *not* the slow-roll relation, which is inapplicable at the fold)."

4. **§8.3 — the `f₂ ≈ 92` dictionary closure.** This is well-handled (the `f₂ = 2.34` Gaussian-cutoff pin is a different scheme; cross-substituting gives the spurious 39× residual). One observational hook worth adding: `f₂ ≈ 92` is an `O(10²)` cutoff moment "the same legitimacy class as the Chamseddine–Connes `f₂` at unification." That is the right comparison. I'd note that this is *not* a free knob in the observational sense — it is fixed by the `M_Pl`/`M_KK` ratio once `a₂^ζ` is pinned, so it does not add a fitting degree of freedom to any data comparison. Worth saying explicitly so `f₂` is not mistaken for a tunable parameter that could absorb a `σ₈` or `G_N` discrepancy.

5. **Verification-ledger hygiene flag (line 506).** The document correctly flags that `M_KK` and `w0_FW` carry values but lack PROVENANCE entries in the knowledge MCP. I **confirm this independently**: `get_constant("w0_FW")` returns `-0.918` with "No PROVENANCE entry." This is a real hygiene gap (not a physics issue). Since I am the sole writer of `falsifier-master-inventory.md` and `w0_FW` is the binding constant for Falsifier #1, I will note it as a carry-forward: **`w0_FW` and `M_KK` need PROVENANCE entries added via `update_constant(...)` before DESI DR3 lands**, so the falsifier's anchor is audit-traceable when the binding event fires. This is a 4-field carry-forward (what: add PROVENANCE to w0_FW + M_KK; inputs: S58 four-fold-lock derivation, S42 Sakharov/zeta route for M_KK; gate: knowledge-MCP provenance-present check; effort: minutes-scale, single hygiene pass).

---

## §8 — Structural assessment (geometry, not verdict)

Reported as constraint-surface geometry per epistemic-discipline, **not** as a probability or a pass/fail tally:

- **What walls the framework respects (observationally):** it lands `Ω_DM h²` at 0.7σ, the CC scale at 1% (given external `H`), `σ₈` between the two ends of the S₈ tension, `m_H` at the ~2% level, `r` within the BICEP/Keck 2σ bound, and `σ/m = 0` structurally — all from zero adjustable cosmological parameters. These are the walls it is *inside*.

- **What wall it is closest to (the live edge):** `wₐ = 0` is a structural lock, and the data is tightening around it. At the canonical anchor it is ~3σ and at the document's tighter combined anchor ~3.4σ. **This is the coordinate where the framework is most likely to be falsified first**, and it is falsified *cleanly* (the lock is structural — there is no parameter to retreat to). DESI DR3 (window opened 2026-04-23) is the binding instrument. This is the framework's most honest and most dangerous exposure, and the document foregrounds it correctly.

- **What remains uncomputed (the next observational gate):** the **effective Friedmann map** (`S_SA(τ) → 4D gravitational action → H²`), the `K_pivot` paradox (C2), and the `M_KK⁻¹ → seconds` normalization — which §6.3 correctly identifies as *one* bridge. Until that bridge is built, **every late-time observable in §7.1 is conditional on a borrowed `H(t)`**, and the framework's data-facing claims are "the spectral *values* are from `D_K`; the *cosmological evaluation* borrows the expansion history." That is the precise scope of what the document is entitled to claim, and — with the §5 dagger recommendation applied — it is exactly what the document *would* claim.

- **The discriminating future test (unique to this equation):** LISA's CGWB acoustic-band signal (~2034), which LCDM cannot produce at all (no fold → no white hole → no GGE relic → no acoustic CGWB). A detection is a signature of the exflation *mechanism itself*, not a parameter fit. This is the one place the framework makes a prediction no container-based model can make, and it is decisive at SNR ~10¹³. It is the headline; DESI DR3 is the cliff-edge; both must be said — and the document says both.

---

## §9 — Bottom line for the authors

The observational sections are **fundamentally sound and unusually honest.** The substrate-first direction holds throughout — every late-time number is positioned as `D_K` spectrum → moment → emergent observable → comparison, never the reverse, and §6.3 refuses to launder the FRW obligation through the emergence reframe. That discipline is the whole game in this field, and the document has it.

The required fix is exactly one: **§7.1's dark-energy `w₀`/`wₐ` anchors must be sourced to a single joint fit with declared provenance** (§2). The strongly-recommended fix is one: **dagger the table rows that consume the borrowed `H(t)` so §7.1 is self-consistent with §6.3** (§5). The rest are calibration tightenings — most of which *strengthen* the document by tying its claims to theorems it already proved (the Decoupling-Theorem grounding of the joint-probability argument, §6, is the clearest example).

Nothing here re-adjudicates a gate. Nothing here weakens a result. The framework's data-facing position is strong precisely *because* it states its borrowed inputs and its open gaps without softening — and the small corrections above make that strength legible to a referee who will, correctly, probe exactly the seams I have flagged.

---

### Carry-forwards (for `/rclab-plan`, not this review)

1. **Add PROVENANCE entries for `w0_FW` and `M_KK`** (knowledge MCP) before DESI DR3 binding event. *Inputs:* S58 four-fold-lock derivation; S42 Sakharov/zeta route. *Gate:* provenance-present check on both constants. *Effort:* minutes (single hygiene pass). [§7.5 note]
2. **Source the §7.1 DE comparison anchor to a single joint `(w₀, wₐ)` posterior** with provenance tag; add the 1D-marginal-vs-2D-rectangle footnote. *Inputs:* canonical DESI release (DR2 `−0.752±0.057 / −0.73±0.25`) or the combined DES-Dovekie compilation, whichever is intended — declare which. *Gate:* anchor carries provenance + the two rows cite one fit. *Effort:* minutes (verbiage). [§2]

---

*Files referenced (all absolute):*
- Source: `C:\sandbox\Ainulindale Exflation\sessions\framework\phonic-exflation-equation.md`
- Framing law: `C:\sandbox\Ainulindale Exflation\.claude\rules\phononic-framing.md`
- My canonical constraints: `C:\sandbox\Ainulindale Exflation\sessions\framework\registry\mack-observational-constraints.md`
- Falsifier inventory (I am sole writer): `C:\sandbox\Ainulindale Exflation\sessions\framework\registry\falsifier-master-inventory.md`
- This review: `C:\sandbox\Ainulindale Exflation\sessions\framework\Collabs\phonic-exflation-equation-mack-collab.md`
