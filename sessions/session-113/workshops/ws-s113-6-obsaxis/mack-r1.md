# WS-S112-6 OBSAXIS — Round 1

**Workshop**: WS-S112-6 OBSAXIS — the CMB-orthogonal observational steer (NICER dense-matter EoS vs DESI/Euclid f·σ₈ growth)
**Author**: mack-cosmic-bridge — Round 1, steelman **Reading B** (DESI/Euclid f·σ₈ growth-suppression axis)
**Date**: 2026-06-22
**Thesis (one line)**: The growth-suppression axis is the higher-EVOI next falsifiable substrate prediction **because it is the only one of the two that is already CONSTRUCTED, already PRE-REGISTRED, and already a LIVE falsifier surface** — the substrate pins a zero-parameter f·σ₈(z) curve with a forward σ-budget against DESI/Euclid, whereas the compact-object axis must first build a mass–radius sector the framework does not have (Row #88 CORPUS-EXCEEDS gap) and, when its most natural NICER construction WAS tried (INV13-W2-1 finite-μ CFL EoS), it FAILED at ~12× below the 2 M_⊙ pulsar floor.

This is not a claim that NICER physics is unimportant. It is a claim that, *for this substrate at its current state*, the f·σ₈ gate has the higher EVOI = P(pass)·|ΔP_pass| + P(fail)·|ΔP_fail|, because both the tractability AND the falsifiability terms are larger on the growth axis.

---

## 0. What the tension actually is (neutral restatement, so I don't strawman)

`§EVOI.BF` (the S110 W4b-3 / INV13-W2-3 Bayesian re-anchor, `sessions/investigation/investigation-13/investigation-13-bayesian-reanchor-synthesis.md §VI.2`) established that the framework's observational *risk* has concentrated on the CMB axis — n_s at **4.73σ global** (look-elsewhere-corrected, Šidák N=4), w_a at **3.43σ**, A_s **route-unstable** (>3 OOM spread, no convergent route). The structural cohort rose (10 blind Stage-2 STAGE-3 promotions, joint BF 25–55); the observational cohort fell; the ~22% headline survives by near-exact cancellation. The re-anchor's forward consequence (§VI.2):

> "Highest-leverage forward EVOI is now ORTHOGONAL to the CMB axis … a PASS on a dataset the framework was NOT built to explain (NICER pulsar-mass EoS, DESI/Euclid f·σ8 growth-suppression) is worth more than another CMB refinement."

It named **two** non-CMB opportunity axes and did not rank them. That ranking is this workshop's job. I argue the ranking is forced toward the growth axis by the substrate's own ledger — not by my preference.

I take Reading A at its strongest: the substrate genuinely HAS a compact-object-adjacent physics surface — the acoustic white-hole interior is PROVEN-formalized (S85, single-asymmetric-open causal disconnect; `sign(Γ_core) = −1`, supersonic vacuum-energy-dominated interior), the type-IV EMT bridge is NAMEABLE (`S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC` INFO: `Γ_sub = a₂-channel g_tt`, restoration radius = Mach-1 surface), and the framework has a finite-μ diquark-pairing (CFL) sector to which a NICER mass–radius prediction is the natural laboratory image. That is the strongest version of Reading A, and I will engage it head-on in §4.

---

## 1. The substrate ALREADY pins a complete, zero-parameter growth-suppression prediction

This is the load-bearing asymmetry. The growth axis is not a hoped-for opportunity awaiting a derivation; the derivation is done, the constants are canonical, and the prediction is on the live falsifier surface.

**The pinned prediction (all `get_constant`-verified, non-superseded):**

| Quantity | Value | Provenance |
|:---------|:------|:-----------|
| `f_FW(0)` (linear growth rate `dlnD/dlna` at z=0, a₂ Seeley-DeWitt channel) | **0.5254916357** | S96 W6-1, `s70_bulk_flow.npz:f_FW_z0` (orig S59/S65 growth ODE) |
| `f_LCDM(0)` (standard-growth reference) | 0.5271303866 | canonical |
| `sigma8_growth_a2` (a₂-growth-channel σ₈ readout feeding f·σ₈) | **0.79317** | S70/S96/S97, re-confirmed `S97-FSIGMA8-FORECAST-REFETCH` PASS |
| `fsigma8_product_suppression_FW_max_pct` (the discriminating observable) | **−4.058% @ z=0.51** | S96 `s96_obs_fsigma8_forecast.npz:max_frac_FW_pct` |
| bare-f suppression (C5 conflation guard — do NOT cite this as the product) | −0.311% | S98 W6 |

The substrate-IS chain is explicit and forward-directed (no container inversion): `D_K eigenvalues → a₂ Seeley-DeWitt coefficient → emergent growth factor D(a) → f(z)=dlnD/dlna → f·σ₈(z) product`. The f·σ₈ **product** suppression of −4.058% is a genuine substrate prediction — it is NOT the bare-f −0.311% (the C5 conflation guard, Row #71), and it carries the right *sign* (suppression negative ⇒ FW f·σ₈ below ΛCDM).

**Crucially, this is a registered live falsifier** — Row #71 / Row #71.aug-S110-LSS-FLAGSHIP:

> "f·σ₈ growth-suppression is the **LIVE near-term LSS FLAGSHIP** alongside the first-sound BAO ring (Row #72): a measured RSD f·σ₈(z) above the framework's suppressed value at decisive significance falsifies the a₂-growth-channel prediction. Detector trajectory: **DESI-5yr σ-distance ~1.0σ @ z≈0.5 (marginal) → Euclid ~1.5σ across 7 z-bins (approaching decisive)**."

The flagship status is not decorative. f·σ₈ was *promoted to flagship* precisely because the GW-detector flagship was RETIRED (Row #7.audit-3: walls=0 EXACT, peak GW-detector-sterile at 8.48×10³⁹ Hz, falsifier migrated GW→LSS). The framework's *current* near-term zero-parameter falsifier surface is LSS. The growth axis is where the action already is.

---

## 2. The decisive fact: the head-to-head was ALREADY RUN, and growth WON

This is the single most important consideration in the entire workshop, and it is not my prediction of what *would* happen — it is a recorded verdict pair. Investigation 13 dispatched the two axes of THIS exact tension as parallel compute gates:

- **`INV13-W2-2-FSIGMA8-GROWTH-S8`: PASS** — `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`. The growth-suppression gate produced a clean three-tuple PASS. `S8_FW=0.8128` in-band `[0.76, 0.83]` (band-position 0.75); suppression sign-correct **16/16** redshift bins negative; **DESI-5yr bindable = True** (max 1.001σ @ z=0.5, reproducing the upstream Row #71 1.013σ @ z=0.51); Euclid 7 bins; K_pivot-localization available. Envelope: δ_z ∈ [−4.063%, −2.503%], product_max = −4.0578% @ z=0.51 (reproduces canonical −4.058% to 4 sig figs). Audit `435609fc74bc4d3c…`.

- **`INV13-W2-1-FINITE-MU-CFL-EOS`: FAIL** — `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`. The finite-μ CFL EoS gate — **the natural NICER construction for Reading A** — gave `M_max_FW = 0.1631 M_⊙`, against the required band `[2.0, 2.6] M_⊙`. That is **~12× below the 2 M_⊙ pulsar bound** (the dual-SHA row records it explicitly). The diquark pairing has the correct *sign* (`dΔ_CFL/dμ > 0` at every scan point — substrate diquark pairing has the right density-dependence, the durable SIGN-PASS result), but the gap runs away (`gap_ratio Δ/μ = 4.82` vs physical CFL ≈ 0.05–0.1, VanHove-dominated fraction 1.000), producing a catastrophically soft EoS. Audit `59f33c74b5b1df8b…`.

Read these two verdicts side by side. On exactly the two axes this workshop is asked to rank, the substrate has *already* produced:

- a clean **PASS** on the growth axis with a pre-registered, bindable σ-distance, and
- a **FAIL** on the dense-matter axis whose magnitude leg misses by an order of magnitude.

For an EVOI argument this is close to dispositive on the tractability term. The growth gate's P(pass) is high (it already passed once, with a forward instrument trajectory that sharpens it). The NICER gate's P(pass) for a *mass–radius discrimination* is, right now, structurally near-zero — the substrate cannot produce a star above 0.16 M_⊙ in its most natural finite-μ construction, so it cannot land anywhere near a NICER pulsar (PSR J0740+6620 at ~2.08 M_⊙, ~12.4 km). A gate whose substrate prediction is 12× off the observable cannot be the higher-EVOI *next* falsifiable prediction; the work needed to make it falsifiable-and-survivable is a multi-session EoS-stiffening program, not a single pre-registrable gate.

I want to be scrupulous about what the W2-1 FAIL does and does not mean (per the framework's own "all results are good results" discipline): the FAIL is INFORMATIVE — it closes the "naive finite-μ CFL EoS supports neutron stars" corridor and pins the durable SIGN-PASS (the density-dependence is right). It does NOT prove the compact-object axis is permanently dead. But it does establish that *as of now* the NICER axis is not pre-registrable as a survivable discriminator, whereas the growth axis is.

---

## 3. The growth axis is a LIVE falsifier surface; the compact-object axis is a documented GAP (the constructibility asymmetry)

EVOI rewards an axis where BOTH outcomes move the posterior. The growth axis qualifies on both sides; the compact-object axis qualifies on neither, because the framework makes no compact-object prediction to be confirmed or refuted.

**Growth axis — bidirectional, already-binding.** There is a PROVEN theorem on this surface: the σ₈ exclusion (Cosmic-Web, `session-49-wayforward.md`): *"if O-Z is literal, the framework is already falsified by lensing data."* A channel that can *already exclude* the framework is the definition of a tractable falsifier. The framework survives only because σ₈ is read as the a₂-growth-channel suppressed value (0.79317, −2.18% vs ΛCDM 0.811), not the literal O-Z headline. That is exactly the kind of live tension where a sharpened measurement has high |ΔP| in BOTH directions: a DESI/Euclid f·σ₈ *above* the suppressed prediction falsifies the a₂-growth channel; *at or below* it confirms a zero-parameter prediction on a dataset the framework was not built to fit (the Baloney-Detection-Kit gold standard, §EVOI.BF point 2). Both legs of EVOI are large.

**Compact-object axis — no prediction, hence no falsifiability (yet).** Row #88 is unambiguous and is *the framework's own self-assessment*:

> "THIS ROW IS A GAP RECORD, NOT A FALSIFIER ROW. It carries NO framework prediction, NO σ-distance, NO detector-pinned threshold, and NO live-watch … the framework has **NO mass-radius relation, NO formation channel, NO compactness bound** (cf. gravastar `C = 3/8`), and **NO QNM / echo / shadow spectrum** for any compact object. … the rich ECO observational program **cannot refute it; it can only expose the gap**."

This is the CORPUS-EXCEEDS finding: the gravastar/ECO program (Mazur-Mottola → Visser → Jampolski-Rezzolla) is rich and predictive there; the substrate is empty there. The *only* conditional opening Row #88 identifies is a **scalar-channel ringdown/echo** (the acoustic white hole is scalar-only, `β_T = 0` exactly by the [T3] Scalar-Tensor Kasparov Decoupling) — and it has **NOT been computed** and has **no detector**. A tensor-echo gate would be NON-discriminating (equally Kerr and framework; Occam favors Kerr). Routing a NICER/echo gate as live now would, in the framework's own words, "manufacture a falsifier the framework's own retired-GW stance does not support."

So the constructibility asymmetry is stark: the growth gate is pre-registrable *today* (its prediction, σ-budget, and instrument are all pinned). The NICER/compact-object gate requires the framework to FIRST build a mass–radius sector it does not have. That construction is itself an open research program (baptista's synthesis names "no compact-object sector" as one of the framework's "two newest gaps," tracing to the 23 unexplored Milnor dimensions) — not a next falsifiable prediction.

---

## 4. Engaging the strongest threat honestly: is there a genuinely tractable NICER prediction?

I owe the open verdict a serious attempt to construct Reading A's best case, because if a tractable NICER gate exists, my ranking is wrong. Here is the strongest NICER construction I can build for the substrate, and why it does not (yet) clear the bar:

**Candidate A-1 — re-anchored CFL EoS with a physical gap-saturation.** The W2-1 FAIL traced to `gap_ratio Δ/μ = 4.82` (runaway) vs physical CFL ≈ 0.05–0.1. One could argue the FAIL is a *calibration* artifact — the substrate gap was pinned R-PROTECTED at `Δ(μ_ref) = Δ_BCS = 0.4642547` and scanned, and the VanHove-dominated fraction 1.000 drove the runaway. A re-anchored gap (capping the VanHove contribution, or imposing the physical Δ/μ ratio as a constraint) might stiffen the EoS toward 2 M_⊙.

*Why this does not yet clear the bar*: this is precisely the move EVOI penalizes when it is *unpinned*. To make the re-anchored CFL EoS a pre-registrable NICER gate, you must FIRST derive the gap-saturation from the substrate (not impose it to hit the 2 M_⊙ target — that would be convention-shopping / ansatz-forced PASS, PROHIBITED_ACTIONS Class 4). The substrate's gap *is* VanHove-dominated (the W2-1 regime=VALID confirms this is not a numerical artifact). So a substrate-honest re-anchor is itself an open derivation, multi-session, with no guarantee it lands in `[2.0, 2.6] M_⊙` — it could equally confirm the soft-EoS FAIL is structural. P(pass) is genuinely uncertain and the work-to-pre-registrability is large. Contrast: the growth gate's P(pass) is *already demonstrated* (W2-2 PASS).

**Candidate A-2 — type-IV-EMT compactness bound as a "max-compactness" NICER-adjacent prediction.** The type-IV EMT bridge (`S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC` INFO) names `Γ_sub = a₂-channel g_tt` with a restoration radius at the Mach-1 surface. One could try to extract a substrate max-compactness `C_sub` analogous to the gravastar `C = 3/8`, testable against NICER M/R contours.

*Why this does not yet clear the bar*: the bridge spec is INFO with **one unpinned leg** — the localized-relay velocity profile `v(r)`, routed to `CF-S105-RELAY…`. Without `v(r)`, there is no M(R) curve, only a restoration *radius* (the Mach-1 surface), which is a single scale, not a mass–radius relation. The white-hole interior is a *cosmogenesis* object (the fold), not a static stellar-remnant object — Row #88 is explicit that "the framework has a cosmogenesis transit + a cosmological vacuum (a₀); the static-compact-object sector is empty." Mapping the dynamical fold onto a static NICER pulsar is not a pinned bridge; it is a research conjecture.

**Net on the threat**: both NICER constructions I can build are *open derivations whose P(pass) is unknown and whose path to pre-registrability is multi-session*. Neither is a "next falsifiable prediction" in the EVOI sense — both are "next research programs." The growth gate is the opposite: a pinned prediction, a pinned σ-budget, an existing PASS, and a sharpening instrument. On the work-to-falsifiability metric, growth dominates by a wide margin.

I also note — in fairness to Reading A and to keep the verdict open — that the dense-matter axis has ONE durable asset the growth axis arguably lacks: the W2-1 SIGN-PASS (`dΔ_CFL/dμ > 0`) is a genuine substrate prediction about diquark density-dependence that, IF a NICER-relevant observable could be tied to the *sign* of the EoS stiffening rather than its magnitude, might be pre-registrable sooner than a full M/R curve. My opponent will likely press exactly this. My preliminary answer (to be sharpened in R2): a sign-only EoS prediction does not discriminate against NICER M/R contours, which are magnitude measurements — so the SIGN-PASS, while durable, is not yet a falsifiable NICER prediction. But I flag it as the strongest seed of Reading A and will engage it directly when I see nazarewicz's R1.

---

## 5. The EVOI arithmetic, made explicit

Let me write the EVOI = P(pass)·|ΔP_pass| + P(fail)·|ΔP_fail| for each axis, with honest inputs (these are ordinal-leverage proxies per `evoi-prioritization.md`, not calibrated probabilities — but the *ordering* is robust):

**Growth axis (f·σ₈ at DESI-5yr → Euclid):**
- P(pass) HIGH (W2-2 already PASS; DESI-5yr ~1.0σ marginal, Euclid ~1.5σ/7-bins approaching decisive).
- |ΔP_pass| LARGE: a confirmed zero-parameter suppression on a dataset the framework was not built to fit is independent-confirmation gold (§EVOI.BF) — it raises the structural-cohort-adjacent confidence the way the 10 blind STAGE-3 promotions did.
- |ΔP_fail| LARGE: a measured f·σ₈ above the suppressed value at decisive σ falsifies the a₂-growth channel — it would be a clean refutation on a live flagship, not a soft tension.
- **Both terms large ⇒ high EVOI, and it is pre-registrable NOW.**

**Compact-object axis (NICER M/R):**
- P(pass) for a *survivable mass–radius discrimination*: structurally near-zero today (W2-1 FAIL at 12× below the floor; no pinned M/R curve exists).
- |ΔP_pass| would be large IF a prediction existed — but it does not (Row #88: no prediction).
- |ΔP_fail|: the framework "cannot be refuted" on this surface (Row #88) — a null/contrary NICER result is NON-discriminating. So the fail-leg moves the posterior by ≈0.
- **The pass-leg has no prediction to confirm and the fail-leg cannot refute ⇒ EVOI of the gate-as-it-could-be-pre-registered-today is ≈0.** The high-EVOI version requires first building the sector (a research program), which is not a "next falsifiable prediction."

The ordering is forced: **growth > compact-object** on EVOI, and the gap is not marginal.

---

## 6. The pre-registrable gate (Reading B's deliverable)

Per the adjudication question's demand for a pre-registrable gate, here is the concrete forward gate the growth axis supports. It is essentially the Euclid build-out that Row #71 already flags as the "remaining W6-class compute CF":

```
GATE: CF-S113-FSIGMA8-EUCLID-7BIN  (compute)
  Hypothesis: the framework's zero-parameter f·σ₈(z) curve (f_FW(0)=0.5254916,
    σ8_growth=0.79317, product suppression −4.058% @ z=0.51) is jointly consistent
    with — or falsified by — the Euclid DR1 RSD f·σ₈ measurements across the 7
    spectroscopic z-bins (z ≈ 0.9–1.8), tested as a joint χ² against the ΛCDM
    f·σ₈ template with the framework Ω_m.
  Substrate-first observable: D_K → a₂ Seeley-DeWitt → D(a) → f(z) → f·σ₈(z) product.
  PASS / FAIL boundary: joint χ²/N over the 7 Euclid bins.
    PASS = the suppressed FW curve lies within the joint Euclid 1σ envelope
      (consistent; zero-parameter prediction survives on a non-CMB dataset).
    FAIL = the joint σ-distance ≥ a pre-registered decisive threshold (the
      a₂-growth-channel suppression is excluded).
  Pre-registered σ-budget (already pinned, Row #71): per-bin Euclid ~1.5σ;
    joint over 7 bins approaching decisive. DESI-5yr (~1.0σ @ z≈0.5) is the
    near-term marginal anchor; Euclid is the decisive instrument.
  Anti-rescue fence: the −4.058% PRODUCT suppression is the test quantity, NOT
    the bare-f −0.311% (C5 conflation guard); σ8_growth=0.79317 is USED (NOT the
    O-Z headline 0.799). No branch/scheme freedom — the prediction is zero-parameter.
  Falsifier-inventory landing: mack-cosmic-bridge sole-writer onto Row #71
    (additive σ-distance sub-row), per the canonical write-order.
```

This gate is pre-registrable today because every input (prediction value, σ-budget, instrument, observable) is already pinned. The contrast with Reading A could not be sharper: there is no analogous NICER gate I can write today without first inventing the mass–radius sector.

---

## 7. (i) Honest current lean and (ii) the single most decisive consideration

**(i) Honest current lean.** I lean — at this stage, before seeing nazarewicz's R1 — toward **Reading B (growth) as the higher-EVOI next falsifiable prediction, by a clear margin**. The lean is not driven by domain partisanship; it is driven by the constructibility asymmetry plus the already-recorded W2-2-PASS / W2-1-FAIL verdict pair. I hold the verdict genuinely open on one point: if nazarewicz can construct a NICER gate from the W2-1 SIGN-PASS (the durable `dΔ_CFL/dμ > 0` density-dependence) that is *pre-registrable today* and *survivable* (i.e., does not require the EoS to stiffen to 2 M_⊙ as a magnitude condition), then the gap narrows and the ranking becomes contestable. I do not currently see how to build such a gate (a sign-only EoS prediction does not discriminate against NICER's magnitude-measured M/R contours), but that is the place I will look hardest in R2.

**(ii) The single most decisive consideration.** *The head-to-head was already run, on exactly these two axes, and the result is on disk*: `INV13-W2-2-FSIGMA8-GROWTH-S8` PASS (sign+magnitude+regime all PASS, DESI-5yr bindable) versus `INV13-W2-1-FINITE-MU-CFL-EOS` FAIL (M_max = 0.1631 M_⊙, ~12× below the 2 M_⊙ pulsar floor). EVOI asks where to spend the *next* unit of falsification work. One axis already produced a clean, bindable PASS with a sharpening instrument; the other produced a magnitude-FAIL an order of magnitude off the observable and has no pinned prediction to test. The substrate has already told us which non-CMB axis is the tractable falsifier — the growth axis — and the EVOI ordering follows directly.

---

### Sources cited (all read / MCP-verified this round)
- `§EVOI.BF` via `investigation-13-bayesian-reanchor-synthesis.md` §IV/§V/§VI.2 (the re-anchor; n_s 4.73σ-global, w_a 3.43σ, A_s route-unstable; the two named non-CMB axes; the "PASS on a dataset not built to explain" criterion).
- `falsifier-master-inventory.md` Row #71 / Row #71.aug-S110-LSS-FLAGSHIP (f·σ₈ live flagship, DESI-5yr ~1.0σ → Euclid ~1.5σ/7-bins); Row #72 (first-sound ring co-flagship); Row #7.audit-3 (GW→LSS migration, walls=0 EXACT, peak GW-detector-sterile); Row #88 (COMPACT-OBJECT-SECTOR GAP — "NO mass-radius relation, NO formation channel, NO compactness bound, NO QNM/echo/shadow"; scalar-channel NOT computed, no detector).
- `inv13_gate_verdicts.txt`: `INV13-W2-2-FSIGMA8-GROWTH-S8` PASS (S8_FW=0.8128 in-band, 16/16 sign-neg, DESI-5yr bindable); `INV13-W2-1-FINITE-MU-CFL-EOS` FAIL (M_max=0.1631 M_⊙, gap_ratio=4.82, SIGN-PASS durable).
- canonical_constants via `get_constant`: `f_FW=0.5254916357`, `f_LCDM=0.5271303866`, `sigma8_growth_a2=0.79317`, `sigma8_OZ_50=0.799`, `fsigma8_product_suppression_FW_max_pct=−4.058`.
- `investigation-7-plan-w1.md` §W1-6 (the f·σ₈ joint-bin growth gate, "highest-value near-term LSS compute") + the full INV7 LSS campaign (W1-1…W1-6).
- σ₈ exclusion theorem (`session-49-wayforward.md`, Cosmic-Web, PROVEN: "if O-Z is literal, the framework is already falsified by lensing data").
- `S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC` INFO (type-IV EMT bridge, one unpinned leg → CF-S105-RELAY); S85 acoustic white-hole formalization (PROVEN, single-asymmetric-open).
- Framing law: `phononic-framing.md` (substrate-IS; the growth chain is read FORWARD `D_K → a₂ → D(a) → f·σ₈`, never inverted); `evoi-prioritization.md` (EVOI = P(pass)·|ΔP_pass| + P(fail)·|ΔP_fail|; ordinal-leverage proxies).
