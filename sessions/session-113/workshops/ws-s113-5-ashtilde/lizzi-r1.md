# WS-S113-5 AS-HTILDE — lizzi-spectral-functional-theorist, Round 1

**Workshop**: WS-S112-5 AS-HTILDE (S113 EVOI-frontier campaign) — "which leg sets the A_s amplitude floor: TD impulse-quench source vs LI H̃-divergence."
**Author / pole**: lizzi-spectral-functional-theorist — **Round 1, steelman Reading B (LI H̃-divergence is the rate-limiter that fixes the amplitude scale; the TD source rides on it).**
**One-line thesis**: The A_s amplitude scale is set by the late-inflation H̃-normalization because H̃ is the ONLY ledger factor that enters the power spectrum **squared** (`d ln A_s / d ln H̃ = +2`, exact), so its branch/scheme spread dominates every other leg by ~14×; the impulse-quench TD source supplies the FLOOR INEQUALITY (`A_s ≥ A_s^{BD}`, sign-locked, permanent) but not the SCALE — and because the H̃ leg is itself "route-unstable / >3 OOM, no convergence", the honest verdict is **floor-permanent / magnitude-OPEN**, which sharpens (does not resolve) the §EVOI.BF A_s liability.

> Substrate frame, binding throughout (`phononic-framing.md`): A_s is the squeezing modulus of the post-transit GGE-relic acoustic state. The arrow is `D_K eigenvalues → τ-flow rate at horizon-exit → H̃ (substrate-IS Hubble-analog, a spectral-moment ratio) → A_s = H̃²/(8π²ε)·(branch-shared legs)`. H̃ is NOT a metric Hubble rate in a container — it is the substrate-internal ratio `H̃² = (16/3π)·(a_0/a_2)·M_KK⁴/M_Pl_red²` (CC96 §4; S82 §IV.A.LI), the rate at which spectral complexity grows inside each point as a mode exits the acoustic horizon. The question "which leg sets the scale" is a question about which spectral functional / which moment-ratio carries the amplitude — exactly my domain.

---

## 0. What this workshop is, and what it is NOT (scope discipline)

Two PRIOR adjudications bound this one; I name them so I do not re-litigate settled axes.

1. **The FLOOR is permanent, three orthogonal axes, NOT in dispute** (`proven_1097`, `S_IC = 1 + 2n_k ≥ 1`; WS-AS-1 S110 LIZ2-1; `_rollup-as-wall §3`). `A_s ≥ A_s^{BD}` is forced by `n_k = |β_k|² ≥ 0` and `|α|²−|β|²=1`. Confirmed reference-state (inv-12 W1-2, `Δ=+1.04e-13>0`), families-index η-form (inv-12 W2-5, η≡0 EXACT), dynamical-Bogoliubov (inv-5/inv-6). **Neither pole re-opens the floor.** This is the TD source's genuine, permanent contribution — and I will concede it cleanly in §4.

2. **WS-AS-1 (S110) already settled a DIFFERENT axis** — the magnitude's epistemic type on the **intensive-vs-extensive** partition (Reading A physical-d.o.f. vs Reading B truncation-band). That workshop converged that the magnitude is SCHEME-DEPENDENT (the number floats; only the inequality is permanent). **The present workshop is orthogonal to that one**: it does not ask "is the magnitude a converged number or a truncation band," it asks **"which LEG ORIGINATES the scale the magnitude sits at — the TD impulse-quench source or the LI H̃-divergence."** I keep these axes separate (cross-corner conflation is exactly the failure `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality"` guards against).

So: floor = settled-permanent (TD-co-owned); magnitude-as-band-vs-number = settled-scheme-dependent (WS-AS-1); **magnitude-ORIGIN = this workshop.** My Reading B claim is about the origin of the SCALE, not the sign and not the truncation-softness.

---

## 1. The structural core: H̃ is the unique squared leg of the ledger

The UNIFIED-AS-79 ledger (S82 W1-2; the form every route shares) is:

