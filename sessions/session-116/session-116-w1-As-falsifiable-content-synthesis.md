# Session 116 W1 Synthesis: Falsifiable Content of the A_s Magnitude Leg After the Exit-Greybody Closed as Irreducibly Fitted

**Date**: 2026-06-28
**Agent**: sagan-empiricist (Sagan)
**Source Documents**:
- `sessions/session-116/workshops/s116-w1-htilde-recon.md` (TD × mack adjudication, R1–R3 + Structural Verdict)
- `sessions/session-116/session-116-w1-workingpaper.md` (§W1-2 CFB1, §W1-3 CF2, §W1-4 CF3)
- `computations/session-116/s116_gate_verdicts.txt` (CFB1 PASS, CF2 FAIL, CF3 INFO)
- `sessions/framework/registry/falsifier-master-inventory.md` (Row #12 floor/magnitude split; audit sub-rows S110/S113/S116)

---

## I. Session Outcome

After S116-W1, the A_s magnitude leg falsifiably predicts **three** things at **zero free parameters**, and **one** thing it does **not** predict at all:

1. **The SCALE** of the primordial scalar amplitude — `A_s^squeeze = O(10⁻⁸)`, within **~1 OOM** of the observed `2.1×10⁻⁹` on every surviving route — is a genuine zero-parameter result (CFB1 PASS, an L_max-stable POINT). This is the strongest piece, and it is real.
2. **The over-production SIGN** — `A_s^squeeze > A_s^Planck` on every route (40.9σ–451σ), robust to the unresolved 𝒩 fork — is a genuine one-sided prediction (a transmission filter `Γ ≤ 1` can only attenuate, so the substrate amplitude is forced to exceed the data).
3. **Tilt-flatness** `α_s(primordial) ≈ 0` (NEW-1 / OQ4) is a genuine, near-future-falsifiable corollary that survives the 𝒩 fork.

What it does **NOT** predict is **the absolute normalization** `A_s = 2.1×10⁻⁹`. That number is **not a stake-claim**: it carries **one fitted O(1) greybody Γ** (CF2 FAIL — irreducibly fitted) **and** **one unresolved 410.7σ fork** (the transfer prefactor 𝒩, CF-S117 pending). Two free handles bridge the last factor-of-7; the absolute magnitude is **recoverable-in-principle but currently un-staked**, gated on two independent substrate closures, neither yet run.

A separate and load-bearing finding: the CF2 "**NOT substrate-derivable**" verdict is **scoped to the near-horizon-barrier construction**. CF2 scanned barrier *scales* within one bridge-map class (the Regge-Wheeler / Pöschl-Teller `sech²` transmission). The dimensionally-natural alternative — a spectral-moment-ratio (Wodzicki two-pole) or Connes-distance transmission, which lives in the `d_A=0` even-morphism sector and is **not** foreclosed by the parity wall that closes `d_A=odd` transports — is **UNTESTED**. The fitted-Γ reading is a mapped boundary on one corridor, not yet a structural wall.

---

## II. Key Results

### II.1 The A_s magnitude leg factorizes into a substrate-prediction part and a fitted part

**Result**: `A_s^obs = A_s^squeeze × Γ_exit`. PHONONIC.

Substrate-first: A_s IS the GGE-relic acoustic squeezing modulus of the post-fold produced state; the lab reads its power IN the CMB container. The chain is `D_K eigenvalues λ_k(τ) → transit Bogoliubov {α_k, β_k} → produced occupation n_k = |β_k̂|² → acoustic squeeze A_s^squeeze`, then an exit-horizon transmission `Γ_exit` (the acoustic white-hole greybody) brings the over-produced squeeze toward the observed amplitude.

The two legs have **opposite** epistemic status after S116-W1:

| Leg | Source | Status | Free parameters |
|:----|:-------|:-------|:----------------|
| `A_s^squeeze` | CFB1 (box-delta Bogoliubov, ξ_KZ-normalized) | **substrate-derived**, L_max-stable POINT, but **fork-valued** (𝒩, CF-S117) | 0, but 2-valued |
| `Γ_exit` | CF2 (near-horizon BdG scattering scan) | **NOT substrate-derived** — irreducibly fitted | 1 fitted O(1) |

An absolute-magnitude prediction requires **both** legs substrate-derived. Today one leg is two-valued and the other is fitted. That is the whole content of "the magnitude is open."

### II.2 The squeeze SCALE is a genuine zero-parameter success — within ~1 OOM, every route

**Result**: `A_s^squeeze = 1.5367×10⁻⁸` (box-delta) or `3.2994×10⁻⁹` (slow-roll-MS); both within 1 OOM of `2.1×10⁻⁹`. PHONONIC. (CFB1 PASS; CF3 route table.)

This deserves explicit credit (honest skepticism acknowledges strengths). The box-delta sudden Bogoliubov squeeze at the Kibble-Zurek scale `k̂ = 1/ξ_KZ`, with **zero tuned parameters**, lands `+0.864` OOM = a factor **7.3** from the observed CMB scalar amplitude. The alternative slow-roll-MS reading lands `+0.196` OOM = a factor **1.57**. Getting the primordial scalar amplitude *scale* right to within an order of magnitude from pure substrate transit dynamics — no inflaton potential, no normalization knob — is a non-trivial pass. The CFB1 verdict further pins it as an **L_max-stable POINT** (`rel_dev_Lmax = 5.43×10⁻⁵`, Friedrich-Bär bottom-saturated at L12), not a truncation-soft band — so the scale is a converged substrate observable, not a numerical artifact.

**Bayes-factor read of the SCALE**: the prior predictive range for "what amplitude could a quench-production mechanism set" spans many decades (the Bogoliubov `|β|²` and the `ξ_KZ³` normalization are not a priori tied to `10⁻⁹`); the posterior lands within ~1 OOM on the over-production side. BF ≈ **3–5** — a genuine but modest pass (right ballpark, low precision; the *exact* normalization is where the fitted handles live). This is a prediction, not an accommodation: the geometric inputs (`ξ_KZ`, `|β_k̂|²`) were computed independently of A_s, so the order-of-knowledge does not demote it.

### II.3 The over-production SIGN is genuine and fork-robust; the absolute magnitude is not

**Result**: `A_s^squeeze > A_s^Planck` on every route; both fork branches sit above Planck (`+0.196 = 40.9σ`, `+0.864 = 451σ`). PHONONIC.

Because a transmission coefficient obeys `Γ_exit ≤ 1` (unitarity — a filter attenuates, never amplifies), the chain `A_s^obs = A_s^squeeze × Γ_exit` is only consistent if `A_s^squeeze ≥ A_s^obs`. The framework therefore makes a **one-sided, zero-parameter, falsifiable** prediction: the pre-filter substrate amplitude exceeds the observed. **Falsifier**: a substrate squeeze *below* Planck would break the chain (no `Γ ≤ 1` could lift it up to the data). The prediction holds on both fork branches, so it is **robust to CF-S117** — its truth does not wait on 𝒩.

This is the correct reading of "the framework predicts over-squeezing; the open question is WHICH overproduction, not WHETHER" (workshop *What Holds*, L552). The "WHETHER" (over-production sign) is genuinely predicted; the "WHICH" (absolute value) is the open part.

**The decisive empirical caveat — "451σ above Planck" is NOT a framework tension.** The σ-distance of the bare squeeze leg from Planck is a *pre-filter descriptive distance*, not a falsification. `Γ_exit` is **part of the prediction chain**, not an error bar; the relevant residual is `A_s^squeeze × Γ_exit − A_s^Planck`, evaluated *after* the filter. Reporting "451σ above Planck" as a tension would mistake the input to the filter for the output of the prediction. The genuine liability is one level deeper: the filter that sets that residual is fitted.

### II.4 The fitted greybody does not even reach the data — the absolute normalization is doubly unpinned

**Result** (Sage-verified): the fitted `Γ = 0.512` closes **neither** fork branch to Planck. PHONONIC. (CF3 product annotation, cross-checked.)

| Branch | OOM over Planck | × fitted Γ=0.512 | residual vs Planck | Γ that *would* close it |
|:-------|:----------------|:-----------------|:-------------------|:------------------------|
| box-delta `+0.864` | 7.32× | `7.87×10⁻⁹` = **+0.574 OOM** | **3.75× over** (does NOT reach) | 0.1367 |
| slow-roll-MS `+0.196` | 1.57× | `1.69×10⁻⁹` = **−0.095 OOM** | 0.80× (over-shoots downward) | 0.6365 |

Two facts fall out, both sharpening "not a stake-claim":

1. **The product over-produces.** `A_s^squeeze × Γ_fit = 7.87×10⁻⁹ = +0.574 OOM` over Planck (CF3). Even *with* its own fitted filter, the box-delta route misses the data by a factor 3.75. The framework does **not** currently reproduce `A_s = 2.1×10⁻⁹`.
2. **The fitted Γ is not even the Γ that would close it.** Closing box-delta to Planck requires `Γ = 0.137`, not `0.512`; closing slow-roll-MS requires `0.636`. The fitted `0.512` (the S95 A2 sigmoid at relic-band midpoint 0.9418) is tuned to an *in-band V0 placement*, not to land any route on Planck. So the absolute normalization carries **two** free handles — the 𝒩 fork (which branch) **and** the fitted Γ (which filter) — and the current value of the second handle reproduces the data on neither branch.

This is why the absolute magnitude cannot be a stake-claim: it is `A_s = (one of two computed squeezes) × (a fitted O(1) knob)`, with `M − N ≤ 0` degrees of freedom against the single datum. A model with one datum and ≥1 free parameter has fitted nothing.

### II.5 The "NOT substrate-derivable" verdict is construction-scoped, not universal

**Result**: CF2 FAIL closes the **near-horizon-barrier** greybody corridor; the moment-ratio / Connes-distance corridors are **UNTESTED**. GEOMETRIC.

CF2 is a strong, regime-VALID result — the EXACT (non-WKB, ODE-converged, `f_used=1.00`) finite-rate BdG scattering through `V(x) = V0·sech²(κx)`, scanning the substrate barrier scales `{ω_q, relic_rms, γ_clock, 2Δ_BCS, κ_exit}`, reaches `Γ=0.512` at **no** substrate scale (best agreement `0.278 ≫ 0.10`). It also disarms S110's `eps_WKB=7.34` breakdown as a method artifact (Kapitza-averaged, finite-rate correction `≤ 7×10⁻⁴`). Within its scope it is decisive, and the corridor it closes is genuinely closed.

But mark the scope precisely. CF2 scanned barrier **scales** within **one** bridge-map class: the Regge-Wheeler / Pöschl-Teller near-horizon transmission. It did **not** test alternative substrate-IS greybody constructions:

- **spectral-moment-ratio transmission** — `Γ` as a ratio of `D_K` spectral moments (a Wodzicki two-pole ratio `Res_W(s)/Res_W(s')`, or an `a_n` moment ratio at the relic band);
- **Connes-distance transmission** — `Γ` from the spectral-triple metric `d_C = 1/(λ_max − λ_min)` on the exit-horizon BdG sector.

These are genuinely **different bridge maps**, not re-parameterizations of the `sech²` barrier. The inference "CF2 FAIL ⇒ the A_s upper-edge filter is NOT substrate-derivable (period)" therefore **over-reaches**: a FAIL on construction-class-1 is a boundary in the constraint map, not a universal theorem. This is exactly the surrogate-vs-canonical scope discipline (`substrate-first-canonical-sourcing.md §(iv-bis)`): a FAIL on one observable proxy does not falsify the canonical unless the proxy's sign/magnitude is *mechanically locked* to it — and a near-horizon barrier scan is not mechanically locked to a moment-ratio bridge.

**A structural reason the alternative is well-motivated, not idle.** The greybody `Γ` is a **dimensionless** transmission (`d_A = 0`). By the parity selection rule (`cross-pillar-bridge-corpus §23.0(5)`; the LRD-T row #88 audit), the foreclosure "every `d_A=odd` substrate observable is unreachable knob-free" rests on `d_A=odd` observables being forced onto the sign-locked **odd** `M_KK¹` scale leg with no even-degree morphism able to correct them. A `d_A=0` transmission lives in the **even-morphism sector** (Wodzicki `−2(s−s')`, HKR `0`) — precisely where moment-ratio constructions live, and precisely *not* where the parity wall bites. So the moment-ratio Γ is **dimensionally admissible** in the even sector; CF2 closed the barrier-scale corridor, but the dimensionally-natural even-sector corridor is open and untested. Until it is run, "NOT substrate-derivable" is established for one construction and **under-determined** for the filter leg as a whole.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S116-W1-AS-CFB1 (squeeze magnitude) | **PASS** (sign/magnitude/regime) | `A_s^squeeze = 1.5367×10⁻⁸`, OOM `+0.8644`, POINT (`rel_dev_Lmax=5.43×10⁻⁵`) |
| S116-W1-AS-CF2 (exit greybody) | **FAIL** (magnitude; regime VALID) | best substrate agreement `0.278 ≫ 0.10`; `Γ=0.512` reaches no substrate scale; `structural_closure=greybody_irreducibly_fitted` |
| S116-W1-AS-CF3 (route reconcile) | **INFO** (S115 PLURALISM confirmed) | `collapse_dist = 0.668 ≫ 0.1`; product `squeeze×Γ_fit = +0.574 OOM` (still over Planck) |
| S116-W1-HTILDE-RECON (workshop) | artifact-existence (no verdict line) | figure-multiplicity CLOSED (CC3 `2.38↔4.76`); magnitude CONDITIONAL on CF-S117 (`𝒩`-spread ≤ 0.1 OOM discriminator) |

These verdicts are authoritative; this synthesis scopes their joint falsifiable content and does not re-adjudicate them.

---

## IV. Structural Implications

### IV.1 Prediction-fit scorecard for the A_s magnitude leg

| # | Claim | Type | Free params | Testable prediction | Falsification criterion | BF |
|:--|:------|:-----|:------------|:--------------------|:------------------------|:---|
| 1 | **FLOOR inequality** `A_s > A_s^BD` (over the substrate Bunch-Davies vacuum) | genuine STRUCTURAL theorem; observationally near-inert | 0 | `A_s/A_s^BD = 1+2n_k = 1.00000061` (a **0.61 ppm** excess) | `A_s < A_s^BD` — but `A_s^BD` is a framework-internal reference, the excess is 0.6 ppm; **NULL practical falsifier** | ~1 (untestable) |
| 2 | **Over-production sign** `A_s^squeeze > A_s^Planck` (over the DATA, pre-filter) | genuine one-sided prediction; fork-robust | 0 | substrate squeeze exceeds observed on every route (40.9σ–451σ); `Γ ≤ 1` can only attenuate | substrate squeeze *below* Planck (no `Γ ≤ 1` could lift it) | ~2 (one-sided, big margin) |
| 3 | **Scale** `A_s^squeeze = O(10⁻⁸)` | genuine zero-param prediction | 0 | amplitude within ~1 OOM of `2.1×10⁻⁹`, both branches | squeeze off by ≫ 1 OOM either way | **3–5** |
| 4 | **Tilt-flatness** `α_s(primordial) ≈ 0` (NEW-1/OQ4) | genuine FALSIFIABLE prediction; near-future | 0 | exactly-zero primordial running (k-flat occupation ⇒ magnitude-only) | CMB-S4 measures `α_s` significantly ≠ 0 at the pivot (~0.002 reach) | TBD — register now |
| 5 | **Absolute normalization** `A_s = 2.1×10⁻⁹` | **NOT a stake-claim** | ≥1 fitted (Γ) **+** 1 unresolved (𝒩) | none currently | unfalsifiable while Γ fitted; current `Γ_fit` reproduces neither branch | — |

**The team-lead's question, answered.** *Is the falsifiable content ONLY the FLOOR inequality + tilt-flatness, with the absolute normalization NOT a stake-claim?* — **Essentially yes**, with two refinements:

- The genuine content is **{ scale (within ~1 OOM) + over-production sign + tilt-flatness }** — three zero-parameter items (rows 2–4), of which the **scale** is the most credit-worthy and the **tilt-flatness** the most observationally falsifiable.
- The **FLOOR inequality (row 1) is a structural sign theorem, observationally inert** at 0.6 ppm. It is genuinely permanent on three axes, but it is a self-comparison (squeeze vs its *own* Bunch-Davies vacuum), **not** the over-Planck statement, and **not** independently measurable. It should not be cited as the framework's observational A_s prediction; the over-Planck *sign* (row 2) is the observationally meaningful version.
- The **absolute normalization is NOT a stake-claim** — and not merely because Γ is fitted: it carries **two** free handles (fitted Γ + unresolved 𝒩 fork), and the present `Γ_fit = 0.512` reproduces the data on neither branch (II.4).

### IV.2 Does CF-S117 + a future substrate-Γ recover a genuine absolute-magnitude prediction?

**Conditionally yes — but it requires BOTH legs to close substrate-naturally, and neither has.** The absolute magnitude is recoverable-in-principle along a two-gate path:

1. **CF-S117-T-FOLD-EXIT-NORMALIZATION** returns `𝒩` regime-stable (spread ≤ 0.1 OOM) ⇒ the squeeze leg collapses to a single value (`+0.864` or `+0.196`), removing the 410.7σ fork (TD's predicted branch). If `𝒩` swings, the fork stands and the squeeze leg itself stays two-valued (mack's predicted branch — the third FAILed selector after CF-S114 and S115).
2. **A substrate-derived Γ** is found (the alternative-construction CF below) ⇒ the filter leg closes, and `A_s = A_s^squeeze × Γ` becomes a zero-parameter absolute prediction, falsifiable against Planck's `2.1×10⁻⁹` at ~1.4%.

**Both** must close substrate-naturally for the absolute normalization to become a stake-claim. Today **neither** is closed: the squeeze leg is fork-valued and the filter leg is fitted. So the absolute magnitude is **not foreclosed permanently** — it is **gated on two independent pre-registered computes** — but it is **not live** as a prediction now, and intellectual honesty requires the framework to carry it as such (the workshop and inventory already do: CF23 MAGNITUDE OPEN, Row #12 magnitude SCHEME-DEPENDENT, atlas-08 CF21 magnitude CF-S117-conditional).

### IV.3 Constraint-map update

- **CLOSED (one corridor)**: the near-horizon-barrier (`sech²`) exit-greybody as a substrate-derived filter (CF2 FAIL, regime-VALID — a clean boundary, not a defeat). Eliminating it strengthens the surviving corridors.
- **OPEN (squeeze leg)**: the 𝒩 transfer prefactor — a 410.7σ fork between two computed values (`+0.196` INV12-W3-5 PASS; `+0.864` S111), un-retired by any gate. CF-S117 decides (already minted; not relisted here).
- **OPEN + UNTESTED (filter leg)**: the moment-ratio / Connes-distance Γ construction — dimensionally admissible (`d_A=0`, even sector), not foreclosed by the parity wall, never scanned. **This is the EVOI-high move**: it is the deciding test for whether the absolute A_s magnitude can *ever* be a stake-claim, and its FAIL would be the move that promotes "irreducibly fitted" from a one-corridor boundary toward a structural wall.
- **PERMANENT (structural)**: the FLOOR sign theorem (`A_s/A_s^BD = 1+2n_k > 1`, 3-axis) and tilt-flatness (`α_s ≈ 0`, Mode-Independent Occupation). Genuine; the first observationally inert, the second observationally live.

### IV.4 Recommended mack falsifier-inventory scoping sub-row (mack is sole writer — fed, not landed here)

For the `Row #12` A_s surface, after `Row #12.audit-S116-W1-HTILDE-RECON`, a SCOPING sub-row recording the **falsifiable-content partition** of the A_s magnitude leg:

> **A_s magnitude leg — falsifiable-content scoping (post-CF2-FAIL).** The leg's genuine zero-parameter content is **{ scale within ~1 OOM (CFB1 PASS) + over-production sign `A_s^squeeze > A_s^Planck`, fork-robust + tilt-flatness `α_s(primordial) ≈ 0` (NEW-1/OQ4, register-now structural falsifier) }**. The **FLOOR inequality** `A_s > A_s^BD` is a 0.61 ppm self-comparison (3-axis PERMANENT, observationally inert) — NOT the over-Planck statement. The **absolute normalization `2.1×10⁻⁹` is NOT a stake-claim**: it carries one fitted O(1) Γ (CF2 FAIL) AND one unresolved 410.7σ fork (𝒩, CF-S117); the present `Γ_fit=0.512` reproduces the data on neither branch (box-delta product `+0.574 OOM` over Planck; required Γ=0.137 ≠ 0.512). σ-hygiene: "451σ above Planck" is a PRE-FILTER descriptive distance on the squeeze leg, NOT a framework tension (the filter is part of the chain). **CF2 scope**: "NOT substrate-derivable" is established for the near-horizon-barrier (`sech²`) family ONLY; the moment-ratio / Connes-distance Γ (`d_A=0`, even-morphism sector, NOT parity-foreclosed) is UNTESTED — fitted-Γ is a one-corridor boundary, not yet a wall (CF-S117-ALT-GREYBODY queued). Absolute magnitude recoverable iff BOTH CF-S117 (𝒩-stable) AND a substrate-Γ gate PASS.

---

## V. Carry-Forward Computations

> CF-S117-T-FOLD-EXIT-NORMALIZATION (the 𝒩 fork discriminator) and CF-S117-ROUTE-B-PW-SOCC (the S_occ Route-B-PW recompute) are **already minted in the workshop Wrap-Up** and are NOT relisted here. The genuine new computation this synthesis identifies is the alternative substrate-IS greybody construction.

### V.1 Alternative substrate-IS exit-greybody construction (the untested filter corridor)

- **What**: Compute the exit-greybody transmission `Γ_exit` via **two** alternative substrate-IS bridge maps that CF2 did NOT scan, both in the `d_A=0` even-morphism sector (so parity-admissible, unlike the `d_A=odd` LRD-T case):
  (1) **spectral-moment-ratio transmission** — `Γ = Res_W(s)/Res_W(s')` (a Wodzicki two-pole ratio at the relic band) or an `a_n^{Pauli-Villars}` moment ratio on the exit-horizon BdG sector;
  (2) **Connes-distance transmission** — `Γ` from the spectral-triple metric `d_C = 1/(λ_max − λ_min)` on the exit-horizon BdG sector.
  Test whether either reproduces the required attenuation **without** an in-band V0 placement (the S95 A2 sigmoid knob). The required `Γ` is set post-CF-S117 by the single-valued squeeze: `Γ_req = 10^{−OOM}` (= 0.137 if box-delta, 0.636 if slow-roll-MS); pre-CF-S117 the fitted comparator `Γ=0.511872` is used as a cross-check target.
- **Inputs**: `s95_w4_3_hawking_greybody_as.npz` (fitted comparator `Γ=0.511872`); `inv12_w3_4_greybody_from_bdg.npz` (exit-horizon BdG dispersion `ω_k`, substrate-derived `∫Γ=0.0363`); `s84_spectrum_cache_L12` (D_K `sector_evals` for the moment ratios and `λ_max`,`λ_min`); `canonical_constants.py` barrier scales `kappa_exit=47.6146`, `Delta_BCS=0.4642547`, `ω_q=2.0128`, `relic_rms=2.9253`; `cross-pillar-bridge-corpus §23.0(5)` (the `d_A=0` even-sector parity admissibility); optionally the CF-S117-T-FOLD-EXIT-NORMALIZATION output (single-valued squeeze OOM → `Γ_req`).
- **Gate**: NEW gate **CF-S117-ALT-GREYBODY** (`a_n` Mellin/Pauli-Villars regulator-pinned; PHONONIC; exit-horizon transmission as moment-ratio / Connes-distance bridge).
  - **PASS** (substrate-Γ found) iff either bridge map reaches `Γ_req` (or the `0.512` comparator) within `rel_tol ≤ 0.10` at a substrate-natural (non-in-band, non-fitted) scale ⇒ the filter leg closes; combined with a CF-S117 convention-blocked PASS, the absolute A_s magnitude becomes a zero-parameter prediction falsifiable vs Planck at ~1.4%.
  - **FAIL** (generalizes the irreducibly-fitted reading) iff BOTH bridge maps miss (best agreement `> 0.10`) at all substrate-natural scales ⇒ "NOT substrate-derivable" generalizes from the near-horizon-barrier family to TWO additional construction classes, promoting fitted-Γ from a one-corridor boundary toward a structural wall.
  - **INFO** iff one map reaches it and one misses ⇒ the filter is bridge-map-sensitive, not universally fitted (construction-dependent).
- **Effort**: 1 agent-session (2–3 hours). Two closed-form bridge-map evaluations on the existing L12 cache + exit-horizon BdG dispersion; no new spectrum build. Modest, single-script.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | A_s squeeze scale `O(10⁻⁸)`, within ~1 OOM, L_max POINT | PHONONIC | CFB1 PASS | Genuine zero-param scale prediction (BF 3–5); the credit-worthy core of the leg |
| 2 | Over-production sign `A_s^squeeze > A_s^Planck`, fork-robust | PHONONIC | genuine, 0-param | One-sided falsifiable; `Γ ≤ 1` forces it; survives CF-S117 |
| 3 | Tilt-flatness `α_s(primordial) ≈ 0` (NEW-1/OQ4) | PHONONIC | genuine, register-now | Most observationally-live A_s prediction; CMB-S4 ~0.002 reach |
| 4 | FLOOR inequality `A_s/A_s^BD = 1.00000061` (3-axis) | PHONONIC | PERMANENT, inert | Structural sign theorem at 0.6 ppm; NULL practical falsifier; ≠ over-Planck claim |
| 5 | Absolute normalization `A_s = 2.1×10⁻⁹` | PHONONIC | **NOT a stake-claim** | 1 fitted Γ + 1 unresolved 𝒩 fork; `Γ_fit` closes neither branch; recoverable iff CF-S117 ∧ CF-S117-ALT-GREYBODY both PASS |
| 6 | CF2 "NOT substrate-derivable" scope | GEOMETRIC | construction-scoped | Near-horizon-barrier corridor closed; moment-ratio / Connes-distance (`d_A=0` even sector, parity-admissible) UNTESTED |
| 7 | Workshop methodology (CF-S117 pre-registered fork discriminator, both sides pre-commit opposite predictions + falsifiers) | NON-PHONONIC (process) | exemplary | Venus-rule discipline: a label dispute converted into one computable gate; commend |
