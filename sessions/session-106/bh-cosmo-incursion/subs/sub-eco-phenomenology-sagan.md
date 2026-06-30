# ECO Observational Phenomenology — Empirical Status Assessment

**Reviewer**: sagan-empiricist (empirical conscience; "extraordinary claims require extraordinary evidence")
**Mandate**: observational fidelity + FALSIFICATION. State what the data SHOWS vs SUGGESTS vs DOES-NOT-ADDRESS. Hunt for where the observational program *contradicts or constrains* theory.
**Date**: 2026-06-13
**Sources**: 15 papers in `downloads/bh-cosmo/eco-phenomenology/` (read in full via paper-search MCP / pypdf on-disk; every σ-value, p-value, ε-bound below is quoted from the fetched text, not from memory). Framework state verified against knowledge MCP ([T3] Scalar-Tensor Kasparov Decoupling; acoustic white hole S85; GW-falsifier-retirement S96).

---

## 0. Executive verdict (lead with the empirical assessment)

**The single most decisive observational fact**: There is **no statistically robust, independently reproduced detection of gravitational-wave echoes**. The two headline claims use **inconsistent significance conventions** (the 2.5σ GW150914 claim is 2-tailed Gaussian; the 4.2σ GW170817 claim is **1-tailed** Gaussian — verbatim footnotes in each paper), and the original 2.5σ collapses **below 2σ** once a proper trials factor (~20, or O(10)) is applied for the post-hoc reduction of the search window (Ashton et al. 2016, verbatim). The largest claimed number (4.2σ, GW170817) is a windowed search whose authors themselves offer a mundane astrophysical alternative (accretion-disk QPO) for the same signal. An independent LIGO-Virgo GWTC-1 search found **no statistical evidence** for echoes (Cardoso-Pani Living Review §5.12, citing [331]).

**Honest current verdict on GW echoes (SHOWS / SUGGESTS / DOES-NOT-ADDRESS)**:
- The echo data **SHOW** nothing that survives adversarial reanalysis: the defensible significance is **< 2σ** for the O1 BBH events and **disputed** for GW170817.
- They **SUGGEST** (weakly, and only to the proposing group) a tentative feature; the proposers themselves keep the word "tentative" on every claim and concede a non-quantum alternative.
- They **DO NOT ADDRESS** the framework: a *null* echo result is consistent with both "Kerr black holes" AND "horizonless object that produces no tensor-channel echoes" — so the echo channel **cannot discriminate the framework's acoustic-boundary picture at all**, in either direction. This is a no-analog, treated in §4.

**Bottom-line on the field**: The model-independent observational bounds on horizonless objects are real and impressive in some channels (ε ≲ 10⁻⁴⁷ from the GW150914 echo *non*-detection at 90% CL for high reflectivity; ε ≲ 10⁻⁴⁰ from the ergoregion/stochastic-background argument for perfect reflectors). But the canonical Living Review's own thesis is that **"BHs exist" is fundamentally unfalsifiable**, and **no ECO family is observationally excluded** as of 2019 — the program *quantifies how close to the horizon experiments reach*, it does not confirm a horizon.

---

## I. The echoes statistical-status verdict (2016 → 2025), with σ-values and rebuttal logic

### I.1 The claim chain (verbatim significances)

| Paper | Event(s) | Claimed significance | p-value / FAP | σ-convention | Search type |
|:------|:---------|:---------------------|:--------------|:-------------|:------------|
| Abedi-Dykaar-Afshordi 2016 (1612.00266) | GW150914 + GW151226 + LVT151012 (combined) | **2.5σ** | FAP = **1%** | **2-tailed** (footnote a: "1−p = 68%, 95% → 1σ, 2σ") | Echo template, 5 free params, Δt_echo predicted from BH mass/spin |
| Abedi-Afshordi 2018 (1803.10454) | GW170817 (BNS post-merger) | **4.2σ** | FAP = **1.56×10⁻⁵** | **1-tailed** (footnote 1: "1−p = 84%, 98% → 1σ, 2σ") | Cross-correlation, freq window 63–92 Hz a-priori, time window 0–1 s borrowed from Abbott 2017; peak (72 Hz, 1.0 s) fit within windows |
| Abedi-Afshordi-Oshita-Wang 2020 (2001.00821) | "unified picture" | **re-states** 2.5σ and 4.2σ unchanged | — | mixed | reconciliation + EM-coincidence corroboration |

