# Session 96 Workshop W-3 — The Acoustic Ω_GW Spectral Shape

**Date**: 2026-05-30
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: little-red-dots (little-red-dots-jwst-analyst), mack (mack-cosmic-bridge)
**Source Documents**:
- sessions/archive/session-96/session-96-w6-workingpaper.md
- computations/session-96/s96_gate_verdicts.txt

**Focus Topics** (the Ω_GW spectral-shape contradiction):
1. The −127.4 OOM contradiction: W6-3 (FAIL) places the CGWB peak at 8.4835e39 Hz with an f³ IR tail; W6-4 (PASS) reports a flat 1e-10 plateau AT the LISA pivot. Under f³, the LISA-band value would be ~10⁻¹³⁷.
2. Is "peak at 10⁴⁰ Hz" (W6-3) even COMPATIBLE with "flat plateau in LISA band" (W6-4), or is one gate's slope framing internally wrong?
3. The Omega_GW_Lambda_A_LISA=1e-10 pin provenance problem (no knowledge-MCP entry; S86/S87 computed it via near-pivot interpolation W6-3 invalidated).
4. Cross-Cutting — does ANY a(t)-independent LISA GW falsifier survive D4? (§7.2 flagship at stake)

---

## Round 1 — little-red-dots: Opening Analysis

### L1: The −127.4 OOM contradiction (peak placement + f³ tail vs flat plateau)

**Key finding (Sage-exact): the two W6 gates jointly imply Ω_GW(LISA) ~ 10⁻¹³⁷·³⁵, which is 80.27 OOM below the (C)-class floor and 124.35 OOM below LISA-PLS — so the flagship `Ω_GW^(A) = 1e-10` AT 3 mHz (W6-4) and the peak at 8.4835e39 Hz with an f³ IR rise (W6-3 + W6-4 discriminator table) cannot both be true. One of the two numbers is wrong; the steelman of MY side (the peak owner) is that the AMPLITUDE is the casualty.**

**The substrate-IS spectrum.** Hold the chain substrate-first: the CGWB IS the acoustic readout of the van Hove fold DOS transduced into the tensor sector — `D_K eigenvalues → van Hove fold (DOS divergence, group velocity → 0) → squeezed-graviton acoustic emission at the fold characteristic frequency → redshift by a(τ_fold)/a(τ_now) → observed Ω_GW(f)`. The spectrum is NOT primordial GW in a container; it is one emission feature with one peak frequency and a causal low-frequency rise. The two structural facts the W6 gates pinned are:

1. **Peak frequency (W6-3, FAIL, `audit_sha256=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e`, verdict line 155).** `f_obs(κ_nat) = f_emit · a_fold/a_now = 1.7962e40 · 0.472291 = 8.4835e39 Hz`, where `a_fold/a_now = 1/(a_fold/a0) = 1/2.117340 = 0.472291` from gate-5's directly-resolved `a_fold/a0 = 2.1173` (`s54_scale_factor.npz`; `s96_obs_lrd_assembly_clock.npz`), and `f_emit = M_KK/(2π)` at `κ_nat = ħ/M_KK = 8.860440e-42 s` (= canonical `M_KK_inv_seconds`). This is **43.93 decades above the LISA low edge (1e-4 Hz)** and robust across the entire swept κ-band [1e-20,1e-10] (121/121 points GHz+).

2. **LISA-band amplitude + IR slope (W6-4, PASS, `audit_sha256=a9998118fdcb96bd41ebae88b0c2af0d5c4fb0c7c6d9bc277b62a50e10a0d382`, verdict line 136).** Discriminator table (§W6-4 (E), w6-workingpaper.md L240-247): the acoustic class is "broad, causal **f³ IR → flat plateau in LISA band**", "Peak location **near LISA pivot**", LISA-band amplitude `Ω_GW^(A) ≈ 1e-10`. The `1e-10` is the Sage-exact `1/10¹⁰`.

**The substitution chain (the −127.4 OOM contradiction).** Take the two facts literally. A causal f³ IR rise means `Ω_GW(f) = Ω_peak · (f/f_peak)³` for `f ≪ f_peak`. The LISA pivot `f_LISA = 3 mHz = 3/1000 Hz` is 42.45 decades below the W6-3 peak:

```
Step 1:  f_LISA / f_peak = (3/1000) / 8.4835e39                         [definition]
Step 2:  log10(f_LISA / f_peak) = −42.451454                            [Sage-exact, QQ-coerced]
Step 3:  f³ suppression at LISA = 3 · log10(f_LISA/f_peak) = −127.35436 OOM   [f³ IR slope]
Step 4:  IF the spectral PEAK carries Ω_peak = 1e-10 (i.e. peak amplitude = flagship):
            log10 Ω_GW(LISA) = log10(1e-10) + 3·log10(f_LISA/f_peak)
                             = −10 + (−127.35436) = −137.35436
         ⇒ Ω_GW(LISA) ~ 10⁻¹³⁷·³⁵                                       [Sage-exact]
Step 5:  vs (C)-class floor log10 Ω^(C) = log10(8.299e-58) = −57.080974:
            OOM below (C)-floor = −57.08 − (−137.35) = 80.27 OOM
         vs LISA-PLS ~ 1e-13: OOM below PLS = −13 − (−137.35) = 124.35 OOM
Conclusion: a peak at 8.4835e39 Hz with an f³ IR rise that hits 1e-10 AT the peak
            lands ~10⁻¹³⁷ at 3 mHz — 80 OOM below even the Companion-null (C)-floor,
            124 OOM below LISA's own sensitivity. LISA would see NOTHING.
```

This reproduces the workshop pre-registered figures exactly (−127.4 OOM; ~10⁻¹³⁷). The contradiction is not a rounding artifact — it is 127 orders of magnitude.

**Steelman of my side (peak owner): the AMPLITUDE is the casualty, not the peak.** The W6-3 peak placement is the more defensible of the two numbers, for three reasons that map directly onto how I reason about high-z sources and detector bands:

- **(a) The peak is DERIVED from a closed redshift chain; the amplitude is INTERPOLATED.** W6-3's `f_obs` consumes two pinned inputs — `a_fold/a0 = 2.1173` (gate-5 directly-resolved, no extrapolation) and `f_emit = M_KK/(2π)` (the substrate's only intrinsic frequency scale). W6-4's `Ω_GW^(A) = 1e-10` carries NO knowledge-MCP provenance (I verified: `get_constant('Omega_GW_Lambda_A_LISA')` → "No PROVENANCE entry"); the W6-4 MCP audit records it as "S87; substrate-physics OOM estimate at LISA 3 mHz" — i.e. it was placed AT the pivot by a band-localized interpolation that presupposed the peak is near the pivot (the discriminator table literally says "Peak location near LISA pivot"). That presupposition is exactly what W6-3 refuted. When a detector-band reasoner sees a redshift-chain-derived frequency vs an interpolated amplitude that assumed the frequency, the redshift chain wins. This is the same discipline I apply to LRD black-hole masses: a virial mass from a measured broad-line width + a measured continuum luminosity is more defensible than a mass inferred from an SED template that assumed the AGN fraction it was trying to measure.

- **(b) "Near LISA pivot" and "8.4835e39 Hz" are 42 decades apart — they are the SAME quantity (the peak frequency) computed two ways, and only one was computed from the substrate.** The W6-4 discriminator row "Peak location: near LISA pivot (fold acoustic scale)" is a PROSE assertion; W6-3's `8.4835e39 Hz` is the same fold acoustic scale carried through the actual redshift factor. They disagree by `log10(8.4835e39 / 3e-3) = 42.45` decades. W6-4 never ran the redshift chain — its MCP audit shows it searched for the amplitude, not the frequency, and `search_knowledge('CGWB peak frequency …')` in W6-3 confirms "No prior gate derives the OBSERVED peak FREQUENCY via the substrate redshift chain — this gate is the first." So the "near pivot" claim has no derivation behind it; the 8.4835e39 Hz does.

- **(c) The redshift factor is the ONE piece that is normalization-independent.** `a_fold/a_now = 0.472291` is a pure ratio of Connes-distance scale factors — it does NOT depend on the open M_KK⁻¹→s knob. The emission-scale magnitude (`f_emit`) depends on κ, but as W6-3 showed, the verdict is GHz+ across the *entire* swept band; reaching LISA needs `κ = 25 s/M_KK⁻¹`, 42.5 OOM from natural and 11.4 OOM beyond the band. So the peak's placement far above LISA is robust to the one free parameter, whereas the amplitude `1e-10` was tuned at a single pivot under a false frequency assumption.

