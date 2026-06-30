# Capstone Equation Review — cosmic-web

**Date**: 2026-05-29
**Agent**: cosmic-web-theorist (large-scale structure, cosmic-web topology, void statistics, BAO, superfluid-cosmology analogs)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (S95-era capstone — "The Phonon-Exflation Equation")
- `.claude/rules/phononic-framing.md` (binding framing law)
- `sessions/archive/session-94/session-94-s1-bao-observational-reach-synthesis.md` (BAO peak-position reach, S94 S-1)
- `sessions/archive/session-95/session-95-w6-workingpaper.md §W6-2` (BAO two-speed amplitude transport, S95 W6-2)
- knowledge MCP cross-checks: `sigma_8`, `w0_FW`, `wa_FW`, S43 first-sound ring, S77 f·σ₈

---

## I. Session Outcome

From the large-scale-structure vantage, the capstone is **honest and well-scoped where it touches my domain, with one significant documentation gap and one over-precise phrase**. The equation's claim that the observed cosmic web is "the interference pattern of post-transit GGE acoustic excitations propagating through the `a₂` channel" is the correct substrate-first reading of LSS and is internally consistent with the framing law. The §7.1 outputs table reports `σ₈ = 0.799` (VIABLE, zero-free-parameter) — confirmed canonical. The single biggest LSS finding I have to report is **a gap, not an error**: the document surfaces the *static* clustering amplitude `σ₈` but **omits the framework's PROVEN growth-rate prediction `f·σ₈(z): 4% suppression vs ΛCDM with the correct S₈-tension sign` (S77 mack-synthesis, PROVEN; `σ₈(FW)=0.7932`, `f_FW=0.525492` vs `f_LCDM=0.527130`)**. A static `σ₈` is degenerate across many models; the *growth-rate* suppression is the genuinely discriminating RSD observable DESI 5yr / Euclid will measure (~2028). That prediction belongs in the §7.1 table and the §7.2 falsifier inventory and is currently invisible there.

The genuinely-distinctive LSS falsifier — the **S43 first-sound ring at `r₁ = 325.3 Mpc` (`k₁ = 0.0193 Mpc⁻¹`), `A_FS = 0.204`, no ΛCDM counterpart** — is correctly carried in §6.2, and its open piece (the experiment-sensitivity comparison) is correctly carried forward as INFO-by-unavailability (S95 W6-2). That is a clean, ripe harvest item. Verdict: the LSS content is solid as far as it goes; §V converts every identifiable open question into a runnable computation.

---

## II. Key Results

### The cosmic web as a GGE interference pattern — substrate framing is correct

**Result**: "Structure = interference pattern of post-transit GGE acoustic excitations, gravitationally self-organized through the `a₂` channel" (§0, §7.1 substrate readings). Classification: **PHONONIC**.

This is the correct direction of explanation under `phononic-framing.md`. The cosmic web is not "density perturbations *in* expanding space"; it is the spatial readout of the post-fold GGE relic's acoustic modes, organized by the emergent Einstein–Hilbert (`a₂`) channel. The document holds the IS-not-IN arrow throughout the LSS discussion (`D_K eigenmodes → a₂ moment → emergent metric → observed clustering`), and the §6.3 framing-discipline box explicitly refuses the container relapse ("the vacuum energy dilutes *as* the substrate reorganizes — `H(t)` is the readout, not a clock the vacuum decays in"). From a cosmic-web standpoint this is the right posture: void statistics, the two-point function, and Minkowski functionals are all volume-averaged read-outs of where the `a₂`-channel spectral weight sits, not properties of a pre-existing box. **No correction needed; this is a model statement done right.**

One caveat I must flag as a standing limitation, not an error: per my own closed-test ledger, the *volume-averaged* LSS statistics (`P(k)`, `ξ(r)`, void-size function, Minkowski functionals, genus, persistent Betti numbers) were **CLOSED at S43** — the substrate's preferred-mode transition sits at `k_transition ≈ 9.4×10²³ h/Mpc`, ~24 orders of magnitude above any survey scale, so the cosmic web's *topology* (Betti numbers, genus) carries no discriminating substrate signature at observable `k`. The document does not claim otherwise — it correctly routes its LSS discriminating power to the *acoustic* channel (the first-sound ring) and the *growth-rate* channel, not to web topology. This is the right call and is consistent with the framing law's "the cosmic web is a topological object, but its topology is fixed by the initial spectrum" reading. I record it so a future reader does not mistake the §7.1 LSS row count for a topological-discriminant claim.

