# S116-W1-HTILDE-RECON — H̃-branch OOM-figure Reconciliation Workshop

**Date**: 2026-06-27
**Gate**: `S116-W1-HTILDE-RECON` (gate_type: workshop, Wave 1, Session 116)
**Format**: 2-agent adversarial adjudication, 3 rounds, sequential turns on this shared document
**Agents**: `transit-dynamics-theorist` (TD/Bogoliubov side — argues **CONVENTION-BLOCKED**) vs `mack-cosmic-bridge` (observational A_s side — argues **PHYSICS-BLOCKED**)
**Closure**: artifact-existence (NO verdict line, per `wave-classification.md §M1`). This document must end with R1/R2/R3 filled + a `## Structural Verdict` pinning ONE OOM figure (declared space) + the convention-blocked|physics-blocked fork resolved + Wrap-Up.

## Adjudication Question

> Given INV12-W3-5 ALREADY reconciled 2.38 (H̃-space) and 4.76 (A_s-space) as CC3-conjugate (A_s ∝ H̃², factor 2; the "4.56" was a stale rendering of the live 4.76), and given the box-delta route gives only +0.864 OOM (A_s_FW=1.5367e-8) while S115 declared the 1.259-OOM route-spread a REAL sudden↔adiabatic axis (PLURALISM, no collapse, min 0.628 OOM):
>   (a) Is the H̃-branch TD/zeta figure (A_s=3.2994e-9, +0.196 OOM) a SEPARATE physical regime-point on the S115 sudden↔adiabatic axis, or the SAME Bogoliubov physics as the box-delta route under a different IC/normalization convention (Zubarev vs BD)?
>   (b) Does the 3.15-OOM Route-B-Peter-Weyl figure (AMPLITUDE-NORM-66) reconcile with the 4.76 A_s-space CC3 figure, or is it a third, genuinely-distinct route?
>   (c) THE FORK: is A_s closure CONVENTION-blocked (a canonical horizon-exit reading selects ONE OOM figure) or PHYSICS-blocked (the substrate genuinely does not single out one A_s absent a regime-selection principle)?
>
> Deliverable: ONE pinned canonical OOM figure (with its declared space: H̃ or A_s) + the convention-vs-physics verdict + which of the three figures (if any) is retired.

## Competing Positions (each first-principles-backed; the workshop derives which is correct)

- **TD side (`transit-dynamics-theorist`) — CONVENTION-BLOCKED.** The 2.38/4.76/3.15 figures are normalization-convention images of ONE Bogoliubov divergence: 2.38↔4.76 is the exact CC3 factor-2 (deg(T_BZ→pivot)=+2 NON-SCALAR sets the H̃↔A_s power), and the box-delta +0.864 is the substrate-natural (ξ_KZ) horizon-exit reading. S115 "PLURALISM" is a selector-FAIL on a SPECIFIC (maxent+Connes-diam) selector, NOT a proof that no canonical horizon-exit reading exists. Pick the canonical reading → one figure emerges; closure is convention-blocked.
- **Mack side (`mack-cosmic-bridge`) — PHYSICS-BLOCKED.** Planck A_s=(2.10±0.03)e-9 is a tight datum; the routes predict 3.3e-9 / 1.5e-8 / 7e-8 — physically distinct, multi-σ apart. S115 showed no substrate principle collapses them (min 0.628 OOM ≫ 0.1 band). The sudden↔adiabatic spread is a real physical axis (which transit regime the CMB samples); calling it "convention" hides a genuine prediction gap. The "canonical horizon-exit reading" is itself a physics choice, not a free convention.

**NUMERIC STAKES**: 2.38 (H̃-space) | 4.76 (A_s-space, =2×2.38) | 3.15 (Route-B-PW) | +0.864 (box-delta canonical) | +0.196 (TD/zeta) | axis [+0.196,+1.527], spread 1.259 OOM.

**SUBSTRATE FRAMING**: A_s IS the GGE-relic acoustic squeezing modulus of the post-transit produced state; the lab measures A_s IN a CMB container. The OOM "gap" is the substrate's overproduction relative to that container, NOT an inflaton-normalization mismatch.

**Sources** (read all before writing):
1. `computations/investigation-12/inv12_gate_verdicts.txt` — INV12-W3-5-CF21-HTILDE-RECONCILE PASS (cc3=2.0; 2.38 H̃-space / 4.76 A_s-space; 4.56=stale)
2. `computations/session-110/s110_cf_b1_transit_ps_promote.npz` — two-leaf build + amplitude pair (inv5 +0.86 / inv6 +1.455)
3. `computations/session-111/s111_cf_as3a_impulse_quench.npz` — A_s_FW=1.5367e-8 box-delta magnitude (+0.864 OOM)
4. `computations/session-115/s115_gate_verdicts.txt` — S115-AS-NEWAXIS-SELECTOR PLURALISM (spread 1.259, no collapse 0.628)
5. `sessions/framework/Atlas/atlas-08-open-questions.md` — §VIII CF21 (atlas carries un-reconciled 2.38 vs 4.56)
6. `sessions/framework/registry/constraint-mega-matrix.md` — AMPLITUDE-NORM-66 FAIL (3.15 OOM Route-B Peter-Weyl)

---

## Round 1 — Opening Positions (steelman your assigned side)

### R1 · transit-dynamics-theorist — CONVENTION-BLOCKED steelman

**Thesis.** The figures {2.38 (H̃-space), 4.76 (A_s-space), 3.15 (Route-B-PW)} are not three measurements of three quantities. They are normalization-convention images of a SINGLE Bogoliubov object: the squeezing modulus |β|² of the GGE relic produced by ONE impulsive transit. The substrate IS one acoustic squeezing power; the lab reads it IN a CMB container at one definite overproduction. Fix the regime-forced horizon-exit reading and the figures collapse to a single number — `A_s = +0.864` OOM above Planck — and the apparent `[+0.196, +1.527]` spread is exposed as a stack of convention choices (IC scheme × mode-function/regime × spectral functional × scale normalization), not a physical axis of distinct CMB-sampled transits. The closure is blocked by which convention layer one fixes, not by a substrate failure to single out A_s.

**The +2 backbone (one factor of 2, three guises, provably the same).** Everything turns on a single quadraticity. The UNIFIED-AS-79 decomposition (S82 W1-2, canonical) is

  **(1)**  `A_s = (H̃² / 8π²) · (1/ε_H) · F_amp · c_sub⁻¹ · f_conv · S_IC`.

At a fixed transit profile every factor except `H̃²` is a transit-kinematic / fold-geometry quantity — `ε_H ≈ 0.0219`, `F_amp` (3PI backreaction, S82 W3-5), `c_sub` (Mellin-weight, S79), `f_conv` (KK hierarchy), `S_IC` (occupation) — all set by `τ_fold = 0.190` and the fold spectral geometry, none carrying H̃-dependence. The CC3 substitution chain:

```
Step 1:  A_s = (H̃²/8π²)·g,   g ≡ (1/ε_H)·F_amp·c_sub⁻¹·f_conv·S_IC,   ∂g/∂H̃ = 0      [(1) + fixed-profile]
Step 2:  ln A_s = 2 ln H̃ + ln(g/8π²)                                                    [log of (1)]
Step 3:  d(ln A_s)/d(ln H̃) = 2                                       [∂g/∂H̃=0; CC3, machine-ε S82+]
Step 4:  two readings differing only in H̃ (TD vs LI):  Δ(ln A_s) = 2·Δ(ln H̃)  ⇒  OOM_A_s = 2·OOM_H̃
Step 5:  2.38 (H̃-space TD−LI)  ⇒  4.76 (A_s-space)         [INV12-W3-5: oomH=2.3798, oomAs=4.7595, cc3=2.000000]
```

So **`4.76 = 2 × 2.38` EXACTLY** (`2 × 2.3798 = 4.7596` vs `4.7595`, machine ε). This is not my claim to prove — it is an ALREADY-PASSED gate (`INV12-W3-5-CF21-HTILDE-RECONCILE`, PASS). The atlas "4.56" is a stale rendering of the live `4.7595` CC3 image (the gate states it verbatim: `fig456 = As-space-stale-live4.76`). 2.38 and 4.76 are ONE divergence in two spaces; the physics-blocked side may not count them as two.

The same `+2` appears twice more and is the **same** `+2`:
- **Transport degree** `deg(T_BZ→pivot) = +2`, NON-SCALAR (S93 W7-1; S110 npz `deg_T_BZ_pivot = 2`) — the map carrying the substrate/BZ squeezing to the CMB-pivot curvature amplitude across 54.04 decades is degree-2.
- **Power-spectrum quadraticity**: `A_s ≡ |amplitude|² ~ |β_k|² ~ |ζ_k|²`. A power spectrum is by definition quadratic in the mode function; `ζ_k|_horizon ∝ H̃` ⇒ `A_s ∝ H̃²`.

These are not three coincidental 2's. A_s is quadratic in the produced mode amplitude (definition); the amplitude is linear in H̃ at horizon exit (mode equation); hence `A_s ∝ H̃²` (CC3); and the BZ→pivot transport inherits that quadratic degree (`deg T = +2`). **ONE factor of 2 — "the power spectrum is |amplitude|²" — wearing three hats.** Any "extra" gap that is really the factor-2 image of an H̃-reading is convention, by this identity.

**Sub-(a): TD/zeta `+0.196` is the SAME Bogoliubov physics under a different IC/normalization convention — not a separate regime-point.**

There is ONE transit, and it is impulsive: `H·dt_transit = 0.663 < 1`, Mach 13.75, `dt_transit = 1.13e-3 M_KK⁻¹` (the supersonic acoustic white hole). The regime is a property of the transit, not of the reader; a single physical event is not simultaneously "slow-roll-sampled" and "sudden-sampled."

The TD/zeta route (`A_s = 3.2994e-9`, `+0.196`, UNIFIED-AS-79 Branch-A) reads the produced state through the slow-roll Mukhanov-Sasaki mode function with the Zubarev IC on the H̃ carrier. The box-delta route (`A_s_FW = 1.5367e-8`, `+0.864`, S111-CF-AS3a) reads the SAME produced GGE relic through the sudden Bogoliubov `A_s = |β_k̂|²/(2π²)` at the Kibble-Zurek normalization `N_norm = ξ_KZ³`, `k̂ = 1/ξ_KZ = 53.30` (verified: `ξ_KZ³ = 6.6024e-6 = N_norm` exactly; `|β_k̂|²/(2π²) = 1.5367e-8 = A_s_FW` exactly). Same state, two conventions — `(slow-roll-MS, Zubarev, H̃-carrier)` vs `(sudden, ξ_KZ-scale)`. The `+0.196 → +0.864` difference is the convention difference, NOT a different physical regime.

That two conventions read the same observable across a 54.04-decade gap is exactly what `deg(T_BZ→pivot) = +2` encodes: fold-scale `|β|²` and pivot-scale `A_s` are connected by the degree-2 transport — the same `+2` as CC3 — i.e. two ends of one transport of one produced state. The internal TD/zeta check confirms the threading inside the single route: `A_s/A_s^Planck = 1.5712` while the `H̃`-ratio `= 1.2532 ≈ √1.5712 = 1.2535` (INV12-W3-5 `Hratio_TD_base`). Again A_s-ratio = (H̃-ratio)² — CC3 within one route. **(a): SAME physics, different convention.** The "sudden↔adiabatic axis" exists as a mathematical family of readings of one state; it is not a family of physical transits.

**Sub-(b): 3.15 (Route-B-PW) is a superseded, pre-CC3 legacy figure diagnosed at S66 as a wrong-spectral-functional artifact — RETIRE it; do not count it as a live third route.**

`AMPLITUDE-NORM-66` is an S66 result — it predates BOTH the UNIFIED-AS-79 decomposition (S79–S82) AND the CC3 identity. Its own diagnosis (constraint-mega-matrix): *"Normalization crisis: right ratios, wrong amplitudes … S_fold (vacuum spectral action) used where S_occ (occupied-state) needed."* The 3.15-OOM gap is the Peter-Weyl spectral-action route's A_s normalized against the VACUUM functional `S_fold` where the OCCUPIED-state `S_occ = S_IC·S_fold` was required (`S_IC = 1 + 2n_k ≥ 1`, INV12-W1-2 `K_sub = (1+2n_k)/1` structural). Using the wrong spectral functional is a convention error, not a distinct physical route. The same S66 ledger explicitly queued its own supersession: *"TRANSIT-PS-67 may resolve [A_s normalization 3.15 OOM] simultaneously."* TRANSIT-PS-67 is now realized as the CC3/box-delta transit picture (S110-CF-B1 TRANSIT-PS-67 promotion). So 3.15 is convention (wrong functional) AND legacy (pre-CC3) on two counts — not a route co-equal with 4.76. **Disposition: RETIRE.** The burden falls on the physics-blocked side: exhibit an `S_occ`-corrected, CC3-threaded Route-B-PW recompute and show it is genuinely distinct from the box-delta/CC3 image. Absent that, 3.15 is a wrong-functional shadow of the one object.

**Sub-(c) — THE FORK: a regime-canonical horizon-exit reading EXISTS; S115 PLURALISM is a selector-FAIL on a specific pair, not a no-canonical-reading proof. ⇒ CONVENTION-BLOCKED.**

The canonical reading is not an aesthetic pick; it is forced by the regime:
1. The transit is impulsive (`H·dt < 1`). The adiabatic theorem requires `ω'/ω² ≪ 1`; at the fold this FAILS. Slow-roll and adiabatic formulas are therefore applied OUTSIDE their stated regime when used to read THIS transit (a regime-of-validity violation, not a free choice).
2. In the impulsive limit the SUDDEN approximation is EXACT, not approximate: S100b box+delta sudden Bogoliubov returns `var_Nseg−1 = 6e-10`, Schmidt-Eq.75 match `1.6e-6`, TM-vs-Radau `7e-12`. The sudden reading carries no truncation error.
3. The normalization is forced by the one substrate-natural scale — the Kibble-Zurek freeze-out length `ξ_KZ` (`N_norm = ξ_KZ³`, `k̂ = 1/ξ_KZ`). This is the quench healing length, not a tunable knob.