```
A_s = [ H̃² / (8π²) ] · (1/ε_H) · F_amp · (1/c_sub) · f_conv · S_IC          (AS79)
```

The substitution chain that fixes the *leverage hierarchy* (mandatory `[SIGN]`, `math-scripts.md`; Sage-verified this round):

```
Claim: "H̃ sets the amplitude SCALE because it is the only leg entering A_s squared;
        every other ledger leg enters linearly (power 1), so H̃'s branch/scheme spread
        dominates the magnitude by the largest log-derivative in the ledger."

Step 1 (definitions):  A_s = H̃²·(8π²)⁻¹·ε_H⁻¹·F_amp·c_sub⁻¹·f_conv·S_IC      [AS79, S82 W1-2]
Step 2 (log-derivatives, each leg):
        d ln A_s / d ln H̃    = +2     [H̃ appears as H̃²]            ← UNIQUE: power 2
        d ln A_s / d ln ε_H   = −1     [1/ε_H]
        d ln A_s / d ln F_amp = +1
        d ln A_s / d ln c_sub = −1     [1/c_sub]
        d ln A_s / d ln f_conv= +1     [f_conv = (M_KK/M_Pl)², the keystone leg]
        d ln A_s / d ln S_IC  = +1     [the floor leg — this is the TD source's slot]
Step 3 (substitute the branch spreads each leg actually carries):
        H̃   spread: TD/LI = 2.3798 OOM   (H_tilde_canonical_TD=5.9076e-3 vs H_tilde_canonical_LI=2.46411e-5)
        ε_H  spread: tree/one-loop = 0.3351 OOM   (0.01 vs 0.02163)
Step 4 (A_s-space leverage = spread × |log-derivative|):
        H̃-leg  A_s leverage = 2 × 2.3798 = 4.7595 OOM        [Sage-exact this round]
        ε_H-leg A_s leverage = 1 × 0.3351 = 0.3351 OOM
        ratio (H̃-leverage / ε-leverage) = 14.205                          [Sage]
Step 5 (direction read-off): the H̃ leg carries 14× the A_s-magnitude leverage of the
        next-most-leveraged scheme leg. The magnitude SCALE is therefore set by H̃.
Conclusion: H̃ is the rate-limiter of the A_s amplitude scale. (AS79's only squared leg.)
```

**This is the lizzi-signature reading made quantitative.** What survives all spectral-functional choices is the *sign* (the floor, the S_IC leg). What carries the *scale* is whichever leg has the largest log-derivative — and that is uniquely H̃, because the Mukhanov-Sasaki power spectrum is quadratic in the horizon-exit expansion rate. The TD impulse-quench source enters through `S_IC = 1 + 2n_k` at power **+1**; H̃ enters at power **+2**. **The leg with the higher power sets the scale; the lower-power leg rides on it.** That is the precise sense of "the TD source rides on the H̃-divergence."

The S82 INV12-W3-5 reconcile script states this in its own words (lines 256–266): *"the fixed legs are H̃-INDEPENDENT; the H̃ divergence passes UNCOMPENSATED into A_s as H̃² (CC3 = +2). This is why CF21 IS the A_s rate-limiter."* The framework's own machinery already names H̃ the rate-limiter — Reading B is reading the ledger as it was built.

---

## 2. What the H̃-divergence IS, structurally (the late-inflation Mukhanov-Sasaki normalization)

H̃ is not an auxiliary input; it is **the boundary value the Mukhanov-Sasaki mode equation freezes into the observable**. Substrate-native form (S82 §IV.A.LI; CC96 §4):

```
A_s = (k³/2π²)·|u_k/z|²_{k=aH}                          [power spectrum at acoustic-horizon exit]
z = a·√(2ε)·M_Pl_red                                     [Mukhanov variable]
⇒ A_s = H̃²(N_k)/(8π²·ε(N_k))   ,  N_k = horizon-exit epoch
H̃²(τ) = (16/3π)·[a_0(τ)/a_2(τ)]·M_KK⁴/M_Pl_red²         [H̃ IS a spectral-moment ratio, CC96]
```