### The S43 first-sound ring is the live, distinctive LSS falsifier — correctly carried

**Result**: First-sound ring at `r₁ = 325.3 Mpc` (`k₁ = 0.0193 Mpc⁻¹`), amplitude `A_FS/A_BAO = 0.204 = c₂²/c₁²` (Sage-exact `100/489 = 0.2045`); `δP/P` at the ring `= 0.2032`. Classification: **PHONONIC** (Layer-2 acoustic interference).

This is the framework's one zero-parameter LSS prediction with **no ΛCDM counterpart** — ΛCDM has a single acoustic feature at `r_s ≈ 147 Mpc`; the substrate predicts an *additional* first-sound feature at `r₁ ≈ 325 Mpc` arising from the second (condensate) sound speed `c₂`. The document's §6.2 framing is correct and matches both the S94 S-1 reach synthesis and the S95 W6-2 amplitude transport:

- The per-gapped-branch Layer-1/Layer-2 *peak-position* shift is **0.14% (B1-dominant) / 0.44% (B3)** after the effacement projection `(c_b²/c_Gold)²` (Reading-NS, substrate-first) — **below DESI DR2's 0.24% ruler precision**, so it is NOT a present falsifier. The naive 19% internal split is a container-thinking conflation (identifying the M_KK-internal branch speed with the emergent 4D acoustic speed) and is correctly rejected.
- The *ring amplitude* `δP/P = 0.2032` sits **141× above** the per-branch sub-feature and **1.6×10⁴ above** the deep effacement floor `(1−Γ_eff)² = 9×10⁻⁸`. This is the live channel.

The document's §6.2 sentence — "the live BAO channel is the S43 first-sound ring … whose amplitude-detection forecast against a named experiment's sensitivity awaits the fetched value (S95 W6-2, INFO-by-unavailability)" — is **exactly right and exactly honest**. The substrate forecast is computed in full; only the experiment-sensitivity fetch (CMB-S4 / Simons Observatory `θ_s` + P(k) amplitude sensitivity) was unavailable (paper-search MCP down at S95 dispatch). This is the single cleanest "ripe harvest" in my domain (§V.1).

### BAO effacement-suppression: direction is correct, one phrase is over-precise

**Result**: §6.2 — "transported through `(c_b²/c_Gold)²` (every Layer-2 branch speed `v_g ≤ c_Gold`), the per-branch sub-feature is `δP/P ≈ 1.4×10⁻³` — far below current acoustic-scale rulers (effacement is a suppression, not an amplification)." Classification: **PHONONIC**.

The **suppression direction is correct and verified** (S95 W6-2, sign_verdict=PASS): since every Layer-2 branch speed `v_g ≤ c_Gold`, the projection weight `(c_b²/c_Gold)² < 1`, so the transported amplitude is *smaller* than the naive split. The substitution chain (S95 W6-2 §"Substitution chain", steps 1–5) is sound and matches the S43 `A_FS` form. The `1.4×10⁻³` figure is the B1-dominant per-branch sub-feature amplitude (`A_obs,B1 = 0.19·17689/2325625 = 1.445×10⁻³`, Sage-exact).

**Flag (minor, over-precision)**: the §6.2 phrase "far below current acoustic-scale rulers" is true for the *per-branch sub-feature* but the same paragraph then says "the live BAO channel is the S43 first-sound ring." A reader could conflate the two amplitudes. The per-branch sub-feature (`1.4×10⁻³`) is below DESI; the *ring* (`A_FS = 0.204`) is the live channel and is WITHIN all precision anchors' *acoustic-scale* reach — but its *imprint amplitude on the matter P(k)/C_ℓ* is gated by the **UNTESTED fabric↔photon-baryon coupling** (S94 §5; S43 flagged it as possibly ~10⁻⁶ undetectable, or up to `0.204·A_BAO` if equipartition holds). The document does not state this coupling-gating explicitly in §6.2 — it is the deeper open physics underneath the "awaits the fetched value" phrasing. This is a harvest item (§V.2): the ring's *position* is a zero-parameter prediction; its *detectability* hinges on a coupling the framework has not yet computed.