**Structural implication for capstone §7.2.** If my steelman holds, the §7.2 GW flagship as historically stated ("Ω_GW ~ 1e-10 peak in the LISA mHz band, 11+ OOM above LISA-PLS") is doubly broken: the peak is 44 decades too high (W6-3), AND the `1e-10` was the amplitude AT a pivot that was wrongly assumed to be the peak — so under the resolved shape the actual LISA-band tail amplitude is ~10⁻¹³⁷, not 1e-10. W8-2 scope-corrected the PROSE ("LISA samples the IR tail", Row #7.audit-2) but did NOT recompute the tail amplitude — leaving `Omega_GW_Lambda_A_LISA = 1e-10` standing on the inventory as if it were the IR-tail value when by the f³ chain it is 127 OOM too large. That is the open wound this workshop must close.

**Questions for mack:**
1. You own the S86/S87 amplitude. Was `Ω_GW^(A) = 1e-10` ever computed as the spectral PEAK amplitude (a height), or only as the value of the spectrum AT 3 mHz under a band-localized interpolation? If the latter, what frequency did that interpolation assume the peak sits at — and was it 3 mHz (now refuted by W6-3) or 8.4835e39 Hz (in which case 1e-10 is the peak height and the IR tail at 3 mHz is ~10⁻¹³⁷)?
2. Is the f³ IR slope in the W6-4 discriminator table a DERIVED causal-rise exponent, or an assumed Hiramatsu-class shape inherited from the wall-spectrum lore? If derived, the −127.4 OOM follows necessarily; if assumed, can you produce the actual acoustic IR slope from the fold DOS?
3. Do you accept that the peak-frequency datum (redshift-chain-derived, normalization-robust) outranks the amplitude datum (interpolated, provenance-less) in the evidence hierarchy — or is there an S86/S87 derivation of `1e-10` I have not seen that makes it the more defensible number?

### L2: Is "peak at 10⁴⁰ Hz" compatible with "flat plateau in LISA band"?

**Key finding: W6-4's OWN discriminator table is internally inconsistent. It asserts BOTH "f³ IR → flat plateau in LISA band" AND "Peak location: near LISA pivot (fold acoustic scale)" for the acoustic class (w6-workingpaper.md L242-243). A causal f³ rise and a flat plateau are different spectral regions; a flat plateau IN the LISA band cannot coexist with a peak at 8.4835e39 Hz (44 decades above LISA) unless the spectrum is flat from 3 mHz all the way up — which contradicts f³. The "flat plateau in LISA band" phrasing is the internally-wrong element, and it is the SAME element that generated the bogus `1e-10` LISA amplitude.**

**The three mutually-incompatible claims.** Lay W6-4's acoustic-class row out as a spectral-shape specification and the inconsistency is structural, not semantic:

| Claim | Source | What it asserts about Ω_GW(f) near LISA |
|:------|:-------|:----------------------------------------|
| (i) "broad, causal f³ IR" | W6-4 disc. table, L242 | `Ω_GW ∝ f³` for `f ≪ f_peak` — STEEPLY RISING in the LISA band |
| (ii) "→ flat plateau in LISA band" | W6-4 disc. table, L242 | `Ω_GW ≈ const ≈ 1e-10` at 3 mHz — FLAT in the LISA band |
| (iii) "Peak location near LISA pivot" | W6-4 disc. table, L243 | the maximum of Ω_GW(f) is AT ~3 mHz |

(i) and (ii) describe the SAME frequency region (the LISA band, [1e-4,1e-1] Hz) with INCOMPATIBLE slopes: a spectrum cannot be both `∝ f³` and `≈ const` over the same decade. And (iii) is incompatible with W6-3's `f_peak = 8.4835e39 Hz` — the two cannot both be the peak location when they are 42.45 decades apart (a flat spectrum has no peak; if there IS a peak it is at 8.4835e39 Hz, not at the pivot).

**Which claim is the wrong one — substrate-first adjudication.** The substrate has exactly one emission feature (the van Hove fold), hence exactly one peak. W6-3 derived that peak's observed frequency from the redshift chain: 8.4835e39 Hz. Therefore claim (iii) ("peak near LISA pivot") is FALSE — refuted by the directly-resolved redshift factor. Given (iii) is false, the LISA band sits 42.45 decades into the IR TAIL of a peak at 8.4835e39 Hz. In the deep IR tail, the causal slope (i) governs: `Ω_GW ∝ f³`, rising. So claim (i) is the physically-correct LISA-band behavior; claim (ii) ("flat plateau in LISA band") is FALSE — there is no plateau in the LISA band, because LISA is 42 decades below the peak where the spectrum is still climbing as f³.

This is a "buried-choice" failure of exactly the kind I flag in LRD photometric selection: a discriminator table presented "flat plateau at 1e-10" as the headline LISA-band number, but that headline silently assumed the peak is near the pivot (the plateau is the region NEAR the peak, where the spectrum has turned over and is flat-to-slowly-falling). Strip the false peak-location assumption and the plateau vanishes — what is actually in the LISA band is the steep f³ tail, whose value at 3 mHz is ~10⁻¹³⁷ (L1), not 1e-10.

**The internal-inconsistency verdict.** W6-3 (FAIL) and W6-4 (PASS) are NOT "different observables of the same spectrum that happen to both be right," as the W6 synthesis framed it (w6-workingpaper.md L432: "LISA samples the deep-IR Ω_GW tail amplitude (survives, W6-4), NOT the spectral peak frequency"). That framing is itself the error: it treats `Ω_GW^(A) = 1e-10` as "the IR tail amplitude," but `1e-10` was computed as a near-pivot plateau value under the assumption the pivot is near the peak. It is NOT the IR-tail amplitude — the IR-tail amplitude at 3 mHz under the resolved shape is ~10⁻¹³⁷. So W6-4's PASS is sound on its narrow operator (`Ω_GW^{walls} = 0` EXACTLY via π₀(U(1))=0 — that topological result is untouched), but the `1e-10` LISA-band amplitude attached to it inherits the false flat-plateau-at-the-pivot framing and is NOT consistent with W6-3's peak placement.

**Structural implication.** The §7.2 flagship and the W6-4 discriminator table both need the LISA-band acoustic spectrum re-specified as: peak at 8.4835e39 Hz (W6-3); LISA band is the f³ IR tail 42 decades below; LISA-band amplitude ~10⁻¹³⁷ (NOT a 1e-10 plateau). The "flat plateau in LISA band" cell is internally wrong and must be retired. The wall=0 topology and the (A)/(C) regulator-class split machinery (47.081 OOM) are SEPARATE results that survive — but neither rescues a 1e-10 LISA amplitude once the peak is 44 decades away.

**Questions for mack:**
1. Do you agree that "flat plateau in LISA band" (W6-4 L242) is the internally-inconsistent cell — that a flat plateau is the NEAR-PEAK region, so placing it in the LISA band silently re-asserts the (refuted) "peak near pivot" claim?
2. Your W6-4 PASS rests on `Ω_GW^{walls} = 0` (topology) — which I do not contest. But the `Ω_GW^(A) = 1e-10` amplitude is a SEPARATE deliverable of the same gate. Will you concede that the amplitude leg and the wall-topology leg can be split, with the wall=0 PASS retained and the 1e-10 LISA amplitude re-opened?
3. Is there a fold-DOS derivation under which the LISA band is genuinely in the PLATEAU (turned-over) region rather than the f³ tail — i.e. is there any normalization where the peak redshifts INTO or below the LISA band? W6-3 says no (κ = 25 s needed, 11.4 OOM beyond band) — do you have a counter?

### L3: The Omega_GW_Lambda_A_LISA pin provenance problem

**Key finding: `Omega_GW_Lambda_A_LISA = 1e-10` carries NO knowledge-MCP provenance (I verified directly: `get_constant('Omega_GW_Lambda_A_LISA')` → "No PROVENANCE entry"), and the only recorded basis (W6-4 MCP audit: "S87; substrate-physics OOM estimate at LISA 3 mHz") is a band-localized-AT-pivot interpolation that presupposed the peak is near 3 mHz — the exact assumption W6-3 refuted. The pin is a Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL defect (OOM estimate, substrate canonical absent) AND a stale-source defect (the interpolation rests on a superseded peak-location assumption). My disposition: it must be RE-PINNED, not silently retired — but re-pinned to the IR-tail value under the RESOLVED shape (~10⁻¹³⁷ at 3 mHz), with the `1e-10` demoted to the spectral PEAK HEIGHT if and only if mack confirms 1e-10 was ever a peak height rather than a pivot interpolation.**

**The provenance audit (three independent defects).** Per `substrate-first-canonical-sourcing.md §(v)` and `epistemic-discipline.md §"Source Reconciliation"`, the pin fires THREE classes simultaneously:

1. **Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL.** The recorded basis "substrate-physics OOM estimate at LISA 3 mHz" matches the placeholder pattern (`OOM estimate`). A substrate canonical for the LISA-band acoustic amplitude does not exist as a derived quantity — W6-4's own audit shows it was an estimate, and W6-3 (`search_knowledge('CGWB peak frequency …')`) confirms "No prior gate derives the OBSERVED peak FREQUENCY via the substrate redshift chain." So there is no first-principles LISA-band amplitude on disk; `1e-10` is the placeholder.

2. **Class-(c) PIN-DRIFT-FROM-STALE-SOURCE.** The interpolation that produced `1e-10` was "band-localized AT pivot," which presupposes the spectral peak is near 3 mHz (W6-4 discriminator table: "Peak location near LISA pivot"). W6-3 is a SUPERSESSION EVENT: it derived the peak at 8.4835e39 Hz, 42.45 decades above the pivot. The pin therefore drifts from a source whose load-bearing assumption (peak-near-pivot) the W6-3 verdict disproved — structurally analogous to the η-invariant stale-source instance in `regulator-pin-discipline.md §"Class-(c) … Calibration Corpus Extension"` (a threshold testing a hypothesis a later Bulletin disproved).

3. **The −127.4 OOM internal-consistency violation (L1).** Even granting the placeholder, `1e-10` AT 3 mHz is inconsistent BY 127 ORDERS with the f³-tail value implied by the W6-3 peak + the W6-4 IR slope. A pin cannot simultaneously be the flat-plateau value at 3 mHz (1e-10) and sit on a spectrum whose f³ tail gives ~10⁻¹³⁷ at 3 mHz. One of the two is wrong; the provenance-less one is `1e-10`.

**Re-pin vs retire — the disposition.** RETIRE (delete the pin, drop the falsifier row) is the wrong move because it would erase a real substrate observable — the CGWB IR-tail amplitude at the LISA pivot IS a well-defined substrate quantity (it is `Ω_peak · (f_LISA/f_peak)³`); it is just ~10⁻¹³⁷, not 1e-10. RE-PIN is correct, but the re-pin target depends on what `1e-10` actually was:

- **Case A — `1e-10` was a near-pivot PLATEAU interpolation (peak assumed at ~3 mHz).** Then it is simply WRONG (the peak is at 8.4835e39 Hz), and the canonical LISA-band amplitude must be re-pinned to the f³-tail value: `Ω_GW(3 mHz) = 1e-10 · (3e-3/8.4835e39)³` IF 1e-10 is the peak height, OR computed directly from the fold DOS. The Sage-exact tail value is `10^(−137.354)` if the peak height is 1e-10. The `1e-10` survives ONLY as a relabeled **peak-height** constant (`Omega_GW_acoustic_peak`, at f = 8.4835e39 Hz), NOT as a LISA-band amplitude.

- **Case B — `1e-10` was genuinely the spectral PEAK HEIGHT (a maximum amplitude), and someone mistakenly attached it to the LISA pivot.** Then the constant's VALUE is fine but its FREQUENCY LABEL is wrong: it should be re-pinned as `Omega_GW_acoustic_peak = 1e-10 at f_peak = 8.4835e39 Hz`, and a NEW constant `Omega_GW_acoustic_LISA_tail ~ 10⁻¹³⁷` (the f³-tail value at 3 mHz) replaces it on the §7.2 LISA row.

In BOTH cases the §7.2 LISA-row amplitude becomes ~10⁻¹³⁷ (detector-sterile), and `1e-10` migrates to a peak-height label at 8.4835e39 Hz. The mack adjudication (L1 Q1) decides which case. Either way, the current pin — `1e-10` tagged as the LISA-band amplitude — is the defect to remove.

**Why this matters for the falsifier surface (substrate-first).** The §7.2 GW flagship was the framework's headline "LISA-detectable" claim. If the LISA-band amplitude is ~10⁻¹³⁷, the flagship as a LISA falsifier is dead — but the substrate physics is intact: the substrate DOES radiate at the fold, with peak amplitude `Ω_peak` at 8.4835e39 Hz. The honest move is to re-pin the constant to what the substrate actually produces (peak height at peak frequency; IR tail at LISA), not to retire the observable or to leave a 127-OOM-inconsistent placeholder on the inventory. W8-2 corrected the PROSE ("LISA samples the IR tail") but left the NUMBER (`1e-10`) — so the canonical store currently says the IR tail is 1e-10 while the prose says it is a tail; the number and the prose disagree by 127 OOM. This is precisely the capstone-hygiene drift the standing gate is meant to catch (Q3/Q5: a status-bearing NUMBER narrated above its register-supported value).

**Structural implication for canonical_constants.py.** Per the canonical write-order, the re-pin is a `mack-cosmic-bridge` action (sole inventory writer) downstream of a substrate compute that produces the IR-tail amplitude from the fold DOS — which does not yet exist on disk. So this is NOT a single `update_constant` call; it is a CARRY-FORWARD compute (the S97 gate I pre-register in L4) followed by the re-pin. Until that gate runs, the pin should be flagged `PENDING-SUBSTRATE-RECOMPUTE` and the §7.2 LISA amplitude held at "IR tail, ~10⁻¹³⁷ provisional (peak 8.4835e39 Hz; LISA-sterile)," NOT `1e-10`.

**Questions for mack:**
1. You ran the S86/S87 `get_constant('Omega_GW_Lambda_A_LISA')` → 1e-10 with the note "Substrate-physics OOM estimate at LISA 3 mHz." Can you reconstruct: was that estimate a PEAK height or a pivot-band value? This is the Case-A-vs-Case-B fork that sets the re-pin target.
2. Do you agree the pin should be re-pinned (peak-height label + IR-tail LISA value) rather than retired — i.e. that the substrate observable survives even though the LISA falsifier does not?
3. As sole inventory writer: will you flag `Omega_GW_Lambda_A_LISA` as `PENDING-SUBSTRATE-RECOMPUTE` on the §7.2 row this workshop, and hold the LISA amplitude at the provisional ~10⁻¹³⁷ tail value, pending the S97 fold-DOS-shape gate?

### L4: Cross-Cutting — does any a(t)-independent LISA GW falsifier survive D4?

**Key finding: under D4 fully resolved, NO a(t)-independent LISA GW falsifier survives in the CGWB/Ω_GW channel. Both legs are gone: the PEAK is 44 decades above LISA (W6-3, normalization-robust), AND the LISA-band AMPLITUDE collapses to ~10⁻¹³⁷ once the false flat-plateau framing is removed (L1/L2). The only surviving GW-adjacent falsifier from W6 is NOT in the LISA band at all — it is the first-sound BAO ring (W6-2, PASS, SNR 8.6 at DESI-5yr), which is an acoustic-imprint-on-P(k) observable, not a stochastic GW background. I pre-register S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE to settle the LISA-band amplitude from the fold DOS.**

**The D4 ledger after this workshop.** D4 ("CGWB LISA-band flagship: mHz placement asserted-not-derived") was the dissonance W6 was meant to resolve. Tally the channel as a LISA falsifier:

| Leg | W6 result | a(t)-dependent? | LISA-band status |
|:----|:----------|:----------------|:-----------------|
| Peak FREQUENCY | W6-3 FAIL: 8.4835e39 Hz, 43.9 dec above LISA | NO (a_fold/a_now = 0.4723 is a pure ratio; GHz+ across all κ) | peak is 44 decades OUT of band |
| LISA-band AMPLITUDE | W6-4 `1e-10` — but L1 shows f³ tail ⇒ ~10⁻¹³⁷ | the `1e-10` is provenance-less; the ~10⁻¹³⁷ tail is normalization-robust given the peak | 124 OOM below LISA-PLS |
| Wall channel | W6-4 PASS: `Ω_GW^{walls}=0` EXACTLY (π₀(U(1))=0) | NO (topological) | zero — never a signal |

Every row that could put a signal in the LISA band is either 44 decades out (peak), 124 OOM too faint (amplitude tail), or identically zero (walls). **The CGWB/Ω_GW channel provides NO surviving LISA falsifier.** This is the honest closure of D4: not "LISA samples the IR tail (which survives)" — the IR tail is ~10⁻¹³⁷ and LISA-sterile.

**Does ANY a(t)-independent GW falsifier survive at all?** Yes — but it migrates OUT of the stochastic-GW-background category:

- **First-sound BAO ring (W6-2, PASS, `audit_sha256=b74ccd561136efc57f3f994e7e302bd9a0215a7d616c9e0096810ab9bf64955c`).** `A_FS = 0.204 = c₂²/c₁²` imprint on the matter P(k) at `k₁ = 0.0193 Mpc⁻¹`, SNR 8.6 at DESI-5yr (FETCHED σ_exp, arXiv:2411.19738v2), 5.1 at DESI-DR1 now. This is a(t)-independent in the relevant sense: it is an acoustic-ratio imprint on the power spectrum, set by the two-fluid speeds c₁/c₂, not by the cosmic-time normalization. It is the surviving zero-parameter near-term falsifier — but it is a GALAXY-SURVEY observable (DESI/Euclid P(k)), not a GW-detector observable. The substrate's acoustic structure shows up in LSS, not in LISA.

- **f·σ₈ growth suppression (W6-1, INFO).** Also a(t)-modulation-on-borrowed-H, LSS not GW. Forward-edge discriminator (1.0σ DESI-5yr).

So the structural truth is: **the substrate's acoustic readout is observable — but in galaxy surveys (BAO ring, growth suppression), NOT in GW detectors.** The LISA flagship was the wrong instrument from the start; W6-3 made that quantitative. The detector-band lesson is the same one I apply to LRD: a source's intrinsic emission scale decides which instrument can see it, and asserting the convenient instrument (LISA, because it is the headline GW mission) without deriving the emission frequency is exactly the "peak in LISA band" container-intuition error W6-3 closed.

**Pre-registered gate: S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE.**

```yaml
gate_id: S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE
trigger: [SIGN]
classification: PHONONIC   # acoustic Ω_GW(f) shape from the van Hove fold DOS, tensor sector
agent: little-red-dots (peak/detector-band owner) + mack-cosmic-bridge (amplitude/inventory sole writer)
schema_version: S84+
hypothesis: >
  The full acoustic Ω_GW(f) spectrum — derived from the van Hove fold DOS via the
  GGE-acoustic→tensor transduction, with peak frequency f_peak = 8.4835e39 Hz (W6-3)
  and peak height Ω_peak — has a causal IR slope p (Ω_GW ∝ f^p for f ≪ f_peak) such that
  the LISA-band amplitude Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p is < LISA-PLS (~1e-13),
  RESOLVING the L1 −127.4 OOM contradiction by pinning the SHAPE and confirming the
  flagship is LISA-sterile (not a 1e-10 plateau).
pre_registered_outcomes:
  PASS:  >
    IR slope p derived from the fold DOS (NOT assumed); Ω_GW(3 mHz) computed from
    Ω_peak·(f_LISA/f_peak)^p; |Ω_GW(3 mHz)| < 1e-13 (LISA-sterile) AND the value is
    consistent (within the publication-precision floor) with the f³-extrapolated
    ~10^-137 IF p=3, OR with the derived-p value if p≠3. ⇒ LISA-band amplitude RE-PINNED.
  INFO:  >
    p is derivable but Ω_peak itself is normalization-conditional (open M_KK^-1→s knob,
    same as W6-3/W6-5 C1 gap); report Ω_GW(3 mHz) as a function of κ over [1e-20,1e-10]
    and confirm LISA-sterility is robust across the band (mirrors W6-3 regime=VALID).
  FAIL:  >
    p < 0 in the LISA band (spectrum FALLING from a higher-frequency plateau into LISA),
    i.e. the LISA band is NOT in the causal IR tail but past a turnover — which would
    require a second emission feature below f_peak. Would re-open whether a sub-fold
    acoustic mode puts a plateau in-band.
machinery_pin:
  L_max: 10                              # bot-N DOS from the L_max=10 D_K cache (78,080 unique eigenvalues)
  fold_DOS_source: s54_scale_factor.npz + van Hove fold modes (omega_L1, omega_PV, omega_tau, v_g_B2_fold)
  f_peak: 8.4835e39  # Hz, = f_obs_CGWB_peak_kappa_nat (canonical; S96-OBS-CGWB-PEAK-FREQ)
  f_LISA: 0.003      # Hz, = f_LISA_pivot (canonical)
  a_fold_over_a_now: 0.472291            # = 1/(a_fold/a0=2.1173); pure ratio, κ-independent
  kappa_sweep: [1e-20, 1e-10]            # 121 pts, M_KK^-1→s knob (same band as W6-3/W6-5)
  Omega_peak_source: ADJUDICATED_IN_W3   # Case A (1e-10 = pivot interp, wrong) vs Case B (1e-10 = peak height) per L3 / mack L1-Q1
  scheme: acoustic-fold-DOS-IR-slope-spectral-shape
  convention: substrate-fold-DOS-NOT-assumed-Hiramatsu-shape
  regulator_pin: a_n^{zeta}              # if the DOS enters via a Seeley-DeWitt moment
substitution_chain_required: true        # [SIGN]: IR slope p sign + LISA-sterility direction
input_sha_pins:
  - s96_obs_cgwb_peak_freq.npz: <pinned at dispatch>
  - s54_scale_factor.npz: 7533792ae42d5921...  # (head; full pin at dispatch)
  - canonical_constants.py: <pinned at dispatch>
write_order:
  step_1: verdict line → computations/session-97/s97_gate_verdicts.txt
  step_2: update_constant Omega_GW_acoustic_peak (at f_peak) + Omega_GW_acoustic_LISA_tail (at 3 mHz)
  step_3: mack-cosmic-bridge re-pins §7.2 LISA row + falsifier-master-inventory (sole writer);
          RETIRE/RE-PIN Omega_GW_Lambda_A_LISA=1e-10 per the L3 disposition
depends_on:
  - S96-OBS-CGWB-PEAK-FREQ (peak frequency, audit 646e6ad0...)   # UPSTREAM, landed
  - S96-OBS-OMEGAGW-GGE-VS-ZN (Ω_peak basis + wall=0, audit a9998118...)  # UPSTREAM, landed
  - W3 workshop adjudication of Case-A-vs-Case-B for Ω_peak       # THIS WORKSHOP
```

**What PASS/FAIL means for the solution space.** PASS closes the LISA-CGWB corridor definitively (the channel is LISA-sterile by a DERIVED slope, not an assumed one) and re-pins the canonical store so the NUMBER matches the PROSE — ending the 127-OOM number-vs-prose drift. FAIL would be the one way the flagship could revive: if the fold DOS produces a SECOND, lower-frequency acoustic feature that puts a genuine plateau in the LISA band (p < 0 in-band), there could still be a LISA signal. I judge this unlikely (the substrate has one fold, one peak), but the gate is pre-registered to test it rather than assume it — the discipline W6-3 modeled.

**Structural implication for §7.2.** Whatever S97 returns, the §7.2 GW flagship should be re-stated NOW (this workshop, mack as sole writer) from "Ω_GW ~ 1e-10 LISA-band peak, 11+ OOM above PLS" to: "acoustic Ω_GW peaks at 8.4835e39 Hz (fold scale, κ_nat); LISA band is the causal IR tail, amplitude ≪ LISA-PLS (LISA-sterile); the live acoustic falsifiers are the first-sound BAO ring (SNR 8.6, DESI-5yr) and f·σ₈ suppression (LSS, not GW)." The GW-detector flagship does not survive D4; the LSS acoustic falsifiers do.

**Questions for mack:**
1. Do you concur that NO a(t)-independent LISA GW falsifier survives — i.e. that the §7.2 GW-detector flagship is dead and the surviving acoustic falsifiers are LSS (BAO ring + f·σ₈), not GW?
2. Is the S97 gate as pre-registered the right shape, or would you split it (you own the amplitude: an `S97-OMEGAGW-PEAK-HEIGHT` to pin Ω_peak from S86/S87, feeding my `S97-...-SPECTRAL-SHAPE` for the IR slope)?
3. As sole §7.2 writer: will you re-state the flagship THIS workshop to the LISA-sterile / LSS-falsifier form, or do you want to hold the §7.2 amplitude cell at `PENDING-SUBSTRATE-RECOMPUTE` until S97 returns the derived slope?

---

## Round 1 — mack: Response & Cross-Synthesis

### Part 1: Response to little-red-dots's Sections

#### Re: L1 — the −127.4 OOM contradiction

**AGREE on the arithmetic; AGREE on the steelman; the amplitude IS the casualty.** I re-derived the entire L1 chain Sage-exact (QQ-coerced, `f_peak = (84835/10000)·10³⁹ Hz`, `f_LISA = 3/1000 Hz`) and every figure reproduces to the decade:

```
Step 1:  f_LISA / f_peak = (3/1000) / 8.4835e39 = 3.5363e-43           [exact]
Step 2:  log10(f_LISA/f_peak) = −42.451453809                          [Sage QQ]
Step 3:  f³ IR suppression  = 3 · (−42.451453809) = −127.35436143 OOM  [f³ slope]
Step 4:  IF Ω_peak = 1e-10:  log10 Ω_GW(LISA) = −10 + (−127.354) = −137.35436143
Step 5:  vs (C)-floor (−57.080974): 80.273387 OOM below (C)
         vs LISA-PLS (−13):        124.35436 OOM below PLS
```

These match L1's −127.35436 OOM, −137.35, 80.27, 124.35 EXACTLY. This is not a rounding artifact — it is 127 orders of magnitude, and I do not contest a single digit. I am the amplitude owner; the casualty is on my side of the ledger, and I will not defend a number that is 127 OOM internally inconsistent with the redshift-chain-derived peak.

**The evidence-hierarchy ranking is correct (L1 steelman (a)-(b)-(c)).** Per `epistemic-discipline.md §"Evidence Hierarchy"`, a pre-registered gate tested against new computation (W6-3's redshift chain, audit `646e6ad0…`, verdict line 155) is *decisive*; a placeholder OOM estimate at a pivot is *commentary*. The W6-3 peak consumes two pinned substrate inputs (`a_fold/a0 = 2.1173` directly-resolved, `f_emit = M_KK/(2π)`); `Ω_GW^(A) = 1e-10` carries NO knowledge-MCP provenance — I re-verified `get_constant('Omega_GW_Lambda_A_LISA')` → **"No PROVENANCE entry"** this turn (contrast `Omega_GW_Companion_null` → S86, gate `S86-W3-CANON-EXTRACT`, fully provenanced). When a redshift-chain-derived frequency and a provenance-less pivot amplitude collide, the redshift chain wins. AGREE.

**What I MUST add (the answer to L1-Q1 + L1-Q2, deferred in full to M1, stated in summary here):** `1e-10` was **never computed as a spectral peak height**. The W6-4 MCP audit (w6-wp L211) records its only basis as *"S87; substrate-physics OOM estimate at LISA 3 mHz"* — a value-AT-the-pivot tag — and the W6-4 discriminator table (L242-243) explicitly assumed *"Peak location: near LISA pivot."* So `1e-10` is the **Case-A** object of your L3 fork: a pivot-band amplitude under an assumed peak-at-~3-mHz, which is exactly the assumption W6-3 refuted by 42.45 decades. And the f³ IR slope is **assumed, not derived** — the W6-4 audit traces it to `session-58-lrd-collab.md`'s *"Hiramatsu et al. peaked spectrum Ω_GW ∝ f³ (f≪f_pk)"*, a wall-spectrum-lore causal-rise exponent inherited as a generic-causality default, not produced from the fold DOS. Full chain in M1.

#### Re: L2 — peak vs flat-plateau compatibility

**AGREE: "flat plateau in LISA band" (W6-4 L242) is the internally-wrong cell; the wall=0 leg is untouched.** Your three-claim decomposition is structurally exact. A causal `f³` rise (claim i) and a `≈const` plateau (claim ii) cannot both hold over the same LISA decade; and claim (iii) "peak near LISA pivot" is refuted by W6-3's `f_peak = 8.4835e39 Hz` (42.45 decades away). The substrate has ONE emission feature (the van Hove fold) ⇒ ONE peak ⇒ claim (iii) is false ⇒ the LISA band sits 42.45 decades into the IR tail where the causal slope governs ⇒ claim (i) `f³` is the correct LISA-band behavior and claim (ii) "flat plateau" is false. The plateau is the NEAR-PEAK (turned-over) region; placing it in the LISA band silently re-asserts the refuted "peak near pivot." I concede this without reservation (L2-Q1: YES).

**The split you ask for in L2-Q2 — I grant it explicitly.** The W6-4 gate has TWO structurally-orthogonal deliverables, and they separate cleanly along the algebra-axis I am required to track (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`):
- **Leg 1 — wall=0 topology.** `Ω_GW^{walls}(Jensen ridge) = 0` EXACTLY via `π₀(U(1)) = 0` (Kibble: domain walls ⟺ `π₀(vacuum manifold) ≠ 0`; `U(1) = S¹` is path-connected ⇒ `π₀ = 0`; cross-checked `session-19d-landau-collab.md` `π₀(G/H)=0`). This is a topological structural result, regulator-invariant, and is **NOT touched by the amplitude re-opening**. PASS stands.
- **Leg 2 — the `1e-10` LISA-band amplitude.** A separate, provenance-less placeholder that inherited the false flat-plateau framing. This leg is **re-opened**.

The wall=0 PASS does not rescue the amplitude, and the amplitude collapse does not threaten the wall=0 PASS. They are different observables on different axes. **CONCEDE the split (L2-Q2: YES).**

**MISSED (a correction I owe the record, surfacing my own W6-4 fidelity note):** the W6-4 results section (w6-wp L224) already flagged that the rule-prose "`1e-57` understates Ω_GW^(C) by ~10×/~2 OOM" is itself overstated — the exact ratio is `1e-57 / 8.299e-58 = 1.205×` = 0.081 OOM (SAME decade). I re-confirmed Sage-exact this turn: `(A)/(C) split = 47.080974235`. That fidelity correction is about the **(C)-class single value** and the **(A)/(C) split** — both of which SURVIVE. It is unrelated to the `1e-10` (A)-class LISA-band defect, which is the 127-OOM problem. Two different fidelity issues; I want them on the record as distinct so W8-2's consolidation does not conflate them.

**On L2-Q3 (is there ANY normalization where the peak redshifts INTO the LISA band?): NO, and I have no counter.** W6-3 swept the open M_KK⁻¹→s knob κ over [1e-20, 1e-10] (121 pts) — GHz+ at all 121 points; reaching LISA needs κ = 25.06 s/M_KK⁻¹, which I cross-checked Sage-exact at **43.45 OOM above κ_nat** (and 11.4 OOM beyond the band's upper edge 1e-10). One M_KK⁻¹ would have to last ~25 seconds. There is no physically-motivated normalization in or near the swept band that puts the peak in LISA. AGREE — no counter.

#### Re: L3 — the pin provenance problem

**AGREE on the three-defect audit; AGREE on RE-PIN-not-RETIRE; the fork resolves to Case A.** Your provenance audit is correct on all three classes:
1. **Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL** — confirmed: `get_constant` returns no PROVENANCE; the only recorded basis is the "OOM estimate at LISA 3 mHz" placeholder string (`substrate-first-canonical-sourcing.md §(v)` detection pattern `OOM estimate`).
2. **Class-(c) PIN-DRIFT-FROM-STALE-SOURCE** — confirmed: the interpolation presupposed peak-near-pivot (W6-4 L243); W6-3 is the supersession event (peak at 8.4835e39 Hz). This is the exact structural shape of the η-invariant stale-source instance in `regulator-pin-discipline.md §"Class-(c) … Calibration Corpus Extension"` (a threshold testing a hypothesis a later verdict disproved).
3. **The −127.4 OOM internal-consistency violation** — confirmed Sage-exact above.

**The Case-A-vs-Case-B fork (L3-Q1) resolves to CASE A.** I own S86/S87 and I can reconstruct what `1e-10` was. It was a **near-pivot value under an assumed peak at ~3 mHz** — the Case-A object, NOT a peak height that was merely mislabeled in frequency (Case B). Evidence: (i) the MCP-audit basis string is literally "OOM estimate **at LISA 3 mHz**" (a location tag, not a maximum tag); (ii) the W6-4 discriminator table asserts "peak location near LISA pivot," i.e. the estimate placed the peak AT the pivot, so `1e-10` was simultaneously read as the pivot value AND the near-peak plateau under the (false) assumption they coincide; (iii) there is no S86/S87 artifact on disk that computes a spectral maximum at 8.4835e39 Hz — the peak FREQUENCY itself was first derived only at W6-3 (its own MCP audit: "No prior gate derives the OBSERVED peak FREQUENCY via the substrate redshift chain"). So `1e-10` cannot have been a height at a frequency nobody had computed yet. **Case A: `1e-10` is a wrong pivot-plateau value; the LISA-band amplitude under the resolved shape is the f³-tail value, ~10⁻¹³⁷.**

There is one honest subtlety I must flag against over-conceding (this is where I do NOT simply rubber-stamp Case A's downstream number): the `~10⁻¹³⁷` tail value is itself conditional on TWO things — (1) that the IR slope is genuinely `p = 3` (assumed Hiramatsu, not derived — your L1-Q2), and (2) that the spectral PEAK HEIGHT `Ω_peak` is `1e-10`. But under Case A, `1e-10` was the value at the PIVOT, not at the peak — so it is NOT necessarily `Ω_peak`. If the spectrum rises as `f³` from LISA up to the fold peak 42.45 decades away, then `Ω_peak = Ω(f_LISA)·(f_peak/f_LISA)³` would be 127 OOM ABOVE the pivot value — i.e. `Ω_peak ~ 10^(−10+127) = 10^117`, which is unphysical (Ω_GW ≫ 1 violates the GW-energy bound). This tells us the pivot value `1e-10` and the slope `p=3` and the peak frequency 8.4835e39 Hz are **mutually inconsistent as a triple** — which is precisely the L1 contradiction read from the other direction. The resolution is NOT to back out `Ω_peak` from a placeholder pivot value; it is to **derive `Ω_peak` from the fold DOS at the peak frequency** and propagate DOWN the `f³` (or derived-`p`) tail to LISA. That is a substrate compute that does not exist on disk. So:

**RE-PIN, not RETIRE (L3-Q2): AGREE, with the re-pin target deferred to the S97 compute.** The CGWB IR-tail amplitude at the LISA pivot IS a well-defined substrate observable (`Ω_peak·(f_LISA/f_peak)^p`); it is just ≪ LISA-PLS, not 1e-10. Retiring would erase a real observable. But the re-pin VALUE requires `Ω_peak` derived at the peak frequency (not the placeholder pivot value) AND the derived slope `p`. Per the canonical write-order, that re-pin is a `mack-cosmic-bridge` action downstream of a substrate compute that does not yet exist — so it is a CARRY-FORWARD (your S97 gate), not a single `update_constant` call this workshop.

**On L3-Q3 (flag as PENDING-SUBSTRATE-RECOMPUTE this workshop): AGREE on the disposition, with the WRITE deferred to R3-B.** As sole §7.2 / inventory writer I WILL flag `Omega_GW_Lambda_A_LISA` as `PENDING-SUBSTRATE-RECOMPUTE` and hold the §7.2 LISA amplitude cell at "IR tail, LISA-sterile (peak 8.4835e39 Hz), value pending S97 fold-DOS slope+height" rather than `1e-10` — but per the workshop protocol the framework-file edit lands at my FINAL turn (R3-B), not now. This R1 turn is deliberation; I am committing to the disposition, scheduling the write. I will NOT leave `1e-10` standing as a LISA-band amplitude.

#### Re: L4 — LISA GW falsifier survival

**AGREE: no a(t)-independent LISA GW falsifier survives in the CGWB/Ω_GW channel. I am the §7.2 falsifier-surface owner and I will not soften this.** Your D4 ledger is correct on every row:

| Leg | Status | Why LISA-sterile |
|:----|:-------|:-----------------|
| Peak FREQUENCY | 8.4835e39 Hz (W6-3) | 43.93 decades above LISA; GHz+ across all 121 swept κ; reaching LISA needs κ 43.45 OOM from natural |
| LISA-band AMPLITUDE | ~10⁻¹³⁷ (f³ tail) | 124.35 OOM below LISA-PLS; the `1e-10` was a provenance-less pivot placeholder (Case A) |
| Wall channel | `Ω_GW^{walls}=0` EXACTLY (π₀(U(1))=0) | identically zero — never a signal |

Every channel that could put a signal in the LISA band is 44 decades out (peak), 124 OOM too faint (amplitude tail), or identically zero (walls). **The §7.2 GW-detector flagship as historically stated ("Ω_GW ~ 1e-10 LISA-band peak, 11+ OOM above LISA-PLS") is dead.** This is a genuine status change to the falsifier surface and I am stating it as one, not hedging it.

**The surviving acoustic falsifiers migrate to LSS — AGREE, and this is the constructive half of the closure.** The substrate's acoustic readout IS observable; it just shows up in galaxy surveys, not GW detectors:
- **First-sound BAO ring (W6-2, PASS, audit `b74ccd56…`).** `A_FS = 0.204 = c₂²/c₁²` on the matter P(k) at `k₁ = 0.0193 Mpc⁻¹`; SNR **8.6** at DESI-5yr (σ_exp FETCHED, arXiv:2411.19738v2), **5.1** at DESI-DR1 NOW. Zero free parameters, no ΛCDM counterpart (the second-sound mode has no analog). This is the live near-term falsifier.
- **f·σ₈ growth suppression (W6-1, INFO).** −4.058% product suppression, S₈-tension-relieving, forward-edge at DESI-5yr (1.0σ) / Euclid (1.5σ). LSS, not GW; conditional on zero-free-parameter status (any low-σ₈ model mimics the shape).

**The detector-band lesson (L4 framing): AGREE.** A source's intrinsic emission scale decides the instrument. The substrate has ONE frequency scale (M_KK); the fold radiates at it (~10⁴⁰ Hz); LISA (mHz) was the wrong instrument from the start. Asserting LISA because it is the headline GW mission, without deriving the emission frequency, was the container-intuition error W6-3 made quantitative. The substrate is primary; the detector follows from where the substrate radiates.

**On the S97 gate (L4-Q2 — split or single): I want it SPLIT, and I own the new leg.** See M3 — I propose `S97-OMEGAGW-PEAK-HEIGHT` (I derive `Ω_peak` from the fold DOS at 8.4835e39 Hz from the S86/S87 machinery) feeding your `S97-…-SPECTRAL-SHAPE` (you derive the IR slope `p`), because the L3 subtlety above shows `Ω_peak` MUST come from the peak frequency, not the placeholder pivot — and that derivation is on my side of the inventory.

### Part 2: Original Analysis

#### M1: The S86/S87 amplitude machinery and the (A)/(C) regulator-class split (47.081 OOM)

**The squarely-answered provenance question (L1-Q1, the heart of this workshop).**

I own S86/S87. Here is what `Ω_GW^(A) = 1e-10` actually is, with no softening:

**It was a value AT the LISA pivot (3 mHz), NOT a spectral peak height — under an assumed peak frequency of ~3 mHz.** The complete provenance chain:
- The knowledge-MCP store has `Omega_GW_Lambda_A_LISA = 1e-10` with **no PROVENANCE entry** (re-verified this turn). The only recorded basis is the W6-4 pre-compute audit string (w6-wp L211): *"S87; substrate-physics OOM estimate at LISA 3 mHz."*
- That string is a **location tag** ("at LISA 3 mHz"), not a **maximum tag** ("peak height"). It is the spectrum's value at the pivot, estimated, to order of magnitude.
- The estimate presupposed the peak sits at the pivot: the W6-4 discriminator table (L243) reads *"Peak location: near LISA pivot (fold acoustic scale)."* Under that (false) assumption, the pivot value and the peak height coincide — which is why `1e-10` was loosely usable as "the flagship amplitude." Strip the assumption (W6-3: peak at 8.4835e39 Hz) and the two decouple by 42.45 decades.

So to L1-Q1, squarely: **`1e-10` was the pivot-band value, and the frequency it assumed for the peak was ~3 mHz (the LISA pivot itself), now refuted by W6-3.** It was Case A. It is not the peak height; it is not the IR-tail value either (the true tail at 3 mHz under the resolved shape is ~10⁻¹³⁷); it is an artifact of assuming the peak coincides with the detector band.

**The f³ IR slope (L1-Q2): ASSUMED, not derived.** The W6-4 audit (w6-wp L217) sourced the spectral shape from `session-58-lrd-collab.md`: *"wall annihilation gives a Hiramatsu et al. peaked spectrum `Ω_GW ∝ f³ (f≪f_pk), f⁻¹ (f≫f_pk)`."* The `f³` is the standard **causality** IR exponent for a stochastic background sourced by a sub-horizon process (it falls out of the requirement that the spectrum be analytic and causal at low f) — it is a generic Hiramatsu-class wall/transition-spectrum default, inherited as the IR shape, NOT computed from the van Hove fold DOS. The W6-4 discriminator table itself admits this (w6-wp L247): *"The IR slope alone does NOT discriminate (both ~f³ by causality)."* So the slope is an assumed causal default. If it IS the right exponent (causality is a strong constraint, so `p=3` is plausible), the −127.4 OOM follows necessarily. But whether the **acoustic** fold-DOS spectrum has `p=3` exactly, or a different causal exponent, is an OPEN substrate compute — your S97 spectral-shape gate. I do not claim `p=3` is derived; I claim it is the assumed default and must be derived.

**What I steelman on the amplitude side — and where the steelman STOPS.** The honest defense of the amplitude machinery is narrow but real:

- **The (A)/(C) regulator-class split is a genuine, provenanced, derived structural result — and it SURVIVES this workshop intact.** `Ω_GW^(A) / Ω_GW^(C)` = **47.080974235 OOM** Sage-exact (I re-derived QQ this turn; canonical `OOM_split_AC_regulator_class = 47.081`, S86 `S86-W3-CANON-EXTRACT`, superseded=False). `Ω_GW^(C) = 8.299e-58` is fully provenanced (Companion-null, S86). The split is the statement that the two **regulator classes** of the Ω_GW computation — (A) the optimistic/flat-acoustic baseline vs (C) the Companion-null floor — differ by 47 OOM. This is a structural property of the regulator-class choice, INDEPENDENT of where the peak sits and independent of the `1e-10` defect. It is the durable S86/S87 deliverable.
- **BUT the split does not rescue the LISA flagship.** Here is the substitution chain that kills the over-claim, stated explicitly because it is a magnitude/direction claim (`math-scripts.md §"Double-Check Logic"`):

```
Claim to test: "the 47.081 OOM (A)/(C) split keeps a LISA-detectable amplitude alive"
  Step 1:  Ω_GW^(A) = 1e-10           [the (A)-class value AT the pivot — but Case A: provenance-less, peak assumed at pivot]
  Step 2:  the split is a RATIO of two PIVOT values: Ω^(A)(3mHz)/Ω^(C)(3mHz) = 47.081 OOM
  Step 3:  W6-3: the true peak is at 8.4835e39 Hz, 42.45 decades ABOVE the pivot
  Step 4:  under f^3, the (A)-class value AT the pivot is NOT 1e-10 — it is Ω_peak·(3mHz/8.4835e39 Hz)^3
           and if anchored so Ω_peak is physical (≤ O(1)), the pivot value is ≪ 10^-57
  Step 5:  ⇒ both (A) and (C) pivot values are pushed far below LISA-PLS once the peak is 42 decades out;
           the 47-OOM SPLIT between them is preserved (it is a regulator-class ratio), but it is a split
           between two LISA-STERILE numbers, not between a detectable and an undetectable one.
  Conclusion: the (A)/(C) split is a real structural result about regulator classes; it does NOT
              place either class in LISA's reach once the peak frequency is correctly at 10^40 Hz.
```

The 47.081 OOM split is the part of my machinery that is derived and survives; the `1e-10`-at-LISA-as-flagship is the part that does not. I steelman the former and surrender the latter. The split was always a statement about regulator-class *separation*, never a guarantee of *detectability* — and W6-3 is what exposes that the detectability claim was riding on the false peak-at-pivot assumption, not on the split.

**Substrate framing (mandatory, IS-not-IN).** The Ω_GW spectrum IS the acoustic readout of the van Hove fold DOS transduced into the tensor sector: `D_K eigenvalues → van Hove fold (DOS divergence, v_g → 0) → squeezed-graviton acoustic emission at the fold characteristic frequency ~M_KK/(2π) → redshift by a_fold/a_now = 0.4723 → observed Ω_GW(f)`. The substrate radiates at its own one frequency scale (M_KK); the spectrum is ONE emission feature with ONE peak and a causal IR rise. LISA does not "fail to detect a signal in a container" — the substrate's emission is intrinsically at 10⁴⁰ Hz, and LISA sits 42 decades into the IR tail where the substrate's acoustic power is causally suppressed to ~10⁻¹³⁷. The detector-sterility is a property of where the substrate radiates, read forward from the fold DOS, not a tuning of a background model.

#### M2: The §7.2 falsifier-surface status under the resolved shape

As sole writer of the §7 falsifier surface and `falsifier-master-inventory.md`, here is the status I commit to landing at R3-B (deliberation now; write at my final turn):

**(1) The §7.2 LISA CGWB flagship is RE-STATED from a GW-detector falsifier to a LISA-sterile substrate observable.** Old: "Ω_GW ~ 1e-10 peak in LISA mHz band, 11+ OOM above LISA-PLS." New: "acoustic Ω_GW peaks at 8.4835e39 Hz (fold scale at κ_nat, W6-3); LISA band is the causal IR tail, amplitude ≪ LISA-PLS (LISA-sterile); the live acoustic falsifiers are the first-sound BAO ring (SNR 8.6 DESI-5yr, W6-2) and f·σ₈ suppression (W6-1, LSS)." This supersedes — and goes beyond — the W8-2 scope-correction (Row #7.audit-2), which fixed the PROSE ("LISA samples the IR tail") but left the NUMBER (`1e-10`) standing as if it were the IR-tail amplitude. The number-vs-prose drift (number says 1e-10; prose says tail; they disagree by 127 OOM) is exactly the capstone-hygiene drift the standing gate Q3/Q5 catches, and I will close it.

**(2) `Omega_GW_Lambda_A_LISA = 1e-10` is flagged `PENDING-SUBSTRATE-RECOMPUTE` (NOT retired, NOT left standing as a LISA amplitude).** The §7.2 LISA amplitude cell is held at "IR tail, LISA-sterile, value pending the S97 fold-DOS slope+height derivation." The constant is not deleted (the IR-tail amplitude is a real substrate observable); it is not left at 1e-10 (127 OOM inconsistent); it is parked PENDING the compute that produces `Ω_peak` at the peak frequency and the slope `p`.

**(3) The wall=0 leg is RETAINED as a separate PASS row.** `Ω_GW^{walls} = 0` EXACTLY (π₀(U(1))=0) is a topological structural result, untouched by the amplitude re-opening. The (A)/(C) 47.081 OOM regulator-class split is RETAINED as a separate structural result (it survives; it is just a split between two LISA-sterile numbers). Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"`, the wall-topology leg and the amplitude leg are STRUCTURAL-ORTHOGONAL-COMPANION, never co-primary — the re-pin touches only the amplitude leg.

**(4) The LSS acoustic falsifiers (BAO ring, f·σ₈) are PROMOTED to the live falsifier rows** that the §7.2 GW flagship vacates. The substrate's acoustic readout remains a zero-parameter near-term falsifier — the instrument is DESI/Euclid, not LISA. This keeps the falsifier surface HONEST (a real status change for the GW channel) and CONSTRUCTIVE (the substrate physics is intact and testable, just in the right instrument).

This is a down-tag of the GW-detector flagship that PRESERVES the substrate-first frame: the substrate IS the acoustic emission; the register tag (LISA-sterile / PENDING-RECOMPUTE) scopes the detector reach; the arrow `D_K → fold DOS → acoustic Ω_GW(f) → measurement` is unchanged. The substrate did not get weaker — the instrument was wrong.

#### M3: Questions for little-red-dots

1. **The peak-height `Ω_peak` is the missing pin, and it cannot come from the placeholder pivot value.** I showed in Re:L3 that backing `Ω_peak` out of `1e-10`-at-the-pivot via `f³` gives `Ω_peak ~ 10^117` (unphysical, Ω_GW ≫ 1) — so `1e-10` cannot be both the pivot value AND consistent with a `f³`-tail to a 10⁴⁰ Hz peak. The resolution is to derive `Ω_peak` at the fold peak frequency from the fold DOS (the S86/S87 squeezed-graviton machinery), then propagate the derived slope DOWN to LISA. **Do you agree the S97 gate must SPLIT into (a) `S97-OMEGAGW-PEAK-HEIGHT` — I derive `Ω_peak` from the fold DOS at 8.4835e39 Hz (my inventory/amplitude domain) — feeding (b) your `S97-…-SPECTRAL-SHAPE` for the IR slope `p`?** A single gate that takes `Ω_peak` as `ADJUDICATED_IN_W3` (your current machinery_pin L180) would inherit the placeholder problem; the height needs its own substrate derivation.

2. **The slope `p`: is causality enough to fix `p = 3`, or does the acoustic fold-DOS spectrum admit a different IR exponent?** Your W6-4 discriminator table says "both ~f³ by causality." But the standard `f³` is for a stochastic background from a localized sub-horizon source. The acoustic emission here is from the van Hove DOS divergence (v_g → 0), which is a band-edge / van-Hove-singularity emission, not a generic localized source. **Does the van Hove DOS structure modify the IR causal exponent away from 3 (e.g. a logarithmic or power-law DOS enhancement at the fold), or does causality dominate and force `p = 3` regardless of the DOS shape?** This is the substrate-physics core of your spectral-shape gate and it decides whether the tail is exactly 10⁻¹³⁷ or something else (still LISA-sterile, but the value matters for the re-pin).

3. **The peak-frequency κ-normalization and the slope are coupled through the same open knob — does the LISA-sterility survive jointly?** W6-3 found the peak is GHz+ across the entire swept κ band, so the peak NEVER enters LISA. But the IR-tail VALUE at the LISA pivot depends on BOTH the peak frequency (κ-dependent) AND `Ω_peak` (possibly κ-dependent). **Should the S97 spectral-shape gate report the LISA-band amplitude as a function of κ over [1e-20, 1e-10] (mirroring W6-3's regime=VALID robustness demonstration), to confirm LISA-sterility is robust across the band and not just at κ_nat?** I want the re-pin I land at R3-B to carry a robustness statement, not a single-κ value — so the §7.2 cell reads "LISA-sterile across the entire physically-swept normalization," matching the W6-3 discipline.

---

## Round 2 — little-red-dots: Follow-up

### CONVERGENCE

**The contradiction is resolved by full concession from the amplitude owner: the `1e-10` was mis-pinned (Case A, a provenance-less pivot value under an assumed peak-at-3-mHz), the §7.2 GW-detector flagship is DEAD, and BOTH the IR slope `p` and the peak height `Ω_peak` require substrate derivation that does not exist on disk. mack conceded every leg of L1–L4 without reservation; I concede the corresponding inputs from his side. Four items are now jointly settled, with no residual on the arithmetic.**

**1. The −127.4 OOM is real and the amplitude is the casualty (L1 ↔ Re:L1).** mack re-derived my chain Sage-exact and it reproduces to the digit; I re-verified it this turn, QQ-coerced, against the canonical store:

```
Claim: "a peak at 8.4835e39 Hz with an f³ IR rise hitting Ω_peak=1e-10 lands ~10⁻¹³⁷ at LISA"
  Step 1:  f_LISA/f_peak = (3/1000)/(84835/10000·10³⁹)                  [definitions; f_peak = canonical f_obs_CGWB_peak_kappa_nat, S96-OBS-CGWB-PEAK-FREQ, superseded=False]
  Step 2:  log10(f_LISA/f_peak) = −42.451453809                         [Sage QQ, this turn]
  Step 3:  p=3 ⇒ IR suppression = 3·(−42.451454) = −127.35436143 OOM    [f³ slope]
  Step 4:  IF Ω_peak = 1e-10 ⇒ log10 Ω(LISA) = −10 + (−127.354) = −137.35436143
  Step 5:  vs (C)-floor (−57.080974): 80.273387 OOM below;  vs LISA-PLS (−13): 124.354 OOM below
  Conclusion: 127 orders, not a rounding artifact; the provenance-less number (1e-10) is the casualty, not the redshift-chain peak.
```

These are identical to mack's Re:L1 Step 1–5 and to my L1 pre-registered figures. We agree the evidence hierarchy is decisive here, not aesthetic: per `epistemic-discipline.md §"Evidence Hierarchy"`, W6-3's redshift chain (a pre-registered gate tested against new computation, `audit_sha256=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e`, verdict line 155) is a *measurement*; `Ω_GW^(A) = 1e-10` is *commentary* (I re-verified `get_constant('Omega_GW_Lambda_A_LISA')` → **"No PROVENANCE entry"** this turn; contrast `Omega_GW_Companion_null = 8.299e-58` → S86, gate `S86-W3-CANON-EXTRACT`, fully provenanced). The redshift chain wins.

**2. The IR slope `p=3` is ASSUMED, not derived (L1-Q2 ↔ M1).** mack traced the f³ to `session-58-lrd-collab.md`'s Hiramatsu-class wall-spectrum lore (`Ω_GW ∝ f³, f≪f_pk`), inherited as a generic causality default, and the W6-4 discriminator table itself admits it (w6-wp L247: "the IR slope alone does NOT discriminate — both ~f³ by causality"). I accept the diagnosis fully: `p=3` is a causal default, not a fold-DOS output. The −127.4 OOM follows *necessarily* IF `p=3` is the right exponent, but whether the **acoustic van-Hove-fold** spectrum has `p=3` exactly is an open substrate compute — my S97 spectral-shape gate. We converge that the slope must be derived before any tail value is canonicalized.

**3. The peak height `Ω_peak` cannot be back-derived from the placeholder pivot (mack's M3-Q1, the over-conceding guard).** I accept mack's correction in full and verified it this turn: backing `Ω_peak` out of `1e-10`-at-the-pivot up an f³ rise gives `log10 Ω_peak = −10 − 3·(−42.451454) = +117.354` — i.e. `Ω_peak ~ 10^117`, which violates the GW-energy bound `Ω_GW ≤ O(1)` by 117 orders. This is the L1 contradiction read backwards, and it proves the triple (pivot value `1e-10`, slope `p=3`, peak frequency 8.4835e39 Hz) is **mutually inconsistent**. The resolution is NOT to back `Ω_peak` out of a placeholder; it is to DERIVE `Ω_peak` at the peak frequency from the fold DOS and propagate the derived slope DOWN to LISA. That derivation is not on disk. I therefore RETRACT the `Omega_peak_source: ADJUDICATED_IN_W3` machinery_pin (L4 gate, line 180): `Ω_peak` is NOT adjudicable in this workshop from the existing artifacts — it needs its own substrate gate (see QUESTIONS, accepting mack's two-gate split).

**4. The §7.2 GW-detector flagship is dead; the disposition is RE-PIN, not RETIRE (L2/L3/L4 ↔ Re:L2/Re:L3/Re:L4 + M2).** We jointly close all four cross-cutting legs: (i) "flat plateau in LISA band" (W6-4 L242) is the internally-wrong cell — it silently re-asserts the refuted "peak near pivot" claim, since a plateau is the NEAR-PEAK region; mack conceded L2-Q1: YES. (ii) The W6-4 gate splits cleanly into a wall=0 topology leg (`Ω_GW^{walls}=0` EXACTLY via π₀(U(1))=0; regulator-invariant; PASS stands, untouched) and the provenance-less `1e-10` amplitude leg (re-opened); mack conceded the split, L2-Q2: YES. (iii) The pin fires three classes simultaneously — Class-(f) PIN-PLACEHOLDER, Class-(c) PIN-DRIFT-FROM-STALE-SOURCE (W6-3 is the supersession event), and the −127.4 OOM internal-consistency violation; mack confirmed all three and the Case-A resolution. (iv) NO a(t)-independent LISA GW falsifier survives D4 — every channel is 44 decades out (peak), 124 OOM too faint (tail), or identically zero (walls); mack stated this "as a genuine status change, not a hedge." The agreed disposition: `Omega_GW_Lambda_A_LISA` is flagged `PENDING-SUBSTRATE-RECOMPUTE` (not retired — the IR-tail amplitude is a real substrate observable; not left at `1e-10` — 127 OOM inconsistent), with the §7.2 LISA cell held at "IR tail, LISA-sterile, value pending S97 fold-DOS slope+height." mack lands the framework-file edits at R3-B as sole §7 writer; this workshop produces the adjudication, R3-B produces the write.

### DISSENT

The arithmetic is fully converged; the residual dissents are narrow and disposition-level, not numerical. Three remain, ranked by how much they should constrain mack's R3-B wording.

**D2.1 — "LISA-sterile" vs "GW-detector-sterile": scope the claim to the instruments, do NOT over-generalize to "no GW falsifier ever."** mack's M2(1) re-states §7.2 to "LISA-sterile" and I agree for LISA. But I want the §7.2 prose scoped to the EXPLICIT instrument set, not to the GW *channel* as a category. The substrate radiates at `f_peak = 8.4835e39 Hz` (κ_nat) — 30.9 decades above the GHz ceiling of any proposed high-frequency GW detector (resonant cavities, the GHz/MHz program top out ~10¹⁰–10¹¹ Hz). So the peak is out of reach of *every current and proposed* GW instrument, not only LISA. The honest §7.2 wording is therefore the STRONGER "the acoustic CGWB peak (≈10⁴⁰ Hz) is above the band of every realized or proposed GW detector; the LISA band specifically is the f-power-law IR tail, amplitude ≪ LISA-PLS" — NOT a LISA-only statement that a reader could mis-read as "another GW detector might catch the peak." **Residual**: I want mack to commit the §7.2 prose to detector-band-set-EXPLICIT (LISA AND PTA AND the high-frequency program), so the claim cannot be narrowed to "LISA-specific" and then rhetorically defeated by pointing at a different GW mission. This is a strengthening, not a softening — and it is the one place I push past mack's current M2 wording.

**D2.2 — re-pin to `PENDING-SUBSTRATE-RECOMPUTE` vs a provisional NUMBER on the §7.2 cell.** mack's M2(2) holds the §7.2 cell at "value pending S97." I agree the canonical CONSTANT must be `PENDING` (no derived `Ω_peak` exists, so no honest tail value exists). But there is a residual on the §7.2 *prose cell*: should it carry a provisional order-of-magnitude bound, or nothing? My position: carry the **upper bound that is slope-independent**, not a single value. From the slope-grid I computed this turn (Ω_peak normalized to the GW-energy ceiling, `log10 Ω_peak = 0`), the LISA tail is ≤ `10^(−42.45)` even at the SHALLOWEST physical causal exponent `p=1` — i.e. 29.45 OOM below LISA-PLS regardless of what S97 returns for `p`. So the §7.2 cell CAN honestly carry "LISA-band amplitude < 10⁻⁴² (slope-independent upper bound; exact value PENDING S97)" rather than a bare PENDING with no magnitude. mack may prefer bare PENDING (cleaner, no provisional number to retract); I prefer the slope-independent bound (it makes the LISA-sterility a stated quantitative fact, not a deferral). **Residual**: bare-PENDING (mack-leaning) vs PENDING-plus-slope-independent-upper-bound (my-leaning). Both are honest; it is mack's sole-writer call, but I flag it so the choice is deliberate.

**D2.3 — does the (A)/(C) split stay on §7.2 at all, or move off the falsifier surface entirely?** mack's M2(3) RETAINS the 47.081 OOM (A)/(C) split as a "separate structural result" companion row. I agree it survives as a *number* (`OOM_split_AC_regulator_class = 47.081`, S86, superseded=False — I re-verified). My residual is presentational: the split is a regulator-class *separation* statement, never a *detectability* statement (mack's own M1 substitution chain shows it is "a split between two LISA-sterile numbers"). Keeping it on the §7.2 *falsifier* surface risks a reader inferring it bounds something observable. **Residual**: I lean toward moving the (A)/(C) split OFF §7.2 (the falsifier surface) and onto a methodology/regulator-class registry row, with §7.2 carrying only a pointer — so the falsifier surface contains only things a detector could actually test. mack leans toward retaining it as a structural-orthogonal-companion on §7.2. Not load-bearing for the physics; it is a question of what the falsifier surface is FOR.

None of these three reopen the −127.4 OOM, the Case-A resolution, or the flagship death. They are wording/placement dispositions for mack's sole-writer R3-B edit. D2.1 is the one I will press hardest in QUESTIONS.

### EMERGENCE

**E2.1 — The GW falsifier does not vanish; it MIGRATES to large-scale structure. The substrate's acoustic readout is observable in galaxy surveys, not GW detectors.** This is the constructive half of the closure and the durable structural change. The death of the §7.2 LISA flagship is not a loss of a falsifier — it is a relocation of the falsifier to the correct instrument. Two live LSS acoustic falsifiers inherit the surface the GW flagship vacates:

- **First-sound BAO ring (W6-2, PASS, `audit_sha256=b74ccd561136efc57f3f994e7e302bd9a0215a7d616c9e0096810ab9bf64955c`).** `A_FS = 0.204 = c₂²/c₁²` imprint on the matter P(k) at `k₁ = 0.0193 Mpc⁻¹`; SNR **8.6** at DESI-5yr (σ_exp FETCHED, arXiv:2411.19738v2), **5.1** at DESI-DR1 now. Zero free parameters, no ΛCDM counterpart (the second-sound mode has no analog). This is the live near-term zero-parameter falsifier — and it is a DESI/Euclid P(k) measurement, not a GW-detector measurement.
- **f·σ₈ growth suppression (W6-1, INFO).** −4.058% product suppression, S₈-tension-relieving; forward-edge at DESI-5yr (1.0σ) / Euclid (1.5σ). LSS, not GW; conditional on zero-free-parameter status.

The structural truth: **a source's intrinsic emission scale decides the instrument.** The substrate has ONE frequency scale (M_KK); the fold radiates at it (~10⁴⁰ Hz); the acoustic IMPRINT, by contrast, lives at the matter-clustering scale (`k₁ = 0.0193 Mpc⁻¹`) where galaxy surveys operate. This is the same detector-band discipline I apply to LRD: a virial mass from a measured broad-line width + measured continuum luminosity is defensible; an SED-template mass that assumed the AGN fraction it was measuring is not — and "Ω_GW peak in the LISA band" was the cosmological analog of the assumed-template inference, asserting the headline instrument (LISA) without deriving the emission frequency. W6-3 made that quantitative; the falsifier migrates where the substrate actually radiates.

**E2.2 — LISA-sterility is robust against the ENTIRE slope uncertainty, so resolving `p` does NOT revive the flagship — it only refines a number nobody can detect.** This is the new quantitative insight from this turn, and it sharpens the S97 stakes. The §7.2 death does NOT wait on the S97 slope derivation. I computed the LISA tail across the full plausible causal-exponent grid (Ω_peak normalized to the GW-energy ceiling, `log10 Ω_peak = 0`, Sage-exact this turn):

| IR exponent `p` | log10 Ω(LISA) | OOM below LISA-PLS (10⁻¹³) |
|:----------------|:--------------|:---------------------------|
| p=1 (shallowest causal) | −42.451 | 29.45 |
| p=2 | −84.903 | 71.90 |
| p=3 (Hiramatsu default) | −127.354 | 114.35 |
| p=4 | −169.806 | 156.81 |
| p=5 | −212.257 | 199.26 |

Even the SHALLOWEST physically-admissible causal exponent (`p=1`, the gentlest rise that is still analytic-and-causal at low f) puts the LISA tail 29.45 OOM below LISA-PLS. Every steeper exponent — including any van-Hove-DOS *enhancement* that steepens `p` above 3 — goes deeper. So the LISA-sterility verdict is INDEPENDENT of the S97 slope outcome: there is no causal `p` that revives the LISA flagship. S97's job is therefore NOT to decide whether LISA sees it (it does not, robustly) but to pin the SHAPE so the canonical store's IR-tail NUMBER matches the PROSE — closing the 127-OOM number-vs-prose drift, not deciding detectability. This reframes S97 from "does the flagship survive" (already answered: no) to "what is the honest re-pin value."

**E2.3 — The two-gate S97 structure (PEAK-HEIGHT → SPECTRAL-SHAPE) emerges as the correct decomposition because `Ω_peak` and `p` are different observables on different sides of the inventory.** mack's M3-Q1 split is the right shape and it falls out of the over-conceding guard (CONVERGENCE #3): `Ω_peak` CANNOT come from the placeholder pivot (back-out gives 10^117, unphysical), so it needs its own substrate derivation at the peak frequency — and that derivation is on mack's side (the S86/S87 squeezed-graviton/amplitude machinery, the inventory domain). The IR slope `p` is the spectral-SHAPE question — the fold-DOS causal-rise exponent — which is my detector-band/peak-owner domain. The clean decomposition: **`S97-OMEGAGW-PEAK-HEIGHT` (mack: derive `Ω_peak` from the fold DOS at 8.4835e39 Hz) FEEDS `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE` (little-red-dots: derive `p`, propagate `Ω_peak·(f_LISA/f_peak)^p` to LISA, confirm < LISA-PLS, re-pin)**. This supersedes my L4 single-gate pre-registration with `Omega_peak_source: ADJUDICATED_IN_W3` — which I now retract (CONVERGENCE #3), because `Ω_peak` is not adjudicable from existing artifacts. The two-gate structure also matches the canonical write-order: mack's PEAK-HEIGHT gate produces the constant he then re-pins as sole inventory writer; my SPECTRAL-SHAPE gate consumes it and produces the LISA-tail re-pin value.

### QUESTIONS

**Answers to mack's M3.**

**M3-Q1 (split S97 into PEAK-HEIGHT → SPECTRAL-SHAPE): YES, accepted, and I retract my single-gate L4 pre-registration.** You are right that `Ω_peak` cannot come from the placeholder pivot (the 10^117 back-out is unphysical), so it needs its own substrate derivation on YOUR side of the inventory. The two-gate decomposition: **(a) `S97-OMEGAGW-PEAK-HEIGHT` — you derive `Ω_peak` from the fold DOS at `f_peak = 8.4835e39 Hz` via the S86/S87 squeezed-graviton machinery (amplitude/inventory domain, sole-writer); (b) `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE` — I derive the IR slope `p` from the fold DOS, propagate `Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p`, confirm `< LISA-PLS`, and produce the re-pin value (peak-owner/detector-band domain).** Gate (a) feeds gate (b); my `Omega_peak_source: ADJUDICATED_IN_W3` machinery_pin (L4 line 180) is RETRACTED and replaced by `Omega_peak_source: S97-OMEGAGW-PEAK-HEIGHT (upstream gate, mack)`. The `depends_on` of gate (b) gains `S97-OMEGAGW-PEAK-HEIGHT` as an UPSTREAM in-session prereq.

**M3-Q2 (does the van Hove DOS modify the IR causal exponent away from `p=3`?): the honest answer is "possibly steepens it, cannot shallow it below the causal floor — and EITHER WAY LISA-sterility holds." This is the substrate-physics core of my gate (b) and I will derive it, but the detector verdict does not wait on it.** The standard `p=3` is the causality floor for a stochastic background from a localized sub-horizon source (analyticity + causality at low f). The acoustic emission here is NOT a generic localized source — it is a van-Hove-singularity emission at the fold where `v_g → 0` and the DOS diverges. A DOS *divergence* at the band edge is an emission *enhancement* concentrated at `f_peak`; propagated to the deep IR it can only steepen the effective rise (more spectral weight piled at the peak ⇒ steeper fall-off into the tail), or leave it at the causal floor `p=3` if causality dominates. It cannot make `p < 1` (that would violate low-f analyticity). I verified the consequence this turn across `p ∈ {1,2,3,4,5}` (EMERGENCE E2.2 table): the LISA tail is 29.45 OOM below LISA-PLS at the SHALLOWEST admissible `p=1` and deeper for every steeper `p`. So my gate (b) derives `p` for the RE-PIN VALUE (to close the number-vs-prose drift), but the LISA-sterility verdict is slope-robust and already settled. I will report `p` with the fold-DOS derivation, flagged FI/RD per `regulator-pin-discipline.md` if it enters via a Seeley-DeWitt moment (`a_n^{ζ}`).

**M3-Q3 (report LISA-sterility as a function of κ across the swept band): YES, the re-pin you land at R3-B should carry a κ-robustness statement, not a single-κ value — and I confirm it holds.** I verified this turn (Sage-exact): the peak scales linearly with the open `M_KK⁻¹→s` knob κ; reaching the LISA edge needs `κ = 25.056 s/M_KK⁻¹`, which is **42.45 OOM above κ_nat and 11.40 OOM beyond the band upper edge (1e-10)**. At the band corner that MINIMIZES the peak (κ = 1e-10), the peak is still ~10⁷⁰ Hz — 61 decades above LISA. So across the entire physically-swept band [1e-20, 1e-10], the peak is ≥ GHz (W6-3: 121/121 points) and the LISA band is always the deep IR tail. My gate (b) will report `Ω_GW(3 mHz)` as a function of κ over [1e-20, 1e-10] (mirroring W6-3's `regime=VALID` robustness demonstration), so the §7.2 cell you write reads "LISA-sterile across the entire physically-swept normalization," not just at κ_nat. The κ-dependence of the TAIL VALUE enters through both `f_peak(κ)` and `Ω_peak(κ)` — both your PEAK-HEIGHT gate and my SHAPE gate carry the κ-axis, AND'd into a joint LISA-sterility-across-band statement.

**Sharper follow-ups for mack's FINAL turn (R3-B) — the concrete sole-writer edits I need from you.**

**Q-R3B-1 (the EXACT §7.2 prose, detector-band-set-EXPLICIT — D2.1).** Will you commit the §7.2 LISA CGWB row to this wording (or your tightened version of it), making the instrument set explicit so it cannot be narrowed to "LISA-only" and rhetorically defeated by a different GW mission:

> "§7.2 — Acoustic CGWB. The substrate's acoustic readout transduces into the tensor sector with peak frequency `f_peak ≈ 8.4835×10³⁹ Hz` (van Hove fold scale at κ_nat; W6-3, S96-OBS-CGWB-PEAK-FREQ, audit `646e6ad0…`), ≥ GHz across the entire physically-swept M_KK⁻¹→s normalization band [1e-20,1e-10] (κ = 25 s needed to reach LISA, 11.4 OOM beyond band). This is above the band of EVERY realized or proposed GW detector (LISA mHz, PTA nHz, and the GHz/MHz high-frequency program ≲10¹¹ Hz). The LISA band specifically is the causal IR tail of this peak, amplitude ≪ LISA-PLS [PENDING-SUBSTRATE-RECOMPUTE: exact value from S97 fold-DOS slope+height; slope-independent upper bound < 10⁻⁴²]. **The acoustic CGWB is NOT a GW-detector falsifier.** The substrate's acoustic structure is testable in large-scale structure: the first-sound BAO ring (`A_FS = 0.204`, SNR 8.6 DESI-5yr, W6-2, audit `b74ccd56…`) and f·σ₈ growth suppression (−4.06%, W6-1, LSS) are the live zero-parameter near-term acoustic falsifiers."

If you tighten it, the load-bearing elements I need preserved are: (i) the explicit three-instrument-set sterility (not LISA-only), (ii) the PENDING-SUBSTRATE-RECOMPUTE tag with the S97 pointer, (iii) the BAO-ring + f·σ₈ promotion to the live-falsifier rows.

**Q-R3B-2 (the `Omega_GW_Lambda_A_LISA` disposition — exact constant-store + inventory action).** Confirm the precise R3-B action on the constant and the inventory row:
- Constant `Omega_GW_Lambda_A_LISA`: flag `PENDING-SUBSTRATE-RECOMPUTE` (NOT `update_constant` to a new value this workshop — no derived `Ω_peak` exists yet; NOT deleted — the IR-tail amplitude is a real observable). Does your sole-writer protocol record the PENDING flag in the inventory row, the canonical-constants PROVENANCE comment, or both? I want the audit trail to show the `1e-10` is parked-with-reason, not silently dropped.
- `falsifier-master-inventory.md` Row #7 (the GW-detector flagship row): does it get a `supersedes`/audit-pin sub-row pointing at this workshop's adjudication + W6-3 audit `646e6ad0…`, per the canonical write-order Step 3? I want the row to carry the supersession event (W6-3) explicitly so a future reader sees WHY the flagship died.
- The §7.2 provisional cell: bare PENDING vs PENDING-plus-slope-independent-upper-bound-`<10⁻⁴²` (D2.2) — your sole-writer call; state which you land.

**Q-R3B-3 (the (A)/(C) split placement — D2.3).** Do you retain the 47.081 OOM (A)/(C) split as a structural-orthogonal-companion ON the §7.2 falsifier surface, or move it to a regulator-class/methodology registry row with §7.2 carrying only a pointer? Either is honest; I flag that keeping a regulator-class *separation* number on the *falsifier* surface risks a detectability mis-read. State the placement so the wall=0 PASS row and the (A)/(C) split row are unambiguously tagged "structural, NOT detector-testable" wherever they land.

**Q-R3B-4 (do you concur with the slope-robustness reframing of S97's purpose — E2.2?).** I now read S97 as pinning the SHAPE to close the number-vs-prose drift, NOT as deciding LISA detectability (already settled: sterile at every causal `p`). Do you concur, so the S97 carry-forward block in the Wrap-Up states the gate's purpose as "derive `Ω_peak` and `p` to produce the honest IR-tail re-pin value; LISA-sterility is already established slope-robustly," rather than "test whether the flagship survives"? This frames the carry-forward so next session does not re-litigate a settled detector verdict.

---

## Round 2 — mack: Cross-Synthesis

### CONVERGENCE

**We are fully converged on the arithmetic, the Case-A resolution, and — the new load-bearing item — E2.2: the §7.2 GW-detector flagship is dead UNCONDITIONALLY, independent of the unresolved IR slope `p`. I accept little-red-dots's four CONVERGENCE items, his retraction of the `ADJUDICATED_IN_W3` machinery pin, and the two-gate S97 decomposition. Nothing on the arithmetic remains open.**

**1. The −127.4 OOM, the Case-A resolution, and the unphysical back-out all re-verified Sage-exact this turn (QQ-coerced).** I re-ran the full chain against the canonical store, `f_peak = (84835/10000)·10³⁹ Hz` (= `f_obs_CGWB_peak_kappa_nat`, S96-OBS-CGWB-PEAK-FREQ, FAIL, `audit_sha256=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e`, verdict line 155, superseded=False), `f_LISA = 3/1000 Hz`:

```
Step 1:  log10(f_LISA/f_peak) = −42.451453809                          [Sage QQ, this turn]
Step 2:  p=3, Ω_peak=1e-10 (historical placeholder):
            log10 Ω(LISA) = −10 + 3·(−42.451454) = −137.35436143       [Sage-exact]
            ⇒ 80.273387 OOM below (C)-floor (−57.080974); 124.354 OOM below LISA-PLS (−13)
Step 3:  back-out check — IF 1e-10 were the PIVOT value, propagated UP an f³ rise to the peak:
            log10 Ω_peak = −10 − 3·(−42.451454) = +117.35436143        [Sage-exact]
            ⇒ Ω_peak ~ 10^117 ≫ O(1), violates the GW-energy bound by 117 OOM ⇒ UNPHYSICAL
```

This reproduces little-red-dots's CONVERGENCE #1 and #3 to the digit. The triple (pivot value `1e-10`, slope `p=3`, peak frequency 8.4835e39 Hz) is mutually inconsistent — read forward it is the −127.4 OOM contradiction, read backward it is the 10^117 unphysical peak. The provenance-less number `1e-10` is the casualty (per `epistemic-discipline.md §"Evidence Hierarchy"`: W6-3's redshift chain is a *measurement*; `Ω_GW^(A)=1e-10` carries **"No PROVENANCE entry"** — re-verified this turn — and is *commentary*). I concede it without reservation; the casualty is on my side of the inventory.

**2. I ACCEPT little-red-dots's retraction of `Omega_peak_source: ADJUDICATED_IN_W3` (his CONVERGENCE #3 + E2.3) and I OWN the gate that replaces it.** My M3-Q1 already argued `Ω_peak` cannot come from the placeholder pivot (the 10^117 back-out); his retraction of the L4 single-gate pin closes the loop. `Ω_peak` is NOT adjudicable from existing artifacts — it needs its own substrate derivation at the peak frequency from the fold DOS (the S86/S87 squeezed-graviton machinery, MY domain). The two-gate decomposition `S97-OMEGAGW-PEAK-HEIGHT` (mack) → `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE` (little-red-dots) is the correct shape and I commit to authoring the PEAK-HEIGHT leg.

**3. CONVERGENCE on E2.2 — and this is the item that upgrades the §7.2 status change from CONDITIONAL to UNCONDITIONAL.** I verified the slope-robustness grid Sage-exact this turn (Ω_peak normalized to the GW-energy ceiling, `log10 Ω_peak = 0`, the physically-conservative anchor):

| IR exponent `p` | log10 Ω(LISA) = `p·(−42.451454)` | OOM below LISA-PLS (10⁻¹³) |
|:----------------|:---------------------------------|:---------------------------|
| p=1 (shallowest causal) | −42.451454 | 29.451454 |
| p=2 | −84.902908 | 71.902908 |
| p=3 (Hiramatsu default) | −127.354361 | 114.354361 |
| p=4 | −169.805815 | 156.805815 |
| p=5 | −212.257269 | 199.257269 |

The substitution chain for the load-bearing direction claim (`math-scripts.md §"Double-Check Logic"`):

```
Claim: "no causal IR exponent p revives the LISA flagship"
  Step 1:  Ω(LISA) = Ω_peak · (f_LISA/f_peak)^p                          [spectral-shape definition]
  Step 2:  Ω_peak ≤ O(1)  (GW-energy bound)  ⇒  log10 Ω_peak ≤ 0          [physical ceiling]
  Step 3:  f_LISA/f_peak < 1  ⇒  log10(f_LISA/f_peak) = −42.451454 < 0    [W6-3; peak 42 dec above LISA]
  Step 4:  p ≥ 1 (causality/analyticity floor at low f)                   [shallowest admissible exponent]
  Step 5:  log10 Ω(LISA) = log10 Ω_peak + p·log10(f_LISA/f_peak)
                         ≤ 0 + 1·(−42.451454) = −42.451454                [maximized at p=1, Ω_peak=O(1)]
  Conclusion: even the SHALLOWEST causal exponent puts Ω(LISA) ≤ 10^−42.45,
              29.45 OOM below LISA-PLS. Every steeper p (including any van-Hove-DOS
              enhancement that STEEPENS p above 3) goes deeper. ⇒ LISA-sterile for ALL p ≥ 1.
```

This is the decisive structural upgrade: the §7.2 death does **not** wait on the S97 slope. Whatever `p` the fold DOS returns, `Ω(LISA)` is bounded above by `10⁻⁴²` (slope-independent), 29.45 OOM below LISA-PLS. As §7.2 sole writer I therefore land the LISA-CGWB-flagship down-tag at R3-B as an **unconditional** status change, not a conditional-pending-S97 one. S97 refines the re-pin VALUE (closing the number-vs-prose drift); it does NOT decide detectability, which is already settled slope-robustly. **CONCUR with Q-R3B-4.**

**4. The two-gate S97 structure (E2.3) is the correct decomposition and matches the canonical write-order.** `Ω_peak` (a height, MY S86/S87 amplitude/inventory domain) and `p` (the fold-DOS causal-rise exponent, little-red-dots's detector-band/peak domain) are different observables on different sides of the inventory. The clean split: `S97-OMEGAGW-PEAK-HEIGHT` (mack derives `Ω_peak` from the fold DOS at `f_peak = 8.4835e39 Hz`) FEEDS `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE` (little-red-dots derives `p`, propagates `Ω_peak·(f_LISA/f_peak)^p` to LISA, confirms `< LISA-PLS`, produces the re-pin value). My PEAK-HEIGHT gate produces the constant I then re-pin as sole inventory writer; his SPECTRAL-SHAPE gate consumes it. ACCEPTED.

### DISSENT

The arithmetic and the flagship-death are fully converged; what remains are the three narrow disposition residuals little-red-dots flagged for my sole-writer R3-B wording (D2.1/D2.2/D2.3). I settle all three here so R3-B is a mechanical landing. On two of them I move TO little-red-dots's position; on the third I hold mine, with the reason stated.

**D2.1 — detector-band-set-EXPLICIT: I ADOPT little-red-dots's stronger wording. The §7.2 sterility is scoped to the EXPLICIT three-instrument set (LISA AND PTA AND the high-frequency GW program), NOT "LISA-only."** This is a strengthening, and the substitution chain makes it forced, not rhetorical:

```
Claim: "the acoustic CGWB peak is above the band of EVERY realized/proposed GW detector"
  Step 1:  f_peak(κ_nat) = 8.4835e39 Hz                                  [W6-3, audit 646e6ad0…]
  Step 2:  decades_above_GHz = 31.93                                     [W6-3 verdict field, line 155]
  Step 3:  the high-frequency GW program (resonant cavities, GHz/MHz detectors)
           tops out ≲ 10¹¹ Hz                                           [detector-band ceiling]
  Step 4:  log10(f_peak / 10¹¹ Hz) = log10(8.4835e39) − 11 = 28.93       [decades above the HF ceiling]
  Step 5:  and across the swept band the peak MINIMIZES at κ=1e-10 → still ~10⁷⁰ Hz (≥ GHz, 121/121 pts, W6-3)
  Conclusion: the peak is ≥ 29 decades above the ceiling of EVERY current/proposed GW instrument
              (LISA mHz, PTA nHz, HF ≲10¹¹ Hz), across the entire physically-swept normalization.
              "LISA-sterile" understates it: the channel is GW-DETECTOR-sterile, full stop.
```

I was wording M2(1) as "LISA-sterile" because LISA is the historical flagship instrument; little-red-dots is correct that this invites a mis-read ("maybe a different GW mission catches the peak"). The honest statement is the stronger one. **R3-B §7.2 prose will carry the explicit instrument set.** This is the one place I move past my own R1 M2 wording, and I move toward the stronger claim.

**D2.2 — PENDING-plus-slope-independent-upper-bound: I ADOPT little-red-dots's position. The §7.2 cell carries `< 10⁻⁴²` (slope-independent), NOT a bare PENDING.** I had leaned bare-PENDING (cleaner, no provisional number to retract). But D2.2 is right that the canonical CONSTANT (`Omega_GW_Lambda_A_LISA`) being `PENDING-SUBSTRATE-RECOMPUTE` is a SEPARATE object from the §7.2 PROSE cell, and the prose cell can honestly carry a *bound* even when the exact *value* is pending. The bound is slope-independent and Sage-verified this turn: at the shallowest causal `p=1` with `Ω_peak ≤ O(1)`, `log10 Ω(LISA) ≤ −42.451454`, i.e. `Ω(LISA) < 10⁻⁴²`, 29.45 OOM below LISA-PLS — and this holds for ALL `p ≥ 1` (every steeper exponent is deeper). Carrying the bound makes the LISA-sterility a *stated quantitative fact*, not a deferral — which is the more useful and more honest disposition. The bound is NOT the re-pin value (that is PENDING S97); it is a slope-independent ceiling that S97 can only tighten. **R3-B §7.2 cell: "LISA-band amplitude < 10⁻⁴² (slope-independent upper bound; exact value PENDING-SUBSTRATE-RECOMPUTE per S97 fold-DOS slope+height)."** The distinction matters: the CONSTANT is parked PENDING (no derived value exists); the PROSE carries a derived BOUND (which does exist, slope-independently). Both honest, and together they are sharper than bare PENDING.

**D2.3 — the (A)/(C) split placement: I HOLD my position (retain on §7.2 as a structural-orthogonal-companion), with the mis-read guard little-red-dots asks for built in.** This is the one residual where I do not move to his position, and the reason is registry-structural, not rhetorical:

- little-red-dots leans toward moving the 47.081 OOM (A)/(C) split OFF the §7.2 falsifier surface entirely (onto a methodology/regulator-class registry row), so the falsifier surface contains only detector-testable things. His concern — that keeping a regulator-class *separation* number on the *falsifier* surface invites a detectability mis-read — is legitimate.
- But the split and the wall=0 leg are the two SURVIVING structural results of the W6-4 gate, and §7.2 is where the GW channel's status is narrated. Removing the split entirely from §7.2 risks the opposite failure: a future reader sees the LISA flagship retired and concludes the *entire* W6-4 gate collapsed, losing the durable structural content. Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"`, the wall-topology leg (`Ω_GW^{walls}=0` via π₀(U(1))=0) and the (A)/(C) split are STRUCTURAL-ORTHOGONAL-COMPANION to the (re-opened) amplitude leg — they belong in the same §-anchor as a companion, never co-primary.
- **Resolution that honors both concerns**: I retain the (A)/(C) split on §7.2 as an explicitly-tagged structural-orthogonal-companion row, carrying the verbatim guard little-red-dots asks for — `[STRUCTURAL regulator-class SEPARATION, NOT detector-testable; the 47.081 OOM is a ratio between two LISA-STERILE numbers, per the M1 substitution chain]`. The wall=0 PASS row gets the same `[STRUCTURAL topological result, NOT a detector signal]` tag. This keeps the falsifier surface honest (every non-detector-testable item is explicitly marked as such) WITHOUT amputating the surviving structural content from the section where the GW channel lives. If little-red-dots prefers a pointer-only arrangement at R3, I will reconsider — but my sole-writer default is retain-with-explicit-tag, because the mis-read risk cuts both ways and the explicit tag closes it directly.

So: D2.1 ADOPTED (stronger), D2.2 ADOPTED (bound not bare-PENDING), D2.3 HELD (retain-with-explicit-guard-tag). All three are now pinned for a mechanical R3-B write.

### EMERGENCE

**The §7.2 GW-detector flagship is retired to a GW-DETECTOR-sterile / LSS-falsifier form UNCONDITIONALLY (E2.2 is what makes it unconditional), and the live acoustic falsifiers are the first-sound BAO ring + f·σ₈ — observables in galaxy surveys, not GW detectors. I stage the exact R3-B sole-writer landings here so my final turn is mechanical.**

**The durable structural change (not a numerical revision).** This is a structural change per `output-standards.md §"What Changed"`: the §7.2 GW-detector flagship changes *epistemic type* — from a "LISA-detectable, 11+ OOM above LISA-PLS" GW-detector falsifier to a GW-detector-STERILE substrate observable whose testable imprint lives in LSS. It is not a band-narrowing or an OOM-sharpening; it is a relocation of the falsifier to the correct instrument. The substrate did not get weaker — the instrument was wrong from the start. The substrate-first frame is preserved exactly: the substrate IS the acoustic emission; the register tag (GW-detector-sterile / PENDING-RECOMPUTE) scopes the detector reach; the arrow `D_K → van Hove fold DOS → acoustic Ω_GW(f) → measurement` is unchanged.

**E2.2 is the upgrade that removes the last conditionality.** Before this turn the §7.2 down-tag could have been read as "pending S97's slope `p`." little-red-dots's slope-robustness finding (re-verified Sage-exact above) removes that: for ALL causal `p ≥ 1`, `Ω(LISA) < 10⁻⁴²` (slope-independent), 29.45 OOM below LISA-PLS. There is no `p` the fold DOS could return that revives the LISA flagship. So the flagship-death is UNCONDITIONAL now, and S97's purpose is reframed (Q-R3B-4): pin the SHAPE to produce the honest IR-tail re-pin VALUE and close the 127-OOM number-vs-prose drift — NOT decide detectability (settled).

**The live acoustic falsifiers migrate to LSS (E2.1) — the constructive half.** The GW flagship vacates the surface; two zero-parameter LSS acoustic falsifiers inherit it:
- **First-sound BAO ring (W6-2, PASS, `S96-OBS-FIRST-SOUND-RING`, `audit_sha256=b74ccd561136efc57f3f994e7e302bd9a0215a7d616c9e0096810ab9bf64955c`, line 149).** `A_FS = 0.204000` (`= c₂²/c₁²` two-fluid ratio; `A_ring_at_k1 = 0.203154`; `A_first_sound_S43 = 0.204499`) on the matter P(k) at `k₁ = 0.0193150 Mpc⁻¹` (`r₁ = 325.30 Mpc`); **SNR 8.6341 at DESI-5yr** (σ_exp FETCHED, arXiv:2411.19738v2, Chen/Ding/Paillas et al.), **5.0789 at DESI-DR1**. Zero free parameters, no ΛCDM counterpart (the second-sound mode has no analog). The live near-term falsifier — a DESI/Euclid P(k) measurement, not a GW-detector measurement.
- **f·σ₈ growth suppression (W6-1, INFO, `S96-OBS-FSIGMA8-FORECAST`, line 143).** `product_supp_max = −4.058% @ z=0.51`, S₈-tension-relieving (`S8_relieving=1`), `σ_DESI5yr = 1.013` at z=0.51 / Euclid forward-edge. LSS, not GW; conditional on zero-free-parameter status.

The structural truth: **a source's intrinsic emission scale decides the instrument.** The substrate has ONE frequency scale (M_KK); the fold radiates at it (~10⁴⁰ Hz, above every GW detector); the acoustic IMPRINT lives at the matter-clustering scale (`k₁ = 0.0193 Mpc⁻¹`) where galaxy surveys operate. "Ω_GW peak in the LISA band" asserted the headline instrument without deriving the emission frequency — the container-intuition error W6-3 made quantitative.

---

**STAGED FOR R3-B (deliberation now; the framework-file edits land at my FINAL turn as §7 falsifier-surface sole writer). Answering Q-R3B-1 through Q-R3B-3 so R3-B is a mechanical landing:**

**Q-R3B-1 — the EXACT §7.2 prose (detector-band-set-EXPLICIT, D2.1 ADOPTED; bound-carrying, D2.2 ADOPTED).** I commit the §7.2 LISA-CGWB row to this wording at R3-B (little-red-dots's three load-bearing elements preserved: explicit three-instrument sterility; PENDING-SUBSTRATE-RECOMPUTE + S97 pointer; BAO-ring + f·σ₈ promotion):

> **§7.2 — Acoustic CGWB.** The substrate's acoustic readout transduces into the tensor sector with peak frequency `f_peak ≈ 8.4835×10³⁹ Hz` (van Hove fold scale at κ_nat; W6-3, S96-OBS-CGWB-PEAK-FREQ, audit `646e6ad0…`), ≥ GHz across the entire physically-swept M_KK⁻¹→s normalization band [1e-20, 1e-10] (reaching LISA needs κ = 25.06 s/M_KK⁻¹ = 42.5 OOM above κ_nat, 11.4 OOM beyond the band; 121/121 swept points are GHz+). This is above the band of **EVERY realized or proposed GW detector** — LISA (mHz), PTA (nHz), and the GHz/MHz high-frequency program (≲ 10¹¹ Hz; the peak is ≥ 29 decades above this ceiling). The LISA band specifically is the causal IR tail of this peak: **LISA-band amplitude < 10⁻⁴²** (slope-independent upper bound — for every causal IR exponent `p ≥ 1` with `Ω_peak ≤ O(1)`, `Ω(LISA) ≤ 10^−42.45`, ≥ 29.45 OOM below LISA-PLS; exact value `PENDING-SUBSTRATE-RECOMPUTE` per S97 fold-DOS slope+height). **The acoustic CGWB is NOT a GW-detector falsifier.** The substrate's acoustic structure is testable in large-scale structure: the **first-sound BAO ring** (`A_FS = 0.204`, SNR 8.6 DESI-5yr, W6-2, audit `b74ccd56…`) and **f·σ₈ growth suppression** (−4.06%, W6-1, LSS) are the live zero-parameter near-term acoustic falsifiers.

**Q-R3B-2 — the `Omega_GW_Lambda_A_LISA` disposition (constant-store + inventory Row #7 action).** Precise R3-B actions:
- **Constant `Omega_GW_Lambda_A_LISA`**: flag `PENDING-SUBSTRATE-RECOMPUTE` in **BOTH** the inventory row AND the `canonical_constants.py` PROVENANCE comment (little-red-dots asked which; answer: both — the audit trail must show the `1e-10` is parked-with-reason at both the registry layer and the constant-store layer, not silently dropped at either). NOT `update_constant` to a new value (no derived `Ω_peak` exists yet — Class-(f) PIN-PLACEHOLDER + Class-(c) PIN-DRIFT-FROM-STALE-SOURCE, W6-3 the supersession event); NOT deleted (the IR-tail amplitude `Ω_peak·(f_LISA/f_peak)^p` is a real substrate observable).
- **`falsifier-master-inventory.md` Row #7** (the GW-detector flagship row): gets an audit-pin **supersedes sub-row** per the canonical write-order Step 3, citing BOTH this workshop's adjudication AND the W6-3 supersession audit `646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e` (full 64-hex) — so a future reader sees WHY the flagship died (peak 42 decades out, amplitude slope-robustly < 10⁻⁴²). The row's disposition flips to `GW-DETECTOR-STERILE → LSS-falsifier-migrated`, with the live rows pointing at W6-2 (`b74ccd56…`) and W6-1.
- **§7.2 provisional cell**: PENDING-plus-slope-independent-upper-bound `< 10⁻⁴²` (D2.2 ADOPTED), NOT bare PENDING.

**Q-R3B-3 — the (A)/(C) split placement (D2.3 HELD, with the mis-read guard).** I RETAIN the 47.081 OOM (A)/(C) split (`OOM_split_AC_regulator_class = 47.081`, S86, W6-4 `audit_sha256=a9998118…`, superseded=False) on the §7.2 surface as a structural-orthogonal-companion row, explicitly tagged `[STRUCTURAL regulator-class SEPARATION — NOT detector-testable; the 47.081 OOM is a ratio between two LISA-STERILE numbers (M1 substitution chain)]`. The wall=0 PASS row (`Ω_GW^{walls}=0` EXACTLY via π₀(U(1))=0) is likewise retained and tagged `[STRUCTURAL topological result — NOT a detector signal]`. Both are STRUCTURAL-ORTHOGONAL-COMPANION to the re-opened amplitude leg, never co-primary (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"`). This closes little-red-dots's detectability-mis-read concern via explicit tagging while keeping the surviving structural content in the section where the GW channel is narrated. (Also for the R3-B record, distinct from the `1e-10` defect: the W6-4 results note that the rule-prose "`1e-57` understates Ω_GW^(C) by ~10×" is itself overstated — exact ratio `1e-57/8.299e-58 = 1.205×` = 0.081 OOM, SAME decade, re-confirmed `round_fig_1e-57_understate=1.205x_0.081OOM` in the W6-4 verdict. That fidelity fix is about the (C)-class single value and the (A)/(C) split — both of which SURVIVE — and must not be conflated with the `1e-10` (A)-class LISA-band defect, the 127-OOM problem.)

**Q-R3B-4 — concur with the slope-robustness reframing of S97's purpose (E2.2): YES.** Per CONVERGENCE #3 above, the LISA-sterility is established slope-robustly (< 10⁻⁴² for all `p ≥ 1`), so S97 does NOT test "whether the flagship survives" (settled: it does not). The S97 carry-forward block in the Wrap-Up will state the gate's purpose as **"derive `Ω_peak` (mack, PEAK-HEIGHT) and `p` (little-red-dots, SPECTRAL-SHAPE) to produce the honest IR-tail re-pin value and close the 127-OOM number-vs-prose drift; LISA-sterility / GW-detector-sterility is already established slope-robustly"** — so next session does not re-litigate a settled detector verdict.

---

## Round 3 — little-red-dots: Follow-up

### CONVERGENCE

**Full convergence — zero residual of substance. mack settled all three disposition residuals (D2.1/D2.2/D2.3) as sole writer, and on the two that were genuine open choices he adopted my stronger positions; on the third his `[STRUCTURAL — NOT detector-testable]` guard tag resolves my placement concern directly. The arithmetic, the Case-A resolution, the unconditional flagship-death (E2.2), and the two-gate S97 decomposition were already closed in Round 2; what Round 2-mack added is the disposition lockdown that makes R3-B a mechanical write. I re-verified every load-bearing number this turn against the canonical store and the verdict file.**

**1. D2.1 ADOPTED — GW-detector-sterile via the explicit three-instrument set (not "LISA-only"). CONVERGED.** mack adopted my stronger wording and supplied the forcing substitution chain (R2-mack DISSENT D2.1). I re-confirm it Sage-exact this turn, against the W6-3 verdict-line fields (line 155: `decades_above_GHz=31.93`, `decades_above_LISA=43.93`):

```
Claim: "the acoustic CGWB peak is above the band of EVERY realized/proposed GW detector"
  Step 1:  f_peak(κ_nat) = 8.4835e39 Hz                                  [W6-3, S96-OBS-CGWB-PEAK-FREQ, audit 646e6ad0…, line 155, superseded=False]
  Step 2:  log10(f_peak / 10¹¹ Hz) = log10(8.4835e39) − 11 = 28.928575   [Sage QQ, this turn — HF-program ceiling ≲10¹¹ Hz: resonant cavities, GHz/MHz program]
  Step 3:  log10(f_peak / 1e-4 Hz)  = 43.928575                          [Sage QQ — decades above LISA low edge; matches verdict-field decades_above_LISA=43.93]
  Step 4:  across the swept band the peak MINIMIZES at κ=1e-10 → still ~10⁷⁰ Hz (≥ GHz; 121/121 pts; verdict any_LISA_in_sweep=False)
  Conclusion: the peak is ≥ 28.93 decades above the ceiling of EVERY current/proposed GW instrument
              (LISA mHz, PTA nHz, HF program ≲10¹¹ Hz), across the entire physically-swept normalization.
              The channel is GW-DETECTOR-sterile, not merely LISA-sterile.
```

This is a strengthening, and it is the one place where the disposition moved past mack's R1 M2 wording — toward the stronger claim, not a softer one. The honest §7.2 statement scopes sterility to the explicit instrument set so the claim cannot be narrowed to "LISA-specific" and rhetorically defeated by pointing at a different GW mission. mack commits the explicit three-instrument-set prose at R3-B (his staged Q-R3B-1). CONVERGED on my stronger position.

**2. D2.2 ADOPTED — the §7.2 prose cell carries the slope-independent bound `< 10⁻⁴²`, not bare PENDING. CONVERGED.** mack adopted my position (R2-mack DISSENT D2.2) and drew the CONSTANT-vs-PROSE distinction exactly right: the canonical constant `Omega_GW_Lambda_A_LISA` is `PENDING-SUBSTRATE-RECOMPUTE` (no derived `Ω_peak` exists, so no honest tail VALUE exists), while the §7.2 PROSE cell carries a derived slope-independent BOUND that does exist. I re-verified the bound Sage-exact this turn:

```
Claim: "the LISA-band amplitude is < 10⁻⁴² for EVERY causal IR exponent, slope-independently"
  Step 1:  Ω(LISA) = Ω_peak · (f_LISA/f_peak)^p                          [spectral-shape definition]
  Step 2:  Ω_peak ≤ O(1)  (GW-energy bound)  ⇒  log10 Ω_peak ≤ 0          [physical ceiling]
  Step 3:  log10(f_LISA/f_peak) = −42.4514538094577 < 0                   [Sage QQ, this turn; W6-3 peak 42.45 dec above LISA]
  Step 4:  p ≥ 1 (causality/analyticity floor at low f)                  [shallowest admissible causal exponent]
  Step 5:  log10 Ω(LISA) = log10 Ω_peak + p·log10(f_LISA/f_peak)
                         ≤ 0 + 1·(−42.4514538) = −42.4514538             [maximized at p=1, Ω_peak=O(1)]
  Conclusion: Ω(LISA) ≤ 10^(−42.451) < 10⁻⁴², i.e. ≥ 29.4514538 OOM below LISA-PLS (10⁻¹³),
              for ALL p ≥ 1. The published bound `< 10⁻⁴²` rounds the exact ceiling 10^(−42.451) UP
              (i.e. it is conservative — the true value is strictly below it).
```

The bound is NOT the re-pin value (that is PENDING S97); it is a slope-independent ceiling that S97 can only tighten. Carrying it makes the LISA-sterility a stated quantitative fact rather than a deferral — the more useful and more honest disposition. CONVERGED on my position.

**3. D2.3 HELD — ACCEPTED. The `[STRUCTURAL — NOT detector-testable]` guard tag resolves my (A)/(C)-placement concern; the split stays on §7.2 but is explicitly non-detector-testable.** This is where I accept mack's sole-writer hold rather than press my lean, and I state why the resolution is correct, not a compromise. My residual (R2 DISSENT D2.3) was that keeping the 47.081 OOM (A)/(C) regulator-class *separation* number on the *falsifier* surface invites a detectability mis-read. mack's hold (R2-mack DISSENT D2.3) showed the mis-read risk **cuts both ways**: removing the split entirely from §7.2 risks the OPPOSITE failure — a future reader sees the LISA flagship retired and wrongly concludes the *entire* W6-4 gate collapsed, amputating the durable structural content (the (A)/(C) split and the wall=0 topology both SURVIVE). The explicit guard tag closes my concern directly without incurring the opposite one:

- (A)/(C) split row: `[STRUCTURAL regulator-class SEPARATION — NOT detector-testable; the 47.081 OOM is a ratio between two LISA-STERILE numbers (M1 substitution chain)]`. I re-verified the number stands: `OOM_split_AC_regulator_class = 47.081` (S86, W6-4 `audit_sha256=a9998118…`, superseded=False); Sage-exact `(A)/(C) = 47.080974235`, and `log10 Ω^(C) = −58.080974` confirms the floor I cited. The split was always a regulator-class separation statement, never a detectability guarantee — mack's M1 chain proved it is "a split between two LISA-STERILE numbers."
- wall=0 row: `[STRUCTURAL topological result — NOT a detector signal]`. `Ω_GW^{walls} = 0` EXACTLY via π₀(U(1))=0 (W6-4, audit `a9998118…`, line 136) is regulator-invariant and untouched by the amplitude re-opening.

Both are STRUCTURAL-ORTHOGONAL-COMPANION to the re-opened amplitude leg, never co-primary (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`). With every non-detector-testable item explicitly marked as such, the falsifier surface stays honest AND the surviving structural content stays in the section where the GW channel is narrated. The guard tag is the right structural instrument: it makes the "structural-not-detector-testable" status a property of the row itself, not of where a reader happens to file it. **ACCEPTED D2.3-HELD without residual.**

**The fully-converged resolution (one sentence each leg).** (i) The −127.4 OOM is real; the provenance-less `1e-10` is the casualty, not the redshift-chain peak (W6-3 `646e6ad0…` is a *measurement*; `Ω_GW^(A)=1e-10` carries "No PROVENANCE entry" — *commentary*). (ii) Case A: `1e-10` was a pivot-band value under an assumed peak-at-3-mHz, refuted by W6-3's peak at 8.4835e39 Hz; the disposition is RE-PIN (the IR-tail amplitude is a real observable), not RETIRE. (iii) The §7.2 GW-detector flagship is dead UNCONDITIONALLY (E2.2: `Ω(LISA) < 10⁻⁴²` for all `p ≥ 1`, slope-independent). (iv) `Omega_GW_Lambda_A_LISA` → `PENDING-SUBSTRATE-RECOMPUTE` in both inventory and canonical_constants; §7.2 prose carries the explicit-instrument-set sterility + the `< 10⁻⁴²` bound; the wall=0 and (A)/(C) rows stay with `[STRUCTURAL — NOT detector-testable]` guards; the live acoustic falsifiers migrate to first-sound BAO ring (W6-2, SNR 8.6341) + f·σ₈ (W6-1).

### DISSENT

**None of substance.** The arithmetic was fully converged at Round 2; mack's Round-2 disposition settlement (D2.1/D2.2 ADOPTED to my positions, D2.3 HELD with the guard tag I accept) closes the last three wording/placement residuals. There is no remaining tension on the physics, the Case-A resolution, the unconditional flagship-death, the two-gate S97 split, or any number. Every figure I cite reproduces Sage-exact and matches the canonical store + the verdict file (lines 136, 149, 155). The only items left are mack's mechanical R3-B sole-writer landings, which I confirm in QUESTIONS — that is a confirmation, not a dissent.

One micro-note for the R3-B record (NOT a dissent — a precision flag so the published bound is not mis-stated as exact): the `< 10⁻⁴²` bound is a CONSERVATIVE rounding of the exact ceiling `10^(−42.4514538)`. The true slope-independent ceiling is `10^(−42.451)`, strictly below `10⁻⁴²`; `< 10⁻⁴²` is correct as an upper bound (the true value is even smaller), so the prose is honest, but the bound should be stated as `< 10⁻⁴²` (an inequality), never as `≈ 10⁻⁴²` (which would understate the sterility by 0.45 OOM). mack's staged Q-R3B-1 prose already states it as the inequality `< 10⁻⁴²`, so this is satisfied — I flag it only so the rounding direction is on the record.

### EMERGENCE

**E3.1 — The §7.2 GW-detector flagship is retired UNCONDITIONALLY to a GW-detector-sterile / LSS-falsifier form. This is a structural change of epistemic type, not a numerical revision.** Per `output-standards.md §"What Changed"`, this belongs in the (b) STRUCTURAL column, not the (a) numerical column: the §7.2 acoustic-CGWB entry changes epistemic TYPE — from a "LISA-detectable, 11+ OOM above LISA-PLS" GW-detector falsifier to a GW-detector-STERILE substrate observable whose testable imprint lives in large-scale structure. It is not a band-narrowing or an OOM-sharpening; it is a relocation of the falsifier to the correct instrument. The unconditionality is the load-bearing upgrade from Round 2 (E2.2): before that finding, the down-tag could have read "pending S97's slope `p`"; the slope-robustness grid removed that conditionality — for ALL causal `p ≥ 1`, `Ω(LISA) < 10⁻⁴²` (re-verified Sage-exact, CONVERGENCE #2 above), so there is no `p` the fold DOS could return that revives the LISA flagship. The substrate-first frame is preserved exactly: the substrate IS the acoustic emission; the register tag (GW-detector-sterile / PENDING-RECOMPUTE) scopes the detector reach; the arrow `D_K → van Hove fold DOS → acoustic Ω_GW(f) → measurement` is unchanged. The substrate did not get weaker — the instrument was wrong from the start.

**E3.2 — The live acoustic falsifiers are the first-sound BAO ring + f·σ₈ — observables in galaxy surveys, not GW detectors. The GW flagship does not vanish; it MIGRATES to LSS.** This is the constructive half of the closure, and it is durable. Two zero-parameter LSS acoustic falsifiers inherit the surface the GW flagship vacates (numbers re-confirmed against the verdict file this turn):

- **First-sound BAO ring (W6-2, PASS, `S96-OBS-FIRST-SOUND-RING`, `audit_sha256=b74ccd561136efc57f3f994e7e302bd9a0215a7d616c9e0096810ab9bf64955c`, line 149).** `A_FS = 0.204000` (`= c₂²/c₁²` two-fluid ratio; `A_ring_at_k1 = 0.203154`) on the matter P(k) at `k₁ = 0.0193150 Mpc⁻¹` (`r₁ = 325.30 Mpc`); **SNR 8.6341 at DESI-5yr** (σ_exp = 0.023529 FETCHED, arXiv:2411.19738v2, Chen/Ding/Paillas et al.), **5.0789 at DESI-DR1**. Zero free parameters, no ΛCDM counterpart (the second-sound mode has no analog). The live near-term zero-parameter falsifier — a DESI/Euclid P(k) measurement, not a GW-detector measurement.
- **f·σ₈ growth suppression (W6-1, INFO, `S96-OBS-FSIGMA8-FORECAST`, line 143).** `product_supp_max = −4.058% @ z=0.51`, S₈-tension-relieving (`S8_relieving=1`), `σ_DESI5yr = 1.013` at z=0.51 / Euclid forward-edge. LSS, not GW; conditional on zero-free-parameter status.

The structural truth — and it is the same detector-band discipline I apply to LRD: **a source's intrinsic emission scale decides which instrument can see it.** The substrate has ONE frequency scale (M_KK); the fold radiates at it (~10⁴⁰ Hz, above every GW detector); the acoustic IMPRINT, by contrast, lives at the matter-clustering scale (`k₁ = 0.0193 Mpc⁻¹`) where galaxy surveys operate. "Ω_GW peak in the LISA band" asserted the headline instrument without deriving the emission frequency — the cosmological analog of an SED-template LRD mass that assumed the AGN fraction it was trying to measure, where the defensible alternative is a virial mass from a measured broad-line width + measured continuum luminosity. W6-3's redshift chain made the band error quantitative; the falsifier migrates where the substrate actually radiates.

**E3.3 — The two-gate S97 structure (PEAK-HEIGHT → SPECTRAL-SHAPE) is the correct decomposition, and S97's purpose is reframed: pin the SHAPE to close the 127-OOM number-vs-prose drift, NOT decide detectability (already settled slope-robustly).** `Ω_peak` (a height, mack's S86/S87 amplitude/inventory domain) and `p` (the fold-DOS causal-rise exponent, my detector-band/peak domain) are different observables on different sides of the inventory, and the split falls out of the over-conceding guard: `Ω_peak` CANNOT come from the placeholder pivot (the back-out gives `log10 Ω_peak = +117.354`, i.e. `~10^117`, unphysical by 117 OOM against the GW-energy bound), so it needs its own substrate derivation at the peak frequency. The clean decomposition, matching the canonical write-order:

- **`S97-OMEGAGW-PEAK-HEIGHT`** (mack): derive `Ω_peak` from the fold DOS at `f_peak = 8.4835e39 Hz` via the S86/S87 squeezed-graviton machinery; produces the constant he then re-pins as sole inventory writer.
- **`S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE`** (little-red-dots): derive the IR slope `p` from the fold DOS; propagate `Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p`; report it as a function of κ over [1e-20, 1e-10] (mirroring W6-3's `regime=VALID` band-robustness demonstration); confirm `< LISA-PLS`; produce the re-pin value. My L4 single-gate pre-registration with `Omega_peak_source: ADJUDICATED_IN_W3` is RETRACTED (CONVERGENCE Round 2 #3) and replaced by `Omega_peak_source: S97-OMEGAGW-PEAK-HEIGHT (upstream gate, mack)`.

The reframing is the durable methodological output: S97 does NOT test "whether the flagship survives" (settled: it does not, for all `p ≥ 1`); it produces the honest IR-tail re-pin value so the canonical store's NUMBER matches the PROSE — ending the 127-OOM number-vs-prose drift that W8-2 left open (W8-2 corrected the prose "LISA samples the IR tail" but left the number `1e-10` standing as if it were the tail value). On the van-Hove-DOS substrate-physics core of my gate (b): the DOS *divergence* at the fold (where `v_g → 0`) is an emission *enhancement* concentrated at `f_peak`; propagated to the deep IR it can only STEEPEN the effective rise (more spectral weight piled at the peak ⇒ steeper fall-off into the tail) or leave it at the causal floor `p=3` — it cannot shallow `p` below the analyticity floor `p=1`. So the derived `p` will be `≥ 1`, the tail is bounded `< 10⁻⁴²` either way, and the LISA-sterility is already settled; gate (b) refines the value, not the verdict. I will report `p` with the fold-DOS derivation, FI/RD-tagged per `regulator-pin-discipline.md` if it enters via a Seeley-DeWitt moment (`a_n^{ζ}`).

### QUESTIONS

**mack's staged Q-R3B-1 through Q-R3B-4 are exactly right for his mechanical R3-B landing. I confirm each as the correct sole-writer action, with one precision confirmation appended.**

**Q-R3B-1 (the EXACT §7.2 prose — detector-band-set-EXPLICIT + bound-carrying): CONFIRMED.** The R2-mack staged prose carries all three load-bearing elements I need preserved: (i) the explicit three-instrument-set sterility (LISA mHz, PTA nHz, HF program ≲10¹¹ Hz — the peak ≥ 28.93 decades above the HF ceiling, Sage-confirmed this turn), so the claim cannot be narrowed to "LISA-only"; (ii) the `LISA-band amplitude < 10⁻⁴²` slope-independent upper bound WITH the `PENDING-SUBSTRATE-RECOMPUTE` tag + S97 pointer for the exact value; (iii) the BAO-ring (SNR 8.6341, `b74ccd56…`) + f·σ₈ promotion to the live zero-parameter falsifier rows. The prose states the bound as the inequality `< 10⁻⁴²` (correct — conservative rounding of the exact ceiling `10^(−42.451)`), not `≈ 10⁻⁴²`. CONFIRMED as-staged.

**Q-R3B-2 (the `Omega_GW_Lambda_A_LISA` disposition — both layers): CONFIRMED.** The disposition is exactly right: (a) flag `PENDING-SUBSTRATE-RECOMPUTE` in **BOTH** the inventory row AND the `canonical_constants.py` PROVENANCE comment — answering my "which layer" question with "both," so the audit trail shows the `1e-10` is parked-with-reason at both the registry layer and the constant-store layer, not silently dropped at either (Class-(f) PIN-PLACEHOLDER + Class-(c) PIN-DRIFT-FROM-STALE-SOURCE, W6-3 the supersession event; NOT `update_constant` to a new value — no derived `Ω_peak` exists; NOT deleted — the IR-tail amplitude is a real observable). (b) `falsifier-master-inventory.md` Row #7 gets an audit-pin **supersedes sub-row** citing BOTH this workshop's adjudication AND the W6-3 supersession audit `646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e` (full 64-hex), so a future reader sees WHY the flagship died — the row disposition flips to `GW-DETECTOR-STERILE → LSS-falsifier-migrated` with the live rows pointing at W6-2 (`b74ccd56…`) and W6-1. (c) §7.2 provisional cell: PENDING-plus-slope-independent-upper-bound `< 10⁻⁴²` (D2.2), not bare PENDING. CONFIRMED as-staged.

**Q-R3B-3 (the (A)/(C) split placement — D2.3 HELD with guard): CONFIRMED.** Retain the 47.081 OOM (A)/(C) split (`OOM_split_AC_regulator_class = 47.081`, S86, W6-4 `audit_sha256=a9998118…`, superseded=False) on §7.2 as a structural-orthogonal-companion row tagged `[STRUCTURAL regulator-class SEPARATION — NOT detector-testable; the 47.081 OOM is a ratio between two LISA-STERILE numbers (M1 substitution chain)]`, and retain the wall=0 PASS row tagged `[STRUCTURAL topological result — NOT a detector signal]`. Both STRUCTURAL-ORTHOGONAL-COMPANION to the re-opened amplitude leg, never co-primary (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"`). I accepted this hold in CONVERGENCE D2.3; the guard tag closes my mis-read concern directly. One ledger note for your record (you raised it in R2 Q-R3B-3, and I confirm it is DISTINCT from the `1e-10` defect, so W8-2 consolidation does not conflate them): the W6-4 fidelity correction `round_fig_1e-57_understate=1.205x_0.081OOM` (the rule-prose "1e-57 understates Ω_GW^(C) by ~10×" is itself overstated — exact ratio `1e-57/8.299e-58 = 1.205×` = 0.081 OOM, SAME decade) is about the (C)-class single value and the (A)/(C) split — both of which SURVIVE — and must stay separate from the `1e-10` (A)-class LISA-band defect, the 127-OOM problem. CONFIRMED as-staged.

**Q-R3B-4 (the slope-robustness reframing of S97's purpose — E2.2): CONFIRMED, and this is the framing I most want preserved in the Wrap-Up carry-forward.** S97 pins the SHAPE to produce the honest IR-tail re-pin value and close the 127-OOM number-vs-prose drift; it does NOT test "whether the flagship survives" (settled slope-robustly: `Ω(LISA) < 10⁻⁴²` for all `p ≥ 1`, 29.45 OOM below LISA-PLS at the shallowest causal exponent). The S97 carry-forward block should state the gate's purpose as "derive `Ω_peak` (mack, PEAK-HEIGHT) and `p` (little-red-dots, SPECTRAL-SHAPE) to produce the honest IR-tail re-pin value and close the number-vs-prose drift; GW-detector-sterility is already established slope-robustly" — so next session does not re-litigate a settled detector verdict. CONFIRMED as-staged.

**One final confirmation for your R3-B mechanical landing (nothing new to resolve — a closeout check).** All four staged actions are mechanical sole-writer landings with no open adjudication remaining: the §7.2 prose (Q-R3B-1), the dual-layer PENDING disposition + Row #7 supersedes sub-row (Q-R3B-2), the (A)/(C)-and-wall=0 guard-tagged companion rows (Q-R3B-3), and the slope-robust S97 carry-forward framing (Q-R3B-4). I have no further residual on any of them; the workshop's adjudication is complete and yours is the mechanical write. The only thing I ask you confirm at R3-B is the one precision point from DISSENT: that the §7.2 bound lands as the inequality `< 10⁻⁴²` (conservative rounding of `10^(−42.451)`), never `≈ 10⁻⁴²`. Over to you for the Verdict + Wrap-Up + the §7.2 sole-writer edits.

---

## Round 3 — mack: Cross-Synthesis

### CONVERGENCE

**Full convergence, zero residual of substance. little-red-dots's Round-3 follow-up confirmed each of my four staged sole-writer actions (Q-R3B-1..4) as the correct mechanical landing, re-verified every load-bearing number Sage-exact against the verdict file (lines 136, 149, 155) and the canonical store, and accepted D2.3-HELD without residual once the `[STRUCTURAL — NOT detector-testable]` guard tag was on the table. The arithmetic, the Case-A resolution, the UNCONDITIONAL flagship-death (E2.2), and the two-gate S97 decomposition were closed at Round 2; Round-3-little-red-dots added only the confirmation that R3-B is a mechanical write. I re-ran the entire numerical spine Sage-exact (QQ-coerced) this final turn before landing — every figure reproduces to the digit.**

**1. The full numerical spine re-verified Sage-exact this turn (QQ).** I re-ran the load-bearing chain one last time before the framework-file write, `f_peak = (84835/10000)·10³⁹ Hz` (= `f_obs_CGWB_peak_kappa_nat`, `S96-OBS-CGWB-PEAK-FREQ`, FAIL, `audit_sha256=646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e`, verdict line 155, superseded=False), `f_LISA = 3/1000 Hz`:

```
log10(f_LISA/f_peak)            = −42.451453809457731754978        [Sage QQ, RealField(200)]
f³ IR suppression               = 3·(−42.451454) = −127.35436142837   [p=3 causal default]
p=3, Ω_peak=1e-10 (placeholder) ⇒ log10 Ω(LISA) = −137.35436142837   [80.273387 OOM below (C); 124.354361 OOM below LISA-PLS]
back-out check (1e-10 as PIVOT, up an f³ rise) ⇒ log10 Ω_peak = +117.35436142837   [≫ O(1); UNPHYSICAL by 117 OOM]
slope-independent ceiling (p=1, Ω_peak≤O(1)) ⇒ log10 Ω(LISA) ≤ −42.451453809        [29.451454 OOM below LISA-PLS]
decades above HF ceiling 10¹¹ Hz = 28.928575064177;   decades above LISA low edge 10⁻⁴ Hz = 43.928575064177
(A)/(C) OOM split               = 47.080974235412639713             [Sage QQ; = log10(1e-10 / 8.299e-58)]
log10 Ω^(C) = log10(8.299e-58)  = −57.080974235412639713            [single-power; the (C)-floor]
```

These reproduce little-red-dots's CONVERGENCE #1–#3 and the Round-3 confirmation tables to the digit. The triple (pivot value `1e-10`, slope `p=3`, peak frequency 8.4835e39 Hz) is mutually inconsistent — read forward it is the −127.4 OOM contradiction, read backward it is the 10^117 unphysical peak — and the provenance-less `1e-10` is the casualty (`epistemic-discipline.md §"Evidence Hierarchy"`: W6-3's redshift chain is a *measurement*; `Ω_GW^(A)=1e-10` carries **"No PROVENANCE entry"** — re-verified `get_constant('Omega_GW_Lambda_A_LISA')` this turn — and is *commentary*).

**One micro-correction for the permanent record (NOT a dissent — a one-decade slip in little-red-dots's R3 prose, fixed before I land it).** little-red-dots's Round-3 CONVERGENCE D2.3 cites `log10 Ω^(C) = −58.080974`. The Sage-exact value is `log10(8.299e-58) = −57.080974235` (the mantissa 8.299 puts it in the −57 decade, not −58). The verdict file line 136 confirms `OmC=8.299e-58`, and the **(A)/(C) split of 47.081 is unaffected** (it is `log10(1e-10/8.299e-58) = 47.080974235`, which I re-verified Sage-exact, and which is independent of the −57-vs-−58 mantissa-vs-exponent slip). I land the inventory rows with the correct `Ω^(C) = 8.299×10⁻⁵⁸` / `log10 Ω^(C) = −57.081` and the correct 47.081 split. The slip changes nothing load-bearing; I flag it only so the §7.2 / inventory text carries the right floor decade.

**2. All four staged Q-R3B actions are confirmed and I land them mechanically at this turn.** little-red-dots confirmed each as the correct sole-writer action with no open adjudication: (Q-R3B-1) the detector-band-set-EXPLICIT + bound-carrying §7.2 prose; (Q-R3B-2) the dual-layer `PENDING-SUBSTRATE-RECOMPUTE` disposition + the Row #7 supersedes sub-row citing W6-3 audit `646e6ad0…` (full 64-hex); (Q-R3B-3) the (A)/(C)-split and wall=0 rows retained on §7.2 with `[STRUCTURAL — NOT detector-testable]` guards; (Q-R3B-4) the slope-robustness reframing of S97's purpose. I accept his one precision confirmation: the §7.2 bound lands as the **inequality `< 10⁻⁴²`** (a conservative rounding of the exact ceiling `10^(−42.451)`, which is strictly below `10⁻⁴²`), NEVER as `≈ 10⁻⁴²` (which would understate the sterility by 0.45 OOM). My staged prose already states it as the inequality; I preserve that.

**3. The flagship-death is UNCONDITIONAL (E2.2), and that is what licenses landing the §7.2 down-tag NOW rather than holding it PENDING-S97.** For ALL causal `p ≥ 1` with `Ω_peak ≤ O(1)`, `log10 Ω(LISA) ≤ 1·(−42.451454) = −42.451454`, i.e. `Ω(LISA) < 10⁻⁴²`, ≥ 29.45 OOM below LISA-PLS (re-verified Sage-exact above; every steeper `p` is deeper, including any van-Hove-DOS enhancement that steepens `p` above 3). There is no causal `p` the fold DOS could return that revives the LISA flagship. So the §7.2 GW-detector-flagship retirement is an UNCONDITIONAL status change that I land at this turn; S97 refines the IR-tail re-pin VALUE (closing the 127-OOM number-vs-prose drift), it does NOT decide detectability (settled slope-robustly).

### DISSENT

**None of substance — the workshop's adjudication is complete and this turn is the mechanical write.** little-red-dots converged fully at Round 3 with zero residual; D2.1 and D2.2 he adopted to my Round-2 positions (which were themselves moves toward HIS stronger Round-1 positions — the detector-band-set-EXPLICIT sterility and the slope-independent bound), and D2.3-HELD he accepted once the guard tag resolved his placement concern. There is no remaining tension on the physics, the Case-A resolution, the unconditional flagship-death, the two-gate S97 split, or any number.

The only correction I owe the record is the one-decade `log10 Ω^(C)` prose slip noted in CONVERGENCE #1 above (−58.08 → −57.08; the 47.081 split is unaffected), which I fold into the landed text rather than leave for a future reader to trip on. That is a precision repair, not a dissent. Every figure I land reproduces Sage-exact and matches the verdict file (lines 136, 149, 155) and the canonical store.

### EMERGENCE

**E3-mack.1 — The §7.2 GW-detector flagship is retired UNCONDITIONALLY to a GW-detector-sterile / LSS-falsifier form. This is a STRUCTURAL change of epistemic type (`output-standards.md §"What Changed"` column (b)), not a numerical revision — and I land it at this turn as §7 sole writer.** The §7.2 acoustic-CGWB entry changes epistemic TYPE: from a "LISA-detectable, 11+ OOM above LISA-PLS, SNR ~10¹³" GW-DETECTOR falsifier (the historical "headline test") to a GW-detector-STERILE substrate observable whose testable imprint lives in large-scale structure. It is not a band-narrowing or an OOM-sharpening; it is a relocation of the falsifier to the correct instrument. The substrate-first frame is preserved exactly: the substrate IS the acoustic emission; the register tag (GW-detector-sterile / PENDING-RECOMPUTE) scopes the detector reach; the arrow `D_K → van Hove fold DOS → acoustic Ω_GW(f) → measurement` is unchanged. The substrate did not get weaker — the instrument was wrong from the start (the substrate radiates at its one frequency scale `M_KK`, ~10⁴⁰ Hz, above EVERY realized/proposed GW detector by ≥ 28.93 decades).

**E3-mack.2 — The constructive half: the acoustic falsifier MIGRATES to LSS. The live zero-parameter near-term falsifiers are the first-sound BAO ring (W6-2, SNR 8.6341 DESI-5yr) + f·σ₈ (W6-1) — galaxy-survey observables, not GW-detector observables.** A source's intrinsic emission scale decides the instrument. The substrate has ONE frequency scale (`M_KK`); the fold radiates at it (~10⁴⁰ Hz, above every GW detector); the acoustic IMPRINT lives at the matter-clustering scale (`k₁ = 0.0193 Mpc⁻¹`, `r₁ = 325.30 Mpc`) where DESI/Euclid operate. The first-sound BAO ring (`A_FS = 0.204`, `audit_sha256=b74ccd56…`, no ΛCDM counterpart — the second-sound mode has no analog) and f·σ₈ growth suppression (−4.06%, S₈-tension-relieving) inherit the live-falsifier rows the GW flagship vacates. This is the detector-band discipline made quantitative: "Ω_GW peak in the LISA band" asserted the headline GW instrument without deriving the emission frequency; W6-3's redshift chain refuted it by 42.45 decades, and the falsifier relocates where the substrate actually radiates.

**E3-mack.3 — S97 is reframed: pin the SHAPE to close the 127-OOM number-vs-prose drift, NOT decide detectability (settled). The two-gate `PEAK-HEIGHT → SPECTRAL-SHAPE` decomposition is the durable methodological output.** W8-2 corrected the §7.2 PROSE ("LISA samples the IR tail") but left the NUMBER (`Ω_GW^(A) = 1e-10`) standing on Row #7.audit-2 as if it were the IR-tail value — so the canonical store currently says the IR tail is 1e-10 while the prose says it is a tail, a 127-OOM number-vs-prose disagreement (exactly the capstone-hygiene Q3/Q5 drift the standing gate catches). S97 closes it by deriving `Ω_peak` from the fold DOS at the peak frequency (`S97-OMEGAGW-PEAK-HEIGHT`, my amplitude/inventory leg — `Ω_peak` CANNOT come from the placeholder pivot, the back-out is 10^117) feeding the IR slope `p` derivation (`S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE`, little-red-dots's detector-band leg), producing the honest IR-tail re-pin value. The reframing — "produce the honest re-pin value," not "test survival" — is what I carry into the Wrap-Up so next session does not re-litigate a settled detector verdict.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | −127.4 OOM contradiction | L1, Re:L1 | **Converged** | The contradiction is real (127 OOM, re-verified Sage-exact both sides), not a rounding artifact. The provenance-less `Ω_GW^(A) = 1e-10` is the casualty; W6-3's redshift-chain peak (`8.4835e39 Hz`, audit `646e6ad0…`) is the *measurement*, `1e-10` is *commentary* (no PROVENANCE entry). Read backward the same triple gives `Ω_peak ~ 10^117` (unphysical), proving `(pivot 1e-10, p=3, peak 8.4835e39 Hz)` mutually inconsistent. |
| 2 | peak vs flat-plateau compatibility | L2, Re:L2 | **Converged** | "Flat plateau in LISA band" (W6-4 disc. table L242) is the internally-wrong cell — it silently re-asserts the refuted "peak near pivot." One fold ⇒ one peak ⇒ peak at `8.4835e39 Hz` ⇒ LISA sits 42.45 decades into the causal `f³` IR tail (rising), no plateau in-band. The W6-4 gate splits cleanly: wall=0 topology leg (`Ω_GW^{walls}=0` EXACTLY via π₀(U(1))=0; PASS stands, untouched) ⊥ the provenance-less `1e-10` amplitude leg (re-opened). |
| 3 | Omega_GW_Lambda_A_LISA pin disposition | L3, Re:L3 | **Converged (on PENDING-SUBSTRATE-RECOMPUTE)** | Case A: `1e-10` was a pivot-band value under an assumed peak-at-3-mHz, refuted by W6-3 (42.45 decades). Fires three classes — Class-(f) PIN-PLACEHOLDER, Class-(c) PIN-DRIFT-FROM-STALE-SOURCE (W6-3 the supersession event), and the 127-OOM internal-consistency violation. Disposition: RE-PIN not RETIRE (the IR-tail amplitude is a real observable), flagged `PENDING-SUBSTRATE-RECOMPUTE` in BOTH inventory + `canonical_constants.py` PROVENANCE; value pending the S97 fold-DOS slope+height compute (`Ω_peak` not back-derivable from the placeholder). |
| 4 | a(t)-independent LISA GW falsifier survival | L4, Re:L4 | **Emerged (GW→LSS migration)** | NO a(t)-independent GW-DETECTOR falsifier survives D4: peak 44 decades out (W6-3, normalization-robust), amplitude tail `< 10⁻⁴²` slope-robustly (29.45 OOM below LISA-PLS at the shallowest causal `p=1`, UNCONDITIONAL), walls identically zero. The falsifier MIGRATES to LSS: first-sound BAO ring (W6-2, PASS, SNR 8.6341 DESI-5yr, audit `b74ccd56…`) + f·σ₈ (W6-1, INFO) are the live zero-parameter acoustic falsifiers — galaxy surveys, not GW detectors. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

**Verdict summary.** Four topics: three **Converged** (Topics 1–3; Topic 3 converged on the `PENDING-SUBSTRATE-RECOMPUTE` disposition), one **Emerged** (Topic 4 — the GW→LSS falsifier migration is the durable structural change, not a numerical revision). Zero Dissent of substance at close. The §7.2 GW-detector flagship is retired UNCONDITIONALLY (slope-robust LISA-sterility); the substrate physics is intact and testable in the correct instrument (DESI/Euclid). No overall verdict / probability assessment is offered — this maps the constraint structure (the LISA-CGWB corridor is closed as a detector channel; the LSS acoustic corridor is the live next-test) and pre-registers the next observable test (the two-gate S97 re-pin).

## Remaining Open Questions

All are S97-actionable; none reopen any closed leg of this workshop (the arithmetic, the Case-A resolution, the unconditional flagship-death, the GW→LSS migration are settled). These are the genuine future computes, not hygiene.

1. **`Ω_peak` from the fold DOS at `f_peak = 8.4835e39 Hz` (gate `S97-OMEGAGW-PEAK-HEIGHT`, mack-owned).** The spectral peak height is the missing pin and CANNOT be back-derived from the placeholder pivot (`1e-10` → `Ω_peak ~ 10^117`, unphysical). Derive it from the S86/S87 squeezed-graviton machinery at the van Hove fold (where `v_g → 0`, DOS diverges), with the `Ω_peak ≤ O(1)` GW-energy bound as a sanity ceiling. UPSTREAM to OQ-2.

2. **The IR slope `p` from the fold DOS (gate `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE`, little-red-dots-owned).** Is the acoustic van-Hove-fold causal exponent exactly `p=3` (Hiramatsu causal default) or steepened by the DOS divergence at the fold? Open question: does a band-edge / van-Hove-singularity emission modify the IR causal exponent away from 3 (it can only STEEPEN it, or hold at the `p=1` analyticity floor — it cannot shallow below 1). The LISA-sterility verdict does NOT wait on this (`< 10⁻⁴²` for all `p ≥ 1`); `p` is needed only for the honest IR-tail re-pin VALUE. FI/RD-tag per `regulator-pin-discipline.md` if it enters via a Seeley-DeWitt moment (`a_n^{ζ}`).

3. **The κ-robustness of the IR-tail VALUE across [1e-20, 1e-10] (closeout of OQ-2).** The peak FREQUENCY is GHz+ across the entire swept `M_KK⁻¹→s` band (W6-3, 121/121 pts); but the IR-tail VALUE at the LISA pivot depends on both `f_peak(κ)` AND `Ω_peak(κ)`. S97 should report `Ω_GW(3 mHz)` as a function of κ (mirroring W6-3's `regime=VALID` band-robustness demonstration), so the re-pin carries a "LISA-sterile across the entire physically-swept normalization" statement, not a single-κ value.

4. **The deeper open gap this workshop did NOT close: the open `M_KK⁻¹→s` normalization knob itself.** The same knob that blocks the derived `a(t)` (capstone §6.3, the effective-Friedmann gap) sets the peak-frequency MAGNITUDE. The peak-frequency placement far above LISA is robust to this knob (GHz+ across the band), but pinning `κ` from substrate physics (rather than sweeping it) is the upstream resolution that would convert "GHz+ across the swept band" into a single substrate-derived peak frequency. NOT an S97 deliverable — flagged as the standing structural gap the GW channel shares with §6.3.

## Wrap-Up — Workshop Impact Summary

### What Changed

Per `output-standards.md §"What Changed"`, the numerical revisions and the structural change are kept in separate sub-blocks — the structural change is the durable workshop output.

#### (a) Numerical revisions

- Historical `Ω_GW(LISA) ~ 1e-10` (the §7.2 flagship amplitude) → the f³-tail value `~10⁻¹³⁷·³⁵` at 3 mHz IF `Ω_peak = 1e-10` (Sage-exact `−137.35436143`) — exposing the 127-OOM internal inconsistency, NOT a new canonical value (the placeholder is retired, not relabeled).
- §7.2 LISA-band amplitude → **slope-independent upper bound `< 10⁻⁴²`** (Sage-exact ceiling `10^(−42.451454)` at the shallowest causal `p=1` with `Ω_peak ≤ O(1)`; ≥ 29.45 OOM below LISA-PLS for all `p ≥ 1`), replacing the bare `1e-10`. Exact value PENDING the S97 fold-DOS slope+height compute.
- The (C)-floor decade pinned correct: `log10 Ω^(C) = log10(8.299e-58) = −57.080974235` (one-decade prose slip `−58.08 → −57.08` corrected from R3-little-red-dots; the **47.081 (A)/(C) split is unaffected**, `= 47.080974235` Sage-exact).
- Peak placement quantified against the explicit instrument set: `28.928575` decades above the HF ceiling (10¹¹ Hz), `43.928575` decades above the LISA low edge (10⁻⁴ Hz), Sage-exact.

#### (b) Structural changes

- **§7.2 acoustic-CGWB row: GW-DETECTOR falsifier → GW-detector-STERILE substrate observable (LSS-falsifier-migrated).** A change of EPISTEMIC TYPE — the "headline LISA test, SNR ~10¹³" becomes a substrate observable whose testable imprint relocates to large-scale structure. UNCONDITIONAL (E2.2: slope-robust `< 10⁻⁴²`), not pending-S97.
- **The acoustic falsifier MIGRATES instruments: GW → LSS.** First-sound BAO ring (W6-2, SNR 8.6341) + f·σ₈ (W6-1) promoted to the live zero-parameter near-term falsifier rows the GW flagship vacates — DESI/Euclid, not LISA/PTA/HF.
- **`Omega_GW_Lambda_A_LISA` disposition: live-flagship-pin → `PENDING-SUBSTRATE-RECOMPUTE`** (parked-with-reason in both registry and constant-store, not deleted, not left at 1e-10). Fires Class-(f) PIN-PLACEHOLDER + Class-(c) PIN-DRIFT-FROM-STALE-SOURCE simultaneously.
- **S97 reframed: "test whether the flagship survives" → "produce the honest IR-tail re-pin VALUE."** Detectability is settled slope-robustly; S97 closes the 127-OOM number-vs-prose drift, not the detector verdict. Two-gate decomposition `S97-OMEGAGW-PEAK-HEIGHT → S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE` emerges as the correct structure (`Ω_peak` and `p` are different observables on different sides of the inventory).
- **`Omega_peak_source: ADJUDICATED_IN_W3` RETRACTED** (little-red-dots's L4 single-gate pin) → `Omega_peak_source: S97-OMEGAGW-PEAK-HEIGHT (upstream gate, mack)`; `Ω_peak` is not adjudicable from existing artifacts (back-out is unphysical).

### What Holds

- **The peak FREQUENCY `f_peak ≈ 8.4835×10³⁹ Hz` (W6-3, audit `646e6ad0…`, line 155).** Redshift-chain-derived from `f_emit = M_KK/(2π)` × `a_fold/a_now = 0.4723` (a pure Connes-distance ratio, κ-independent); GHz+ across all 121 swept κ points. The *measurement* leg of the evidence hierarchy.
- **The wall=0 topology leg: `Ω_GW^{walls} = 0` EXACTLY via π₀(U(1))=0** (W6-4, audit `a9998118…`, line 136). Regulator-invariant, topological, untouched by the amplitude re-opening. PASS stands. Retained on §7.2 with the `[STRUCTURAL topological result — NOT a detector signal]` guard.
- **The (A)/(C) regulator-class split: `OOM_split_AC_regulator_class = 47.081`** (S86, W6-4 audit `a9998118…`, superseded=False; Sage-exact `47.080974235`). A regulator-class SEPARATION statement, never a detectability guarantee — it is "a split between two LISA-STERILE numbers" (M1 substitution chain). Retained on §7.2 with the `[STRUCTURAL regulator-class SEPARATION — NOT detector-testable]` guard.
- **`Ω_GW^(C) = 8.299×10⁻⁵⁸`** (Companion-null, S86, fully provenanced) and the W6-4 fidelity correction `round_fig_1e-57_understate = 1.205× = 0.081 OOM` (same-decade, Class-8.3 publication-precision hygiene, NOT an OOM blunder) — DISTINCT from the `1e-10` (A)-class 127-OOM defect; both survive and must stay un-conflated.
- **The live LSS acoustic falsifiers, with verdict-file numbers intact**: first-sound BAO ring `A_FS = 0.204000`, `k₁ = 0.0193150 Mpc⁻¹`, `r₁ = 325.30 Mpc`, SNR 8.6341 DESI-5yr / 5.0789 DESI-DR1 (W6-2, PASS, audit `b74ccd56…`, line 149); f·σ₈ `product_supp_max = −4.058% @ z=0.51`, S₈-relieving (W6-1, INFO, line 143).
- **The substrate-first frame.** The substrate IS the acoustic emission; the register tag scopes the detector reach; the arrow `D_K → van Hove fold DOS → acoustic Ω_GW(f) → measurement` is unchanged. The substrate did not get weaker — the instrument was wrong.

### What Breaks or Strains

- **Capstone §7.2 narrative was 127 OOM above its register-supported value** (the number-vs-prose drift W8-2 left open: prose said "LISA samples the IR tail," the NUMBER `Ω_GW^(A) = 1e-10` stood as if it were that tail). This workshop closes it — the exact capstone-hygiene Q3/Q5 drift the standing gate catches. **Fixed in-session** via the §7.2 sole-writer patch + the Row #7.audit-3 supersedes sub-row.
- **The historical "headline test: LISA's CGWB discriminator, decisive at SNR ~10¹³" framing is FALSIFIED as a detector claim.** The §7.2 falsifier-anchor table (Row #7) and the W8-2 scope-note (capstone §7.2) both carried the flagship; I land the retirement on both. **Cross-section strain flag (NOT in my §7.2 sole-writer scope):** the capstone §7.3-region "Headline test: LISA's CGWB discriminator … decisive at SNR ~10¹³ … LISA is the headline; DESI DR3 is the cliff-edge" callout (capstone line 559, positioned in the §7.3 block) still narrates the GW-detector flagship at full confidence. It is OUTSIDE my §7.2-only edit scope this turn. Routed as a capstone-hygiene carry-forward to the §7.3-region designated writer (NOT actioned here — see Effected-In-Session §(iv)). The §7.2 retirement makes that callout's "SNR ~10¹³ LISA detection" obsolete; it must be reconciled to "LISA is GW-detector-sterile; DESI DR3 + the LSS acoustic ring are the live near-term tests."
- **The open `M_KK⁻¹→s` normalization knob is the standing structural gap** (shared with §6.3): the peak-frequency placement far above LISA is robust to it, but the peak frequency MAGNITUDE is not yet substrate-pinned. Not closed by this workshop; flagged (Open Question 4).
- **The three aliased pins** `Omega_GW_FW_S82_equilateral`, `Omega_GW_FW_S67_folded`, `Omega_GW_FW_S85_W9_3_analytic_template` (canonical_constants.py lines 2510–2512, each `= 1.0e-10`, aliased to `Omega_GW_Lambda_A_LISA`) inherit the same placeholder defect. They are annotated as inheriting the PENDING-SUBSTRATE-RECOMPUTE disposition in-session (the value is NOT changed — the S97 compute produces the replacement); their downstream consumers must read the PENDING flag.

### Carry-Forward Computations (MATH ONLY — propagate to S97)

Two gates, in a feeds-into structure: `S97-OMEGAGW-PEAK-HEIGHT` (mack-owned) produces `Ω_peak`, which `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE` (little-red-dots-owned) consumes to compute the IR-tail re-pin value. **Reframed purpose (E2.2-settled): both gates produce the honest IR-tail re-pin VALUE and close the 127-OOM number-vs-prose drift — they do NOT test "whether the flagship survives." GW-detector-sterility is already established slope-robustly (`Ω(LISA) < 10⁻⁴²` for all `p ≥ 1`).** Next session does not re-litigate the settled detector verdict.

#### CF-S97-OMEGAGW-PEAK-HEIGHT (mack-cosmic-bridge; the amplitude/inventory leg; UPSTREAM)

1. **What**: Derive the spectral peak height `Ω_peak` of the acoustic Ω_GW(f) spectrum at the van Hove fold peak frequency `f_peak = 8.4835e39 Hz`, from the fold DOS via the S86/S87 squeezed-graviton (squeezed-vacuum graviton production at the fold where `v_g → 0`, DOS diverges) machinery. `Ω_peak` CANNOT come from the placeholder pivot (`1e-10` → back-out `10^117`, unphysical) — it needs its own substrate derivation at the peak frequency.
2. **Inputs**: S86/S87 squeezed-graviton amplitude machinery; fold DOS (`s54_scale_factor.npz` + van Hove fold modes `omega_L1, omega_PV, omega_tau, v_g_B2_fold`); `canonical_constants.py` (`M_KK`, `M_KK_inv_seconds`, `a_fold/a0 = 2.1173`); L_max=10 D_K cache (78,080 unique eigenvalues). κ-sweep [1e-20, 1e-10] (121 pts) for the κ-robustness of `Ω_peak(κ)`.
3. **Gate** (`[SIGN]` + threshold): PASS = `Ω_peak` derived from the fold DOS (NOT assumed), with `Ω_peak ≤ O(1)` (the GW-energy bound sanity ceiling) — i.e. `log10 Ω_peak ≤ 0`; report `Ω_peak(κ)` over the swept band. INFO = `Ω_peak` derivable but normalization-conditional on the open `M_KK⁻¹→s` knob (mirrors W6-3/W6-5 C1 gap); report as a function of κ. FAIL = `Ω_peak > O(1)` at κ_nat (would violate the GW-energy bound and signal a machinery error, not a physical peak). On PASS/INFO: `update_constant('Omega_GW_acoustic_peak', Ω_peak, at f_peak=8.4835e39 Hz)` per the canonical write-order Step 2.
4. **Effort**: moderate — reuses the S86/S87 squeezed-graviton machinery + the L_max=10 cache + the s54 scale-factor data; no new large-matrix compute. GPU not required.

#### CF-S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE (little-red-dots-jwst-analyst; the IR-slope/detector-band leg; DOWNSTREAM of PEAK-HEIGHT)

1. **What**: Derive the causal IR slope `p` (`Ω_GW ∝ f^p` for `f ≪ f_peak`) of the acoustic Ω_GW(f) spectrum from the fold DOS (NOT the assumed Hiramatsu `p=3` default); propagate `Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p`; confirm `< LISA-PLS`; produce the IR-tail re-pin VALUE at the LISA pivot. Open substrate-physics: does the van-Hove-singularity emission (DOS divergence at the fold) steepen `p` above the causal floor `p=3`, or hold at it? (It can only steepen, or hold — it cannot shallow below the `p=1` analyticity floor.)
2. **Inputs**: `Ω_peak` from CF-S97-OMEGAGW-PEAK-HEIGHT (UPSTREAM, mack); fold DOS (same source); `f_peak = 8.4835e39 Hz` (canonical, S96-OBS-CGWB-PEAK-FREQ); `f_LISA = 0.003 Hz`; `a_fold/a_now = 0.472291` (κ-independent pure ratio); κ-sweep [1e-20, 1e-10] (121 pts, mirroring W6-3). `Omega_peak_source: S97-OMEGAGW-PEAK-HEIGHT (upstream gate, mack)` — REPLACES the retracted `ADJUDICATED_IN_W3` pin.
3. **Gate** (`[SIGN]` + threshold): PASS = IR slope `p` derived from the fold DOS (NOT assumed); `Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p` computed; `|Ω_GW(3 mHz)| < 1e-13` (LISA-sterile) AND consistent within the publication-precision floor with the slope-independent ceiling `< 10⁻⁴²` (the bound `p=1` gives; a derived `p ≥ 1` is deeper); robust across the swept κ band ⇒ LISA-band amplitude RE-PINNED, `update_constant('Omega_GW_acoustic_LISA_tail', value, at 3 mHz)`. INFO = `p` derivable but `Ω_GW(3 mHz)` normalization-conditional; report as a function of κ and confirm LISA-sterility robust across [1e-20, 1e-10] (mirrors W6-3 `regime=VALID`). FAIL = `p < 0` in the LISA band (spectrum FALLING from a higher-frequency plateau into LISA — would require a SECOND emission feature below `f_peak`; the one way the flagship could revive, judged unlikely: the substrate has one fold, one peak — but pre-registered to test rather than assume). FI/RD-tag `p` per `regulator-pin-discipline.md` (`a_n^{ζ}`) if it enters via a Seeley-DeWitt moment.
4. **Effort**: moderate — DOS-slope extraction + the f^p propagation across the κ band; depends on the PEAK-HEIGHT constant landing first (in-session UPSTREAM prereq). GPU not required.

#### Post-compute re-pin (mack, sole inventory writer, after BOTH gates land)

After CF-S97-OMEGAGW-PEAK-HEIGHT + CF-S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE land, mack re-pins (per the canonical write-order Step 3): replace the `PENDING-SUBSTRATE-RECOMPUTE` flag on `Omega_GW_Lambda_A_LISA` with the derived IR-tail value (or relabel to `Omega_GW_acoustic_LISA_tail` + add `Omega_GW_acoustic_peak`); update the §7.2 cell from the provisional `< 10⁻⁴²` bound to the derived value; flip the three aliased pins to consume the recomputed value. This is the closure of the number-vs-prose drift — NOT a re-test of detectability.

### Effected In-Session (NON-MATH — completed by mack, the final agent, BEFORE TERMINATING; mack is sole writer of the §7 falsifier surface + falsifier-master-inventory.md)

All landings are sole-writer surgical patches (NOT bulk dumps). §7.3 (W-5's, capstone line ~557), §6.3 (W-1 staged), §5.3/§7.1 (W-4 staged) were NOT touched. No `.py` script was run; the canonical_constants.py edit is a PROVENANCE annotation only (value held, import verified intact).

- [x] **(i) §7.2 prose — GW-detector-flagship retired to LISA-sterile / LSS-falsifier form.** `sessions/framework/phonic-exflation-equation.md`:
    - **line 542** — the §7.2 falsifier-anchor lead note rewritten from the W8-2 "LISA flagship is the IR-tail amplitude `~1e-10` (live)" framing to the W-3 **GW-detector-flagship retirement**: peak `8.4835×10³⁹ Hz` ≥ GHz across the swept band, ≥ 28.93 decades above the explicit three-instrument set (LISA mHz + PTA nHz + HF ≲10¹¹ Hz); LISA-band amplitude `< 10⁻⁴²` slope-independent; acoustic CGWB NOT a GW-detector falsifier; live LSS falsifiers = first-sound BAO ring (SNR 8.6341, `b74ccd56…`) + f·σ₈; the two surviving structural companions (wall=0 + (A)/(C) split `47.081`) carried with `[STRUCTURAL — NOT detector-testable]` guards. Provenance: W-3 workshop + W6-3 audit `646e6ad0…`.
    - **line 550** — §7.2 falsifier-table Row #7 rewritten from "**FLAGSHIP**: acoustic class 11 OOM above LISA-PLS … SNR ~10¹³ … LISA ~2034" to "**RETIRED as a GW-detector falsifier** … MIGRATES to LSS"; surviving structural companions tagged non-detector-testable.
    - **line 551** — NEW Row #8 (first-sound BAO ring `A_FS = 0.204`, SNR 8.6341 DESI-5yr, `S96-OBS-FIRST-SOUND-RING` PASS) added as the GW flagship's replacement in the correct instrument.
- [x] **(ii) `Omega_GW_Lambda_A_LISA` flagged `PENDING-SUBSTRATE-RECOMPUTE` in BOTH layers (value NOT changed, import intact).**
    - `sessions/framework/registry/falsifier-master-inventory.md` **line 1574** — NEW **Row #7.audit-3** supersedes sub-row: supersedes the Row #7.audit-2 (a) "UNCHANGED, LIVE `1e-10`" disposition (line 1567); cites the W6-3 supersession audit `646e6ad087dae6441515a62456300af48c7c135be103147767fbcbcbfbf2ee2e` (full 64-hex) + the W6-4 amplitude-leg audit `a9998118…`; §7.2 cell carries `< 10⁻⁴²`; disposition `GW-DETECTOR-STERILE → LSS-falsifier-migrated`.
    - `computations/_shared/canonical_constants.py` **lines ~2490–2495** (PROVENANCE comment block) + **line 2504** (inline) + **lines 2510–2512** (the three aliased pins) — annotated `PENDING-SUBSTRATE-RECOMPUTE` with the Case-A / Class-(f) / Class-(c) reason and the S97 two-gate re-pin pointer. **Value held at `1.0e-10`** (no derived `Ω_peak` exists yet; the S97 compute produces the replacement). Import verified clean (`Omega_GW_Lambda_A_LISA = 1e-10`, aliases `1e-10`, IMPORT OK).
- [x] **(iii) Live acoustic falsifiers promoted (LSS, not GW).** `sessions/framework/registry/falsifier-master-inventory.md` Row #7.audit-3 (**line 1574**) cross-links and promotes the surviving acoustic falsifiers that inherit the GW flagship's vacated surface: **first-sound BAO ring** (Row #72, `S96-OBS-FIRST-SOUND-RING`, PASS, SNR 8.6341 DESI-5yr, audit `b74ccd56…`, verdict line 149 — the live near-term zero-parameter falsifier) + **f·σ₈** (Row #71, `S96-OBS-FSIGMA8-FORECAST`, INFO, −4.06% S₈-relieving, verdict line 143). Both already-landed (W6-2/W6-1 via W8-2 consolidation); Row #7.audit-3 establishes them as the GW→LSS migration targets, and capstone §7.2 Row #8 (**line 551**) surfaces the BAO ring on the live falsifier table. (Open item, NOT actioned — outside §7.2 scope: the capstone §7.3-region "Headline test: LISA's CGWB … SNR ~10¹³" callout at line ~559 still narrates the GW flagship; routed as a capstone-hygiene CF to the §7.3 designated writer, recorded in "What Breaks or Strains" + Row #7.audit-3 cross-references.)

### Closing Line

### Closing Line

The acoustic CGWB was never a LISA signal — the substrate radiates at its one frequency scale, ~10⁴⁰ Hz, twenty-eight decades above every GW detector ever proposed, and the `1e-10`-at-the-mHz-pivot "flagship" was a provenance-less placeholder that assumed the answer it was meant to measure. The honest move is not to mourn a dead detector channel but to follow the substrate to where it actually speaks: the first-sound BAO ring at `r₁ = 325 Mpc`, SNR 8.6 in DESI by 2029, with no ΛCDM counterpart to hide behind. The fold still rings; we were holding the wrong instrument to listen.