The decisive structural facts:

- **H̃ is the amplitude-SETTING boundary condition of the mode equation.** The frozen spectrum `|u_k/z|²` carries the value of H̃ **at the WKB-to-frozen transition** (Parker 1969; Birrell-Davies §3.4 eq 3.72; Mukhanov-Feldman-Brandenberger 1992 §10.3). The mode oscillates with WKB amplitude `∝1/√k` until horizon exit; **only the horizon-exit H̃ survives in the frozen amplitude.** So H̃ is not "a correction" to a TD-set amplitude — H̃ IS the quantity the freezing operation reads off into A_s. The TD Bogoliubov coefficients set *how far above Bunch-Davies* the state sits (the `S_IC` multiplier); H̃ sets *what the Bunch-Davies amplitude itself is at the freezing epoch* (the `H̃²/(8π²ε)` carrier). The carrier is the scale; the multiplier rides on it.

- **H̃ is itself a spectral-functional object — the `a_0/a_2` moment ratio.** This is why it is MY domain and not (solely) the transit-dynamics domain. H̃² = (16/3π)·(a_0/a_2)·M_KK⁴/M_Pl_red². The *value* of H̃ depends on **which regularization weights `a_0` and `a_2`** — exactly the spectral-functional pluralism I track. The S82 OOM §III.B / Observation 6.3 makes this explicit: the LI Path-B reading splits `H̃_B^SDW / H̃_B^Zubarev = 181` (= 2.26 OOM) — **the SAME bare-vacuum-vs-zero-point-subtracted split that is the CC problem, surfacing in H-form rather than Λ-form.** The H̃ that sets A_s carries the unresolved a_0/a_2 functional choice. That is the structural reason the amplitude scale is unpinned: it inherits the CC-sector functional freedom through the `a_0/a_2` ratio.

- **The TD source does not change H̃; it rides through `S_IC`.** In AS79, the impulse-quench Bogoliubov output enters EXCLUSIVELY through `S_IC = 1 + 2n_k` (and, via the SHAPE, through the tilt, not the normalization scale — S57/S62 Mode-Independent Occupation makes `|β_k|²` mode-independent, so the produced occupation is a constant `n̄` that multiplies, it does not set, the carrier amplitude). `S_IC` enters at power +1; for the framework's locked relic, `S_IC = 1 + 2n̄` is an O(1) multiplier. **An O(1) power-+1 multiplier cannot set a scale that a power-+2 carrier spanning 4.76 OOM controls.**

**Phononic translation (substrate-first):** the post-fold spectral-complexity relaxation freeze-dries the acoustic mode at the horizon-exit epoch; the amplitude it freezes in is set by the `a_0/a_2` spectral-moment ratio at that epoch (= H̃²). The impulse-quench transit determines that the relic sits *above* its Bunch-Davies floor (n_k > 0 ⇒ S_IC > 1) — the SIGN. But *how high the floor itself is* is the H̃ carrier, which is the spectral-moment-ratio normalization. Sign from the transit; scale from the moment ratio.

---

## 3. Why this makes the magnitude OPEN, not pre-registrable (the honest reading)

Here I engage the second half of the adjudication question head-on: *is the magnitude pre-registrable via the H̃ leg, or is A_s_FW = 1.537e-08 a floor-only statement?*

**Reading B's honest answer: A_s_FW = 1.537e-08 is a floor-anchored POINT on ONE leg (the impulse-quench S_IC slot at one functional), NOT a pre-registered magnitude — because the SCALE-setting leg (H̃) is route-unstable across a 4.76-OOM A_s span with no convergence criterion that selects a value.** The chain:

1. The amplitude scale is the H̃-carrier (§1, §2): `A_s ∝ H̃²`, the unique squared leg, 14× the leverage of any other.
2. H̃ is route-unstable: the TD/LI branches span 2.3798 OOM (Sage-exact), → **4.7595 OOM in A_s** under CC3. The S82 W1-1 divergence-chase workshop found this gap is **structural, not a scheme artifact removable by reconciliation** (Observation 6.4: even reconciling the ε convention leaves ≥2.2 OOM; the static-vs-dynamic functional split is the genuine physics disagreement). §EVOI.BF independently flags A_s as *"route-unstable, >3 OOM, no convergence."*
3. INV12-W3-5 *selected* Branch-A TD/zeta as canonical horizon-exit (A_s = 3.2994e-9, 1.57× Planck, PASS-F2) and ruled out Branch-B LI (A_s FAIL-GT15). **But that selection is a horizon-EPOCH argument (the Mukhanov-Sasaki "evaluate at k=aH, N_pivot=55" semantics), not a functional-CONVERGENCE argument.** It picks WHICH epoch H̃ is read at; it does NOT pin the `a_0/a_2` functional weighting that sets H̃'s VALUE at that epoch. The 181× SDW/Zubarev Path-B split (the CC-sector functional freedom) is untouched by the epoch selection. So even the "selected" Branch-A H̃ carries an unpinned functional choice in its `a_0/a_2` content.
4. Therefore the amplitude scale is **bounded but not predicted**: bounded below by the floor (S_IC ≥ 1, permanent); its SCALE inherited from a route-unstable spectral-moment-ratio carrier whose functional weighting is the open CC-sector choice. `A_s_FW = 1.537e-08` is the impulse-quench number at ONE functional (the S111 AS3a frozen-occupation normalization) — defensible as a representative point, but it is **+0.864 OOM over Planck** (Sage: A_s_FW/Planck = 7.318) and sits inside a 4.76-OOM scheme band on the carrier leg. **Pinning it as "the" magnitude would be functional-shopping a single point out of a route-unstable band** — exactly the move `epistemic-discipline.md §"Source Reconciliation"` and my own ledger forbid.

**This is the §EVOI.BF liability sharpened, not dissolved.** §EVOI.BF says A_s is "route-unstable, >3 OOM, no convergence" — Reading B explains WHY structurally: the amplitude scale rides on the unique squared leg (H̃), that leg is a spectral-moment ratio carrying the unresolved CC-sector functional choice, and no convergence criterion selects its value (the branch selection is epoch-based, not functional-based). The honest verdict Reading B drives toward: **FLOOR-PERMANENT / MAGNITUDE-OPEN**, with the magnitude's openness localized to the H̃-carrier's functional freedom (the `a_0/a_2` ratio), which is the CC problem in H-form (S82 Obs 6.3). That is a *stronger, more precise* statement than "route-unstable" — it names the rate-limiting leg and its functional origin.

---

## 4. Engaging the strongest threat: the TD impulse-quench source genuinely setting the floor with H̃ sub-dominant (Reading A)

I steelman Reading B, but I do not strawman the opponent. The strongest Reading-A case is genuinely strong, and here it is, fairly stated, with my honest response.

**Reading A's best case** (transit-dynamics pole, as I'd build it for them): The impulse-quench Bogoliubov source (AS3a, S111, `A_s_FW = 1.537e-08`) is a *converged physical amplitude* — locked `{β_k}`, Floquet-frozen (WS-FLOQUET=DEAD, relic NOT re-pumped), L-saturated for the shape (S57/S62). It is computed end-to-end from the transit dynamics with no free knob, and it lands +0.86 OOM over Planck — a *narrow, sign-definite over-production*. The H̃-divergence, by contrast, is a 4.76-OOM *spread* that the framework already RESOLVED by selecting Branch-A (INV12-W3-5 PASS: single canonical reading namable, `divergence_is_structural=False`). So the H̃ "divergence" is a closed ledger/figure reconciliation, while the impulse-quench number is a live, locked physical prediction. The floor scale IS the impulse-quench |β_k|²; H̃ is a sub-dominant, already-reconciled correction.

**My honest response (three points; the first two CONCEDE real ground):**