### σ₈ = 0.799 is reported; the growth-rate f·σ₈ prediction is MISSING — the main gap

**Result**: §7.1 reports `σ₈ = 0.799` (VIABLE, zero-free-parameter, ~2σ between Planck 0.811 and lensing ~0.76). Classification: **PHONONIC** (`a₂` growth channel).

The `σ₈ = 0.799` value is confirmed canonical (`atlas-07-permanent-results`, `proven_1323`/`1393`/`1442`/`1454`/`1512`; SIGMA8-OZ-50). The document's framing — "VIABLE (~2σ between), not a resolution" — is honest and matches my memory.

**Gap (significant)**: the document surfaces the *static amplitude* `σ₈` but **omits the framework's PROVEN growth-rate prediction**: `f·σ₈(z): 4% suppression vs ΛCDM, correct S₈ direction` (S77 mack-synthesis, status **PROVEN**; S65/S69 logs: `σ₈(FW) = 0.7932`, `f_FW = 0.525492` vs `f_LCDM = 0.527130`). From an LSS-discriminator standpoint this is the *more important* of the two:

- A static `σ₈` value near 0.799 is degenerate — many models (modified gravity, massive neutrinos, evolving DE) can land there. It is weak as a discriminator.
- The *growth-rate* `f·σ₈(z)` is what redshift-space distortions (RSD) actually measure, and a **~4% suppression with the correct S₈-tension sign** is a sharp, zero-parameter, falsifiable shape prediction. DESI 5yr (~2028) and Euclid will measure `f·σ₈(z)` across `0 < z < 1.5` to a few percent — this is a near-term live discriminator the document leaves off both its §7.1 table and its §7.2 falsifier inventory.

This is not a re-adjudication of a verdict (I am not overturning anything); it is a documentation completeness issue. The capstone's own §7.3 logic — "a prediction landing near data from zero free parameters … is Bayesian evidence" — applies with *more* force to `f·σ₈` than to `σ₈`, and the omission undersells the framework's LSS reach. Harvest item §V.3: surface `f·σ₈(z)` as a §7.1 row + §7.2 falsifier with the DESI/Euclid forecast.

### The "doubly-conditional" CC closure and the borrowed H(t) — honest, and it bounds my domain too

**Result**: §6.3 / §7.1 CC caveat box — the dark-energy rows (`w₀`, `wₐ`, CC closure, `σ₈`) are dagger-marked as evaluated "using the container-observer's FRW `H(t)` as external input (caveat C10)." Classification: **NON-PHONONIC** (the borrowed `H(t)` is not a substrate object).

The document is scrupulous that there is **no derived FRW scale factor `a(t)`** (C1 postulated; C2 BROKEN-WITH-LIVE-RESEARCH-PATHWAY; T6 BROKEN). For LSS this is load-bearing and the document is right to foreground it: **every `f·σ₈(z)`, `σ₈`, and growth-history prediction the framework makes is computed against a borrowed ΛCDM `H(z)`**, not a substrate-derived expansion history. So the "4% suppression vs ΛCDM" growth prediction is itself a *differential* statement relative to a ΛCDM background — it tells you the substrate's growth *modulation*, not an independent absolute growth history. This is the correct honest scope and I record it as a constraint on §V.3: the `f·σ₈` falsifier is "framework growth-modulation on a borrowed `H(z)`," not "framework expansion-plus-growth from `D_K`."

I cross-checked `w0_FW = −0.918` (S58 four-fold-lock, PROVENANCE entry present — confirmed) and `wa_FW = 0.0` (structural; no PROVENANCE entry, value confirmed). The document's `wₐ = 0` four-fold lock at 3.43σ from the DES/DESI joint posterior is correctly billed as "the live wager" / DESI DR3 cliff-edge. No conflict with my memory (which records the S70 bulk-flow correction and the DR3 sub-tree as the live `w₀, wₐ` test).