**CRITICAL EMPIRICAL FINDING (the σ-convention switch)**: The 2016 paper explicitly uses **2-tailed** Gaussian (its footnote a). The 2018 paper explicitly uses **1-tailed** Gaussian (its footnote 1). These are quoted verbatim from the two PDFs. A 1-tailed convention makes the *same* p-value look like a *higher* σ. This is not fraud — both are disclosed in footnotes — but it means the headline numbers "2.5σ" and "4.2σ" are **not on the same scale**, and any reader comparing them is being implicitly misled unless they read the footnotes. Lyons (2008, Sagan corpus #17) and Gross-Vitells (2010, #16) are explicit that significance conventions must be stated and held fixed; switching them between two papers in the same series is a Baloney-Detection-Kit red flag.

### I.2 The rebuttal logic (Ashton et al. 2016, 1612.05625 — verbatim)

Ashton et al. (10 LIGO/Virgo-affiliated authors) restate the ADA 2016 combined significance as **2.9σ (p = 3.7×10⁻³); 2.7σ in the one-sided convention** — already marginal. They identify three concrete defects, each pushing the true significance *lower*:

1. **Inconsistent relative amplitudes across events.** The claimed echo SNR is *largest* for LVT151012 — the *weakest* of the three events (1.7σ detection, SNR 9.7). To produce this, the echo amplitude parameter A "would have to be about 2-3 times larger for LVT151012 than for GW150914," which is physically unmotivated.

2. **Parameter railing against priors.** The maximized parameters γ (damping) and t₀ "are found to lie very close to the boundary of [their] prior range, 0.9 and −0.1 respectively" — γ→1 means *non-decaying* echoes (unphysical). Railing means "these values may not be the best fits to the data; if these values are in fact arbitrary, reflecting the priors rather than the data, they cannot be reliably considered as evidence." This is textbook overfitting.

3. **The decisive one — post-hoc window reduction / trials factor.** ADA allowed t_echo to range over ±5%·Δt_echo but found the peak within 0.54%·Δt_echo, then estimated the background over the *full* ±5% range. Ashton: *"A naïve accounting for this post-hoc reduction in the extent of the parameter range would apply a trials factor of about 20 to the number of higher-SNR background samples, **which would reduce the significance below 2σ.** A more sophisticated treatment ... indicates a trials factor of O(10)."*

Ashton's conclusion (verbatim): *"there are sufficient problems with the data analysis methodology ... to cast grave doubt on their claimed significance of a 2.9σ effect ... their current methodology cannot provide observational evidence for or against the existence of near-horizon Planck-scale structure."*

**A second rebuttal axis (energetics)**: Ashton's "very rough calculation" implies the echoes would carry **~0.1 M⊙ (GW150914) and ~0.2 M⊙ (LVT151012)** of energy, versus ~3 M⊙ and ~1.5 M⊙ radiated by the primary signal. Echoes at ~3–13% of the *total* radiated energy are an extraordinary claim demanding extraordinary evidence — and would be hard to hide.

### I.3 The 4.2σ GW170817 claim — anatomy

This is the strongest claim and deserves precise treatment (the prediction-fit distinction matters here):
- **What is genuinely a-priori**: the frequency window (63–92 Hz, Eq. 2.4, derived from BH spin range + Planck-length uncertainty *before* the search) and the time window (0–1 s, *borrowed* from the LVC's own pre-registered post-merger search). The Δt_echo ∝ M·ln(M/M_Pl) scaling is a genuine theory prediction. To the proposers' credit, this is **not** an unbounded post-hoc fit.
- **What is fit**: the *exact* peak (72 Hz, 1.0 s) within those windows; the look-elsewhere correction is done via off-source time-shifted backgrounds inside the windows.
- **The fatal ambiguity (authors' own words)**: *"Could it be that we are simply detecting the QPOs in (a much more massive) post-merger accretion disk?"* and the half-frequency calibration-line worry (LIGO calibration lines at 34–37 Hz ≈ ½ × 72 Hz). A 4.2σ "echo" that the authors *themselves* cannot distinguish from an accretion-disk QPO is not a horizon-structure detection.
- **Method-dependence tension**: the authors note their own p-value is *>2 orders of magnitude* stronger than Conklin-Holdom-Ren's analysis of the *same* event (p = 1/300). Same data, different pipeline, ~100× different significance — a hallmark of an analysis-choice-dominated result, not a signal.

### I.4 The 2020 "status update" — re-statement, not vindication

The 2020 paper (2001.00821) does **not** raise or lower the headline numbers; it re-states 2.5σ and 4.2σ and reframes the critics' deflationary reanalyses (Westerweck p=6%, Nielsen Bayes-factors, Lo, Tsang) as "consistent" with an internal ordering rather than rebutting them. It concedes: *"these similarities do not guarantee that the signals found are the same (or real)"*; the field "remains extremely confusing." The O1 BBH ADA-template searches sit at **few-percent p-values** (combined O1+O2 ≈ 0.047 per Uchikata). The Living Review independently reports that an LVC GWTC-1 search **found no echoes** within 0.1 s of the main burst, and that Ref. [529] found a **Bayes factor favoring noise over the echo hypothesis** for GW150914.

### I.5 Verdict on echoes

| Question | Verdict |
|:---------|:--------|
| Is there a robust echo detection? | **NO.** SHOWS nothing surviving adversarial reanalysis. |
| Defensible significance, O1 BBH | **< 2σ** after proper trials factor (Ashton; trials ~20 or O(10)). |
| Defensible significance, GW170817 | **Disputed**; the 4.2σ is 1-tailed, windowed, and has an authors-acknowledged QPO alternative. |
| Independent reproduction? | **NO** — different pipelines give p from 1.6×10⁻⁵ to "favors noise" on overlapping data. |
| Bayesian read | This is a **low-prior** claim (Planck-scale structure at horizons) with a Bayes factor that does **not** clear "substantial" (10) once look-elsewhere is honest. The proposers' own word — "tentative" — is the correct one, and after 9 years (2016→2025) it has not converted to a confirmation. |

The honest position is the Living Review's: echoes are an *unconfirmed, disputed* feature whose interpretation "is under debate."

---

## II. Mathur's causality argument (Guo-Mathur 2022, 2205.10921) — stated precisely + implications

### II.1 The argument, in three steps (verbatim structure)

Guo & Mathur argue that **detectable tensor-channel echoes are nearly impossible for *any* horizonless model that respects causality** — and therefore that *if* echoes are detected, it would force "a profound change in our understanding of physics." The argument:

**(i) An ECO *can* reflect a GW.** A naive ECO surface a Planck proper-distance s_surface outside R=2GM only lets out a solid angle ~10⁻⁷⁶ around radial (a rough surface scatters into high-l harmonics that the angular-momentum barrier traps). But a *fluid* surface undergoing collective oscillation can specular-reflect: a perfect-fluid shell at proper distance s_shell gives h_reflected ~ (GM₀ s_shell / R²) h_incident, and at the maximum allowed shell energy M₀ ~ (R/s_shell)M this gives **h_reflected ~ h_incident** — a reflected wave "not parametrically smaller than the signal of the primary GW." So far, echoes look possible.

**(ii) Backreaction re-traps the reflected wave.** A pulse of energy E falling onto the ECO raises the total mass to M+E, which forms a **new closed trapped surface (apparent horizon)** at proper distance s_trapped ≈ 4GM^(1/2) E^(1/2) outside R=2GM. For E ~ 0.01M on a solar-mass object (R~3 km), **s_trapped ~ 600 m** — *vastly* larger than the s_shell ≪ R the reflecting surface must sit at (Planckian for fuzzballs). Since s_shell < s_trapped, the reflected pulse "will not be able to emerge out to infinity. The pulse will be swallowed ... its energy will then leak out slowly at the rate of Hawking radiation. Thus there will be no observable echo signal here on earth." The escape is possible "only for GWs composed of just a few gravitons" — undetectable.

**(iii) The only assumption is causality.** Mathur's deepest point: a closed trapped surface forms *first* (forced by causality — N particles falling in radially at c cannot signal each other, so each crosses r=2GM "uneventfully," creating the trapped surface), and *only then*, over a few crossing times, can extended-vacuum-fluctuation ("vecro"/fuzzball) physics convert the interior. **"If we do see echoes, then we would learn something very nontrivial and unexpected about how quantum gravity behaves around black holes."**

### II.2 Implication for horizonless models — and the framework

This is a genuine *constraint* on the whole ECO echo program, not a confirmation of anything. Adversarially:

- **For generic ECOs**: Mathur's argument says the very backreaction that makes a merger remnant massive enough to ring *also* re-traps any reflected wave. If correct, the entire tensor-channel echo-detection program (Cardoso-Pani's "smoking gun") is searching for a signal that causality forbids at detectable amplitude. This *strengthens* the empirical null: not only is there no robust detection, there's a first-principles reason a detectable tensor echo would require new physics.

- **For the framework's acoustic-boundary picture — this may be a NO-ANALOG, and the framework's structure *evades* the argument by a different route.** Press on this carefully:
  - Mathur's argument is about the **gravitational (tensor) sector** — the reflected *gravitational* wave being re-trapped by a *gravitational* apparent horizon formed by the wave's own stress-energy.
  - The framework's [T3] **Scalar-Tensor Kasparov Decoupling** (PROVEN, VdD-Hawking, β_T = 0 *exactly* at linear order, knowledge MCP verified) says the acoustic white hole is a **scalar-sector** structure: the acoustic horizon lives in g_acoustic, while **tensor (GW) modes cross the fold freely on the a₂-emergent metric g_M.** A framework compact object would therefore **not generically reflect a tensor wave at all** — there is no condensate-surface boundary condition *in the tensor channel* for the GW to reflect off.
  - **Consequence**: Mathur's "the reflected wave is re-trapped" is, for the framework, mooted by "there is no reflected tensor wave to begin with." The framework reaches the *same observational endpoint* (no detectable tensor echoes) as Mathur — but via a structurally different mechanism (sector decoupling, not backreaction re-trapping). These are **two independent reasons to expect a tensor-echo null**, which is epistemically interesting but observationally **degenerate** (see §IV.3).
  - **Honest caveat / where the framework should NOT overclaim**: the framework has essentially **no worked compact-object phenomenology** — no computed scalar-channel signature, no ringdown spectrum, no boundary-condition calculation for a framework remnant. The statement "no tensor echoes" is a *structural* prediction (β_T=0), but it has not been turned into a quantitative observable, and the *scalar* sector (where the acoustic horizon does live) has not been worked into any GW or EM signature. Mathur's argument is *quantitative* (he computes s_trapped, h_reflected); the framework's counterpart is *qualitative*. This is a genuine gap — see §IV.2.

---

## III. Per-channel data-status table (SHOWS / SUGGESTS / DOES-NOT-ADDRESS)

For each observational channel, what the *data* currently establishes about **horizon existence** (not what theory hopes). Anchored to the Living Review (Cardoso-Pani 2019, 1904.05363) Table 3 model-independent bounds, plus the 2025 probes.

| Channel | Data status re: horizon existence | Detail (verbatim-anchored) |
|:--------|:----------------------------------|:---------------------------|
| **Ringdown QNM (prompt)** | **SUGGESTS BH; DOES-NOT-ADDRESS horizon directly.** Bounds ε ≲ O(0.01). | GW150914 ringdown consistent with a BH (Living Review Table 3 #2). But "large measurement errors on the QNM frequencies; precise bounds are model dependent." The prompt ringdown is governed by the *photon sphere*, not the horizon — Cardoso-Pani: "the horizon plays no special role in the response of high-frequency waves." A photon sphere is a UCO feature, not a horizon feature. So consistency with a BH ringdown does **not** establish a horizon. |
| **GW echoes (late ringdown)** | **DOES-NOT-ADDRESS** (no robust signal). Strongest *non*-detection bound: ε ≲ 10⁻⁴⁷ at 90% CL for η>0.9. | The echo *non*-detection (GWTC-1, [331]) translates into the tightest ε bound in the field, but **only for high reflectivity η>0.9** and it "deteriorates for smaller η." A null echo result is consistent with (a) a true horizon, (b) a low-reflectivity surface, (c) a no-tensor-echo object (framework). The channel cannot distinguish these — see §IV.3. The *positive* claims (§I) are not robust. |
| **Shadow / EHT (Sgr A*, M87*)** | **SHOWS a photon-sphere-scale dark region; DOES-NOT-ADDRESS horizon.** Bound only ε ~ 1. | Living Review §5.3, Eq. 102: EHT images "consistent with a point source of radius r0 = (2−4)M, or ε ∼ 1." Crucially: "it is extremely challenging to use such an effect to place a constraint much stronger than Eq. (102)." A shadow is cast by the photon sphere (r=3M for Schwarzschild), which **any UCO has** — gravastars and fuzzballs cast shadows too (Sakai-Saida-Tamaki 2014, Cardoso-Pani Fig. 7). The shadow images a photon ring, **not** an event horizon. Gravastars with transparent surfaces show *distinct interior features* (a bright disk + dark ring inside the would-be-dark region; Sakai 2014) — so a shadow is in principle a discriminator, but current resolution does not exclude horizonless models. |
| **TDE non-detection (EM)** | **SHOWS no hard surface for M > 10^7.5 M⊙** (at 99.7% CL), under strong assumptions. ε ≈ 10⁻⁴·⁴. | Living Review §5.1, Eq. 96: absence of optical/UV transients (Pan-STARRS 3π) excludes a hard surface at radius > 2M(1+ε) with ε ≈ 10⁻⁴·⁴ — but "assumes all objects are horizonless, have a hard surface, spherical symmetry, isotropy," and explicitly **excludes boson stars** (weakly interacting matter). |
| **Accretion / Sgr A* luminosity** | **SHOWS ε ≲ 10⁻¹⁴** (no low-luminosity surface re-radiation). | Living Review Table 3 #4. NOTE: the more extreme historical "ε ≲ 10⁻³⁵" claim is **explicitly rejected** by Cardoso-Pani ("the argument has several flaws") — strong lensing breaks the assumed disk-object equilibrium. An empiricist should not cite 10⁻³⁵. |
| **Ergoregion instability / stochastic GW background** | **SHOWS perfect reflectors with ε ≲ 10⁻⁴⁰ are excluded** (absence of stochastic background), for spin above χ_crit ≈ 0.07. | Living Review §4.4.1/§5.5, Table 3 #5. "Perfectly-reflecting horizonless objects must then be unstable." This rules out the *most extreme* (perfect-reflection, Planckian-ε, spinning) mimickers — but assumes "hard surface (perfect reflection); exterior Kerr; all horizonless." Partial absorption restabilizes (Destounis cites Ref. [131]). |
| **Tidal Love numbers (inspiral)** | **DOES-NOT-ADDRESS at current precision.** BH Love number = 0; ECO k ~ 1/\|log ε\|. | Living Review §5.8: ECO TLNs are "only roughly 4 orders of magnitude smaller than for a neutron star ... probably out of reach even with 3G ... would require LISA golden binaries." GW170817 gives *no* ECO ε bound (logarithmic k–ε map makes errors propagate exponentially). Projected LISA EMRI bound ε ≲ exp(−10⁴/ζ) is **forecast-only**. |
| **Tidal heating (inspiral)** | **DOES-NOT-ADDRESS yet.** BH γ=1, perfect reflector γ=0. | Living Review §5.7: a LISA-type detector "will place stringent constraints"; Hawking-area-theorem-type support needs "≈10⁴ LIGO-Virgo detections at 90% CL." Not current. |
| **Multipole moments / no-hair** | **DOES-NOT-ADDRESS strongly.** Current ε ≲ 1; spins compatible with zero. | Living Review §5.6: δφ₂ ≲ 0.3 at 90% CL, but "component spins ... compatible with zero so these constraints cannot be translated into a bound on the spin-induced quadrupole." |
| **Sgr A* NIR flare polarimetry (GRAVITY)** | **DOES-NOT-ADDRESS yet — SUGGESTS future discrimination.** | Aimar et al. 2025 (2506.23931): **SIMULATED** data only; **no fit to real GRAVITY 2018 data; no ECO excluded.** With *current* GRAVITY uncertainties, "none of the metrics model are discernible" (all <log₁₀K> < 1). BH-vs-ECO discrimination is **forecast-conditional on the GRAVITY+ upgrade** (~7× flux sensitivity, service 2026). Even then it gives only a Kerr-vs-ECO verdict, "not ... which specific ECO." Signature is degenerate (see §IV). |
| **QNM spectral stability (theory)** | **DOES-NOT-ADDRESS data; bears on whether ringdown/echo *discrimination* is reliable.** | Destounis et al. 2025 (2509.16310): **theory/numerics only, no data.** Fundamental + long-lived (echo-generating) modes of *ultra-compact* ECOs are **spectrally ROBUST** ("essentially pinned"); overtones are fragile (overtaking instability). But the instability "never becomes a genuine modal instability," and its imprints "manifest in uncharted, late-time territories, where current detectors do not possess the required sensitivity." See §IV.4. |

**Summary read of the table**: *Every* channel that constrains ε tightly (10⁻⁴⁰, 10⁻⁴⁷) does so via a **non-detection** of a *specific* signature (stochastic background from perfect reflection; high-reflectivity echoes) under **strong model assumptions** (hard surface, perfect reflection, exterior Kerr). The channels that probe the *generic* near-horizon region with *current data* (shadow, ringdown) bound ε only at ~1 to ~0.01 and image the *photon sphere*, not the horizon. **No channel directly observes a horizon**; the Living Review is explicit that none can ("there is no direct observable associated to the horizon").

---

## IV. FALSIFICATION / TENSION

### IV.1 (a) Where does the observational program CONTRADICT a theoretical ECO claim?

**Yes — there is a clean, decisive observational contradiction of a specific ECO claim**, and it is the most rigorous result in this corpus:

- **Chirenti-Rezzolla 2007 (0706.1513)** showed gravastars are stable to axial perturbations and that their QNM spectrum *differs* from a same-mass BH (same oscillation frequency achievable, but **different decay time**) — "can be used to discern, beyond dispute, a gravastar from a black hole."
- **Chirenti-Rezzolla 2016 (1602.08759, "Did GW150914 produce a rotating gravastar?")** then applied this to real data and found (per the index #04, "the key negative result") that **the GW150914 ringdown cannot be modeled as a rotating gravastar**. This is a genuine data-vs-theory falsification of a *specific* mimicker for a *specific* event.

This is the program working *correctly*: a horizonless model made a quantitative ringdown prediction, and the data ruled it out for that event. Note the asymmetry (Cardoso-Pani's Popper-black-swan thesis): the data **falsified a gravastar**, it did **not confirm a horizon**.

A second contradiction: **Cardoso-Hopper-Macedo 2016 (1608.08637)** found that head-on collisions of *ultracompact* boson stars compact enough to mimic a BBH up to merger **exceed the max boson-star mass and collapse to a BH** — so "the coalescence of compact boson stars might be almost indistinguishable from that of black-holes." This *contradicts* the optimistic claim that all ECOs leave a clean echo signature: the most BH-like ECOs may simply *become* BHs on merger.

### IV.2 (b) Is the ECO program MORE rigorous / more predictive than the framework's compact-object treatment? Should the framework own this gap?

**Yes, unambiguously, and yes the framework should own it.** Adversarial honesty requires stating this plainly:

- The ECO program is **vastly more developed** in compact-object phenomenology. It has: a quantitative taxonomy (UCO/ClePhO thresholds ε<1/2, ε≲0.019; Living Review §2.1.5), a master model-independent bounds table (Table 3, 7 channels with numerical ε limits and per-row caveats), specific falsifiable QNM predictions (Chirenti-Rezzolla), worked echo templates with parameter counts (Cardoso-Hopper; the ADA 5-param template), a causality theorem (Mathur), a pseudospectral stability analysis (Destounis), and a forecast polarimetry discriminator (Aimar). Each result states its assumptions and its falsification condition.
- The **framework has essentially no compact-object phenomenology**. It has a *structural* claim ([T3]: acoustic white hole is scalar-sector, β_T=0, tensors cross freely) and a *cosmogenesis* acoustic-white-hole (S85, a one-time transit event, NOT an astrophysical stellar-collapse remnant). It has **not** produced: a framework-remnant ringdown spectrum, a scalar-sector boundary-condition calculation, a predicted (scalar) echo or its absence as a *number*, a shadow prediction, or any quantitative observable for an astrophysical compact object. The S85 acoustic white hole is a *cosmological* fold transit, not a model of a 3-km stellar-mass object that LIGO would ring.
- **The framework should own this as a genuine gap, not paper over it.** The honest framing: the framework makes *one* structural prediction relevant to compact objects (no generic tensor-channel echoes, from sector decoupling), and that prediction is **observationally vacuous at present** because the tensor-echo data are themselves null (§IV.3). It does not have a worked compact-object program, and it should not pretend the GW-falsifier-retirement (S96, walls=0 EXACT, falsifier migrated GW→LSS) *substitutes* for one — those are different physics (cosmological domain walls, not compact-object remnants). The correct posture per the Sagan standard: **the framework is silent on astrophysical compact-object phenomenology, and that silence is a gap relative to a mature observational program, not a strength.**

### IV.3 (c) The framework's "no tensor echoes" prediction vs the (null) echo data — does it discriminate?

This is the sharpest empirical question in the prompt, and the answer is **no, it does not discriminate — and the framework must not claim it does.** The logic, laid out as a truth table:

| Hypothesis | Predicts tensor echoes? | Consistent with null echo data? |
|:-----------|:------------------------|:--------------------------------|
| Kerr black hole (GR) | No (horizon absorbs) | **YES** |
| Framework acoustic object (β_T=0, scalar-only) | No (no tensor reflection) | **YES** |
| Generic high-reflectivity ECO | Yes | **NO** (would have been seen; ε≲10⁻⁴⁷ excludes high η) |
| Low-reflectivity ECO | Weakly | YES (echoes below detection) |

A null tensor-echo result is consistent with **both** "Kerr" and "framework scalar-only object." Therefore the null **cannot distinguish the framework from standard GR black holes in this channel.** This is a **DOES-NOT-ADDRESS** for the framework, in both directions:
- The null does **not** confirm the framework (Kerr explains it equally well — Occam's razor actually *favors* Kerr here, since it requires no new sector structure).
- The null does **not** refute the framework (the framework predicts exactly this null).
- A *positive* robust echo detection **would** refute the framework's generic-scalar-only picture (the framework predicts NO generic tensor echoes) — *and* would simultaneously vindicate Mathur's "profound new physics" warning. But no such robust detection exists.

**The framework's tensor-echo prediction is currently unfalsifiable-by-confirmation and unconfirmable** — it lives in the same epistemic box as "BHs exist" (Cardoso-Pani's unfalsifiable statement). It is a *consistent* structural feature, but it is **not evidence for the framework**, and presenting it as such would violate the prediction-fit distinction (it is not even a fit — it is an accommodation that any horizonless-scalar OR any-true-horizon model also produces).

**One place the framework's structure is genuinely distinctive (and worth a future computation)**: Mathur's causality argument re-traps the *tensor* reflected wave, but says nothing about a *scalar* channel. The framework's acoustic horizon lives precisely in the scalar sector. So the *one* discriminating question is whether a framework compact object would produce a **scalar-channel** signature (scalar GW polarization, extra-polarization modes — Cardoso-Pani §VIa note such modes "could be another indication of new physics"). The framework has not computed this. **If** it predicts a specific scalar-polarization echo or its absence, *that* would be a falsifiable, framework-distinctive observable — unlike the tensor null. This is the actionable gap.

### IV.4 (d) Does Destounis spectral instability undercut echo/ringdown discrimination?

**Partially, but not fatally — and importantly it does NOT rescue the echo program either.** Destounis et al. 2025 (verbatim-extracted):
- **Robust**: the fundamental QNM and the long-lived **echo-generating interior modes** of *ultra-compact* ECOs are "essentially pinned" — unaffected by environmental bumps in any astrophysically plausible range. So the in-principle echo-discrimination program for ultra-compact objects is *not* destroyed by spectral instability.
- **Fragile**: overtones undergo a repetitive "overtaking instability" (exterior trapped modes metamorphose into "perturbed fundamental modes"), which "would be invisible to a purely modal analysis" and could "complicat[e] attempts to use BH spectroscopy as a precision test of GR."
- **But**: "their imprints usually manifest themselves in uncharted, late-time territories, where current detectors do not possess the required sensitivity." And it "never becomes a genuine modal instability" — ECOs are "spectrally fragile yet modally robust."

**Empirical read**: Destounis is a *theory* result (idealized non-rotating Schwarzschild-exterior reflective ECO + by-hand Gaussian bump, scalar ℓ=2, no data). It tells us (i) overtone-based BH spectroscopy is environment-sensitive (a caution for *all* ringdown discrimination, BH or ECO), and (ii) the discrimination-relevant *fundamental/long-lived* modes of ultra-compact objects survive. It neither rescues the (null) echo claims nor refutes the discrimination program — it relocates the systematic-uncertainty frontier to late times beyond current sensitivity. For the framework: irrelevant in the tensor channel (β_T=0, no tensor QNM cavity); potentially relevant to any *scalar*-channel signature the framework might compute, where overtone instability would be an additional systematic.

### IV.5 Cross-framework FALSIFICATION summary

- **The ECO program contradicts**: a specific gravastar model for GW150914 (Chirenti-Rezzolla 2016); the universal-clean-echo expectation (Cardoso-Hopper: compact boson stars collapse to BHs). It does **not** contradict the framework — because the framework makes no quantitative compact-object prediction to contradict.
- **The framework is constrained-but-not-tested**: its only relevant structural claim (no tensor echoes) is observationally consistent with the null data but **non-discriminating**. The framework owns a real **phenomenology gap** here.
- **No observational fact in this corpus supports the framework over standard GR** for compact objects, and none refutes it. The honest status is **NEUTRAL / DOES-NOT-ADDRESS**, with one actionable opening (compute a scalar-sector signature).

---

## V. Scorecard (Sagan standard)

| Claim | Status | Free params | Testable prediction | Falsification criterion | Verdict |
|:------|:-------|:------------|:--------------------|:------------------------|:--------|
| GW echoes detected (ADA 2.5σ, O1 BBH) | **fit/accommodation** | ≥5 (template) + post-hoc window | yes (echo train) | reproduce at >5σ with a-priori template | **FALSIFIED-AS-CLAIMED** (< 2σ after trials, Ashton) |
| GW echoes detected (4.2σ, GW170817) | **windowed fit** | windows a-priori, peak fit | yes | independent reproduction | **NOT ROBUST** (1-tailed σ; QPO alternative; 100× method-dependence) |
| Echoes are universal for photon-sphere objects (Cardoso-Hopper) | **theory prediction** | 0 (test-particle) | yes (echo delay ∝ M ln(M/M_Pl)) | non-detection at design sensitivity | **SOUND THEORY, UNCONFIRMED** |
| Mathur causality: no detectable tensor echoes | **theorem** | 0 (causality only) | yes (echo → new physics) | a robust echo detection | **STRONG ARGUMENT; consistent with null data** |
| Gravastar QNM ≠ BH QNM (Chirenti-Rezzolla) | **prediction** | model params | yes (decay time) | matched-filter ringdown | **CONFIRMED-DISCRIMINATOR; gravastar excluded for GW150914** |
| ε ≲ 10⁻⁴⁷ (echo non-detection) | **bound from null** | reflectivity η | n/a (it's a limit) | — | **VALID at η>0.9 only** |
| ε ≲ 10⁻⁴⁰ (ergoregion/stochastic) | **bound from null** | perfect reflection assumed | n/a | — | **VALID for perfect reflectors** |
| Sgr A* flare polarimetry discriminates ECO/BH | **forecast** | hot-spot model | yes (Q/I, U/I time-dep) | GRAVITY+ data 2026+ | **SUGGESTS-ONLY; simulated, degenerate, forecast-conditional** |
| Destounis: ultra-compact fundamental modes robust | **theory** | reflectivity, bump | yes (mode migration) | late-time ringdown (future) | **THEORY-ONLY; relocates systematics to late times** |
| Framework: no generic tensor echoes (β_T=0, [T3]) | **structural prediction (PROVEN internally)** | 0 | qualitative only | a robust tensor echo | **CONSISTENT-BUT-NON-DISCRIMINATING; degenerate with Kerr** |
| Framework: compact-object phenomenology | **ABSENT** | — | none | none | **GAP — framework should own it** |

---

## VI. What the framework should do (constraint-map, not advocacy)

Pre-registered, falsifiable openings (the only things that would *move* a probability estimate):

1. **Compute a scalar-sector compact-object signature.** The framework's acoustic horizon lives in the scalar sector (β_T=0 sends tensors through freely). Mathur's causality re-trapping is a *tensor*-sector argument. The *one* discriminating, framework-distinctive observable would be a **scalar-channel** signature (scalar-polarization GW mode, or its predicted absence). This is the actionable gap. Pre-registration: does a framework remnant produce a scalar-polarization echo with a specific Δt, or none?
2. **Own the no-tensor-echo prediction as non-discriminating.** Do NOT cite the null echo data as support — it is equally explained by Kerr (Occam disfavors the framework here). The correct registry status is DOES-NOT-ADDRESS.
3. **Do not conflate GW-falsifier-retirement (S96, cosmological walls) with compact-object phenomenology.** Different physics. The framework remains silent on astrophysical compact objects; that silence is a gap.
4. **The decisive external check is GRAVITY+ (2026) and 3G/LISA ringdown** — but these test ECOs generically, not the framework specifically, until (1) yields a number.

---

## VII. Provenance

All σ-values, p-values, ε-bounds, and verbatim quotes are sourced from the on-disk PDFs in `downloads/bh-cosmo/eco-phenomenology/` (read via paper-search MCP `read_arxiv_paper` for new-style IDs and pypdf for old-style on-disk IDs), per `feedback_research-corpus.md` (no citation from training knowledge). Framework facts ([T3] β_T=0; acoustic white hole S85; GW-falsifier-retirement S96) verified live against the knowledge MCP.

**Gaps / NOT FOUND, marked explicitly**:
- The Living Review does **not** quote "2.5σ"/"4.2σ" numerically (summarizes the dispute via "Bayes factor favoring noise" + GWTC-1 null); those σ-values come from the primary ADA papers, quoted directly.
- The Living Review gives **no single closed-form |R|² < X** reflectivity bound (renders it as η>0.9 @ 90% CL + the ergoregion exclusion region in Figs. 17–18).
- The Aimar paper performs **no fit to real GRAVITY archival data** (simulated datasets only) — explicitly verified absent.
- Chirenti-Rezzolla 2016 (GW150914-not-a-gravastar, #04) and Conklin-Holdom-Ren 2017 (#09) were read via the index summary + cross-citations in the fetched primary texts, not opened in full this pass — their conclusions as stated are anchored to the index (#04 "key negative result") and to Abedi-Afshordi 2018's own comparison to [12] (p=1/300). Flagged as a partial read.