- **CONCEDE: the impulse-quench source is the cleaner, more locked computation, and it sets the FLOOR (the inequality and its realization).** WS-FLOQUET=DEAD genuinely forecloses re-pumping; the `{β_k}` are a frozen output; S_IC = 1 + 2n_k is a locked O(1) multiplier. I co-credited this in `_rollup-as-wall §3` and I credit it again. **Reading A is RIGHT that the impulse-quench source realizes the floor as a concrete produced state.** Where I disagree is the inference *floor ⇒ scale*: realizing the inequality `A_s ≥ A_s^{BD}` (the +1-power S_IC leg) is not the same as setting the amplitude SCALE (the +2-power H̃ carrier). The impulse-quench source pins the multiplier; it does not pin the carrier.

- **CONCEDE-AND-REFRAME: INV12-W3-5 did select Branch-A — but it did NOT close the magnitude.** This is the crux of my rebuttal, and I state it precisely so R2 can test it. INV12-W3-5's PASS is a **horizon-EPOCH** selection (Mukhanov-Sasaki: read H̃ at k=aH, N_pivot=55, which rules out the Branch-B LI *epoch* reading). It is NOT a **functional-CONVERGENCE** result. The script's own §5 says Branch-A is "the substrate-NATIVE Mukhanov-Sasaki horizon-exit reading" — a statement about WHICH EPOCH, not about WHICH FUNCTIONAL weights the `a_0/a_2` ratio that gives H̃ its value. The 181× SDW-vs-Zubarev Path-B split (S82 Obs 6.3) — the CC-sector functional freedom inside H̃ — is *orthogonal* to the epoch selection and remains open. So "the divergence is resolved" is true for the EPOCH axis (Branch-A vs Branch-B) and FALSE for the FUNCTIONAL axis (which a_0/a_2 weighting). The amplitude SCALE inherits the latter. Reading A's "already-reconciled" claim conflates the epoch selection with a functional pin.

- **PUSH BACK: the impulse-quench number's apparent locked-ness is on the +1 leg; the scale uncertainty lives on the +2 leg it does not control.** A_s_FW = 1.537e-08 is locked *as an S_IC-slot evaluation at one functional*. But the same AS79 ledger that produces it carries H̃² at power +2 spanning 4.76 OOM. The impulse-quench computation does not *set* H̃ — it inherits whatever H̃ the ledger uses (S111 AS3a uses the substrate-natural frozen-occupation normalization; INV12-W3-5 uses Branch-A TD). **The number is locked given a choice of H̃-carrier; it is not locked across the route-unstable carrier.** That the impulse-quench *band* is narrow (+0.86 OOM) is a statement about the S_IC multiplier's stability, NOT about the carrier's. Reading A reads the multiplier's narrowness as the scale's narrowness; they are different legs.

**Where the threat is genuinely live (honest):** if R2 can show that the impulse-quench normalization is *independent of* the H̃-carrier — i.e., that AS3a computes A_s from `|β_k|²` *directly* (a count/KZ-volume normalization, `A_s = |β_k̂|²/(2π²)` with KZ-volume `ξ_KZ³`) WITHOUT routing through `H̃²/(8π²ε)` — then the impulse-quench source would be an INDEPENDENT amplitude determination, not a rider on H̃, and Reading A wins the origin question. That is the strongest Reading-A move and I flag it as the decisive test (see §6). My anticipatory answer: even a direct `|β_k|²/(2π²)` normalization is the *same* GGE-relic amplitude that the Mukhanov-Sasaki form `H̃²/(8π²ε)·S_IC` expresses — the two are dual expressions of one observable (`_rollup-as-wall §3` netted them as the SAME floor through two functionals), and the *scale* of `|β_k|²` is itself set by the transit's energy injection, which is governed by the same `a_0/a_2`-driven H̃(τ) trajectory through the fold. But whether the AS3a normalization *operationally* breaks the H̃-dependence is the empirical question R2 must settle, and I will not pre-judge it.

---

## 5. Sub-verdict map (what each pole owns, on Reading B's reading)