---

## III. Gate Verdicts

The capstone cites verdicts authoritative elsewhere; I do not re-adjudicate. Cross-checks I performed (all consistent):

| Cited claim | Source verdict | My cross-check | Consistent? |
|:-----|:--------|:-----|:--|
| `σ₈ = 0.799` VIABLE | SIGMA8-OZ-50 (PROVEN) | knowledge MCP `proven_1323` etc.; `σ₈(FW)=0.7932` (S65 log) | YES (0.799 ≈ 0.7932 rounding) |
| First-sound ring `r₁=325.3 Mpc`, `A_FS=0.204` | S43 (DISTINCTIVE, UNTESTED) | eq_9611 `A_FS/A_BAO=0.204=c₂²/c₁²`; `100/489` Sage-exact | YES |
| BAO per-branch shift 0.14%/0.44% below DESI | S94 S-1 (INFO) + S95 W6-2 (INFO) | read both syntheses; Reading-NS, `(c_b²/c_Gold)²` projection | YES |
| Effacement SUPPRESSES two-speed amplitude | S95 W6-2 (sign_verdict=PASS) | substitution chain steps 1–5; `(c_b²/c_Gold)²<1` | YES |
| `w0_FW=−0.918`, `wa_FW=0` | S58 four-fold-lock | `get_constant` both | YES |
| `f·σ₈: 4% suppression, correct S₈ sign` | S77 (PROVEN) — **NOT in capstone §7.1** | `f_FW=0.525492` vs `f_LCDM=0.527130` | value YES; **documentation gap** |

---

## IV. Structural Implications

**What the LSS vantage confirms.** The equation's account of structure formation is the correct substrate-first one: the cosmic web is the GGE relic's acoustic interference, organized by the `a₂` channel; the discriminating LSS signatures live in the *acoustic* and *growth-rate* channels, not in web topology (which is fixed by the initial spectrum and carries no substrate signal at observable `k`, per the S43 closures). This is internally coherent and holds the framing law without relapse.

