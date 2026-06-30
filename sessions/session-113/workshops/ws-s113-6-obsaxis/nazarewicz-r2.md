# WS-S112-6 OBSAXIS — Round 2

**Agent**: nazarewicz-nuclear-structure-theorist — Round 2, rebuttal
**Pole**: Reading A (NICER dense-matter EoS / pulsar M–R). I have now read mack's R1 (Reading B, DESI/Euclid f·σ8 growth).

**One-line R2 position**: Mack's strongest point — a *recorded head-to-head verdict pair on these exact two axes* (`INV13-W2-2-FSIGMA8-GROWTH-S8: PASS` vs `INV13-W2-1-FINITE-MU-CFL-EOS: FAIL`) — is genuine, on-disk, and I verified it; on the **tractability term of EVOI as of today, growth wins, and I concede that.** But mack's R1 was written without the S110-CF-CO1-EOS result that *post-dates* the W2-1 FAIL and *fixes the specific pathology* his Candidate A-1 named (the runaway gap ratio); the dense-matter axis is therefore not "FAIL, ~12× off, dead" — it is "FAIL → INFO, gap-ratio pathology resolved, one surface-derivation wave from a falsifiable M–R." The honest residual disagreement is narrow and I state it precisely.

---

## 1. Where mack is right, and I concede it plainly

I will not defend ground the on-disk ledger has already taken from me. Three concessions:

**(a) The head-to-head was run, and growth won — verified.** I independently re-read both verdict lines this round:
- `INV13-W2-2-FSIGMA8-GROWTH-S8: PASS` — `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`, `S8_FW=0.8128` in-band [0.76,0.83], 16/16 z-bins sign-negative, `bind_DESI5yr_max=1.001σ@z0.5`, `bind_Euclid_max=1.516 (7 bins)`. Audit `435609fc…`. This is a clean three-tuple PASS with a forward instrument trajectory.
- `INV13-W2-1-FINITE-MU-CFL-EOS: FAIL` — `M_max_FW=0.1631 M_⊙`, ~12× below the 2 M_⊙ floor.

Mack is correct that on *exactly the two axes this workshop ranks*, the substrate has already produced a bindable PASS on one and a magnitude-FAIL on the other. For the **P(pass) and constructibility terms of EVOI, that pair is close to dispositive**, and I concede it.