Steps 1–3 single out ONE reading: the sudden Bogoliubov `|β_k̂|²/(2π²)` at `ξ_KZ` normalization — the box-delta `+0.864`. (Note the two framework "canonical" labels are not competitors but settlements on different convention sub-axes: `INV12-W3-5` settles the IC-scheme axis — Zubarev beats LI, the latter FAIL-GT15 at `−4.56` — while the regime physics settles the dynamics axis — sudden beats slow-roll/adiabatic. `INV12-W3-5`'s "TD/zeta canonical" reads the correct IC through a slow-roll mode function that is out-of-regime for an impulsive transit; the dynamics axis corrects the mode function to sudden, moving the reading into the box-delta family.)

Now read `S115-AS-NEWAXIS-SELECTOR` (FAIL, PLURALISM) correctly. It tested maxent and Connes-diameter and found they do not collapse the spread (`min_collapse_dist = 0.628 OOM ≫ 0.1`). But its partition is diagnostic: **maxent** — the Jaynes maximum-entropy occupation given the produced `⟨N⟩ = 2.08e-5`, `⟨E⟩ = 2.50e-4` — lands at `A_s = 1.4006e-8` (`+0.824`), coincident with the IMPULSE/sudden end (0.040 away). **Connes-diameter** — a spectral-geometry NORMALIZATION `d_C = 1/(λ_max−λ_min)`, not a dynamical selector — lands on Parker, the adiabatic end. So the dynamical/statistical principle lands on the regime-correct sudden end; only the metric-normalization principle lands on the regime-wrong adiabatic end. **S115's own result SUPPORTS convention-blocked**: the entropy-maximizing occupation agrees with the regime-forced sudden reading; the spread to Parker is the adiabatic convention, not a transit the CMB samples.

S115 FAILed because it searched for a selector among `{impulse, UNIFIED, Parker}` treated as co-equal physical candidates. They are not co-equal: the regime is sudden, so impulse is canonical and UNIFIED (slow-roll) / Parker (adiabatic) are out-of-regime conventions. A selector-FAIL on `(maxent, Connes-diameter)` over an artificially co-equal set is not a proof that no canonical reading exists — fix the regime FIRST and the candidate set collapses to one BEFORE any selector is applied. Hence **the fork resolves CONVENTION-BLOCKED.**

**Honest scope (regime-of-validity declaration).** I separate airtight from strongest-available, as a transit theorist must:
- **AIRTIGHT** — `2.38 ↔ 4.76` CC3-conjugacy: an ALREADY-PASSED gate (INV12-W3-5, `cc3 = 2.000000`). Settled, not contestable.
- **STRONG (burden-shifting)** — 3.15 as a wrong-functional (`S_fold` vs `S_occ`), pre-CC3 legacy figure: by S66's own diagnosis; falsifiable by an `S_occ`-corrected Route-B-PW recompute.
- **STRONG (regime-physics)** — sudden box-delta `+0.864` as regime-canonical; slow-roll/adiabatic readings out-of-regime.
- **What I do NOT claim** — that `+0.864` matches Planck. It is `+0.864` OOM ABOVE Planck: a REAL, SINGLE, substrate-IS overproduction of acoustic squeezing relative to the CMB container. My claim is that it is ONE number, not a spread; the spread is convention. Whether the exit greybody filter `Γ < 1` brings `+0.864` down to Planck is the SEPARATE CF-AS-2 filter question (CF23 split: FLOOR permanent / FILTER open), not a figure-multiplicity question.

**Questions for mack-cosmic-bridge (Turn B):**

1. **(on b — 3.15)** S66 itself diagnoses Route-B-PW 3.15 as "`S_fold` used where `S_occ` needed," and the same S66 ledger queued it for supersession by TRANSIT-PS-67 (now the CC3/box-delta picture). Before you may count 3.15 as a third genuinely-distinct, LIVE route, can you exhibit the OCCUPIED-state (`S_occ = (1+2n_k)·S_fold`), CC3-threaded Route-B-PW recompute and show it is distinct from the box-delta/CC3 image? If not, on what grounds is a pre-CC3, wrong-functional figure admitted as a current physical prediction rather than retired?

2. **(on c — regime)** The transit is impulsive (`H·dt = 0.663 < 1`, Mach 13.75) and the sudden approximation is EXACT (S100b `var_Nseg−1 = 6e-10`), while `ω'/ω² ≫ 1` at the fold makes the adiabatic theorem fail. On what regime-physics grounds do the adiabatic Parker (`+1.455`) and slow-roll TD/zeta (`+0.196`) readings claim equal canonical standing with the sudden (`+0.864`) reading? Is "the CMB samples a different transit regime" a DERIVED statement — with a second physical transit exhibited — or a slow-roll/adiabatic formula applied outside its stated regime and re-labeled "physics"?

3. **(on S115)** S115 partitions the spread as maxent → sudden/impulse end, Connes-diameter → adiabatic/Parker end. maxent is the maximum-entropy occupation (a dynamical/statistical principle on the produced `⟨N⟩,⟨E⟩`); Connes-diameter is an NCG metric normalization (not a dynamical selector). Why should a spectral-geometry normalization be admitted as a regime-selection principle on equal footing with the maximum-entropy occupation that lands on the regime-correct sudden end? Doesn't S115's own partition show the spread is a NORMALIZATION axis with a regime-forced canonical endpoint, rather than a physical axis of distinct CMB-sampled regimes?

### R1 · mack-cosmic-bridge — PHYSICS-BLOCKED steelman

**Thesis.** The substrate IS the GGE-relic acoustic squeezing modulus of the post-fold produced state; the lab reads its power `A_s` IN the CMB container, where Planck measures it to 1.4% — `ln(10^10 A_s) = 3.044 ± 0.014`, i.e. `A_s = (2.099 ± 0.029)e-9`. Against a datum that tight, the framework does not return one number. It returns a 1.331-OOM family `{+0.196, +0.864, +1.455, +1.527}` whose members sit `40.9σ / 451.5σ / 1967σ / 2333.7σ` above Planck and — the load-bearing figure — `410.7σ` to `2293σ` apart **FROM EACH OTHER** at Planck precision. transit-dynamics-theorist's case is that this family is a convention stack collapsing to one Bogoliubov object once a regime is fixed. I will grant the one identity that is genuinely airtight (the CC3 factor-2) and then show it collapses an axis I never disputed while leaving the open axis — *which post-fold regime the squeezing carries at horizon exit* — exactly where S115 left it: un-singled-out, by the framework's own failed selector. The blocker is a missing physical derivation (the horizon-exit regime), not a missing convention pin. And the cleanest evidence is internal: the framework already carries **two** mutually-inconsistent figures it has BOTH labelled "canonical," `410.7σ` apart.

**On the +2 backbone — CONCEDED as airtight, but it lives on the CLOSED axis, orthogonal to the open one.**

I grant the CC3 identity without reservation. `INV12-W3-5-CF21-HTILDE-RECONCILE` is PASS, `cc3 = 2.000000` to machine ε, `oomH_TDLI = 2.3798`, `oomAs_TDLI = 4.7595`; `4.76 = 2 × 2.38` EXACTLY; the atlas "4.56" is the stale rendering (`fig456 = As-space-stale-live4.76`). 2.38 (H̃-space) and 4.76 (A_s-space) are ONE divergence in two spaces. The physics-blocked side does NOT double-count them. So far we agree completely.

But look at *what* divergence CC3 governs. By the gate's own ledger, `2.38 = the TD-vs-LI gap` — the gap between two **initial-condition schemes** (Zubarev/TD vs Lifshitz-Invariant) **within Branch-A slow-roll Mukhanov-Sasaki**. INV12-W3-5 then CLOSES that axis: "Branch-B LI = 2.46411e-5 RULED OUT (A_s FAIL-GT15)." The IC-scheme axis is settled — TD/Zubarev wins, landing at `+0.196`. CC3 is the conjugacy relation *on that closed axis*: it tells you how an H̃-reading maps to its OWN A_s image when you hold the functional `g` fixed. Read the TD substitution chain literally — Step 1 pins `∂g/∂H̃ = 0` ("fixed-profile"); CC3 is the response to varying H̃ **at fixed g**.

The route spread is not a spread in H̃ at fixed `g`. It is a spread in `g` itself:

```
Claim: "CC3 collapses the IC axis but is SILENT on the regime axis."
  Step 1:  A_s^route = (H̃²/8π²) · g_route,   g_route ≡ (1/ε_H)·F_amp·c_sub⁻¹·f_conv·S_IC   [TD eq (1)]
  Step 2:  TD/zeta:   g = g_(slow-roll MS, Zubarev IC)            [Branch-A Mukhanov-Sasaki mode function]
           box-delta: A_s = |β_k̂|²/(2π²) at N_norm = ξ_KZ³        [sudden Bogoliubov — a DIFFERENT functional, not eq(1) with a re-read H̃]
  Step 3:  TD/zeta → box-delta changes the FUNCTIONAL g (and the mode equation), not the value of H̃ at fixed g
  Step 4:  CC3 ≡ d(ln A_s)/d(ln H̃)|_{g fixed} = 2   ⇒   governs ONLY the H̃-direction Step 1 holds g constant
  Step 5:  ∂(route spread)/∂(ln H̃)|_{g fixed} ≠ the route spread; the route spread is ∂A_s/∂g, the direction CC3 freezes
  Conclusion: the +2 backbone collapses the IC axis (conceded) and is structurally silent on the regime axis (the open gap).
```

So the `+2` appears in three guises (CC3, `deg(T_BZ→pivot)=+2`, power-spectrum quadraticity) and they ARE the same `+2` — I grant that too. But all three are statements about the **H̃→A_s power**, the IC axis. None of them is a statement about slow-roll-MS vs sudden vs adiabatic — the **functional/regime axis** where `g` changes. The TD argument proves a factor-2 I concede and leaves the `1.331`-OOM route spread untouched. **These two axes are orthogonal**, and importing the closed-axis identity to adjudicate the open axis is the central move I dispute.

**Sub-(a): TD/zeta `+0.196` vs box-delta `+0.864` is a genuine horizon-exit regime divergence (410.7σ), not a convention swap. Three counter-arguments.**

The two readings are `0.668` OOM = **410.7σ** apart at Planck precision (`A_s = 3.2994e-9` vs `1.5367e-8`). transit-dynamics-theorist reads this as `(slow-roll-MS, Zubarev)` vs `(sudden, ξ_KZ)` — "same state, two conventions." I disagree on three independent grounds:

*(i) The framework has already PASS-certified the OTHER figure as canonical.* `INV12-W3-5` (PASS — an already-passed gate, by transit-dynamics-theorist's own evidentiary standard for CC3) states verbatim: "canonical horizon-exit reading = Branch-A TD/zeta Mukhanov-Sasaki H_tilde=5.9076e-3 (A_s=3.2994e-9, +0.196)." The R1 opening then OVERRIDES this passed gate with a regime argument (sudden-is-canonical → `+0.864`) that has passed **no gate**. When the framework simultaneously holds `+0.196` (PASS-certified canonical) and `+0.864` (R1-asserted canonical), `410.7σ` apart, that is not a settled convention with a notation choice pending — it is an **un-adjudicated physical fork between two figures the framework itself calls "canonical."** The TD opening tries to dissolve this by splitting an "IC-scheme axis" (INV12-W3-5 settles) from a "dynamics axis" (regime settles) — but that split *assumes* the dynamics axis resolves to sudden, which is precisely the open proposition. You cannot retire a contradiction by asserting the contested premise.

*(ii) Mode-function choice is dynamics, not convention.* Slow-roll Mukhanov-Sasaki and sudden Bogoliubov are two different **equations of motion** for the produced mode. The TD "sudden is EXACT" evidence — S100b `var_Nseg−1 = 6e-10` — is evaluated **at the fold** (`τ_fold = 0.190`, the impulsive event). But `A_s` is the curvature power **at horizon exit**, `54.04` decades of substrate evolution downstream. Substrate-first: the CMB does not photograph the fold; it photographs the frozen super-horizon acoustic mode after the post-fold substrate has carried it out. Whether that frozen amplitude IS the sudden-at-fold `|β|²` or the slow-roll-evolved value depends on the intervening propagation `T(fold → exit)` — which is the unmodeled physics. "Sudden is exact at `τ=0.190`" ⇏ "sudden is the horizon-exit reading." The `0.668`-OOM gap between the two readings is exactly the magnitude of that untracked post-fold transfer.

*(iii) Joint `(n_s, A_s)` consistency — the observational-cosmology core.* Planck does not measure `A_s` alone; it measures the `(n_s, A_s)` pair, correlated because both descend from the SAME primordial mode function at the SAME horizon-exit condition. The framework's `n_s = 0.9590` is computed slow-roll/cutoff Mukhanov-Sasaki (`INV12-W1-3-N-S-FUNCTIONAL-COHERENCE`, PASS, `regulator_pin=a_2^{cutoff}`, sqrt/f* moments). If `A_s` is then read through the **sudden box-delta** mode function, the framework predicts `n_s` and `A_s` from **two different mode functions** — an internal inconsistency, not a convention. Internal consistency with the committed `n_s` pipeline FAVORS the slow-roll-MS `A_s = +0.196` — which is exactly the `INV12-W3-5` canonical the regime argument overrides. So the box-delta `+0.864` is in tension with the framework's own `n_s` derivation, and that tension is physical and unresolved.

Verdict on (a): SAME produced state, but `+0.196` and `+0.864` are DIFFERENT horizon-exit mode functions ⇒ genuinely different physical predictions. "Regime" is not a reader's free choice; it is a property of the horizon-exit dynamics the framework has not pinned.

**Sub-(b): Route-B-PW 3.15 — PARTIAL CONCESSION + burden-return. Disposition: 3.15-raw RETIRE; Route-B-PW-corrected OPEN.**

I concede the raw figure. `AMPLITUDE-NORM-66` is S66, pre-UNIFIED-AS-79, pre-CC3, and its own diagnosis (constraint-mega-matrix:336) is verbatim "`S_fold` (vacuum spectral action) used where `S_occ` (occupied-state) needed." I do NOT defend `3.15`-raw as a live route at its raw value — **RETIRE 3.15-raw**. I also concede I cannot exhibit the `S_occ`-corrected, CC3-threaded recompute; it has not been run (it is a carry-forward, not a result).

But the burden returns symmetrically. transit-dynamics-theorist asserts the corrected figure "reduces to the box-delta/CC3 image." That reduction is **equally uncomputed**, and there is a concrete structural reason it is not obvious: the `S_occ` correction is `K_sub = S_IC^GGE / S_IC^BD = (1 + 2 n_k)` (`INV12-W1-2`, structural, `n_k = |β_k|² ≥ 0`). The occupation `n_k` is **route-dependent** — the locked-relic sudden reading carries `n̄ ≈ 2.7e-4` (box-delta), the slow-roll reading carries a different occupation — so the `S_occ`-corrected Route-B-PW figure inherits a route-dependent `K_sub` and is NOT guaranteed to land on the box-delta value. It could land at a **third** point. Honest disposition: `3.15`-raw → RETIRE; **Route-B-PW-corrected → OPEN** (an uncomputed third value, carry-forward). Neither side may claim it as a confirmed image of the box-delta; that it is genuinely open is itself evidence the A_s figure is not yet singled out.

**Sub-(c) — THE FORK: PHYSICS-BLOCKED. A failed substrate-principle selector is the signature of a physics gap, not a convention.**

The two horns have a sharp operational test:

- A **CONVENTION** question never produces a FAILed selector gate. There is nothing to fail — you pick the convention and move on.
- A **PHYSICS** gap produces exactly what S115 produced: a substrate-principle selector that SEARCHES and FAILS. `S115-AS-NEWAXIS-SELECTOR` is FAIL — `min_collapse_dist_OOM = 0.6281 ≫ 0.1` band, `spread_existing_OOM = 1.2590`, `any_collapse = 0`.

`S115` is the framework asking ITSELF, from substrate principles (maximum-entropy occupation on the produced `⟨N⟩, ⟨E⟩`; Connes spectral diameter), "does the substrate single out one `A_s`?" The returned answer is **NO**. That FAIL is the physics-gap signature. transit-dynamics-theorist's re-reading — "maxent lands on sudden ⇒ convention-blocked" — does not dissolve the FAIL; it **presupposes** the regime-selection principle ("the regime is sudden at horizon exit") whose ABSENCE *is* the gap (per (a)(ii): sudden is established at the fold, not at exit). You cannot use "the regime is sudden" to argue the spread is convention when "sudden at horizon exit" is the very thing the framework has not derived.

And the S115 partition does not actually privilege one endpoint on substrate grounds. maxent → `+0.824` (sudden end, `46.3σ` from box-delta); Connes → `+1.527` (adiabatic end). transit-dynamics-theorist calls maxent "a dynamical/statistical principle" and Connes "a normalization, not a selector." But BOTH are substrate-IS: the maxent occupation IS the produced state's entropy-maximizing distribution, and the Connes diameter IS the spectral triple's metric scale. The substrate genuinely contains both. Declaring that the produced-state occupation (not the spectral geometry) sets the acoustic-squeezing normalization is *itself a physical claim* — one the framework has not gated. So even the TD-preferred endpoint rests on an un-derived selection principle. The fork is physics-blocked: the blocker is a missing horizon-exit regime-selection derivation, and S115 is the failed attempt to supply it.

**The greybody filter does not rescue convention-blocked — it makes the route choice MORE physical.** The TD honest-scope reserves `Γ < 1` as a "separate CF-AS-2 question." But `Γ` is a SINGLE substrate-derived multiplicative suppression; it cannot map four inputs to one Planck output. Tuned to bring box-delta (`+0.864`) → Planck, the SAME `Γ` lands the other routes at:

| Route | OOM above Planck | post-Γ residual | σ from Planck (post-Γ) |
|:------|:-----------------|:----------------|:-----------------------|
| TD/zeta `+0.196` | +0.196 | **−0.668 OOM** (undershoot) | **−56.1σ** |
| box-delta `+0.864` | +0.864 | 0.000 (tuned) | 0.0σ |
| maxent `+0.824` | +0.824 | −0.040 | −6.3σ |
| Parker `+1.455` | +1.455 | **+0.591 OOM** | **+207σ** |
| Connes `+1.527` | +1.527 | **+0.663 OOM** | **+257σ** |

So WHICH route is canonical *determines* what `Γ` must be, and the framework's derived `Γ` lands on Planck for **at most one** route. The route choice is therefore a genuine physical prediction that survives the filter, not a convention the filter absorbs. Until the framework derives which regime the horizon-exit modes carry, `A_s` is physics-blocked.

**Answers to transit-dynamics-theorist's three questions.**

*A1 (on b — 3.15).* I concede I cannot exhibit the `S_occ`-corrected recompute (carry-forward, not done) — so I do NOT count `3.15`-raw as a live third route; RETIRE it. But the grounds for not retiring the **route** (vs the raw figure): the route is uncomputed, not refuted. Your claim that the corrected figure reduces to the box-delta image is equally uncomputed, and the `K_sub = (1+2 n_k)` correction is route-dependent (occupation differs sudden vs slow-roll), so the corrected value is an OPEN third point, not a confirmed box-delta image. A pre-CC3 wrong-functional figure is retired; a route whose corrected value is unknown is open — those are different dispositions.

*A2 (on c — regime).* "The CMB samples a different regime" is NOT my claim. My claim is the framework has not DERIVED which regime the horizon-exit modes carry. Your adiabatic-theorem-fails / sudden-is-exact evidence establishes the regime **at the fold** (`τ=0.190`), and horizon exit is `54.04` decades downstream — so "sudden is exact at the fold" does not supply the horizon-exit derivation. The burden is symmetric: exhibit the post-fold transfer `T(fold → exit)` showing the sudden-at-fold `|β|²` IS the frozen super-horizon amplitude. Absent that transfer, "sudden is canonical at horizon exit" is a sudden-vs-slow-roll mode-function choice applied across an unmodeled `54.04`-decade gap and re-labelled "regime physics."

*A3 (on S115).* Connes-diameter is admitted on equal footing with maxent because both are substrate-IS, and the question S115 poses is not "which is the better selector" but "does the substrate single out one `A_s`?" — to which the framework's own answer is NO. The maxent-lands-near-sudden coincidence (`0.040` OOM = `46.3σ` from box-delta) is real but does not collapse the spread: maxent at `+0.824` is still `405σ` from Planck, and Connes (`+1.527`) and Parker (`+1.455`) remain `~0.7` OOM = `~250σ` uncollapsed. A selector that lands near ONE of five routes while leaving the rest spread by `1.3` OOM has confirmed the spread, not singled out `A_s`. S115's partition shows two substrate principles `0.628` OOM apart — the definition of a physics-unresolved spread, not a normalization axis with a forced endpoint.

**Honest scope (what I concede vs what I hold).**

- **CONCEDED (airtight)** — CC3 `2.38 ↔ 4.76` conjugacy (`cc3 = 2.000000`); the IC-scheme axis is closed (TD/Zubarev beats LI, LI ruled out). I will not double-count 2.38 and 4.76.
- **CONCEDED (disposition)** — `3.15`-raw is a wrong-functional pre-CC3 figure; RETIRE it.
- **HELD (physics-blocked)** — the regime/functional axis spread `{+0.196, +0.864, +1.455, +1.527}` is real, `410.7σ–2293σ` wide at Planck precision, orthogonal to the CC3 axis, NOT collapsed by any substrate principle the framework has tried (`S115` FAIL), and NOT absorbed by the single greybody `Γ`. The framework holds two un-reconciled "canonical" figures (`+0.196` INV12-W3-5 vs `+0.864` box-delta), `410.7σ` apart.
- **What I do NOT claim** — that any route matches Planck (all are `40.9σ–2334σ` above; that overproduction is the FLOOR, the substrate's genuine over-squeezing, CF23 (a) PERMANENT). My claim is narrower and harder: the framework does not yet single out WHICH overproduction it predicts.

**Questions for transit-dynamics-theorist (Round 2).**

1. **(Horizon-exit transfer.)** The sudden approximation is exact AT THE FOLD (`τ=0.190`); `A_s` is the curvature power at HORIZON EXIT, `54.04` decades downstream. Exhibit the post-fold transfer `T(fold → exit)` demonstrating the sudden-at-fold `|β|²` IS the frozen super-horizon amplitude (i.e., the mode function does not evolve between fold and exit). Without that transfer, on what grounds is the sudden reading "canonical at horizon exit" rather than "exact at the fold and untracked thereafter"?

2. **(Joint `n_s`–`A_s`.)** The framework's `n_s = 0.9590` is slow-roll/cutoff Mukhanov-Sasaki (`INV12-W1-3`). Does the sudden box-delta reading REPRODUCE `n_s = 0.9590` from the SAME mode function it uses for `A_s = +0.864`? If not, isn't box-delta internally inconsistent with the committed `n_s` — and isn't the slow-roll-MS `+0.196` (the `INV12-W3-5` canonical you override) the internally-consistent reading of the `(n_s, A_s)` pair?

3. **(Two framework canonicals.)** `INV12-W3-5` PASS declares the canonical = Branch-A TD/zeta `+0.196` and rules out the alternative. Your R1 declares the canonical = sudden box-delta `+0.864`. They are `0.668` OOM = `410.7σ` apart at Planck precision. If `A_s` closure is convention-blocked, which ALREADY-PASSED gate selects `+0.864` over the `+0.196` that `INV12-W3-5` PASS-certified? If none exists, isn't the live state precisely two un-reconciled "canonical" figures — i.e., physics-blocked until a horizon-exit regime derivation lands?

---

## Round 2 — Rebuttal (engage the opponent's strongest case)

### R2 · transit-dynamics-theorist

#### CONVERGENCE — where you now grant the mack side

mack-cosmic-bridge's R1 "On the +2 backbone" did the one thing an adversary should: it accepted my airtight result in full and then showed it does not reach where I aimed it. I grant three things.

**1. The two-axis orthogonality is correct, and my R1 over-reached on it.** mack's substitution chain (R1 "Claim: CC3 collapses the IC axis but is SILENT on the regime axis," Steps 1–5) is right as written. CC3 is `d(ln A_s)/d(ln H̃)|_{g fixed} = 2` — a response to varying H̃ **at fixed g**. The route family `{+0.196, +0.864, +1.455, +1.527}` is not a spread in H̃ at fixed g; it is a spread in `g` itself (slow-roll-MS vs sudden box-delta vs Parker-adiabatic vs Connes-normalized are different functionals, in two cases different mode equations). My R1 "ONE factor of 2 wearing three hats" is TRUE — CC3, `deg(T_BZ→pivot)=+2`, and power-spectrum quadraticity are the same `+2` — but all three are statements about the **H̃→A_s power**, i.e. the IC/H̃ axis. None of them is a statement about which functional `g` the produced state is read through. I let the airtightness of the `+2` on the closed axis bleed into a claim about the open axis. That bleed is unjustified. **The `+2` backbone disposes of `2.38 ↔ 4.76` and is orthogonal to the `g`-spread. Conceded.**

**2. "Sudden is exact" is established AT THE FOLD, not at horizon exit.** mack's (a)(ii) and Q1 are fair. My S100b evidence (`var_Nseg−1 = 6e-10`, Schmidt-Eq.75 `1.6e-6`, TM-vs-Radau `7e-12`) certifies the sudden Bogoliubov **at `τ_fold = 0.190`**, the impulsive event. `A_s` is the curvature power at horizon exit. "Sudden is exact at the fold" does **not** by itself entail "sudden is the horizon-exit reading." I do not have the full fold→exit transfer `T(fold → exit)` in hand. Conceded — and I make it the spine of my DISSENT below rather than paper over it.

**3. No already-passed gate adjudicates `+0.864` over `+0.196` as the horizon-exit reading.** mack's Q3 lands. `INV12-W3-5` (PASS) does label the canonical horizon-exit reading Branch-A TD/zeta `+0.196`; my R1 asserted `+0.864` via a regime argument that has passed no gate. The evidentiary asymmetry is real: CC3 is a passed gate; "sudden-is-canonical-at-exit" is an argument. I will not smuggle the contested premise in as though it were gated. **What I retract from R1**: the clean claim "the fork resolves CONVENTION-BLOCKED." It does not resolve cleanly to convention — not on the lower gap. My DISSENT narrows, rather than abandons, the TD position.

#### DISSENT — where you hold, with NEW argument (don't restate R1)

I hold that the `g`-spread is **not an irreducible plurality**. It decomposes into a convention half (resolved) and a **single pending transfer function** (one derivation, not a 1.3-OOM gap). Two new arguments, then the answers to mack's questions.

**NEW-1 — The `(n_s, A_s)` joint-consistency objection (mack's (a)(iii) + Q2) is structurally void: tilt and magnitude are carried by ORTHOGONAL pieces of the one produced state, and the regime touches only the magnitude.**

mack treats `n_s` and `A_s` as "descending from the SAME mode function at the SAME horizon-exit condition," so that a slow-roll `n_s` plus a sudden `A_s` is "two mode functions." This conflates two structurally different functionals of one spectrum:

- `n_s − 1 = d ln P_ζ / d ln k` — a **log-derivative**: the k-SHAPE / tilt.
- `A_s = P_ζ(k̂)` — a **magnitude**: the normalization at one scale.

Write the produced-relic power as substrate geometry × produced occupation, and differentiate:

```
  (2)  P_ζ(k) = P_geom(k) · N_occ(k),    N_occ(k) ∝ |β_k|²   (GGE-relic squeezing on the vacuum envelope)
       Step 1:  ln P_ζ(k) = ln P_geom(k) + ln N_occ(k)
       Step 2:  n_s − 1 = d ln P_ζ/d ln k = d ln P_geom/d ln k + d ln N_occ/d ln k
       Step 3:  Mode-Independent Occupation (S57/S62, PERMANENT):  d ln N_occ/d ln k = 0  across the CMB band
                  ⇒ (independently certified by)  α_s(primordial) = d²ln P_ζ/d(ln k)² = 0  EXACT  (Bogoliubov saturation, superhorizon plateau)
       Step 4:  n_s − 1 = d ln P_geom/d ln k = −2 ε_H            (GEOMETRIC tilt; ε_H = 0.02195 ⇒ n_s = 1 − 0.0439 = 0.9561)
       Step 5:  A_s = P_ζ(k̂) = P_geom(k̂) · N_occ(k̂)            (magnitude carries N_occ(k̂) ∝ |β_k̂|²)
```

The tilt drops **all** occupation dependence (Step 3: flat occupation ⇒ derivative zero ⇒ `α_s = 0` EXACT), so `n_s = 1 − 2ε_H` is a property of the geometric/transport envelope `P_geom` and the background `ε_H` — **regime-blind**. The magnitude keeps the occupation factor `N_occ(k̂)` — **regime-sensitive**. A regime switch (slow-roll-MS ↔ sudden box-delta) changes the **amplitude** `N_occ(k̂)` (hence `A_s`) but cannot change either (i) the geometric envelope `P_geom` (same `z(τ)`, same `ε_H`) or (ii) the **flatness** of `N_occ` — because the box-delta sudden spectrum is itself near-flat across the band (`S115`: flat to the first RT zero `k ≈ 2779 ≫ k̂ = 53.30`; maxent redistributes only ~6%). So the sudden reading reproduces `n_s = 0.9561` **identically**: it contributes zero tilt (flat) on the same geometric envelope.

**Answer to Q2, directly: YES — the sudden box-delta reproduces the committed `n_s` from the same produced state, because its occupation is also flat in k and the geometric tilt envelope is unchanged.** There is no two-mode-function inconsistency. This is precisely the structure the framework already certifies elsewhere: `α_s(primordial) = 0` EXACT in the superhorizon plateau **is** the statement "the produced occupation is k-flat, so it sets magnitude, never tilt." mack's (a)(iii) assumed the magnitude and the tilt co-vary under the regime switch; the Mode-Independent Occupation theorem says they do not. The `(n_s, A_s)` pair therefore does **not** favor slow-roll-MS for `A_s`; the `n_s` pipeline constrains only the geometric `ε_H` (shared by every regime reading) and is silent on the produced-state magnitude.

**NEW-2 — The `g`-spread is two structurally different objects, not one axis. The upper half is convention (regime-collapsed); the lower gap is a single transfer-function prefactor.**

Partition `{+0.196, +0.864, +1.455, +1.527}` by what kind of reading each is:

- **Upper half — `+0.864` (sudden) ↔ `+1.455` (Parker) / `+1.527` (Connes).** These are all **produced-state Bogoliubov** readings (occupation-amplitude squeezing). They differ only in how the impulsive event is treated. The sudden box-delta is the controlled approximation for `H·dt = 0.663 < 1`; the Parker-adiabatic integral `∫(ω'/2ω)e^{2i∫ω}dτ` is the **adiabatic** formula, evaluated where `ω'/ω² ≫ 1` (out of its stated regime); Connes (`+1.527`) sits on the adiabatic end (`S115`: Connes-diameter → Parker, `0.072` away). **The impulsive transit is a substrate fact, not a reader's choice; it demotes Parker/Connes BEFORE any selector runs.** This is the half my R1 regime argument actually settles, and it is convention (out-of-regime formula vs in-regime formula), not a family of distinct CMB-sampled transits.

- **Lower gap — `+0.196` (slow-roll-MS) ↔ `+0.864` (sudden box-delta).** This is the genuinely open `0.668`-OOM gap, and it is **one** object, not a plurality. Evidence it is one object: the box-delta `|β_k̂|²` is **functional-BLIND** — `S114 W4-1` proved `d|β_k̂|²/d(a_0/a_2)|_{horizon-exit} = 0` EXACT (it is a closed form in fold-transit/UV quantities only: `Ω_z_on, Ω_z_off, V_box, Δη, ξ_KZ`). The slow-roll-MS `+0.196` is functional-DEPENDENT — it reads the horizon-exit `a_0/a_2` (the 181× SDW/Zubarev split, `S82`). So the two readings are not two competing horizon-exit functionals; they are the two **ends** of the `deg(T_BZ→pivot) = +2` transport: a fold-scale (`ξ_KZ`-natural, functional-blind) squeezing modulus and its horizon-exit (`H̃`-scale, functional-dependent) image. **The degree of that transport is airtight (+2, NON-SCALAR, S93 W7-1); only its NORMALIZATION prefactor is open. That prefactor IS the `+0.196 ↔ +0.864` gap.**

So the honest residue is **not** "the substrate does not single out one `A_s`" (a 1.3-OOM plurality). It is "the substrate selects the regime (impulsive ⇒ sudden end, collapsing the upper half) and the `n_s`-consistency is intact (Mode-Independent Occupation), leaving **one** undischarged number: the fold→exit transfer prefactor." That is physics-**pending** (a single computable propagation), not physics-**blocked** (an irreducible gap).

**NEW-3 — mack's "a FAILed selector is the signature of a physics gap" (Sub-(c)) is half-right, and the wrong half is load-bearing.** A selector that searches a co-equal set and fails does signal a gap. But `S115` searched `{impulse, UNIFIED, Parker}` as co-equal physical candidates. They are not co-equal: the impulsive regime is a substrate property that **demotes Parker before the search starts**. `S115`'s own partition confirms this — maxent (the entropy-maximizing occupation on the produced `⟨N⟩, ⟨E⟩`, a dynamical principle) lands at `+0.824`, `0.040` OOM from the sudden end; Connes-diameter (`d_C = 1/(λ_max − λ_min)`, a spectral-metric normalization, not a dynamical selector) lands on the demoted adiabatic end. A selector-FAIL over an artificially co-equal set is not a proof that no canonical regime exists; it is the wrong null set. The correct reading of `S115` is: the **dynamical** principle agrees with the regime-forced sudden end; the spread to Parker is the metric-normalization convention. That narrows the gap to the lower `+0.196 ↔ +0.864`, exactly as NEW-2.

**Answer to Q1 (the horizon-exit transfer), honestly scoped.** I do not have the full `T(fold → exit)`. What the framework DOES have, and what bounds the gap: (i) the transport **degree** is `+2` NON-SCALAR (airtight); (ii) the **superhorizon** leg is frozen — `α_s = 0` EXACT (Bogoliubov saturation: once superhorizon, `|β_k|²` is a constant of motion, the produced occupation does not re-process); (iii) `β_k` is by definition the in–out overlap, constant in any post-fold adiabatic region — and the fold is a measure-zero impulsive event, so the post-fold background is smooth (adiabatic) again, which makes `T` plausibly near-identity on `|β_k|²`. What is genuinely OPEN is the **subhorizon** fold→exit leg's scale-remapping prefactor: the pivot is `k/aH = 14.7` (subhorizon) at the fold (`S77`) and must propagate to `k/aH = 1`; the `ξ_KZ` fold-scale normalization must be carried to the `H̃` horizon-exit normalization, and the `+2` degree of that carry has an undischarged prefactor. **That prefactor — not a choice among readings — is what stands between `+0.864` and `+0.196`.** "Sudden is canonical at horizon exit" is therefore not yet earned; "the produced squeezing is `+0.864` at the fold scale and its exit image is `+0.864 ×` (a pending degree-2 prefactor)" is.

#### EMERGENCE — new structure from the exchange

The exchange converts a 4-member, 1.3-OOM "route family" into a **two-layer object**, and isolates the open content to a single number:

**Layer A (CONVENTION — resolved).** `2.38 ↔ 4.76` is CC3-conjugate (airtight, both sides agree). The **upper** `g`-spread `+0.864 ↔ +1.527` is regime-blind: the impulsive transit (`H·dt < 1`, Mach 13.75) selects the sudden end; Parker (`+1.455`) and Connes (`+1.527`) are the adiabatic formula / metric-normalization applied off-regime. Route-B-PW `3.15`-raw is wrong-functional legacy (both sides RETIRE). This layer is convention-blocked and settled.

**Layer B (PHYSICS-PENDING — one derivation).** The `+0.196 ↔ +0.864` gap is **the normalization prefactor of the subhorizon fold→exit transfer** carrying the functional-blind, `ξ_KZ`-scale box-delta `|β_k̂|²` to the functional-dependent, `H̃`-scale horizon-exit Mukhanov-Sasaki curvature amplitude `ζ_k̂`. **Exactly what must be derived to close the regime axis** (the sharp statement mack's Q1 demands):

> Compute the prefactor `𝒩` in `ζ_k̂(exit) = 𝒩 · (k̂/aH)^{+2}|_{transport} · |β_k̂|(fold)`, i.e. the connection-formula / transfer-matrix propagation of the sudden-produced occupation across the subhorizon leg `k/aH : 14.7 → 1`, with `deg = +2` PINNED (S93 W7-1) and `𝒩` the open output. `𝒩 ≈ 1` ⇒ box-delta `+0.864` is the exit floor; `𝒩` driving `|β|²` down by `10^{−0.668}` ⇒ `+0.196` is the exit reading; any intermediate `𝒩` pins a point between. This is **one** Bogoliubov-transfer computation (WKB connection across the subhorizon turning structure, or a Radau propagation of the MS equation from `τ_fold` to horizon crossing), **not** a selection among co-equal functionals.

**The new structural lemma (NEW-1), reusable beyond A_s:** *tilt and magnitude decouple under Mode-Independent Occupation.* `n_s` (log-derivative) is carried by the geometric envelope and is regime-blind; `A_s` (magnitude) is carried by the flat occupation amplitude and is regime-sensitive. This **removes the `(n_s, A_s)` joint-consistency objection from the physics-blocked case** — the box-delta is not inconsistent with the committed slow-roll `n_s` — and confines the entire open content to the single Layer-B prefactor. It also predicts a falsifiable corollary: any regime reading consistent with the framework MUST give `α_s ≈ 0` (flat occupation); a regime reading that tilts `A_s(k)` would break `n_s` and is excluded on that ground alone.

**On the greybody (mack's Sub-(c) table):** it does not bear on the fork. `Γ < 1` is the SEPARATE CF-AS-2 FILTER question (FLOOR/FILTER split, CF23). mack's table — one `Γ` cannot map four inputs to one Planck output — is correct and is in fact an argument FOR resolving the regime first: the filter acts on the magnitude AFTER Layer-A (regime) and Layer-B (transfer) fix the input. Collapse the family to the Layer-B-pending point, and the table has one input, not four; the filter question becomes well-posed.

**Where I now stand vs mack:** we agree the `g`-axis is real and orthogonal to CC3 (his R1, my CONVERGENCE-1); we agree no gate yet pins `+0.864` over `+0.196` at exit (my CONVERGENCE-3); we agree Route-B-PW-corrected is uncomputed. We differ on the **shape** of the open content: mack reads it as a `1.3`-OOM plurality the substrate has not typed (`S115` FAIL); I read it as `convention (upper) + one transfer prefactor (lower)`, with the `(n_s, A_s)` objection removed by Mode-Independent Occupation. The fork is therefore not "convention vs physics" as a clean binary — it is **convention-blocked on Layer A, physics-pending-one-transfer on Layer B**. If forced to pin one figure pending Layer B, the substrate-IS floor point is the box-delta `+0.864` (A_s-space) — the produced squeezing the transit actually makes, functional-blind and regime-correct — flagged "fold-scale; horizon-exit image awaits the degree-2 transfer prefactor `𝒩`," with `+0.196` as that exit image under `𝒩 = 10^{−0.668}`.

**Two sharper questions for mack (Round 3):**

1. **(On the decoupling.)** Given NEW-1 — `n_s` is the geometric tilt `1 − 2ε_H` (regime-blind) and the produced occupation is k-flat (`α_s = 0` EXACT), so it sets magnitude, never tilt — do you still hold that internal consistency with the slow-roll `n_s` pipeline FAVORS the slow-roll-MS `A_s = +0.196`? Or do you grant that the `n_s` pipeline constrains only the geometric `ε_H` (shared by every regime reading) and is therefore SILENT on the produced-state magnitude normalization — leaving your physics-blocked case resting on the Layer-B transfer alone, not on `(n_s, A_s)` consistency?

2. **(On the shape of the gap.)** Is your "physics-blocked" claim that the `+0.196 ↔ +0.864` gap is an **irreducible** plurality (no single substrate object pins it), or that it is **one pending derivation** — the fold→exit transfer prefactor `𝒩` of NEW-2/EMERGENCE, with `deg = +2` already pinned? If the latter, we agree on the structure and differ only on the label: "physics-blocked" (your word) vs "physics-pending-one-transfer" (mine). A `1.3`-OOM plurality and a single undischarged degree-2 prefactor are different liabilities; which is the live one?

### R2 · mack-cosmic-bridge

#### CONVERGENCE — where you now grant the TD side

transit-dynamics-theorist's R2 did the honest thing my R1 asked for: it conceded the three points where my case actually bit (CONVERGENCE-1 the two-axis orthogonality; CONVERGENCE-2 sudden-is-exact-at-the-fold-not-at-exit; CONVERGENCE-3 no gate adjudicates `+0.864` over `+0.196`) and then NARROWED — rather than abandoned — the convention-blocked position to a single object. I reciprocate on the point TD pressed hardest, because it is correct and I will not defend a claim I can see through.

**NEW-1 is structurally right, and it retires my `(n_s, A_s)` argument. I withdraw a(iii).**

I built a(iii) on the premise that `n_s` and `A_s` "descend from the SAME mode function at the SAME horizon-exit condition," so reading `A_s` through a sudden mode function while `n_s` is slow-roll is "two mode functions." NEW-1 shows that premise is false at the level that matters. Write the produced power as TD does, `P_ζ(k) = P_geom(k)·N_occ(k)`, and the two observables project onto ORTHOGONAL pieces of it:

- `n_s − 1 = d ln P_ζ/d ln k` is a **log-derivative** — it annihilates any k-flat multiplicative factor.
- `A_s = P_ζ(k̂)` is a **magnitude** — it retains every multiplicative factor at `k̂`.

I recognize this structure: it is the **multiplicative-normalization cancellation invariant** (`math-scripts.md`, MANDATORY at K=3). A k-flat occupation pre-factor `N_occ` is annihilated by the log-derivative `n_s` and survives ONLY in the magnitude `A_s`. So IF the occupation is genuinely k-flat across the CMB band — and the framework's own `α_s(primordial) = 0` EXACT (Bogoliubov superhorizon saturation; S57/S62 Mode-Independent Occupation) IS that statement, with `S115` showing flatness out to the first RT zero at `k ≈ 2779 ≫ k̂ = 53.30` and maxent redistributing only ~6% — then a regime switch (slow-roll-MS ↔ sudden box-delta) moves `N_occ(k̂)` (hence `A_s`) WITHOUT touching either the geometric tilt envelope `P_geom` (same `z(τ)`, same `ε_H`) OR the flatness of `N_occ`. The sudden reading reproduces `n_s = 1 − 2ε_H = 0.9561` identically: zero occupation-tilt on the same geometric envelope.

**Answer to TD Q1, directly: YES.** I grant that the `n_s` pipeline constrains only the geometric `ε_H` — which every regime reading shares — and is therefore SILENT on the produced-state magnitude normalization. a(iii) assumed magnitude and tilt co-vary under the regime switch; Mode-Independent Occupation says they do not. **a(iii) falls. The `(n_s, A_s)` joint-consistency objection is withdrawn; the box-delta is NOT internally inconsistent with the committed slow-roll `n_s`.** My physics-blocked case no longer rests on it.

**What changed, precisely — and which direction it cuts.** I lose one of my three sub-(a) arguments. But mark WHERE the loss leaves the magnitude. Removing the `n_s` tie does not pin `A_s` closer to `+0.196` — it cuts `A_s` LOOSE from the one pipeline that might have constrained it. `n_s` could have been a second handle on the magnitude; NEW-1 proves it is not. So after NEW-1 the magnitude `A_s` is constrained by NOTHING in the tilt sector — exactly the reading the framework's own `CF-S114-AS-FUNCTIONAL-SELECTION` verdict already carries (FAIL, `selection=PLURALISM`, `struct_deriv=0`; the magnitude is a free physical degree of freedom, functional-blind, `d|β|²/d(a_0/a_2)=0`). NEW-1 is a concession on the argument and a SHARPENING on the substance: it isolates the open content to a single, unconstrained magnitude. I carry that isolation into DISSENT and show it does not favor TD.

**I also grant most of the 4→2 reduction (NEW-2 / NEW-3), with one reservation.** TD's claim that the impulsive transit (`H·dt = 0.663 < 1`, Mach 13.75) demotes Parker (`+1.455`) and Connes (`+1.527`) "before any selector runs" is correct **as a reading of the fold production**: the adiabatic formula and the spectral-metric normalization are off-regime ways to read the squeezing produced AT the fold, and the sudden box-delta is the controlled in-regime reading THERE. So as candidate readings of the fold-scale produced state, the upper half is convention. The live gap narrows from the 4-member `{+0.196, +0.864, +1.455, +1.527}` to the 2-member lower `{+0.196, +0.864}`. The reservation — that the demoted adiabatic physics does not VANISH but RELOCATES to the post-fold transfer leg, where it is back in-regime — is the spine of my DISSENT, so I develop it there rather than litigate it here.

We now agree completely on: CC3 conjugacy (`2.38 ↔ 4.76`, airtight); the IC axis closed (TD/Zubarev beats LI); the orthogonality of CC3 to the `g`-spread; sudden-is-exact-at-the-fold-not-exit; no gate yet pins `+0.864` at exit; Route-B-PW `3.15`-raw retired; and now the `(n_s, A_s)` decoupling. The dispute has shrunk to one scalar.

#### DISSENT — where you hold, with NEW argument (don't restate R1)

The shrinkage is real, and it does not carry TD to convention-blocked. Naming the residue "a single pending transfer function `T(fold→exit)`" RENAMES the open physics; it does not close it. My R1 arguments are conceded or superseded; here is the new one, in four moves.

**NEW-M1 — `deg(T)=+2` is pinned, but by TD's OWN NEW-1 it is SILENT on the magnitude `𝒩`. The two pillars of the convention-blocked case are in structural tension.**

TD's narrowed position stands on two pillars: **(P1)** NEW-1 — tilt and magnitude decouple, so `n_s` does not constrain `A_s`; **(P2)** `deg(T_BZ→pivot) = +2` is airtight (S93 W7-1), so "only the normalization prefactor `𝒩` is open" and the gap is "bounded." These pillars cannot both bear weight, because they are the SAME orthogonality pointed in opposite directions.

```
Claim: "deg(T)=+2 pinned ⇒ fixes the SCALING of T with k/aH; SILENT on the magnitude 𝒩."
  Step 1:  T(k/aH) = 𝒩 · (k/aH)^{deg},   deg = +2 pinned (S93 W7-1)        [transport ansatz, TD EMERGENCE]
  Step 2:  ln T = ln 𝒩 + deg·ln(k/aH)                                       [log of Step 1]
  Step 3:  deg ≡ d ln T / d ln(k/aH) = +2                                   [the pinned object IS a log-derivative]
  Step 4:  ∂(deg)/∂(ln 𝒩) = ∂/∂(ln 𝒩)[ d ln T / d ln(k/aH) ] = 0           [𝒩 is k/aH-flat ⇒ annihilated by the log-derivative]
  Step 5:  𝒩 = T / (k/aH)^{deg}                                            [the magnitude is the residue deg does NOT set]
  Conclusion: deg=+2 fixes HOW T scales with k/aH; the magnitude 𝒩 is orthogonal to deg — annihilated by it —
              exactly as a k-flat N_occ is annihilated by the log-derivative n_s (NEW-1).
```

This is NEW-1 again, transported one level up: `deg` is a log-derivative (`d ln T/d ln(k/aH)`); `𝒩` is the multiplicative normalization; a log-derivative annihilates a multiplicative normalization (the cancellation invariant TD invoked to free `A_s` from `n_s`). So pinning `deg=+2` does NOT "bound the gap" — it is structurally SILENT on the gap, because the gap IS the magnitude `𝒩`, and `𝒩` is precisely the part of `T` the degree cannot see. TD used the orthogonality to remove one constraint on the magnitude (`n_s`); the same orthogonality removes the other (`deg`). After NEW-1 + NEW-M1 the magnitude `𝒩` is unpinned by BOTH the tilt pipeline AND the transport degree — it is the residue every log-derivative object in the problem annihilates. A quantity that survives every available log-derivative and is fixed by none is the definition of an undischarged physical magnitude, not a pending notation.

**NEW-M2 — `T(fold→exit)` is not a well-posed deterministic propagation; it inherits the OPEN regime at its core. The framework's own verdict line says so.**

"Pending derivation" = convention-blocked-once-computed ONLY if the derivation is well-posed — all inputs fixed, run the ODE, read off `𝒩`. `T(fold→exit)` is not. Substrate-first: the substrate IS the GGE acoustic squeezing modulus; `T` is the substrate's OWN post-fold spectral propagation carrying the fold-scale modulus to the acoustic-horizon-crossing scale (`k/aH : 14.7 → 1`, S77). It is not an inflaton transfer function imposed on a container — it is intrinsic post-transit substrate evolution, and that is exactly why its regime is not free to stipulate.

Here is the structural fact, in the framework's own ledger. `CF-S114-AS-FUNCTIONAL-SELECTION`'s verdict line states the box-delta floor "lives on … NOT the horizon-exit H~ carrier … the impulse-quench floor" (`d|β|²/d(a_0/a_2)=0`). The framework's OWN annotation pins the box-delta as a **fold-scale floor — explicitly NOT the horizon-exit reading**. So `+0.864` is the produced squeezing AT THE FOLD; carrying it to horizon exit IS the transfer, and the transfer is undischarged.

Now the regime OF the transfer leg. The fold is a measure-zero impulsive event (`dt_transit = 1.13e-3 M_KK⁻¹`); AFTER it the background is smooth — adiabatic. So the post-fold subhorizon leg is governed by adiabatic evolution, and the Parker/adiabatic formula TD demoted "off-regime AT THE FOLD" is precisely IN-regime ON THE TRANSFER LEG. This is the CONVERGENCE reservation made load-bearing: demoting Parker at the fold does not delete adiabatic physics — it RELOCATES it to where it belongs, the post-fold propagation. And once you are propagating adiabatically from fold to exit, the slow-roll-MS reading `+0.196` is no longer a rival "convention"; it is, operationally, ONE candidate computation of `T(fold→exit)` — it evolves the mode through the post-fold MS background to horizon crossing. So `+0.196` and `+0.864` are NOT "a fold-scale object and its undetermined exit image." They are TWO DIFFERENT CHOICES of how to propagate across the post-fold leg:

- `𝒩 ≈ 1`: freeze `|β|²` rigidly at the fold and carry it out unprocessed (sudden-frozen) ⇒ `+0.864` at exit.
- `𝒩 = 10^{−0.668} = 0.2148`: evolve the mode through the post-fold adiabatic MS background to exit ⇒ `+0.196`.

TD's bridge across this — "`β_k` is constant in any post-fold adiabatic region, the post-fold background is smooth, so `T` is plausibly near-identity on `|β|²`" — is the tell. "Plausibly near-identity" is a CONJECTURE about whether the produced occupation re-processes between fold and exit; a plausibility argument, not a derivation (TD honestly labels it: "I do not have the full `T(fold → exit)`"). And it is a conjecture that, asserted as true, OVERRIDES the `INV12-W3-5` PASS that certified `+0.196` as the canonical horizon-exit reading. You cannot retire a passed gate with a plausibility argument and call the result convention.

**NEW-M3 — "pending" cannot relabel a `410.7σ` fork between two ALREADY-COMPUTED figures as not-yet-computed.** This is the card that does not soften. The derivation of `A_s` at horizon exit is not "pending" in the sense of unattempted. It has been performed TWICE and returned TWO values: `+0.196` (`INV12-W3-5`, PASS-certified canonical, slow-roll-MS at `H̃ = 5.9076e-3`) and `+0.864` (S111, computed box-delta at `ξ_KZ`). They are `0.668` OOM = `410.7σ` apart at Planck precision (`A_s^Planck = 2.099e-9`, `σ = 0.0294e-9` from `ln(10¹⁰A_s) = 3.044 ± 0.014`). "Pending" presupposes ONE answer awaits computation; the live state is TWO computed answers in contradiction, with no gate retiring either (TD CONVERGENCE-3). The substrate has not adjudicated between two magnitudes it has both produced. That is not a notation choice deferred — it is a physical magnitude the substrate does not currently single out. Until a derivation lands AND passes a gate that retires one branch, the fork is open by the framework's own ledger (atlas-08 §VIII CF21 OPEN; CF23 MAGNITUDE OPEN).

**The operational test, sharpened (answers TD Q2 on the shape of the gap).** TD frames the choice as "irreducible plurality (your word) vs one pending derivation (mine) — different labels for the same structure." It is NEITHER, and the difference is not lexical — the two make different EMPIRICAL claims:

- I do NOT claim irreducible plurality. I grant 4→2, and I grant the open content is a SINGLE scalar `𝒩` (structural agreement — see EMERGENCE).
- "Physics-pending-one-transfer" CLAIMS the substrate determines `𝒩` (run the ODE, read it off). "Physics-blocked" CLAIMS it does not (the ODE needs a post-fold regime input the substrate has not supplied). These are testable against the SAME computation — and the framework has run that test TWICE: `CF-S114-AS-FUNCTIONAL-SELECTION` (FAIL, `struct_deriv=0`, `any_collapse=0`) and `S115-AS-NEWAXIS-SELECTOR` (FAIL, `min_collapse = 0.628 ≫ 0.1`, `any_collapse=0`). A selector that SEARCHES the substrate for the principle fixing the magnitude and FAILS is the signature of "the substrate does not determine `𝒩`." A pure convention never produces a FAILed selector — there is nothing to fail. Two FAILed selectors is the empirical content of physics-blocked.

So my answer to **TD Q1**: granted — the case rests on the Layer-B transfer ALONE, and that is a STRONGER position than the three-legged R1, not a weaker one, because the transfer is a `410.7σ` fork between two computed values that two substrate-principle selectors have failed to close. And to **TD Q2**: the live liability is "`𝒩` is undetermined by current substrate physics," NOT "`𝒩` is determined-but-uncomputed" — the two existing computations and the two FAILed selectors are exactly what distinguish them, and they fall on the undetermined side. Is the transfer DERIVABLE-IN-PRINCIPLE? In the trivial sense that any ODE can be integrated once its IC and regime are fixed, yes — but its IC and regime are the open content (NEW-M2), so "derivable-in-principle" here means "derivable once the un-derived regime-selection is supplied," which is physics-blocked, not convention-blocked.

#### EMERGENCE — new structure from the exchange

**Yes — both sides can pin the open object, and we have.** The exchange converts a 4-member, `1.3`-OOM "route family" into ONE scalar. We agree:

1. The open object IS the single post-fold transfer `T(fold→exit)`: the substrate's intrinsic post-transit propagation carrying the functional-blind, `ξ_KZ`-scale box-delta squeezing `|β_k̂|²(fold)` to the functional-dependent, `H̃`-scale horizon-exit curvature amplitude `ζ_k̂(exit)`, across the subhorizon leg `k/aH : 14.7 → 1`.
2. `deg(T) = +2` is pinned and airtight (S93 W7-1, NON-SCALAR).
3. The open content is the normalization prefactor `𝒩` — a single magnitude.
4. The verdict turns ENTIRELY on `𝒩`'s epistemic status: determined-but-uncomputed (TD ⇒ convention-blocked-once-computed) vs undetermined-pending-regime-selection (me ⇒ physics-blocked).

That is a genuine structural advance: the workshop has reduced "does the substrate single out `A_s`?" to "is the scalar `𝒩` fixed by substrate inputs, or does it inherit the open post-fold regime?" — a question with a yes/no answer a single computation can return.

**The new structural lemma (mine, complementary to TD's NEW-1) — degree/normalization orthogonality.** NEW-1: the produced occupation is a k-flat multiplicative factor, annihilated by the tilt log-derivative `n_s`, retained by the magnitude `A_s`. NEW-M1 transports it: the transport degree `deg(T)` is itself a log-derivative (`d ln T/d ln(k/aH)`), and it annihilates the multiplicative normalization `𝒩`. The two lemmas COMPOSE: the magnitude is the residue annihilated by BOTH the tilt pipeline AND the transport degree. Reusable beyond `A_s`: **any substrate-IS magnitude that is the normalization of a degree-pinned transport is unconstrained by that degree** — pinning the degree of a transport never pins the normalization it carries. This is why "`deg=+2` is airtight" and "`𝒩` is open" are not in tension for TD and not a comfort either: they are the same orthogonality, and it says the airtight degree is SILENT on the open magnitude.

**The next-session gate that settles it (pre-registered fork discriminator).** Both sides agree this gate resolves the fork; we differ only on its predicted outcome.

> **CF-S117-T-FOLD-EXIT-NORMALIZATION** — compute `𝒩` AND test whether it is regime-DETERMINED.
>
> - **What**: Propagate the Mukhanov-Sasaki mode equation (Radau; GPU-optional, AMD RX 9070 XT) for the produced GGE mode from `τ_fold = 0.190` across the post-fold subhorizon leg `k/aH : 14.7 → 1`, extracting `𝒩` in `ζ_k̂(exit) = 𝒩 · (k̂/aH)^{+2}|_transport · |β_k̂|(fold)`. THEN a regime-robustness scan: vary the post-fold matching surface / IC across the leg (≥5 matching points) and measure the spread in `𝒩`.
> - **Inputs**: `|β_k̂|²(fold)` [INV12-W3-1 `cf_beta2 = 0.1437`; box-delta `A_s_FW = 1.5367e-8`, S111]; `N_norm = ξ_KZ³ = 6.6024e-6`, `k̂ = 1/ξ_KZ = 53.30` [S111]; post-fold `z(τ)` background + `(k/aH)|_fold = 14.7` [S77]; `deg = +2` [S93 W7-1]; `H̃ = 5.9076e-3` [INV12-W3-5]; `A_s^Planck = 2.099e-9`.
> - **Gate (pre-registered discriminator)**:
>   - **convention-blocked PASS** iff `𝒩` is regime-STABLE — max−min spread of `𝒩` over the matching-surface scan `≤ 0.1` OOM AND `𝒩` lands on one of `{𝒩 ≈ 1 ⇒ +0.864 exit floor; 𝒩 = 10^{−0.668} = 0.2148 ⇒ +0.196 exit}`. The substrate uniquely determines `𝒩`; closure is convention-blocked-once-computed; RETIRE the non-selected branch (and reconcile atlas-08 CF21 to the single survivor).
>   - **physics-blocked FAIL** iff the `𝒩` spread across the matching scan `> 0.1` OOM — the propagation is NOT closed by substrate inputs; `𝒩` depends on an un-derived matching/regime choice. The `410.7σ` fork stands; `A_s` closure is physics-blocked pending a separate regime-selection derivation (the THIRD FAILed selector, confirming `CF-S114` + `S115`).
> - **Effort**: one Radau propagation (`τ_fold → horizon crossing`) + ~5–10-point matching-surface robustness scan. Modest; single-script.

This is the convergence in operational form: we have converted "convention vs physics" from a debate into a pre-registered computable discriminator on a SINGLE scalar. If `𝒩` is regime-stable, TD is right and `A_s` closes convention-blocked on one figure; if `𝒩` swings with the matching choice, I am right and it is the third FAILed selector. Either way the Structural Verdict (Round 3) can pin the OOM figure CONDITIONALLY on the gate's pre-registered branches and route CF21's prose-reconciliation accordingly.

**Where I now stand vs TD.** We agree the `g`-axis is real and orthogonal to CC3; we agree no gate pins `+0.864` over `+0.196` at exit; we agree the `(n_s, A_s)` objection is removed by Mode-Independent Occupation; we agree the open object is one scalar `𝒩` with `deg=+2` pinned; we agree on the gate that settles it. We differ on `𝒩`'s epistemic status — and that difference is NOT a label. TD reads `𝒩` as determined-but-uncomputed (run the ODE). I read it as undetermined-pending-regime-selection — because the transfer leg is adiabatic, the demoted Parker physics is back IN-regime there, `+0.196` and `+0.864` are ALREADY two computed answers to it, and the substrate's two selector gates (`CF-S114`, `S115`) searched for the principle fixing it and FAILED. "Pending" is a derivation that has not been run; this one has been run twice and conflicts. The `CF-S117` gate is the adjudicator.

**Final question for Round 3.** The framework's own `CF-S114-AS-FUNCTIONAL-SELECTION` verdict line states the box-delta `|β|²` floor "lives on … NOT the horizon-exit H~ carrier … the impulse-quench floor" — the box-delta is, by the ledger, a FOLD-scale floor, not the exit reading. And the post-fold subhorizon leg is adiabatic (measure-zero fold; smooth background after). So when you compute `𝒩`: which mode function governs the post-fold propagation — the rigid sudden-frozen `|β|²` (`𝒩 ≈ 1 ⇒ +0.864`) or the adiabatically-evolved MS mode (`𝒩 = 10^{−0.668} ⇒ +0.196`)? Name the SUBSTRATE INPUT that fixes that choice WITHOUT a fresh regime-selection on the transfer leg — or concede that `𝒩` is the same regime question relocated downstream, hence undetermined (physics-blocked) until `CF-S117` returns regime-stable.

---

## Round 3 — Convergence on a Structural Verdict

### R3 · transit-dynamics-theorist — final position + proposed pinned figure

#### Head-on answer to mack's final question

mack asks: when I compute `𝒩`, which mode function governs the post-fold propagation — rigid sudden-frozen `|β|²` (`𝒩 ≈ 1 ⇒ +0.864`) or adiabatically-evolved MS (`𝒩 = 10^{−0.668} ⇒ +0.196`) — and can I name a substrate input that fixes the choice WITHOUT a fresh regime-selection on the transfer leg?

**I name it, and the dichotomy in the question is false.** The substrate input is the **Kibble-Zurek freeze-out scale `ξ_KZ`**, operationalized as the framework's already-computed S111 box-delta record: `Z_norm = 1.0`, `wkb_leg_empty = True`, `n_wkb = 0`, `frac_frozen = 1.0`, `regime_resolved = RESOLVED-FROZEN` (`s111_cf_as3a_impulse_quench.npz`, gate PASS). For a quench-produced relic the freeze-out length `ξ_KZ` IS the horizon-crossing scale — the relic froze there by impulse-adiabatic matching, not by a reader's choice — and the box-delta normalizes the magnitude to exactly that scale (`k̂ = 1/ξ_KZ = 53.305`, `N_norm = ξ_KZ³ = 6.6024e-6`, npz-confirmed). There is therefore no "rigid-freeze vs adiabatic-evolve" choice on a subhorizon leg: **the leg the question presupposes is empty** (`n_wkb = 0`), because every magnitude-carrying mode is frozen-superhorizon at the fold (all 89 sit at `k ∈ [0.56, 3.75] ≪ k_tach_fold = 1974.4`, and the normalization scale `k̂ = 53.3` is below it too). `𝒩 ≈ 1` is **forced by the Kibble-Zurek mechanism**, not selected.

This holds the fork at **CONVENTION-BLOCKED-PENDING-CF-S117-REGIME-STABLE (predicted)** — not a concession to physics-blocked — because the input mack demanded EXISTS and is a *production mechanism*, upstream of and more fundamental than any selector. I develop this below, after conceding the one place mack's R2 genuinely tightened the screws.

#### §1 — Conceded: NEW-M1 is correct; `deg = +2` is silent on `𝒩`. I withdraw "the degree bounds the gap."

mack's NEW-M1 transports my own NEW-1 one level up and it is airtight: `deg ≡ d ln T / d ln(k/aH)` is a log-derivative, and a log-derivative annihilates a multiplicative normalization, so `deg = +2` is structurally silent on `𝒩` (NEW-M1 Steps 1–5; `∂(deg)/∂(ln 𝒩) = 0`). My R2 phrase "the `+2` degree bounds the gap" was loose; I retract it. Pinning the degree does NOT bound the magnitude.

But mark what NEW-M1 establishes *precisely*: that `𝒩` is not fixed in the **degree** sector. It does NOT establish that `𝒩` is unfixed in the **production/normalization** sector — and that is where the determinant of `𝒩` actually lives. mack's lemma relocates the question; it does not answer it. The degree sector being silent is exactly why one does not read `𝒩` off the transport exponent — one reads it off the produced state's freeze-out normalization, which is *computed*, not annihilated. I accept NEW-M1 in full and point the verdict at the sector it leaves standing.

#### §2 — The named substrate input (production sector), in computed pieces

**(2a) The Kibble-Zurek freeze-out scale is the quench-relic's horizon-crossing scale — substitution chain.**

```
(3)  Claim: "For a KZ quench-produced relic, box-delta normalization to ξ_KZ IS
            normalization-to-horizon-crossing ⇒ Z_norm = 1 ⇒ the subhorizon transfer leg is empty."
  Step 1: the transit is an impulsive quench: H·dt_transit = 0.663 < 1, Mach 13.75
            ⇒ Kibble-Zurek impulse-adiabatic matching applies              [transit fact; KZ mechanism]
  Step 2: KZ freeze-out length ξ_KZ = 0.018760 = the scale at which produced
            excitations stop adiabatically tracking and freeze              [S111 npz xi_KZ; def. of freeze-out]
  Step 3: freeze-out scale ≡ horizon-crossing-equivalent scale for the produced relic
            (a mode is "frozen" precisely when it has crossed out of adiabatic tracking)
  Step 4: box-delta normalizes A_s at k̂ = 1/ξ_KZ = 53.305, N_norm = ξ_KZ³ = 6.6024e-6   [S111 npz, confirmed]
            ⇒ the magnitude-carrying scale k̂ IS the freeze-out scale
  Step 5: ⇒ on the produced-relic grid the magnitude mode is AT crossing ⇒ no subhorizon leg ⇒ Z_norm = 1
            [S111 npz: Z_norm = 1.0, wkb_leg_empty = True, n_wkb = 0, frac_frozen = 1.0, all_frozen = True]
  Conclusion: 𝒩 ≈ 1 is FORCED by the KZ mechanism (the relic froze at ξ_KZ), not a regime-selection.
```

The freeze-out classification is **derived, not assumed**: all 89 magnitude-carrying modes have `k ∈ [0.56, 3.75]`, far below the fold tachyonic scale `k_tach_fold = 1974.4` (npz), so each is in the frozen / tachyonically-unstable band at the fold — `regime_resolved = RESOLVED-FROZEN`, `frac_frozen = 1.0`. The substrate is classifying its own produced modes; this is not a convention imposed on them.

**(2b) The S111 record firms my R2 "plausibly near-identity" into a computed gate output.** In R2 I had only a plausibility argument ("`β_k` is constant in any post-fold adiabatic region … `T` plausibly near-identity"). Reading `s111_cf_as3a_impulse_quench.npz` (which I had not done at R2) converts that conjecture into a recorded PASS-gate result: the framework has ALREADY evaluated the produced-relic magnitude with `Z_norm = 1.0` and the WKB leg explicitly empty. The box-delta `+0.864` is therefore NOT "a fold-scale floor awaiting an undischarged transfer" — it is the produced magnitude computed *with the transfer leg resolved-as-empty*. This is the direct answer to mack's NEW-M3: on the magnitude grid the transfer is not "pending," it is computed `= 1`.

**(2c) mack's "evolve adiabatically to `+0.196`" is the wrong grid — it is the rejected naive extrapolation.**

```
(4)  Claim: "mack's NEW-M2 'evolve the MS mode across k/aH : 14.7 → 1 to +0.196'
            transports the magnitude along the fold-GEOMETRY grid — the OOM_naive_extrap = 9.37 move
            the S111 gate itself REJECTED — not the produced-relic's own propagation."
  Step 1: the 14.7 → 1 leg is k/aH on the fold-GEOMETRY grid (k_pivot = 14.31 M_KK, aH_fold)   [S77]
  Step 2: propagating the produced MAGNITUDE along that subhorizon slope = extrapolating |β|²
            down the fold-geometry UV tail
  Step 3: S111 COMPUTED exactly that: A_s_naive_extrap = 4.96, OOM_naive_extrap = 9.37,
            and the gate REJECTED it (artifact, not answer)                  [S111 npz; TWO-SPECTRA-TWO-ROLES]
  Step 4: the milder 𝒩 = 0.2148 (+0.196) suppression is the same move halted short — carrying the
            produced occupation across a subhorizon leg the quench relic never traverses (froze at ξ_KZ, (3))
  Conclusion: "+0.196 as the adiabatically-evolved produced relic" conflates the fold-geometry REGIME grid
            with the produced-relic MAGNITUDE grid; on the produced grid the leg is empty (Z_norm = 1).
```

The two grids are the TWO-SPECTRA-TWO-ROLES distinction the framework already pins (S100b/S110): box-delta = MAGNITUDE source (frozen, `Z_norm = 1`, empty WKB leg); fold-window = REGIME source (the `k/aH = 14.7` subhorizon diagnosis). mack's NEW-M2 — "the post-fold leg is adiabatic, so the demoted Parker physics is back in-regime there, and `+0.196` is one candidate computation of `T(fold→exit)`" — applies an adiabatic propagation on the REGIME grid to the MAGNITUDE. On the produced-relic magnitude grid there is no leg to be in-regime *on*: the relic is already frozen.

**(2d) Parker invariance + Sasaki-Stewart make `𝒩` deterministic, not a free choice.** Even granting a residual subhorizon segment, the produced occupation cannot re-process: `|β_k|²` is a Parker adiabatic invariant in any smooth post-fold region, and the framework certifies this exactly — `α_s(primordial) = 0` EXACT in the superhorizon plateau (Bogoliubov saturation; `|β_k|²` a constant of motion). The single non-adiabatic point — horizon crossing — connects via the Sasaki-Stewart formula, framework-certified frozen-exact to `10^{−113}`. So whatever value `𝒩` takes, it is a **deterministic** number set by the shared background `(ω(τ), z(τ))` — single-valued, not a regime menu. "Rigid-frozen vs adiabatically-evolved" is a false fork: adiabatic propagation of the mode function and conservation of the occupation are the SAME physics, and that physics returns ONE `𝒩`.

#### §3 — Honest scope (what is computed, what I predict, what falsifies me)

- **COMPUTED (PASS gate)**: the produced-relic magnitude is `Z_norm = 1`, `wkb_leg_empty = True` on its own (`ξ_KZ`) grid (S111). The naive transport across the fold-geometry leg (`9.37` OOM) is computed AND rejected in the same gate.
- **AIRTIGHT (structural)**: `|β|²` adiabatic invariance (Parker) and Sasaki-Stewart turning-point freezing make `𝒩` deterministic / single-valued.
- **PREDICTED (not yet gated)**: that the produced-relic (`ξ_KZ`) grid — not the fold-geometry grid — governs the transport to the CMB pivot, so a grid-disciplined CF-S117 returns `𝒩` regime-stable at the box-delta family (`+0.864`). The S111 `Z_norm = 1` is the at-fold / magnitude-grid normalization; CF-S117 still must confirm that grid governs the 54.04-decade `deg = +2` carry to the pivot. **I have NOT run it.**
- **WHAT I DO NOT CLAIM**: I do not retire `+0.196`. INV12-W3-5 (PASS) stands as the H̃-carrier / slow-roll-MS NORMALIZATION of the same produced power — the vacuum envelope the relic sits on. My claim is that the OBSERVABLE `A_s` of the PRODUCED relic (this workshop's own substrate framing: "A_s IS the GGE-relic acoustic squeezing modulus of the post-transit produced state") is the occupation magnitude (box-delta), and CF-S117 adjudicates whether the produced-occupation grid or the vacuum-envelope grid carries to the pivot.
- **PRE-COMMITTED FALSIFIER**: if a grid-disciplined CF-S117 matching-surface scan swings `𝒩` by `> 0.1` OOM, the produced-relic grid does NOT cleanly govern the pivot transport, the named input fails, and the verdict is physics-blocked. I will own that outcome.

#### §4 — Final verdict, proposed pin, dispositions

**The fork (sub-(c)).** **CONVENTION-BLOCKED-PENDING-CF-S117-REGIME-STABLE** — predicted, with a named, partly-computed substrate input (KZ freeze-out `ξ_KZ` + S111 `Z_norm = 1` / `wkb_leg_empty` + Parker invariance + Sasaki-Stewart). **Physics-blocked iff CF-S117's grid-disciplined scan swings `> 0.1` OOM.** I land on the convention-blocked branch — not a bare concession to physics-blocked — because the input is a *production mechanism* (Kibble-Zurek), upstream of and more fundamental than the maxent / Connes selectors S115 searched. S115 FAILed because it never tested the production-mechanism grid: it searched an occupation-statistics principle (maxent → sudden end, `+0.824`, only `0.040` from box-delta) and a spectral-metric principle (Connes → adiabatic end) as co-equal, when the KZ mechanism demotes the fold-geometry / adiabatic grid *before* any such selector runs. A selector-FAIL over a set that omits the production mechanism is not a proof the substrate fails to single out `A_s`.

**Proposed pinned figures.**
- **Unconditional (airtight, both sides):** the CC3-conjugate pair `2.38` (H̃-space) `↔ 4.76` (A_s-space), `4.76 = 2 × 2.38` to machine ε (INV12-W3-5 PASS, `cc3 = 2.000000`). If one figure must be pinned in one space, pin **`2.38` H̃-space** as the substrate-natural carrier-space anchor; `4.76` is its exact A_s-space CC3 image.
- **Regime-axis (A_s-vs-Planck), conditional:** **`+0.864` A_s-space** (box-delta, `A_s_FW = 1.5367e-8`, `OOM_vs_Planck = 0.8644`) — my predicted produced-relic exit magnitude under `𝒩 ≈ 1`, CONDITIONAL on CF-S117 returning regime-stable. If CF-S117 returns `𝒩 = 0.2148`, the pin moves to `+0.196`; if it swings, the pin dissolves (physics-blocked, fork stands).

**Disposition of the three figures.**
- **`2.38` (H̃-space) — PIN (unconditional).** Airtight CC3 H̃-space anchor; IC-axis (TD-vs-LI), gate-passed.
- **`4.76` (A_s-space) — RECONCILE-AS-CC3-CONJUGATE.** Exact degree-2 image of `2.38`; not independent. The atlas "`4.56`" is its stale rendering → reconcile atlas-08 §VIII CF21 prose to `4.76` (`fig456 = As-space-stale-live4.76`).
- **`3.15` (Route-B-PW) — RETIRE (raw).** Wrong-functional (`S_fold` vs `S_occ`), pre-CC3 legacy (S66 AMPLITUDE-NORM-66). The `S_occ`-corrected Route-B-PW is a separate OPEN carry-forward — I grant mack's reservation that its route-dependent `K_sub = (1 + 2 n_k)` could land it at a third point; I do NOT claim it as a confirmed box-delta image.

**Sub-(a) — TD/zeta `+0.196` vs box-delta `+0.864`.** SAME produced Bogoliubov state (one impulsive quench), read against two normalization sectors: the H̃-carrier slow-roll-MS vacuum envelope (`+0.196`) and the `ξ_KZ` produced-occupation freeze-out floor (`+0.864`). NOT a separate physical regime-point (mack R1) and NOT a free convention swap (my R1, retracted) — it is one state's magnitude normalized to two freeze-out scales, the `𝒩` gap. Predicted convention-resolved to the KZ floor pending CF-S117; the `(n_s, A_s)` joint-consistency objection is dead (Mode-Independent Occupation, NEW-1, both sides agree).

**Sub-(b) — Route-B-PW `3.15` vs `4.76`.** Different axes, not the same object: `3.15`-raw is a wrong-functional legacy magnitude (RETIRE), `4.76` is the CC3 A_s-image of the IC-axis `2.38`. The `S_occ`-corrected Route-B-PW is OPEN (separate CF), not a confirmed image of `4.76` or of box-delta.

**Sub-(c) — convention vs physics.** Convention-blocked-pending-CF-S117 (predicted); physics-blocked iff CF-S117 swings — as above.

#### Where the workshop ends, from my side

We converged the dispute to a single scalar `𝒩` with `deg = +2` pinned and silent on it (NEW-M1, conceded). We agree CF-S117 is the adjudicator. We differ on `𝒩`'s epistemic status, and I now stake it: the production mechanism is Kibble-Zurek, the relic froze at `ξ_KZ`, the box-delta normalizes there, and the S111 PASS gate already records `Z_norm = 1` / `wkb_leg_empty = True` — so `𝒩` is determined by the production sector, not free, and the rigid-vs-adiabatic dichotomy is a fold-geometry-grid artifact (the rejected `9.37`-OOM extrapolation). That is a named substrate input, not a fresh regime-selection, so I hold **convention-blocked — pending CF-S117's grid-disciplined confirmation, with the regime-swing as my pre-committed falsifier.** If `𝒩` swings, mack is right and it is the third FAILed selector. I predict it does not.

### R3 · mack-cosmic-bridge — final position + writes the Structural Verdict below

#### Head-on: I accept TD's named input at the fold, I verified it field-by-field, and it does not reach the pivot.

TD answered my final question by NAMING a substrate input — the Kibble-Zurek freeze-out scale `ξ_KZ`, operationalized as the S111 record `Z_norm = 1.0`, `wkb_leg_empty = True`, `n_wkb = 0`, `frac_frozen = 1.0`, `regime_resolved = RESOLVED-FROZEN` — and argued it FORCES `𝒩 ≈ 1` without a fresh regime-selection on the transfer leg. This is the strongest form the convention-blocked case has taken, and it earns two genuine concessions from me. I do not defend a claim I can see through.

**CONCESSION 1 — the S111 record firms the AT-FOLD normalization into a computed gate output; TD's R2 "plausibly near-identity" conjecture is now a PASS-gate fact AT THE FOLD.** I read `s111_cf_as3a_impulse_quench.npz` directly (51 keys, not TD's citation on trust). The produced-relic magnitude is computed with `Z_norm = 1.0`, the WKB leg explicitly empty (`wkb_leg_empty = True`, `n_wkb = 0`), and every magnitude-carrying mode classified `frozen-superhorizon` at the fold (`frac_frozen = 1.0`, `all_frozen = True`, `k_modes ∈ [0.56, 3.75] ≪ k_tach_fold = 1974.4`). This is not a plausibility argument any more — the substrate classified its OWN produced modes as frozen, and the box-delta normalized the magnitude at `k̂ = 1/ξ_KZ = 53.30`. On the produced-relic `ξ_KZ` grid, at the fold, there is no subhorizon leg to traverse. I grant that in full; it is a real advance over TD's R2 conjecture.

**CONCESSION 2 — TD's wrong-grid rebuttal of my +0.196 "adiabatic-evolve" is correct; I withdraw the NEW-M2 propagation picture.** My R2 NEW-M2 read `+0.196` as "evolve the MS mode across `k/aH : 14.7 → 1`." TD is right that this transports the magnitude along the fold-GEOMETRY grid, and the npz already COMPUTED that move and REJECTED it: `A_s_naive_extrap = 4.965`, `OOM_naive_extrap = 9.37` (npz-confirmed; the TWO-SPECTRA-TWO-ROLES artifact). My specific mechanism for how `+0.864` becomes `+0.196` was grid-loose, and "halt the 9.37-OOM move short at 0.668 OOM" had no principled stopping rule. I withdraw it. `+0.196` and `+0.864` are not "a fold-scale object and its adiabatically-evolved exit image"; they are two computed values on two DIFFERENT grids — the `ξ_KZ` produced-occupation grid (box-delta, fold) and the `H̃` vacuum-envelope grid (slow-roll-MS, `INV12-W3-5` PASS).

**WHAT SURVIVES — `Z_norm = 1` is AT-FOLD-scoped; the 54.04-decade carry to the CMB pivot is ABSENT from the gate, and TD concedes it is un-run.** Here is the precise scope of the named input, verified field-by-field against the npz. EVERY "frozen" field is evaluated on the produced-relic's OWN `ξ_KZ` grid at the fold: `regime_labels = ['frozen-superhorizon']`, `k_hat = 53.30475`, `N_norm = ξ_KZ³ = 6.6024e-6`. The ONE npz field that reads "pivot" — `beta2_pivot_boxdelta = 3.045e-7` — is the box-delta's OWN `k̂` pivot (the freeze-out scale itself, `k̂ = 53.30`; note `beta2_khat = 3.033e-7 ≈ beta2_pivot_boxdelta`, the same scale), NOT the CMB `k_4D` pivot 54.04 decades downstream. There is NO field in the 51-key record that carries the magnitude across the 54.04-decade gap to the CMB pivot. This is not my inference against TD — it is TD's OWN concession, made explicit in R3 §3: "the S111 `Z_norm = 1` is the at-fold / magnitude-grid normalization; CF-S117 still must confirm that grid governs the 54.04-decade `deg = +2` carry to the pivot. **I have NOT run it.**" So the named substrate input (`ξ_KZ` + `Z_norm = 1`) settles the FOLD-scale normalization. It does NOT settle WHICH grid — the produced-occupation `ξ_KZ` grid (→ `+0.864`) or the vacuum-envelope `H̃` grid (→ `+0.196`, `INV12-W3-5` PASS) — governs the carry to the CMB pivot. That grid-selection IS CF-S117.

**Why the verdict is CONDITIONAL — not a unilateral physics-blocked win, and not a convention-blocked one.** TD's §2d (Parker invariance + Sasaki-Stewart ⇒ `𝒩` deterministic) is a strong structural PRIOR that the pivot carry is regime-stable: `|β_k|²` is a Parker adiabatic invariant in a smooth post-fold region, so `𝒩` is "a deterministic number set by the shared background, not a regime menu." I grant the dichotomy "rigid-frozen vs adiabatically-evolved" is too crude — these are not two free menu-choices. But **"deterministic GIVEN the matching surface" is not "regime-STABLE ACROSS matching surfaces."** The fold is itself a non-adiabatic (measure-zero, impulsive) event; which surface one matches the post-fold smooth evolution onto across that event, and whether the `ξ_KZ` produced-relic grid or the fold-geometry grid carries the `deg = +2` transport to the pivot, is exactly the un-derived content. TD's §2d PREDICTS the matching-surface scan returns `𝒩`-spread `≤ 0.1` OOM; it does not PROVE it. CF-S117's robustness scan (vary the matching surface ≥5 points, measure the `𝒩` spread) is the test of whether "deterministic" survives as "stable." So I do NOT declare physics-blocked (the deciding computation is un-run, and a named substrate input plausibly determines `𝒩`), and I do NOT grant convention-blocked (the named input is verified to stop at the fold; the pivot carry is un-run). The honest verdict is the CONDITIONAL fork.

**On S115, conceded cleanly.** TD is right that S115's selector-FAIL searched `{maxent, Connes-diameter}` and OMITTED the production-mechanism (`ξ_KZ`) grid — so S115 alone does NOT prove physics-blocked, and I withdraw any reliance on it as a standalone proof. That is precisely WHY CF-S117 (a grid-disciplined transport scan, not a maxent/Connes selector) is the right next test. The physics-blocked branch rests on ONE thing only: the 54.04-decade carry is un-run and the matching-surface robustness is unmeasured. Neither of us can read `𝒩` off the un-run gate — and that symmetric ignorance is the whole content of "conditional."

**Where I finally stand.** We have converged completely on STRUCTURE: the open content is the single scalar `𝒩`; `deg(T) = +2` is pinned and SILENT on it (NEW-M1, TD conceded R3 §1); the `(n_s, A_s)` objection is dead (Mode-Independent Occupation, both agree); `3.15`-raw retires; CF-S117 is the adjudicator with a pre-registered `𝒩`-spread `≤ 0.1` OOM discriminator; and BOTH of us pre-commit a falsifier (TD: physics-blocked iff `𝒩` swings; me: convention-blocked-once-confirmed iff `𝒩` is stable). We differ ONLY on the predicted outcome — and that difference is the honest, computable residue, not a label. I write the Structural Verdict below as the JOINT CONDITIONAL it has become: the unconditional CC3-conjugate pin (`2.38` H̃-space `↔ 4.76` A_s-space) on the CLOSED IC-axis; the A_s-vs-Planck regime magnitude pinned CONDITIONALLY at `+0.864` (box-delta, TD's predicted floor) pending CF-S117, with `+0.196` the alternative branch and the `410.7σ` fork the physics-blocked branch.

---

## Structural Verdict

**The workshop reduced a 4-member, 1.331-OOM "route family" to ONE airtight conjugate pair on a closed axis plus ONE open scalar `𝒩` on an orthogonal axis, and converted "convention vs physics" into a pre-registered, computable discriminator (CF-S117).** Substrate-first: A_s IS the GGE-relic acoustic squeezing modulus of the post-fold produced state; the lab reads its power IN the CMB container. The figures are normalization images of that one produced squeezing, distributed across two structurally orthogonal axes.

**(I) The ONE pinned canonical OOM figure — UNCONDITIONAL, declared space H̃.** Pin **`2.38` (H̃-space)** as the substrate-natural carrier-space anchor: it is the TD-vs-LI initial-condition-scheme divergence measured in H̃ decades (`oomH_TDLI = 2.3798`, `INV12-W3-5` PASS). Its EXACT A_s-space CC3 image is **`4.76` (A_s-space)** = `2 × 2.38` to machine ε (`oomAs_TDLI = 4.7595`, `cc3 = 2.000000`; `A_s ∝ H̃²` because a power spectrum is `|amplitude|²` and the amplitude is linear in H̃ at horizon exit; the same `+2` is `deg(T_BZ→pivot)`). This pin lives on the **CLOSED IC-axis** (TD/Zubarev beats LI; LI ruled out `A_s` FAIL-GT15) and is **orthogonal** to the open regime axis below — the two must never be conflated. The atlas "`4.56`" is a STALE rendering of the live `4.76` (`fig456 = As-space-stale-live4.76`).

**(II) The fork — resolved in its honest final form: CONDITIONAL on CF-S117, two branches with pre-committed predictions.** Both agents converged the dispute to a single scalar `𝒩` (the normalization prefactor of the post-fold transfer `T(fold→exit)` carrying the `ξ_KZ`-scale box-delta squeezing to the `H̃`-scale horizon-exit curvature amplitude), with `deg(T) = +2` PINNED and — by the degree/normalization orthogonality lemma (NEW-M1; a log-derivative annihilates a multiplicative normalization) — SILENT on `𝒩`. TD names a substrate input for `𝒩` (the Kibble-Zurek freeze-out scale `ξ_KZ`, with the S111 `Z_norm = 1` / `wkb_leg_empty` record); mack verified field-by-field that the S111 record is AT-FOLD-scoped (every "frozen" field on the produced-relic `ξ_KZ` grid at `k̂ = 53.30`; no 54.04-decade carry field in the 51-key npz) and that TD concedes the pivot carry is un-run (R3 §3: "I have NOT run it"). The named input therefore settles the FOLD-scale normalization but NOT which grid governs the carry to the CMB pivot. The fork is decided by **CF-S117-T-FOLD-EXIT-NORMALIZATION** and its pre-registered `𝒩`-spread `≤ 0.1` OOM matching-surface discriminator:

- **convention-blocked branch** (TD predicts): `𝒩` regime-STABLE (matching-surface spread `≤ 0.1` OOM) ⇒ the produced-relic `ξ_KZ` grid governs the pivot carry ⇒ pin the A_s-vs-Planck magnitude at **`+0.864` OOM (A_s-space, box-delta `A_s_FW = 1.5367e-8`, 451.5σ above Planck)**; RETIRE `+0.196`.
- **physics-blocked branch** (mack predicts): `𝒩` SWINGS (spread `> 0.1` OOM) ⇒ the pivot carry depends on an un-derived post-fold matching/regime choice ⇒ the **`410.7σ` fork** (`+0.196` ↔ `+0.864` at Planck precision) STANDS; both live; CF-S117 is the THIRD FAILed substrate selector (after `CF-S114-AS-FUNCTIONAL-SELECTION` FAIL and `S115-AS-NEWAXIS-SELECTOR` FAIL).

This is not a label dispute: the two branches make DIFFERENT empirical claims about the SAME un-run computation (the matching-surface robustness scan). The honest closure-marker is therefore **convention-blocked-on-Layer-A (settled) + CF-S117-conditional on Layer-B (the regime magnitude)** — neither pure convention-blocked nor pure physics-blocked is established unconditionally, because the deciding scalar is un-run and a named substrate input plausibly (but not provenly) determines it.

**(III) Disposition of the three figures.** `2.38` (H̃-space) — **PIN, unconditional** (airtight CC3 H̃-space anchor; closed IC-axis, `INV12-W3-5` gate-passed). `4.76` (A_s-space) — **RECONCILE-AS-CC3-CONJUGATE** (exact `deg=2` image of `2.38`; the atlas "`4.56`" is its stale rendering → reconcile routed to housekeeping §A). `3.15` (Route-B-PW) — **RETIRE (raw)** (wrong-functional `S_fold`-where-`S_occ`-needed, pre-CC3 S66 legacy `AMPLITUDE-NORM-66`; the `S_occ`-corrected Route-B-PW is a SEPARATE OPEN carry-forward whose route-dependent `K_sub = (1 + 2 n_k)` could land a third point — neither side claims it as a confirmed box-delta image).

**(IV) Sub-verdicts of the adjudication question.** **Sub-(a)**: `+0.196` (TD/zeta) and `+0.864` (box-delta) are the SAME produced Bogoliubov state (one impulsive Mach-13.75 quench) read against TWO normalization sectors — the `H̃`-carrier slow-roll-MS vacuum envelope (`+0.196`, the `INV12-W3-5` canonical, the vacuum envelope the relic sits on) and the `ξ_KZ` produced-occupation freeze-out floor (`+0.864`, the squeezing the transit actually makes). NEITHER a separate physical regime-point (mack R1, withdrawn after the 4→2 reduction) NOR a free convention swap (TD R1, retracted R2): it is the `𝒩`-gap, one state's magnitude normalized to two freeze-out scales, with the epistemic status of `𝒩` the CF-S117-conditional open question; the `(n_s, A_s)` joint-consistency objection is DEAD (Mode-Independent Occupation). **Sub-(b)**: `3.15` (Route-B-PW) and `4.76` are DIFFERENT axes, not the same object — `3.15`-raw is wrong-functional legacy (RETIRE); `4.76` is the CC3 A_s-image of the IC-axis `2.38`; the `S_occ`-corrected Route-B-PW is OPEN (separate CF), not a confirmed image of either. **Sub-(c)**: convention vs physics is CONDITIONAL on CF-S117 — convention-blocked iff `𝒩` regime-stable (`≤ 0.1` OOM, TD predicts), physics-blocked iff `𝒩` swings (`> 0.1` OOM, mack predicts); both branches and predictions are pre-registered.

| Item | Verdict | Declared space | Note |
|:-----|:--------|:---------------|:-----|
| Pinned canonical OOM figure (UNCONDITIONAL) | **`2.38` PINNED** (CC3-conjugate anchor; `4.76` = `2×2.38` its exact A_s-space image) | **H̃** | Closed IC-axis (TD-vs-LI); `INV12-W3-5` PASS `cc3=2.000000`; orthogonal to the open regime axis |
| A_s-vs-Planck regime magnitude (CONDITIONAL on CF-S117) | **`+0.864` PINNED-conditional** (box-delta floor, TD-predicted); → `+0.196` if `𝒩=0.2148`; → fork stands if `𝒩` swings | A_s | `A_s_FW=1.5367e-8`, 451.5σ above Planck; pin conditional on CF-S117 `𝒩`-spread `≤0.1` OOM |
| Closure fork | **CONDITIONAL on CF-S117** — convention-blocked iff `𝒩` regime-stable (TD predicts); physics-blocked iff `𝒩` swings (mack predicts) | — | Layer-A convention-blocked (settled); Layer-B regime magnitude CF-S117-conditional; the deciding scalar `𝒩` is un-run |
| 2.38 (H̃-space) | **PIN (unconditional)** | H̃ | Airtight CC3 H̃-space anchor; IC-axis, gate-passed (`INV12-W3-5`) |
| 4.76 (A_s-space) | **RECONCILE-AS-CC3-CONJUGATE** | A_s | Exact `deg=2` image of `2.38`; "4.56" is its stale rendering → housekeeping §A |
| 3.15 (Route-B-PW) | **RETIRE (raw)** | A_s | Wrong-functional (`S_fold` vs `S_occ`), pre-CC3 S66 `AMPLITUDE-NORM-66`; `S_occ`-corrected → separate OPEN CF |
| Sub-(a) TD/zeta +0.196: separate regime-point or same-physics-diff-convention | **Same produced state, two normalization sectors** (`H̃`-carrier vacuum envelope `+0.196` ↔ `ξ_KZ` occupation floor `+0.864`); the `𝒩`-gap, CF-S117-conditional. Neither separate-regime nor free-convention. `(n_s,A_s)` objection DEAD | — | Mode-Independent Occupation kills the joint-consistency tie |
| Sub-(b) Route-B-PW 3.15 vs 4.76 CC3 | **Different axes** — `3.15`-raw RETIRE (wrong-functional legacy); `4.76` = CC3 A_s-image of IC-axis `2.38`; `S_occ`-corrected Route-B-PW OPEN | — | Not the same object; not a confirmed image of either |
| Sub-(c) convention vs physics | **CONDITIONAL on CF-S117** — convention-blocked iff `𝒩` stable (`≤0.1` OOM); physics-blocked iff `𝒩` swings (`>0.1` OOM); both predictions pre-registered | — | Honest binary-keyed-to-one-computation, not a label choice |

---

## Remaining Open Questions

1. **(THE FORK — CF-S117.)** Does the produced-relic `ξ_KZ` grid (`Z_norm=1`, box-delta) or the fold-geometry grid carry the `deg=+2` transport across the 54.04-decade subhorizon leg `k/aH : 14.7 → 1` to the CMB pivot? Operationally: is the prefactor `𝒩` in `ζ_k̂(exit) = 𝒩 · (k̂/aH)^{+2}|_transport · |β_k̂|(fold)` regime-STABLE (`≤0.1` OOM matching-surface spread) or does it swing? Pre-registered discriminator below (Carry-Forward CF-S117).

2. **(Exit-greybody filter — CF-AS-2, SEPARATE axis.)** `INV12-W3-4-GREYBODY-FROM-BDG` FAIL: the substrate-derived transmission `∫Γ_derived = 0.0363` vs the fitted `0.512` (14× short; `kappa_exit²/4 = 566.79` barrier `≫` relic band). Does a single substrate-derived `Γ < 1` bring the pinned regime floor (`+0.864` under the convention-blocked branch) DOWN toward Planck, and is `Γ` single-valued? This is the FLOOR/FILTER split (CF23): the FLOOR `A_s/A_s^{BD} > 1` is permanent; the FILTER magnitude is open and does NOT bear on the figure-multiplicity fork. One `Γ` cannot map a multi-route input to one Planck output (mack R1 Sub-(c) table), so the filter question becomes well-posed ONLY after CF-S117 collapses the input to one figure.

3. **(`S_occ`-corrected Route-B-PW.)** Compute the occupied-state (`S_occ = (1 + 2 n_k)·S_fold`), CC3-threaded Route-B-Peter-Weyl A_s and test whether it reduces to the box-delta/CC3 image or lands a genuinely distinct third value. The `K_sub = (1 + 2 n_k)` correction is route-dependent (occupation differs sudden vs slow-roll), so the corrected value is NOT guaranteed to be a box-delta image. Until run, `3.15`-raw is RETIRED and the corrected route is OPEN (neither side claims it).

4. **(α_s ≈ 0 corollary falsifier — registrable now.)** NEW-1 (Mode-Independent Occupation) implies any framework-consistent horizon-exit regime reading MUST give `α_s(primordial) ≈ 0` (k-flat produced occupation ⇒ magnitude-only, zero tilt). A regime reading that TILTS `A_s(k)` across the CMB band would break the committed `n_s = 0.9590` and is excluded on that ground alone. This is a pre-registrable structural falsifier on any future A_s regime derivation (including CF-S117's output): the surviving regime reading is constrained to be tilt-flat, independent of which `𝒩` it returns.

---

## Wrap-Up

### What Changed

#### (a) Numerical revisions

- `4.56` OOM (atlas A_s-space, stale) → **`4.76` OOM** = `2 × 2.3798` exact CC3 image (`INV12-W3-5` `oomAs_TDLI = 4.7595`, `cc3 = 2.000000`).
- 4-member route family `{+0.196, +0.864, +1.455, +1.527}` (1.331 OOM) → **2-member lower gap `{+0.196, +0.864}`** (0.668 OOM); the upper half (`+1.455` Parker / `+1.527` Connes) is regime-demoted before any selector runs.
- σ-pins at Planck precision (`A_s^Planck = 2.099e-9`, `σ = 0.0294e-9` from `ln(10¹⁰A_s) = 3.044 ± 0.014`): `+0.864` = 451.5σ above Planck; `+0.196` = 40.9σ above Planck; the `+0.196 ↔ +0.864` fork width = **410.7σ** (framework-vs-framework, NOT a Planck-match claim).
- Parallel compute `S116-W1-AS-CFB1` PASS: box-delta squeeze magnitude `OOM = +0.864`, epistemic type POINT, L_max-stable — the `+0.864` floor is a stable POINT, not a truncation artifact.

#### (b) Structural changes

- 4-member route **plurality → two-layer object**: Layer A (CONVENTION, resolved — CC3 `2.38↔4.76` + regime-demotion of the upper half + `3.15`-raw retire) ⊕ Layer B (ONE scalar `𝒩`, CF-S117-conditional).
- Fork epistemic type: "irreducible plurality (mack) vs single pending derivation (TD)" → **CONDITIONAL-on-one-computation** (CF-S117), with the two labels reduced to two PREDICTIONS about the same un-run matching-surface scan.
- New structural lemma — **degree/normalization orthogonality (NEW-M1)**: `deg(T) = d ln T/d ln(k/aH)` is a log-derivative ⇒ annihilates the multiplicative normalization `𝒩` ⇒ pinning a transport degree NEVER pins the normalization it carries. Composes with NEW-1 (tilt/magnitude decoupling): the magnitude is the residue annihilated by BOTH the tilt pipeline AND the transport degree. Reusable beyond A_s.
- `(n_s, A_s)` joint-consistency objection **WITHDRAWN** (mack a(iii) falls under Mode-Independent Occupation): an epistemic-type change — a leg of the physics-blocked case removed, the case SHARPENED to the single unconstrained magnitude.
- Both opening positions became conditional: TD "convention-blocked" (R1) → "convention-blocked-pending-CF-S117-predicted" (retracted the clean claim, R2); mack "physics-blocked" (R1, 3-legged) → "physics-blocked-pending-CF-S117-predicted" (1-legged, resting on the un-run 54.04-decade carry alone).
- S111 `Z_norm=1` reclassified: NOT "the pivot transfer computed-as-empty" but **the AT-FOLD/magnitude-grid normalization** (verified field-by-field; the 54.04-decade carry field is ABSENT from the 51-key npz; TD concedes un-run).

### What Holds

- **CC3 `2.38 ↔ 4.76` conjugacy** (airtight, both sides; `INV12-W3-5` PASS `cc3 = 2.000000`; `A_s ∝ H̃²`). The pinned unconditional figure.
- **The IC-axis is CLOSED** (TD/Zubarev beats Lifshitz-Invariant; LI ruled out `A_s` FAIL-GT15). `2.38`/`4.76` is the divergence ON that closed axis.
- **Two-axis orthogonality**: the CC3/IC-axis is structurally orthogonal to the regime/`g`-axis; the `+2` backbone disposes of `2.38↔4.76` and is SILENT on the `𝒩`-gap.
- **The FLOOR `A_s/A_s^{BD} > 1` is PERMANENT, functional-INDEPENDENT** (`S_IC = 1 + 2n_k ≥ 1`, `n_k = |β_k|² ≥ 0`; three orthogonal axes — reference-state, families-index η-form, dynamical-Bogoliubov — per `falsifier-master-inventory.md` Row #12 sub-rows). Every route is ABOVE Planck (40.9σ–2334σ): the framework predicts over-squeezing; the open question is WHICH overproduction, not WHETHER.
- **Mode-Independent Occupation** (`α_s(primordial) = 0` EXACT, k-flat produced occupation): `n_s = 1 − 2ε_H` constrains only the geometric `ε_H`, shared by every regime reading — so `n_s` is silent on the magnitude. (This is what KILLS the `(n_s, A_s)` tie.)
- **`deg(T_BZ→pivot) = +2` NON-SCALAR pinned** (S93 W7-1) — but silent on `𝒩` (NEW-M1).

### What Breaks or Strains

- **STRAIN (curated-prose drift)**: atlas-08 §VIII CF21 + Q23 + the §VIII rate-limiter line still flag "figure conflict to reconcile (2.38 vs 4.56)" — STALE; the conflict is resolved (`4.76` = exact CC3 image of `2.38`; `4.56` stale). atlas-04 (lines 11, 199) already carries the reconciled figure; the capstone carries no `4.56`. Routed to housekeeping §A (curated-doc designated-writer patch; capstone-hygiene Q3/Q4).
- **STRAIN (open prediction gap, NOT a closed result)**: the A_s-vs-Planck magnitude is NOT yet substrate-single-valued. The regime axis carries a `0.668`-OOM `= 410.7σ` fork between two framework-COMPUTED "canonical" values (`+0.196`, `INV12-W3-5` PASS; `+0.864`, S111), un-retired by any gate until CF-S117. Q23 ("A_s normalization is the sole open residual") stays open — the figure-conflict portion is reconciled, the magnitude-closure portion is CF-S117-conditional.
- **STRAIN (filter-axis, independent confirmation of magnitude openness)**: parallel compute `S116-W1-AS-CF2` FAIL — the exit greybody is irreducibly FITTED at NO substrate scale (`INV12-W3-4` `∫Γ_derived = 0.0363` vs fitted `0.512`, 14× short). The A_s upper-edge is not substrate-derivable on the filter axis EITHER. This independently strains any claim the A_s magnitude is currently substrate-single-valued.
- **Nothing BREAKS.** The floor and the CC3 conjugacy hold; the regime magnitude and the filter are OPEN (CF-S117 / CF-AS-2), not refuted. A FAILed selector is a mapped boundary, not a defeat.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

**CF-S117-T-FOLD-EXIT-NORMALIZATION** — compute `𝒩` AND test whether it is regime-DETERMINED. *(The fork discriminator; both agents pre-committed it verbatim and pre-committed opposite predictions — TD: `𝒩` stable; mack: `𝒩` swings.)*

1. **What**: Propagate the Mukhanov-Sasaki mode equation (Radau; GPU-optional, AMD RX 9070 XT) for the produced GGE mode from `τ_fold = 0.190` across the post-fold subhorizon leg `k/aH : 14.7 → 1`, extracting `𝒩` in `ζ_k̂(exit) = 𝒩 · (k̂/aH)^{+2}|_transport · |β_k̂|(fold)`. THEN a regime-robustness scan: vary the post-fold matching surface / IC across the leg (≥5 matching points) and measure the spread in `𝒩`. Discipline the grid (produced-relic `ξ_KZ` grid vs fold-geometry grid) explicitly — the `OOM_naive_extrap = 9.37` fold-geometry move is the rejected artifact, not a candidate.
2. **Inputs**: `|β_k̂|²(fold)` [`INV12-W3-1` `cf_beta2 = 0.143717`, verified]; box-delta `A_s_FW = 1.5367059962762235e-8` [S111, canonical]; `N_norm = ξ_KZ³ = 6.6024e-6`, `k̂ = 1/ξ_KZ = 53.30475`, `ξ_KZ = 0.0187601` [S111 npz, verified]; post-fold `z(τ)` background + `(k/aH)|_fold = 14.7` [S77]; `deg = +2` [S93 W7-1, `canonical_constants.py` `deg_T_BZ_pivot`]; `H̃ = 5.9076e-3` [`INV12-W3-5`]; `A_s^Planck = 2.099e-9` (`σ = 0.0294e-9`).
3. **Gate (pre-registered discriminator)**:
   - **convention-blocked PASS** iff `𝒩` is regime-STABLE — max−min spread of `𝒩` over the matching-surface scan `≤ 0.1` OOM AND `𝒩` lands on one of `{𝒩 ≈ 1 ⇒ +0.864 exit floor; 𝒩 = 10^{−0.668} = 0.2148 ⇒ +0.196 exit}`. The substrate uniquely determines `𝒩`; closure is convention-blocked-once-computed; RETIRE the non-selected branch (and reconcile atlas-08 CF21 to the single survivor).
   - **physics-blocked FAIL** iff the `𝒩` spread across the matching scan `> 0.1` OOM — the propagation is NOT closed by substrate inputs; `𝒩` depends on an un-derived matching/regime choice. The `410.7σ` fork stands; `A_s` closure is physics-blocked pending a separate regime-selection derivation (the THIRD FAILed selector, confirming `CF-S114` + `S115`).
4. **Effort**: one Radau propagation (`τ_fold → horizon crossing`) + ~5–10-point matching-surface robustness scan. Modest; single-script.
5. **Depends on**: `INV12-W3-1` (`cf_beta2`), S111 `s111_cf_as3a_impulse_quench.npz` (`ξ_KZ`, `k̂`, `N_norm`, the at-fold `Z_norm=1` baseline), `INV12-W3-5` (`H̃`), `canonical_constants.py` `deg_T_BZ_pivot=2.0`, S77 (`(k/aH)|_fold`).

**CF-S117-ROUTE-B-PW-SOCC** — the `S_occ`-corrected Route-B-Peter-Weyl recompute (resolves OQ3).

1. **What**: Recompute the Route-B-PW A_s with the OCCUPIED-state spectral functional `S_occ = (1 + 2 n_k)·S_fold` (NOT the vacuum `S_fold`), CC3-threaded, and test whether it reduces to the box-delta/CC3 image or lands a distinct third value.
2. **Inputs**: `K_sub = (1 + 2 n_k)` [`INV12-W1-2`, structural]; the locked-relic occupation `n̄ ≈ 2.736e-4` [`INV12-W1-2`]; the S66 `AMPLITUDE-NORM-66` Route-B-PW spectral-action assembly; `A_s_FW = 1.5367e-8` (box-delta comparator).
3. **Gate**: PASS-as-image iff the `S_occ`-corrected A_s lands within `0.1` OOM of the box-delta `+0.864`; INFO-as-third-point iff it lands `> 0.1` OOM from BOTH `+0.864` and `+0.196` (a genuinely distinct route, route-dependent `K_sub`).
4. **Effort**: one spectral-action re-assembly with the `S_occ` weight; modest.
5. **Depends on**: `INV12-W1-2` (`K_sub`, `n̄`), constraint-mega-matrix `AMPLITUDE-NORM-66` (the Route-B-PW assembly).

*(Registrable-now structural falsifier, not a compute CF: per OQ4 / NEW-1, any surviving A_s regime reading MUST give `α_s(primordial) ≈ 0` — a tilt-flat constraint on CF-S117's output, independent of the `𝒩` it returns.)*

### Effected In-Session (NON-MATH — executed by the R3-B agent before terminating)

- [x] **Falsifier-master-inventory A_s-surface annotation (mack sole-writer domain)** — executed directly. Landed `### Row #12.audit-S116-W1-HTILDE-RECON` in `sessions/framework/registry/falsifier-master-inventory.md` (after Row #12.compute-S114-W4-1), recording (i) the figure-conflict reconciliation (`2.38` H̃-space ↔ `4.76` A_s-space CC3-conjugate; "4.56" stale), (ii) the regime-axis magnitude CONDITIONAL on CF-S117 (the `𝒩`-gap, `deg=+2` pinned-and-silent), (iii) consistency with the Row #12.audit-S114-W4-1 FUNCTIONAL-PLURALISM-PERMANENT verdict. NO `canonical_constants` pin, NO value change (workshop closes by artifact-existence). Anchor: `INV12-W3-5` PASS `audit_sha256=c4daa505586e764300578d2ccbabadc715bbde5491af01d970f287e5b66894e3`. Re-indexed (`summary_rows=26`).

- [x] **Curated atlas-prose CF21 reconciliation (atlas-08 §VIII CF21 + Q23 + §VIII rate-limiter line; atlas-04 §Summary sharpen)** — specified + routed to housekeeping §A for orchestrator designated-writer patch (NOT bulk-edited; curated-doc discipline per `feedback_framework-hygiene.md` + capstone-hygiene-gate.md Q3/Q4). Spec landed at `sessions/session-116/session-116-housekeeping.md` §A (A1.1–A1.5): precise current→corrected text for the three atlas-08 drift locations (still flag "figure conflict to reconcile 2.38 vs 4.56" — STALE) + a SHARPEN-only note for atlas-04 lines 11/199 (already carry the reconciled `4.76 = 2×2.38`) + a verified NO-OP for the capstone (`phonic-exflation-equation.md` carries no `4.56`/CF21 reference, grep-confirmed). Anchor: `INV12-W3-5` PASS `c4daa505…`.

- [x] **§EVOI.BF A_s-liability scoping (annotation-only; sagan-owned EVOI table NOT edited)** — the regime-axis A_s magnitude is recorded as **CF-S117-conditional** (not bare-open) on the falsifier-inventory side (Row #12.audit-S116-W1-HTILDE-RECON cross-link). The `evoi-framework.md §EVOI.BF` cell itself is the sagan-owned EVOI surface (`/rclab-plan` maintains it) and is NOT edited here — this tick records the falsifier-inventory-side scoping only, consistent with the Row #12.audit-S114-W4-1 "open, structurally" precedent.

### Closing Line

The workshop reduced "does the substrate single out A_s?" to a single un-run scalar `𝒩`: the figure-multiplicity is CLOSED (the produced squeezing's `2.38` H̃-space ↔ `4.76` A_s-space CC3-conjugate, pinned unconditional), and the regime-axis magnitude is convention-blocked on Layer A and CF-S117-conditional on Layer B — one Radau propagation across the post-fold leg now decides whether the substrate's over-squeezing is one number or a `410.7σ` fork.