| Object | Power in AS79 | Owner | Status |
|:--|:--|:--|:--|
| FLOOR inequality `A_s ≥ A_s^{BD}` (S_IC ≥ 1) | +1 (S_IC slot) | **TD impulse-quench source** | PERMANENT, 3 axes — TD's genuine win |
| Amplitude SCALE carrier `H̃²/(8π²ε)` | **+2 (H̃)** | **LI H̃-divergence** | route-unstable, 4.76 OOM, OPEN |
| Epoch selection (which N_k reads H̃) | — | INV12-W3-5 (Mukhanov-Sasaki) | RESOLVED: Branch-A TD/zeta |
| Functional selection (which a_0/a_2 weights H̃) | — | **OPEN (CC-sector, 181× SDW/Zub)** | the rate-limiter's residual freedom |
| Magnitude number `A_s_FW=1.537e-08` | — | S111 AS3a (one functional) | floor-anchored POINT, not pre-registered |

Reading B's claim in one row: **the leg with the higher power (H̃, +2) sets the scale; the lower-power leg (S_IC, +1) realizes the floor and rides on the carrier. The magnitude is open because the carrier's functional weighting (the CC-sector a_0/a_2 choice) is unpinned.**

---

## 6. (i) Honest current lean and (ii) the single most decisive consideration

**(i) Honest current lean.** I lean **Reading B for the SCALE-ORIGIN question and FLOOR-PERMANENT / MAGNITUDE-OPEN for the pre-registrability question** — but with an explicit, important boundary: I do NOT claim the H̃-divergence is the rate-limiter of the *floor* (it isn't — the floor is the S_IC leg, TD-owned, permanent). I claim it is the rate-limiter of the *amplitude scale*, which is the quantity "the A_s magnitude" actually refers to. The structural fact carrying my lean is leg-power: H̃ enters A_s squared, alone among the ledger factors, with 14× the magnitude-leverage of the next leg; the framework's own INV12-W3-5 script names H̃ "the A_s rate-limiter" for exactly this reason. The honest concession that tempers the lean: the TD impulse-quench source is the more locked computation and genuinely realizes the floor — so the TD pole is not wrong about its object (the floor); it is wrong only if it claims the floor-realization *is* the scale-determination. My lean is therefore a CLEAN SPLIT: **floor ← TD (permanent); scale ← H̃ (open)** — which is itself the structural verdict I'd push the workshop to pin, rather than a winner-take-all on one pole.

**(ii) The single most decisive consideration.** *Does the AS3a impulse-quench normalization determine A_s INDEPENDENTLY of the H̃-carrier, or does it route through `H̃²/(8π²ε)`?* If AS3a's `A_s = |β_k̂|²/(2π²)` (KZ-volume normalized) is an independent amplitude determination that does NOT inherit the route-unstable H̃, then the TD source sets the scale and Reading A wins the origin question (H̃ becomes a consistency cross-check, not the carrier). If AS3a is a dual expression of the SAME GGE-relic amplitude whose scale is governed by the `a_0/a_2`-driven H̃(τ) transit trajectory — as the `_rollup-as-wall §3` "same floor through two functionals" net suggests — then the impulse-quench number rides on the H̃-divergence and Reading B wins. **This is a concrete, decidable test** (compare the AS3a normalization chain against the AS79 `H̃²/(8π²ε)·S_IC` chain; check whether the AS3a `|β_k̂|²` scale is itself a function of the fold-transit H̃(τ) or an H̃-independent count). It is the one consideration that flips the verdict, and it is exactly the kind of "which functional carries the observable" question my methodology exists to settle. I commit to opening R2 on it.

---

*End lizzi-spectral-functional-theorist Round 1 (steelman Reading B). FLOOR conceded permanent (TD-owned, 3 axes); SCALE argued H̃-carried (the unique +2 leg, 14× leverage, Sage-verified 4.76-OOM A_s span); magnitude argued OPEN (functional freedom in the a_0/a_2 carrier = CC-in-H-form). Verdict and opponent's section deliberately not written. Decisive test for R2 flagged: is AS3a H̃-independent or H̃-routed.*