**(b) The growth prediction is genuinely zero-parameter and pinned — verified.** `get_constant("fsigma8_product_suppression_FW_max_pct")` returns **−4.058%** (S96, non-superseded, traceable to S65). The chain `D_K → a₂ Seeley-DeWitt → D(a) → f(z) → f·σ8(z)` is forward, substrate-first, and the test quantity (the −4.058% *product*, not the −0.311% bare-f) is correctly distinguished. This is a live, registered flagship falsifier (Row #71), pre-registrable *today* with prediction, σ-budget, and instrument all pinned. My R1 underweighted how *complete* this surface already is — I treated growth as "clean but untested"; it is in fact "clean, pinned, AND already once-passed."

**(c) Leverage ≠ tractability, and mack is right that I conflated them in R1's EVOI claim.** My R1 argued the dense-matter axis has *maximal posterior predictive width* (M_max band [0.16, 4.78], factor ~30) and called that maximal EVOI. Mack's correct rejoinder: a wide band is only high-EVOI if the gate that collapses it is *pre-registrable and survivable*. A band that is wide *because the surface condition is a free dial* is not high-information — it is under-determined, and collapsing it requires deriving the surface from the substrate (a research wave), which is exactly what makes it NOT a "next falsifiable prediction." On the **work-to-pre-registrability metric, growth dominates.** I concede the metric.

---

## 2. The one thing mack's R1 did not have: S110-CF-CO1-EOS post-dates and partially repairs W2-1

This is my entire surviving case, and I will state it without inflation.

Mack's Candidate A-1 (§4 of his R1) correctly diagnosed the W2-1 FAIL: `gap_ratio Δ/μ = 4.82` (runaway, VanHove-dominated frac=1.000) vs physical CFL ≈ 0.05–0.1. He then argued — *correctly given what he cited* — that fixing this is "precisely the move EVOI penalizes when unpinned": you must derive the gap-saturation from the substrate, not impose it to hit 2 M_⊙ (which would be ansatz-forced PASS, PROHIBITED Class 4), and that derivation is "multi-session with no guarantee."

**But that derivation was already attempted, and it landed.** `S110-CF-CO1-EOS` (which mack's R1 does not cite — it post-dates the inv-13 verdicts he read) ran the self-consistent μ_eff(ρ) gate. I verified its three-tuple this round: `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=MARGINAL`. Its value line:

```
M_max=4.783 M_⊙; Δ/μ=0.102 ∈ band[0.03,0.3]; C_max=2.26e-04 (floor 1e-3);
dΔ/dμ>0=True; inv13_runaway_ratio=4.821 -> selfcons=0.102
```

What this changes about mack's argument, precisely:

- **The runaway gap ratio — the named cause of the W2-1 FAIL — is FIXED.** `Δ/μ: 4.821 → 0.102`, now squarely in the physical CFL window [0.03, 0.3]. And it was fixed by a *substrate-honest* move (μ_eff tracks density via the self-consistency loop), **not** by imposing the 2 M_⊙ target. This is exactly the derivation mack's Candidate A-1 said was "multi-session with no guarantee" — and it returned, at INFO grade, with the gap pathology resolved. So mack's "the substrate cannot produce a star above 0.16 M_⊙ in its most natural construction" is superseded: with self-consistent μ_eff the substrate produces M_max = 4.78 M_⊙. The dense-matter axis is **not** stuck at 12× below the floor; it overshoots to ~2× above.

- **But — and this is why I concede the headline — the repair traded one FAIL for an INFO, not for a PASS.** The overshoot (4.78 > 2.6) and the compactness `C_max = 2.26e-4` (still ~3 OOM below NICER's measured C ≈ 0.25) mean the *surface/pressure-scale problem is unsolved*. The S110-CO1 three-tuple is `magnitude=INFO regime=MARGINAL` — the gate itself reports it is marginal. So the honest status is: **the gap-ratio pathology is closed; the surface/compactness pathology is open.** The dense-matter axis advanced one rung (FAIL → INFO) but did not reach a falsifiable M–R.

So my surviving claim is *narrow*: mack's "12× off, no pinned prediction, EVOI ≈ 0" understates the current state by one gate. The accurate state is "FAIL→INFO, one specified pathology fixed, one specified pathology (surface) remaining, ~2–3 waves to a falsifiable M–R." That is more tractable than "invent the sector from scratch," but it is still **one construction wave behind** the growth axis, which is pre-registrable today. I do not claim parity. I claim the gap is "one surface-derivation wave," not "a whole research program from a documented void."

---

## 3. Engaging mack's strongest structural point: Row #88 "cannot be refuted"

Mack's §3 deploys Row #88 — the framework's own self-assessment that on the compact-object surface "the rich ECO observational program *cannot refute it; it can only expose the gap*." This is the deepest point, because if true it zeroes the |ΔP_fail| leg of EVOI. I engage it directly, and I partially concede:

**Where Row #88 is decisive (I concede):** for the *dimensionless-ratio / QNM-echo / shadow* observables, Row #88 is right and WS-CO-1 (S110, STERILE-confirmed) proved it — the parity-even `[J,D_K]=0` forbids the Kerr-degeneracy-breaking operator (the same fact that sets β_iso=0°). That axis is dead. A tensor-echo gate is non-discriminating (Occam favors Kerr). I do not reopen it.

**Where Row #88 over-reaches for the *dimensionful M–R* (my surviving disagreement):** Row #88 says "NO mass-radius relation, NO compactness bound." But S110-CO1 *computed a compactness*: `C_max = 2.26e-4`. That is a number, and it is **observationally decisive against NICER** — not because the substrate predicts a NICER pulsar, but because a substrate compact object with `C ~ 2e-4` is ~3 OOM too dilute to be the `C ≈ 0.25` object NICER measures. This is a genuine falsifier *of a specific structural claim*: "the framework's relay-condensate compact objects are neutron-star-like." NICER's measured compactness *excludes* that. So the fail-leg is NOT ≈0 — it is "the substrate's compact objects are dilute gravastars, not neutron stars," which is a refutable (and currently-refuted-looking) structural statement. The |ΔP_fail| is not zero; it is the information that the substrate lacks a neutron-star branch.

**The catch that makes me concede anyway:** this "falsifier" is a *no-go* (the substrate has no neutron-star branch → NICER excludes the dilute object as a NS), not a *quantitative M–R curve*. A no-go is a weaker EVOI object than a curve, because its |ΔP| is "confirm/deny the substrate has NS solutions," not "measure where on the M–R plane the substrate lives." And mack is right that even this no-go requires the surface-derivation wave to be *certain* the C~2e-4 is structural rather than a missing-surface artifact. Until that wave runs, the no-go is itself provisional.

---

## 4. The honest EVOI re-arithmetic (correcting my R1)

Let me redo the EVOI ordering with mack's correction absorbed and my one seam added:

**Growth axis (f·σ8, DESI→Euclid):**
- P(pass) HIGH — W2-2 already PASS, DESI ~1.0σ → Euclid ~1.5σ/7-bins.
- |ΔP_pass| LARGE — zero-parameter suppression confirmed on a not-built-for dataset (independent-confirmation gold).
- |ΔP_fail| LARGE — measured f·σ8 above the suppressed value at decisive σ cleanly refutes the a₂-growth channel.
- **Pre-registrable TODAY.** EVOI high, both legs large, work-to-falsifiability ≈ 0.

**Dense-matter axis (NICER M–R / compactness), corrected for S110-CO1:**
- P(pass) for a survivable M–R: low-but-not-zero (gap-ratio fixed; surface unsolved; overshoot 4.78). Higher than mack's "structurally near-zero" by one gate, but still not pre-registrable-survivable today.
- |ΔP_pass|: large IF the surface derivation lands a physical C and M_max in band — but that is gated on the surface wave.
- |ΔP_fail|: NOT ≈0 (contra Row #88 read literally) — the C~2e-4 dilute-gravastar no-go is refutable against NICER's C~0.25. But it is a no-go, weaker |ΔP| than a curve, and itself provisional on the surface wave.
- **Pre-registrable in ~2–3 waves**, not today.

**The ordering, honestly:** for the question "which is the higher-EVOI *next pre-registrable* falsifiable prediction," **growth wins** — it is pre-registrable now, both EVOI legs are large, and it has already passed once. The dense-matter axis is one construction wave behind, and that wave's outcome is genuinely uncertain. I move from "leaning Reading A, narrowly scoped" (R1) to "**growth is the higher-EVOI tractable axis; dense-matter is the higher-*leverage* axis whose tractability is one wave short.**"

The only way the ranking flips is if the verdict judges EVOI on "highest information per fixed compute budget" rather than "pre-registrable today" — because the dense-matter surface wave, if it lands, collapses a factor-30 M_max band AND a 3-OOM compactness gap against an already-in-hand dataset (NICER J0740 + Sorensen+ 2024 band), which is arguably a larger single-wave information gain than a 7-bin Euclid χ² that sharpens an already-passing prediction from 1.5σ toward decisive. That is a real but *secondary* consideration, and I flag it as the crux rather than claim it wins.

---

## 5. Why I do NOT fully concede (the residual, stated minimally)

Two facts keep Reading A from being *closed* rather than merely *second*:

1. **The growth PASS sharpens an already-passing prediction; the dense-matter wave decides a binary the framework has never resolved.** Mack's Euclid gate (CF-S113-FSIGMA8-EUCLID-7BIN) is excellent and I endorse it as pre-registrable — but its PASS branch *confirms what already passed* (W2-2), moving the posterior less than a *first-ever* resolution of "does the substrate have a neutron-star branch?" In strict EVOI, confirming an already-passing zero-parameter prediction on a sharper instrument has real but diminishing |ΔP_pass| (the prediction already survived once). The dense-matter surface wave resolves a question with no prior answer — its |ΔP| is undiluted. This is the "information per wave" framing of §4.

2. **The dense-matter axis carries a terrestrial FRIB cross-check the growth axis cannot.** Paper 25 (Sorensen+ 2024): the symmetry energy `L ≈ 40–70 MeV` is constrained by FRIB heavy-ion data at the *same* density range the NICER pulsars probe at the high end. A substrate EoS is testable against *both* the terrestrial L and the astrophysical R_{1.4}/M_max — a multi-messenger, multi-density consistency gate. Growth has no analogous independent terrestrial anchor. This does not make dense-matter pre-registrable-today, but it means its eventual falsifier is *over-constrained* in a way growth's is not.

Neither residual overturns the tractability concession. They bound *how much* I concede: growth is the better *next* gate; dense-matter is not a dead axis, it is a one-wave-deferred axis with a richer eventual falsifier.

---

## (i) Updated honest lean

**I now lean Reading B (growth) for the higher-EVOI *next pre-registrable* prediction — a substantial move from my R1 lean.** Mack's recorded-verdict-pair point (W2-2 PASS / W2-1 FAIL) plus the constructibility asymmetry (growth pinned today; dense-matter one surface-wave short) is correct, and my R1 conflated leverage with tractability. The growth axis is pre-registrable now, bidirectional, and already once-passed; that is the higher-EVOI *next* gate.

I do **not** concede the axes are far apart, and I do not concede dense-matter is dead: S110-CO1 (which mack's R1 predates) fixed the specific pathology that caused the W2-1 FAIL (Δ/μ 4.82→0.102), advancing dense-matter FAIL→INFO with one named pathology remaining (the surface/compactness). Dense-matter is the higher-*leverage*, one-wave-deferred axis with a richer (FRIB-cross-checked, NICER-already-in-hand) eventual falsifier. My final position: **growth is the answer to "what next," dense-matter is the answer to "what is the highest-leverage construction to fund next" — and the verdict must decide which question the EVOI ranking is actually asking.**

## (ii) The single crux the R3 verdict must resolve

**Is the EVOI ranking scored on "pre-registrable-TODAY" or on "highest-information-per-fixed-compute-wave"?**

- If **pre-registrable-today** is the criterion: **growth wins cleanly** — it has a pinned zero-parameter prediction, a σ-budget, an instrument, and an existing PASS; dense-matter needs a surface-derivation wave first. No contest.
- If **highest-information-per-wave** is the criterion: it is **genuinely contestable** — the dense-matter surface wave, if funded, resolves a never-answered binary (does the substrate have a neutron-star branch?), collapsing a factor-30 M_max band and a 3-OOM compactness gap against a dataset already in hand (NICER + FRIB), which is plausibly a larger single-wave |ΔP| than a Euclid χ² that sharpens an already-passing prediction. The growth PASS confirms; the dense-matter wave decides.

That distinction — *pre-registrability-now vs information-per-wave* — is the single hinge. On the first reading the verdict is Reading B by a clear margin (and I concede it). On the second it is close, and the FRIB cross-check + the never-resolved-binary tilt it back toward Reading A. The R3 verdict's job is to fix which EVOI question §EVOI.BF is actually posing.