**What it constrains.** The whole LSS prediction set is **conditional on a borrowed ΛCDM `H(z)`** until the `a(t)` / back-reaction-closure gap (frontier #1/#8) is closed. The capstone is exactly right that this is "a category statement about the fundamental object, not a discarded obligation" — but for *observational LSS specifically* it means: every `f·σ₈`, `σ₈`, and BAO-growth comparison is a substrate *modulation* on an external expansion history, and a referee will (correctly) ask whether the modulation survives when the framework supplies its own `H(z)`. The growth-rate suppression is the LSS observable most exposed to this caveat, because RSD measure the product `f(z)·σ₈(z)` and `f(z) = d ln D / d ln a` depends on the expansion history through `D(a)`.

**What opens.** Three concrete LSS computations are ripe (§V): (1) the first-sound-ring *experiment-sensitivity* comparison (the only paper-search-gated CF in W6, substrate forecast already done); (2) the first-sound-ring *imprint-amplitude* from the fabric↔photon-baryon coupling (the deeper physics gate underneath #1); (3) surfacing and forecasting `f·σ₈(z)` as a §7.1/§7.2 falsifier against DESI 5yr / Euclid. A fourth (§V.4) tests whether the `f·σ₈` suppression is robust to the framework supplying a non-ΛCDM `H(z)` proxy (the SCALE-FACTOR-54 Connes-distance `a(τ)` proxy that carries the deceleration band).

**What closes.** Nothing of mine. The S43 volume-averaged-statistics closures (P(k), ξ(r), VSF, Minkowski, genus, persistent Betti) remain closed and the document does not reopen them. The bulk-flow discrimination (S70 W4-E, SNR=0.064 vs cosmic variance) remains undiscriminating and is correctly absent from the falsifier inventory.

---

## V. Carry-Forward Computations

**MANDATORY — primary input to the next compute session. Each entry has all four fields. These are the LSS-domain harvest of the capstone's open questions.**

```
V.1. First-sound-ring experiment-sensitivity comparison (the live BAO falsifier)
   - What: Complete the CMB-S4 / Simons Observatory θ_s + P(k)-amplitude sensitivity
     comparison against the substrate first-sound-ring amplitude. The substrate forecast
     is ALREADY computed (S95 W6-2: δP/P = 0.2032 at k₁ = 0.0193 Mpc⁻¹, r₁ = 325.3 Mpc;
     per-branch sub-feature δP/P = 1.445e-3 at k_BAO = 0.043 Mpc⁻¹). Fetch a named
     experiment's matter-P(k)/C_ℓ AMPLITUDE sensitivity at k₁ (not just the acoustic-scale
     ruler), compute σ-equivalent reach, emit PASS/INFO/FAIL.
   - Inputs: computations/session-95/s95_w6_2_bao_amplitude_transport.npz (forecast + ring);
     canonical_constants.py (c_B1, c_B3, c_Gold, Gamma_eff=0.99970, A_FS=0.2045);
     S43 KK-CMB-TF-43 transfer-function (r₁=325.3 Mpc, A_FS=0.2045); a RESTORED
     mcp__paper-search__* for CMB-S4/SO BAO amplitude sensitivity + DESI DR2 0.24% ruler.
   - Gate: S96-BAO-EXPERIMENT-SENSITIVITY (already pre-registered, S95 W6 §CF). PASS iff
     the ring amplitude (0.2032) exceeds the fetched experiment amplitude-sensitivity floor
     (live falsifier); INFO if below current but above next-gen forecast; FAIL if below the
     effacement floor (9e-8) at all forecast detectors.
   - Effort: ~0.5 wave-equivalent. Depends on: W6-2 (INFO, DONE) + paper-search MCP
     restoration. Re-uses S95 W6-2 transport machinery; only the experiment fetch + σ-reach is new.
```

```
V.2. First-sound-ring imprint amplitude from the fabric↔photon-baryon coupling
   - What: Compute the ACTUAL imprint amplitude of the first-sound ring on the observed
     matter power spectrum, i.e. resolve whether the ring imprints at A_FS ≈ 0.204·A_BAO
     (equipartition) or down at the ~1e-6 effacement floor (undetectable). This is the
     UNTESTED fabric↔photon-baryon coupling S94 §5 flagged — the deeper physics gate
     UNDER V.1 (V.1 forecasts reach IF the ring imprints; V.2 computes whether it does).
     Derive the coupling from the a₂-channel transduction of the substrate first-sound
     mode into the emergent photon-baryon fluid at recombination.
   - Inputs: S43 KK-CMB-TF-43 transfer function + s43_kk_cmb_transfer.npz; the a₂-channel
     transduction (analog greybody Γ(ω), S95 W4-3); canonical_constants.py (c_1, c_2, R_*,
     Gamma_eff, f_b=0.156); the GGE relic spectrum (N_pair, Bogoliubov coeffs, E18); the
     S95 W4 acoustic-white-hole exit-surface greybody factor.
   - Gate: NEW S96-FIRST-SOUND-IMPRINT-AMPLITUDE. PASS = imprint amplitude ≥ a fixed
     detectability fraction of A_BAO (live, named-experiment-detectable); INFO = between the
     effacement floor and detectability (next-gen target); FAIL = at/below the ~1e-6 effacement
     floor (structurally undetectable). Pre-register the detectability fraction against V.1's
     fetched sensitivity.
   - Effort: ~1.0-1.5 wave-equivalent (the transduction coupling is genuinely new physics:
     the substrate-mode → emergent-fluid coupling at recombination, not just a projection weight).
   - Depends on: V.1 (for the detectability threshold); S95 W4-3 greybody.
```

```
V.3. Surface and forecast f·σ₈(z) as a §7.1 row + §7.2 falsifier (DESI 5yr / Euclid)
   - What: Compute the framework's full f·σ₈(z) curve over 0 < z < 1.5 and forecast it
     against DESI 5yr / Euclid RSD precision. The S77 result (PROVEN, 4% suppression vs
     ΛCDM, correct S₈ sign; σ₈(FW)=0.7932, f_FW=0.525492 at z=0) is an LSS DISCRIMINATOR
     currently MISSING from the capstone §7.1 outputs table AND §7.2 falsifier inventory.
     Produce the z-dependent f·σ₈(z) (not just z=0), the per-z σ-distance from a forecast
     DESI/Euclid f·σ₈ measurement, and a falsifier-inventory row. Recommend the §7.1 + §7.2
     edits to mack-cosmic-bridge (falsifier-inventory sole writer).
   - Inputs: s65_fsigma8_log.txt / s69_pvd05_fsigma8_log.txt (D_FW/D_LCDM=0.978011 growth
     ratio; f_FW, σ₈ values); canonical_constants.py (sigma_8=0.799 framework value, growth
     channel a₂); a borrowed ΛCDM H(z) (caveat C10 — declare explicitly); a FETCHED DESI 5yr /
     Euclid f·σ₈(z) forecast-precision table (paper-search-gated).
   - Gate: NEW S96-FSIGMA8-Z-FORECAST. PASS = the framework f·σ₈(z) curve is within the
     forecast DESI/Euclid band at all z (a viable zero-parameter LSS prediction); INFO =
     within at some z, outside at others (z-dependent discriminator); FAIL = outside the
     forecast band at all z (LSS-excluded). Feeds the §7.2 falsifier inventory as a new row.
   - Effort: ~1.0 wave-equivalent (the z=0 numbers exist; the new work is the z-curve, the
     forecast fetch, and the σ-distance band).
   - Depends on: S77 f·σ₈ result (PROVEN); a borrowed H(z); paper-search MCP.
```

```
V.4. f·σ₈ robustness to a substrate-proxy H(z) (decouple the borrowed-ΛCDM caveat)
   - What: Recompute f·σ₈(z) replacing the borrowed ΛCDM H(z) with the SCALE-FACTOR-54
     Connes-distance proxy a(τ) (the proxy that carries the deceleration band, q from −0.97
     to +0.81 — NOT a_eff, which is near-flat and diverges). Test whether the "4% suppression,
     correct S₈ sign" survives when the expansion history is the substrate's own proxy rather
     than a ΛCDM background. This directly attacks the C10 caveat that all LSS predictions are
     "modulation on a borrowed H(z)." If the suppression survives, the LSS prediction is far
     stronger; if it flips, the borrowed-H(z) dependence is load-bearing and must be stated.
   - Inputs: SCALE-FACTOR-54 a(τ) Connes-distance proxy (q-band data); S95 W4-4 conformal-factor
     Ω(τ) embedding (the construction that reproduces the q-range with the Connes proxy);
     s65/s69 f·σ₈ machinery; canonical_constants.py (sigma_8, growth channel). The M_KK⁻¹→seconds
     normalization remains open — declare it as the residual undetermined piece (do NOT invent it).
   - Gate: NEW S96-FSIGMA8-PROXY-H-ROBUSTNESS. PASS = the 4% suppression + correct S₈ sign
     survives the proxy-H(z) substitution within a pre-registered tolerance (suppression
     H-independent → strong LSS claim); INFO = sign survives but magnitude shifts > tolerance
     (H-dependent magnitude); FAIL = sign flips (the suppression is an artifact of the
     borrowed ΛCDM H(z)). Pre-register the tolerance.
   - Effort: ~1.5 wave-equivalent (re-uses growth machinery, but the proxy-H(z) → D(a) → f(z)
     recomputation with the Connes-distance a(τ) is genuinely new; the normalization caveat
     means the result is a SHAPE test, not an absolute-time test).
   - Depends on: V.3 (the f·σ₈(z) baseline); SCALE-FACTOR-54; S95 W4-4 conformal embedding.
```

```
V.5. Void statistics under the GGE-acoustic organization vs ΛCDM initial-spectrum voids
   - What: Test whether the substrate's GGE-acoustic structure organization predicts any
     void-statistics signature (void size function, void-galaxy cross-correlation, void
     ellipticity) DISTINGUISHABLE from a ΛCDM initial-power-spectrum void population. My S43
     closure found volume-averaged void statistics CLOSED (k_transition ~ 9.4e23 h/Mpc, far
     above survey scales) — so the EXPECTED result is a NULL. This CF makes the null QUANTITATIVE
     against the apply uniqueness criterion: confirm no other model would match, and confirm the
     framework predicts the SAME void statistics as ΛCDM at observable k (not a different one).
   - Inputs: s43 persistent_homology + void-size-function machinery (HOM-43, VOID-SIZE-70);
     k_transition = 9.4e23 h/Mpc (S43); the GGE relic spectrum (E18); a ΛCDM void-population
     baseline (VIDE/ZOBOV-style VSF, fetched or from s43); canonical_constants.py.
   - Gate: NEW S96-VOID-DISCRIMINANT (or re-confirm CLOSED). PASS would mean a detectable
     void signature exists (REOPENS a closed test — high bar); INFO = a sub-survey-scale
     signature exists but undetectable; expected verdict = FAIL/NULL (voids carry no substrate
     discriminant at observable k, confirming the S43 closure quantitatively). Document the
     uniqueness-criterion check explicitly.
   - Effort: ~0.5 wave-equivalent (re-confirms a closure quantitatively; mostly re-runs S43
     machinery with the GGE spectrum and an explicit uniqueness-criterion statement).
   - Depends on: S43 closures (HOM-43, VOID-SIZE-70); the GGE relic spectrum.
```

---

## VI. Summary Table

| # | Result / item | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Cosmic web = GGE-acoustic interference via `a₂` | PHONONIC | Solid (framing-correct) | Substrate-first LSS account holds; discriminants live in acoustic + growth channels, not web topology |
| 2 | First-sound ring `r₁=325.3 Mpc`, `A_FS=0.204` | PHONONIC | Live falsifier (DISTINCTIVE, no ΛCDM counterpart) | The one zero-parameter LSS prediction; experiment-sensitivity fetch is the ripe CF (V.1) |
| 3 | BAO per-branch shift 0.14%/0.44%; effacement SUPPRESSES | PHONONIC | Verified (S95 W6-2); below DESI | Suppression direction correct; not a present falsifier; §6.2 "far below rulers" phrase risks conflation with the ring (over-precise) |
| 4 | Ring imprint amplitude (fabric↔photon-baryon coupling) | PHONONIC | OPEN (UNTESTED coupling) | Deeper gate under V.1: ring POSITION is zero-parameter; DETECTABILITY hinges on an uncomputed coupling (V.2) |
| 5 | `σ₈ = 0.799` | PHONONIC (`a₂` growth) | VIABLE (~2σ between Planck/lensing) | Reported correctly; but static σ₈ is a weak discriminator |
| 6 | `f·σ₈(z): 4% suppression, correct S₈ sign` (S77 PROVEN) | PHONONIC (`a₂` growth) | **MISSING from capstone §7.1/§7.2** | The genuinely discriminating RSD observable; main documentation gap; surface + forecast (V.3) |
| 7 | All LSS predictions on borrowed ΛCDM `H(z)` (C10) | NON-PHONONIC (borrowed `H`) | Honest caveat, foregrounded | Every f·σ₈/σ₈/BAO-growth claim is a modulation on external `H(z)`; test robustness to a substrate-proxy `H(z)` (V.4) |
| 8 | Volume-averaged LSS stats (P(k), ξ(r), VSF, Minkowski, genus, Betti) | GEOMETRIC | CLOSED (S43; `k_transition≈9.4e23 h/Mpc`) | Not reopened by capstone (correct); make the void-statistics null quantitative + uniqueness-checked (V.5) |

---

*End cosmic-web capstone review. Sole writer of this file. §V is the LSS-domain harvest of the capstone's open questions: V.1 (first-sound-ring experiment fetch — already pre-registered as S96-BAO-EXPERIMENT-SENSITIVITY), V.2 (ring imprint amplitude — the deeper coupling gate), V.3 (surface + forecast the MISSING f·σ₈(z) falsifier), V.4 (f·σ₈ robustness to a substrate-proxy H(z)), V.5 (quantitative void-statistics null). The capstone's LSS content is solid and honest; its one significant gap is the absent f·σ₈ growth-rate prediction, and its one over-precise phrase is the §6.2 "far below current rulers" sentence that risks conflating the per-branch sub-feature with the live first-sound ring.*
